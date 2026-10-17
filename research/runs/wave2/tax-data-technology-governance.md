# Tax data technology: governance angle

Archetype: tax. Module: tax-data-technology (in-house tax operations and data architecture). Angle: governance and evidence (what constrains and measures the work). Prepared 2026-10-17 (wave 2). Working folder was a private temporary directory. Excludes indirect-tax determination engines and GloBE Information Return filing (routed, section 4).

## 1. Summary

- 15 candidate use cases: grade A 0, B 1, C 11, D 2 (labelled ideas). No use case reaches grade A. The only measured outcomes in the public record are survey figures published by firms and vendors, one vendor benchmark (Column Tax) and one independent academic measurement of e-invoicing mandates (Peru) that sits on the tax-authority side, so it caps the grade at B (and the e-invoicing entry stays at C because no named in-house deployment is behind it).
- 45 distinct sources read or seen (43 opened, 2 search-only). By type: survey 10, regulator 8, press 6, standard-setter 4, academic 5, professional-body 3, firm 3, vendor 3, conference 3 (the Thomson Reuters Institute recaps of the 2026 TEI seminar are typed conference). Counts are in section 5.
- What constrains the work, in order of weight: (1) record-keeping and documentation rules that make the ERP-to-return data flow auditable (IRS Rev. Proc. 98-25); (2) a growing set of real-time reporting mandates that make bad master data a legal-validity problem (EU ViDA timetable, UK 2029 mandate, more than 60 jurisdictions on continuous transaction controls per a TEI seminar account); (3) internal-control frameworks that now cover generative AI (COSO, February 2026) and agent interoperability standards that carry their own security rules (MCP specification, NIST AI Agent Standards Initiative, OWASP).
- What measures the work: almost nothing independent. Surveys measure adoption, barriers and confidence. There is no published error rate, override rate, parallel-run result or inspection finding for AI in in-house tax data pipelines. The nearest quality evidence is adjacent: a vendor benchmark in which frontier models computed fewer than one third of simplified federal individual returns correctly, a 2019 vendor survey of bot failure and an independent study of e-invoicing mandates in Peru.
- Practitioners at the 2026 TEI Tax Technology Seminar (as reported by Thomson Reuters Institute) said tax rarely owns AI implementation: two hands out of more than 50 when polled. A vendor-run survey of indirect tax leaders found only 12.5% had specific AI targets or KPIs and 57.4% were not confident they could defend AI-assisted decisions to an authority.
- Three landscape statements could not be confirmed on the pages opened (EY 80% and 75% figures, the Deloitte Pillar Two Agent, and the OECD Tax Administration 2025 body text). See Gaps.

## 2. Use cases

