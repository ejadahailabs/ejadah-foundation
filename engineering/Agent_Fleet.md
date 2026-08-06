# Agent Fleet — many executors, one discipline

Work Items ([Work_Tracking.md](Work_Tracking.md)) are the dispatch queue. Agents are
executors assigned to items — never assumed, never self-appointed. The fleet scales the
*doing*; it changes nothing about the rules, which is the point.

## The state machine (labels)

| Label | Meaning | Who sets it |
|---|---|---|
| `wi:ready` | acceptance criteria written; an agent may claim it | **a human, always** |
| `wi:claimed` | one executor owns it; others must not touch it | the claiming agent |
| `wi:blocked` | a `depends_on` is open | agent or human |
| `gate:review` | PR open — awaiting the human gate | the agent |
| `gate:owner` | an escalation condition was hit; work stopped | the agent |

An item nobody marked `wi:ready` is invisible to the fleet. That single rule keeps
humans in charge of *what* gets worked, while agents own *how*.

## Fleet law

1. **One item, one executor.** A claimed item is untouchable by other agents.
2. **Never main.** All work on `wi/<number>-<slug>` branches; delivery is a PR. The PR
   is the human gate, and CI green is its precondition — an agent may not weaken a
   check to get there (the ratchet rule applies to the fleet).
3. **Acceptance criteria are the contract.** No criteria → not `wi:ready` → no agent.
4. **Evidence at close, always**: gate output, commit SHA, measurements — commented on
   the item before it closes.
5. **Escalation stops work.** Business, legal, pricing, branding, credentials,
   security-sensitive beyond policy, or a conflict with an adopted ADR → label
   `gate:owner`, state the reason, stop. Silence is never consent for these.
6. **Releases and publishes are human acts.** No agent tags, publishes, or deploys.

## Roles (routed by the item's `type` label)

| Type | Executor behavior |
|---|---|
| `feature` | vertical slice; releasable after merge; ADR if architecture moved |
| `defect` | reproduce as a failing test first; fix to green; root cause in the commit |
| `verification` | produce evidence for an existing claim; touches tests/fixtures only |
| `doc` | docs and boards; byte-precision on frozen documents — amend, never edit |
| `debt` | measure → baseline → ratchet; pay down only what the item scopes |
| `decision` | draft the ADR with rejected alternatives; always ends at `gate:owner` |
| `ops` | CI, packaging, infrastructure; consumes artifacts in shipped form |

## Runtimes

**Primary — GitHub Actions**: labeling `wi:ready` triggers the fleet workflow; runs in
the cloud, works while every laptop is off. Requires the `ANTHROPIC_API_KEY` repository
secret (owner-installed; key custody is an owner escalation).

**Fallback — local dispatcher**: a Claude Code session on any machine may act as an
executor under exactly the same protocol — claim by label, branch, PR. The protocol,
not the runtime, is the contract.
