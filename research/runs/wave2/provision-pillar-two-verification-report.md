# Verification report: tax / provision-pillar-two

- **Verified:** 2026-10-17 (verifier brief `verify-provision-pillar-two.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/provision-pillar-two.yaml` (16 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/provision-pillar-two.md`
- **Method:** I reopened all 52 distinct sources with `curl` in a private working folder: the 36 cited in the YAML and the 16
  more keyed only in module §10. I used `pdftotext`/`pdfinfo` for the 7 PDFs (TEI agenda, PCAOB spotlight, OECD GIR XML user
  guide, EY slipsheet, Deloitte brochure, Werfel appendices, SJSU deck). I used the `r.jina.ai` mirror for the 2 pages that
  returned 403 (Wolters Kluwer, PwC Ireland) and to find the CAQ report PDF. I checked every figure, date, attribution and
  quotation against the page text. For dates I checked `article:published_time`, JSON-LD `datePublished`, `datePosted`,
  datelines, arXiv submission history and PDF creation dates. No web searches were used.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `INFO ... 16 use cases, 0 graded A/B (0%)`
  and the expected WARN that the A/B share is below target.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 4 (`#05`, `#06`, `#07`, `#13`) |
| Fixed | 12 (`#01`, `#02`, `#03`, `#04`, `#08`, `#09`, `#10`, `#11`, `#12`, `#14`, `#15`, `#16`) |
| Rejected | 0 |

Every cited source exists and was reached. Each entry's core claim holds once corrected, so nothing was rejected. The module
file received 15 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 0 | 0 |
| C | 13 | 13 |
| D | 3 (02, 06, 10) | 3 (unchanged) |

- No grade changed. The C grades are already the floor for vendor claims. The synthesis chose to grade the six rules-based
  software entries (`#09`, `#11`, `#12`, `#13`, `#15`, `#16`) for **AI use**, which gives C, rather than for software
  automation, which would give A or B. I confirmed that none of their sources claims AI for the core work, so that choice
  stands. One nuance: the unnamed insurer's case study says the XatBot copilot helped with day-to-day filing issues. I added
  this to `#16` and the module, but because the customer is unnamed it does not lift any grade.
- `#14` (XatBot) stays at C. It is the only generative-AI use with a customer, and that customer is unnamed.
- No A or B entry exists, so no search-only figure supports one. Every YAML source is `access: full`.

**Ladder (unchanged):** assist 2, augment 6, automate 8, delegate 0. **Change scope (unchanged):** step 11, process 3, model 2.

## 3. Fixes and rejections

### Use cases

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | 01 | Problem: provision team "moves between spreadsheets and research tools to check ... uncertain tax positions" [BTAX-ASC740-2026] | Fix | Embellished. The page says only that tax teams face immediate pressure after close, and it pitches in-spreadsheet research "to reduce interruptions". It does not mention uncertain tax positions |
| 2 | 01 | "TR reports from its Future of Professionals 2025 report that 91% ... 41% ..." | Fix | Wrong document. The TR blog gives the 91%/41% figures without naming a survey; the FoP report is cited only for other figures (51%, 22%, 80%). Now reads "TR states ..., the article does not name the survey" |
| 3 | 02 | TEI Midyear "ran a hands-on Tax Lab"; date 2026-03-15 | Fix | The source is a *preliminary* programme (PDF created 2026-02-09), so it shows what was scheduled, not what took place. "Hands-on" belongs to the Power Query lab, not the AI lab (embellished qualifier). Now reads "scheduled". Date set to 2026-02, matching the compliance-corporate verifier's fix for the same ref |
| 4 | 03 | "Its [Kognitos's] figure that 58% ... comes from the TR 2025 survey" | Fix | Unsourced link. Kognitos cites "one analysis" without naming it. Now: Kognitos cites an unnamed analysis, and the same figure appears in TR's survey of 288 departments |
| 5 | 03 | Checkpoint: "Tax staff review the exceptions the data layer raises" [KOGNITOS-2026] | Fix | Unsourced connective claim. Kognitos says its platform reasons about exceptions and logs steps; it never says who reviews them |
| 6 | 03 | role_evolution: "TR and Kognitos both say the time returned goes to forecasting, modelling and advisory work" | Fix | Wrong speaker for part of it. Only Kognitos says forecasting/modelling/advisory; TR says "judgment-intensive work" |
| 7 | 04 | Prerequisite: Finrep says "anomaly detection otherwise flags noise with the signal" | Fix | Claim attached to the wrong step. Finrep's noise/signal pitfall is about Step 1 (difference identification), not Step 3 anomaly detection. Reworded, and the Step 1 locator added |
| 8 | 04 | Checkpoint: "A reviewer clears each flagged item before sign-off" | Fix | Embellished. Finrep says only that outliers are flagged "for human review before close" |
| 9 | 04 | TR-JOB-2026 locator "third bullet" | Fix | Anomaly detection is in the second bullet |
| 10 | 08 | "Orbitax says its Tax Flows mode ... sends comparison reports" | Fix | Mixed attribution. Orbitax's release says Tax Flows tracks regulatory changes; "distributes comparison reports" comes from TR's article. Now attributed separately |
| 11 | 08 | Prerequisite "the platform's regulatory content across jurisdictions"; checkpoint "stakeholders ... decide the accounting or compliance response" | Fix | Unsourced connective claims. Replaced with what the sources say: a XatBot subscription, and reports go to stakeholders, with no review step described |
| 12 | 08, 11 | OECD-SBS-2026 (KPMG UK) dated 2026-01-22 | Fix | Wrong date. JSON-LD `datePublished` is 2026-01-21 |
| 13 | 09 | "AMG says the Accelerator cut its implementation path to around 10 days" | Fix | Wrong speaker. The ~10-day line is Orbitax's narrative in the case study, not an AMG quote |
| 14 | 09 | Prerequisite "Finance teams ... willing to supply entity-level data" | Fix | Embellished. The case study says data was collected "through close collaboration with accounting and finance teams" |
| 15 | 10 | EY's technology leader says "... intrinsic data quality issues still need human correction" | Fix | Wrong speaker. The intrinsic-data point is the article's own text (and Charles Brayne), not John Farrelly. Now attributed to the EY article |
| 16 | 11 | Prerequisite "Tracking each OECD package and local law" [WK-PILLAR2-2026] | Fix | Embellished. Wolters Kluwer mentions OECD releases (guidance, safe harbours, GIR artefacts), not local law |
| 17 | 11 | Checkpoint "Tax staff review dashboards and results before filing" [EY-GLOBE-ENGINE-2026] | Fix | Overstated. The slipsheet lists dashboards and reports to review; it does not describe a staff review step. Reworded |
| 18 | 12 | "only 20% of GIRs were filed successfully ..., the rest failing validation" | Fix | Statistic overstated. The source says "based on KPMG's experience", and that in those jurisdictions "the vast majority failed initial validation checks". Both qualifiers restored |
| 19 | 12 | role_evolution: work shifts toward managing data, validation results and local filings, "a point Lucanet and Orbitax make" | Fix | Wrong document. The Lucanet article says nothing about role shifts. Now cites only what Orbitax says about local obligations and post-calculation work, plus Lucanet's actual point (XML mapping needs technical skill) |
| 20 | 14 | Verification risk omitted Orbitax's "without requiring a separate manual verification step" | Fix | The omission softened the vendor claim. Restored, and marked as not independently tested. Autopilot checkpoint now notes that the user can also launch without review |
| 21 | 15 | "Deloitte Germany demonstrated it live in a February 2026 webcast" | Fix | Overstated. The source is a pre-event notice that promised a live demo, not evidence that one happened. DELOITTE-ITR-2025 was listed but never cited; it now supports an award sentence |
| 22 | 15 | Checkpoint "Clients review and sign off data and results"; role_evolution "client team steps back to review and sign-off" | Fix | Embellished, and an unsourced connective claim. The brochure offers "options for reviewing and signing off on data". The role sentence was replaced with "no source describes" |
| 23 | 15 | Notes: "Deloitte survey date and sample are not given on the page" | Fix | Contradicts the page, which gives the sample as "over 500 tax leaders and CFOs". Only the date is missing |
| 24 | 16 | Notes say "software, not AI" with no mention of XatBot | Fix | The insurer case study cited in `#16` says XatBot helped its team; now disclosed |

### Module file

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| 25 | §1 | "the hard part was data and XML plumbing, not tax law or AI [FGS, BTAX-KPMG]" | Fix | Embellished. Neither source mentions AI; FGS says XML creation and transmission, not tax law. Rewritten with each source's own point |
| 26 | §3 | `#16` "Ask whether AI is part of either; the sources say no" | Fix | The insurer source mentions XatBot helping. Corrected |
| 27 | §4 probe 10 | "TR hires experienced provision staff" | Fix | It is a job posting. Now "is recruiting" |
| 28 | §5 | 67% row: "sample not stated on the page" | Fix | The page states 288 tax departments worldwide |
| 29 | §5 | 91%/41% row attributed to "TR Future of Professionals 2025" | Fix | Same misattribution as fix 2 |
| 30 | §5 | 70%/76% row: no sample | Fix | Added "over 500 tax leaders and CFOs" from the page |
| 31 | §5, §6, §10 | CAQ 12% "search-only, relayed by a BDO article"; §6 "BDO says tax errors are a common source of material weakness (via CAQ)" | Fix | I found and read the CAQ report PDF. The Taxes row shows 717 restatement events, 12% of 5,793 for 2013–2022, falling to 7% in 2022, so the figure is now `full` and its measure is stated precisely. The BDO material-weakness claim was attributed to the wrong document (it is not in the CAQ report) and the BDO article could not be located, so it was removed |
| 32 | §6 | "PCAOB staff ... say ... the user stays responsible"; "Nothing tax-specific exists" | Fix | Wrong speaker. Audit *firms* told PCAOB staff that an engagement team member using GenAI stays responsible. The absence claim is now "was found" |
| 33 | §7 | "Lucanet and Orbitax say Pillar Two work shifts toward managing data, validation results and local filings" | Fix | Same as fix 19 |
| 34 | §7 | "A SaaS company's tax manager posting" | Fix | The posting does not call Gamma a SaaS company. Now "Gamma's senior tax manager posting" |
| 35 | §8 | TEI Midyear "ran" sessions | Fix | Preliminary programme; now "scheduled", with the programme date |
| 36 | §8 | KPMG Digital Gateway "tax clients first" | Fix | The release says "initial focus on tax clients and private equity (PE) firms" |
| 37 | §9 | "PCAOB staff say the user stays responsible"; "the platforms used in the first season are rules-based" | Fix | Wrong speaker (see 32), and an overgeneralisation from two entries |

Checked and confirmed without change: all §2 step-table claims, the ASU 2023-09 thresholds and effective dates, the OECD
June and September 2026 packages, the 120+ business rules, the 19 + 37 jurisdictions, 1,700+/34/60%/one-third, AMG's
2 people/70-80 entities/25 jurisdictions, the EY 85%/81%/21% figures (n = 1,600), the KPMG Germany 71/66/47/41/41/58/72
figures, the Paperjam 92%, TaxCalcBench "less than a third", the Law&Order date and its LLM-plus-verification method,
the SJSU multi-agent slide, the TPMinds 18 June session, the Acast 25 June episode, PwC Ireland's forecasting and new-role
statements, the AICPA CART (20 risk areas), Sala's argument, and the Apple and TR job postings and their dates.

## 4. Sources that couldn't be reached directly

- **Wolters Kluwer** procurement guide (403): read through the `r.jina.ai` mirror, published 2026-02-16. Claims confirmed.
- **PwC Ireland** (403): read through the mirror, dated 21 July 2026. Claims confirmed.
- **CAQ landing page** shows no tax figure. The linked report PDF was downloaded and confirms the 12%.
- **BDO article** (the old relay for the CAQ figure): no URL was recorded and none was found. Its material-weakness
  statement was removed.
- Not reopened because nothing in these files relies on them: the OECD's own June 2026 GIR XML guidance (cited through
  OECDPillars), the FASB ASU page (cited through KPMG), the Deloitte and EY survey reports (figures come from their pages),
  and the Orbitax First Pillar Two Filing Report.

## 5. Targets

| Target | Result |
|---|---|
| 15–25 use cases | Met (16) |
| ≥ 50% graded A or B | **Not met (0%)**. This is structural. No named organisation publishes AI use in the provision or Pillar Two work, and the six named deployments are rules-based software graded for AI use. Meeting the target would mean either grading the software entries on their own terms (`#09` and `#16` would be A, `#11`, `#12` and `#15` would be B) or finding new named AI deployments |
| Every source dated | Met. Every YAML source has an ISO date. CORPTAX-2026 is year-only because the page is undated. Every module-only key in §10 carries a date |
| Ids unique, vocabulary values valid | Met (validator 0 errors) |
| Quotations under 25 words | Met. The longest is "with appropriate professional judgment applied" |

## 6. Error patterns to fix in the briefs

1. **Wrong speaker inside one source.** Analysts attributed the article's narrative or another person's words to the quoted
   expert or customer: AMG's "10 days" (Orbitax), EY's Farrelly (article text), "PCAOB staff say" (audit firms said),
   Orbitax Tax Flows reports (TR said). Briefs should require naming *who* in the source says it.
2. **Co-citation laundering.** A second source was added to a claim it doesn't support (Lucanet on role shifts, TR on
   forecasting work, WK on local law). Briefs should require every cited source in a multi-ref sentence to support the
   whole sentence, or the sentence should be split.
