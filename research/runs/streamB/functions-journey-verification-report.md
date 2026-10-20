# Verification report: function cards, journey stages, index §7-§8

Date: 2026-10-20. Verifier: fact-check pass for Stream B.

Files checked:

- the 10 function cards in `plugins/transformation-advisor/skills/transformation-advisor/references/library/functions/`
- `library/journey-stages.md`
- §7-§8 of `library/index.md`

## Summary

| Measure | Count |
|---|---|
| Cited claims checked (citation instances in card bodies) | about 560 |
| Archetype use-case ids checked against the YAML (id exists, grade matches) | 100 references to 78 ids; all exist, all grades match |
| Source entries checked (URL, date, type, title) | 219 (174 unique URLs, plus 3 keys the first pass missed) |
| Sources opened in full | all 177 URLs, directly or through the text mirror; 9 only partly (see below) |
| Claims kept as written | about 495 |
| Claims fixed (wording, figure, date, attribution, grade or source) | 61 logged fixes in the table below (some rows cover several edits in one file) |
| Claims removed outright | 2 (an unsupported "figures changed between versions" clause; an unsourced "30% of its time back" figure). Four more unsupported claims were replaced with what the source actually says; they are counted as fixes |
| Grade changes | 4 downgrades (ANZ A to B; UK GDS coding trial A to B; DBT Copilot A to B; Walmart order value A to B); 0 upgrades |
| Validator (`scripts/validate.py`) | 0 errors before and after; no ERROR in these files |
| Size and contents | every file is 300 lines or fewer (largest: journey-stages.md, 253) and has a table of contents; all in-file anchors resolve |
| Links to `../patterns/<id>.md` | all 11 pattern files now exist; every pattern link from the function cards resolves. None unresolved |
| Vendor recommendations | none found. Product names appear only as facts about named deployments |
| index.md §7-§8 | checked against onboarding.md §5, journey-stages.md and the card set; accurate, so no edit |

## Fixes and removals

