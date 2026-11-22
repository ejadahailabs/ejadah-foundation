# 9 · Templates

Everything here is built from the tokens and the logo drawings. **Regenerate, don't hand-edit:**
`python3 -I make-templates.py` (in `templates/`) after a token or logo change.

## What's here

| Template | File | Register | Notes |
|---|---|---|---|
| Social post (LinkedIn, X) | `templates/social-post-1200x627.svg` | either | Eyebrow, 2-line headline, one supporting line, status, motif, lockup |
| Open Graph image | `templates/og-image-1200x630.svg` | Assurance | One per website page; replace `ejadah-website/public/og.png` per page |
| GitHub social preview | `templates/github-social-1280x640.svg` | Builder | Lockup, headline, repo or command in mono |
| LinkedIn company banner | `templates/linkedin-banner-1584x396.svg` | Assurance | Content starts at x=520: the profile logo covers the bottom-left |
| Article header | `templates/article-header-1600x840.svg` | Assurance | For `/insights` articles |
| Carousel slide | `templates/carousel-slide-1080x1350.svg` | either | Page counter, 3-line headline, 4 points, status, lockup. Export each slide, combine into a PDF |
| One-pager | `templates/one-pager.html` | Assurance | A4, light. Capability table with status words built in. Print to PDF from Chrome |
| Email signature | `templates/email-signature.html` | — | Inline styles and tables only; logo from a hosted PNG |
| Slide master | [Sanad slide master](https://claude.ai/artifact/PNkkcRSB4pQtT1D2mgJxQp) (Slides; exports to PowerPoint and PDF) | either | Title, section, claim + evidence, diagram, status table, close |

## How to use an SVG template

1. Copy the file; never edit the original.
2. Replace every `{{PLACEHOLDER}}`, including `{{ALT_TEXT}}` in the root `aria-label`.
   Delete lines you don't need (e.g. a second headline line).
3. Keep text inside the 64px safe area. Headlines: 8 words maximum.
4. Export to PNG at 1× and 2× from Chrome or Figma **with Inter and JetBrains Mono installed**
   (the text is live, so a machine without the fonts falls back to system fonts).
5. Run the checklist in [chapter 8](08-digital-marketing.md) before posting.

## Adding a template

Add it to `make-templates.py` using the helpers there (`eyebrow`, `headline`, `support`,
`status`, `graph`, `lockup`), so it inherits the tokens. A template that hard-codes a colour
not in `tokens.json` is a defect.
