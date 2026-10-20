# AI in advisory FP&A and performance consulting: combined practice, discourse and governance pass

Archetype: advisory. Module: fpa-performance. Run date: 2026-10-20. Wave 5. Angle: combined (practice, discourse, governance and evidence).

## 1. Summary

**Scope and honesty.** Public evidence on AI in FP&A and performance consulting *as delivered by advisory firms to private, middle-market clients* is thin. Most of what exists is firm service pages, vendor alliance announcements, vendor-sponsored surveys and analyst commentary. No advisory firm in this pass published a measured outcome (error rate, override rate, parallel run, forecast accuracy, cycle time) for AI-assisted FP&A work. Sixteen candidate use cases follow: 0 at grade A, 2 at B, 13 at C and 1 at D (an idea). Where a figure appears, its provenance is stated.

**What the evidence supports**

1. **Advisory firms are productising platform-led FP&A.** RSM announced an alliance with Abacum (2026-06-22), CFGI followed (2026-09-05), and Armanino, CohnReznick and Forvis Mazars publish service pages around Abacum, Solver and Workday Adaptive Planning. These are announced offers; none reports a client result.
2. **The only named-firm usage figures are old and vendor-published.** Jirav's October 2024 release names Creative Planning (10 clients to over 200) and Practice Executive (one $40K engagement). Cox Enterprises' before-and-after times come from OneStream's webinar and describe an in-house team, not an advisory engagement.
3. **Independent measurement points the other way on forecasting.** In Gartner's March 2026 survey of 204 finance leaders, financial forecasting and insight generation were among the lowest-rated AI use cases, and 63% said AI implementation was slower than expected in 2025. The FP&A Trends Survey (475 respondents, OneStream-sponsored) found only 22% of teams describe themselves as optimized or performing well; AI users score higher, though OneStream's reading is that they already had stronger data and planning foundations.
4. **Data foundations, not models, are the stated constraint.** RSM (1,030 leaders), Kaufman Rossin (100 decision-makers), OneStream and Intuit all name data quality or integration as the leading barrier. This makes readiness assessment and data work the most consistently supported advisory opening.
5. **Verification is a real cost.** A Datarails (vendor) survey of 270 CFOs and finance leaders reports an average 26% of work time spent checking AI output; 75% cite lack of auditability as a reason to hold back.
6. **Independence shapes the offer.** For audit clients of SEC registrants, Regulation S-X lists financial information systems design and implementation and management functions among services that impair independence (unless results are not subject to audit procedures). CFGI markets itself as free of that constraint. The AICPA rules for private-company audit clients were not checked.
7. **Managed FP&A is the model shift to watch.** ISG's September 2026 quadrant says consulting and accounting firms are increasing their role in managed services and lists outcome-based pricing as a leading indicator; the profiled providers are mainly Big Four and outsourcing firms.

**Correction to the landscape file.** The landscape (item 4 of its summary) says the 42% 'fully assurance ready' figure in CPAPA-AGENTSCLOSE-2026 may be conflated with another KPMG figure. KPMG's own release (KPMG-AIFINANCE-2026) states both: fewer than half of organisations (42%) are fully assurance-ready for AI-enabled finance processes, and, separately, assurance-ready organisations report 42% confidence in scaling AI versus 14% for others. The CPA Practice Advisor article's use is consistent with the release.


## 2. Use cases

