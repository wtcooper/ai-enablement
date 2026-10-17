# Tax / indirect-tax: practice angle (wave 2)

- **Archetype:** tax. **Module:** indirect-tax (VAT, GST, US sales and use tax, e-invoicing and continuous transaction controls, marketplace and digital-services rules, agentic commerce, indirect-tax audits).
- **Angle:** practice. What firms, vendors and in-house teams actually do.
- **Prepared:** 2026-10-17. Method: pages opened with `curl` (text extraction, `pdftotext` for PDFs); one site (Withum) was opened only through the r.jina.ai text mirror because it blocked `curl`. Web search was used until the shared budget ran out; it ran out before the podcast and community searches (see Gaps).
- **Prerequisites:** items marked (inferred) are not stated by a source; the rest are taken from the product descriptions.
- **Reading convention:** every figure below carries its provenance in the YAML (`self-reported`, `vendor-published`, `independent`). Nothing in this file is `independent`.

## 1. Summary

- **Evidence is almost entirely vendor-published.** The module has no measured outcome from a named deploying organization, so no use case reaches grade A. Of 20 use cases, 2 are grade B, 16 are C and 2 are D (ideas). The two B entries rest on one named beta customer (Singer Equipment, quoted in an Avalara release) and one employer's job posting (Plusgrade).
- **What changed in the work between Sep 2025 and Oct 2026:** the tax-engine vendors moved from calculation plus "copilot" help to agents that classify products, validate exemption certificates, prepare returns, diagnose e-invoice errors and draft tax rules, always with an approval step before anything is filed or activated. Avalara announced Avi and a network of agents (Sep-Nov 2025) and Avalara Aviator (23-24 Sep 2026, general availability planned after CRUSH Europe). Thomson Reuters launched ONESOURCE Sales and Use Tax AI (15 Jan 2026). Sovos expanded Sovi AI (24 Mar 2026), made Compliance Network generally available (2 Jun 2026), and bought Blue dot (15 Sep 2026) and Flowie (1 Oct 2026). Vertex reports its first commercial AI product, Smart Categorization, is in production use (7 May 2026 call).
- **E-invoicing is where the volume is.** France's mandate began on 1 Sep 2026. Sovos reports a 1.6% invoice rejection rate in live production against its own estimate of about 20% market-wide. That is a platform metric the source does not attribute to AI.
- **Quality evidence is thin and unflattering to the "AI is already measured" story.** Fonoa's survey of 176 indirect-tax leaders found 92% use AI, only 12.5% have specific targets or KPIs, 57.4% would not be confident defending AI-assisted decisions to a tax authority, and only about a third run formal human-in-the-loop review. Thomson Reuters reports 65% use GenAI tools but only 26% measure ROI. No error rate, override rate or parallel-run result was found for any AI use in this module.
- **The constraint is data and people, not models.** In KPMG's May 2026 benchmarking (53 large multinationals), data quality is the top concern for 58% (44% in 2021), only 23% say their ERP is fit for purpose, about one third have no technology specialists in the indirect-tax team, and 58% expect headcount to stay largely unchanged because of AI (21% expect an increase, 21% a decrease).
- **Agentic commerce is a live open question, not a deployment.** Practitioner commentary (Bloomberg Tax, Sales Tax Institute, TaxCloud) says the operator of an agent with integrated checkout and payment handling is likely to face marketplace-facilitator or deemed-supplier treatment, and that merchants' existing tax engines still compute the tax. No vendor documentation for tax inside agent checkout was found.

## 2. Use cases

