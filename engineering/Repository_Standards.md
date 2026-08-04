# Repository Standards

## Repository separation is a deployment concern, not an architectural one

A repository is a packaging and distribution unit. Architecture is expressed by
dependency direction, contracts and ownership — none of which a repository boundary can
create, and all of which it can hide.

**Consequence:** an argument about repository layout is an argument about deployment, and
must never be answered with an architectural change.

## Modularity comes from enforced checks, not boundaries

Ten repositories with no enforced dependency rule are ten things that drift
independently, invisibly, until integration fails. One repository with a CI-enforced
boundary is more modular in practice.

**Therefore:** every architectural boundary a repository claims must have a script that
fails the build when it is crossed. A boundary asserted only in documentation does not
exist.

## When a new repository is justified

| Justified | Not justified |
|---|---|
| It ships to a different audience | "It feels like a separate concern" |
| It has a genuinely independent lifecycle | It might have consumers one day |
| It is code-free and depended on by nothing | Tidiness |

**Never create a repository for a product with no user waiting for it.** An empty
repository signals progress that does not exist, and will be created wrong — the lessons
that shape it are learned by shipping the previous one.

## Required in every repository

| File | Purpose |
|---|---|
| `README.md` | What it is, how to build, how to test |
| `LICENSE` | Explicit, never assumed |
| `CONTRIBUTING.md` | How to propose a change |
| `SECURITY.md` | How to report a vulnerability |
| `CHANGELOG.md` | What changed, per release |
| `CODEOWNERS` | Who reviews what |
| `ROADMAP.md` | Where it is going |
| `adr/` | Decisions, with rejected alternatives |
| `docs/` | Reasoning that outlives the code |
| `.github/` | CI that runs the full gate |

Templates: [`../templates/`](../templates/).

## Branching and history

- Default branch `main`.
- Commit messages state **why**, not what — the diff already says what.
- A structural change ships with its diagram in the same commit.
- Never commit a rendered export of a text-source diagram. The text is canonical; a
  committed render is a second source of truth that drifts.

## Release verification

> **A test suite verifies correctness. A release pipeline verifies shippability.**

These are different problems, and conflating them has cost us activation-killing defects
that survived hundreds of green test runs — because the tests ran the sources directly
and never loaded the built artefact the way a real host does.

**Rule:** any change to what ships — build config, manifest, packaging ignore lists,
dependencies — is verified by consuming the artefact **in its shipped form**, not by the
test suite alone.

## Inheriting from this repository

Reference these standards by link. Never vendor a copy — a copy is a fork that drifts
silently. And never make a build depend on this repository being present.