```yaml
- id: advisory-fpa-performance-01
  title: AI-drafted variance and flux commentary for management and board reporting
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - data-reporting
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Variance explanations and performance narratives are written by hand, late in the reporting cycle. In the 2026 FP&A Trends Survey, teams reported spending 47% of their time on data collection and validation and 32% on insight generation.
  solution: AI features inside planning and reporting platforms (the sources name Solver Copilot and Abacum's narrative layer) draft variance summaries, flag outliers and propose root causes from the planning model. An analyst or advisor reviews and edits before anything reaches management or a board. Pigment's page says it plans agent-based drafting of monthly budget variance analysis (planned, not shipped).
  outcomes:
  - lever: capacity
    description: An unnamed CFO of a global media and information services firm said a flux analysis agent, built in three weeks, took variance commentary from 40 people manually producing it to five people reviewing and refining the agent's output.
    figure: 40 people to 5 people
    measures: People manually producing monthly variance commentary, before and after, as recalled by the CFO in a KPMG article; the organisation is not named and no method is given
    provenance: self-reported
    source_ref: KPMG-CFOREMODEL-2026
  - lever: quality
    description: In Gartner's March 2026 survey of 204 finance leaders, financial forecasting and insight generation were among the lowest-rated AI use cases.
    figure: none (ranking only)
    measures: Ratings of realized versus expected value by AI use case; the release gives no percentage for these use cases
    provenance: independent
    source_ref: GARTNER-AIREPORTCARD-2026
  - lever: cost
    description: Finance teams reported spending an average of 26% of their working time verifying or correcting AI-generated finance outputs.
    figure: 26%
    measures: Average share of work time spent verifying or correcting AI-generated finance outputs, among 270 CFOs and finance leaders in a Datarails (vendor) survey; 96% of respondents spent at least 10%
    provenance: vendor-published
    source_ref: CFODIVE-DATARAILS-2026
  prerequisites:
  - Actuals, plan and driver data already consolidated in one model (only 19% of FP&A teams rate their data quality advanced)
  - Agreed variance thresholds and commentary templates
  - A reviewer who knows the client's business
  risks_and_guardrails:
  - 'Unreviewed AI output is a professional liability: Deloitte Australia agreed to repay the final instalment of a roughly AU$440,000 contract after a report was found to contain incorrect footnotes and references, and the updated report disclosed generative AI use (CITYAM-DELOITTE-2025).'
  - A practitioner checklist says agent output feeding the financial statements needs a human approval step whose depth scales with materiality, and that evidence should be replayable (CPAPA-AGENTSCLOSE-2026, controls 2 and 3).
  - Vendor time-saving claims are marketing until a client's own data reproduces them (CPAPA-AGENTSCLOSE-2026, control 2).
  human_checkpoints:
  - Analyst checks each drafted explanation against the ledger and the business context
  - Named reviewer signs off before the pack goes to the client or board
  role_evolution: KPMG's Erin McShane sees AI supporting FP&A, spreadsheet modelling, data extraction and variance commentary, with talent needs moving from a reporting factory toward interpreting AI outputs and advising leaders (KPMG-CFOREMODEL-2026).
  evidence_grade: C
  sources:
  - ref: KPMG-CFOREMODEL-2026
    title: CFOs remodel the finance function for an AI-driven world
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2026/cfo-remodel-finance-function-ai-driven-world.html
    date: '2026-09-29'
    access: full
    locator: Section 'The AI maturity spectrum', CFO of a global media and information services firm; Erin McShane paragraph
  - ref: GARTNER-AIREPORTCARD-2026
    title: Gartner Says CFOs Must Stop Mistaking Finance AI Deployment for Value Creation
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation
    date: '2026-05-28'
    access: full
    locator: Paragraph 'Report Card Shows Progress and Value Gaps'
  - ref: CFODIVE-DATARAILS-2026
    title: 'AI verification eats up 26% of finance teams'' workweek: Datarails'
    publisher: CFO Dive
    type: survey
    url: https://www.cfodive.com/news/ai-verification-eats-26percent-finance-teams-workweek-datarails/832210/
    date: '2026-10-06'
    access: full
    locator: Dive Brief paragraphs 1-2
  - ref: FORVIS-SOLVER-2026
    title: Elevate Financial Reporting in Business Central With Solver (webinar slide deck)
    publisher: Forvis Mazars US
    type: firm
    url: https://www.forvismazars.us/getattachment/b4a1114e-4173-4e2a-b632-6b1b4aecea5d/Elevate-Financial-Reporting-in-Business-Central-With-Solver.pdf
    date: '2026-07-23'
    access: full
    locator: 'Slide ''Analysis Agent: Solver Copilot'' (root cause analysis on variances, narrative summaries); title slide dated July 23, 2026'
  - ref: ABACUM-INTELLIGENCE-2026
    title: Abacum Rethinks AI for Finance with the Launch of Abacum Intelligence, a Platform-Wide Intelligence Layer
    publisher: Abacum
    type: vendor
    url: https://abacum.ai/newsroom/abacum-rethinks-ai-for-finance-with-the-launch-of-abacum-intelligence-a-platform-wide-intelligence-layer
    date: '2026-04-09'
    access: full
    locator: Bullet 'Narrative Intelligence'
  - ref: ARMANINO-SOLVER-2026
    title: Solver Financial Planning and Analysis Software
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/software/solver/
    date: '2026'
    access: full
    locator: Section 'Make Smarter Decisions With AI'
  - ref: PIGMENT-AI-2026
    title: 'Introducing Pigment AI: Smarter Planning Tools'
    publisher: Pigment
    type: vendor
    url: https://www.pigment.com/blog/ai-launch
    date: '2026-09-03'
    access: full
    locator: Key takeaways, last bullet (planned monthly Budget Variance Analysis)
  - ref: ONESTREAM-FPAWEBINAR-2026
    title: '2026 FP&A trends: How AI is testing the foundations of Finance (webinar page with full transcript)'
    publisher: OneStream and FP&A Trends Group
    type: conference
    url: https://www.onestream.com/resources/2026-fp-and-a-trends-replay-webinar/
    date: '2026-07-09'
    access: full
    locator: Transcript, time-allocation segment (47% and 32%; 19% data quality advanced)
  - ref: CITYAM-DELOITTE-2025
    title: Deloitte refunds Australian government after AI 'made up citations' in report
    publisher: City A.M.
    type: press
    url: https://www.cityam.com/?p=2367690
    date: '2025-10-06'
    access: full
    locator: Paragraphs on the DEWR report, the refund and the generative AI disclosure
  - ref: CPAPA-AGENTSCLOSE-2026
    title: 'Before You Let the Agents Run the Close: Five Controls to Put in Writing First'
    publisher: CPA Practice Advisor (author Anthony L. Fulmore Sr., Texas A&M University-Central Texas)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/
    date: '2026-08-13'
    access: full
    locator: Controls 2 and 3
  - ref: RILLET-SERIESB-2025
    title: Rillet raises $70M Series B from Andreessen Horowitz and ICONIQ
    publisher: Rillet
    type: vendor
    url: https://rillet.com/blog/fundraise-announcement/
    date: '2025-08-06'
    access: full
    locator: Paragraph naming Armanino (top 20) and Wiss (top 50) as partners
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Forvis Mazars US (top-100, mid-market) and Armanino (described as a top-20 firm in Rillet''s release) deliver Solver; Abacum and Pigment are vendors. The Forvis Mazars deck is a webinar showing a tool, not a client deployment. The only figure that sounds like a measurement is anonymous and recalled, so the grade is C. No named advisory firm published an override rate, edit rate or error rate for AI-drafted commentary. For audit clients of SEC registrants, see the independence note in the module notes.'
- id: advisory-fpa-performance-02
  title: Client cash-flow and budget forecasts generated by AI inside planning software, with the firm's judgment layered on top
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'The vendor describes client forecasting as a weeks-long process: strategic discussion with the client, then trained staff building driver-based models.'
  solution: Jirav Intelligent Forecasting (JIF) uses AI and machine learning to generate a forward-looking cash-flow forecast from a client's historical data. The firm then adds its own market intelligence and client knowledge as further forecasts. Jirav says driver-based models built by skilled FP&A staff remain appropriate for some clients.
  outcomes:
  - lever: growth
    description: The owner of Practice Executive, a firm named in Jirav's release, said JIF insights 'already led to a $40K engagement with one of our clients'.
    figure: $40K engagement (one client)
    measures: Fee of one client engagement that the firm's owner attributes to JIF-derived insights, quoted in a vendor press release; no tracked metric
    provenance: vendor-published
    source_ref: JIRAV-JIF-2024
  - lever: capacity
    description: Creative Planning, named as an early adopter, 'initially included JIF for 10 clients' and increased use to over 200 clients, per the release.
    figure: 10 clients to over 200 clients
    measures: Number of clients for which the firm used JIF, as stated in the vendor's release; the date of the increase is not given
    provenance: vendor-published
    source_ref: JIRAV-JIF-2024
  prerequisites:
  - Several periods of clean historical ledger data in the client's accounting system
  - A planning-software subscription (Jirav is CPA.com's preferred planning partner per the release)
  - A CAS or advisory team able to add client-specific forecasts
  risks_and_guardrails:
  - No accuracy, back-test or error figure for JIF was published in the sources read.
  - The vendor itself says some clients still need driver-based models built by skilled staff (JIRAV-JIF-2024, section 'Customizable and Ready for Growth').
  human_checkpoints:
  - Advisor reviews the machine forecast and layers on firm and client knowledge before presenting it
  role_evolution: Jirav's CEO says the tool lets firms scale advisory services without increasing headcount; this is a vendor statement (JIRAV-JIF-2024, 'Scaling Advisory Services Without Adding Staff').
  evidence_grade: B
  sources:
  - ref: JIRAV-JIF-2024
    title: Accounting Firms Accelerate Growth with AI-powered Jirav Intelligent Forecasting (JIF)
    publisher: Jirav
    type: vendor
    url: https://jirav.com/press-releases/jirav-artificial-intelligence-transforms-cas-practices
    date: '2024-10-03'
    access: full
    locator: Paragraph quoting Andrew Tucker (Practice Executive); paragraph on Creative Planning (Chris Gallo); section 'Customizable and Ready for Growth'
  - ref: JIRAV-CEO-2024
    title: Jirav Announces Michael Morrison as CEO and Launches New Artificial Intelligence Forecasting Product
    publisher: Jirav (Business Wire, via Silicon UK)
    type: vendor
    url: https://www.silicon.co.uk/press-release/jirav-announces-michael-morrison-as-ceo-and-launches-new-artificial-intelligence-forecasting-product
    date: '2024-09-17'
    access: full
    locator: Paragraph describing JIF as an AI product that instantaneously creates a forward-looking cash flow forecast
  - ref: INTUIT-ACCTTECH-2026
    title: 'The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future'
    publisher: CPA Practice Advisor (reporting Intuit QuickBooks survey)
    type: survey
    url: https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807
    date: '2026-07-02'
    access: full
    locator: 'Paragraph on AI adoption: financial forecasting named by 51% as a top client-service use'
  last_reviewed: '2026-10-20'
  notes: 'Firm type: small and mid-size CAS firms; their ranks were not checked. Vendor: Jirav. Grade B, not A: the figures are quotes and counts in a vendor press release, not a tracked metric reported by the firm. Both sources are 2024, older than the 18-month window, and no later follow-up was found. The Intuit survey shows financial forecasting among the most common client-service uses of AI (51% of respondents in a 725-person sample of US accounting and bookkeeping professionals; the article does not state the denominator for the use list), but names no firms.'
- id: advisory-fpa-performance-03
  title: Natural-language reporting, document search and document-analysis agents inside the planning platform
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - data-reporting
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: 'Per OneStream''s account of Cox Enterprises: manual friction in finance, ad hoc reports built by hand, answers buried in documentation, and contracts reviewed line by line.'
  solution: 'Three agents in the planning platform: a finance analyst agent turns natural-language requests into governed reports; a search analyst agent returns cited answers from approved finance documentation; a deep analysis agent reads and structures large documents such as contract batches. Abacum and Pigment market similar natural-language interfaces to business users.'
  outcomes:
  - lever: speed
    description: Time per ad hoc report fell from 10 minutes to one minute.
    figure: 90% reduction
    measures: Time per ad hoc report before and after, as presented by OneStream's product marketing lead for Cox during a private preview; method not stated
    provenance: vendor-published
    source_ref: ONESTREAM-FPAWEBINAR-2026
  - lever: speed
    description: Time per document lookup fell from eight minutes to 30 seconds.
    figure: 94% reduction
    measures: Time per lookup of approved finance documentation, before and after, as presented by OneStream; method not stated
    provenance: vendor-published
    source_ref: ONESTREAM-FPAWEBINAR-2026
  - lever: speed
    description: Before, a contract batch (agreements of 2 to 30 pages each) took almost half an hour to 10 hours; the presenter reports a 67% to 98% reduction in time after.
    figure: 67% to 98% reduction
    measures: Time per contract batch before and after, as presented by OneStream; the transcript wording on the after-time is unclear and the range is as stated by the presenter
    provenance: vendor-published
    source_ref: ONESTREAM-FPAWEBINAR-2026
  prerequisites:
  - Cox already had actuals, plans and consolidations in one platform
  - Cross-functional discovery of pain points, with use cases ranked by impact
  - Success criteria set up front (accuracy, efficiency, trust by design); the presenter describes a six-month process
  risks_and_guardrails:
  - In the FP&A Trends poll, data quality was the single largest barrier to deploying AI agents (35% per the webinar) (ONESTREAM-FPAWEBINAR-2026).
  - The presenter says agents showed their thought process and linked sources, which built trust with Cox's finance team (ONESTREAM-FPAWEBINAR-2026).
  human_checkpoints:
  - Users can inspect the sources and steps the agent used before relying on an answer
  role_evolution: OneStream says the agents free finance staff for insight work; a vendor statement. Pigment's page quotes an FP&A director at Uberall expecting the tool to reduce time spent answering simple stakeholder questions (PIGMENT-AI-2026).
  evidence_grade: B
  sources:
  - ref: ONESTREAM-FPAWEBINAR-2026
    title: '2026 FP&A trends: How AI is testing the foundations of Finance (webinar page with full transcript)'
    publisher: OneStream and FP&A Trends Group
    type: conference
    url: https://www.onestream.com/resources/2026-fp-and-a-trends-replay-webinar/
    date: '2026-07-09'
    access: full
    locator: Transcript, the Cox Enterprises segment (before-and-after figures and the six-month discovery process)
  - ref: ABACUM-INTELLIGENCE-2026
    title: Abacum Rethinks AI for Finance with the Launch of Abacum Intelligence, a Platform-Wide Intelligence Layer
    publisher: Abacum
    type: vendor
    url: https://abacum.ai/newsroom/abacum-rethinks-ai-for-finance-with-the-launch-of-abacum-intelligence-a-platform-wide-intelligence-layer
    date: '2026-04-09'
    access: full
    locator: Bullets 'Narrative Intelligence' and 'Workflow Intelligence'
  - ref: PIGMENT-AI-2026
    title: 'Introducing Pigment AI: Smarter Planning Tools'
    publisher: Pigment
    type: vendor
    url: https://www.pigment.com/blog/ai-launch
    date: '2026-09-03'
    access: full
    locator: Key takeaways; quote from Eda Karael, FP&A Director, Uberall
  last_reviewed: '2026-10-20'
  notes: This is an in-house deployment at a very large private company ($23B revenue per the presenter) on a vendor platform, not an advisory-firm engagement. Evidence is adjacent to the module, so the grade is capped at B. The figures are vendor-published and the method is not shown, so they do not meet the grade A rule. Abacum separately says 60% of its customers use its AI layer daily and that there were 10,000+ agent interactions in Q1 2026; these are unnamed-customer vendor claims and are not used as outcomes. Advisory firms (RSM, CFGI, Armanino) sell the implementation of such platforms; see use case 04.
- id: advisory-fpa-performance-04
  title: Advisory firms add AI-native or AI-embedded planning platforms to their FP&A implementation and managed-service portfolio
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - software-systems
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Planning, budgeting and forecasting still run on spreadsheets and legacy tools. Armanino's white paper describes budgets emailed as spreadsheets to dozens of people, then consolidated by hand, with no audit trail or role-based access.
  solution: 'Firms pair a planning platform that has AI built in with their own FP&A and CPM implementation practice. Examples in the sources: RSM with Abacum (alliance announced 2026-06-22), CFGI with Abacum (announced 2026-09-05), Armanino listing Abacum and Solver, CohnReznick with Workday Adaptive Planning, and Forvis Mazars with Solver on Business Central. Offers cover continuous forecasting, scenario analysis, rolling plans and support for training and change management.'
  outcomes:
  - lever: speed
    description: CohnReznick's page says to 'accelerate planning and reporting cycle times by 50-70%' with Workday Adaptive Planning solutions.
    figure: 50-70%
    measures: Reduction in planning and reporting cycle times that a firm service page attributes to a vendor's platform; baseline, sample and method not stated
    provenance: vendor-published
    source_ref: COHNREZNICK-WORKDAY-2026
  prerequisites:
  - Data readiness assessed before implementation (CohnReznick says it evaluates whether data is accurate, accessible and structured first)
  - Integration with the client's ERP or ledger
  - Testing, training and change management (RSM)
  risks_and_guardrails:
  - An analyst report says AI messaging is becoming similar across providers and proof of adoption and realised outcomes will become the differentiator (ISG-FAOFPA-2026, Executive Summary, paragraph beginning 'Providers are adapting their portfolios').
  - In-house finance teams in a March 2026 Gartner survey of 204 leaders said AI implementation was slower than expected in 2025 (63%) (GARTNER-AIREPORTCARD-2026).
  - 'Independence: for audit clients of SEC registrants, Regulation S-X lists financial information systems design and implementation, and management functions, among services that impair independence unless the results will not be subject to audit procedures (SEC-REGSX-2026). CFGI says it is free of auditor independence constraints (CFGI-FINEFFECTIVENESS-2026).'
  human_checkpoints:
  - Advisors design and validate the model structure
  - Users are trained to interpret AI-supported insights and apply professional judgment (CohnReznick)
  role_evolution: RSM's Megan Riley frames transformation as people, process and technology working together, and says RSM sees strong demand for AI-enabled FP&A (ABACUM-RSM-2026). Abacum says it expects practitioners to stay in the loop, supported by the technology rather than replaced; a vendor statement.
  evidence_grade: C
  sources:
  - ref: ABACUM-RSM-2026
    title: Abacum and RSM Announce Strategic Alliance to Deliver AI-Native FP&A to High-Growth Finance Teams
    publisher: Abacum
    type: vendor
    url: https://www.abacum.ai/blog/abacum-and-rsm-announce-strategic-alliance-to-deliver-ai-native-fp-a-to-high-growth-finance-teams
    date: '2026-06-22'
    access: full
    locator: Announcement paragraphs; quote from Megan Riley, Partner, Data & Digital Services, RSM
  - ref: RSM-ABACUM-2026
    title: AI native financial planning and analysis, delivered by RSM (Abacum solutions)
    publisher: RSM US LLP
    type: firm
    url: https://rsmus.com/services/digital-transformation/abacum-solutions.html
    date: '2026-09-30'
    access: full
    locator: Sections 'AI-native planning at scale', 'Continuous planning and forecasting'; closing list of benefits
  - ref: ABACUM-CFGI-2026
    title: Abacum and CFGI Partner to Bring AI-Native FP&A to Strategic Advisory
    publisher: Abacum
    type: vendor
    url: https://www.abacum.ai/blog/abacum-and-cfgi-partner-to-bring-ai-native-fp-a-to-strategic-advisory
    date: '2026-09-05'
    access: full
    locator: Paragraphs on CFGI's AI-Enabled Finance practice and the planning-layer alliance; 'About CFGI'
  - ref: CFGI-FINEFFECTIVENESS-2026
    title: Finance Effectiveness (Assess, Design, Build, Optimize)
    publisher: CFGI
    type: firm
    url: https://www.cfgi.com/finance-effectiveness
    date: '2026'
    access: full
    locator: '''No audit restrictions'' line; lifecycle and Phase 0 description'
  - ref: ARMANINO-FPA-2026
    title: Financial Planning & Analysis Services
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/software/financial-planning-analysis/
    date: '2026'
    access: full
    locator: Section 'Financial Planning & Analysis Solutions' (Abacum)
  - ref: ARMANINO-FPAROADMAP-2025
    title: 'FP&A Transformation: How to Evolve Your Financial Planning & Analysis'
    publisher: Armanino Advisory LLC
    type: firm
    url: https://www.armanino.com/white-papers/fpa-transformation-roadmap/
    date: '2025-06-30'
    access: full
    locator: Section 'How Did FP&A Become So Complex?'
  - ref: COHNREZNICK-WORKDAY-2026
    title: Workday Alliance | CohnReznick Digital Advisor
    publisher: CohnReznick
    type: firm
    url: https://www.cohnreznick.com/services/advisory/digital/digital-alliance-workday-adaptive-planning
    date: '2026'
    access: full
    locator: Section 'AI Planning with Workday Adaptive Planning'; data-readiness section
  - ref: FORVIS-SOLVER-2026
    title: Elevate Financial Reporting in Business Central With Solver (webinar slide deck)
    publisher: Forvis Mazars US
    type: firm
    url: https://www.forvismazars.us/getattachment/b4a1114e-4173-4e2a-b632-6b1b4aecea5d/Elevate-Financial-Reporting-in-Business-Central-With-Solver.pdf
    date: '2026-07-23'
    access: full
    locator: Objectives and 'What is Solver?' slides
  - ref: ISG-FAOFPA-2026
    title: 'ISG Provider Lens Finance and Accounting Outsourcing (FAO) Services 2026: Financial Planning & Analysis quadrant report'
    publisher: Information Services Group (ISG), copy hosted by PwC
    type: survey
    url: https://www.pwc.com/gx/en/about/analyst-relations/financial-planning-and-analysis.pdf
    date: 2026-09
    access: full
    locator: Executive Summary, paragraph beginning 'Providers are adapting their portfolios'
  - ref: GARTNER-AIREPORTCARD-2026
    title: Gartner Says CFOs Must Stop Mistaking Finance AI Deployment for Value Creation
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation
    date: '2026-05-28'
    access: full
    locator: Paragraph 'Report Card Shows Progress and Value Gaps'
  - ref: SEC-REGSX-2026
    title: 17 CFR 210.2-01 Qualifications of accountants (current eCFR text)
    publisher: U.S. Securities and Exchange Commission (via eCFR)
    type: regulator
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.2-01
    date: '2026-10-01'
    access: full
    locator: (c)(4)(ii) and (c)(4)(vi)
  last_reviewed: '2026-10-20'
  notes: 'Firm types: RSM, CohnReznick, Forvis Mazars (FY2025 revenue $2.24B per its deck) and Armanino are large mid-market or top-100 firms; CFGI is described by Abacum as a portfolio company of Carlyle and CVC (PE-backed advisory platform that does not audit); Abacum, Workday and Solver are vendors. These are announced alliances and service pages. No client outcome, implementation time or forecast accuracy figure was published by any of the firms. Reg S-X applies to auditors of SEC registrants; the AICPA rules for private-company audit clients were not checked.'
- id: advisory-fpa-performance-05
  title: AI readiness and data-foundation assessment, with a prioritised use-case roadmap, for client finance functions
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Mid-market clients use AI widely but have not made it work at scale, and the barriers named most often are data quality and integration rather than the models.
  solution: 'Advisory teams run a structured diagnostic before building: activity surveys, stakeholder interviews, a maturity assessment, benchmarking and prioritised recommendations (CFGI''s five-week Phase 0), AI strategy assessments that align leaders on vision, rank finance use cases and define a phased roadmap (CFGI''s job posting), data-readiness checks before implementation (CohnReznick) and maturity modelling to find where AI helps most (Cherry Bekaert, 2024).'
  outcomes:
  - lever: quality
    description: 'No firm-side outcome was published. Demand-side context: among organisations reporting moderate or limited AI pilot success, 53% named data quality issues and 47% integration challenges as leading barriers to scaling AI.'
    figure: 53% and 47%
    measures: Share of respondents with moderate or limited pilot success naming each barrier, in an RSM survey of 1,030 senior business leaders; the subgroup size is not stated in the release
    provenance: self-reported
    source_ref: RSM-MMAI-2026
  - lever: risk
    description: In the FP&A Trends poll, data quality was the number one barrier to deploying AI agents.
    figure: 35%
    measures: Share of FP&A professionals naming data quality as the single largest barrier to deploying AI agents, as read out in the webinar; poll size not stated
    provenance: vendor-published
    source_ref: ONESTREAM-FPAWEBINAR-2026
  prerequisites:
  - Access to client process data and time-allocation information
  - Client sponsor willing to act on findings
  risks_and_guardrails:
  - OneStream's presenter warns that putting AI on poor data 'automates the mess faster'; this is a vendor view (ONESTREAM-FPAWEBINAR-2026).
  - Only 19% of surveyed FP&A teams say they have formal AI governance in place and ready to scale (ONESTREAM-FPAWEBINAR-2026).
  human_checkpoints:
  - Executive working sessions agree vision and priorities
  - Findings reviewed with finance leadership before any build
  role_evolution: CFGI's posting seeks a managing director with 12 or more years of experience to lead AI strategy assessments, build proprietary finance tools and accelerators, and take them to market (CFGI-JOB-2026).
  evidence_grade: C
  sources:
  - ref: CFGI-FINEFFECTIVENESS-2026
    title: Finance Effectiveness (Assess, Design, Build, Optimize)
    publisher: CFGI
    type: firm
    url: https://www.cfgi.com/finance-effectiveness
    date: '2026'
    access: full
    locator: Sections on AI Assessment & Design and the five-week Phase 0 assessment
  - ref: CFGI-JOB-2026
    title: Data and AI - Managing Director (job posting, Finance Effectiveness practice)
    publisher: CFGI (listing on Built In Austin)
    type: job-posting
    url: https://www.builtinaustin.com/job/data-and-ai-managing-director/9295428
    date: '2026-06-03'
    access: full
    locator: Role description paragraphs 1-3 and qualifications
  - ref: COHNREZNICK-WORKDAY-2026
    title: Workday Alliance | CohnReznick Digital Advisor
    publisher: CohnReznick
    type: firm
    url: https://www.cohnreznick.com/services/advisory/digital/digital-alliance-workday-adaptive-planning
    date: '2026'
    access: full
    locator: Data-readiness paragraph
  - ref: CBH-FINANCEFUTURE-2024
    title: 'AI and Advanced Analytics: The Finance Function of the Future'
    publisher: Cherry Bekaert
    type: firm
    url: https://www.cbh.com/insights/articles/ai-and-advanced-analytics-the-finance-function-of-the-future/
    date: '2024-06-10'
    access: full
    locator: Sections 'AI and Data Readiness' and maturity modelling
  - ref: RSM-MMAI-2026
    title: 'RSM Survey: The Middle Market Has Embraced AI. Now Comes the Hard Part.'
    publisher: RSM US LLP
    type: survey
    url: https://rsmus.com/newsroom/2026/rsm-survey-middle-market-embraced-ai-now-comes-hard-part.html
    date: '2026-07-21'
    access: full
    locator: Section 'AI Passed the Test'
  - ref: KAUFMANROSSIN-AIMIDMARKET-2026
    title: 94% of mid-market companies use generative AI, but few have what it takes to scale (The State of Artificial Intelligence in the Mid-Market)
    publisher: Kaufman Rossin
    type: survey
    url: https://kaufmanrossin.com/news/ai-in-the-middle-market-press-release/
    date: '2026-05-14'
    access: full
    locator: Paragraphs 1-3 (94%, 83%, 2%)
  - ref: ONESTREAM-FPAWEBINAR-2026
    title: '2026 FP&A trends: How AI is testing the foundations of Finance (webinar page with full transcript)'
    publisher: OneStream and FP&A Trends Group
    type: conference
    url: https://www.onestream.com/resources/2026-fp-and-a-trends-replay-webinar/
    date: '2026-07-09'
    access: full
    locator: Transcript segments on data quality and the AI-readiness poll
  - ref: GARTNER-TALENT-2026
    title: Gartner Survey Reveals Acquiring and Developing AI and Digital Talent Is CFOs' Top Near-Term Challenge
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/newsroom/press-releases/2026-03-23-gartner-survey-reveals-acquiring-and-developing-ai-and-digital-talent-is-cfos-top-near-term-challenge
    date: '2026-03-23'
    access: full
    locator: Paragraph on 'The CFO's Guide to Building a Finance AI Roadmap'
  last_reviewed: '2026-10-20'
  notes: 'Firm types: CFGI (PE-backed advisory platform; says it is free of auditor independence constraints), CohnReznick and Cherry Bekaert (top-100 firms), RSM and Kaufman Rossin (top-50 CPA and advisory firm per its release) as survey publishers. Kaufman Rossin''s mid-market survey (100 decision-makers, December 2025) found 94% use generative AI, 83% had moved to deliberate trials or embedded processes and 2% had operationalised AI at scale. The CFGI posting was open from 2026-06-03 to 2026-06-12 per its structured data, so it shows a practice being built, not delivered engagements.'
- id: advisory-fpa-performance-06
  title: Advisory partners enable and govern native AI agents inside mid-market ERP (Sage Intacct, Microsoft, NetSuite)
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: ERP vendors now ship AI assistants and agents on a quarterly cadence. Clients need someone to decide which to turn on, configure roles and permissions, and connect them to workflows.
  solution: Partner firms run release webinars and write-ups and offer agent services. Armanino's August 12, 2026 deck says Sage Intacct's Finance Intelligence Agent is being rolled out to all customers 'this summer and fall' (phased early adopter) and describes a marketplace of Sage-certified partner agents with an admin console and role-based access. EisnerAmper's write-up covers the same release. Rand Group says it helps enable native agents in Microsoft, NetSuite and Sage products and build custom agents.
  outcomes:
  - lever: capacity
    description: none published for the advisory service
    figure: none
    measures: 'Not applicable: the sources describe product releases and service offers, with no client results'
    provenance: vendor-published
    source_ref: ARMANINO-INTACCTR3-2026
  prerequisites:
  - Admin configuration of each agent in the client's environment
  - Roles and permissions that limit who can call an agent
  - Data quality in the ledger (the agents answer from it)
  risks_and_guardrails:
  - GRF CPAs & Advisors says the strongest parts of Intacct's 2026 Release 2 are usability gains in day-to-day work rather than headline AI alone (GRF-INTACCTR2-2026).
  - Many agentic close tools are subservice organisations in SOC terms, and a practitioner article says AICPA guidance on AI in SOC reporting had not yet been published, so existing SOC reports may be silent on AI components (CPAPA-AGENTSCLOSE-2026, control 4).
  human_checkpoints:
  - Administrator enables each agent and sets role access
  - Marketplace agents are certified by the vendor through a technical, security and legal process (Armanino deck)
  role_evolution: Implementation partners shift from module configuration toward choosing, governing and connecting agents; the sources show the offer, not a measured change.
  evidence_grade: C
  sources:
  - ref: ARMANINO-INTACCTR3-2026
    title: 'Sage Intacct 2026 Release 3: Latest Updates (webinar deck)'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/-/media/pdf/webinars/2026/sage-intacct-2026-r3-release-overview.pdf
    date: '2026-08-12'
    access: full
    locator: 'Slides ''Sage AI and Automation'': Finance Intelligent Agent phased early adopter; ''Discover and Use AI Agents in Sage Intacct'''
  - ref: EISNERAMPER-INTACCTR3-2026
    title: Sage Intacct 2026 R3 Release Delivers New AI and AP Enhancements
    publisher: EisnerAmper
    type: firm
    url: https://www.eisneramper.com/insights/sage-intacct-insights/sage-intacct-2026-r3-release-ai-ap-enhancements-0826/
    date: '2026-08-26'
    access: full
    locator: Section 'Discover and Use AI Agents in Sage Intacct'
  - ref: GRF-INTACCTR2-2026
    title: 'Sage Intacct 2026 Release 2: AI and Real-Time Finance Insights'
    publisher: GRF CPAs & Advisors
    type: firm
    url: https://www.grfcpa.com/resource/sage-intacct-2026-release-2-ai-and-real-time-finance-insights/
    date: '2026-06-11'
    access: full
    locator: Opening paragraph
  - ref: RAND-AGENTS-2026
    title: AI agent services for ERP and CRM
    publisher: Rand Group
    type: firm
    url: https://www.randgroup.com/software-engineering/ai-machine-learning/ai-agents/
    date: '2026-09-09'
    access: full
    locator: Opening paragraphs
  - ref: GARTNER-TECHPORTFOLIO-2026
    title: Gartner Predicts by 2029, CFOs Who Implement Strategic AI Deployment Will Add 10 Margin Points of Growth
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartnerpredicts-by-2029-cfos-who-implement-strategic-ai-deploymnt-will-add-10-margin-points-of-growth
    date: '2026-04-28'
    access: full
    locator: Paragraphs on cloud ERP and embedded AI
  - ref: ACCOUNTEX-2026
    title: 'Accountex London 2026: product roundup'
    publisher: Financial Accountant (IFA)
    type: press
    url: https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/
    date: '2026-05-19'
    access: full
    locator: Paragraph on Sage Intacct Advisory update
  - ref: CPAPA-AGENTSCLOSE-2026
    title: 'Before You Let the Agents Run the Close: Five Controls to Put in Writing First'
    publisher: CPA Practice Advisor (author Anthony L. Fulmore Sr., Texas A&M University-Central Texas)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/
    date: '2026-08-13'
    access: full
    locator: Control 4
  - ref: RILLET-SERIESB-2025
    title: Rillet raises $70M Series B from Andreessen Horowitz and ICONIQ
    publisher: Rillet
    type: vendor
    url: https://rillet.com/blog/fundraise-announcement/
    date: '2025-08-06'
    access: full
    locator: Paragraph naming Armanino (top 20) as a partner
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Armanino (described as top 20 in Rillet''s release), EisnerAmper and GRF CPAs & Advisors (US accounting and advisory firms; ranks not checked), Rand Group (technology consultancy); Sage is the vendor. Gartner''s April 2026 release (314 organisations, September-October 2025) says cloud ERP adoption rose 7% year over year and embedded AI is gaining momentum in cloud ERP; Gartner''s figures describe in-house technology portfolios, not advisory work. A search-result summary of Sage''s releases was not verified against Sage''s own pages.'
- id: advisory-fpa-performance-07
  title: Partner-delivered implementation of AI-native ERP for mid-market finance teams
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: announced
  problem: Rillet says legacy ERPs act as 'dumb databases' where the real work happens in spreadsheets, and that traditional implementations take about 12 months.
  solution: An AI-native ERP applies AI inside the general ledger, with native integrations feeding structured data. Rillet says accounting firms are strategic partners, naming Armanino (top 20) and Wiss (top 50). Rillet's release says customers report implementing in as little as 4 weeks.
  outcomes:
  - lever: speed
    description: Rillet says customers consistently report cutting close times to a few days and implementing as fast as 4 weeks versus the 12 months it says traditional systems need.
    figure: 4 weeks versus 12 months
    measures: Implementation time as reported by the vendor, comparing its fastest customers with a vendor-stated traditional baseline; no sample, definition or named firm-led project
    provenance: vendor-published
    source_ref: RILLET-SERIESB-2025
  prerequisites:
  - Standard integrations to the client's source systems
  - A client finance team willing to leave spreadsheet-based processes
  risks_and_guardrails:
  - More than a quarter of organisations in Panorama's 2026 ERP study exceeded project budgets, with additional technology needs the leading cause; Panorama is an ERP consultancy and the full report is gated (PANORAMA-ERP-2026).
  - Vendor release; a single-vendor source. Customer closes and implementation times could not be checked.
  human_checkpoints:
  - Implementation partner designs the chart of accounts, integrations and controls
  role_evolution: Rillet says its leaders are former EY, PwC and CPA practitioners and its customers run lean teams; the release gives no data on partner staffing.
  evidence_grade: C
  sources:
  - ref: RILLET-SERIESB-2025
    title: Rillet raises $70M Series B from Andreessen Horowitz and ICONIQ
    publisher: Rillet
    type: vendor
    url: https://rillet.com/blog/fundraise-announcement/
    date: '2025-08-06'
    access: full
    locator: Paragraphs on customer close times and implementation; paragraph on partnerships with Armanino and Wiss
  - ref: PANORAMA-ERP-2026
    title: Panorama Consulting Group Releases Latest Study of ERP Implementation Outcomes Across the Globe (2026 ERP Report)
    publisher: Panorama Consulting Group
    type: survey
    url: https://panorama-consulting.com/panorama-consulting-group-releases-latest-study-of-erp-implementation-outcomes-across-the-globe
    date: '2026-03-04'
    access: full
    locator: Paragraph 'The report also revealed that more than a quarter of organizations exceeded their project budgets'
  last_reviewed: '2026-10-20'
  notes: 'Firm types: vendor (Rillet) with Armanino (top 20) and Wiss (top 50) as partners, both ranks as stated by Rillet. The partnership is announced; no partner-led implementation was documented. Series B release dated 2025-08-06, so older than 12 months, and later status of the partnerships was not found. Change scope is model because the offer replaces the incumbent ERP rather than improving one step.'
- id: advisory-fpa-performance-08
  title: Continuous, driver-based planning with AI-assisted scenarios replaces the annual budget cycle
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Planning horizons are shrinking and scenario work is slow. In the 2026 FP&A Trends Survey, 44% of organisations could plan with high confidence only up to three months ahead, and only 19% of FP&A teams could run a scenario in real time or within one day.
  solution: Firms and vendors pitch rolling, driver-based forecasts that update as the business changes, with what-if scenarios on pricing, headcount, demand and investment (RSM and Abacum), continuous scenario-based forecasting with AI-enabled insights and governance (Grant Thornton webcast, August 20, 2026), and trigger-based adaptive scenario planning (Gartner). Abacum's release describes goal-seeking such as 'How do we reach $125M without adding headcount?'.
  outcomes:
  - lever: speed
    description: 'Baseline, not an outcome: only 19% of FP&A teams can run a scenario in real time or within a single day.'
    figure: 19%
    measures: Share of FP&A teams in the 2026 FP&A Trends Survey (475 respondents, 52 countries; sponsored by OneStream) that can run a scenario in real time or within a single day
    provenance: vendor-published
    source_ref: ONESTREAM-FPATRENDS-2026
  prerequisites:
  - Driver-based models (19% use mature models that automatically identify and apply drivers; 40% still use basic or non-driver approaches, per the webinar)
  - Integrated financial and operational planning (10% fully integrate them)
  - Timely data (11% have real-time or near-real-time access to critical data)
  risks_and_guardrails:
  - OneStream's presenter says AI compounds an existing advantage and does not create one, since AI users were already strong on data and connected planning (ONESTREAM-FPAWEBINAR-2026).
  - Gartner says traditional scenario planning relies on static assumptions and over-weights internal drivers (GARTNER-TALENT-2026).
  human_checkpoints:
  - Finance leaders set the trigger thresholds and contingency actions
  - Advisors challenge assumptions before scenarios go to management
  role_evolution: Gartner expects finance teams to shift from control and business-partnering roles toward digitally skilled 'catalysts' who build tools and manage AI-driven workflows (GARTNER-TALENT-2026).
  evidence_grade: C
  sources:
  - ref: ONESTREAM-FPATRENDS-2026
    title: 'The Readiness Gap: New 10th Annual FP&A Trends Survey Reveals AI Is Outpacing FP&A''s Foundations'
    publisher: OneStream (survey by FP&A Trends Group, sponsored by OneStream)
    type: survey
    url: https://www.onestream.com/blog/the-readiness-gap-new-10th-annual-fp-and-a-trends-survey-reveals-ai-is-outpacing-fp-and-a-s-foundations/
    date: '2026-07-08'
    access: full
    locator: Sections 'The business wants FP&A to see further ahead' and 'Where AI fits in'
  - ref: ONESTREAM-FPAWEBINAR-2026
    title: '2026 FP&A trends: How AI is testing the foundations of Finance (webinar page with full transcript)'
    publisher: OneStream and FP&A Trends Group
    type: conference
    url: https://www.onestream.com/resources/2026-fp-and-a-trends-replay-webinar/
    date: '2026-07-09'
    access: full
    locator: Transcript segments on driver-based models and integrated planning; audience poll on where AI has the strongest potential value in FP&A (29% simulation of scenarios)
  - ref: RSM-ABACUM-2026
    title: AI native financial planning and analysis, delivered by RSM (Abacum solutions)
    publisher: RSM US LLP
    type: firm
    url: https://rsmus.com/services/digital-transformation/abacum-solutions.html
    date: '2026-09-30'
    access: full
    locator: Section 'Continuous planning and forecasting'
  - ref: ABACUM-INTELLIGENCE-2026
    title: Abacum Rethinks AI for Finance with the Launch of Abacum Intelligence, a Platform-Wide Intelligence Layer
    publisher: Abacum
    type: vendor
    url: https://abacum.ai/newsroom/abacum-rethinks-ai-for-finance-with-the-launch-of-abacum-intelligence-a-platform-wide-intelligence-layer
    date: '2026-04-09'
    access: full
    locator: Bullet 'Scenario Intelligence'
  - ref: GT-FORECASTWEBCAST-2026
    title: 'Modern forecasting for CFOs: AI-enabled, continuous, and decision-ready (webcast)'
    publisher: Grant Thornton Advisors LLC
    type: firm
    url: https://www.grantthornton.com/events/advisory/2026/08-20-modern-forecasting-for-cfos
    date: '2026-08-20'
    access: full
    locator: Webcast description and learning objectives (broadcast August 20, 2026)
  - ref: GARTNER-TALENT-2026
    title: Gartner Survey Reveals Acquiring and Developing AI and Digital Talent Is CFOs' Top Near-Term Challenge
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/newsroom/press-releases/2026-03-23-gartner-survey-reveals-acquiring-and-developing-ai-and-digital-talent-is-cfos-top-near-term-challenge
    date: '2026-03-23'
    access: full
    locator: Paragraph on adaptive scenario planning; paragraph on Finance 2030 workforce shifts
  - ref: KPMG-WEBCASTS-2026
    title: 'CFO webcast series (includes ''The Future of FP&A: From Forecasting to Value Steering'', July 29, 2026)'
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/webcasts/cfo-webcast-series.html
    date: '2026-07-29'
    access: full
    locator: 'Listing for July 29, 2026: The Future of FP&A: From Forecasting to Value Steering'
  last_reviewed: '2026-10-20'
  notes: 'Firm types: RSM and Grant Thornton Advisors (large firm; the landscape file describes it as backed by New Mountain Capital, which was not re-verified here), KPMG (Big Four); Abacum and OneStream are vendors. These are pitches, webcast descriptions and survey baselines; no named firm reported a planning-cycle result. The poll result (29% of webinar attendees chose simulation of scenarios as the strongest potential value from AI in FP&A, ahead of 27% for insight into drivers, 21% for automated reporting and commentary and 19% for better forecasts) is from an audience poll, not a survey sample.'
- id: advisory-fpa-performance-09
  title: Planning models built and changed in plain language, with agents cascading structural changes
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - software-systems
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Building and changing multidimensional planning models normally needs specialist administrators or implementation consultants.
  solution: Abacum says its Modeling Intelligence lets finance teams build and modify models in plain language, with agents handling structural changes such as adding entities, currencies and product lines and cascading updates without breaking downstream reports. RSM's Abacum page says models can be built quickly without specialist admins while keeping transparency and auditability.
  outcomes:
  - lever: capacity
    description: none published
    figure: none
    measures: 'Not applicable: product descriptions only; no customer result for model building was published'
    provenance: vendor-published
    source_ref: ABACUM-INTELLIGENCE-2026
  prerequisites:
  - A governed model structure and clear dimension design
  - Reviewer able to inspect changes the agent makes
  risks_and_guardrails:
  - In a 2026 working paper, three frontier LLMs correctly solved 63, 58 and 42 of 100 synthetic leveraged buyout modelling cases, and accuracy fell as structure grew more complex; the author says none should be relied on without deterministic verification (SSRN-VIDAL-2026). This is an adjacent task (LBO models) and not planning-model building.
  - Daily finance work is only as good as the model logic, so a change log and reviewer sign-off matter more than speed (practitioner view in CPAPA-AGENTSCLOSE-2026, controls 2 and 3).
  human_checkpoints:
  - Reviewer inspects structural changes and reconciles outputs to the prior model before release
  role_evolution: If model builds move to plain language, the work of implementation consultants and model administrators shifts toward design, review and testing; the sources assert this for the vendor's product but show no measured effect.
  evidence_grade: C
  sources:
  - ref: ABACUM-INTELLIGENCE-2026
    title: Abacum Rethinks AI for Finance with the Launch of Abacum Intelligence, a Platform-Wide Intelligence Layer
    publisher: Abacum
    type: vendor
    url: https://abacum.ai/newsroom/abacum-rethinks-ai-for-finance-with-the-launch-of-abacum-intelligence-a-platform-wide-intelligence-layer
    date: '2026-04-09'
    access: full
    locator: Bullet 'Modeling Intelligence'
  - ref: RSM-ABACUM-2026
    title: AI native financial planning and analysis, delivered by RSM (Abacum solutions)
    publisher: RSM US LLP
    type: firm
    url: https://rsmus.com/services/digital-transformation/abacum-solutions.html
    date: '2026-09-30'
    access: full
    locator: Paragraph on building multidimensional models without specialist admins
  - ref: SSRN-VIDAL-2026
    title: Analysis of Frontier Large Language Models (LLMs) in Financial Leveraged Buyout (LBO) Modeling (Vidal)
    publisher: SSRN working paper
    type: academic
    url: https://doi.org/10.2139/ssrn.7273418
    date: '2026'
    access: full
    locator: Abstract (63, 58 and 42 of 100 cases; decline with complexity)
  - ref: CPAPA-AGENTSCLOSE-2026
    title: 'Before You Let the Agents Run the Close: Five Controls to Put in Writing First'
    publisher: CPA Practice Advisor (author Anthony L. Fulmore Sr., Texas A&M University-Central Texas)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/
    date: '2026-08-13'
    access: full
    locator: Controls 2 and 3
  last_reviewed: '2026-10-20'
  notes: 'Firm type: vendor (Abacum), delivered through RSM, Armanino and CFGI as in use case 04. Pigment''s Modeler Agent was seen only in a search summary and is not used. The LBO study is routed to transactions as its main home and is cited here only as quality evidence for LLM model building.'
- id: advisory-fpa-performance-10
  title: Managed FP&A delivered with agent-led forecasting and variance analysis, priced on outcomes
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Enterprises want external help with planning, forecasting and decision support, not only transactional finance, and are comfortable sourcing more of it.
  solution: ISG's September 2026 FP&A quadrant says providers apply predictive models and GenAI to variance analysis, scenario modelling, forecast generation and management reporting, with early agentic capability that gathers data and flags deviations. It describes PwC's outcomes-based FP&A managed service with agent-led forecasting and variance analysis, EY's multi-agent forecasting framework, Deloitte's agentic forecasting, EXL's outcome-based delivery model and Sutherland's agentic CFO control tower aimed at midmarket and PE-backed enterprises.
  outcomes:
  - lever: speed
    description: ISG describes EY's multi-agent forecasting framework as turning variance analysis that once took thousands of hours into minutes.
    figure: thousands of hours to minutes
    measures: Variance analysis effort as characterised by ISG in the EY profile, from a provider-questionnaire process; no client, baseline or method given
    provenance: vendor-published
    source_ref: ISG-FAOFPA-2026
  prerequisites:
  - Data foundations and a unified data layer across FP&A and controllership (ISG on PwC)
  - Clients willing to source planning and analysis externally
  risks_and_guardrails:
  - 'ISG says maturity varies considerably: production implementations sit alongside early deployments, pilots and demonstrations, and differentiation will depend on evidence that analytics improve forecast accuracy and decisions (ISG-FAOFPA-2026, FP&A observations).'
  - ISG lists weak data foundations and insufficient governance as risks that could slow progress (ISG-FAOFPA-2026, Outlook).
  - 'Independence: for audit clients of SEC registrants, performing decision-making, supervisory or ongoing monitoring functions is listed as impairing independence (SEC-REGSX-2026, (c)(4)(vi)); whether a given managed FP&A scope crosses that line was not analysed here.'
  human_checkpoints:
  - ISG describes agentic capabilities operating under human oversight; sign-off points are not specified
  role_evolution: ISG says consulting and accounting firms are increasing their participation in managed services, which raises competition in FP&A, tax and controllership, and that experienced finance talent, industry context and data foundations drive differentiation (ISG-FAOFPA-2026).
  evidence_grade: C
  sources:
  - ref: ISG-FAOFPA-2026
    title: 'ISG Provider Lens Finance and Accounting Outsourcing (FAO) Services 2026: Financial Planning & Analysis quadrant report'
    publisher: Information Services Group (ISG), copy hosted by PwC
    type: survey
    url: https://www.pwc.com/gx/en/about/analyst-relations/financial-planning-and-analysis.pdf
    date: 2026-09
    access: full
    locator: FP&A 'Observations' paragraph; provider profiles for EY, PwC, Deloitte, EXL and Sutherland; Executive Summary on portfolio boundaries; Outlook
  - ref: SEC-REGSX-2026
    title: 17 CFR 210.2-01 Qualifications of accountants (current eCFR text)
    publisher: U.S. Securities and Exchange Commission (via eCFR)
    type: regulator
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.2-01
    date: '2026-10-01'
    access: full
    locator: (c)(4)(vi)
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Big Four (PwC, EY, Deloitte), and AI-native or outsourcing providers (EXL, Sutherland, Accenture, Capgemini and others in the report). Not mid-market accounting firms, apart from ISG''s remark that consulting and accounting firms are increasing their managed-service role. ISG is an analyst firm; the report is a provider-customized edition hosted by PwC. The outcome is a provider claim as relayed by ISG, so it cannot support a B or A grade.'
- id: advisory-fpa-performance-11
  title: Real-time KPI dashboards and auto-generated monthly reporting packages with commentary for advisory clients
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - document-production
  - data-reporting
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: CAS and advisory teams compile monthly statements by hand and add client-specific commentary late. Clients want insight, not only numbers.
  solution: AI reporting and analysis tools produce dashboards and draft packages with commentary from ledger data, trends and KPIs. Withum's Jim Bourke told a May 2026 conference that AI lets firms deliver real-time dashboards on the metrics clients want, and that AI can quickly find a variance and suggest an explanation. CohnReznick CAS leaders list tools in this class (Reach Reporting, Qvinci, Spotlight Reporting, Datarails) in the Journal of Accountancy.
  outcomes:
  - lever: capacity
    description: 86% of surveyed accounting professionals expect AI to increase their advisory capacity over the next 12 months; 30% name manual data cleanup as the top blocker to proactive advisory work.
    figure: 86% and 30%
    measures: Share of 725 US accounting and bookkeeping professionals in an Intuit-sponsored survey expecting more advisory capacity from AI, and naming manual data cleanup the top blocker
    provenance: vendor-published
    source_ref: INTUIT-ACCTTECH-2026
  prerequisites:
  - Clean, current ledger data and integrations (only 41% of surveyed firms say their tools are fully integrated)
  - A 30-60 day pilot on one workflow with time saved, added review time and errors measured (JofA)
  risks_and_guardrails:
  - Three in five surveyed accountants say clients ask for proof of AI data protection always or frequently, yet only a third proactively explain how AI supports their work (INTUIT-ACCTTECH-2026).
  - Commentary drafted by AI needs the same review as an analyst's draft (CPAPA-AGENTSCLOSE-2026, control 3).
  human_checkpoints:
  - Advisor reviews commentary and insights before delivery
  - Pilot measures review time and error reduction before scaling (JOFA-CASAI-2026)
  role_evolution: Withum says advisory-based services are where the profession will grow, and Bourke told attendees AI in CAS is where firms get 'the most bang for your buck' (ACCTODAY-CASKEYS-2026). Hiring data in the Intuit survey shows 38% prioritising strategic judgment and 22% AI fluency (INTUIT-ACCTTECH-2026).
  evidence_grade: C
  sources:
  - ref: ACCTODAY-CASKEYS-2026
    title: CAS delivers 'the keys to the kingdom'
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom
    date: '2026-05-22'
    access: full
    locator: Section 'AI in CAS', Bourke quotes on variances and dashboards
  - ref: JOFA-CASAI-2026
    title: Simple but effective AI use cases for CAS
    publisher: Journal of Accountancy (AICPA & CIMA); authors Kane Polakoff and Michelle Voyer, CohnReznick
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/
    date: '2026-01-01'
    access: full
    locator: 'Steps 3 and 6; category ''Reporting: Auto-generated monthly reporting with commentary''; category ''Business insights'''
  - ref: INTUIT-ACCTTECH-2026
    title: 'The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future'
    publisher: CPA Practice Advisor (reporting Intuit QuickBooks survey)
    type: survey
    url: https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807
    date: '2026-07-02'
    access: full
    locator: Paragraphs on advisory bandwidth, integration, client trust and hiring
  - ref: KARBON-ENGAGE-2026
    title: AICPA & CIMA ENGAGE 2026 (curated session list, held June 8-11, 2026)
    publisher: Karbon Magazine
    type: conference
    url: https://karbonhq.com/resources/aicpa-cima-engage-2026/
    date: '2026-05-21'
    access: full
    locator: Session 'The tech-enabled adviser' (Matthew Wallace, Armanino; Floriana Allen, Wiss & Company)
  - ref: CPAPA-AGENTSCLOSE-2026
    title: 'Before You Let the Agents Run the Close: Five Controls to Put in Writing First'
    publisher: CPA Practice Advisor (author Anthony L. Fulmore Sr., Texas A&M University-Central Texas)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/
    date: '2026-08-13'
    access: full
    locator: Control 3
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Withum (top-100), CohnReznick (top-100), Armanino and Wiss (as session speakers). Bourke''s statement is general advice and does not say Withum measures dashboard results, so no named deployment with figures was confirmed; hence emerging and C. The survey reports current use by unnamed firms (financial forecasting 51% and real-time insights 49% among top client-service uses). The boundary with CAS is close: bookkeeping-based reporting packages belong in client-accounting-services, and this entry covers the FP&A and KPI layer.'
- id: advisory-fpa-performance-12
  title: AI-assisted opportunity analysis for performance improvement (pricing, cost and driver diagnosis)
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Gartner says the best AI opportunities are material business problems that are hard to diagnose with traditional methods, such as identifying drivers and decision points, and that many initiatives still aim at incremental improvements.
  solution: LLMs and analytics are used to find and size improvement opportunities. In KPMG's article, an automotive company used AI and large language models to scrape pricing data and optimise its parts business. EXL's profile in ISG's report cites cost command centers and contract intelligence for CFO decision support.
  outcomes:
  - lever: cost
    description: An unnamed automotive company's use of AI and LLMs to scrape pricing data and optimise the parts business saved $100 million 'this year alone', according to KPMG's article.
    figure: $100 million
    measures: Savings attributed by a KPMG article to one use of AI at an unnamed automotive company in the current year; method and baseline not given
    provenance: self-reported
    source_ref: KPMG-CFOREMODEL-2026
  prerequisites:
  - Access to pricing, cost and operational data outside the ledger
  - Business owners who will act on findings
  risks_and_guardrails:
  - The savings figure comes from an anonymous company and cannot be checked.
  - In Gartner's March 2026 survey, forecasting and insight generation were among the lowest-rated AI use cases (GARTNER-AIREPORTCARD-2026).
  human_checkpoints:
  - Business and finance leaders validate opportunities before commitments
  role_evolution: Gartner's FP&A agenda says AI is shifting the finance team pyramid into a diamond by eliminating entry-level roles, and recommends upskilling analysts into 'citizen data scientists' who build models (GARTNER-FPALEADER-2026, Priority 3).
  evidence_grade: C
  sources:
  - ref: GARTNER-FPALEADER-2026
    title: 2026 FP&A Leader Agenda
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/finance/trends/fpa-leader-agenda/unlocked
    date: '2026-05-13'
    access: full
    locator: Priority 2 ('diagnosis-resistant' problems)
  - ref: GARTNER-AIREPORTCARD-2026
    title: Gartner Says CFOs Must Stop Mistaking Finance AI Deployment for Value Creation
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation
    date: '2026-05-28'
    access: full
    locator: Paragraph 'Report Card Shows Progress and Value Gaps' and the Steecker quote on material business problems
  - ref: KPMG-CFOREMODEL-2026
    title: CFOs remodel the finance function for an AI-driven world
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2026/cfo-remodel-finance-function-ai-driven-world.html
    date: '2026-09-29'
    access: full
    locator: Paragraph on the automotive company's ten big bets and the parts-business pricing example
  - ref: ISG-FAOFPA-2026
    title: 'ISG Provider Lens Finance and Accounting Outsourcing (FAO) Services 2026: Financial Planning & Analysis quadrant report'
    publisher: Information Services Group (ISG), copy hosted by PwC
    type: survey
    url: https://www.pwc.com/gx/en/about/analyst-relations/financial-planning-and-analysis.pdf
    date: 2026-09
    access: full
    locator: EXL profile
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Gartner (analyst), KPMG (Big Four) relaying a client account, EXL (outsourcing provider). No mid-market advisory firm described a performance-improvement engagement that used AI, so this is the thinnest entry in the module. The practitioner discussion is real (Gartner, KPMG) but the figure is anonymous.'
- id: advisory-fpa-performance-13
  title: 'Idea: validation, back-testing and sign-off protocol for AI-generated forecasts and commentary, sold as an advisory service'
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: 'Finance leaders hesitate to trust AI for mission-critical work: in a vendor survey, 75% cited lack of auditability, 71% accuracy and hallucination concerns and 54% regulatory or compliance concerns.'
  solution: 'Practitioners and standard-setters describe pieces of such a service: an inventory of agents with named owners, evidence a reviewer can replay, sign-off gates scaled to risk, exception metrics with a kill threshold, and a short pilot that measures time saved, added review time and errors (CPA Practice Advisor, JofA). COSO''s February 2026 guidance maps generative AI capabilities, including insight generation, to its 17 control principles. Grant Thornton''s August 2026 webcast covers governance for AI-enabled forecasting.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: No published results from an advisory service of this kind were found
    provenance: self-reported
    source_ref: COSO-GENAI-2026
  prerequisites:
  - A baseline of manual forecast accuracy to compare against
  - A client willing to log AI-assisted work and review results
  risks_and_guardrails:
  - KPMG's survey found only 29% of organisations track where AI adoption fails (KPMG-AIFINANCE-2026).
  - Independence implications of advisors validating a client's AI forecasts were not researched beyond the Regulation S-X management-functions text (SEC-REGSX-2026).
  human_checkpoints:
  - Named owner per agent
  - Human approval before outputs feed financial statements or board reporting
  role_evolution: Not discussed in the sources for this service.
  evidence_grade: D
  sources:
  - ref: CPAPA-AGENTSCLOSE-2026
    title: 'Before You Let the Agents Run the Close: Five Controls to Put in Writing First'
    publisher: CPA Practice Advisor (author Anthony L. Fulmore Sr., Texas A&M University-Central Texas)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/
    date: '2026-08-13'
    access: full
    locator: The five controls (agent inventory, replayable evidence, sign-off gates, third-party assurance, monitoring and exit)
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (COSO publication and press release page)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/generative-ai
    date: '2026-02-23'
    access: full
    locator: Press release paragraphs 1-2
  - ref: DELOITTE-DART-COSO-2026
    title: 'Heads Up: COSO Releases Publication on Internal Controls Related to Generative AI'
    publisher: Deloitte DART
    type: firm
    url: https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai
    date: '2026-04-03'
    access: full
    locator: Paragraph 1 (capability-based view, 17 principles, insight generation)
  - ref: JOFA-CASAI-2026
    title: Simple but effective AI use cases for CAS
    publisher: Journal of Accountancy (AICPA & CIMA); authors Kane Polakoff and Michelle Voyer, CohnReznick
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/
    date: '2026-01-01'
    access: full
    locator: Step 3 (30-to-60-day pilot measuring time saved, added review time, error reduction)
  - ref: GT-FORECASTWEBCAST-2026
    title: 'Modern forecasting for CFOs: AI-enabled, continuous, and decision-ready (webcast)'
    publisher: Grant Thornton Advisors LLC
    type: firm
    url: https://www.grantthornton.com/events/advisory/2026/08-20-modern-forecasting-for-cfos
    date: '2026-08-20'
    access: full
    locator: Learning objectives
  - ref: CFODIVE-DATARAILS-2026
    title: 'AI verification eats up 26% of finance teams'' workweek: Datarails'
    publisher: CFO Dive
    type: survey
    url: https://www.cfodive.com/news/ai-verification-eats-26percent-finance-teams-workweek-datarails/832210/
    date: '2026-10-06'
    access: full
    locator: Dive Insight (75%, 71%, 54%)
  - ref: KPMG-AIFINANCE-2026
    title: 'AI adoption in finance doubles, but assurance readiness determines who wins (2026 Global AI in Finance: The Decision Advantage)'
    publisher: KPMG International
    type: survey
    url: https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html
    date: '2026-05-11'
    access: full
    locator: Paragraph on assurance readiness (29% track where AI fails)
  last_reviewed: '2026-10-20'
  notes: 'Idea: labelled D. Practitioners and COSO discuss the controls, but no firm was found selling forecast validation as a service. Related assurance work for AI systems (AICPA and AIUC certification, Grant Thornton Enterprise Assurance Services) is routed to risk-controls and the assurance archetype. Firm types: standard-setter and professional-body sources only.'
- id: advisory-fpa-performance-14
  title: Governed planning data exposed to general-purpose AI assistants through MCP connectors
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - data-reporting
  - software-systems
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Business users wait in the finance queue for answers, and finance staff already use general-purpose assistants outside governed data.
  solution: Abacum says its workflow layer extends to Claude, ChatGPT and Slack through MCP, so users get governed financial context in tools they already use. Xero integrated Anthropic's Claude into its product on May 12, 2026 per Accountex coverage. Karbon's Byron Patrick ran an ENGAGE session on building automations live with Claude Code, and the Accounting Technology Lab hosts describe a Copilot agent demo showing access to Claude and OpenAI models.
  outcomes:
  - lever: experience
    description: none published
    figure: none
    measures: No customer results for MCP-connected finance assistants were found
    provenance: vendor-published
    source_ref: ABACUM-INTELLIGENCE-2026
  prerequisites:
  - Permissions that carry through to the assistant
  - A governed data model to ground answers
  risks_and_guardrails:
  - Pigment says customers choose which blocks and metrics its AI can access, permissions are enforced and customer data is excluded from model training (PIGMENT-AI-2026).
  - Three in five surveyed accountants say clients ask for proof of AI data protection always or frequently (INTUIT-ACCTTECH-2026).
  human_checkpoints:
  - Users validate answers against the governed model before use in decisions
  role_evolution: The sources do not describe role effects.
  evidence_grade: C
  sources:
  - ref: ABACUM-INTELLIGENCE-2026
    title: Abacum Rethinks AI for Finance with the Launch of Abacum Intelligence, a Platform-Wide Intelligence Layer
    publisher: Abacum
    type: vendor
    url: https://abacum.ai/newsroom/abacum-rethinks-ai-for-finance-with-the-launch-of-abacum-intelligence-a-platform-wide-intelligence-layer
    date: '2026-04-09'
    access: full
    locator: Bullet 'Workflow Intelligence'; paragraph on MCP integration
  - ref: ACCOUNTEX-2026
    title: 'Accountex London 2026: product roundup'
    publisher: Financial Accountant (IFA)
    type: press
    url: https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/
    date: '2026-05-19'
    access: full
    locator: Paragraph on Xero's Claude integration (launched 12 May)
  - ref: KARBON-ENGAGE-2026
    title: AICPA & CIMA ENGAGE 2026 (curated session list, held June 8-11, 2026)
    publisher: Karbon Magazine
    type: conference
    url: https://karbonhq.com/resources/aicpa-cima-engage-2026/
    date: '2026-05-21'
    access: full
    locator: Session 'Building automations live' (Byron Patrick, Karbon)
  - ref: CPAPA-TECHLAB-2026
    title: Thought Leader & 40 Under 40 AICPA Think Tank - Accounting Technology Lab Podcast - July 2026
    publisher: CPA Practice Advisor
    type: podcast
    url: https://www.cpapracticeadvisor.com/podcasts/thought-leader-40-under-40-aicpa-think-tank-accounting-technology-lab-podcast-july-2026/
    date: '2026-07-01'
    access: full
    locator: Transcript paragraph on the Copilot agent demonstration
  - ref: PIGMENT-AI-2026
    title: 'Introducing Pigment AI: Smarter Planning Tools'
    publisher: Pigment
    type: vendor
    url: https://www.pigment.com/blog/ai-launch
    date: '2026-09-03'
    access: full
    locator: Security and privacy bullet
  - ref: INTUIT-ACCTTECH-2026
    title: 'The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future'
    publisher: CPA Practice Advisor (reporting Intuit QuickBooks survey)
    type: survey
    url: https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807
    date: '2026-07-02'
    access: full
    locator: Paragraph on clients asking for proof of AI data protection
  last_reviewed: '2026-10-20'
  notes: 'Firm types: vendors (Abacum, Xero, Pigment, Karbon) and a conference session; no advisory firm named as deploying MCP-connected planning data. Announced only.'
- id: advisory-fpa-performance-15
  title: Agents collect budget inputs, route approvals and consolidate submissions
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Armanino's white paper describes budgets emailed as spreadsheets to dozens of people, with divisions adding lines that break links, and consolidation that takes manual effort and lacks an audit trail and role-based access.
  solution: Abacum says its workflow layer automates budget input collection, approval routing and cross-team collaboration. Armanino pitches software-driven FP&A transformation to replace the emailed-spreadsheet process.
  outcomes:
  - lever: speed
    description: none published
    figure: none
    measures: No results for automated budget collection were published
    provenance: vendor-published
    source_ref: ABACUM-INTELLIGENCE-2026
  prerequisites:
  - Standard chart of accounts and dimensions across entities
  - Roles and permissions for contributors and approvers
  risks_and_guardrails:
  - Armanino notes the manual process lacks audit trail and role-based access; a replacement needs to keep both (ARMANINO-FPAROADMAP-2025).
  human_checkpoints:
  - Approvers sign off submissions
  - Finance reviews consolidated budget before release
  role_evolution: The sources do not describe role effects.
  evidence_grade: C
  sources:
  - ref: ARMANINO-FPAROADMAP-2025
    title: 'FP&A Transformation: How to Evolve Your Financial Planning & Analysis'
    publisher: Armanino Advisory LLC
    type: firm
    url: https://www.armanino.com/white-papers/fpa-transformation-roadmap/
    date: '2025-06-30'
    access: full
    locator: Section 'How Did FP&A Become So Complex?', paragraphs on the budgeting process
  - ref: ABACUM-INTELLIGENCE-2026
    title: Abacum Rethinks AI for Finance with the Launch of Abacum Intelligence, a Platform-Wide Intelligence Layer
    publisher: Abacum
    type: vendor
    url: https://abacum.ai/newsroom/abacum-rethinks-ai-for-finance-with-the-launch-of-abacum-intelligence-a-platform-wide-intelligence-layer
    date: '2026-04-09'
    access: full
    locator: Bullet 'Workflow Intelligence'
  - ref: RILLET-SERIESB-2025
    title: Rillet raises $70M Series B from Andreessen Horowitz and ICONIQ
    publisher: Rillet
    type: vendor
    url: https://rillet.com/blog/fundraise-announcement/
    date: '2025-08-06'
    access: full
    locator: Paragraph naming Armanino (top 20) as a partner
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Armanino (described as top 20 in Rillet''s release), vendor Abacum. Much of the described workflow automation is conventional planning-platform functionality; the AI part is Abacum''s claim that agents run it.'
- id: advisory-fpa-performance-16
  title: AI and machine-learning forecasting inside client planning platforms to improve forecast accuracy
  archetype: advisory
  module: fpa-performance
  function: service-delivery
  work_types:
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: 'Forecasts are hard to hold beyond a short horizon: in the 2026 FP&A Trends Survey, 44% could plan with high confidence only up to three months ahead, and confidence beyond six months fell from 39% to 29%.'
  solution: Statistical and ML forecasting features generate baseline forecasts that analysts adjust. In the FP&A Trends Survey, ML use in forecasting reached 12%, the highest in the survey's history, and generative AI use reached 21%.
  outcomes:
  - lever: quality
    description: 64% of respondents in KPMG's survey of 1,013 senior finance leaders reported stronger forecast accuracy over the past year.
    figure: 64%
    measures: Share of senior finance leaders at organisations with revenue of at least $250M ($500M in the US) reporting stronger forecast accuracy over the past year; self-reported, no measured error rate
    provenance: self-reported
    source_ref: KPMG-AIFINANCE-2026
  - lever: quality
    description: AI users scored 64% versus 35% for non-users on forecast quality in the FP&A Trends Survey, as presented in the webinar.
    figure: 64% versus 35%
    measures: Forecast quality, as presented in the webinar; the definition is not stated in the transcript and the report cautions the association does not show AI causes the difference
    provenance: vendor-published
    source_ref: ONESTREAM-FPAWEBINAR-2026
  - lever: quality
    description: Financial forecasting and insight generation were among the lowest-rated AI use cases in Gartner's March 2026 survey of 204 finance leaders.
    figure: none (ranking only)
    measures: Ratings of realized versus expected value by AI use case; no percentage published for these use cases
    provenance: independent
    source_ref: GARTNER-AIREPORTCARD-2026
  prerequisites:
  - Data quality (36% in KPMG's survey call it both the top barrier and opportunity)
  - Back-testing against manual forecasts
  risks_and_guardrails:
  - KPMG found 71% of banking leaders reported moderate or significant forecast-accuracy gains against 44% in healthcare, which it attributes to data foundations (KPMG-AIFINANCE-2026).
  - The two 64% figures measure different things in different surveys and should not be combined.
  human_checkpoints:
  - Analysts review and adjust machine baselines
  - Forecast error is tracked against actuals
  role_evolution: Gartner recommends upskilling FP&A analysts into citizen data scientists and adding AI product managers and knowledge engineers (GARTNER-FPALEADER-2026, Priority 3).
  evidence_grade: C
  sources:
  - ref: KPMG-AIFINANCE-2026
    title: 'AI adoption in finance doubles, but assurance readiness determines who wins (2026 Global AI in Finance: The Decision Advantage)'
    publisher: KPMG International
    type: survey
    url: https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html
    date: '2026-05-11'
    access: full
    locator: Key findings; section 'AI improves financial judgment, but sector gaps persist'; 'About Global AI in Finance'
  - ref: ONESTREAM-FPAWEBINAR-2026
    title: '2026 FP&A trends: How AI is testing the foundations of Finance (webinar page with full transcript)'
    publisher: OneStream and FP&A Trends Group
    type: conference
    url: https://www.onestream.com/resources/2026-fp-and-a-trends-replay-webinar/
    date: '2026-07-09'
    access: full
    locator: 'Transcript: ''Forecast quality, 64% versus 35%''; ML 12% and generative AI 21%'
  - ref: ONESTREAM-FPATRENDS-2026
    title: 'The Readiness Gap: New 10th Annual FP&A Trends Survey Reveals AI Is Outpacing FP&A''s Foundations'
    publisher: OneStream (survey by FP&A Trends Group, sponsored by OneStream)
    type: survey
    url: https://www.onestream.com/blog/the-readiness-gap-new-10th-annual-fp-and-a-trends-survey-reveals-ai-is-outpacing-fp-and-a-s-foundations/
    date: '2026-07-08'
    access: full
    locator: Sections 'The business wants FP&A to see further ahead' and 'Where AI fits in'
  - ref: GARTNER-AIREPORTCARD-2026
    title: Gartner Says CFOs Must Stop Mistaking Finance AI Deployment for Value Creation
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation
    date: '2026-05-28'
    access: full
    locator: Paragraph 'Report Card Shows Progress and Value Gaps'
  - ref: GARTNER-FPALEADER-2026
    title: 2026 FP&A Leader Agenda
    publisher: Gartner
    type: survey
    url: https://www.gartner.com/en/finance/trends/fpa-leader-agenda/unlocked
    date: '2026-05-13'
    access: full
    locator: Priority 2 (84% deploying, 4% scaling) and Priority 3
  last_reviewed: '2026-10-20'
  notes: No named organisation and no measured forecast error. Evidence is survey self-report from KPMG (Big Four; the survey covers large organisations, not the middle market) and a sponsored vendor survey. Gartner's FP&A page says 84% of finance teams are deploying AI and only 4% are scaling it across the function; the page does not state the sample for that pair of figures. Maturity is piloting because Gartner's pair of figures describes mostly early deployment.
```


