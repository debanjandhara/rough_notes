## Technical Reference Notes: CSS Concepts

### CSS Selectors and Types

#### CSS Selectors and Types
**Definition:** A Selector is a pattern that can select multiple HTML elements using the HTML element attributes like class, id, and type, etc.. Once the elements are selected, we can apply the style to all the selected elements.

**Syntax:** `Selector { property: value }`

**Notes:**
* We use selectors to specifically select HTML elements according to the requirement and style them.

#### Types of Selectors

##### 1. Type Selector (Element selector)
**Definition:** Selects all the HTML elements that match the tag/node name. Also known as Element selector.

**Syntax:** `Tag_Name{property: value}`

**Examples:**
* CSS: `p {color: green}`

**Notes:**
* The styling applies to all matching elements, even if they are nested inside other tags (e.g., a `<p>` inside a `<div>`).

##### 2. Id Selector
**Definition:** Used for the case where we must specifically select a single element and style it.

**Syntax:** `#Id_Value { property: value; }`

**Examples:**
* HTML: `<p id="backgrdOrange">...</p>`
* CSS: `#backgrdOrange { background-color: orange; }`

**Notes:**
* `#` indicates Id selector.
* Id attribute's value should be unique because we use Id selector to style only a specific element.

##### 3. Class Selector
**Definition:** Used for cases where you must apply the styling to multiple elements.

**Syntax:** `.Class_Name { property: value; }`

**Examples:**
* HTML: `<tr class="setGray">`
* CSS: `.setGray{ background-color: gray }`

**Notes:**
* To use class selectors, we must provide an attribute named `class` to all elements intended for styling.
* `.` represents it is a class selector.
* `.setGray` selects all elements with `class="setGray"`.

**CommonMistakes:**
* ⚠️ Using a unique ID selector for multiple elements leads to increased code size, difficulty in maintenance, and decreased readability.

##### 4. Universal Selector
**Definition:** Selects all the HTML elements on the webpage. It is generally used when you need to apply the same style for all the elements of the webpage.

**Syntax:** `*{property: value}`

**Examples:**
* CSS: `*{ font-family: cursive; }`

##### 5. Attribute Selector
**Definition:** Selects the HTML elements if the attribute and its values of the HTML element match the selector.
*Types of attribute selectors:*
* **a) [attribute]**
    **Definition:** Selects all the HTML elements which have the attribute.
    **Example:** `p[id] { color: orange; }`
* **b) [attribute=keyword]**
    **Definition:** Selects all the HTML elements which have the attribute and its value should match the keyword.
    **Example:** `p[id="pId"] { color: orange; }`
* **c) [attribute \*= keyword]**
    **Definition:** Selects all the HTML elements which has the attribute and its value containing the keyword.
    **Example:** `[href\*="sparsh"] {/*Styling properties*/} selects <a href="https://sparsh.com">Sparsh</a>`
* **d) [attribute^=keyword]**
    **Definition:** Selects all the HTML elements which has the attribute and the keyword is at the beginning of the value.
    **Example:** `[name^= "happy"] {/*Styling properties*/} selects <div name="happyFace">Hello World</div>`
* **e) [attribute $= keyword]**
    **Definition:** Selects all the HTML elements which has the attribute and the keyword is at the end of the value.
    **Example:** `[href$="com"] {/*Styling properties*/} selects <a href="https://icompass.com">Compass</a>`

#### Combinators
**Definition:** Selectors formed by combining multiple selectors and establishing a relationship between them using symbols: `>`, `+`, `~`, or space (` `). Used for selecting a specific element/node to style them.

**Syntax:** `Selector1 (>, +, ~, (space)) Selector2`

**Notes:**
* Types of Combinators: 1. Descendant Combinator, 2. Child Combinator, 3. Adjacent Sibling Combinator, 4. General Sibling Combinator.

##### 1. Descendant Combinator
**Definition:** Selects the second element which is a descendant (child/grandchild etc.) of the first element. It is represented by a space (` `).

**Syntax:** `Selector1 Selector2 {/* styling properties*/}`

**Examples:**
* CSS: `#firstDiv .p1{ font-style: italic; background-color: orange; }`

##### 2. Child Combinator
**Definition:** Selects the second element which is a direct child of the first element. It is represented by `>`.

