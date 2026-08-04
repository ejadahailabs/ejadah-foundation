# Product Family

## The principle

> **Each workbench is a complete product on its own. Together they compose. Neither
> configuration is broken.**

This is a commercial property as much as a technical one: it lets us sell one workbench
at a time, and lets a customer get real value without buying a suite.

## How they compose — and how they do not

**No workbench ever invokes another.** They compose through two things they already
share: **the Git repository** and **the graph ontology**.

E-AEW writes architecture artefacts as files with declared roles. E-REW's producers read
them as facts. The graph turns roles into typed edges. E-REW then answers questions about
architecture coverage without knowing E-AEW exists.

```
E-REW ──writes──►  ┌──────────────────────┐
E-AEW ──writes──►  │  the Git repository  │ ──► producers ──► graph ──► answers
E-VEW ──writes──►  └──────────────────────┘
```

**Forbidden:** imports between products, exported APIs, a shared runtime service, a
message bus, or any exchange format other than the on-disk format.

## Degradation is honest, by design

A workbench whose neighbours are absent sees no artefacts carrying those roles. The
analyses needing them **stand down with a stated reason** — never defaulted, never
estimated, never reported as complete.

## The lifecycle chain

```
E-REW      requirements
  ↓
E-AEW      architecture
  ↓
E-SWE      software
  ↓
E-VEW      verification evidence
  ↓
E-CEW      certification package

E-RVW  reviews across all of the above
E-SEW  systems engineering above all of it
```

Every arrow is *files plus ontology* — never a call.

## Build order

| Order | Product | Trigger |
|---|---|---|
| 1 | **E-REW** | shipping |
| 2 | next workbench | **a real user waiting for it** |
| 3+ | the rest | same |

There is no schedule, and that is deliberate. A workbench is built when someone needs it,
because the lessons that shape it come from shipping the previous one.

## E-REW is the reference implementation

Not merely the first product. The Platform is **extracted from** E-REW as capabilities
prove themselves — so the shared substrate grows from demonstrated need rather than
speculation. Every later workbench inherits proven code, not a guess.