## 3. Module notes

### Processes and key steps (with work types)

- **Budgeting and planning cycle.** Input collection and approvals (coordination-scheduling), consolidation (data-reporting), target-setting and challenge (expert-judgment). Armanino describes the manual version as emailed spreadsheets consolidated by hand (ARMANINO-FPAROADMAP-2025, section 'How Did FP&A Become So Complex?').
- **Rolling forecasts and scenario planning.** Baseline forecast (data-reporting), scenarios and assumptions (expert-judgment).
- **Variance and flux analysis, management and board reporting.** Variance detection (data-reporting), explanation and narrative (document-production).
- **KPI dashboards and reporting packages.** Document-production and client-interaction; the bookkeeping-based layer sits in client-accounting-services.
- **Performance improvement.** Diagnosing cost, pricing, working-capital and driver issues (research-synthesis, expert-judgment).
- **FP&A operating-model design and transformation roadmaps.** Expert-judgment; CFGI's five-week diagnostic is an example (CFGI-FINEFFECTIVENESS-2026, Phase 0 description).
- **Planning-platform (CPM) and ERP selection and implementation.** Software-systems and coordination-scheduling; includes data readiness, integration and training.
- **Managed or co-sourced FP&A.** Recurring delivery of forecasting and reporting by an external team (ISG-FAOFPA-2026, FP&A observations).

