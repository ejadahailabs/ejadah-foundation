# The Platform

**Sanad is the Ejadah Engineering Intelligence Platform — it generates, validates and governs
the digital thread of a product.** This document describes its architecture. The name is the
product's; there is no separate substrate to name. See
[../adr/ADR-0003-One-Product-One-Platform.md](../adr/ADR-0003-One-Product-One-Platform.md).

## What it is, precisely

Not a layer beneath the capabilities, and not a service they call. It is the **contract set
plus the kernel implementing it**: the repository model, the engineering graph and its
ontology, the policy compiler, the analysis runtime, the evidence currency, the
question/answer contract and the AI gateway.

Every capability in [Capabilities.md](Capabilities.md) is built on that contract set and
composes with the others through the repository and the ontology, never through a call.

## Status — honest

Sanad is a **build in progress**, released as a free beta. The architecture below is adopted
and in use; the capabilities standing on it are at different depths, and none is complete.
**Nothing is called complete until its signed verification record exists.**

The kernel seam — the line between the discipline-invariant core and everything discipline-
specific — is identified, measured and enforced by CI. It is maintained because it keeps the
core honest, not because a second product is planned. There is none.

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

## What the kernel owns, and what a capability owns

| Kernel | Capability |
|---|---|
| Repository access, file identity, Git | Discipline templates *(data)* |
| Graph contract, ontology, query surface | Ontology extensions it contributes |
| Policy compilation | Rule packs *(data)* |
| Engine contract, runner | Engines *(code)* |
| Findings, metrics, report projection | Authoring actions, commands |
| Question → Answer contract | Prompts, skills, vocabulary |
| AI gateway, context builder | — |

**The rule that keeps it honest:** the kernel never contains a discipline noun in its logic.
A discipline word appearing as an ontology *value* is correct; appearing as an *identifier*
is a breach.

## Hosts

VS Code and a command-line interface today. The architecture admits JetBrains, Visual Studio,
web, cloud, REST and remote agents because every host is a rim adapter — nothing in the core
knows any of them exist. Each is built when it has a user.

---

## History

Until 2026-09-08 this document opened "**Ejadah Engineering Intelligence Platform** — the
shared substrate beneath every workbench", and its Status section read "the Platform is a
name for a direction, not a shipped artefact… it becomes a platform when a second workbench
reuses it". The ownership table above was headed *Platform · Workbench*.

Superseded by [ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md): Platform names the
product, the substrate is an internal architecture fact, and the second workbench is not
coming. The pipeline, the ownership split and the discipline-noun rule are unchanged.
