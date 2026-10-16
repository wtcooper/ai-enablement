# Assurance x state of AI adoption and disruption

- **Archetype:** assurance. External audit and other assurance services (financial statement and ICFR audits, SOC, sustainability and other attest), performed by firms of all sizes, overlapping with in-house internal audit.
- **Topic:** state-of-ai-disruption. Measured adoption today, firm platforms and investment, maturity spread, and disruption scenarios.
- **Prepared:** 2026-10-16. **Landscape:** `research/runs/wave1/landscape-assurance.md`.
- **Method.** Pages were fetched with `curl` (and `pdftotext` for PDFs); 4 web searches were used (SEC filer status, FRC SME market study, audit-fee pricing, CSRD Omnibus). About 50 distinct sources were opened. The fetch dates are 2026-10-16. Each source in section 5 is marked `access: full` (page or PDF opened and read) or `access: search-only` (seen only in a search result).
- **Reading convention.** Tags used throughout:
  - **[MEASURED]**: a count or percentage a named party measured.
  - **[ANNOUNCED]**, **[PILOT]**, **[IN USE]**: tense of a deployment claim.
  - **[FORECAST: who]**: a prediction, labelled with who made it and any interest they have in it.
  - Provenance is stated for every figure: `independent`, `regulator-observed`, `self-reported`, `vendor-published`.
  - Quotations are under 25 words.

---

## 1. Summary

- **Adoption is real at the top and thin below it, and almost nothing is measured independently.**
  - The Big Four and Grant Thornton US announced firm-wide agent platforms between Apr 2025 and Jun 2026 (EY-CANVAS-2026, KPMG-CLARA-2025, DELOITTE-OMNIA-2026, GT-GTAP-2026).
  - The best public data on smaller firms is a 54-firm US survey: 75% had no documented transformation plan and only 11% had an automated substantive-analytics solution (CPACOM-ATR-2025, pp.3, 9, 10).
  - Regulators' own counts show uneven use by audit area: journal entries 88%, controls testing 43%, IT applications 39% "frequently observed" (IFIAR-TTF-2025, 2024 table).
- **The measured time savings so far are modest.**
  - PwC's US assurance leader said in Oct 2026 that busy-season time savings are "not that drastic yet" and the final audit report "still looks the same" (CFODIVE-PWC-2026).
  - The large productivity numbers in circulation are vendor-published (DataSnipper "$1.4B"; Optro/Reddit "60%") (DATASNIPPER-2026, OPTRO-CRX-2026).
- **The disruption that is evidenced is structural, not yet economic.**
  - Capital is flowing into AI-native audit ventures: Modus $85M (Apr 2026), Repodo EUR 8.2M (Aug 2026), Fieldguide $75M at $700M valuation (Feb 2026) (MODUS-2026, REPODO-2026, FIELDGUIDE-2026).
  - Independence rules are being rewritten around private equity and AI-tool vendors (AT-PEEC-2026, TR-HOHL-2026).
  - I found no measured loss of audit revenue or demonstrated fee fall attributable to AI. The one fee case is a second-hand report of a 14% fee drop in KPMG's own audit (VERDANTIX-KPMGFEE-2026; LDS-KPMGFEE-2026).
- **Scope changes that matter more than AI in the near term are regulatory.**
  - The SEC's 19 May 2026 filer-status proposal would, if finalised, move roughly half of currently attested issuers out of SOX 404(b) (UNIQUS-FILER-2026). Comments closed 20 Jul 2026 and the proposal is not final.
  - The EU's Omnibus Directive (EU) 2026/470 (26 Feb 2026) narrowed CSRD scope and removed the requirement to adopt reasonable-assurance standards (EURLEX-2026-470, recitals 2, 3, 11; Art. 26a(3)).
  - Neither source ties its change to AI.
- **Standard-setters are deliberately not setting technology requirements yet.** The IAASB's Aug 2026 exposure draft says it is "premature" to set technology-related requirements and that GenAI tools strain the audit-evidence "input-output model" (IAASB-ED500-2026, EM paras 65-69, p.20).
- **Demand for assurance over AI and AI-affected controls is the clearest forecast growth line, and it is firm-forecast.**
  - EY, KPMG and Deloitte each launched or described AI-assurance offers (EY-SOC-2026; KPMGUK-GOVAI-2026; DELOITTE-OMNIA-2026).
  - Audit partners rate AI governance maturity at their largest client as "advanced" in only 6% of cases (BOARDMEMBER-CAQ-2026).
  - The accreditation layer for AI assurance is still maturing (CSA-AIASSURE-2026, a lead).
- **Pricing is the open scenario.** Analysts argue both that AI should lower audit fees and that continuous assurance could be repriced upward (VERDANTIX-KPMGFEE-2026). The CPA.com survey shows 74% of small and mid-size firms expect to raise fees as a growth strategy (CPACOM-ATR-2025, p.9). No source measures realised pricing under AI.
- **Several data points in circulation are weaker than they look.** See section 6 for the specific conflicts, including a benchmark paper (FinancialAuditBench) whose listed authors include names matching the Modus co-founders.

---

## 2. Findings

### 2.1 Measured adoption today

**Regulator-observed use by audit area (international).**
- IFIAR's annual inspection-findings survey asks members how often they see automated tools and techniques (ATTs) in audit files. In the 2024 data, "frequently observed" was reported for journal-entry testing 88% (48 members answering), risk assessment 55% (47), substantive procedures 55% (47), internal-controls testing 43% (46) and IT applications and security configurations 39% (44) (IFIAR-TTF-2025, 2024 table, p.5). `regulator-observed`; it measures how often regulators see a tool in files they inspect, not what share of audits use one.
- The 2023 equivalents were 86%, 49%, 51%, 33% and 33% (IFIAR-TTF-2025, 2023 table). The report describes "a trend of more frequent ATT adoption" (IFIAR-TTF-2025, p.5).
- 31% of members reported findings that a tool "was not used as intended", up from 29% (IFIAR-TTF-2025, p.5). Report released 27 Mar 2025.
- IFIAR also says many members observe that "a relatively small number" of tools are used on all or most audits within a network (IFIAR-TTF-2025, section on tool development).
- IFIAR members encourage firms to consult them early where AI makes judgments without human involvement (IFIAR-TTF-2025, key message 4). That is a stated supervisory position, not a prohibition.

**Smaller and mid-size US firms (the best public benchmark).**
- CPA.com's 2025 Audit Benchmark (fielded Jun-Aug 2025) had 74 firms register and 54 with complete data. The report itself says the sample is "not a representative view of all CPA firms" (CPACOM-ATR-2025, pp.3, 27). `independent` of firms, but a convenience sample recruited at ENGAGE and through firm associations.
- 75% of the 54 firms had not formally documented a transformation plan (CPACOM-ATR-2025, p.3, p.9).
- The report is inconsistent on non-use of AI: "nearly one-quarter report no use of AI or advanced automation tools" (p.3), "approximately one-fourth of firms aren't using AI at all, and 22% have zero automated solutions" (p.4), and "approximately one-third" not using AI at all (p.11).
- Share of firms with an automated solution: workflow management 39%, foot and proofing 39%, confirmations 39%, trial-balance import 35%, engagement letters 26%, time and billing 24%, risk assessment 22%, data ingestion 19%, report production 17%, substantive analytics 11%, none 22% (CPACOM-ATR-2025, p.10 chart).
- Top obstacles: staff not trained in advanced approaches 66%, poor-quality client data 60%, lack of access to client information and systems 53%, budget constraints 53%, current methodology does not enable transformation 30% (CPACOM-ATR-2025, p.8 chart).
- ROI measure firms use: staff efficiency 83%, audit quality 54%, cost savings 37%, "do not currently measure" 6% (CPACOM-ATR-2025, p.12 chart).
- The report says the firms furthest along spend a larger share of time on planning and less on fieldwork and wrap-up, and that many such firms use familiar tools such as Excel and Power BI for analysis (CPACOM-ATR-2025, p.4; p.15). It does not publish a quantified time split in the text I read.
- 87% of firms track realization and 76% billable hours; only 13% track the share of engagements on value-billing agreements (CPACOM-ATR-2025, p.22 chart).
- 66% of firms communicate their technology and methodology to clients as a differentiator (CPACOM-ATR-2025, p.12).

