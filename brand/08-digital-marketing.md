# 8 · Digital marketing

## Channels and register

| Channel | Register | Ground | Notes |
|---|---|---|---|
| Website, articles | Assurance | ink | The 11-question narrative (`ejadah-website/NARRATIVE.md`) |
| LinkedIn company page | Assurance, some Builder | ink | Category, research, milestones |
| LinkedIn personal posts (founder) | Builder | ink or paper | Build-in-public, before/after |
| Reddit, Discord, dev communities | Builder | — (text first) | Answer the question asked; link only when it helps |
| Show HN | Builder | — | Plain title: "Show HN: Sanad – traceability from requirements to tests in VS Code" |
| VS Code Marketplace | Builder | ink banner | Lead with what changes for the developer |
| GitHub (`E-REW-support`) | Builder | — | README with lockup, real screenshots |
| Email | Assurance | paper | Plain text or very light HTML, signature template |

## Sizes

| Asset | Size (px) | Template |
|---|---|---|
| LinkedIn / X link post image | 1200 × 627 | `templates/social-post-1200x627.svg` |
| LinkedIn carousel slide (PDF) | 1080 × 1350 | `templates/carousel-slide-1080x1350.svg` |
| LinkedIn company banner | 1584 × 396 | `templates/linkedin-banner-1584x396.svg` |
| Open Graph image | 1200 × 630 | `templates/og-image-1200x630.svg` |
| GitHub social preview | 1280 × 640 | `templates/github-social-1280x640.svg` |
| Article header | 1600 × 840 | `templates/article-header-1600x840.svg` |
| Marketplace icon | 256 × 256 PNG | `logos/sanad-app-icon.svg` |

Keep text inside the **safe area**: 64px from every edge (LinkedIn crops on mobile).

## Layout rules for every graphic

- Ink ground. One headline (Inter 600, max 8 words). One supporting line at most.
- One gold element. Usually the key node or a single highlighted word, never both.
- Sanad lockup or mark bottom-left, at the safe-area edge. Ejadah only in the endorsement.
- If it shows a capability, it shows its status word (*build in progress* or *planned*).
- No screenshots in Assurance graphics; real screenshots welcome in Builder graphics.

## Recurring post formats

| Format | Register | Shape |
|---|---|---|
| **Question made answerable** | Assurance | "Which requirements does this commit affect?" → how Sanad answers → evidence image |
| **Before / after** | Builder | Two panels: the manual way vs the Sanad view. Real screenshots |
| **This week's build** | Builder | 3 bullets, each with a status word. Honest, including what slipped |
| **Standards explainer** | Assurance | One DO-178C / ISO 26262 objective in plain words, and what evidence answers it |
| **Research note** | Assurance | Links to an `/insights` article; diagram as the image |

## UTM naming (for the beta funnel analytics)

```
utm_source   = linkedin | reddit | hn | discord | x | email | marketplace | github
utm_medium   = social | community | email | listing | referral
utm_campaign = beta-<stage>   (e.g. beta-s2-invite, beta-s3-recruit, beta-s4-launch)
utm_content  = <post-format>-<yyyymmdd>   (e.g. before-after-20261201)
```

All lowercase, hyphens not underscores. One campaign name per beta stage, so the funnel
dashboard groups cleanly.

## Before anything goes out

- [ ] Every claim has a source (capability, test result, real run).
- [ ] Status words present for each capability mentioned.
- [ ] No banned words ([chapter 5](05-voice.md)).
- [ ] No internal IDs (E-REW, ADR or rule numbers).
- [ ] Text contrast checked (the template colours already pass).
- [ ] Alt text written.
- [ ] Owner approval for anything new about the product (POSITIONING rule).
