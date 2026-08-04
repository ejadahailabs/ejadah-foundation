# Values

Five, in priority order. When they conflict, the earlier wins.

## 1. Honesty over completeness

Silence with a stated reason beats a plausible number. A tool that cries wolf gets
switched off — and takes every other finding with it.

*In practice:* an undeclared role disables the analysis that needs it. No defaults, no
estimates, no "100 % coverage" computed over data we never had.

## 2. Evidence over assertion

Anything we claim, we can show. Anything we cannot show, we do not claim.

*In practice:* findings carry provenance. Inferred results are marked as candidates for
human judgement, never as established fact.

## 3. Proof over speculation

Build what a real consumer needs now; design so the next one is cheap. Generality is
earned by a second real consumer, never granted in advance.

*In practice:* a shared component moves only when it passes all three extraction tests.

## 4. Durability over speed

Architectural integrity outranks implementation speed. A "no" to a design question means
stop and redesign — not proceed and refactor later.

*In practice:* decisions are recorded with their rejected alternatives, so the reasoning
survives the people.

## 5. Deletability over dependency

Every capability should be removable without changes elsewhere. What cannot be deleted
cannot be reasoned about.

*In practice:* AI is deletable today and permanently. The architecture is graph-centred
with AI as a consumer — not AI-centred with a graph attached.