**Syntax:** `Selector1 > Selector2 {/* styling properties*/}`

**Examples:**
* CSS: `ol>li { border-top: 3px solid aqua; }`

**Notes:**
* The style is applied only on the `<li>` tags which are a direct child of `<ol>` tags, and not for the `<li>` tags inside the `<ul>` tag.

##### 3. Adjacent Sibling Combinator
**Definition:** Selects the second element which is adjacent (i.e. right next to) to the first element and both having the same parent. It is represented by `+`.

**Syntax:** `Selector1 + Selector2 {/* styling properties*/}`

**Notes:**
* Used to style only the paragraph that is next to the heading.

##### 4. General Sibling Combinator
**Definition:** Selects all the elements that match the second selector and are siblings to the first element. It is represented by `~`.

**Syntax:** `Selector1 ~ Selector2 {/* styling properties*/}`

**Notes:**
* Used to style all paragraphs that are siblings to the heading.

#### Precedence of Selectors
**Mechanism:** When multiple selectors select the same element and have common CSS properties, CSS gives priority to the selector which is more specific. The most specific selector styling is applied.

**Precedence Order:** Id > Class > Type

### CSS Syntax & Properties

#### CSS Syntax
**Definition:** The CSS syntax (rule set) consists of two important parts: selectors and a declaration block.

**Syntax (Rule Set):**
```css
selectors {
css-property: value;
}
```

**Notes:**
* The code inside the curly braces is known as CSS declaration block. Selectors refer to the HTML element that requires styling.

#### CSS Declarations
**Definition:** The declaration block consists of one or more stylings separated by semicolon. A key and value pair together is called a declaration. Each declaration consists of CSS property name and a value, separated by a colon. All declarations are wrapped inside curly braces and together it is known as CSS declarations box.

#### CSS Properties (Commonly Used)
| Properties | Values | Description | Example |
| :--- | :--- | :--- | :--- |
| **color** | \#RRGGBB (Red, Green, Blue hex values) | Used to apply colors for the text. Can take hex values or rgb values | `h1 { color: #FF00FF }` |
| **text-align** | left \| right \| center \| justify | Used to align the inner text of a block element | `p { text-align: center; }` |
| **text-decoration**| none \| underline \| overline \| line-through \| blink \| inherit | Used to add decoration to the text | `h1 { text-decoration: overline; }` |
| **font-size** | px or em value | Used to set the size of a font | `h1 { font-size: 15px; }` |
| **font-style** | normal \| italic \| oblique \| initial \| inherit | Used to specify the font style for the text | `h1 { font-style: italic; }` |
| **background-color** | color \| transparent \| initial \| inherit | Used to set the background color for the element | `h1 { background-color: red; }` |
| **background-image** | url \| none \| initial \| inherit | Used to set background image for an element | `h1 { background-image: url("imagename.jpg"); }` |
| **border** | Border-width border-style border-color \| initial \| inherit | Used to specify the style of an element's border | `h1 { border: 5px solid red; }` |
| **border-radius**| Border-width border-style border-color \| initial \| inherit | Used to add rounded borders to an element | `h1 { border-radius: 5px; }` |
| **overflow** | scroll \| hidden \| auto \| visible \| initial \| inherit | Used to specify what should happen if content overflows an element's box | `div { overflow: auto; }` |
| **display** | none \| inline \| block \| [inline-block etc.](content not found in source) | Used to specify the display behavior of an element | `p { display: inline; }` |
| **opacity** | number \| initial \| inherit | Used to set the opacity level for an element | `div { opacity: 0.5; }` |

**Notes:**
* Comma (`,`) is used to group multiple selectors.

### Adding CSS to HTML

#### Adding CSS to HTML
**Types:** 1. Inline CSS, 2. Embedded CSS, 3. External CSS.

##### 1. Inline CSS
**Definition:** The CSS is directly written in the HTML element, inside the `style` attribute.

**Syntax:** `<element style="property1:value1; property2:value2">Content</element>`

**Notes:**
* Used only when styling must be applied to only that HTML element and the CSS is not going to be repeated anywhere.
* Increases page loading time and makes maintenance difficult.

##### 2. Embedded CSS
**Definition:** The CSS is added to the HTML in the `style` tag of the head section.

**Notes:**
* Applies styling only to that HTML page where it is written.
* If the same styling must be applied to another page, it has to be written again.

