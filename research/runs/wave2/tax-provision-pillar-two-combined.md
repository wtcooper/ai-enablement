# Provision and Pillar Two: combined deep dive (practice, discourse, governance and evidence)

Archetype: tax. Module: provision-pillar-two (income tax accounting under ASC 740 and IAS 12, ASU 2023-09 disclosures, and the global minimum tax: GloBE calculations, safe harbours, the GloBE Information Return (GIR) and its XML filing, QDMTTs, and the data pipeline and audit overlap). Angle: combined. Prepared 2026-10-17 (wave 2). Working folder was a private temporary directory.

## 1. Summary

- **16 candidate use cases: grade A 2, B 3, C 8, D 3.** Both A entries (08 and 16) rest on one vendor-published case study of a named customer, AMG Critical Materials [ORBITAX-AMG-2026], and describe software automation, not AI. The three B entries are Pillar Two computation (10), GIR XML and filing (11) and firm-run platforms (14); they describe rules-based tooling. The three D entries are labelled ideas.
- **49 sources opened and read** (18 vendor, 10 firm, 5 conference, 4 academic, 2 each of survey, regulator, press, professional-body and job-posting, 1 each of standard-setter and podcast). None is search-only. The four academic items include three arXiv abstracts on adjacent personal-income-tax work; only the abstracts were read.
- **Practice.** The public record is strongest for the Pillar Two data and filing pipeline in the first GIR season (due 30 June 2026) and weakest for AI in the provision itself. For provision I found product pages, one roadmap, one product-team job posting and vendor blogs, but no named customer, no outcome figure and no error, override or parallel-run result. The only generative AI built into a Pillar Two engine that I found is Orbitax's XatBot, whose customer examples are unnamed [ORBITAX-XATBOTPRO-2026, ORBITAX-LEAN-2026].
- **Discourse.** Practitioner talk is thin and mostly known from titles: TEI Midyear 2026 held a "Pillar Two and Technology" lab, a hands-on Excel-and-AI lab and a "Tax GPT" closing plenary [TEI-MIDYEAR-2026]; Bloomberg Tax's June 2026 forum listed an AI-in-provisioning panel but I found only the pre-event notice [BTAX-FORUM-2026]; a June 2026 podcast covered Pillar Two and AI (show notes only) [ACAST-TAXTECH-2026]. No session, article or community thread specific to AI in the ASC 740 provision was found.
- **Governance and evidence.** I found no regulator, standard-setter or audit-firm publication specific to AI in the provision or to auditing AI-prepared tax balances. The nearest items are the PCAOB staff's July 2024 outreach spotlight on generative AI [PCAOB-GENAI-2024], the AICPA's September 2026 Council on AI Risk in Tax, whose framework is aimed at tax preparation and administration [AICPA-CART-2026], and the OECD's own corrections to the GIR XML rules [OECDPILLARS-GIRXML-2026]. There is no independent measurement of accuracy for any use case here.
- **Two most important insights.** (1) In Pillar Two the binding constraint in the first season was data and XML plumbing, not tax law or AI: KPMG International authors report that in some jurisdictions only 20% of GIRs were filed successfully before the initial deadline [BTAX-KPMG-GIR-2026], and FGS says country-specific XML variants and faulty business rules were the main hurdle [FGS-GIR-2026]. (2) Almost all "AI in provision" evidence is vendor roadmap or marketing, while the unanswered governance question is how auditors will rely on AI-assisted provisions; nobody has published an answer.

## 2. Use cases

