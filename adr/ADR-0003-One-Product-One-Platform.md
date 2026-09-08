# ADR-0003 — One Product, One Platform

**Adopted 2026-09-08.**

Two documents in this repository described a family of seven discipline workbenches with a
shared Platform beneath them. The product adopted a different shape on 2026-08-14 (ADR-0054
in the Sanad repository) and the positioning settled on 2026-09-08 makes the old framing
unusable. This ADR records the choice against ADR-0001 (this repository is the naming
authority) and ADR-0002 (the methodology is the asset, not the product taxonomy).

---

## The decision, in one sentence

> **Sanad is the Ejadah Engineering Intelligence Platform.**

Stated in full, as every surface must state it:

> **Sanad is an Engineering Intelligence Platform that generates, validates and governs the
> digital thread of a product, keeping requirements, models, code, tests and certification
> evidence continuously aligned.**

It is **built for every engineer involved in developing a regulated product** — never one
discipline, and never "regulated systems" as the audience.

Capabilities live inside Sanad and compose through the Git repository and the graph
ontology. There is no second product, and no separate substrate to name.

## Context

The seven-workbench family was written when one product existed and the honest question was
"which discipline next". Everything decided since answers a different question: depth in one
product. Architecture, software design, verification, review and certification evidence are
now capabilities of Sanad, each a build in progress inside it, not products waiting their
turn.

At the same time the word **Platform** carried two meanings that cannot both hold. Internally
it named the discipline-invariant substrate under many workbenches — explicitly "a name for a
direction, not a shipped artefact". Externally the product is now called an Engineering
Intelligence Platform. One word, two referents, in documents that are meant to be the naming
authority.

## 1. What "Platform" means from today

**Platform** names the product. `product/Platform.md` describes the architecture of Sanad —
the repository model, the engineering graph and its ontology, the policy compiler, the
analysis runtime, the evidence currency, the question/answer contract and the AI gateway.
That architecture is unchanged; only its framing changes. It is an internal architecture
fact, not a second brand.

## 2. What replaces the family

`product/Capabilities.md` replaces `product/Product_Family.md`. It lists capability names and
the outcome each serves — **Understand · Generate · Validate · Govern** — and nothing else. It
names no file, no rule number and no product internal, per ADR-0001.

## 3. Status vocabulary

Two words are permitted for anything in Sanad: **build in progress** (it exists in the beta)
and **planned**. Nothing is called complete, built, shipping, qualified or available.

> **Nothing is called complete until its signed verification record exists.**

This binds every document in this repository, not only the product ones.

## 4. What is retired from public use

The identifiers **E-AEW · E-SWE · E-VEW · E-RVW · E-SEW · E-CEW** name nothing that exists.
They are retired from every public surface — website, marketing, product documentation,
prose. They survive only under the History heading of `product/Naming.md`, so that a reader
can see the decision was made rather than find the record silently rewritten.

`E-REW` remains the repository name and the historical release line (0.1.0–0.3.0). It has not
named the product since ADR-0054.

## Supersedes

- `product/Product_Family.md` in full (renamed to `product/Capabilities.md`).
- `product/Platform.md` §Status — "the Platform is a name for a direction, not a shipped
  artefact".
- `product/Naming.md` §The product family — the seven-workbench table, kept under History.
- `company/Mission.md` §What we do — "Build Engineering Workbenches, each covering one
  engineering discipline".
- `company/Branding.md` products row — "Sanad (shipping); E-AEW, … (planned)".
- The 2026-08-21 website hero line "requirements and engineering governance platform".

## Keeps

ADR-0001 and ADR-0002 unchanged. The four commitments, the five values, the engineering
principles, AI governance, and the composition rule: capabilities compose through the Git
repository and the graph ontology, **never a call**.

---

## Rejected alternatives

**Rejected: keep "Platform" for the substrate and call Sanad the Engineering Intelligence
Workbench.** This was the genuinely attractive option — it is ADR-0054's own descriptor, it
requires no change to this repository, and "workbench" is honest about the form (it runs
inside an editor). It was rejected because it demands the buyer learn a two-level model
before the first sentence lands, and because the substrate has no second consumer and is not
forecast to get one. A name reserved for a thing that may never exist costs every sentence
that has to route around it.

**Rejected: keep the seven-workbench family as a stated vision.** It reads as six products we
have not built. Under the honesty value that is a claim we cannot show, and it invites the
question "when is E-CEW out?" which has no truthful answer.

**Rejected: delete the family documents.** Rewriting history hides that the decision was
made, which is the policy `product/Naming.md` already applies to the "REW" conflict. The text
moves under History with a pointer here.

---

## What this forbids

- Any public surface naming E-AEW, E-SWE, E-VEW, E-RVW, E-SEW or E-CEW as a product.
- Describing Sanad as one of several workbenches, or naming a substrate beneath it.
- The words complete, built, shipping, qualified or available applied to any part of Sanad on
  any surface.
- A capability invoking another capability. Composition is files plus ontology.
- Claiming certification. We produce evidence *for* certification; the authority certifies.

**Revisit trigger:** a real customer who needs a capability delivered as a separate product,
bought and installed on its own. At that point the substrate acquires a second consumer, the
extraction bar in `engineering/Engineering_Principles.md` §4 applies, and this ADR is amended
with the customer named.
