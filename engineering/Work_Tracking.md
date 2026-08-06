# Work Tracking — every change is a Work Item

Derived from **APDS** (the Work Item Model and Digital Thread), adapted for Ejadah and
self-contained here so no repository references another company's governance. Within
Ejadah, this document is the authority; on conflict with anything else here, the
foundation wins.

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

## In practice

**In an issue body:**
```
implements: #12
depends_on: #9
derives_from: adr/ADR-0041
```

**In a commit message**, as trailer lines the thread can be walked from:
```
Work-Item: #12
Verifies: #12
```

**A PR** references its item; merging it is the `implements` edge; the gate run linked
at close is the `verifies` edge.

## Scope

Applies to every Ejadah repository: E-REW, EPS, ejadah-website, this foundation, and
all future products. Each repository's board (PROGRAM_BOARD or Projects view) is a
**projection** of its Work Items — never a second place where truth lives.