```yaml
- id: tax-indirect-tax-01
  title: Confidence-scored product-to-tax-code classification and mapping
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Mapping thousands of product SKUs to tax categories is manual, slow and inconsistent between reviewers.
    Wrong mappings produce wrong tax at transaction time and are hard to defend in an audit.
  solution: >-
    A language model proposes a tax category for each product, with a confidence score, from the product
    description and the vendor's tax content. Reviewers approve or choose another category, and the workflow
    keeps role-based access and an audit history. Vertex's tool covers US sales tax categories and says it
    accounts for sales tax holidays through its retail category tree. Thomson Reuters embeds CoCounsel in
    ONESOURCE Determination to return up to three commodity-code suggestions with confidence scores. Avalara
    lists mapping products to tax codes among the first Aviator capabilities.
  outcomes:
    - lever: speed
      description: Observed time to categorize a product fell from more than a minute and a half to a few seconds.
      figure: ">1.5 minutes to a few seconds per product"
      measures: >-
        Observed categorization time per product, as stated by Vertex's CEO for live Smart Categorization
        customers. Customers, sample size and measurement method are not given.
      provenance: vendor-published
      source_ref: VERTEX-Q1CALL-2026
    - lever: speed
      description: Thomson Reuters states that bulk classification of 100 SKUs takes about 5 minutes versus days of manual review.
      figure: "100 SKUs in 5 minutes"
      measures: >-
        Thomson Reuters's illustrative benefit statement for ONESOURCE Determination with CoCounsel; no customer,
        sample or baseline given.
      provenance: vendor-published
      source_ref: TR-CLASSIFICATION-2026
    - lever: quality
      description: none published (no accuracy, override or error rate found for AI-proposed mappings)
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: VERTEX-SMARTCAT-2026
  prerequisites:
    - Product catalogue in digital form with usable descriptions (the vendors' tools work from catalogue data uploaded or entered by the user).
    - A tax engine with a defined category tree (Vertex O Series or ONESOURCE Determination in the two named products).
    - Reviewer roles and an approval workflow with audit history.
  risks_and_guardrails:
    - Thomson Reuters says wrong codes at the mapping stage lead to wrong tax at transaction time, and that generic models can express high confidence in wrong classifications (TR-CLASSIFICATION-2026, section on the data and control problem).
    - Vertex positions AI around a deterministic tax engine that remains the system of record (VERTEX-Q1CALL-2026, prepared remarks on AI strategy).
  human_checkpoints:
    - Users review, approve or adjust AI-proposed mappings; the confidence score is used to order the review queue (VERTEX-SMARTCAT-2026, p.1-2).
    - Thomson Reuters suggests auto-processing high-confidence items (90% and above) and routing uncertain ones to specialists. This is TR's suggested workflow, not a reported practice (TR-CLASSIFICATION-2026).
  role_evolution: >-
    Thomson Reuters describes classifiers becoming reviewers who spend their time on low-confidence and
    nuanced cases (TR-CLASSIFICATION-2026). Vertex says every active customer is expected to send 100% of its
    catalogue through the tool (VERTEX-Q1CALL-2026).
  evidence_grade: C
  sources:
    - {ref: VERTEX-Q1CALL-2026, title: "Vertex (VERX) Q1 2026 Earnings Transcript", publisher: "Vertex Inc. / Motley Fool transcript", type: vendor, url: "https://finance.yahoo.com/markets/stocks/articles/vertex-verx-q1-2026-earnings-203016568.html", date: "2026-05-07", access: full, locator: "CEO prepared remarks, AI strategy section (Smart Categorization paragraphs)"}
    - {ref: VERTEX-SMARTCAT-2026, title: "Vertex Smart Categorization data sheet", publisher: "Vertex Inc.", type: vendor, url: "https://www.vertexinc.com/sites/default/files/2026-05/202604-data-sheet-vertex-smart-categorization-v3.pdf", date: "2026-04", access: full, locator: "p.1-2 (confidence score; human in the loop; sales tax holidays)"}
    - {ref: TR-CLASSIFICATION-2026, title: "How AI can rescue product classification for indirect tax teams", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/blog/how-ai-can-rescue-product-classification-for-indirect-tax-teams/", date: "2026-04-10", access: full, locator: "sections 'How it works' and 'Practical benefits'"}
    - {ref: AVALARA-AVIATOR-2026, title: "Avalara Ushers in New Era of Agentic Tax and Compliance with Avalara Aviator", publisher: "Avalara via iTWire", type: vendor, url: "https://itwire.com/guest-articles/company-news/avalara-ushers-in-new-era-of-agentic-tax-and-compliance-with-avalara-aviator", date: "2026-09-23", access: full, locator: "list of initial Aviator capabilities"}
  last_reviewed: "2026-10-17"
  notes: >-
    Maturity is in-production on the strength of Vertex's statement that customers have moved to production; the
    customers are not named, so the grade stays C. Thomson Reuters's 94/81/67% confidence figures in its blog are
    an illustration of the output format, not measured accuracy.

- id: tax-indirect-tax-02
  title: Agent-prepared sales and use tax and VAT returns with approval before filing
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Return preparation across many jurisdictions is repetitive: pull transaction data, validate it, map it to
    forms, reconcile, file. It consumes team time at every period end and leaves little room for review.
  solution: >-
    Agents ingest transaction data, apply jurisdiction rules, build the return and present it for inspection,
    editing and approval. Filing proceeds only after approval and every step is logged. Thomson Reuters markets
    this as "touchless compliance" for US sales and use tax (more than 1,200 official returns; e-filing in 33
    states plus Canada). Avalara's Returns AI invokes headless Returns APIs and files on approval. Deloitte
    describes proof-of-concept agents that gather data and populate VAT returns with review built in.
  outcomes:
    - lever: speed
      description: Thomson Reuters states routine reporting time falls by up to 65%.
      figure: "up to 65%"
      measures: >-
        Reduction in time spent on routine reporting, per TR's launch release; baseline, sample and customers
        are not stated.
      provenance: vendor-published
      source_ref: TR-SUTAI-2026
    - lever: speed
      description: Thomson Reuters states large-enterprise compliance cycles fall from 30 days to 11.
      figure: "30 days to 11 days"
      measures: >-
        Compliance cycle length for large enterprises as stated by TR; which customers or how many is not stated.
      provenance: vendor-published
      source_ref: TR-SUTAI-2026
    - lever: risk
      description: Thomson Reuters says early customers report up to a 75% reduction in audit exposure.
      figure: "up to 75%"
      measures: >-
        Reduction in audit exposure reported by early customers, per TR; the metric is not defined and customers
        are not named.
      provenance: vendor-published
      source_ref: TR-SUTAI-2026
    - lever: capacity
      description: The earlier ONESOURCE+ release gave a lower range for preparation time savings.
      figure: "40-60%"
      measures: >-
        Preparation time saved with ONESOURCE Sales and Use Tax AI per TR's 5 Nov 2025 ONESOURCE+ release; basis
        not stated. It differs from the 65% in the Jan 2026 release.
      provenance: vendor-published
      source_ref: TR-ONESOURCEPLUS-2025
  prerequisites:
    - Clean, complete transaction data reaching the tax engine (Deloitte says outcomes depend on data quality).
    - A tax engine or return platform with form and jurisdiction coverage and e-filing connections.
    - Defined review and sign-off roles (TR: final review and approval).
  risks_and_guardrails:
    - Deloitte warns that poor implementation can cause filing errors and penalties, and says its Tax Transformation Trends 2025 research found 77% of surveyed tax leaders require 90% or better accuracy before trusting AI (DELOITTE-AGENTIC-2026, section 'Mitigating risk and supporting accountability').
    - Avalara states nothing is submitted without explicit human consent and that steps are logged (AVALARA-AVI-2025, section 'Agentic workflow').
  human_checkpoints:
    - Tax professionals keep final review and sign-off before filing (TR-SUTAI-2026).
    - Return is presented for inspection, editing and approval before automatic filing (AVALARA-AVI-2025).
  role_evolution: >-
    Thomson Reuters says professionals shift from operations to advisory (TR-SUTAI-2026 subtitle). Deloitte says
    tax teams get "clearer visibility into where judgment is actually being applied" (DELOITTE-AGENTIC-2026).
  evidence_grade: C
  sources:
    - {ref: TR-SUTAI-2026, title: "Thomson Reuters Launches AI Tax Compliance Solution That Saves Time and Reduces Risk", publisher: "Thomson Reuters", type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk", date: "2026-01-15", access: full, locator: "bullets 'Reclaims time' to 'Meets deadlines'; paragraph on Touchless Compliance"}
    - {ref: TR-ONESOURCEPLUS-2025, title: "Thomson Reuters launches ONESOURCE+", publisher: "Thomson Reuters", type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-onesource-plus-the-ai-powered-intelligent-compliance-network", date: "2025-11-05", access: full, locator: "product highlights, first bullet"}
    - {ref: AVALARA-AGENTIC-2025, title: "Avalara launches 'always on, always ready' AI agents", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents", date: "2025-09-30", access: full, locator: "paragraph on Returns AI"}
    - {ref: AVALARA-AVI-2025, title: "Avalara launches Avi AI agents for secure automated tax compliance", publisher: "IT Brief UK", type: press, url: "https://itbrief.co.uk/story/avalara-launches-avi-ai-agents-for-secure-automated-tax-compliance", date: "2025-11-04", access: full, locator: "sections 'Functions and agent network' and 'Agentic workflow'"}
    - {ref: AVALARA-AGENTIC-2025b, title: "Avalara Launches Agentic Tax and Compliance: AI Agents That Work for You", publisher: "Avalara via iTWire", type: vendor, url: "https://itwire.com/business-it-news/data/avalara-launches-agentic-tax-and-compliance-ai-agents-that-work-for-you", date: "2025-10-01", access: full, locator: "section 'Have Your Agent Call Our Agent' (VAT returns in Europe)"}
    - {ref: DELOITTE-AGENTIC-2026, title: "Agentic AI and indirect tax: a practical view for tax directors", publisher: "Deloitte Global", type: firm, url: "https://www.deloitte.com/global/en/services/tax/perspectives/agentic-ai-and-indirect-tax-practical-view-for-tax-directors.html", date: "2026-07-01", access: full, locator: "section 2 'Filing'; section 'Mitigating risk and supporting accountability'"}
  last_reviewed: "2026-10-17"
  notes: >-
    Maturity is piloting because the public evidence is early-access programmes (Avalara), proof-of-concept work
    (Deloitte) and unnamed early customers (Thomson Reuters), even though TR says its product is available now.
    Avalara's Returns AI also covers European VAT returns per its Oct 2025 release (AVALARA-AGENTIC-2025b, section 'Have Your Agent Call Our Agent'); no customer evidence found. TR figures disagree between releases (40-60% vs up to 65%).

- id: tax-indirect-tax-03
  title: Full-population exemption and resale certificate validation
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Exemption and resale certificates are collected, stored and checked by hand, so invalid or expired
    certificates stay undiscovered until an audit.
  solution: >-
    Document intelligence extracts and validates certificate data at scale. Avalara describes exemption agents
    that cross-check certificates against authoritative registries to keep records accurate, and lists
    certificate validation among Aviator's first capabilities. Numeral says that when customers move their
    existing certificates onto its platform it validates them and often finds a large share fail.
  outcomes:
    - lever: quality
      description: Numeral reports that many certificates moved onto its platform fail validation.
      figure: "30% to 40%"
      measures: >-
        Share of customers' existing exemption certificates that fail validation when moved onto Numeral's
        platform, per Numeral ("often finds"); number of customers and certificates not given.
      provenance: vendor-published
      source_ref: NUMERAL-2026
    - lever: capacity
      description: Numeral says its certificate management offering can save up to 400 hours a year per company.
      figure: "up to 400 hours each year"
      measures: >-
        Hours saved per company per year by Numeral's exemption certificate management offering, per Numeral;
        basis not given.
      provenance: vendor-published
      source_ref: NUMERAL-2026
  prerequisites:
    - Existing certificates digitised or uploadable (inferred).
    - Access to registries or validation sources for the jurisdictions in scope (Avalara names authoritative registries; the rest is inferred).
    - A link between each customer and its certificate in the billing or tax engine (inferred).
  risks_and_guardrails:
    - Certificates that fail validation indicate compliance issues that may not have been identified before (NUMERAL-2026), so findings need a remediation process, not just a report.
    - Avalara says its agents run within its security perimeter and keep checkpoints for human review (AVALARA-AVI-2025).
  human_checkpoints:
    - Not described in detail for certificate validation in the sources; Avalara states human review and approval checkpoints exist at every stage of its agent platform (AVALARA-AVI-2025).
  role_evolution: >-
    Not described beyond Avalara's general statement that agents handle scanning and cross-verification while
    people keep decisions (AVALARA-AVI-2025).
  evidence_grade: C
  sources:
    - {ref: NUMERAL-2026, title: "Numeral Raises $100 Million Series C to Expand AI-Powered Tax Compliance Across Industries", publisher: "Numeral", type: vendor, url: "https://www.numeralhq.com/blog/series-c", date: "2026-09-23", access: full, locator: "paragraph beginning 'Customers using Numeral can reduce...'"}
    - {ref: AVALARA-AVI-2025, title: "Avalara launches Avi AI agents for secure automated tax compliance", publisher: "IT Brief UK", type: press, url: "https://itbrief.co.uk/story/avalara-launches-avi-ai-agents-for-secure-automated-tax-compliance", date: "2025-11-04", access: full, locator: "section 'Functions and agent network', exemption agents"}
    - {ref: AVALARA-AVIATOR-2026, title: "Avalara Ushers in New Era of Agentic Tax and Compliance with Avalara Aviator", publisher: "Avalara via iTWire", type: vendor, url: "https://itwire.com/guest-articles/company-news/avalara-ushers-in-new-era-of-agentic-tax-and-compliance-with-avalara-aviator", date: "2026-09-23", access: full, locator: "capability list"}
    - {ref: TR-INSTITUTE-2025, title: "AI and the indirect tax department: From compliance to strategy", publisher: "Thomson Reuters Institute", type: vendor, url: "https://www.thomsonreuters.com/en/institute/articles/ai-indirect-tax", date: "2025-09-17", access: full, locator: "section 'The force multiplier' (document intelligence)"}
  last_reviewed: "2026-10-17"
  notes: >-
    Customers are not named. Numeral's two figures are marketing numbers inside a funding release.

- id: tax-indirect-tax-04
  title: In-platform taxability research and Q&A assistant
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >-
    Indirect-tax staff spend time finding and interpreting taxability and regulatory answers across jurisdictions
    and languages, and checking how a product's own documentation applies.
  solution: >-
    Assistants built into tax platforms answer questions in the flow of work. Ask Sovi answers regulatory
    questions across 150+ countries and languages from a knowledge base maintained by Sovos specialists. Avalara
    Aviator explains taxability in plain language and supports research; its beta included Singer Equipment.
    Vertex Copilot answers questions from product documentation and release notes.
  outcomes:
    - lever: quality
      description: >-
        A named beta customer (Singer Equipment Company) says Aviator explains taxability in plain language,
        surfaces considerations she might have missed and provides research she can rely on. No measurement published.
      figure: none published
      measures: not applicable; a single customer quotation
      provenance: vendor-published
      source_ref: AVALARA-AVIATOR-2026
  prerequisites:
    - A vendor knowledge base maintained by tax specialists.
    - Context on the customer's entities and registrations if answers are to be business-specific (Sovos says Sovi uses entity structures, registrations and filing history).
  risks_and_guardrails:
    - Fonoa argues general AI can give fluent but wrong answers on recent tax changes, and that every answer should carry its primary source (FONOA-CITATION-2026). This is a vendor's argument for its own product.
    - Sovos says customer data stays inside its security perimeter and is not used to train external models (SOVOS-SOVI-2026).
  human_checkpoints:
    - Sovos plans to extend answers into guided, human-approved actions; today's capability is Q&A (SOVOS-SOVI-2026, Ask Sovi paragraph).
  role_evolution: >-
    The Singer Equipment tax accountant describes using the tool to think about questions she had not asked,
    which she links to audit readiness (AVALARA-AVIATOR-2026).
  evidence_grade: B
  sources:
    - {ref: AVALARA-AVIATOR-2026, title: "Avalara Ushers in New Era of Agentic Tax and Compliance with Avalara Aviator", publisher: "Avalara via iTWire", type: vendor, url: "https://itwire.com/guest-articles/company-news/avalara-ushers-in-new-era-of-agentic-tax-and-compliance-with-avalara-aviator", date: "2026-09-23", access: full, locator: "quotation from Preya Chandan, Senior Tax Accountant, Singer Equipment Company"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "paragraphs on Ask Sovi and security perimeter"}
    - {ref: VERTEX-COPILOT-2025, title: "AI and the Customer Experience: How Vertex Copilot is Shaping the Future", publisher: "Vertex Inc.", type: vendor, url: "https://www.vertexinc.com/node/7552", date: "2025-05-06", access: full, locator: "section 'Vertex's latest AI-powered solution'"}
    - {ref: FONOA-CITATION-2026, title: "Why Primary Source Citation Matters for Tax Audit Defense", publisher: "Fonoa", type: vendor, url: "https://www.fonoa.com/resources/blog/primary-source-tax-law-citation-audit", date: "2026-09-21", access: full, locator: "section 'Why general AI can't be trusted for tax research'"}
  last_reviewed: "2026-10-17"
  notes: >-
    Grade B rests on one named beta customer and no published measurement. Aviator general availability is
    stated as following "next month's" CRUSH Europe event (release dated 23-24 Sep 2026), so GA had not been
    confirmed when this was written.

- id: tax-indirect-tax-05
  title: Plain-language tax rule drafting with simulation on historical transactions
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [software-systems, expert-judgment]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Configuring custom tax rules and mappings in a tax engine needs specialist knowledge of the product and the
    law, and changes can conflict with other rules.
  solution: >-
    The user describes a needed rule in plain language. Avalara's agent drafts the rule, simulates its impact on
    past transactions and flags conflicts with other rules; the customer reviews and approves before it is
    activated. Vertex reports a technical customer used its AI copilot in a question-and-answer exchange to
    configure the product successfully.
  outcomes:
    - lever: speed
      description: Avalara claims Aviator turns days of manual compliance work into minutes of oversight.
      figure: "days to minutes (qualitative)"
      measures: >-
        Avalara's general claim for the Aviator agent hub, not specific to rule drafting; no baseline or sample.
      provenance: vendor-published
      source_ref: AVALARA-AVIATOR-2026
  prerequisites:
    - Historical transaction data in the engine to simulate against.
    - Role-based approval for tax-logic changes (TR Institute advice).
  risks_and_guardrails:
    - Thomson Reuters Institute advises segregation of duties and approval workflows for changes to tax logic, and versioned prompts and outputs (TR-INSTITUTE-2025, last section on controls). This is vendor-institute advice, not a reported practice.
  human_checkpoints:
    - Customer reviews and approves the drafted rule before the agent activates it (AVALARA-AVIATOR-2026).
  role_evolution: >-
    Not described. Vertex says it sees room to simplify how customers configure tax rules and manage data updates (VERTEX-Q1CALL-2026, analyst Q&A).
  evidence_grade: C
  sources:
    - {ref: AVALARA-AVIATOR-2026, title: "Avalara Ushers in New Era of Agentic Tax and Compliance with Avalara Aviator", publisher: "Avalara via iTWire", type: vendor, url: "https://itwire.com/guest-articles/company-news/avalara-ushers-in-new-era-of-agentic-tax-and-compliance-with-avalara-aviator", date: "2026-09-23", access: full, locator: "paragraph beginning 'For example, a customer can describe a needed tax rule...'"}
    - {ref: VERTEX-Q1CALL-2026, title: "Vertex (VERX) Q1 2026 Earnings Transcript", publisher: "Vertex Inc. / Motley Fool transcript", type: vendor, url: "https://finance.yahoo.com/markets/stocks/articles/vertex-verx-q1-2026-earnings-203016568.html", date: "2026-05-07", access: full, locator: "analyst Q&A, answer on customer experience and copilot"}
    - {ref: TR-INSTITUTE-2025, title: "AI and the indirect tax department: From compliance to strategy", publisher: "Thomson Reuters Institute", type: vendor, url: "https://www.thomsonreuters.com/en/institute/articles/ai-indirect-tax", date: "2025-09-17", access: full, locator: "final controls paragraph"}
  last_reviewed: "2026-10-17"
  notes: Avalara's example is a described design; the release names no customer who used rule drafting.

- id: tax-indirect-tax-06
  title: E-invoice rejection diagnosis and approved remediation
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [transaction-processing, software-systems]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Under continuous transaction controls an invoice must clear a government platform before goods move or
    payment is triggered, so teams need to know why an invoice failed and which upstream process caused it.
    Today this runs through support tickets and handoffs.
  solution: >-
    Sovi AI diagnoses root causes of e-invoice and filing errors, proposes specific fixes and executes
    corrections once a Sovos user approves, with every recommendation and action logged. Sovos says the Blue dot
    acquisition adds AI it intends to embed so diagnosis explains why the underlying business event was wrong
    and what to change upstream.
  outcomes:
    - lever: quality
      description: >-
        Sovos reports a 1.6% invoice rejection rate in live French production against an estimated 20% market-wide.
        The source does not attribute this to AI diagnosis.
      figure: "1.6% vs about 20%"
      measures: >-
        Invoice rejection rate in live production in France three weeks after the 1 Sep 2026 mandate, as stated by
        Sovos; the 20% market figure is Sovos's own estimate; the denominator and period are not given.
      provenance: vendor-published
      source_ref: SOVOS-FRANCE-2026b
  prerequisites:
    - Certified connection to the government platform or accredited platform, and format validation (inferred from Sovos's PA status and format-validation remarks).
    - Access to the upstream transaction data and master data that cause errors (stated as the goal in the Blue dot release).
  risks_and_guardrails:
    - Sovos says the AI is built within its security perimeter, customer data is not used to train external models, and workflows are designed with human oversight and auditability (SOVOS-SOVI-2026).
    - Sovos describes French penalties for late submission beginning at 10% of VAT due, rising to 40% for repeat non-compliance and up to 80% for fraud, and per-invoice penalties capped at 25% (SOVOS-FRANCE-2026). This is the vendor's summary of the law.
  human_checkpoints:
    - Corrections are executed once approved by Sovos users (SOVOS-SOVI-2026, 'Problem-to-Resolution Guidance').
  role_evolution: >-
    Sovos says the intent is resolution without support tickets or handoffs (SOVOS-SOVI-2026).
  evidence_grade: C
  sources:
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "capability list, 'Problem-to-Resolution Guidance'"}
    - {ref: SOVOS-CN-2026, title: "Sovos Launches Compliance Network", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-launches-compliance-network-to-address-unprecedented-wave-of-global-e-invoicing-mandates/", date: "2026-06-02", access: full, locator: "paragraph on PA status and Sovi AI error diagnosis"}
    - {ref: SOVOS-BLUEDOT-2026, title: "Sovos Acquires Blue dot", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-acquires-blue-dot-expanding-ai-native-diagnostics-workflow-and-intelligence-capabilities-widening-sovos-tax-compliance-platform-technology-lead/", date: "2026-09-15", access: full, locator: "sections 'The Compliance Problem Getting Harder to Ignore' and 'Accelerating AI Across the Sovos Platform'"}
    - {ref: SOVOS-FRANCE-2026b, title: "Three Weeks into France E-Invoicing Mandate: Sovos Hits Unparalleled Production Scale", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/three-weeks-into-france-e-invoicing-mandate-sovos-hits-unparalleled-production-scale/", date: "2026-09-23", access: full, locator: "section 'Quality at Scale'"}
    - {ref: SOVOS-FRANCE-2026, title: "Sovos Brings Global 2000 Clients Live in France", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-brings-global-2000-clients-live-in-france-ahead-of-the-worlds-most-complex-e-invoicing-mandate/", date: "2026-08-18", access: full, locator: "paragraph on penalties"}
  last_reviewed: "2026-10-17"
  notes: >-
    Sovos's own transaction volume differs between releases: "nearly 20 billion transactions per year" (24 Mar 2026)
    and "more than 70 billion" (18 Aug and 23 Sep 2026). Treat vendor scale figures as unreconciled.

- id: tax-indirect-tax-07
  title: Continuous regulatory-change monitoring with cited primary sources
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [research-synthesis]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Indirect-tax rules change in many jurisdictions and languages. Fonoa says more than 70 countries have added
    or changed e-invoicing rules since 2020. Monitoring relies on one person watching a few countries, advisor
    digests and forwarded newsletters, so changes surface at filing time.
  solution: >-
    Central monitoring filtered to the company's jurisdictions and tax types, with every alert linked to the
    primary source and a confidence score so only high-confidence changes surface and proposals are labelled as
    such (Fonoa Knowledge). Sovos describes regulatory intelligence that assesses how rule changes affect each
    customer's configuration. Avalara's research agents summarise primary sources with citations. Thomson Reuters
    Institute describes horizon scanning and impact assessments that map rule changes to products and systems.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: FONOA-MONITORING-2026
  prerequisites:
    - A profile of the entities, jurisdictions and tax types in scope (Fonoa: monitoring filtered to the company's profile).
    - Access to primary legal sources (gazettes, directives) in their languages (Fonoa).
  risks_and_guardrails:
    - Fonoa says summaries are a reading of the law, not the law, and cannot be relied on alone in an audit (FONOA-CITATION-2026).
    - Fonoa reports a confidence score on each alert and says uncertainty is disclosed (FONOA-CITATION-2026). No accuracy of those scores is published.
  human_checkpoints:
    - Tax team decides whether a surfaced change matters to the business; Fonoa's description stops at alerts (FONOA-MONITORING-2026).
  role_evolution: >-
    Fonoa says coverage stops depending on headcount (FONOA-MONITORING-2026, section 'How leading tax teams monitor regulatory change differently').
  evidence_grade: C
  sources:
    - {ref: FONOA-MONITORING-2026, title: "Why Manual Indirect Tax Regulatory Change Monitoring No Longer Scales", publisher: "Fonoa", type: vendor, url: "https://www.fonoa.com/resources/blog/indirect-tax-regulatory-change-monitoring", date: "2026-09-16", access: full, locator: "sections 'Why are indirect tax regulations increasing so quickly?' to 'How Fonoa Knowledge helps'"}
    - {ref: FONOA-CITATION-2026, title: "Why Primary Source Citation Matters for Tax Audit Defense", publisher: "Fonoa", type: vendor, url: "https://www.fonoa.com/resources/blog/primary-source-tax-law-citation-audit", date: "2026-09-21", access: full, locator: "section 'Start with the primary source, then add the interpretation'"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "'Regulatory Intelligence' bullet"}
    - {ref: AVALARA-AVI-2025, title: "Avalara launches Avi AI agents for secure automated tax compliance", publisher: "IT Brief UK", type: press, url: "https://itbrief.co.uk/story/avalara-launches-avi-ai-agents-for-secure-automated-tax-compliance", date: "2025-11-04", access: full, locator: "research agents"}
    - {ref: TR-INSTITUTE-2025, title: "AI and the indirect tax department: From compliance to strategy", publisher: "Thomson Reuters Institute", type: vendor, url: "https://www.thomsonreuters.com/en/institute/articles/ai-indirect-tax", date: "2025-09-17", access: full, locator: "section 'Taking the first steps' (horizon scanning)"}
  last_reviewed: "2026-10-17"
  notes: No customer, usage or accuracy data found for any of these monitoring products.

- id: tax-indirect-tax-08
  title: AI extraction and enrichment of T&E and AP data for VAT recovery
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing, data-reporting]
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Input VAT on travel, expense and payables transactions is lost because receipts and invoices are fragmented
    and not validated or enriched with tax context.
  solution: >-
    Blue dot's platform extracts, cleanses, validates, enriches and contextualises invoice, receipt and expense
    data so eligible VAT can be identified and recovered. Sovos bought the company on 15 Sep 2026 and intends to
    embed its models in the compliance flow and to reconcile structured B2B invoices with employee expenses and
    card transactions to avoid duplicate or inconsistent VAT reporting.
  outcomes:
    - lever: quality
      description: Sovos states Blue dot has demonstrated high accuracy across VAT and taxable employee benefits lifecycles.
      figure: ">98%"
      measures: >-
        Accuracy "across VAT and taxable employee benefits lifecycles" as stated by Sovos about Blue dot; the metric
        definition, sample and period are not given.
      provenance: vendor-published
      source_ref: SOVOS-BLUEDOT-2026
  prerequisites:
    - Access to T&E and AP source systems (Blue dot is an SAP Concur Endorsed App).
  risks_and_guardrails:
    - Integration into Sovos is stated as intent ("intends to embed"); nothing about the combined product is in production per the release.
  human_checkpoints:
    - Not described in the release.
  role_evolution: Not described.
  evidence_grade: C
  sources:
    - {ref: SOVOS-BLUEDOT-2026, title: "Sovos Acquires Blue dot", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-acquires-blue-dot-expanding-ai-native-diagnostics-workflow-and-intelligence-capabilities-widening-sovos-tax-compliance-platform-technology-lead/", date: "2026-09-15", access: full, locator: "paragraphs 'Expanding the Tax Compliance Platform into VAT Recovery' and 'Accelerating AI Across the Sovos Platform'"}
  last_reviewed: "2026-10-17"
  notes: >-
    Sovos says Blue dot serves hundreds of enterprise customers across banking and finance, consumer goods, retail
    and manufacturing; none are named. Single-source entry.

- id: tax-indirect-tax-09
  title: Pre-filing anomaly and variance detection on indirect-tax data
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Misapplied rates, address mismatches and unusual swings in tax amounts are found at return time or after the
    authority asks, when correction is most expensive.
  solution: >-
    Machine-learning anomaly detection flags outliers in tax data before filing and routes exceptions to
    reviewers (Thomson Reuters Institute gives the example of Pennsylvania sales tax jumping from about $3,000 to
    $10,000 in a month). Sovos lists proactive issue detection that surfaces compliance problems before filing
    deadlines.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: TR-BUSINESSCASE-2026
  prerequisites:
    - Consolidated tax data across entities and periods (inferred).
  risks_and_guardrails:
    - Thomson Reuters Institute recommends regular sampling of AI decisions with documented findings (TR-INSTITUTE-2025, controls paragraph). The example in TR-BUSINESSCASE-2026 is illustrative.
  human_checkpoints:
    - Flagged items go to review (TR-BUSINESSCASE-2026, section 'The AI revolution in indirect tax processes').
  role_evolution: Not described beyond general "shift from processing to advisory" language (TR-INSTITUTE-2025).
  evidence_grade: C
  sources:
    - {ref: TR-BUSINESSCASE-2026, title: "How to build a business case for indirect tax process automation", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/blog/how-to-build-a-business-case-for-indirect-tax-process-automation/", date: "2026-02-05", access: full, locator: "section 'The AI revolution in indirect tax processes', predictive analytics bullet"}
    - {ref: TR-INSTITUTE-2025, title: "AI and the indirect tax department: From compliance to strategy", publisher: "Thomson Reuters Institute", type: vendor, url: "https://www.thomsonreuters.com/en/institute/articles/ai-indirect-tax", date: "2025-09-17", access: full, locator: "section 'The force multiplier'"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "'Proactive Issue Detection' bullet"}
  last_reviewed: "2026-10-17"
  notes: The sources describe capabilities. No deployment or detection rate found.

- id: tax-indirect-tax-10
  title: Data validation and enrichment at the point of entry (master data, AR/AP, determination)
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [data-reporting, software-systems]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: >-
    Most indirect-tax errors start upstream (missing fields, inconsistent configuration, timing differences) and
    surface later as reconciliations, adjustments or audit questions. In KPMG's survey 61% correct data quality
    predominantly manually.
  solution: >-
    Agents positioned near master-data setup, AR/AP flows or tax determination extract, enrich and validate data
    as transactions occur, instead of at month end or return time. Deloitte describes proof-of-concept work in
    VAT and says this is where outcomes depend on data quality. In KPMG's survey, about 49% of respondents said
    their primary AI use case will be improving data quality.
  outcomes:
    - lever: quality
      description: none published for the AI use itself
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: DELOITTE-AGENTIC-2026
  prerequisites:
    - Access to ERP and billing master data and transaction flows.
    - Upskilling tax staff in basic data management (Deloitte).
    - Technology specialists in the team (about one third of KPMG respondents have none).
  risks_and_guardrails:
    - Only 23% of KPMG respondents think their ERP is fit for purpose, which limits what AI can do on fragmented data (KPMG-INDIRECT-2026, p.6).
  human_checkpoints:
    - Deloitte says AI surfaces results for human review where judgment is required (DELOITTE-AGENTIC-2026, 'What Agentic AI potentially changes').
  role_evolution: >-
    KPMG's foreword expects indirect-tax professionals to become data managers and gatekeepers to ERP changes
    (KPMG-INDIRECT-2026, p.2). Respondents see AI as a tool to improve data quality, not to reduce workforce size (p.5).
  evidence_grade: C
  sources:
    - {ref: DELOITTE-AGENTIC-2026, title: "Agentic AI and indirect tax: a practical view for tax directors", publisher: "Deloitte Global", type: firm, url: "https://www.deloitte.com/global/en/services/tax/perspectives/agentic-ai-and-indirect-tax-practical-view-for-tax-directors.html", date: "2026-07-01", access: full, locator: "section 1 'Data: Reducing rework and late surprises'"}
    - {ref: KPMG-INDIRECT-2026, title: "Benchmarking Indirect Tax in a data-driven era (2026 KPMG Indirect Tax Benchmarking Survey)", publisher: "KPMG International", type: survey, url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf", date: "2026-05", access: full, locator: "p.2, p.5, p.6, p.7, p.15"}
  last_reviewed: "2026-10-17"
  notes: >-
    The KPMG figure is stated intent in a survey of 53 large multinationals, not a measured deployment, so it
    supports the problem statement rather than an outcome.

- id: tax-indirect-tax-11
  title: Nexus monitoring and registration preparation agents
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [transaction-processing, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Companies cross economic-nexus thresholds, or begin selling into new countries, without registering in time.
    Registration is a paper-heavy, multi-authority process.
  solution: >-
    Avalara registration agents prepare and file registration documents with authorities and track the process
    through to storage of the signed documents. Numeral supports nexus monitoring and registrations alongside
    calculation and filing. Deloitte describes an agent that flags activity patterns relevant to registration when
    a business starts selling into a new jurisdiction, for tax professionals to consider.
  outcomes:
    - lever: speed
      description: Numeral states customers can reduce time on filings and registrations by up to 80%.
      figure: "up to 80%"
      measures: >-
        Reduction in time spent on tax filings and registrations, per Numeral; baseline, sample and customers not given.
      provenance: vendor-published
      source_ref: NUMERAL-2026
  prerequisites:
    - Sales and transaction data by state or country, current enough to track thresholds (inferred).
    - Authority integrations or the vendor's filing channels (inferred).
  risks_and_guardrails:
    - TaxCloud notes a few stray orders from a new channel can push a seller past a state's nexus threshold (TAXCLOUD-2025, section 'AI is simply the next test'), which is the risk this use case addresses.
  human_checkpoints:
    - Avalara states human review and approval checkpoints at every stage (AVALARA-AVI-2025).
  role_evolution: >-
    Deloitte describes tax teams engaging earlier in business decisions (DELOITTE-AGENTIC-2026, section 3).
  evidence_grade: C
  sources:
    - {ref: AVALARA-AVI-2025, title: "Avalara launches Avi AI agents for secure automated tax compliance", publisher: "IT Brief UK", type: press, url: "https://itbrief.co.uk/story/avalara-launches-avi-ai-agents-for-secure-automated-tax-compliance", date: "2025-11-04", access: full, locator: "registration agents; early access programmes"}
    - {ref: NUMERAL-2026, title: "Numeral Raises $100 Million Series C", publisher: "Numeral", type: vendor, url: "https://www.numeralhq.com/blog/series-c", date: "2026-09-23", access: full, locator: "paragraphs on the compliance lifecycle and claimed savings"}
    - {ref: DELOITTE-AGENTIC-2026, title: "Agentic AI and indirect tax: a practical view for tax directors", publisher: "Deloitte Global", type: firm, url: "https://www.deloitte.com/global/en/services/tax/perspectives/agentic-ai-and-indirect-tax-practical-view-for-tax-directors.html", date: "2026-07-01", access: full, locator: "section 3 'Capacity', illustrative examples"}
    - {ref: TAXCLOUD-2025, title: "Agentic commerce is expanding ecommerce and your tax risk", publisher: "TaxCloud", type: vendor, url: "https://taxcloud.com/blog/agentic-commerce-is-expanding-ecommerce/", date: "2025-10-29", access: full, locator: "section 'AI is simply the next test for commerce and compliance'"}
  last_reviewed: "2026-10-17"
  notes: >-
    Avalara said early access programmes were under way with select enterprise partners in Nov 2025; no
    registration outcome was published. TaxCloud was read through the r.jina.ai mirror.

- id: tax-indirect-tax-12
  title: Tax-authority notice intake, classification and routing
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [transaction-processing, coordination-scheduling]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Tax authority notices arrive in many forms and jurisdictions and must be received, classified, routed and
    tracked to deadlines.
  solution: >-
    Avalara describes notice-management agents that automate receipt, classification, routing and tracking of
    tax authority notices across jurisdictions, within its agent network.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: AVALARA-AVI-2025
  prerequisites:
    - Notices received in a channel the agent can read (inferred).
  risks_and_guardrails:
    - Avalara says agents run inside its existing security perimeter with audit trails (AVALARA-AVI-2025).
  human_checkpoints:
    - Avalara states human checkpoints for review and approval are integrated at every stage (AVALARA-AVI-2025). Specific notice-response checkpoints are not described.
  role_evolution: Not described.
  evidence_grade: C
  sources:
    - {ref: AVALARA-AVI-2025, title: "Avalara launches Avi AI agents for secure automated tax compliance", publisher: "IT Brief UK", type: press, url: "https://itbrief.co.uk/story/avalara-launches-avi-ai-agents-for-secure-automated-tax-compliance", date: "2025-11-04", access: full, locator: "section 'Functions and agent network', notice management agents"}
  last_reviewed: "2026-10-17"
  notes: Single-source entry describing a product component; no customer or measurement found.

- id: tax-indirect-tax-13
  title: Continuous audit trail and evidence retrieval for indirect-tax audits
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Audit support pulls experienced people off day-to-day work, and documentation is reconstructed under time
    pressure. In Fonoa's survey 57.4% would not be confident defending AI-assisted decisions to a tax authority.
  solution: >-
    Agents log actions, data sources and rationale as work happens, then retrieve, assess and summarise invoices,
    contracts or customs records when documents are requested (Deloitte's description). Sovos documents every
    recommendation, approval and action. Fonoa says its Audit product assembles every determination, override and
    approval trail on demand. Thomson Reuters says its sales and use tax product keeps audit trails for each
    automated decision.
  outcomes:
    - lever: risk
      description: none published for this use case
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: FONOA-2026
  prerequisites:
    - Actions and decisions captured in the workflow at the time they occur (Deloitte).
    - Access to invoices, contracts and customs records (Deloitte).
  risks_and_guardrails:
    - Fonoa's survey found the strongest predictor of audit confidence was whether a defined process sat behind the output, not the tool; only about a third run formal human-in-the-loop review (FONOA-2026, section 'Why AI governance matters more than the AI model you choose').
    - A BDO indirect-tax partner is quoted: you are not defending a technology, you are demonstrating a process (FONOA-2026).
  human_checkpoints:
    - Tax professionals answer the authority; agents prepare the documentation (DELOITTE-AGENTIC-2026, section 4).
  role_evolution: >-
    Deloitte expects less reliance on institutional memory when questions arise (DELOITTE-AGENTIC-2026, section 4).
  evidence_grade: C
  sources:
    - {ref: DELOITTE-AGENTIC-2026, title: "Agentic AI and indirect tax: a practical view for tax directors", publisher: "Deloitte Global", type: firm, url: "https://www.deloitte.com/global/en/services/tax/perspectives/agentic-ai-and-indirect-tax-practical-view-for-tax-directors.html", date: "2026-07-01", access: full, locator: "section 4 'Tax audit readiness'"}
    - {ref: FONOA-2026, title: "State of Indirect Tax in the AI Era 2026", publisher: "Fonoa", type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: "2026-06-17", access: full, locator: "survey sections on defending AI decisions and validating AI outputs; 'How Fonoa Intelligence helps'"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "'Full Audit Transparency' bullet"}
    - {ref: TR-SUTAI-2026, title: "Thomson Reuters Launches AI Tax Compliance Solution", publisher: "Thomson Reuters", type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk", date: "2026-01-15", access: full, locator: "bullet 'Answers auditor questions instantly'"}
    - {ref: OPENAI-JOB-2026, title: "Indirect Tax Technology Manager (OpenAI)", publisher: "Stripes job board (OpenAI posting)", type: job-posting, url: "https://jobs.stripes.co/companies/openai/jobs/78936040-indirect-tax-technology-manager", date: "2026-05-15", access: full, locator: "responsibilities: 'Support indirect tax audits by assisting with transaction-level data gathering, reconciliations, and system documentation'"}
  last_reviewed: "2026-10-17"
  notes: >-
    The OpenAI posting shows the current human baseline for audit data gathering in one in-house team; it does
    not mention AI doing that work. Fonoa survey details (176 respondents) come from the public landing page; the full report is gated.

- id: tax-indirect-tax-14
  title: AI-native onboarding, data mapping and invoice data extraction for e-invoicing in Latin America
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Real-time e-invoicing regimes (the source cites Latin America) need onboarding, data mapping, invoice data
    extraction and product classification done accurately and with audit evidence.
  solution: >-
    Vertex bought Brinta in Q1 2026, described as an AI-first compliance and e-invoicing start-up whose offerings
    target onboarding and data mapping, invoice data extraction and product classification. Avalara describes
    a connector that digitises invoices from Microsoft Outlook and e-invoicing agents that connect invoices to
    government portals for validation.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: VERTEX-Q1CALL-2026
  prerequisites:
    - Local clearance connectivity and certification (inferred).
  risks_and_guardrails:
    - Vertex says in regions like Latin America accuracy, auditability and regulatory evidence are non-negotiable (VERTEX-Q1CALL-2026, CEO remarks on Brinta).
  human_checkpoints:
    - Not described.
  role_evolution: Not described.
  evidence_grade: C
  sources:
    - {ref: VERTEX-Q1CALL-2026, title: "Vertex (VERX) Q1 2026 Earnings Transcript", publisher: "Vertex Inc. / Motley Fool transcript", type: vendor, url: "https://finance.yahoo.com/markets/stocks/articles/vertex-verx-q1-2026-earnings-203016568.html", date: "2026-05-07", access: full, locator: "CEO remarks on the Brinta acquisition"}
    - {ref: AVALARA-AVI-2025, title: "Avalara launches Avi AI agents for secure automated tax compliance", publisher: "IT Brief UK", type: press, url: "https://itbrief.co.uk/story/avalara-launches-avi-ai-agents-for-secure-automated-tax-compliance", date: "2025-11-04", access: full, locator: "e-invoicing agents; section on Avi interfaces (Outlook)"}
  last_reviewed: "2026-10-17"
  notes: Acquisition and product description only; no deployment or customer evidence found.

- id: tax-indirect-tax-15
  title: Tax engines exposed to customers' own agents through MCP, A2A and APIs
  archetype: tax
  module: indirect-tax
  function: technology-it
  work_types: [software-systems]
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Tax calculation, classification, registration and filing are reached through applications and screens, which
    does not fit customers whose ERP, e-commerce or finance agents need to call compliance services directly.
  solution: >-
    Vendors expose compliance functions as agent-callable tools. Avalara's October 2025 release describes MCP
    servers and a "have your agent call our agent" model for validating taxes, classifying products, initiating
    registrations or filing forms, and hosted a developer event on agent-based architectures (26 Mar 2026). Sovos
    is developing an MCP Gateway for governed agent access and expects over time to support A2A orchestration.
    Taxually presented APIs for working with clients' internal AI ecosystems. Vertex says it is building agents
    on ERPs, with one announced for Microsoft.
  outcomes:
    - lever: growth
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: AVALARA-AGENTIC-2025b
  prerequisites:
    - Authentication, data isolation and audit logging for external agent calls.
    - Customer-side agent platforms (ERP, POS, e-commerce, productivity tools).
  risks_and_guardrails:
    - Sovos describes the MCP Gateway as providing standardised, governed access, and says capabilities are "expected" to support A2A over time, so interoperability is a plan, not a current capability (SOVOS-SOVI-2026, paragraph on the MCP Gateway).
  human_checkpoints:
    - Avalara says agents notify a human for novel situations or decisions that affect the compliance footprint (AVALARA-AGENTIC-2025).
  role_evolution: >-
    Sovos describes compliance consumed "not only through applications, but through trusted, interoperable
    agents" (SOVOS-SOVI-2026).
  evidence_grade: C
  sources:
    - {ref: AVALARA-AGENTIC-2025b, title: "Avalara Launches Agentic Tax and Compliance: AI Agents That Work for You", publisher: "Avalara via iTWire", type: vendor, url: "https://itwire.com/business-it-news/data/avalara-launches-agentic-tax-and-compliance-ai-agents-that-work-for-you", date: "2025-10-01", access: full, locator: "sections 'Have Your Agent Call Our Agent' and 'Agentic Compliance: A New Operating Model'"}
    - {ref: AVALARA-AGENTIC-2025, title: "Avalara launches 'always on, always ready' AI agents", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents", date: "2025-09-30", access: full, locator: "paragraphs on human-in-the-loop"}
    - {ref: AVALARA-NEXT-2026, title: "Avalara NEXT: The future of agentic tax and compliance", publisher: "Avalara", type: conference, url: "https://www.avalara.com/us/en/blog/avalara-next-2026-building-the-future-of-agentic-tax-and-compliance.html", date: "2026-03-04", access: full, locator: "event description and highlights"}
    - {ref: SOVOS-SOVI-2026, title: "Sovos Expands Sovi AI with New Capabilities", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/", date: "2026-03-24", access: full, locator: "MCP Gateway paragraph"}
    - {ref: TAXUALLY-2026, title: "Taxually Launched New E-Invoicing and Tax Calculation Products at Taxually Connect 2026", publisher: "Taxually", type: vendor, url: "https://www.taxually.com/blog/taxually-connect-2026-new-e-invoicing-and-tax-calculation-products", date: "2026-10-12", access: full, locator: "paragraph on new API capabilities"}
    - {ref: VERTEX-Q1CALL-2026, title: "Vertex (VERX) Q1 2026 Earnings Transcript", publisher: "Vertex Inc. / Motley Fool transcript", type: vendor, url: "https://finance.yahoo.com/markets/stocks/articles/vertex-verx-q1-2026-earnings-203016568.html", date: "2026-05-07", access: full, locator: "analyst Q&A, comment on agents built on the ERPs"}
  last_reviewed: "2026-10-17"
  notes: >-
    Function is technology-it because the change is to how tax services are consumed. Avalara's later April 2026
    release (search-only, not opened) is described in the landscape as adding MCP servers.

- id: tax-indirect-tax-16
  title: Tax-readiness review for agent-initiated checkout (idea)
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    When an AI agent buys on a customer's behalf there may be no human at checkout. Practitioners ask who must
    collect tax and whether time-limited rules such as sales tax holidays, destination sourcing and product
    thresholds are applied correctly.
  solution: >-
    Idea discussed by practitioners: tax teams review whether their engines' holiday rules are current and
    machine-readable, whether catalogue metadata lets agents identify eligible items, and how the platform
    handles tax in agent-initiated checkout; and assess whether operating an agent with integrated checkout and
    payment handling creates marketplace-facilitator or deemed-supplier status.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: STI-AGENTIC-2026
  prerequisites:
    - A current inventory of channels, including AI assistants, through which sales can occur (inferred).
    - Machine-readable catalogue data and tax-engine rules (Sales Tax Institute's recommended checks).
  risks_and_guardrails:
    - Bloomberg Tax commentary says the answer depends on how existing marketplace rules apply; AI systems have no legal personality, so the company operating the agent may have to collect tax (BTAX-AGENTICCOMMERCE-2026).
    - Sales Tax Institute notes that most agentic commerce models rely on the merchant's existing tax determination systems, and that agents can accelerate errors if configurations are stale (STI-AGENTIC-2026).
  human_checkpoints:
    - Tax and e-commerce teams confirm configuration before peak events (STI-AGENTIC-2026, recommended checks).
  role_evolution: Not described.
  evidence_grade: D
  sources:
    - {ref: STI-AGENTIC-2026, title: "Can AI Shopping Agents Apply Sales Tax Holidays?", publisher: "Sales Tax Institute", type: firm, url: "https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays", date: "2026-07-29", access: full, locator: "sections 'Where the Responsibility Actually Lands' and 'What This Means for Retailers and Tax Teams Today'"}
    - {ref: BTAX-AGENTICCOMMERCE-2026, title: "Artificial Intelligence Goes Shopping, Creates Tax Challenges", publisher: "Bloomberg Tax", type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/artificial-intelligence-goes-shopping-creates-tax-challenges", date: "2026-02-24", access: full, locator: "sections 'EU Value-Added Tax', 'US Sales Tax', 'Practical Takeaway'"}
    - {ref: TAXCLOUD-2025, title: "Agentic commerce is expanding ecommerce and your tax risk", publisher: "TaxCloud", type: vendor, url: "https://taxcloud.com/blog/agentic-commerce-is-expanding-ecommerce/", date: "2025-10-29", access: full, locator: "section 'AI is simply the next test for commerce and compliance'"}
  last_reviewed: "2026-10-17"
  notes: >-
    Idea. No vendor documentation of tax calculation inside agent checkout was found. The McKinsey estimate of
    $3-5 trillion in agent-orchestrated sales by 2030 is relayed by Bloomberg Tax and was not checked against McKinsey.

- id: tax-indirect-tax-17
  title: Compliance-by-design inside autonomous finance and procurement agents
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [transaction-processing, software-systems]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Companies add finance and tax applications around the ERP, creating integration and governance burdens while
    tax authorities require real-time clearance against jurisdiction-specific rules.
  solution: >-
    Sovos bought Flowie (1 Oct 2026), an agentic finance orchestration platform whose agents run accounts payable,
    procure-to-pay, contracts, invoicing, collections and onboarding on top of an ERP. Sovos says the agents will
    draw on its tax compliance and regulatory data so each action is grounded in the rules of the jurisdiction,
    and that they will work alongside its Sovi Agent Studio compliance agents (goods-and-service code mapping,
    e-invoice error diagnosis, data reconciliation).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: SOVOS-FLOWIE-2026
  prerequisites:
    - An ERP the agents can sit on top of.
    - Sovos tax and regulatory data feeds embedded in the agents' actions.
  risks_and_guardrails:
    - The release describes the combination as a launch announced on the acquisition date; integration is future tense ("will draw").
  human_checkpoints:
    - Not described.
  role_evolution: >-
    Flowie's CEO says the agents already run processes end-to-end; the release says CFOs and CIOs could retire
    surrounding applications (SOVOS-FLOWIE-2026).
  evidence_grade: C
  sources:
    - {ref: SOVOS-FLOWIE-2026, title: "Sovos Acquires Flowie, Launching the Industry's First Agentic Compliant Finance Orchestration Platform", publisher: "Sovos", type: vendor, url: "https://sovos.com/press-releases/sovos-acquires-flowie-launching-the-industrys-first-agentic-compliant-finance-orchestration-platform/", date: "2026-10-01", access: full, locator: "opening paragraphs and section 'The Inevitable Collision of AI, Tax Compliance, and Enterprise Finance Software'"}
  last_reviewed: "2026-10-17"
  notes: Announcement only, 16 days old at review. Overlaps finance operations; see Routed section.

- id: tax-indirect-tax-18
  title: AI-enabled managed sales tax and VAT compliance for growth companies
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [transaction-processing, client-interaction]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    Fast-growing software, distribution and manufacturing companies face multi-state and multi-country obligations
    without the in-house staff to register, calculate, file and manage certificates.
  solution: >-
    Providers such as Numeral run the compliance lifecycle (nexus monitoring, registrations, calculation, filing,
    remittance, certificates, VAT/GST in more than 90 countries) as a service, with AI doing much of the work and
    named humans for complex issues. KPMG's survey shows the wider shift away from purely local preparation toward
    central hubs and external providers.
  outcomes:
    - lever: growth
      description: Numeral reports transaction volume growth.
      figure: "327% year over year"
      measures: >-
        Increase in Numeral's total transaction volume year over year, per its Sep 2026 funding release; Numeral also
        expects to process more than 80 million transactions via its tax engine.
      provenance: vendor-published
      source_ref: NUMERAL-2026
    - lever: growth
      description: Taxually reports client growth.
      figure: "almost 40%"
      measures: Growth in Taxually's active clients, per its own Oct 2026 post; period and base not stated.
      provenance: vendor-published
      source_ref: TAXUALLY-2026
    - lever: capacity
      description: >-
        Adjacent measure, not an AI outcome: in-house local return preparation fell between KPMG's 2021 and 2026
        surveys while co-sourced and outsourced models grew.
      figure: "44% to about 23% prepared locally"
      measures: >-
        Share of surveyed organizations that prepare VAT/GST returns locally in-house (2021 survey vs 2026 survey);
        2026 split is 32% in-house centrally, 23% locally, 26% co-sourced, 19% outsourced (n=53 in 2026).
      provenance: independent
      source_ref: KPMG-INDIRECT-2026
  prerequisites:
    - Billing and ERP connections (Numeral lists over 40 supported systems).
  risks_and_guardrails:
    - Numeral says customers need access to a person when a complex issue arises (NUMERAL-2026, CEO quotation), which implies the escalation path is part of the offer.
  human_checkpoints:
    - Complex issues go to tax experts at the provider (NUMERAL-2026).
  role_evolution: >-
    Shift from in-house local preparation to central hubs and external partners (KPMG-INDIRECT-2026, p.10).
  evidence_grade: C
  sources:
    - {ref: NUMERAL-2026, title: "Numeral Raises $100 Million Series C", publisher: "Numeral", type: vendor, url: "https://www.numeralhq.com/blog/series-c", date: "2026-09-23", access: full, locator: "milestones paragraph; CEO quotation"}
    - {ref: TAXUALLY-2026, title: "Taxually Launched New E-Invoicing and Tax Calculation Products at Taxually Connect 2026", publisher: "Taxually", type: vendor, url: "https://www.taxually.com/blog/taxually-connect-2026-new-e-invoicing-and-tax-calculation-products", date: "2026-10-12", access: full, locator: "section 'How is Taxually growing?'; programme paragraph on a logistics client"}
    - {ref: KPMG-INDIRECT-2026, title: "Benchmarking Indirect Tax in a data-driven era", publisher: "KPMG International", type: survey, url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf", date: "2026-05", access: full, locator: "p.10 'Compliance delivery models'"}
  last_reviewed: "2026-10-17"
  notes: >-
    The KPMG delivery-model shift is not attributed to AI by the source and is an adjacent measure; it caps nothing
    here because the grade is already C. Taxually's keynote session featured an unnamed head of indirect tax at a
    shipping and logistics company with more than 700 entities, who spoke of automation helping compliance, accuracy
    and visibility; no AI claim or figure was made.

- id: tax-indirect-tax-19
  title: General-purpose GenAI for first-pass analysis and month-end summaries in in-house indirect tax
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types: [research-synthesis, document-production, data-reporting]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Small in-house indirect-tax teams cover multiple jurisdictions and cannot spend scarce time on recurring data
    analysis and summaries.
  solution: >-
    Plusgrade's Tax Manager, Indirect posting says AI handles the first pass on recurring data analysis and
    month-end tax summaries so the manager focuses on judgment calls and multi-jurisdictional research. It asks
    candidates to have replaced recurring manual work with workflows they built and to tell trustworthy output from
    output needing judgment. Survey data say usage is broad: Thomson Reuters reports 65% use public GenAI tools such as ChatGPT.
  outcomes:
    - lever: capacity
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: PLUSGRADE-JOB-2026
  prerequisites:
    - Access to approved AI tools; Plusgrade says its teams are given AI tools and encouraged to use them thoughtfully.
    - A manager able to judge output quality (the posting requires this).
  risks_and_guardrails:
    - Thomson Reuters reports 36% of corporate professionals use AI tools their organization has not sanctioned, and 44% of those at organizations with a named AI strategy say their day-to-day practice does not match it (TR-INDIRECT-DATA-2026, section 'The data caught up').
  human_checkpoints:
    - The Tax Manager owns the final call on complex transactions and reviews AI output (PLUSGRADE-JOB-2026).
  role_evolution: >-
    The role is framed as architect of end-to-end indirect-tax processes and the face of the company in audits,
    with AI taking the first pass (PLUSGRADE-JOB-2026). Thomson Reuters Institute advises staff to become
    translators between tax and technology (TR-INSTITUTE-2025).
  evidence_grade: B
  sources:
    - {ref: PLUSGRADE-JOB-2026, title: "Tax Manager, Indirect (Plusgrade)", publisher: "Built In Toronto (Plusgrade posting)", type: job-posting, url: "https://builtintoronto.com/job/tax-manager-indirect/8736459", date: "2026-05", access: full, locator: "'What You'll Be Doing' and 'What You Bring'"}
    - {ref: TR-INDIRECT-DATA-2026, title: "What three years of data reveal about AI in corporate indirect tax", publisher: "Thomson Reuters", type: survey, url: "https://tax.thomsonreuters.com/blog/what-three-years-of-data-reveal-about-ai-in-corporate-indirect-tax/", date: "2026-08-27", access: full, locator: "Highlights; section '2026: The data caught up'"}
    - {ref: TR-INSTITUTE-2025, title: "AI and the indirect tax department: From compliance to strategy", publisher: "Thomson Reuters Institute", type: vendor, url: "https://www.thomsonreuters.com/en/institute/articles/ai-indirect-tax", date: "2025-09-17", access: full, locator: "section 'Elevating your profile'"}
  last_reviewed: "2026-10-17"
  notes: >-
    The posting date was not shown; the page says the job was removed on 21 May 2026, so date 2026-05 is the removal
    month. A recruiter's description is a weak real-use signal, which is why the grade is B and no outcome is
    claimed. TR's 65% and 26% figures come from a TR survey whose population and sample are not described on the
    page (the page speaks of tax professionals; some figures are for corporate professionals across functions), so
    they are adjacent measures.

- id: tax-indirect-tax-20
  title: Indirect-tax exposure, accrual and scenario analysis with agents (idea)
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types: [expert-judgment, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Indirect-tax teams answer ad hoc business questions about supply-chain changes, new markets and pricing, and
    book conservative accruals because of data gaps.
  solution: >-
    Idea discussed by practitioners: agents run ongoing scenario analysis for supply-chain or trade changes,
    give a view of exposures that may reduce conservative over-accruals, and flag transactions that create
    unmanaged exposure (Deloitte). Thomson Reuters Institute adds forecasting VAT/GST cash flows and quantifying
    audit exposure by country, product and customer segment.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: DELOITTE-AGENTIC-2026
  prerequisites:
    - Consolidated transaction and customer data with product mapping (inferred).
  risks_and_guardrails:
    - Deloitte calls its examples "illustrative" and says tax professionals stay responsible for decisions (DELOITTE-AGENTIC-2026, section 3 and the introduction to 'Mitigating risk').
  human_checkpoints:
    - Structured input is provided for consideration by tax professionals (DELOITTE-AGENTIC-2026, section 3).
  role_evolution: >-
    Tax engages earlier in decisions rather than validating after the fact (DELOITTE-AGENTIC-2026, section 3).
  evidence_grade: D
  sources:
    - {ref: DELOITTE-AGENTIC-2026, title: "Agentic AI and indirect tax: a practical view for tax directors", publisher: "Deloitte Global", type: firm, url: "https://www.deloitte.com/global/en/services/tax/perspectives/agentic-ai-and-indirect-tax-practical-view-for-tax-directors.html", date: "2026-07-01", access: full, locator: "section 2 (accruals) and section 3 (scenario analysis)"}
    - {ref: TR-INSTITUTE-2025, title: "AI and the indirect tax department: From compliance to strategy", publisher: "Thomson Reuters Institute", type: vendor, url: "https://www.thomsonreuters.com/en/institute/articles/ai-indirect-tax", date: "2025-09-17", access: full, locator: "paragraph beginning 'As AI takes on more processing'"}
  last_reviewed: "2026-10-17"
  notes: Idea. No deployment found.
```

