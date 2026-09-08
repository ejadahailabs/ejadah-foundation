# Branding

## The two lines every surface aligns to

> **Sanad is an Engineering Intelligence Platform that generates, validates and governs the
> digital thread of a product, keeping requirements, models, code, tests and certification
> evidence continuously aligned.**

> **Built for every engineer involved in developing a regulated product.**

Every page, deck, listing and README paraphrases the first and carries the second. None
contradicts either. Short form, for a hero, a footer or a meta description: **Sanad generates,
validates and governs the digital thread of a regulated product.**

Retired 2026-09-08: "requirements and engineering governance platform". It reads as a peer of
the requirements tools Sanad is not one of.

## Names, exactly

| Entity | Written as | Never |
|---|---|---|
| Company | **Ejadah AI Labs** | Ejadah Labs · EjadahAI · EJADAH |
| Product | **Sanad**, the Ejadah Engineering Intelligence Platform | E-REW for the product in prose · REW · e-rew · E_REW |
| Product, short | **Sanad** *(after first full use)* | EEIP · EIP · "the Ejadah platform" as the product name |
| Products | **Sanad (beta, build in progress)** — there is no second product | E-AEW, E-SWE, E-VEW, E-RVW, E-SEW, E-CEW on any public surface |

`E-REW` names the repository and the historical release line (0.1.0–0.3.0), not the product.
Full authority: [../product/Naming.md](../product/Naming.md). The one-product decision:
[../adr/ADR-0003-One-Product-One-Platform.md](../adr/ADR-0003-One-Product-One-Platform.md).

## Status words — only two

**build in progress** — it exists in the beta. **planned** — it does not.

Never "built", "complete", "shipping", "qualified" or "available" on any surface. **Nothing
is called complete until its signed verification record exists.** A reader who installs the
beta must find exactly what we said they would find.

## The one naming rule that is architectural

**"Engineering Intelligence" is the product's name, never a component's.**

Externally it describes what Sanad is. Internally, no module, directory, layer or class may
carry the word "intelligence" — a box with that name collects whatever nobody else wants to
own. This is not style; it is enforced by ADR-0024 in the product repository.

## Voice

Precise, plain, unhurried. We sell to engineers who are accountable for safety, and they
recognise overstatement instantly.

| Do | Do not |
|---|---|
| "Answers with evidence attached" | "AI-powered insights" |
| "Reproducible at a commit" | "Enterprise-grade" |
| "No hazard role declared — safety analysis stood down" | "100 % compliant" |
| Name the limitation | Imply completeness we cannot prove |
| Use the guidance's own words | Coin vocabulary of our own |

Never claim certification. We produce *evidence for* certification; the authority
certifies. Blurring that is a legal and professional error, not a marketing choice.

---

## History

Until 2026-09-08 the names table carried a **Platform** row ("Ejadah Engineering Intelligence
Platform", short form "the Platform") distinct from a **Products** row reading "**Sanad**
(shipping); **E-AEW**, … (planned)", and noted that "planned workbenches not yet built keep
the `E-` plus three letters convention until each is named". Superseded by
[ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md): Platform names the product, there
are no planned workbenches, and Sanad is a build in progress, not shipping.
