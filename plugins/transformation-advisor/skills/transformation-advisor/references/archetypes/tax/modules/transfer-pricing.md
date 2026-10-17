# Transfer pricing (tax)

Last reviewed 2026-10-17. Use cases live in `../use-cases/transfer-pricing.yaml` (22 entries). Ids are shortened
here: `#06` means `tax-transfer-pricing-06`. Source keys in brackets, such as [IRS-LBI-TP-2026], are in the YAML or
in §10. **Evidence is thin.** Only 3 of 22 entries are graded A or B, and all three are rules-based automation or
sourcing changes. Almost every figure is vendor-published (mostly by Aibidia, a TP software vendor) or a conference speaker's own
claim. No error rate, override rate, parallel run or independent test of AI in TP exists. Say so when you quote a figure.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Transfer pricing (TP) is the pricing of transactions between companies in the same group, which must follow the
arm's-length principle (the price unrelated parties would agree). The module runs from TP policy and intercompany
agreements through benchmarking (finding comparable independent companies or deals), local files, master files and
country-by-country (CbC) reports, intragroup services and operational TP (setting and monitoring prices during the
year), to audit defence, advance pricing agreements (APAs) and mutual agreement procedures (MAPs). It covers in-house
TP teams and advisory firms. Tax authorities' AI for picking TP audits is in `tax-controversy-13` (IRS) and
`tax-controversy-15` (Hungary, HMRC and others).

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Policy design and planning | Characterise transactions, choose method, allocate risk | expert-judgment | Results, rates and new business models interact across many jurisdictions |
| Intercompany agreements | Draft and update agreements that match policy and conduct | document-production, review-assurance | Drafting "often stalls for weeks" [PLANTEMORAN-2026]; IRS flags risk analysis inconsistent with agreements [IRS-TPFAQ-2026] |
| Data collection | Pull entity financials and transactions from ERPs and local finance | data-reporting | 79% spend >10% of TP time on data; nearly half run 4+ ERP or reporting systems (vendor survey) [AIBIDIA-LEADERS-2026] |
| Functional and industry analysis | Interviews and documents on functions, assets, risks; DEMPE for intangibles (who develops, enhances, maintains, protects, exploits) | research-synthesis, expert-judgment | Most probed by authorities; generic profiles that mirror contracts [BDO-AIGOV-2026] |
| Benchmarking | Search databases, screen, adjust, set the arm's-length range | research-synthesis, data-reporting | Hours or days per study [AIBIDIA-WEBINAR-2026]; the IRS wants a complete comparability analysis, with risk and function differences and adjustments explained [IRS-TPFAQ-2026] |
| Local file, master file, CbC report | Annual documentation per entity and for the group | document-production, data-reporting | Up to six weeks per local file and 3-4 review rounds (Trivium) [AIBIDIA-TRIVIUM-2026]; 30 days to hand over on IRS request [TR-CHECKPOINT-2025] |
| Requirements and consistency review | Check country rules; reconcile figures across TP files, CbC reports, VAT and tax returns | review-assurance | Rules change often; mismatches invite automated flags [BTAX-AFRICA-2026] |
| Intragroup services | Benefit test, allocation keys, cost-plus | expert-judgment | OECD rewriting the guidance; benefit-test disputes [HLB-CH7-2026] |
| Operational TP | Monthly calculation, monitoring, true-ups, invoicing, posting | transaction-processing, data-reporting | 60% rely on Excel and email; 7% monitor monthly; half report significant year-end adjustments [AIBIDIA-LEADERS-2026] |
| Audit defence and controversy | Answer information requests, expert reports, appeals | expert-judgment, document-production | Half spend 50-200 hours on audit response (vendor survey) [AIBIDIA-SOTP-2025] |
| APAs and MAPs | Negotiate certainty with one or more authorities | expert-judgment | Long negotiations; no AI evidence found |
| Research and regulatory tracking | Follow legislation, guidance, deadlines | research-synthesis | Dozens of jurisdictions; local subsidiaries touch TP "perhaps once a year" [AIBIDIA-WEBINAR-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome), reinvent (the service or operating model changes). Improve is crowded but grade C; automate
has the only measured cases, and they are rules-based automation, not generative AI; delegate is announced or
conference-reported only. No automate entry is at the step level.