## 3. Module notes

### Processes, steps and work types
- **Tax determination at transaction (rates, taxability, jurisdiction):** transaction-processing, run in a tax engine integrated with ERP, billing and checkout. Vendors keep AI around a deterministic engine (Vertex says the engine remains the system of record).
- **Product and customer master data (classification, mapping, certificates):** data-reporting and review-assurance. Use cases 01, 03.
- **Returns (US sales and use, VAT/GST):** collect, validate, map, reconcile, file. Transaction-processing and data-reporting. Use case 02. Thomson Reuters cites more than 19,000 US jurisdictions and 1,200 official returns (TR-SUTAI-2026).
- **Registration and nexus:** transaction-processing with expert judgment. Use case 11.
- **E-invoicing and continuous transaction controls (clearance, post-audit, Peppol five-corner, SAF-T):** software-systems and transaction-processing. Sovos lists France and Spain as clearance via certified private providers, Poland as a central government platform, Germany as post-audit, and Peppol networks in the UAE, Oman, Slovakia, Norway and Singapore (SOVOS-CN-2026). Use cases 06, 14.
- **Reconciliation and VAT recovery:** use case 08.
- **Audits and notices:** use cases 12, 13.
- **Regulatory-change monitoring and impact assessment:** research-synthesis. Use case 07.
- **Advisory, accruals, scenario work:** expert judgment. Use case 20.