**UK smaller firms.** The FRC's SME audit-market study (final steps, Mar 2026) concluded that technology constraints should be addressed through a technology sandbox (ICAEW-FRCSME-2026). The FRC's Jun 2026 release launched an "Unlocking barriers to audit tech" project to build an evidence base on smaller firms' adoption challenges (FRC-SANDBOX-2026). That is an acknowledgement that the evidence base does not yet exist; I did not find the FRC's own adoption figures (see Gaps).

**Internal audit.**
- Gartner's survey of 119 chief audit executives (Aug 2025; released 27 Jan 2026): 83% of audit functions are piloting or using AI and another 12% plan to within the year. Over 70% call analytics and GenAI important priorities, yet Gartner says CAEs "lack confidence" in achieving them because of data quality, skills and access (GARTNER-2026). `self-reported`, CAE perception; "piloting or using" lumps pilots with production.
- KPMG's 2025 SOX Survey (company-side): the cost of maintaining SOX controls rose 45% between its 2023 and 2025 surveys; average testing hours per control rose from 12 (FY2022) to 16 (FY2024); 52% of internal audit departments spent more than 40% of internal-audit hours on SOX in FY2024 (KPMG-SOX-2026, p.4 insert). `self-reported` by surveyed companies; sample size not given in the excerpt. This is a baseline of rising cost before AI, which is what AI-based testing claims to reverse.
- Vendor-published: Optro said Reddit's internal audit team automated 175 controls, "more than 40 percent" of its SOX scope, and cut testing time per control by 60% on average in its first three months (OPTRO-CRX-2026, 14 Oct 2026). Single customer, vendor-reported.
- RSM US and Andera announced on 26 Aug 2026 an AI-enabled control-testing platform "for internal audit" functions, integrated into RSM's next-generation audit platform [ANNOUNCED] (ANDERA-RSM-2026).

**Whole-profession and adjacent surveys (not audit-specific or not auditor-measured).**
- Thomson Reuters Institute, Future of Professionals 2026 (tax and audit paper, 21 Jul 2026): 81% of tax and audit professionals say they use AI regularly; over a quarter would not accept a job at a firm lacking professional-grade AI; almost 1 in 3 would consider leaving if AI expectations go unmet within two years; more than one-third admit using unauthorised AI tools; nearly half feel pressure to generate financial gains from AI; one-third say their firms have not adapted commercial models (TRI-FOP-2026). `self-reported`, vendor-run (Thomson Reuters sells audit software). This corrects the landscape, which said the unauthorised-AI figure was not on the opened page.
- ISACA AI Pulse Poll (5 May 2026; 3,400+ digital-trust professionals, global): 38% have a formal comprehensive AI policy (28% in 2025), 22% say AI ROI met or exceeded expectations, 90% believe employees use AI (ISACA-PULSE-2026). Not audit-firm-specific.

**Client-side maturity (drives assurance work).**
- CAQ Spring 2026 Audit Partner Pulse (15 Jul 2026): nearly 90% of respondents rated AI-governance maturity at their largest client "developing" or "early stage" (CAQ-PULSE-2026). The breakdown, reported in a Corporate Board Member article, is 6% advanced, 40% developed but incomplete, 46% early stage (BOARDMEMBER-CAQ-2026).
- 57% say AI governance is audit committees' biggest challenge, ahead of cybersecurity 51% and finance transformation 36%; two-thirds say the audit committee raised AI in operations or reporting (BOARDMEMBER-CAQ-2026). `self-reported` audit-partner perception; number of respondents not stated in the pages I read.

**What measurement is missing.**
- I found no independent measure of the accuracy, error rate or audit-quality effect of any firm's production audit AI. The nearest are lab-style benchmarks: ICAEW's single test found chatbots did not do ISA 315 risk assessment as a human would (ICAEW-PIERPOINT-2025, test conclusion), and the FinancialAuditBench preprint (26 Sep 2026) evaluated 11 frontier models on 90 workpaper tasks across six synthetic engagements and found they "complete substantial portions" of staff-level tasks but sometimes perform inappropriate procedures or write incorrect documentation (ARXIV-FAB-2026, abstract).
- No source I opened reports measured changes in audit hours, fees, staffing pyramids or margins attributable to AI at firm level.

### 2.2 Firm platforms and investment

| Firm | What was said | Scale claim | Tense | Date | Ref |
|---|---|---|---|---|---|
| **EY** | Multi-agent framework embedded in EY Canvas on Microsoft Azure, Foundry and Fabric; "immediately embeds AI in all phases of the audit"; "expected to support all end-to-end audit activities by 2028" | 130,000 assurance professionals, 160,000 engagements, 150+ countries; Canvas processes 1.4 trillion journal-entry lines a year; part of a US$1b four-year assurance technology programme (earlier releases) | rolled out (announced as global roll-out); end-to-end is a forecast | 7 Apr 2026 | EY-CANVAS-2026 |
| **KPMG** | AI agents in KPMG Clara for expense vouching, unrecorded-liability search and accrued expenses; Financial Report Analyzer for disclosure checklists; "additional AI agents will be deployed over the next 12 months", including controls testing | "more than 95,000 auditors" (the release says the deployment "aims to empower" them) | announced | 22 Apr 2025 | KPMG-CLARA-2025 |
| **Deloitte** | "Unified agentic intelligence network" in Omnia; agents execute preliminary procedures and draft preliminary conclusions "for professionals to review"; tutor mode | "nearly 85,000" audit and assurance practitioners; built by internal engineering teams; "more than a decade of investment" | launched | 24 Jun 2026 | DELOITTE-OMNIA-2026 |
| **PwC** | Tools for planning (Simplified Audit for Private Business), Advanced Walkthrough Assistant, Evidence Match (cash, receivables, payables); controls-testing automation "expected"; "one global new agentic platform" about 18 months after 2026 | Global chair's letter: "nearly $1.5 billion" accelerated AI investment (firm-wide, not assurance-only) | mixed: some in use, others planned | 28 Oct 2025; 7 Oct 2026 | PWC-AT-2025; CFODIVE-PWC-2026 |
| **Grant Thornton US** | gtap, a proprietary audit infrastructure that ingests data from any ERP and supports full-population analysis; private-company audits first, "public company audits next year"; designed as foundation for an "agentic audit model" | Platform of nearly 20 aligned firms and about 25,000 professionals; operates under an alternative practice structure | launched (phase 1) | 7 May 2026 | GT-GTAP-2026 |
| **RSM US** | Alliance with Andera for control testing for internal audit; Ask Luca and Luca Resourcing (landscape, not re-opened) | none stated | announced | 26 Aug 2026 | ANDERA-RSM-2026 |

