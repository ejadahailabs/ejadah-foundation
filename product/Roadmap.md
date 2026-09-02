# Roadmap

> Company-level. Product milestones live in each product repository.
> **Triggers, not dates.** A date we cannot honour is a promise we should not make.

## Now

| | |
|---|---|
| **Shipping** | Sanad (repository: E-REW) — requirements, traceability, quality, impact, dashboards |
| **Adopted** | Platform topology · single-repository strategy · workbench interoperability |
| **Enforced** | Headless core · kernel seam ratchet, in CI |
| **Established** | This constitution |

## Next — Sanad depth, not product breadth

The strategic question is not "which workbench next" but **"is Sanad indispensable to
one real team yet"**. Until that is yes, a second workbench divides attention across two
half-products.

Priority order:

1. **Field use.** Real repositories, real engineers, findings they act on. Nothing on
   this roadmap outranks it.
2. **The time axis.** Impact-on-diff, baselines, run-to-run comparison — comparing two
   runs at two commits. This is the single largest unlock: it turns point-in-time
   analysis into *drift detection*, which is the vision's central capability.
3. **Producers, not products.** A code index, a coverage importer, a requirements-tool
   importer. Each makes existing engines answer more without adding a product.

## The trigger for workbench #2

> **A real user waiting for it.** Not an interesting one.

At that moment, and not before: rename to the ecosystem repository, extract the kernel
into a package, and add the second product beside Sanad. The extraction is a directory
move plus a mechanical rename — the seam is already measured.

## Later, in dependency order

| Capability | Depends on |
|---|---|
| Drift detection across disciplines | the time axis + producers |
| Process packs (DO-178C, ISO 26262, ASPICE) | rule pack grammar at scale |
| Methodologies distributed as packages | process packs proven internally |
| Multi-host (CLI, web, cloud, REST) | a customer who cannot use an editor |
| Enterprise server | multi-user demand we have actually met |

## What we will not do

- Build the Platform before a second consumer needs it.
- Create repositories for products with no users.
- Ship a capability whose output cannot be defended.
- Promise dates for work whose trigger has not fired.