```yaml
- id: tax-provision-pillar-two-01
  title: Cited research and AI insights embedded in the provision and direct-tax workflow
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: After the books close, the provision team has little time and moves between spreadsheets and research
    tools to check rates, rules and positions such as uncertain tax positions [BTAX-ASC740-2026].
  solution: Vendors place an AI assistant where the provision work happens. Bloomberg Tax describes AI-powered insights
    and current rates inside its Workpapers spreadsheets [BTAX-ASC740-2026]. Thomson Reuters says CoCounsel Tax
    was embedded in ONESOURCE direct tax solutions in late 2024 and can research uncertain tax positions and R&D
    credit qualification, with links to primary sources [TR-CORPAI-2026, TR-AGENTICCORP-2025]. Neither source names
    a customer.
  outcomes:
  - lever: speed
    description: Thomson Reuters says research that used to take hours now takes minutes.
    figure: hours to minutes
    measures: General statement about research tasks; no sample, baseline or method is stated.
    provenance: vendor-published
    source_ref: TR-AGENTICCORP-2025
  prerequisites:
  - Provision workpapers and calculations held in the same vendor suite as the assistant, with Workpapers outputs
    pushed to Provision [BTAX-ASC740-2026].
  - Access to the vendor's research content (Checkpoint for CoCounsel Tax) [TR-AGENTICCORP-2025].
  risks_and_guardrails:
  - TR reports from its Future of Professionals 2025 report that 91% of tax professionals believe AI outputs should
    be more accurate than human work and 41% will not use AI without human review unless it is 100% accurate [TR-AGENTICCORP-2025].
  - Bloomberg Tax (selling its own tools) warns that a single reasoning error can cascade through provision calculations,
    ETR analysis and disclosures, and that generic tools can invent citations [BTAX-HALLUC-2026].
  human_checkpoints:
  - The preparer reads the linked primary sources before relying on an answer; TR says each response links to them
    and shows the reasoning chain [TR-AGENTICCORP-2025].
  role_evolution: TR says junior staff can handle research that previously needed senior review [TR-AGENTICCORP-2025],
    a vendor claim. Sala argues the corporate tax function does tax practice (engagement with authorities, auditors
    and executives), not only preparation, so AI will shrink teams less than predicted [SALA-TAXNOTES-2026].
  evidence_grade: C
  sources:
  - ref: BTAX-ASC740-2026
    title: Accelerate your ASC 740 process (Bloomberg Tax Research, Provision and Workpapers product page)
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/products/accelerate-your-asc-740-process/
    date: '2026-03-25'
    access: full
    locator: Section 'Get research answers directly in your spreadsheets'
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: 'Section ''Thomson Reuters: From compliance to intelligent compliance'', paragraph 2'
  - ref: TR-AGENTICCORP-2025
    title: How agentic AI is transforming corporate tax departments
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/how-agentic-ai-is-transforming-corporate-tax-departments/
    date: '2025-11-11'
    access: full
    locator: 'Sections ''Agentic AI: What is it, and why does it matter?'' and the CoCounsel Tax paragraphs'
  - ref: BTAX-HALLUC-2026
    title: 'AI Hallucinations in Tax: The Risks and How to Mitigate Them'
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/artificial-intelligence/ai-hallucinations-in-tax-the-risks-and-how-to-mitigate-them/
    date: '2026-05-11'
    access: full
    locator: Section 'Why does generative AI hallucinate?', third reason
  - ref: SALA-TAXNOTES-2026
    title: AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Tax Notes State 121:189; abstract on TaxProf Blog)
    publisher: Michael V. Sala / Tax Analysts (via TaxProf Blog)
    type: academic
    url: https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/
    date: '2026-07-20'
    access: full
    locator: Abstract, paragraph 2
  last_reviewed: '2026-10-17'
  notes: Generic tax research with AI belongs to the research-advisory module; this entry covers only the embedding
    inside provision and direct-tax tools. No customer, error rate or override rate is published.
- id: tax-provision-pillar-two-02
  title: Provision data assembly and the close-to-tax handoff
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: The provision runs on financial data from the close. Kognitos (a vendor) calls the handoff from close
    to tax an often manual, error-prone junction and says tax accuracy is decided in the source data, not the calculation
    [KOGNITOS-2026]. Its figure that 58% of tax departments are under-resourced comes from the TR 2025 survey [TR-CORPTAX-2025].
  solution: Bloomberg Tax describes automated data cleansing, rollforwards and book-to-tax adjustments in Workpapers
    that push into Provision [BTAX-ASC740-2026]. Thomson Reuters says its aim is agentic AI that handles data import,
    validation and mapping while tax professionals keep oversight [TR-CORPAI-2026]. Kognitos positions an agentic
    layer upstream of the tax engines that pulls and reconciles ledger data with every step logged, and says it
    does not calculate the provision [KOGNITOS-2026].
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: KOGNITOS-2026
  prerequisites:
  - Consistent chart-of-accounts mapping, clean entity hierarchies and documented lineage from ledger to provision
    input; this is Finrep's advice, not a measured requirement [FINREP-ASC740-2026].
  - Financial data that is final from the close [KOGNITOS-2026].
  risks_and_guardrails:
  - Finrep says AI inherits every error in the source data, and that teams that skip data cleanup can get a longer
    review list rather than a shorter one [FINREP-ASC740-2026].
  - Kognitos says its steps are logged so the data preparation is auditable, because the provision feeds audited
    statements [KOGNITOS-2026].
  human_checkpoints:
  - Tax staff review the exceptions the data layer raises before data reaches the provision engine [KOGNITOS-2026].
  - Direct tax professionals keep oversight of import, validation and mapping [TR-CORPAI-2026].
  role_evolution: TR and Kognitos both say the time returned goes to forecasting, modelling and advisory work [TR-CORPAI-2026,
    KOGNITOS-2026]; these are vendor statements with no measured change in roles.
  evidence_grade: C
  sources:
  - ref: BTAX-ASC740-2026
    title: Accelerate your ASC 740 process (Bloomberg Tax Research, Provision and Workpapers product page)
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/products/accelerate-your-asc-740-process/
    date: '2026-03-25'
    access: full
    locator: Sections 'Automate book-to-tax adjustments' and 'Clean, map, and export your data with ease'
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: 'Section ''Thomson Reuters: From compliance to intelligent compliance'', paragraph 1'
  - ref: KOGNITOS-2026
    title: AI for Corporate Tax and Provision Automation (2026)
    publisher: Kognitos
    type: vendor
    url: https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/
    date: '2026-06-17'
    access: full
    locator: 'Sections ''The split: tax engines vs the data layer'' and FAQ ''How does AI help with the close-to-tax
      handoff?'''
  - ref: FINREP-ASC740-2026
    title: 'AI Tax Provision ASC 740 Reporting: A 2026 Practitioner Walkthrough'
    publisher: Finrep (Gana Misra, CEO)
    type: vendor
    url: https://www.finrep.ai/blog/ai-tax-provision-asc-740-reporting-a-2026-practitioner-walkthrough
    date: '2026-09-30'
    access: full
    locator: 'Section ''Step 1: Book-to-Tax Difference Identification'''
  - ref: TR-CORPTAX-2025
    title: Why most tax departments aren't using AI yet (reporting the 2025 State of the Corporate Tax Department
      report)
    publisher: Thomson Reuters Tax & Accounting / Thomson Reuters Institute
    type: survey
    url: https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/
    date: '2025-10-22'
    access: full
    locator: Highlights, second bullet
  last_reviewed: '2026-10-17'
  notes: Much of this is rules-based automation rather than generative AI; the sources use 'AI' loosely. A search
    extract of a ChatFin guide claimed a provision cycle cut from 5-7 to 2-4 business days; that page was not opened
    and the figure is excluded.
- id: tax-provision-pillar-two-03
  title: Pre-close anomaly flagging and document comparison in provision review
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - review-assurance
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Reviewers must catch outliers in deferred tax balances, rate reconciliation lines and source documents
    before the provision is final. Finrep describes comparing current-period deferred tax balances with historical
    patterns and flagging outliers for human review before close [FINREP-ASC740-2026].
  solution: CSC Corptax lists PDF comparison to streamline document analysis on its AI/ML roadmap [CORPTAX-2026].
    Thomson Reuters advertised for a product specialist to develop, test and validate generative AI and intelligent
    automation for ONESOURCE Tax Provision, including document understanding, automated reconciliation, anomaly
    detection and AI-assisted review [TR-JOB-2026]. Both are development signals, not shipped features with named
    users.
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: TR-JOB-2026
  prerequisites:
  - Clean source data first; Finrep says anomaly detection otherwise flags noise with the signal [FINREP-ASC740-2026].
  risks_and_guardrails:
  - The TR posting asks for awareness of auditability, explainability and appropriate AI use in regulated accounting
    and tax settings [TR-JOB-2026].
  - Finrep says valuation allowance and uncertain tax position recognition remain human judgments that AI should
    not make [FINREP-ASC740-2026].
  human_checkpoints:
  - A reviewer clears each flagged item before sign-off [FINREP-ASC740-2026].
  role_evolution: 'Thomson Reuters wants practitioners with 5-7 years of provision experience to judge AI accuracy
    and fitness for high-stakes tax work [TR-JOB-2026]: experienced provision staff move into validating AI features.'
  evidence_grade: C
  sources:
  - ref: CORPTAX-2026
    title: 'AI and ML in Tax: Applications, Considerations, and Responsible Engagement (webinar page with Corptax
      AI/ML roadmap)'
    publisher: CSC Corptax with ACT
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: '2026'
    access: full
    locator: '''Corptax AI/ML roadmap'' bullet list'
  - ref: TR-JOB-2026
    title: Senior Tax Product Specialist, ONESOURCE Tax Provision (job posting, via Ann Arbor USA job board)
    publisher: Thomson Reuters
    type: job-posting
    url: https://jobs.annarborusa.org/companies/thomson-reuters/jobs/83860571-senior-tax-product-specialist
    date: '2026-06-24'
    access: full
    locator: Section 'Product Roadmap Delivery & AI', third bullet; 'AI & Technology Fluency'
  - ref: FINREP-ASC740-2026
    title: 'AI Tax Provision ASC 740 Reporting: A 2026 Practitioner Walkthrough'
    publisher: Finrep (Gana Misra, CEO)
    type: vendor
    url: https://www.finrep.ai/blog/ai-tax-provision-asc-740-reporting-a-2026-practitioner-walkthrough
    date: '2026-09-30'
    access: full
    locator: 'Section ''Step 3: Deferred Tax Assets and Liabilities'''
  last_reviewed: '2026-10-17'
  notes: Corptax's roadmap also lists audit prediction; that is routed to the controversy module. Finrep's table
    classes anomaly detection as machine learning, not generative AI.
- id: tax-provision-pillar-two-04
  title: ASU 2023-09 rate reconciliation and income-taxes-paid disclosure assembly
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  - document-production
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: ASU 2023-09 requires public business entities to give a tabular rate reconciliation in percentages and
    amounts by specific categories, with certain reconciling items at or above 5% of the statutory tax broken out
    by nature or jurisdiction, and income taxes paid split between federal, state/local and foreign [KPMG-ASU-2023].
    It applies to public business entities for annual periods in fiscal years beginning after 15 December 2024 and
    to other entities after 15 December 2025 [KPMG-ASU-2023]. Thomson Reuters lists it among the pressures on corporate
    tax departments [TR-AGENTICCORP-2025].
  solution: Finrep says AI-assisted categorization of reconciling items from ERP and tax-system data is the practical
    answer, and says Bloomberg Tax Provision and ONESOURCE have adapted rate reconciliation modules [FINREP-ASC740-2026].
    Neither vendor's own page was found to confirm this.
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: FINREP-ASC740-2026
  prerequisites:
  - Jurisdiction-level and category-level data for pre-tax income, tax expense and cash taxes paid, which Finrep
    says legacy Excel processes struggle to produce [FINREP-ASC740-2026].
  risks_and_guardrails:
  - Finrep says how reconciling items are classified and described for SEC comment-letter purposes stays a human
    judgment [FINREP-ASC740-2026].
  - Finrep says the SEC Division of Corporation Finance has a history of challenging rate-reconciliation explanations,
    so generic AI-categorised narratives carry comment-letter risk; this is the vendor's statement and was not checked
    against SEC letters [FINREP-ASC740-2026].
  human_checkpoints:
  - The tax director reviews and approves the categorisation and the narrative [FINREP-ASC740-2026].
  role_evolution: No source describes a change in roles for this step.
  evidence_grade: C
  sources:
  - ref: KPMG-ASU-2023
    title: FASB issues ASU to disaggregate income tax disclosures (Defining Issues)
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/frv/reference-library/2023/fasb-issues-asu-to-disaggregate-income-tax-disclosures.html
    date: 2023-12
    access: full
    locator: Sections 'Relevant dates' and 'Key Impacts'
  - ref: FINREP-ASC740-2026
    title: 'AI Tax Provision ASC 740 Reporting: A 2026 Practitioner Walkthrough'
    publisher: Finrep (Gana Misra, CEO)
    type: vendor
    url: https://www.finrep.ai/blog/ai-tax-provision-asc-740-reporting-a-2026-practitioner-walkthrough
    date: '2026-09-30'
    access: full
    locator: 'Section ''Step 6: Rate Reconciliation'''
  - ref: TR-AGENTICCORP-2025
    title: How agentic AI is transforming corporate tax departments
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/how-agentic-ai-is-transforming-corporate-tax-departments/
    date: '2025-11-11'
    access: full
    locator: Section 'Navigating the perfect storm in tax', paragraph 1
  last_reviewed: '2026-10-17'
  notes: The workload driver is well documented; the AI response is only a vendor's description. No public customer,
    accuracy or time figure was found.
- id: tax-provision-pillar-two-05
  title: Generative AI first draft of income tax footnote disclosures and rate-reconciliation narrative (idea)
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Tax disclosures must be company-specific and consistent with the provision; Finrep says generic AI language
    risks SEC comment letters [FINREP-ASC740-2026].
  solution: 'Idea: generative AI drafts disclosure language from provision data and prior-year disclosures, and
    a tax professional reviews and approves it. Finrep describes this workflow and says Big Four firms are piloting
    it, but gives no source for that attribution [FINREP-ASC740-2026]. The PCAOB''s outreach found preparers using
    GenAI for initial drafts of internal documents and for some account reconciliations, not specifically tax disclosures
    [PCAOB-GENAI-2024].'
  outcomes:
  - lever: speed
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: FINREP-ASC740-2026
  prerequisites:
  - Provision data and prior-year disclosures as inputs [FINREP-ASC740-2026].
  risks_and_guardrails:
  - Finrep says drafts may be accurate but generic, and miss company-specific judgments on valuation allowances
    or uncertain positions [FINREP-ASC740-2026].
  - PCAOB staff report that preparers raise the black-box nature of some GenAI tools and inconsistent output as
    audit-ability concerns [PCAOB-GENAI-2024].
  human_checkpoints:
  - A tax professional reviews, edits and approves every draft [FINREP-ASC740-2026].
  - PCAOB staff report that preparers stress human review of GenAI output [PCAOB-GENAI-2024].
  role_evolution: No source describes role change.
  evidence_grade: D
  sources:
  - ref: FINREP-ASC740-2026
    title: 'AI Tax Provision ASC 740 Reporting: A 2026 Practitioner Walkthrough'
    publisher: Finrep (Gana Misra, CEO)
    type: vendor
    url: https://www.finrep.ai/blog/ai-tax-provision-asc-740-reporting-a-2026-practitioner-walkthrough
    date: '2026-09-30'
    access: full
    locator: 'Section ''Step 7: Footnote Disclosure Drafting'''
  - ref: PCAOB-GENAI-2024
    title: 'Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence
      in Audits and Financial Reporting'
    publisher: PCAOB
    type: regulator
    url: https://pcaobus.org/documents/generative-ai-spotlight.pdf
    date: 2024-07
    access: full
    locator: Pages 5-6, 'Observations Related to GenAI Integration in Financial Reporting'
  last_reviewed: '2026-10-17'
  notes: Idea. The only tax-specific description is a vendor blog; its claim that Big Four firms are piloting this,
    and its 29% adoption figure attributed to an EY survey, could not be traced and are not used.
- id: tax-provision-pillar-two-06
  title: Law-change and guidance monitoring feeding the provision and Pillar Two compliance
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: 'Enacted-law changes drive deferred tax remeasurement and Pillar Two rules keep moving: the Side-by-Side
    package of 5 January 2026 and a second OECD package with a revised GIR on 11 September 2026 [OECD-SBS-2026,
    OECD-P2-SEP-2026]. Finrep notes that a rate change signed into law but not yet effective forces immediate remeasurement
    of deferred balances [FINREP-ASC740-2026].'
  solution: Orbitax says its Tax Flows mode tracks regulatory changes across jurisdictions and sends comparison
    reports to stakeholders [TR-CORPAI-2026, ORBITAX-XATBOT-2026]. CSC Corptax lists tax code version tracking on
    its roadmap [CORPTAX-2026]. KPMG US's tax vice chair says building an AI agent to help clients adjust to changing
    tax rules went from weeks to minutes on KPMG's Digital Gateway with Claude [KPMG-ANTHROPIC-2026].
  outcomes:
  - lever: speed
    description: KPMG says building an agent to help clients adjust to changing tax regulations now takes minutes
      rather than weeks.
    figure: weeks to minutes
    measures: Time to build an AI agent for adjusting to changing tax regulations, as stated by KPMG US's Vice Chair,
      Tax; no sample or baseline given.
    provenance: self-reported
    source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
  - For Orbitax Tax Flows, the platform's regulatory content across jurisdictions [ORBITAX-XATBOT-2026].
  risks_and_guardrails:
  - Orbitax adds a Verification tab that scores each key point High, Medium or Low against its database and live
    web sources [ORBITAX-XATBOT-2026]; this is a vendor control, not independently tested.
  - Bloomberg Tax notes that models trained on static data can give outdated tax guidance [BTAX-HALLUC-2026].
  human_checkpoints:
  - Stakeholders read the comparison reports and decide the accounting or compliance response [TR-CORPAI-2026].
  role_evolution: No source describes role change.
  evidence_grade: C
  sources:
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: 'Section ''Orbitax: International tax intelligence and the Pillar Two deadline'', ''Tax Flows'''
  - ref: ORBITAX-XATBOT-2026
    title: 'XatBot''s Latest Release: Autopilot, Deep Research, MCP Connections, and Intelligent Tax Skills'
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/announcements/xatbots-latest-release-autopilot-deep-research-mcp-connections-and-intelligent-tax-skills
    date: '2026-04-19'
    access: full
    locator: Introduction (three modes) and 'Verification Tab'
  - ref: CORPTAX-2026
    title: 'AI and ML in Tax: Applications, Considerations, and Responsible Engagement (webinar page with Corptax
      AI/ML roadmap)'
    publisher: CSC Corptax with ACT
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: '2026'
    access: full
    locator: '''Tax code version tracking'' roadmap bullet'
  - ref: KPMG-ANTHROPIC-2026
    title: KPMG Partners with Anthropic for Digital Gateway Powered by Claude
    publisher: CPA Practice Advisor (reproducing the KPMG and Anthropic announcement)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/
    date: '2026-05-20'
    access: full
    locator: Quote from Rema Serafi, Vice Chair, Tax at KPMG US
  - ref: OECD-SBS-2026
    title: Further details on the OECD Pillar Two 'Side-by-Side' package (KPMG UK Tax Matters Digest; the OECD package
      was released 5 January 2026)
    publisher: KPMG UK
    type: firm
    url: https://kpmg.com/uk/en/insights/tax/tmd-further-details-on-the-oecd-pillar-two-side-by-side-package.html
    date: '2026-01-22'
    access: full
    locator: Paragraphs 1 and 4
  - ref: OECD-P2-SEP-2026
    title: OECD Releases New Pillar Two Guidance, Updated GIR And Framework For Legislative Reviews (Loyens & Loeff;
      the OECD package was released 11 September 2026)
    publisher: Loyens & Loeff via Mondaq
    type: firm
    url: https://www.mondaq.com/oecd-releases-new-pillar-two-guidance-updated-gir-and-framework-for-legislative-reviews/1842556
    date: '2026-09-14'
    access: full
    locator: Section 'Updated GIR'
  last_reviewed: '2026-10-17'
  notes: KPMG's statement concerns building agents for clients in general, not provision or Pillar Two specifically.
- id: tax-provision-pillar-two-07
  title: Live R&D credit data feeding provision estimates
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: TR says R&D credit amounts in the provision can rest on estimates or prior-year placeholders rather than
    live data [TR-CORPAI-2026]. The revised IRS Form 6765 adds business-component reporting that TR says becomes
    mandatory for tax year 2026 returns [TR-CORPAI-2026].
  solution: Neo.Tax connects to project-management and engineering tools, groups the data into candidate business
    components, applies the four-part test, and reconciles payroll and ledger data to allocate costs. TR says that,
    because the data is live, the credit can be visible in real time and this can reduce return-to-provision adjustments
    [TR-CORPAI-2026].
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: TR-CORPAI-2026
  prerequisites:
  - Project-management and engineering tools where R&D work is recorded as it happens, plus payroll and ledger feeds
    [TR-CORPAI-2026].
  risks_and_guardrails:
  - The credit position rests on contemporaneous documentation that meets IRS expectations, per TR [TR-CORPAI-2026];
    a claimed benefit, not a tested one.
  human_checkpoints:
  - No source describes the review step.
  role_evolution: No source describes role change.
  evidence_grade: C
  sources:
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: 'Sections ''The regulatory crunch hitting direct tax right now'' and ''Neo.Tax: Automating R&D credits
      under the new IRS rules'', ''Real-time provision and prior-year audit support'''
  last_reviewed: '2026-10-17'
  notes: Primarily a compliance-corporate use case; included here only for the claimed provision link. Vendor description
    with no named customer.
- id: tax-provision-pillar-two-08
  title: Pillar Two data collection seeded from validated country-by-country reporting data
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Pillar Two data drives actual tax, unlike country-by-country reporting (CbCR), and needs more granular
    data than finance and CbCR processes held [ORBITAX-LEAN-2026]. TR says the first GIR required more than 100
    data points that many existing systems did not capture [TR-CORPAI-2026].
  solution: AMG Critical Materials uploaded its existing, validated CbCR XML into Orbitax's Pillar Two Compliance
    Accelerator as the starting point, then completed the extra Pillar Two information [ORBITAX-AMG-2026]. A Swiss-parented
    insurer likewise built on its CbCR templates and added data elements [ORBITAX-LEAN-2026]. The sources describe
    software automation; none claims AI for this step.
  outcomes:
  - lever: speed
    description: AMG says the Accelerator cut its implementation path to around 10 days.
    figure: around 10 days
    measures: Time for AMG to implement Pillar Two data collection after uploading its existing validated CbCR XML;
      no baseline stated.
    provenance: vendor-published
    source_ref: ORBITAX-AMG-2026
  prerequisites:
  - An existing validated CbCR XML file [ORBITAX-AMG-2026].
  - Finance teams in each jurisdiction willing to supply entity-level data [ORBITAX-LEAN-2026].
  risks_and_guardrails:
  - Pillar Two needed data beyond CbCR; the insurer found entities in Latin American jurisdictions newly in scope
    through the UK income inclusion rule [ORBITAX-LEAN-2026].
  - Small inconsistencies, such as sign conventions for related-party amounts, can move a jurisdiction's effective
    tax rate [ORBITAX-LEAN-2026].
  human_checkpoints:
  - The tax team completes and reviews the additional Pillar Two information; AMG says it kept control of the financial
    data [ORBITAX-AMG-2026].
  - The insurer used the platform as an independent check on its own Excel calculations [ORBITAX-LEAN-2026].
  role_evolution: AMG's vice president of tax and one manager handled this without added headcount [ORBITAX-AMG-2026].
  evidence_grade: A
  sources:
  - ref: ORBITAX-AMG-2026
    title: How AMG Brought Pillar Two Compliance In-House with Orbitax (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/amg-pillar-two-compliance-case-study
    date: '2026-09-28'
    access: full
    locator: Sections 'Accelerating Implementation with Existing CbCR Data' and 'Results'
  - ref: ORBITAX-LEAN-2026
    title: How a lean global tax team completed Swiss and UK Pillar Two filings ahead of deadline (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/how-a-lean-global-tax-team-completed-swiss-and-uk-pillar-two-filings
    date: '2026-08-10'
    access: full
    locator: Section 'Data Integrity and Compliance Obstacles'
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: Section 'The regulatory crunch hitting direct tax right now', paragraph 3
  last_reviewed: '2026-10-17'
  notes: Grade A rests on one vendor-published case study with a named customer and an unbaselined figure; AI is
    not claimed. Treat as the strongest named evidence in the module, not as evidence of AI effect.
- id: tax-provision-pillar-two-09
  title: AI-assisted mapping of ERP data to GloBE data points (idea)
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  - software-systems
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: The GloBE rules need jurisdiction-level calculations built from entity-level data held in several ERPs,
    which EY calls a substantial change from single-entity income tax work [EY-P2DATA-2024]. Mapping tax data into
    a compliant XML structure takes significant technical skill [LUCANET-2025].
  solution: 'Idea: AI helps map data from different ERP systems to common data standards. EY''s global compliance
    technology leader says AI can assist in this mapping, but standardisation is long-term and needs governance,
    and intrinsic data quality issues still need human correction [EY-P2DATA-2024].'
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: EY-P2DATA-2024
  prerequisites:
  - Secure, standardised data processes first; EY says automation and AI should follow them [EY-P2DATA-2024].
  risks_and_guardrails:
  - AI can quickly spot incomplete or incorrect entries, but manual review and correction are needed [EY-P2DATA-2024].
  human_checkpoints:
  - Manual review and correction of flagged data issues [EY-P2DATA-2024].
  role_evolution: No source describes role change.
  evidence_grade: D
  sources:
  - ref: EY-P2DATA-2024
    title: How to alleviate BEPS 2.0 Pillar Two data challenges
    publisher: EY
    type: firm
    url: https://www.ey.com/en_gl/insights/tax/how-to-alleviate-beps-2-0-pillar-two-data-challenges
    date: '2024-11-22'
    access: full
    locator: Sections on data standards and 'AI drives the need for data standards'
  - ref: LUCANET-2025
    title: 'Pillar Two and XML: The Digital Backbone of GloBE Reporting'
    publisher: Lucanet
    type: vendor
    url: https://www.lucanet.com/en/insights/regulatory-insights/pillar-two-and-xml-digital-backbone-globe-reporting-05-12-2025/
    date: '2025-12-05'
    access: full
    locator: Section 'The practical challenges for MNEs'
  last_reviewed: '2026-10-17'
  notes: Idea. The EY article is from November 2024, older than the preferred window.
- id: tax-provision-pillar-two-10
  title: Pillar Two computation with safe-harbour tests, scenarios and interim provision estimates
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: end-to-end-case-agent
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'GloBE calculations must be run by jurisdiction, and the rules keep changing: the Side-by-Side package
    added a permanent simplified ETR safe harbour and extended the transitional CbCR safe harbour to 1 January 2027,
    and a revised GIR followed on 11 September 2026 [OECD-SBS-2026, OECD-P2-SEP-2026].'
  solution: Purpose-built engines hold the rules, run safe-harbour tests, and run compliance, provision, modelling
    and scenario work from one data set. EY's GloBE Engine runs multiple projects (compliance, provision, modelling,
    scenario planning, CbCR) [EY-GLOBE-ENGINE-2026]. Deloitte's Pillar Two Agent covers safe-harbour calculations,
    accruals, estimates and compliance [DELOITTE-P2BROCH-2024]. AMG used Orbitax for first-year compliance [ORBITAX-AMG-2026].
    These are rules-based tools; the sources do not describe them as AI.
  outcomes:
  - lever: quality
    description: A Swiss-parented insurer (unnamed) ran the platform as an independent check on its Excel calculations;
      it says this surfaced data issues before filing and that it knew in December it was in a safe-harbour position
      in every jurisdiction.
    figure: null
    measures: 'None: qualitative customer statement; the organization is not named.'
    provenance: vendor-published
    source_ref: ORBITAX-LEAN-2026
  prerequisites:
  - Entity-level data collected and validated in the platform [ORBITAX-AMG-2026, EY-GLOBE-ENGINE-2026].
  - Tracking each OECD package and local law, since both change calculations and filing mechanics [WK-PILLAR2-2026].
  risks_and_guardrails:
  - Pillar Two calculations are sensitive to individual data elements [ORBITAX-LEAN-2026].
  - KPMG UK recommends early dialogue with auditors on financial reporting while Side-by-Side legislation is pending
    [OECD-SBS-2026].
  human_checkpoints:
  - Tax staff review dashboards and results before filing [EY-GLOBE-ENGINE-2026].
  - In-scope groups must assess the Side-by-Side components themselves, including the end of the transitional CbCR
    safe harbour and the new ETR safe harbour [OECD-SBS-2026].
  role_evolution: AMG ran this with a two-person tax function and no extra headcount [ORBITAX-AMG-2026].
  evidence_grade: B
  sources:
  - ref: EY-GLOBE-ENGINE-2026
    title: Introducing EY GloBE Engine (slipsheet)
    publisher: EY
    type: firm
    url: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/tax/documents/ey-gl-globe-engine-slipsheet-06-2026.pdf
    date: 2026-06
    access: full
    locator: 'Page 2, ''EY GloBE Engine: your Pillar Two command center'''
  - ref: DELOITTE-P2BROCH-2024
    title: Facilitating your Pillar Two compliance and reporting obligations (Pillar Two Agent brochure)
    publisher: Deloitte
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2024/dttl-pillar-two-agent.pdf
    date: '2024-05-15'
    access: full
    locator: Page 2, 'One-stop shop'
  - ref: ORBITAX-AMG-2026
    title: How AMG Brought Pillar Two Compliance In-House with Orbitax (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/amg-pillar-two-compliance-case-study
    date: '2026-09-28'
    access: full
    locator: Sections 'Choosing to Bring Pillar Two In-House' and 'Results'
  - ref: ORBITAX-LEAN-2026
    title: How a lean global tax team completed Swiss and UK Pillar Two filings ahead of deadline (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/how-a-lean-global-tax-team-completed-swiss-and-uk-pillar-two-filings
    date: '2026-08-10'
    access: full
    locator: Section 'Selecting Orbitax for Pillar Two Compliance'
  - ref: OECD-SBS-2026
    title: Further details on the OECD Pillar Two 'Side-by-Side' package (KPMG UK Tax Matters Digest; the OECD package
      was released 5 January 2026)
    publisher: KPMG UK
    type: firm
    url: https://kpmg.com/uk/en/insights/tax/tmd-further-details-on-the-oecd-pillar-two-side-by-side-package.html
    date: '2026-01-22'
    access: full
    locator: Paragraphs 1-4
  - ref: OECD-P2-SEP-2026
    title: OECD Releases New Pillar Two Guidance, Updated GIR And Framework For Legislative Reviews (Loyens & Loeff;
      the OECD package was released 11 September 2026)
    publisher: Loyens & Loeff via Mondaq
    type: firm
    url: https://www.mondaq.com/oecd-releases-new-pillar-two-guidance-updated-gir-and-framework-for-legislative-reviews/1842556
    date: '2026-09-14'
    access: full
    locator: Section 'Updated GIR'
  - ref: WK-PILLAR2-2026
    title: BEPS Pillar Two Technology Procurement Guide
    publisher: Wolters Kluwer
    type: vendor
    url: https://www.wolterskluwer.com/en/expert-insights/beps-pillar-two-procurement-checklist
    date: '2026-02-16'
    access: full
    locator: Section 'Why technology matters now'
  last_reviewed: '2026-10-17'
  notes: Deterministic automation, not AI. No error rate, parallel-run or override figure is published. Grade B
    because AMG is named but the outcome is qualitative.
- id: tax-provision-pillar-two-11
  title: GloBE Information Return population, XML generation, validation and direct transmission
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  - software-systems
  pattern: end-to-end-case-agent
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: For many groups the first GIR season (due 30 June 2026) was an XML problem more than a tax-law problem
    [FGS-GIR-2026]. Germany and the Netherlands adopted the OECD schema largely unchanged, while Luxembourg, France
    and Austria changed it, so vendors kept several country variants [FGS-GIR-2026]. National portals with business
    rules acted as gatekeepers; some opened days or weeks before the deadline, and the OECD schema itself held errors
    and conflicting rules [FGS-GIR-2026, BTAX-KPMG-GIR-2026]. KPMG International authors say that in some jurisdictions
    only 20% of GIRs were filed successfully before the initial deadline, the rest failing validation [BTAX-KPMG-GIR-2026].
    The OECD issued guidance on 8 June 2026 with fixes, workarounds and switched-off validation rules [OECDPILLARS-GIRXML-2026].
  solution: Platforms populate the GIR from calculation outputs, generate the XML, validate it against schema and
    OECD content rules, and send it by machine-to-machine link where authorities allow. Orbitax reports an M2M GIR
    submission to the Netherlands (3 June 2026), support for UK, Canada, Germany and Dutch submissions, and ATO
    transmission of Australian returns [ORBITAX-NL-2026, ORBITAX-ATO-2026]. EY's engine and Deloitte's Pillar Two
    Agent generate XML files for filing [EY-GLOBE-ENGINE-2026, DELOITTE-P2BROCH-2024]. The sources describe rules-based
    tooling; none claims AI here.
  outcomes:
  - lever: capacity
    description: Orbitax says it prepared or submitted more than 1,700 Pillar Two filings across 34 jurisdictions.
    figure: 1,700+
    measures: Pillar Two filings prepared or submitted through Orbitax's platform across 34 jurisdictions between
      November 2025 and June 2026; more than 60% of filing activity was notifications and self-assessment returns
      rather than GIRs.
    provenance: vendor-published
    source_ref: ORBITAX-SEASON-2026
  - lever: risk
    description: An unnamed Swiss-parented insurer filed Swiss and UK GIRs on 24 June 2026, six days before the
      30 June deadline, after a first Swiss submission was rejected over an apostrophe in one entity name.
    figure: 6 days before the deadline
    measures: Date of successful Swiss and UK GIR filings against the 30 June 2026 deadline; customer not named.
    provenance: vendor-published
    source_ref: ORBITAX-LEAN-2026
  prerequisites:
  - Validated entity data and a tested XML before the portal opens; FGS says Germany's test environment was available
    only briefly and many groups could not test under real conditions [FGS-GIR-2026].
  - 'Local credentials: AMG needed a Dutch certificate for submission [ORBITAX-AMG-2026].'
  - 'Tracking OECD business-rule changes: four OECD rules (60025, 60026, 70092, 70028) were switched off after the
    first season [FGS-GIR-2026].'
  risks_and_guardrails:
  - The OECD sets a 1% tolerance for calculation-based business rules, but FGS says some national implementations,
    notably Austria's, rejected technically correct files; in individual cases PDF submission was a fallback [FGS-GIR-2026].
  - Revised GIR for fiscal years commencing on or after 31 December 2025, with a revised XML schema expected [OECD-P2-SEP-2026].
  - Corrections are possible only against accepted messages and replace whole sections, not single fields [FGS-GIR-2026].
  human_checkpoints:
  - The tax team reviews validation results and resolves errors; the insurer called this the most demanding part
    of the season [ORBITAX-LEAN-2026].
  role_evolution: The tax team's work shifts toward managing data, validation results and local filing obligations,
    a point Lucanet and Orbitax make [LUCANET-2025, ORBITAX-SEASON-2026].
  evidence_grade: B
  sources:
  - ref: FGS-GIR-2026
    title: 'XML statt Steuerrecht: Die wahren Herausforderungen der ersten Pillar-2-Saison (German)'
    publisher: Flick Gocke Schaumburg
    type: firm
    url: https://www.fgs.de/news-and-insights/blog/detail/xml-statt-steuerrecht-die-wahren-herausforderungen-der-ersten-pillar-2-saison
    date: '2026-08-03'
    access: full
    locator: Sections on country variants, business rules, schema gaps, deactivated rules and corrections
  - ref: BTAX-KPMG-GIR-2026
    title: Pillar Two's First Real Test Has Lessons for 2027 Filing Season (Conrad Turley and Tam Do, KPMG International)
    publisher: Bloomberg Tax (Daily Tax Report)
    type: firm
    url: https://news.bloombergtax.com/daily-tax-report/pillar-twos-first-real-test-has-lessons-for-2027-filing-season
    date: '2026-08-21'
    access: full
    locator: Section 'Filing template tribulations' and 'Tax authority filing portals late to go live'
  - ref: OECD-GIR-XML
    title: 'GloBE Information Return (Pillar Two) XML Schema: User Guide for Tax Administrations'
    publisher: OECD
    type: regulator
    url: https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/01/globe-information-return-pillar-two-xml-schema_3980638f/c594935a-en.pdf
    date: 2025-01
    access: full
    locator: Pages 6-8, field requirement and validation rules for the XML schema
  - ref: OECDPILLARS-GIRXML-2026
    title: The OECD releases June 2026 Guidance on the use of the GIR XML Schema for first GloBE filings
    publisher: OECDPillars.com (independent site, not affiliated with the OECD)
    type: press
    url: https://oecdpillars.com/2026/06/08/
    date: '2026-06-08'
    access: full
    locator: Full post
  - ref: ORBITAX-NL-2026
    title: Orbitax Completes First GIR Submission to the Netherlands and Expands Global Pillar Two Filing Readiness
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/orbitax-completes-first-gir-submission-to-the-netherlands-and-expands-global-pillar-two-filing-readiness
    date: '2026-06-03'
    access: full
    locator: Paragraphs 1-4
  - ref: ORBITAX-DIGIPOORT-2026
    title: Orbitax Successfully Establishes Direct Transmission Connectivity with the Netherlands' Logius Digipoort
      for Pillar Two Reporting
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/orbitax-successfully-establishes-direct-transmission-connectivity-with-netherlands-logius-digipoort-for-pillar-two-reporting
    date: '2026-04-23'
    access: full
    locator: Paragraphs 1-2
  - ref: ORBITAX-ATO-2026
    title: 'Australian CGDMTR Filing: Building a Repeatable Pillar Two Process with Direct ATO Transmission'
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/australia-cgdmtr-filing-ato-transmission
    date: '2026-08-19'
    access: full
    locator: Section 'Moving from Calculations to a Controlled Filing Process'
  - ref: ORBITAX-SEASON-2026
    title: 'Inside the First Pillar Two Filing Season: Trends, Challenges, and Lessons (1,700+ filings)'
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/inside-the-first-pillar-two-filing-season
    date: '2026-08-20'
    access: full
    locator: Sections 'Beyond the GIR' and 'Filing Activity Concentrated Near the Deadline'
  - ref: ORBITAX-LEAN-2026
    title: How a lean global tax team completed Swiss and UK Pillar Two filings ahead of deadline (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/how-a-lean-global-tax-team-completed-swiss-and-uk-pillar-two-filings
    date: '2026-08-10'
    access: full
    locator: Sections 'Managing the Filing Season and Technical Hurdles' and 'FY2024 Compliance Results'
  - ref: ORBITAX-AMG-2026
    title: How AMG Brought Pillar Two Compliance In-House with Orbitax (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/amg-pillar-two-compliance-case-study
    date: '2026-09-28'
    access: full
    locator: Section 'From Implementation to First Filing'
  - ref: OECD-P2-SEP-2026
    title: OECD Releases New Pillar Two Guidance, Updated GIR And Framework For Legislative Reviews (Loyens & Loeff;
      the OECD package was released 11 September 2026)
    publisher: Loyens & Loeff via Mondaq
    type: firm
    url: https://www.mondaq.com/oecd-releases-new-pillar-two-guidance-updated-gir-and-framework-for-legislative-reviews/1842556
    date: '2026-09-14'
    access: full
    locator: Section 'Updated GIR'
  - ref: EY-GLOBE-ENGINE-2026
    title: Introducing EY GloBE Engine (slipsheet)
    publisher: EY
    type: firm
    url: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/tax/documents/ey-gl-globe-engine-slipsheet-06-2026.pdf
    date: 2026-06
    access: full
    locator: Page 2, 'Comply with all Pillar Two filing requirements'
  - ref: DELOITTE-P2BROCH-2024
    title: Facilitating your Pillar Two compliance and reporting obligations (Pillar Two Agent brochure)
    publisher: Deloitte
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2024/dttl-pillar-two-agent.pdf
    date: '2024-05-15'
    access: full
    locator: Page 1, 'Filing'
  last_reviewed: '2026-10-17'
  notes: The richest practice evidence in the module, but all vendor-published or firm-reported and not AI. Orbitax's
    April 2026 Digipoort connection was a test with sample data against a test environment [ORBITAX-DIGIPOORT-2026].
    The 20% figure is KPMG's experience in some jurisdictions, not a global rate.
- id: tax-provision-pillar-two-12
  title: GIR correction and amendment management (DocRefId tracking)
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: The GIR schema handles corrections through MessageTypeIndic, DocTypeIndic, DocRefId and CorrDocRefId;
    corrections work only against already accepted messages, and affected sections must be replaced in full [FGS-GIR-2026].
    FGS expects the number of corrections to rise because of deactivated rules and later OECD clarifications, and
    says groups must document submitted XML history and references in an audit-proof way [FGS-GIR-2026].
  solution: FGS says its Pillar 2 Management App already supports correction returns and has largely automated the
    management and referencing of corrected DocRefIds [FGS-GIR-2026]. FGS names no client.
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: FGS-GIR-2026
  prerequisites:
  - A versioned history of every XML file submitted and its reference IDs [FGS-GIR-2026].
  risks_and_guardrails:
  - A wrong reference to a corrected document breaks the correction chain; the schema allows no field-level correction
    [FGS-GIR-2026].
  human_checkpoints:
  - No source describes the review step.
  role_evolution: No source describes role change.
  evidence_grade: C
  sources:
  - ref: FGS-GIR-2026
    title: 'XML statt Steuerrecht: Die wahren Herausforderungen der ersten Pillar-2-Saison (German)'
    publisher: Flick Gocke Schaumburg
    type: firm
    url: https://www.fgs.de/news-and-insights/blog/detail/xml-statt-steuerrecht-die-wahren-herausforderungen-der-ersten-pillar-2-saison
    date: '2026-08-03'
    access: full
    locator: 'Section ''Der nächste große Fokus: Korrekturerklärungen'' and ''Fazit'''
  last_reviewed: '2026-10-17'
  notes: One firm's own statement about its own app. Not AI.
- id: tax-provision-pillar-two-13
  title: Conversational copilot over live Pillar Two scenarios
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  - research-synthesis
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: After the calculations are done, the work left is reviewing jurisdiction and entity data, answering finance
    and audit-committee questions, validating XML and documenting decisions; Orbitax calls these workflow problems,
    not research problems [ORBITAX-XATBOTPRO-2026, TR-CORPAI-2026].
  solution: Orbitax says its XatBot assistant can read a team's live GMT scenarios and answer questions in natural
    language (for example, which jurisdictions have a GloBE ETR below 15%), analyse uploaded CSV files for outliers,
    run Deep Research reports on Pillar Two questions, draft emails and PowerPoint updates for the audit committee,
    and, in Autopilot mode, create and navigate scenarios from a conversation [ORBITAX-XATBOTPRO-2026]. A Pillar
    Two and GloBE 'Skill' standardises answers across the team [ORBITAX-XATBOTPRO-2026]. Orbitax offered Pro+ at
    no extra cost to GMT users from the 4 May 2026 post until 30 June 2026 [ORBITAX-XATBOTPRO-2026].
  outcomes:
  - lever: speed
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: ORBITAX-XATBOTPRO-2026
  prerequisites:
  - Scenarios and entity data already in the Orbitax platform [ORBITAX-XATBOTPRO-2026].
  - Optional MCP connections to data warehouses, document stores and ERPs [ORBITAX-XATBOT-2026].
  risks_and_guardrails:
  - Orbitax's Verification tab scores each key point against its database and the web, and Orbitax says High-confidence
    points can go into a filing file 'with appropriate professional judgment applied' [ORBITAX-XATBOTPRO-2026];
    this is the vendor's claim.
  - Deep Research during the beta was limited to five requests a month [ORBITAX-XATBOTPRO-2026].
  human_checkpoints:
  - Autopilot lets the user review the generated workflow before it runs [ORBITAX-XATBOT-2026].
  - Professional judgment on anything entering a filing file [ORBITAX-XATBOTPRO-2026].
  role_evolution: No source quantifies role change. Orbitax's case study says XatBot helped the unnamed insurer's
    lean team work through many day-to-day issues in the filing season [ORBITAX-LEAN-2026].
  evidence_grade: C
  sources:
  - ref: ORBITAX-XATBOTPRO-2026
    title: XatBot Pro+ now free for Orbitax GMT Users to make your June 2026 Pillar Two filing season easier
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/announcements/xatbot-pro-now-free-for-orbitax-gmt-users-to-make-your-june-2026-pillar-two-filing-season-easier
    date: '2026-05-04'
    access: full
    locator: Sections 'Autopilot', 'Live scenario analysis', 'Deep Research', 'Response Verification', 'CSV uploads'
  - ref: ORBITAX-XATBOT-2026
    title: 'XatBot''s Latest Release: Autopilot, Deep Research, MCP Connections, and Intelligent Tax Skills'
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/announcements/xatbots-latest-release-autopilot-deep-research-mcp-connections-and-intelligent-tax-skills
    date: '2026-04-19'
    access: full
    locator: Sections 'Automate Multi-Step Workflows with Autopilot', 'Connect XatBot to Your Entire Workflow with
      MCP'
  - ref: ORBITAX-LEAN-2026
    title: How a lean global tax team completed Swiss and UK Pillar Two filings ahead of deadline (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/how-a-lean-global-tax-team-completed-swiss-and-uk-pillar-two-filings
    date: '2026-08-10'
    access: full
    locator: Section 'Managing the Filing Season and Technical Hurdles', paragraph 1
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: Section 'Orbitax', 'A workflow problem, not a research problem'
  last_reviewed: '2026-10-17'
  notes: The only generative-AI product found that is built into a Pillar Two engine. The customer using it is unnamed,
    so maturity stays 'announced'. No accuracy, hallucination or override measurement is published.
- id: tax-provision-pillar-two-14
  title: Firm-run Pillar Two platform with specialist team (co-sourcing or outsourcing)
  archetype: tax
  module: provision-pillar-two
  function: service-delivery
  work_types:
  - data-reporting
  - transaction-processing
  pattern: end-to-end-case-agent
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Heads of Tax and Big Four or Tier 1 advisory teams must run Pillar Two compliance quickly and with audit-ready
    transparency [WK-PILLAR2-2026]. Deloitte's research of more than 500 tax leaders and CFOs says 70% expect to
    pay over US$500,000 a year to comply and 76% of CFOs expect to use technology to meet higher compliance cost
    at unchanged staffing [DELOITTE-P2AGENT-2024].
  solution: Deloitte offers its Pillar Two Agent only when clients work with its tax team under co-sourcing or outsourcing;
    the platform collects data by API or manually, calculates top-up tax, validates returns, and produces GIR and
    QDMTT filings, with Deloitte teams filing [DELOITTE-P2AGENT-2024, DELOITTE-P2BROCH-2024]. Deloitte Germany demonstrated
    it live in a February 2026 webcast [DELOITTE-DE-TTI-2026]. EY's slipsheet offers access to EY professionals
    with its GloBE Engine [EY-GLOBE-ENGINE-2026]. FGS runs its own Pillar 2 Management App for clients [FGS-GIR-2026].
    The sources do not describe AI.
  outcomes:
  - lever: capacity
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: DELOITTE-P2AGENT-2024
  prerequisites:
  - A co-sourcing or outsourcing engagement with Deloitte [DELOITTE-P2AGENT-2024].
  risks_and_guardrails:
  - AMG weighed outsourcing against in-house and chose in-house to keep ownership of its data, calculations and
    process [ORBITAX-AMG-2026].
  human_checkpoints:
  - Clients review and sign off data and results inside the platform [DELOITTE-P2BROCH-2024].
  role_evolution: The client team steps back to review and sign-off; Deloitte's research lists technology skills
    as the third biggest talent gap in Pillar Two implementation [DELOITTE-P2AGENT-2024].
  evidence_grade: B
  sources:
  - ref: DELOITTE-P2AGENT-2024
    title: 'Pillar Two Agent: Tech-powered compliance'
    publisher: Deloitte
    type: firm
    url: https://www.deloitte.com/global/en/services/tax/services/tech-powered-compliance.html
    date: '2024-07-26'
    access: full
    locator: Sections 'Supported by specialists' and the survey statistics list
  - ref: DELOITTE-P2BROCH-2024
    title: Facilitating your Pillar Two compliance and reporting obligations (Pillar Two Agent brochure)
    publisher: Deloitte
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2024/dttl-pillar-two-agent.pdf
    date: '2024-05-15'
    access: full
    locator: Pages 1-2
  - ref: DELOITTE-ITR-2025
    title: Deloitte Wins Big at 2025 ITR Americas Awards (press release)
    publisher: Deloitte US
    type: firm
    url: https://www.deloitte.com/us/en/about/press-room/deloitte-announces-wins-at-2025-itr-americas-tax-awards.html
    date: '2025-10-27'
    access: full
    locator: Paragraph on the Pillar Two Agent
  - ref: DELOITTE-DE-TTI-2026
    title: 'Tax Technology Insights #69: Pillar 2 / SbS & Simplified Safe Harbour (webcast notice, German)'
    publisher: Deloitte Germany
    type: conference
    url: https://www.deloitte.com/de/de/services/tax/events/tax-technology-insights-69.html
    date: '2026-02-24'
    access: full
    locator: Section 'Über den Webcast'
  - ref: EY-GLOBE-ENGINE-2026
    title: Introducing EY GloBE Engine (slipsheet)
    publisher: EY
    type: firm
    url: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/tax/documents/ey-gl-globe-engine-slipsheet-06-2026.pdf
    date: 2026-06
    access: full
    locator: Page 1, 'Access to EY professionals when you need it'
  - ref: FGS-GIR-2026
    title: 'XML statt Steuerrecht: Die wahren Herausforderungen der ersten Pillar-2-Saison (German)'
    publisher: Flick Gocke Schaumburg
    type: firm
    url: https://www.fgs.de/news-and-insights/blog/detail/xml-statt-steuerrecht-die-wahren-herausforderungen-der-ersten-pillar-2-saison
    date: '2026-08-03'
    access: full
    locator: Section 'Fazit'
  - ref: WK-PILLAR2-2026
    title: BEPS Pillar Two Technology Procurement Guide
    publisher: Wolters Kluwer
    type: vendor
    url: https://www.wolterskluwer.com/en/expert-insights/beps-pillar-two-procurement-checklist
    date: '2026-02-16'
    access: full
    locator: Section 'Introduction'
  last_reviewed: '2026-10-17'
  notes: Named firms operate these platforms, but none publishes a client, volume or outcome figure. Despite the
    product name 'Agent', the sources do not describe generative AI. The Deloitte survey date and sample are not
    given on the page.
- id: tax-provision-pillar-two-15
  title: AI analysis of Excel-based provision workpapers (idea)
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Many provision teams still build workpapers in Excel; Finrep calls an Excel-only provision a control
    risk that auditors are increasingly unwilling to accept [FINREP-ASC740-2026].
  solution: 'Idea: an AI assistant reads provision workbooks to explain formulas, check tie-outs and answer questions.
    TEI Midyear 2026 ran a hands-on Tax Lab on using AI to analyse Excel files for accountants [TEI-MIDYEAR-2026].
    Bloomberg Tax describes AI-powered insights inside Workpapers spreadsheets [BTAX-ASC740-2026]. No source shows
    a provision team doing this.'
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    provenance: vendor-published
    source_ref: TEI-MIDYEAR-2026
  prerequisites:
  - No source states prerequisites.
  risks_and_guardrails:
  - Finrep says AI tools embedded in provision workflows must be treated as controls for audit purposes, which is
    Finrep's reading and not a cited standard [FINREP-ASC740-2026].
  human_checkpoints:
  - No source describes the review step.
  role_evolution: No source describes role change.
  evidence_grade: D
  sources:
  - ref: TEI-MIDYEAR-2026
    title: TEI Midyear Conference 2026 At a Glance Agenda (rev 3.2)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: '2026-03-15'
    access: full
    locator: 'Page 3, Tuesday 17 March 2026, ''TEI Tax Lab: Escaping Excel: Using AI to Analyze Excel Files for
      Accountants'''
  - ref: FINREP-ASC740-2026
    title: 'AI Tax Provision ASC 740 Reporting: A 2026 Practitioner Walkthrough'
    publisher: Finrep (Gana Misra, CEO)
    type: vendor
    url: https://www.finrep.ai/blog/ai-tax-provision-asc-740-reporting-a-2026-practitioner-walkthrough
    date: '2026-09-30'
    access: full
    locator: Opening paragraph and section 'SOX 404 and PCAOB Audit Implications'
  - ref: BTAX-ASC740-2026
    title: Accelerate your ASC 740 process (Bloomberg Tax Research, Provision and Workpapers product page)
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/products/accelerate-your-asc-740-process/
    date: '2026-03-25'
    access: full
    locator: Section 'Get research answers directly in your spreadsheets'
  last_reviewed: '2026-10-17'
  notes: Idea. The TEI lab is a generic accountants' session, not provision-specific.
- id: tax-provision-pillar-two-16
  title: Bringing Pillar Two compliance in-house on a platform instead of outsourcing it
  archetype: tax
  module: provision-pillar-two
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: end-to-end-case-agent
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: AMG's tax function is small and could not add headcount for the Pillar Two workload; it had to choose
    between outsourcing to an accounting firm and building the capability itself [ORBITAX-AMG-2026].
  solution: AMG chose software run in-house, after learning that many accounting firms themselves used the same
    vendor's technology [ORBITAX-AMG-2026]. A Swiss-parented insurer with a lean global tax team also chose to file
    in-house, with local advisors supplying jurisdiction-specific expertise as needed [ORBITAX-LEAN-2026]. AMG was
    already a Thomson Reuters customer for tax provision and income tax [ORBITAX-AMG-2026]. The sources describe
    software, not AI.
  outcomes:
  - lever: capacity
    description: AMG's two-person tax function delivered first-year Pillar Two compliance across 70-80 entities
      in 25 jurisdictions with no additional headcount.
    figure: 2 people; 70-80 entities; 25 jurisdictions; no added headcount
    measures: Size of AMG's tax function against the entities and jurisdictions covered in its first-year Pillar
      Two compliance, as stated in the vendor's case study.
    provenance: vendor-published
    source_ref: ORBITAX-AMG-2026
  prerequisites:
  - Existing CbCR data to seed the platform [ORBITAX-AMG-2026].
  - Support from the vendor; the insurer credits the support team for filing on time [ORBITAX-LEAN-2026].
  risks_and_guardrails:
  - First-year filings met unexpected hurdles, such as a Dutch certificate requirement for AMG and a Swiss portal
    rejection for the insurer [ORBITAX-AMG-2026, ORBITAX-LEAN-2026].
  - Orbitax's own data show more than 60% of filing activity was notifications and self-assessment returns, so local
    obligations add workload beyond the GIR [ORBITAX-SEASON-2026].
  human_checkpoints:
  - AMG's vice president of tax reviewed and filed; she says she is confident in the data and what she filed [ORBITAX-AMG-2026].
  role_evolution: The in-house tax team keeps the data, calculations and process rather than handing them to a provider
    each year [ORBITAX-AMG-2026].
  evidence_grade: A
  sources:
  - ref: ORBITAX-AMG-2026
    title: How AMG Brought Pillar Two Compliance In-House with Orbitax (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/amg-pillar-two-compliance-case-study
    date: '2026-09-28'
    access: full
    locator: Introduction, 'Choosing to Bring Pillar Two In-House' and 'Results'
  - ref: ORBITAX-LEAN-2026
    title: How a lean global tax team completed Swiss and UK Pillar Two filings ahead of deadline (case study)
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/case-studies/how-a-lean-global-tax-team-completed-swiss-and-uk-pillar-two-filings
    date: '2026-08-10'
    access: full
    locator: Section 'A lean global tax team takes on Pillar Two'
  - ref: ORBITAX-SEASON-2026
    title: 'Inside the First Pillar Two Filing Season: Trends, Challenges, and Lessons (1,700+ filings)'
    publisher: Orbitax
    type: vendor
    url: https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/inside-the-first-pillar-two-filing-season
    date: '2026-08-20'
    access: full
    locator: Section 'Beyond the GIR'
  last_reviewed: '2026-10-17'
  notes: Same named case study as 08. Vendor-published, not independent, no baseline cost. Software, not AI.
```