- Investment levels are disclosed unevenly and are not comparable: EY's US$1b figure is a four-year assurance technology programme (EY-CANVAS-2026, related-news items); PwC's "nearly $1.5 billion" is firm-wide AI investment, per a spokesperson pointing to the Global Annual Review 2025 letter (CFODIVE-PWC-2026); I found no disclosed audit-specific investment figure for KPMG, Deloitte, Grant Thornton or RSM in the pages opened.
- PwC says AI-assisted audit tools began being used "one year ago this month" (Oct 2025) and that for 2026 year-end audits its Simplified Audit - Execute tool reads supporting documents and flags missing information, with a second tool analysing audit-committee communications (CFODIVE-PWC-2026). That is the nearest thing to an "in production" statement from PwC.
- PwC's own Oct 2025 forecast, "end-to-end AI-driven automation should be expected sometime within calendar year 2026", came with hedges in the same article: some tools "soon", others piloting (PWC-AT-2025). By Oct 2026 the firm described time savings as modest (CFODIVE-PWC-2026).
- Deloitte's release says "additional capabilities expected to build on this foundation over time", and EY's end-to-end claim is for 2028 (DELOITTE-OMNIA-2026; EY-CANVAS-2026). These are the firms' own roadmaps, not outcomes.
- Software vendors and platforms mid-tier firms can license:
  - Fieldguide raised $75M on a $700M valuation (Series C, led by Goldman Sachs Alternatives Growth Equity; $125M raised in total) on 2 Feb 2026 (FIELDGUIDE-2026).
  - Thomson Reuters launched Disclosure Review for Guided Assurance customers "at no additional cost" on 23 Sep 2026; roughly 30% of eligible Disclosure-module customers use it, generating close to 300 analyses a month (TR-DISCLOSURE-2026). `vendor-published`.
  - MindBridge launched Agentic Risk Assessment for audit planning on 22 Sep 2026 (MINDBRIDGE-ARA-2026).
  - DataSnipper claims "more than $1.4 billion" in customer productivity savings in 2025 and 600,000+ users (the user figure comes from the landscape); the release also cites a UK Public Accounts Committee hearing referencing efficiency savings of GBP 400,000 at the National Audit Office (DATASNIPPER-2026). `vendor-published`; method of calculation not given in the release.
- TR describes an "extended customer beta" before launch (TR-DISCLOSURE-2026), and says future versions will extend into "no" and "not applicable" calls (same source), the harder judgments.

### 2.3 Maturity spread

- **Tier 1: global networks.** Platform-wide agentic AI announced or rolled out across tens of thousands of staff; firm-run training programmes (EY global training programme; Deloitte AI Academy and tutor mode) (EY-CANVAS-2026; DELOITTE-OMNIA-2026). IFIAR's view of networks is that monitoring of tool quality impact and certification varies and that firms hold many tools but few are used on most audits (IFIAR-TTF-2025). The FRC's thematic review of certification at the six largest UK firms found most had processes, some less mature and undocumented (landscape FRC-ATT-2025; not re-opened).
- **Tier 2: large national and mid-tier.** Grant Thornton US built or adapted its own platform (gtap, from Grant Thornton Ireland) and RSM licensed a vendor (Andera) (GT-GTAP-2026; ANDERA-RSM-2026). These firms are in or near the private-equity wave: Grant Thornton US operates under an alternative practice structure, with attest in the licensed CPA firm and non-attest in a separate advisory entity (GT-GTAP-2026, boilerplate).
- **Tier 3: small and mid-size practices.** 75% without a documented plan, a quarter to a third using no AI, 22% with no automated solution, and a profile of using Excel, Power BI and basic automation (CPACOM-ATR-2025, pp.3-4, 10-11). Blockers named by firms are staff training, client data quality, system access and budget (CPACOM-ATR-2025, p.8). Thomson Reuters's own executives say adoption "has not been at the pace that many expected" because auditors are conservative (TR-STATE-2026, Q6). `vendor interview`.
- **New entrants.** AI-native regulated firms (Repodo in Denmark, Oath Verified in the US) and holding companies investing in audit firms (Modus) exist as announced starts, not as measured market share (REPODO-2026; AT-PEEC-2026; MODUS-2026). Repodo says onboarding is "slated for 2026" with a waitlist open (REPODO-2026), and Modus has invested in one top-200 firm and deployed "seven AI workflows" in it, per Lightspeed (MODUS-2026).
- **Gap between tiers is also a regulatory concern.** The FRC created an "Unlocking barriers to audit tech" project because of challenges smaller firms face (FRC-SANDBOX-2026). Christina Ho (Oath Verified; an interested party) argues the AICPA's draft independence rules could favour large firms that build AI in-house over firms that must license it (AT-PEEC-2026).

### 2.4 Disruption scenarios: who forecasts what

All items in this table are forecasts or positions, not measurements. "Interest" is my note on the speaker's stake.

| # | Scenario | Forecast or position | By whom | Interest | Date | Ref |
|---|---|---|---|---|---|---|
| F1 | **End-to-end AI audit** | "Expected to support all end-to-end audit activities by 2028"; "AI in all phases" now | EY (firm release) | Selling its audit and AI-assurance services | 7 Apr 2026 | EY-CANVAS-2026 |
| F2 | **End-to-end AI audit** | End-to-end automation "within calendar year 2026", then one global agentic platform "within the next year and a half after that" | PwC US assurance transformation leader | Same | 28 Oct 2025 | PWC-AT-2025 |
| F3 | **Agentic audit model** | Agents "increasingly orchestrate audit activity, continuously assess risk and adapt procedures"; public-company audits on gtap "next year" | Grant Thornton US | Same; also owned by a PE investor | 7 May 2026 | GT-GTAP-2026 |
| F4 | **Continuous assurance and full-population testing** | SOX moves from periodic, sample-based to "continuous, automated, and increasingly predictive"; "a more broad-based shift" to full-population assurance that "will represent one of the most significant advances in audit methodology" since computerised accounting; "AI as the subject of the audit" becomes a new mandate; AI-related material weaknesses avoided so far, "that may not last" | KPMG (SOX 2030 point of view) | Sells SOX, internal audit and AI-assurance advice | 24 Sep 2026 | KPMG-SOX-2026, pp.4, 6, 9 |
| F5 | **Subscription / continuous audit repricing** | Two camps: fees should stay roughly unchanged because humans must verify; or AI supports "continuous assurance, not cheaper assurance", possibly a subscription "Audit as a Service" | Verdantix analyst, reporting views of "risk practitioners" | Analyst; sells research | 10 Feb 2026 | VERDANTIX-KPMGFEE-2026 |
| F6 | **Firm-level change** | Three strategic paths for tax and audit firms: "elevate", "scale", "reimagine" (replace periodic compliance with continuous, proactive support) | Thomson Reuters Institute | Sells professional software | 21 Jul 2026 | TRI-FOP-2026 |
| F7 | **Workforce-driven adoption** | "Existential workforce challenge"; "75% of audit partners are scheduled to retire in the next 10 years" (unsourced claim); 2026 "may mark a tipping point" | Thomson Reuters Tax & Accounting executives | Sells audit software | 30 Mar 2026 | TR-STATE-2026 |
| F8 | **AI-native audit firms** | Rebuild audit as an AI-first regulated firm with lower cost and "faster closes, fewer surprises"; "world's first AI-native audit technology for accounting firms" | Repodo founders; Lightspeed (Modus investor) | Venture investors and founders | 25 Aug 2026; 8 Apr 2026 | REPODO-2026; MODUS-2026 |
| F9 | **Standards stay principles-based** | GenAI tools challenge the audit-evidence input-output model; premature to require specific technology procedures; guidance, not requirements | IAASB (explanatory memorandum, ED-500) | Standard-setter position | 5 Aug 2026 | IAASB-ED500-2026, EM paras 67-69 |
| F10 | **AI both improves and erodes audit** | AI can "analyze entire populations"; also risks eroding skepticism and junior skill-building; PE capital can finance AI but "profitability" may outweigh quality | PCAOB acting chair George Botic (Dec 2025 remarks) | Regulator | 9 Dec 2025 (per landscape C3; report page undated in extract) | CAALLEY-PCAOBPE-2025 |
| F11 | **Independence reset** | OCA reviewing independence rules because PE is investing in firms and "both companies and audit firms are adopting AI to reduce costs"; "nothing could be further from the truth" that rules are being weakened | SEC Chief Accountant Kurt Hohl | Regulator | 4 Jun 2026 | TR-HOHL-2026 |
| F12 | **404(b) stays valuable** | Attestation provides "meaningful investor protection"; "technology-driven complexity increases the need for robust controls and independent oversight" | CAQ (audit-firm trade body) | Represents public-company audit firms | 20 Jul 2026 | CAQ-404-2026 |
| F13 | **AI-assurance demand** | "AI assurance is becoming essential"; the question has moved from "Does it work?" to "Can we explain and defend it?" | EY (SOC conference highlights) | Sells AI assurance | Sep 2026 | EY-SOC-2026 |
| F14 | **AI-assurance quality gap** | Accreditation of AI-assurance providers lags the standards; the UK government counted 84 specialised AI assurance suppliers in 2024 versus 17 in 2023 | Cloud Security Alliance research note (AI-assisted; not CSA-reviewed per the landscape) citing UK DSIT | Industry body; low authority | 27 Sep 2026 | CSA-AIASSURE-2026 |
| F15 | **Legal-structure challenge** | Licensing an AI audit tool may or may not raise an independence conflict under the AICPA's alternative-practice-structure draft; a vendor could "sit on both sides of the engagement" | Christina Ho (Oath Verified chief assurance officer; ex-PCAOB board); Accounting Weekly commentary | Interested party; opinion piece | 31 Aug 2026; 1 Sep 2026 | AT-PEEC-2026; ACCWEEKLY-INDEP-2026 |