```yaml
- id: tax-data-technology-01
  title: Reconciled ERP-to-return tax data layer with documented lineage
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [data-reporting, software-systems]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Tax data is assembled from several systems before tax work starts, and many functions are early in data management maturity. EY reports that 51% of surveyed tax and finance functions are in the early stages of data management maturity (EY-TFO-2025). US recordkeeping rules require that retained machine-sensible records reconcile to the books and the return, and that the data flow, internal controls and field definitions be documented (IRS-REVPROC-9825)."
  solution: "Tax owns or co-owns a governed data layer between the ERP and the tax engines, with documented record layouts, field definitions and reconciliations to the ledger and the return, so automation and AI tools read from one source. Deloitte's survey reports that 46% of respondents had already enhanced their ERP systems with AI-driven tax analysis tools and a further 44% plan to (DELOITTE-TTT-2025). Kognitos, a vendor, argues that accuracy is decided in the data layer beneath the tax engines, not in the engines (KOGNITOS-2026)."
  outcomes:
    - lever: quality
      description: "Baseline, not an outcome of the use case: share of tax and finance functions still early in data management maturity (firm-published survey)"
      figure: "51%"
      measures: "Tax and finance functions in the early stages of data management maturity, among 1,600 CFOs, senior finance and tax leaders across 30 jurisdictions and 22 industries"
      provenance: vendor-published
      source_ref: EY-TFO-2025
    - lever: quality
      description: "Baseline, not an outcome of the use case: respondents naming the inability to execute a sustainable plan for data, AI and technology as the biggest barrier to delivering the tax function's vision (firm-published survey)"
      figure: "44%"
      measures: "Respondents saying the inability to execute on a sustainable plan for data, AI and tech is their biggest barrier, same 1,600-respondent EY survey"
      provenance: vendor-published
      source_ref: EY-TFO-2025
    - lever: quality
      description: "Outcome of reconciliation and lineage work: none published"
      figure: null
      measures: null
      provenance: vendor-published
      source_ref: KOGNITOS-2026
  prerequisites:
    - "A defined data strategy that names which data matters for tax process flows, which systems hold it, and what privacy and confidentiality limits apply (DELOITTE-TTT-2025)."
    - "Tax is part of the ERP migration and centralisation that many departments are already undertaking, which consumes budget and attention (TR-CORPTAX-2025)."
    - "Documentation of the business processes that create, modify and maintain the records, including the flow of data, internal controls and charts of accounts (IRS-REVPROC-9825)."
  risks_and_guardrails:
    - "Retained records must reconcile to the taxpayer's books and return by account, carry enough transaction-level detail to identify source documents, and be available to the IRS and capable of being processed (IRS-REVPROC-9825)."
    - "Fewer than half of 170 surveyed tax leaders reported a budget increase in the prior year, so a data-layer build competes for scarce funding (TR-CORPTECH-2026)."
  human_checkpoints:
    - "Evidence that retained records reconcile to the books and to the return is kept and produced on request (IRS-REVPROC-9825)."
  role_evolution: "EY reports that 73% of respondents are prioritising the hiring of data scientists and tax technology experts, and 89% are investing in upskilling and reskilling existing staff (EY-TFO-2025)."
  evidence_grade: C
  sources:
    - { ref: EY-TFO-2025, title: "EY report indicates CFOs and tax leaders innovating with AI to manage mounting geopolitical turbulence, talent shortages and regulatory developments", publisher: EY, type: survey, url: "https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments", date: "2025-11-18", access: full, locator: "Press release, paragraphs on data management maturity and workforce" }
    - { ref: IRS-REVPROC-9825, title: "Rev. Proc. 98-25 (retention of machine-sensible records)", publisher: Internal Revenue Service, type: regulator, url: "https://www.irs.gov/pub/irs-drop/rp-98-25.pdf", date: "1998-03-16", access: full, locator: "Sections 5.01(2)-(4), 6.01-6.03, 14" }
    - { ref: DELOITTE-TTT-2025, title: "AI-enabled Tax Transformation (Tax Transformation Trends 2025 analysis)", publisher: Deloitte Luxembourg, type: survey, url: "https://www.deloitte.com/lu/en/services/tax/research/ai-enabled-tax-transformation.html", date: "2025-11-19", access: full, locator: "Sections 'Employ an outcomes-based approach' (Fig. 3) and 'Prepare tax data for AI'" }
    - { ref: TR-CORPTAX-2025, title: "Why most tax departments aren't using AI yet", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/", date: "2025-10-22", access: full, locator: "Section 'Why tax departments are holding back'" }
    - { ref: TR-CORPTECH-2026, title: "Corporate tax department technology report 2026", publisher: Thomson Reuters Institute with Tax Executives Institute, type: survey, url: "https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026", date: "2026-03-16", access: full, locator: "Section 'A growing frustration gap'" }
    - { ref: KOGNITOS-2026, title: "AI for Corporate Tax and Provision Automation (2026)", publisher: Kognitos, type: vendor, url: "https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/", date: "2026-06-17", access: full, locator: "TL;DR and section 'Tax engines vs the data layer'" }
  last_reviewed: 2026-10-17
  notes: "Maturity is set to piloting because no source in this angle names an organization running the data layer. The practice-angle file for this module covers named job postings (Snowflake, Fortive, Apple) for the same use case. Deloitte's page does not state the survey sample size. The landscape quoted an EY figure of 80% struggling with foundational data; that figure is not on the EY press release page opened here."

- id: tax-data-technology-02
  title: Pre-submission validation of invoice and master data for clearance and real-time reporting regimes
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "In clearance regimes an invoice has no legal force until the tax authority returns its identifier, so a wrong VAT ID, malformed schema or mismatched master data gets the invoice rejected; the article adds that Italy charges a fee of 70% of the disputed VAT (TR-AUDITOR-2026). A Thomson Reuters Institute 2026 ViDA readiness survey found that 86% of those surveyed are familiar with ViDA but only 22% have a formal transition program in place (TR-VIDA-2026)."
  solution: "Tax, finance and IT run an owned validation layer over ERP invoice data, checking identifiers, schema and master data before submission, with an exception queue for rejected or at-risk invoices. At the 2026 TEI seminar, attendees polled themselves on data platforms (Alteryx, Power Platform, Snowflake, Databricks, Microsoft Fabric and Palantir Foundry) and the article describes deploying validation agents to critique their own outputs (TR-AUDITOR-2026). The article names no company and does not say the validation agents target outbound invoices."
  outcomes:
    - lever: risk
      description: "Baseline, not an outcome of the use case: organizations with a formal ViDA transition program (vendor-owned research institute survey)"
      figure: "22%"
      measures: "Respondents to the Thomson Reuters Institute 2026 ViDA Readiness Survey whose organizations have a formal transition program in place; 86% said they are familiar with ViDA; sample size not stated on the blog page"
      provenance: vendor-published
      source_ref: TR-VIDA-2026
    - lever: risk
      description: "Outcome of pre-submission validation: none published"
      figure: null
      measures: null
      provenance: vendor-published
      source_ref: TR-AUDITOR-2026
  prerequisites:
    - "Accurate master data, KYC processes and system integration; the survey blog says most finance, IT and operations respondents report low preparedness in these areas (TR-VIDA-2026)."
    - "A single accountable owner across tax, IT and finance; the blog describes a 'bystander effect' in which each function assumes another is leading (TR-VIDA-2026)."
    - "Regime timetable known: ViDA digital reporting requirements for cross-border B2B transactions apply from 1 July 2030 and domestic real-time reporting systems must align by 1 January 2035 (EC-VIDA-2026). The UK has announced mandatory e-invoicing for all VAT invoices from 2029 with a roadmap due at Budget 2026 (UK-EINV-2025)."
  risks_and_guardrails:
    - "AI coding tools let an analyst deploy an integration pipeline that nobody else has reviewed, documented or knows how to maintain (TR-AUDITOR-2026)."
    - "The respondents' top fear in the ViDA survey was rejected and unpaid invoices, ahead of fines (TR-VIDA-2026)."
  human_checkpoints:
    - "The sources do not describe a human checkpoint for invoice validation; they say accountability for ViDA is unclear in large organizations (TR-VIDA-2026)."
  role_evolution: "A TEI panel account says the job at the high end has become as much a data science problem as an accounting one, and one panelist described a shift from preparing returns to answering notices on data that has been shared (TR-AUDITOR-2026)."
  evidence_grade: C
  sources:
    - { ref: TR-AUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "Sections 'End of the traditional model' and 'Outgunned'" }
    - { ref: TR-VIDA-2026, title: "Confident, but not prepared: What the data reveals about ViDA readiness", publisher: Thomson Reuters Europe, type: survey, url: "https://europe.thomsonreuters.com/blog/vida-readiness-europe", date: "2026-07-03", access: full, locator: "Sections 'A bystander effect is in play' and 'Three findings stood out'" }
    - { ref: EC-VIDA-2026, title: "VAT in the Digital Age (ViDA)", publisher: European Commission, type: regulator, url: "https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en", date: "2026-07-29", access: full, locator: "Timeline section; Directive (EU) 2025/516, published in the Official Journal on 25 March 2025" }
    - { ref: UK-EINV-2025, title: "Promoting electronic invoicing across UK businesses and the public sector (consultation response)", publisher: HM Revenue & Customs and Department for Business and Trade, type: regulator, url: "https://www.gov.uk/government/consultations/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector", date: "2025-11-26", access: full, locator: "Outcome summary, final paragraph" }
  last_reviewed: 2026-10-17
  notes: "Maturity piloting is a conservative setting: clearance regimes are operating, but no source names a company running AI-assisted validation. The Italy 70% fee is as stated by the Thomson Reuters Institute article and was not checked against Italian law. The survey blog does not state the sample size, so the 22% and 86% figures cannot be compared with other surveys."

- id: tax-data-technology-03
  title: Reconcile data held by the tax authority with the ledger and returns before notices arrive
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "In jurisdictions with mature continuous transaction controls, tax authorities arrive at audits with structured transaction data they have already analysed, and one panelist at the 2026 TEI seminar described a shift from preparing returns to answering notices on data that has been shared (TR-AUDITOR-2026)."
  solution: "Idea: the company keeps its own view of what the authority holds and reconciles it with the ledger and filed positions continuously, so differences surface before a notice. Deloitte's scenario framework describes a scenario of heightened audit and dispute exposure with real-time data-driven oversight from tax authorities when authority AI progress outruns the company's (DELOITTE-RIDING-2026). Idea, no public deployment found."
  outcomes:
    - lever: risk
      description: none published
      figure: null
      measures: null
      provenance: vendor-published
      source_ref: TR-AUDITOR-2026
  prerequisites:
    - "Structured, reconciled transaction data on the company side (see tax-data-technology-01 and -02)."
  risks_and_guardrails:
    - "The TEI account says the advantage accrues to the side with the fastest and cleanest pipelines, and describes the government as increasingly winning (TR-AUDITOR-2026)."
    - "The same account reports hearing of companies that give up on compliance and pad numbers with a safety margin; a panelist responded 'Do not do this' (TR-AUDITOR-2026)."
  human_checkpoints:
    - "Not described in the sources."
  role_evolution: "Not described beyond the shift from preparing returns to answering notices (TR-AUDITOR-2026)."
  evidence_grade: D
  sources:
    - { ref: TR-AUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "Sections 'Outgunned' and 'Two ways to lose'" }
    - { ref: DELOITTE-RIDING-2026, title: "Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: "2026-07", access: full, locator: "Pages 2-3, four-scenario framework (Scenario 3)" }
  last_reviewed: 2026-10-17
  notes: "Idea. Practitioners discuss the asymmetry; no source describes a company-side reconciliation of authority-held data. The Deloitte date is the PDF creation month (July 2026) with a 2026 copyright line; no printed publication date was found."

- id: tax-data-technology-04
  title: Tax staff build data integration pipelines with AI coding and low-code agent tools under review and documentation controls
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [software-systems, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Integration pipelines that tax needs can sit in an IT queue; the Thomson Reuters Institute account says attendees are vibe-coding data integration pipelines in 15 minutes that would have waited two months in an IT queue (TR-AUDITOR-2026). The same coverage warns that this also lets an analyst deploy something nobody else has reviewed or documented, and describes Alteryx workflows nobody could explain after the builder left (TR-AUDITOR-2026; TEI-TAXTECH-2026)."
  solution: "Tax analysts use AI coding tools and low-code agent builders to create ingestion and transformation pipelines, under change control, documentation and inventory requirements. At the 2026 TEI seminar, four members of OpenAI's own tax department demonstrated live automation pipelines, and Google and Microsoft walked attendees through building agents (TEI-TAXTECH-2026). COSO's generative AI guidance names ingestion and transformation as capability types with their own control expectations (JOFA-COSO-2026)."
  outcomes:
    - lever: speed
      description: "Pipelines built in 15 minutes that would have waited about two months in an IT queue, as characterised by the article authors about attendees; no organization, sample or method given"
      figure: "15 minutes vs two months"
      measures: "Time to build a data integration pipeline with AI coding tools versus time waiting in an IT queue; the article's characterisation of attendees' practice, not a measured result"
      provenance: self-reported
      source_ref: TR-AUDITOR-2026
  prerequisites:
    - "An approved environment and IT sign-off; in the KPMG Germany quick survey the biggest hurdles to expanding AI were IT approvals (47%), data protection requirements (41%) and lack of knowledge of AI applications (41%) (KPMG-DE-2026)."
    - "An inventory of AI use cases with clear ownership and escalation paths, which COSO's guidance emphasises to counter uncontrolled adoption ('shadow AI') (DART-COSO-2026)."
  risks_and_guardrails:
    - "An OpenAI panelist conceded the point when an audience member asked about the security implications of vibe coding (TR-AUDITOR-2026)."
    - "A transformation director described a training program for dozens of global clients that failed, and a tool meant to save two hours consumed a day because users had not been consulted (TEI-TAXTECH-2026)."
  human_checkpoints:
    - "Review and documentation of any pipeline before it is relied on; the article says unreviewed, undocumented pipelines are the failure mode (TR-AUDITOR-2026)."
  role_evolution: "Tax analysts become pipeline builders, and a senior director is quoted saying you will not survive in the field without a change mindset (TEI-TAXTECH-2026)."
  evidence_grade: B
  sources:
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "Sections 'A very good man' and 'A very bad wizard'" }
    - { ref: TR-AUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "Sections 'End of the traditional model' and 'Two ways to lose'" }
    - { ref: JOFA-COSO-2026, title: "COSO creates audit-ready guidance for governing generative AI", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/", date: "2026-02-26", access: full, locator: "Paragraph on the capability-first taxonomy" }
    - { ref: DART-COSO-2026, title: "COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up, Vol. 33, Issue 3)", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: "2026-04-03", access: full, locator: "Opening summary and monitoring paragraph" }
    - { ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-07", access: full, locator: "Section 'AI boosts efficiency but requires clear organizational prerequisites'" }
  last_reviewed: 2026-10-17
  notes: "Grade B rests on the Thomson Reuters Institute's account that OpenAI's tax department demonstrated live automation pipelines; a demonstration is weaker than a production claim, so maturity is piloting. No measurement is published; the 15-minute figure is a characterisation, not a measurement. The practice-angle file covers OpenAI's job postings for the same team."

- id: tax-data-technology-05
  title: Sustaining deployed tax automation with run history, documentation and drift monitoring
  archetype: tax
  module: tax-data-technology
  function: technology-it
  work_types: [software-systems, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Automation breaks when the systems it depends on change. A 2019 Pegasystems survey of more than 500 RPA and desktop-automation decision makers (not tax-specific) found 87% experienced some level of bot failures and 41% said ongoing bot management was taking more time and resources than expected (PEGA-RPA-2019). In tax, TEI seminar attendees described Alteryx workflows nobody could explain after the person who built them left (TEI-TAXTECH-2026)."
  solution: "Tax and IT treat each automation as a controlled asset: documented logic, an owner, run history, KPI monitoring and revalidation after changes. TEI ran a November 2025 session titled 'Automation Sustainment: Ensuring Deployed Automation Continues to Deliver; Best Practices, Tips and Frameworks' (TEI-TECHTAX-2025). Deloitte's COSO commentary says 'set-and-forget' does not work for generative AI in financial reporting and suggests monitoring transaction volume, transaction size and override percentages to detect drift (DART-COSO-2026)."
  outcomes:
    - lever: quality
      description: "Baseline, not an outcome of the use case: bot failures in a vendor-run survey of automation users (not tax-specific)"
      figure: "87%"
      measures: "Respondents among more than 500 decision makers at global businesses using RPA or robotic desktop automation who experience some level of bot failures; vendor-sponsored, 2019"
      provenance: vendor-published
      source_ref: PEGA-RPA-2019
    - lever: capacity
      description: "Baseline, not an outcome of the use case: share saying ongoing bot management takes more time and resources than expected"
      figure: "41%"
      measures: "Respondents in the same Pegasystems survey saying ongoing bot management is taking more time and resources than expected"
      provenance: vendor-published
      source_ref: PEGA-RPA-2019
  prerequisites:
    - "A named owner and a documented logic for every automation; the TEI account ties the failure to the builder leaving without documentation (TEI-TAXTECH-2026)."
    - "KPIs for monitoring and an evaluation of accuracy and root causes such as prompt design, retrieval issues and vendor changes (DART-COSO-2026)."
  risks_and_guardrails:
    - "Pegasystems found that on average only 39% of bots are deployed on schedule and organizations expect bots to last about three years, against initiatives that were 1.8 years old on average (PEGA-RPA-2019)."
    - "The Pegasystems survey is from 2019, is vendor-sponsored and covers all industries, so it only indicates direction for tax."
  human_checkpoints:
    - "Evaluations of accuracy and reliability and root-cause assessment of deficiencies after a drift signal (DART-COSO-2026)."
  role_evolution: "The sustainment role moves from building to owning a portfolio of automations with documented logic and monitoring (TEI-TAXTECH-2026; DART-COSO-2026)."
  evidence_grade: C
  sources:
    - { ref: PEGA-RPA-2019, title: "Survey: Most Businesses Find RPA Effective But Hard To Deploy and Maintain", publisher: Pegasystems, type: survey, url: "https://www.pega.com/node/80501", date: "2019-09-10", access: full, locator: "Paragraphs on bot deployment, lifespans and maintenance" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "Section 'A very bad wizard'" }
    - { ref: TEI-TECHTAX-2025, title: "2025 TechTAXcelerate: Unleashing the Future of Tax Technology (Webinar Series)", publisher: Tax Executives Institute, type: professional-body, url: "https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series", date: "2025-11-17", access: full, locator: "Agenda, Tuesday 18 November" }
    - { ref: DART-COSO-2026, title: "COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up, Vol. 33, Issue 3)", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: "2026-04-03", access: full, locator: "Paragraph beginning 'We believe that the COSO GenAI guidance is most effective'" }
  last_reviewed: 2026-10-17
  notes: "Adjacent evidence: the bot-failure figures come from a non-tax, 2019, vendor survey, which caps the grade at C. No tax-specific figure for automation breakage, mean time to repair or rework was found. TEI's session is dated by the event start (17 November 2025); the sustainment session was on 18 November 2025."

- id: tax-data-technology-06
  title: Tax-owned AI inventory, policy and accountability inside the enterprise control framework
  archetype: tax
  module: tax-data-technology
  function: risk-compliance-legal
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "When TEI seminar attendees were polled on whether the tax function owns AI implementation at their company, two hands went up out of more than 50 (TEI-TAXTECH-2026). In the Thomson Reuters 2025 Generative AI in Professional Services Report, as relayed by Thomson Reuters Tax & Accounting, 17% of corporate tax departments had specific AI and data policies, 21% covered generative AI under general technology policies and 45% had no relevant policy (TR-GENAI-2025)."
  solution: "Tax keeps a live inventory of its AI and automation use cases with owners and escalation paths, written policy, and control mapping to the enterprise framework. COSO's February 2026 guidance on generative AI maps risks to the five components and 17 principles of its Internal Control-Integrated Framework and sets a six-step roadmap: govern, inventory, assess, design, implement, monitor (DART-COSO-2026). It sorts use cases into eight capability types, including ingestion, transformation, posting, orchestration, judgment, monitoring, regulatory intelligence and human-AI interaction (JOFA-COSO-2026). TEI scheduled a session on 'AI Governance, Deployment and Current Regulation' in November 2025 (TEI-TECHTAX-2025)."
  outcomes:
    - lever: risk
      description: "Baseline, not an outcome of the use case: corporate tax departments with no relevant AI policy"
      figure: "45%"
      measures: "Corporate tax departments with no relevant policy for generative AI, in the Thomson Reuters 2025 Generative AI in Professional Services Report as relayed by Thomson Reuters Tax & Accounting; sample size not stated on the blog page; vendor-owned research"
      provenance: vendor-published
      source_ref: TR-GENAI-2025
    - lever: risk
      description: "Baseline, not an outcome of the use case: TEI attendees saying tax owns AI implementation"
      figure: "2 of more than 50"
      measures: "Hands raised when attendees at the 2026 TEI Tax Technology Seminar were asked whether the tax function owns AI implementation at their company; informal poll"
      provenance: self-reported
      source_ref: TEI-TAXTECH-2026
  prerequisites:
    - "Management mandate and governance roles; COSO's roadmap starts with 'govern' (DART-COSO-2026)."
    - "Coordination with IT and data-protection owners, since IT approvals and data protection were the top hurdles in the KPMG Germany quick survey (KPMG-DE-2026)."
  risks_and_guardrails:
    - "GAO found the IRS's own AI use case inventory was incomplete and that over 25% of use cases did not say how they would benefit the agency; the report is about a tax authority, not corporate tax (GAO-2026)."
    - "COSO's guidance addresses rapid change, limited explainability and uncontrolled adoption, and stresses ongoing inventories, ownership and escalation paths (DART-COSO-2026)."
  human_checkpoints:
    - "Named ownership and escalation paths for each inventoried use case (DART-COSO-2026)."
  role_evolution: "Not described for tax specifically; COSO's roadmap is written for management, internal audit, IT risk, legal, the board and external auditors (DART-COSO-2026)."
  evidence_grade: C
  sources:
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "Section 'A very bad wizard', polling paragraph" }
    - { ref: TR-GENAI-2025, title: "5 GenAI tensions corporate tax departments should address", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address", date: "2025-06-24", access: full, locator: "Tension point 4: the policy and governance development need" }
    - { ref: DART-COSO-2026, title: "COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up, Vol. 33, Issue 3)", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: "2026-04-03", access: full, locator: "Opening summary" }
    - { ref: JOFA-COSO-2026, title: "COSO creates audit-ready guidance for governing generative AI", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/", date: "2026-02-26", access: full, locator: "Paragraphs on the capability-first taxonomy and control mapping" }
    - { ref: TEI-TECHTAX-2025, title: "2025 TechTAXcelerate: Unleashing the Future of Tax Technology (Webinar Series)", publisher: Tax Executives Institute, type: professional-body, url: "https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series", date: "2025-11-17", access: full, locator: "Agenda, Tuesday 18 November" }
    - { ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-07", access: full, locator: "Section 'AI boosts efficiency but requires clear organizational prerequisites'" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: U.S. Government Accountability Office, type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: "2026-03-24", access: full, locator: "Highlights, 'What GAO Found'" }
  last_reviewed: 2026-10-17
  notes: "The COSO publication itself was not opened; two secondary summaries were read (Journal of Accountancy, Deloitte DART). The GAO date is carried from the landscape file; the text mirror used here showed no date. COSO's eight capability types are listed in JOFA-COSO-2026; DART-COSO-2026 describes them in different words."

- id: tax-data-technology-07
  title: Acceptance thresholds and ongoing accuracy and override measurement for tax AI and automation
  archetype: tax
  module: tax-data-technology
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Tax functions are told to adopt AI but are not told what good looks like. In a 176-respondent survey of indirect tax leaders run by the vendor Fonoa, only 12.5% had specific targets or KPIs, and only a third ran formal human-in-the-loop review of AI outputs (FONOA-2026). In Deloitte's survey, 77% of tax leaders required 90% or higher accuracy before entrusting AI with their tax processes (DELOITTE-TTT-2025)."
  solution: "Tax sets acceptance thresholds before go-live and monitors accuracy, override rates and cycle time afterwards. COSO-based commentary names transaction volume, transaction size and override percentages as indicators of drift and calls for accuracy and reliability evaluations and root-cause analysis (DART-COSO-2026). Fonoa's diagnostic asks whether leadership has set AI KPIs, whether time saved, cost avoided or cycle-time reduction is measured by workflow, and whether a documented audit trail exists for AI-assisted decisions (FONOA-2026)."
  outcomes:
    - lever: capacity
      description: "A small cohort with accountability structures reported compliance workload falling faster than others (vendor survey, indirect tax)"
      figure: "8x the rate of everyone else"
      measures: "Compliance workload decrease reported by the small cohort of surveyed indirect tax leaders that closed the AI accountability gap, relative to all other respondents, per Fonoa's page; the definition of the cohort and the underlying measure are in the gated report"
      provenance: vendor-published
      source_ref: FONOA-2026
    - lever: risk
      description: "Baseline, not an outcome of the use case: surveyed indirect tax leaders not confident they could defend AI-assisted decisions to an authority"
      figure: "57.4%"
      measures: "Respondents (of 176 indirect tax leaders) who would not be confident that AI-assisted decisions would hold up if challenged by a tax authority"
      provenance: vendor-published
      source_ref: FONOA-2026
    - lever: quality
      description: "Baseline, not an outcome of the use case: tax leaders requiring high accuracy before trusting AI"
      figure: "77%"
      measures: "Tax leaders among Deloitte's Tax Transformation Trends respondents requiring 90% or higher accuracy before entrusting AI with their tax processes; sample size not stated on the page"
      provenance: vendor-published
      source_ref: DELOITTE-TTT-2025
  prerequisites:
    - "A baseline and a test set: Fonoa's checklist asks whether the AI is grounded in current rules, transaction data and the company's own context (FONOA-2026)."
  risks_and_guardrails:
    - "Silent failure: a TEI attendee described an AI agent that, when challenged, said it could not open the file and was telling the user what they wanted to hear (TEI-TAXTECH-2026)."
    - "Measurement of ROI is rare: the Thomson Reuters relayed report says only 20% of organizations across professional services are measuring return on investment (TR-GENAI-2025)."
    - "TIGTA found the IRS had no process to evaluate whether its examination-selection AI models performed better than prior methods; this is a tax-authority finding and an analogy only (TIGTA-2025)."
  human_checkpoints:
    - "Formal human-in-the-loop review of AI outputs before they inform tax decisions, run by about a third of Fonoa's respondents (FONOA-2026)."
  role_evolution: "Tax leaders define KPIs and accountability structures (FONOA-2026); TEI attendees said reviewing a growing volume of quiet, polite errors is the unresolved question (TEI-TAXTECH-2026)."
  evidence_grade: C
  sources:
    - { ref: FONOA-2026, title: "State of Indirect Tax in the AI Era 2026", publisher: Fonoa, type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: "2026-06-17", access: full, locator: "Landing page sections on the AI mandate, defending AI decisions, governance and the diagnostic checklist" }
    - { ref: DELOITTE-TTT-2025, title: "AI-enabled Tax Transformation (Tax Transformation Trends 2025 analysis)", publisher: Deloitte Luxembourg, type: survey, url: "https://www.deloitte.com/lu/en/services/tax/research/ai-enabled-tax-transformation.html", date: "2025-11-19", access: full, locator: "Section 'Sink or swim: Address the barriers'" }
    - { ref: DART-COSO-2026, title: "COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up, Vol. 33, Issue 3)", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: "2026-04-03", access: full, locator: "Paragraph on monitoring KPIs and override percentages" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "Section 'A very bad wizard'" }
    - { ref: TR-GENAI-2025, title: "5 GenAI tensions corporate tax departments should address", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address", date: "2025-06-24", access: full, locator: "Tension point 3: the ROI measurement gap" }
    - { ref: TIGTA-2025, title: "The IRS Could Leverage Examination Results in Artificial Intelligence Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022)", publisher: Treasury Inspector General for Tax Administration, type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: "2025-05-19", access: full, locator: "Highlights page, 'What TIGTA Found'" }
  last_reviewed: 2026-10-17
  notes: "Grade capped at C: the Fonoa survey covers indirect tax leaders (adjacent process) and the 8x figure is vendor-published with its measure in a gated report. Fonoa's cohort definition and the Deloitte sample size are not on the pages opened. The 20% ROI figure in TR-GENAI-2025 is stated for organizations in professional services, not for corporate tax departments."

- id: tax-data-technology-08
  title: Decision log and audit trail for AI-assisted tax determinations
  archetype: tax
  module: tax-data-technology
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Most surveyed indirect tax leaders (57.4%) were not confident they could defend AI-assisted decisions to a tax authority, and the survey's strongest predictor of audit confidence was whether a defined process sat behind the output (FONOA-2026). One interviewee in the Fonoa report put it as demonstrating a process, not defending a technology (FONOA-2026)."
  solution: "Tax records which AI-assisted outputs affected filings, determinations or authority responses, what inputs and sources were used, and which suggestions were accepted, modified or rejected, so the position can be reconstructed. Fonoa's checklist asks whether the company can identify AI-assisted decisions that affected filings in the last 12 months and produce a documented audit trail for them (FONOA-2026). The AICPA-published risk register for preparers lists documentation of which AI suggestions were accepted, modified or rejected as an illustrative control (AICPA-WERFEL-2026). Savant announced a TEI 2026 session, with Oxford Industries' senior director of tax and accounting, on audit-ready outputs with full traceability (SAVANT-TEI-2026)."
  outcomes:
    - lever: risk
      description: none published
      figure: null
      measures: null
      provenance: vendor-published
      source_ref: SAVANT-TEI-2026
  prerequisites:
    - "US machine-sensible record rules already require documentation of the processes that create and modify retained records and of the internal controls over them (IRS-REVPROC-9825)."
    - "Logs of inputs, outputs and human review decisions kept independently of the vendor; the AICPA register lists tamper-proof logging and audit trail access independent of vendor cooperation as a control for tax authorities (AICPA-WERFEL-2026)."
  risks_and_guardrails:
    - "The IRS Office of Professional Responsibility says practitioners using generative AI must verify the accuracy of facts, citations and calculations; the alert applies to practitioners before the IRS and not to in-house departments as such (IRS-OPR-2026)."
  human_checkpoints:
    - "Practitioner review of all AI-created documents before delivery or submission (IRS-OPR-2026)."
  role_evolution: "Not described beyond reviewers carrying documented responsibility for AI-suggested positions (AICPA-WERFEL-2026)."
  evidence_grade: C
  sources:
    - { ref: FONOA-2026, title: "State of Indirect Tax in the AI Era 2026", publisher: Fonoa, type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: "2026-06-17", access: full, locator: "Sections 'Most tax teams can't defend their AI decisions' and 'How to identify your AI accountability gap'" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and C (Danny Werfel)", publisher: AICPA (The Tax Adviser), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix C risk 1 and Appendix A risk 18" }
    - { ref: SAVANT-TEI-2026, title: "Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026", publisher: Savant Labs, type: vendor, url: "https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/", date: "2026-04-16", access: full, locator: "Session description and learning points" }
    - { ref: IRS-REVPROC-9825, title: "Rev. Proc. 98-25 (retention of machine-sensible records)", publisher: Internal Revenue Service, type: regulator, url: "https://www.irs.gov/pub/irs-drop/rp-98-25.pdf", date: "1998-03-16", access: full, locator: "Sections 6.01-6.03" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Section 'Regulatory Framework: Circular 230 Provisions', item 1 (section 10.22)" }
  last_reviewed: 2026-10-17
  notes: "Maturity announced: the only named-company item is a vendor press release dated before the session (16 April 2026, session 28 April 2026); the sources do not show what Oxford Industries uses in production. The AICPA register covers tax preparers and tax authorities, not in-house departments. The Rev. Proc. 98-25 date is the bulletin date of 1998-11 I.R.B. 7 (16 March 1998)."

- id: tax-data-technology-09
  title: Agents call tax engines through MCP with least-privilege scopes and full tool-call logging
  archetype: tax
  module: tax-data-technology
  function: technology-it
  work_types: [software-systems, transaction-processing]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Tax engines expose capabilities through APIs that developers integrate one by one; vendors now publish Model Context Protocol servers so a company's own agents can call them as tools, which raises questions of authorization, identity and logging. Avalara's May 2026 developer primer says its MCP servers expose the same capabilities as standardised AI tools (AVALARA-MCP-2026)."
  solution: "The tax technology team connects its own agents to vendor MCP servers under the protocol's authorization rules. Avalara's primer says its servers use OAuth 2.1, that clients should grant only the OAuth scopes the agent needs, audit consents periodically, and log every tool call, its inputs and the response status (AVALARA-MCP-2026). The MCP specification says servers must not accept tokens not issued for them ('token passthrough') and that proxy servers must guard against the confused deputy problem (MCP-SPEC-2025). MCP was contributed to the Linux Foundation's Agentic AI Foundation in December 2025 (LF-AAIF-2025), and A2A was contributed to the Linux Foundation in June 2025 (LF-A2A-2025)."
  outcomes:
    - lever: speed
      description: none published
      figure: null
      measures: null
      provenance: vendor-published
      source_ref: AVALARA-MCP-2026
  prerequisites:
    - "An MCP-capable client that supports OAuth 2.1 and an active subscription with entitlements to the services called (AVALARA-MCP-2026)."
    - "Agent identity and authorization: NIST's NCCoE published a draft concept paper on software and AI agent identity and authorization for enterprise use cases, and NIST's CAISI sought input on agent security (NIST-CAISI-2026)."
  risks_and_guardrails:
    - "The MCP security best practices document names confused deputy, token passthrough, server-side request forgery and session hijacking as attack patterns (MCP-SPEC-2025)."
    - "OWASP publishes a peer-reviewed Top 10 of the most critical security risks facing autonomous and agentic AI systems, developed with more than 100 experts (OWASP-AGENTIC-2025)."
    - "Vendor guidance warns that agents are nondeterministic and that logs are how you debug them (AVALARA-MCP-2026)."
    - "A benchmark by Column Tax found frontier models computed fewer than one third of simplified federal individual returns correctly, so tax calculation should not rest on model arithmetic (COLUMN-TAXCALCBENCH-2025)."
  human_checkpoints:
    - "User consent to the requested permissions during the OAuth flow, and periodic audit of consents (AVALARA-MCP-2026)."
  role_evolution: "Tax technology staff become owners of agent access, scopes and logs for tax platforms (AVALARA-MCP-2026)."
  evidence_grade: C
  sources:
    - { ref: AVALARA-MCP-2026, title: "Inside Avalara MCP servers: A developer's primer for agentic tax and compliance", publisher: Avalara, type: vendor, url: "https://www.avalara.com/us/en/blog/avalara-mcp-servers.html", date: "2026-05-27", access: full, locator: "Sections on authorization and 'Operational realities'" }
    - { ref: MCP-SPEC-2025, title: "Model Context Protocol specification, version 2025-11-25: Security Best Practices and Authorization", publisher: Model Context Protocol project, type: standard-setter, url: "https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices", date: "2025-11-25", access: full, locator: "Sections 'Confused Deputy Problem', 'Token Passthrough', 'Server-Side Request Forgery', 'Session Hijacking'" }
    - { ref: LF-AAIF-2025, title: "Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF), Anchored by New Project Contributions Including Model Context Protocol (MCP), goose and AGENTS.md", publisher: The Linux Foundation, type: press, url: "https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation", date: "2025-12-09", access: full, locator: "Opening paragraphs and MCP section" }
    - { ref: LF-A2A-2025, title: "Linux Foundation Launches the Agent2Agent Protocol Project to Enable Secure, Intelligent Communication Between AI Agents", publisher: The Linux Foundation, type: press, url: "https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents", date: "2025-06-23", access: full, locator: "Opening paragraphs" }
    - { ref: NIST-CAISI-2026, title: "AI Agent Standards Initiative", publisher: NIST (CAISI and NCCoE), type: standard-setter, url: "https://www.nist.gov/caisi/ai-agent-standards-initiative", date: "2026-02-17", access: full, locator: "Initiative description and the RFI and concept paper items" }
    - { ref: OWASP-AGENTIC-2025, title: "OWASP Top 10 for Agentic Applications for 2026", publisher: OWASP Gen AI Security Project, type: standard-setter, url: "https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/", date: "2025-12-09", access: full, locator: "About section (landing page; the list itself was not read)" }
    - { ref: COLUMN-TAXCALCBENCH-2025, title: "TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task", publisher: Column Tax (arXiv 2507.16126), type: academic, url: "https://arxiv.org/abs/2507.16126", date: "2025-07-22", access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: "The vendor server is an indirect-tax product, but the MCP security and authorization rules apply to any tax engine; tax-determination content itself is routed to indirect-tax. No customer use of MCP with a tax engine is published in these sources (the practice-angle file covers Avalara, Kintsugi and Sovos product claims). TaxCalcBench was written by employees of a vendor that sells a deterministic engine and covers individual returns, so it is adjacent evidence."

- id: tax-data-technology-10
  title: Route tax computation to a deterministic or symbolic engine and use the model for translation and orchestration
  archetype: tax
  module: tax-data-technology
  function: technology-it
  work_types: [software-systems, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Frontier models misuse tax tables, make calculation errors and misjudge eligibility: in TaxCalcBench they computed fewer than one third of simplified federal individual returns correctly (COLUMN-TAXCALCBENCH-2025). Johns Hopkins researchers argue that automated tax systems must deliver high accuracy and auditability, which makes modern LLMs poorly suited to compute tax on their own (JHU-TAXREASON-2025)."
  solution: "The model translates facts and rules into a form a deterministic engine or logic program computes, so the arithmetic and rule application are auditable. The JHU paper integrates an LLM with a symbolic solver on the SARA statutory reasoning dataset and adds a cost model based on real-world penalties for tax errors (JHU-TAXREASON-2025). Columbia's TaxBench, still in development, plans field-by-field deterministic comparison with reference returns and tests whether agents ask for missing information and apply rule precedence (COLUMBIA-TAXBENCH-2026). TEI attendees flagged rising token costs that could change the economic case for automation (TEI-TAXTECH-2026)."
  outcomes:
    - lever: quality
      description: "Baseline, not an outcome of the use case: model accuracy on direct tax calculation"
      figure: "fewer than a third of returns"
      measures: "Share of simplified federal individual income tax returns that state-of-the-art models calculated correctly on TaxCalcBench; the abstract gives no exact percentage; benchmark authored by a vendor of a deterministic engine"
      provenance: vendor-published
      source_ref: COLUMN-TAXCALCBENCH-2025
    - lever: cost
      description: "The JHU paper reports that the approach reduces expected cost to well below real-world averages of error penalties; no figure is given in the abstract"
      figure: null
      measures: null
      provenance: independent
      source_ref: JHU-TAXREASON-2025
  prerequisites:
    - "A formalised rule base or an existing tax engine that the model can call (JHU-TAXREASON-2025)."
  risks_and_guardrails:
    - "TaxBench is not released and its counts may change before release (COLUMBIA-TAXBENCH-2026)."
    - "Token costs could change the economics of agent-based automation (TEI-TAXTECH-2026)."
  human_checkpoints:
    - "Not described in the sources; TaxBench scores whether an agent requests missing information from the taxpayer (COLUMBIA-TAXBENCH-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - { ref: COLUMN-TAXCALCBENCH-2025, title: "TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task", publisher: Column Tax (arXiv 2507.16126), type: academic, url: "https://arxiv.org/abs/2507.16126", date: "2025-07-22", access: full, locator: "Abstract" }
    - { ref: JHU-TAXREASON-2025, title: "Language Models and Logic Programs for Trustworthy Tax Reasoning", publisher: Johns Hopkins University (arXiv 2508.21051, v3 5 Feb 2026), type: academic, url: "https://arxiv.org/abs/2508.21051", date: "2025-08-28", access: full, locator: "Abstract" }
    - { ref: COLUMBIA-TAXBENCH-2026, title: "TaxBench", publisher: Columbia DAP Lab, type: academic, url: "https://daplab.cs.columbia.edu/benchmarks/taxbench/", date: "2026-10-16", access: full, locator: "'What it evaluates' and 'Release status'" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "Key insights" }
  last_reviewed: 2026-10-17
  notes: "Adjacent evidence: both benchmarks concern US individual income tax, not corporate data pipelines. Only abstracts were read for the arXiv papers. The TaxBench page date is the page's published-time metadata; the benchmark is under development."

- id: tax-data-technology-11
  title: AI extraction of tax notices and source documents into structured data with independent verification
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "State tax notices never arrive in the same format twice, and the TEI seminar account says attendees are using AI image-to-text solutions to pull structured data out of them (TR-AUDITOR-2026). The AICPA-published risk register for preparers describes incorrect document extraction as errors that flow silently into a return, with a W-2 box 12 misclassification as its scenario (AICPA-WERFEL-2026)."
  solution: "AI extracts fields from notices and source documents into the tax data layer; every extracted value is verified against the source document and complex or ambiguous documents escalate to a person. The register's illustrative controls are independent verification of AI-extracted figures against source documents, spot-check audits of extraction accuracy and an escalation protocol (AICPA-WERFEL-2026). The Tax Court-style example of silent failure at TEI: an agent that said it could not open the file after giving numbers that looked wrong (TEI-TAXTECH-2026)."
  outcomes:
    - lever: quality
      description: none published
      figure: null
      measures: null
      provenance: self-reported
      source_ref: TR-AUDITOR-2026
  prerequisites:
    - "A defined verification step and a sample of documents with known values to measure extraction accuracy (AICPA-WERFEL-2026)."
  risks_and_guardrails:
    - "Errors enter without triggering any flag and are discovered only when a notice arrives (AICPA-WERFEL-2026)."
    - "The register covers tax preparers; the in-house setting is adjacent."
  human_checkpoints:
    - "Independent verification of extracted figures against source documents for all returns, and escalation when documents are complex or ambiguous (AICPA-WERFEL-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - { ref: TR-AUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "Section 'End of the traditional model', platform paragraph" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and C (Danny Werfel)", publisher: AICPA (The Tax Adviser), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix C, risk 3 (Incorrect Document Extraction)" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "Section 'A very bad wizard'" }
  last_reviewed: 2026-10-17
  notes: "The TEI account does not name the organizations extracting notices. No extraction error rate for tax documents was found in any source."

- id: tax-data-technology-12
  title: Tax AI runs on the enterprise-standard platform under IT and data-protection approval
  archetype: tax
  module: tax-data-technology
  function: technology-it
  work_types: [software-systems, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "In KPMG Germany's quick surveys, the biggest hurdles to expanding AI in tax departments were IT approvals (47%), data protection requirements (41%) and lack of knowledge about AI applications (41%) (KPMG-DE-2026). Deloitte's survey lists data security and privacy concerns among the factors holding tax leaders back, cited by 30% of respondents (DELOITTE-TTT-2025)."
  solution: "Tax uses AI tools the company has already approved for enterprise use, rather than separate tax-only tools. KPMG Germany reports that 89% of surveyed companies used company-wide standard AI solutions and 29% used specialised applications for tax issues, with use cases ranging from researching and processing tax information to analysing large volumes of data and supporting documentation and reporting (KPMG-DE-2026)."
  outcomes:
    - lever: speed
      description: "AI users reporting noticeable time savings (firm-published quick survey, Germany)"
      figure: "66%"
      measures: "Share of AI users among surveyed tax departments in Germany who report noticeable time savings; the release does not state the sample size"
      provenance: vendor-published
      source_ref: KPMG-DE-2026
    - lever: experience
      description: "AI users reporting generally positive effects on daily work"
      figure: "57%"
      measures: "Share of AI users in the same KPMG quick surveys who report generally positive effects on their daily work; sample size not stated"
      provenance: vendor-published
      source_ref: KPMG-DE-2026
  prerequisites:
    - "IT approval and data-protection clearance for the tool and the data types it will see (KPMG-DE-2026)."
    - "Training: Deloitte reports 45% of respondents named AI-related skills as their greatest need over one to two years (DELOITTE-TTT-2025)."
  risks_and_guardrails:
    - "The release says expansion of AI is tied to prerequisites and names IT approvals, data protection and knowledge as hurdles (KPMG-DE-2026)."
    - "The IRS OPR alert warns of confidentiality leakage between clients when a generative tool reuses data, and says third-party AI tools should be vetted; it is addressed to practitioners (IRS-OPR-2026)."
  human_checkpoints:
    - "IT and data-protection approval before use (KPMG-DE-2026)."
  role_evolution: "KPMG's survey reports 58% of companies expect domestic tax headcount to stay constant and 72% expect the same abroad (KPMG-DE-2026)."
  evidence_grade: C
  sources:
    - { ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-07", access: full, locator: "Key findings and section 'Tax departments are already making extensive use of AI'" }
    - { ref: DELOITTE-TTT-2025, title: "AI-enabled Tax Transformation (Tax Transformation Trends 2025 analysis)", publisher: Deloitte Luxembourg, type: survey, url: "https://www.deloitte.com/lu/en/services/tax/research/ai-enabled-tax-transformation.html", date: "2025-11-19", access: full, locator: "Sections 'Sink or swim' and 'Topping up the talent pool'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Opening section and 'Contracting with external providers'" }
  last_reviewed: 2026-10-17
  notes: "KPMG Germany's release states the 71% usage figure but not the sample size or whether the 89% and 29% overlap. German-market evidence; a firm-published survey. Maturity is piloting only because no organization is named."

- id: tax-data-technology-13
  title: Tax technology team and operating model built with finance and IT
  archetype: tax
  module: tax-data-technology
  function: people-hr
  work_types: [coordination-scheduling, software-systems]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Corporate tax departments are under-resourced and spend more than half their time on reactive work: in the Thomson Reuters Institute 2025 State of the Corporate Tax Department report, 58% called their department under-resourced, up from 51% (TR-CORPTAX-2025). Fewer than half of 170 surveyed tax leaders got a budget increase in the previous year (TR-CORPTECH-2026)."
  solution: "Tax builds a technology function with data and automation skills, hires and upskills, and works with finance and IT. In the same report, departments that spent more than half their time on proactive work reported fewer penalties than those spending more than half their time reactively (TR-CORPTAX-2025). About two thirds of tax professionals surveyed said company investment in technology had enabled a shift toward more proactive tax work (TR-CORPTECH-2026)."
  outcomes:
    - lever: risk
      description: "Association between time mix and penalties; not shown to be caused by technology"
      figure: "31% vs 56%"
      measures: "Respondents who spend more than half their time on proactive work whose departments incurred penalties (31%), against respondents who spend more than half their time in reactive mode whose departments faced penalties (56%), in the Thomson Reuters Institute 2025 survey; sample size not stated on the blog page"
      provenance: vendor-published
      source_ref: TR-CORPTAX-2025
    - lever: capacity
      description: "Tax professionals saying technology investment enabled a shift to proactive work"
      figure: "67%"
      measures: "Surveyed tax professionals (170 tax leaders) saying their company's investment in technology had enabled a shift toward more proactive tax work"
      provenance: vendor-published
      source_ref: TR-CORPTECH-2026
    - lever: quality
      description: "KPMG readiness survey: top-quartile tax-readiness organizations outperform"
      figure: "4-6x more likely"
      measures: "Organizations in the top quartile of tax readiness compared with the bottom quartile, more likely to outperform peers on innovation, resilience, workforce capability and enterprise value; 2,084 senior leaders in 25 jurisdictions; correlation from a firm-published survey"
      provenance: vendor-published
      source_ref: KPMG-READINESS-2026
  prerequisites:
    - "Close collaboration with finance and IT (DELOITTE-TTT-2025)."
    - "Skills: 45% of Deloitte's respondents named AI-related skills their greatest need in one to two years, 94% believed AI skills will be essential within four to five years, and 53% were actively recruiting digitally native talent (DELOITTE-TTT-2025)."
  risks_and_guardrails:
    - "Most tax leaders surveyed by Thomson Reuters Institute and TEI said upgrading tax technology is still a relatively low priority at their company (TR-CORPTECH-2026)."
    - "In the 2025 Generative AI report relayed by Thomson Reuters, 24% of organizations considered generative AI skills nice to have in new hires and 2% made them a requirement (TR-GENAI-2025)."
  human_checkpoints:
    - "Not described in the sources."
  role_evolution: "EY reports 73% prioritising the hiring of data scientists and tax technology experts and 89% investing in upskilling (EY-TFO-2025); KPMG Germany reports 58% expect stable domestic tax headcount (KPMG-DE-2026); a Tax Notes State article summarised in the landscape argues AI will not shrink corporate tax teams much (not opened here)."
  evidence_grade: C
  sources:
    - { ref: TR-CORPTAX-2025, title: "Why most tax departments aren't using AI yet", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/", date: "2025-10-22", access: full, locator: "Sections 'The confidence gap and resource connection' and 'Budget realities'" }
    - { ref: TR-CORPTECH-2026, title: "Corporate tax department technology report 2026", publisher: Thomson Reuters Institute with Tax Executives Institute, type: survey, url: "https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026", date: "2026-03-16", access: full, locator: "Sections 'A growing frustration gap' and 'Moving toward more proactive work, albeit slowly'" }
    - { ref: KPMG-READINESS-2026, title: "2026 KPMG Global Tax Readiness Dividend", publisher: KPMG International, type: survey, url: "https://kpmg.com/xx/en/our-insights/transformation/global-tax-readiness-dividend.html", date: "2026-06-22", access: full, locator: "Sections 'Readiness is becoming a performance multiplier' and 'About the research'" }
    - { ref: DELOITTE-TTT-2025, title: "AI-enabled Tax Transformation (Tax Transformation Trends 2025 analysis)", publisher: Deloitte Luxembourg, type: survey, url: "https://www.deloitte.com/lu/en/services/tax/research/ai-enabled-tax-transformation.html", date: "2025-11-19", access: full, locator: "Section 'Topping up the talent pool'" }
    - { ref: TR-GENAI-2025, title: "5 GenAI tensions corporate tax departments should address", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address", date: "2025-06-24", access: full, locator: "Tension point 5" }
    - { ref: EY-TFO-2025, title: "EY report indicates CFOs and tax leaders innovating with AI to manage mounting geopolitical turbulence, talent shortages and regulatory developments", publisher: EY, type: survey, url: "https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments", date: "2025-11-18", access: full, locator: "Press release, workforce paragraph" }
    - { ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-07", access: full, locator: "Headline findings" }
  last_reviewed: 2026-10-17
  notes: "All figures are associations from vendor- or firm-owned surveys; none show that the operating model caused the outcome. The 31% and 56% penalty shares are the blog's statement of survey responses. The Sala article cited in the landscape was not opened by this run and is not used as a source."

- id: tax-data-technology-14
  title: AI transparency and data-handling due diligence for tax service providers and software vendors
  archetype: tax
  module: tax-data-technology
  function: procurement-supply-chain
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "In the Thomson Reuters 2025 Generative AI report relayed by its tax blog, 77% of business tax departments wanted their tax service providers to use generative AI, yet 59% were not sure whether their companies were using it (TR-GENAI-2025). The AICPA-published risk register lists vendor dependence, including a vendor discontinuing a core product at 30 days' notice, as a risk for preparers (AICPA-WERFEL-2026)."
  solution: "Idea: tax asks providers and software vendors to disclose where and how AI is used on its data and work, and adds contract terms on data use, portability and notice. The register's illustrative controls include vetting AI vendors for data retention and training practices, contractual prohibition on vendor use of client data for training, vendor diversification, documented manual workflows and contract protections for data portability and reasonable notice (AICPA-WERFEL-2026). IRS OPR says outsourced or third-party AI tools should be vetted (IRS-OPR-2026)."
  outcomes:
    - lever: risk
      description: none published
      figure: null
      measures: null
      provenance: vendor-published
      source_ref: TR-GENAI-2025
  prerequisites:
    - "Contract and procurement involvement; the sources are written for practitioners and do not detail the in-house process."
  risks_and_guardrails:
    - "Without knowing whether providers use AI, a department cannot measure efficiency gains or benchmark fees (TR-GENAI-2025)."
    - "Both the register and the OPR alert are written for practitioners and tax authorities, not in-house departments."
  human_checkpoints:
    - "Not described in the sources."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
    - { ref: TR-GENAI-2025, title: "5 GenAI tensions corporate tax departments should address", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address", date: "2025-06-24", access: full, locator: "Tension point 1: the vendor transparency gap" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and C (Danny Werfel)", publisher: AICPA (The Tax Adviser), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix C, risks 2 and 14" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Section on firm procedures, 'Contracting with external providers'" }
  last_reviewed: 2026-10-17
  notes: "Idea, labelled D: the sources describe the transparency gap and the practitioner-side controls, but no in-house tax department practice was found."

- id: tax-data-technology-15
  title: Transaction-level real-time reporting to tax authorities replaces periodic return data
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: bulk-transformation
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Periodic returns give authorities data weeks after the transaction. According to the Thomson Reuters Institute account of the 2026 TEI seminar, more than 60 jurisdictions have moved or are moving to continuous transaction controls, and in those regimes authorities see, validate and pre-fill from structured data as it happens (TR-AUDITOR-2026). The EU adopted the ViDA package on 11 March 2025 and will roll it out progressively until January 2035 (EC-VIDA-2026)."
  solution: "Companies send invoice and transaction data to the authority as it is created and build their tax data architecture around that interface. ViDA digital reporting requirements for cross-border B2B transactions take effect from 1 July 2030, and by 1 January 2035 Member States with domestic real-time transaction reporting must align with the EU model (EC-VIDA-2026). The UK will introduce mandatory e-invoicing for all VAT invoices from 2029 (UK-EINV-2025); a trade-press report says the 23 June 2026 UK announcement chose Peppol and initially has no e-reporting to HMRC (FISCAL-UK-2026). The OECD Forum on Tax Administration commissioners agreed in November 2025 to move toward pilots of real-time automated sharing of secure information (OECD-FTA-2025)."
  outcomes:
    - lever: quality
      description: "Independent study of Peru's staggered mandate: e-invoicing raised reported figures in the first year after adoption"
      figure: "over 5%"
      measures: "Increase in reported firm sales, purchases and VAT liabilities in the first year after adopting e-invoicing, from quasi-experimental variation in the roll-out among about 53,000 firms in a balanced panel; the paper reports intent-to-treat increases of 7.4% in taxable sales and 5.5% in taxable purchases"
      provenance: independent
      source_ref: BELLON-PERU-2022
    - lever: cost
      description: "European Commission estimate for ViDA digital reporting: reduced VAT fraud and compliance costs"
      figure: "up to EUR 11 billion a year less VAT fraud; over EUR 4.1 billion a year lower compliance costs"
      measures: "Commission statement that the move to e-invoicing will reduce VAT fraud by up to EUR 11 billion a year and bring down administrative and compliance costs for EU traders by over EUR 4.1 billion per year over the next ten years; a projection, not a measured outcome"
      provenance: independent
      source_ref: EC-VIDA-2026
  prerequisites:
    - "Master data, system integration and ownership across tax, IT and finance (TR-VIDA-2026)."
    - "Knowledge of each regime's timetable and scope; UK scope and phasing are expected in a roadmap at Budget 2026 (UK-EINV-2025)."
  risks_and_guardrails:
    - "In clearance regimes an invoice has no legal force until the authority returns its identifier (TR-AUDITOR-2026)."
    - "The Commission's VAT gap page reports a 2023 EU VAT compliance gap of 9.5% of the VAT total tax liability, 1.6 percentage points lower than in 2019; the page read here does not attribute the change to e-invoicing (EC-VATGAP-2025)."
    - "The IMF paper on firm digitalisation and tax revenue finds digitalisation is associated with higher tax paid, strongest among high-risk taxpayers, and with a synergy with digital tax administration; it studies firms generally, not tax departments (IMF-WP-2025-089)."
  human_checkpoints:
    - "Not described in the sources for in-house teams."
  role_evolution: "Tax teams move from preparing periodic returns to managing data pipelines and answering notices on shared data (TR-AUDITOR-2026)."
  evidence_grade: C
  sources:
    - { ref: BELLON-PERU-2022, title: "Digitalization to improve tax compliance: Evidence from VAT e-invoicing in Peru", publisher: Journal of Public Economics (Bellon, Dabla-Norris, Khalid, Lima; PubMed Central copy), type: academic, url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9168443/", date: "2022-06", access: full, locator: "Abstract and introduction paragraphs on the estimates" }
    - { ref: EC-VIDA-2026, title: "VAT in the Digital Age (ViDA)", publisher: European Commission, type: regulator, url: "https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en", date: "2026-07-29", access: full, locator: "Timeline and 'Real-time Digital Reporting Requirements' sections" }
    - { ref: UK-EINV-2025, title: "Promoting electronic invoicing across UK businesses and the public sector (consultation response)", publisher: HM Revenue & Customs and Department for Business and Trade, type: regulator, url: "https://www.gov.uk/government/consultations/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector", date: "2025-11-26", access: full, locator: "Outcome summary" }
    - { ref: FISCAL-UK-2026, title: "UK Confirms Peppol for B2B E-Invoicing Mandate from April 2029", publisher: Fiscal Solutions, type: press, url: "https://www.fiscal-requirements.com/news/5673-uk-confirms-peppol-for-b2b-e-invoicing-mandate-from-april-2029", date: "2026-06-29", access: full, locator: "Summary and 'Key Features'" }
    - { ref: OECD-FTA-2025, title: "Heads of tax administrations agree further work on collaborative projects to reduce compliance burdens and deepen co-operation in tackling tax gaps", publisher: OECD, type: regulator, url: "https://www.oecd.org/en/about/news/announcements/2025/11/heads-of-tax-administrations-agree-further-work-on-collaborative-projects-to-reduce-compliance-burdens-and-deepen-co-operation-in-tackling-tax-gaps.html", date: "2025-11-20", access: full, locator: "First bulleted outcome" }
    - { ref: TR-AUDITOR-2026, title: "2026 TEI Tax Technology Seminar: What the auditor already knows", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows", date: "2026-05-12", access: full, locator: "Section 'End of the traditional model'" }
    - { ref: TR-VIDA-2026, title: "Confident, but not prepared: What the data reveals about ViDA readiness", publisher: Thomson Reuters Europe, type: survey, url: "https://europe.thomsonreuters.com/blog/vida-readiness-europe", date: "2026-07-03", access: full, locator: "Section 'Three findings stood out'" }
    - { ref: EC-VATGAP-2025, title: "VAT gap in Europe - report 2025", publisher: European Commission, type: regulator, url: "https://taxation-customs.ec.europa.eu/vat-gap_en", date: "2025-12-11", access: full, locator: "Section 'Development of VAT compliance gap between 2019 and 2023'" }
    - { ref: IMF-WP-2025-089, title: "Leveraging Digital Technologies in Boosting Tax Collection (Working Paper 2025/089)", publisher: International Monetary Fund (Nose, Pierri, Honda), type: academic, url: "https://econpapers.repec.org/paper/imfimfwpa/2025_2f089.htm", date: "2025-05-09", access: full, locator: "Abstract (RePEc record; the IMF site was blocked)" }
  last_reviewed: 2026-10-17
  notes: "Grade scope: the Peru study measures a tax-authority regime on taxpayers' reported figures, an adjacent measurement that caps the grade at B; no named in-house deployment is behind it, so the grade is C. In-production is stated at regime level (the EC and TEI sources say regimes operate) not for a named company. The Commission figures are projections. The UK Peppol and 23 June 2026 details come from a trade-press item (Fiscal Solutions), not from the gov.uk page; the gov.uk consultation response (26 November 2025) confirms mandatory e-invoicing from 2029 and a roadmap at Budget 2026. The Commission VAT gap page was read in part; it does not mention e-invoicing."
```

