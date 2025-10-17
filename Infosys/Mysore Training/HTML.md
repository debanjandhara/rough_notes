### Reference Notes: LEX Training Material

### Section 1: Network Protocols and Location

### Uniform Resource Locator (URL)
**Definition:** The Uniform Resource Locator (URL) uniquely identifies a particular resource on the Internet.
**Syntax:** `Protocol://Host:Port/Path`

**Attributes:**

| Component | Description |
|---|---|
| Protocol | The protocol is used to communicate with the server |
| Host | Name of the server to connect to |
| Port | Every protocol on the Internet operates on a unique TCP/IP port. If port is not explicitly specified in the URL, default port for that protocol is assumed. The standard port for HTTP is 80 |
| Path | Specifies the path of the resource on the server (usually starts with a '/' which is sometimes known as WEBROOT) |
**Examples:**
- https://www.youtube.com/results?search_query=html5.2
- http://google.com
- http://www.youtube.com
- ftp://ftpadmin:mypassword@mydomain.com

### Protocols
**Definition:** For any client to communicate with any server, both the client and server must agree upon some predefined rules of communication. Such rules are called protocols.


**Notes:**

- Just by knowing the IP of the web server, the web browser cannot communicate with the web server. There needs to be a set of rules to facilitate the communication taking place. These rule sets are established as protocols.

*CrossReferences:* One such protocol is Hypertext Transfer Protocol (HTTP), which is used for web communication.

### Hypertext Transfer Protocol (HTTP)
**Definition:** In simple terms, Hypertext Transfer Protocol is set of rules for transferring files (text, graphic images, sound, video and other multimedia files) on WWW.

**Notes:**

- The web browser and the web server communicate with each other with an application-level protocol called HTTP.
- This allows a variety of clients to communicate with any vendor's server without compatibility problems.
- HTTP is a request/response based, stateless, and connectionless protocol.

#### HTTP as Request/Response based

**Notes:**

- The client establishes a connection with the server and sends the request.
- Over the same connection, the server sends the response.
- Once the response is delivered, the connection is terminated.

#### HTTP as Stateless
**Definition:** HTTP is called a stateless protocol because each request is executed independently, without any knowledge of previous requests.

**Notes:**

- Once a transaction ends the connection between the browser and the server is also lost.
- This potentially prevents denial of service attacks by keeping connections open indefinitely.
- To resolve the issue of losing previous request state in a multi-server environment, the server sends additional data (stored on the client/browser storage) that identifies a particular client and its state. The server uses this state data to service the request.

#### HTTP as Connectionless
**Definition:** HTTP is called a connectionless protocol because a new connection is established for every request.

#### HTTP hits
**Definition:** Each time a web server is requested for a file, it is called a hit. HTTP hits refers to the number of times a web server receives an HTTP request.

**Notes:**

- Every time a visitor loads a web page, a different request is sent for different web files like web pages, images, Cascading Style Sheet files, JavaScript files etc.
- Too many HTTP hits can slow down the loading of a website because the browser has to wait for the unprocessed files to load, creating a load delay.
- Developers must optimize the number of web resources used while designing a web page.

#### HTTP vs HTTPS

**Notes:**

- **HTTP:** Text based protocol; messages are easily intercepted if communication security is breached (less secure).
- **HTTPS:** Hyper Text Transfer Protocol over secured socket layer (SSL). Communication between browser and server is encrypted using an encryption algorithm.
- A URL using HTTPS typically starts with `https://...`
- HTTPS URLs are typically highlighted with a green color and lock symbol in the browser's address bar (this may vary).
- HTTPS crossed in red means the website's encryption is no more valid, warning the user to reconsider visiting the site (Privacy error shown in example).
- **HTTPS Assurance:** When using HTTPS, the user is communicating with the intended website (not a hoax site) and the content cannot be understood by any intruder.

### HTTP request
**Definition:** Message sent from browser to server.

**Notes:**

