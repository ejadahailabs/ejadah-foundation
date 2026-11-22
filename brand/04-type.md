# 4 · Type

## Two fonts

| Font | Use | Why |
|---|---|---|
| **Inter** | Everything: headings, body, UI, slides | Neutral, highly legible at small sizes, free, already on the website |
| **JetBrains Mono** | Identifiers, paths, hashes, code: `REQ-SYS-042`, `a1b2c3d`, `@implements` | **Evidence should look like evidence.** A requirement ID in mono reads as a real, checkable thing |

Both are open-licence (SIL OFL). Load from Google Fonts on the web; install locally for
slides and documents. Fallbacks are in `tokens.json`.

No third font. No serif, no display face, no script.

## Scale

| Style | Size | Weight | Tracking | Line height | Use |
|---|---|---|---|---|---|
| Display | clamp(2.5rem, 6vw, 4.5rem) | 600 | −0.045em | 1.05 | One per page: the hero line |
| H1 | 2.25rem | 600 | −0.03em | 1.15 | Page and slide titles |
| H2 | 1.5rem | 600 | −0.02em | 1.25 | Sections |
| Eyebrow | 0.75rem | 500 | +0.18em, UPPERCASE | 1.4 | The label above a heading |
| Body | 1rem | 400 | 0 | 1.65 | Paragraphs |
| Small | 0.875rem | 400 | 0 | 1.6 | Captions, table cells |

**Measure:** body text never runs wider than **68 characters** (`max-w-reading`).

## Rules

- Sentence case for headings and buttons. UPPERCASE only for eyebrows.
- Tight tracking on large type, open tracking on small caps. Never letter-space body text.
- Numbers in tables: tabular figures (`font-variant-numeric: tabular-nums`).
- Mono is for things a reader could copy and check. Don't use it for decoration or "techy"
  flavour.
- Weights: 400, 500, 600. No light (300) or black (800+): thin type disappears on dark
  grounds, heavy type shouts.