### 2.5 Scope and value of the audit: regulatory changes

**SOX 404(b) and the SEC's filer-status proposal.**
- On 19 May 2026 the SEC proposed to collapse five filer categories into two (large accelerated and non-accelerated) and raise the large-accelerated-filer float threshold from $700 million to $2 billion; comments were due 20 Jul 2026 (UNIQUS-FILER-2026).
- Per the SEC fact sheet as reported by Uniqus: the share of reporting companies classed as large accelerated filers would fall from 35.4% to 19.2%; non-accelerated filers would rise from 51.9% to 80.8% (UNIQUS-FILER-2026, table "The Numbers That Matter"). Uniqus states that, on the SEC's own analysis, about half of currently attested issuers would leave the 404(b) regime. The 80.8% is a share of reporting companies that would be non-accelerated, not a share losing attestation (the pilot verification report made the same correction). I did not reach the SEC fact sheet itself (sec.gov returned 403).
- A five-year on-ramp would keep newly public companies out of large-accelerated-filer status for 60 months regardless of float (UNIQUS-FILER-2026, table).
- The CAQ's comment letter supports simplification in principle, opposes the five-year exemption for new public companies "regardless of size", and says "technology-driven complexity increases the need for robust controls and independent oversight" (CAQ-404-2026).
- A Texas CPA society committee supports the proposal while noting concern about reduced 404(b) scope; it says companies still subject to attestation would represent about 95% of US public market capitalisation, and that PCAOB inspections of internal-control audits at smaller companies are often "disproportionately rigorous and costly" (TXCPA-FILER-2026).
- I found no source that links the proposal to AI, and none that estimates its effect on audit-firm revenue (see Gaps). Status: proposal, not final, as of 16 Oct 2026.
- The interaction is a scenario, not a finding: AI-driven continuous testing could be cheap enough to make 404(b)-style assurance viable for a wider set of companies, or the proposal could remove demand before that happens. No source I opened analyses this.

**EU sustainability assurance scope (CSRD Omnibus).**
- Directive (EU) 2026/470 was published in the Official Journal on 26 Feb 2026. Recitals say the scope change is to undertakings with a net turnover over EUR 450,000,000 and more than 1,000 employees on average; the Commission's deadline to adopt limited-assurance standards moves to 1 July 2027; and the empowerment to adopt reasonable-assurance standards by 1 Oct 2028 is removed "to avoid an increase in the costs of assurance" (EURLEX-2026-470, recitals on Art. 26a, scope and dates; Art. 26a(3)).
- A recital also says it would be "disproportionate" to apply the full financial-audit approval requirements to firms that only carry out sustainability assurance (EURLEX-2026-470, recital on Art. 3 of Directive 2006/43/EC), which lowers the entry barrier for non-audit assurance providers.
- Secondary reports that Wave 2 would have brought about 1,700 Irish companies into scope under the old thresholds, and that IAASA reported 17 Wave 1 entities with seven firms giving limited assurance for the first time, come from a low-authority news site that also contains a statement about a "pathway to reasonable assurance by 2028" that conflicts with the Directive text (GREENAWARDS-2026). Treat as leads.
- The result is a smaller, capped-at-limited-assurance sustainability assurance market. No source I opened reports AI use by sustainability assurance providers (see Gaps).

**Audit-evidence and technology standards.**
- IAASB's exposure drafts of ISA 500, 330 and 520 (5 Aug 2026; comments due 15 Dec 2026) explicitly decline a technology requirement: "premature to determine a single workable model", because "in some cases it may not be possible to fully evaluate the appropriateness of inputs" to GenAI-enabled tools (IAASB-ED500-2026, EM para 68, p.20). Guidance is said to be the better means (para 69). Final standards are not before 2027 (inference; landscape FS1).
- AICPA's practice aid on AI considerations for financial statement auditors (13 Oct 2026) has two parts: the entity's use of AI, and the firm's own use of AI; later additions are planned on risk of material misstatement and audit evidence (AICPA-PA-2026; JOFA-AIPA-2026).
- The PCAOB's inspections approach is moving to a firm-system-of-quality-control model; staff materials say roughly 90% of registration and inspection data is unstructured and describe early AI pilots to support inspection work (STARLING-IMC-2026). These are staff discussion drafts, not Board decisions (same source).
- The FRC published generative and agentic AI guidance on 30 Mar 2026 (landscape FRC-GENAI-2026, not re-opened) and opened an Audit Tech and AI Sandbox on 4 Jun 2026, open to UK audit firms "of all sizes", with the FRC stating it will not endorse products (FRC-SANDBOX-2026).

**Independence and ownership.**
- AICPA PEEC took its alternative-practice-structure revisions to a second exposure draft (comments to end Aug 2026; October interim meeting) (AT-PEEC-2026). The 81 comment letters on the first draft included none from technology companies, per Christina Ho (AT-PEEC-2026).
- SEC OCA is revisiting independence rules and says the review starts with refreshed independence FAQs (TR-HOHL-2026).
- AAA issued a 2026 call for papers on how private equity affects audit practice, noting PE sees accounting firms as targets for "predictable revenue" and "technology/talent investment needs" (AAA-PE-2026).
- Accountancy Europe counted 385 PE-related transactions involving accountancy and audit firms in Europe in 2025, of which 139 (36%) involved audit firms, and 497 in Jan 2025-Apr 2026 (ACCTEU-PE-2026, "market overview"). The paper does not discuss AI. PE capital is relevant to disruption because it funds technology, but this source does not show that.
- PCAOB leadership noted PE "can be used to ... finance investments in technologies including AI" and warned that profitability may shift ahead of audit quality (CAALLEY-PCAOBPE-2025).

### 2.6 Demand shift: assurance over AI

- **Assurance over AI governance and controls** is being packaged by the Big Four.
  - EY: a "suite of assurance services for audit and non-audit clients spanning AI diagnostics, governance, risk management, and controls" (EY-CANVAS-2026), and a 2026 SOC conference organised around AI assurance (EY-SOC-2026).
  - KPMG UK: a service giving independent confidence that AI governance is "embedded, controlled and ready for scrutiny", with the framing "AI Assurance is shifting from policy to proof" (KPMGUK-GOVAI-2026).
  - Deloitte: an AI Assurance offering "to assess and advise on governance" of AI controls, outputs, data integrity and model performance (DELOITTE-OMNIA-2026).
  - These are service descriptions, not revenue; I found no disclosed volume, fee or client count for any of them.
