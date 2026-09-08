# Engineering Principles

> **This document is the company's primary intellectual property.**
>
> The code can be rewritten. This methodology is what gives Sanad its identity, and it was
> not designed up front — it was extracted from what repeatedly worked while building it.
> Treat it as a strategic asset: the basis of IP, training, enterprise offerings and
> hiring, alongside the software.

Ten principles. Each states a rule, why it exists, and how it is enforced — an
unenforced principle is a preference.

Principles 1–6 were recorded by [ADR-0002](../adr/ADR-0002-Engineering-Philosophy.md) on
2026-08-04. Principles 7–10 were adopted in practice over the months after and written down
on 2026-09-08; they were rules the organisation already ran on, living only in conversation,
which is exactly the failure ADR-0002 exists to prevent.

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

## 7. The vocabulary of the guidance, not our own

> Where a standard has a word for it, we use that word.

DO-178C, DO-330, ARP4754A, ISO 26262, INCOSE and SysML v2 name requirements, design,
verification, review, configuration management and qualification. We use their terms in
documents, in the product surface and in code identifiers, and we do not coin a synonym
because ours reads better.

**Why:** our reader is an engineer who is accountable under one of those standards. An
invented term forces them to translate before they can trust, and a term we invented cannot
be cited in an argument with an authority. It also hides gaps: a coined word can mean
whatever the writer needed it to mean that day.

**Enforced by:** a terminology map in the product repository's qualification set, and by
review — a new term is a defect unless the map shows no standard supplies one.

---

## 8. The organisation configures; we recommend

> Every rule the product applies is chosen by the organisation using it. We ship
> recommendations, never settings.

Rule packs, criticality bands, profiles, thresholds and templates are staged per capability
and adopted deliberately. Nothing is enabled because we thought it sensible.

**Why:** a rule the customer did not choose is a rule they cannot defend to an authority, and
the first finding it produces that they disagree with switches the whole tool off. Their
process is theirs; we make it enforceable, not ours.

**Enforced by:** compiled governance (principle 2) — configuration is data, resolved once, and
a default that cannot be traced to an organisation's choice is a defect.

---

## 9. Requirements are the source of truth

> When code and requirement disagree, the code is wrong.

The direction is strictly top-down: requirements, then design, then implementation, then
verification evidence. Code changes to meet the requirement. A requirement changes only by
being changed deliberately, as its own decision, before the work that depends on it starts.

**Why:** the reverse — adjusting the requirement to match what was built — produces a document
set that agrees with itself and describes nothing anyone decided. It is undetectable
afterwards, and it is the failure certification evidence exists to make impossible.

**Enforced by:** traceability with coverage; an implementation with no requirement above it,
or a requirement edited to match a merged change, fails review.

---

## 10. Design first, then implement — verified by someone else

> No line of code before the design is complete, and no feature is done on the word of
> whoever built it.

A feature is design-complete when its system and high-level requirements are written, its
design decision is recorded with rejected alternatives, its tests are specified, and no
question is open. Only then does implementation start. Implementation and verification are
performed by different parties, and the feature closes on a signed record, not an assertion.

**Why:** design questions answered mid-implementation are answered by whatever is cheapest to
type. And a party verifying its own work verifies its own assumptions along with it — the
independence requirement in the guidance is not bureaucracy, it is the only thing that
catches a misunderstanding shared by author and code.

**Enforced by:** the qualification set in the product repository, written to DO-330: one
record per feature, carrying the requirements, the design decision, the test specification,
the verification result and the signature. **Nothing is called complete until that record is
signed.**

---

## How these compose

1 and 6 make output **defensible**. 2 and 8 make it **consistent** and the customer's own.
3 keeps it **honest** as AI capability grows. 4 and 5 keep the codebase **movable**. 7 keeps
it **legible** to the engineer who has to defend it. 9 and 10 keep the thread pointing one
way, so what is built is what was decided.

Remove any one and the others weaken. That interlock, not any single rule, is the asset.
