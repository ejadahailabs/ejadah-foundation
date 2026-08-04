# AI Governance

Applies to AI **inside our products** and AI **used to build them**. Both are governed;
the rules differ.

---

## Part 1 — AI inside the products

### The two doors

| Door | What it is | Output |
|---|---|---|
| **1. Skills at the rim** | Context built from answers and the graph; result lands as ordinary Git edits | A human accepts or rejects |
| **2. Optional engine inference** | An engine may consult a model | Marked **inferred**, rendered as a candidate |

**There is no third door.** AI never sits on a mandatory path. Every product must
function completely with AI disabled — not degraded into uselessness, but genuinely
working, minus the assistive parts.

### The attestation rule

> **AI may propose. Only deterministic analysis attests.**

Inferred output never participates in byte-identical evidence. A certification artefact
containing a model's opinion is not evidence, however good the opinion.

### Presentation

An inferred finding renders as *a candidate for human judgement*, never as established
fact — and the distinction survives every render site, including exports and dashboards.
Clamping it at one site and not another is the defect this rule exists to prevent.

### Provider neutrality

Models reach the product through one gateway. No provider's API shape leaks into a
product. Multi-model routing waits for demonstrated demand.

### What AI may never do

- Attest to a compliance or safety claim.
- Modify a file the user did not open.
- Determine policy, criticality or rigour.
- Be required for the product to start, analyse or report.

---

## Part 2 — AI used to build Ejadah products

We build with AI agents at scale. That is a capability, and it is governed.

### Non-negotiable

| Rule | Reason |
|---|---|
| Every change passes the same gate as a human's | An agent's confidence is not evidence |
| Architectural decisions are recorded with rejected alternatives | Otherwise the reasoning is lost the moment the session ends |
| An agent may not weaken a check to make a build pass | The single most damaging failure mode available to it |
| Fixtures with deliberately seeded defects stay seeded | Tests assert those defects are found |
| Findings reported honestly, including "I could not finish" | A silent partial is worse than a stated gap |

### The rule that matters most

> **Fix the code, not the assertion.**

When a check fails, the first hypothesis is that the change is wrong — not that the check
is. Raising a ratchet baseline, widening a budget, or deleting an assertion to get green
is a governance failure, not a shortcut. It is also the easiest thing in the world for an
agent to do, which is exactly why it is written down.

### Autonomy boundaries

An agent may research, design, implement, test, document and report. It may **not** make
decisions that are legally, ethically or financially the owner's; send anything to a
third party; close a safety gate; spend money; or claim a real-world fact it cannot
verify. Those stop and escalate.
