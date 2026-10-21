# Verification report: advisory / transactions

Checked 2026-10-21 against every cited source. Files edited in place:

- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/transactions.yaml`
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/transactions.md`

All 49 URLs were opened, either directly or through the r.jina.ai mirror. Every use-case source exists. Six had the
wrong date, URL or attribution and were fixed. One search-only source was dropped because its URL is dead.

## Counts

| Action | Use cases |
|---|---|
| Kept | 1 (`-16`) |
| Fixed | 15 (`-01` to `-15`) |
| Rejected | 0 |

No grade changed. Most fixes are wording, attribution or dates. Five entries (`-03`, `-05`, `-06`, `-07` and `-08`)
were changed only because a shared source, QOEAGENT-HOME-2026, had the wrong date. That date changed everywhere it
appears.

## Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 0 | none |
| B | 5 | 01, 02, 03, 09, 11 |
| C | 10 | 04, 05, 06, 07, 08, 10, 12, 13, 14, 15 |
| D | 1 | 16 (idea) |

The B grades hold. Each rests on a named deployment or a named customer: the Forvis Mazars Group rollout, Miller Cooper,
QoEAgent's named searcher client, PwC's ToltIQ usage counts and Deloitte's count of 1,000+ engagements. None reports a
measured outcome, so no entry meets the A rule. Miller Cooper's "shaved days" comment is a recollection, which the
2026-10-17 rule caps at B.

## Fixes and rejections

| Entry / location | Problem found | Fix |
|---|---|---|
| 01 human checkpoint | "Judgment calls between dataroom and report" was attributed to Opio's site. The phrase comes from the Opio boilerplate in the Forvis Mazars Group release | Reworded to what the Opio site says ("AI suggests, and your team shapes the conclusion") |
| 01 risks | Not a factual error: Opio's site markets "controlled delegation… without supervising", which conflicts with the Group's mandatory human review | Added as a risk, with both sources |
| 02 risk | The practitioner was described as one who "sells a competing tool". The source says he "built and used" Provafi | Reworded; reply date (about 2026-01) added to the locator |
| 02 checkpoint, risk | An unsourced connective claim that the QoE team "decides which flags become adjustments" | The release only says flags are "potential EBITDA adjustments to discuss with management". Now says that, and says who decides is not stated |
| 03 problem | "Takes weeks (QoEAgent)" was cited to pages that do not say it | Now cited to QOEAGENT-SBAREQ-2026 ("weeks of work"; "about four weeks" by hand); source added |
| 03 outcomes | A better vendor figure was available | Added the vendor-published 99.4% match rate on one engagement (QOEAGENT-WHO-2026). Notes now say the case page does not show which steps the software performed |
| 03, 05 to 08 (shared source) | QOEAGENT-HOME-2026 was dated with the access date and called "undated". The page carries article:modified_time 2026-10-15 (first published 2025-12-09) | Date set to 2026-10-15 in all five entries |
| 04 risk; module §5 | Intralinks cluster figures were left out | Added the 48% access-control and 40% hallucination figures, with the caveat that the base is not stated |
| 05 solution | "Fixed fees quoted up front" for QoEAgent is not on the cited page | Removed. Product list corrected to QoEAgent's four products plus the lender QoE |
| 05 outcome; module §3, §5 | Shepi's $1,000 price is on /pricing, not on the cited home page | New source SHEPI-PRICING-2026; Done-For-You $5,000 added |
| 05 sources | QOE-VENDORS-2026 (Barchart, search-only) now returns "page not found" | Source removed; notes say why |
| 06 | Missing evidence for the sub-contract model | Added Shepi's Firm Edition (white-label and resale) and QoEAgent's "we are their capacity" model, where the CPA firm signs the report. Grade stays C, maturity stays announced |
| 07 problem | "Lenders and buyers need many such reports quickly" had no source | Replaced with QoEAgent's sourced claim that the rule adds weeks to the credit process |
| 07 SBA | Could the clause be confirmed against the SBA text? | Tried again: the SOP 8.1 .docx linked from sba.gov still returns 404. The clause stays labelled as QoEAgent's reading; page last-updated date added |
| 09 (and module §7) | Wrong speaker: Toby Popplewell was called "PwC UK deals leader". ICAEW gives his title as transactions director and deals GenAI leader | Corrected in every place |
| 09 role_evolution | Distorted quote: "hard to predict which tasks are replaced versus created". He said replacement is *easier* to predict than creation | Corrected |
| 09 problem; module §2 | Tense embellished: contract review "is often descoped". He said it *was*, two years earlier | Corrected |
| 10 problem, notes | The causal framing ("routine consumes the time") goes beyond the source, and the author was called a "practice leader" | Reworded to the article's claim; author named as managing director Mike Laurie |
| 11 source URL | The DELOITTE-MAPLATFORM-2026 URL returned 404 | Corrected to `/us/en/about/press-room/…`; release content confirmed |
| 11 problem | "Deal teams run … as separate, isolated tasks" overstated the release | Reworded to the release's own contrast with "isolated M&A tasks" |
| 11, 14 | DELOITTE-PULSE-2026 was dated "2026" and called undated | The page's JSON-LD gives 2026-07-27; date set |
| 12 problem; module §2 | "Slow, senior-reviewed work" was attributed to the job posting, which says neither | Rewritten to what the posting shows: specialist work that needs 4+ years at a top firm. Added that no source measures the time |
| 12 risk | "AU$440,000 government review" was garbled | Now reads "final instalment of its AU$440,000 contract for a government review" |
| 13 outcome; module §3, §5 | A statistic reported as something it does not measure: S&P's 31% was labelled "GPs". The release's respondents include PE, VC and LPs, and the report itself (quoted by Post-Trade 360) says "just shy of one in four GPs" | Relabelled "31% of respondents"; conflict explained in notes and in the module table |
| 15 problem | Embellished cause: integration "pushes acquirers to rip out and replace". The abstract says knowledge is threatened, and only the first acquirer ripped and replaced | Corrected |
| Module §5 | McKinsey row said "corporate acquirers, not TAS". That is not stated in the source | Changed to "M&A generally, not TAS-specific (survey February 2025)" |
| Module §8 | PwC/ToltIQ "exclusive relationship" overstated the deal | Corrected: a strategic relationship, with PwC as ToltIQ's exclusive professional services advisor |
| Module §8 | Fasken "likely recurring" exclusions overstated the article | Corrected: scrutiny is underway, and *some* insurers *may* standardize exclusions |
| Module §9 | Claim attributed to the wrong document: the RSM 40% external-consulting figure is not on the cited RSM introduction page | Re-sourced to CPA Practice Advisor's report of the survey (CPAPA-RSMMM-2026, 2026-07-22), the ref the risk-controls module already uses. Wording changed from "buyers" to "dealmakers" for the Datasite 45% |
| Module §7 | "Withum's leader" was vague and overstated the quote | Corrected to the managing director of advisory services; wording matched to the quote |
| Module §10 | The arXiv paper was described as simply "withdrawn" | The source says "temporarily withdrawn", by the authors; corrected |
| All entries | — | `last_reviewed` set to 2026-10-21; YAML header notes the verification |