## 3. Module notes

### Processes and key steps (with work types)

Provision (ASC 740 / IAS 12). Finrep, a vendor, splits the provision into seven steps [FINREP-ASC740-2026]; the work types are my mapping.

- Pull close data and map the trial balance into provision inputs (data-reporting) [KOGNITOS-2026, BTAX-ASC740-2026].
- Identify book-to-tax differences and calculate current tax (transaction-processing) [FINREP-ASC740-2026].
- Calculate deferred tax assets and liabilities and roll balances forward (transaction-processing, data-reporting) [FINREP-ASC740-2026].
- Assess valuation allowances (expert-judgment) [FINREP-ASC740-2026].
- Analyse uncertain tax positions (expert-judgment, research-synthesis) [FINREP-ASC740-2026, TR-AGENTICCORP-2025].
- Prepare the rate reconciliation and income-taxes-paid tables required by ASU 2023-09 (data-reporting) [KPMG-ASU-2023].
- Draft footnotes, review, document controls and support the auditor (document-production, review-assurance) [FINREP-ASC740-2026].

Pillar Two.

- Collect and map entity data (data-reporting) [EY-P2DATA-2024, WK-PILLAR2-2026].
- Compute jurisdictional ETRs, safe-harbour tests, top-up tax and QDMTT (transaction-processing) [DELOITTE-P2BROCH-2024].
- Account for the top-up tax in the financial statements; the IASB amended IAS 12 in May 2023 for Pillar Two [IFRS-IAS12-2023].
- Populate the GIR, generate and validate XML, transmit (data-reporting, software-systems) [OECD-GIR-XML, ORBITAX-NL-2026].
- Handle GIR notifications, self-assessment and QDMTT returns and registrations (coordination-scheduling); Orbitax says over 60% of its filing activity was notifications and self-assessment returns [ORBITAX-SEASON-2026].
- File corrections [FGS-GIR-2026] and track the revised GIR and peer reviews of domestic legislation [OECD-P2-SEP-2026].
- Talk to the auditor about financial reporting under Side-by-Side [OECD-SBS-2026].

