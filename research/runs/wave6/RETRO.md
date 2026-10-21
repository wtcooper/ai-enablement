# Wave 6 retro: mid-market modules for assurance and tax

Date: 2026-10-21 · Feeds: the plan's waves and costs, the brief templates

## Result

**Four new modules and five widened ones**, covering work for private, middle-market companies, owners and families. The
landscape scan (93 source rows, 70 opened and read) proposed the set, and the owner chose "4 new + widen". The scan
merged private-company audits with reviews and compilations into one module, because public AI material on SSARS work is
too thin to stand alone. It also showed that peer-review reports give the clearest split of mid-market assurance work:
single audits, ERISA, other audits, reviews and compilations.

| Archetype | Module | Use cases | A/B | Evidence | Entries fixed by verifier |
|---|---|---|---|---|---|
| assurance | private-company (new) | 20 | 45% | moderate | 15 / 20 |
| assurance | benefit-plans (new) | 15 | 47% | moderate | 15 / 15 |
| assurance | nonprofit-government (new) | 16 | 62% | strong | 13 / 16 |
| tax | multistate-private (new) | 14 | 7% | thin | 12 / 14 |
| assurance | quality-management (widened) | 28 | 36% | moderate | 7 / 13 checked across the three |
| assurance | soc-attestation (widened) | 18 | 61% | strong | (with quality-management) |
| assurance | assurance-over-ai (widened) | 27 | 26% | thin | (with quality-management) |
| tax | compliance-individual-business (widened: entries 26-31) | 31 | 32% | moderate | 8 / 13 checked |
| tax | research-advisory (widened: entries 26-28) | 28 | 39% | moderate | 4 / 6 checked |

**No entry was rejected.** In the new modules verification corrected 55 of 65 entries (85%). In the widened modules
only the new or changed entries were checked; 19 of 32 were corrected. No grade changed in the widened tax modules.
Assurance now has 13 modules and 265 entries; tax has 9 modules and 206.

**Integration.** One agent added the new modules to both `ARCHETYPE.md` files (each kept at 100 lines), the value
chains and the interview guides, with mid-market cues (for example "Form 5500", "Uniform Guidance", "Form 7203"). It also unified the source
keys:
- 36 old assurance keys were folded into existing ones, mostly into the keys `sources.md` already used;
- four keys that each named two different documents were split;
- the Vals tax-agent benchmark was dated 2026-10-20 everywhere, with earlier figures marked in their locators.

A follow-up pass made 77 `sources.md` entries match the YAML, folded 8 older duplicate pairs, and gave the
Journal of Accountancy small-firms article one key across tax and assurance. A few keys whose YAML records disagree
with each other were left open for review (report: `sources-cleanup-report.md`). Part B of each `sources.md` lists only
keys that archetype-level files cite, so the new module keys stay in the YAML and module source lists.

## What the evidence says

The landscape found mid-market AI material in four places:
- audit-platform launches by mid-tier firms and vendors;
- agentic tax-preparation start-ups aimed at CPA firms;
- AICPA guidance, led by the October 2026 practice aid for financial statement auditors;
- state tax agencies adopting AI for audit selection.

It found almost no AI-specific material for SSARS engagements, benefit plan audits, single audits, fiduciary and estate
returns or Form 990 work, and no AI finding from peer review or the oversight bodies for plan and government audits.
The benefit-plans and nonprofit-government modules still reach 47% and 62% A/B, but every one of those entries is
B: no entry in either reaches A. Multistate tax for private companies is the
thinnest module: one entry reaches A or B. In the Thomson Reuters survey the landscape cites, larger and mid-sized tax
firms report being further along with technology than small firms.

## Cost and time

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Landscape scan, 6 new-module dives, 2 widening dives | 9 | Sonnet | 3.1M |
| Synthesis and verification (4 new, 2 widening) | 12 | Opus | 3.2M |
| Integration and sources cleanup | 2 | Opus | about 0.9M |
| **Total** | **23** | | **about 7.2M** |

Token figures are each agent's final context size, the same measure as earlier retros.

## What went wrong, and what changed

| # | Problem | Change |
|---|---|---|
| 1 | One research agent's Write was refused by a guard, and its output sat in a temp file | The orchestrator read it and copied it into the run folder. Check each agent's output path before synthesis starts |
| 2 | New and widened modules reused documents already keyed differently in older assurance files | A dedicated integration step unified keys before the archetype files were updated; a cleanup pass covered `sources.md` and older files. For future waves, give the synthesis brief the archetype's key list up front |
| 3 | The same Journal of Accountancy article had different keys in tax and assurance | The cleanup pass checked it. Future consistency passes should check keys across archetypes, not only within one |
| 4 | Several modules miss the 50% A/B target, and multistate-private is at 7% | No grade was raised. The modules are rated in `ARCHETYPE.md`, and the advisor says so |
| 5 | Widened modules were verified only on what changed | This is deliberate: earlier waves verified the existing entries. The verifier checks every entry that the widening changed, not just the new ones |
