# Work Tracking — every change is a Work Item

Derived from **APDS** (the Work Item Model and the **APDS digital thread**), adapted for
Ejadah and self-contained here so no repository references another company's governance.
Within Ejadah, this document is the authority; on conflict with anything else here, the
foundation wins.

> **Two different threads, and they must not be confused.** The **APDS digital thread** is
> the trail of our own work — which item derives from which, what implements it, what
> verifies it. The **digital thread of a product** is what Sanad generates, validates and
> governs for a customer: requirements, models, code, tests and certification evidence,
> continuously aligned. This document governs the first. Say "APDS digital thread" whenever
> the internal one is meant.

## The rule

> **Git is truth. GitHub is execution.**
> Anything governed, versioned or audited is a file in a repository. Anything being
> *coordinated* is a Work Item — a GitHub Issue in the repository whose code it changes.
> Never put decisions, architecture or standards into Issues; Issues track work, not truth.

**No change without a Work Item.** A commit that is not traceable to a Work Item is
untracked work — allowed only for trivial mechanical fixes (typos, formatting), and even
then the commit message says why no item exists.

## The Work Item

Every item — whatever its type — carries the same fields:

| Field | Meaning |
|---|---|
| `type` (label) | flat, open set: `feature` · `defect` · `decision` · `verification` · `doc` · `debt` · `ops` |
| `intent` | the outcome this delivers, one sentence |
| `owner` | the single accountable owner |
| `executor` | who/what performs it — human or agent, **assigned, never assumed** |
| `relations` | thread verbs, in the body (below) |
| `acceptance_criteria` | how "done" is judged — written **before** work starts |
| `evidence` | link to proof at close: gate output, commit SHA, test run, measurement |

> **An item may not close without evidence.** "Done" is a claim; evidence is what makes
> it a fact. This is Evidence First applied to our own work, not only our product's.

## The thread verbs — the only allowed link vocabulary

| Verb | Meaning |
|---|---|
| `derives_from` | exists because of that (intent lineage) |
| `implements` | realizes that |
| `verifies` | provides acceptance evidence for that |
| `depends_on` | blocked by that |
| `owned_by` | accountable to that |
| `generated_by` | produced by that work/process |
| `supersedes` | replaces that |
| `amends` | formally changes that without replacing it |

Containment (`parent` / sub-issues) is structure, not a thread verb. The set is closed:
a new verb is a governance change to this document, never an improvisation.

## The hierarchy — containment is native, not a verb

Items nest four deep, using GitHub's own sub-issue links rather than any thread verb:

```
Product  →  Epic  →  Feature  →  Task
```

A Product is the top; Epics are its goals; Features are releasable slices; **Tasks are the
leaves — the only thing an executor runs.** A task hangs off a feature, never directly off
an epic. Containment is structure; the thread verbs above are lineage. Keeping the two
apart is what lets a board be a pure projection — nesting comes from sub-issue links,
meaning comes from the verbs, and neither is re-authored anywhere else.

## In practice

**In an issue body**, the lineage verbs sit in the APDS digital-thread block, and a dedicated
`Depends-on:` line carries the blockers the daemon reads to decide eligibility:
```
implements: #12
derives_from: adr/ADR-0041
Depends-on: #9
```

**A task also carries a Lifecycle checklist** — claimed → implemented → self-tested → PR
opened → reviewed → CI green → merged → evidence recorded → closed. The executor ticks
what it does; the daemon ticks what it can observe (PR opened, CI green, merged, closed).

**A PR references its item** (`implements #12`, `closes #12`); merging it is the
`implements` edge, and the review run linked at close is the `verifies` edge.

## The mechanism is replaceable; this document is not

How these rules are *run* — the task template and its Lifecycle, the board tool, the
daemons that derive status and land PRs, the queue, the executor identifiers — is the
organisation's **Control Center operating model**, a mechanism that may be rewritten as
the organisation learns. This document is the authority it must conform to; where they
differ, the mechanism changes. Other repositories reference this; none depend on it.

## Scope

Applies to every Ejadah repository: E-REW (the Sanad repository), EPS, ejadah-website,
this foundation, and any repository added later. Each repository's board (PROGRAM_BOARD or Projects view) is a
**projection** of its Work Items — never a second place where truth lives.
