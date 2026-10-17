# Verification report: tax / transfer-pricing

- **Verified:** 2026-10-17 (verifier brief `verify-transfer-pricing.md`, wave 2)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/transfer-pricing.yaml` (22 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/transfer-pricing.md`
- **Method:** I extracted all 78 distinct URLs cited in the two files (YAML plus module §10) and reopened every one with `curl`
  in a private working folder. I used `pdftotext` for the 8 PDFs (CIAT working paper, ABA May Meeting programme, Riddle
  Aggregates transcript, KPMG TaxNewsFlash reprint, Werfel appendices, TIGTA, Oxford CBT booklet). I used the `r.jina.ai`
  text mirror for the pages that returned 403 or 404 (BDO Canada, Aprio, GAO, KPMG Germany 2025, ABA Tax Times). I checked
  every figure, date, attribution and quotation against the page text. For dates I checked on-page bylines,
  `article:published_time`, JSON-LD and PDF metadata. I used one web search, to date the Aibidia/BIP announcement.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this module it gives `INFO ... 22 use cases, 3 graded
  A/B (14%)` and the expected WARN that the A/B share is below 50%. The other warnings belong to other streams' files.

## 1. Counts

| | Use cases |
|---|---|
| Kept as written | 6 (`#03`, `#04`, `#11`, `#12`, `#16`, `#20`) |
| Fixed | 16 (`#01`, `#02`, `#05`, `#06`, `#07`, `#08`, `#09`, `#10`, `#13`, `#14`, `#15`, `#17`, `#18`, `#19`, `#21`, `#22`) |
| Rejected | 0 |

No grade changed. Every source the entries rely on exists and opened. The figures in A and B entries match their pages.
Most fixes correct wording that went further than the source, a misquote, or a date.

## 2. Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 1 | `#09` (Trivium and Fortum statements on the vendor's site; rules-based document automation, not shown to be AI) |
| B | 2 | `#12` (Kemira), `#21` (Trivium and Fortum insourcing) |
| C | 16 | `#01`-`#08`, `#10`, `#11`, `#13`-`#16`, `#19`, `#22` |
| D | 3 | `#17`, `#18`, `#20` (all titled "(idea)") |

A/B share: 3 of 22 (14%).

## 3. Fixes and rejections

