# Module deep dive: professional-services / firm-finance. Angle: governance & evidence

Prepared 2026-10-19. Method: `curl` and `pdftotext` on 45 pages and files read in full, a text mirror (r.jina.ai) for pages that blocked `curl` (Clio, the Law Society), and 7 rationed web searches; the search budget then ran out. Two sources are search-only (the ABA Formal Opinion 512 text, which returned HTTP 403, and a Law360 headline). Quotations are under 25 words. Public sources only. In-house examples are tagged `in-house`.

## 1. Summary

**What constrains and measures the work in firm finance.** The binding constraints are bar fee rules, client AI terms, ownership and independence rules, and professional-indemnity insurance. The measures are mostly surveys by organizations that sell AI products or research. No independent measurement of AI's effect on rates, realization, margin or partner income was found.

- **Fee rules are clear on hourly billing and split on flat fees.** California, Texas and DC say an hourly bill must reflect time actually spent, so time saved by AI cannot be billed (CALBAR-GENAI-2026, p. 8; TXBAR-OP705-2025; DCBAR-388-2024). On flat fees, ABA Formal Opinion 512 is quoted as saying the same flat fee may be unreasonable when a tool makes work much faster, while Virginia's March 2025 committee draft disagrees (VSB-LEO1901-2025, pp. 2-3).
- **AI costs have a billing rule.** California treats general AI subscriptions as overhead and allows matter-specific AI costs only at actual cost, disclosed in the fee agreement, with no markup without informed written consent (CALBAR-GENAI-2026, p. 8). Some vendors are moving from seats to consumption (NONBILLABLE-2026), which turns overhead into a per-matter cost question.
- **Clients want matter-level proof of savings and firms cannot yet give it.** At Legalweek 2026, firm speakers described ROI measurement as anecdotal; Thomson Reuters said firms with a GenAI strategy are 3.9 times more likely to achieve ROI and only 22% have one (TRI-LEGALWEEK-2026).
- **Rates and profit are moving apart.** Q1 2026 Am Law 100 worked-rate growth was almost 10%, yet the LFFI sat at its long-run average of 55 (TRI-LFFI-Q1-2026). Thomson Reuters Institute warns that rate rises justified by AI without visible client value are exposed (TRI-SOTLM-2026).
- **Outside capital is moving through an ethics rulebook.** The AICPA's ethics committee asked for comment in December 2025 on independence rules for private-equity-backed firms, with comments due 30 April 2026 (NYSSCPA-APS-2025). Crowe, which said it would separate attest and non-attest services, closed a KKR investment in August 2026 (AT-CROWE-KKR-2026; AT-CROWE-2026). Arizona had 114 active non-lawyer-ownership licences at the end of 2024 (AZ-ABS-2025).
- **Insurance is a stated blocker for agentic AI.** The Law Society's study reports that professional indemnity insurance rarely covers AI-related mistakes (LAWSOC-AGENTIC-2026, p. 45).
- **Evidence is thin.** Of 18 use cases, none reaches grade A: 4 are B, 8 are C, 6 are D (ideas). Every outcome figure is self-reported or vendor-published except the Arizona licence counts.

**Count by grade:** A 0, B 4, C 8, D 6 (labelled "idea"). In-house: 1 entry (18).

## 2. Use cases

Source locators for PDFs use the PDF page; for web pages they name the section. Evidence grade reflects this module only. Where an outcome comes from an adjacent process, it is noted and capped.