- **Certification of AI by third parties** is developing: KPMG LLP announced on 27 Aug 2026 that its own agentic platform "aIQ Capture" achieved AIUC-1 certification after more than 900 technical tests, building on an ISO 42001 certification (AIUC-KPMG-2026). `vendor-published` (AIUC). It shows a Big Four firm as a client of AI assurance and AI-certification providers, not as the provider.
- **Client-side demand signals.** Audit partners see immature client AI governance (BOARDMEMBER-CAQ-2026), and the AICPA's practice aid tells auditors to consider AI-operated controls, service-organisation reports and team competence in acceptance (AICPA-PA-2026). KPMG forecasts that ICFR programmes will extend to AI systems (KPMG-SOX-2026, p.6).
- **SOC reporting.** EY's conference poll (multiple answers allowed; sample size not stated) of how participants use AI in SOC work: evidence collection 63%, updating Section 3 (system description) 45%, drafting management responses to deviations 41%, project management 29% (EY-SOC-2026, chart). `self-reported`; conference attendees at an EY event.
- **Market-structure risk.** The CSA research note (a lead; low authority) says AI-assurance suppliers grew faster than accreditation can vet them, and cites a UK government market study (DSIT, Nov 2024) of 17 specialised suppliers in 2023 and 84 a year later, in an ecosystem of 524 firms (CSA-AIASSURE-2026, intro). I did not open the DSIT study.
- **Sustainability assurance demand** is regulated by scope, not by AI (section 2.5). No assurance-provider adoption data was found.

### 2.7 Pricing and the economics of audit

- **Measured by surveys:** 74% of the CPA.com firms listed increasing fees among anticipated growth strategies; 89% expect revenue growth in the next three years; the median audit-practice revenue growth was 8% (CPACOM-ATR-2025, p.9). 33% listed "add technology to create capacity to take on more clients" (same chart). `self-reported`, small sample.
- **KPMG's fee argument.** Verdantix (10 Feb 2026) writes that KPMG "reportedly argued" in discussions with its auditor, Grant Thornton UK, that AI rollout should make parts of audit cheaper and be reflected in fees (VERDANTIX-KPMGFEE-2026). A news aggregator citing the Financial Times (reported on 16 Feb 2026, a date that conflicts with Verdantix's earlier post) gives a drop from $416,000 (2024) to $357,000 (LDS-KPMGFEE-2026); MYCPE describes a 14% fee drop (MYCPE-KPMGFEE-2026). I could not open the FT article. The figures are second-hand and for one small audit of a Big Four firm's own accounts. Treat as an anecdote and an early signal, not a trend.
- **Firm-side view.** PwC's US leader says the audit product is "what it is" and the time saving is "an evolution", with efficiencies expected to grow "in subsequent years" (CFODIVE-PWC-2026).
- **Firms' metrics.** Only 13% of CPA.com firms track the share of engagements on value-billing agreements, while 87% track realization and 76% billable hours (CPACOM-ATR-2025, p.22). The report says traditional metrics such as realization "may begin to lose meaning" as AI shortens tasks (p.22).
- **Product pricing signal.** Thomson Reuters included its Disclosure Review in Guided Assurance at no additional cost (TR-DISCLOSURE-2026). One data point on how vendors price AI features into existing subscriptions.
- **Inputs to the cost side.** KPMG's SOX survey shows testing hours per control rose from 12 to 16 and SOX control cost rose 45% between survey waves (KPMG-SOX-2026, p.4). That is client-side cost growth that firms and vendors say AI can offset (forecast, not shown).

### 2.8 AI-native audit firms and platforms

- **Modus** (announced 8 Apr 2026): $85M seed and Series A led by Lightspeed; "invest in and partner with audit-first accounting firms"; launched Jun 2025; has invested in one top-200 firm and "deployed seven AI workflows" in it (per Lightspeed) (MODUS-2026). The structure (a technology company investing in audit firms) is the type the AICPA's alternative-practice-structure draft addresses (AT-PEEC-2026); no source opened says how Modus is structured legally.
- **Repodo** (Denmark): EUR 8.2M pre-seed led by Hedosophia and Seed Capital; a licensed auditor on the founding team can issue statutory opinions; SME audits first; "onboarding is slated for 2026"; the article notes the firm "would carry professional liability" for opinions, "unlike a software supplier" and that whether clients and supervisors will trust a young technology-first firm remains "an open question" (REPODO-2026).
- **Oath Verified** (US): venture-backed assurance firm using an alternative practice structure; raised about $10M; its chief assurance officer is a former PCAOB board member (AT-PEEC-2026).
- **Fieldguide:** platform from planning through reporting for audit and advisory firms; $75M Series C on a $700M valuation, led by Goldman Sachs Alternatives Growth Equity (FIELDGUIDE-2026).
- **Benchmark provenance.** The FinancialAuditBench preprint lists authors including Pranav Pillai and Arush Jain, the names given for Modus co-founders in the Accounting Today article (ARXIV-FAB-2026; MODUS-2026). I did not confirm affiliations on the preprint page; if the match is real, the benchmark comes from an interested vendor, though it reports a mixed result.
- **What is not shown:** market share, audit-opinion volumes, quality outcomes or regulatory inspection results for any AI-native firm. Repodo's and Modus's own statements are the only evidence.

---

## 3. What it means for an AI transformation conversation

### 3.1 Implications

1. **Use the three-way distinction in every conversation.** What is *measured* (regulators see AI tools mostly in journal-entry testing and risk assessment; small firms mostly automate foot-and-proof, confirmations and trial-balance import), what is *announced* (agent platforms at the Big Four and some mid-tier firms), and what is *forecast* (end-to-end by 2028, continuous assurance by 2030). A leader who treats the last two as the first will over-invest or panic.
2. **The disruption most likely to reach a firm first is structural, not technological.** Ownership (PE and alternative practice structures), independence rules for tool vendors, and scope changes (404(b), CSRD) are moving faster and with more primary-source evidence than AI-driven fee compression. A transformation plan should name them next to AI.
3. **Small and mid-size firms are mostly at the data and basics stage.** Their stated blockers are staff training, client data and budget, not model capability (CPACOM-ATR-2025, p.8). A plan for these firms starts with a documented transformation plan (the thing 75% lack) and the highest-adoption steps, not agents.
4. **The scope of the audit is not shrinking because of AI, but the market for it may shrink through regulation.** If the SEC proposal is adopted as proposed, roughly half of attested issuers would leave 404(b), whatever the technology does (UNIQUS-FILER-2026). That changes the economics of controls-testing investment, which is where several firms' agents are aimed (KPMG-CLARA-2025; OPTRO-CRX-2026).
5. **New work is being created on the other side.** Clients' AI governance is immature (BOARDMEMBER-CAQ-2026), regulators and standard-setters tell auditors to consider AI-operated controls (AICPA-PA-2026), and AI-assurance products are being launched. These are forecasts of demand, backed only by supply-side announcements so far.
6. **Pricing is the question leaders are least prepared for.** Only 13% of surveyed firms track value-billing share (CPACOM-ATR-2025, p.22); the first public AI-based fee argument was made by a Big Four firm to its own auditor (VERDANTIX-KPMGFEE-2026). A firm that cannot say what it would charge for the same opinion with half the hours is exposed.
7. **Quality and supervision costs may offset time savings.** IFIAR reports 31% of members found tools not used as intended (IFIAR-TTF-2025), and PwC says savings are "not that drastic yet" (CFODIVE-PWC-2026). Regulators are asking firms to monitor quality impact, not just adopt.

### 3.2 Interview probes

For a managing partner or firm leader:
1. "Which steps of your audit does a tool now perform on most engagements, and which are still pilot? How do you know the tool is used as intended?" (Measured use versus announced; IFIAR 31% finding.)
2. "Do you have a documented transformation plan with owners, budget and metrics? What do you measure to know it worked?" (75% have none; 83% measure only time savings.)
3. "If a client asked for a lower fee citing AI, what would you say, and what evidence would you show?" (Pricing; KPMG case.)
4. "How many of your audited entities would no longer need an ICFR audit if the SEC proposal is adopted, and what would replace that revenue?" (404(b).)
5. "What share of your clients have an AI governance framework you could rely on? What work do you do when they do not?" (Assurance demand; CAQ 6% advanced.)
6. "Are you licensing AI tools from vendors who also serve your audit clients? Has anyone reviewed that for independence?" (AT-PEEC-2026; ACCWEEKLY-INDEP-2026.)
7. "Where would a junior learn the judgment that tools now do?" (PCAOB remarks; TRI-FOP-2026 on early-career roles.)

