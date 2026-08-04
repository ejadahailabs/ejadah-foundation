# Mission

> **Transform engineering using AI, deterministic governance, evidence-driven
> engineering, and autonomous engineering workflows.**

> ### On the wording: "engineering", not "verification"
>
> The original charter read *evidence-driven **verification***. Corrected 2026-08-04,
> because it understated the system.
>
> "Verification" carries two meanings, and we ship a product named after one of them.
> As a **discipline** it means testing and coverage — E-VEW, one workbench. As an **act**
> it means checking that a claim holds — everything. The sentence meant the second; beside
> a product called E-VEW it reads as the first, and so promises evidence only where tests
> live.
>
> **Evidence is the currency of every artifact, not one discipline's output.** A
> requirement's weak wording, a broken trace, an unmitigated hazard and a drifted
> implementation all carry the same provenance and the same byte-identical reproducibility
> as a coverage number. Every analysis emits into one currency — `Finding` and `Metric` —
> and verification is one contributor among eleven, privileged nowhere in the pipeline.

## What we do

Build Engineering Workbenches — each covering one engineering discipline, each a
complete product on its own, all sharing one substrate.

## The four commitments

**1. Deterministic before intelligent.** Every claim a product makes is reproducible.
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
