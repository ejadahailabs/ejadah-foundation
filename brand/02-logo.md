# 2 · Logo

> **Draft status.** The SVGs in [logos/](logos/) are flat redraws of the original PNG marks,
> made so we have vector, one-colour and small-size versions at all. They need owner
> approval, and ideally a designer's pass, before they replace the PNGs. Edit
> `logos/make-logos.py`, never the SVGs: every variant is generated from one drawing so
> variants can't drift.

## The two marks

| Mark | What it shows | Use for |
|---|---|---|
| **E-mark** (`ejadah-mark*.svg`) | A gold E inside an arc; edges converge from two nodes onto a third: knowledge arriving at an answer | Company surfaces: website header, careers, investor material, the footer of Sanad materials |
| **Sanad mark** (`sanad-mark*.svg`) | Two links of one chain, an orbit of evidence, one checked node | Everything about the product: Marketplace, app icon, social, product pages, decks |

## Variants

| File | Ground | Notes |
|---|---|---|
| `*-mark.svg` | ink (dark) | The default. Gold + mist |
| `*-mark-on-light.svg` | paper (light) | gold.dim + ink, so it passes contrast on light |
| `*-mark-mono.svg` | anything | `currentColor`: one colour, set by the surrounding text colour |
| `sanad-mark-small.svg` | anything | 16–32px. The two links only; orbit and nodes drop out |
| `sanad-app-icon.svg` | its own ink tile | Marketplace, favicons, app stores |
| `sanad-lockup.svg` / `-on-light` | dark / light | Mark + "Sanad" + "BY EJADAH AI LABS" |

## Rules

- **Clear space:** at least one node diameter (about 8% of the mark's width) on every side.
- **Minimum size:** full mark 48px on screen, 15mm in print. Below 48px, use `sanad-mark-small.svg`.
- **Lockup text** is live Inter in the draft. Outline it to paths before sending to print or
  third parties.
- **Pick the variant for the ground.** The default marks are for ink only; on light use
  `-on-light` or `-mono`. Never put the default mark on a light or busy ground.

## Never

- Add gradients, glows, bevels, shadows or metallic effects (the original PNGs have these; the
  flat versions replace them).
- Recolour outside the palette, or use more than one colour in a mono context.
- Rotate, stretch, outline, or put the mark in a container other than the app-icon tile.
- Rebuild the mark from a screenshot or an AI image generator.
- Combine the two marks side by side as equals. Ejadah endorses Sanad; it doesn't co-sign.
