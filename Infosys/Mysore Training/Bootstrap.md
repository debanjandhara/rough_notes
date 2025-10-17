# Technical Reference Notes: Bootstrap

### About Bootstrap
**Definition:** Bootstrap is an HTML, CSS, and JavaScript framework used to quickly create responsive webpages by utilizing its built-in components. It is a sleek, intuitive front-end framework that follows the mobile-first approach.
**Notes:**
* It helps in the quick development of responsive websites by providing HTML layout and CSS templates for UI components like Forms, Tables, Navigation menus, Dropdowns, Carousel, etc.
* It uses HTML, CSS, and JS for faster and easier web development.
* This course is designed to enable learners to quickly create stylish and responsive web pages through a hands-on approach.

### Learning Outcomes
**Notes:**
After completing this course, you will be able to:
* Design the layout of a webpage using container, row, and column classes of Bootstrap.
* Develop webpages that can be viewed on various devices using the grid system of Bootstrap.
* Apply typography classes in order to achieve the desired look and feel for a given text.
* Organize data into tables using Bootstrap table classes.
* Make the images responsive using Bootstrap image classes.
* Use UI components in order to create interactive web pages.
* Build applications which facilitate easy navigation using the navigation bar.
* Design forms using different layouts for a webpage.

### Need of Bootstrap
**Definition:** We need Bootstrap to overcome certain disadvantages inherent in traditional CSS styling.
**Notes:**
In spite of the various advantages CSS has, it has certain disadvantages as well:
* Though CSS is compatible with all browsers, the level of compatibility varies with each browser. This means that certain CSS features may not be supported by some browsers. So, every time you design a website, you need to ensure that its appearance remains uniform across browsers.
* All enterprise-level applications are huge and difficult to maintain. They have many web pages with different styling requirements. Several CSS stylesheets are required for styling those pages. It is difficult to manage them, as the browser compatibility might vary.

### Browser Compatibility
**Definition:** The CSS property `all` is used to reset all properties to their initial or inherited value.
**Attributes:**
| Value | Description |
| :--- | :--- |
| `initial` | Sets the initial values for all properties applied to the element or its parent. |
| `inherit` | Sets all properties of a child to the parent's value. |
| `unset` | Sets all properties of a child to the parent's value, if no parent exists then the initial value is used. |
**Notes:**
* **Observation (Chrome):** Properties applied to the `<p>` element before `all: inherit` were reset, and only the `color` property was applied.
* **Observation (Internet Explorer):** `background-color` and `color` properties were applied, and `all: inherit` was altogether ignored. This shows that the `all` property is not compatible with IE.
*CrossReferences:* This is where CSS frameworks come to the rescue.

### CSS framework
**Definition:** It is nothing but a package made up of files and folders of standardized CSS code that makes it easier and faster for creating web designs that are compliant with certain standards (like browser compliance etc.).
**Notes:**
* It gives everything a typical website would require, but is also flexible enough for any further customization as well.
* There are many CSS frameworks like Foundation, Skeleton, Bootstrap, etc.
* In this course, we will learn Bootstrap.

### Bootstrap Features
**Notes:**
* Was built at Twitter Inc. by Mark Otto and Jacob Thornton as a framework for internal tools.
* Is a complete CSS framework offering Grid system and configurations, Typography classes, UI components like forms, tables and more.
* Is a widely used framework in the development of responsive websites.
* Has very good documentation which can be found in Bootstrap site.
* Because of its amazing features, it has emerged to be one of the most popular CSS frameworks.
* As on 15th February 2015, Bootstrap was ranked number one on GitHub.
* Currently, there are over 1 million websites which make use of Bootstrap. Some examples include: `paypal.com`, `fontawesome.io`, `allegro.pl`, `npmjs.com`.

### Responsive Web Design
**Definition:** Responsive web design is all about providing an optimal viewing experience across a wide variety of devices. This means that the entire content of the site should appear without loss of any information along with the maintenance of its appeal, when it is viewed on different screen sizes.
**Attributes:**
| Feature | Description |
| :--- | :--- |
| **Fluid Layout** | Layout grows and shrinks based on the size of the device browser. |
| **Flexible Images** | Images adapt to the size of the device browser. |
| **Responsiveness** | Selectively apply CSS based on the size of browser/device using responsive patterns. |