```yaml
- id: professional-services-firm-finance-01
  title: "Pre-bill fee-compliance check for AI-assisted work: hours billed match time spent, AI charges classed as overhead or matter cost, flat fees tested for reasonableness"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ review-assurance, data-reporting ]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Bar opinions agree that an hourly bill must reflect time actually spent, but they differ on whether a flat fee has to come down when AI shortens the work, and on how AI tools may be charged. A billing partner has to apply these rules matter by matter, and across states."
  solution: "Idea: a review step before invoicing that flags matters where AI was used, checks hourly entries against time actually spent (including time spent refining and checking AI output), classes any AI charge as general overhead or a matter-specific cost, and prompts a reasonableness review of flat and alternative fees. The regulator texts set the duty; no firm or vendor was found describing this check."
  outcomes:
    - { lever: risk, description: "none published. The sources set rules and report no measured result of a compliance check.", figure: "none published", measures: "not applicable: idea", provenance: independent, source_ref: CALBAR-GENAI-2026 }
  prerequisites:
    - "Firm policy on which AI tools are general overhead and which are billed to a client, and fee-agreement wording that says how AI costs are charged (CALBAR-GENAI-2026, p. 8)"
    - "A record of which matters used AI tools. ILTA says tracking and compliance tools for work-product governance are in use at fewer than one in five firms (ILTA-TECHSURVEY-2026, p. 9)"
  risks_and_guardrails:
    - "California: hourly billing must reflect time actually spent; general office AI subscriptions typically count as overhead; matter-specific AI costs must reasonably reflect actual cost, with no markup or profit element without the client's informed written consent (CALBAR-GENAI-2026, p. 8)"
    - "Texas Opinion 705 says a lawyer may not charge hourly fees for time 'saved' by using AI, and that per-use AI fees will generally not be recoverable above the amount actually incurred and paid (TXBAR-OP705-2025, Fees section)"
    - "DC Opinion 388 says that, absent a different fee arrangement, a lawyer can bill only for the time the lawyer spent (DCBAR-388-2024, Part E)"
    - "States differ on flat fees. Virginia's draft opinion quotes ABA Formal Opinion 512 as saying it may be unreasonable to charge the same flat fee when a tool makes the work much faster, and then disagrees, concluding that charging the same non-hourly fee is not per se unreasonable (VSB-LEO1901-2025, pp. 2-3). North Carolina says a flat fee may be appropriate if it is not clearly excessive and the client consents, but a lawyer may not bill on the 'time-value represented' by the end product (NCBAR-FEO1-2024, billing inquiry). The Virginia text is a March 2025 committee draft and its final status was not confirmed"
    - "Thomson Reuters Institute argues Opinion 512 may leave clients room to seek to reopen a flat fee that was agreed as reasonable (TRI-ABA512-2025)"
  human_checkpoints:
    - "Billing partner judges reasonableness of flat and alternative fees (CALBAR-GENAI-2026, p. 8)"
    - "Client informed written consent before any markup on matter-specific AI costs (CALBAR-GENAI-2026, p. 8)"
  role_evolution: "No source describes how billing-partner or finance roles change for this check."
  evidence_grade: D
  sources:
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)", publisher: "State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC)", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05, access: full, locator: "p. 8, 'Charging for Work Produced by Generative AI and Generative AI Costs'" }
    - { ref: TXBAR-OP705-2025, title: "Opinion 705", publisher: "Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics)", type: professional-body, url: "https://www.legalethicstexas.com/resources/opinions/opinion-705/", date: 2025-02, access: full, locator: "Fees section" }
    - { ref: DCBAR-388-2024, title: "Ethics Opinion 388: Attorneys' Use of Generative Artificial Intelligence in Client Matters", publisher: "District of Columbia Bar", type: professional-body, url: "https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388", date: 2024, access: full, locator: "Part E, Fees" }
    - { ref: NCBAR-FEO1-2024, title: "2024 Formal Ethics Opinion 1: Use of Artificial Intelligence in a Law Practice", publisher: "North Carolina State Bar", type: professional-body, url: "https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/", date: 2024-11-01, access: full, locator: "inquiry on billing a client for AI-assisted work" }
    - { ref: VSB-LEO1901-2025, title: "Legal Ethics Opinion 1901 (committee draft): Reasonable Fees and the Use of Generative Artificial Intelligence", publisher: "Virginia State Bar, Legal Ethics Committee", type: professional-body, url: "https://vsb.org/common/Uploaded%20files/docs/032725-prop-leo-1901.pdf", date: 2025-03-20, access: full, locator: "pp. 2-3, Analysis under Rule 1.5(a)" }
    - { ref: TRI-ABA512-2025, title: "Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it?", publisher: "Thomson Reuters Institute", type: press, url: "https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512", date: 2025-04-02, access: full, locator: "article body, fee discussion" }
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: "American Bar Association, Standing Committee on Ethics and Professional Responsibility", type: professional-body, url: "https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf", date: 2024-07-29, access: search-only, locator: "fee section; text not opened (HTTP 403). Quoted only as it appears in VSB-LEO1901-2025 and TRI-ABA512-2025" }
    - { ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: "International Legal Technology Association", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "p. 9, 'Curtain Call for the Data Center'" }
  last_reviewed: 2026-10-19
  notes: "Labelled idea. The duty is documented by regulators and bars; the pre-bill check is the proposal. ABA Formal Opinion 512 is cited only through two secondary quotations because americanbar.org returned HTTP 403."

- id: professional-services-firm-finance-02
  title: "Matter-level evidence of AI savings, built from AI usage and time records, for client conversations about value"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ data-reporting, client-interaction ]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Clients ask firms to show how AI produces savings on their own matters. At Legalweek 2026, firm speakers said they were still gathering data or relying on conventional wisdom rather than hard evidence (TRI-LEGALWEEK-2026). The ACC and Everlaw survey page says a majority of in-house respondents lack visibility into how their law firms use GenAI and report no tangible cost savings so far (EVERLAW-ACC-2025)."
  solution: "Record which AI tasks ran on a matter and link them to time entries and fees, so a firm can show a client what changed against a comparable baseline. Legora and Laurel announced on 2026-10-13 that Laurel will turn each task a lawyer completes in Legora into a time entry, with client, matter and what was done, for the lawyer to review (LEGORA-LAUREL-2026). The announcement text read here does not describe savings measurement."
  outcomes:
    - { lever: experience, description: "none published. Firm speakers at Legalweek 2026 described ROI measurement as anecdotal or based on conventional wisdom.", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: TRI-LEGALWEEK-2026 }
    - { lever: experience, description: "none published. The survey page states a majority of in-house respondents lack visibility into law-firm GenAI use and see no tangible savings, with no percentage given.", figure: "none published", measures: "not applicable: majority statement without a stated figure", provenance: vendor-published, source_ref: EVERLAW-ACC-2025 }
  prerequisites:
    - "A record that links AI tasks to client, matter and narrative; the Legora-Laurel announcement describes this for work done in Legora (LEGORA-LAUREL-2026)"
    - "A GenAI strategy. Thomson Reuters' Steven Petrie said firms with a GenAI strategy are 3.9 times more likely to achieve ROI than those without, and that only 22% of firms have one (TRI-LEGALWEEK-2026)"
  risks_and_guardrails:
    - "Clients do not speak with one voice: some ask for line-item AI transparency on invoices, while others issue guidelines saying they will not pay for certain services performed by AI (TRI-LEGALWEEK-2026)"
    - "California says a lawyer must consider telling clients about AI use and must follow client instructions or guidelines that restrict it (CALBAR-GENAI-2026, p. 7)"
    - "DLA Piper's Barclay Blair advised firms not to wait for the client to set the terms, and to lead the AI ROI conversation (TRI-LEGALWEEK-2026)"
  human_checkpoints:
    - "The lawyer reviews each drafted time entry (LEGORA-LAUREL-2026)"
  role_evolution: "Greenberg Traurig's Chief Pricing and Innovation Officer and DLA Piper's Senior Managing Director of AI Innovation spoke on these panels, which shows roles that sit between pricing, innovation and client conversations (TRI-LEGALWEEK-2026)."
  evidence_grade: C
  sources:
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "sections on ROI measurement, client demands and billing" }
    - { ref: LEGORA-LAUREL-2026, title: "Legora and Laurel partner to capture the time lawyers spend in Legora as they work", publisher: "Legora", type: vendor, url: "https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work", date: 2026-10-13, access: full, locator: "announcement summary and date; body text limited" }
    - { ref: EVERLAW-ACC-2025, title: "Generative AI's Growing Strategic Value for Corporate Law Departments (Everlaw and Association of Corporate Counsel survey page)", publisher: "Everlaw with the Association of Corporate Counsel", type: survey, url: "https://www.everlaw.com/resources/acc-genai-survey-2025/", date: 2025, access: full, locator: "survey page, section on law-firm GenAI use" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)", publisher: "State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC)", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05, access: full, locator: "p. 7, Communication Regarding Generative AI Use" }
  last_reviewed: 2026-10-19
  notes: "Vendor announcement only; no deployment or measurement. The landscape file reports that a second phase of the Legora-Laurel work will measure AI usage and value; that statement was not visible on the page text read for this file. Pattern is `other`: a measurement-and-reporting loop that links usage data to client value statements."

- id: professional-services-firm-finance-03
  title: "Firm-level tracking of AI spend, adoption and measured benefit against a named AI strategy"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ data-reporting, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Firms are raising technology spending while evidence of return is thin. Thomson Reuters Institute reports law-firm technology spending up 39.3% from 2021 to 2025 (TRI-SOTLM-2026), and only 22% of firms have a GenAI strategy (TRI-LEGALWEEK-2026). Among A&E firms in Deltek's study, 38% report measurable positive business impact from AI (DELTEK-CLARITY-2026)."
  solution: "A recurring review that ties AI spending (licences, usage, platform build) to adoption and to outcome measures that the CFO and board already track. SPI's report page invites firms to tie AI to utilization, margin, revenue per employee and EBITDA (SPI-AI-2026). The sources describe the need and the metrics; none describes a firm's own tracking system."
  outcomes:
    - { lever: cost, description: "Law-firm technology spending rose 39.3% and knowledge-management spending 37.2% from 2021 to 2025.", figure: "39.3% (technology); 37.2% (knowledge management)", measures: "increase in law-firm technology (and knowledge-management) spending in 2025 against 2021 spending, per the report analysis; the article does not give the sample", provenance: vendor-published, source_ref: TRI-SOTLM-2026 }
    - { lever: growth, description: "Thomson Reuters' speaker said firms with a GenAI strategy are 3.9 times more likely to achieve ROI, and that only 22% have a strategy.", figure: "3.9x; 22%", measures: "relative likelihood of achieving ROI for firms with versus without a GenAI strategy; share of firms with a GenAI strategy; both as stated by a Thomson Reuters speaker, with no sample given on the page", provenance: vendor-published, source_ref: TRI-LEGALWEEK-2026 }
    - { lever: quality, description: "Only 38% of A&E respondents reported measurable positive business impact tied to AI use; 39% said it was too early or they were still piloting.", figure: "38%; 39%", measures: "share of A&E respondents (study built on 896 A&E firms) reporting measurable positive business impact tied to AI use; share saying it is too early or still piloting", provenance: vendor-published, source_ref: DELTEK-CLARITY-2026 }
    - { lever: experience, description: "Among professionals whose organization has a named AI strategy, 66% say AI is meeting or exceeding expectations for creating value, and 35% say day-to-day practice does not match the strategy.", figure: "66%; 35%", measures: "share of professionals in firms or departments with a named AI strategy (survey of 1,816 professionals, March-April 2026) saying AI is meeting or exceeding expectations for creating value; share saying day-to-day practice does not match the strategy", provenance: vendor-published, source_ref: TR-FOP-2026 }
  prerequisites:
    - "A named AI strategy that reaches day-to-day practice (TR-FOP-2026, key findings)"
    - "Usage visibility. 34% of professionals say they use AI tools their organization has not sanctioned, which would sit outside any spend or benefit tracking (TR-FOP-2026, key findings)"
  risks_and_guardrails:
    - "Thomson Reuters Institute's analysis says firms using AI mainly to justify higher billing rates, without improving outcomes, would be more exposed if an AI-investment bubble burst (TRI-SOTLM-2026)"
    - "ILTA says the 'high cost of technology' now shares top billing among leadership concerns with security compliance and risk management (ILTA-TECHSURVEY-2026, p. 6)"
  human_checkpoints:
    - "Firm leadership reviews AI spend against the KPIs the CFO and board track (SPI-AI-2026, report description list under 'Use it to')"
  role_evolution: "No source describes role changes for this review."
  evidence_grade: C
  sources:
    - { ref: TRI-SOTLM-2026, title: "State of the US Legal Market 2026 analysis: Will the AI bubble burst? A crucial warning for law firms", publisher: "Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession", type: survey, url: "https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble", date: 2026-01-14, access: full, locator: "sections on technology and knowledge-management spend, and bubble risk" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "section on the strategy gap (Steven Petrie)" }
    - { ref: DELTEK-CLARITY-2026, title: "The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures for Project-Based Businesses", publisher: "Deltek", type: survey, url: "https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/", date: 2026-05-12, access: full, locator: "Key Findings from the 47th Deltek Clarity Architecture & Engineering Report" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-10-16, access: full, locator: "key findings on strategy and shadow AI; survey description" }
    - { ref: SPI-AI-2026, title: "2026 AI in Professional Services Survey / report page", publisher: "SPI Research", type: survey, url: "https://spiresearch.com/reports/2026-ai-professional-services-survey/", date: 2026-07-14, access: full, locator: "report description list: 'Tie AI to the KPIs your CFO and board already track'" }
    - { ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: "International Legal Technology Association", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "p. 6, 'When GenAI Ambition Meets Budget Reality'" }
  last_reviewed: 2026-10-19
  notes: "All figures come from surveys or market commentary by organizations that sell AI products or research (Thomson Reuters, Deltek, SPI). No independent measure of firm-level AI ROI was found. Deltek's companion government-contracting study reports 45% of respondents unclear on AI ROI; those are government contractors, not professional services firms, and are not used as outcomes. Thomson Reuters' 'ROI' basis for the 3.9x figure is not described on the page read."

- id: professional-services-firm-finance-04
  title: "AI to shorten the research and drafting time that gets written down, to raise realization"
  archetype: professional-services
  module: firm-finance
  function: service-delivery
  work_types: [ research-synthesis, document-production, data-reporting ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "Partners write down time that took too long or became too expensive, and Thomson Reuters Institute puts the average partner's own write-downs at about 300 hours a year (TRI-EFFICIENCY-2025). Associates may write off research time that clients are reluctant to pay for (LEXIS-FORRESTER-2025)."
  solution: "Use AI research and drafting tools so tasks that used to be written down take less time and more of the recorded time can be billed. A Forrester Consulting study commissioned by LexisNexis models, for a theoretical large firm, up to 35% of previously written-off research hours becoming billable (LEXIS-FORRESTER-2025). Thomson Reuters Institute's white paper, written with the Chief Legal Operations Officer of Miles & Stockbridge, proposes starting from a revenue-leakage analysis (TRI-EFFICIENCY-2025)."
  outcomes:
    - { lever: growth, description: "In a modelled firm, up to $6.2m of previously written-off fees recovered over 3 years, and as much as 35% of hours previously written off on research can be allocated to billable hours.", figure: "up to $6.2m over 3 years; up to 35%", measures: "modelled recovery of written-off research fees over three years for a theoretical large law firm; modelled share of previously written-off research hours that can become billable; built from interviews with large firms using Lexis+ AI", provenance: vendor-published, source_ref: LEXIS-FORRESTER-2025 }
    - { lever: capacity, description: "Partners and senior associates can save up to 2.5 hours per week on drafting and legal analysis in the model, worth $1.8m over 3 years.", figure: "up to 2.5 hours per week; $1.8m over 3 years", measures: "modelled hours saved per week by partners and senior associates, and modelled gains over three years, for the same theoretical firm", provenance: vendor-published, source_ref: LEXIS-FORRESTER-2025 }
  prerequisites:
    - "A revenue-leakage analysis to find where hours are lost before choosing AI tools (TRI-EFFICIENCY-2025)"
  risks_and_guardrails:
    - "The figures are modelled for a theoretical firm and the study was commissioned by the product vendor (LEXIS-FORRESTER-2025)"
    - "Hourly bills must still reflect time actually spent, including time refining and checking AI output, not time saved (CALBAR-GENAI-2026, p. 8; TXBAR-OP705-2025, Fees section)"
  human_checkpoints:
    - "Partners decide whether to write down time; TRI says they often choose not to bill because the work took too long or became too expensive (TRI-EFFICIENCY-2025)"
  role_evolution: "LexisNexis says partners and senior associates may reallocate part of the saved time to high-value client work (LEXIS-FORRESTER-2025)."
  evidence_grade: C
  sources:
    - { ref: LEXIS-FORRESTER-2025, title: "How AI drives law firm profitability (summary of Forrester Consulting's Total Economic Impact of Lexis+ AI for Large Law Firms)", publisher: "LexisNexis", type: vendor, url: "https://www.lexisnexis.com/community/insights/legal/b/thought-leadership/posts/how-ai-drives-law-firm-profitability", date: 2026-09, access: full, locator: "sections on written-off research hours and senior-attorney drafting time" }
    - { ref: TRI-EFFICIENCY-2025, title: "The AI-driven future of legal efficiency: How can law firms reclaim millions in lost revenue while enhancing client value?", publisher: "Thomson Reuters Institute", type: press, url: "https://www.thomsonreuters.com/en/institute/reports/ai-driven-legal-efficiency-white-paper-2025", date: 2025-04-14, access: full, locator: "article body, billing-inefficiency discussion" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)", publisher: "State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC)", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05, access: full, locator: "p. 8" }
    - { ref: TXBAR-OP705-2025, title: "Opinion 705", publisher: "Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics)", type: professional-body, url: "https://www.legalethicstexas.com/resources/opinions/opinion-705/", date: 2025-02, access: full, locator: "Fees section" }
  last_reviewed: 2026-10-19
  notes: "Customers in the Forrester study are not named. Thomson Reuters sells legal AI, and its 300-hour figure is a baseline from its own billing research (period and sample not stated on the page), not an outcome of AI."

- id: professional-services-firm-finance-05
  title: "Resell or reprice the hours AI saves, and track utilization, margin and revenue per head against them"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ data-reporting, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Time saved by AI does not reach revenue unless the firm decides what happens to it. SPI's report page says AI saves time but few firms turn those hours into revenue, and one chapter is titled 'Every Hour AI Saves Must Be Resold or Repriced' (SPI-AI-2026). Clio's summary of its 2026 solo and small-firm survey says most solo and small firms have not changed pricing since adopting AI (CLIO-SOLO-2026)."
  solution: "Decide in advance how released capacity is used (new work, repricing, or a lower price to a client) and track the result in utilization, margin and revenue per employee. Clio's blog says the fastest-growing firms built a plan for the time AI gives back (CLIO-SOLO-2026). SPI lists utilization, margin, revenue per employee and EBITDA as the KPIs to tie AI to (SPI-AI-2026)."
  outcomes:
    - { lever: growth, description: "Clio's blog says only about a third of solo and small firms using AI have grown revenue from it.", figure: "about one third", measures: "approximate share of solo and small law firms said to have grown revenue from AI, per Clio's blog summary of its 2026 Legal Trends for Solo and Small Law Firms (survey of over 1,700 respondents); the blog does not state the exact denominator", provenance: vendor-published, source_ref: CLIO-SOLO-2026 }
    - { lever: growth, description: "86% of solo firms and 78% of small firms have not changed pricing since they started using AI, against 51% of mid-market and 46% of enterprise firms; 3% of solos and 5% of small firms raised prices.", figure: "86%, 78%, 51%, 46%; 3%, 5%", measures: "share of firms in each size band that have not changed pricing at all since starting to use AI; share of solo and small firms that raised prices to reflect higher-quality AI-assisted work", provenance: vendor-published, source_ref: CLIO-SOLO-2026 }
    - { lever: capacity, description: "SPI's page says 84.8% say AI saves them time; the matching figure for firms saying AI generates revenue is locked on the page.", figure: "84.8%", measures: "share of respondents saying AI saves them time, in SPI's study of 245 firms; the page does not define the denominator beyond the study sample", provenance: vendor-published, source_ref: SPI-AI-2026 }
  prerequisites:
    - "A deliberate plan for the time AI gives back (CLIO-SOLO-2026)"
    - "SPI says profit goes only to firms that have built four foundations; the foundations are named only inside the paid report (SPI-AI-2026)"
  risks_and_guardrails:
    - "Under hourly billing, saved time cannot be billed as if it had been spent (TXBAR-OP705-2025, Fees section; DCBAR-388-2024, Part E)"
    - "Thomson Reuters Institute reports that Am Law 100 profit per FTE grew faster than revenue per FTE in Q2 2026 while Midsize firm productivity kept contracting (TRI-LFFI-Q2-2026), so the capacity question differs by firm size"
  human_checkpoints:
    - "Leadership sets the use of released capacity before rollout, per Clio's advice (CLIO-SOLO-2026)"
  role_evolution: "No source measures role change for finance or pricing staff."
  evidence_grade: C
  sources:
    - { ref: CLIO-SOLO-2026, title: "Why Working Faster Isn't Making Your Solo Practice More Profitable (And What to Do About It)", publisher: "Clio", type: vendor, url: "https://www.clio.com/blog/small-solo-law-firm-profitability/", date: 2026-05-20, access: full, locator: "sections on adoption versus revenue gains and on pricing" }
    - { ref: CLIO-LTR-2026, title: "2026 Legal Trends Report for Solo and Small Law Firms (report landing page)", publisher: "Clio", type: survey, url: "https://www.clio.com/resources/legal-trends/2026-solo-small-firm-report/", date: 2026-05, access: full, locator: "survey description" }
    - { ref: SPI-AI-2026, title: "2026 AI in Professional Services Survey / report page", publisher: "SPI Research", type: survey, url: "https://spiresearch.com/reports/2026-ai-professional-services-survey/", date: 2026-07-14, access: full, locator: "'The headline', 'The Leak', and contents list" }
    - { ref: TXBAR-OP705-2025, title: "Opinion 705", publisher: "Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics)", type: professional-body, url: "https://www.legalethicstexas.com/resources/opinions/opinion-705/", date: 2025-02, access: full, locator: "Fees section" }
    - { ref: DCBAR-388-2024, title: "Ethics Opinion 388: Attorneys' Use of Generative Artificial Intelligence in Client Matters", publisher: "District of Columbia Bar", type: professional-body, url: "https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388", date: 2024, access: full, locator: "Part E" }
    - { ref: TRI-LFFI-Q2-2026, title: "Q2 2026 LFFI: A heavier load, yet a faster crossing", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed", date: 2026-08-10, access: full, locator: "paragraphs on productivity and profit per FTE" }
  last_reviewed: 2026-10-19
  notes: "Clio and SPI sell software or research, and the Clio figures are for small firms, so they cap this entry at C for firm-level finance. SPI's page also reports that 43.6% of projects now use AI, up from 23.1% in 2025; that measures adoption, not finance."

- id: professional-services-firm-finance-06
  title: "Rate and discount decisions tested against measured AI efficiency before the annual rate round"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ expert-judgment, data-reporting ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Worked rates are rising quickly while profit signals follow only in part. In Q1 2026 Am Law 100 worked-rate growth was almost 10% and demand growth 2.7%, yet the LFFI landed at its long-run average of 55 (TRI-LFFI-Q1-2026). Thomson Reuters Institute says most of the growth in fees worked per lawyer came from rate increases, and warns that premium billing tied to AI is sustainable only when clients clearly see added value (TRI-SOTLM-2026)."
  solution: "Idea: use matter-level AI efficiency evidence (see use case 02) when setting standard rates, accepted discounts and AI-related fee language, so that rate rises and AI savings are decided together. Practitioners discuss the tension; no firm describes doing this."
  outcomes:
    - { lever: growth, description: "none published", figure: "none published", measures: "not applicable: idea", provenance: vendor-published, source_ref: TRI-SOTLM-2026 }
  prerequisites:
    - "Matter-level evidence of AI savings (use case 02)"
  risks_and_guardrails:
    - "Large firms in Q1 2026 raised standard rates faster than worked rates, accepting deeper discounts; Midsize firms did the opposite, and their profit growth ran at roughly half the pace of Am Law peers (TRI-LFFI-Q1-2026)"
    - "Clients are arriving with savings mandates while firms' rates averaged more than 7% growth in 2025 (TRI-LEGALWEEK-2026)"
  human_checkpoints:
    - "No source describes a checkpoint"
  role_evolution: "Greenberg Traurig has a Chief Pricing and Innovation Officer, a role that sits next to this decision (TRI-LEGALWEEK-2026)."
  evidence_grade: D
  sources:
    - { ref: TRI-LFFI-Q1-2026, title: "Q1 2026 LFFI: Strong inputs, average output, and the first drops of rain", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output", date: 2026-05-13, access: full, locator: "key insights; 'The segments' strategy split'" }
    - { ref: TRI-LFFI-Q2-2026, title: "Q2 2026 LFFI: A heavier load, yet a faster crossing", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed", date: 2026-08-10, access: full, locator: "paragraph on worked rates in Q2" }
    - { ref: TRI-SOTLM-2026, title: "State of the US Legal Market 2026 analysis: Will the AI bubble burst? A crucial warning for law firms", publisher: "Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession", type: survey, url: "https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble", date: 2026-01-14, access: full, locator: "sections on profit per lawyer, fees worked per lawyer and sticker shock" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "section on rates and savings mandates" }
  last_reviewed: 2026-10-19
  notes: "Labelled idea. The sources document the rate trend and the client tension; none says AI evidence is used in setting rates. Where human_checkpoints says no checkpoint is described, none was found in the sources; that does not mean none exists."

- id: professional-services-firm-finance-07
  title: "Fixed-fee and subscription margin model that includes variable AI cost"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ data-reporting, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Fixed fees and subscriptions move AI savings into firm margin, but AI cost is becoming variable. Baker Donelson's guide says similar-looking prompts can cost very differently depending on model, input size, output length, reasoning effort and agent steps (BD-TOKEN-2026, section 2). Harvey's co-founder said a simple drafting query could cost about $20 in tokens against about $20,000 for agents reviewing 100,000 contracts (NONBILLABLE-2026)."
  solution: "Idea: price each fixed-fee product from a cost-per-matter model that includes AI consumption (model tier, volume, agent steps) alongside lawyer time, and re-run margins when vendor pricing changes. Baker Donelson says at least one major vendor adjusted rates in ten of the last 13 months (BD-TOKEN-2026, section 3). No firm describes its own model."
  outcomes:
    - { lever: cost, description: "none published", figure: "none published", measures: "not applicable: idea", provenance: vendor-published, source_ref: BD-TOKEN-2026 }
  prerequisites:
    - "Usage data by matter and task type (use case 08)"
    - "Contract flexibility on price changes (BD-TOKEN-2026, section 3)"
  risks_and_guardrails:
    - "California allows flat fees that build in AI savings, and says fee agreements should explain how AI factors into rates (CALBAR-GENAI-2026, p. 8)"
    - "North Carolina allows a flat fee if it is not clearly excessive and the client consents (NCBAR-FEO1-2024, billing inquiry)"
    - "ILTACON hallway talk about moving from seat-based to consumption-based AI pricing included the term 'tokengeddon', and vendors did not say much about it (EDISCOVERYTODAY-ILTACON-2026)"
  human_checkpoints:
    - "No source describes a checkpoint for this model"
  role_evolution: "No source describes role change."
  evidence_grade: D
  sources:
    - { ref: BD-TOKEN-2026, title: "AI Tokenomics Guide: Understanding Token-Based AI Pricing for Legal Technology", publisher: "Baker Donelson (Justin Daniels)", type: firm, url: "https://www.bakerdonelson.com/webfiles/Bios/Token-Pricing-Guide-for-Clients-August-2026.pdf", date: 2026-08-20, access: full, locator: "sections 2, 3 and 4" }
    - { ref: NONBILLABLE-2026, title: "The $10 million AI bill is coming. Can law firms explain it?", publisher: "Non-Billable", type: press, url: "https://www.nonbillable.co.uk/news/legal-ai-moves-usage-based-pricing-consumption-harvey-legora", date: 2026-07-09, access: full, locator: "article body, Pereyra quotes" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)", publisher: "State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC)", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05, access: full, locator: "p. 8" }
    - { ref: NCBAR-FEO1-2024, title: "2024 Formal Ethics Opinion 1: Use of Artificial Intelligence in a Law Practice", publisher: "North Carolina State Bar", type: professional-body, url: "https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/", date: 2024-11-01, access: full, locator: "billing inquiry" }
    - { ref: EDISCOVERYTODAY-ILTACON-2026, title: "My Five ILTACON 2026 Takeaways", publisher: "eDiscovery Today (Doug Austin)", type: press, url: "https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/", date: 2026-09-04, access: full, locator: "paragraph on seat-based to consumption-based pricing" }
  last_reviewed: 2026-10-19
  notes: "Labelled idea. The cost drivers are documented; no source shows a firm modelling fixed-fee margin with them. 'tokengeddon' is attributed by the source to a colleague's term."

- id: professional-services-firm-finance-08
  title: "Matter-level metering and allocation of consumption-priced AI costs, with pass-through rules"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ data-reporting, transaction-processing ]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "As legal AI moves to agents, token use rises and some vendors move from per-seat to consumption pricing. Harvey's co-founder said token usage across its platform rose 14 times in six months, and Legora introduced consumption-based pricing for its Agent Pro product (NONBILLABLE-2026). Under seat pricing, a firm could treat AI as overhead; under consumption pricing, cost varies by matter."
  solution: "Use vendor dashboards and usage controls to see AI spend by matter, user and task type, and decide per matter whether the cost stays in overhead or is billed as a matter-specific cost. Legora launched real-time spending dashboards and usage controls with its consumption pricing (NONBILLABLE-2026). Baker Donelson advises clients to ask vendors for itemised token consumption by matter, user or task type, and whether list prices are passed through 1:1 or marked up (BD-TOKEN-2026, section 7). Harvey's co-founder said passing usage costs to clients may become more common (NONBILLABLE-2026)."
  outcomes:
    - { lever: cost, description: "Harvey's co-founder said token usage across its platform increased 14x over six months.", figure: "14x", measures: "increase in token usage across Harvey's legal AI platform over the preceding six months, as stated by Harvey's co-founder on X and reported by Non-Billable; the baseline and unit are not given", provenance: vendor-published, source_ref: NONBILLABLE-2026 }
  prerequisites:
    - "A usage dashboard or itemised report by matter, user or task (BD-TOKEN-2026, section 7)"
    - "Contract terms on model usage, included allowances, overages and price-change rights (BD-TOKEN-2026, section 5)"
  risks_and_guardrails:
    - "California: matter-specific AI costs may be charged only if the fee agreement discloses it, at reasonable actual cost, with no markup without informed written consent (CALBAR-GENAI-2026, p. 8)"
    - "Texas: a lawyer will generally not recover more than the AI provider's amount actually incurred and paid (TXBAR-OP705-2025, Fees section)"
    - "Law360 ran the headline 'Legora's New AI Pricing Model May Usher In Larger Changes' on 2026-06-26; the body is paywalled and was not read (LAW360-LEGORA-2026)"
  human_checkpoints:
    - "Billing partner and client agreement decide whether a cost is passed through (CALBAR-GENAI-2026, p. 8)"
  role_evolution: "Non-Billable reports that firms may begin allocating AI costs to individual matters instead of absorbing them as overhead, which raises the question of whether clients will see the savings (NONBILLABLE-2026)."
  evidence_grade: C
  sources:
    - { ref: NONBILLABLE-2026, title: "The $10 million AI bill is coming. Can law firms explain it?", publisher: "Non-Billable", type: press, url: "https://www.nonbillable.co.uk/news/legal-ai-moves-usage-based-pricing-consumption-harvey-legora", date: 2026-07-09, access: full, locator: "article body; published 2026-07-09 per page metadata" }
    - { ref: BD-TOKEN-2026, title: "AI Tokenomics Guide: Understanding Token-Based AI Pricing for Legal Technology", publisher: "Baker Donelson (Justin Daniels)", type: firm, url: "https://www.bakerdonelson.com/webfiles/Bios/Token-Pricing-Guide-for-Clients-August-2026.pdf", date: 2026-08-20, access: full, locator: "sections 4, 5 and 7" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)", publisher: "State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC)", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05, access: full, locator: "p. 8" }
    - { ref: TXBAR-OP705-2025, title: "Opinion 705", publisher: "Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics)", type: professional-body, url: "https://www.legalethicstexas.com/resources/opinions/opinion-705/", date: 2025-02, access: full, locator: "Fees section" }
    - { ref: LAW360-LEGORA-2026, title: "Legora's New AI Pricing Model May Usher In Larger Changes", publisher: "Law360", type: press, url: "https://www.law360.com/articles/2494404", date: 2026-06-26, access: search-only, locator: "headline and date only" }
  last_reviewed: 2026-10-19
  notes: "Vendor announcements and a firm's guidance for clients. Baker Donelson's guide advises clients on buying; it does not say the firm meters its own AI spend by matter. Vendor list prices in the guide are not reproduced here because they change often."

- id: professional-services-firm-finance-09
  title: "Client AI-terms register applied at bill time: consent, disclosure and billing limits recorded per client"
  archetype: professional-services
  module: firm-finance
  function: risk-compliance-legal
  work_types: [ review-assurance, client-interaction ]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Client guidelines on AI are inconsistent. DLA Piper's Barclay Blair said firms receive some directives that look like 2023 (for example, demands to warrant that models are unbiased, or bans on AI without permission) in the same inbox as demands to use AI to hit savings targets, and some clients say they will not pay for certain services performed by AI (TRI-LEGALWEEK-2026)."
  solution: "Idea: a register of each client's AI requirements (consent, disclosure, approved tools, billing limits) that is checked when work is staffed and again before billing. Everlaw suggests in-house teams put light-touch disclosure requirements into outside counsel guidelines, RFPs or matter kickoffs (EVERLAW-BLOG-2026). No firm describes such a register."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable: idea", provenance: self-reported, source_ref: TRI-LEGALWEEK-2026 }
  prerequisites:
    - "A way to read and structure client guidelines; not described in any source"
  risks_and_guardrails:
    - "California says a lawyer must follow applicable client instructions or guidelines that restrict AI (CALBAR-GENAI-2026, p. 7)"
    - "Firm policies vary by size: 'must obtain client approval' is a current policy at 8% of firms with under 50 lawyers, 20% at 50-149, 24% at 150-349, 38% at 350-699 and 34% at over 700 (ILTA-TECHSURVEY-2026, p. 5, Q3.18)"
  human_checkpoints:
    - "Billing or relationship partner reviews flagged matters before invoicing (inference from CALBAR-GENAI-2026, p. 7)"
  role_evolution: "No source describes role change."
  evidence_grade: D
  sources:
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "section on contradictory client guidelines" }
    - { ref: EVERLAW-BLOG-2026, title: "Setting Expectations for GenAI Usage and Pricing with Outside Counsel", publisher: "Everlaw", type: vendor, url: "https://www.everlaw.com/blog/corporations/setting-expectations-for-genai-usage-and-pricing-with-outside-counsel/", date: 2026-01-29, access: full, locator: "section on disclosure requirements" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)", publisher: "State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC)", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05, access: full, locator: "p. 7" }
    - { ref: ILTA-TECHSURVEY-2026, title: "The ILTA Technology Survey 2026 Executive Summary", publisher: "International Legal Technology Association", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: 2026-06, access: full, locator: "p. 5, table Q3.18" }
  last_reviewed: 2026-10-19
  notes: "Labelled idea. The ILTA percentages measure the share of firms in each lawyer-count band that selected the policy item 'Must obtain client approval' in answering 'which of the following best describe your firm's current official policies or guidance on the use of generative AI tools'. Intapp's Terms product appears in the landscape file as a possible vendor, but its page was not readable, so no vendor claim is made here."

- id: professional-services-firm-finance-10
  title: "Shift the firm's fee mix toward hybrid and outcome-linked pricing as AI weakens the link between hours and effort"
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types: [ expert-judgment, data-reporting ]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "When AI does part of the work, reported hours are a noisier signal of effort. Stanford's paper argues time-based pricing becomes a worse instrument and that clients on time-based contracts may pay for hours that no longer match the work done (STANFORD-DEL-2026, pp. 14-15)."
  solution: "Firms add hybrid contracts (a base fee plus an outcome-linked component) and, where outcomes can be measured and attributed, outcome-based fees. The Stanford paper reports that McKinsey's UK managing partner said in a November 2025 briefing that the firm is doing more performance-based work, and that McKinsey disclosed roughly a quarter of its global fees now come from outcome-based pricing (STANFORD-DEL-2026, p. 14). It also reports PwC's US tax leader saying time is 'becoming less and less of relevance' in pricing conversations, with the firm exploring charging on value and outcomes (STANFORD-DEL-2026, pp. 14-15). A Forrester analyst writes that consultancies have already moved toward putting fees at risk and expects more of it (FORRESTER-BLOG-2025)."
  outcomes:
    - { lever: risk, description: "McKinsey disclosed that roughly a quarter of its global fees come from outcome-based pricing.", figure: "roughly 25%", measures: "share of McKinsey's global fees from outcome-based pricing, as reported by Business Insider (Thompson, 2025) and cited by the Stanford paper; a rough figure reported second-hand", provenance: self-reported, source_ref: STANFORD-DEL-2026 }
  prerequisites:
    - "Measurement infrastructure before outcome pricing: the Stanford paper's third rule says to invest in measurement first, then negotiate outcome-linked pricing (STANFORD-DEL-2026, p. 21)"
    - "Clean attribution of results to the firm's work (STANFORD-DEL-2026, p. 3)"
  risks_and_guardrails:
    - "Attribution risk sets a floor on how informative an outcome signal can be, which caps how far outcome-based pricing can go; where the contribution is confounded, hybrid contracts are the destination (STANFORD-DEL-2026, p. 3)"
    - "Fees are exposed when AI errors reach a deliverable. Deloitte Australia agreed to partially refund an AUD 440,000 payment for a report with apparent AI-generated errors (CTV-DELOITTE-2025)"
    - "The Stanford authors say the framework's fit with observed pricing offers qualitative plausibility, not confirmatory validation, and note a monetary gift from Accenture to the lab not tied to the study (STANFORD-DEL-2026, pp. 1, 5)"
  human_checkpoints:
    - "Executives locate each engagement on the outcome-observability and input-cost-observability map before choosing a pricing structure (STANFORD-DEL-2026, p. 20)"
  role_evolution: "The paper says firms should build hybrid pricing capability as a strategic competence (STANFORD-DEL-2026, p. 22)."
  evidence_grade: B
  sources:
    - { ref: STANFORD-DEL-2026, title: "Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives", publisher: "Stanford Digital Economy Lab (Brynjolfsson) and USC (Petropoulos)", type: academic, url: "https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf", date: 2026-08-23, access: full, locator: "pp. 3, 14-15, 20-22" }
    - { ref: FORRESTER-BLOG-2025, title: "The Future Of AI Consulting Services Is Disruptively Bright", publisher: "Forrester", type: press, url: "https://www.forrester.com/blogs/the-future-of-ai-consulting-services-is-disruptively-bright", date: 2025-09-15, access: full, locator: "fifth position, 'Modify their economic models to share more risk'" }
    - { ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: "CTV News (AP)", type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: 2025-10-07, access: full, locator: "page description and date" }
  last_reviewed: 2026-10-19
  notes: "Grade B: a named firm and a named share, but the McKinsey figure is rough and second-hand, so it cannot reach A. The landscape file lists a different McKinsey figure (about a third) from a secondary summary; not reconciled here. Deal-level pricing choices belong to scoping-pricing; this entry covers the firm-level revenue mix. The Deloitte page body did not load, so only the headline description is used."

- id: professional-services-firm-finance-11
  title: "Productised, subscription-priced services sold on a firm's AI platform (PwC One)"
  archetype: professional-services
  module: firm-finance
  function: product-service-development
  work_types: [ expert-judgment, document-production ]
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "CPA Practice Advisor, summarizing an FT interview, reports that PwC's US CEO said the firm would start to offer alternatives to billing clients by hours worked, as it overhauls its core services and pricing models to protect its business from being undermined by AI (CPAPA-PWC-2026)."
  solution: "PwC launched PwC One, an AI platform giving clients access to six automated services, with more promised, and its US CEO said some tax and consulting services would be converted into AI-powered tools clients could use 'without a PwC person in the loop', potentially paid for on an annual subscription (CPAPA-PWC-2026). The Stanford paper quotes a PwC principal calling PwC One 'a front door into the firm' and notes PwC's announcement stops short of pricing specifics (STANFORD-DEL-2026, p. 15)."
  outcomes:
    - { lever: growth, description: "PwC One was launched with six automated services, with more to be added.", figure: "6", measures: "number of automated services on PwC One at launch, per CPA Practice Advisor's summary of an FT interview with PwC's US CEO; no revenue or usage figure is given", provenance: self-reported, source_ref: CPAPA-PWC-2026 }
  prerequisites:
    - "A platform and automated services ready for client use (CPAPA-PWC-2026)"
    - "Oversight inside the platform: PwC presents it as an environment where AI performs analytical work under professional oversight (STANFORD-DEL-2026, p. 15)"
  risks_and_guardrails:
    - "For law firms, the Law Society's study says solicitors stay responsible for agentic AI outputs they cannot fully audit, and that professional indemnity insurance rarely covers AI-related mistakes (LAWSOC-AGENTIC-2026, p. 45)"
    - "No price, revenue or usage result for PwC One is published in the sources read (CPAPA-PWC-2026; STANFORD-DEL-2026, p. 15)"
  human_checkpoints:
    - "Professional oversight sits inside the platform, per PwC's description (STANFORD-DEL-2026, p. 15)"
  role_evolution: "The CEO said senior staff who were not 'paranoid about being AI-first' would probably be replaced (CPAPA-PWC-2026). Law Society interviewees compared the model to Big Four accounting, where technology is sold alongside services (LAWSOC-AGENTIC-2026, p. 57)."
  evidence_grade: B
  sources:
    - { ref: CPAPA-PWC-2026, title: "PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/", date: 2026-03-25, access: full, locator: "article body" }
    - { ref: STANFORD-DEL-2026, title: "Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives", publisher: "Stanford Digital Economy Lab (Brynjolfsson) and USC (Petropoulos)", type: academic, url: "https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf", date: 2026-08-23, access: full, locator: "p. 15, section 5.2" }
    - { ref: LAWSOC-AGENTIC-2026, title: "Shaping the future of agentic AI in legal practice (full report)", publisher: "Law Society of England and Wales", type: professional-body, url: "https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice", date: 2026-04-14, access: full, locator: "p. 45 (insurance) and p. 57 (productisation)" }
  last_reviewed: 2026-10-19
  notes: "Named deployment, no measured outcome. The CEO's statements are reported second-hand via the FT. Pattern is `other` (service delivered as a product); the Reimagine path in Thomson Reuters' report also names subscription advisory and productized services (TR-FOP-2026, 'Reimagine' path)."

- id: professional-services-firm-finance-12
  title: "Network-funded AI platform and training programme with disclosed spend (PwC)"
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types: [ software-systems, data-reporting ]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Large firms must decide how much to fund AI platforms and training before the return is clear. PwC reported global revenue of $60.2 billion for the fiscal year ending 30 June 2026 (AT-PWC-2026)."
  solution: "PwC firms invested $3 billion across the network to expand capabilities in AI and other key areas. The spend covered the initial rollout of PwC One, continued investment in an AI-native assurance platform, a tax data aggregation and project management platform, and other agentic and data-driven delivery models. More than 330,000 people have taken AI training (AT-PWC-2026)."
  outcomes:
    - { lever: cost, description: "PwC firms invested $3 billion across the network in AI and other key areas in the year.", figure: "$3 billion", measures: "investment by PwC firms across the network to expand capabilities in AI technology and other key areas in the fiscal year ending 30 June 2026, as reported by PwC", provenance: self-reported, source_ref: AT-PWC-2026 }
    - { lever: capacity, description: "More than 330,000 people have taken AI training at PwC.", figure: "330,000+", measures: "people who have taken AI training at PwC, cumulative to the date of the report", provenance: self-reported, source_ref: AT-PWC-2026 }
    - { lever: growth, description: "Global revenue rose 5.7% in US dollars and 3.5% at constant exchange rates. The article reports revenue next to the investment but states no link between them.", figure: "5.7%; 3.5%", measures: "change in PwC global revenue for the fiscal year ending 30 June 2026 against the prior year", provenance: self-reported, source_ref: AT-PWC-2026 }
  prerequisites:
    - "Network-level funding and shared platforms (AT-PWC-2026)"
  risks_and_guardrails:
    - "No return on the $3 billion is published, and the article states no causal link between spend and revenue (AT-PWC-2026)"
  human_checkpoints:
    - "No checkpoint is described in the source"
  role_evolution: "More than 330,000 people have taken AI training (AT-PWC-2026)."
  evidence_grade: B
  sources:
    - { ref: AT-PWC-2026, title: "PwC grows 2026 global revenue to $60.2B", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b", date: 2026-10-19, access: full, locator: "article body" }
  last_reviewed: 2026-10-19
  notes: "Named firm, self-reported spend figure. It is an input, not a measured return, so the entry stays at B. Regional growth and line-of-service growth in the article are not used."

- id: professional-services-firm-finance-13
  title: "Outside capital to fund talent and technology, with attest and non-attest services separated (Crowe and KKR)"
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types: [ expert-judgment, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Firms that want to invest in technology and talent at scale may seek outside capital, and where an attest firm is involved, independence rules constrain how investors relate to it. The AICPA's ethics committee voted on 19 December 2025 to seek comment on changes to its Code for alternative practice structures that involve private equity (NYSSCPA-APS-2025)."
  solution: "Crowe announced a KKR investment on 2026-06-11, with capital to be used on talent, technology and innovation, and said it would separate attest and non-attest services into Crowe LLP and Crowe Advisory LLC, with KKR investing in Crowe Advisory (AT-CROWE-KKR-2026). Accounting Today reports the investment closed in August 2026 and that Crowe then launched CroweONE, a shared ownership plan open to all employees without upfront investment (AT-CROWE-2026). The sources do not name AI as a use of the capital."
  outcomes:
    - { lever: growth, description: "none published for the use of capital; Crowe has not published results of the investment in the sources read.", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: AT-CROWE-KKR-2026 }
    - { lever: growth, description: "In Arizona, which removed its ban on non-lawyer ownership of law firms, 114 alternative business structures were actively licensed at 31 December 2024, and 51 licences were granted in 2024.", figure: "114; 51", measures: "licensed ABSs (non-lawyer ownership regime for legal practice) active at 31 Dec 2024; licences granted in calendar year 2024; 47 of the 51 were traditional law firms", provenance: independent, source_ref: AZ-ABS-2025 }
  prerequisites:
    - "For attest firms, a structure that meets AICPA independence rules; the committee's exposure draft would revise the alternative-practice-structure interpretation, distinguish investor 'significant influence' from 'control', and change the 'network firm' definition (NYSSCPA-APS-2025)"
    - "For legal practice in Arizona, a licence from the Supreme Court on the ABS committee's recommendation (AZ-ABS-2025)"
  risks_and_guardrails:
    - "Comments on the AICPA exposure draft were due 30 April 2026. If approved in 2026, the changes would take effect a year after adoption, with early adoption allowed. Adoption status was not confirmed in the sources read (NYSSCPA-APS-2025)"
    - "Texas Society of CPAs' standards committee supports the proposals and asks for clearer, principle-based guidance that applies consistently across attest services (TXCPA-APS-2026)"
    - "The Arizona report describes the 2020 decision to eliminate Ethical Rule 5.4, which had barred non-lawyer ownership of law firms and fee sharing between lawyers and non-lawyers; the sources read do not say which other states follow this (AZ-ABS-2025, Background)"
  human_checkpoints:
    - "Arizona's ABS committee reviews applications and recommends licensing to the Supreme Court (AZ-ABS-2025)"
  role_evolution: "Crowe says CroweONE lets employees share in the firm's success without upfront investment (AT-CROWE-2026)."
  evidence_grade: B
  sources:
    - { ref: AT-CROWE-KKR-2026, title: "Crowe gets PE investment from KKR", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/crowe-gets-pe-investment-from-kkr", date: 2026-06-11, access: full, locator: "article body" }
    - { ref: AT-CROWE-2026, title: "Crowe launches shared ownership plan (URL slug: crowe-launches-esop-with-kkr-investment)", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/crowe-launches-esop-with-kkr-investment", date: 2026-10-19, access: full, locator: "article body and editorial note" }
    - { ref: NYSSCPA-APS-2025, title: "AICPA Calls for Comments on Ethics Rules Update for Alternative Practice Structures in Private Equity", publisher: "New York State Society of CPAs", type: professional-body, url: "https://nysscpa.org/news/1045198-aicpa-calls-for-comments-on-ethics-rules-update-for-alternative-practice-structures-in-private-equity-2025-12-22", date: 2025-12-22, access: full, locator: "article body" }
    - { ref: TXCPA-APS-2026, title: "PSC Comments on Proposed AICPA Code Revisions Addressing Alternative Practice Structures and Private Equity", publisher: "Texas Society of CPAs", type: professional-body, url: "https://www.tx.cpa/news-publications/news-announcements/article/2026/04/29/psc-comments-on-proposed-aicpa-code-revisions-addressing-alternative-practice-structures-and-private-equity", date: 2026-04-29, access: full, locator: "summary of comment letter" }
    - { ref: AZ-ABS-2025, title: "Annual Report of the Committee on Alternative Business Structures to the Arizona Supreme Court (calendar year 2024)", publisher: "Arizona Supreme Court, Committee on Alternative Business Structures", type: regulator, url: "https://www.azcourts.gov/Portals/0/26/ABS%20Committee%20Annual%20Report%20to%20Supreme%20Court%20for%202024%20(02_28_2025).pdf", date: 2025-04, access: full, locator: "Executive Summary; Background; Applications, Renewals and Licenses" }
    - { ref: ILTA-ILTACON-2026, title: "ILTACON 2026 keynotes (G200 executive session abstract)", publisher: "International Legal Technology Association", type: conference, url: "https://iltacon.org/keynotes", date: 2026-08, access: full, locator: "G200 executive session abstract on private equity, alternative ownership, pricing models and AI commercialization" }
  last_reviewed: 2026-10-19
  notes: "Outside capital is in this module's scope, but this is a capital-structure change, not an AI task, and the sources do not tie the Crowe capital to AI. Correction to the landscape file: Accounting Today's editorial note says CroweONE was first described incorrectly as an employee stock ownership plan, and the KKR deal was announced in June and closed in August. The ILTACON G200 abstract describes a session already held (23-27 August 2026), and is cited only as a signal of the topic."

- id: professional-services-firm-finance-14
  title: "Leverage and partner-economics modelling that assumes AI changes who does the work below equity partners"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ data-reporting, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "The Q2 2026 LFFI shows the ratio of hours worked by non-equity partners to equity partners at its highest since late 2018, with associates and non-equity partners carrying most of the extra workload and generating fees well above their cost. The report does not attribute this to AI (TRI-LFFI-Q2-2026). Law Society interviewees expected top firms to cut staff and support roles and shift toward fixed-fee or subscription models as billable hours erode (LAWSOC-AGENTIC-2026, p. 59)."
  solution: "Idea: scenario models of leverage, billing mix and partner income under different assumptions about how much junior and support work AI takes over. A Forrester analyst notes that diamond-shaped and pod-like structures are being proposed in place of the pyramid (FORRESTER-BLOG-2025). No firm describes using such a model."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none published", measures: "not applicable: idea", provenance: independent, source_ref: TRI-LFFI-Q2-2026 }
  prerequisites:
    - "Timekeeper-level hours, rates and cost data (implied by TRI-LFFI-Q2-2026)"
  risks_and_guardrails:
    - "In an NBER trial of 133 patent lawyers, AI raised the quality of delivered work, but the advantage without AI after three months was concentrated among senior lawyers and junior scores bifurcated (NBER-AUTOR-2026, abstract). This bears on the supply of future partners, not on current economics"
    - "Forrester says consultancies still need a talent pipeline to develop the next generation of expertise (FORRESTER-BLOG-2025)"
  human_checkpoints:
    - "No checkpoint is described"
  role_evolution: "Law Society interviewees said junior lawyers may do less administrative work and more oversight (LAWSOC-AGENTIC-2026, p. 57). Thomson Reuters Institute's report puts the cost at an estimated $232,000 per replacement when professionals who see an AI value gap leave (TR-FOP-2026)."
  evidence_grade: D
  sources:
    - { ref: TRI-LFFI-Q2-2026, title: "Q2 2026 LFFI: A heavier load, yet a faster crossing", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed", date: 2026-08-10, access: full, locator: "paragraphs on demand by title, leverage and expenses" }
    - { ref: LAWSOC-AGENTIC-2026, title: "Shaping the future of agentic AI in legal practice (full report)", publisher: "Law Society of England and Wales", type: professional-body, url: "https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice", date: 2026-04-14, access: full, locator: "p. 59, expected impact by firm type; p. 57" }
    - { ref: FORRESTER-BLOG-2025, title: "The Future Of AI Consulting Services Is Disruptively Bright", publisher: "Forrester", type: press, url: "https://www.forrester.com/blogs/the-future-of-ai-consulting-services-is-disruptively-bright", date: 2025-09-15, access: full, locator: "fourth position, 'Rethink their hiring, development, and organizational models'" }
    - { ref: NBER-AUTOR-2026, title: "Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720)", publisher: "National Bureau of Economic Research (EconPapers record)", type: academic, url: "https://econpapers.repec.org/RePEc:nbr:nberwo:35720", date: 2026-09, access: full, locator: "abstract" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-10-16, access: full, locator: "section on mid-career departures" }
  last_reviewed: 2026-10-19
  notes: "Labelled idea. The NBER trial measures drafting quality and judgment, not firm economics, so it is adjacent evidence; talent effects are routed to talent-learning."

- id: professional-services-firm-finance-15
  title: "Partner and staff performance criteria that include AI adoption"
  archetype: professional-services
  module: firm-finance
  function: people-hr
  work_types: [ expert-judgment, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Partner economics depend on partners changing how they work. PwC's US CEO told the FT that partners who resist AI have no place at the firm and that nobody gets a free pass (CPAPA-PWC-2026)."
  solution: "A firm leader states that adopting AI is a condition of staying at the firm. The source reports the CEO's statements; it does not describe a scorecard, a pay formula or any change to performance criteria. This entry tracks the idea that such statements become changed criteria."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none published", measures: "not applicable: statement of intent", provenance: self-reported, source_ref: CPAPA-PWC-2026 }
  prerequisites:
    - "Professional-grade AI tools that people can use. 41% of professionals who use AI at work lack access to tools that meet their confidentiality, grounding and explainability needs (TR-FOP-2026, key findings)"
  risks_and_guardrails:
    - "From 2 December 2027, high-risk AI systems used for employment and worker management are subject to strict obligations under the EU AI Act (EC-AIACT-2026)"
    - "California flags that AI used in employment actions or screening may present a risk of unlawful or unethical bias (CALBAR-GENAI-2026, p. 9)"
    - "Among professionals who see an AI value gap, 24% are considering leaving within two years (TR-FOP-2026, key findings)"
  human_checkpoints:
    - "No checkpoint is described"
  role_evolution: "TR-FOP reports professionals split their AI priorities between reclaiming time and finding meaning; few rank financial incentives or career advancement first, though the report expects recognition and pay expectations to shift (TR-FOP-2026)."
  evidence_grade: C
  sources:
    - { ref: CPAPA-PWC-2026, title: "PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/", date: 2026-03-25, access: full, locator: "article body" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026-10-16, access: full, locator: "key findings on access, value gap and priorities" }
    - { ref: EC-AIACT-2026, title: "AI Act: regulatory framework for AI (page read 2026-10-19)", publisher: "European Commission", type: regulator, url: "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai", date: 2026-07-27, access: full, locator: "section on high-risk use cases and timeline" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023)", publisher: "State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC)", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026-05, access: full, locator: "p. 9, Prohibition on Discrimination, Harassment, and Retaliation" }
  last_reviewed: 2026-10-19
  notes: "A CEO statement, second-hand via the FT; no scorecard, pay formula or result is published. The percentage in the risks line for 24% measures professionals experiencing an AI value gap who are considering leaving; it is a survey of 1,816 professionals by a vendor of AI."

- id: professional-services-firm-finance-16
  title: "Independent testing and assurance evidence to support insurance cover and client trust for agentic AI"
  archetype: professional-services
  module: firm-finance
  function: risk-compliance-legal
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "The Law Society's study says solicitors remain responsible for agentic AI outputs even though they cannot fully audit them, that professional indemnity insurance rarely covers AI-related mistakes, and that members saw unresolved insurance questions as a key blocker (LAWSOC-AGENTIC-2026, p. 45)."
  solution: "Idea: a firm obtains independent testing and assurance reports on its AI systems and uses them with insurers and clients. The AICPA and the Artificial Intelligence Underwriting Company announced a joint certification that combines SOC 2 and AIUC-1 examinations into one CPA-led engagement; it is being piloted at several CPA firms, including PwC, and is planned for full launch in early 2027 (AT-AIUC-2026). No source says the certification is used to obtain insurance."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable: idea", provenance: independent, source_ref: LAWSOC-AGENTIC-2026 }
  prerequisites:
    - "Clearer standards on testing, auditing and accreditation for agentic AI, which the Law Society report calls urgent (LAWSOC-AGENTIC-2026, executive summary)"
  risks_and_guardrails:
    - "The pilot's customers and scope are not described beyond 'entities' and 'several CPA firms' (AT-AIUC-2026)"
  human_checkpoints:
    - "A CPA-led engagement produces a single report (AT-AIUC-2026)"
  role_evolution: "No source describes role change in the firm's finance function."
  evidence_grade: D
  sources:
    - { ref: LAWSOC-AGENTIC-2026, title: "Shaping the future of agentic AI in legal practice (full report)", publisher: "Law Society of England and Wales", type: professional-body, url: "https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice", date: 2026-04-14, access: full, locator: "p. 45, liability and insurance; executive summary" }
    - { ref: AT-AIUC-2026, title: "New AI assurance certification combines SOC 2, AIUC-1", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/new-ai-assurance-certification-combines-soc-2-aiuc-1", date: 2026-10-19, access: full, locator: "article body" }
  last_reviewed: 2026-10-19
  notes: "Labelled idea for firm finance; the certification itself belongs to the assurance archetype (assurance over AI) and is routed there."

- id: professional-services-firm-finance-17
  title: "AI-native, PE-backed accounting platform with automatic timekeeping, project price recommendations and productivity benchmarking (Ascend)"
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types: [ data-reporting, expert-judgment ]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "Ascend's founder says mix-and-match tool stacks bring many challenges for accounting firms, and that no AI-native product suite can be bought off the shelf because vendors build narrow point solutions (AT-AINATIVE-2026)."
  solution: "Ascend, described as a private-equity-based accounting firm platform with a 30-person AI team, argues for a closed loop in which controlling the whole software layer lets timekeeping happen automatically, productivity be compared across projects, and prices be recommended from scope (AT-AINATIVE-2026). The founder presents these as capabilities of an AI-native design, not as measured results."
  outcomes:
    - { lever: capacity, description: "none published. The founder describes possibilities and reports no measured result.", figure: "none published", measures: "not applicable: descriptive claim by the firm's founder", provenance: self-reported, source_ref: AT-AINATIVE-2026 }
  prerequisites:
    - "Capital to invest, an innovative culture, technology talent, and fast decision-making; the founder says these are more likely in a corporate model than a legacy partnership (AT-AINATIVE-2026)"
  risks_and_guardrails:
    - "The founder says the stack must be secure, scalable and auditable to meet quality management requirements in the profession (AT-AINATIVE-2026)"
  human_checkpoints:
    - "No checkpoint is described in the interview"
  role_evolution: "The founder says the same system could surface who is moving quickly or getting stuck and offer personalised learning (AT-AINATIVE-2026)."
  evidence_grade: C
  sources:
    - { ref: AT-AINATIVE-2026, title: "The AI-native firm (On the Air with Accounting Today, with Ascend founder David Wurtzbacher)", publisher: "Accounting Today", type: podcast, url: "https://www.accountingtoday.com/podcast/the-ai-native-firm", date: 2026-10-19, access: full, locator: "transcript, discussion of AI-native closed loop and critical success factors" }
  last_reviewed: 2026-10-19
  notes: "Founder statements in a podcast transcript (the transcript states it was created by AI). The page metadata date is 2026-10-19. The firm's practice-level deployment status was not independently confirmed."

- id: professional-services-firm-finance-18
  title: "[in-house] Outside counsel guidelines that require AI disclosure and share AI savings, with capped or fixed-fee pilots"
  archetype: professional-services
  module: firm-finance
  function: procurement-supply-chain
  work_types: [ review-assurance, client-interaction ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "In-house teams have little visibility into law-firm AI use and see few savings. The ACC and Everlaw survey of 657 in-house legal professionals reports that a majority lack visibility into how their law firms use GenAI and report no tangible cost savings, and that a majority are ready to push for new pricing models, with nearly half believing their own demand will be the primary driver of change (EVERLAW-ACC-2025)."
  solution: "Everlaw recommends adding light-touch AI disclosure requirements to outside counsel guidelines, RFPs or matter kickoffs, and piloting fixed fees for defined workflows, capped fees, or blended hourly and flat models (EVERLAW-BLOG-2026). Mars Inc's head of legal ops said AI dilutes the time-equals-money calculus and the company expects more leverage to push for fee arrangements tied to outputs and outcomes (EVERLAW-BLOG-2026). GSK's Chief of Staff, Legal and Compliance, said the questions to firms are now what they use, how, and how it generates savings (TRI-LEGALWEEK-2026)."
  outcomes:
    - { lever: cost, description: "Adoption of GenAI for legal work among US respondents more than doubled to 52% in the survey year.", figure: "52%", measures: "share of US respondents to the ACC and Everlaw survey (657 in-house legal professionals globally) using GenAI for legal work, as stated on the survey page; prior-year figure not given", provenance: vendor-published, source_ref: EVERLAW-ACC-2025 }
  prerequisites:
    - "Consistent expectations applied across matters and firms (EVERLAW-BLOG-2026)"
  risks_and_guardrails:
    - "Everlaw cautions that framing GenAI as a demand for immediate discounts may gain less traction than discussing how efficiency changes the mix of work, leverage or predictability (EVERLAW-BLOG-2026)"
    - "Guidelines already in use are inconsistent and sometimes dated (TRI-LEGALWEEK-2026)"
  human_checkpoints:
    - "Disclosure of safeguards and human oversight is one of Everlaw's suggested questions to firms (EVERLAW-BLOG-2026)"
  role_evolution: "The ACC publishes a list of 10 GenAI questions for in-house teams to put to outside firms (EVERLAW-BLOG-2026)."
  evidence_grade: C
  sources:
    - { ref: EVERLAW-ACC-2025, title: "Generative AI's Growing Strategic Value for Corporate Law Departments (Everlaw and Association of Corporate Counsel survey page)", publisher: "Everlaw with the Association of Corporate Counsel", type: survey, url: "https://www.everlaw.com/resources/acc-genai-survey-2025/", date: 2025, access: full, locator: "survey page, sections on law-firm use, adoption and pricing" }
    - { ref: EVERLAW-BLOG-2026, title: "Setting Expectations for GenAI Usage and Pricing with Outside Counsel", publisher: "Everlaw", type: vendor, url: "https://www.everlaw.com/blog/corporations/setting-expectations-for-genai-usage-and-pricing-with-outside-counsel/", date: 2026-01-29, access: full, locator: "sections on transparency and pricing" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "GSK and DLA Piper remarks" }
  last_reviewed: 2026-10-19
  notes: "Tagged in-house: client-side practice (corporate legal departments). The survey is published by a vendor and the page does not state its date; the 2026-01-29 blog calls it a recent survey. The client side of the same tension is covered from the firm side in use cases 02 and 09."
```


