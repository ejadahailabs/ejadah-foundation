# Roadmap

> Company-level. Product milestones live in each product repository.
> **Triggers, not dates.** A date we cannot honour is a promise we should not make.

**Status vocabulary is two words:** *build in progress* — it exists in the beta — and
*planned*. Nothing is complete, built, shipping, qualified or available.
**Nothing is called complete until its signed verification record exists.**

## Now — Sanad, a build in progress

| | |
|---|---|
| **Build in progress** | Sanad (repository: E-REW) — the thirteen capabilities in [Capabilities.md](Capabilities.md), released as a free beta inside VS Code and on the command line |
| **In the beta** | Requirements authoring and explorer · engineering graph and ontology · traceability and impact · rule packs with findings · test coverage per requirement · SysML v2 design canvas · reports and certification evidence · baselines and drift · review records · AI that proposes and asks |
| **Adopted** | One product, one Platform ([ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md)) · Git as the only truth · single-repository strategy · the organisation configures every rule, we recommend |
| **Enforced** | Headless core · kernel seam ratchet, in CI · design before implementation, with independent verification per feature |
| **Under way beside the product** | The qualification set in the product repository, written to DO-330 · licensing and identity (EPS) for the transition out of beta · beta terms |
| **Established** | This constitution |

Nothing in that table is complete. The beta is well short of it, and says so on every
surface.

## Next — the nine capabilities

Depth in one product, in the priority order set on 2026-09-06. Each is *planned*; each is
described in [Capabilities.md](Capabilities.md).

| # | Capability | Trigger |
|---|---|---|
| 1 | Function catalogue | the graph carries requirements, design and verification — it does, so this is the next thing started |
| 2 | Capability discovery | functions exist as graph nodes for discovery to recover into |
| 3 | AI planning mode | discovery can supply the gaps the planner asks about |
| 4 | Interface change analysis | interfaces carry enough structure that a change can be resolved to affected items |
| 5 | Architecture rule checking | the function and interface layers exist to be checked |
| 6 | Verification closure | verification evidence is attached to cases, not only to requirements |
| 7 | Baseline management | configuration management proves out over a real programme's history |
| 8 | Decision-record intelligence | decision records carry links a query can follow |
| 9 | Maturity tracking | the eight above supply the evidence maturity would be derived from |

Above all of them, unchanged in rank: **field use.** Real repositories, real engineers,
findings they act on. Nothing on this roadmap outranks it.

## Later, in dependency order

| Capability | Depends on |
|---|---|
| Drift detection across disciplines | the time axis + producers |
| Process packs (DO-178C, ISO 26262, ASPICE) | rule pack grammar at scale |
| Methodologies distributed as packages | process packs proven internally |
| Multi-host (web, cloud, REST) | a customer who cannot use an editor or the command line |
| Enterprise server | multi-user demand we have actually met |

## What we will not do

- Name a second product, or a substrate beneath Sanad, before a real customer needs a
  capability delivered separately ([ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md)).
- Create repositories for products with no users.
- Ship a capability whose output cannot be defended.
- Call anything complete before its verification record is signed.
- Promise dates for work whose trigger has not fired.

---

## History

Until 2026-09-08 this document listed Sanad as *shipping*, listed "Platform topology and
workbench interoperability" as adopted, framed Next as "Sanad depth, not product breadth"
against the question "which workbench next", and carried a section headed *The trigger for
workbench #2*. Superseded by
[ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md): there is no workbench #2, and
nothing in Sanad ships until its verification record is signed.
