To send continuous data via an API, you can use a streaming API. In Python, you can achieve this using Flask-SSE, which is an extension for Flask that allows you to send Server-Sent Events (SSE) to clients in real-time.

Here's how you can implement it using Flask-SSE:

1. **Install Flask-SSE**:

   You can install Flask-SSE using pip:

   ```bash
   pip install flask-sse
   ```

2. **Write Python Code**:

   Here's a simplified example of how to implement it:

   ```python
   from flask import Flask
   from flask_sse import sse

   app = Flask(__name__)
   app.config["REDIS_URL"] = "redis://localhost:6379/0"  # You need Redis for Flask-SSE

   @app.route("/")
   def index():
       return "This is the SSE example."

   @app.route("/events")
   def sse_request():
       return sse(sse_id="my_sse_id", data="Your data goes here")

   if __name__ == "__main__":
       app.register_blueprint(sse, url_prefix="/stream")
       app.run(debug=True)
   ```

3. **Redis**:

   Flask-SSE uses Redis to manage events. Make sure you have Redis installed and running on your system. You can adjust the `app.config["REDIS_URL"]` to match your Redis setup.

4. **Comparison to Other Technologies**:

   - **REST**: REST is request-response-based and not suitable for continuous updates. It's more suitable for static data retrieval.

   - **GraphQL**: GraphQL allows clients to request specific data, but it's still based on request-response, not real-time updates.

   - **gRPC**: gRPC is efficient for high-performance, but it's not designed for continuous data streaming. It's more for remote procedure calls.

   - **Webhooks**: Webhooks allow real-time updates, but they rely on the client having a publicly accessible endpoint. SSE is simpler for one-way communication.

   - **Websockets**: Websockets are designed for bidirectional, full-duplex communication. If you need two-way real-time interaction, Websockets may be a better choice.

Remember, this is a basic example, and you can extend it to meet your specific requirements. SSE is suitable for sending continuous updates to clients, and you can adapt this to your program to keep the user engaged while the data is being fetched.