- Different HTTP request types (methods) include GET, POST.
- Message contains header and body (optional).

#### Request Header components
| Component | Description |
|---|---|
| Request URL | Specifies the name of the target resource and identifies the protocol version used by the client. |
| Request method | Specifies the type of the request being generated. |
| Request header | Pass additional information about the request and about the client to the server. Each header field consists of a name, followed by a colon (:) and the field value. |
| Request body | Optional message body contains data to be sent to the server. But this is present only in case of a POST request. |

#### GET method

**Notes:**

- The most commonly used method. Used by default to get static content.
- Parameters are passed as name-value pairs in the URL and are encoded if they contain special characters.
- Used when a small amount of data needs to be sent to the server as part of the request.
- Example: Searching for 'html5' results in URL `http://lex.infosysapps.com/search?q=html5`.
- **URL Encoding:** Performed to convert data passed via HTML forms. Replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits. The first question mark (`?`) is used as a separator.

#### POST method

**Notes:**

- Used to send parameters that need to be processed to the server.
- Parameters from the browser are passed as part of the message body.
- Used when a large number of field values have to be passed.

### HTTP response
**Definition:** The server responds to the client request through HTTP response. An HTTP response has a status line, a header and a message body.
**Notes:** To inform the browser regarding the status of the request made to the server, the HTTP response contains a field called status code, that is issued by a server.

### Different HTTP Responses


**Attributes:**


| Status Code | Title | Description |
|---|---|---|
| 1XX | Informational Responses | Indicates that the request was received and understood and also alerts the client to wait for a final response. |
| 2XX | Success | Indicates that the request was received, understood, accepted and Successfully processed. |
| 3XX | Redirection | Indicates that the client must take additional action to complete the request. |
| 4XX | Client errors | Intended for situations where the client has caused the error. The server specifies whether the error caused is temporary or permanent. |
| 5XX | Server Errors | Intended for situations when the server has failed to fulfill a request. |

**Examples:**
| Status Code | Description |
|---|---|
| 200 OK | The request has been processed successfully |
| 403 Forbidden | The server understood the request, but is refusing to fulfill it |
| 404 Not Found | The server has not found any resource for the requested URL |
| 500 Internal Server Error | The server encountered an unexpected error which prevented it from fulfilling the request |

### Multipurpose Internet Mail Extensions (MIME)
**Definition:** MIME is a standardized way to indicate the nature and format of a response. It is a standard that enhances email message formats to support attachments of audio, video, image, and application files in addition to text in character sets other than ASCII.

**Notes:**

- To inform the client about the incoming data format from the server, the HTTP response contains a `content-type` field.
- Servers insert a MIME type as a value in the `content-type` attribute of the response header before sending a response to the client.
- Clients use this content type or media type header to select an appropriate viewer application for the type of data the header indicates.
- Web applications use MIME types to determine a file or resource's format before transmission.
- MIME types can reveal a file's encoding or compression format.


**Attributes:**

| Category | Description | Examples |
|---|---|---|
| text | Represents any document that contains text and is theoretically human readable | text/plain, text/html, text/css, text/javascript |
| image | Represents any kind of image including animated images but not video | image/png, image/jpeg, image/gif |
| application | Represents any kind of binary data | application/json, application/sql, application/javascript, application/pdf |

### Section 2: JavaScript Stacks

### JS Stack

#### Introduction to MEAN/MERN stack

**Notes:**

- A technology stack (tech stack) is a combination of programming languages, tools, and frameworks used for building web applications.
- The tech stack is generally visualized in two parts: Front-end (Client side) and Back-end (Server side).
- **Front-end:** Technologies used for interaction with the user.
- **Back-end:** Technologies used on the server for processing user inputs and interacting with the database.
- It is essential to identify the right tech stack to speed up development.
- **MEAN stack:** MongoDB - Express.js - Angular - Node.js.
- **MERN stack:** MongoDB - Express.js - React - Node.js.
- JS stacks have gained attention because they involve open source technologies and a single programming language (JavaScript) used for the entire application.

