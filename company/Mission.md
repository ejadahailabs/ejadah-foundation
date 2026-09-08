# Mission

> **Transform engineering using AI, deterministic governance, evidence-driven
> engineering, and autonomous engineering workflows.**

## What we do

> **Sanad is an Engineering Intelligence Platform that generates, validates and governs the
> digital thread of a product, keeping requirements, models, code, tests and certification
> evidence continuously aligned.**

It is **built for every engineer involved in developing a regulated product** — requirements,
systems, software, verification, review and certification engineers, and the authority's
designated reviewers who sign. Never one discipline, never "regulated systems" as the
audience.

One product. Capabilities live inside it and are listed in
[../product/Capabilities.md](../product/Capabilities.md). Sanad is a **build in progress**,
released as a free beta; nothing in it is called complete until its signed verification
record exists ([ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md)).

## The four commitments

**1. Deterministic before intelligent.** Every claim the product makes is reproducible.
AI may propose; only deterministic analysis attests. A number on a safety dashboard is
either provable or absent — never estimated.

**2. Evidence, not opinion — for every artifact.** Output carries its provenance: which
nodes, which rule, which producer, which commit. A report that cannot be regenerated
byte-identically is not evidence.

This applies to requirements, architecture, design, code, reviews and certification
artefacts alike. Evidence is not something the verification stage produces at the end; it
is what every stage produces continuously. An organisation that can only evidence its
tests has evidence for the last mile of engineering and none for the decisions that
determined it.

**3. Honest silence over confident error.** Where the data does not support an answer,
we say so and state why. A confidently wrong number on a certification artefact is the
worst thing we could ship.

**4. The repository is the truth.** Engineering data lives in Git, in formats that
outlive us. No proprietary store, no lock-in, no artefact a customer cannot read
without our software.

## How we measure ourselves

Not by features shipped. By **deterministic engineering questions made answerable** —
questions a team could not previously answer at all, or could only answer by hand.

If a proposed capability makes no new question answerable, it probably should not exist.

---

## History

### On the wording: "engineering", not "verification"

The original charter read *evidence-driven **verification***. Corrected 2026-08-04, because
it understated the system.

"Verification" carries two meanings. As a **discipline** it means testing and coverage. As an
**act** it means checking that a claim holds — everything. The sentence meant the second; at
the time we also planned a product named for the first, which made it read as the narrower
meaning and so promised evidence only where tests live.

**Evidence is the currency of every artifact, not one discipline's output.** A requirement's
weak wording, a broken trace, an unmitigated hazard and a drifted implementation all carry
the same provenance and the same byte-identical reproducibility as a coverage number. Every
analysis emits into one currency — `Finding` and `Metric` — and verification is one
contributor among many, privileged nowhere in the pipeline.

### What we do — superseded 2026-09-08

This section read: "Build Engineering Workbenches — each covering one engineering discipline,
each a complete product on its own, all sharing one substrate." Superseded by
[ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md): one product, capabilities inside it,
no substrate to name. The workbench identifiers are recorded in
[../product/Naming.md](../product/Naming.md) §History.