| Entry / location | Problem found | Fix |
|---|---|---|
| `#01` role_evolution | Merged two webinar speakers into one "participant". One speaker (Bas van Houts) talked about checking definitions, deadlines and local requirements. A different speaker (Luis Nouel) talked about not burdening the central team. | Rewrote to attribute each point to a different speaker. |
| `#02` human_checkpoints | Embellished qualifier. The source says "an accountable professional", not a "named" one. | Removed "named" and quoted the source's wording. |
| `#05` prerequisites, human_checkpoints | "Source websites the practitioner can cite" and "checks facts and sources" are not in the DDTC report. | Cut to what the source says: detailed instructions to the model, and supervision, risk assessment and quality clean-up of AI drafts. |
| `#06` risks | Unsourced connective claim ("a screen that cannot show its rejection logic fails that expectation") read as if the IRS said it. | Marked it as an inference, not an IRS statement. |
| `#07` problem, solution, notes | (a) The "most common mistake" quote was narrowed to generic descriptions only. The speaker named check-the-box documents that lack substance, generic or copied descriptions, and outdated benchmarks. (b) "BDO lists drafting and summarising" was vaguer than BDO's actual list. (c) The notes said the survey percentage was "not readable", but the page states 75%. | Restored the full quote, listed BDO's actual items, and added the 75% figure labelled as an expectation. |
| `#08` risks | A claim about IRS scrutiny was given as fact but comes from an Exactera speaker quoted by Checkpoint. | Attributed it to the speaker. |
| `#09` sources | Wrong date. AIBIDIA-MANUAL-2026 has an on-page byline of 2026-04-29, while the JSON-LD says 2026-05-07. | Date set to 2026-04-29, with the discrepancy noted in the locator. |
| `#10` problem, risks | (a) "Large agreement sets are hard to update and check" is unsourced, and "especially in growing companies" turned the article's audience into a cause. (b) "So poorly aligned agreements may be flagged" was an unsourced connective. The KPMG authors also describe contract reading during South African audit document review, not during selection. | Rewrote the problem to Plante Moran's actual statement. Rewrote the risk to what BTAX-AFRICA-2026 says. |
| `#13` solution | "Vendors describe ERP-connected drift monitoring" rests on one competitor's comparison page. That page attributes the monitoring to Aibidia's "Aurora", which Aibidia markets as a research assistant. | Attributed it to the competitor page and flagged the inconsistency. |
| `#14` outcome measures | Wrong document. The "fictional group and sample data" caveat belongs to the October 2026 preview (TPINTEL). The EUR 4.8m figure comes from the September Helsinki demo (LEADERS), whose data is not described. | Separated the two. |
| `#14` sources | TPMINDS-WC-2026 was dated 2026-11-04, the future event date, not a publication date. | Set to the retrieval date, with the event date in the locator. |
| `#15` risks | Misquote. KPMG-TNF-2024 warns of an AI arms race "among tax authorities with multinationals caught in the middle", not a race between authorities and multinationals. | Corrected and quoted it more fully. |
| `#17` sources, notes | Wrong date. The Proskauer post is dated 29 July 2026 on the page; the entry said "2026-07" and claimed the date came from the syndication path. The Charlotin entry is only visible through the page search. | Date set to 2026-07-29 and the note corrected. The Charlotin locator now gives the search route. |
| `#18` sources, notes | TPMINDS-AM-2027 was dated 2027-03-01, a future event date. | Set to the retrieval date, with the event dates in the locator. |
| `#19` role_evolution, risks | (a) A statistic reported as something it doesn't measure. "Respondents expect AI to touch strategic policy design" implied many did; the page shows only 8%. (b) "Test substance over form" is not in the podcast description, and the topic is TP of AI, an adjacent subject. | Stated the 8% figure as the source gives it. Rewrote the risk to the description's wording and labelled it TP of AI. |
| `#21` problem | "Outsourcing local-file preparation cost over EUR 10,000-15,000" added a cause. The case study says "spending over EUR 10,000-15,000 per entity on documentation". | Reworded to match. |
| `#22` ladder, pattern, runtime, sources | (a) The ladder `delegate`, pattern `end-to-end-case-agent` and runtime `managed-agent-runtime` imply agent delivery. Commenda says "experts do the work", and neither provider says what the AI does. (b) The AIBIDIA-BIP-2026 date of 2026-02-26 does not appear on the page, which shows 3 July 2026 (a re-publication date, as on other Aibidia news items). A secondary company profile dates the partnership to February 2026. | Set ladder `augment`, pattern `other` and runtime `workflow-automation`, with the reason in the notes. Date set to "2026-02", with the basis given in the locator. |
| Module §2 Benchmarking row | Wrong document. "Every rejection must be justified [IRS-TPFAQ-2026]" was attributed to the IRS, but the FAQ's rejection language concerns rejected *methods*, not rejected comparables. | Replaced with the FAQ's actual comparability expectation, plus the hours-or-days claim sourced to the webinar. |
| Module §2 Research row | "About once a year" is firmer than the source's "perhaps once a year". | Quoted the source. |
| Module §3 | "PwC Singapore speakers" said AI may do ~80%, but only the partner said it. | Corrected. |
| Module §5 Comparability row | A statistic reported as something it doesn't measure. Placing the "100 hours to ~30 minutes" figure in a comparability row presents it as comparability work. The senior manager was describing "analysis" from modelling to value-chain work. | Split the two figures by speaker and scope. |
| Module §5 Local-file row | "Was EUR 10,000-15,000 per entity outsourced" added "outsourced". The row also omitted the 2-5 day typical baseline. | Corrected. |
| Module §5 Penalty row | "Up to 40% of the adjustment" is a speaker's wording. The rate base (adjustment versus underpayment) was not checked against a primary source. | Labelled it as the speaker's words, with the rate base unverified. |
| Module §5 | The survey's AI expectation figures (75% first drafts, 8% policy design) were missing. GAO's 126 use cases had no as-of date. | Added a row for the expectations and "as of June 2025" for GAO. |
| Module §8 | (a) "First ABA Tax Section panel on AI and section 482" is not stated in the programme. (b) "2026-06-01 to 2026-08" for the OECD consultation does not match the 22 July 2026 comment deadline. (c) The TPMinds recap date was conflated with the event dates. | Removed "first". Dated the consultation 2026-06-01 to 2026-07-22 and added the 2026-08-24 publication of submissions [HLB-CH7-2026]. Separated the event dates from the 2026-06-25 recap date. |

## 4. Sources that couldn't be reached directly

