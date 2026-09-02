# Engineering Principles

> **This document is the company's primary intellectual property.**
>
> The code can be rewritten. This methodology is what gives the Platform its identity,
> and it was not designed up front — it was extracted from what repeatedly worked while
> building Sanad. Treat it as a strategic asset: the basis of IP, training, enterprise
> offerings and hiring, alongside the software.

Six principles. Each states a rule, why it exists, and how it is enforced — an
unenforced principle is a preference.

---

## 1. Evidence-first engineering

> A claim without provenance is an opinion. Ship answers, not opinions.

Every output identifies what produced it: which nodes, which rule, which commit. A user
must always be able to ask *"why does it say that?"* and get a mechanical answer.

**Why:** our customers are accountable to certification authorities. An answer they
cannot defend is worse than no answer, because they will defend it anyway.

**Enforced by:** findings carry rule provenance; reports are deterministic projections
of findings and metrics, never independent readings of the data.

---

## 2. Compiled governance

> Policy is resolved once, at load time. Nothing downstream re-evaluates it.

Inheritance, criticality bands, profile composition, defaults and overrides are computed
by one compiler. Engines, reports, dashboards and AI **look policy up — they never
compute it**.

**Why:** policy logic duplicated into consumers produces divergent answers to the same
question, and the divergence is invisible until an audit finds it.

**Enforced by:** a band comparison or inheritance rule inside an engine is a defect
regardless of correctness.

---

## 3. Deterministic AI subordination

> AI may propose. Only deterministic analysis attests.

AI enters through exactly two doors: skills at the rim, whose output lands as ordinary
edits a human accepts; and optional inference inside an engine, whose output is marked
inferred and rendered as a candidate for human judgement.

There is no third door, and AI never sits on a mandatory path — the product works fully
with AI deleted.

**Why:** a non-reproducible input to an evidence artefact destroys the artefact's value.
Also: models change under you, and certification evidence must not.

**Enforced by:** inferred findings carry a flag and are excluded from byte-identical
evidence. See [AI_Governance.md](AI_Governance.md).

---

## 4. Extraction by proof

> Generality is earned by a second real consumer, never granted in advance.

A component becomes shared only when it passes **all three** tests:

| Test | Question |
|---|---|
| **Discipline** | Does it survive deleting every discipline-specific noun? |
| **Second Consumer** | Is there a *named, real* second consumer — not an interesting one? |
| **Reconstruction** | Does extraction preserve single-SHA reproducibility of evidence? |

Two of three is not a pass. **Reconstruction has veto power** over the other two.

**Why:** an abstraction with one consumer is shaped by that consumer's accidents, then
frozen by the boundary drawn around it. A platform with one consumer is not a platform —
it is a layer of indirection with a hopeful name.

**Enforced by:** an extraction register recording every candidate and its test status.

---

## 5. Measurable technical debt — the Ratchet Principle

> Debt that is measured, frozen and forbidden from growing is under control. Debt
> described in prose is not.

Where the right fix is real but premature, we do not choose between a refactor nobody
asked for and a comment nobody reads. We **count the violations, freeze the count, and
fail the build if it rises.**

**Why:** it separates *knowing* from *fixing*. The count is an honest statement of
distance from the goal; when the work is finally scheduled, the baseline is the worklist.

**Design rules learned the hard way:**
- Ratchet on **counts per file**, not line numbers — line numbers drift, and a check
  that cries wolf is a check somebody deletes.
- Regenerate the baseline through the **checker's own code path**. A baseline produced
  by a second copy of the matching logic is how a ratchet quietly stops ratcheting.
- Lowering the number is a celebration. Raising it is a defect.

---

## 6. Single-SHA reproducibility

> The repository is the unit of deterministic reconstruction until proven otherwise.

One commit must reproduce the entire toolchain that produced an evidence artefact.

**Why:** "regenerates byte-identically at a commit" is meaningless if half the producing
code lives at another SHA behind a lockfile. This is why repository layout is a
**deployment** concern that may never be answered with an architectural change — and why
anything that would split reconstruction carries the burden of proof.

**Enforced by:** the extraction bar's third test, which vetoes.

---

## How these compose

1 and 6 make output **defensible**. 2 makes it **consistent**. 3 keeps it **honest** as
AI capability grows. 4 and 5 keep the codebase **movable** — able to become a platform
without having to guess in advance what the platform is.

Remove any one and the others weaken. That interlock, not any single rule, is the asset.