### Common pain points

- **Time goes to data handling.** FP&A teams reported 47% of time on data collection and validation and 32% on insight generation (ONESTREAM-FPAWEBINAR-2026, time-allocation segment).
- **Short planning horizon.** 44% can plan with high confidence only up to three months ahead (ONESTREAM-FPATRENDS-2026, section 'The business wants FP&A to see further ahead').
- **Data quality and timeliness.** 19% rate data quality advanced and 11% have real-time or near-real-time access to critical data (ONESTREAM-FPATRENDS-2026, section on data).
- **Implementation drag.** 63% of finance organisations said AI implementation was slower than expected in 2025 (GARTNER-AIREPORTCARD-2026, paragraph 'Report Card Shows Progress and Value Gaps'). More than a quarter of ERP projects exceeded budgets (PANORAMA-ERP-2026, key findings paragraph).
- **Advisory capacity.** 30% of surveyed accountants name manual data cleanup the top blocker to proactive advisory work (INTUIT-ACCTTECH-2026, advisory section).

### Metrics and benchmarks (what each measures)

| Figure | What it measures | Source | Provenance |
|---|---|---|---|
| 30% to 75% | Active use of AI across the finance function, 2024 to March 2026; 1,013 senior finance leaders at organisations with revenue of at least $250M ($500M in the US) | KPMG-AIFINANCE-2026, key findings | self-reported |
| 64% | Share reporting stronger forecast accuracy over the past year (same sample) | KPMG-AIFINANCE-2026, key findings | self-reported |
| 33% vs 6% | Error-reduction improvement rates, assurance-ready organisations versus others | KPMG-AIFINANCE-2026, key findings | self-reported |
| 42% | Share 'fully assurance-ready' for AI-enabled finance processes; separately, 42% confidence in scaling among assurance-ready organisations | KPMG-AIFINANCE-2026, 'Assurance readiness powers AI performance' | self-reported |
| 29% | Share that track where AI adoption fails | KPMG-AIFINANCE-2026, same section | self-reported |
| 66% | Among finance organisations that adopted AI, share naming efficiency and productivity a top benefit (204 finance leaders, March 2026) | GARTNER-AIREPORTCARD-2026 | independent |
| 84% and 4% | Finance teams deploying AI versus scaling it across the function (sample not stated on the page) | GARTNER-FPALEADER-2026, Priority 2 | independent |
| 21% / 12% | FP&A teams using generative AI / ML in forecasting (475 respondents) | ONESTREAM-FPATRENDS-2026, 'Where AI fits in' | vendor-published |
| 19% / 59% | Formal AI governance ready to scale / informal guidance or no policies | ONESTREAM-FPAWEBINAR-2026, governance segment | vendor-published |
| 26% | Average work time spent verifying or correcting AI output (270 CFOs and finance leaders) | CFODIVE-DATARAILS-2026 | vendor-published |
| 86% / 97% / 17% | Mid-market organisations with AI partially or fully integrated / satisfied with AI investments / pursuing transformational AI across the enterprise (1,030 leaders) | RSM-MMAI-2026 | self-reported (firm survey) |
| 94% / 83% / 2% | Mid-market companies using generative AI / past early experimentation / operationalised at scale (100 decision-makers, December 2025) | KAUFMANROSSIN-AIMIDMARKET-2026 | self-reported (firm survey) |
| 40% | Among those increasing AI spending, share reallocating budget from external consulting services (43% from BI and analytics, 41% from cybersecurity) | RSM-MMAI-2026, reallocation paragraph | self-reported (firm survey) |
| 65% / 84% | Finance leaders rating AI performance good or excellent / saying AI ROI meets or exceeds expectations (nearly 230 US finance leaders) | GT-CFOSURVEY-2026 | self-reported (firm survey) |
| 61% vs 19% | Finance leaders who had purchased FP&A software in 2024 versus those citing FP&A solutions as a must-have in 2023, in a 2024 Datarails survey (older than the window; sample not stated in the article) | FMMAG-CFOSENT-2024, paragraph 3 | vendor-published |
| 51% | Surveyed accountants naming financial forecasting a top client-service use of AI (725 US professionals; denominator for the list not stated) | INTUIT-ACCTTECH-2026 | vendor-published |