##### 3. External CSS
**Definition:** The CSS is written in another file (`<<file_name>>.css`) and linked to HTML through a `link` tag.

**Syntax (Linking):** `<link rel="stylesheet" href="Path of the CSS file">`

**Notes:**
* This method is the best when you must apply the same styling to multiple HTML files.

#### Inheritance
**Definition:** Inheritance is a mechanism where the styling properties of the parent will be passed down to the children.

**Notes:**
* Saves repetitive tasks of specifying the same style for parents and children.
* Not all properties will be inherited by the children (e.g., `background-image` applied to `<body>` is not inherited by child elements).

### CSS Box Model & Layout

#### CSS Box Model
**Definition:** An invisible box which wraps around every HTML element. HTML elements are considered as boxes.

**Properties:** margins, borders, padding, actual content.

**Notes:**
* **Components:**
    1.  **Content:** The innermost box; actual data/text/image displayed.
    2.  **Padding:** Immediate box enclosing content. Provides space between border and content. Transparent.
    3.  **Border:** Visible box enclosing content and padding. Dimensions can be modified, and border can be styled (colored dotted/continuous line/etc.).
    4.  **Margin:** Transparent box outside the border. Used to display content and avoid content overlapping.

#### Height and Width of an Element
**Definition:** Used to specify the dimensions of the content area inside the box.

**Notes:**
* **Observation:** The total width/height of the box includes content size, padding, margin, and border.

* **Calculation:** Total Width = (width + padding L + padding R + margin L + margin R + border L + border R)

#### Margins by browser
**Problem:** Browsers provide default margins that interfere even when margins are explicitly set to 0.

**Solution:** Use the universal selector (`*`) to explicitly set all margins to 0.

#### Multiple values to margins and padding (Shorthand)

**Notes:**
* **Four values:** Applied in clockwise order: top, right, bottom, and left.

* **Two values:** 1st value applies to top-bottom pair; 2nd value applies to right-left pair.

* **Three values:** 1st value applies to top; 2nd applies to right-left pair; 3rd applies to bottom.

#### Box-Sizing
**Definition:** Defines how the height and the width of an element is to be calculated, whether to include the paddings and borders or not.

**Types:**
* **1. Content-box (default):** Does not include borders and padding in the specified size.
* **2. Border-box:** Includes border and padding in the specified size.

**Notes:**
* Setting `box-sizing: border-box;` ensures the total width/height remains fixed to the dimension specified, accommodating borders and padding within that size.

#### Overflow
**Definition:** Controls what happens to content when it is too big to fit into an area. Specifies whether to clip the contents or to add scroll bars.

**Values:**
* **1. hidden:** Overflow is clipped; rest of content is hidden.
* **2. visible (default):** Overflowing content is rendered outside the box.
* **3. scroll:** Overflow is clipped, but a scrollbar is added to scroll inside the box.
* **4. auto:** Like scroll, but adds scrollbars only when necessary.
* **5. Overflow-x / Overflow-y:** Used to control horizontal (`-x`) or vertical (`-y`) overflow respectively. Values remain `visible, hidden, scroll, auto`.

### CSS Positioning

#### CSS Positioning
**Definition:** The CSS Position property sets how an element is positioned in a webpage.

**Properties:** Top, Bottom, Left, Right. Used to decide the exact location of an element.

**Notes:**
* Types of Position: 1. Static, 2. Absolute, 3. Relative, 4. Fixed, 5. Sticky.

##### 1. Static
**Definition:** Default position for all HTML elements. Not affected by `top, right, bottom, left` properties. Elements move up when the page scrolls.

**Notes:**
* Explicitly setting position to `static` and providing positional values results in no change.

##### 2. Relative
**Definition:** Element's original position remains in the flow of the document. `top, right, bottom, left` and `z-index` properties will work. Element is positioned relative to its original position.

**Notes:**
* Positional adjustments (e.g., `top: 20px`) calculate spacing from the element's original position. Relative positioning does not affect the position of other elements.

##### 3. Absolute
**Definition:** Positions elements against the containing element (parent element).

**Notes:**
* The element is removed from the flow of the document.
* It is positioned relative to its closest positioned ancestor (if any, and not static), otherwise, it is placed relative to the browser.
* Its ultimate position is determined by `top/right/bottom/left` values.

