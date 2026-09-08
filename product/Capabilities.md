# Capabilities

Sanad is one product. Capabilities live inside it. See
[../adr/ADR-0003-One-Product-One-Platform.md](../adr/ADR-0003-One-Product-One-Platform.md).

This document names capabilities and the outcome each serves. It names no file, no rule
number and no product internal — those belong in the product repository (ADR-0001).

## The four outcomes

| Outcome | What the engineer gets |
|---|---|
| **Understand** | Read what the repository already holds — requirements, models, architecture, code, tests — as one connected thread. |
| **Generate** | Draft the artifacts with built-in tools, so the thread is created rather than transcribed. |
| **Validate** | Check every artifact against the rest of the thread: consistency, coverage, traceability, drift. |
| **Govern** | Hold the line over time: baselines, reviews, gates, certification records. |

A capability often serves more than one outcome. The group below names its primary one.

## Build in progress

Everything here exists in the beta and is a build in progress. **Nothing is called complete
until its signed verification record exists.**

| Capability | What it does | Outcome | Status |
|---|---|---|---|
| **Graph** | Turns the files in the repository into one connected engineering graph with a declared ontology. | Understand | build in progress |
| **Workspaces** | Sets up a repository for Sanad and holds the organisation's own configuration of every rule. | Understand | build in progress |
| **Traceability** | Follows a link in either direction — what a requirement affects, and what proves it. | Understand | build in progress |
| **Requirements** | Authors and organises requirements, with standard requirement patterns offered as you write. | Generate | build in progress |
| **System design** | Captures the system-level design — functions, interfaces, allocation — as files in the repository. | Generate | build in progress |
| **Software design** | Captures the software design and its relationship to the requirements above it and the code below. | Generate | build in progress |
| **Design canvas** | Draws SysML v2 diagrams from the model, and lets an engineer author the model by drawing. | Generate | build in progress |
| **Reporting** | Produces reports and certification evidence that regenerate byte-identically at a commit. | Generate | build in progress |
| **AI** | Proposes drafts, asks clarifying questions, and writes only what an engineer confirms. It never attests. | Generate | build in progress |
| **Analysis** | Runs the organisation's rule packs over the graph and reports findings with their provenance. | Validate | build in progress |
| **Verification** | Relates requirements to the tests that verify them, and reports what is covered and what is not. | Validate | build in progress |
| **Configuration** | Manages baselines and the configuration of an engineering item over time, in the repository. | Govern | build in progress |
| **Review** | Records reviews and their dispositions as evidence, alongside the artifacts reviewed. | Govern | build in progress |

## Planned

Not built. Listed in the priority order set on 2026-09-06.

| # | Capability | What it would do | Outcome | Status |
|---|---|---|---|---|
| 1 | **Function catalogue** | Make functions first-class in the graph, between requirements and architecture, so a function can be traced to what implements, realises and verifies it. | Understand | planned |
| 2 | **Capability discovery** | Recover capabilities, functions, scenarios and operational threads from supplied documents, not only requirements and interfaces. | Understand | planned |
| 3 | **AI planning mode** | Read a supplied design document, ask questions, identify gaps, agree a plan with the engineer, and generate artifacts only after approval. | Generate | planned |
| 4 | **Interface change analysis** | From a change to an interface, report the affected components, functions, simulations and tests, and produce an Interface Control Document. | Validate | planned |
| 5 | **Architecture rule checking** | Check the architecture the way requirements are checked today — unallocated functions, orphan ports, cyclic dependencies, unowned interfaces. | Validate | planned |
| 6 | **Verification closure** | Carry a requirement through verification case, evidence and closure status, so "what prevents certification today" is answerable. | Govern | planned |
| 7 | **Baseline management** | Make a baseline a graph object across requirements, design, verification and code, so two baselines can be compared natively. | Govern | planned |
| 8 | **Decision-record intelligence** | Link architecture decision records to the requirements and components they affect, so the effect of a decision is queryable. | Understand | planned |
| 9 | **Maturity tracking** | Report engineering maturity per item — defined, designed, verified, simulated — from evidence rather than a status field. | Govern | planned |

## How capabilities compose — and how they do not

> **No capability ever invokes another.** They compose through two things they already share:
> **the Git repository** and **the graph ontology**.

System design writes architecture artefacts as files with declared roles. The producers read
them as facts. The graph turns roles into typed edges. Traceability then answers questions
about architecture coverage without knowing the system design capability exists.

```
requirements  ──writes──►  ┌──────────────────────┐
system design ──writes──►  │  the Git repository  │ ──► producers ──► graph ──► answers
verification  ──writes──►  └──────────────────────┘
```

**Forbidden:** imports between capabilities, exported APIs, a shared runtime service, a
message bus, or any exchange format other than the on-disk format.

## Degradation is honest, by design

A capability whose neighbours have written nothing sees no artefacts carrying those roles.
The analyses needing them **stand down with a stated reason** — never defaulted, never
estimated, never reported as complete.

That is the same rule as the first value: silence with a stated reason beats a plausible
number.

---

## History

Until 2026-09-08 this document was `Product_Family.md`. It described seven discipline
workbenches — Sanad plus E-AEW, E-SWE, E-VEW, E-RVW, E-SEW and E-CEW — sold and built one at
a time, composing through files and ontology, with a Platform extracted from Sanad beneath
them. The lifecycle chain it drew (requirements → architecture → software → verification
evidence → certification package) is now the set of capabilities above, inside one product.

Superseded by [ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md). The composition rule
and the honest-degradation rule survived unchanged; only the things being composed changed
from products to capabilities. The workbench identifiers are recorded in
[Naming.md](Naming.md) §History.
