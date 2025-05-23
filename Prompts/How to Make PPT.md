Role:** Act as an expert front-end developer specializing in creating highly polished, interactive, single-page web applications that mimic presentation software canvases.

**Goal:** Generate a single, self-contained `.html` file that functions as a horizontal-scrolling presentation canvas. This file should serve as a reusable template. I will provide the specific slide content later.

**Core Requirements:**

1.  **Output Format:** A single `.html` file including all necessary HTML structure, CSS styling (within `<style>` tags), and JavaScript functionality (within `<script>` tags). No external CSS or JS files.
2.  **Structure:**
    *   A main container (`.presentation-container`) that enables horizontal scrolling (`overflow-x: scroll`) and occupies the full viewport height and width.
    *   Individual slides represented by `<section class="slide">` elements arranged horizontally using `display: flex` on the container.
    *   Each slide must occupy the full viewport width (`100vw`) and height (`100vh`) and use `flex-shrink: 0`.
3.  **Scrolling & Snapping:**
    *   Implement mandatory horizontal scroll snapping (`scroll-snap-type: x mandatory`) on the `.presentation-container`.
    *   Slides should snap to the center (`scroll-snap-align: center`).
    *   Visually hide the browser's default scrollbar for the `.presentation-container`.
4.  **Slide Content Area:**
    *   Within each `.slide`, include a `.slide-content` div.
    *   This `.slide-content` should have a maximum width (use `--content-max-width` variable, default around `850px`).
    *   Allow for vertical scrolling (`overflow-y: auto`) *only within* the `.slide-content` if its content exceeds the available slide height (minus padding).
    *   Include subtle custom scrollbar styling for this vertical scrollbar (using `-webkit-scrollbar` pseudo-elements).
5.  **Navigation:**
    *   Implement fixed navigation arrow buttons (`.nav-arrow`) positioned at the bottom-right of the viewport.
    *   Use Feather Icons (or similar SVG icons loaded via CDN or embedded) for `arrow-left` and `arrow-right`.
    *   JavaScript logic:
        *   Clicking the arrows should smoothly scroll (`scrollTo({ left: ..., behavior: 'smooth' })`) to the previous/next slide.
        *   Disable the 'previous' arrow on the first slide and the 'next' arrow on the last slide (add/remove a `.disabled` class).
        *   Support keyboard navigation: Left/Right arrow keys and PageUp/PageDown keys should navigate between slides.
        *   Update the current slide index and disabled button states accurately based on both clicks and scrolls (use a debounced scroll listener).
6.  **Visual Design & Styling (Luxury UI/UX - based on our previous conversation):**
    *   **Color Palette:** Use CSS variables:
        *   `--primary-bg: #0a192f` (Deep Navy)
        *   `--secondary-bg: #112240` (Lighter Navy)
        *   `--accent-color: #F5D0A0` (Soft Gold/Cream)
        *   `--text-primary: #ccd6f6` (Light Steel Blue)
        *   `--text-secondary: #8892b0` (Slate Gray)
        *   `--text-highlight: #ffffff`
    *   **Typography:** Use CSS variables:
        *   `--font-primary: 'Montserrat', sans-serif`
        *   `--font-heading: 'Playfair Display', serif` (Import from Google Fonts).
    *   **Default Sizing (Smaller/Zoomed-Out Feel):** Implement the smaller sizing as the default. Use CSS variables extensively for font sizes, padding, margins, icon sizes, grid gaps etc. (Reference values: `--font-size-h1: 3.1rem`, `--font-size-p: 1.0rem`, `--slide-padding-vertical: 50px`, `--icon-size-regular: 28px`, etc., similar to the final version we developed).
    *   **Layout Elements:** Apply styles consistently using the variables (e.g., list item padding, tech item padding, CTA button padding).
    *   **Visual Details:** Include subtle background gradients on slides, slightly rounded corners on list/tech items, hover effects (slight lift/shadow), left border accent on list items, frosted glass effect on navigation buttons (`backdrop-filter`).
    *   **Icons:** Ensure Feather Icons script is included (`<script src="https://unpkg.com/feather-icons"></script>`) and `feather.replace()` is called in the JavaScript. Style icons using CSS variables for size/color.
7.  **Template Structure for Content:**
    *   Inside each `<section class="slide">`, within the `<div class="slide-content">`, provide clear placeholder comments indicating where the actual slide content should be inserted later. Example: `<!-- SLIDE 1: Title Slide Content Goes Here -->`, `<!-- SLIDE 2: Points List Content Goes Here -->`, etc.
    *   **Do not** hardcode the specific presentation text content (like "Omni: Crafting...", "We Hear You...", budget numbers, etc.) from our previous example. The goal is a *template*. Generate maybe 3-4 placeholder slide structures.
8.  **Code Quality:**
    *   Generate clean, well-commented HTML.
    *   Use CSS Variables extensively for easy customization of colors, fonts, and spacing/sizing.
    *   Write efficient, non-blocking JavaScript for navigation and scroll handling. Ensure smooth performance.

**Final Output:** A single, ready-to-use `.html` file containing the complete presentation canvas template structure, styling, and functionality as described above, ready for me to populate with specific slide content.

---

**How to Use This Prompt:**

1.  Provide this prompt to a capable AI model.
2.  The AI should generate the `.html` file structure.
3.  Review the generated code for adherence to all requirements (especially horizontal scrolling, snapping, navigation, CSS variables, default smaller sizes, and visual styling).
4.  Once satisfied with the template, you can manually replace the placeholder comments (`<!-- SLIDE X CONTENT HERE -->`) within each `<div class="slide-content">` with your actual presentation content (headings, paragraphs, lists, images, etc., using appropriate HTML tags).

This prompt is designed to be specific enough to recreate the desired canvas while being general enough regarding the *content* to be reusable.