##### 4. Fixed
**Definition:** The element is removed from the flow of the document. It sticks onto the browser window and will not move even if the page scrolls.

**Notes:**
* Fixed elements affect the positioning of subsequent elements, as if the fixed element were never there in the first place.

##### 5. Sticky
**Definition:** A combination of Static and Fixed. Initially behaves as Static, but as soon as it reaches the top/bottom of the screen when scrolling, it becomes fixed there.

### Transformations, Transitions, and Animations

#### Transformations
**Definition:** An effect that lets an element change its shape, size, and position using the `transform` CSS property (move, tilt, scale).

**Functions:** 1. Translate, 2. Scale, 3. Rotate.

##### 1. Translate
**Definition:** Moves an element in the horizontal, vertical direction and sideways.

**Syntax:** `transform: translate(x, y)`

**Parameters:**
* `x`: moves right by x value (from current position). Negative values move left.
* `y`: moves down by y value (from current position). Negative values move up.

**Notes:**
* `translateX()` and `translateY()` functions move the element in one direction (horizontal or vertical).

##### 2. Scale
**Definition:** Resizes an element (shrinks or expands).

**Syntax:**
* `transform: scale(x)` -> scales height and width by x-value.
* `transform: scale(x,y)` -> scales element width (x-value) and height (y value).

##### 3. Rotate
**Definition:** Rotates an element around a fixed point in the clockwise direction.

**Syntax:** `transform: rotateY(120deg)` or `transform: rotateY(2turn)`

**Notes:**
* `rotateX()`, `rotateY()` functions rotate the element in x and y direction respectively.

#### Transitions
**Definition:** Allows changing CSS property values over a given duration in a smooth manner (not immediately).

**Requirements to create a transition effect:** Specify the CSS property to affect and the duration of the effect.

##### CSS Transitions properties
| Transition sub-property | Description |
| :--- | :--- |
| **transition-property** | The CSS property which needs to be transited over a period (e.g., height, width, background color, etc.). Accepts a comma-separated list or `all`. |
| **transition-duration** | Sets the length of time that a transition should take. If omitted, the transition will not have any effect. |
| **transition-delay** | Sets the delay between the interaction and the beginning of the transition sequence. |
| **transition-timing-function** | Controls the pace/speed of the transition. Possible values: linear, ease-in, ease-out, ease, etc. |
| **transition** | Shorthand property for the other four properties. Example: `transition: width 2s linear 1s;` |

#### Animations
**Definition:** CSS3 Animations replace animated images, scripts, and flash animations. Done using key-frames.

**@keyframes rule:** Defines the set of keyframes making up an animation sequence. Controls the intermediate steps.

**Defining Keyframes:** Define styles for the start and end using `from`/`to` keywords or percentage values (0% for start, 100% for complete).

##### Animation sub-properties
| Animation sub-property | Description |
| :--- | :--- |
| **animation-name** | Specifies the name of the `@keyframes` at-rule. |
| **animation-duration** | Sets the length of time that animation should take to complete one cycle. |
| **animation-delay** | Sets the delay between the time the element is interacted with and the beginning of the animation sequence. |
| **animation-timing-function**| Controls the pace/speed of the animation. Possible values: linear, ease-in, ease-out, ease, etc. |
| **animation-iteration-count**| Sets the number of times the animation should repeat (use `infinite` to repeat indefinitely). |
| **animation** | Shorthand property for all other four properties. Example: `animation: name duration timing-function delay iteration-count direction;` |

**Best Practice:**
* Favor CSS Animations over JavaScript animations as the browser's rendering engine can optimize CSS animations more efficiently (e.g., frame skipping).

### CSS RWD and Media Queries

#### What is Responsive Web Design? (RWD)
**Definition:** An approach of designing web applications to make them render well on devices with different sizes.

**Mechanism:** Screen elements and contents automatically change size and reshuffle positions according to the available screen size.

#### The Viewport
**Definition:** The user's visible area of the web page. Varies based on screen size.

**Setting the viewport:** Include the following meta tag for responsiveness:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Notes:**
* `width` can be set to a specific pixel value or `device-width`. `initial-scale` is the initial zoom level.

#### Media Queries
**Definition:** Used to specify how the web page should look on different screen sizes.

