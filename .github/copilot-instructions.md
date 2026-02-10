# Eye On Fleet UI - Copilot Instructions

## Project Overview
This is a production marketing website for **Eye On Fleet**, a GPS & IoT fleet management platform. The codebase is a static HTML/CSS site with a clean, minimalist structure focused on user engagement and solution showcase.

## Architecture & Key Files

### Site Structure
- **[index.html](../index.html)** - Landing page featuring hero section, solutions grid (4 solution cards), and navigation
- **[css/style.css](../css/style.css)** - All styling (single file, minified format); uses CSS Grid for responsive layout
- **[images/](../images/)** - Product assets (logo, hero, solution screenshots)
- **Linked pages** (referenced but not yet created): `solutions/fleet.html`, `industries.html`, `contact.html`

## Design Patterns & Conventions

### Color Scheme
- **Primary Green**: `#22c55e` (buttons, accents)
- **Light Green**: `#dcfce7` (header background)
- **Background**: `#f0fdf4` (light green tint)
- **Dark Footer**: `#020617` (contrast)

### CSS Architecture
- **Minified single file** - All styles in one concatenated line
- **CSS Grid** for layouts (`.hero-grid` 2-column, `.cards` 4-column grid)
- **Mobile-first responsive** - Media query at `@media(max-width:768px)` switches grids to single column
- **Reusable classes**: `.btn` (green button style), `.card` (white padded container)

### Component Structure
- **Header** (`<header class="header">`) - Contains branding and navigation
- **Hero Section** (`<section class="hero">`) - Two-column layout with headline + image
- **Solutions Grid** (`<section class="section">`) - Four equal-width cards
- **Footer** (`<footer class="footer">`) - Copyright info

## Development Workflow

### Making CSS Changes
1. Edit [css/style.css](../css/style.css) directly - modify inline styles (file is single minified line)
2. For readability, consider expanding the line with newlines during development, then minify before committing
3. Always test responsive behavior at `768px` breakpoint

### Adding New Pages
- Follow naming convention: `kebab-case.html` (e.g., `contact.html`, `fleet.html`)
- Mirror header/footer structure from [index.html](../index.html) for consistency
- Import `css/style.css` with relative path adjustments (e.g., `../css/style.css` if nested in subdirectory)
- Update navigation links in header

### Image Management
- Store all images in [images/](../images/)
- Use descriptive filenames (e.g., `solution-fleet.webp`, `hero.webp`)
- Use `.webp` format for modern browsers; `.png` for logos/icons needing transparency

## Key Conventions

### Navigation Structure
- **Header links** are hardcoded in [index.html](../index.html); update here for site-wide nav consistency
- Links to undefined pages (e.g., `solutions/fleet.html`) should be created before linking

### Button Styling
- Use `class="btn"` for all call-to-action buttons
- Applies green background (`#22c55e`), white text, padding, rounded corners

### Responsive Classes
- `.section` wraps content sections with padding
- `.cards` uses `grid-template-columns: repeat(4,1fr)` (desktop) → `1fr` (mobile)
- `.hero-grid` uses `grid-template-columns: 1fr 1fr` (desktop) → `1fr` (mobile)

## Common Tasks

### Update a Button Text or Link
Edit [index.html](../index.html) - locate the `<a class="btn">` tag, update `href` attribute and text content.

### Add a New Solution Card
In [index.html](../index.html), add a new `<div class="card">` inside `.cards` container with the solution name/description.

### Change Brand Colors
Edit [css/style.css](../css/style.css) - find and replace hex values:
- Primary green: `#22c55e`
- Header green: `#dcfce7`
- Background: `#f0fdf4`

### Create a New Page
1. Create `newpage.html` at project root or in subdirectory (e.g., `solutions/newpage.html`)
2. Copy structure from [index.html](../index.html) (DOCTYPE, head with `css/style.css` link, header/footer)
3. Update relative CSS path if needed (`../css/style.css` for subdirectories)
4. Add link in header navigation of [index.html](../index.html)

## Notes for Agents
- This is a **static site** - no server-side processing, no database, no build step required
- CSS is intentionally minified in one line; maintain this for performance but consider readability tools during editing
- All future pages should maintain the header/footer structure and color scheme for brand consistency
- No JavaScript currently used - keep it minimal if adding interactivity
