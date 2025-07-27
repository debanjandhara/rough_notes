
# 🧠 HTML Complete Notes

## 📝 Document Structure

- `<!DOCTYPE html>`: Defines that the document is HTML5.
- `<html>`: Root element of an HTML page.
- `<head>`: Contains metadata (not visible).
- `<title>`: Page title (shown in browser tab).
- `<body>`: Contains all visible contents (headings, paragraphs, images, links, etc).

## 🖋️ Text Elements

- `<h1>` to `<h6>`: Headings, `<h1>` being the largest.
- `<p>`: Paragraph.
- `<br>`: Line break (empty element, no end tag).
- `<b>`: Bold text.
- `<strong>`: Important text (semantically bold).
- `<i>`: Italic text.
- `<em>`: Emphasized text.
- `<mark>`: Highlighted text.
- `<small>`: Smaller text.
- `<del>`: Deleted text.
- `<ins>`: Inserted text.
- `<sub>`: Subscript text.
- `<sup>`: Superscript text.

## 💬 Quotation and Citation Elements

- `<abbr>`: Abbreviation or acronym.
- `<address>`: Contact info.
- `<bdo>`: Text direction.
- `<blockquote>`: Quoted section.
- `<cite>`: Title of a work.
- `<q>`: Inline quote.

## 🎨 Styling and Attributes

- All HTML elements can have **attributes**.
- `href`: Specifies link destination in `<a>`.
- `src`: Specifies image path in `<img>`.
- `width`, `height`: Specify image size.
- `alt`: Alternate text for image.
- `style`: Inline styles (color, font, etc.).
- `lang`: Declares language.
- `title`: Extra info on hover.

### Common CSS Properties

- `background-color`, `color`
- `font-family`, `font-size`
- `text-align`

## 🌈 HSL Color

```css
hsl(hue, saturation%, lightness%)
```

- Hue: 0–360 (0 = red, 120 = green, 240 = blue)
- Saturation: 0% (gray) to 100% (full color)
- Lightness: 0% (black) to 100% (white)

## 🧬 Cascading and Inheritance

- Cascading: Parent style applies to children unless overridden.

## 🎨 Style Inclusion

- Inline: `style` attribute
- Internal: `<style>` in `<head>`
- External: `<link rel="stylesheet" href="style.css">`

## 🔗 Links

- Unvisited: Blue & underlined
- Visited: Purple & underlined
- Active: Red & underlined

### `target` attribute

- `_self`: Same tab (default)
- `_blank`: New tab
- `_parent`: Parent frame
- `_top`: Full body window

## 🗺️ Image Map

- `<map>`: Defines image map.
- `<area>`: Defines clickable areas.

## 📊 Tables

| Tag | Description |
|------|-------------|
| `<table>` | Table |
| `<th>` | Table header |
| `<tr>` | Table row |
| `<td>` | Table cell |
| `<caption>` | Table caption |
| `<colgroup>` | Group of columns |
| `<col>` | Column properties |
| `<thead>` | Header group |
| `<tbody>` | Body group |
| `<tfoot>` | Footer group |

## 📋 Lists

- `<ul>`: Unordered list
- `<ol>`: Ordered list
- `<li>`: List item
- `<dl>`: Description list
- `<dt>`: Term
- `<dd>`: Description

### Styling Lists

- Use `list-style-type` to customize bullets.
- `float: left;` for horizontal layout.

## 📦 Block vs Inline

- Block: Full width, new line. (e.g. `<div>`)
- Inline: Inline width, no new line. (e.g. `<span>`)

## 🆔 Class and ID

- `class`: reusable, case-sensitive.
- `id`: unique, must not start with a number or contain whitespace.

## 🧩 iframe

- `<iframe>`: Embed webpage
- `src`: URL
- `title`: Required for accessibility
- `width`, `height`: Size
- `style="border:none;"`: Remove border

## 🧠 Head Element

- `<head>` contains `<title>`, `<style>`, `<meta>`, `<link>`, `<script>`, `<base>`.

## 📱 Viewport

- `1vw` = 1% of viewport width

## 🧱 Semantic Elements

- HTML5 uses semantic tags like `<header>`, `<footer>`, `<main>`, etc.

## 🔒 XHTML

- A stricter XML-based version of HTML.

## 📨 HTML Form Attributes

| Attribute | Description |
|-----------|-------------|
| `accept-charset` | Form encoding |
| `action` | Submission URL |
| `autocomplete` | On/Off |
| `enctype` | Form encoding type |
| `method` | HTTP method |
| `name` | Name of form |
| `novalidate` | Disable validation |
| `rel` | Relationship of linked resource |
| `target` | Response display target |

## 🧾 HTML Form Elements

| Tag | Description |
|------|-------------|
| `<form>` | Form container |
| `<input>` | Input field |
| `<textarea>` | Multiline text |
| `<label>` | Label for input |
| `<fieldset>` | Group related fields |
| `<legend>` | Caption for group |
| `<select>` | Dropdown |
| `<optgroup>` | Group in dropdown |
| `<option>` | Dropdown item |
| `<button>` | Clickable button |
| `<datalist>` | Pre-defined options |
| `<output>` | Output result |
