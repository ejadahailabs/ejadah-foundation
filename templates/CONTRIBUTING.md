# Contributing

## Before you change anything

Read `CLAUDE.md` (or `CONTRIBUTING` equivalents) in this repository first. It records the
rules a newcomer would otherwise violate — each exists because breaking it cost real
damage, not because of taste.

## The gate

```bash
npm run check     # boundaries + typecheck + tests. All green, no exceptions.
```

> **Fix the code, not the assertion.**

Every test here was written because something specific went wrong. If one fails, the
first hypothesis is that your change is wrong. Weakening a check to get green — raising a
ratchet baseline, widening a budget, deleting an assertion — is a governance failure, not
a shortcut.

Fixtures may contain **deliberately seeded defects** that tests assert are found. Read the
fixture's own README before "fixing" anything in it.

## Before implementing a feature

Answer these. **A "no" means stop and redesign — not proceed and refactor later.**

- Is the capability plugin-grade — owns its contracts, tests, docs; removable with no
  changes elsewhere?
- Does dependency direction still point strictly downward?
- Does it introduce hidden state or a second source of truth?
- Is the decidable part testable without a UI?
- **Which new deterministic engineering questions does this make answerable?**

## Commits

- State **why**, not what — the diff already says what.
- A structural change ships with its diagram in the same commit.
- An architectural decision ships with an ADR recording its **rejected alternatives**.
- Never commit a rendered export of a text-source diagram.

## Review

Reviewed in this order: boundaries → second source of truth → honesty → determinism →
deletability → correctness → clarity. A problem at the first level makes the last two
irrelevant.

Blocking findings are architectural, honesty or determinism failures. Everything else is
advisory and marked as such.

## Reporting security issues

See `SECURITY.md`. Do not open a public issue.