**Mechanism:** Use the `@media` rule to apply styles based on media type or media features of the device. Helps adjust position, button size, font size, margins, and paddings for smaller screens.

**Syntax:**
```css
@media not only mediatype and (expressions){
css-code
}
```

**Components:**
* **media type:** Screen type being rendered. (Values: `All`, `Print`, `Screen`, `Speech`).
* **expressions:** Specifications like `min-height`, `max-width`, `max-resolution`, etc. Must resolve to true or false.
* **Operators:** `not` or `only` (optional). `not` negates the query; `only` prevents old browsers from applying the style.
* **CSS Code:** Styling applied if the query is true and media type matches.

**Notes:**
* Can target devices using `min-width` or `orientation` (portrait/landscape).
* When using multiple queries, default styles apply to all devices, and specific styles apply only when max-width/min-width criteria are met.
* **Media query in external CSS (Best Practice):** Use separate stylesheets for different media queries and link them using the `media` attribute in the HTML `<link>` tag.

### CSS Units

#### Units in CSS
**Classification:** 1. Absolute Units, 2. Relative Units.

##### 1. Absolute Units
**Definition:** Units that do not depend on the viewport. They remain the same in all screen dimensions.

**Units:** Centimeter (Cm), Inch (In), Millimeter (Mm), **Pixel (Px)**.

**Notes:**
* Pixels are the most widely used due to crystal-clear control and accuracy on a computer screen.

##### 2. Relative Units
**Definition:** Units that depend on the viewport size or properties of the parent element. They change size relatively with respect to changes in other elements.

**Units:** percent, vw/vh, em, rem.

###### Relative Units - percent (%)
**Definition:** Styles the element in terms of percentage of the viewport size.

**Notes (No Parent):**
* Percentage is relative to the viewport size.

**Notes (With Parent):**
* Percentage value is based on the parent element's attribute (e.g., width 50% of parent's width).

###### Relative Units - VW and VH Units
**Definition:** Provide dimension for elements relative to the width (`vw`) and height (`vh`) of the viewport.

**Notes:**
* `vw` and `vh` DO NOT consider padding and margins while computing width/height relative to the viewport size, whereas percentage units DO consider padding and margins.

###### Relative Units - EM Units
**Definition:** Styles the element relative to the font-size of the **parent element** (for typographical properties). Else, relative to its font-size (for other properties).

**Notes:**
* Font size changes relatively with the parent element's font-size. When nesting elements, the size keeps multiplying (e.g., 2em inside 1.5em parent results in 3 times the original font size).

###### Relative Units - REM Units
**Definition:** Styles the element relative to the font-size of the **root element** (`<html>`). Works otherwise like `em` units.

**Notes:**
* Font size is obtained from the root element, not the parent element. This prevents the size from multiplying when nesting elements.

#### CSS Calc() Function
**Definition:** Used in CSS to perform simple mathematical calculations while specifying values for CSS properties (length, percentage, number, etc.).

**Usage:** Served as the value for a suitable CSS property that supports numbers.

**Example:** `width: calc(20px + 30px)`

**Notes:**
* Supports mixing of units (e.g., percent + pixel).
* When using `*`, at least one argument should be a number (E.g., `100px*2`).
* When using `/`, the divider should be a number (E.g., `150vh/5`).
* Will not work properly with media queries.
* **Scenarios for use:** Creating simple and responsive grids, positioning elements at a particular part of the webpage, centering elements if they are positioned absolute.

### Flexbox Item Properties

#### Step 1 - Ordering the flex elements
**Properties of flex elements:** `order`, `flex-basis`, `flex-grow`, `flex-shrink`.

**order property:** Changes the order of rendering flex elements. Takes a number value.

**Notes:**
* When `order` is used, it is mandatory to provide the `order` property for all flex items; otherwise, it will not work as expected.

#### Step 2 - flex-basis property for a flex item
**Definition:** Defines the customized size for a flex item.

**Observation:** If content exceeds the set `flex-basis`, the content wraps to the next line.

**Direction Dependency:** If `flex-direction` is `row`, `flex-basis` controls the **width**. If `flex-direction` is `column`, `flex-basis` controls the **height**.

#### Step 3 - flex-grow property for a flex item
**Definition:** Defines the expansion rate of a flex item in the remaining or available space.