3. **Event notices and preliminary programmes reported as events.** "Ran", "demonstrated" and "held" were used for TEI's
   preliminary programme and Deloitte's webcast notice. This recurs from compliance-corporate, so briefs should mandate
   "scheduled" or "promised" wording and the programme's own date.
4. **"Not stated" claims that are false.** Sample sizes were said to be missing when the page gives them (TR's 288,
   Deloitte's 500+). Briefs should require a search for "surveyed/respondents" before writing "not stated".
5. **Survey attribution drift.** A figure was credited to a named survey when the page doesn't make that link (91%/41% to
   FoP). Only name the survey when the sentence carrying the figure names it.
6. **Unsourced checkpoints and role lines.** Several `human_checkpoints` and `role_evolution` fields described plausible
   review steps that no source mentions. When the source is silent, briefs should default to "No source describes the
   review step".
7. **Search-only figures can often be upgraded.** The CAQ 12% was reachable as a PDF from the landing page. Briefs should ask
   analysts to follow landing-page download links before marking a figure search-only.
8. **Shared refs with different dates across modules** (TEI-MIDYEAR-2026 2026-02 vs 2026-03-15; BTAX-ASC740-2026 "2026" in
   one compliance-corporate entry vs JSON-LD 2026-03-25 here). Synthesis should reconcile ref dates repo-wide. Here I aligned
   TEI to 2026-02 and kept BTAX-ASC740-2026 at 2026-03-25, which JSON-LD `datePublished` confirms. The other module's
   year-only date should be updated to match.
9. **Open date question, not changed.** AICPA-WERFEL-2026 is dated 2026-06 in 24 places (upload path 2026/06, PDF created
   2026-05-14). The CART article of 23 September 2026 calls the framework "published earlier this month", so the article
   itself may date from September 2026. Worth a check by whoever owns the cross-cutting guardrails module.
