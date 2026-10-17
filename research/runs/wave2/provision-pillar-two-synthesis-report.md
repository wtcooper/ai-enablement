# Synthesis report: tax / provision-pillar-two

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-tax.md`, `tax-provision-pillar-two-combined.md` (one combined deep dive; the landscape rated provision low-density and recommended combining it with international-pillar-two), plus the "Routed to other modules" sections of every other `tax-*-*.md` file in wave 2.
- **Outputs:** `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/provision-pillar-two.md` (243 lines) and `.../tax/use-cases/provision-pillar-two.yaml` (16 entries). `scripts/validate.py`: 0 errors; one expected warning for this file (A/B share 0%, below the 50% target).

## Counts in and out

| | Combined deep dive | Routed items | Total |
|---|---|---|---|
| Candidates in | 16 (A 2, B 3, C 8, D 3) | 0 new candidates (facts and figures only) | 16 |
| Out | | | 16 (A 0, B 0, C 13, D 3) |

No candidate was dropped. One routed item could have become an entry (provision-side forecasting of effective tax rates and deferred tax balances, PWC-IE-2026); it was cross-referenced to `tax-compliance-corporate-14` and `-18` instead, because those published entries already describe the same change.

## Duplicates merged

None. The 16 candidates describe distinct changes. Pairs checked and kept apart:

- combined-08 (CbCR seeding) and combined-16 (insourcing): same AMG case study, but one is a data step and the other a sourcing-model change.
- combined-14 (firm-run platform) and combined-16 (in-house platform): opposite sourcing choices, not the same change.
- combined-04 (ASU 2023-09 categorisation) and combined-05 (footnote drafting, idea): data categorisation versus narrative drafting.
- combined-01 (research in tools) and combined-15 (Excel workpaper analysis, idea): research answers versus checking the workbook itself.

Overlaps with other published tax modules were cross-referenced by id rather than duplicated: `tax-compliance-corporate-01`, `-03`, `-07`, `-09`, `-10`, `-11`, `-12`, `-13`, `-14`, `-15`, `-18`; `tax-research-advisory-01`, `-23`; `tax-transfer-pricing-04`, `-21`.

**Id map (final ← combined):** 01←01, 02←15, 03←02, 04←03, 05←04, 06←05, 07←07, 08←06, 09←08, 10←09, 11←10, 12←11, 13←12, 14←13, 15←14, 16←16.

**Other normalisation:** -15 runtime changed from `managed-agent-runtime` to `workflow-automation` (no agent is described). Titles of the six rules-based entries now say "no AI claimed". Canonical keys: BTAX-KPMG-GIR-2026 (the tax-data-technology discourse file calls the same article BTAX-KPMGP2-2026); SALA-TAXNOTES-2026 (not TAXPROF-SALA-2026), as in compliance-corporate; KPMG-DE-2026 dated 2026-05, as in compliance-corporate. The TPMinds Pillar 2 Summit page (agenda/4/, 18 June 2026) gets its own key, TPMINDS-P2-2026, because it is a different page from TPMINDS-INTL-2026.

## Grading decision (important)

Grades are for **AI use in this module**, as instructed. Five candidates were graded A or B in the input for rules-based software: combined-08 and -16 (A; AMG case study, vendor-published) and combined-10, -11 and -14 (B). The sources state that none of these uses AI. All five are now **C**, together with combined-12 (already C, also not AI). Each note says what grade the software evidence alone would earn. I chose C over D because D must be labelled "idea", which would misdescribe deployments that are real. C covers the only AI link these entries have, which is vendor positioning: TR presents Orbitax's Pillar Two tooling under "AI in corporate tax", Orbitax offers XatBot to GMT users, and Deloitte calls its platform an "Agent". The vocabulary has no grade for "real deployment, no AI" (see the suggestions below). Maturity on these entries still describes the software (`in-production`).

## Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 01, 02 (D) | | | 2 |
| augment | 04, 05, 06 (D), 08, 10 (D), 14 | | | 6 |
| automate | 03, 09*, 13* | 07, 11*, 12* | 15*, 16* | 8 |
| delegate | | | | 0 |

\* rules-based software, no AI claimed.

- **Delegate: no evidence.** The only signal is a TEI-SJSU panel deck that places multi-agent provision-to-return workflows at the top of a progression (SJSU-TEIHTTI-2025, held by tax-data-technology). It is mentioned under Frontier, not added as an entry.
- **AI automate** rests on vendor descriptions only (-03, -07).
- **Process and model scopes** are covered only by rules-based software, apart from the R&D-credit vendor claim (-07).
- **Assist and augment** for AI are all C or D: vendor pages, a roadmap, a job posting and one embedded assistant (XatBot) with an unnamed user.

## Grade mix

A 0, B 0, C 13 (81%), D 3 (19%). Grades were not raised to reach the 50% A/B target, and the module says at the top that its evidence is thin. If grading were for software rather than AI, the mix would be A 2, B 3, C 8, D 3.

## Gaps

- **No AI-in-provision customer or outcome.** No named company reports AI in its ASC 740 provision with a result. No error rate, override rate, parallel run or independent accuracy test exists for any provision or Pillar Two AI use.
- **No audit-side evidence.** Nothing from a regulator, standard-setter or audit firm covers auditing AI-prepared tax balances. The PCAOB July 2024 staff spotlight is generic, and PCAOB inspection reports were not opened.
- **Primary documents not reached:** OECD June 2026 XML guidance (seen via OECDPillars), the FASB ASU page (403), the IAS 12 amendment text, the EY TFO survey report, Deloitte's Pillar Two research, Orbitax's full filing report, and its other named case studies (EPAM, Columbia Sportswear, NXP).
- **Search-only and excluded from grading:** PwC Finland's Pillar Two Engine, the ChatFin cycle-time claim, Finrep's adoption statistics, and the CAQ 12% restatement figure (used once in the module, flagged as search-only).
- **Steps with no AI evidence:** valuation allowance, the current-tax computation, Pillar Two notifications and QDMTT registrations, and IAS 12 Pillar Two accounting.
- **Discourse:** no transcripts from the TEI labs, the Bloomberg forum or the TPMinds Pillar 2 Summit, and no practitioner community threads.

## Items routed to provision-pillar-two from other files

Used:

- Kognitos data-layer argument, Bloomberg Workpapers, Neo.Tax provision link and ASU 2023-09 (compliance-corporate practice, discourse and governance): already in the combined dive, -03, -05 and -07.
- PwC's explainable ETR model (PWC-MEGNA-2025; research-advisory practice and governance, compliance-corporate discourse): cross-referenced as `tax-compliance-corporate-18`, not duplicated.
- Bloomberg Tax error-compounding point (BTAX-HALLUC-2026): -01 and -08.
- PWC-IE-2026 forecasting and new roles (tax-data-technology discourse): §3 and §7, cross-referenced to `tax-compliance-corporate-14`.
- EY-TFO-2025, 21% very prepared for Pillar Two (tax-data-technology governance): §5.
- CAQ-RESTATE-2024 via BDO (tax-data-technology governance): §5 and §6, flagged search-only.
- APPLE-JOB-2026, Pillar Two knowledge preferred (tax-data-technology practice): §7.
- EY-PAPERJAM-2026, 92% expect disputes to rise (controversy practice): §5.
- TPMinds Pillar 2 Summit session (transfer-pricing discourse): §8.
- BTAX-FORUM-2026 (controversy governance): §8.
- GIR XML pipeline detail (tax-data-technology discourse): already in -12.

Not used:

- AIBIDIA-PRIORITIES-2026 and AIBIDIA-TPMINDS-2026 (Pillar Two and GloBE interplay with operational transfer pricing; transfer-pricing practice): the routing line gives no detail and the sources were not in this synthesis's inputs.
- Pillar One Amount B and UN dispute-prevention items (transfer-pricing governance): not Pillar Two.
- Tax policy of AI (nexus, permanent establishment) and the taxability of AI products (research-advisory and indirect-tax discourse): tax on AI, not AI in tax work.

## Routed from this module's inputs to other modules (for their synthesis)

- **compliance-corporate:** Neo.Tax, R&D credit automation and Form 6765 Section G (TR-CORPAI-2026).
- **indirect-tax:** Savant Labs with Oxford Industries (SAVANT-2026).
- **controversy:** Corptax "audit prediction" roadmap item (CORPTAX-2026).
- **transfer-pricing:** TP and statutory reporting as AI growth areas; the Oxford session on delegating decisions to AI (TR-CORPAI-2026, OXFORD-CBT-2026).
- **compliance-individual-business:** TaxCalcBench, the legal-critical software agent study, Law&Order (ARXIV-TAXCALCBENCH-2025, ARXIV-LEGALCRITICAL-2025, ARXIV-LAWORDER-2026).
- **guardrails and professional responsibility (cross-cutting):** hallucination risk, AICPA CART, the Werfel framework (BTAX-HALLUC-2026, AICPA-CART-2026, AICPA-WERFEL-2026).
- **workforce and talent (cross-cutting):** Sala, the Gamma and Thomson Reuters postings, KPMG Germany headcount (SALA-TAXNOTES-2026, GAMMA-JOB-2026, TR-JOB-2026, KPMG-DE-2026).
- **state of AI disruption (cross-cutting):** KPMG and Anthropic alliance (KPMG-ANTHROPIC-2026).
- **assurance archetype, audit module:** PCAOB observations on auditors' GenAI use (PCAOB-GENAI-2024).
- **tax-data-technology:** Orbitax MCP connections, Lucanet on XML, public CbCR (ORBITAX-XATBOT-2026, LUCANET-2025).

## Suggested improvements to the briefs

1. **Add a way to record "real deployment, no AI".** Examples: an `ai_claimed: true|false` field, or a rule that grades software-only deployments C with a fixed note. Without it, platform evidence either inflates the A/B share or has to be forced into C or D.
2. **Tell deep-dive analysts to grade for AI use from the start**, and to put software-only evidence in module context rather than in A or B entries.
3. **For modules rated low-density, allow fewer than 15 entries**, or count cross-references to other modules toward the target. Padding to 15 risks weak entries.
4. **Give a canonical-key registry** for documents that several deep dives cite (for example BTAX-KPMG-GIR-2026 and BTAX-KPMGP2-2026, and the TPMinds pages), so synthesis does not have to reconcile keys.
5. **Ask routed-item lines to carry enough detail to use** (claim, figure, locator). Several routed items (the Aibidia pair) are one-line pointers that synthesis cannot verify.
6. **Add an audit-reliance search angle** for provision (PCAOB inspection findings on income taxes, the Big Four tax accounting groups' publications) in the next wave. It is the module's main open question.