### Common pain points
- Data quality is the top concern for 58% of KPMG respondents (44% in 2021), 61% fix data predominantly manually, and 23% say their ERP is fit for purpose (KPMG-INDIRECT-2026, p.5-6).
- Flat headcount against a wider scope: almost 60% expect headcount largely unchanged for five years; about one third have no technology specialists; teams also own e-invoicing (33%), tax data reporting such as SAF-T (26%), digital services taxes (18%) and customs and excise (16%) (KPMG-INDIRECT-2026, p.7).
- E-invoicing ownership is fragmented: Finance 38%, Tax or tax technology 30%, IT 11% (p.11). About two thirds prefer a global solution provider.
- Manual classification and certificate handling cause inconsistency and audit exposure (TR-CLASSIFICATION-2026; NUMERAL-2026).
- Rule change outpaces watchers: more than 70 countries changed e-invoicing rules since 2020 (FONOA-MONITORING-2026, vendor statement).

### Metrics and benchmarks (all vendor-published unless marked)
- Product categorization time per product: from over 1.5 minutes to a few seconds (Vertex, VERTEX-Q1CALL-2026).
- Routine sales and use tax reporting time: up to 65% less; compliance cycle 30 days to 11 days; audit exposure up to 75% lower per early customers; 40-60% preparation time saved in the earlier release (Thomson Reuters, TR-SUTAI-2026, TR-ONESOURCEPLUS-2025). Customers unnamed.
- E-invoice rejection rate in France: 1.6% against an estimated 20% market-wide (Sovos, SOVOS-FRANCE-2026b). Not attributed to AI.
- Existing certificates failing validation on migration: 30-40% (Numeral).
- Time on filings and registrations: up to 80% less; manual spreadsheet work and filing errors up to 95% less (Numeral, NUMERAL-2026; the 95% was not used in a use case because its baseline is undefined).
- Forrester total-economic-impact study for ONESOURCE Indirect Tax (non-AI tax engine, commissioned by Thomson Reuters, 7 customers aggregated into a composite organization): invoice error rate from 3% to well below 1%; 120% ROI over three years (TR-FORRESTER-2024). Adjacent, pre-GenAI, composite figures.
- Adoption and maturity (survey): Fonoa, 176 indirect-tax leaders, June 2026: 92% use AI in some form, 12.5% have specific targets or KPIs, 57.4% would not be confident defending AI-assisted decisions to a tax authority, about a third run formal human-in-the-loop review, a small cohort with accountability structures reports compliance workload falling at 8x the rate of others (FONOA-2026).
- Thomson Reuters, Aug 2026: 65% of tax professionals use GenAI tools, 26% measure ROI, 36% of corporate professionals use unsanctioned tools (TR-INDIRECT-DATA-2026).
- Deloitte (relaying its Tax Transformation Trends 2025): 77% of surveyed tax leaders require 90% or better accuracy before trusting AI.
- Avalara (Censuswide, 1,500+ finance leaders, US/UK/India/Australia, Aug 2026): 92% feel career pressure to prove agent ROI, 76% lack in-house expertise to understand how their agents work, 30% have not updated internal controls for AI-driven actions, 46% say AI incident response plans are untested or in development (AVALARA-GOVERNANCE-2026). Finance-wide, not indirect-tax specific.
- **Independent quality evidence:** none found. No override rate, error rate on AI outputs, parallel-run result or inspection finding was found in any source for AI in indirect tax.