**Research, data and self-service**
- Improve: `#01` grounded research assistant (TP Aurora, Aibidia with IBFD data; vendor claims 90% less research
  time). `#02` staff use Copilot, ChatGPT and Claude for drafting, research and stress-testing (93% use AI in some
  form, vendor survey). `#03` internal chatbot answers local finance and escalates to the TP team (Deloitte Poland
  offering). `#04` AI aggregation of data from several ERPs (one firm article; "standardise data first").

**Analysis and benchmarking**
- Improve: `#05` AI-drafted functional and industry analysis, e.g. explaining glove-maker margin surges (PwC
  Singapore example); BDO: AI cannot tell whether contracts reflect practice. `#06` comparables search and screen
  (RoyaltyRange, Exactera products; a PwC Singapore partner: AI "may" do ~80% of comparability work).

**Documentation and agreements**
- Improve: `#07` first-draft local and master file narratives with expert sign-off (job postings now ask for it;
  BDO lists recurring quality gaps). `#08` review against country rules and cross-filing consistency (Exactera,
  early adopter). `#10` first-draft agreements from the written policy, "weeks to hours" (firm statement).
- Automate: `#09` central data generates bulk local files; Trivium reports 80% time saving, Fortum 65% transaction
  automation (grade A, vendor-published; AI role not shown).
- Delegate: `#11` multi-agent review of an agreement's legal, TP, VAT and withholding-tax effects before drafting
  (unnamed TPMinds example; human checkpoints not described).

**Operational TP and monitoring**
- Automate: `#12` Kemira's automated price calculation, invoicing and SAP posting across 62 entities ("hundreds
  of hours"; rules and robotics).
- Improve: `#13` in-year margin monitoring against policy with flags; `#15` self-screening against the indicators
  authorities use (Hungary, Philippines).
- Reinvent (announced): `#14` connected "system of intelligence" over policies, agreements and evidence (Aibidia TP
  Intelligence, release planned December 2026; EUR 4.8 million risk found in a demo, not a client result).

**Controversy, APAs and governance**
- Improve: `#16` drafting and stress-testing audit responses from prior files. Ideas (D): `#17` AI in expert
  economic reports with full disclosure; `#18` APA and MAP outcome prediction; `#20` AI-use and verification log.
