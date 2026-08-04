# Review Standards

## What review is for

Not defect-catching alone — tests do that better. Review exists to check the things a
test cannot: **is this the right shape, does it hold the boundaries, and will the next
person understand why.**

## The order to review in

Reviewing in this order catches expensive problems while they are still cheap:

1. **Boundaries** — does dependency direction still point downward? Any new coupling a
   contract could have avoided?
2. **Second source of truth** — does this introduce state duplicating something else?
3. **Honesty** — can any output now claim more than the data supports?
4. **Determinism** — can this change make evidence non-reproducible?
5. **Deletability** — could this capability still be removed cleanly?
6. **Correctness** — logic, edge cases, error paths.
7. **Clarity** — will this read correctly in two years?

A problem at level 1 makes levels 6 and 7 irrelevant. Do not start at the bottom.

## Blocking versus advisory

| Blocking | Advisory |
|---|---|
| Boundary violation | Naming preference |
| A check weakened to pass | Structure that could be tidier |
| Output claiming more than it can prove | Test that could be clearer |
| Non-determinism on an evidence path | Comment that could be fuller |
| Missing decision record for an architectural change | — |

Advisory comments are marked as such. A review that blocks on preferences trains people
to ignore reviews.

## Reviewing AI-generated changes

Same standard, plus three checks that matter more because the failure modes differ:

- **Did it weaken a check to pass?** Ratchet baselines raised, budgets widened,
  assertions deleted, exceptions added. Always look.
- **Did it re-implement something already present?** Agents write plausible new code more
  readily than they find existing code.
- **Does the explanation match the diff?** A confident summary of a change that does
  something slightly different is the characteristic failure.

## Records

An architectural decision is recorded with its **rejected alternatives** and the trigger
that would justify revisiting it. A decision without its alternatives is unreviewable —
nobody can tell whether the choice was reasoned or accidental.