### Guardrails and regulatory points
- Every vendor design reviewed puts a human approval before filing or rule activation (Avalara, Thomson Reuters, Sovos) and logs each action for audit.
- EU VAT in the Digital Age (ViDA): adopted 11 Mar 2025, in force 14 Apr 2025. From 1 Jul 2028 deemed-supplier rules for platforms in short-term accommodation rental and road passenger transport and the Single VAT Registration reforms start; digital reporting requirements for cross-border B2B transactions apply from 1 Jul 2030; national real-time systems must align by 1 Jan 2035 (EC-VIDA-2026). The Commission says e-invoicing could cut VAT fraud by up to EUR 11 billion a year and compliance costs by over EUR 4.1 billion a year over ten years (Commission estimate). The landscape file's EU-VIDA-2024 entry (Fonoa blog, 5 Nov 2024) predates final adoption and lists an "OSS expansion" in July 2028; the Commission page names the July 2028 item as the Single VAT Registration pillar.
- France's mandate: all established companies must be able to receive e-invoices from 1 Sep 2026; large and medium-sized companies must also issue and report; smaller businesses follow in Sep 2027 (SOVOS-FRANCE-2026, vendor summary).
- Marketplace and agentic commerce: US marketplace-facilitator laws generally apply to all taxable sales through the platform once nexus thresholds are met; EU deemed-supplier treatment is narrower (BTAX-AGENTICCOMMERCE-2026).
- Authorities scrutinise AI use: a Fonoa-surveyed majority lacks confidence in defending AI-assisted decisions; Fonoa and Thomson Reuters both advise citing primary sources and keeping versioned outputs.