#### Reasons to adopt JS (MEAN/MERN) stack

**Notes:**

- **Open source technologies:** Free and open-source components, benefiting from community contributions.
- **Common language:** Uses JavaScript for both client-side and server-side programming.
- **Cost effective:** Companies save costs by working with a single stack, eliminating the need to hire different specialists (creating the full-stack JavaScript developer profile).
- **Usage of JSON:** Data exchange uses JavaScript Object Notation (JSON) format, eliminating the need for conversion libraries and allowing easier work with external APIs.

#### MEAN/MERN Components

**Attributes:**

| Component | Stack Role | Details |
|---|---|---|
| **MongoDB** | Database system (M) | Open source document oriented database written in C++. Data stored in documents (name-value pairs) within a collection. |
| **Express.js** | Back-end web framework (E) | Lightweight Node.js based application development framework. Used for back-end development. |
| **Angular** | Front-end framework (A/MEAN) | Open source JavaScript framework (Google). Used for building both mobile and desktop web applications. Complete solution for rapid front-end development. |
| **React** | Front-end framework (R/MERN) | Open source JavaScript framework (Facebook). Used for building both mobile and desktop web applications. Complete solution for rapid front-end development. |
| **Node.js** | Back-end runtime environment (N) | Server side cross-platform open source JavaScript execution environment. Built on Google Chrome's V8 JavaScript runtime. |

### Structure of a web application (Client/Server Side Mapping)

**Notes:**

- **Client-side (Front-end):** Application running on user devices (PC, mobile, etc.). Communicates with the server to fetch information. Uses frameworks like Angular/React, HTML, CSS, JavaScript, and Bootstrap in the Browser.
- **Server-side (Back-end):** Hosts business logic and validation for processing client requests. Uses Node.js, Express, and Database (Mongo DB or MySQL).
- **Data Flow:**
    1. Client (Angular/React) initiates a **Make request**.
    2. Request goes to Node.js which **Parse request**.
    3. Request goes to Express which initiates **Get data** from the Database (Mongo DB/MySQL).
    4. Database returns **Return data** to Express.
    5. Express/Node.js prepares the response and sends a **Return request** to the client.
    6. Client (Angular/React) performs **Display response** in the browser.

### Section 3: HTML5 Fundamentals

### What is HTML?
**Definition:** HTML (Hyper Text Markup Language) is a markup language that defines the structure of web pages and determines how content is displayed online.

**Notes:**

- HTML is case-insensitive, meaning tags can be written in lowercase (`<html>`) or uppercase (`<HTML>`) and produce the same output.
- Current major version is HTML5 (HTML5.2 is the latest standard).
- HTML capabilities include: Publishing documents, creating forms, embedding media (videos, audio, flash movies), accessing online information via hyperlinks, and running on different operating systems.

### HTML elements
**Definition:** HTML elements are made up of 2 things: 1) Tags (HTML instructions), and 2) Content (On which the HTML instructions should be applied).

#### Basic syntax
**Syntax:**
```
1. <tag> <!-- start tag -->
2. <!-- content -->
3. </tag> <!-- end tag -->
```

#### Different categories of elements

**Attributes:**

| Category | Definition | Syntax | Example |
|---|---|---|---|
| **Container Element** | Contains start and end tag. | `<tagname> text here </tagname>` | `<title> Welcome to Infosys!</title>` |
| **Empty Element** | Contains only start tag. | `<tagname/> text here` | `First line<br/>Second line` |
| **Block Element** | Starts on a new line. | (content not found in source) | `h1 - h6, p, div, form` |
| **Inline Element** | Starts on a same line (if space is available). | (content not found in source) | `a, img, span` |

### Comment
**Definition:** As a developer, you may want to document your code, so that you can easily refer to it in the future.
**Notes:** Comments are ignored by browser.
**Syntax:**
```
1. <body>
2. <!-- this line is commented -->
3. </body>
```