Independent quality evidence is adjacent only. A Journal of Accounting Research paper (277 accountants plus field data on 79 SMEs and 200,000+ transaction records) links generative AI to productivity gains and faster month-end closing, finds accountants intervene when AI confidence is low, and finds that relying on non-consensus AI recommendations can raise error risk (STANFORD-JAR-2026, abstract). A 2026 working paper found three frontier LLMs solved 63, 58 and 42 of 100 synthetic LBO modelling cases (SSRN-VIDAL-2026, abstract). Neither covers FP&A.

### Guardrails and regulatory points

- **Independence (SEC registrants).** Regulation S-X rule 210.2-01(c)(4) lists, as impairing independence unless results are not subject to audit procedures, bookkeeping services, financial information systems design and implementation, and internal audit outsourcing; it separately lists management functions, meaning any decision-making, supervisory or ongoing monitoring function (SEC-REGSX-2026, (c)(4)(i), (ii), (v), (vi)). Whether specific FP&A or ERP scopes fall inside these was not analysed. The AICPA Code for private-company audit clients was not checked.
- **Internal control over generative AI.** COSO's publication of 2026-02-23 takes a capability-based view (data extraction, reconciliation, orchestration, insight generation, monitoring) and maps it to the 17 principles of the 2013 framework (DELOITTE-DART-COSO-2026, paragraph 1; COSO-GENAI-2026, press release).
- **Practitioner control checklist.** Agent inventory with named owner, replayable evidence, sign-off gates scaled to risk, third-party assurance read closely, monitoring with an exit threshold (CPAPA-AGENTSCLOSE-2026, controls 1 to 5).
- **Deliverable quality.** Deloitte Australia agreed to repay the final instalment of a roughly AU$440,000 contract after a report contained incorrect references; the updated report disclosed generative AI use (CITYAM-DELOITTE-2025).
- **Client confidentiality.** Three in five surveyed accountants say clients ask for proof of AI data protection always or frequently (INTUIT-ACCTTECH-2026, client-trust paragraph). Only 21% of firms had an AI policy or strategy in Karbon's survey (KARBON-AISTATE-2026, summary paragraph).
- **Assurance expectations.** KPMG says regulators and external auditors increasingly require proof that AI-enabled finance processes are controlled and explainable (KPMG-AIFINANCE-2026, 'Assurance readiness powers AI performance').