**Notes:**
* `flex-grow` increases the size along the main axis. This differs from `flex-basis`, which fixes the size.

#### Step 4 - flex-shrink property for a flex item
**Definition:** Used to shrink a flex item when its size is larger than the flex container, accommodating all items within the container.

**Scenario:** This situation occurs only when flex-item size is greater than the flex-container AND `flex-shrink` property is set to 0.

**Solution:** Use a positive value (not 0) for `flex-shrink` to overcome scenarios where items spill out of the container.

**Notes:**
* Once the element reaches maximum shrinkage, increasing the value beyond that point (e.g., beyond 4) gives the same output.

#### Shorthand properties for a Flexbox
* **1. flex-flow:**
    
    **Definition:** Combination of `flex-direction` and `flex-wrap`.
    
    **Example:** `flex-flow: row wrap`
    
    **Default:** `row` and `nowrap`.
* **2. flex:**

    **Definition:** Combination of `flex-basis`, `flex-grow`, and `flex-shrink`.
    
    **Example:** `flex: 2 1 100px` (`flex-grow` 2, `flex-shrink` 1, `flex-basis` 100px).

### Flexbox Container Properties

#### Introduction to Flexbox
**Definition:** A widely used CSS property to align elements within the available HTML space.

**Characteristics:** One-dimensional layout structure. Dynamically aligns items by maintaining proper spaces. Supports expansion and shrinkage.

#### Flex Container and its Properties
**Definition:** The container within which flex elements are aligned. It alters the elements within, but not other elements.

**Properties:** `display`, `flex-direction`, `flex-wrap`.

#### Step 1 - Creating flex Container
**Mechanism:** Must be created using the `display` property.

**`display` property values:**
* **1. flex:** Container spreads over the whole page (block level element).
* **2. inline-flex:** Container spreads until all elements are covered (inline element).
* **3. block:** Behaves like a block level element.
* **4. inline-block:** Container tries to fit all block-level elements in one line.

#### Step 2 - Providing direction to the flex container
**Axes:** Main-axis and cross-axis.

**Property:** `flex-direction`.

**Values:**
* **1. row (default):** Items aligned horizontally (A, B, C). Main-axis: horizontal; Cross-axis: vertical.
* **2. row-reverse:** Items aligned horizontally in reverse order (C, B, A).
* **3. column:** Items aligned vertically (A, B, C). Main-axis: vertical; Cross-axis: horizontal.
* **4. column-reverse:** Items aligned vertically in reverse order (C, B, A).

#### Step 3 - Wrapping the flex elements
**Property:** `flex-wrap`.

**Values:**
* **1. nowrap (default):** Wrapping is not applied; items remain on one line (shrinking if necessary).
* **2. wrap:** Wrapping applied; elements move to the next line once maximum screen width is reached.
* **3. wrap-reverse:** Wrapping applied in reverse order; elements start to arrange from bottom to top once maximum screen width is reached.

#### Properties of Flexbox (Alignment)
* **1. align-items:**
    
    **Definition:** Aligns flex items vertically (along the cross-axis).
    
    **Values:** `flex-start`, `flex-end`, `stretch` (content not found in source), `center`.

* **2. justify-content:**
    
    **Definition:** Aligns flex items horizontally (along the main-axis).
    
    **Values:** `flex-start`, `flex-end`, `stretch` (content not found in source), `center`.

### CSS Grid

#### CSS Grid
**Definition:** The latest method for creating layouts, allowing for 2D structure (rows and columns).

**Declaration:** Use `display: grid` on a container element.

#### Specifying Columns and Rows
**Properties:** `grid-template-rows` and `grid-template-columns`.

**Unit 'fr':** Fraction unit. `1fr` occupies one fraction of the available space.

#### Positioning Items (Spanning)
**Parameters:** `grid-row` and `grid-column`.

**Syntax (Spanning):** `grid-column: start / end`

**Mechanism:** Elements are positioned using grid line numbers.

#### Key properties of CSS Grid
| Property | Description |
| :--- | :--- |
| `display: grid` | Creates the grid system on the container element. |
| `grid-column-template: 1fr 1fr` | Creates a template for columns, occupying one fraction of available space each. |
| `grid-column: 3/5` | Spans a column across grid lines (from line 3 to 5). |
| `grid-gap: 5px` | Applies a gap between all rows and columns. |