### Frontier signals (dated, sourced)
- Avalara Aviator unveiled at CRUSH, 23-24 Sep 2026; general availability stated as following CRUSH Europe in the next month; initially at no additional cost to existing customers; "self-healing" agents are planned (AVALARA-AVIATOR-2026).
- Sovos: Compliance Network GA 2 Jun 2026; Blue dot (15 Sep 2026) and Flowie (1 Oct 2026) acquisitions move it toward agent-run finance processes (SOVOS-CN-2026, SOVOS-BLUEDOT-2026, SOVOS-FLOWIE-2026).
- Vertex: Smart Categorization in production; Brinta acquired in Q1 2026; ERP agents (a Microsoft one announced); cost reduction in force announced alongside the AI roadmap (VERTEX-Q1CALL-2026). Vertex also says it expects e-invoicing revenue to ramp after French mandates and again in 2027 when German mandates come online.
- Funding: Numeral raised $100M Series C on 23 Sep 2026 (NUMERAL-2026).
- Regulators: France mandate live 1 Sep 2026; Fonoa reports Spain published B2B e-invoicing dates (5 Oct 2026), the Netherlands confirmed plans (28 Sep 2026), Bulgaria proposed mandatory structured e-invoicing from 2028 (9 Oct 2026) (FONOA-BLOG-2026, headlines only, seen 17 Oct 2026).
- Agentic commerce: Google's Universal Commerce Protocol and ChatGPT's Agentic Commerce Protocol (which TaxCloud attributes to Stripe) are referenced by Sales Tax Institute and TaxCloud; Visa, Mastercard and American Express announced agentic commerce initiatives as of April 2026 (STI-AGENTIC-2026).
- Tax authorities: the OECD Global Forum on VAT met in Paris on 26-29 Jan 2026 and discussed crypto-assets and AI (search-only, OECD-GFVAT-2026). South Carolina's DOR is adding AI audit selection to GenTax in 2026 (see Routed).