### Frontier signals (dated)

- **2026-02-23.** COSO publishes generative AI control guidance (DELOITTE-DART-COSO-2026).
- **2026-04-09.** Abacum launches a platform-wide AI layer with agents that flag anomalies, draft narratives, model scenarios and connect to Claude, ChatGPT and Slack through MCP (ABACUM-INTELLIGENCE-2026).
- **2026-05-28.** EY and Microsoft hold a half-day CFO AI Lab on moving from AI use cases to agentic finance, with practical examples listed for source-to-pay, order-to-cash, FP&A and record-to-report (EY-CFOAILAB-2026, event description; event page only). The same day, Gartner says finance should prepare for embedded AI assistants and AI-enabled simulation, and that forecasting and insight generation are among the lowest-rated use cases (GARTNER-AIREPORTCARD-2026).
- **2026-06-22 and 2026-09-05.** RSM and CFGI announce Abacum alliances (ABACUM-RSM-2026; ABACUM-CFGI-2026).
- **2026-07-08.** FP&A Trends Survey: 15% of organisations expect to use AI agents within six months and 51% at some point (ONESTREAM-FPAWEBINAR-2026, agents segment).
- **2026-08-12.** Sage Intacct's Finance Intelligence Agent is in phased rollout and an agent marketplace is announced (ARMANINO-INTACCTR3-2026).
- **2026-09.** ISG says consulting and accounting firms are increasing their role in managed services and lists outcome-linked commercial structures as a leading indicator (ISG-FAOFPA-2026, Executive Summary and Outlook).
- **2026-09-29.** KPMG's CFO article describes a flux analysis agent cutting variance-commentary staffing at an unnamed company (KPMG-CFOREMODEL-2026).
- **2026-10-19.** AICPA and AIUC announce a joint certification for AI systems and agents, with multiple CPA firms already delivering it and a full launch expected in early 2027 (JOFA-AIUC-2026). Routed to risk-controls.