### Getting Started
#### Way 1: Download
**Definition:** Download the `bootstrap.css` file required.
**Notes:**
* The `bootstrap.css` file should be placed inside the 'css' folder under 'Web Content' of a 'Dynamic Web Project'.
* Include it in the HTML page just as an external stylesheet.
**Syntax:**
```html
1. <link href="bootstrap.css" rel="stylesheet">
```
#### Way 2: CDN (Content Delivery Network)
**Definition:** Include Bootstrap 5 from a CDN by using the given links in the HTML page.
**Notes:**
* MaxCDN provides CDN support for Bootstrap's CSS and JavaScript.
* For JavaScript, you must also include JavaScript plugins and Popper.
**Syntax:**
**Compiled and Minified CSS:**
```html
1. <!--compiled and minified CSS -->
2. <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
```
**JavaScript - Bundle:**
```html
1. <!--JavaScript - Bundle-->
2. <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
```
**JavaScript - Separate:**
```html
4. <!--JavaScript - Separate-->
5. <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLX15PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
6. <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2A14u+LWgxfKTRIcfu@JTxR+EQDz/bgldoEy14H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
```

### Bootstrap 5 vs Bootstrap 4
**Attributes:**
| Differs on | Bootstrap 5 | Bootstrap 4 |
| :--- | :--- | :--- |
| **Extended color palette** | More color options added to the color palette. | Color options are limited. |
| **jQuery Deprecation** | Bootstrap 5 drops jQuery and forced dependency. | jQuery has been used by Bootstrap 4 as a dependency. |
| **Floating Labels** | Bootstrap 5 version supports floating labels for the input fields in forms. | Bootstrap 4 version does not support floating labels for the input fields in forms. |
| **Browser support** | No such support for Internet Explorer on Bootstrap 5. | Bootstrap 4 supported Internet Explorer 10 and 11. |
| **Bootstrap Icons** | Bootstrap 5 has introduced a SVG library having over 1000 icons. | There was no library for SVG icons in Bootstrap 4. |
| **RTL Support** | Bootstrap 5 has also introduced the RTL support which allows us to develop the type of content that we need to write from the right-hand side to the left-hand side of the page. | Bootstrap 4 does not have any such RTL support. |
| **Enhanced Grid System** | Bootstrap 5 retains the previous grid system and enhances further by introducing extra grid tier `xxl` to minimize the effort of making responsive webpages. | Bootstrap 4 had a grid system. |
| **Placeholder Components** | Loading placeholders on the page is possible in Bootstrap 5. | Loading placeholders on the page is not possible in Bootstrap 4. |
| **Enhanced Form Elements** | The form elements of Bootstrap 5 are with a custom design that gives a consistent look and feel for all browsers. | The form elements of Bootstrap 4 are known to default to the view provided by the browser. |

### Container Classes
**Definition:** In order to properly place the content in a webpage, Bootstrap needs a container element to wrap the page contents.
**Notes:**
* All content of a page should be inside a container class for the proper rendering of a webpage.
**Syntax:**
```html
1. <div class="container/container-fluid">
2. Enter text here
3. </div>
```
**Notes:** Bootstrap classes are nothing but CSS classes, so you can modify their CSS properties (e.g., adding a background color).
#### .container
**Definition:** A fixed width responsive container.
**Notes:**
* The width of the container is fixed for specific viewport ranges:
    * From 1200px onwards: width remains constant as **1140px**.
    * From 992px to 1199px: width remains constant as **960px**.
    * From 768px to 991px: width remains constant as **720px**.
