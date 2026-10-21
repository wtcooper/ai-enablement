# Advisory archetype verification A: report

Checked 2026-10-21. Files: `advisory/economics.md`, `state-of-ai.md`, `frontier.md`, `disruption.md`, `workforce.md`
(under `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/`). All 124 cited source URLs
were fetched (direct `curl`, `pdftotext`, or `r.jina.ai` for blocked sites) and each figure, date, attribution,
regulatory point and forecast was compared with the source text. Module references (`CAS #01` and similar) were
spot-checked against the use-case YAML, not re-verified.

## Counts

| | Count |
|---|---|
| Claims checked (figures, dates, attributions, rules, forecasts) | about 255 |
| Kept | about 217 |
| Fixed | 37 |
| Removed | 1 |

By file: economics 10 changes, state-of-ai 8, frontier 10, disruption 7, workforce 3.

## Fixes and removals

| File | Claim as written | Action | Reason |
|---|---|---|---|
| economics §3 | "Billable hours per CAS person: about 1,700 to 500-600 at BST & Co." | Fixed | JofA says these are the CAS leader's own hours (Berdar), not per person. Misread statistic |
| economics §1, §4 | Broker estimate of QoE "$25,000-$200,000" | Fixed | CT Acquisitions gives tiers: $25K-$120K regional, $50K-$250K mid-market, $100K-$500K+ Big Four. Range was truncated, and the source is an M&A adviser's page |
| economics §3 | CAS margins "over 40%" as Woodard data | Fixed | The 40% is from the Accounting Today Top 100 report as discussed on the podcast. Woodard's own data is the 60-70% |
| economics §3 | SOX "control cost up 45%" | Fixed | Added the period (KPMG 2023 vs 2025 surveys) |
| economics §4 | Contingent fees "barred for SEC issuer audit clients and restricted under the AICPA Code" | Fixed | Rule 2-01(c)(5) covers SEC audit clients. AICPA ET 1.510 prohibits contingent fees (not merely restricts them) for audit, review, compilation-without-independence-disclosure and PFI-examination clients. Rule was stated too narrowly |
| economics §5 | "BDO USA: $1B+ over five years" | Fixed | The release says the strategy is "backed by a global investment" (BDO global). Attribution drift |
| economics §5 | "Integration, not model quality, is the blocker the survey names" | Removed | Not in the Intuit survey, an unsourced connective claim. Replaced with the survey's own 48% "functional but fragmented" |
| economics §5 | "Verification averages 26% of work time" | Fixed | Datarails surveyed corporate finance teams (270 CFOs and finance leaders), not firms. Population was misapplied |
| economics §7 | CPA Trendlines "calling its count 'a floor, not a ceiling'" | Fixed | The phrase refers to recent monthly counts. Also added the tracker's definition (525 events since 2016, transacted EV) |
| state-of-ai §1 | AI use at "88-98% of firms" | Fixed | Intuit's 88% is respondents (professionals), not firms |
| state-of-ai §1, §3 | RSM "36% fully embedded" | Fixed | Not in the cited release or the CPA Practice Advisor copy. Found on RSM's survey page; added an inline link and date |
| state-of-ai §2 | Gartner "poll of 743" | Fixed | It was a webinar poll, which matters for the sample |
| state-of-ai §2 | ACFE "AI or ML in analysis" | Fixed | Source: "in their anti-fraud programs" |
| state-of-ai §2 | OneStream "genAI in forecasting 21%" | Fixed | 21% is genAI use by FP&A teams. Only ML (12%) is forecasting-specific. Misread statistic |
| state-of-ai §3 | KPMG "revenue $250M+" | Fixed | Added $500M+ for US respondents and the March 2026 fieldwork date |
| state-of-ai §4 | GT "Copilot to 13,500+ people" | Fixed | Source: "in the process of equipping", so it is a rollout |
| frontier §2 | AO-41: "appraiser judges whether AI output is accurate and appropriate" | Fixed | BVWire: no new requirements; responsibility for the analysis and conclusions stays with the appraiser |
| frontier §2 | IRS OPR guidance "binds advisory work" | Fixed | The OPR issue is introductory guidance applying Circular 230. Changed to "applies Circular 230 duties" (overstated) |
| frontier §2 | "AICPA ethics staff write" | Fixed | The author is the Ethics Division's communications manager. Now "an AICPA Professional Ethics Division article" |
| frontier §4 | Firms "developing" value and outcome pricing | Fixed | Bloomberg Law reports leaders "brainstorming" and "exploring". Embellished qualifier |
| frontier §4 | IFAC 1,052 transactions | Fixed | Added the source's definition (177 direct investments plus 875 roll-ups) |
| frontier §4 | Crowe: split "becoming the standard structure for outside capital" | Fixed | Unsourced generalisation. Now states what Crowe's release shows |
| frontier §5; disruption §7 | "7% of anti-fraud professionals feel more than moderately prepared" | Fixed (2) | The source asks about their organisations' preparedness |
| frontier §5 | TR: clients see AI-enabled quality "as essential" | Fixed | Source: "very important or essential" |
| frontier §6 | ACFE Canada "AI and analytics session on 16 Nov" | Fixed | The 16 Nov agenda has no AI session. The AI session is the 15 Nov pre-conference |
| frontier §6 | EU AI Act 2 Dec 2027 [CUATRECASAS-AIOMNIBUS-2026] | Fixed | The key has no URL. Added the European Commission AI Act page (confirms Annex III from 2 Dec 2027; Omnibus in force 27 Jul 2026) |
| disruption §2 | Contingent fees "barred or restricted for audit clients" | Fixed | Same independence precision as economics §4 |
| disruption §4 | IFAC and CPA Trendlines totals | Fixed | Added deal-count definitions |
| disruption §4 | Multiplier "doubled" margins | Fixed | Source: "more than double" |
| disruption §4 | "services the attest arm can no longer buy from the advisory arm" | Fixed | Logic error. It is attest clients who cannot buy restricted services |
| disruption §6 | Withum "uses AI for variance finding and real-time dashboards" | Fixed | Bourke recommends this ("think how quickly Claude could find a variance"); no firm practice is stated. Embellished |
| disruption §6 | Bourke predicts "near-complete" tax automation | Fixed | He said "complete automation of the tax process". Now quoted, labelled as his forecast |
| workforce §2 | "KPMG recalls one company moving ... 40 producers to five reviewers" | Fixed | It is a quote from an unnamed media-company CFO in a KPMG article. Attribution drift |
| workforce §3 | UK Big Four graduate cuts "from 2023 to 2025" | Fixed | Figures compare 2023 with 2024 (article of June 2025). Wrong date. Indeed's 44% is 2025 against 2023 |
| workforce §7 | "An AI company pays TAS managers $100 an hour to evaluate AI-made QoE pages" | Fixed | Ethos is an expert network recruiting for an AI lab, to create and evaluate AI-made QoE exhibits and deal slides |