For an internal audit leader:
8. "Which controls are tested by an agent, what is the re-performance rate, and who signs off?" (Reddit vendor claim; Gartner low confidence.)
9. "Is your SOX testing cost per control going up or down?" (KPMG 12 to 16 hours.)

### 3.3 Objections and evidence-based responses

| Objection | Response from the evidence |
|---|---|
| "The Big Four have already automated the audit; we cannot compete." | The announcements are platform roll-outs and roadmaps; PwC's own leader says time savings are "not that drastic yet" and the report looks the same (CFODIVE-PWC-2026). IFIAR sees most tool use concentrated in a few areas and few tools used on most audits (IFIAR-TTF-2025). Competitive risk is real but the evidence is of capability, not measured cost advantage. |
| "AI will make audit fees collapse." | The evidence is one reported fee reduction in KPMG's own audit (second-hand) and analyst debate; no survey I found measures realised AI-linked fee changes. Surveyed small firms expect to raise fees (CPACOM-ATR-2025, p.9). Both directions remain forecasts. |
| "Regulators will block AI in audit." | None of the regulators opened prohibits AI. The FRC issued guidance and a sandbox; the IAASB chose guidance over a requirement; the PCAOB's acting chair called AI's potential to transform audits real while warning on skepticism (FRC-SANDBOX-2026; IAASB-ED500-2026; CAALLEY-PCAOBPE-2025). The binding constraints are quality monitoring, independence and human oversight. |
| "AI-native firms will take our clients." | They exist and are funded (Modus, Repodo, Oath Verified), but they are starting with SME or private-company audits, report no market share, and face professional liability and independence rules still being drafted (REPODO-2026; AT-PEEC-2026). Watch them; do not assume them. |
| "The audit is going away, replaced by continuous assurance." | That is KPMG's and the Verdantix camp's forecast; PwC says the product is unchanged; the IAASB says the technology is too early for requirements; CAQ argues 404(b) remains valuable (KPMG-SOX-2026; CFODIVE-PWC-2026; IAASB-ED500-2026; CAQ-404-2026). Statutory audits and 404(b) attestations are legally mandated; continuous monitoring is first-line and internal-audit work in KPMG's own framing (KPMG-SOX-2026, p.10 on the three lines of defense). |
| "Our clients are not asking for AI." | The CAQ survey says audit committees raise AI first (two-thirds), but audit partners rate client AI governance as mostly early or developing (BOARDMEMBER-CAQ-2026). TR's survey reports rising client expectations for AI-enabled quality, among its own respondents (TRI-FOP-2026). The demand is for governance and quality evidence, not necessarily for tools. |
| "AI assurance is a gold mine." | Offers are launched by all Big Four-type firms but no volume or fee data is public; accreditation and standards are still maturing; the AICPA SOC guidance is TQA-based with no new criteria (landscape R21; CSA-AIASSURE-2026). Treat as growing supply with unproven demand size. |

---

## 4. Frontier signals

| Date | Signal | Type | Ref |
|---|---|---|---|
| 26 Feb 2026 | Directive (EU) 2026/470 published: CSRD scope narrowed; reasonable-assurance standard-setting empowerment removed; limited-assurance standards due by 1 Jul 2027 | regulatory (adopted) | EURLEX-2026-470 |
| 2 Feb 2026 | Fieldguide raises $75M at a $700M valuation | funding | FIELDGUIDE-2026 |
| 10 Feb 2026 | Reported KPMG argument that AI should lower its own audit fee; Verdantix calls it a "pricing inflection point" | pricing signal (second-hand) | VERDANTIX-KPMGFEE-2026 |
| 7 Apr 2026 | EY embeds agents in all phases of Canvas; end-to-end by 2028 expected | firm announcement | EY-CANVAS-2026 |
| 8 Apr 2026 | Modus raises $85M to invest in audit firms and build AI-native audit technology | funding / structure | MODUS-2026 |
| 7 May 2026 | Grant Thornton US launches gtap; public-company audits "next year" (2027) | firm launch | GT-GTAP-2026 |
| 19 May 2026 | SEC proposes filer-status overhaul (roughly half of attested issuers out of 404(b) if final) | regulatory proposal | UNIQUS-FILER-2026 |
| 4 Jun 2026 | FRC opens Audit Tech and AI Sandbox and a smaller-firm technology-barriers project | regulator | FRC-SANDBOX-2026 |
| 4 Jun 2026 | SEC Chief Accountant: independence review driven by PE and AI adoption; no weakening | regulator | TR-HOHL-2026 |
| 24 Jun 2026 | Deloitte unifies agents in Omnia for nearly 85,000 practitioners | firm launch | DELOITTE-OMNIA-2026 |
| 15 Jul 2026 | CAQ pulse: nearly 90% of audit partners see client AI governance as developing or early stage | survey | CAQ-PULSE-2026 |
| 20 Jul 2026 | CAQ comment letter opposes broad 404(b) exemption; cites technology-driven complexity | position | CAQ-404-2026 |
| 5 Aug 2026 | IAASB exposure drafts: technology-related requirements premature; comments due 15 Dec 2026 | standard-setter | IAASB-ED500-2026 |
| 25-26 Aug 2026 | Repodo AI-built audit firm announced; RSM and Andera control-testing alliance | entrants / mid-tier | REPODO-2026; ANDERA-RSM-2026 |
| 27 Aug 2026 | KPMG's own agentic platform certified under AIUC-1 | AI-assurance market | AIUC-KPMG-2026 |
| 31 Aug 2026 | AICPA PEEC independence draft: ambiguity over licensing AI audit tools; second exposure draft expected after the October 2026 meeting | independence | AT-PEEC-2026 |
| 23 Sep 2026 | Thomson Reuters Disclosure Review: 30% of eligible customers use it; no added fee | vendor / pricing | TR-DISCLOSURE-2026 |
| 24 Sep 2026 | KPMG "Future of SOX 2030": continuous, 100%-coverage testing and a mandate to assure AI systems | forecast | KPMG-SOX-2026 |
| 26 Sep 2026 | FinancialAuditBench preprint: agents do much staff-level work but sometimes use inappropriate procedures | benchmark | ARXIV-FAB-2026 |
| 7 Oct 2026 | PwC: savings "not that drastic yet"; global agentic platform still to come | firm statement | CFODIVE-PWC-2026 |
| 13 Oct 2026 | AICPA AI practice aid for financial statement auditors; evidence and risk sections to follow | standard-setter | AICPA-PA-2026 |
| 14 Oct 2026 | Optro extends autonomous testing beyond SOX; vendor-reported Reddit result | vendor | OPTRO-CRX-2026 |
| 6-7 Nov 2026 | WCARS 75th symposium (continuous auditing, AI governance and assurance) | event | WCARS-2026 |
| 15 Dec 2026 | IAASB ED comment deadline; QC 1000 and ISA 620 revisions take effect (landscape) | scheduled | IAASB-ED500-2026 |
| 2027 | Grant Thornton public-company audits on gtap (firm plan); Commission limited-assurance standards due 1 Jul 2027 | scheduled / planned | GT-GTAP-2026; EURLEX-2026-470 |
| 2028 | EY end-to-end audit AI (EY forecast) | forecast | EY-CANVAS-2026 |
| 2030 | KPMG SOX 2030 horizon | forecast | KPMG-SOX-2026 |

---

## 5. Sources

