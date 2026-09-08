# Naming

**Authoritative.** Where any document, diagram, marketing asset or repository disagrees
with this file, this file is correct and the other is a defect.

---

## Company, product, capabilities

| Level | Name | Short form |
|---|---|---|
| Company | **Ejadah AI Labs** | Ejadah |
| Product | **Sanad**, the Ejadah Engineering Intelligence Platform | Sanad |
| Inside the product | **capabilities** — named in [Capabilities.md](Capabilities.md) | capability |

There is one product. Capabilities are not products, are not sold separately, and never
carry a product identifier of their own
([ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md)).

## The sentence every surface aligns to

> **Sanad is an Engineering Intelligence Platform that generates, validates and governs the
> digital thread of a product, keeping requirements, models, code, tests and certification
> evidence continuously aligned.**

Short form, for a hero, a footer or a meta description: **Sanad generates, validates and
governs the digital thread of a regulated product.**

Audience, written this way everywhere: **built for every engineer involved in developing a
regulated product.** Never one discipline, never "regulated systems" as the audience.

`E-REW` names the repository and the historical release line (0.1.0–0.3.0). It has not named
the product since ADR-0054 (2026-08-14). In prose about the product, always **Sanad**.

## Naming rules

**1. "Engineering Intelligence" names the product, never a component.** No module,
directory, layer or class may contain "intelligence". A box with that name collects
whatever nobody else wants to own. Architecturally enforced.

**2. Never name a component for a discipline if it is meant to be shared.** A shared
component called `RequirementGraph` cannot serve architecture without lying about itself.
Shared things take discipline-neutral names — `Artefact`, not `Requirement`.

**3. Do not call a contract an SDK.** Naming drives architecture: call something an SDK
and someone will export it, document it, and then be unable to change it.

**4. Repositories are lowercase, products are uppercase.** A filesystem convention and a
brand are different things. The `E-REW` repository predates the rule and keeps its name; the
product it holds is **Sanad**.

**5. A name that promises completeness must be earned.** Nothing is called "complete",
"full", "total" or "100 %" unless it is provable. On Sanad the permitted words are **build in
progress** and **planned** — nothing is called complete until its signed verification record
exists.

**6. Use the vocabulary of the guidance, not our own.** DO-178C, DO-330, ARP4754A, ISO 26262,
INCOSE and SysML v2 supply the words for requirements, design, verification, review and
configuration management. Where one of them has a term, we use it and do not coin a synonym.

---

## History

Deleting superseded text would hide that a decision was made. The record stays.

### The product family — withdrawn 2026-09-08

Until [ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md) this file named a **Platform**
(the Ejadah Engineering Intelligence Platform, a shared substrate) and a **Product**
(*Engineering Workbench*, one per discipline), with seven identifiers:

| ID | Name | Discipline |
|---|---|---|
| **E-REW** | Requirements Engineering Workbench | requirements, traceability, SRS/HLR/LLR, reviews, impact |
| **E-AEW** | Architecture Engineering Workbench | architecture, ADRs, interfaces, design decisions |
| **E-SWE** | Software Engineering Workbench | source analysis, **reverse engineering**, refactoring, dependencies |
| **E-VEW** | Verification Engineering Workbench | verification, coverage, quality gates, evidence |
| **E-RVW** | Review Engineering Workbench | reviews across disciplines, disposition, review metrics |
| **E-SEW** | Systems Engineering Workbench | MBSE, SysML, functional analysis, allocation |
| **E-CEW** | Certification Engineering Workbench | DO-178C, ISO 26262, IEC 61508, ARP4754, evidence packages |

The convention was `E-` plus three letters, uppercase, hyphenated.

**E-AEW, E-SWE, E-VEW, E-RVW, E-SEW and E-CEW are retired from public use.** They name
nothing that exists. Each discipline they described is a capability of Sanad, listed in
[Capabilities.md](Capabilities.md) as a build in progress or as planned. Where a historical
document uses one of these identifiers, read it as that capability.

An intermediate step is also on the record: ADR-0054 (2026-08-14, product repository) renamed
the product from `E-REW` to **Sanad**, descriptor "Sanad — Engineering Intelligence
Workbench", and replaced the family with one product organised into capability packs (Sanad
Requirements, Sanad Interfaces, Sanad Data Dictionary, Sanad Concepts, Sanad Verification,
Sanad Drift). Those pack names no longer match the product; the current names are in
[Capabilities.md](Capabilities.md), and the descriptor is now *Engineering Intelligence
Platform*, not *Workbench*.

### Resolved conflict — "REW"

⚠️ **Historical documents expand REW as "Reverse Engineering Workbench".** That is
**withdrawn**. `future/Future_Vision.md` in the product repository, written before the
product family was settled, uses that expansion throughout.

| | |
|---|---|
| **Correct** | **E-REW = Requirements Engineering Workbench** — the repository name and the historical release line |
| Withdrawn | REW = Reverse Engineering Workbench |
| Reverse engineering belongs to | discovery inside Sanad — a fact producer, not a product |

**Why this matters beyond tidiness:** the two readings imply different products. A
reverse-engineering tool starts from code and recovers intent; Sanad starts from intent and
governs everything downstream, and reverse engineering enters it as *one fact producer among
many* feeding the graph — a module, not a product identity.

Historical documents keep their original text (rewriting history hides that the decision was
made). They carry a correction note pointing here.