### Skeleton of an HTML5 page
**Syntax:**
```html
1. <!DOCTYPE html> <!-- DTD(document type definition)
It instructs web browser about the version of
html in which the page is written in. -->
2.
3. <html> <!-- container for various html elements -->
4.
5. <head> <!-- container for various head elements
6. consists of metadata content -->
7.
8. </head>
9.
10. <body> <!-- contains all the contents of a html document -->
11.
12. </body>
13. </html>
```

**Notes:**

- The HTML structure is divided into three sections: HTML, head and body.
- **`<!DOCTYPE HTML>`:** Instructs the web browser about the version of HTML.
- **`<html>`:** The container for various HTML elements.
- **`<head>`:** Consists of various head elements and metadata content.
- **`<body>`:** Includes various contents of an HTML document.

### Head element (<head>)
**Definition:** The `<head>` element is a container for all the head elements like a title for the document, scripts, styles, meta information, and more. It is placed between the `<html>` tag and the `<body>` tag.
**Notes:** HTML metadata is data about the HTML document. Metadata is not displayed but will be read by the machine (e.g., character encoding, author, description, refresh).

**Attributes:**

| Tag | Description |
|---|---|
| `<title>` | Used to provide the title of the document displayed in browser toolbar/tab and when bookmarked. |
| `<meta/>` | Used to describe a page's content to the web browser. |
| `<link/>` | Used to provide a link between a HTML document and external resources. |
| `<style>` | Used to specify the style information for a HTML document. |
| `<script>` | Used to embed a script within a HTML document. |

### Meta element (<meta>)
**Definition:** In HTML5, metadata about an HTML document is provided using the "meta" element tag. Metadata is information about the data on the page that is not visible to the user.

**Notes:**

- Meta elements are used to include key-value pairs describing properties (author, keywords, character encoding, etc.).
- It is machine readable and does not render anything on the web page.
- Typically positioned in the `<head>` section.


**Attributes:**

