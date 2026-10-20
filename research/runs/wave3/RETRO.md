# Wave 3 retro: professional services archetype

Date: 2026-10-20 · Feeds: the plan's waves and costs, the brief templates, stream B (backbone library)

## Result

**Professional services archetype (pillar 2).** Twelve verified modules and 11 archetype-level files.
Professional services is now listed as available in `archetypes/index.md`. It is the base that assurance and tax
extend and that security service providers use; those three `ARCHETYPE.md` files now link to it.

The landscape scan proposed 12 modules (the original 8 plus talent-learning, firm-finance, client-development and a
thin shared work-production module). With the owner's sign-off: in-house legal and shared-service teams were tagged
inside the modules rather than given their own; acceptance-risk had one combined dive because public detail is thin;
two cross-cutting topics were researched (guardrails and professional conduct; state of AI and disruption). Economics
and workforce were drawn from the firm-finance, scoping-pricing, talent-learning and staffing modules.

| Module | Use cases | A/B | Evidence | Entries fixed by verifier |
|---|---|---|---|---|
| work-production | 25 | 72% | strong | 22 / 25 |
| scoping-pricing | 23 | 61% | strong | 15 / 23 |
| quality-review | 18 | 61% | strong | 17 / 18 |
| talent-learning | 25 | 60% | strong | 17 / 25 |
| firm-finance | 17 | 53% | strong | 16 / 17 |
| knowledge-management | 23 | 52% | strong | 22 / 23 |
| client-development | 22 | 50% | strong | 16 / 22 |
| delivery-management | 15 | 47% | moderate | 13 / 16 |
| pursuit-proposals | 20 | 45% | moderate | 19 / 20 |
| acceptance-risk | 14 | 43% | moderate | 14 / 14 |
| billing-collections | 17 | 29% | thin | 13 / 17 |
| staffing-resourcing | 21 | 24% | thin | 14 / 21 |

**No entry was rejected.** 198 of 241 entries (82%) were corrected, the highest share of any wave. The consistency
pass later merged one delivery-management entry into knowledge-management (240 entries now).

**Consistency pass:** 14 source-key aliases merged and 5 overloaded keys split (29 conflicting source records to 0);
two keys renamed because tax uses them for different documents (`VALS-VLAIRFEB-2025`, `TR-FOP-REPORT-2026`); dates
settled for ILTA's 2026 survey (2026-08-14), California's guidance (2026-05-14) and Thomson Reuters' Future of
Professionals report (2026-06-22); about 45 overlapping pairs cross-referenced both ways. No grade changed.

**Archetype-level verification:** about 570 claims checked across the 11 files: 58 fixed, 3 removed. Main fixes:
survey figures applied to the wrong population (senior legal leaders called "legal professionals"; respondents
counted as organisations; firm-size bands mixed); attribution drift (Clio data credited to CMS; a company forecast that
was its CEO's view; paraphrases shown as quotes); overstated wording ("the only", "no organisation"). Reports:
`professional-services-archetype-verification-A-report.md` and `-B-report.md`.

## What the evidence says

Professional services has plenty of vendor case studies, surveys and conduct guidance, and almost no measured
results from firms. In 10 of 12 modules no entry reaches A: no named firm publishes an error rate, override rate,
win rate or margin effect for its own AI use. The measured evidence is about tools (Stanford and Vals benchmarks), one
field experiment, and the NBER patent-lawyer trial, which Google ran and funded (six of seven authors). Conduct rules
agree everywhere: the professional stays responsible, verification is enforced by courts, and hourly billing must
reflect time actually spent. The open questions are pricing (who keeps the saving), junior development, and variable
AI cost.

## Cost and time

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Landscape scan | 1 | Sonnet | 0.3M |
| 33 module dives, 1 combined dive and 2 cross-cutting topics | 36 | Sonnet | 12.2M |
| Module synthesis | 12 | Opus | 4.8M |
| Module verification | 12 | Opus | 4.4M |
| Consistency pass and archetype-level synthesis | 2 | Opus | about 1.1M |
| Archetype-level verification | 2 | Opus | about 0.6M |
| **Total** | **65** | | **about 23.5M** |

Close to the plan's estimate of about 64 agents; the twelve modules cost about as much as security's eleven.

## What went wrong, and what changed

| # | Problem | Change |
|---|---|---|
| 1 | Overlapping modules synthesized in parallel (the wave 4 lesson) | Each synthesis brief named the finished modules to read first. To avoid idle waits, the order was flipped as research finished (talent-learning before staffing, firm-finance before billing, client-development before pursuit, acceptance-risk before quality-review). Later syntheses cross-referenced about 40 entries instead of copying them |
| 2 | Parallel agents gave the same document different keys, and one key different documents | The consistency pass unified them. For future waves, give the synthesis brief a shared key list from finished modules, and check keys against other archetypes |
| 3 | Five modules miss the 50% A/B target | No grade was raised to meet it. Thin modules are rated in `ARCHETYPE.md`, as planned. The validator's generic 15-entry minimum also flags acceptance-risk (14), which met its own 12-20 target |
| 4 | Web searches ran out early in most dives (often 6-12 per agent) | Landscape leads and `curl` carried the work; consulting and accounting coverage stayed thin. Future briefs: name target firms and pages per module up front |
| 5 | Key primary texts blocked (ABA Formal Opinion 512, SRA pages, some vendor sites) | Read through named secondary sources and labelled "as quoted by"; a blocked SRA notice is marked search-only |
| 6 | The NBER trial was labelled independent in some files | Settled as vendor-published with a note on who ran it |
| 7 | Verification corrected 82% of entries | No change: verification stays mandatory. The common fixes are the same as earlier waves (attribution, dates, statistics described as something else, embellished wording) |