Access codes: `full` = page or PDF opened and the relevant parts read; `search-only` = seen in a search result or carried from the landscape and not opened. The first block was opened in this task. "Landscape" marks items cited only through the landscape file.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| EY-CANVAS-2026 | EY launches enterprise-scale agentic AI to redefine the audit experience for the AI era | EY (EY Canada newsroom) | firm | https://www.ey.com/en_ca/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era | 7 Apr 2026 (page carries no explicit date in the text; date from the CPA Practice Advisor copy and page metadata) | full |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 22 Apr 2025 | full |
| DELOITTE-OMNIA-2026 | Deloitte unveils connected agentic intelligence in Deloitte Omnia | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 24 Jun 2026 | full |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://www.accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 28 Oct 2025 | full |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 7 Oct 2026 | full |
| GT-GTAP-2026 | Grant Thornton launches gtap to transform audit delivery across U.S. practice | Grant Thornton US | firm | https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us | 7 May 2026 | full |
| ANDERA-RSM-2026 (landscape key RSM-BEACON-2026) | Andera and RSM US partner to create AI-enabled control testing platform for internal audit | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/ | 26 Aug 2026 | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (Audit Benchmark Survey) | AICPA and CPA.com | professional body / survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | Dec 2025 (survey Jun-Aug 2025) | full |
| IFIAR-TTF-2025 | Use of technology in the audit: observations, risks and further evolution | IFIAR (copy hosted by Japan FSA) | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 27 Mar 2025 | full |
| CAQ-PULSE-2026 | Audit Partners See Companies Moving Forward with Greater Intent... CAQ Survey Finds | Center for Audit Quality | professional body / survey | https://www.thecaq.org/audit-partners-see-companies-moving-forward-with-greater-intent-as-evolving-risks-reshape-strategy-caq-survey-finds | 15 Jul 2026 | full |
| BOARDMEMBER-CAQ-2026 | What audit partners are seeing on AI and what it means for audit committees | Corporate Board Member | press | https://boardmember.com/what-audit-partners-are-seeing-on-ai-and-what-it-means-for-audit-committees/ | Jul 2026 (exact day not seen) | full |
| MODUS-2026 | Modus raises $85M to invest in audit firms, tech | Accounting Today | press | https://www.accountingtoday.com/news/modus-raises-85m-to-invest-in-audit-firms-tech | 8 Apr 2026 | full |
| REPODO-2026 | Former Lunar execs to launch AI-enabled audit firm Repodo after securing new funding | Crowdfund Insider | press | https://www.crowdfundinsider.com/2026/08/302190-former-lunar-execs-to-launch-ai-enabled-audit-firm-repodo-after-securing-new-funding/ | Aug 2026 (25 Aug per landscape) | full |
| FIELDGUIDE-2026 | Fieldguide raises $75M on $700M valuation to scale agentic AI for audit and advisory firms | SiliconANGLE | press | https://siliconangle.com/2026/02/02/fieldguide-raises-75m-700m-valuation-scale-agentic-ai-audit-advisory-firms/ | 2 Feb 2026 | full |
| GARTNER-2026 | Gartner survey shows audit departments are embracing AI and data analytics to drive innovation in 2026 | Gartner | analyst / survey | https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-01-27-gartner-survey-shows-audit-departments-are-embracing-ai-and-data-analytics-to-drive-innovation-in-2026 | 27 Jan 2026 | full |
| TRI-FOP-2026 | What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey / vendor | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 21 Jul 2026 | full |
| TR-STATE-2026 | The state of AI in audit in 2026: interview with experts | Thomson Reuters Tax and Accounting | vendor | https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/ | 30 Mar 2026 | full |
| TR-DISCLOSURE-2026 | Turning disclosure review from manual matching into AI-assisted confidence | Thomson Reuters | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/ | 23 Sep 2026 | full |
| VERDANTIX-KPMGFEE-2026 | What goes around comes around: KPMG's AI-driven fee argument raises uncomfortable questions about audit pricing models | Verdantix | analyst | https://www.verdantix.com/venture/blog/what-goes-around-comes-around--kpmg-s-ai-driven-fee-argument-raises-uncomfortable-questions-about-audit-pricing-models | 10 Feb 2026 | full |
| LDS-KPMGFEE-2026 | KPMG seeks reduced audit fees citing AI | Let's Data Science (news aggregator citing the Financial Times) | press (low authority) | https://letsdatascience.com/news/kpmg-seeks-reduced-audit-fees-citing-ai-da4dbd49 | cites FT of 16 Feb 2026 | full |
| MYCPE-KPMGFEE-2026 | How a Big Four audit fee cut raises a bigger AI question | MYCPE One | press (low authority) | https://my-cpe.com/insights/news-and-insights/accounting-and-taxes/how-a-big-four-audit-fee-cut-raises-a-bigger-ai-question | 2026 (day not seen; page mostly paywalled) | full (summary lines only) |
| KPMG-SOX-2026 | The Future of SOX: 2030 and beyond (point of view) | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf | 24 Sep 2026 (per landscape) | full |
| KPMGUK-GOVAI-2026 | Independent confidence in how you govern AI | KPMG UK | firm | https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html | 2026 (undated) | full |
| ARXIV-FAB-2026 | FinancialAuditBench: Benchmark construction under differential privacy using real-world priors (arXiv 2609.32835) | arXiv | academic preprint | https://arxiv.org/abs/2609.32835 | 26 Sep 2026 | full (abstract) |
| OPTRO-CRX-2026 | Optro launches domain-trained agents for audit, compliance, third-party risk and AI governance | Optro | vendor | https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance | 14 Oct 2026 | full |
| DATASNIPPER-2026 | DataSnipper delivers $1.4B in productivity savings in 2025 | DataSnipper | vendor | https://www.datasnipper.com/resources/datasnipper-delivers-1-4b-in-productivity-savings-in-2025-as-audit-and-finance-enter-the-ai-era | 14 Jan 2026 | full |
| MINDBRIDGE-ARA-2026 | MindBridge advances financial oversight for the agentic era with new platform capabilities | MindBridge (via BNN Bloomberg) | vendor | https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/ | 22 Sep 2026 | full |
| UNIQUS-FILER-2026 | What the SEC's filer status overhaul means for ICFR governance | Uniqus | firm (advisory) | https://uniqus.com/what-the-secs-filer-status-overhaul-means-for-icfr-governance/ | 4 Jun 2026 | full |
| CAQ-404-2026 | Comment letter to the SEC on simplification of filer status | Center for Audit Quality | professional body | https://www.thecaq.org/comment-letter-to-the-sec-on-simplification-of-filer-status | 20 Jul 2026 | full (summary page; letter PDF not opened) |
| TXCPA-FILER-2026 | PSC comments on SEC proposal to streamline public company filer status | Texas Society of CPAs | professional body | https://www.tx.cpa/news/latest-news/news/article/2026/07/16/psc-comments-on-sec-proposal-to-streamline-public-company-filer-status | 16 Jul 2026 | full |
| EURLEX-2026-470 | Directive (EU) 2026/470 (CSRD/CSDDD omnibus amendments) | EUR-Lex, Official Journal of the EU | regulator (legislation) | https://eur-lex.europa.eu/eli/dir/2026/470/oj/eng | 26 Feb 2026 | full |
| GREENAWARDS-2026 | CSRD Omnibus I reshapes Ireland's sustainability reporting landscape | Green Awards (Ireland) | press (low authority) | https://greenawards.ie/news/csrd-omnibus-i-reshapes-irelands-sustainability-reporting-landscape-and-opens-the-2026-2027-planning-window | 2026 (day not seen) | full |
| IAASB-ED500-2026 | Explanatory memorandum, exposure draft proposed ISA 500 (Revised) | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf | 5 Aug 2026 | full (section 1-F) |
| AICPA-PA-2026 | AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing | AICPA and CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 13 Oct 2026 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | Oct 2026 | full |
| AT-PEEC-2026 | AICPA weighs PE and tech impact on audit independence | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules | 31 Aug 2026 | full |
| ACCWEEKLY-INDEP-2026 | AI audit tools and the independence gap nobody fixed | Accounting Weekly | press (opinion; low authority) | https://www.accountingweekly.com/trending-news/ai-audit-tools-and-the-independence-gap-nobody-fixed | 1 Sep 2026 (per landscape) | full |
| TR-HOHL-2026 | SEC Chief Accountant Hohl dispels rumors of weakening auditor independence rules | Thomson Reuters Tax and Accounting | press | https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/ | Jun 2026 (speech 4 Jun 2026) | full |
| CAALLEY-PCAOBPE-2025 | PCAOB warns auditors about AI and PE | CAalley | press | https://caalley.com/news-updates/international-news/pcaob-warns-auditors-about-ai-and-pe | Dec 2025 (page undated in extract; remarks at AICPA conference 8-10 Dec 2025) | full |
| AAA-PE-2026 | Call for papers: Current Issues in Auditing, private equity impact on auditing | American Accounting Association | professional body | https://aaahq.org/portals/0/documents/calls/2026/CIIA%20PE%20and%20Audit%20Firms.pdf | 2026 (undated) | full |
| ACCTEU-PE-2026 | Private equity in European accountancy and audit firms: market update Jan 2025-Apr 2026 | Accountancy Europe | professional body | https://accountancyeurope.eu/wp-content/uploads/2026/05/260629-Private-equity-investment-in-accountancy-and-audit-sector-in-EU-from-January-2025-to-April-2026.pdf | Jun-Jul 2026 | full |
| FRC-SANDBOX-2026 | FRC invites firms and companies to experiment, innovate and reduce burdens through new sandbox programmes | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/06/frc-invites-firms-and-companies-to-experiment-innovate-and-reduce-burdens-through-new-sandbox-programmes/ | 4 Jun 2026 | full |
| ICAEW-FRCSME-2026 | FRC sets out next steps for SME audit | ICAEW | professional body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/mar-2026/frc-sets-out-next-steps-for-sme-audit | Mar 2026 | full |
| STARLING-IMC-2026 | Modernizing US PCAOB audit inspections | Starling Insights | press | https://insights.starlingtrust.com/content/observations/modernizing-us-pcaob-audit-inspections | 1 Sep 2026 (per landscape) | full |
| ICAEW-PIERPOINT-2025 | Testing Gen AI platforms: can they do audit work? | ICAEW | professional body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | Sep 2025 | full |
| EY-SOC-2026 | How AI assurance builds trust with SOC, attestation and certification (conference highlights) | EY | firm | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf | Sep 2026 | full |
| AIUC-KPMG-2026 | KPMG LLP becomes first Big Four firm with AIUC-1 certified AI capability | AIUC | vendor | https://aiuc.com/updates/kpmg-llp-becomes-first-big-four-firm-with-aiuc-1-certified-ai-capability | 27 Aug 2026 | full |
| CSA-AIASSURE-2026 | Who assures the assurers? Third-party AI assessment standards (research note) | Cloud Security Alliance Labs | professional body (low authority) | https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/ | 27 Sep 2026 | full (the AI-generation disclaimer the landscape reports was not visible on the web page) |
| ISACA-PULSE-2026 | AI use accelerates while governance and ROI lag, says new ISACA research | ISACA | professional body / survey | https://isaca.org/about-us/newsroom/press-releases/2026/ai-use-accelerates-while-governance-and-roi-lag-says-new-isaca-research | 5 May 2026 | full |
| WCARS-2026 | 75th World Continuous Auditing and Reporting Symposium | Rutgers | conference | https://raw.rutgers.edu/75wcars.html | 6-7 Nov 2026 (event) | full (page has little text; not used for claims beyond the date) |
| FERF-AUDITFEE-2026 | FERF 16th annual audit fee survey (FY2024 data) | Financial Executives Research Foundation | professional body / survey | https://www.financialexecutives.org/About-FEI/For-the-Press/2026/ferf-16th-annual-audit-fee-survey-2024-insights.aspx | 2026 | search-only (403) |
| BDO-CSRD-2025 | Navigating CSRD reporting and the Omnibus | BDO | firm | https://www.bdo.com/insights/sustainability-and-esg/navigating-csrd-reporting-and-the-omnibus-what-companies-should-know | 2025 (proposal stage) | full (superseded by EURLEX-2026-470; not used for claims) |
| FRC-GENAI-2026; FRC-ATT-2025; KPMG-HOHL-2026; DART-SECPCAOB-2025; IAASB-ISSA5000-2026; TR-PCAOBPLAN-2026; CAQ-RSM-2026 | cited only through the landscape | various | various | see landscape | various | landscape only |

