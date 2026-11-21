# 3 · Colour

Values live in [tokens/tokens.json](tokens/tokens.json). This chapter explains them. Run
`node brand/tokens/check-contrast.mjs` after any change.

## The palette: deep navy, gold, cool white

The palette comes from the mark, not from a mood board. **Three colour families used
consistently read as considered; a fourth reads as decorated.**

| Family | Value | Share of a dark surface | Job |
|---|---|---|---|
| **Ink** (dominant) | `#070B14`, raised `#0B1220`, line `#16203A` | about 80–85% | The ground. Quiet, deep, out of the way |
| **Mist** | `#E8ECF5`, dim `#9AA7BF`, muted `#7A88A3`, faint `#61708C` | about 10% | Text, in four steps of emphasis |
| **Gold** | `#C9A227`, bright `#E6C158`, dim `#8A6F1C`, deep `#7A6218` | about 5%, **never more than 10%** | The one thing that matters most |
| **Paper** (light surfaces) | `#F7F8FB`, raised `#FFFFFF`, line `#DDE2EC` | — | Documents, print, slides, light theme |

### Why these colours

- **Navy reads as authority and reliability:** the colour of institutions people trust with
  consequences (aviation, banking, defence). Our buyer is accountable for safety; a quiet dark
  ground says *serious*. It's also the developer's dark-mode IDE, so the site and the product
  feel like one place.
- **Gold reads as value, permanence and *verified*:** a seal, a gold standard. Used sparingly
  it points the eye; overused it turns into luxury or crypto, which is the wrong signal. Hence
  the 10% cap.
- **Cool off-white, not pure white:** less glare on dark grounds; calmer.
- **What we deliberately don't use:** electric blue, violet, neon and gradients. That is the
  generic "AI startup" look, and our voice already rejects "AI-powered".

## The gold rule

Gold marks **one** thing per view: the mark's E, the key node in a diagram, the primary
button, the focus ring. If two things on a screen are gold, one of them is wrong.

## Light surfaces

The website is dark-only, but documents, print, slides and the brand page need light.

| On paper, use | Not | Why |
|---|---|---|
| `gold.deep #7A6218` for gold **text** | `gold #C9A227` | Plain gold on paper is 2.3:1, unreadable |
| `gold.dim #8A6F1C` for gold **fills and strokes** | `gold` | 4.5:1 as a graphic |
| `paper.text`, `paper.dim`, `paper.muted` | mist tones | Mist is for ink only |

## Contrast: what's allowed

Measured by `check-contrast.mjs` (WCAG 2.2: text 4.5:1, large text and graphics 3:1).

| Pair | Ratio | Allowed for |
|---|---|---|
| mist on ink | 16.6:1 | everything |
| mist.dim on ink | 8.1:1 | secondary text |
| mist.muted on ink | 5.5:1 | small tertiary text |
| **mist.faint on ink** | **3.9:1** | **large text (18px+, or 14px bold) and decoration only** |
| gold on ink | 8.1:1 | text, graphics |
| ink on gold | 8.1:1 | button labels |
| paper.text on paper | 18.5:1 | everything |
| gold.deep on paper | 5.5:1 | gold text on light |

> **Known issue on the website.** `text-mist-faint` is used for small body text in about 30
> places (`app/page.tsx`, `app/products/page.tsx`, …), which fails AA. The fix is to switch
> those to `text-mist-muted` (5.5:1). It's a visible change, so it's tracked as a separate
> website PR, not done silently.

## Status colours: the honesty words

What we say about maturity has two words (ADR-0003), and each has a colour. **The word is always
shown; the colour only supports it.**

| Word | On ink | On paper | Extra cue |
|---|---|---|---|
| build in progress | `#5FB98A` | `#1F7A4D` | solid dot |
| planned | `#7A88A3` | `#5B6780` | dashed outline |

Never use red or gold for status. Red means hazard (see below); gold means "the point".

## Diagram colours: the same as the product

Marketing diagrams use **Sanad's own picture theme** (`Sanad/src/design/pictureTheme.ts`),
so a diagram on LinkedIn reads exactly like a picture in the product. Each kind has a hue
and a shape cue, so it still works in greyscale and for colour-blind readers.

| Kind | Hue | Shape cue |
|---|---|---|
| part | blue | heavier outline |
| port | green | small square on the edge |
| requirement | yellow | cut top-right corner |
| state | purple | fully rounded corners |
| lifeline | cyan | dashed lifeline |
| hazard | red | double border |

Exact fill and stroke values for dark and light are in `tokens.json` under
`color.diagram`, all checked for contrast.

**Conceptual diagrams** (the knowledge graph, the pipeline) stay in the brand palette:
line-coloured edges, mist nodes, one gold node. See [chapter 6](06-imagery-diagrams.md).