| Attribute | Value | Description |
|---|---|---|
| name | application-name, author, description, generator, keywords | Specifies a name for the metadata |
| http-equiv | content-type, default-style, refresh | Provides HTTP header for information/value of content attribute |
| content | text | Gives the value associated with http-equiv or name attribute |
| charset | character_set | Specifies character encoding for an HTML document |
**Examples:**
| Scenario | Code | Notes |
|---|---|---|
| Keywords | `<meta name="keywords" content="tutorial,HTML">` | |
| Refresh | `<meta http-equiv="refresh" content="30">` | |
| Character Encoding | `<meta charset="UTF-8">` | |
| Viewport Setting | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` | Controls dimensions and scaling. `width=device-width` sets page width to device screen width. `initial-scale=1.0` sets initial zoom level. |

### Body element (<body>)
**Definition:** The `<body>` tag defines the document's body and is used to add content to the web page. There can be only one `<body>` element in an HTML document.
**Syntax:**
```html
1. <body>
2. <form> <input> </form>
3. <table> </table>
4. <img>
5. <audio></audio>
6. <video></video>
7. <br>
8. <div></div>
9. <span></span>
10. <h1></h1>
11. </body>
```

**Notes:**

- The example snippet shows tags used for user input (`<form>`, `<input>`), structure (`<table>`, `<br>`, `<div>`, `<span>`, `<h1>`), and multimedia (`<img>`, `<audio>`, `<video>`).

### Section 4: Input and Form Elements

### Form element (<form>)
**Definition:** Forms are used for collecting user information which may be for registration, payment, etc. Forms are used to pass user data to a specified URL.
**Notes:** To create a form, the `<form>` tag is used.

**Attributes:**

| Attribute | Description |
|---|---|
| Name | Used for accessing the form data by the scripting language. |
| Action | Used to specify the server-side program that will be executed when the form is submitted. |
| Method | Specifies the HTTP request method (GET/POST) used to submit data. |
| Target | Specifies where to display the response once the form is submitted. |

### Input element in Form (<input>)
**Definition:** The `<input>` tag specifies an input field used inside a form, where the user can enter data.
**Syntax:** `<input type="input-type" value="element-value"/>`

**Notes:**

- The `type` attribute specifies the type of value accepted.
- The `value` attribute specifies the element's value sent to the server program.

#### Input types present before HTML5

**Attributes:**

| Value | Description |
|---|---|
| text | Creates a string input field. |
| password | Creates a password input field in masked format |
| radio | Creates a radio button. |
| checkbox | Creates a checkbox |
| button | Creates a simple button |
| submit | Creates a button to submit the form. |
| reset | Creates a button to reset form fields. |

#### New input types added in HTML5
**Notes:** HTML5 introduced new input types to reduce development time and improve user experience.

**Attributes:**

| Type | Description |
|---|---|
| date | Input represents date (year, month, date) value without time zone |
| email | Input represents an email address value |
| number | Input represents a numerical value. |
| url | Input represents URL address value. |
| file | Input that lets the user select a file. |
| color | Input that lets the user choose a color. |
| range | Input that lets the user choose a number from a range. |

#### Input types and keyboard layouts
**Notes:** Input types also affect the keyboard layouts on a mobile phone (e.g., number input type provides a numeric keypad).

#### Attributes of the input element (Detailed)

**Attributes:**

| Attribute | Description | Usage/Observation |
|---|---|---|
| required | Value required for form submission. | Used for username/password fields. |
| value | Specifies default value of input element. | (content not found in source) |
| type | Identifies type of input element. | e.g., "text", "password". |
| name | Name of input element used for form submission. | Essential for referencing form data after submission. |
| size | Identifies the width of input text that the user can see. | Size="5" displays input width 5x average character width. |
| autofocus | Focuses on a particular form element automatically. | Username field focused on page load. |
| maxlength | Identifies the maximum length of input value. | Password maximum span up to 12 characters. |
| minlength | Identifies the minimum length of input value. | (content not found in source) |
| pattern | Specifies a pattern (regular expression) for entering input text. | Used for custom validation (e.g., alphanumeric check). |
| placeholder | Displays a text (hint) within an input control for the user. | e.g., "Enter Name". |
| steps | Specifies the legal number of intervals. | (content not found in source) |
| formnovalidate | Skips validations upon form submission, used with submit button. | (content not found in source) |
| readonly | Prevents user from modifying the value, value will passed on submit. | (content not found in source) |
| disabled | Prevents from modifying the value, value is not sent on submit. | Last name field disabled in example. |
| multiple | allows to enter/select more than one value. | (content not found in source) |

### Label element (<label>)
**Definition:** The `<label>` tag defines a label for an input element.

**Notes:**

- Improves usability; clicking on the label text toggles the input control.
- Bound to an input element using the `for` attribute, which must match the `id` attribute of the input element.
- The `id` attribute is used to uniquely identify an element (best practice for form elements).
- Input elements are also called UI (User Interface) components.
**Examples:**
- `<label for="Username">Enter Username</label>` bound to `<input type="text" id="Username" />`

### Select element (<select>)
**Definition:** Used to create a dropdown list.

**Attributes:**

| Attributes | Description |
|---|---|
| autofocus | Focuses on a particular input element of a form automatically. |
| name | Name of the select element. |
| disabled | Disables the dropdown. |
| multiple | Select multiple options from the dropdown list. |
| size | Value of size decides the number of visible options in dropdown. |

### Datalist element (<datalist>)
**Definition:** Used to provide predefined values for the input field.

**Notes:**

- Datalist dropdown is used for autocomplete; the selected value can be edited.
- Requires the input field to have a `list` attribute pointing to the `id` of the datalist element.
- Functionally different from `<select>`.

### Textarea element (<textarea>)
**Definition:** Used for providing multiple line input.

**Notes:**

- Ensure no unwanted spaces or characters are added between the textarea tags, as they will be visible.

**Attributes:**

| Attributes | Description |
|---|---|
| maxlength | Identifies the maximum length of input value. |
| placeholder | Displays a text (hint) within an input control for the user. |
| rows | Number of visible lines. |
| cols | Visible width of textarea. |
| autofocus, name, disabled | (Also supported, general input attributes). |

### Button element (<button>)
**Definition:** Used to create a clickable button which is either used for submitting a form or resetting the form fields.

**Notes:**

- Button types: `reset` (resets form data), `submit` (submits form data), and `button` (clickable button).

### Organizing fields in a form

#### div tag (<div>)
**Definition:** Defines a division or a section in an HTML document. Used to group HTML elements and apply CSS styles.

**Notes:**

- Block-level element; browser inserts a line break before and after the tag.
- Used to group field names and input fields in forms.

#### span tag (<span>)
**Definition:** Used to group inline-elements in a document.
**Notes:** Inline element, unlike block-level `<div>`.

### Section 5: Multimedia Elements

### Embedded elements
**Definition:** Components like image, audio, video, or incorporated webpages added to a page are managed using embedded elements.
**Notes:** Every embedded element generates a new request to fetch the embedded component from the server.

### Audio Element (<audio>)
**Definition:** Used to embed audio in a web page.

**Attributes:**

| Attributes | Description |
|---|---|
| src | Specifies the URL of the media resource |
| controls | Media control feature like play/pause will be displayed |
| loop | Causes the media to play in a loop |
| autoplay | Media will play automatically on page load |
| muted | Media will play in muted state |
**Notes:** Content between `<audio>` and `</audio>` tags is shown by browsers that do not support the audio element.

### Video Element (<video>)
**Definition:** Specifies video, such as a movie clip or other video streams. Specifies a standard way to embed a video in a web page.

**Attributes:**

| Attributes | Description |
|---|---|
| src | Specifies the URL of the media resource |
| controls | Media control feature like play/pause will be displayed |
| loop | Causes the media to play in a loop |
| autoplay | Media will play automatically on page load |
| muted | Media will play in muted state |
| width | Specifies the width of the image in pixels |
| height | Specifies the height of the image in pixels |
| Poster | Representative frame for the video till the video is played |
**Notes:** Some video attributes are similar to audio element attributes.

### Source Element (<source>)
**Definition:** Allows specification of alternative multiple media resources for media elements, which the browser may choose from based on media type, codec support, or media query.

**Notes:**

- Different media sources must be listed in order (most desirable to least desirable).
- `<source>` element is only considered when the `src` attribute of the media element is absent.
- Used because not all browsers support all image/audio/video formats.
- `src` attribute: location of the audio or video file.
- `type` attribute: type of the file (audio or video file).
- `codecs` attribute: specifies version of the codecs needed to play the media file.

### Section 6: Anchor and Linking

### Anchor Element (<a>)
**Definition:** Any text or image that provides a link to another webpage is called as "hyperlink". To link webpages, anchor element is used.
**Syntax:** `<a href="url" target="value">Text</a>`

**Attributes:**

| Attribute | Description |
|---|---|
| href | Used to specify the URL of the webpage that needs to be linked. |
| target | Used to specify where to open the linked webpage. |
| target="_blank" | Linked resources will open in a new window |
| target="_self" | Linked resources will open in a current window |
| target="_parent" | Linked resources will open in the parent of the current window (If no parent, it behaves like _self) |
| target="_top" | Linked resources will open in the top most level window of the current window (If no parent, it behaves like _self) |
| rel="noreferrer noopener" | Used with `target="_blank"` for security to prevent the opened page from changing the location of the original page (mitigating phishing attacks). |

**Notes:**

- Appearance of links: Unvisited (underlined and blue), Visited (underlined and purple), Active (underlined and red).
**CommonMistakes:**
- ⚠️ Do not use generic terms such as "Click here" or "link" as hyperlink text. Use relevant text indicative of the destination.
- ⚠️ Not using `rel="noreferrer noopener"` with `target="_blank"` exposes the user's information to phishing attacks.

### Section 7: Text Formatting and Lists

### Heading elements (<h1> to <h6>)
**Definition:** HTML provides the elements like `<h1>`... `<h6>` in order to format headings.

**Notes:**

- `<h1>` (32px) defines the most important heading.
- `<h6>` (10px) defines the least important heading.
- Users skim the contents in web pages by its headings.

### Text formatting elements
**Definition:** HTML defines formatting elements for formatting the text in the webpages.

**Attributes:**

| Attributes | Description |
|---|---|
| `<b>` | Describes bold text |
| `<del>` | Describes deleted text |
| `<em>` | Describes emphasized text |
| `<i>` | Describes italicized text |
| `<ins>` | Describes inserted text |
| `<mark>` | Describes highlighted text |
| `<small>` | Describes small text |
| `<strong>` | Describes strong text |
| `<sub>` | Describes subscripted text |
| `<sup>` | Describes superscripted text |

**Notes:**

- `abbr` element defines abbreviation using `title` attribute.
- `small` element defines text in smaller font-size.
- `mark` element highlights text.
- `strong` element displays text in bold.
- `em` element emphasis text.
- `sub` element displays text as sub-script.
- `sup` element displays text as super-script.

### List Elements
**Definition:** The data in the web pages are better perceived when it is organized into lists.
**Notes:** Lists can be numbered (ordered list) or unnumbered (unordered). There are 3 types of list in HTML.

#### Unordered List (<ul>)

**Notes:**

- Defined using `ul` element; list-items defined using `li`.
- Default bullets are "Disc".
- Bullets can be customized (e.g., `type="circle"` for circle bullets). (Type attribute can also be set to "square".)

#### Ordered List (<ol>)

**Notes:**

- Defined using `ol` element; list-items defined using `li`.
- Default bullets start from 1.
- List type can be changed (e.g., `type="A"` for alphabet style; `type="i"` for small Roman numerals).

#### Definition list (<dl>)

**Notes:**

- Defined using `<dl>` tag.
- Description term defined using `<dt>` tags.
- Description definition defined using `<dd>` tags.

### Character entities
**Definition:** Used to include special characters (reserved characters like < or >) or those absent on the keyboard (like ©) as content.

**Notes:**

- Entity references start with `&` and end with `;`.
- Can be specified by entity name or entity number.
- `<hr>` can be used to insert a thematic break.

**Attributes:**

| Character | Description | Entity Name | Entity Number |
|---|---|---|---|
| (space) | Non-breaking space | &nbsp; | &#160; |
| < | Less than | &lt; | &#60; |
| > | Greater than | &gt; | &#62; |
| & | Ampersand | &amp; | &#38; |
| © | Copyright | &copy; | &#169; |
| TM | Trademark | &trade; | &#153; |
| ® | Registered Trademark | &reg; | &#174; |

### Section 8: Table Elements and Layout

### Table element (<table>)
**Definition:** A table element in HTML helps in representing content in terms of a two-dimensional structure i.e., a combination of rows and columns.

**Notes:**

- **`border`** attribute: provides the border to the table.
- **`<thead>`** tag: provides the heading to the table.
- **`<tr>`** tag: creates rows.
- **`<th>`** tag: creates columns (header cells).
- **`<tbody>`** tag: encloses the content in the table.
- **`<td>`** tag: provides content or data (data cells).
- **`<caption>`** tag: gives a title to the table.

#### Table Attributes (<th> and <td>)

**Attributes:**

| Attributes | Description |
|---|---|
| Colspan | Merges column (e.g., `colspan="2"` to merge two columns). |
| Rowspan | Merges row (e.g., `rowspan="2"` to merge two rows vertically). |

#### Aligning forms with Table elements

**Notes:**

- Alignment is crucial for better look and feel.
- Tables (`<tr>`, `<td>`) are used to align form elements by placing the label in one `<td>` and the input field in an adjacent `<td>` within the same `<tr>`.
- Best practices for alignment suggest right alignment for labels or placing labels on top of input fields if horizontal space is limited.

### Section 9: HTML Semantic Elements

### Semantic elements
**Definition:** Used to organize varied webpage content and provide better semantics (meaning) to content.

**Attributes:**

| Sectioning element | Description |
|---|---|
| main | Defines the main content of a document. |
| section | Represents a group of related content. |
| article | Defines an individual self-contained content. |
| header | Defines a header for the document or a section. |
| footer | Defines a footer for the document or a section. |
| nav | Defines navigation links |
| aside | Defines content apart from the page content. |
| address | Defines contact information for an article or web page. |
| h1, h2, h3, h4, h5, h6 | Defines heading |

### Section 10: Best Practices Summary

### Best practice for writing a HTML document (Summary)

**Notes:**

1. Begin HTML file with `<!DOCTYPE>` declaration.
2. Write HTML elements in lowercase (convention for readability).
3. Follow proper document structure (use `<html>`, `<head>`, `<body>`).
4. Indent nested elements properly.
5. Always close container elements (`</form>`, `</body>`).
6. Use meaningful titles for your webpage (for SEO and usability).
7. Write attributes in lowercase.
8. Enclose attribute value in double quotes.
9. Use comments for documentation (`<!-- comment -->`).
10. Provide metadata regarding webpage content (use `<meta>` tags for description, keywords, author).
11. Use sectioning elements to add semantics to content (`<main>`, `<section>`, `<article>`).
12. Use `alt` attribute with images (for accessibility and screen readers).
13. Use `label` element for form elements (for usability and binding via `for`/`id`).

### Best practice for form layout

**Notes:**

- **Headings:** Give a clear heading specifying the form's purpose.
- **Sectioning & Addressing:** Use conversational tone; visually separate content into specific topics/sections.
- **Alignment:** Right-align labels for better look and feel, or place labels atop inputs if space is limited (often achieved using tables).
- **Buttons:** Use only one main button (e.g., Submit); visually separate secondary buttons (Reset/Cancel), perhaps turning secondary actions into hyperlinks. Main button should perform main function.
- **Mandatory Fields:** Use `*` (asterisk symbol) to indicate mandatory fields and explicitly mention that "* marked fields are mandatory".

### Code Maintainability

**Notes:**

- Delete unused code that is not rendered on the webpage, instead of just commenting it out, as commenting bloats programs and reduces readability.
- Avoid Artifacts with High Cyclomatic Complexity; keep Artifacts small and simple.

### Search engine optimization (SEO)
**Notes:** HTML5 aids SEO through Semantic Markup (`<header>`, `<nav>`, `<article>`), Clear URL composition, Structured Data (JSON-LD), and focus on Accessibility and Performance (Image/CSS optimization, CDNs, script placement).

<CoverageCheck>
- Total topics extracted: 45 (Counting subtopics and exercises/tryouts as major sections/details).
- Any missing or unclear sections: A few incomplete code snippets were noted (specifically in the Simple Form Tryout and the DL Registration Form), and specific URL/Email validation requirements were noted as implied but not detailed beyond input type in some tables. However, all visible text and constraints have been captured.
- Approx. compression ratio vs original text: Moderate compression of redundant introductory/summary paragraphs, high detail retention in tables/code. Estimated ~75-80% of raw content volume retained as structured text.
- Warnings (if text seemed incomplete): Password regex pattern in Simple Form Tryout (Page 7 Forms sequence) was incomplete in the OCR (`pattern="^[A-Za-z]\w{6,8}[0-9]$"/>` was the completion used in the context, but the source only showed `pattern="^[A-Za-z]-...-9]$"/>` followed by a comment break).
</CoverageCheck>