- Context: authorities using AI to select TP audits (Hungary's 2026 plan, IRS models): `tax-controversy-13`, `-15`.
  EY's TP Doc Insights checks documentation against public data: `tax-controversy-05`.

**Operating and service model**
- Reinvent: `#21` insourcing recurring documentation with advisors limited to review (Trivium, Fortum; grade B).
  `#22` platform-plus-experts packages at fixed prices (Commenda; Aibidia with BIP Law & Tax). `#19` policy
  modelling for planning is improve-level and early.

## 4. Interview probes

Ask in the person's setting (in-house TP team, advisory practice or controversy group).

1. **"Take your last local-file cycle: how many entities, how many review rounds, how long from data request to
   sign-off, and where did the time go?"** Reveals the baseline (Trivium: up to six weeks, 3-4 rounds) and whether
   the pain is data (`#04`, `#09`), drafting (`#07`) or review (`#08`).
2. **"How many ERPs and ledgers feed your TP work, who owns the mapping, and how clean is the data at year end?"**
   Reveals readiness. Only 22% call their data clean enough for AI; the named results rest on central data.
3. **"Which TP steps do people already do with a general assistant, what do they paste in, and is company data
   allowed?"** Reveals shadow use (`#02`) and confidentiality exposure [IRS-OPR-2026].
4. **"When AI suggests comparables, can you reproduce the rejection reason for every excluded company, and who
   signs the range?"** Reveals whether `#06` output would meet IRS comparability expectations [IRS-TPFAQ-2026].
5. **"How do you know before year end that margins are inside policy? How big were last year's true-ups?"**
   Reveals the monitoring gap (`#13`, `#12`); only 7% monitor monthly in the vendor survey.
6. **"Has an AI-drafted narrative, clause or flag ever been wrong or challenged? How was it caught?"** Reveals
   whether any quality evidence exists. None is public; BDO's gap list is the checklist [BDO-AIGOV-2026].
7. **"If an authority or court asked how an AI-assisted analysis was produced, what could you show: inputs,
   formulas, tool, reviewer?"** Reveals readiness for IRS expectations [IRS-LBI-TP-2026] and whether `#20` exists.
8. **"Do your functional analysis, agreements, local files, CbC report and returns tell the same story?"** Reveals
   exposure to authority analytics (`tax-controversy-15`) and the case for `#08` and `#15`.
9. **"Which work do you pay advisors for, and what would you bring in-house if the data were structured?"** Reveals
   sourcing options (`#21`, `#22`); 53% already run hybrid models (vendor survey).
10. **"Who in the team writes down how TP decisions are made, so a model can be given that context?"** Reveals
    tacit-knowledge risk; KPMG Germany says even the best prompt is not enough without written-down context [KPMG-KITP-2026].

## 5. Metrics and benchmarks

All survey figures are vendor-published by Aibidia (sample stated as 97 in-house professionals on one page and 138
on another; method not given) [AIBIDIA-LEADERS-2026] [AIBIDIA-SOTP-2026].

| Measure | Figure | Provenance |
|---|---|---|
| AI use among TP professionals | 93% some use; no use fell 36% to 7%; regular use 37% (from 18%) | vendor survey |
| AI expectations | 75% expect AI to handle a first documentation draft in 2-3 years; 8% expect AI to touch strategic policy design [AIBIDIA-SOTP-2026] | vendor survey |
| TP data clean enough for AI without manual work | 22% | vendor survey |
| Time on data | 79% spend >10% of TP time; 21% at least half; 14% draw from a single ERP | vendor survey |
| Team size vs reach | 63% have three or fewer TP staff; 58% operate in more than 30 jurisdictions | vendor survey |
| Operational TP discipline | 38% well defined; 60% Excel/email; 7% monthly monitoring; half significant year-end adjustments | vendor survey |
| Sourcing | 53% hybrid in-house plus advisors, up from 38% in 2024 | vendor survey |
| Audit response burden (2025) | Half spend 50-200 hours; half report USD 50,000-500,000 cost [AIBIDIA-SOTP-2025] | vendor survey |
| Local-file time (Trivium) | 80% saving; 2-5 working days (up to six weeks when waiting on data and advisors) to a few hours for a simple local file; earlier spend over EUR 10,000-15,000 per entity [AIBIDIA-TRIVIUM-2026] | vendor-published customer statement |
| Transaction automation (Fortum) | 65% in one year; 8,000+ transactions in the model vs 200 [AIBIDIA-FORTUM-2026] | vendor-published customer statement |
| Comparability work (PwC Singapore) | Partner: AI "may" do ~80% of comparability-analysis work. Senior manager, on "analysis" from modelling to value-chain work (not comparables specifically): up to 100 hours to ~30 minutes "under certain conditions" [DDTC-WUTA-2026] | self-reported opinions, conference |
| Packaged service price | ~USD 9,000 and ~4 weeks for a first set vs a claimed USD 60K and six months [COMMENDA-TP-2026] | vendor claim |
| Penalty exposure | "Up to 40% of the adjustment" without contemporaneous documentation, in an Exactera speaker's words as reported; the rate base was not checked against the statute [TR-CHECKPOINT-2025] | self-reported |
| IRS AI oversight (adjacent) | IRS lacks processes to show its selection models beat prior methods [TIGTA-2025]; 126 active IRS AI use cases as of June 2025 [GAO-2026] | independent, not TP-specific |

What to measure in a pilot: hours per local file and per benchmarking study; review rounds; share of entities
documented; reviewer override rate on AI drafts and comparables; year-end adjustment size; time to answer an
information request. None of these has a published AI benchmark. The nearest independent accuracy test is
adjacent: models computed fewer than a third of simplified US returns correctly [COLUMN-TAXCALCBENCH-2025].

## 6. Guardrails

- **No TP-specific AI rules exist.** Existing duties bind. IRS LB&I's TP operations director (29 Jul 2026): AI can
  "support" but not replace legal, economic and factual judgment; experts must explain inputs, assumptions, methods
  and AI tools, and the IRS wants to see the formulas [IRS-LBI-TP-2026]. A PwC TP principal says examiners expect
  to see the underlying work [TR-CHECKPOINT-2026].
- **US documentation standard.** Section 6662(e) documentation avoids the penalty only if adequate and reasonable;
  the IRS wants reasons for the method chosen, sources reviewed and methods rejected, and calculations in working
  formats [IRS-TPFAQ-2026]. No source tests how AI-drafted documentation fares under these rules.
- **Practitioner conduct.** IRS OPR Alert 2026-19 maps AI onto Circular 230 (due diligence, competence, firm
  procedures, written advice), says client data should not go to unsecured tools, and says AI savings should be
  credited to clients; the AICPA has asked for clarification [IRS-OPR-2026] [AICPA-CART-2026]. UK PCRT bodies issued AI
  guidance [ATT-PCRTAI-2026].
- **Courts and evidence.** Clinco: the Tax Court found likely hallucinated citations and issued a warning
  [TAXCT-CLINCO-2026]. An IRS valuation expert report in Riddle Aggregates was challenged over hallucinated
  citations and recorded as withdrawn [RIDDLE-TRANSCRIPT-2026]. On proposed Federal Rule of Evidence 707 (machine
  output), a federal rules committee decided in June 2026 not to recommend action yet [PROSKAUER-707-2026].
- **OECD.** The Chapter VII (intragroup services) draft of June 2026 has 21 new examples and is "not intended to
  change the general principles" [PWCDE-CH7-2026] [HLB-CH7-2026]. Bloomberg reports some examples involve AI tools
  shared between affiliates, and that AstraZeneca and others asked how AI transactions are characterised
  [OECD-INTRAGROUP-2026].
  There is no law or international standard on pricing shared AI agents [BGOV-AGENTS-2026]. This is TP of AI, not
  AI in TP; see research-advisory.
- **Cross-tax.** The CJEU's Arcomet ruling on VAT consequences of TP adjustments matters for year-end true-ups
  [BTAX-VAT2026]; multi-agent cross-tax review (`#11`) should cover it.
- **Data and security.** Use a closed environment for company data [DDTC-WUTA-2026]; evaluate vendor security
  [PLANTEMORAN-2026]. EU AI Act treatment of AI in TP is unsettled [INTERTAX-SIVA-2026].
- **Steps that need human judgment:** method selection; functional characterisation and DEMPE, tested against how
  the business actually runs; accepting comparables and the range; sign-off of every file; agreement terms;
  testimony; APA and MAP negotiation. LLMs are weak with numbers, so calculations need a deterministic layer
  [AIBIDIA-WEBINAR-2026].

## 7. Roles and how they evolve

- **Preparers become supervisors.** A P&G head of tax likens AI to a junior associate needing supervision and
  clean-up; PwC Singapore speakers keep "the crucial 20%" for people [DDTC-WUTA-2026]. Speakers say judgment and
  accountability matter more, not less [AIBIDIA-WEBINAR-2026].
- **Hiring signals.** Twilio's TP manager posting asks the hire to lead integrating AI into the TP workflow; Adobe
  (Frame.io) lists applying AI to research, benchmarking, drafting and review; dsm-firmenich asks for strong
  interest in AI [JOB-TWILIO-2026] [JOB-ADOBE-2026] [JOB-DSM-2026].
- **New titles and teams.** Global Head of TP and Tax Automation at Deutsche Bank [TPMINDS-INTL-2026]; KPMG's
  Global TP Technology Leader [TPMINDS-WC-2026]; KPMG Germany's TP innovation and technology centre
  [KPMG-KITP-2026]; a BIP and Aibidia task force of TP specialists, data engineers and technologists [AIBIDIA-BIP-2026].
- **Sourcing shifts.** In-house teams question paying advisors mainly for validation and risk absorption; hybrid
  models rose to 53%; the source does not attribute this to AI [AIBIDIA-LEADERS-2026]. Trivium and Fortum moved
  advisors to review (`#21`).
- **Ownership.** Andersen asks who owns AI-assisted documentation when the preparer is not a TP specialist
  [ANDERSEN-AI-2026]. Werfel's register warns of skill erosion and institutional knowledge loss [AICPA-WERFEL-2026].
- **Headcount.** A scheduled TPMinds West Coast panel on human TP skills explicitly covers "rationalizing headcount"
  (programme text, outcome not reported) [TPMINDS-WC-2026].

## 8. Frontier

- 2025-05-22: TP Aurora launched [AIBIDIA-IBFD-2025]. 2025-07-09: RoyaltyRange CompID AI launched [ROYALTYRANGE-2025].
- 2026-02-03: a CIAT blog author argues authorities are moving from predictive risk models to agentic AI for
  end-to-end TP control, under human supervision (opinion) [CIAT-BLOG-2026].
- 2026-03-12: Hungary's 2026 inspection plan uses AI-based models to pick TP audit targets [WTS-HU-2026].
- 2026-05-08: ABA Tax Section May Meeting panel on AI and section 482, with an IRS panelist [ABA-MAYMTG-2026].
- 2026-06-01 to 2026-07-22: OECD Chapter VII consultation; submissions published 2026-08-24 [PWCDE-CH7-2026] [HLB-CH7-2026];
  companies ask how AI transactions are characterised [OECD-INTRAGROUP-2026].
- 2026-06-16/17: TPMinds International; the sponsor's recap (2026-06-25) says AI moved from theory to practice and
  cites an unnamed multi-agent example [AIBIDIA-TPMINDS-2026]. 2026-06-26: Oxford CBT asks how delegating decisions to AI affects TP law [OXFORD-CBT-2026].
- 2026-07-29: IRS LB&I sets expert-witness expectations on AI [IRS-LBI-TP-2026].
- 2026-09-23: majorities of vendor-survey respondents expect AI agents to gather and format data, monitor compliance
  and do first-pass audit reviews within two to three years [AIBIDIA-LEADERS-2026].
- 2026-10-15: Aibidia announces TP Intelligence; first release planned December 2026 [AIBIDIA-TPINTEL-2026].
- 2026-11-04/05 (scheduled): TPMinds West Coast case studies with TP heads from Anthropic, OpenAI and Uber
  [TPMINDS-WC-2026]. 2027-03-01 (planned): TPMinds Americas AI Transformation Day and "The AI Arms Race in TP"
  [TPMINDS-AM-2027].

## 9. Common objections

- **"AI hallucinates; TP can't tolerate that."** Fair: participants report hallucination and overconfidence
  [AIBIDIA-LEADERS-2026], and Clinco and Riddle Aggregates show the cost. Response: use grounded tools with
  citations (`#01`), keep a verification log (`#20`), and have a named professional sign every output.
- **"Our data isn't ready."** Usually true (22% say it is). Response: the named results (Trivium, Fortum, Kemira)
  all rest on centralised data and harmonised systems (`#09`, `#12`); AI drafting would sit on that layer.
- **"The authority won't accept AI work."** The IRS says AI can support judgment if you can show inputs and
  formulas [IRS-LBI-TP-2026]. Plante Moran: an AI comparables list is a first pass, unlikely to meet standards on
  its own [PLANTEMORAN-2026]. Use AI for the first pass and keep the documented screen.
- **"LLMs can't do the maths."** Agreed by practitioners [AIBIDIA-WEBINAR-2026]. Response: keep calculations in
  rules-based tools (`#12`) and use language models for narrative, search and review.
- **"Polished drafts hide weak analysis."** BDO sees exactly this [BDO-AIGOV-2026]. Response: check functional facts
  against how decisions are actually made, and sign off method and benchmarks separately (`#07`).
- **"It's vendor hype."** Mostly vendor-sourced, yes; no independent test exists. Response: ask for a parallel run
  on last year's files and track override rates before scaling.
- **"Confidential data can't go into AI."** Response: closed or enterprise-approved tools only [IRS-OPR-2026]
  [DDTC-WUTA-2026]; Deloitte's chatbot keeps data inside the organisation [DELOITTE-PL-2025].
- **"Authorities are arming themselves; it's an arms race."** Hungary already screens with AI [WTS-HU-2026] and
  the worry is voiced [KPMG-TNF-2024]. Response: screen yourself first (`#15`) and make filings consistent (`#08`).

## 10. Sources

Full details for keys used in the use cases are in the YAML. Keys cited above that are not in the YAML:

- BGOV-AGENTS-2026: "Companies' Sharing of AI Agents Risks More Tax Fights", Bloomberg Government, 2026-08-21, https://news.bgov.com/daily-tax-report/companies-sharing-of-ai-agents-risks-more-tax-fights (first paragraphs)
- BTAX-VAT2026: "Digital Mandates and AI Reshape VAT Compliance Landscape in 2026" (E. Trombitas), Bloomberg Tax, 2026-01-06, https://news.bloombergtax.com/tax-insights-and-commentary/digital-mandates-and-ai-reshape-vat-compliance-landscape-in-2026 (routed from indirect-tax)
- CIAT-BLOG-2026: "Artificial Intelligence Agents in the control of Transfer Pricing" (P. Porporatto), CIAT, 2026-02-03, https://www.ciat.org/artificial-intelligence-agents-in-the-control-of-transfer-pricing/?lang=en
- GAO-2026: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management" (GAO-26-107522), GAO, 2026-03-24, https://www.gao.gov/products/gao-26-107522
- COLUMN-TAXCALCBENCH-2025: "TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task", arXiv (Column Tax), 2025-07-22, https://arxiv.org/abs/2507.16126 (abstract)
- HLB-CH7-2026: "OECD Proposes Revisions to TP Guidelines on Intra-group Services", HLB Thailand, 2026-08-31, https://www.hlbthai.com/oecd-proposes-revisions-to-transfer-pricing-guidelines-on-intra-group-services/
- OECD-INTRAGROUP-2026: "Companies Want OECD to Clarify Character of AI Transactions", Bloomberg Tax Daily Tax Report, 2026-08-25, https://news.bgov.com/daily-tax-report/companies-want-oecd-to-clarify-character-of-ai-transactions (first paragraphs)
- OXFORD-CBT-2026: Oxford CBT Summer Conference 2026 booklet, Session 4, 2026-06-26, https://oxfordtax.sbs.ox.ac.uk/sitefiles/cbt-summer-conference-booklet-2026
- TIGTA-2025: "The IRS Could Leverage Examination Results in AI Examination Case Selection Models and Improve Processes to Evaluate Performance" (2025-308-022), TIGTA, 2025-05-19, https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf
- PWCDE-CH7-2026: "OECD: Public consultation on Transfer Pricing Guidelines", PwC Germany, 2026-06-10, https://blogs.pwc.de/en/german-tax-and-legal-news/article/255082/oecd-public-consultation-on-transfer-pricing-guidelines/