## 3. Module notes

### Processes and key steps (with work types)

| Step | Work type | Governance point |
|---|---|---|
| Extract ERP and ledger data into a tax data layer and map it to tax attributes | data-reporting, software-systems | Records must reconcile to books and return, with documented data flow and field definitions (IRS-REVPROC-9825) |
| Reconcile, cleanse and approve data before it feeds engines and returns | review-assurance, data-reporting | Reconciliation evidence is a documentation requirement (IRS-REVPROC-9825); COSO treats ingestion, transformation and posting as capability types with control expectations (JOFA-COSO-2026) |
| Build, document and sustain automations and pipelines | software-systems | Undocumented Alteryx flows and unreviewed AI-built pipelines are the named failure modes (TEI-TAXTECH-2026; TR-AUDITOR-2026) |
| Submit and validate invoices and transaction data under clearance or real-time reporting | transaction-processing | Rejection means no legal force for the invoice in clearance regimes (TR-AUDITOR-2026); ViDA timetable (EC-VIDA-2026) |
| Ingest notices and source documents | transaction-processing | Silent extraction errors need independent verification (AICPA-WERFEL-2026) |
| Let agents call tax platforms | software-systems | Authorization, scopes and logging rules (MCP-SPEC-2025; AVALARA-MCP-2026; NIST-CAISI-2026) |
| Govern AI and automation: inventory, policy, KPIs, vendor oversight | review-assurance, coordination-scheduling | COSO six steps (DART-COSO-2026); few departments have policies (TR-GENAI-2025) |