### Common pain points

- **Data, not calculation.** Kognitos (vendor) says data assembly is the binding constraint after Pillar Two [KOGNITOS-2026]; EY says GloBE needs jurisdictional aggregation of entity data from several ERPs [EY-P2DATA-2024]; an insurer found extra data elements beyond CbCR and sign-convention differences that moved ETRs [ORBITAX-LEAN-2026].
- **XML and portals.** Country variants, gatekeeper business rules, portals opened late, a short-lived German test environment, rounding-tolerance rules misapplied, schema gaps, and later switched-off rules [FGS-GIR-2026, BTAX-KPMG-GIR-2026, OECDPILLARS-GIRXML-2026].
- **A moving target.** The Side-by-Side package (5 January 2026) and a second package with a revised GIR (11 September 2026) changed safe harbours and the return; a revised XML schema is expected [OECD-SBS-2026, OECD-P2-SEP-2026].
- **Central filing uncertainty.** Exchange relationships were not all active and groups relied on a political commitment to allow central filing; only 6 of 19 "second wave" jurisdictions had signed the GIR exchange agreement at the time of the KPMG authors' piece [BTAX-KPMG-GIR-2026].
- **Disclosure workload.** ASU 2023-09 adds category and jurisdiction detail to the rate reconciliation [KPMG-ASU-2023, TR-AGENTICCORP-2025].
- **Capacity.** 58% of surveyed corporate tax departments say they are under-resourced, up from 51% the year before [TR-CORPTAX-2025].

