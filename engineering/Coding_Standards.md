# Coding Standards

Language-agnostic rules first; per-language specifics live in the product repository.

## Comments

> Comment **why**, not what.

A comment explaining a non-obvious constraint is worth ten explaining syntax.

**Where a bug was subtle, say so in the comment** — including what breaks if the fix is
"tidied" away. Code that looks redundant and is not will be simplified by someone
eventually unless the comment stops them. This has cost us real defects and is the single
highest-value comment we write.

## Types

Strictest available settings, on. A type system relaxed for convenience stops catching
the class of error it was adopted for.

Prefer omitting an optional property to assigning it an empty value — "absent" and
"present but empty" are different facts, and collapsing them loses information the
analysis depends on.

## Errors

Never swallow. Never fall back to a plausible default on a path that produces a user-
facing claim — a wrong number that looks right is worse than a failure. If a component
cannot do its job, it says so and stands down with a stated reason.

## Dependencies

Each one is a permanent liability: supply chain, licence, maintenance, packaging.

Order of preference: **already in the codebase → standard library → platform feature →
existing dependency → a few lines of our own → a new dependency.** Reach the last rung
only with a reason worth writing down.

## Tests

Every test exists because something specific went wrong. When one fails, the first
hypothesis is that the change is wrong.

- Test names state the behaviour and, where useful, the rule they defend.
- Fixtures may contain deliberately seeded defects; read the fixture's own README before
  "fixing" anything in it.
- Non-trivial logic — a branch, a parser, a money or safety path — leaves one runnable
  check behind.

## Determinism

Any code producing evidence must be deterministic: no wall-clock, no randomness, no
locale-dependent ordering, no iteration-order dependence. Same inputs, same bytes.

## Size and clarity

Boring over clever. Clever is what someone decodes at 3 a.m. during an incident.

Deletion is a legitimate and preferred form of progress.