No use case was rejected.

## Sources that couldn't be reached

| Source | Status | Effect |
|---|---|---|
| SBA SOP 50 10 8.1 .docx (linked from SBA-SOP5010-2026) | 404 from sba.gov; the archive.org copy reset the connection | The QoE clause stays "per QoEAgent's reading". The SBA landing page (version, effective date) was read |
| QOE-VENDORS-2026 (Barchart) | Page not found | Removed |
| AM-EURODD-2026 (Alvarez & Marsal) | 403 | Stays search-only, in notes of a C entry, not used as an outcome |
| FASKEN-RWI-2026 | Direct fetch 403 | Read in full through the r.jina.ai mirror |
| QOEAGENT-SBAREQ-2026; POSTTRADE-SPGLOBAL-2026; RSM page; CTACQ-QOE-2026 | Mirror blocked (CAPTCHA or rate limit) | Read directly with curl |

## Targets

| Target | Result |
|---|---|
| 12 to 20 use cases | Met: 16 |
| At least 50% graded A or B | **Not met**: 5 of 16 (31%). The public evidence does not support more B grades. A or B would need named-firm outcome data, such as Forvis Mazars measuring its Opio pilot or PwC publishing ToltIQ accuracy or time data |
| Every source dated | Met. Every source has an ISO date. One is year-only: ECIS-PMI-2026, whose page shows no month. Undated pages (Opio, Shepi home and pricing, EY Diligence Edge, SEC eCFR) carry the access date |
| Ids unique, vocabulary values, quotations under 25 words | Met. `validate.py` reports 0 errors; the only transactions warning is the A/B share |
| Cross-references | All exist: assurance-acceptance-independence-15; professional-services-scoping-pricing-16, -17, -19; talent-learning-07, -19; quality-review-04; delivery-management-03; staffing-resourcing module. The "valuation module" named in §1 has no module file yet in `advisory/modules/` |

## Error patterns to fix in the briefs

1. **Speaker titles drift upward.** A "deals GenAI leader" became "deals leader", and a "managing director" became a
   "practice leader". Briefs should require the exact title as printed.
2. **Quotes get paraphrased into the opposite meaning.** "Easier to predict replacement than creation" became "hard to
   predict either". Paraphrases of attitude or prediction claims should be checked against the quote.
3. **Tense and cause get embellished.** "Was descoped" became "is descoped", and "threatens knowledge" became "pushes
   acquirers to rip and replace". Present tense and causal verbs need a source sentence.
4. **The population behind a statistic gets mislabelled.** The S&P "31% of GPs" is the clearest case. Briefs should
   require the respondent base exactly as the source states it, and a check of any secondary source that quotes the
   report itself.
5. **A figure is cited to the wrong page of the same publisher.** The RSM intro page had no 40% figure, and Shepi's
   price was on /pricing, not the home page. Locators should name the page where the figure was actually seen.
6. **Problem statements get unsourced connective claims** ("slow, senior-reviewed", "need many reports quickly").
   Problem fields need the same source discipline as `role_evolution`.
7. **Dates on "undated" pages.** WordPress and Deloitte pages carry article:modified_time or JSON-LD dates. Check
   these before falling back to the access date.
8. **URLs copied with path errors.** The Deloitte URL had `about-us` for `about`. Re-fetch every URL at synthesis.
