# Income tax provision and Pillar Two (tax)

Sources checked 2026-10-17. Use cases live in `../use-cases/provision-pillar-two.yaml` (16 entries). Ids are
shortened here: `#05` means `tax-provision-pillar-two-05`; other modules' ids are in full. Source keys in brackets, such as [FGS-GIR-2026], are given in full in
the YAML or in §10. **Evidence is thin, and thinner still for AI.** No entry has a measured AI outcome from a named
organisation: 13 entries are grade C and 3 are labelled ideas (grade D). The strongest named evidence (AMG Critical
Materials, `#09`, `#16`) is about rules-based Pillar Two software, not AI, so it is graded for AI use, not for software.
Almost every figure is vendor-published. Say so when you quote one.

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

Income tax accounting: the tax provision under ASC 740 (US GAAP) and IAS 12 (IFRS), meaning
current and deferred tax, valuation allowances and uncertain tax positions, plus the expanded disclosures required by
ASU 2023-09. It also covers the OECD global minimum tax (Pillar Two): GloBE calculations by jurisdiction, safe-harbour
tests, the GloBE Information Return (GIR) and its XML filing, domestic top-up tax returns (QDMTTs), and the data
pipeline and audit conversations around them. For many groups the hardest part of the first GIR season (due 30 June
2026) was creating and transmitting the XML files, not tax law [FGS-GIR-2026]; KPMG authors describe schema errors,
conflicting business rules and portals that went live late [BTAX-KPMG-GIR-2026]. Return preparation, R&D credit studies and stand-alone
tax research sit in other tax modules (compliance-corporate, research-advisory).

## 2. Processes and key steps

Finrep, a vendor, splits the provision into seven steps [FINREP-ASC740-2026]; work types are the analyst's mapping.

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Close data to provision inputs | Pull trial balances, map accounts into provision inputs | data-reporting | Kognitos (vendor) calls the close-to-tax handoff often manual and error-prone [KOGNITOS-2026] |
| Book-to-tax and current tax | Identify book-to-tax differences, compute current tax | transaction-processing | Rules-heavy; AI inherits every source-data error [FINREP-ASC740-2026] |
| Deferred tax and rollforward | Compute deferred tax assets and liabilities; remeasure for enacted rate changes | transaction-processing, data-reporting | A rate change signed but not yet effective forces immediate remeasurement [FINREP-ASC740-2026] |
| Valuation allowance and uncertain tax positions | Judge whether deferred tax assets will be realised; assess positions that may not be sustained | expert-judgment, research-synthesis | Finrep says these stay human judgments [FINREP-ASC740-2026] |
| Rate reconciliation and taxes paid (ASU 2023-09) | Tabular reconciliation by category; items at or above 5% broken out; taxes paid by federal, state/local, foreign | data-reporting | New category and jurisdiction detail that Excel processes struggle to produce [KPMG-ASU-2023, FINREP-ASC740-2026] |
| Footnotes, review, controls, auditor support | Draft disclosures, review, document controls | document-production, review-assurance | Generic wording risks SEC comment letters (vendor view) [FINREP-ASC740-2026] |
| Pillar Two data collection | Collect entity-level data beyond what CbCR (country-by-country reporting) held | data-reporting | More than 100 data points in the first GIR [TR-CORPAI-2026]; data from several ERPs [EY-P2DATA-2024] |
| GloBE computation | Jurisdictional effective tax rates (ETRs), safe-harbour tests, top-up tax, QDMTT | transaction-processing | Rules changed in January and September 2026 [OECD-SBS-2026, OECD-P2-SEP-2026] |
| Pillar Two in the accounts | Account for top-up tax under the May 2023 IAS 12 amendment | expert-judgment | Early auditor dialogue advised while Side-by-Side law is pending [OECD-SBS-2026] |
| GIR filing | Populate the GIR, generate and validate XML, transmit | data-reporting, software-systems | Country XML variants, gatekeeper business rules, late portals [FGS-GIR-2026] |
| Notifications and local returns | GIR notifications, self-assessment and QDMTT returns, registrations | coordination-scheduling | Over 60% of Orbitax's filing activity [ORBITAX-SEASON-2026] |
| Corrections | Amend accepted filings by reference ID | data-reporting | Whole sections replaced, no field-level fixes [FGS-GIR-2026] |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment one step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the process or the service model changes). Coverage:
assist 2, augment 6, automate 8, delegate 0. Scope: step 11, process 3, model 2. **Six of the eight automate
entries, including both model entries, are rules-based software with no AI claimed** (`#09`, `#11`, `#12`, `#13`, `#15`,
`#16`). No delegate-level evidence exists for this module; do not imply otherwise.