### Workforce and role effects
- KPMG: 58% expect VAT/GST headcount largely unchanged because of AI, 21% an increase and 21% a decrease; respondents see AI as a means to enhance data quality, not cut workforce (KPMG-INDIRECT-2026, p.5, p.7).
- Role shape: tax technology and data roles are growing. OpenAI's Finance tax team hires an Indirect Tax Technology Manager to run Vertex, product mappings, exemption configuration and testing, working with Financial Engineering, Product Engineering and Finance Systems (OPENAI-JOB-2026). EY advertises a "Tax Technology and Transformation - Indirect Tax" manager role built around implementing transaction-tax engines (EY-JOB-2026). Plusgrade's posting expects a CPA who builds AI workflows (PLUSGRADE-JOB-2026).
- Ownership of AI: Fonoa reports that teams with accountability structures see far better results; its survey shows only 12.5% have specific AI targets (FONOA-2026). TR Institute advises upskilling existing staff as tax-technology translators (TR-INSTITUTE-2025).
- Vendors' own staffing: Vertex announced a reduction in force while saying support analysts can handle higher case volumes with AI (VERTEX-Q1CALL-2026). Vertex reported this as early results.

### Objections and concerns practitioners raise
- Defensibility to authorities (57.4% lack confidence; Fonoa).
- No KPIs or measurement (12.5% have targets; 26% measure ROI; Thomson Reuters).
- Shadow AI (36% unsanctioned use; Thomson Reuters).
- General models can be fluently wrong on recent changes; primary-source citation is the remedy (Fonoa).
- Deterministic versus probabilistic: Vertex insists tax answers must be 100% accurate, explainable and auditable; Fonoa argues the comparison should be coverage and error rate against current manual practice, citing spreadsheet error rates it does not source on that page (FONOA-AIERA-2025). Treat Fonoa's 24%-90% spreadsheet error range as unverified.
- Governance lagging deployment (Avalara survey).
- Data and ERP readiness (KPMG).

### Interview probes for an advisor
1. When your tax engine or an AI tool proposes a product code, certificate decision or return line, who approves it, and what share do reviewers change? Is that override rate tracked?
2. If an authority asked next month how an AI-assisted determination or filing was made, what could you hand over (inputs, source, version, approver)?
3. Who owns e-invoicing and the data feeding it (Tax, Finance or IT), and what happens to the team when an invoice is rejected by the clearance platform at 6 pm on a filing day?
4. Which of these do you let a vendor's agent do without a person today: validate certificates, prepare a return, file, register, correct an error? Where is the line and who drew it?
5. What happens in your function if your AI vendor's agents are called by your own finance or procurement agents, or by a customer's shopping agent?

## 4. Routed to other modules

- **Customs and trade classification (HS and tariff codes):** Avalara cross-border agents classify products, identify HS codes and check restricted-party lists (AVALARA-AVI-2025); Thomson Reuters ONESOURCE Global Classification AI suggests HS codes and writes audit-ready rationales (TR-ONESOURCEPLUS-2025). Route to tax-data-technology (or a customs/trade sub-topic, as the landscape suggests).
- **Property tax agents (fixed-asset classification and filing):** Avalara (AVALARA-AVI-2025). Route to compliance.
- **State and local tax-authority AI audit selection:** South Carolina DOR is adding AI and analytics to its GenTax platform (FAST Enterprises) to flag higher-risk business returns, starting in 2026 (KOGOD-SCDOR-2026, summarising a Post and Courier article that was not opened). Withum's report on the 2026 SEATA meeting says state commissioners from Alabama, Arkansas, Georgia, Florida, Kentucky, Mississippi, West Virginia and Virginia described AI and analytics for audit selection, fraud detection and enforcement (WITHUM-SEATA-2026; the report itself notes no Florida-specific technical presentation was identified). Route to controversy (and the landscape's proposed tax-authority AI module).
- **Accounts payable and procure-to-pay automation (Flowie agents):** SOVOS-FLOWIE-2026; the finance-operations part is outside the tax archetype.
- **Cross-cutting governance and survey evidence (Avalara/Censuswide, Fonoa, Thomson Reuters):** route the AI-governance findings to the governance and evidence angle. The shadow-AI and incident-response numbers are not indirect-tax specific.
- **MCP/A2A interoperability architecture:** use case 15 is written here for the indirect-tax angle; route the technical architecture to tax-data-technology.
- **EY India AI Tax Hub (agents for research, compliance and litigation) and India GST platform:** EY India announced on 18 Feb 2026 an AI Tax Hub with agents for research, compliance and litigation, plus an Accounts Payable Automation tool covering TDS, GST and India's Invoice Management System, within its India Tax Platform (EY-INDIA-2026). The platform figures (4,000+ clients, US$750bn annual tax transactions, 2.6bn invoices processed on its GST platform) are EY's own and are scale context, not AI outcomes. Route the research and litigation agents to research-advisory and controversy; the GST platform context stays here.

## 5. Sources

