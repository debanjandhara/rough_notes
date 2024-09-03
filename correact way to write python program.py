# Check the proper defination of FastAPI Code here : https://github.com/chrisK824/fastapi-sso-example

require 'colorize'
require 'sinatra/base'

# A simplistic local server to receive authorization tokens from the browser
def run_local_server(authorizer, port, user_id)

    require 'thin'
    Thin::Logging.silent = true

    Thread.new {

        Thread.current[:server] = Sinatra.new do

            enable :quiet
            disable :logging
            set :port, port
            set :server, %w[ thin ]

            get "/" do
                request = Rack::Request.new env
                state = {
                    code:  request["code"],
                    error: request["error"],
                    scope: request["scope"]
                }
                raise Signet::AuthorizationError, ("Authorization error: %s" % [ state[:error] ] ) if state[:error]
                raise Signet::AuthorizationError, "Authorization code missing from the request" if state[:code].nil?
                credentials = authorizer.get_and_store_credentials_from_code(
                    user_id: user_id,
                    code: state[:code],
                    scope: state[:scope],
                )
                [
                    200,
                    { "Content-Type" => "text/plain" },
                    "All seems to be OK. You can close this window and press ENTER in the application to proceed.",
                ]
            end

        end
        Thread.current[:server].run!
    }

end

# Returns user credentials for the given scope. Requests authorization
# if requrired.
def user_credentials_for(scope, user_id = 'default')
        client_id = Google::Auth::ClientId.new(ENV['GOOGLE_CLIENT_ID'], ENV['GOOGLE_CLIENT_SECRET'])
        token_store = Google::Auth::Stores::FileTokenStore.new(:file => ENV['GOOGLE_CREDENTIAL_STORE'])
        port = 6969
    redirect_uri = "http://localhost:#{port}/"
    authorizer = Google::Auth::UserAuthorizer.new(client_id, scope, token_store, redirect_uri)

    credentials = authorizer.get_credentials(user_id)
    if credentials.nil? then
        server_thread = run_local_server(authorizer, port, user_id)
        url = authorizer.get_authorization_url
        $stderr.puts ""
        $stderr.puts "-----------------------------------------------"
        $stderr.puts "Requesting authorization for '#{user_id.yellow}'"
        $stderr.puts "Open the following URL in your browser and authorize the application."
        $stderr.puts
        $stderr.puts url.yellow.bold
        $stderr.puts
        $stderr.puts "⚠️ If you are authorizing on a different machine, you will have to port-forward"
        $stderr.puts "so your browser can reach #{redirect_uri.yellow}"
        $stderr.puts
        $stderr.puts "⚠️ If you get a " << "This site can't be reached".red << " error in the browser,"
        $stderr.puts "just copy the failing URL below. Copy the whole thing, starting with #{redirect_uri.yellow}."
        $stderr.puts "-----------------------------------------------"
        code = $stdin.readline.chomp
        server_thread[:server].stop!
        server_thread.join
        credentials = authorizer.get_credentials(user_id)
        # If the redirect failed, the user must have provided us with a code on their own
        if credentials.nil? then
            begin
                require 'uri'
                require 'cgi'
                code = CGI.parse(URI.parse(code).query)['code'][0]
            rescue StandardException
                # Noop, if we could not get a code out of the URL, maybe it was
                # not the URL but the actual code.
            end

            credentials = authorizer.get_and_store_credentials_from_code(
                user_id: user_id,
                code: code,
                scope: scope,
            )
        end
    end
    credentials
end

credentials = user_credentials_for(['https://www.googleapis.com/auth/drive.readonly'])
