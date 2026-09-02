# The Platform

**Ejadah Engineering Intelligence Platform** — the shared substrate beneath every
workbench.

## What it is, precisely

Not a layer beneath the products, and not a service they call. It is the **contract set
plus the kernel implementing it**: the repository model, the engineering graph and its
ontology, the policy compiler, the analysis runtime, the evidence currency, the
question/answer contract and the AI gateway.

## Status — honest

> **The Platform is a name for a direction, not a shipped artefact.**

Today it is the discipline-invariant part of one product, Sanad. It becomes a platform
when a second workbench reuses it — not before, and calling it one earlier would be a
layer of indirection with a hopeful name.

The extraction is *known but not performed*: the seam is identified, measured and
enforced by CI, and deferred until a real second consumer exists.

## The pipeline

```
Git repository ── code index ── imported artefacts
        │            │              │
        └──── fact producers (N of them) ────┘
                       ▼
              Repository Model        FACTS — what the sources say
                       │
  rule packs ──► Policy Compiler      resolved once, at load
                       ▼
            Engineering Graph         MEANING — roles become typed edges
                       ▼
            Runner + Engines          ANALYSIS — the only place it happens
                       ▼
            Findings · Metrics        EVIDENCE — one currency, deterministic
                       ▼
            Questions → Answers       the product surface
                       │
     ┌────────┬────────┴────────┬──────────────┐
     ▼        ▼                 ▼              ▼
  editor   reports          AI skills     integrations
              — the rim: adapters only, all deletable —
```

## What the Platform owns, and what a workbench owns

| Platform | Workbench |
|---|---|
| Repository access, file identity, Git | Discipline templates *(data)* |
| Graph contract, ontology, query surface | Ontology extensions it contributes |
| Policy compilation | Rule packs *(data)* |
| Engine contract, runner | Engines *(code)* |
| Findings, metrics, report projection | Authoring actions, commands |
| Question → Answer contract | Prompts, skills, vocabulary |
| AI gateway, context builder | — |

**The rule that keeps it honest:** the Platform never contains a discipline noun in its
logic. A discipline word appearing as an ontology *value* is correct; appearing as an
*identifier* is a breach.

## Hosts

VS Code today. The architecture admits JetBrains, Visual Studio, web, cloud, CLI, REST
and remote agents because every host is a rim adapter — nothing in the core knows any of
them exist. Each is built when it has a user.
