# Branding

## Names, exactly

| Entity | Written as | Never |
|---|---|---|
| Company | **Ejadah AI Labs** | Ejadah Labs · EjadahAI · EJADAH |
| Platform | **Ejadah Engineering Intelligence Platform** | EEIP in prose · "the Ejadah platform" |
| Platform, short | **the Platform** *(after first full use)* | EIP as a customer-facing term |
| Products | **Sanad** (shipping); **E-AEW**, … (planned) | E-REW for the shipping product in prose · REW · e-rew · E_REW |

Sanad is the shipping product's brand (ADR-0054, E-REW repository); its repository name
and historical release line (0.1.0–0.3.0) still read `E-REW`. Planned workbenches not yet
built keep the `E-` plus three letters convention until each is named.

Full authority, including the Sanad rename and the reverse-engineering naming conflict:
[../product/Naming.md](../product/Naming.md).

## The one naming rule that is architectural

**"Engineering Intelligence" is the product's name, never a component's.**

Externally it describes what the Platform is. Internally, no module, directory, layer or
class may carry the word "intelligence" — a box with that name collects whatever nobody
else wants to own. This is not style; it is enforced by ADR-0024 in the product
repository.

## Voice

Precise, plain, unhurried. We sell to engineers who are accountable for safety, and they
recognise overstatement instantly.

| Do | Do not |
|---|---|
| "Answers with evidence attached" | "AI-powered insights" |
| "Reproducible at a commit" | "Enterprise-grade" |
| "No hazard role declared — safety analysis stood down" | "100 % compliant" |
| Name the limitation | Imply completeness we cannot prove |

Never claim certification. We produce *evidence for* certification; the authority
certifies. Blurring that is a legal and professional error, not a marketing choice.