## 3. Module notes

### Processes and key steps (with work types)

1. **Annual rate round and discount policy** (expert-judgment, data-reporting): standard rates, accepted discounts and worked rates. Large firms in Q1 2026 raised standard rates faster than worked rates; Midsize firms did the opposite (TRI-LFFI-Q1-2026).
2. **Realization and write-down management** (data-reporting, review-assurance): partners decide whether to bill time that took too long (TRI-EFFICIENCY-2025).
3. **Profitability, leverage and partner economics** (data-reporting, expert-judgment): the Q2 2026 LFFI shows non-equity partner hours relative to equity partner hours at their highest since late 2018 (TRI-LFFI-Q2-2026).
4. **AI investment decisions and ROI tracking** (data-reporting, expert-judgment): technology and knowledge-management spend are among the fastest-growing overhead categories (TRI-LFFI-Q2-2026).
5. **AI cost metering, allocation and pass-through** (data-reporting, transaction-processing): moves from seat-based overhead toward per-matter cost where vendors meter consumption (NONBILLABLE-2026).
6. **Fee compliance and client AI terms** (review-assurance, client-interaction): hourly bills, flat fees and AI charges tested against bar opinions and client guidelines (CALBAR-GENAI-2026, p. 8; TRI-LEGALWEEK-2026).
7. **Capital and ownership structure** (expert-judgment, review-assurance): outside investment and, for attest firms, independence (NYSSCPA-APS-2025).

