# 🎨 CSS Complete Reference (Markdown Format)

## 🔹 CSS Selectors
| Selector | Example | Description |
|----------|---------|-------------|
| `#id` | `#firstname` | Selects the element with id="firstname" |
| `.class` | `.intro` | Selects all elements with class="intro" |
| `*` | `*` | Selects all elements |
| `element` | `p` | Selects all `<p>` elements |
| `element, element` | `div, p` | Selects all `<div>` and `<p>` elements |

---

## 🔹 CSS Specificity (Cascade Priority)
1. Inline style (`style=""`)
2. Internal/External CSS (in `<head>`)
3. Browser default

---

## 🔹 CSS Property: `background`
### Shorthand Value Order:
1. `background-color`
2. `background-image`
3. `background-repeat`
4. `background-attachment`
5. `background-position`

### All `background` Properties
| Property | Description |
|----------|-------------|
| `background` | Sets all background properties in one |
| `background-attachment` | Fixed or scroll |
| `background-clip` | Painting area |
| `background-color` | Background color |
| `background-image` | Background image |
| `background-origin` | Starting position |
| `background-position` | Starting point |
| `background-repeat` | Repeat pattern |
| `background-size` | Size of background image |

---

## 🔹 CSS Border

### `border-style` Values
- `dotted`, `dashed`, `solid`, `double`
- `groove`, `ridge`, `inset`, `outset`
- `none`, `hidden`

### Border Style Shorthand Rules
```css
/* Four values: top right bottom left */
border-style: dotted solid double dashed;

/* Three values: top, right/left, bottom */
border-style: dotted solid double;

/* Two values: top/bottom, right/left */
border-style: dotted solid;

/* One value: all sides */
border-style: dotted;
```

### Shorthand: `border`
```css
border: 2px solid red;
```
Includes:
- `border-width`
- `border-style`
- `border-color`

---

## 🔹 Box Model Explanation
- **Content**: Where text/images appear
- **Padding**: Space around content (transparent)
- **Border**: Around padding and content
- **Margin**: Outside border (transparent)

> **Note**: Outline is different. It is outside the element’s dimensions.

---

## 🔹 Text Decoration
| Property | Description |
|----------|-------------|
| `text-decoration` | All properties in one |
| `text-decoration-color` | Color of the line |
| `text-decoration-line` | `underline`, `overline`, etc. |
| `text-decoration-style` | `solid`, `dotted`, etc. |
| `text-decoration-thickness` | Thickness of the line |

---

## 🔹 CSS Lists
| Property | Description |
|----------|-------------|
| `list-style` | All list properties in one |
| `list-style-image` | Image as list marker |
| `list-style-position` | Marker position (inside/outside) |
| `list-style-type` | Type of bullet |

---

## 🔹 Display Property
| Value | Description |
|-------|-------------|
| `inline` | Inline element |
| `block` | Block element |
| `inline-block` | Inline element with block features |
| `flex` | Flexbox container |
| `grid` | Grid container |
| `none` | Removes the element |
| `contents` | Removes the element box, shows children |
| `inline-flex` | Inline flex container |
| `inline-grid` | Inline grid container |
| `list-item` | Behaves like `<li>` |
| `run-in` | Block or inline based on context |
| `table`, `table-row`, `table-cell`, etc. | Table elements |
| `initial` | Sets default value |
| `inherit` | Inherits from parent |

---

## 🔹 CSS Position
- `static`: Default
- `relative`: Relative to normal position
- `absolute`: Positioned relative to the nearest positioned ancestor
- `fixed`: Fixed to viewport
- `sticky`: Scrolls until a threshold, then sticks

---

## 🔹 !important Rule
- Overrides all other rules on the same property, even inline styles.
```css
color: red !important;
```

---

## 🔹 Attribute Selectors
| Selector | Example | Description |
|----------|---------|-------------|
| `[attr]` | `[target]` | Selects elements with `target` attribute |
| `[attr=value]` | `[target="_blank"]` | Exact value match |
| `[attr~=value]` | `[title~="flower"]` | Space-separated value list contains "flower" |
| `[attr|=value]` | `[lang|="en"]` | Value starts with `en-` |
| `[attr^=value]` | `a[href^="https"]` | Starts with value |
| `[attr$=value]` | `a[href$=".pdf"]` | Ends with value |
| `[attr*=value]` | `a[href*="w3schools"]` | Contains substring |

---

## 🔹 Object-Fit Property
```css
.fill { object-fit: fill; }
.contain { object-fit: contain; }
.cover { object-fit: cover; }
.scale-down { object-fit: scale-down; }
.none { object-fit: none; }
```

---

## 🔹 CSS Animation Properties
| Property | Description |
|----------|-------------|
| `@keyframes` | Defines animation sequence |
| `animation` | Shorthand for all animation properties |
| `animation-name` | Animation name |
| `animation-duration` | Length of animation |
| `animation-delay` | Start delay |
| `animation-iteration-count` | Number of cycles |
| `animation-direction` | Forward, reverse, alternate |
| `animation-fill-mode` | State before/after |
| `animation-play-state` | `running` or `paused` |
| `animation-timing-function` | Speed curve |

---

## 🔹 @property (Custom CSS Variables)
Define variables in CSS without JS.
```css
@property --myColor {
  syntax: '<color>';
  inherits: false;
  initial-value: #c0ffee;
}
```

---

## 🔹 box-sizing
```css
box-sizing: border-box;
```
Includes `padding` and `border` in element’s width and height.

---

## 🔹 Flexbox vs. Grid
- **Flexbox**: One-dimensional (row OR column)
- **Grid**: Two-dimensional (row AND column)

---

## 🔹 Flex Container Properties
| Property | Description |
|----------|-------------|
| `display` | Enables flex context |
| `flex-direction` | Row, row-reverse, column, column-reverse |
| `flex-wrap` | No wrap, wrap, wrap-reverse |
| `flex-flow` | Shorthand: direction + wrap |
| `justify-content` | Horizontal alignment |
| `align-items` | Vertical alignment |
| `align-content` | Line alignment (multiline) |

## Flex Item Properties
| Property | Description |
|----------|-------------|
| `order` | Item order |
| `flex-grow` | Grow factor |
| `flex-shrink` | Shrink factor |
| `flex-basis` | Initial size |
| `flex` | Shorthand for grow, shrink, basis |
| `align-self` | Individual alignment |

---

## 🔹 Grid Properties
| Property | Description |
|----------|-------------|
| `display` | Enables grid context |
| `grid-template-rows` | Define row structure |
| `grid-template-columns` | Define column structure |
| `grid-template-areas` | Named layout areas |
| `grid-row`, `grid-column` | Positioning grid items |
| `grid-auto-rows`, `grid-auto-columns` | Default size for auto tracks |
| `grid-auto-flow` | Auto-placement direction |
| `gap`, `row-gap`, `column-gap` | Spacing between items |
| `justify-content`, `align-content` | Container alignment |
| `justify-self`, `align-self` | Item alignment |
| `place-content`, `place-self` | Shorthand alignment |

---

End of CSS Reference 🧠