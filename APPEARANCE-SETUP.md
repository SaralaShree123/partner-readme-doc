# Appearance setup (logo, CSS, icons)

Logo and theme **cannot** be changed via Git sync. Configure these in the ReadMe dashboard.

---

## 1. Replace ReadMe logo with Gupshup logo

Use the same logo as production [partner-docs.gupshup.io](https://partner-docs.gupshup.io).

### Steps

1. Open [dash.readme.com](https://dash.readme.com) → project **partner-doc-360**
2. Go to **Appearance** (or **Settings → Theme**)
3. Under **Branding**:
   - **Logo** — upload `branding/gupshup-partner-logo.svg` from this repo  
     (or download from production: the Gupshup Partner header logo)
   - **Logo (dark / white)** — upload the same SVG if your header uses a dark background
   - **Favicon** — upload a Gupshup favicon (optional; use a square PNG/ICO)
4. Set **Project name** to: `Gupshup Partner Documentation`
5. **Save** and preview the hub

### Logo file in this repo

```
branding/gupshup-partner-logo.svg
```

Copied from the live Gupshup partner docs ReadMe project.

### Recommended logo settings

| Setting | Value |
|---------|--------|
| Format | SVG (preferred) |
| Height | 24px or 40px (Modern theme) |
| Alt text | Gupshup Partner Documentation |

---

## 2. Remove “Powered by ReadMe” footer (optional)

If your plan includes it:

- **Appearance → Theme → Footer** → disable **Show ReadMe logo**

Or add to **Custom CSS** (see section 3):

```css
.rm-Footer .ReadMeLogo,
.rm-Footer a[href*="readme.com"],
.rm-PageFooter a[href*="readme.io"] {
  display: none !important;
}
```

---

## 3. Bold main sections (Get Started, Onboarding, Partner API, …)

1. Open **Settings → Custom CSS**
2. Paste the contents of `APPEARANCE-CUSTOM-CSS.css`
3. Save

---

## 4. Page icons

Set via `icon:` frontmatter on overview and hub pages (already in Git).

---

## 5. Overview cards

Overview uses ReadMe `<Cards>` / `<Card kind="tile">` blocks in `docs/get-started/overview.md`.