* For a particular range of values, the container size is fixed.
#### .container-fluid
**Definition:** A full width responsive container, utilizing the entire width of the browser/viewport (webpage's visible area).
**Notes:**
* This class does not have media query constraints on width, so it constantly resizes as you change the width of the viewport.

### Grid System in Bootstrap
**Definition:** In Bootstrap, each webpage can be divided into rows and column-grids.
**Notes:**
* Each row has 12 column-grids.
* Width of each grid = (100/12) % = 8.333333%.
#### Row Class
**Definition:** To create a row in Bootstrap, `.row` class needs to be used.
**Notes:**
* The row occupies the entire width of the container.
* Multiple rows can be created within the same container.
**Syntax:**
```html
1. <div class="container/container-fluid">
2. <div class="row">Enter text here</div>
3. </div>
```
#### Row without Container
**Notes:**
* If a row is placed without a container, 15px of content on the left and right sides will not be visible on the screen.
* This happens because the `.row` class is defined with `margin-right: -15px;` and `margin-left: -15px;` in `bootstrap.css`.
* The `.container`/`.container-fluid` classes apply opposing padding (`padding-right: 15px;` and `padding-left: 15px;`) and margin (`margin-right: auto;` and `margin-left: auto;`). When a row is inside a container, the container's padding adjusts the row's margin, so the entire content of the row is visible.
#### Column Classes
**Definition:** To create a column in Bootstrap, `.col-<sq>-<n>` class needs to be used.
**Notes:**
* `<sq>` is the size qualifier and `<n>` is the number of grids the column should occupy (0 to 12).
**Attributes:**
| Size Qualifier (`<sq>`) | Description | Screen Width |
| :--- | :--- | :--- |
| `lg` | For large devices | >= 1200px |
| `md` | For medium devices | < 1200px and >=992px |
| `sm` | For small devices | < 992px and >=768px |
| `xs` | For extra small devices | < 768px |
**Syntax:**
```html
1. <div class="container-fluid">
2. <div class="row">
3. <div class="col-<sq>-<n>">Enter text here</div>
4. </div>
5. </div>
```
#### Column without Row
**Notes:**
* If a column is not put inside a row, the columns will start after the padding of 15px.
* This occurs because the row's margin of -15px normally compensates for the container's padding of 15px. Without a row, this compensation does not happen.
#### Equal and Unequal Column Width
**Notes:**
* The page layout is always designed by using 12 grids.
* Elements can span for multiple grids as required.
* In total, a row will have a width of 12 grids.
#### Overflow (Grid System)
**Definition:** Overflow occurs if the sum of all column widths crosses 12 grids.
**Notes:**
* Overflow can happen in two ways:
    1. **Horizontal Overflow:** If the total grids exceed 12 (e.g., 14 grids), the subsequent column moves to the next line of the same row.
    2. **Vertical Overflow:** If the text content inside a column cannot fit into the allocated grids, it overflows vertically within the column box.
#### Column Offset
**Definition:** Used to give space between two columns.
**Notes:**
* Using `col-md-m offset-n` creates a column with `m` grids, and a column of `n` blank grids to the left of it.

### Margin and Padding Utilities
**Definition:** Used to control the spacing and sizing of the elements and components.
**Notes:**
* Utilities can be applied to any element using the `m-` (margin) and `p-` (padding) prefix classes respectively.

### Gutters
**Definition:** Gutters are the spacing or padding between the columns which is used to align the content in the grid system.
**Notes:**
* They are responsively adjusted.
* Gutters can be applied to individual columns or to the entire row by using horizontal (`.gx`) and vertical (`.gy`) gutters.
#### Horizontal Gutters
**Definition:** The horizontal gutter class is used to control the horizontal widths.
**Syntax:**
```html
1. <div class="container/container-fluid">
2. <div class="row gx-2">
3. <div class="col">Enter the text here</div>
4. <div class="col">...</div>
5. </div>
6. </div>
```
#### Vertical Gutters
**Definition:** The vertical gutter class is used to control the vertical widths.
**Syntax:**
```html
1. <div class="container/container-fluid">
2. <div class="row gy-2">
3. <div class="col">Enter the text here</div>
4. <div class="col">...</div>
5. </div>
6. </div>
```

### Layout for Multiple Devices
**Definition:** We need to design a layout that will enable optimal viewing in multiple screen sizes (mobile, tab, desktop).
**Syntax:**
```html
1. <div class="container-fluid">
2. <div class="row">
3. <div class="col-<sq1>-<n> col-<sq2>-<m>"> ... </div>
4. </div>
5. </div>
```
**Examples:**
**Example Configuration (2 Images):**
* **On desktops (md):** Images appear one beside the other (e.g., 4 grids, 1 offset left).
* **On a tablet screen (sm):** Each image appears one below the other, in the center of the screen (e.g., 5 grids, 3 offset left).
* **On a mobile screen (xs):** Images displayed one below the other, occupying the entire width of the screen (e.g., 12 grids, no offset).

### Typography
**Definition:** Typography refers to the styling of textual matter on the page.
**Notes:**
* Bootstrap has modified most of the element selectors and introduced classes to address modern UX demands.
* The classes and element selectors under Typography are categorized into four groups:
**Attributes:**
| Category | Description |
| :--- | :--- |
| Text size | These classes and element selectors take care of the font type and size. |
| Text Alignment | These classes take care of the alignment of the text. |
| Text Emphasis | These classes and elements selectors emphasize the text by playing with the font weight and color. |
| Text Transformation | These classes transform the case of the text. |
#### Text Size
**Definition:** Bootstrap has modified element selectors (`<h1>` through `<h6>`, `<small>`) to make headings attractive.
**Syntax:**
Normal HTML heading structure is used, linking Bootstrap provides the styling modifications.
#### Display Text
**Definition:** Bootstrap 5 provides display headings to make headings that stand out better in between text.
**Notes:**
* These headings are created by adding the `.display-x` class to the heading tag (where x is 1 through 6).
**Syntax:**
```html
1. <div class="container">
2. <h1 class="display-1">Display 1</h1>
3. <h1 class="display-2">Display 2</h1>
4. <h1 class="display-3">Display 3</h1>
5. <h1 class="display-4">Display 4</h1>
6. <h1 class="display-5">Display 5</h1>
7. <h1 class="display-6">Display 6</h1>
8. </div>
```
#### Text Alignment
**Definition:** Classes provided by Bootstrap for text alignment.
**Notes:**
* `.text-start`: First word of every line touches the left edge, while the last word of each line won't touch the right edge.
* `.text-center`: All the lines in the paragraph will be centrally aligned.
* `.text-end`: First word of every line will not touch the left edge, instead the last word of each line will touch the right edge.
#### Text Emphasis
**Definition:** Classes provided by Bootstrap for text emphasis (by adjusting font weight and color).
#### Text Transformation
**Definition:** Classes provided by Bootstrap for text transformation (changing case).

### Tables
**Definition:** HTML provides tables to present data in a tabular format. Bootstrap provides different classes to make the appearance of these tables attractive.
**Notes:**
* The `.table` class provides horizontal dividers and small cell padding (8px).
* In order to group head and body sections, `<thead>` and `<tbody>` should be used inside the `<table>` element.
#### Table Bordered
**Definition:** Adds borders to all the table cells.
**Syntax:**
```html
1. <table class="table table-bordered">
2. <thead>...</thead>
3. <tbody>...</tbody>
4. </table>
```
#### Small Table
**Definition:** Makes the table more compact.
**Syntax:**
```html
1. <table class="table table-sm">
2. <thead>...</thead>
3. <tbody>...</tbody>
4. </table>
```
#### Table Hover
**Definition:** Enables the hover state of the table rows.
**Syntax:**
```html
1. <table class="table table-hover">
2. <thead>...</thead>
3. <tbody>...</tbody>
4. </table>
```
#### Table Striped
**Definition:** Provides alternate colors (like Zebra stripes) to table rows.
**Syntax:**
```html
1. <table class="table table-striped">
2. <thead>...</thead>
3. <tbody>...</tbody>
4. </table>
```
#### Table Responsive
**Definition:** Makes a table responsive in nature.
**Notes:**
* We will get the border and a horizontal scrollbar below the table for those devices which have a screen width under 767px only when the entire text content cannot be shown in the available screen width.
* Above 767px, there is no effect on the table.
**Syntax:**
```html
1. <div class="table-responsive">
2. <table class="table">
3. <thead>...</thead>
4. <tbody>...</tbody>
5. </table>
6. </div>
```

### Bootstrap classes for styling images
**Definition:** Bootstrap provides classes to style images and make them responsive.
#### Rounded Images
**Purpose:** To add rounded corners to the image.
**Syntax:**
```html
1. <img src="aeroplane.jpg" class="rounded"/>
```
#### Circular Images
**Purpose:** To give the image a circular shape.
**Syntax:**
```html
1. <img src="aeroplane.jpg" class="rounded-circle"/>
```
#### Thumbnail Images
**Purpose:** To give thumbnail appearance to an image.
**Syntax:**
```html
1. <img src="aeroplane.jpg" class="img-thumbnail"/>
```
#### Responsive Images
**Purpose:** To fit images automatically to the screen size available.
**Notes:**
* The `.img-fluid` class has the CSS properties: `max-width: 100%;` and `height: auto;`.
* Because of these properties, the image automatically adjusts its size with respect to the screen size.
**Syntax:**
```html
1. <img src="aeroplane.jpg" class="img-fluid"/>
```

### Cards
**Definition:** A card in Bootstrap 5 is a bordered box with some padding around its content.
**Notes:**
* Cards can have a header, body, and footer.
* They come in various colors and can align content in various ways.
* A simple card uses the `.card` and `.card-body` classes.
#### Basic Card
**Syntax:**
```html
1. <div class="card">
2. <div class="card-body">Basic card</div>
3. </div>
```
#### Header and Footer in Cards
**Notes:** Used the `.card-header` and `.card-footer` classes.
**Syntax:**
```html
1. <div class="card">
2. <div class="card-header">Header</div>
3. <div class="card-body">Basic card</div>
4. <div class= "card-footer">Footer</div>
5. </div>
```
#### Contextual Cards
**Notes:**
* Background color can be added using contextual classes like: `.bg-primary`, `.bg-success`, `.bg-danger`, etc.
* To ensure text visibility on dark backgrounds, use `.text-white` alongside the background class.
#### Card Title
**Notes:** A title can be added using the `.card-title` class on any heading in the card.
#### Cards with images
**Notes:** Images can be added using `.card-img-top`, `.card-img-bottom`, or `.card-img-overlay` applied to an `<img>` tag.
#### Grouping of cards (Bootstrap 5)
**Notes:**
* In Bootstrap 5, grid property `.row-cols` classes are used for grouping cards.
#### Card-deck class (Bootstrap 4)
**Notes:**
* **Context:** Used in Bootstrap 4.
* **Purpose:** Create a grid of cards that are of equal height and width.
* **Class:** `.card-deck`.

### UI Components
**Definition:** UI (User Interface) components are those components using which a user interacts with a webpage.
**Notes:**
* HTML pages may have several UI components such as input fields, select menus, text areas, buttons, etc.
* While these elements can be styled using HTML itself, this may not be visually appealing.
* Bootstrap provides a wide range of predefined classes for styling UI components.
#### .form-control Class
**Notes:**
* The class `.form-control` can be used for form elements like `<input>`, `<textarea>`, `<select>`.
* Elements with the class `.form-control` are set to `width: 100%` of the parent element (`<div>`).
* **Note:** Generally for `<input type="button/reset/submit">`, `.form-control` is not used.
#### Radio Buttons
**Notes:**
* Bootstrap provides classes like `.form-check` to style radio buttons and checkboxes.
* The `type` attribute of `<input>` tag specifies the creation of the radio button.
* The default alignment using `.form-check` creates vertically aligned radio buttons.
* The class `.form-check-inline` creates horizontal alignment for radio buttons.
#### Button - Style Variants
**Definition:** Bootstrap provides many classes for styling and sizing the buttons.
**Notes:**
* To provide styling to buttons, the base class `.btn` should be used with `<button>` elements or `<input type="button/reset/submit">`.
* Style variants include: Standard Button (base `.btn`), `.btn-default`, `.btn-primary`, `.btn-success`, `.btn-info`, `.btn-warning`, `.btn-danger`, `.btn-link`.
#### Button - Size Variants
**Notes:**
* Size variants are created using `.btn-lg` (Large) and `.btn-sm` (Small).
* The medium button uses the default `.btn` class.
#### Button - Block Level
**Notes:**
* To create a block level button (width of button equals width of parent element), the `.d-grid` class should be used on the parent element.
**Syntax:**
```html
1. <div class="d-grid gap-2">
2. <button class="btn btn-secondary" type="button">...</button>
3. </div>
```
#### Badges
**Definition:** Badges are indicators for numerical values and are generally used to show how many items are there in association with a particular list/link.
**Notes:**
* Badges can be added inside a button, hyperlink, and list elements.
#### Form Group
**Definition:** Used to have a consistent look and feel and optimum spacing between the form elements across various resolutions.
**Notes:**
* Every `<label>` and its corresponding form element should be wrapped in a `<div>` having `.form-group`.
* Every form input element (except button) should have class `.form-control`.
* Every form label element (except button) should have class `.form-label`.
#### Use of form-floating class
**Definition:** Used to make the label float over the input field, enabling Floating Labels.
**Notes:**
* Wrap a pair of input and label elements within a container using the `.form-floating` class.
**Syntax:**
```html
1. <div class="form-floating mb-3">
2. <input type="email" class="form-control" placeholder="name@example.com" />
3. <label>Email address</label>
4. </div>
```

### Form Layouts
**Definition:** Bootstrap simplifies the process of aligning form elements (labels, input fields, buttons, etc.) by providing two types of form layouts.
*   Vertical Form Layout
*   Inline Form Layout
#### Vertical Form Layout
**Notes:**
* Bootstrap provides a vertical layout to the forms by default (no separate Bootstrap class is needed, as the `<form>` element selector has been modified in `bootstrap.css`).
* Labels and corresponding form elements will be left aligned and stacked one below the other.
#### Inline Form Layout
**Purpose:** To align all the form elements and their labels in a single row.
**Notes:**
* Grid utilities are used to achieve this implementation (`.row row-cols-lg-auto g-3 align-items-center`).
**Syntax:**
```html
<form class="row row-cols-lg-auto g-3 align-items-center">
...
</form>
```

### Navigation Bar
**Definition:** A navigation bar (`navbar`) is a section intended to aid users in accessing different webpages of a website.
**Notes:**
* HTML5 provides the `<nav>` element to create a navigation bar.
* Bootstrap has different classes for better appearance.
* A responsive navbar collapses when viewed on smaller screens, and expands otherwise (this requires `bootstrap.css` and `bootstrap.bundle.js`).
#### Navbar Skeleton (Components)
**Notes:**
1. **Brand or logo:** Positioned in the top left corner, unaffected by resizing.
2. **Links:** Visible on large/medium screens. On small screens, links are placed inside the collapsible drawer.
3. **Navbar toggler button:** Used to expand or minimize the drawer on small screens.
#### Navbar Brand and Toggle Button (Classes)
**Notes:**
* Use the `.navbar-brand` class with the `<a>` tag to add a brand.
* Use the `.navbar-toggler` class with a `<button>` to create a collapsible navbar.
* `data-bs-target="#nav-collapse"`: Points to the `div` which contains the links (must have `id="nav-collapse"`).
* `data-bs-toggle="collapse"`: Tells Bootstrap to switch between visual states (collapsing when the user clicks the button).
#### Navbar Links
**Notes:**
* `.navbar-nav`: By default, aligns links on the left side and keeps them all on one line.
* `.active` or `.disabled`: Added to the `<a>` tag to make a link appear pressed or unavailable.
* `id="nav-collapse"`: Identifier for the div containing all links, used by the toggler button.
* `.collapse` and `.navbar-collapse`: Give the appropriate styling when collapsed.
#### Navbar Dark Explained (Colors)
**Notes:**
* Adding `.bg-color` classes (e.g., `.bg-primary`, `.bg-dark`) to the `<nav>` tag changes the navbar color.
* `.navbar-dark`: Makes all text white colored.
* `.navbar-light`: Makes all text black colored.
#### Navbar Links Alignment
**Purpose:** To push links to the right corner of the navbar.
**Notes:**
* `.ms-auto` is a margin utility class that sets the left-margin to auto, pushing elements to the right.
**Syntax:**
```html
1. <ul class="navbar-nav ms-auto">
2. <li class="nav-item"> <a class="nav-link" href="#">Profile</a></li>
3. <li class="nav-item"> <a class="nav-link" href="#">Logout</a></li>
4. </ul>
```

### Modal
**Definition:** It is a dialog box/popup window.
**Notes:**
* Modals are achieved using HTML, CSS, and JavaScript Plugins / Popper.
* They are displayed on top of the current page.
* Bootstrap supports only one modal window in the given time.
* The position property can be any, but by default, the position is fixed.
*   Outer container: `.modal`
*   Inner elements: `.modal-dialog`, `.modal-content` (wraps header, body, footer).
**Syntax:**
```html
1. <div class="modal" tabindex="-1">
2. <div id="modaldialog" class="modal-dialog">
3. <div id="modalcontent" class="modal-content">
4. <div id="modalheader" class="modal-header">
5. <h5 id="modaltitle" class="modal-title">Modal title</h5>
6. </div>
7. <div id="modalbody" class="modal-body">
8. <p>Modal body message</p>
9. </div>
10. <div class="modal-footer">
11. <button type="button" class="btn btn-secondary"
12. data-bs-dismiss "modal">Go back</button>
13. </div>
14. </div>
15. </div>
16. </div>
```

### Responsive Design - Patterns
**Notes:**
* The principle in designing responsive pages is **"Mobile First"**. The developer should first decide on the layout for the smallest screen and then keep adding items for larger screens.
#### Layout Patterns
##### Mostly Fluid
**Notes:**
* The layout is kept almost the same for most of the device sizes.
* The smallest device size has a single column structure.
* Easier to implement as it has only a single break point.
##### Drop Column
**Notes:**
* The columns are dropped as the device size reduces.
* This would need multiple break points.
##### Layout-Shifter
**Notes:**
* The layout drastically changes from one device to the other.
* Slightly difficult to implement than the other two patterns.
#### Responsive Design - Navigation patterns
**Notes:**
* When designing a page, content comes before navigation. Navigational links should not block the main content.
##### Do Nothing
**Notes:**
* Displays the same navigational set in all devices.
* Applicable only when navigation is simple with few links or options (not suited if there are submenus).
##### Select
**Notes:**
* Menu items are kept as a drop down, reducing the space occupied by the navigation bar.
##### Hamburger Menu
**Notes:**(content not found in source)
#### Responsive Design - Image
**Notes:**
* **Fluid Images:** Image keeps resizing as screen size reduces. However, this is not performance friendly as the same larger image resolution is loaded and then resized.
* **Load Different Resolutions:** A larger screen gets an image with larger resolution, and a smaller screen gets a smaller one, achieved via the `<source>` tag and `srcset` attribute.
* **Art Direction:** Loads different images or different cropped versions of the same image based on device size. This ensures the main element stays in focus when background detail is cropped on smaller screens.
**Syntax:**
(Loading different resolutions example)
```html
1. <source media="(max-width: 480px)" srcset="infy_small.jpg">
2. <source media="(max-width: 640px)" srcset="infy_medium.jpg">
```

### CSS Grid
**Definition:** CSS Grid is the latest way to create layouts. It allows creating rows and columns, and spanning them using grid line numbers.
**Attributes:**
| Property | Description |
| :--- | :--- |
| `display: grid` | Creates a grid system. Typically applied to a container element within which all the content is placed. |
| `grid-template-columns: 1fr 1fr` | Allows creating a template for columns in all rows. Example creates two columns which occupy one fraction (`fr`) each of the available space. |
| `grid-column: 3/5` | Allows spanning a column across grid lines. Example spans the column from grid line 3 to 5. |
| `grid-gap: 5px` | Allows applying a gap between all rows and columns. Example creates a gap of 5 px. |
#### Creating Grid Lines Using CSS Grid
**Notes:**
* **Note on 'fr':** 'fr' is a measurement unit called fraction. 1fr means occupying one fraction of the available space.
* **Creating rows:** Every element which is directly a child of the main-layout class becomes an item in the grid, occupying one column. Rows are created automatically, but their size can be controlled using CSS.
* **Spanning columns:** Done using the `grid-column` property (e.g., `grid-column: 1/5` spans from 1st to 5th grid line, covering 4 columns).
* **Spanning rows:** Done using the `grid-row` property (e.g., `grid-row: 3/5` spans 2 rows).
#### CSS Grid Compatibility
**Notes:**
* CSS Grid (as of June 2023) is fully supported by Edge 16 onwards and all the latest versions of other browsers.
* Edge 15 and below, and IE 10 and IE 11 follow an older specification of CSS Grid, requiring rewriting CSS and HTML.
* Older browsers do not support the `grid-gap` property.
**Attributes:**
| Supported Browsers | IE 11 (Older Specification) |
| :--- | :--- |
| `display: grid` | `display: -ms-grid;` |
| `grid-column: 1/3` | `-ms-grid-column: 1; -ms-grid-row: 1; -ms-grid-column-span: 2;` |
#### CSS Grid vs Bootstrap
**Notes:**
* **Columns:** Bootstrap restricts developers to 12 columns; CSS Grid allows any number of columns.
* **Structure Modification:** Changing layout in Bootstrap requires modifying the semantic structure of HTML; in CSS Grid, layout can be changed without modifying the HTML structure.
* **Offsets/Classes:** CSS Grid avoids additional classes and offsets.
* **Height:** In Bootstrap, columns with different content end up with different heights (requires separate fixing); in CSS Grid, all columns in a row will be of the same height.
#### CSS Grid vs Flex
**Notes:**
* **Dimensions:** Flex is one dimensional (row or column); CSS Grid allows creating a 2D structure.
* **Wrapping:** Because of Flex wrap, an element spans across multiple columns by default to fill space; in CSS Grid, each element by default occupies only one column.
* **Purpose:** Flex is primarily meant to distribute content evenly; CSS Grid allows defining width for each column.
* **Bootstrap:** In Bootstrap 4, flex is used internally for creating layouts.

### Jumbotron (Resource from Bootstrap 4)
**Definition:** The bootstrap jumbotron is used to enclose content in a big grey box. It calls out for extra attention to specific contents in a page.
**Notes:**
* A jumbotron can contain any valid HTML element including other bootstrap elements like containers, tables, etc.
* The content inside the jumbotron can be styled using other bootstrap classes.
**Syntax:**
```html
1. <div class="jumbotron">
2. <h1>Jumbotron</h1>
3. <p>I am inside the Jumbotron</p>
4. </div>
```

### Course Summary
**Notes:**
In this course, you have learned how to:
* Design the layout of a webpage using container, row and column classes of Bootstrap.
* Develop webpages that can be viewed on various devices using a grid system of Bootstrap.
* Apply typography classes in order to achieve the desired look and feel for a given text.
* Organize data into tables using Bootstrap table classes.
* Make the images responsive using Bootstrap image classes.
* Use UI components in order to create interactive web pages.
* Build applications which facilitate easy navigation using the navigation bar.
* Design forms using different layouts for a webpage.

<CoverageCheck>
- Total topics extracted: 26 (with multiple subtopics totaling over 50 sections)
- Any missing or unclear sections: "Hamburger Menu" definition/details were mentioned as a title but the body content was missing in the source OCR.
- Approx. compression ratio vs original text: Moderate (Detailed reproduction of tables and code snippets prevented high compression).
- Warnings (if text seemed incomplete): The text occasionally referenced Bootstrap 4 concepts (like `.card-deck` and `.jumbotron`) alongside Bootstrap 5 concepts, which has been maintained in the notes as per the source material.
</CoverageCheck>
