# 5 · Voice

## The voice

**Precise, plain, unhurried.** We sell to engineers who are accountable for safety, and they
recognise overstatement instantly. The feeling is confidence; the conclusion — that this
matters — is one the reader reaches on their own.

| Do | Do not |
|---|---|
| "Answers with evidence attached" | "AI-powered insights" |
| "Reproducible at a commit" | "Enterprise-grade" |
| "No hazard role declared — safety analysis stood down" | "100% compliant" |
| Name the limitation | Imply completeness we cannot prove |

**Never claim certification.** We produce *evidence for* certification; the authority
certifies. Blurring that is a legal and professional error, not a marketing choice.

## Two registers, one voice

The same company speaks to two audiences. The voice stays the same; the register changes.

| | **Assurance** register | **Builder** register |
|---|---|---|
| For | Regulated buyers: chief engineers, safety leads, auditors, DERs | Developers, SMB teams (3–50), consultancies |
| Where | Website, one-pagers, sales decks, compliance pages, articles | LinkedIn dev posts, Reddit, Discord, Show HN, Marketplace, README |
| Sentences | Full, complete, measured | Shorter, second person ("you") |
| Leads with | The problem and its cost, then evidence | A concrete before/after |
| Standards names | Yes: DO-178C, ISO 26262, ARP4754A | Only when the reader brought them up |
| Visual weight | Dark, spacious, one gold accent | Same palette; more light surfaces, more real screenshots and code |

**Assurance example:**
> Every requirement in Sanad carries its trace to design, code and test, rebuilt at any
> commit. When a link is missing, Sanad says so and names it.

**Builder example:**
> You changed `parseConfig()`. Sanad shows the three requirements it implements and the one
> test that no longer covers it. Before you push.

Both are true, both are calm, neither hypes.

## Honesty rules (from the website positioning, binding everywhere)

1. **Problem first, philosophy last.** Search topic → known problem → Sanad's mechanism →
   the Engineering AI Harness. Never open with the harness.
2. **Status is always stated.** Use the two words: *build in progress* and *planned*. Never "built", "complete", "shipping", "qualified" or "available". Nothing
   is called complete until its signed verification record exists.
3. **Planned work, exact wording:** "AI participation capabilities under development within
   the Engineering AI Harness architecture."
4. **The differentiating line:** "We built the governance foundation first."
5. **No internal numbers in public:** no rule IDs, ADR numbers or source crosswalks. Write
   "a product principle enforced in code".
6. **Every claim has a source.** Before publishing, each factual claim points at a shipped
   capability, a test result or a real run (e.g. the cold-chain showcase). No source, no claim.

## Banned words

AI-powered · enterprise-grade · seamless · revolutionary · game-changing · cutting-edge ·
best-in-class · certified (about us or Sanad) · compliant (as a guarantee) · 100% ·
complete / full / total (unless provable) · magic · effortless · unlock · supercharge

## Style mechanics

- British spelling (organisation, colour, programme, licence as noun), matching the product
  and foundation docs. *Owner to confirm:* the website copy is currently mixed (10 ×
  "organization", 2 × "organisation", 2 × "programme" in `lib/content.ts` and `lib/articles.ts`).
  Whichever is chosen, one site uses one spelling.
- Em dashes sparingly; one per paragraph at most.
- Numbers: numerals for 10 and over, and always for measurements and percentages.
- Calls to action are verbs plus object: "Explore Sanad", "Read the research". Not "Learn more".
- No exclamation marks.
- Emoji: none in Assurance; at most one functional emoji (✓, →) per Builder post.