**Provision data and calculation**
- Improve: `#01` cited research and AI insights inside Bloomberg Tax Workpapers and ONESOURCE (CoCounsel Tax); TR's
  "hours to minutes" has no baseline. `#02` idea: AI explains and checks Excel provision workbooks (a TEI lab topic).
- Automate: `#03` automated cleansing, rollforwards and book-to-tax adjustments, with an agentic data layer upstream
  of the engine (vendor descriptions only; the data layer itself is `tax-data-technology-02`). `#07` live R&D credit data in the provision, which TR says can reduce
  return-to-provision adjustments (vendor; the credit work itself is `tax-compliance-corporate-09`).
- Forecasting: PwC Ireland says AI on a sound data foundation can improve forecasts of effective tax rates and
  deferred tax balances [PWC-IE-2026]. Not a separate entry here; see `tax-compliance-corporate-14` (continuous ETR
  modelling) and `tax-compliance-corporate-18` (PwC's ETR model that explains its inputs and locks approved logic).

**Review and disclosure**
- Improve: `#04` anomaly flagging of deferred balances and PDF comparison (Corptax roadmap; a TR job posting to test
  anomaly detection and AI-assisted review). `#05` AI categorisation of ASU 2023-09 reconciling items (one vendor's
  account). `#06` idea: GenAI first draft of tax footnotes, with every draft approved by a tax professional.

**Rules and law changes**
- Improve: `#08` Orbitax Tax Flows tracks regulatory change and sends comparison reports; Corptax roadmap item; KPMG
  says building an agent for changing tax rules fell from weeks to minutes (self-reported, general).

**Pillar Two data, computation and filing**
- Improve: `#14` Orbitax XatBot answers questions over live scenarios (for example, which jurisdictions have a GloBE ETR below 15%), checks
  uploaded CSVs and drafts audit-committee updates. The only generative AI found inside a Pillar Two engine; its user
  is unnamed. `#10` idea: AI-assisted mapping of ERP data to GloBE data points (EY).
- Automate (rules-based): `#09` seeding Pillar Two data from validated CbCR XML (AMG: around 10 days to implement).
  `#11` engines for safe harbours, scenarios and interim provision estimates. `#12` GIR population, XML validation and
  machine-to-machine transmission (Orbitax: 1,700+ filings). `#13` correction management by reference ID (FGS app).

**Operating and service model**
- Reinvent (rules-based): `#15` firm-run platforms sold with specialist teams (Deloitte Pillar Two Agent under
  co-sourcing; EY GloBE Engine; FGS). `#16` insourcing: AMG's two-person team covered 70-80 entities in 25
  jurisdictions with no added headcount (vendor case study). Ask whether AI is part of either; the sources claim no AI for the core work, though the insurer's case
  study says the XatBot copilot helped with day-to-day filing-season issues [ORBITAX-LEAN-2026].

## 4. Interview probes

1. **Which provision steps (data pull, book-to-tax, deferred rollforward, uncertain positions, rate reconciliation,
   footnotes) does AI touch today, and what has your auditor asked about each?** Separates real AI use from rules-based
   automation, and shows whether audit reliance has been discussed at all (nobody has published how auditors rely).
2. **Where does the close-to-tax handoff break, and who owns the data between ledger and provision?** The usual
   bottleneck is data [KOGNITOS-2026]; it decides whether `#03` or `#04` can work.
3. **How do you build the ASU 2023-09 rate reconciliation, and who signs off the category and narrative?** Shows the
   data gap behind `#05` and who holds the judgment [FINREP-ASC740-2026].
4. **Is any part of the provision still Excel-only, and what controls sit around it?** Points to `#02` and to control
   documentation needs.
5. **How do law changes reach the deferred tax calculation, and how fast?** Tests whether `#08` monitoring would
   change anything.
6. **In the first GIR season, where did errors surface (data mapping, safe-harbour tests, XML validation, portal
   rejection), who found them, and did you run a parallel check against Excel?** The insurer used its platform as an
   independent check [ORBITAX-LEAN-2026]; answers locate the real constraint.
7. **How are you planning corrections, the revised GIR and XML schema, and 2027 filings with more jurisdictions?**
   Shows readiness for `#13` and the 2027 test [BTAX-KPMG-GIR-2026].
8. **Did you insource or outsource Pillar Two, and what happened to headcount and to how the team spends its time?**
   Places the client on `#15` or `#16`.
9. **Does your Pillar Two platform include an AI assistant, and does anyone use it for filing-file content?** Tests
   `#14` and whether verification and professional judgment are recorded [ORBITAX-XATBOTPRO-2026].
10. **Who validates an AI feature before your team relies on it: the vendor, your team, or your auditor?** TR is
    recruiting experienced provision staff to validate its AI features [TR-JOB-2026].
11. **Have you measured anything before and after: close days, review findings, return-to-provision true-ups,
    audit adjustments?** No published baseline exists for this module, so any number the client has is valuable.

## 5. Metrics and benchmarks

What to measure: days from close to final provision; review findings and audit adjustments on tax balances;
return-to-provision true-up size; GIR validation failures and resubmissions; days filed before deadline; hours per
entity on Pillar Two data. **No error rate, override rate, parallel-run result or independent accuracy test exists for
AI in provision or Pillar Two work.**

| Figure | What it counts | Source and caveat |
|---|---|---|
| 67% | Corporate tax departments not using GenAI | [TR-CORPTAX-2025], vendor-owned survey of 288 tax departments |
| 58% (51% a year earlier) | Departments saying they are under-resourced | [TR-CORPTAX-2025] |
| 71% / 66% | Companies' tax departments using AI tools / AI users reporting noticeable time savings | [KPMG-DE-2026], KPMG Germany quick survey, sample not stated |
| 47% / 41% / 41% | Hurdles: IT approvals / data protection / lack of knowledge | [KPMG-DE-2026] |
| 91% / 41% | Want AI more accurate than humans / will not use AI without review unless 100% accurate | [TR-AGENTICCORP-2025], vendor blog; the article does not name the survey behind these two figures |
| 20% | GIRs filed successfully before the initial deadline in some jurisdictions | [BTAX-KPMG-GIR-2026], KPMG's experience, not a global rate |
| 120+ | Business rules in the OECD digital rulebook | [BTAX-KPMG-GIR-2026] |
| 100+ | Data points the first GIR required | [TR-CORPAI-2026], vendor |
| 1,700+ / 34 | Pillar Two filings prepared or submitted through Orbitax / jurisdictions, Nov 2025 to Jun 2026; over 60% notifications and self-assessment returns; nearly a third in the final week | [ORBITAX-SEASON-2026], vendor-published |
| ~10 days; 2 people; 70-80 entities; 25 jurisdictions | AMG's implementation time and team size for first-year Pillar Two compliance | [ORBITAX-AMG-2026], vendor case study, no baseline, not AI |
| 21% | Respondents very prepared for Pillar Two reporting | [EY-TFO-2025], EY survey (1,600 CFOs and tax and finance leaders) |
| 85% / 81% | Expect to pay more tax / call Pillar Two the biggest legislative change | [EY-GLOBE-ENGINE-2026], EY quoting its 2025 survey |
| 70% / 76% | Expect to pay over US$500,000 a year to comply / CFOs expecting technology to absorb cost at the same staffing | [DELOITTE-P2AGENT-2024], Deloitte survey of over 500 tax leaders and CFOs, date not stated |
| 92% | Respondents expecting a global minimum tax to increase disputes | [EY-PAPERJAM-2026], EY Luxembourg, promotional |
| 12% | Share of US restatement events citing tax accounting issues, 2013-2022 (717 of 5,793; 7% in 2022) | [CAQ-RESTATE-2024], report PDF read; context only, not AI |
| < 1/3 | Simplified US personal federal returns computed correctly by frontier models | [COLUMN-TAXCALCBENCH-2025], adjacent (individual tax), not provision |

## 6. Guardrails

- **Shared conduct rules** for tax practitioners (IRS OPR Alert 2026-19, section 7216, PCRT, TPB) are in
  [the archetype guardrails](../guardrails.md). The rules below are specific to tax accounting and Pillar Two filing.
- **ASU 2023-09.** Public business entities must give a tabular rate reconciliation in percentages and amounts by
  category, with items at or above 5% of statutory tax broken out, and taxes paid by federal, state/local and
  foreign; effective for fiscal years beginning after 15 December 2024 (others after 15 December 2025) [KPMG-ASU-2023].
- **IAS 12** was amended in May 2023 for the Pillar Two model rules [IFRS-IAS12-2023] (the amendment text was not read).
- **OECD filing rules.** The GIR XML user guide sets validation elements a receiver may check automatically
  [OECD-GIR-XML]; June 2026 guidance fixed errors and switched off some rules [OECDPILLARS-GIRXML-2026]; the
  11 September 2026 package brings a revised GIR and a peer review of domestic laws [OECD-P2-SEP-2026].
- **Audit.** A PCAOB staff spotlight (July 2024; staff views, not Board policy) reports that audit firms expect GenAI
  to augment, not replace, people and that an engagement team member using GenAI stays responsible for the work; it
  also reports preparers' concerns about black-box tools and inconsistent output [PCAOB-GENAI-2024]. No tax-specific
  guidance on auditing AI-prepared tax balances was found. Tax accounting issues were cited in 12% of US restatements
  from 2013 to 2022, falling to 7% in 2022 [CAQ-RESTATE-2024].
- **Controls.** Finrep (vendor) says AI inside a provision should be documented as a SOX control; this reading was not
  verified [FINREP-ASC740-2026]. Kognitos logs every data step because the provision feeds audited statements [KOGNITOS-2026].
- **Professional body.** The AICPA's Council on AI Risk in Tax (23 September 2026) will refine a 20-risk framework
  for tax administration and preparation [AICPA-CART-2026]; its appendices do not mention provision or ASC 740 [AICPA-WERFEL-2026].
- **Human judgment stays with people on:** valuation allowances and uncertain tax positions [FINREP-ASC740-2026];
  classification and wording of rate-reconciliation items [FINREP-ASC740-2026]; Side-by-Side and safe-harbour
  elections [OECD-SBS-2026]; anything entering a Pillar Two filing file [ORBITAX-XATBOTPRO-2026]; resolving XML
  validation errors [ORBITAX-LEAN-2026].
- **Verification controls offered by vendors** (untested): Orbitax scores each key point High, Medium or Low against
  its database and the web [ORBITAX-XATBOT-2026]; TR links answers to primary sources [TR-AGENTICCORP-2025].

## 7. Roles and how they evolve

- **Lean teams on platforms.** AMG's vice president of tax and one manager delivered first-year Pillar Two compliance
  with no added headcount (vendor-published, not AI) [ORBITAX-AMG-2026].
- **Validators of AI.** Thomson Reuters seeks provision practitioners with 5-7 years' experience to judge AI accuracy
  [TR-JOB-2026]. Gamma's senior tax manager posting asks for a builder who uses AI and automation to keep the function
  lean [GAMMA-JOB-2026]. Apple's tax technology lead posting lists Pillar Two reporting knowledge as preferred [APPLE-JOB-2026].
- **Data and validation managers.** Orbitax says understanding local filing obligations became as important as the
  calculations, with reviews, validation checks and submissions still to manage once calculations were done
  [ORBITAX-SEASON-2026]. PwC Ireland expects "tax data lead" and "model
  governance lead" roles [PWC-IE-2026].
- **Skills gap.** Deloitte's research lists technology skills as the third biggest talent gap in Pillar Two
  implementation [DELOITTE-P2AGENT-2024].
- **Headcount.** 58% of companies expect stable domestic tax headcount and 72% stable international headcount
  [KPMG-DE-2026]. Sala argues AI will shrink corporate tax teams little because AI cannot hold culpability and tax
  practice is more than preparation [SALA-TAXNOTES-2026].

## 8. Frontier

- **2025-11-03:** a TEI-SJSU panel deck puts multi-agent workflows, including provision-to-return automation with
  people handling exceptions, at the top of its progression [SJSU-TEIHTTI-2025]. Delegate-level; no deployment shown
  (see `tax-data-technology-10`).
- **2026-01-05 and 2026-09-11:** OECD Side-by-Side package, then a second package with a revised GIR; a revised XML
  schema is expected [OECD-SBS-2026, OECD-P2-SEP-2026].
- **2026-03-15 to 18:** TEI Midyear's preliminary programme (February 2026) scheduled a "Pillar Two and Technology"
  lab, an Excel-and-AI lab and a "Tax GPT" closing plenary (titles only) [TEI-MIDYEAR-2026].
- **2026-04-19 and 2026-05-04:** Orbitax adds Autopilot, Deep Research, MCP connections and Tax Skills to XatBot, then
  offers Pro+ to GMT users for the filing season [ORBITAX-XATBOT-2026, ORBITAX-XATBOTPRO-2026].
- **2026-05-20:** KPMG and Anthropic announce Claude in KPMG's Digital Gateway, with an initial focus on tax clients and
  private equity firms [KPMG-ANTHROPIC-2026].
- **2026-06-16 and 18:** a Bloomberg Tax forum panel on AI in compliance, provisioning and risk (pre-event notice only)
  [BTAX-FORUM-2026]; a TPMinds Pillar 2 Summit session on operational implementation, data and technology [TPMINDS-P2-2026].
- **2026-06-24:** Thomson Reuters recruits a ONESOURCE Tax Provision specialist to test generative AI features [TR-JOB-2026].
- **2026-06-25:** a podcast episode covered Pillar Two data collection and how AI helps with complex rules (show
  notes only) [ACAST-TAXTECH-2026].
- **2026-08-03 and 2026-08-21:** FGS expects corrections to rise [FGS-GIR-2026]; KPMG authors expect a bigger 2027 test
  as 19 second-wave jurisdictions join the original 37 [BTAX-KPMG-GIR-2026].
- **2026-10-02:** an arXiv preprint proposes LLM-plus-verification turning tax forms into executable code (adjacent,
  US personal tax) [HAN-LAWORDER-2026].

## 9. Common objections

- **"AI is not accurate enough for audited numbers."** Agree on the evidence: 41% will not use AI without review unless
  it is 100% accurate [TR-AGENTICCORP-2025], and no accuracy test exists for provision AI. Start with assist and
  augment uses (`#01`, `#04`, `#14`) where a person reviews every output, and keep judgments human.
- **"Our auditor will not rely on it."** No regulator or audit firm was found saying how it would. Audit firms told PCAOB
  staff that the person using GenAI stays responsible for the work [PCAOB-GENAI-2024]. Raise it early, as KPMG UK advises for Side-by-Side reporting [OECD-SBS-2026].
- **"Our data is not ready."** Often true. EY says automation and AI should follow standardised data processes
  [EY-P2DATA-2024]; Finrep warns that skipping cleanup lengthens the review list [FINREP-ASC740-2026]. Data work
  (`#03`, `#09`) comes first.
- **"The AI features are marketing."** Partly right: several are roadmap items or rules-based tools [CORPTAX-2026,
  FINREP-ASC740-2026]. Ask vendors for a named customer and an error rate; none has published one.
- **"Pillar Two is a filing problem, not an AI problem."** The first season supports this: XML variants and business
  rules were the main hurdle [FGS-GIR-2026], and the platforms described in `#11` and `#12` are rules-based.
- **"We cannot get approvals."** IT approvals, data protection and lack of knowledge are the top hurdles [KPMG-DE-2026].
- **"AI cannot take responsibility."** True, and Sala's argument [SALA-TAXNOTES-2026]: sign-off stays with people.

## 10. Sources

Keys used above that are not in this module's YAML (all opened; show notes and abstracts are marked):

- ACAST-TAXTECH-2026: Tax, tech, and other stuff podcast (Acast), ep. 26, Tax, Tech & The Pillar Two Reality Check,
  2026-06-25 (show notes only), https://shows.acast.com/tax-tech-and-other-stuff/episodes/6a3ce7b00ad474357457b7fb
- AICPA-CART-2026: The Tax Adviser (AICPA), AICPA, former IRS commissioner to lead initiative on AI in tax, 2026-09-23,
  https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/
- AICPA-WERFEL-2026: The Tax Adviser (AICPA), A Risk Framework for the Use of AI in Tax Administration and
  Preparation: appendices A to D, 2026-06, https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
- APPLE-JOB-2026: Apple (via AnitaB.org job board), Tax Technology Lead, 2026-06-25,
  https://jobs.anitab.org/companies/apple/jobs/84254724-tax-technology-lead
- BTAX-FORUM-2026: Bloomberg Tax, Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk,
  2026-06-10, https://pro.bloombergtax.com/?p=17345
- CAQ-RESTATE-2024: Center for Audit Quality, Financial Restatement Trends in the United States 2013-2022, 2024-06,
  https://thecaq.wpenginepowered.com/wp-content/uploads/2024/06/caq-financial-restatement-trends-us-2013-2022_2024-06.pdf
  (Taxes row in the accounting-issues table).
- COLUMN-TAXCALCBENCH-2025: Column Tax authors (Bock, Molisee, Ozer, Shah), arXiv preprint, TaxCalcBench: Evaluating
  Frontier Models on the Tax Calculation Task (arXiv 2507.16126), 2025-07-22 (abstract), https://arxiv.org/abs/2507.16126
- EY-PAPERJAM-2026: Paperjam (EY Luxembourg, promotional), Tax controversy in a GenAI world, 2026-03-06,
  https://en.paperjam.lu/article/tax-controversy-in-a-genai-world
- EY-TFO-2025: EY, EY Tax and Finance Operations Survey press release, 2025-11-18,
  https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments
- GAMMA-JOB-2026: Gamma, Senior Tax Manager job posting (via Accel job board), 2026-08-04,
  https://jobs.accel.com/companies/gamma-3/jobs/88655517-senior-tax-manager
- HAN-LAWORDER-2026: arXiv preprint (Han, Takashima, Wei, Li, Genesereth), Law And Order: Tax Law Autoformalization
  (arXiv 2610.02792), 2026-10-02 (abstract), https://arxiv.org/abs/2610.02792
- IFRS-IAS12-2023: IFRS Foundation / IASB, International Tax Reform - Pillar Two Model Rules (amendments to IAS 12
  project page), 2023-05, https://www.ifrs.org/projects/completed-projects/2023/international-tax-reform-pillar-two-model-rules/
- KPMG-DE-2026: KPMG Germany, Tax departments are increasingly turning to artificial intelligence (KPMG Germany quick
  surveys), 2026-05-07, https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html
- PWC-IE-2026: PwC Ireland, Evolving the tax function with AI: Four key insights to guide tax leaders, 2026-07-21,
  https://www.pwc.ie/services/tax/insights/evolving-the-tax-function-with-ai.html
- SJSU-TEIHTTI-2025: TEI and San Jose State University, AI and Other Emerging Technologies for Tax Practitioners
  (High Tech Tax Institute panel deck), 2025-11-03, https://www2.sjsu.edu/taxinstitute/docs/4D_AI.pdf
- TPMINDS-P2-2026: Informa Connect, TPMinds International Pillar 2 Summit agenda, 2026-06-18,
  https://informaconnect.com/tp-minds-international-conference/agenda/4/
