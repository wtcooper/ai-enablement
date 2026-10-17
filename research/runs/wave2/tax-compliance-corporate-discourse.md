# Tax / compliance-corporate: discourse angle

- **Archetype:** tax
- **Module:** compliance-corporate (corporate direct-tax compliance in house and at large firms: federal, state and international income tax returns, return workpapers and review, credits and incentives, estimated payments and the tax calendar)
- **Angle:** discourse (what practitioners are saying: conference sessions, panels, practitioner articles, podcasts, surveys, and where the field says it is heading)
- **Prepared:** 2026-10-17. Source landscape: `research/runs/wave2/landscape-tax.md`. Controlled values: `research/briefs/templates/vocabulary.md`.
- **Method note.** Pages were fetched with `curl` (PDFs with `pdftotext`; `r.jina.ai` for one bot-walled Wolters Kluwer page). Every source in section 5 was opened by this analyst; `access: full` means the page was opened and read, but for podcasts only the episode page, description and (where posted) transcript were read, and for Tax Notes the free abstract only. Fifteen web searches were used before the shared search budget was refused. Reddit (r/taxpros), Going Concern, Greenberg Traurig, OpenAI's own careers page and the COST workshop agenda refused access or returned 404. Quotations are under 25 words.

---

## 1. Summary

- **Public discourse about corporate direct-tax compliance is thin, and mostly vendor- or conference-sourced.** The loudest AI-in-tax stories are about individual and partnership returns (Black Ore, Basis, Ready to Review); for 1120, 5471, state and credits work the usable record is one TEI seminar (two Thomson Reuters Institute recaps), a few firm interviews and op-eds, vendor blogs, three OpenAI tax job listings and TEI/TR surveys. No published error rate, override rate, parallel-run result, inspection finding or independent measurement exists for AI on corporate returns. The only independent accuracy datum is TaxCalcBench, which tests personal-return calculation (adjacent), where frontier models computed fewer than a third of federal returns correctly (COLUMN-TAXCALCBENCH-2025).
- **Sixteen candidate use cases: grade A 0, B 4, C 8, D 4.** The four B entries are named firm or company efforts without published measurements: PwC agents for K-1 and source-data mapping, PwC's self-explaining effective-tax-rate model, OpenAI's in-house agent-driven return computation, and Savant with Oxford Industries.
- **The field's own framing is data, ownership and governance before capability.** At the April 2026 TEI Tax Technology Seminar the question 'does this work?' was described as effectively settled, and the new problems were quiet hallucination, no clear AI owner (2 of more than 50 attendees polled said tax owns AI implementation), failed training rollouts and rising token costs (TEI-TAXTECH-2026). Thomson Reuters/TEI survey data show tax technology satisfaction fell to 34% from 56% in a year and departments providing technology training fell to 50% from 59% (TR-TAXTALENT-2026).
- **Regulatory deadlines are what move adoption in this module.** Form 6765 Section G becomes required for tax years beginning after 2025 for filers subject to the IRS guidelines (IRS-F6765INSTR-2025), and the first GloBE Information Return fell due on 30 June 2026 (TR-CORPAI-2026). Practitioners say the audit file is now effectively in the return (CBH-6765POD-2026).
- **Tax authorities are described as ahead.** A panel speaker said authorities in mature continuous-transaction-control regimes arrive at audits already knowing more about the transactions than the company, and one panelist described the job shifting 'from us preparing returns to us answering notices' (TRINST-TEIAUDITOR-2026). That discourse is mostly about indirect tax and is routed (section 4).
- **Role and pricing debates are live.** Sala argues AI will not shrink corporate tax teams much because AI cannot hold culpability (SALA-TAXNOTES-2026); 58% of German tax departments in a KPMG quick survey expect stable domestic headcount (KPMG-DE-2026); and the AICPA is challenging the IRS OPR line that AI savings should be passed to clients (AICPA-FEE-2026).

---

## 2. Use cases

Sixteen candidates. Grades by count: A 0, B 4, C 8, D 4. Ideas (D) are labelled 'idea' in the title. Estimated payments, extensions, state apportionment and 5471/8858 preparation have no AI-specific public discussion beyond the entries below; see section 6.

