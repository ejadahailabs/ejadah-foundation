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

And the distinction that carries the most weight of any sentence we write:

> **Requirements tools, MBSE tools and ALM tools manage artifacts. Sanad manages and
> validates the relationships between artifacts.**

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

## 2. Why we rejected the workbench family

The fact is recorded below under *Rejected alternatives*. The reasoning belongs here,
because it is what a future reader will need when the family looks tempting again.

**One product is easier to understand.** A buyer should never have to learn seven names
before understanding what we make. Seven names is a taxonomy lesson standing between the
reader and the first useful sentence.

**One product is easier to deploy.** One extension, one setup, one version, one licence. A
family means the customer decides which pieces they have, and every support conversation
starts by establishing that.

**One product is easier to market.** Every surface says one thing. A family divides the
message seven ways and each share is too small to land.

**Capabilities can evolve independently without becoming products.** A capability may be
deep or shallow, ahead or behind, and may be retired — none of which requires a name, a
release line, a price or a commitment to a customer. Making it a product freezes all of
that on the day it is named.

**Customers buy outcomes, not internal architectural partitions.** The discipline split
between requirements, architecture, software, verification, review and certification is our
map of the work, not the customer's. What they buy is the digital thread of their product
generated, validated and governed. Selling them our internal partition asks them to pay for
our org chart.

## 3. What replaces the family

`product/Capabilities.md` replaces `product/Product_Family.md`. It lists capability names and
the outcome each serves — **Understand · Generate · Validate · Govern** — and nothing else. It
names no file, no rule number and no product internal, per ADR-0001.

## 4. The two halves of the sentence are coupled

**Never write "Sanad is an Engineering Intelligence Platform." on its own.** The sentence
always continues "…that generates, validates and governs the digital thread of a product".

*Engineering Intelligence* is a category we coined; a reader has no prior meaning for it and
will supply one of their own. *Digital thread* is recognised vocabulary and carries an exact
meaning. Each half carries the other: the coined term is what makes the claim ours, the
recognised term is what makes it legible. Split them and one sentence says nothing and the
other says something we did not mean.

## 5. Status vocabulary

Two words are permitted for anything in Sanad: **build in progress** (it exists in the beta)
and **planned**. Nothing is called complete, built, shipping, qualified or available.

> **Nothing is called complete until its signed verification record exists.**

This binds every document in this repository, not only the product ones.

## 6. What is retired from public use

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
- Writing "Sanad is an Engineering Intelligence Platform." without the rest of the sentence.
- The words complete, built, shipping, qualified or available applied to any part of Sanad on
  any surface.
- A capability invoking another capability. Composition is files plus ontology.
- Claiming certification. We produce evidence *for* certification; the authority certifies.

**Revisit trigger:** a real customer who needs a capability delivered as a separate product,
bought and installed on its own. At that point the substrate acquires a second consumer, the
extraction bar in `engineering/Engineering_Principles.md` §4 applies, and this ADR is amended
with the customer named.
