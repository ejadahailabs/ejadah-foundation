# 1 · Architecture and naming

## Two brands, one family

| Level | Name, exactly | Role | Mark |
|---|---|---|---|
| Company | **Ejadah AI Labs** | Who makes it. Trust, research, hiring, investors | E-mark |
| Product | **Sanad** | What people use. Leads on every product and marketing surface | Sanad link mark |

**Sanad leads, Ejadah endorses.** A product surface says *Sanad*, with *by Ejadah AI Labs*
as the endorsement. The company site leads with Ejadah and introduces Sanad as the proof.

## The words, exactly

| Use | Written as | Never |
|---|---|---|
| Company | Ejadah AI Labs (short: Ejadah) | Ejadah Labs · EjadahAI · EJADAH |
| Product | Sanad | SANAD · sanad (in prose) · Sanad AI |
| Product descriptor | **Sanad, the Ejadah Engineering Intelligence Platform** | "Workbench" for Sanad · a second product name |
| Lockup | Sanad · by Ejadah AI Labs | Ejadah Sanad · Sanad by Ejadah |
| Category | Engineering Intelligence | as the name of a module, layer or class (ADR-0024) |
| Philosophy | the Engineering AI Harness | as a headline or opening line: it's where the story lands, never where it starts |
| The sentence | "Sanad is an Engineering Intelligence Platform that generates, validates and governs the digital thread of a product, keeping requirements, models, code, tests and certification evidence continuously aligned." | cut short after "Platform" |
| Audience | built for every engineer involved in developing a regulated product | one discipline · "regulated systems" |

## Internal IDs stay internal

There is one product. Sanad is the Ejadah Engineering Intelligence Platform, and everything
else is a capability inside it ([ADR-0003](../adr/ADR-0003-One-Product-One-Platform.md)).
The canonical sentence, the audience line and the two status words are set in
[../company/Branding.md](../company/Branding.md); this chapter repeats them and never overrides them.

`E-REW` and any other `E-xxx` IDs are **engineering identifiers**.
They belong in repositories, ADRs, code, issues and package names. They never appear in
public copy, on the website, in the Marketplace listing or in marketing. Customers see
**Sanad**. Capabilities never carry a product identifier of their own.

See [../product/Naming.md](../product/Naming.md) for the full ID table and its history.

## The name's meaning (owner to confirm before public use)

*Sanad* (Arabic سند) means support, backing, a document you can rely on. It shares its root
with *isnad*, a chain of attribution that lets a statement be traced back to its source.
That is exactly what the product does for engineering claims. **Do not publish this story
until the owner approves the wording.**

## Naming rules that carry over

1. Status takes two words only: **build in progress** and **planned**. A name that promises completeness must be earned: nothing is "complete", "full",
   "total" or "100%" unless provable.
2. Repositories are lowercase (`ejadah-website`), products are capitalised (Sanad).
3. Third-party designations (DAL, ASIL, SIL) may appear on story and compliance surfaces
   of the website. Internal rule numbers, ADR numbers and source crosswalks never appear
   on a public page: write "a product principle enforced in code".