#### CSS Grid vs Flex
**Dimensionality:** Flex is one dimensional; Grid is 2D.

**Element Space:** Flex wrap allows elements to span multiple columns to fill space. Grid elements occupy only one column by default.

**Width Definition:** In Flex, using explicit `width` values defeats the purpose of distribution. In Grid, we can define width for each column.

### CSS Variables (Custom Properties)

#### Variables in CSS
**Definition:** Custom properties used to change the appearance of the webpage, referred to as CSS variables.

**Benefit:** Simplifies maintenance and updates by modifying a value only once.

#### How to use Custom properties or the variables?
* **1. Declaring a variable:**
    
**Syntax:** Must start with `--` followed by the property name. E.g., `--text-color: brown;`
* **2. Using the declared variable:**
    
    **Function:** Used with the `var()` function. E.g., `color: var(--text-color);`
    
    **Scope (Selector):** When declared within a specific selector, the scope is restricted to that selector. If used outside, the styling is not applied.
    
    **Scope (Document):** Declaring the variable under the root element (`:root{...}`) makes the variable available for usage anywhere in the document.
    
    **`var()` parameters:** Takes two parameters. The first (declared variable) is mandatory. The second is optional, used as a fallback if the first parameter is invalid or unset.

**Notes:**
* CSS variables are case sensitive.

### Pseudo Classes and Elements

#### Pseudo-classes
**Definition:** A keyword added to a selector defining a special state of selected elements (e.g., focus, hover).

**Syntax:** `selector: pseudo-class { css-property: value; }`

##### Link and Input related Pseudo classes
| Pseudo-class | Description |
| :--- | :--- |
| `:link` | Styles links which are not visited. |
| `:visited` | Styles the state of the link when link is visited at least once. |
| `:hover` | Styles the state of the link when mouse is placed over the link. |
| `:active` | Styles the state of the link, when you can click on the link. |
| `:focus` | Styles the state of element that is currently targeted or activated by mouse. |
| `:enabled` | Styles the state of element that is enabled and associated with input field. |
| `:required` | Styles the input element with required attribute. |
| `:checked` | Styles the state of element when it is selected. |

**Notes:**
* `a:hover` styles must be defined after `a:link` and `a:visited` in the CSS style definition. Pseudo-classes can be used with HTML elements other than links/inputs.

#### Pseudo Elements
**Definition:** A keyword added to a selector to design a specific part of selected elements (e.g., placeholder, first line). Used to add content before/after text.

**Notation:** Denoted by double colons (`::`).

**Syntax:** `selector::pseudo-element{ property: value; }`
| Pseudo-element | Description |
| :--- | :--- |
| `::first-line` | Used to style first line of the text. |
| `::first-letter` | Styles the first letter of text (Applied only to block level elements). |
| `::before` | Used to insert content or style before the content of element. |
| `::after` | Used to insert content or style after the content of element. |
| `::selection` | Used to style the portion of element that is selected by the user. |

### Accessibility

#### Need for Accessibility
**Context:** Web pages must be accessible to users with visual disabilities (e.g., color blindness, permanent visual loss) who use screen reader tools.

**WCAG2.0 Luminosity Ratio:** 4.5:1 for normal text, 3:1 for large text.

#### Hiding Content
**Styles to avoid for hidden content accessed by screen readers:** `Display: none;` / `visibility: hidden;`. These remove content from the visual flow and skip screen readers.

**Accessible Method:** Absolutely positioning content off screen (`left: -10000px; height: 1px; width: 1px; overflow: hidden;`).

**Notes:**
* Links and form elements should not be hidden using this method as sighted keyboard users rely on focus indication.

#### Skip Links
**Definition:** Internal page links to navigate around repetitive content. Mainly used by screen reader users.

**Best Practice:** Skip links should be first in the source code, followed by main content, then navigation.

**Accessibility Enhancement:** Hide the link until the user tabs to it (`a:focus` pseudo class changes position from `absolute` off-screen to `static` on-screen).

#### Keyboard Accessibility
**Requirement:** Web page must be operable using just the keyboard.

**WCAG Guidelines:**
* **1. Obvious keyboard focus:** Redesign focus highlight if browser default blends with site background.
* **2. Make all interactive elements accessible:** Use `tabindex` to ensure access via keyboard (forms, buttons, etc.).
* **3. High contrast mode:** Improves usability for low vision/light sensitive users.