---

## 6. Gaps

**Not found or not reachable.**
- Independent measurement of AI tool accuracy, error rates, override rates or audit-quality effect in live audits (none found for any firm).
- Measured change in audit hours, fees, staffing mix or margins attributable to AI at any firm; the nearest are PwC's qualitative "not that drastic yet" and a second-hand KPMG fee anecdote.
- Smaller-firm adoption data beyond the 54-firm CPA.com survey. The FRC's SME market-study report and its technology findings were not opened (search result and ICAEW summary only). I also found no non-US equivalent of the CPA.com benchmark.
- Non-Big-Four audit-AI platform detail for BDO, Forvis Mazars, Baker Tilly, Crowe and similar: no audit-specific launches were found (consistent with the landscape).
- Any study of how the SEC filer-status proposal changes audit-firm revenue, or of its interaction with AI; the SEC fact sheet itself (sec.gov 403) and the CAQ comment letter PDF were not opened.
- FERF's audit-fee survey (FY2024 data; search extract says a third of respondents are reconsidering auditor relationships and a median S&P 500 audit fee of $7.96M); the page returned 403, so none of it is used above.
- South Korea's regulator's statement that average listed-company audit fees fell for four consecutive years (a search-result extract only); not opened and not used.
- The Financial Times article behind the KPMG fee story (paywalled); the $416,000 to $357,000 figures appear only on an aggregator, and the dates conflict (Verdantix 10 Feb, aggregator citing FT 16 Feb).
- Sustainability assurance providers' use of AI; the Verdantix ESG assurance Green Quadrant and Reuters Events preparer survey (landscape items) were not re-opened.
- Disclosed audit-specific AI investment for KPMG, Deloitte, Grant Thornton and RSM; revenue or client counts for any AI-assurance service.
- The UK DSIT AI-assurance market study (cited via the CSA note only).
- Whether KPMG delivered the controls-testing agents it said would arrive within 12 months of Apr 2025; a headline in the landscape (Bloomberg Law, 1 Apr 2026) suggests a next phase but was not opened.

**Conflicts and cautions in the data.**
- CPA.com's own report says non-AI use is "nearly one-quarter", "approximately one-fourth" and "approximately one-third" in different places (CPACOM-ATR-2025, pp.3, 4, 11). Use "a quarter to a third".
- CPA.com's survey is a convenience sample of 54 firms and its authors say it is not representative.
- IFIAR figures measure regulators' frequency of seeing a tool, from 42-49 members per row; they do not measure the share of audits using a tool.
- "Piloting or using" (Gartner 83%) combines pilots and production.
- The TR Institute and Thomson Reuters figures come from a software vendor; DataSnipper, Optro and Fieldguide are vendors; Modus and Repodo statements are from interested founders or investors.
- The "75% of audit partners will retire within 10 years" claim is quoted from a vendor executive with no source (TR-STATE-2026).
- The FinancialAuditBench author list contains names matching the Modus co-founders; affiliation not confirmed on the preprint page.
- Dates: the EY release does not state its date in the page text I extracted (7 Apr 2026 comes from the CPA Practice Advisor copy and the landscape); Modus's Accounting Today article is dated 8 Apr 2026 (the landscape said 7 Apr); the EY SOC highlights and KPMG UK page are undated beyond month or year.
- Greenawards.ie says a "pathway to reasonable assurance by 2028" remains, which contradicts the Directive text that removes the requirement to adopt reasonable-assurance standards; the primary text governs.
- RSM and Andera's platform is described by its press copy as for internal audit functions; the landscape listed it as a control-testing platform without that qualifier.

**Not covered by this angle (belongs to module work).** Controls-testing detail, FRC and IFIAR quality-management specifics, acceptance and independence tool detail, SOC TQA 9561 content and the AI-in-audit use cases themselves.
