# 6 · Imagery and diagrams

## The principle

**The diagram is the argument.** A knowledge graph and a lifecycle are exactly what the
product builds, so drawing them states the thesis without a paragraph. We show structure,
evidence and real output, not people pointing at screens.

## What we use

| Image type | Where | Rules |
|---|---|---|
| **Conceptual diagrams** (graph, pipeline, chain) | Website, decks, social | SVG, drawn in node · edge · check geometry. Edges in `ink.line` (dark) or `paper.line` (light), nodes in mist, **one gold node**: the answer. See `ejadah-website/components/Visuals.tsx` |
| **Engineering diagrams** (SysML, trace, coverage) | Articles, product pages, social | Sanad's picture-theme colours and shape cues ([chapter 3](03-colour.md)). Prefer exporting from Sanad itself |
| **Product screenshots** | Product page, Marketplace, docs, Builder-register social | Real workspace, real data (the cold-chain showcase repo), VS Code default dark theme, 1px `ink.line` frame, 12px radius, no fake browser chrome |
| **Real outputs** | Anywhere as proof | The traceability report, a finding with its evidence, a CI gate result. Crop to the part that proves the claim |

## What we never use

- Stock photography of people, offices, handshakes or "engineers at whiteboards".
- AI-generated illustrations, glowing brains, circuit-board textures, robots, abstract "data" particles.
- Fake data presented as real. If a screenshot uses example data, say so in the caption.
- Screenshots on the homepage (existing website rule: the category comes before the product).
- Decorative gradients, glows or glass effects. The one allowed soft glow is behind the
  central gold node in conceptual diagrams, at 20% opacity or less.

## Diagram mechanics

- Stroke widths: 1.25px edges, 2px node outlines, at 600px width. Scale proportionally.
- Corner radius: 6px on boxes, matching `radius.md`.
- Labels in Inter 500, sentence case; IDs in JetBrains Mono.
- Every diagram has a text alternative (`role="img"` and an `aria-label` that says what it
  shows, not what it looks like).
- Colour is never the only cue: shape, label or line style must carry the same meaning.
- Flow reads left to right or top to bottom. Arrows only where direction matters.

## Motion

Minimal. A diagram may draw its edges in once (≤600ms, ease-out). Nothing loops. Respect
`prefers-reduced-motion` (the website already does).