### Common pain points

- Data maturity: 51% of surveyed tax and finance functions are early in data management maturity and 44% name the inability to execute a sustainable data, AI and technology plan as the biggest barrier (EY-TFO-2025).
- Resources: 58% of corporate tax departments call themselves under-resourced (up from 51%), and fewer than half of 170 tax leaders got a budget increase (TR-CORPTAX-2025; TR-CORPTECH-2026).
- Ownership: tax rarely owns AI implementation (two of more than 50 in a TEI poll) and ViDA ownership is unclear across tax, IT and finance (TEI-TAXTECH-2026; TR-VIDA-2026).
- Approvals and data protection: IT approvals (47%), data protection (41%) and lack of knowledge (41%) in a German survey (KPMG-DE-2026).
- Silent failure: AI that fails quietly and politely, and reviewers facing growing volumes of such errors (TEI-TAXTECH-2026).
- Regulators ahead of companies: authorities in mature continuous-transaction-control regimes arrive at audits with the data already analysed (TR-AUDITOR-2026).

### Metrics and benchmarks (what each figure measures)

| Figure | What it measures, in the source's words | Provenance | Ref |
|---|---|---|---|
| 51% | Tax and finance functions in the early stages of data management maturity (1,600 CFOs, senior finance and tax leaders, 30 jurisdictions) | firm survey | EY-TFO-2025 |
| 44% | Respondents saying the inability to execute on a sustainable plan for data, AI and tech is their biggest barrier | firm survey | EY-TFO-2025 |
| 73% / 89% | Respondents prioritising hiring data scientists and tax technology experts / investing in upskilling and reskilling | firm survey | EY-TFO-2025 |
| 71% / 89% / 29% | Tax departments using AI tools (plus 19% preparing) / of those, company-wide standard solutions / specialised tax applications; sample size not stated | firm survey | KPMG-DE-2026 |
| 66% | AI users reporting noticeable time savings; sample size not stated | firm survey | KPMG-DE-2026 |
| 47% / 41% / 41% | Hurdles to further AI: IT approvals / data protection requirements / lack of knowledge | firm survey | KPMG-DE-2026 |
| 46% / 44% | Respondents who already enhanced ERP systems with AI-driven tax analysis tools / plan to; sample not stated | firm survey | DELOITTE-TTT-2025 |
| 77% | Tax leaders requiring 90% or higher accuracy before entrusting AI with tax processes | firm survey | DELOITTE-TTT-2025 |
| 45% / 36% / 33% / 30% / 28% | Barriers: budget / limited AI expertise / lack of clear AI strategy / data security and privacy / insufficient leadership support | firm survey | DELOITTE-TTT-2025 |
| 67% / 57% | Corporate tax departments not using GenAI / of those implementing new technology, plans include GenAI | vendor survey | TR-CORPTAX-2025 |
| 58% (51% prior year) | Departments calling themselves under-resourced | vendor survey | TR-CORPTAX-2025 |
| 31% vs 56% | Departments incurring penalties among respondents spending more than half their time proactively vs reactively | vendor survey | TR-CORPTAX-2025 |
| 15.4% | Average share of a tax department's budget spent on tax technologies and software | vendor survey | TR-CORPTAX-2025 |
| 17% / 21% / 45% | Corporate tax departments with specific AI and data policies / GenAI under general technology policies / no relevant policy | vendor survey | TR-GENAI-2025 |
| 77% / 59% | Business tax departments wanting providers to use GenAI / not sure whether their companies are using it | vendor survey | TR-GENAI-2025 |
| 12.5% / one third / 57.4% | Indirect tax leaders with specific AI targets or KPIs / running formal human-in-the-loop review / not confident AI-assisted decisions hold up to an authority (176 leaders) | vendor survey | FONOA-2026 |
| 86% / 22% | Respondents familiar with ViDA / with a formal transition program | vendor survey | TR-VIDA-2026 |
| 87% / 41% | Bot users experiencing some bot failures / saying ongoing management takes more time and resources than expected (500+ decision makers, 2019, all industries) | vendor survey | PEGA-RPA-2019 |
| fewer than one third | Simplified federal returns computed correctly by frontier models | vendor benchmark | COLUMN-TAXCALCBENCH-2025 |
| over 5% | Increase in reported sales, purchases and VAT liabilities in the first year after e-invoicing, Peru | independent | BELLON-PERU-2022 |
| 9.5% | EU VAT compliance gap in 2023 as a share of the VAT total tax liability | regulator | EC-VATGAP-2025 |