#### Hyperlinks
**Best Practices:**
* **1. Color of links:** Choose colors that identify the element as a link.
* **2. Visited links:** Change color of visited links using `a:visited`.
* **3. Hover:** Cursor must change visibly (e.g., to a hand).
* **4. Writing good links:** Use descriptive link text (e.g., "Find out more about CSS" instead of "Click here").
* **5. Link Titles:** Use `title` attribute for more information upon hover.

#### Abbreviations
**Mechanism:** Use the `<abbr>` element to provide the full form via the `title` attribute. The full form is displayed when hovering.

#### Images
**Requirement:** Use alternative text (`alt` attribute) on images.

**Reasons:**
* When content is not obvious, or when image fails to render (slow connectivity, `src` error), or for screen reader users.

#### Heading Tags
**Usage:** Use headings (`<h1>` to `<h6>`) to show document structure and relationships between sections. Do not use them purely for styling (Bold/Big text).

**Importance:** Crucial for screen reader navigation.

#### Time Element
**HTML Element:** `<time>`

**Definition:** Represents a machine-readable date and time.

**`datetime` attribute:** States a standardized version of time for assistive devices, avoiding human confusion.

#### Emphasized Texts
**Best Practice:** Use semantic markup (e.g., `<b>`, `<i>`) to properly announce style changes to all users.

### CSS Best Practices and Performance Optimization

#### CSS Best Practices and Performance Optimization
* **1. Make it readable:** Write CSS styling in multiple lines.
* **2. Comments:** Use multi-line comments (`/* ... */`) to organize CSS sections and save time locating changes.
* **3. Shorthand Properties:** Use shorthand (e.g., `margin: 10px 20px 30px 40px`) instead of long-form properties to save time and enhance readability.
* **4. Using px when it is not needed:** Omit `px` when the value is 0 (e.g., use `0` instead of `0px`).
* **5. Repetition of code:** Avoid repeating styles; combine selectors (`.class-name, another-class-name { ... }`).
* **6. Using Hex code instead of using Name 'Color':** Use hexadecimal color format (e.g., `#ff0000`) for consistency, variety, and performance, as color names may not be uniformly defined across browsers.
* **7. Appropriate Naming Convention:** Name classes/IDs based on their properties, not transient attributes (e.g., `.post-title` instead of `.title-red`).
* **8. Avoid Inline styling:** Inline styling is messy and difficult to understand.
* **9. Use External CSS:** Best practice for maintenance and page load speed.
* **10. Minify CSS:** Reduce file size (remove whitespaces, strip comments) before deployment to accelerate CSS stacking.
* **11. Cross Browser Compatibility:** Write vendor prefixes (e.g., `-webkit-`, `-moz-`) for CSS properties that need to run across different browser types/versions.
* **12. CSS Preprocessors:** Use scripting languages that extend CSS (e.g., SASS) to manage large projects.
* **14. Selectors Performance:** Browsers apply rules from right to left. Prioritize selectors for faster performance: ID > Class > Type > Adjacent sibling > Descendant > Universal > Attribute > Pseudo-classes/-elements.
* **15. Favor CSS Animations instead of JavaScript:** CSS animations are optimized by the browser rendering engine.
* **16. Using hyphens and underscores:** Use hyphens (`-`) for class names and underscores (`_`) for IDs.
* **17. Use a Reset:** Use CSS reset (or normalize) to eliminate browser inconsistencies (heights, margins, etc.).
* **18. Make use of Generic Classes:** Create generic classes (e.g., `.left { float: left}`) for frequently used styles and apply them to elements instead of repeating styles.

### Backward Compatibility and Polyfills

#### Backward Compatibility
**Definition:** Process of making content render similarly even in older browsers where certain properties are unsupported.

**Fixing Compatible Issues:** Achieved by using values that the older browser supports.

**Example:** Use `display: ms-flexbox` along with `display: flex` for IE9 compatibility.

#### Polyfills
**Definition:** Simple JavaScript code snippets that provide the latest available functionalities (e.g., Canvas element, text-shadow) to older browser platforms that do not support them natively.

**Mechanism:** Fills the loopholes and gaps in the browser to ensure features work properly.