| Source | Status | Effect |
|---|---|---|
| BDO-AIGOV-2026 (bdo.ca) | 403 to curl and to the default mirror. I read it in full through the `r.jina.ai` browser engine. The page says "Updated: August 20, 2026" and "current as of August 5, 2026". | Claims confirmed; no change. |
| APRIO-AI-2025 (aprio.com) | 403 to curl; read in full through the mirror (published 2025-08-14). | Confirmed. |
| GAO-2026 (gao.gov) | 403 to curl; content read through the mirror. The 2026-03-24 date is not on the mirrored page but matches the date used in other tax files. | Figure confirmed (126 use cases, as of June 2025). |
| KPMG-DE-2025 | 404 (already labelled search-only in `#07`). | Supports nothing on its own; unchanged. |
| ABA-TAXTIMES-2026 (americanbar.org) | 403 to curl; the mirror is blocked for the domain (already labelled search-only in `#16`). | Supports nothing on its own; unchanged. |
| Internet Archive | Temporarily offline during the check. | No archived copies used. |
| CHARLOTIN-DB-2026 | The base page does not list the case; the entry appears only through `?q=Riddle`. | Locator updated. |

Paywalled sources were checked only as far as the open text: the IBFD ITPJ and Intertax abstracts, the opening of the
Bloomberg KPMG Q&A, and the Bloomberg first paragraphs. No claim in the files goes beyond that text.

## 5. Module targets

| Target | Status |
|---|---|
| 15-25 use cases | Met (22) |
| At least 50% graded A or B | **Not met** (3 of 22, 14%). This is real thinness, not a grading error. No error rate, override rate, parallel run or independent test of AI in TP was found. The only named, measured deployments are rules-based automation published by one vendor (Aibidia). |
| Every source dated | Met. Every source has a URL and an ISO date. Undated vendor pages use the retrieval date (2026-10-17), and this is stated in each locator. Two future event dates were replaced with retrieval dates. |
| Vocabulary values, unique ids, quotations under 25 words | Met (validator 0 errors; 22 unique ids; no quotation reaches 25 words). |

**Caveat for readers:** IRS-TPFAQ-2026 is dated 2026-06-28, which is the page's "last reviewed or updated" date. The FAQ
content predates that date. The files do not present the FAQ as new 2026 guidance, so I left the date as it is.

`#09` stays at grade A under the vocabulary: it is a measured outcome from a named organization. It rests on a customer
statement on the vendor's own site ("easily an 80% time saving"), and no step is shown to use AI. The module header and
the `#09` notes already say this. An advisor quoting it should say both.

## 6. Error patterns to fix in the briefs

1. **Speaker merging and drift in attribution.** Synthesis merged several webinar or conference speakers into one, or gave a
   speaker's claim as fact (`#01`, `#08`; module §3 "speakers"). Briefs should require the speaker's role for every
   quoted opinion.
2. **Adjacent-figure placement.** A figure lands in a table row or sentence whose label changes what it measures (100
   hours to 30 minutes under "comparability work"; the 8% policy-design expectation read as broad expectation). Briefs
   should require the `measures` wording to travel with the figure into module tables.
3. **Caveats moved between documents.** A caveat from one vendor document was attached to a figure from another (`#14`).
   Briefs should require each caveat to cite the same ref as its figure.
4. **Small embellishments.** "Named", "outsourced", "first", "especially in growing companies", "test substance over
   form". These are one-word additions that change the claim. Verifiers should diff qualifiers against the source text.
5. **Future and re-publication dates.** Event pages were dated to future event days, and Aibidia's CMS re-publication
   date (3 July 2026) was taken at face value on some news items. One date (BIP, 2026-02-26) had no visible basis. Briefs
   should say that a source date can never be later than the retrieval date, and that a byline beats JSON-LD.
6. **Unsourced connectives in risks.** "So poorly aligned agreements may be flagged" and "a screen that cannot show its
   rejection logic fails". Briefs should require such inferences to be labelled "inference" or removed.
7. **Ladder inflation from marketing language.** A managed service where "experts do the work" was classed `delegate` /
   `managed-agent-runtime` (`#22`). The ladder should reflect what the source says the AI does; when the source is silent,
   use the lowest defensible value and say so.
8. **Competitor pages as evidence about rivals.** Commenda's comparison page attributes features to Aibidia products that
   Aibidia describes differently. Treat a competitor's description of a rival as a claim about the competitor's
   marketing, not about the rival.
