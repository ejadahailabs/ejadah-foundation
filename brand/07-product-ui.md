# 7 · Product UI (Sanad)

## The rule: Sanad looks like the editor, not like us

Inside VS Code, Sanad uses **no brand colours**. Every colour is a VS Code theme token, so
the product is correct in light, dark and high-contrast themes automatically, including the
accessibility cases. This is a recorded product decision
(`Sanad/docs/DESIGN_DECISIONS.md`: "Never hard-code colours. Use theme colour identifiers").

The brand is the **behaviour**: calm, precise, honest about what it doesn't know.

## What the UI already does, and keeps doing

| Area | Rule |
|---|---|
| Colour | `var(--vscode-*)` tokens only: `foreground`, `descriptionForeground`, `panel-border`, `focusBorder`, `button-*`, `input-*`, `errorForeground`, `editorWarning-foreground`, `testing-iconPassed` |
| Icons | Codicons (`$(refresh)`, `$(new-file)`, …). No custom icon set inside the editor |
| Type | `--vscode-font-family` and `--vscode-editor-font-family`. Never load Inter in a webview |
| Findings | Native Problems panel, squiggles and quick fixes; no custom findings UI |
| Diagrams | The picture theme (`src/design/pictureTheme.ts`): kind colours from the editor's chart tokens, a shape cue per kind, organisation themes refused below 4.5:1 text / 3:1 stroke |
| Accessibility | WCAG 2.2 1.4.1 (colour never the only cue), 1.4.3 and 1.4.11 (contrast); visible focus everywhere |

## Where the brand does appear

Exactly four places, all outside the editing surface:

| Surface | What | Asset |
|---|---|---|
| Activity bar icon | The two links, one colour | `logos/sanad-mark-small.svg` (`currentColor`, VS Code tints it) |
| Marketplace listing | App icon + gallery banner | `logos/sanad-app-icon.svg` (export 256px PNG); `galleryBanner: { "color": "#070B14", "theme": "dark" }` |
| Walkthrough / welcome | The lockup at the top, then plain VS Code UI | `logos/sanad-lockup*.svg` |
| README header | The lockup, then text | same |

## Writing in the UI

The Assurance register, shortened. Full sentences, no status codes, no jargon the user
didn't bring.

| Situation | Write | Not |
|---|---|---|
| Analysis can't run | "No hazard role declared — safety analysis stood down." | "Safety: N/A" or "0 hazards" |
| An inferred finding | "Candidate: this sentence may be ambiguous. Your call." | "Ambiguous requirement" |
| A destructive action | "Delete REQ-SYS-042? It stays in Git history and can be restored." | "Are you sure?" |
| AI suggestion | "Proposed — not written until you confirm." | "AI generated" |
| Empty state | Say what's missing and the one action that fixes it | An illustration |

## Not in scope here

**Generated reports** (HTML traceability reports, evidence packs) stay neutral and
unbranded. They are the customer's evidence, and they must regenerate byte-identically at a
commit. Any change to their look is a Sanad product change, made through Sanad's own process
(an ADR, a feature folder, the byte-identical tests), not through this guide.
