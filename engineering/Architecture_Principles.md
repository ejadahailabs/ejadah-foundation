# Architecture Principles

## 1. Core and rim, never a tower

A pipeline core with adapters at the rim. Adapters — editor integrations, report
projections, AI skills, enterprise integrations — point **inward** and are individually
deletable. Nothing in the core knows an adapter exists.

**Rejected permanently:** layering AI or the editor into the mandatory execution path.
That inverts dependency direction and makes basic function impossible without optional
components.

## 2. Facts and meaning are different layers

The model holds **facts** — what the sources say, uninterpreted, 1:1. The graph holds
**meaning** — the single place a declared role becomes a typed edge.

**Why:** semantics assigned upstream produce two interpreters and an invalidation problem
on every save. Interpret once, downstream.

## 3. The contract is the abstraction; the instance is disposable

What is central is the *contract* — the owned ontology and its query surface. The
compiled instance is rebuilt per run and trustworthy **because** it cannot outlive the
files it came from.

**Rejected permanently:** a persistent or authoritative graph store, under any name.
Centres attract persistence, persistence attracts authority, and an authoritative store
is a second source of truth. Git remains the only one.

## 4. Query roles, never field names

We define no metadata schema. Each repository's templates declare their own fields, and
a field may carry a *role* saying what it means. Analysis resolves through roles.

**Why:** it is what lets a customer keep their own vocabulary and still get full
analysis with zero configuration.

## 5. An undeclared role disables the analysis that needs it

No hazard role means **no safety findings** — never "100 % hazard coverage". Silence with
a stated reason is the only honest answer.

## 6. Plugin-grade or not built

Every capability owns its contracts, tests, docs and configuration, and is removable
with no changes elsewhere. If it cannot be deleted cleanly, it is not finished.

## 7. Extension through data, not code

Third parties extend by **declaring**: rule packs, templates, role declarations. Only
first-party code is loaded.

**Why:** a customer repository is untrusted input. Executing code found inside one is
not a feature.

## 8. Do not generalise ahead of demand

Two engines before eleven. One workbench before six. Direction documents are direction —
never a licence to build abstraction now.

## 9. No component named "intelligence"

A box with that name collects whatever nobody else wants to own. The *product* carries
the name; no component does.

---

## The guardian questions

Before building anything, answer these. **A "no" means stop and redesign — not proceed
and refactor later.**

- Is the capability plugin-grade?
- Does dependency direction still point strictly downward?
- Does it add coupling a contract could have avoided?
- Does it introduce hidden state or a second source of truth?
- Is the decidable part testable without a UI?
- Is the decision recorded with its rejected alternatives?
- **Which new deterministic engineering questions does this make answerable?**

The last one is the strongest filter. If the answer is none, the feature probably should
not exist.
