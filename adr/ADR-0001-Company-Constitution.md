# ADR-0001 — The Company Constitution

**Adopted 2026-08-04.**

## Decision

> **`ejadah-foundation` is the single authoritative source of organisational standards.
> Everything references it. Nothing depends on it.**

No product code. Ever.

## Context

Company-scope governance — principles, standards, naming, philosophy — had accumulated
inside a *product* repository, because that was the only repository that existed. It
worked with one product and gets worse with every product added: either the text is
duplicated (and diverges) or later products import from a peer product (and inherit its
lifecycle).

## The asymmetry, and why it is the whole design

| Permitted | Forbidden |
|---|---|
| Any repository may **link** here | Any repository **building** against this |
| Any repository may **copy a template** as a starting point | Any repository **vendoring** a standard |

A repository that could break because this one changed makes this repository a
deployment coupling — and then ten repositories cannot move without a release here. It is
stable precisely because nothing downstream can break.

**Test:** deleting this repository must break no build anywhere. It would cost the
organisation its memory, not its ability to ship.

## Rejected alternatives

**Rejected: keep governance in the product repository.** Forces later products to depend
on a peer product for company standards, inheriting its release cadence and its
lifecycle. Also misrepresents scope — company principles are not E-REW's property.

**Rejected: nine flat files.** The charter's original list. Flat structures give no
signal about *rate of change* — Vision moves on a decade scale, Roadmap per milestone.
Grouping by directory makes that legible, and makes it obvious where a new document goes.

**Rejected: a shared package published from here.** The moment it is installable it is a
dependency, and the asymmetry above is gone. Templates are copied, never installed.

**Rejected: duplicating these standards into each repository.** Duplication diverges
silently; a copied standard is a fork nobody remembers forking.

## Forbids

- Product code, build files, CI that builds a product, or any installable artefact.
- Any repository taking a build, test or runtime dependency on this one.
- A standard here contradicting one in a product repository without this one being
  updated in the same change.
- Vendored copies of these documents.

**Revisit trigger:** a genuine need for a *shared executable* asset across repositories.
That is not this repository — it would be a package in the ecosystem repository, subject
to the extraction bar.
