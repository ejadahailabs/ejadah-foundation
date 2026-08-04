# Ejadah Foundation

**The corporate constitution of Ejadah AI Labs.**

> Everything references it. Nothing depends on it.

This repository contains **no code**, and never will. It is the single authoritative
place from which every Ejadah repository inherits organisational standards.

## The rule that makes it work

| | |
|---|---|
| **Reference** | Any repository may link to any document here. |
| **Depend** | No repository may *build*, *test* or *run* against anything here. |

That asymmetry is the whole design. A repository that could break because this one
changed would make this repository a deployment coupling — and then ten repositories
would be unable to move without a release here. Stability comes from having nothing
downstream that can break.

**Practical test:** deleting this repository must break no build, anywhere. It would
only cost the organisation its memory.

## Layout

| Directory | Contains | Changes |
|---|---|---|
| `company/` | Vision, Mission, Values, Branding | rarely |
| `engineering/` | Principles, standards, AI governance | deliberately |
| `product/` | Platform, product family, naming, roadmap | per milestone |
| `adr/` | Company-level decisions | append-only |
| `templates/` | Starting points every repository copies | rarely |

## What lives here, and what does not

| Here | In the product repository |
|---|---|
| *Why* we engineer this way | *How* this product works |
| Standards every repo inherits | This repo's build, tests, CI |
| Company-level ADRs | Product ADRs |
| Naming authority | Product implementation |

A document that names a specific product's internals is in the wrong repository.

## Status

Established 2026-08-04. Ejadah AI Labs operates one shipping product (E-REW) and one
adopted platform architecture. Everything here is written from what is proven in that
product, not from what is imagined for the others — the same discipline
`engineering/Engineering_Principles.md` requires of code.