Checked and kept, though they first looked doubtful:
- The GT CEO's statement that governance demand will grow "as regulators give guidance" (the source quotes it).
- The Penrose figure that balances were more than 15% off (in the body text).
- The Thomson Reuters release and report difference.
- The Rule 707 withdrawal vote recorded in the October agenda book.
- The IIA Topical Requirement dates.
- The SBA SOP 50 10 8.1 effective date.

## Sources that couldn't be reached directly

Every source was read in the end; none was removed for access.
- **Blocked to `curl`, read through `r.jina.ai`:** GARTNER-AIREPORTCARD-2026, GARTNER-FPALEADER-2026, ISG-FAOFPA-2026, JSHELD-AIFRAUD-2026, PWC-TOLTIQ-2026 (second attempt), PKF-ASSETA-2026, CROWE-KKR-2026 (second attempt), the six BVR pages, ACCA-ETHICS-2026 (redirect loop), ARMANINO-FOTRENDS-2026, PENROSE-ACCTBENCH-2025, SEC-RULE2-01-2026 (eCFR), CPACOM-CASBENCH-2026, CITI-AIFO-2026, SBA-SOP5010-2026.
- **No URL:** CUATRECASAS-AIOMNIBUS-2026. Its frontier claim now also cites the European Commission page inline.
- **Date not on the document:** COSO-GENAI-2026 (the PDF is undated). The key's date of 2026-02-23 was kept.

## For the owner of `sources.md` (not edited here)

- Give CUATRECASAS-AIOMNIBUS-2026 a URL, or replace it with a key for the European Commission AI Act page (https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).
- Add a key for RSM's survey page (https://rsmus.com/insights/services/digital-transformation/rsm-middle-market-ai-survey.html), which carries the 36% figure. The two inline links can then become keys.

## Error patterns seen

| Pattern | Instances | Examples |
|---|---|---|
| Misread statistics | 4 | BST hours per person; OneStream genAI "in forecasting"; QoE price range cut off; 88% "of firms" |
| Attribution drift | 5 | BDO global versus BDO USA; KPMG versus a quoted CFO; Woodard versus Top 100 report; AICPA ethics "staff"; Ethos as "an AI company" |
| Embellished qualifiers | 6 | Withum "uses" AI; "near-complete" automation; firms "developing" pricing; "essential"; OPR "binds"; ACFE individuals versus organisations |
| Unsourced connective claims | 3 | "Integration, not model quality"; Crowe split as "the standard structure"; the attest-arm logic slip |
| Wrong dates or periods | 3 | UK graduate cuts 2023-2025; KPMG 45% with no period; ACFE Canada session day |
| Survey population misapplied | 2 | Datarails corporate finance teams read as firms; Intuit respondents as firms |
| Independence rule stated too narrowly | 2 | AICPA contingent-fee rule called "restricted" for audit and review clients only |
| Deal counts without definitions | 3 | IFAC and CPA Trendlines totals |
| Forecasts presented as facts | 0 new | Forecasts were already labelled; Bourke's prediction is now quoted |

Structure: all 125 source keys used resolve in `sources.md` with a date. One has no URL, which is fixed inline as above.
All five files have tables of contents and are under 300 lines (102-182). `scripts/validate.py` reports 0 errors.

Note: the orchestrator's checkpoint commits 61ff6bb and 0285b0e include these edits. Commit 61ff6bb is titled "verification B"; this agent made no commits.