### Metrics and benchmarks (what each figure measures)

- 67% of corporate tax departments not using GenAI; of departments implementing new technology, 57% plan to include GenAI, 36% machine learning and 17% to explore more advanced AI such as agentic AI; 58% under-resourced (51% the prior year); 38% intend to hire (32% in 2024); 59% lack confidence in upgrading technology over two years. Source: Thomson Reuters Institute 2025 State of the Corporate Tax Department, as reported by TR; vendor-owned, sample size not stated [TR-CORPTAX-2025].
- 71% of surveyed companies' tax departments use AI tools and 19% are preparing; 89% of those use company-wide standard tools and 29% specialised tax applications; 66% of AI users report noticeable time savings; hurdles: IT approvals 47%, data protection 41%, lack of knowledge 41%. KPMG Germany quick survey; sample size not stated in the release [KPMG-DE-2026].
- 51% of tax teams under-resourced and 61% of work on tactical tasks; only 22% of organizations have a visible AI strategy; 91% believe AI outputs should be more accurate than human work. TR Future of Professionals 2025 as quoted by TR (a different survey from the 58% figure) [TR-AGENTICCORP-2025].
- More than 1,700 Pillar Two filings prepared or submitted through Orbitax across 34 jurisdictions, November 2025 to June 2026; over 60% of activity was notifications and self-assessment returns; nearly one-third of activity fell in the final week before 30 June. Vendor-published [ORBITAX-SEASON-2026].
- In some jurisdictions only 20% of GIRs were filed successfully before the initial deadline (KPMG's experience); the OECD digital rulebook has more than 120 business rules; 19 second-wave jurisdictions join the original 37 [BTAX-KPMG-GIR-2026].
- The first GIR required more than 100 data points, per TR [TR-CORPAI-2026].
- AMG: around 10 days to implement Pillar Two data collection from existing CbCR XML; a two-person team covered 70-80 entities in 25 jurisdictions. Vendor-published [ORBITAX-AMG-2026].
- 85% of businesses expect to pay more tax because of Pillar Two and 81% call its implementation the biggest legislative and regulatory change, from the 2025 EY Tax and Finance Operations survey as quoted by EY (the survey itself was not opened) [EY-GLOBE-ENGINE-2026].
- Deloitte's Pillar Two research of over 500 tax leaders and CFOs: 70% expect to pay over US$500,000 a year to comply; 76% of CFOs expect to use technology to address higher compliance cost at the same staffing. Survey date not stated [DELOITTE-P2AGENT-2024].
- Absent: no error rate, override rate, parallel-run result, inspection outcome or independent accuracy test for AI in provision or Pillar Two work. The nearest independent measurement is adjacent: a benchmark found frontier models computed fewer than a third of simplified US federal personal returns correctly [ARXIV-TAXCALCBENCH-2025].

### Guardrails and regulatory points

- ASU 2023-09: public business entities give a tabular rate reconciliation in percentages and amounts by specific categories, with reconciling items at or above 5% of statutory tax broken out further, and income taxes paid by federal, state/local and foreign; effective for public business entities for fiscal years beginning after 15 December 2024 and for other entities after 15 December 2025 [KPMG-ASU-2023].
- IAS 12 was amended in May 2023 for Pillar Two model rules [IFRS-IAS12-2023]. I did not open the amendment text.
- OECD: the GIR XML user guide (approved 30 October 2024) sets validation elements that must be present and may be checked automatically by the receiver [OECD-GIR-XML]; a June 2026 guidance note gave fixes and switched off some validation rules [OECDPILLARS-GIRXML-2026]; the 11 September 2026 package adds a revised GIR and a peer-review framework for domestic legislation [OECD-P2-SEP-2026].
- PCAOB staff (July 2024, not Board policy): audit firms expect GenAI to augment, not replace, people; an engagement team member using a GenAI tool is still responsible for the result; reviewers apply the same diligence; preparers use GenAI for first drafts and some reconciliations but raise black-box and inconsistent-output concerns [PCAOB-GENAI-2024].
- AICPA: the Council on AI Risk in Tax (23 September 2026) will refine a 20-risk framework designed by Danny Werfel for tax administration and preparation [AICPA-CART-2026]. A text search of its appendices found nothing on provision or ASC 740 [AICPA-WERFEL-2026].
- Audit overlap: KPMG UK recommends early dialogue with auditors on financial reporting under Side-by-Side [OECD-SBS-2026]. Finrep (vendor) says AI inside a provision should be documented as a SOX control and cites PCAOB standards; I could not verify its reading [FINREP-ASC740-2026].

### Frontier signals (dated)

- 2026-01-05 and 2026-09-11: OECD Side-by-Side package and a second package with a revised GIR; a revised XML schema is expected [OECD-SBS-2026, OECD-P2-SEP-2026].
- 2026-04-19: Orbitax announces XatBot Autopilot, Deep Research, MCP connections and Tax Skills inside its International Tax Platform; 2026-05-04: Pro+ offered to GMT users for the filing season [ORBITAX-XATBOT-2026, ORBITAX-XATBOTPRO-2026].
- 2026-05-20: KPMG and Anthropic announce Claude in KPMG's Digital Gateway, tax clients first; KPMG US's tax vice chair says building an agent for changing tax rules went from weeks to minutes [KPMG-ANTHROPIC-2026].
- 2026-06-08: OECD guidance on using the GIR XML schema in the first cycle [OECDPILLARS-GIRXML-2026].
- 2026-06-24: Thomson Reuters recruits a ONESOURCE Tax Provision product specialist to test generative AI features [TR-JOB-2026].
- 2026-08-03: FGS expects correction filings to rise and says XML handling will matter as much as the calculation [FGS-GIR-2026].
- 2026-08-21: KPMG authors expect a bigger 2027 test as 19 second-wave jurisdictions join [BTAX-KPMG-GIR-2026].
- 2026-10-02: an arXiv preprint proposes LLM-plus-verification formalisation of tax forms into executable code; adjacent, US personal tax [ARXIV-LAWORDER-2026].

### Workforce and role effects

- AMG delivered first-year Pillar Two compliance with a two-person function and no added headcount (vendor-published) [ORBITAX-AMG-2026].
- KPMG Germany: 58% of companies expect stable domestic tax headcount and 72% stable international headcount [KPMG-DE-2026]. Sala argues AI will shrink corporate tax teams little because AI cannot hold culpability and tax practice is more than preparation [SALA-TAXNOTES-2026].
- Thomson Reuters seeks provision practitioners with 5-7 years' experience to validate AI features [TR-JOB-2026]; a SaaS company's tax manager posting asks for a builder who uses AI and automation to keep the function lean [GAMMA-JOB-2026].
- Deloitte's research lists technology skills as the third biggest talent gap in Pillar Two implementation [DELOITTE-P2AGENT-2024].

### Objections and concerns practitioners raise

- Accuracy and trust: 41% of tax professionals will not use AI without human review unless it is 100% accurate [TR-AGENTICCORP-2025]; hallucinated citations and cascading errors (from a vendor selling mitigation) [BTAX-HALLUC-2026].
- Organisational barriers: IT approvals, data protection and lack of knowledge [KPMG-DE-2026].
- Accountability: AI cannot take regulatory, ethical or financial responsibility [SALA-TAXNOTES-2026].
- Auditability: preparers worry about black-box tools and inconsistent output [PCAOB-GENAI-2024].
- Data first: EY says automation and AI should follow secure, standardised data processes [EY-P2DATA-2024].
- Vendor-sourced claims: several "AI" provision features are rules-based or on a roadmap [CORPTAX-2026, FINREP-ASC740-2026].

### Discourse snapshot

- TEI Midyear (15-18 March 2026): a "Pillar Two and Technology" Tax Lab (18 March), an Excel-and-AI lab (17 March), a "Corporate Tax and Generative AI" session and a "Tax GPT" closing plenary; titles only [TEI-MIDYEAR-2026].
- Bloomberg Tax Leadership Forum (16 June 2026): a panel to cover AI in compliance, provisioning and risk, with speakers from Home Depot, OpenAI, EisnerAmper and KPMG; I found only the pre-event notice [BTAX-FORUM-2026].
- Oxford CBT (26 June 2026): separate sessions on the Side-by-Side package and on tax and AI [OXFORD-CBT-2026].
- EY webcast (19 February 2026) listed EY's global tax accounting leader beside its BEPS leader and promised discussion of delivery models and data and technology challenges [EY-WEBCAST-2026]; Deloitte Germany demonstrated its Pillar Two Agent live (24 February 2026) [DELOITTE-DE-TTI-2026].
- A podcast episode (25 June 2026) covered Pillar Two data collection and how AI helps tax professionals with complex rules; I read only the show notes [ACAST-TAXTECH-2026].

### Interview probes for an advisor

1. Which provision steps (data pull, book-to-tax, deferred rollforward, UTP, rate reconciliation, footnotes) does AI touch today, and what has your auditor asked about each?
2. Where does the close-to-tax handoff break most often, and who owns the data between the ledger and the provision?
3. In Pillar Two, where did errors surface in the first GIR season (data mapping, safe-harbour tests, XML validation, portal rejection), who found them, and did you run a parallel check against Excel?
4. How are you planning corrections, the revised GIR and XML schema, and the 2027 filings with more jurisdictions?
5. Did you insource or outsource Pillar Two, and what happened to headcount and to how the team spends its time?

## 4. Routed to other modules

- Neo.Tax and R&D credit automation, IRS Form 6765 Section G: compliance-corporate [TR-CORPAI-2026].
- Savant Labs agentic automation with Oxford Industries (sales and use tax, VAT and GST, reconciliation): indirect-tax [SAVANT-2026].
- Corptax "audit prediction" on its AI roadmap: controversy [CORPTAX-2026].
- Transfer pricing and statutory reporting expected as growth areas for AI; the Oxford session on delegating decisions to AI and transfer pricing law: transfer-pricing [TR-CORPAI-2026, OXFORD-CBT-2026].
- TaxCalcBench, the agentic legal-critical software study and Law&Order (US personal and federal tax preparation): compliance-individual-business [ARXIV-TAXCALCBENCH-2025, ARXIV-LEGALCRITICAL-2025, ARXIV-LAWORDER-2026].
- Hallucination risk, AICPA CART and Werfel risk framework: tax guardrails and professional responsibility cross-cutting module [BTAX-HALLUC-2026, AICPA-CART-2026, AICPA-WERFEL-2026].
- Sala's headcount argument, the Gamma and Thomson Reuters postings, KPMG Germany headcount expectations: tax workforce and talent cross-cutting module [SALA-TAXNOTES-2026, GAMMA-JOB-2026, KPMG-DE-2026].
- KPMG and Anthropic alliance: state of AI disruption cross-cutting module [KPMG-ANTHROPIC-2026].
- PCAOB observations on auditors' use of GenAI (administrative and research tasks, disclosure completeness checks): the assurance archetype, audit module. Nothing tax-specific was found [PCAOB-GENAI-2024].
- Orbitax MCP connections, Lucanet on XML as the digital backbone, public CbCR: tax-data-technology [ORBITAX-XATBOT-2026, LUCANET-2025].

## 5. Sources

Format: ref | title | publisher | type | URL | date | access (note). All 49 were opened; none is search-only.

- ACAST-TAXTECH-2026 | Tax, Tech & The Pillar Two Reality Check (Tax, tech, and other stuff, ep. 26) | Tax, tech, and other stuff podcast (Acast) | podcast | https://shows.acast.com/tax-tech-and-other-stuff/episodes/6a3ce7b00ad474357457b7fb | 2026-06-25 | access: full (show notes only; the audio was not heard)
- AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax (Council on AI Risk in Tax) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | access: full
- AICPA-WERFEL-2026 | Appendices to 'A Risk Framework for the Use of AI in Tax Administration and Preparation' (Danny Werfel) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 | access: full (text search of the appendices found no mention of tax provision or ASC 740)
- ARXIV-LAWORDER-2026 | Law And Order: Tax Law Autoformalization | arXiv (2610.02792) | academic | https://arxiv.org/abs/2610.02792 | 2026-10-02 | access: full (abstract only; adjacent (US tax forms); preprint)
- ARXIV-LEGALCRITICAL-2025 | An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software | arXiv (2509.13471) | academic | https://arxiv.org/abs/2509.13471 | 2025-09-16 | access: full (abstract only; adjacent (US federal tax preparation))
- ARXIV-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | arXiv (2507.16126) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | access: full (abstract only; adjacent (US personal income tax))
- BTAX-ASC740-2026 | Accelerate your ASC 740 process (Bloomberg Tax Research, Provision and Workpapers product page) | Bloomberg Tax | vendor | https://pro.bloombergtax.com/products/accelerate-your-asc-740-process/ | 2026-03-25 | access: full (datePublished in JSON-LD; page modified 2026-06-18)
- BTAX-FORUM-2026 | Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk (press release for the 16 June 2026 forum) | Bloomberg Tax | conference | https://pro.bloombergtax.com/?p=17345 | 2026-06-10 | access: full (pre-event description; no record of what was said on the day was found)
- BTAX-HALLUC-2026 | AI Hallucinations in Tax: The Risks and How to Mitigate Them | Bloomberg Tax | vendor | https://pro.bloombergtax.com/insights/artificial-intelligence/ai-hallucinations-in-tax-the-risks-and-how-to-mitigate-them/ | 2026-05-11 | access: full (vendor marketing for its own AI tools)
- BTAX-KPMG-GIR-2026 | Pillar Two's First Real Test Has Lessons for 2027 Filing Season (Conrad Turley and Tam Do, KPMG International) | Bloomberg Tax (Daily Tax Report) | firm | https://news.bloombergtax.com/daily-tax-report/pillar-twos-first-real-test-has-lessons-for-2027-filing-season | 2026-08-21 | access: full (opinion piece by KPMG authors; the 20% figure is 'based on KPMG's experience')
- CORPTAX-2026 | AI and ML in Tax: Applications, Considerations, and Responsible Engagement (webinar page with Corptax AI/ML roadmap) | CSC Corptax with ACT | vendor | https://go.corptax.com/act-ai-ml-tax | 2026 | access: full (year only: page shows a 2026 copyright and no publication date)
- DELOITTE-DE-TTI-2026 | Tax Technology Insights #69: Pillar 2 / SbS & Simplified Safe Harbour (webcast notice, German) | Deloitte Germany | conference | https://www.deloitte.com/de/de/services/tax/events/tax-technology-insights-69.html | 2026-02-24 | access: full (webcast date; notice only)
- DELOITTE-ITR-2025 | Deloitte Wins Big at 2025 ITR Americas Awards (press release) | Deloitte US | firm | https://www.deloitte.com/us/en/about/press-room/deloitte-announces-wins-at-2025-itr-americas-tax-awards.html | 2025-10-27 | access: full (awards cover work executed January 2024 to January 2025)
- DELOITTE-P2AGENT-2024 | Pillar Two Agent: Tech-powered compliance | Deloitte | firm | https://www.deloitte.com/global/en/services/tax/services/tech-powered-compliance.html | 2024-07-26 | access: full (page modified 2026-04-08; Deloitte's own survey figures on the page are not independent)
- DELOITTE-P2BROCH-2024 | Facilitating your Pillar Two compliance and reporting obligations (Pillar Two Agent brochure) | Deloitte | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2024/dttl-pillar-two-agent.pdf | 2024-05-15 | access: full (date from the PDF creation date; text refers to 2025 filing deadlines)
- EY-GLOBE-ENGINE-2026 | Introducing EY GloBE Engine (slipsheet) | EY | firm | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/tax/documents/ey-gl-globe-engine-slipsheet-06-2026.pdf | 2026-06 | access: full (date taken from the file name (06-2026) and a 2026 copyright; PDF modified 2026-06-11)
- EY-P2DATA-2024 | How to alleviate BEPS 2.0 Pillar Two data challenges | EY | firm | https://www.ey.com/en_gl/insights/tax/how-to-alleviate-beps-2-0-pillar-two-data-challenges | 2024-11-22 | access: full (older than 18 months; kept as a practitioner statement on AI and Pillar Two data)
- EY-WEBCAST-2026 | BEPS Pillar Two: Managing FY24 compliance (EY webcast notice for 19 February 2026) | EY | conference | https://taxnews.ey.com/news/2026-0394-thursday-february-19-beps-pillar-two-managing-fy24-compliance-1100-am-et-1600-gmt | 2026-02-09 | access: full (notice only)
- FGS-GIR-2026 | XML statt Steuerrecht: Die wahren Herausforderungen der ersten Pillar-2-Saison (German) | Flick Gocke Schaumburg | firm | https://www.fgs.de/news-and-insights/blog/detail/xml-statt-steuerrecht-die-wahren-herausforderungen-der-ersten-pillar-2-saison | 2026-08-03 | access: full (German-language source, translated by the analyst)
- FINREP-ASC740-2026 | AI Tax Provision ASC 740 Reporting: A 2026 Practitioner Walkthrough | Finrep (Gana Misra, CEO) | vendor | https://www.finrep.ai/blog/ai-tax-provision-asc-740-reporting-a-2026-practitioner-walkthrough | 2026-09-30 | access: full (vendor blog; its headline adoption statistics and its attributions to PCAOB, Deloitte, PwC, EY and the AICPA are not traceable and are excluded)
- GAMMA-JOB-2026 | Senior Tax Manager (job posting, via Accel job board) | Gamma | job-posting | https://jobs.accel.com/companies/gamma-3/jobs/88655517-senior-tax-manager | 2026-08-04 | access: full (posted 4 August 2026; no longer accepting applications)
- IFRS-IAS12-2023 | International Tax Reform - Pillar Two Model Rules (project page: amendments to IAS 12) | IFRS Foundation / IASB | standard-setter | https://www.ifrs.org/projects/completed-projects/2023/international-tax-reform-pillar-two-model-rules/ | 2023-05 | access: full (page confirms issue in May 2023 only; the amendment text was not opened)
- KOGNITOS-2026 | AI for Corporate Tax and Provision Automation (2026) | Kognitos | vendor | https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/ | 2026-06-17 | access: full
- KPMG-ANTHROPIC-2026 | KPMG Partners with Anthropic for Digital Gateway Powered by Claude | CPA Practice Advisor (reproducing the KPMG and Anthropic announcement) | press | https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/ | 2026-05-20 | access: full
- KPMG-ASU-2023 | FASB issues ASU to disaggregate income tax disclosures (Defining Issues) | KPMG US | firm | https://kpmg.com/us/en/frv/reference-library/2023/fasb-issues-asu-to-disaggregate-income-tax-disclosures.html | 2023-12 | access: full (foundation for ASU 2023-09; the FASB's own page returned 403)
- KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence (KPMG quick surveys) | KPMG AG Wirtschaftspruefungsgesellschaft (Germany) | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-07 | access: full (dateline Berlin, 7 May 2026; JSON-LD 2026-05-06; sample size not stated)
- LUCANET-2025 | Pillar Two and XML: The Digital Backbone of GloBE Reporting | Lucanet | vendor | https://www.lucanet.com/en/insights/regulatory-insights/pillar-two-and-xml-digital-backbone-globe-reporting-05-12-2025/ | 2025-12-05 | access: full
- OECD-GIR-XML | GloBE Information Return (Pillar Two) XML Schema: User Guide for Tax Administrations | OECD | regulator | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/01/globe-information-return-pillar-two-xml-schema_3980638f/c594935a-en.pdf | 2025-01 | access: full (approved by the Inclusive Framework on 30 October 2024; PDF opened from the link in a Bloomberg Tax article)
- OECD-P2-SEP-2026 | OECD Releases New Pillar Two Guidance, Updated GIR And Framework For Legislative Reviews (Loyens & Loeff; the OECD package was released 11 September 2026) | Loyens & Loeff via Mondaq | firm | https://www.mondaq.com/oecd-releases-new-pillar-two-guidance-updated-gir-and-framework-for-legislative-reviews/1842556 | 2026-09-14 | access: full
- OECD-SBS-2026 | Further details on the OECD Pillar Two 'Side-by-Side' package (KPMG UK Tax Matters Digest; the OECD package was released 5 January 2026) | KPMG UK | firm | https://kpmg.com/uk/en/insights/tax/tmd-further-details-on-the-oecd-pillar-two-side-by-side-package.html | 2026-01-22 | access: full (same URL as the landscape's OECD-SBS-2026 row)
- OECDPILLARS-GIRXML-2026 | The OECD releases June 2026 Guidance on the use of the GIR XML Schema for first GloBE filings | OECDPillars.com (independent site, not affiliated with the OECD) | press | https://oecdpillars.com/2026/06/08/ | 2026-06-08 | access: full (secondary report; the OECD document itself could not be opened)
- ORBITAX-AMG-2026 | How AMG Brought Pillar Two Compliance In-House with Orbitax (case study) | Orbitax | vendor | https://orbitax.com/newsroom/case-studies/amg-pillar-two-compliance-case-study | 2026-09-28 | access: full (page modified 2026-10-11; named customer AMG Critical Materials N.V.)
- ORBITAX-ATO-2026 | Australian CGDMTR Filing: Building a Repeatable Pillar Two Process with Direct ATO Transmission | Orbitax | vendor | https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/australia-cgdmtr-filing-ato-transmission | 2026-08-19 | access: full
- ORBITAX-DIGIPOORT-2026 | Orbitax Successfully Establishes Direct Transmission Connectivity with the Netherlands' Logius Digipoort for Pillar Two Reporting | Orbitax | vendor | https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/orbitax-successfully-establishes-direct-transmission-connectivity-with-netherlands-logius-digipoort-for-pillar-two-reporting | 2026-04-23 | access: full (test submission with sample data to a test environment)
- ORBITAX-LEAN-2026 | How a lean global tax team completed Swiss and UK Pillar Two filings ahead of deadline (case study) | Orbitax | vendor | https://orbitax.com/newsroom/case-studies/how-a-lean-global-tax-team-completed-swiss-and-uk-pillar-two-filings | 2026-08-10 | access: full (customer is not named (a Swiss-parented insurance group))
- ORBITAX-NL-2026 | Orbitax Completes First GIR Submission to the Netherlands and Expands Global Pillar Two Filing Readiness | Orbitax | vendor | https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/orbitax-completes-first-gir-submission-to-the-netherlands-and-expands-global-pillar-two-filing-readiness | 2026-06-03 | access: full (dateline 3 June 2026; page dated 4 June)
- ORBITAX-SEASON-2026 | Inside the First Pillar Two Filing Season: Trends, Challenges, and Lessons (1,700+ filings) | Orbitax | vendor | https://orbitax.com/newsroom/solutions/global-minimum-tax-gmt/inside-the-first-pillar-two-filing-season | 2026-08-20 | access: full (summary page; the full report was not opened)
- ORBITAX-XATBOT-2026 | XatBot's Latest Release: Autopilot, Deep Research, MCP Connections, and Intelligent Tax Skills | Orbitax | vendor | https://orbitax.com/newsroom/announcements/xatbots-latest-release-autopilot-deep-research-mcp-connections-and-intelligent-tax-skills | 2026-04-19 | access: full
- ORBITAX-XATBOTPRO-2026 | XatBot Pro+ now free for Orbitax GMT Users to make your June 2026 Pillar Two filing season easier | Orbitax | vendor | https://orbitax.com/newsroom/announcements/xatbot-pro-now-free-for-orbitax-gmt-users-to-make-your-june-2026-pillar-two-filing-season-easier | 2026-05-04 | access: full
- OXFORD-CBT-2026 | Oxford University Centre for Business Taxation Summer Conference booklet, 26 June 2026 | Oxford University Centre for Business Taxation | conference | https://oxfordtax.sbs.ox.ac.uk/sitefiles/cbt-summer-conference-booklet-2026 | 2026-06-26 | access: full (page footers say 2025 but the cover says 26 June 2026)
- PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting | PCAOB | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 | access: full (staff views, not Board policy; older than 18 months, kept as the main regulator statement on preparers' and auditors' GenAI use)
- SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Tax Notes State 121:189; abstract on TaxProf Blog) | Michael V. Sala / Tax Analysts (via TaxProf Blog) | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 | access: full (only the abstract and excerpt were read, not the full article)
- SAVANT-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | access: full (routed: sales and use tax and VAT, not provision)
- TEI-MIDYEAR-2026 | TEI Midyear Conference 2026 At a Glance Agenda (rev 3.2) | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03-15 | access: full (preliminary programme; dated to the conference start (15-18 March 2026))
- TR-AGENTICCORP-2025 | How agentic AI is transforming corporate tax departments | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/how-agentic-ai-is-transforming-corporate-tax-departments/ | 2025-11-11 | access: full
- TR-CORPAI-2026 | AI in corporate tax: 2026 key trends and use cases | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/ | 2026-07-01 | access: full (page modified 2026-10-16)
- TR-CORPTAX-2025 | Why most tax departments aren't using AI yet (reporting the 2025 State of the Corporate Tax Department report) | Thomson Reuters Tax & Accounting / Thomson Reuters Institute | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 | access: full (vendor-owned survey; sample size not stated on the page)
- TR-JOB-2026 | Senior Tax Product Specialist, ONESOURCE Tax Provision (job posting, via Ann Arbor USA job board) | Thomson Reuters | job-posting | https://jobs.annarborusa.org/companies/thomson-reuters/jobs/83860571-senior-tax-product-specialist | 2026-06-24 | access: full (posted 24 June 2026)
- WK-PILLAR2-2026 | BEPS Pillar Two Technology Procurement Guide | Wolters Kluwer | vendor | https://www.wolterskluwer.com/en/expert-insights/beps-pillar-two-procurement-checklist | 2026-02-16 | access: full (opened through the r.jina.ai text mirror; the checklist itself is behind a form)

