# Naming

**Authoritative.** Where any document, diagram, marketing asset or repository disagrees
with this file, this file is correct and the other is a defect.

---

## Company, platform, product

| Level | Name | Short form |
|---|---|---|
| Company | **Ejadah AI Labs** | Ejadah |
| Platform | **Ejadah Engineering Intelligence Platform** | the Platform |
| Product | **Engineering Workbench**, one per discipline | workbench |

## The product family

| ID | Name | Discipline |
|---|---|---|
| **E-REW** | Requirements Engineering Workbench | requirements, traceability, SRS/HLR/LLR, reviews, impact |
| **E-AEW** | Architecture Engineering Workbench | architecture, ADRs, interfaces, design decisions |
| **E-SWE** | Software Engineering Workbench | source analysis, **reverse engineering**, refactoring, dependencies |
| **E-VEW** | Verification Engineering Workbench | verification, coverage, quality gates, evidence |
| **E-RVW** | Review Engineering Workbench | reviews across disciplines, disposition, review metrics |
| **E-SEW** | Systems Engineering Workbench | MBSE, SysML, functional analysis, allocation |
| **E-CEW** | Certification Engineering Workbench | DO-178C, ISO 26262, IEC 61508, ARP4754, evidence packages |

Every ID is `E-` plus three letters, uppercase, hyphenated. No exceptions, no aliases.

---

## Resolved conflict — "REW"

⚠️ **Historical documents expand REW as "Reverse Engineering Workbench".** That is
**withdrawn**. `future/Future_Vision.md` in the E-REW repository, written before the
product family was settled, uses that expansion throughout.

| | |
|---|---|
| **Correct** | **E-REW = Requirements Engineering Workbench** |
| Withdrawn | REW = Reverse Engineering Workbench |
| Reverse engineering belongs to | **E-SWE** |

**Why this matters beyond tidiness:** the two readings imply different products. A
reverse-engineering tool starts from code and recovers intent; a requirements workbench
starts from intent and governs everything downstream. The adopted architecture is the
second, and reverse engineering enters it as *one fact producer among many* feeding the
graph — a module, not a product identity.

Historical documents keep their original text (rewriting history hides that the decision
was made). They carry a correction note pointing here.

---

## Naming rules

**1. "Engineering Intelligence" names the product, never a component.** No module,
directory, layer or class may contain "intelligence". A box with that name collects
whatever nobody else wants to own. Architecturally enforced.

**2. Never name a component for a discipline if it is meant to be shared.** A shared
component called `RequirementGraph` cannot serve architecture without lying about itself.
Shared things take discipline-neutral names — `Artefact`, not `Requirement`.

**3. Do not call a contract an SDK.** Naming drives architecture: call something an SDK
and someone will export it, document it, and then be unable to change it.

**4. Repositories are lowercase, products are uppercase.** `e-rew` the repository,
**E-REW** the product. The first is a filesystem convention; the second is the brand.

**5. A name that promises completeness must be earned.** Nothing is called "complete",
"full", "total" or "100 %" unless it is provable.