### Workforce and role effects

- Gartner says AI is turning the finance pyramid into a diamond by eliminating entry-level roles, and recommends upskilling analysts into citizen data scientists and adding AI product managers and knowledge engineers (GARTNER-FPALEADER-2026, Priority 3). It also expects finance teams to shift from guardians and partners to catalysts and tool builders (GARTNER-TALENT-2026, Finance 2030 session).
- KPMG's Erin McShane describes talent needs moving from a reporting factory to interpreting AI outputs and advising leaders (KPMG-CFOREMODEL-2026).
- 88% of mid-market respondents expect their workforce size and composition to look fundamentally different within two to three years (RSM-MMAI-2026, workforce paragraph).
- Among accounting firms, 38% prioritise strategic judgment in hiring and 22% AI fluency, and 56% say a new entry-level hire needs six months or more to reach full billable capacity (INTUIT-ACCTTECH-2026, hiring paragraphs).
- 91% of surveyed professionals say graduates are more likely to join firms using AI (KARBON-AISTATE-2026, summary).
- Demand-side signal for advisors: among organisations raising AI spending, 40% say they are reallocating budget from external consulting (RSM-MMAI-2026, reallocation paragraph).

### Objections and concerns practitioners raise

- **Auditability, accuracy and compliance.** 75%, 71% and 54% of surveyed CFOs cite them as reasons to hold back on mission-critical use (CFODIVE-DATARAILS-2026, Dive Insight).
- **Foundations first.** OneStream's presenter warns that leading with agents 'automates the mess faster' (ONESTREAM-FPAWEBINAR-2026, foundation segment; a vendor view).
- **Value not yet realised.** Gartner says counts of pilots and tools do not prove value (GARTNER-AIREPORTCARD-2026, Steecker quote).
- **Hype.** GRF says the strongest parts of Intacct's release are usability gains rather than headline AI (GRF-INTACCTR2-2026). OneStream's presenter tells practitioners not to be a guinea pig for an unproven marketing message (ONESTREAM-FPAWEBINAR-2026, closing segment).
- **Competition and substitution.** Withum's Jim Bourke warns that bigger firms are coming down market using AI and expects complete automation of the tax process (ACCTODAY-CASKEYS-2026, section 'AI in CAS'). Fractional CFO Jason Hope said some clients could do the accounting with AI and some probably will, but he had been surprised by how little they had so far (CFODIVE-FRACTIONAL-2026, section 'An AI-enabled finance future').
- **Unmeasured ROI.** An Accounting Today opinion piece models 40-60% workload reductions for a hypothetical $40M company; it is an illustration, not data (ACCTODAY-AQUILA-2026).

### Interview probes for an advisor

1. Which FP&A deliverables (variance commentary, board pack, forecast, dashboard) does your team now draft with AI? What share of drafts survives review unchanged, and what do you log?
2. Before you recommend or implement a planning platform or ERP agent, how do you test a client's data readiness, and what do you do when it fails?
3. What evidence does a reviewer leave that AI output was checked, and could a client's auditor replay it?
4. How are engagements priced and staffed now compared with two years ago (hourly, fixed, outcome-based), and what happened to junior analyst hours?
5. For clients you or an affiliate audit, which FP&A and ERP services are off limits, and has AI changed where that line sits?


## 4. Routed to other modules

- **client-accounting-services.** Fractional and interim CFO demand linked to AI: interim CFO demand up 14% year on year per Business Talent Group, as cited by CFO Dive (CFODIVE-FRACTIONAL-2026, paragraphs 3-4). Close and reconciliation agents that clients run (BlackLine Verity Prepare generally available July 2026, FloQast, Microsoft reconciliation agent in preview, Workday close agent announced) (CPAPA-AGENTSCLOSE-2026, opening paragraphs). Field evidence on AI in SME bookkeeping-type work (STANFORD-JAR-2026). Bookkeeping-based reporting packages (JOFA-CASAI-2026).
- **risk-controls.** The five-controls checklist for client AI agents and COSO's generative AI guidance as an advisory service (CPAPA-AGENTSCLOSE-2026; COSO-GENAI-2026). Use case 13 above stays here only as an idea.
- **assurance archetype (and risk-controls).** AICPA and AIUC joint SOC 2 plus AIUC-1 certification, announced 2026-10-19 (JOFA-AIUC-2026, paragraphs 1-5). Grant Thornton Enterprise Assurance Services (GT-EAS-2026, from the landscape file, not re-read here).
- **transactions.** Frontier LLM accuracy on LBO modelling (SSRN-VIDAL-2026) and the Forvis Mazars quality-of-earnings article (FORVIS-QOE-2026, from the landscape file; the page was fetched but not read in depth).
- **valuation.** Kim, Muhn and Nikolaev on LLM earnings prediction from financial statements (SSRN-KMN-2024, search-only).
- **professional-services (firm operations).** Firm-level quality control for AI-assisted deliverables, using the Deloitte Australia case (CITYAM-DELOITTE-2025). PE and alternative practice structure context for CFGI (Carlyle and CVC) and the independence split (ABACUM-CFGI-2026, 'About CFGI'). Pricing shifts toward outcome-based commercial structures (ISG-FAOFPA-2026, Outlook). Junior-talent pipeline data (INTUIT-ACCTTECH-2026; KARBON-AISTATE-2026).
- **tax.** Not applicable here beyond Withum's expectation of complete automation of the tax process, kept as a competitive signal (ACCTODAY-CASKEYS-2026).


## 5. Sources

All sources below were opened and read unless marked search-only. 'Access: full' includes pages read through a mirror, noted in the last column. Types follow the vocabulary; ISG is an analyst report filed as `survey`.