Access is `full` unless noted. Types follow the controlled vocabulary. "Via mirror" means the page blocked `curl` and was read through the r.jina.ai text mirror.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| TR-SUTAI-2026 | Thomson Reuters Launches AI Tax Compliance Solution That Saves Time and Reduces Risk | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk | 2026-01-15 | full |
| TR-ONESOURCEPLUS-2025 | Thomson Reuters launches ONESOURCE+ | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-onesource-plus-the-ai-powered-intelligent-compliance-network | 2025-11-05 | full |
| TR-CLASSIFICATION-2026 | How AI can rescue product classification for indirect tax teams | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/how-ai-can-rescue-product-classification-for-indirect-tax-teams/ | 2026-04-10 | full |
| TR-INDIRECT-DATA-2026 | What three years of data reveal about AI in corporate indirect tax | Thomson Reuters | survey | https://tax.thomsonreuters.com/blog/what-three-years-of-data-reveal-about-ai-in-corporate-indirect-tax/ | 2026-08-27 | full |
| TR-BUSINESSCASE-2026 | How to build a business case for indirect tax process automation | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/how-to-build-a-business-case-for-indirect-tax-process-automation/ | 2026-02-05 | full |
| TR-INSTITUTE-2025 | AI and the indirect tax department: From compliance to strategy | Thomson Reuters Institute | vendor | https://www.thomsonreuters.com/en/institute/articles/ai-indirect-tax | 2025-09-17 | full |
| TR-FORRESTER-2024 | The corporate tax department business case (Forrester TEI summary) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/the-corporate-tax-department-business-case-making-the-final-tax-technology-pitch/ | 2024-03-25 | full |
| SOVOS-SOVI-2026 | Sovos Expands Sovi AI with New Capabilities | Sovos | vendor | https://sovos.com/press-releases/sovos-expands-sovi-ai/ | 2026-03-24 | full |
| SOVOS-CN-2026 | Sovos Launches Compliance Network | Sovos | vendor | https://sovos.com/press-releases/sovos-launches-compliance-network-to-address-unprecedented-wave-of-global-e-invoicing-mandates/ | 2026-06-02 | full |
| SOVOS-FRANCE-2026 | Sovos Brings Global 2000 Clients Live in France | Sovos | vendor | https://sovos.com/press-releases/sovos-brings-global-2000-clients-live-in-france-ahead-of-the-worlds-most-complex-e-invoicing-mandate/ | 2026-08-18 | full |
| SOVOS-FRANCE-2026b | Three Weeks into France E-Invoicing Mandate: Sovos Hits Unparalleled Production Scale | Sovos | vendor | https://sovos.com/press-releases/three-weeks-into-france-e-invoicing-mandate-sovos-hits-unparalleled-production-scale/ | 2026-09-23 | full |
| SOVOS-BLUEDOT-2026 | Sovos Acquires Blue dot | Sovos | vendor | https://sovos.com/press-releases/sovos-acquires-blue-dot-expanding-ai-native-diagnostics-workflow-and-intelligence-capabilities-widening-sovos-tax-compliance-platform-technology-lead/ | 2026-09-15 | full |
| SOVOS-FLOWIE-2026 | Sovos Acquires Flowie | Sovos | vendor | https://sovos.com/press-releases/sovos-acquires-flowie-launching-the-industrys-first-agentic-compliant-finance-orchestration-platform/ | 2026-10-01 | full |
| AVALARA-AGENTIC-2025 | Avalara launches 'always on, always ready' AI agents | Accounting Today | press | https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents | 2025-09-30 | full |
| AVALARA-AGENTIC-2025b | Avalara Launches Agentic Tax and Compliance: AI Agents That Work for You | Avalara via iTWire | vendor | https://itwire.com/business-it-news/data/avalara-launches-agentic-tax-and-compliance-ai-agents-that-work-for-you | 2025-10-01 (byline 2 Oct) | full |
| AVALARA-AVI-2025 | Avalara launches Avi AI agents for secure automated tax compliance | IT Brief UK | press | https://itbrief.co.uk/story/avalara-launches-avi-ai-agents-for-secure-automated-tax-compliance | 2025-11-04 | full |
| AVALARA-AVIATOR-2026 | Avalara Ushers in New Era of Agentic Tax and Compliance with Avalara Aviator | Avalara via iTWire | vendor | https://itwire.com/guest-articles/company-news/avalara-ushers-in-new-era-of-agentic-tax-and-compliance-with-avalara-aviator | 2026-09-23 (byline 24 Sep) | full |
| AVALARA-NEXT-2026 | Avalara NEXT: The future of agentic tax and compliance | Avalara | conference | https://www.avalara.com/us/en/blog/avalara-next-2026-building-the-future-of-agentic-tax-and-compliance.html | 2026-03-04 (event 2026-03-26) | full |
| AVALARA-GOVERNANCE-2026 | Agentic AI in finance: Speed is outrunning governance | Avalara | survey | https://www.avalara.com/us/en/blog/agentic-ai-finance-governance-survey.html | 2026-08-10 | full |
| VERTEX-Q1CALL-2026 | Vertex (VERX) Q1 2026 Earnings Transcript | Vertex Inc. (Motley Fool transcript on Yahoo Finance) | vendor | https://finance.yahoo.com/markets/stocks/articles/vertex-verx-q1-2026-earnings-203016568.html | 2026-05-07 (call date; transcript posted 2026-06-01) | full |
| VERTEX-SMARTCAT-2026 | Vertex Smart Categorization data sheet | Vertex Inc. | vendor | https://www.vertexinc.com/sites/default/files/2026-05/202604-data-sheet-vertex-smart-categorization-v3.pdf | 2026-04 (from filename) | full |
| VERTEX-COPILOT-2025 | AI and the Customer Experience: How Vertex Copilot is Shaping the Future | Vertex Inc. | vendor | https://www.vertexinc.com/node/7552 | 2025-05-06 | full |
| FONOA-2026 | State of Indirect Tax in the AI Era 2026 (landing page; full report gated) | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 | full (landing page only) |
| FONOA-CITATION-2026 | Why Primary Source Citation Matters for Tax Audit Defense | Fonoa | vendor | https://www.fonoa.com/resources/blog/primary-source-tax-law-citation-audit | 2026-09-21 | full |
| FONOA-MONITORING-2026 | Why Manual Indirect Tax Regulatory Change Monitoring No Longer Scales | Fonoa | vendor | https://www.fonoa.com/resources/blog/indirect-tax-regulatory-change-monitoring | 2026-09-16 | full |
| FONOA-AIERA-2025 | Preparing for the Era of AI if You Manage Indirect Tax | Fonoa | vendor | https://www.fonoa.com/resources/blog/ai-era-indirect-tax-strategy | 2025-11-19 | full |
| FONOA-BLOG-2026 | Fonoa blog index (regulatory updates, Oct 2026 headlines) | Fonoa | vendor | https://www.fonoa.com/resources/blog | 2026-10-09 (latest item listed) | full (index page only) |
| EU-VIDA-2024 | EU Member States Approve the VAT in the Digital Age (ViDA) Package | Fonoa | vendor | https://www.fonoa.com/resources/blog/eu-member-states-approve-vat-in-the-digital-age-vida-package | 2024-11-05 | full |
| EC-VIDA-2026 | VAT in the Digital Age (ViDA) | European Commission, DG TAXUD | regulator | https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en | 2026-05-20 (page lists items to 2026-07-28) | full |
| KPMG-INDIRECT-2026 | Benchmarking Indirect Tax in a data-driven era (2026 KPMG Indirect Tax Benchmarking Survey) | KPMG International | survey | https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf | 2026-05 | full |
| DELOITTE-AGENTIC-2026 | Agentic AI and indirect tax: a practical view for tax directors | Deloitte Global (first in International Tax Review, 2026-06-12) | firm | https://www.deloitte.com/global/en/services/tax/perspectives/agentic-ai-and-indirect-tax-practical-view-for-tax-directors.html | 2026-07-01 | full |
| EY-INDIA-2026 | EY India strengthens tax technology leadership with the launch of AI-enabled enterprise tax solutions | EY India | firm | https://www.ey.com/en_in/newsroom/2026/02/ey-india-strengthens-tax-technology-leadership-with-the-launch-of-ai-enabled-enterprise-tax-solutions | 2026-02-18 | full |
| STI-AGENTIC-2026 | Can AI Shopping Agents Apply Sales Tax Holidays? | Sales Tax Institute | firm | https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays | 2026-07-29 | full |
| BTAX-AGENTICCOMMERCE-2026 | Artificial Intelligence Goes Shopping, Creates Tax Challenges | Bloomberg Tax | press | https://news.bloombergtax.com/tax-insights-and-commentary/artificial-intelligence-goes-shopping-creates-tax-challenges | 2026-02-24 | full |
| TAXCLOUD-2025 | Agentic commerce is expanding ecommerce and your tax risk | TaxCloud | vendor | https://taxcloud.com/blog/agentic-commerce-is-expanding-ecommerce/ | 2025-10-29 | full (via mirror) |
| TAXUALLY-2026 | Taxually Launched New E-Invoicing and Tax Calculation Products at Taxually Connect 2026 | Taxually | vendor | https://www.taxually.com/blog/taxually-connect-2026-new-e-invoicing-and-tax-calculation-products | 2026-10-12 (event 2026-09-29) | full |
| NUMERAL-2026 | Numeral Raises $100 Million Series C to Expand AI-Powered Tax Compliance Across Industries | Numeral | vendor | https://www.numeralhq.com/blog/series-c | 2026-09-23 | full |
| OPENAI-JOB-2026 | Indirect Tax Technology Manager (OpenAI) | Stripes job board | job-posting | https://jobs.stripes.co/companies/openai/jobs/78936040-indirect-tax-technology-manager | 2026-05-15 | full |
| PLUSGRADE-JOB-2026 | Tax Manager, Indirect (Plusgrade) | Built In Toronto | job-posting | https://builtintoronto.com/job/tax-manager-indirect/8736459 | 2026-05 (removal month) | full |
| EY-JOB-2026 | Tax Technology and Transformation - Indirect Tax - Manager (New York) | EY Careers | job-posting | https://careers.ey.com/ey/job/new-york-tax-technology-and-transformation-indirect-tax-manager-ny-10001-8604/1437580833/ | 2026-10-15 (datePosted in page metadata) | full |
| WITHUM-SEATA-2026 | Key Takeaways From the 2026 SEATA Conference | Withum | firm | https://www.withum.com/resources/key-takeaways-from-the-2026-seata-conference/ | 2026-07-14 | full (via mirror) |
| KOGOD-SCDOR-2026 | Artificial Intelligence Being Used by SC Department of Revenue to Determine Who to Audit this Year (summary of Post and Courier coverage) | Kogod School of Business, American University | press | https://kogod.american.edu/news/artificial-intelligence-being-used-by-sc-department-of-revenue-to-determine-who-to-audit-this-year | 2026-04-29 | full (summary page) |
| SALESTAX-AI-2026 | Are You Using AI to Find Businesses That Aren't Paying Sales Tax? | The Sales Tax People | firm | https://sales.tax/sales-tax-updates/states-ai-sales-tax-audits-enforcement-2026/ | 2026-05-18 | full; read but not relied on (marketing piece, claims cite other outlets) |
| AVALARA-AGENTIC-2026 | Avalara Advances Agentic Compliance, Moving from AI-Assisted to AI-Executed Workflows | Avalara (PR Newswire / StreetInsider) | vendor | https://www.streetinsider.com/Press+Releases/Avalara+Advances+Agentic+Compliance%2C+Moving+from+AI-Assisted+to+AI-Executed+Workflows/26293078.html | 2026-04 (month per landscape file; not verified) | search-only |
| OECD-GFVAT-2026 | Tax and business leaders gather at OECD to advance global dialogue on future-ready VAT systems | OECD | regulator | https://www.oecd.org/en/about/news/announcements/2026/01/tax-and-business-leaders-gather-at-oecd-to-advance-global-dialogue-on-future-ready-vat-systems-amid-digital-transformation.html | 2026-01 | search-only (page blocked) |
| POSTCOURIER-SCDOR-2026 | SC using Artificial Intelligence to determine who to audit | The Post and Courier | press | https://www.postandcourier.com/news/sc-taxes-artificial-intelligence-audits-fast-scdor/article_54662d56-ae30-4130-845a-366547409477.html | 2026-04 (month of the Kogod summary) | search-only (blocked) |
| KINTSUGI-2026 | Kintsugi Sales Tax Monthly: March 2026 | Kintsugi | vendor | https://trykintsugi.com/blog/kintsugi-sales-tax-monthly-march-2026.md | 2026-03 | search-only (page returned 404 to curl) |

**Counts.** 43 sources opened (access full) and 4 search-only. By type, opened: vendor 25, survey 4, firm 5, press 4, conference 1, regulator 1, job-posting 3. Search-only: vendor 2, regulator 1, press 1. No professional-body, academic or podcast source was reached.

## 6. Gaps

- **No named-customer outcome with measurements.** The only named deploying customers are Singer Equipment (a beta quotation) and the employers whose job postings were read. Vertex, Thomson Reuters, Numeral, Sovos and Taxually figures all come from the vendor and mostly refer to unnamed customers.
- **No independent quality evidence.** Error rates, override rates, parallel runs, inspection findings: none found. The Forrester study is commissioned, pre-GenAI and a composite.
- **Podcasts and community discussion.** The shared web-search budget ran out before these searches, so no podcast, forum or newsletter source was reached. Tax Notes Talk, Reddit tax communities and Sales Tax Institute podcasts remain unchecked.
- **Searches that did not surface named deployments:** Big Four VAT agents (only EY India's launch and Deloitte's thought piece found), Stripe Tax, Anrok, Pagero and Basware customer cases. Stripe's newsroom was fetched and held no tax-AI item.
- **Not reachable:** Avalara's 9 Apr 2026 release (PR Newswire link returned 404; StreetInsider copy blocked), OECD announcement (Cloudflare check), Post and Courier (403), Kintsugi pages (curl error and 404), Anrok (403), the gated Fonoa and Thomson Reuters Institute full reports, Thomson Reuters's 2025 Indirect Tax Report, Avalara CRUSH 2026 sessions, ITR AI in Tax Forum agenda.
- **Date and figure conflicts noted:** TR savings (40-60% vs up to 65%); Sovos volume (nearly 20 billion vs more than 70 billion transactions a year); landscape's ViDA approval date (Council agreement 5 Nov 2024 vs final adoption 11 Mar 2025); Avalara NEXT date (Avalara's own page says 26 Mar 2026, which settles the landscape's conflict with the 28 Apr listing); the Aviator and Accounting Today bylines are a day later than the UTC metadata for iTWire pieces.
- **Job postings:** only three postings read. None names an AI agent or describes an AI team's structure; they show tax-technology roles and AI-fluency expectations only.
- **Not covered:** non-US/UK/EU markets beyond India headlines and Latin America via Vertex's Brinta remark; Peppol-specific AI practice; customs duty and VAT on imports; indirect-tax outsourcing firms' (BPO) own deployments.