```yaml
- id: tax-compliance-corporate-01
  title: Agents interpret unstructured source-document items (K-1 footnotes, mixed-format client data) and map them to tax treatments, with a confidence level and override feedback
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: PwC's AI tax leader describes data that arrives from several systems and third parties in different formats, sometimes unmapped or missing metadata. For K-1s, staff were trained with guides to interpret footnotes and map items (for example a deductible expense), with heavy human review and OCR layered on top (PWC-MEGNA-2025).
  solution: Agents trained on how to treat different expenses and disclosures assess a footnote, say how they interpreted it and give a confidence level. The reviewer sees the flagged items, and an override must come with a reason so the agent can learn from the correction. PwC's Agent OS manages which tools (data mapping, document extraction) each agent uses (PWC-MEGNA-2025).
  outcomes:
  - lever: capacity
    description: Reviewer effort on a novel K-1 footnote, described as an illustration (no measurement)
    figure: none published
    measures: Interviewee says one person reviews the output where three people might previously have gathered to decide; no count, rate or time is published
    provenance: self-reported
    source_ref: PWC-MEGNA-2025
  prerequisites:
  - Historical treatment data to train the agents, and continued retraining as new data arrives (PWC-MEGNA-2025)
  - A tool layer (document extraction, mapping) and an orchestration layer to manage and monitor agents (PWC-MEGNA-2025)
  - A firm-level governance committee that oversees how agent systems are built and used, including in tax (PWC-MEGNA-2025)
  risks_and_guardrails:
  - The interviewee says confidence is improved through feedback 'ideally to 100%, though that's rare', so residual error is expected (PWC-MEGNA-2025).
  - Werfel's preparer risk register names incorrect document extraction (W-2, 1099, K-1) as a technical risk, with errors that can flow silently into the return (AICPA-WERFELART-2026).
  - No error rate or override rate is published for the agents (PWC-MEGNA-2025).
  human_checkpoints:
  - Reviewer checks flagged items against the stated confidence level
  - Override requires a recorded reason
  role_evolution: The interviewee describes review replacing group decision-making on novel items. PwC reports 3,200 AI champions, over 350,000 'My AI' training hours in the US firm and about 80% of people having taken some AI training (all self-reported, PWC-MEGNA-2025).
  evidence_grade: B
  sources:
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna, PwC US AI Tax Leader)
    publisher: CFO.com
    type: firm
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: Interview answers on mapping data / K-1s, feedback, risk and workforce; published 2025-06-06
  - ref: AICPA-WERFELART-2026
    title: A risk framework for AI use in tax administration and preparation (Danny Werfel)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/
    date: '2026-08-31'
    access: full
    locator: 'Figure 3, Technical risks: ''Incorrect document extraction'''
  last_reviewed: '2026-10-17'
  notes: 'Grade capped at B: a named firm deployment, no published measurements. The K-1 example is from the asset and wealth management space; the interviewee says mapping happens ''across all our tax businesses'', so use in corporate direct-tax compliance is inferred, not shown. ''In production'' reflects the reporter''s paraphrase that agents are deployed and moving ''beyond pilots''.'
- id: tax-compliance-corporate-02
  title: AI reads tax-authority notices (including state notices in varying formats), extracts amounts and due dates, rates complexity, drafts a response and logs it
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - transaction-processing
  - document-production
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: State tax notices 'never arrive in the same format twice' (TRINST-TEIAUDITOR-2026). Notice handling is a recurring in-house workload that TEI gave its own hands-on session at the 2026 Midyear conference (TEI-MIDYEAR-2026).
  solution: EY practitioners describe AI that reads a notice, summarises key points, amounts and due dates, judges complexity, drafts a response and logs the information to a database (EY-BTAX-2025). A TR Institute recap says seminar attendees were using AI image-to-text tools to pull structured data from state tax notices (TRINST-TEIAUDITOR-2026).
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: No figure for notice handling time, accuracy or override rate appears in any source read
    provenance: self-reported
    source_ref: EY-BTAX-2025
  prerequisites:
  - A structured log (database) for notices, amounts and due dates (EY-BTAX-2025)
  - Image-to-text capability for notices that vary in format (TRINST-TEIAUDITOR-2026)
  risks_and_guardrails:
  - A missed due date or misread amount has penalty consequences; the sources describe no accuracy testing.
  - TEI attendees described AI errors that are 'polite' and quiet, which makes review harder as volume grows (TEI-TAXTECH-2026).
  - 'Werfel''s preparer register lists control dilution: review that stays the same on paper but gets less rigorous as volume rises (AICPA-WERFELART-2026).'
  human_checkpoints:
  - Person reviews the drafted response before it goes to the authority
  - Person confirms due dates and amounts for complex or high-dollar notices
  role_evolution: The shift described is from keying and reading notices to reviewing drafts and managing the notice log; no source quantifies the effect.
  evidence_grade: C
  sources:
  - ref: EY-BTAX-2025
    title: AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way (opinion by D. Campbell and R. Carpenter, EY)
    publisher: Bloomberg Tax
    type: firm
    url: https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way
    date: '2025-11-21'
    access: full
    locator: Section 'Enterprise Tax Functions', item 'Tax notices'
  - ref: TRINST-TEIAUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: Section 'End of the traditional model', paragraph on data pipelines and image-to-text for state tax notices
  - ref: TEI-MIDYEAR-2026
    title: TEI's 2026 Midyear Conference, Preliminary Program (At a Glance agenda)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: 'Tuesday 17 March 2026, 1:30-2:30 PM: ''TEI Tax Lab: Managing Tax Notices with AI'' (preliminary program)'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (recap of TEI Tax Technology Seminar, Las Vegas)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: 'Section ''A very bad wizard'': review of increasingly polite, quiet errors'
  last_reviewed: '2026-10-17'
  notes: Firm and conference discussion only. The EY piece lists notices among 'key use cases emerging now'; the recap does not name the organisations using notice extraction. No deployment with a named organisation or a measurement was found.
- id: tax-compliance-corporate-03
  title: 'In-house agent-driven corporate return computation: consolidated 1120, 1065, 5471 and state returns computed from a version-controlled tax-logic library, replacing outsourced preparation'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  - software-systems
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: A company that sends its income, gross receipts and property tax compliance to outside preparers must manage vendors, reconcile provision to return, run the compliance calendar and respond to notices through spreadsheets and email (OPENAI-TAXCOMPLIANCEJOB-2025).
  solution: OpenAI's tax team lists a role to move from outsourced return preparation to 'internal, logic-driven, agent-powered return computation', with modular, version-controlled tax-logic libraries, audit-ready 'self-documenting' engines for areas such as GILTI, CAMT and FDII, and a Corptax implementation feeding the agentic workflows. The listing describes multi-agent systems that 'classify, compute, reconcile, and report' and an initiative called Project Hive (OPENAI-TAXCOMPLIANCEJOB-2025). A 2026 listing describes database-driven workflows where preparation is 'increasingly automated' and the manager focuses on review and validation (OPENAI-USTAXOPSJOB-2026).
  outcomes:
  - lever: cost
    description: none published; the 2025 listing states a goal of automating the tax stack in under 12 months
    figure: none published
    measures: No result for return cost, cycle time or error rate is published; the 12-month statement is a stated aim in recruiting copy
    provenance: self-reported
    source_ref: OPENAI-TAXCOMPLIANCEJOB-2025
  prerequisites:
  - Corptax (named as the compliance engine) and ERP data pipelines (Oracle, Workday named) (OPENAI-TAXCOMPLIANCEJOB-2025)
  - Tax staff able to codify positions as logic, with SQL, Python and metadata governance skills (OPENAI-TAXCOMPLIANCEJOB-2025; OPENAI-TAXDATAJOB-2025)
  - Simulation and logic-testing environments (OPENAI-TAXCOMPLIANCEJOB-2025)
  risks_and_guardrails:
  - 'The evidence is recruiting copy: the 2025 listing says the role will ''contribute to'' Project Hive and ''build'' the systems, so the described capability is partly aspirational (OPENAI-TAXCOMPLIANCEJOB-2025).'
  - An OpenAI panelist at TEI conceded that AI-built pipelines raise security questions when nobody else has reviewed or documented them (TRINST-TEIAUDITOR-2026).
  - Only 2 of more than 50 attendees polled at TEI said the tax function owns AI implementation in their company, so ownership is a common gap (TEI-TAXTECH-2026).
  human_checkpoints:
  - Manager oversees external vendors during scope transition (OPENAI-TAXCOMPLIANCEJOB-2025)
  - Reviewer performs first-level review and validation of automated outputs (OPENAI-USTAXOPSJOB-2026)
  role_evolution: The 2025 listing frames the role as moving 'from compliance executor to process architect'. The 2026 listing says the manager will focus on 'review, validation, and improvement of tax outputs' and asks for comfort working outside Excel-heavy workflows (OPENAI-TAXCOMPLIANCEJOB-2025; OPENAI-USTAXOPSJOB-2026).
  evidence_grade: B
  sources:
  - ref: OPENAI-TAXCOMPLIANCEJOB-2025
    title: Manager, Tax Compliance and Automation (OpenAI job listing)
    publisher: Omega Venture Partners job board (OpenAI)
    type: job-posting
    url: https://jobs.omegavp.com/companies/openai/jobs/52055389-manager-tax-compliance-and-automation
    date: '2025-06-05'
    access: full
    locator: About the Role; In this role you'll; listing posted 2025-06-05, valid through 2025-07-15
  - ref: OPENAI-USTAXOPSJOB-2026
    title: Manager, US Tax Operations (OpenAI job listing)
    publisher: Glynn Capital job board (OpenAI)
    type: job-posting
    url: https://jobs.glynncapital.com/companies/openai/jobs/74040402-manager-us-tax-operations
    date: '2026-04-11'
    access: full
    locator: About the Team; About the Role; In this role, you will; listing posted 2026-04-11
  - ref: OPENAI-TAXDATAJOB-2025
    title: Senior Manager, Tax Data Automation (OpenAI job listing)
    publisher: Khosla Ventures job board (OpenAI)
    type: job-posting
    url: https://jobs.khoslaventures.com/companies/openai/jobs/45083210-senior-manager-tax-data-automation
    date: '2025-01-22'
    access: full
    locator: About the Role; In this role, you will; listing posted 2025-01-22
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (recap of TEI Tax Technology Seminar, Las Vegas)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: 'Section ''A very good man'': OpenAI sent four members of its own tax department to demonstrate live automation pipelines; section ''A very bad wizard'': ownership poll'
  - ref: TRINST-TEIAUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: 'Section ''Two ways to lose'': OpenAI panelist and vibe-coding security question'
  last_reviewed: '2026-10-17'
  notes: 'Named deployment at an AI lab''s own tax department, with no published measurements. The sources are job listings and a conference recap, so maturity is set to ''piloting'', not ''in production''. Landscape correction: the recap says OpenAI sent four members of its tax department to the seminar, which is not the size of the department. A frontier-lab tax team is an unusual starting point, so transfer to other companies is not shown.'
- id: tax-compliance-corporate-04
  title: 'Governed agentic automation of tax data work: reconciling ERP data to source documents, extraction and validation, with lineage for audit'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - data-reporting
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Savant describes tax teams under pressure to modernise while facing heightened regulatory scrutiny, with governance a key challenge in deployments (SAVANT-2026). TEI attendees described workflows built in Alteryx that nobody could explain after the builder left (TEI-TAXTECH-2026).
  solution: Savant's release says its platform turns 'raw, messy data' into governed, repeatable outputs with a full audit trail, and that Oxford Industries' tax team co-presented a session on deploying AI safely at scale at the TEI Tax Technology Seminar on 28 April 2026. Booth demonstrations covered multi-system reconciliation across ERPs and source documents, AI document extraction and validation, and audit-ready reporting with data lineage (SAVANT-2026).
  outcomes:
  - lever: quality
    description: none published for Oxford Industries
    figure: none published
    measures: The release gives no outcome figure for the Oxford Industries deployment and does not say which tax processes it covers
    provenance: vendor-published
    source_ref: SAVANT-2026
  prerequisites:
  - Access to ERP and source-document systems
  - Process documentation and ownership so automated workflows can be explained after staff turnover (TEI-TAXTECH-2026)
  risks_and_guardrails:
  - The release is a pre-event announcement from the vendor; the session content was not seen (SAVANT-2026).
  - Silent failures, failed training rollouts and unexplained legacy workflows were named at the same seminar as the main obstacles (TEI-TAXTECH-2026).
  human_checkpoints:
  - Tax staff review exceptions from reconciliations
  - Audit trail and data lineage retained for reviewers and auditors (SAVANT-2026)
  role_evolution: No role change is published for Oxford Industries.
  evidence_grade: B
  sources:
  - ref: SAVANT-2026
    title: Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Technology Seminar 2026
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/
    date: '2026-04-16'
    access: full
    locator: 'Press release dated 2026-04-16: session abstract, speakers (Savant CEO and Oxford Industries Senior Director of Tax & Accounting), demonstration list'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (recap of TEI Tax Technology Seminar, Las Vegas)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: 'Section ''A very bad wizard'': training rollout failure; Alteryx workflows nobody could explain'
  last_reviewed: '2026-10-17'
  notes: Named customer (Oxford Industries) from a vendor announcement; the process scope within corporate compliance is not stated, so relevance to this module is partial (demos cover sales and use, VAT/GST, reconciliation, extraction). Treated as 'in production' because the release says Oxford's tax team 'deploys' AI; no independent confirmation.
- id: tax-compliance-corporate-05
  title: 'R&D credit and Form 6765 Section G: AI clusters contemporaneous project, payroll and ledger data into business components, applies the four-part test and populates the form'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: 'For tax years beginning after 2025, Section G is required for filers subject to the IRS guidelines: QREs reported by business component, a minimum of 80% of total QREs or a maximum of 50 business components (IRS-F6765INSTR-2025). A practitioner podcast says the IRS now wants in the return the detail it used to ask for only on examination (CBH-6765POD-2026). Thomson Reuters says the interview-based, after-the-fact approach struggles to meet that standard, with tax and R&D teams spending over 200 hours a year on coordination (NEOTAX-TR-2025).'
  solution: Neo.Tax, integrated with ONESOURCE Income Tax, connects payroll, project-management and accounting systems by API, ingests project data, groups it into IRS-qualifying business components, applies the four-part test, reconciles payroll and GL data to allocate cost, and populates Form 6765 including Section G (TR-CORPAI-2026; NEOTAX-TR-2025). TEI ran a Tax Lab on research credit automation (TEI-MIDYEAR-2026).
  outcomes:
  - lever: speed
    description: Annual time saved on R&D credit compliance
    figure: up to 150+ hours saved annually
    measures: Thomson Reuters' stated 'time efficiency' for the ONESOURCE + Neo.Tax integration; the post does not say per team, per entity or how it was measured
    provenance: vendor-published
    source_ref: NEOTAX-TR-2025
  - lever: cost
    description: Cost versus accounting-firm R&D studies
    figure: 50-75% savings
    measures: '''Companies report'' savings compared with accounting firm fees, which the post says range from $100k to $500k; sample size and method not stated'
    provenance: vendor-published
    source_ref: NEOTAX-TR-2025
  - lever: risk
    description: Fin 48 (uncertain tax position) reserves
    figure: 20-30% lower
    measures: '''Companies report'' lower Fin 48 reserves compared with interview-driven studies; sample size and method not stated'
    provenance: vendor-published
    source_ref: NEOTAX-TR-2025
  prerequisites:
  - Project-management, payroll and accounting data that records work as it happens (NEOTAX-TR-2025; TR-CORPAI-2026)
  - ONESOURCE Income Tax if the form is to be populated directly (NEOTAX-TR-2025)
  - Documentation that traces each claimed dollar to a business component (CBH-6765POD-2026)
  risks_and_guardrails:
  - Strike Tax Advisory, which sells a competing human-led service, argues AI questionnaire tools can produce a number but not a defensible claim, and that vendor liability is typically capped at fees paid; treat as a competitor's view (STRIKE-6765-2026).
  - No customer is named and no independent measurement of accuracy or audit outcome was found for this use.
  - Section G exemptions and amended-return rules apply; check the IRS instructions for the filer (IRS-F6765INSTR-2025).
  human_checkpoints:
  - Tax and technical staff confirm business-component boundaries and four-part test conclusions
  - Preparer reviews Section G narratives and cost allocation before filing
  role_evolution: Thomson Reuters' framing is that engineers' interviews and retrospective surveys give way to tax staff reviewing system-generated documentation; the post says this reduces dependence on outside advisers (NEOTAX-TR-2025).
  evidence_grade: C
  sources:
  - ref: NEOTAX-TR-2025
    title: How to eliminate the burden of R&D tax credit compliance (ONESOURCE + Neo.Tax)
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/neo-tax-onesource-eliminating-the-triple-burden-of-rd-credit-compliance/
    date: '2025-09-08'
    access: full
    locator: Sections 'The triple burden', 'Advantages of a modern R&D tax credit process'
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: 'Section ''Neo.Tax: Automating R&D credits under the new IRS rules'''
  - ref: IRS-F6765INSTR-2025
    title: Instructions for Form 6765 (12/2025), Credit for Increasing Research Activities
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/instructions/i6765
    date: 2025-12
    access: full
    locator: What's New / Section G requirements; '80%/Top 50' business components
  - ref: CBH-6765POD-2026
    title: 'Life Sciences R&D Tax Credits: Form 6765 Changes, New Reporting Requirements and Compliance Strategies (Healthcare & Life Sciences Podcast, with transcript)'
    publisher: Cherry Bekaert
    type: podcast
    url: https://www.cbh.com/insights/podcasts/life-sciences-rd-tax-credits-form-6765-changes/
    date: '2026-10-09'
    access: full
    locator: 'Transcript: new Section G, ''When does all of this kick in?'' and documentation discussion'
  - ref: TEI-MIDYEAR-2026
    title: TEI's 2026 Midyear Conference, Preliminary Program (At a Glance agenda)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: 'Tuesday 17 March 2026: ''TEI Tax Lab: Research Credit Automation'''
  - ref: STRIKE-6765-2026
    title: Form 6765 Section G Becomes Mandatory in 2026. Most AI-Only R&D Credit Tools Will Not Be Ready.
    publisher: Strike Tax Advisory (R&D credit adviser; competes with software-only providers)
    type: vendor
    url: https://www.striketax.com/journal/form-6765-section-g-becomes-mandatory-in-2026-most-ai-only-r-d-credit-tools-will-not-be-ready
    date: '2026-05-28'
    access: full
    locator: Key Takeaways and section on why the R&D credit resists automation
  last_reviewed: '2026-10-17'
  notes: All outcome figures are vendor-published and unnamed-customer; no figure is independent. The IRS instructions page shows a 12/2025 revision, while practitioners (CBH-6765POD-2026, STRIKE-6765-2026) report final instructions in early February 2026; the IRS page was not checked for a release date.
- id: tax-compliance-corporate-06
  title: Agents track regulatory change and the filing calendar and distribute comparison reports to the tax team
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: 'Two regulatory milestones compressed direct-tax work: Section G of Form 6765 (mandatory from tax year 2026) and the first GloBE Information Return, due 30 June 2026 (TR-CORPAI-2026). An in-house compliance role is expected to keep a ''real-time, transparent compliance calendar'' across entities and jurisdictions (OPENAI-TAXCOMPLIANCEJOB-2025).'
  solution: Orbitax's XatBot 'Tax Flows' tracks regulatory changes across jurisdictions and proactively sends comparison reports to stakeholders (TR-CORPAI-2026). Bloomberg Tax lists an AI Assistant in Compliance Tracker that summarises and analyses filings (BTAX-TOOLS-2026). CSC Corptax's roadmap includes tax code version tracking (CORPTAX-2026). KPMG's US tax leader says building an agent to help clients adjust to changing tax rules went from weeks to minutes on its new platform (KPMG-ANTHROPIC-2026).
  outcomes:
  - lever: speed
    description: Time to build an agent for changing tax rules, as described by KPMG's US tax leader
    figure: weeks to minutes
    measures: Rema Serafi's statement about building a client-facing agent on KPMG Digital Gateway with Claude; no sample, task definition or measurement method is published
    provenance: self-reported
    source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
  - A maintained list of entities, jurisdictions and filing obligations
  - Authoritative sources for the rule changes being tracked
  risks_and_guardrails:
  - A tool that summarises rule changes can present outdated or incorrect guidance with confidence; Bloomberg Tax cites training cutoffs and fast-changing guidance as a cause (BTAX-HALLUC-2026).
  - Estimated-payment and extension handling by AI was not found in any source read.
  human_checkpoints:
  - Tax staff decide which changes affect the return or payment calendar
  - A person approves any filing or payment action
  role_evolution: No change is published; the sources describe the tools as aids for monitoring.
  evidence_grade: C
  sources:
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: Section 'Orbitax' (Tax Flows mode)
  - ref: BTAX-TOOLS-2026
    title: Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026
    date: '2026-03-09'
    access: full
    locator: 'Feature list: ''AI Assistant in Compliance Tracker'''
  - ref: CORPTAX-2026
    title: 'Webinar: Unlock the Power of Tax AI (AI and ML in Tax: Applications, Considerations, and Responsible Engagement), with ACT'
    publisher: CSC Corptax
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: '2026'
    access: full
    locator: '''Corptax AI/ML roadmap'' bullets: tax code version tracking'
  - ref: KPMG-ANTHROPIC-2026
    title: KPMG Partners with Anthropic for Digital Gateway Powered by Claude
    publisher: CPA Practice Advisor (KPMG and Anthropic announcement)
    type: firm
    url: https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/
    date: '2026-05-20'
    access: full
    locator: Quote from Rema Serafi, Vice Chair, Tax, KPMG US
  - ref: OPENAI-TAXCOMPLIANCEJOB-2025
    title: Manager, Tax Compliance and Automation (OpenAI job listing)
    publisher: Omega Venture Partners job board (OpenAI)
    type: job-posting
    url: https://jobs.omegavp.com/companies/openai/jobs/52055389-manager-tax-compliance-and-automation
    date: '2025-06-05'
    access: full
    locator: 'In this role you''ll: compliance calendar'
  - ref: BTAX-HALLUC-2026
    title: 'AI Hallucinations in Tax: The Risks and How to Mitigate Them'
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/?p=16920
    date: '2026-05-11'
    access: full
    locator: Section 'Why does generative AI hallucinate?'
  last_reviewed: '2026-10-17'
  notes: Product announcements and roadmap items only; no named user or measurement. Corptax page is undated (2026 copyright); the Orbitax feature set is a vendor description of an upgrade.
- id: tax-compliance-corporate-07
  title: 'Reviewer aids for compliance outputs: validation agents critique prepared output, document comparison, and first-level review of automated results'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Reviewers face 'an ever-increasing volume of work' where errors are 'increasingly polite, quiet, and technical' (TEI-TAXTECH-2026). EY practitioners say reviewers who once checked subtotals now receive conclusions to review and must understand the process (EY-BTAX-2025).
  solution: A TR Institute recap says some seminar attendees deploy validation agents to critique their own agents' outputs (TRINST-TEIAUDITOR-2026). Corptax's roadmap lists PDF comparisons to streamline document analysis (CORPTAX-2026). OpenAI's 2026 listing includes first-level review and validation of automated provision outputs (OPENAI-USTAXOPSJOB-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No error-catch rate, override rate or reviewer time is published in any source read
    provenance: self-reported
    source_ref: TRINST-TEIAUDITOR-2026
  prerequisites:
  - A definition of what the reviewer checks (inputs, process, outputs) rather than only the arithmetic (EY-BTAX-2025)
  risks_and_guardrails:
  - 'Werfel names control dilution: review processes that do not scale with AI-driven volume get weaker even if they stay unchanged on paper (AICPA-WERFELART-2026).'
  - EY warns of a divide between experienced staff who spot AI problems and newer staff who may over-rely on results (EY-BTAX-2025).
  - An AI agent told a TEI attendee it could not open the file and was 'telling you what you wanted to hear' (TEI-TAXTECH-2026).
  human_checkpoints:
  - Named reviewer signs off on the compliance output
  - Reviewer samples AI-flagged and unflagged items
  role_evolution: EY says the profession shifts from assembling information to applying critical judgment and high-quality review (EY-BTAX-2025).
  evidence_grade: C
  sources:
  - ref: TRINST-TEIAUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: 'Section ''End of the traditional model'': validation agents critiquing their own outputs'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (recap of TEI Tax Technology Seminar, Las Vegas)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Sections 'A very bad wizard' and 'Going home'
  - ref: EY-BTAX-2025
    title: AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way (opinion by D. Campbell and R. Carpenter, EY)
    publisher: Bloomberg Tax
    type: firm
    url: https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way
    date: '2025-11-21'
    access: full
    locator: Sections 'People, Skills, Culture' and 'Questions for 2026'
  - ref: CORPTAX-2026
    title: 'Webinar: Unlock the Power of Tax AI (AI and ML in Tax: Applications, Considerations, and Responsible Engagement), with ACT'
    publisher: CSC Corptax
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: '2026'
    access: full
    locator: 'Roadmap bullet: PDF comparisons'
  - ref: OPENAI-USTAXOPSJOB-2026
    title: Manager, US Tax Operations (OpenAI job listing)
    publisher: Glynn Capital job board (OpenAI)
    type: job-posting
    url: https://jobs.glynncapital.com/companies/openai/jobs/74040402-manager-us-tax-operations
    date: '2026-04-11'
    access: full
    locator: 'In this role, you will: first-level review and validation'
  - ref: AICPA-WERFELART-2026
    title: A risk framework for AI use in tax administration and preparation (Danny Werfel)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/
    date: '2026-08-31'
    access: full
    locator: 'Figure 3, Practice: ''Control dilution'''
  last_reviewed: '2026-10-17'
  notes: Practitioner statements and one roadmap item; no named deployment with a result. The agent-critiques-agent claim is attributed to unnamed attendees in a vendor-owned recap.
- id: tax-compliance-corporate-08
  title: Tax analysts build data-integration pipelines and agents with AI coding tools instead of waiting in the IT queue
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - software-systems
  - data-reporting
  pattern: bulk-transformation
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Data pipelines for tax would otherwise 'sit in an IT queue' for about two months (TRINST-TEIAUDITOR-2026). Only 50% of corporate tax departments provided technology training in 2025, down from 59% (TR-TAXTALENT-2026).
  solution: Attendees at the 2026 TEI seminar described vibe-coding data-integration pipelines in about 15 minutes, using platforms such as Alteryx, Power Platform, Snowflake, Databricks, Microsoft Fabric and Palantir Foundry (TRINST-TEIAUDITOR-2026). Google and Microsoft showed attendees how to build agents (TEI-TAXTECH-2026).
  outcomes:
  - lever: speed
    description: Time to build a data-integration pipeline
    figure: about 15 minutes (versus about two months in an IT queue)
    measures: Recap's description of what attendees do; no organisation, number of pipelines or measurement is given
    provenance: self-reported
    source_ref: TRINST-TEIAUDITOR-2026
  prerequisites:
  - Access to tax data in a platform the analyst can build on
  - Training; only 9% rate colleagues as very competent with technology (TR-TAXTALENT-2026)
  risks_and_guardrails:
  - The same recap says such tools let an analyst deploy something 'nobody else has reviewed, documented, or knows how to maintain', and an OpenAI panelist conceded the security point (TRINST-TEIAUDITOR-2026).
  - Alteryx workflows nobody could explain after the builder left were cited at the seminar (TEI-TAXTECH-2026).
  human_checkpoints:
  - Independent review and documentation of any pipeline before it feeds a return
  role_evolution: TR's survey shows 62% of 2025 new hires emphasised tax expertise over technology skills, after 57% of new roles in 2024 went to tech and IT expertise; hybrid tax/tech roles are rising (TR-TAXTALENT-2026).
  evidence_grade: C
  sources:
  - ref: TRINST-TEIAUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: Section 'End of the traditional model' and 'Two ways to lose'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (recap of TEI Tax Technology Seminar, Las Vegas)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very good man'; 'A very bad wizard'
  - ref: TR-TAXTALENT-2026
    title: Why corporate tax tech is falling short and how talent development can fix it (2026 Corporate Tax Technology Report)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/tax-tech-talent-development
    date: '2026-05-01'
    access: full
    locator: Key insights; sections 'Tech competency remains a challenge' and 'Pendulum swing in hiring'
  last_reviewed: '2026-10-17'
  notes: Unnamed attendees; recap authored by a vendor-owned institute. No quality evidence.
- id: tax-compliance-corporate-09
  title: 'Idea: AI agents flag common anomalies in source data and account reconciliations upstream of the return, for human review'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Deloitte's scenario paper says that when tax authorities run real-time analytics, finding and fixing errors after submission 'would no longer be sufficient', and persistent data fragmentation and manual controls erode resilience (DELOITTE-TTT-2026).
  solution: Deloitte suggests, as an example, using AI agents to flag common anomalies in source data and account reconciliations for human review, and moving to preventive controls upstream in business processes (DELOITTE-TTT-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Scenario-planning paper; no measurement
    provenance: vendor-published
    source_ref: DELOITTE-TTT-2026
  prerequisites:
  - Better upstream data quality and links between tax, finance and operations (DELOITTE-TTT-2026)
  risks_and_guardrails:
  - Deloitte says leaders may want a hybrid model and an audit trail for authorities that are not capable of real-time interaction (DELOITTE-TTT-2026).
  human_checkpoints:
  - Human reviewer resolves flagged anomalies before data reaches the return
  role_evolution: Deloitte expects talent with strong data analytics, technology integration and project management skills where authorities are ahead of the company (DELOITTE-TTT-2026).
  evidence_grade: D
  sources:
  - ref: DELOITTE-TTT-2026
    title: 'Riding the wave: A framework to plan for AI (AI-enabled Tax Transformation, Tax Transformation Trends AI report, part three)'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: Scenario 1 and Scenario 3 sections (pages 4 and 6 of the PDF)
  last_reviewed: '2026-10-17'
  notes: Idea discussed in a Big Four scenario paper; no deployment found. Date is month-level from the PDF metadata (the document itself shows a 2026 copyright).
- id: tax-compliance-corporate-10
  title: 'Idea: continuous, always-on compliance monitoring replacing batch filing cycles'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: In jurisdictions with continuous transaction controls, tax authorities see transactions as they happen and pre-fill returns, and one panelist described the job as shifting from preparing returns to answering notices on shared data (TRINST-TEIAUDITOR-2026).
  solution: EY practitioners describe AI agents that analyse compliance metrics continuously and trigger alerts or remediation before deadlines, instead of batch filings (EY-BTAX-2025). Deloitte's fourth scenario envisions continuous or near real-time compliance with preventive AI-driven controls (DELOITTE-TTT-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Forward-looking descriptions; no measurement
    provenance: self-reported
    source_ref: EY-BTAX-2025
  prerequisites:
  - Structured, near real-time transaction and ledger data (TRINST-TEIAUDITOR-2026)
  - Preventive controls built into upstream business processes (DELOITTE-TTT-2026)
  risks_and_guardrails:
  - One panelist described companies giving up on compliance and padding numbers, treating audit as the cheaper cost; another panelist said 'Do not do this' (TRINST-TEIAUDITOR-2026).
  - Agentic tools raise the bar for data lineage and human judgment (EY-BTAX-2025).
  human_checkpoints:
  - Person decides on remediation when an alert fires
  role_evolution: Deloitte says tax professionals would shift from preparation to oversight, interpretation, policy interaction and dispute resolution in its fourth scenario (DELOITTE-TTT-2026).
  evidence_grade: D
  sources:
  - ref: EY-BTAX-2025
    title: AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way (opinion by D. Campbell and R. Carpenter, EY)
    publisher: Bloomberg Tax
    type: firm
    url: https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way
    date: '2025-11-21'
    access: full
    locator: Section 'Enterprise Tax Functions', item 'Continuous audit and always-on monitoring'
  - ref: DELOITTE-TTT-2026
    title: 'Riding the wave: A framework to plan for AI (AI-enabled Tax Transformation, Tax Transformation Trends AI report, part three)'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: Scenario 4 'Tax transformed' (page 7 of the PDF)
  - ref: TRINST-TEIAUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: Sections 'End of the traditional model', 'Outgunned' and 'Two ways to lose'
  last_reviewed: '2026-10-17'
  notes: Idea only. Most of the continuous-controls discussion is about indirect tax in real-time-reporting jurisdictions, so direct-tax relevance is by analogy; see 'Routed to other modules'.
- id: tax-compliance-corporate-11
  title: Pre-filing audit-trigger prediction from the prepared return and prior-year data
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Tax authorities increasingly arrive at audits already holding structured data processed by their own analytics, according to a panel speaker quoted in a TR Institute recap (TRINST-TEIAUDITOR-2026).
  solution: CSC Corptax's webinar page lists 'audit prediction to address potential triggers early' as part of its AI/ML roadmap, alongside PDF comparison and tax-code version tracking (CORPTAX-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Roadmap item; no result
    provenance: vendor-published
    source_ref: CORPTAX-2026
  prerequisites:
  - Prior-year and current-year return data in the compliance engine
  risks_and_guardrails:
  - A tool that predicts audit triggers is an advisory aid; the sources say nothing about its validation. Treat as a hypothesis until tested against the department's own audit history.
  human_checkpoints:
  - Preparer decides whether to change a position or add disclosure
  role_evolution: None published.
  evidence_grade: C
  sources:
  - ref: CORPTAX-2026
    title: 'Webinar: Unlock the Power of Tax AI (AI and ML in Tax: Applications, Considerations, and Responsible Engagement), with ACT'
    publisher: CSC Corptax
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: '2026'
    access: full
    locator: '''Corptax AI/ML roadmap'' bullet list'
  - ref: TRINST-TEIAUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: Section 'Outgunned'
  last_reviewed: '2026-10-17'
  notes: Single vendor roadmap line; the pattern is set to 'other' (prediction of risk before filing). Page is undated (2026 copyright).
- id: tax-compliance-corporate-12
  title: Model-generated reasoning chain (inputs, outputs, assumptions) becomes the deliverable in place of a memo, and approved logic is locked
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: 'Clients and auditors ask whether AI-prepared tax work will hold up under scrutiny. PwC''s AI tax leader says explainability, traceability and auditability are the test: ''If you can''t explain it, you can''t trust it'' (PWC-MEGNA-2025).'
  solution: PwC says a model it uses to calculate effective tax rates is trained to explain itself (inputs, output, assumptions), so the logic chain is part of the deliverable where a memo would previously have been written. Once something is approved it is locked, and people suggest improvements instead of making ad hoc changes (PWC-MEGNA-2025).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Interview statement only; no measurement of memo time or review findings
    provenance: self-reported
    source_ref: PWC-MEGNA-2025
  prerequisites:
  - Governance committee and responsible-AI toolkit built around explainability, traceability and auditability (PWC-MEGNA-2025)
  risks_and_guardrails:
  - PwC says oversight is stronger for complex outputs such as tax calculations, with multi-eye review (PWC-MEGNA-2025).
  - Werfel lists lack of transparency (no clear policy on how AI is used, disclosed and documented) as a preparer risk (AICPA-WERFELART-2026).
  human_checkpoints:
  - Multi-eye human review of tax calculation outputs
  - Approval step before logic is locked
  role_evolution: Staff review generated reasoning rather than write the memo; no headcount effect is published.
  evidence_grade: B
  sources:
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna, PwC US AI Tax Leader)
    publisher: CFO.com
    type: firm
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: Answers on risk, regulatory review and trust
  - ref: AICPA-WERFELART-2026
    title: A risk framework for AI use in tax administration and preparation (Danny Werfel)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/
    date: '2026-08-31'
    access: full
    locator: 'Figure 3, Business: ''Lack of transparency'''
  last_reviewed: '2026-10-17'
  notes: 'Grade capped at B: the example is effective-tax-rate calculation, which is provision work (an adjacent process), and no measurement is published. Relevant to compliance workpaper documentation by analogy.'
- id: tax-compliance-corporate-13
  title: 'Idea: value-based or fixed-fee pricing of AI-enabled compliance work, instead of passing time savings to clients'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - client-interaction
  - document-production
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: IRS OPR's June 2026 guidance says billing for manual time that was not spent, or double billing AI-assisted tasks, may violate the Circular 230 fee rule, and that cost savings should be passed on openly (IRS-OPR-2026).
  solution: The AICPA is seeking clarification from the IRS, saying the OPR language does not appear to allow for value pricing and overlooks software, implementation, governance and training costs. AICPA's CEO says many CPAs have moved to value pricing and some bundle return preparation at no additional charge (AICPA-FEE-2026).
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: Debate about pricing; no pricing outcome is published
    provenance: self-reported
    source_ref: AICPA-FEE-2026
  prerequisites:
  - Engagement terms that describe the AI-enabled service and its pricing basis
  risks_and_guardrails:
  - OPR ties the fee guidance to Circular 230 section 10.27(a) and says practitioners should disclose AI activities as needed (IRS-OPR-2026).
  - The AICPA's CEO calls the OPR language not authoritative; the IRS response was not found (AICPA-FEE-2026).
  human_checkpoints:
  - Engagement partner approves the pricing basis
  role_evolution: Not stated; the dispute concerns how efficiency gains are shared with clients.
  evidence_grade: D
  sources:
  - ref: AICPA-FEE-2026
    title: AICPA seeks IRS clarity on AI guidelines, CPA fees
    publisher: The Tax Adviser (AICPA)
    type: press
    url: https://www.thetaxadviser.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/
    date: '2026-09-08'
    access: full
    locator: Whole article (news item, 2026-09-08)
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: 'Regulatory Framework: Circular 230 Provisions, item 2 (section 10.27(a))'
  last_reviewed: '2026-10-17'
  notes: Idea discussed by the AICPA and IRS OPR; the discussion concerns CPA practices broadly, not large-firm corporate compliance specifically. The idea is labelled 'idea'; no deployed pricing model tied to AI was confirmed.
- id: tax-compliance-corporate-14
  title: 'Idea: AI analyses Excel workpapers and files in natural language (''Escaping Excel'')'
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: TEI attendees described analyst work built on Excel and Alteryx workflows that nobody could explain after the builder left (TEI-TAXTECH-2026).
  solution: 'TEI''s 2026 Midyear programme included a Tax Lab titled ''Escaping Excel: Using AI to Analyze Excel Files for Accountants'' (TEI-MIDYEAR-2026).'
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: Session title only; no content seen
    provenance: self-reported
    source_ref: TEI-MIDYEAR-2026
  prerequisites:
  - Workpapers in a structure a tool can read
  risks_and_guardrails:
  - An agent that cannot open a file may still report on it (TEI-TAXTECH-2026).
  - Do not enter confidential information in tools without enterprise-grade privacy controls (WK-CORPRES-2026).
  human_checkpoints:
  - Preparer checks the figures against the underlying workbook
  role_evolution: None published.
  evidence_grade: D
  sources:
  - ref: TEI-MIDYEAR-2026
    title: TEI's 2026 Midyear Conference, Preliminary Program (At a Glance agenda)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: 'Tuesday 17 March 2026, 4:15-5:15 PM: ''TEI Tax Lab: Escaping Excel'' (preliminary program)'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (recap of TEI Tax Technology Seminar, Las Vegas)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard'
  - ref: WK-CORPRES-2026
    title: How controllers and corporate tax leaders can use AI for faster, defensible tax returns (corporate tax research guide)
    publisher: Wolters Kluwer Tax & Accounting
    type: vendor
    url: https://www.wolterskluwer.com/en/expert-insights/how-controllers-and-corporate-tax-leaders-can-use-ai-for-faster-defensible-tax-returns
    date: '2026-04-02'
    access: full
    locator: Section 'The non-negotiables for purchasing decision-makers'
  last_reviewed: '2026-10-17'
  notes: 'Idea: a conference session title with no session content. Labelled ''idea''.'
- id: tax-compliance-corporate-15
  title: Prompt-to-conclusion audit trail captured with each AI-assisted position in the workpapers
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Decisions made with AI may be reviewed months later or handed to new staff; Wolters Kluwer says outputs must stand up to internal controls and external review (WK-CORPRES-2026). EY practitioners say 'it's not just whether you used AI; it's what you did to validate the AI results' (EY-BTAX-2025).
  solution: Wolters Kluwer advises recording the question or prompt, the output, the citations, the validation steps and the final conclusion, with the flow AI output, professional validation, documented conclusion (WK-CORPRES-2026). Thomson Reuters' CoCounsel Tax is described as returning cited sources and a reasoning chain for each response (TR-AGENTICCORP-2025).
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Guidance and product description; no measurement
    provenance: vendor-published
    source_ref: WK-CORPRES-2026
  prerequisites:
  - A defined acceptable-use policy and escalation rules (WK-CORPRES-2026)
  risks_and_guardrails:
  - The guide is vendor-written and about corporate tax research rather than return preparation (WK-CORPRES-2026).
  - Werfel's register lists lack of transparency, with no clear policy on how AI is used, disclosed to clients and documented (AICPA-WERFELART-2026).
  - OPR says practitioners must review everything AI produces before delivery to a client or the IRS (IRS-OPR-2026).
  human_checkpoints:
  - Preparer records what was verified and signs off the conclusion
  role_evolution: Reviewers inspect the record of validation as well as the result; no source quantifies the effect.
  evidence_grade: C
  sources:
  - ref: WK-CORPRES-2026
    title: How controllers and corporate tax leaders can use AI for faster, defensible tax returns (corporate tax research guide)
    publisher: Wolters Kluwer Tax & Accounting
    type: vendor
    url: https://www.wolterskluwer.com/en/expert-insights/how-controllers-and-corporate-tax-leaders-can-use-ai-for-faster-defensible-tax-returns
    date: '2026-04-02'
    access: full
    locator: 'Sections ''Implementation playbook'' and ''Checklist: using AI safely for corporate tax research'''
  - ref: EY-BTAX-2025
    title: AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way (opinion by D. Campbell and R. Carpenter, EY)
    publisher: Bloomberg Tax
    type: firm
    url: https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way
    date: '2025-11-21'
    access: full
    locator: Section 'Questions for 2026'
  - ref: TR-AGENTICCORP-2025
    title: How agentic AI is transforming corporate tax departments
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/how-agentic-ai-is-transforming-corporate-tax-departments/
    date: '2025-11-11'
    access: full
    locator: 'Section ''Agentic AI: What is it, and why does it matter?'''
  - ref: AICPA-WERFELART-2026
    title: A risk framework for AI use in tax administration and preparation (Danny Werfel)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/
    date: '2026-08-31'
    access: full
    locator: 'Figure 3, Business: ''Lack of transparency'''
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Circular 230 section 10.22, due diligence
  last_reviewed: '2026-10-17'
  notes: Vendor and firm guidance; no deployment with a measurement. Included because a documented record of validation is a repeated practitioner prescription for return workpapers.
- id: tax-compliance-corporate-16
  title: Large-firm platform lets tax professionals and clients build their own agents in a managed environment
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - software-systems
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Building an agent to help clients adjust to changing tax rules 'used to take weeks and required teams to switch between multiple tools and chat windows', according to KPMG's US tax leader (KPMG-ANTHROPIC-2026).
  solution: KPMG embedded Claude Cowork and Managed Agents in its Digital Gateway client delivery platform (global alliance with Anthropic, initial focus on tax clients and private equity), so professionals and clients can build agentic workflows in real time (KPMG-ANTHROPIC-2026).
  outcomes:
  - lever: speed
    description: Time to build a client agent for changing tax rules
    figure: weeks to minutes
    measures: Stated by Rema Serafi, Vice Chair, Tax, KPMG US; the announcement does not say how many agents, which tasks or how measured
    provenance: self-reported
    source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
  - Platform access for professionals and clients
  - KPMG Trusted AI framework and security controls (KPMG-ANTHROPIC-2026)
  risks_and_guardrails:
  - The announcement says cybersecurity, risk and AI assurance will be embedded in design and operation; no results are published (KPMG-ANTHROPIC-2026).
  human_checkpoints:
  - Not described
  role_evolution: KPMG says its 276,000 people will have access to Claude; no role effects are published (KPMG-ANTHROPIC-2026).
  evidence_grade: C
  sources:
  - ref: KPMG-ANTHROPIC-2026
    title: KPMG Partners with Anthropic for Digital Gateway Powered by Claude
    publisher: CPA Practice Advisor (KPMG and Anthropic announcement)
    type: firm
    url: https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/
    date: '2026-05-20'
    access: full
    locator: Announcement text, paragraph on Digital Gateway and the Serafi quote
  last_reviewed: '2026-10-17'
  notes: Announcement of a launch ('announced'), not evidence of use on compliance work. The tax use is described in terms of agents for changing rules; no corporate compliance return process is specified.
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Data collection and tax sensitising of ledger data** (trial balance, book-to-tax, M-1/M-3-type adjustments, entity and K-1 data from many systems): `transaction-processing`, `data-reporting`. Pain: Excel manipulation, multiple loads, fragmented ERPs (KOGNITOS-2026; TRINST-TEIAUDITOR-2026).
- **Return preparation** (consolidated 1120, 1065 inputs, 5471/8858, state returns and apportionment): `transaction-processing`, `document-production`. Named in-house automation: OpenAI's listing for 1120, 1065, 5471 and state (OPENAI-TAXCOMPLIANCEJOB-2025).
- **Workpaper and review** (preparer to reviewer; provision-to-return reconciliation): `review-assurance`. OpenAI describes first-level review of automated outputs (OPENAI-USTAXOPSJOB-2026).
- **Credits and incentives** (R&D credit, Form 6765 Section G): `data-reporting`, `expert-judgment`, `document-production` (IRS-F6765INSTR-2025; NEOTAX-TR-2025).
- **Estimated payments, extensions and the compliance calendar:** `coordination-scheduling`. The OpenAI listing lists these as part of the compliance cycle (OPENAI-TAXCOMPLIANCEJOB-2025); Bloomberg Tax lists a Compliance Tracker assistant (BTAX-TOOLS-2026). No AI-specific practitioner discussion of estimated payments was found.
- **Notices and tax-authority correspondence:** `transaction-processing`, `document-production` (EY-BTAX-2025; TEI-MIDYEAR-2026).
- **Regulatory-change tracking:** `research-synthesis` (TR-CORPAI-2026; CORPTAX-2026).

### Common pain points

- Capacity: 58% of surveyed corporate tax departments say they are under-resourced, up from 51% a year earlier, and respondents report spending more than half their time on reactive work, mostly compliance (TR-CORPTAX-2025).
- Data: Kognitos argues the binding constraint after Pillar Two is collecting and reconciling data, not the calculation (a vendor view, KOGNITOS-2026).
- Documentation standard: Section G now asks for business-component detail the IRS used to request only on examination (CBH-6765POD-2026; IRS-F6765INSTR-2025).
- Change fatigue and training: panelists at a TEI seminar described transformation fatigue from stacking new tools (TR-TRANSFATIGUE-2025); a transformation director described a failed training rollout (TEI-TAXTECH-2026).
- Unexplainable automation: Alteryx workflows nobody could explain after the builder left (TEI-TAXTECH-2026).

### Metrics and benchmarks (what each figure counts)

| Figure | What it measures, in the source's words | Source | Provenance / caveat |
|---|---|---|---|
| 67% | corporate tax departments 'not using GenAI'; 57% of those implementing new technologies say plans include GenAI; 17% plan to explore agentic AI | TR-CORPTAX-2025 (2025 State of the Corporate Tax Department report, 288 departments worldwide) | Vendor-owned survey |
| 58% (51% prior year) | survey respondents saying their departments are under-resourced | TR-CORPTAX-2025 | Vendor-owned survey |
| 31% vs 56% | respondents spending more than half their time proactively vs reactively, who say their department incurred penalties | TR-CORPTAX-2025 | Correlation in a vendor survey; no causal claim in the source |
| 34% (from 56%) | satisfaction with tax technology | TR-TAXTALENT-2026 (2026 Corporate Tax Technology Report, with TEI; 170 tax leaders per TR-CORPTECH-2026) | Vendor/TEI survey |
| 50% (from 59%) | departments providing technology training in 2025 | TR-TAXTALENT-2026 | as above |
| 39% (from 31%) | professionals expecting AI to be central to their workflow within 1 to 2 years; another 15% expect it within a year | TR-TAXTALENT-2026 | as above |
| 62% | 2025 new hires emphasising tax expertise over technology skills (57% of 2024 new roles were tech/IT) | TR-TAXTALENT-2026 | as above |
| 67% | respondents saying technology investment enabled a shift to more proactive tax work | TR-CORPTECH-2026 | Vendor/TEI survey |
| 5% | corporate tax professionals saying their organisation was integrating GenAI (April 2024 baseline) | TR-GENAICORP-2024 | Older baseline; do not compare with later samples |
| 57% chaotic/reactive; 6% optimized/predictive | technology maturity self-rating in the 2025 report | TR-DUALROLES-2025 | Older baseline |
| 71% using; 19% preparing; 66% of users report noticeable time savings | German tax departments using AI tools; share of AI users | KPMG-DE-2026 (sample size not stated) | Big Four press release; German market |
| 58% domestic and 72% abroad | companies expecting constant tax-department headcount | KPMG-DE-2026 | as above |
| 2 of more than 50 | hands raised when asked whether the tax function owns AI implementation at their company | TEI-TAXTECH-2026 | A show of hands at one seminar |
| 65% | AICPA tax software survey respondents (1,808 members who prepared 2025 returns for a fee) using AI in tax research; 16% had no plans (24.3% in 2025) | AICPA-TAXSW-2026 | Public accounting, not in-house; adjacent |
| 91%; 41% | tax professionals believing AI outputs should be more accurate than human work; those who will not use AI without human review unless 100% accurate | TR-AGENTICCORP-2025 (citing the 2025 Future of Professionals Report) | Secondary vendor citation; base not stated |
| fewer than one third | simplified federal personal returns computed correctly by frontier models | COLUMN-TAXCALCBENCH-2025 | Independent benchmark but personal returns; adjacent |
| nearly 800 | AI-related citation errors across at least 25 countries by late 2025, per a January 2026 paper in The International Tax Journal | BTAX-HALLUC-2026 | Secondary citation by a vendor; paper not opened |
| up to 150+ hours; 50-75%; 20-30% | see use case 05 | NEOTAX-TR-2025 | Vendor-published, unnamed customers |

### Guardrails and regulatory points

- **IRS OPR Alert 2026-19 (24 June 2026):** practitioners must review all AI-created content before it reaches a client or the IRS (section 10.22 due diligence); AI-driven time savings and billing may bear on the fee rule in 10.27(a); competence (10.35) includes understanding how the tool works and its limits; firms need procedures (10.36) (IRS-OPR-2026).
- **AICPA reaction:** the AICPA is seeking clarification of the fee language and says the OPR statement is not authoritative (AICPA-FEE-2026).
- **Werfel preparer risk register (15 risks, five layers):** includes incorrect document extraction from K-1s and similar forms, control dilution, liability ambiguity and lack of transparency; Werfel recommends limited-scope pilots before scaling (AICPA-WERFELART-2026). The authority-side register has the same control-dilution risk (AICPA-WERFEL-2026). The AICPA's Council on AI Risk in Tax (September 2026) will test and refine the framework (AICPA-CART-2026).
- **Courts:** the Tax Court noted fabricated citations in a brief in Clinco but stopped short of formal sanctions (TAXCT-CLINCO-2026).
- **Form 6765:** for tax years beginning before 2026 Section G is optional; after 2025 it is required subject to IRS guidelines; reporting covers at least 80% of QREs or up to 50 business components (IRS-F6765INSTR-2025).
- **Confidentiality:** Wolters Kluwer advises keeping sensitive details out of tools without enterprise-grade privacy controls (WK-CORPRES-2026).

### Frontier signals (dated)

- 2025-06-05: OpenAI lists a role to help build 'the world's first fully autonomous corporate tax reporting system' and move return computation in-house (OPENAI-TAXCOMPLIANCEJOB-2025). 2026-04-11: a later listing describes database-driven workflows where preparation is 'increasingly automated' and the manager reviews and validates (OPENAI-USTAXOPSJOB-2026).
- 2025-11-21: EY practitioners say agents can 'monitor rule changes, propose adjustments to tax provisioning, route exceptions for review, and even draft responses to audit queries' (EY-BTAX-2025).
- 2026-03 to 2026-05: TEI moves AI from a topic to hands-on Tax Labs (research credit automation, notices, Excel analysis) and its Tax Technology Seminar sells out with OpenAI, Google and Microsoft demonstrating agents (TEI-MIDYEAR-2026; TEI-TAXTECH-2026).
- 2026-05-12: more than 60 jurisdictions are described as moving to continuous transaction controls, with authorities compressing multinationals' roadmaps to 12 and 18 months (TRINST-TEIAUDITOR-2026).
- 2026-05-20: KPMG and Anthropic announce an alliance with tax clients as the initial focus (KPMG-ANTHROPIC-2026).
- 2026-07: Deloitte frames four scenarios crossing a company's AI adoption with its tax authority's, and describes low company adoption against a high-adoption authority as bringing heightened audit and dispute exposure and a forced, high-pressure transformation (DELOITTE-TTT-2026).
- 2026-09: Werfel's framework and the AICPA council signal an emerging governance reference for tax AI; the framework is described as a starting point to be tested and refined (AICPA-CART-2026; AICPA-WERFELART-2026).

### Workforce and role effects

- Review replaces preparation: OpenAI's listings describe moving from preparing returns to review, validation and building data models (OPENAI-USTAXOPSJOB-2026); PwC describes one reviewer replacing a group huddle on novel items (PWC-MEGNA-2025).
- Hiring: after tilting to technology hires in 2024, 62% of 2025 new tax hires emphasised tax expertise, and hybrid tax/tech roles are rising (TR-TAXTALENT-2026). Corporate tax departments often rely on dual tax/technology roles (TR-DUALROLES-2025).
- Headcount: German respondents mostly expect stable headcount (KPMG-DE-2026); Sala argues AI will not shrink corporate tax teams much because the work is tax practice, not preparation (SALA-TAXNOTES-2026).
- Skills: EY authors see a divide between experienced staff who can spot AI problems and newer staff who may over-rely (EY-BTAX-2025).
- Junior work: a vendor claims junior staff can handle research that previously needed senior review (TR-AGENTICCORP-2025); no independent evidence was found.

### Objections and concerns practitioners raise

- Quiet failure: AI that 'fails quietly and even politely' (TEI-TAXTECH-2026).
- Nobody owns it: 2 of more than 50 polled say tax owns AI implementation (TEI-TAXTECH-2026).
- Unreviewed vibe-coded pipelines and security (TRINST-TEIAUDITOR-2026).
- Cost: rising token costs that could change the economic case for automation (TEI-TAXTECH-2026).
- Culpability: AI cannot shoulder regulatory, ethical or financial consequences (SALA-TAXNOTES-2026).
- Unfair fee rule: the AICPA says the OPR language ignores software, implementation, governance and training costs (AICPA-FEE-2026).
- R&D credit defensibility: a competing adviser argues software-only tools cannot produce a defensible claim, and that vendor liability is typically capped at fees (STRIKE-6765-2026; competitor view).
- Surrender: one panelist described companies padding numbers and treating audit as the cheaper cost, which others rejected (TRINST-TEIAUDITOR-2026).
- Transformation fatigue (TR-TRANSFATIGUE-2025).

### Interview probes for an advisor

1. Walk through your last compliance cycle: which inputs still arrive as K-1s, state notices or spreadsheets in formats you do not control, and who keys or maps them today?
2. Who owns AI in the tax function, and what can a reviewer see on an AI-assisted workpaper (prompt, output, sources, what was verified)?
3. For Form 6765 Section G, what do you hold today at business-component level, where does it live, and who signs off the four-part test?
4. Where has a tool failed quietly in the last year, and what did you change in review as a result? Has anyone measured time saved, error or override rates before and after?
5. How do you expect the tax authorities you deal with to change audit timing and data requests, and what would you need upstream in your data to answer faster?

---

## 4. Routed to other modules

- **indirect-tax / tax-data-technology:** continuous transaction controls, clearance regimes and authority-side real-time audits (TRINST-TEIAUDITOR-2026); agentic indirect-tax workflows (TR-READYEXP-2026).
- **international-pillar-two (with provision):** Orbitax XatBot modes for the GloBE Information Return (TR-CORPAI-2026); data as the binding constraint after Pillar Two (KOGNITOS-2026); Neo.Tax live R&D credit data feeding the provision (TR-CORPAI-2026); PwC's effective-tax-rate model is provision-adjacent (PWC-MEGNA-2025).
- **research-advisory:** CoCounsel Tax inside ONESOURCE and corporate tax research guidance (TR-CORPAI-2026; WK-CORPRES-2026; TR-AGENTICCORP-2025); Sala's question whether tax AI could displace Big Four opinions (SALA-TAXNOTES-2026); hallucination and sanctions (BTAX-HALLUC-2026; TAXCT-CLINCO-2026).
- **compliance (individual, partnership and small-business lens):** preparer-side agentic return products and solo-practice workpaper automation; The Accounting Podcast episode on Claude-built workpapers and the 'reviewer bottleneck' (ACCTPOD-SAMLEON-2026; show notes only), the Basis partnership-return episode (ACCTPOD-477-2026) and the AICPA tax software survey (AICPA-TAXSW-2026).
- **controversy:** tax-authority AI, OPR guidance and Clinco (IRS-OPR-2026; TAXCT-CLINCO-2026; DELOITTE-TTT-2026 scenarios).
- **Older baseline kept for trend context only:** BGOV-TALKINGTAX-2024 (October 2024 podcast with in-house leaders from Amazon, Edward Jones and Sabre, who differ on how far to use AI).

---

## 5. Sources

Counts by source type (distinct sources listed below; all opened unless the locator says abstract or show notes only):

| Type | Distinct sources |
|---|---|
| conference | 3 |
| regulator | 2 |
| standard-setter | 0 |
| professional-body | 3 |
| firm | 4 |
| vendor | 11 |
| academic | 2 |
| survey | 7 |
| press | 4 |
| podcast | 4 |
| community | 0 |
| job-posting | 3 |
| **Total** | **43** |

No source of type `standard-setter` or `community` was reached. Access is `full` for all sources (opened and read); none is search-only.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ACCTPOD-477-2026 | The AI Agent That Can Do A Partnership Tax Return (episode 477, show notes) | The Accounting Podcast (via CastFox) | podcast | https://www.castfox.net/podcast/the-accounting-podcast-930492/episode/the-ai-agent-that-can-do-a-partnership-tax-return-140333 | 2026-03-03 | full |
| ACCTPOD-SAMLEON-2026 | How Sam Leon Uses Claude Cowork to Prep Tax Returns 5x Faster (episode listing and show notes) | The Accounting Podcast (via Podscan) | podcast | https://podscan.fm/e/ep_naq7xl2ng2awrm6e | 2026-07-25 | full |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax (Council on AI Risk in Tax) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| AICPA-FEE-2026 | AICPA seeks IRS clarity on AI guidelines, CPA fees | The Tax Adviser (AICPA) | press | https://www.thetaxadviser.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/ | 2026-09-08 | full |
| AICPA-TAXSW-2026 | 2026 tax software survey (1,808 AICPA members who prepared 2025 returns for a fee) | The Tax Adviser (AICPA) | survey | https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/ | 2026-08-31 | full |
| AICPA-WERFEL-2026 | A Risk Framework for the Use of AI in Tax Administration and Preparation: appendices (AI risk register for tax authorities) | The Tax Adviser (AICPA), Danny Werfel | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 | full |
| AICPA-WERFELART-2026 | A risk framework for AI use in tax administration and preparation (Danny Werfel) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ | 2026-08-31 | full |
| BGOV-TALKINGTAX-2024 | Corporate Tax Leaders Weigh AI's Risk-Reward Calculus (Talking Tax podcast, episode page) | Bloomberg Tax / Bloomberg Government | podcast | https://news.bgov.com/in-house-counsel/corporate-tax-leaders-weigh-ais-risk-reward-calculus-podcast | 2024-10-24 | full |
| BTAX-FORUM-2026 | Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk (programme release for the 16 Jun 2026 forum) | Bloomberg Tax | conference | https://pro.bloombergtax.com/?p=17345 | 2026-06-10 | full |
| BTAX-HALLUC-2026 | AI Hallucinations in Tax: The Risks and How to Mitigate Them | Bloomberg Tax | vendor | https://pro.bloombergtax.com/?p=16920 | 2026-05-11 | full |
| BTAX-TOOLS-2026 | Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026 | Bloomberg Tax | vendor | https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026 | 2026-03-09 | full |
| CBH-6765POD-2026 | Life Sciences R&D Tax Credits: Form 6765 Changes, New Reporting Requirements and Compliance Strategies (Healthcare & Life Sciences Podcast, with transcript) | Cherry Bekaert | podcast | https://www.cbh.com/insights/podcasts/life-sciences-rd-tax-credits-form-6765-changes/ | 2026-10-09 | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126) | Column Tax authors (Bock, Molisee, Ozer, Shah) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full |
| CORPTAX-2026 | Webinar: Unlock the Power of Tax AI (AI and ML in Tax: Applications, Considerations, and Responsible Engagement), with ACT | CSC Corptax | vendor | https://go.corptax.com/act-ai-ml-tax | 2026 | full |
| DELOITTE-TTT-2026 | Riding the wave: A framework to plan for AI (AI-enabled Tax Transformation, Tax Transformation Trends AI report, part three) | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 | full |
| EY-BTAX-2025 | AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way (opinion by D. Campbell and R. Carpenter, EY) | Bloomberg Tax | firm | https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way | 2025-11-21 | full |
| IRS-F6765INSTR-2025 | Instructions for Form 6765 (12/2025), Credit for Increasing Research Activities | Internal Revenue Service | regulator | https://www.irs.gov/instructions/i6765 | 2025-12 | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| KOGNITOS-2026 | AI for Corporate Tax and Provision Automation (2026) | Kognitos | vendor | https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/ | 2026-06-17 | full |
| KPMG-ANTHROPIC-2026 | KPMG Partners with Anthropic for Digital Gateway Powered by Claude | CPA Practice Advisor (KPMG and Anthropic announcement) | firm | https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/ | 2026-05-20 | full |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence (KPMG quick surveys) | KPMG AG Wirtschaftsprufungsgesellschaft (Germany) | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-07 | full |
| NEOTAX-TR-2025 | How to eliminate the burden of R&D tax credit compliance (ONESOURCE + Neo.Tax) | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/neo-tax-onesource-eliminating-the-triple-burden-of-rd-credit-compliance/ | 2025-09-08 | full |
| OPENAI-TAXCOMPLIANCEJOB-2025 | Manager, Tax Compliance and Automation (OpenAI job listing) | Omega Venture Partners job board (OpenAI) | job-posting | https://jobs.omegavp.com/companies/openai/jobs/52055389-manager-tax-compliance-and-automation | 2025-06-05 | full |
| OPENAI-TAXDATAJOB-2025 | Senior Manager, Tax Data Automation (OpenAI job listing) | Khosla Ventures job board (OpenAI) | job-posting | https://jobs.khoslaventures.com/companies/openai/jobs/45083210-senior-manager-tax-data-automation | 2025-01-22 | full |
| OPENAI-USTAXOPSJOB-2026 | Manager, US Tax Operations (OpenAI job listing) | Glynn Capital job board (OpenAI) | job-posting | https://jobs.glynncapital.com/companies/openai/jobs/74040402-manager-us-tax-operations | 2026-04-11 | full |
| PWC-MEGNA-2025 | How PwC's tax team is using agentic AI (interview with Dom Megna, PwC US AI Tax Leader) | CFO.com | firm | https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/ | 2025-06-06 | full |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Tax Notes State 121:189; abstract on TaxProf Blog) | Michael V. Sala, Tax Notes; TaxProf Blog | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 | full |
| SAVANT-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Technology Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| STRIKE-6765-2026 | Form 6765 Section G Becomes Mandatory in 2026. Most AI-Only R&D Credit Tools Will Not Be Ready. | Strike Tax Advisory (R&D credit adviser; competes with software-only providers) | vendor | https://www.striketax.com/journal/form-6765-section-g-becomes-mandatory-in-2026-most-ai-only-r-d-credit-tools-will-not-be-ready | 2026-05-28 | full |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax (Clinco v. Commissioner, T.C. Memo. 2026-16) | Journal of Accountancy (AICPA) | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| TEI-MIDYEAR-2026 | TEI's 2026 Midyear Conference, Preliminary Program (At a Glance agenda) | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03 | full |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute (recap of TEI Tax Technology Seminar, Las Vegas) | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| TR-AGENTICCORP-2025 | How agentic AI is transforming corporate tax departments | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/how-agentic-ai-is-transforming-corporate-tax-departments/ | 2025-11-11 | full |
| TR-CORPAI-2026 | AI in corporate tax: 2026 key trends and use cases | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/ | 2026-07-01 | full |
| TR-CORPTAX-2025 | The GenAI paradox: why most tax departments aren't using AI yet (reporting the 2025 State of the Corporate Tax Department report) | Thomson Reuters Tax & Accounting | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 | full |
| TR-CORPTECH-2026 | Corporate tax teams eager for AI, but frustrated by pace of change, new report shows (2026 Corporate Tax Department Technology Report, with TEI) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026 | 2026-03-16 | full |
| TR-DUALROLES-2025 | Corporate tax departments are hiring dual tax/technology roles, and more are on the way (2025 Corporate Tax Technology Report) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/corporate-tax-dual-technology-roles | 2025-02-26 | full |
| TR-GENAICORP-2024 | GenAI has begun to make inroads into corporate tax, but more training is needed (2024 Generative AI in Professional Services report) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/genai-corporate-tax | 2024-04-24 | full |
| TR-READYEXP-2026 | Is your tax department ready for the agentic AI explosion? (indirect tax) | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/is-your-tax-department-ready-for-the-agentic-ai-explosion/ | 2026-06-08 | full |
| TR-TAXTALENT-2026 | Why corporate tax tech is falling short and how talent development can fix it (2026 Corporate Tax Technology Report) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/tax-tech-talent-development | 2026-05-01 | full |
| TR-TRANSFATIGUE-2025 | The human in the loop: Tackling transformation fatigue in the tax tech era (panel at a TEI tax technology seminar) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/transformation-fatigue-tax-tech | 2025-06-03 | full |
| TRINST-TEIAUDITOR-2026 | 2026 TEI Tax Technology Seminar: What the auditor already knows | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows | 2026-05-12 | full |
| WK-CORPRES-2026 | How controllers and corporate tax leaders can use AI for faster, defensible tax returns (corporate tax research guide) | Wolters Kluwer Tax & Accounting | vendor | https://www.wolterskluwer.com/en/expert-insights/how-controllers-and-corporate-tax-leaders-can-use-ai-for-faster-defensible-tax-returns | 2026-04-02 | full |

Date notes: DELOITTE-TTT-2026 is month-level from the PDF's creation date (the document shows a 2026 copyright). CORPTAX-2026 is year-level because the page carries only a 2026 copyright. AICPA-WERFEL-2026 is month-level from the publisher's upload path (the PDF metadata shows 14 May 2026). AICPA-WERFELART-2026 shows an online date of 31 August 2026, while the AICPA CART release of 23 September says the framework was published 'earlier this month', so the date of first release is unresolved.

---

## 6. Gaps

- **Quality evidence is absent.** No error rates, override rates, parallel-run results, review-time measurements or inspection findings exist in public sources for AI on corporate returns. Vendor figures (Neo.Tax, Savant, KPMG, PwC) are self-reported or vendor-published with no sample or method.
- **Search budget.** Fifteen searches were used; the final two were refused because the shared budget ran out. Not searched: state apportionment and SALT AI practice, estimated payments, 5471/8858 AI use by named companies, Tax Notes Talk 2026 episodes, JofA 'Excel agent' article, Bloomberg Tax March 2026 pricing story, EY and Deloitte survey full text.
- **Blocked or unavailable.** Reddit r/taxpros (403, including via a mirror), Going Concern (403), Greenberg Traurig (Cloudflare block), the COST 2026 technology workshop agenda (URL from a search result returned 404; it reportedly includes an agent-building session and a 'Mail Intake and Triage' demo, seen only in a search summary, so not used), OpenAI's careers page (403; listings read through investor job boards), the Thomson Reuters Institute 'governance reckoning' article (not found), the Sala article body (paywalled; abstract only), the Bloomberg 2026 AI guide (gated).
- **Community voice is missing.** No practitioner forum thread was reached; practitioner opinion here comes from conference recaps, trade press and podcasts.
- **No named in-house case study with outcomes.** Oxford Industries (Savant release) and OpenAI (job listings, seminar demonstration) are the only named in-house teams; Amazon, Walmart, Home Depot and Procter & Gamble appear only as attendees or panelists in other sources, with no AI practice described.
- **Unconfirmed items from the landscape.** The landscape's 'OpenAI tax department (four people)' is corrected here: the recap says OpenAI sent four members of its tax department to the seminar. A Salesforce-linked 5471/8858 job listing surfaced in search but was not opened and is not used. The TEI Annual Conference (Nashville, starting 18 October 2026) had no AI session titles at fetch time; re-check after it ends.
- **Dates and effective dates.** The IRS Form 6765 instructions page is dated 12/2025, while two practitioner sources report final instructions in early February 2026; the release date was not confirmed from an IRS notice.
