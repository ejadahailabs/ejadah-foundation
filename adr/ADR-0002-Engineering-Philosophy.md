# ADR-0002 — Engineering Philosophy as a Strategic Asset

**Adopted 2026-08-04.**

## Decision

> **The methodology is treated as a first-class company asset, on the same footing as
> the software: documented, versioned, taught, and defended.**

Six principles, recorded in `engineering/Engineering_Principles.md`: evidence-first
engineering, compiled governance, deterministic AI subordination, extraction by proof,
measurable technical debt (the Ratchet Principle), single-SHA reproducibility.

## Context

The methodology was **not designed up front**. It was extracted from what repeatedly
worked while building E-REW — each principle traceable to a specific decision, and
several to a specific defect that motivated them.

That origin is why it is worth protecting. It is not a set of opinions about good
engineering; it is a record of what survived contact with a real product in a regulated
domain.

## Why this is the durable advantage

Every individual feature we ship is implementable by a competent team with a coding
assistant. Features are not defensible.

What is hard to copy is the **interlock**:

- evidence-first makes output **defensible**;
- compiled governance makes it **consistent**;
- AI subordination keeps it **honest** as model capability grows;
- extraction by proof and the ratchet keep the codebase **movable**;
- single-SHA reproducibility makes it **certifiable**.

Remove one and the others weaken. A competitor can copy a feature in a sprint. Reproducing
the interlock requires making the same mistakes we made, in the same order.

## Consequences

**It gets written down before it is needed.** A methodology that lives only in the heads
of the people applying it is not an asset.

**It constrains us.** Adopting these as company principles means declining work that
violates them — including profitable work. That is the point; a principle abandoned under
commercial pressure was a preference.

**It is a product surface.** Training, certification-readiness consulting, process packs
and enterprise offerings all derive from it. Some of what is documented here will
eventually be sold, not just applied.

## Rejected alternatives

**Rejected: leave it implicit.** It survives only while the people who formed it are
present, and cannot be taught, sold, or defended as IP.

**Rejected: publish it openly now.** Premature. It is our clearest differentiator while
E-REW has no field usage; publication is a decision to take deliberately, with commercial
intent, not by default.

**Rejected: treat it as marketing.** Marketing claims do not fail builds. These do.

**Revisit trigger:** a principle that repeatedly obstructs correct work. That is evidence
the principle is wrong, and it is amended explicitly — with its rejected alternatives —
never quietly ignored.
