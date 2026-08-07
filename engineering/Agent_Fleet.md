# Agent Fleet — many executors, one discipline

Work Items ([Work_Tracking.md](Work_Tracking.md)) are the dispatch queue. Agents are
executors assigned to items — never assumed, never self-appointed. The fleet scales the
*doing*; it changes nothing about the rules, which is the point.

## Claiming and state — assignment, not status labels

The board is a **derived projection**, never a place state is authored. There are no
`status/*` labels — an early version had them and they were removed, because two sources
of truth for one fact is one too many.

**Claiming is self-assignment.** An executor claims an item by assigning itself. GitHub
has no atomic claim, so contention resolves deterministically: the **earliest `assigned`
event wins; ties go to the lexicographically smallest login.** An executor re-reads the
item after assigning; if it is not the sole assignee it lost the race — back off and claim
another. The timeline is immutable, so every evaluation yields the same winner.

**Status is derived every sweep** from GitHub state — open and unclaimed → *Backlog*;
claimed or a PR up → *In Progress*; owner action needed → *Waiting on You*; closed →
*Done*. Hand-setting a status proves nothing; the sweep overwrites it.

The labels that *do* carry meaning are few:

| Label | Meaning | Who sets it |
|---|---|---|
| `blocked` | a dependency is still open | the daemon, from dependency state |
| `owner-gate` | needs the architecture/safety gate — work stops here | the executor |
| `wave-gate` | holds a whole wave back regardless of dependencies | a human |
| `cap/*` | routes the item to an executor capability (`cap/engineering` default) | whoever files it |

An item with no unmet dependency, no gate label, and acceptance criteria written is
eligible — no human has to hand it out. Humans stay in charge of *what* gets worked
through the four gates (direction, architecture/safety, feature acceptance, issue
filing), not by labelling each task ready.

## Fleet law

1. **One item, one executor.** A claimed item is untouchable by other agents.
2. **Never main.** All work on a task branch; delivery is a PR. CI green is a precondition
   and no agent may weaken a check to reach it (the ratchet rule applies to the fleet).
3. **Independent review, automated merge.** Every PR is reviewed by a *different* executor
   than its author — one review per head commit — and merged by the merge daemon once that
   exact commit is approved, conflict-free and green. **No agent reviews or merges its own
   work, and no human merges at all.** The human gate is not the PR; it is acceptance of
   the finished feature.
4. **The executor closes its own task** once its lifecycle is complete — merged, evidence
   recorded. Features are closed by the owner (that close *is* acceptance testing); epics
   close by automation when their features are done.
5. **Acceptance criteria are the contract.** No criteria → not eligible → no agent.
6. **Evidence at close, always**: gate output, commit SHA, measurements — recorded on the
   item before it closes.
7. **Escalation stops work.** Business, legal, pricing, branding, credentials,
   security-sensitive beyond policy, or a conflict with an adopted ADR → label
   `owner-gate`, state the reason, stop. Silence is never consent for these.
8. **Releases, publishes and deploys are human acts.** Automation merges to the trunk; it
   never tags, publishes, or deploys.

## Roles (routed by the item's `type` label)

| Type | Executor behavior |
|---|---|
| `feature` | vertical slice; releasable after merge; ADR if architecture moved |
| `defect` | reproduce as a failing test first; fix to green; root cause in the commit |
| `verification` | produce evidence for an existing claim; touches tests/fixtures only |
| `doc` | docs and boards; byte-precision on frozen documents — amend, never edit |
| `debt` | measure → baseline → ratchet; pay down only what the item scopes |
| `decision` | draft the ADR with rejected alternatives; always ends at `owner-gate` |
| `ops` | CI, packaging, infrastructure; consumes artifacts in shipped form |

## Runtimes

The protocol, not the runtime, is the contract — anything below acts as an executor under
exactly the rules above.

- **The runner** reads the eligible queue and spawns a build session per task (or a
  human-run session fans out sub-agents to the same effect).
- **Two zero-model daemons** keep GitHub and the board in sync. One derives board status,
  ticks the observable lifecycle boxes, and manages the `blocked` label every sweep; the
  other is the **merge train**, which lands a PR only when an independent review has
  approved the current head, the PR is conflict-free, and CI on that head is green. No
  model runs inside either — they are plain API pollers, safe to leave running.
- **Cloud execution** (GitHub Actions) runs the same protocol while every laptop is off;
  it needs the `ANTHROPIC_API_KEY` repository secret, whose custody is an owner escalation.

## The mechanism is replaceable; this discipline is not

The concrete expression of this protocol — the exact label strings, the branch-name
convention, the runner and daemon scripts, the queue file, the liveness heartbeat — lives
in the organisation's **Control Center operating model**, a mechanism document that may be
rewritten as the fleet evolves. This document governs the discipline that mechanism must
honour; where the two differ, the mechanism is what changes. As with everything in this
foundation, other repositories *reference* it and none *depend* on it.