| File | Claim (source key) | Change | Reason |
|---|---|---|---|
| finance-accounting | AIA forecast example (TREASURYTODAY-2024) | Added "a pilot in some markets" | Source says the pilot is deployed in some AIA markets; omitted qualifier overstated scope |
| finance-accounting | Vals benchmark score (VALS-2026) | "as accessed 2026-10-20" changed to "as of 2026-06-04"; source date changed to updated 2026-06-04 | Leaderboard states results as of 4 June 2026 |
| finance-accounting | Accountants' role shift (STANFORD-2025) | "shifted toward client communication" changed to "can redirect that time toward business communication ... client-facing advisory" | Embellished qualifier: source says time can be redirected, and says business communication |
| finance-accounting | "final judgment call" (STANFORD-2025) | Attributed to co-author Jung Ho Choi | Attribution drift: the quote is Choi's, about auditors, not the write-up's own statement |
| finance-accounting | KPMG talent mix (KPMG-2026) | "most are upskilling ... only 28% rethinking talent" changed to 38% upskilling, 28% hiring for different skill sets | KPMG's summary says "most" but its own chart gives 38%; used the measured figures |
| finance-accounting | DELOITTE-DART-2026 source type | "professional body commentary" changed to "firm commentary" | Deloitte is a firm, not a professional body |
| finance-accounting | KOGNITOS-2026 title | Corrected to "Why AI Hasn't Shortened Your Month-End Close" | Title mis-transcribed |
| finance-accounting | GARTNER-2025 source | Noted publisher route "via CPA Practice Advisor" | URL is a republication, not Gartner's site |
| customer-service | Alibaba trial (NI-2026) | "an Alibaba co-author" changed to "two Alibaba co-authors"; dropped "Independent" | Two of six authors are Alibaba Group staff |
| customer-service | GOV.UK Chat accuracy (GOVTRANS-2026), §3 and §4 | "expert-rated accuracy" changed to "accuracy in internal benchmarking ... against published guidance" | Embellished qualifier: the report says internal benchmarking, not expert rating |
| customer-service | Pre-sale chatbot (FANG-2026) | "against no support ... independent" changed to "than an automated 'support unavailable' message ... two authors consulted for the platform" | Control condition misdescribed; authors disclose consulting for the platform |
| customer-service | AI disclosure (EU-AIACT-ART50-2024), §6 | "EU deployers must tell people" changed to a provider design duty | Article 50(1) places the interaction-disclosure duty on providers, not deployers |
| customer-service | Workforce pain (NBER-BRYNJOLFSSON-2023) | Reworded as industry estimates of turnover cost per departing agent | The paper cites third-party estimates of attrition cost, not ramp cost |
| people-hr | Canada TBS screening (TBS-AIA-2024) | "pilot ... hiring managers review all candidates" changed to "proposed pilot ... TBS intends to review all candidates" | The impact assessment describes a proposed pilot and an intention |
| people-hr | IBM AskHR NPS (IBM-THINK-2025) | Clarified that IBM shut HR phone and email for all employees and HR partner support for 21,000 first-line managers | Misread: the 21,000 figure applies to partner support, not phone and email |
| people-hr | PSG voice interviews (CHICAGO-JABARIAN-2026) | PSG described as recruitment process outsourcing (Teleperformance subsidiary); "Independent" replaced by disclosure that the lead author later took an unpaid chief-economist role at PSG | Vendor/partner tie omitted; the paper discloses it |
| people-hr | Gartner HR survey (GARTNER-HR-2026), §4, §5, §7, §8 | Opened in full: removed "reportedly" and "search-only"; wording aligned to release; real title added | Source reachable via text mirror; wording matched to "some capacity" and "significant or transformational value" |
| people-hr | Probe 8 | Removed "30% of its time back" | Figure not in any cited source |
| people-hr | Resume-screening bias (UW-WILSON-2024) | "up to 85.1% of LLM" changed to "85.1% of language-model" | Source gives 85.1% of cases (no "up to"); the models are text-embedding models, not LLMs |
| people-hr, technology-it | ORACLE-AISD-2025 | URL changed to Oracle's blog post (the cited title); people-hr probe 3 reworded to what the blog shows (a ticket for a support engineer) | Cited title is a blog post, not the customer page; the customer page does not show the route to a person |
| procurement-supply-chain | Walmart negotiation bot (PYMNTS-2023) | "68% of negotiations closed" changed to "deals closed with 68% of suppliers approached" | Misread statistic: the figure counts suppliers, as §4 already said |
| procurement-supply-chain | Demand forecasting PoC (SUPCHAINS-2025), §2, §3, §8 | Opened in full (mirror); removed "search-only"; added baseline (retailer's current software), "machine learning, not generative AI", exact date 2025-06-16 | Source now read; baseline and technique were missing |
| procurement-supply-chain | Roles §7 (DELOITTE-2025) | "survey finds technology and talent competencies correlate with performance" changed to a Deloitte principal's statement | Misattribution: the release contains only a quote, no correlation finding |
| procurement-supply-chain | NPS-2026 source | Recast as a vendor-authored (Eudia) paper prepared for the NPS symposium | Vendor claim presented as academic: all authors are from the vendor |
| product-service-development | P&G top-decile results (NBER-DELLACQUA-2025), §4 | "9.2 points" changed to "9.2 percentage points" (twice) | Unit was ambiguous; the paper reports percentage points |
| product-service-development | EU marking rule (EU-AIACT-ART50-2024), §6 | "content shown to customers is subject to marking rules" made specific: provider marking duty plus deployer deepfake disclosure | Overbroad: Article 50 marks outputs at the provider level, not all content shown to customers |
| risk-compliance-legal | DWP referral delay (DWP-UCADV-2025) | "median delay 1 day" changed to "paid a median 1 day later than automatically approved ones" | Misread: the figure is a difference against auto-approved advances |
| risk-compliance-legal | AI governance pain (DOJ-ECP-2024), §2 | "Regulators ask how fast" changed to "US prosecutors ask how quickly" | DOJ guidance is for prosecutors; wording matched to the quote |
| risk-compliance-legal | Legal productivity (UMN-SCHWARCZ-2025), §4 | Removed "published figures changed between versions"; added "(speed, not quality)" | Version-change claim not supported by any opened source |
| risk-compliance-legal | Air Canada award, §6 | Added "in damages plus interest and fees" and the tribunal decision as a source (CRT-2024 added to §8) | The cited law-firm note does not give the amount; $650.88 is the damages component only |
| risk-compliance-legal | MCCARTHY-MOFFATT-2024, QANOONI-ITG-2026 source types | "professional body" changed to "law firm commentary"; "press" changed to "vendor-written associate content" | Source types misclassified (vendor content presented as press) |
| risk-compliance-legal | Read-this-first: regulators | Scoped to US and UK regulators and prosecutors, noted the EU AI Act exception, added sources | Unsourced connective claim that contradicted the card's own EU AI Act guardrails |
| sales-marketing-bd | Prospecting pain (MICROSOFT-2024), §2 | "Account research took about four hours" changed to "Lumen estimates its assistant saves sellers four hours a week" | Misread statistic: the source's four hours is a weekly saving estimate, not research time |
| sales-marketing-bd | Qualification pain (SAASTR-2025a), §2 | "great human salesperson outperforms agents on complex deals" replaced by SaaStr's actual practice (agents hand $50-100K+ deals to humans) | Claim not found in either SaaStr source |
| sales-marketing-bd | Sales-ops pain and probe 2 (SAASTR-2025a) | "Opportunities never logged in the CRM ... incomplete logging" replaced by "broken RevOps processes ... about 1,000 leads never followed up" | Embellished: the source says RevOps was broken and leads were ghosted, not that opportunities were unlogged |
| sales-marketing-bd, customer-service | Fang et al. retail experiments (FANG-2026) | "Independent" removed; disclosed two consultant authors and one platform employee; control condition described | Vendor/partner ties presented as independent; card's own §4 already noted the ties |
| sales-marketing-bd | Klarna spend cut (VERDICT-2024), §4 | "annualized" removed; 11% stated as Q1 2024 | Wrong period: the 11% is a Q1 2024 figure |
| sales-marketing-bd | EU disclosure (EU-AIACT-ART50-2024), §6 | "Digital Omnibus" corrected to "AI Omnibus", grace date added, AG-OMNIBUS-2026 added to §8 | Wrong instrument named; claim was unsourced |
| service-delivery | Pilot-to-production rate (MIT-NANDA-2025), §2 | "5% of custom enterprise tools" changed to "5% of evaluated enterprise-grade tools, custom or vendor-sold" | Misread: the denominator includes vendor-sold tools |
| service-delivery | Outsourcing savings (MIT-NANDA-2025), §3 | "its largest documented savings" changed to "some of the most dramatic savings" | Embellished qualifier |
| service-delivery | IAI-CONSULT-DWP-2025 date | 2025-08-27 changed to 2025-10 | The report carries no date; the PDF and its GOV.UK asset were created 2025-10-20; 2025-08-27 could not be traced |
| strategy-planning | Option-evaluation pain (CSASZAR-2024), §2 | "evaluators disagreed enough that an LLM's scores explained 29%" replaced by the paper's agreement measures (judge-judge ICC 0.25; judge-LLM ICC 0.51) | Misread statistic: 29% is variance in investor scores explained by LLM scores, not a measure of disagreement |
| strategy-planning | Outside-frontier result (HBS-DELLACQUA-2023), §6 | "19% lower odds" changed to "19% less likely to produce a correct solution" | Statistic reported as something it does not measure (likelihood, not odds) |
| strategy-planning | INDIAMART-2025 | Opened in full; "search-only" removed; type "press" changed to "firm blog" | Source reachable; it is a corporate blog |
| technology-it | Process framework (APQC-PCF-PAYOR-2019), §2 | Disclosed that the edition opened is the health-insurance payor PCF | Attribution drift: cited as "a cross-industry framework" but the source is an industry edition |
| technology-it | Build-and-change pain (AWS-QTRANSFORM-2024), §2 | "upgrades take months or years" replaced by Amazon's estimate of 4,500+ developer-years | Claim not in the source |
| technology-it | ANZ coding trial (ANZ-COPILOT-2024) | Grade A changed to B; noted times were self-reported by unmonitored participants | Grade inflated: self-reported times on algorithmic exercises are not a measured work outcome (A rule, 2026-10-17) |
| technology-it | UK public-sector coding trial (UK-GDS-AICA-2025) | Grade A (telemetry) changed to B | Only measured figure is an acceptance rate (usage), not a work outcome; time saving is a survey estimate |
| technology-it | Adidas (DORA-2025) | Added "in a generative AI pilot" | Omitted qualifier from the foreword |
| technology-it | DX share of code (DX-AIIMPACT-2026), §4 | "merged code" changed to "code" | "Merged" not in the report |
| journey-stages | Intro: no longitudinal study (SADIQ-2021) | Separated the author's own finding from the review's; added the review's measured point (7 of 15 models validated) | Unsourced connective claim attributed to the review |
| journey-stages | Curious "Emphasize" (MITCISR-2024) | "Make safe use possible rather than only prohibiting it" changed to "acceptable-use policies that make safe use possible" | Attribution drift: CISR lists acceptable-use policies; the anti-ban framing is not in the source |
| journey-stages | Pilot-to-production 5% (MIT-NANDA-2025), §3 | Denominator corrected to "evaluated enterprise-grade tools, custom or vendor-sold" | Misread statistic |
| journey-stages | Barrier ranking (MIT-NANDA-2025), §3 | "Change management, executive sponsorship, UX and output quality head the ranking" changed to "unwillingness to adopt new tools leads, then output quality" | Misread chart: the report names resistance to new tools first and model quality second |
| journey-stages | DBT example (DBT-COPILOT-2025), §3 | "with a control group" replaced by the actual design (diaries, observed tasks, interviews incl. six control-group staff); grade A changed to B | Embellished design; findings rest on self-reports, consistent with the DWP example graded B |
| journey-stages | CISR stage step (MITCISR-2025), §5 | Reworded as CISR's statement, with the point that growth turns positive at stage 3 | The card's "largest step" was not what CISR's own numbers show (stage 1 to 2 is a larger gap); now attributed to CISR's text |
| journey-stages | Walmart AOV (WALMART-Q4FY26-2026), §5 | Grade A changed to B | A user vs non-user gap is not a measured outcome of the AI (A rule) |
| journey-stages | Italgas revenue (MITCISR-2025), §6 | Clarified that EUR 3 million is Bludigit's company revenue, not revenue from the AI tool | Attribution drift |
| journey-stages | BCG 2026 tiers, §8 | Added BCG-AIX-2026-PUB as source | 4.5% and 47% shares appear only in the publication, not the cited press release |
| journey-stages | Maturity model table, §9 | "Early Scaling" under BCG marked as not a named tier; "five in 8 of 15 models" changed to "five is the most frequent count among 15 models" | BCG has no "Early Scaling" tier (contradicted the file's own note); 8-of-15 count not found in the review |
| procurement-supply-chain | Walmart bot scope (PYMNTS-2023; HBR-2022) | "price, payment terms and other items" changed to "cost and purchase terms" | Wording not in either opened source (HBR is paywalled beyond the opening) |

## Sources that could not be fully reached or verified

| Source key | Problem | What was done |
|---|---|---|
| HBR-2022 | Paywalled beyond the opening paragraphs | Kept only the claims the opening supports (100,000+ suppliers, about 20% on non-negotiated terms); bot-scope wording now follows PYMNTS-2023 |
| WHARTON-2025 | Report page returns only a summary; wave labels not shown | The 2026 report confirms waves 3-4 and groups waves 1-2 as "Exploration"; the §9 labels "Exploration (2023)" and "Experimentation (2024)" are kept but only partly verified |
| JOA-2026 | Page text extracted thinly | The COSO points it backs are confirmed by DELOITTE-DART-2026 |
| GARTNER-2026 (procurement) | Cited URL is on a gcom.pdo.aws.gartner.com mirror; the canonical gartner.com page could not be confirmed | Content read in full on the cited URL; URL left as is. The coordinator may want the canonical link |
| IAI-CONSULT-DWP-2025 | The report carries no date; the cited 2025-08-27 could not be traced | Date changed to 2025-10, the PDF and GOV.UK asset creation date |
| DX-AIIMPACT-2026 | The report body is mostly images | Headline figures confirmed; the word "merged" (not found) was removed |
| KPMG-2026 | The report contradicts itself ("most organizations are upskilling" against a 38% chart) | The card now uses the chart figures |
| CRT-2024, GALLUP-2025, BOSCH-PT-2024, SAASTR-2025a/b, GARTNER-HR-2026, SUPCHAINS-2025, several BCG and Gartner pages | Blocked or thin on direct fetch | Read in full through the r.jina.ai text mirror |
| ORACLE-AISD-2025 | The customer page is short and does not show the cited title or the route to a person | The cited title belongs to Oracle's blog post, which was found and read; the URL now points to it in both cards |

## Error patterns seen

1. **Misread statistics (most common, 10 cases).** A figure is reported as something it does not measure. Examples: the 29% of variance in investor scores explained by an LLM was presented as evidence that evaluators disagree; "19% less likely" became "19% lower odds"; Lumen's four-hours-a-week saving became "account research took four hours"; NANDA's 5% denominator lost its "or vendor-sold" tools; the NANDA barrier chart was read in reverse order; a 1-day *difference* in DWP payment delay became a 1-day delay.
2. **Independence overstated (vendor or partner ties dropped, 5 cases).** Fang et al. (consultant authors and a platform employee), Jabarian (lead author later chief economist at the partner), Alibaba (two company co-authors), the NPS acquisition paper (written entirely by the vendor), Qanooni (vendor-written associate content listed as press).
3. **Embellished qualifiers (8 cases).** "Expert-rated" for internal benchmarking; "with a control group" for six control-group interviewees; "largest" for "some of the most dramatic"; "shifted toward" for "can redirect"; "up to 85.1%" for "85.1%"; "annualized" for a Q1 figure; "merged code"; and "LLM" for embedding models.
4. **Attribution drift (8 cases).** Stanford's "final judgment call" quote belongs to co-author Choi; Article 50's disclosure duty is a provider duty, not a deployer one; "Digital Omnibus" for the AI Omnibus; Bludigit company revenue presented as revenue from one AI tool; BCG tier shares cited to a press release that lacks two of them; a payor-edition APQC framework called cross-industry; a Deloitte principal's quote presented as a survey correlation; Oracle's blog title attached to the customer page.
5. **Unsourced connective claims (6 cases).** "A great human salesperson outperforms agents" and "opportunities never logged" (not in SaaStr); "upgrades take months or years" (not in AWS); "regulators are asking for evidence rather than new rules" (contradicted by the card's own EU AI Act guardrails); "no study follows the same organizations" attributed to a literature review; "figures changed between versions".
6. **Grades inflated by non-outcome measures (4 cases).** These were downgraded under the 2026-10-17 A rule. Self-reported times on algorithmic exercises (ANZ), a code-acceptance rate (UK GDS), a diary-based evaluation (DBT) and a user against non-user order-value gap (Walmart) are not measured work outcomes.
7. **Wrong or unverifiable dates (3 cases).** Vals "accessed" date replaced with the leaderboard's own date; IAI-DWP date; SUPCHAINS exact date added.
8. **Forecasts presented as facts.** None found uncorrected: Gartner's cancellation prediction, the NPS lead-time projections and DSIT's 75,000-day figure are already labelled as predictions, projections or estimates.
9. **Search-only sources inside graded entries.** Three sources were marked search-only: GARTNER-HR-2026, SUPCHAINS-2025 and INDIAMART-2025. All three are now opened in full and relabelled. None supported an A or B grade.

## Items left as they are, for the coordinator's judgment

- **Chipotle (people-hr, grade B).** Its figures (12 to 4 days; completion 50% to 85%) are company-reported tracked metrics, relayed by press and a vendor. Under the A rule this could be A; it was left at B as the conservative choice.
- **The Microsoft, Salesforce, Klarna, IBM, HSBC and Oracle A grades** are self-reported figures from organizations that also sell the underlying product. Each card already states this. They were kept, because the A rule turns on measurement, not independence.
- **The Wharton 2026 "acts with monitoring (31%)" wording** maps the report's "fullest capacity" category, the 7% that rely on real-time monitoring and guardrails. It is a fair reading but not verbatim.