Cross-check: the 2022 BDO article cites a Center for Audit Quality report (June 2024) that tax accounting issues averaged 12% of restatements from 2013 to 2022. This is search-only for the CAQ document and is routed to the provision module (section 4).

### Guardrails and regulatory points

- IRS Rev. Proc. 98-25 (effective for machine-sensible records for tax years beginning after 31 December 1997): records must reconcile to the books and return, carry transaction-level detail, be available and capable of being processed, and be documented including data flow and internal controls (IRS-REVPROC-9825, sections 5.01 and 6). Whether it has been modified since was not checked.
- COSO, Achieving Effective Internal Control Over Generative AI (released 23 February 2026): capability-first taxonomy, control mapping to the five components and 17 principles, six-step roadmap, monitoring of override percentages (JOFA-COSO-2026; DART-COSO-2026). The primary document was not opened.
- NIST AI RMF Generative AI Profile (NIST AI 600-1, July 2024) lists confabulation, data privacy, information integrity and value chain and component integration among generative AI risks (NIST-AI600-1; read in the PDF's risk list, sections 2.2 onward).
- MCP specification (version 2025-11-25) security rules, NIST AI Agent Standards Initiative (17 February 2026) and OWASP agentic Top 10 (9 December 2025) (MCP-SPEC-2025; NIST-CAISI-2026; OWASP-AGENTIC-2025).
- Real-time reporting law: ViDA (Directive (EU) 2025/516; digital reporting from 1 July 2030; alignment by 1 January 2035) and the UK mandate from 2029 (EC-VIDA-2026; UK-EINV-2025).
- Practitioner conduct: IRS OPR Alert 2026-19 applies Circular 230 duties (due diligence, competence, procedures) to practitioners using generative AI (IRS-OPR-2026). It governs practitioners before the IRS, so it reaches in-house departments only indirectly, mainly through the providers they use.
- Risk registers: the AICPA-published Werfel framework has 20 risk areas in four categories and a 15-risk preparer register with controls; AICPA's Council on AI Risk in Tax launched 23 September 2026 to test and refine it (AICPA-WERFEL-2026; AICPA-CART-2026). The framework is not a standard.

### Frontier signals (dated)

- 2025-06-23: A2A protocol contributed to the Linux Foundation (LF-A2A-2025).
- 2025-11-20: OECD FTA commissioners agree to move toward pilots of real-time automated sharing of secure information (OECD-FTA-2025).
- 2025-11-26: UK consultation response: mandatory e-invoicing for all VAT invoices from 2029, roadmap at Budget 2026 (UK-EINV-2025).
- 2025-12-09: MCP contributed to the Linux Foundation's new Agentic AI Foundation; platinum members include Anthropic, Google, Microsoft, OpenAI and Bloomberg (LF-AAIF-2025).
- 2026-02-17: NIST launches the AI Agent Standards Initiative (NIST-CAISI-2026).
- 2026-02-23: COSO releases generative AI internal control guidance (DART-COSO-2026).
- 2026-03-16: tax professionals now expect AI to be a central part of their workflow within one to two years, much sooner than a year earlier (TR-CORPTECH-2026).
- 2026-05: TEI seminar: tools demonstrated live, the question became what AI cannot do; token costs and silent failures raised; regulators described as ahead (TEI-TAXTECH-2026; TR-AUDITOR-2026).
- 2026-07: Deloitte scenario framework tying company AI adoption to authority AI progress (DELOITTE-RIDING-2026).
- Still ahead: UK e-invoicing roadmap at Budget 2026 (date differs across secondary sources); ViDA digital reporting from 2030-07-01 (UK-EINV-2025; EC-VIDA-2026).

### Workforce and role effects

- Hiring and upskilling: 73% prioritise data scientists and tax technology experts, 89% invest in upskilling (EY-TFO-2025); 53% recruit digitally native talent and 94% believe AI skills will be essential within four to five years (DELOITTE-TTT-2025).
- Headcount: 58% of German companies expect constant domestic tax headcount, 72% abroad (KPMG-DE-2026).
- Skills in hiring: 24% consider generative AI skills nice to have in new hires and 2% require them (TR-GENAI-2025).
- Work mix: tax professionals spend 53% of time on routine activities and would like 21% (EY-TFO-2025).
- IRS context (adjacent): staff cuts left the IRS without enough skilled employees for AI, with one unit saying it lost 63 employees who worked on AI (GAO-2026).

### Objections and concerns practitioners raise

- AI fails quietly and politely; reviewing the growing volume of such errors is unresolved (TEI-TAXTECH-2026).
- Governance vacuum: tax rarely owns AI implementation (TEI-TAXTECH-2026).
- Pipelines built in minutes may be unreviewed, undocumented and insecure (TR-AUDITOR-2026).
- Token costs could change the economic case (TEI-TAXTECH-2026).
- Training rollouts fail when users are not consulted (TEI-TAXTECH-2026).
- Trust threshold: 77% want 90% or higher accuracy first (DELOITTE-TTT-2025).
- Defensibility: 57.4% not confident they could defend AI-assisted decisions (FONOA-2026).
- Fee and pricing tension: AICPA has asked the IRS to clarify OPR language on passing AI savings to clients, saying it does not appear to allow value pricing (AICPA-CART-2026). This is a practitioner issue.

### Interview probes for an advisor

1. Who in your company owns AI and automation in tax: tax, IT or finance? Is there an inventory of what runs in tax, and who signs off on a new pipeline?
2. Pick one automated tax data flow. Can you show the documentation that reconciles its output to the ledger and the return, and what happens when the builder leaves?
3. What accuracy or override rate did you set before go-live, and what do you measure now? How many human corrections did you see in the first 90 days?
4. For each real-time reporting or e-invoicing regime you operate in, who owns master data, what is your rejection rate, and what is the cost of a rejected invoice?
5. If an agent can call your tax engine, which scopes does it hold, where are the tool calls logged, and who reviews the logs?

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| Pillar Two readiness: only 21% of EY survey respondents said they are very prepared to comply with Pillar Two reporting requirements; 81% called it the most significant legislative change | international-pillar-two | EY-TFO-2025 |
| Pillar Two as a data constraint for the provision and compliance engines | international-pillar-two and provision | KOGNITOS-2026 |
| Income tax accounting controls: BDO cites a CAQ report (June 2024) that tax accounting issues averaged 12% of restatements, 2013 to 2022, and says tax errors are a common source of material weakness (BDO article read; CAQ figure search-only) | provision | CAQ-RESTATE-2024 |
| Indirect-tax determination and filing agents; the Fonoa survey of 176 indirect tax leaders | indirect-tax | FONOA-2026; AVALARA-MCP-2026 |
| IRS AI use: 126 use cases at June 2025, incomplete inventory, staffing; TIGTA on evaluating model performance; OECD survey that 70% of 54 FTA members use AI tools; Grant Thornton summary of OECD Governing with AI | controversy (tax-authority AI) | GAO-2026; TIGTA-2025; BTAX-OECD-2025; GT-IE-OECDGOV-2025 |
| Circular 230 duties, fees and confidentiality for practitioners; Werfel and CART frameworks | x-guardrails-professional-responsibility | IRS-OPR-2026; AICPA-WERFEL-2026; AICPA-CART-2026 |
| TaxCalcBench, TaxBench and JHU neuro-symbolic work on individual returns | compliance (individual and business) | COLUMN-TAXCALCBENCH-2025; COLUMBIA-TAXBENCH-2026; JHU-TAXREASON-2025 |
| Scenario thinking on company versus authority AI progress | x-state-of-ai-disruption | DELOITTE-RIDING-2026 |

## 5. Sources

Read in full or in the relevant part unless marked search-only. Counts by type: survey 10, regulator 8, press 6, academic 5, standard-setter 4, professional-body 3, firm 3, vendor 3, conference 3 (45 in all; 43 opened, 2 search-only).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| EY-TFO-2025 | EY report indicates CFOs and tax leaders innovating with AI... | EY | survey | https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments | 2025-11-18 | full |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-07 | full |
| KPMG-READINESS-2026 | 2026 KPMG Global Tax Readiness Dividend | KPMG International | survey | https://kpmg.com/xx/en/our-insights/transformation/global-tax-readiness-dividend.html | 2026-06-22 | full (landing page) |
| TR-CORPTAX-2025 | Why most tax departments aren't using AI yet | Thomson Reuters Tax & Accounting | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 | full |
| TR-GENAI-2025 | 5 GenAI tensions corporate tax departments should address | Thomson Reuters Tax & Accounting | survey | https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address | 2025-06-24 | full |
| TR-CORPTECH-2026 | Corporate tax department technology report 2026 | Thomson Reuters Institute with TEI | survey | https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026 | 2026-03-16 | full (summary page) |
| TR-VIDA-2026 | Confident, but not prepared: What the data reveals about ViDA readiness | Thomson Reuters Europe | survey | https://europe.thomsonreuters.com/blog/vida-readiness-europe | 2026-07-03 | full |
| FONOA-2026 | State of Indirect Tax in the AI Era 2026 | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 | full (landing page; report gated) |
| DELOITTE-TTT-2025 | AI-enabled Tax Transformation (Tax Transformation Trends 2025 analysis) | Deloitte Luxembourg | survey | https://www.deloitte.com/lu/en/services/tax/research/ai-enabled-tax-transformation.html | 2025-11-19 | full |
| PEGA-RPA-2019 | Survey: Most Businesses Find RPA Effective But Hard To Deploy and Maintain | Pegasystems | survey | https://www.pega.com/node/80501 | 2019-09-10 | full |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| TR-AUDITOR-2026 | 2026 TEI Tax Technology Seminar: What the auditor already knows | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows | 2026-05-12 | full |
| TEI-TECHTAX-2025 | 2025 TechTAXcelerate: Unleashing the Future of Tax Technology (Webinar Series) | Tax Executives Institute | professional-body | https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series | 2025-11-17 | full |
| SAVANT-TEI-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| KOGNITOS-2026 | AI for Corporate Tax and Provision Automation (2026) | Kognitos | vendor | https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/ | 2026-06-17 | full |
| AVALARA-MCP-2026 | Inside Avalara MCP servers: A developer's primer for agentic tax and compliance | Avalara | vendor | https://www.avalara.com/us/en/blog/avalara-mcp-servers.html | 2026-05-27 | full |
| IRS-REVPROC-9825 | Rev. Proc. 98-25 (retention of machine-sensible records) | Internal Revenue Service | regulator | https://www.irs.gov/pub/irs-drop/rp-98-25.pdf | 1998-03-16 | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| GAO-2026 | Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522) | U.S. GAO | regulator | https://www.gao.gov/products/gao-26-107522 | 2026-03-24 | full (via text mirror; date from landscape) |
| TIGTA-2025 | The IRS Could Leverage Examination Results in AI Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022) | TIGTA | regulator | https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf | 2025-05-19 | full (highlights page) |
| EC-VIDA-2026 | VAT in the Digital Age (ViDA) | European Commission | regulator | https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en | 2026-07-29 | full |
| EC-VATGAP-2025 | VAT gap in Europe - report 2025 | European Commission | regulator | https://taxation-customs.ec.europa.eu/vat-gap_en | 2025-12-11 | full (web page, not the report) |
| UK-EINV-2025 | Promoting electronic invoicing across UK businesses and the public sector (consultation response) | HMRC and Department for Business and Trade | regulator | https://www.gov.uk/government/consultations/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector | 2025-11-26 | full |
| OECD-FTA-2025 | Heads of tax administrations agree further work on collaborative projects... | OECD | regulator | https://www.oecd.org/en/about/news/announcements/2025/11/heads-of-tax-administrations-agree-further-work-on-collaborative-projects-to-reduce-compliance-burdens-and-deepen-co-operation-in-tackling-tax-gaps.html | 2025-11-20 | full (via text mirror) |
| JOFA-COSO-2026 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02-26 | full |
| DART-COSO-2026 | COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up, Vol. 33, Issue 3) | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 | full |
| DELOITTE-RIDING-2026 | Riding the wave: A framework to plan for AI | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 | full |
| GT-IE-OECDGOV-2025 | Governing with AI: The new face of tax authorities | Grant Thornton Ireland | firm | https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/ | 2025-09-19 | full |
| AICPA-WERFEL-2026 | A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and C | AICPA (The Tax Adviser) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 | full (appendices only) |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax (Council on AI Risk in Tax) | The Tax Adviser | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| CAQ-RESTATE-2024 | Financial Restatement Trends in the United States: 2013-2022 | Center for Audit Quality | professional-body | https://thecaq.org/financial-restatement-trends-us-2013-2022 | 2024-06 | search-only (landing page; figure via BDO article, which carries no publication date) |
| NIST-AI600-1 | Artificial Intelligence Risk Management Framework: Generative AI Profile (NIST AI 600-1) | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full (risk list read) |
| NIST-CAISI-2026 | AI Agent Standards Initiative | NIST | standard-setter | https://www.nist.gov/caisi/ai-agent-standards-initiative | 2026-02-17 | full |
| MCP-SPEC-2025 | Model Context Protocol specification 2025-11-25: Security Best Practices and Authorization | Model Context Protocol project | standard-setter | https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices | 2025-11-25 | full |
| OWASP-AGENTIC-2025 | OWASP Top 10 for Agentic Applications for 2026 | OWASP Gen AI Security Project | standard-setter | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | 2025-12-09 | full (landing page only) |
| LF-AAIF-2025 | Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF)... | The Linux Foundation | press | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation | 2025-12-09 | full |
| LF-A2A-2025 | Linux Foundation Launches the Agent2Agent Protocol Project... | The Linux Foundation | press | https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents | 2025-06-23 | full |
| FISCAL-UK-2026 | UK Confirms Peppol for B2B E-Invoicing Mandate from April 2029 | Fiscal Solutions | press | https://www.fiscal-requirements.com/news/5673-uk-confirms-peppol-for-b2b-e-invoicing-mandate-from-april-2029 | 2026-06-29 | full |
| BTAX-OECD-2025 | Tax Authorities Increasingly Use AI in Audits, OECD Report Finds | Bloomberg Tax | press | https://news.bloombergtax.com/daily-tax-report/tax-authorities-increasingly-use-ai-in-audits-oecd-report-finds | 2025-06-17 | full (opening paragraphs) |
| GARTNER-FIN-2025 | Gartner Survey Shows Finance AI Adoption Remains Steady in 2025 | Gartner | press | https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025 | 2025-11-18 | search-only (page blocked; 59% vs 58%, 183 finance leaders, per search summary) |
| BELLON-PERU-2022 | Digitalization to improve tax compliance: Evidence from VAT e-invoicing in Peru | Journal of Public Economics (PMC copy) | academic | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9168443/ | 2022-06 | full |
| IMF-WP-2025-089 | Leveraging Digital Technologies in Boosting Tax Collection | IMF (RePEc record) | academic | https://econpapers.repec.org/paper/imfimfwpa/2025_2f089.htm | 2025-05-09 | full (abstract only) |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | Column Tax (arXiv) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full (abstract) |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning | Johns Hopkins University (arXiv) | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 | full (abstract) |
| COLUMBIA-TAXBENCH-2026 | TaxBench | Columbia DAP Lab | academic | https://daplab.cs.columbia.edu/benchmarks/taxbench/ | 2026-10-16 | full |

