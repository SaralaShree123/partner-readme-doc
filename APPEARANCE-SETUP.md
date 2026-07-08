# Appearance setup (360dialog look)

## 1. Bold main sections (Get Started, Onboarding, Partner API, …)

ReadMe does **not** bold category titles via Git. Paste this CSS:

1. Open ReadMe project → **Settings → Custom CSS** (or Appearance → Custom CSS)
2. Paste the contents of `APPEARANCE-CUSTOM-CSS.css`
3. Save

## 2. Page icons (hand / rocket / book)

Already set via `icon:` frontmatter on Overview, Quickstarts, and section hubs.
After Git sync, open a page in the ReadMe editor if an icon does not appear and re-select Font Awesome if needed.

## 3. Overview cards

Overview now uses ReadMe `<Cards>` / `<Card kind="tile">` blocks (Partner API Reference, Quickstarts, Early Access, Support) — same pattern as 360dialog’s Get started containers.