### Common pain points

- Firms cannot yet show clients matter-level savings; one panelist called the industry "still in the anecdotal phase" of measuring returns (TRI-LEGALWEEK-2026).
- Strong pricing and demand inputs produced only an average LFFI in Q1 2026, with overhead rising and productivity slipping (TRI-LFFI-Q1-2026).
- Saved hours do not become revenue without a plan: SPI says AI saves time but few firms turn the hours into revenue (SPI-AI-2026).
- Cost visibility is a leadership concern: ILTA says the "high cost of technology" now shares top billing with security compliance and risk management (ILTA-TECHSURVEY-2026, p. 6).
- Rules differ by state on flat fees (VSB-LEO1901-2025, pp. 2-3), and a firm with clients in several states must apply the strictest.
- 34% of professionals use AI tools their organization has not sanctioned, so spend and use are partly invisible (TR-FOP-2026).

### Metrics and benchmarks (each with what it measures)

| Metric | Value | What it measures (source's words, shortened) | Provenance | Source |
|---|---|---|---|---|
| LFFI, Q1 2026 | 55 | Composite law-firm financial performance index; equals its long-run average since 2006 | vendor-published | TRI-LFFI-Q1-2026 |
| Am Law 100 worked-rate growth, Q1 2026 | almost 10% (above 12% for the largest firms) | Growth in worked rates; demand growth was 2.7% | vendor-published | TRI-LFFI-Q1-2026 |
| Law-firm technology spend vs 2021 | +39.3% by end-2025 (knowledge management +37.2%) | Increase in spending against 2021 levels | vendor-published | TRI-SOTLM-2026 |
| Profit per lawyer / fees worked per lawyer | +8.4% / +16.8% above pre-2022 levels by end-2025 | Increase over pre-2022 levels, as stated; most of the growth came from rate increases | vendor-published | TRI-SOTLM-2026 |
| Firms with a GenAI strategy | 22%; those with one 3.9x more likely to achieve ROI | Share of firms with a strategy; relative likelihood of achieving ROI | vendor-published | TRI-LEGALWEEK-2026 |
| Professionals with named strategy saying AI meets or exceeds expectations | 66% | Of professionals in firms or departments with a named AI strategy (1,816 surveyed) | vendor-published | TR-FOP-2026 |
| Corporate clients rating AI quality gains very important or essential / saying most providers deliver | 78% / 6% | Corporate clients who buy professional services | vendor-published | TR-FOP-2026 |
| Corporate clients reconsidering firm relationships | 32% | Already reconsidered or planning to within 12 months | vendor-published | TR-FOP-2026 |
| Firms engaged with GenAI | 94% (up 14 points) | Responding firms in a survey of 508 firms | independent (trade association) | ILTA-TECHSURVEY-2026, p. 3 |
| Firms using tracking and compliance tools for work-product governance | fewer than one in five | Firms using sophisticated tracking and compliance tools | independent (trade association) | ILTA-TECHSURVEY-2026, p. 9 |
| A&E firms reporting measurable positive AI impact | 38% (adoption 70%) | Respondents among 896 A&E firms | vendor-published | DELTEK-CLARITY-2026 |
| A&E utilization / operating profit | just under 60% / 16.7% | Reported levels in the 2026 study; not attributed to AI by the source | vendor-published | DELTEK-CLARITY-2026 |
| Solo and small firms that have not changed pricing since adopting AI | 86% / 78% (mid-market 51%, enterprise 46%) | Share of firms in each size band | vendor-published | CLIO-SOLO-2026 |
| In-house GenAI adoption (US) | 52% | Share of US respondents using GenAI for legal work | vendor-published | EVERLAW-ACC-2025 |
| Active ABS licences in Arizona | 114 at 2024-12-31 | Licensed non-lawyer-ownership entities | independent (court committee) | AZ-ABS-2025 |
| MCA weighted 12-month growth outlook | 5.7% (24-month 7.4%) | Weighted growth rate expected by 1,060 surveyed consultants at UK consultancies | independent (trade association) | MCA-SURVEY-2026 |
| Technology consulting spend growth, 2026 | 7.5% (projected) | Source Global Research projection | vendor-published | SOURCE-INSIGHTS-2026 |
| Harvey token usage | 14x in six months | Growth across Harvey's platform, per its co-founder | vendor-published | NONBILLABLE-2026 |
| Token price spread | output 4-6x input; most capable model 10-50x the cheapest from the same vendor | List-price structure of Claude, GPT and Gemini as of 2026-08-20, as stated in the guide | self-reported | BD-TOKEN-2026 |

**Quality and independent measurement.** No error rate, override rate or parallel-run result was found for any firm-finance use of AI (rate setting, realization, forecasting). The only independent measurements that touch the module are adjacent: an NBER randomized trial of 133 patent lawyers found AI raised delivered work quality by 0.34 SD at 10 days and 0.38 SD at 90 days, with the later no-AI advantage concentrated among senior lawyers (NBER-AUTOR-2026, abstract); this is evidence for talent, not for firm finance, and it caps nothing here above B. Fee-at-risk exposure shows up as incidents, such as Deloitte Australia's partial refund (CTV-DELOITTE-2025). Every ROI figure above comes from surveys, vendor-commissioned models or market commentary.

### Guardrails and regulatory points

- **Fees, hourly:** time actually spent only (CALBAR-GENAI-2026, p. 8; TXBAR-OP705-2025; DCBAR-388-2024, Part E; NCBAR-FEO1-2024).
- **Fees, flat or alternative:** California allows flat fees that build in AI savings (CALBAR-GENAI-2026, p. 8); North Carolina allows them if not clearly excessive and the client consents (NCBAR-FEO1-2024); ABA Formal Opinion 512 is quoted as warning that the same flat fee may be unreasonable if a tool makes work much faster (VSB-LEO1901-2025, p. 2; TRI-ABA512-2025); Virginia's draft rejects that reading (VSB-LEO1901-2025, p. 3). ABA 512 itself was not opened.
- **AI costs:** overhead versus matter-specific cost, no markup without informed written consent (CALBAR-GENAI-2026, p. 8); Texas limits recovery to the amount actually incurred (TXBAR-OP705-2025).
- **Client instructions:** California requires following client guidelines that restrict AI (CALBAR-GENAI-2026, p. 7).
- **Agentic AI:** California says lawyers must not let agentic systems make substantive legal determinations or act in a representative capacity without meaningful supervision, and must not permit autonomous external transmission of client information without safeguards and human review (CALBAR-GENAI-2026, pp. 2, 6).
- **Ownership and independence:** AICPA exposure draft on alternative practice structures (NYSSCPA-APS-2025; TXCPA-APS-2026); Arizona ABS regime (AZ-ABS-2025).
- **EU AI Act:** applicable from 2 August 2026, with Annex III high-risk obligations, including AI for employment and worker management, extended to 2 December 2027 (EC-AIACT-2026). Relevant to AI used in staffing or evaluating people.
- **Insurance:** professional indemnity insurance rarely covers AI-related mistakes, per the Law Society's study (LAWSOC-AGENTIC-2026, p. 45).
- **Not reached:** the SRA, the Bar Standards Board, the FRC and the PCAOB pages did not yield AI-and-fees text (see Gaps).

### Frontier signals (dated and sourced)

- **2026-10-19:** AICPA and AIUC announced a joint SOC 2 and AIUC-1 AI assurance certification, piloted at several CPA firms including PwC, with full launch planned for early 2027 (AT-AIUC-2026).
- **2026-10-19:** PwC reported $3 billion invested across the network in AI and other key areas in the year to 30 June 2026 (AT-PWC-2026).
- **2026-10-19:** Crowe launched CroweONE, a shared ownership plan, after the KKR investment closed in August (AT-CROWE-2026).
- **2026-08-23:** Stanford's pricing paper argues AI pushes consulting toward hybrid and asset-based structures (STANFORD-DEL-2026, abstract).
- **2026-08-20:** Baker Donelson published a client guide to token-based AI pricing, noting a shift from flat subscriptions toward usage-based models (BD-TOKEN-2026, section 4).
- **2026-06-26 and 2026-07-09:** Legora introduced consumption-based pricing for Agent Pro; Harvey's co-founder said token use rose 14 times in six months (LAW360-LEGORA-2026, headline; NONBILLABLE-2026).
- **2026-06-11:** Crowe announced the KKR investment (AT-CROWE-KKR-2026).
- **2026-05 (PDF metadata date):** California replaced its 2023 guidance with a version covering agentic AI at the Supreme Court's request (CALBAR-GENAI-2026, executive summary).
- **2026-04-30:** deadline for comments on the AICPA exposure draft; adoption status not confirmed (NYSSCPA-APS-2025).
- **2026-03-25:** PwC's US CEO said some tax and consulting services would be converted to AI-powered tools clients could use without a PwC person in the loop (CPAPA-PWC-2026).
- **2026-03-13:** Legalweek panels on firm and client disagreement over who gains from AI (TRI-LEGALWEEK-2026).
- **Scheduled:** the 25th Annual Law Firm COO & CFO Forum is listed for 21-22 October 2026 (TRI-EVENTS-2026). Its content was not available and supports no grade.

### Workforce and role effects

- Roles appearing at the boundary of pricing, innovation and client value: Greenberg Traurig's Chief Pricing and Innovation Officer and DLA Piper's Senior Managing Director of AI Innovation (TRI-LEGALWEEK-2026).
- Associates and non-equity partners carry most extra demand while equity partner demand slipped (TRI-LFFI-Q2-2026).
- Among professionals who see an AI value gap, 24% are considering leaving within two years, at an estimated $232,000 per replacement (TR-FOP-2026). Routed to talent-learning.
- Law Society interviewees expected top firms to cut staff and support roles and shift toward fixed-fee or subscription models (LAWSOC-AGENTIC-2026, p. 59).
- PwC's US CEO said senior staff who were not "paranoid about being AI-first" would probably be replaced (CPAPA-PWC-2026).

### Objections and concerns practitioners raise

- "Until accuracy and quality improve, it is an expensive toy": an ILTA survey respondent (ILTA-TECHSURVEY-2026, p. 3).
- Rate rises may be seen as a pure pricing move, and a $2,000-an-hour associate rate in a downturn could cause sticker shock (TRI-SOTLM-2026).
- Clients both demand AI use and refuse to pay for AI-done work (TRI-LEGALWEEK-2026).
- ABA 512's flat-fee reasoning could expose agreed fixed fees to buyer's remorse, in Thomson Reuters Institute's view (TRI-ABA512-2025).
- Zarwin Baum's managing director asked whether clients would accept a return to a single line-item "services rendered" bill as itemized hourly detail undersells AI-compressed work (TRI-LEGALWEEK-2026).
- Insurance and liability gaps (LAWSOC-AGENTIC-2026, p. 45).
- Vendors say little about consumption pricing when asked (EDISCOVERYTODAY-ILTACON-2026).
- **In-house:** a corporate legal-ops head said AI dilutes the time-equals-money calculus and expects more leverage to push for outcome-based arrangements (EVERLAW-BLOG-2026).

### Interview probes for an advisor

1. When AI shortens an hourly task, what happens to the time entry and the write-down decision, and which bar opinions or client guidelines does your billing team apply?
2. Can you show one client a matter-level figure for what AI saved, and who in the firm owns that number?
3. Where does AI spend sit today (overhead or matter cost), who watches consumption, and what changes at renewal if the vendor moves from seats to usage?
4. If work below equity partners shrinks, what in leverage, partner income or hiring would you change first, and what data would you need?
5. What ownership, independence or insurance constraint limits how you fund or deploy AI, and who in the firm owns that conversation?

## 4. Routed to other modules

- **scoping-pricing (professional-services):** the Stanford paper's four decision rules for choosing a pricing structure for each engagement (STANFORD-DEL-2026, pp. 20-22); Zarwin Baum's single line-item bill idea (TRI-LEGALWEEK-2026); alternative-fee pilots such as fixed fees for defined workflows (EVERLAW-BLOG-2026).
- **billing-collections (professional-services):** automatic time capture from AI tasks (LEGORA-LAUREL-2026); Clio's realization and flat-fee commentary (CLIO-SOLO-2026); the write-down mechanics in TRI-EFFICIENCY-2025.
- **quality-review (professional-services):** hallucination rates in legal research tools (STANFORD-MAGESH-2024); the Deloitte Australia refund as a review failure (CTV-DELOITTE-2025).
- **talent-learning (professional-services):** the NBER trial on juniors and seniors (NBER-AUTOR-2026); mid-career departure risk and the timeline to trusted judgment (TR-FOP-2026); the pyramid debate (FORRESTER-BLOG-2025).
- **client-development (professional-services):** 78% of corporate clients rate AI quality gains important, 6% say most providers deliver, 32% are reconsidering relationships (TR-FOP-2026).
- **staffing-resourcing (professional-services):** utilization just under 60% in A&E firms (DELTEK-CLARITY-2026).
- **assurance archetype, assurance over AI:** the AICPA and AIUC joint certification (AT-AIUC-2026).
- **assurance archetype, acceptance and independence:** the AICPA alternative-practice-structure independence proposals (NYSSCPA-APS-2025; TXCPA-APS-2026).
- **assurance archetype, finance and accounting work:** a Mercor test of 12 junior CPAs against an AI model on month-end close tasks (AT-MERCOR-2026); not read for its figures.
- **acceptance-risk (professional-services):** California's rules on confidentiality, agentic access to client systems and supervision (CALBAR-GENAI-2026, pp. 5-7).


## 5. Sources

Ref format is PUBLISHER-SHORT-YYYY. Access `full` means the page or file was opened and read; `search-only` means only a headline or quoted passage was seen.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version, replaces Nov 2023) | State Bar of California, Standing Committee on Professional Responsibility and Conduct (COPRAC) | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full |
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools | American Bar Association, Standing Committee on Ethics and Professional Responsibility | professional-body | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 2024-07-29 | search-only |
| TRI-ABA512-2025 | Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it? | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512 | 2025-04-02 | full |
| TXBAR-OP705-2025 | Opinion 705 | Professional Ethics Committee for the State Bar of Texas (hosted by the Texas Center for Legal Ethics) | professional-body | https://www.legalethicstexas.com/resources/opinions/opinion-705/ | 2025-02 | full |
| DCBAR-388-2024 | Ethics Opinion 388: Attorneys' Use of Generative Artificial Intelligence in Client Matters | District of Columbia Bar | professional-body | https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388 | 2024 | full |
| NCBAR-FEO1-2024 | 2024 Formal Ethics Opinion 1: Use of Artificial Intelligence in a Law Practice | North Carolina State Bar | professional-body | https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/ | 2024-11-01 | full |
| VSB-LEO1901-2025 | Legal Ethics Opinion 1901 (committee draft): Reasonable Fees and the Use of Generative Artificial Intelligence | Virginia State Bar, Legal Ethics Committee | professional-body | https://vsb.org/common/Uploaded%20files/docs/032725-prop-leo-1901.pdf | 2025-03-20 | full |
| LAWSOC-AGENTIC-2026 | Shaping the future of agentic AI in legal practice (full report) | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/research/the-future-of-agentic-ai-in-legal-practice | 2026-04-14 | full |
| AZ-ABS-2025 | Annual Report of the Committee on Alternative Business Structures to the Arizona Supreme Court (calendar year 2024) | Arizona Supreme Court, Committee on Alternative Business Structures | regulator | https://www.azcourts.gov/Portals/0/26/ABS%20Committee%20Annual%20Report%20to%20Supreme%20Court%20for%202024%20(02_28_2025).pdf | 2025-04 | full |
| NYSSCPA-APS-2025 | AICPA Calls for Comments on Ethics Rules Update for Alternative Practice Structures in Private Equity | New York State Society of CPAs | professional-body | https://nysscpa.org/news/1045198-aicpa-calls-for-comments-on-ethics-rules-update-for-alternative-practice-structures-in-private-equity-2025-12-22 | 2025-12-22 | full |
| TXCPA-APS-2026 | PSC Comments on Proposed AICPA Code Revisions Addressing Alternative Practice Structures and Private Equity | Texas Society of CPAs | professional-body | https://www.tx.cpa/news-publications/news-announcements/article/2026/04/29/psc-comments-on-proposed-aicpa-code-revisions-addressing-alternative-practice-structures-and-private-equity | 2026-04-29 | full |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026 | full |
| EC-AIACT-2026 | AI Act: regulatory framework for AI (page read 2026-10-19) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-07-27 | full |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab (Brynjolfsson) and USC (Petropoulos) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720) | National Bureau of Economic Research (EconPapers record) | academic | https://econpapers.repec.org/RePEc:nbr:nberwo:35720 | 2026-09 | full |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362) | Stanford RegLab and HAI researchers (Magesh et al.) | academic | https://arxiv.org/abs/2405.20362 | 2024-05 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026-10-16 | full |
| TRI-LFFI-Q1-2026 | Q1 2026 LFFI: Strong inputs, average output, and the first drops of rain | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 | full |
| TRI-LFFI-Q2-2026 | Q2 2026 LFFI: A heavier load, yet a faster crossing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed | 2026-08-10 | full |
| TRI-SOTLM-2026 | State of the US Legal Market 2026 analysis: Will the AI bubble burst? A crucial warning for law firms | Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-EFFICIENCY-2025 | The AI-driven future of legal efficiency: How can law firms reclaim millions in lost revenue while enhancing client value? | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/reports/ai-driven-legal-efficiency-white-paper-2025 | 2025-04-14 | full |
| TRI-EVENTS-2026 | Thomson Reuters Institute events (25th Annual Law Firm COO & CFO Forum listing) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/events | 2026-10-21 | full |
| ILTA-TECHSURVEY-2026 | The ILTA Technology Survey 2026 Executive Summary | International Legal Technology Association | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| ILTA-ILTACON-2026 | ILTACON 2026 keynotes (G200 executive session abstract) | International Legal Technology Association | conference | https://iltacon.org/keynotes | 2026-08 | full |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways | eDiscovery Today (Doug Austin) | press | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures for Project-Based Businesses | Deltek | survey | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| SPI-AI-2026 | 2026 AI in Professional Services Survey / report page | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-07-14 | full |
| CLIO-SOLO-2026 | Why Working Faster Isn't Making Your Solo Practice More Profitable (And What to Do About It) | Clio | vendor | https://www.clio.com/blog/small-solo-law-firm-profitability/ | 2026-05-20 | full |
| CLIO-LTR-2026 | 2026 Legal Trends Report for Solo and Small Law Firms (report landing page) | Clio | survey | https://www.clio.com/resources/legal-trends/2026-solo-small-firm-report/ | 2026-05 | full |
| EVERLAW-ACC-2025 | Generative AI's Growing Strategic Value for Corporate Law Departments (Everlaw and Association of Corporate Counsel survey page) | Everlaw with the Association of Corporate Counsel | survey | https://www.everlaw.com/resources/acc-genai-survey-2025/ | 2025 | full |
| EVERLAW-BLOG-2026 | Setting Expectations for GenAI Usage and Pricing with Outside Counsel | Everlaw | vendor | https://www.everlaw.com/blog/corporations/setting-expectations-for-genai-usage-and-pricing-with-outside-counsel/ | 2026-01-29 | full |
| LEXIS-FORRESTER-2025 | How AI drives law firm profitability (summary of Forrester Consulting's Total Economic Impact of Lexis+ AI for Large Law Firms) | LexisNexis | vendor | https://www.lexisnexis.com/community/insights/legal/b/thought-leadership/posts/how-ai-drives-law-firm-profitability | 2026-09 | full |
| BD-TOKEN-2026 | AI Tokenomics Guide: Understanding Token-Based AI Pricing for Legal Technology | Baker Donelson (Justin Daniels) | firm | https://www.bakerdonelson.com/webfiles/Bios/Token-Pricing-Guide-for-Clients-August-2026.pdf | 2026-08-20 | full |
| NONBILLABLE-2026 | The $10 million AI bill is coming. Can law firms explain it? | Non-Billable | press | https://www.nonbillable.co.uk/news/legal-ai-moves-usage-based-pricing-consumption-harvey-legora | 2026-07-09 | full |
| LAW360-LEGORA-2026 | Legora's New AI Pricing Model May Usher In Larger Changes | Law360 | press | https://www.law360.com/articles/2494404 | 2026-06-26 | search-only |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | full |
| AT-CROWE-KKR-2026 | Crowe gets PE investment from KKR | Accounting Today | press | https://www.accountingtoday.com/news/crowe-gets-pe-investment-from-kkr | 2026-06-11 | full |
| AT-CROWE-2026 | Crowe launches shared ownership plan (URL slug: crowe-launches-esop-with-kkr-investment) | Accounting Today | press | https://www.accountingtoday.com/news/crowe-launches-esop-with-kkr-investment | 2026-10-19 | full |
| AT-PWC-2026 | PwC grows 2026 global revenue to $60.2B | Accounting Today | press | https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b | 2026-10-19 | full |
| AT-AIUC-2026 | New AI assurance certification combines SOC 2, AIUC-1 | Accounting Today | press | https://www.accountingtoday.com/news/new-ai-assurance-certification-combines-soc-2-aiuc-1 | 2026-10-19 | full |
| AT-MERCOR-2026 | AI beats human accountants at monthly close, transaction categorization | Accounting Today | press | https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization | 2026-10-16 | full |
| AT-AINATIVE-2026 | The AI-native firm (On the Air with Accounting Today, with Ascend founder David Wurtzbacher) | Accounting Today | podcast | https://www.accountingtoday.com/podcast/the-ai-native-firm | 2026-10-19 | full |
| CPAPA-PWC-2026 | PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 2026-03-25 | full |
| FORRESTER-BLOG-2025 | The Future Of AI Consulting Services Is Disruptively Bright | Forrester | press | https://www.forrester.com/blogs/the-future-of-ai-consulting-services-is-disruptively-bright | 2025-09-15 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | CTV News (AP) | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| SOURCE-INSIGHTS-2026 | Precision segmentation: How consulting firms can target clients' sector and functional AI budgets | Source Global Research | press | https://sourceglobalresearch.com/market-update/precision-segmentation-how-consulting-firms-can-target-clients-sector-and-functional-ai-budgets | 2026-09-28 | full |

## 6. Gaps

**Not reached or only partly read**
- ABA Formal Opinion 512: americanbar.org returned HTTP 403 (also via the text mirror); the fee reasoning is known only through quotations in VSB-LEO1901-2025 and TRI-ABA512-2025. Florida Opinion 24-1 loaded as a script page with no body text; NYC Formal Opinion 2024-5 opened but its text did not address fees in the portion read, so it is not cited.
- UK regulators: the SRA page returned a security check (also via the mirror), and the BSB home page had no AI text. SRA price-transparency rules, SRA treatment of AI fees and the BSB "absolute caution" guidance were not read.
- The AICPA exposure draft itself and the PEEC's adoption status: the AICPA pages did not yield the draft, so the proposal is described through NYSSCPA-APS-2025 and TXCPA-APS-2026. Whether the proposals were adopted by 2026-10-19 is unknown.
- PCAOB, SEC and FRC: pages opened but showed no AI-and-fees or private-equity items in the text read. A search on Deloitte Australia's primary documents (the department's statements) and on KPMG Law in Arizona could not be run because the search budget was exhausted.
- Law360: body paywalled (LAW360-LEGORA-2026 is a headline and date only).
- The CLOC analysis of outside counsel guidelines and the ACC sample AI guidelines for outside counsel: referenced in search results but not found; no survey measuring how many outside counsel guidelines restrict billing for AI was found.
- Paywalled: SPI's full report (four foundations are named only inside it), Source Global Research reports, Forrester's full Wave, Thomson Reuters Institute full reports beyond web summaries (LFFI and State of the Legal Market downloads), the full ILTA tech survey.
- Dates not found on the page: EVERLAW-ACC-2025 (year only, inferred from a 2026 blog calling it a recent survey), DCBAR-388-2024 (year only), MCA-SURVEY-2026 (year only), and the exact month of ILTA-TECHSURVEY-2026 (taken from the file name `2606`; the PDF's metadata creation date is 2026-08-14). TR-FOP-2026 shows "Published: Fri Oct 16 2026" on the page; the survey ran March-April 2026.
- Thomson Reuters Institute's rates report analysis (a direct URL returned 404) and the ICAEW AI governance page (404).

**Not found at all**
- Any independent measurement of AI's effect on law-firm or consultancy rates, realization, margin or partner income. No firm-published realization or rate data tied to AI.
- Any error rate, override rate or parallel-run result for an AI forecasting, pricing or profitability tool.
- Public deployments of AI-assisted rate setting, matter-level AI cost metering, or client AI-terms registers by a named firm.
- Evidence from mid-tier and small consultancies and from in-house shared-service teams outside legal.

**Cautions**
- The landscape file describes CroweONE as an employee stock ownership plan and the KKR closing as a 2026 event without a month; Accounting Today says the plan is shared ownership, corrected an earlier ESOP description, announced the investment in June and reported the close in August.
- McKinsey's outcome-based fee share appears as about a quarter (via the Stanford paper citing Business Insider) and, in the landscape, as about a third (secondary); only the first was read.
- Thomson Reuters, Deltek, SPI, Clio, Everlaw and LexisNexis sell AI or research; their survey and modelled figures are marked vendor-published.
- Landscape reference names used: TRI-LFFI-Q1-2026 follows the landscape; TRI-LFFI-Q2-2026 and TRI-ABA512-2025 are new. The Forrester blog is cited as FORRESTER-BLOG-2025; the landscape's FORRESTER-WAVE-2026 snippet (all 10 providers willing to put fees at risk) was not opened and is not used.