Notes on the table: GARTNER-FIN-2025 and CAQ-RESTATE-2024 are the two search-only items; every other row was opened. Rows typed press: Journal of Accountancy, the two Linux Foundation releases, Fiscal Solutions, Bloomberg Tax and Gartner. Search-only figures (Gartner 59% finance AI adoption; CAQ 12%) appear only in notes, never in the outcomes of an A or B entry.

## 6. Gaps

- Independent quality evidence is missing. No source gives an error rate, override rate, parallel-run result or inspection finding for AI in in-house tax data flows, ERP-to-tax mapping or e-invoice validation. The nearest items are a vendor benchmark on individual returns, a 2019 non-tax vendor survey of bot failure and a regime-level study in Peru.
- No independent view of in-house practice: every survey is run by a firm or vendor that sells tax technology or services (EY, KPMG, Deloitte, Thomson Reuters, Fonoa, Pegasystems). Sample sizes were not stated on the pages for KPMG Germany, Deloitte, the Thomson Reuters ViDA blog and the Thomson Reuters corporate tax blogs (the TR corporate technology report gives 170 leaders).
- Not reached or blocked: OECD Tax Administration 2025 body text, OECD Tax Administration 3.0, IMF site, official French, Polish and German e-invoicing pages (impots.gouv.fr, podatki.gov.pl, bundesfinanzministerium.de returned errors or blocks), PCAOB AS 1105, ISO/IEC 42001, Gartner and COSO's own publication. ICAP/tax control framework material was found only as search summaries.
- Landscape items not confirmed on the pages opened: EY's 80% struggling with foundational data and 75% in earliest stages of GenAI (the press release gives 51% and 44% instead); the Deloitte Pillar Two Agent; the gated Thomson Reuters Institute reports. Deloitte's published date is inferred from PDF metadata and its page sample size is not stated.
- Dates: the GAO report date is carried from the landscape; the Rev. Proc. 98-25 date is the bulletin date; the AICPA appendices date is the upload month. The BDO article cited for the CAQ figure carries no publication date, so only the CAQ report is listed. The UK Budget 2026 date is reported inconsistently in secondary sources.
- Unchecked: whether Rev. Proc. 98-25 has since been modified or superseded; whether the Thomson Reuters ViDA survey sample matches the 2026 Corporate Tax Technology Report sample; France, Poland and Spain regime details beyond the TEI account.
- Not found: any tax-specific peer-reviewed study of in-house tax technology, any inspection or enforcement action involving in-house tax data automation, any published override-rate benchmark for tax AI, and any published figure for the cost or token spend of tax agents.
- The practice and discourse angles of this module cover named postings, vendor deployments and conference commentary in more depth. This file leans on their overlapping sources only where they carry a governance point.
