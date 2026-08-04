# Branding

## Names, exactly

| Entity | Written as | Never |
|---|---|---|
| Company | **Ejadah AI Labs** | Ejadah Labs · EjadahAI · EJADAH |
| Platform | **Ejadah Engineering Intelligence Platform** | EEIP in prose · "the Ejadah platform" |
| Platform, short | **the Platform** *(after first full use)* | EIP as a customer-facing term |
| Products | **E-REW**, **E-AEW**, … | REW · e-rew · E_REW in prose |

Product identifiers are uppercase with a hyphen. Repository and package names are
lowercase (`e-rew`) — a filesystem convention, not a brand.

Full authority, including the reverse-engineering naming conflict:
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