## 6. Gaps

- **No AI-in-provision customers or outcomes.** I found no named company using AI in its ASC 740 provision with a published result, and no error rate, override rate, parallel-run result or independent accuracy test for any provision or Pillar Two use case.
- **No audit-side evidence.** Searches on auditors' reliance on AI-prepared provisions, tax specialists on audits and PCAOB inspection findings on income taxes returned nothing usable. PCAOB inspection reports and staff updates were not opened. The only regulator item is the July 2024 GenAI spotlight, which is not tax-specific.
- **Primary documents not reached.** OECD pages and the June 2026 GIR XML guidance were blocked or unavailable (seen via OECDPillars and law-firm summaries); the FASB's ASU page returned 403; the IAS 12 amendment text was not opened; the EY Tax and Finance Operations survey and Deloitte's Pillar Two research report were not opened (figures come from EY and Deloitte pages).
- **Seen only in search results and excluded.** PwC Finland's statement that it used its own Pillar Two Engine for the first GIRs; job postings at Toast, Workiva and Applied Materials that mention AI and ASC 740 (employer pages were not opened); a ChatFin claim that a provision cycle fell from 5-7 to 2-4 business days; a Deloitte Belgium alert and an EY OECD-toolkit alert; Taxmann and TaxBench evaluations.
- **Leads not opened.** Orbitax's "First Pillar Two Filing Report" and its other named case studies (EPAM, Columbia Sportswear, NXP Semiconductors per its page) [ORBITAX-SEASON-2026]; Bloomberg Tax's "Global Minimum Tax Filing Hiccups" (18 August 2026); Thomson Reuters' Pillar Two white paper.
- **Finrep's statistics excluded.** Its figures (67% of large corporate tax departments piloting AI in provision, 18% end-to-end, and a 29% disclosure-drafting figure attributed to an EY survey) and its attributions to a "2023 PCAOB Staff Spotlight", Deloitte, PwC, KPMG and the AICPA could not be traced and are not used. The PCAOB GenAI spotlight I found is dated July 2024.
- **Landscape item checked.** The Deloitte "Pillar Two Agent" is a real platform sold with Deloitte's tax team; Deloitte's pages do not describe it as generative or agentic AI.
- **Survey details missing.** Sample sizes are not stated for KPMG Germany's and Thomson Reuters' surveys; the 51% (Future of Professionals) and 58% (State of the Corporate Tax Department) under-resourcing figures come from different surveys.
- **Discourse.** No transcript, slide deck or recording from the TEI labs or the Bloomberg forum; the Corptax webinar is undated; no community thread (for example Reddit) on AI in provision turned up in the searches I ran. TEI's annual conference was not covered.
- **Search budget.** I used 11 web searches; the rest of the work used direct page and PDF fetches.