| Ref | Title | Publisher | Type | URL | Date | Access | Note |
|---|---|---|---|---|---|---|---|
| KPMG-AIFINANCE-2026 | AI adoption in finance doubles, but assurance readiness determines who wins (2026 Global AI in Finance: The Decision Advantage) | KPMG International | survey | https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html | 2026-05-11 | full |  |
| GARTNER-AIREPORTCARD-2026 | Gartner Says CFOs Must Stop Mistaking Finance AI Deployment for Value Creation | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation | 2026-05-28 | full | Direct fetch blocked; read through Gartner's alternate host gcom.pdo.aws.gartner.com |
| GARTNER-TALENT-2026 | Gartner Survey Reveals Acquiring and Developing AI and Digital Talent Is CFOs' Top Near-Term Challenge | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2026-03-23-gartner-survey-reveals-acquiring-and-developing-ai-and-digital-talent-is-cfos-top-near-term-challenge | 2026-03-23 | full | Read through alternate host |
| GARTNER-TECHPORTFOLIO-2026 | Gartner Predicts by 2029, CFOs Who Implement Strategic AI Deployment Will Add 10 Margin Points of Growth | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartnerpredicts-by-2029-cfos-who-implement-strategic-ai-deploymnt-will-add-10-margin-points-of-growth | 2026-04-28 | full | Read through alternate host |
| GARTNER-FPALEADER-2026 | 2026 FP&A Leader Agenda | Gartner | survey | https://www.gartner.com/en/finance/trends/fpa-leader-agenda/unlocked | 2026-05-13 | full | Date is the page's dateOfPublication metadata; read through alternate host |
| ONESTREAM-FPATRENDS-2026 | The Readiness Gap: New 10th Annual FP&A Trends Survey Reveals AI Is Outpacing FP&A's Foundations | OneStream (survey by FP&A Trends Group, sponsored by OneStream) | survey | https://www.onestream.com/blog/the-readiness-gap-new-10th-annual-fp-and-a-trends-survey-reveals-ai-is-outpacing-fp-and-a-s-foundations/ | 2026-07-08 | full |  |
| ONESTREAM-FPAWEBINAR-2026 | 2026 FP&A trends: How AI is testing the foundations of Finance (webinar page with full transcript) | OneStream and FP&A Trends Group | conference | https://www.onestream.com/resources/2026-fp-and-a-trends-replay-webinar/ | 2026-07-09 | full | Date is the page's video uploadDate; the transcript is the only place the 64% vs 35% and Cox figures were found |
| CFODIVE-DATARAILS-2026 | AI verification eats up 26% of finance teams' workweek: Datarails | CFO Dive | survey | https://www.cfodive.com/news/ai-verification-eats-26percent-finance-teams-workweek-datarails/832210/ | 2026-10-06 | full | Reports a Datarails vendor survey |
| INTUIT-ACCTTECH-2026 | The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future | CPA Practice Advisor (reporting Intuit QuickBooks survey) | survey | https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807 | 2026-07-02 | full |  |
| KARBON-AISTATE-2026 | Karbon State of AI in Accounting 2026 Report | Karbon Magazine | survey | https://karbonhq.com/resources/state-of-ai-accounting-2026 | 2026-01-23 | full | Date is page metadata; the landscape file gives a release date of 2026-01-20 |
| RSM-MMAI-2026 | RSM Survey: The Middle Market Has Embraced AI. Now Comes the Hard Part. | RSM US LLP | survey | https://rsmus.com/newsroom/2026/rsm-survey-middle-market-embraced-ai-now-comes-hard-part.html | 2026-07-21 | full |  |
| KAUFMANROSSIN-AIMIDMARKET-2026 | 94% of mid-market companies use generative AI, but few have what it takes to scale (The State of Artificial Intelligence in the Mid-Market) | Kaufman Rossin | survey | https://kaufmanrossin.com/news/ai-in-the-middle-market-press-release/ | 2026-05-14 | full |  |
| PANORAMA-ERP-2026 | Panorama Consulting Group Releases Latest Study of ERP Implementation Outcomes Across the Globe (2026 ERP Report) | Panorama Consulting Group | survey | https://panorama-consulting.com/panorama-consulting-group-releases-latest-study-of-erp-implementation-outcomes-across-the-globe | 2026-03-04 | full | Press release only; the full report is gated |
| GT-CFOSURVEY-2026 | Grant Thornton survey: CFO profit optimism reaches record high despite economic uncertainty (Q3 2026 CFO Survey) | Grant Thornton Advisors LLC | survey | https://www.grantthornton.com/insights/press-releases/2026/september/grant-thornton-survey-cfo-profit-optimism-reaches-record-high | 2026-09-24 | full |  |
| ISG-FAOFPA-2026 | ISG Provider Lens Finance and Accounting Outsourcing (FAO) Services 2026: Financial Planning & Analysis quadrant report | Information Services Group (ISG), copy hosted by PwC | survey | https://www.pwc.com/gx/en/about/analyst-relations/financial-planning-and-analysis.pdf | 2026-09 | full | Analyst report dated September 2026; direct fetch blocked, read through the r.jina.ai text mirror; hosted copy is a provider-customized edition |
| ARMANINO-FPA-2026 | Financial Planning & Analysis Services | Armanino | firm | https://www.armanino.com/software/financial-planning-analysis/ | 2026 | full | Undated service page; Cloudflare blocked curl, read through r.jina.ai mirror |
| ARMANINO-SOLVER-2026 | Solver Financial Planning and Analysis Software | Armanino | firm | https://www.armanino.com/software/solver/ | 2026 | full | Undated service page; read through mirror |
| ARMANINO-FPAROADMAP-2025 | FP&A Transformation: How to Evolve Your Financial Planning & Analysis | Armanino Advisory LLC | firm | https://www.armanino.com/white-papers/fpa-transformation-roadmap/ | 2025-06-30 | full | Read through mirror; date from the page's published-time field |
| ARMANINO-INTACCTR3-2026 | Sage Intacct 2026 Release 3: Latest Updates (webinar deck) | Armanino | firm | https://www.armanino.com/-/media/pdf/webinars/2026/sage-intacct-2026-r3-release-overview.pdf | 2026-08-12 | full |  |
| RSM-ABACUM-2026 | AI native financial planning and analysis, delivered by RSM (Abacum solutions) | RSM US LLP | firm | https://rsmus.com/services/digital-transformation/abacum-solutions.html | 2026-09-30 | full | Date is the HTTP Last-Modified header, not a publication date |
| COHNREZNICK-WORKDAY-2026 | Workday Alliance / CohnReznick Digital Advisor | CohnReznick | firm | https://www.cohnreznick.com/services/advisory/digital/digital-alliance-workday-adaptive-planning | 2026 | full | Undated service page |
| FORVIS-SOLVER-2026 | Elevate Financial Reporting in Business Central With Solver (webinar slide deck) | Forvis Mazars US | firm | https://www.forvismazars.us/getattachment/b4a1114e-4173-4e2a-b632-6b1b4aecea5d/Elevate-Financial-Reporting-in-Business-Central-With-Solver.pdf | 2026-07-23 | full |  |
| CBH-FINANCEFUTURE-2024 | AI and Advanced Analytics: The Finance Function of the Future | Cherry Bekaert | firm | https://www.cbh.com/insights/articles/ai-and-advanced-analytics-the-finance-function-of-the-future/ | 2024-06-10 | full | Older than the 12-18 month window; used for the maturity-model approach only |
| CFGI-FINEFFECTIVENESS-2026 | Finance Effectiveness (Assess, Design, Build, Optimize) | CFGI | firm | https://www.cfgi.com/finance-effectiveness | 2026 | full | Undated service page; read through mirror |
| CFGI-JOB-2026 | Data and AI - Managing Director (job posting, Finance Effectiveness practice) | CFGI (listing on Built In Austin) | job-posting | https://www.builtinaustin.com/job/data-and-ai-managing-director/9295428 | 2026-06-03 | full | Posting valid through 2026-06-12 per its structured data; the original Lever posting now returns 404 |
| EISNERAMPER-INTACCTR3-2026 | Sage Intacct 2026 R3 Release Delivers New AI and AP Enhancements | EisnerAmper | firm | https://www.eisneramper.com/insights/sage-intacct-insights/sage-intacct-2026-r3-release-ai-ap-enhancements-0826/ | 2026-08-26 | full |  |
| GRF-INTACCTR2-2026 | Sage Intacct 2026 Release 2: AI and Real-Time Finance Insights | GRF CPAs & Advisors | firm | https://www.grfcpa.com/resource/sage-intacct-2026-release-2-ai-and-real-time-finance-insights/ | 2026-06-11 | full |  |
| GT-FORECASTWEBCAST-2026 | Modern forecasting for CFOs: AI-enabled, continuous, and decision-ready (webcast) | Grant Thornton Advisors LLC | firm | https://www.grantthornton.com/events/advisory/2026/08-20-modern-forecasting-for-cfos | 2026-08-20 | full | Webcast description only; no recording content read |
| KPMG-CFOREMODEL-2026 | CFOs remodel the finance function for an AI-driven world | KPMG US | firm | https://kpmg.com/us/en/articles/2026/cfo-remodel-finance-function-ai-driven-world.html | 2026-09-29 | full | Date is page metadata |
| KPMG-WEBCASTS-2026 | CFO webcast series (includes 'The Future of FP&A: From Forecasting to Value Steering', July 29, 2026) | KPMG US | firm | https://kpmg.com/us/en/webcasts/cfo-webcast-series.html | 2026-07-29 | full | Listing page only; the webcast content was not read. Date is the webcast date shown on the listing |
| EY-CFOAILAB-2026 | CFO AI LAB - AI-Driven Finance: How to scale from AI use cases to agentic finance (event page) | EY Finland with Microsoft | conference | https://www.ey.com/en_fi/events/2026/05/cfo-ai-lab-ai-driven-finance-how-to-scale-from-ai-use-cases-to-agentic-finance | 2026-05-28 | full | Event page only; event date from page structured data |
| RAND-AGENTS-2026 | AI agent services for ERP and CRM | Rand Group | firm | https://www.randgroup.com/software-engineering/ai-machine-learning/ai-agents/ | 2026-09-09 | full | Technology consultancy; date is page metadata |
| JIRAV-JIF-2024 | Accounting Firms Accelerate Growth with AI-powered Jirav Intelligent Forecasting (JIF) | Jirav | vendor | https://jirav.com/press-releases/jirav-artificial-intelligence-transforms-cas-practices | 2024-10-03 | full | Older than the 18-month window |
| JIRAV-CEO-2024 | Jirav Announces Michael Morrison as CEO and Launches New Artificial Intelligence Forecasting Product | Jirav (Business Wire, via Silicon UK) | vendor | https://www.silicon.co.uk/press-release/jirav-announces-michael-morrison-as-ceo-and-launches-new-artificial-intelligence-forecasting-product | 2024-09-17 | full | Older than the 18-month window |
| ABACUM-RSM-2026 | Abacum and RSM Announce Strategic Alliance to Deliver AI-Native FP&A to High-Growth Finance Teams | Abacum | vendor | https://www.abacum.ai/blog/abacum-and-rsm-announce-strategic-alliance-to-deliver-ai-native-fp-a-to-high-growth-finance-teams | 2026-06-22 | full |  |
| ABACUM-CFGI-2026 | Abacum and CFGI Partner to Bring AI-Native FP&A to Strategic Advisory | Abacum | vendor | https://www.abacum.ai/blog/abacum-and-cfgi-partner-to-bring-ai-native-fp-a-to-strategic-advisory | 2026-09-05 | full |  |
| ABACUM-INTELLIGENCE-2026 | Abacum Rethinks AI for Finance with the Launch of Abacum Intelligence, a Platform-Wide Intelligence Layer | Abacum | vendor | https://abacum.ai/newsroom/abacum-rethinks-ai-for-finance-with-the-launch-of-abacum-intelligence-a-platform-wide-intelligence-layer | 2026-04-09 | full | Release dated April 9, 2026; the newsroom post is dated April 14 |
| RILLET-SERIESB-2025 | Rillet raises $70M Series B from Andreessen Horowitz and ICONIQ | Rillet | vendor | https://rillet.com/blog/fundraise-announcement/ | 2025-08-06 | full | Release dateline August 6, 2025; page metadata updated 2026-08-25 |
| PIGMENT-AI-2026 | Introducing Pigment AI: Smarter Planning Tools | Pigment | vendor | https://www.pigment.com/blog/ai-launch | 2026-09-03 | full | Date is the page's datePublished metadata; the general-availability date of the product is not stated on the page, so treat the date as uncertain |
| SEC-REGSX-2026 | 17 CFR 210.2-01 Qualifications of accountants (current eCFR text) | U.S. Securities and Exchange Commission (via eCFR) | regulator | https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.2-01 | 2026-10-01 | full | Date is the eCFR version date used for the fetch; the rule applies to auditors of SEC registrants |
| COSO-GENAI-2026 | Achieving Effective Internal Control Over Generative AI (COSO publication and press release page) | COSO | standard-setter | https://www.coso.org/generative-ai | 2026-02-23 | full | Publication date from the Deloitte DART summary; the COSO page itself carries no date |
| DELOITTE-DART-COSO-2026 | Heads Up: COSO Releases Publication on Internal Controls Related to Generative AI | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 | full |  |
| JOFA-CASAI-2026 | Simple but effective AI use cases for CAS | Journal of Accountancy (AICPA & CIMA); authors Kane Polakoff and Michelle Voyer, CohnReznick | professional-body | https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/ | 2026-01-01 | full | Date is page metadata for the January 2026 issue |
| JOFA-AIUC-2026 | AICPA partners on new offering that assures AI systems and agents | Journal of Accountancy (AICPA & CIMA) | professional-body | https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/ | 2026-10-19 | full |  |
| FMMAG-CFOSENT-2024 | Transformation: CFOs look to evolve alongside their organisations | FM magazine (AICPA & CIMA) | professional-body | https://www.fm-magazine.com/news/2024/nov/transforming-cfo-roles-with-ai-and-fpa-software/ | 2024-11-18 | full | Older than the window; reports a 2024 Datarails survey |
| STANFORD-JAR-2026 | Human + AI in Accounting: Early Evidence from the Field (Choi and Xie), Journal of Accounting Research 64(3) | Stanford GSB / Journal of Accounting Research | academic | https://www.gsb.stanford.edu/index%2ephp/node/629989 | 2026-06 | full | Abstract read; full paper not read. Concerns SME bookkeeping-type accounting, so adjacent to this module |
| SSRN-VIDAL-2026 | Analysis of Frontier Large Language Models (LLMs) in Financial Leveraged Buyout (LBO) Modeling (Vidal) | SSRN working paper | academic | https://doi.org/10.2139/ssrn.7273418 | 2026 | full | Abstract read through the Crossref record; single-author working paper, not peer reviewed; concerns LBO models, so adjacent |
| SSRN-KMN-2024 | Financial Statement Analysis with Large Language Models (Kim, Muhn, Nikolaev) | SSRN working paper (Chicago Booth) | academic | https://doi.org/10.2139/ssrn.4835311 | 2024-05-21 | search-only | Title, authors and date confirmed from the Crossref record; the finding that the model out-predicted analysts on earnings direction was seen only in a search snippet. Adjacent (earnings prediction) |
| ACCTODAY-CASKEYS-2026 | CAS delivers 'the keys to the kingdom' | Accounting Today | press | https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom | 2026-05-22 | full |  |
| ACCTODAY-AQUILA-2026 | Will AI replace accounting firms in the small biz market? (AT Think opinion by August Aquila) | Accounting Today | press | https://www.accountingtoday.com/opinion/will-ai-replace-accounting-firms-in-the-small-biz-market | 2026-08-24 | full | Opinion piece with hypothetical hours and cost model, not measured data |
| CFODIVE-FRACTIONAL-2026 | Fractional CFOs see demand surge in AI age | CFO Dive | press | https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/ | 2026-08-06 | full |  |
| CPAPA-AGENTSCLOSE-2026 | Before You Let the Agents Run the Close: Five Controls to Put in Writing First | CPA Practice Advisor (author Anthony L. Fulmore Sr., Texas A&M University-Central Texas) | press | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/ | 2026-08-13 | full |  |
| ACCOUNTEX-2026 | Accountex London 2026: product roundup | Financial Accountant (IFA) | press | https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/ | 2026-05-19 | full |  |
| CITYAM-DELOITTE-2025 | Deloitte refunds Australian government after AI 'made up citations' in report | City A.M. | press | https://www.cityam.com/?p=2367690 | 2025-10-06 | full | Older than 12 months; used as the clearest dated failure case for AI-assisted consulting deliverables |
| CPAPA-TECHLAB-2026 | Thought Leader & 40 Under 40 AICPA Think Tank - Accounting Technology Lab Podcast - July 2026 | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/thought-leader-40-under-40-aicpa-think-tank-accounting-technology-lab-podcast-july-2026/ | 2026-07-01 | full | Transcript read; ENGAGE recap |
| KARBON-ENGAGE-2026 | AICPA & CIMA ENGAGE 2026 (curated session list, held June 8-11, 2026) | Karbon Magazine | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 | full | Session titles and abstracts only; no session content. Date is the page's publication date; the event ran June 8-11, 2026 |

Total: 56 sources (55 read in full, 1 search-only).


## 6. Gaps

**Not found**

- **Measured outcomes from any advisory firm.** No error rate, edit or override rate, parallel-run result, inspection finding or forecast-accuracy measurement for AI-assisted FP&A, budgeting or performance work by an accounting or advisory firm. The only named-firm figures are in a 2024 vendor release (JIRAV-JIF-2024).
- **Independent measurement specific to FP&A.** Gartner's survey is the only independent source on forecasting use cases and publishes no percentage for them. Academic work found is adjacent (SME bookkeeping, LBO models, earnings prediction).
- **Community discussion.** No practitioner forum, newsletter or community threads on this module were read. The web search allowance ran out before a community-focused search could run, and no search engine was queried by other means.
- **Podcasts.** Only the Accounting Technology Lab July 2026 episode was read; it covers ENGAGE and PE rather than FP&A specifics.
- **Job postings.** One relevant posting (CFGI, June 2026). Search results listed EY FP&A postings that mention automation and AI, but the EY page had been removed when fetched.
- **Conference content.** ENGAGE session titles and abstracts only, no session content (KARBON-ENGAGE-2026). No AFP, IMA, Gartner symposium session or Digital CPA FP&A agenda was retrieved. The KPMG, Grant Thornton and EY items are event or webcast descriptions, not recordings.
- **Deloitte CFO Signals 2026 and the Gartner figure on forecast-accuracy gains.** Neither primary document was found. Vendor blogs quote an accuracy improvement attributed to McKinsey (22% reduction in forecast error) and other accuracy-gain figures; none had a primary source and none is used.
- **Private-company independence rules.** The AICPA Code for attest clients of non-SEC firms was not checked; only Regulation S-X was read.

**Blocked, gated or partial**

- Armanino pages (Cloudflare) read through the r.jina.ai mirror; Gartner pages read through Gartner's alternate host; the ISG report read through the mirror; BPM, Wipfli and Quisitive pages were blocked and not read; Datarails' own pages returned 403 (its survey is read only through CFO Dive); SSRN returned a bot check (Kim, Muhn and Nikolaev stays search-only); AFP's article page returned a generic landing page; Panorama's ERP and AI-ERP reports are gated; the Pigment page is undated and its general-availability date is unknown.
- OneStream's 64% versus 35% forecast-quality comparison appears only in the webinar transcript, not in its blog summary, and 'forecast quality' is not defined there. The full FP&A Trends report was not read.
- Dates for several firm service pages (Armanino, CohnReznick, CFGI) could not be found and are given as the year.

**Weak or conflicting items**

- KPMG's 42% figure: see the correction in the Summary.
- Vendor-reported adoption (Abacum's 60% daily use, Rillet's implementation times, CohnReznick's 50-70%) have no independent check.
