# Module deep dive: tax / indirect-tax. Angle: governance & evidence

- **Archetype:** tax
- **Module:** indirect-tax. VAT, GST and sales and use tax: determination and rates, exemption certificates, returns, e-invoicing and continuous transaction controls (ViDA, Peppol), marketplace and digital-services rules, tax in agentic commerce, indirect-tax audits; state and local sales tax.
- **Angle:** governance & evidence. What constrains and measures the work: regulator and tax-authority statements, professional-body guidance, standards, academic studies, surveys and benchmarks.
- **Prepared:** 2026-10-17
- **Method note.** I read `landscape-tax.md` and the vocabulary first, then fetched pages with `curl`, read PDFs with `pdftotext`, used the `r.jina.ai` text mirror for pages that block `curl` (Bloomberg, EUR-Lex, GAO), and used arXiv's own search page to find academic papers. 37 sources are listed in section 5, each with an `access` value; every one was opened, though some only in part (noted in the title). The web-search quota ran out after two searches in this run, so the last planned directions (India GST, Brazil, SAF-T, Peppol and AI, state audit-selection AI, exemption-certificate acceptance rules) were not searched. Source keys follow `PUBLISHER-SHORT-YYYY` and reuse the landscape's keys where the document is the same. Quotations are under 25 words.

---

## 1. Summary

**What the evidence says, as of 17 Oct 2026.** Indirect tax has plenty of vendor claims and a few useful independent measurements. It has no published error rate, override rate, parallel-run result or inspection finding for any commercial VAT, GST or sales-tax engine or agent.

- **The best independent quality evidence is on VAT determination, and it is not reassuring.** A peer-reviewed study on Austrian and EU VAT law found that retrieval-grounded GPT-4o identified the place of supply in 93.24% of 74 textbook cases (plain GPT-4o 68.92%), but only 16 of 20 real client inquiries (80%) got a correct analysis, and fine-tuned or combined set-ups scored 70% and 55%. The authors call a 20-30% error rate unacceptable and say LLM-only decision-making is insufficient (LUKETINA-VAT-2026). A separate preprint on synthetic cross-border VAT cases found a tuned single agent at 0.755 accuracy and a single schema-valid hallucinated record degrading every agent set-up (SANTOS-VAT-2026).
- **Governance is lagging adoption.** In Fonoa's survey of 176 indirect tax leaders, 92% of tax functions use AI in some form, 57.4% would not be confident defending an AI-assisted decision to a tax authority, only about a third run a formal documented sign-off, and 12.5% have specific targets (FONOA-INDIRECT-2026, FONOA-BLOG-2026). Thomson Reuters reports 36% of corporate professionals use unsanctioned AI tools (TR-INDIRECT-2026). At TEI's April 2026 seminar, two hands of more than 50 said tax owns AI implementation at their company (TEI-TAXTECH-2026). Fonoa and Thomson Reuters are vendors, so treat their survey figures as vendor-published.
- **I found no regulator rules written specifically for AI in indirect tax.** The binding constraints are general: the EU's ViDA directive (structured e-invoicing and digital reporting; EN 16931), the AI Act (AI literacy duty for deployers; tax-administration systems treated as administrative, not law-enforcement), professional-conduct rules (IRS OPR Alert 2026-19 for federal practice, UK PCRT guidance from 19 Jan 2026), and state agency rules on what advice taxpayers can rely on (CDTFA Publication 70).
- **Authorities are the other half.** Austria's risk models examined nearly 27.5 million cases in 2023 across income, corporate, VAT and customs; HMRC plans real-time risking on VAT submissions; the OECD reports 29 of 38 members use AI in tax administration. KPMG's survey of 53 large multinationals ties the push to real-time, data-driven oversight, with data quality now the top VAT/GST concern for 58% (KPMG-INDIRECT-2026, OECD-GOVAI-2025, HMRC-ROADMAP-2025).
- **Agentic commerce is a live question, not yet a rule.** The OECD's VAT forum (26-29 Jan 2026) named AI an emerging challenge for VAT administration; practitioner commentary says an AI commerce app that takes payment and sends orders is likely to meet deemed-supplier or marketplace-facilitator tests (BTAX-OECDVAT-2026, BTAX-BAL-2026).

**Use cases.** 16 candidate use cases. Evidence grades: A 3, B 3, C 7, D 3. Grade A: VAT advisory assistant (research evaluation on real cases), the CDTFA agent-assist tool (production, thin measure) and product tax-code prediction (Dell test-set measure). Grade D entries are ideas that regulators or researchers actually discuss.

**Sources.** 37 sources by type: vendor 7, press 7, regulator 6, academic 6, professional-body 4, survey 3, podcast 1, conference 1, firm 1, standard-setter 1.

**Two most important insights.**
1. **Defensibility, not accuracy, is the stated bottleneck.** The survey data show adoption near universal and governance thin: authorities ask for the rule applied, the reviewer and the approval, which are records, and most teams cannot produce them (FONOA-BLOG-2026). The one independent accuracy study found a 20-30% wrong-analysis rate on real VAT cases (LUKETINA-VAT-2026), and both the researchers and the UK profession's guidance keep a named human responsible for outputs (LUKETINA-VAT-2026, ICAEW-PCRT-2026).
2. **Indirect tax runs on structured data, so authorities' data feeds raise the bar for taxpayers.** ViDA's e-invoice and reporting rules, HMRC's plan for real-time risking and Austria's ML risk scoring mean authorities will see transaction-level data. Taxpayers' main constraint is their own data quality: 58% of KPMG respondents name it their biggest concern and 23% say their ERP is fit for purpose (KPMG-INDIRECT-2026).

**Corrections to the landscape file.**
- Hadwick's paper counts "at least 85 different AI systems" in 26 EU Member States (HADWICK-EUAIACT, Sect. II.2), not about 70 systems in 18 Member States.
- The OECD figure from *Governing with AI* is 29 of 38 OECD members reporting AI use in tax administration in the 2024 Inventory of Tax Technology Initiatives (OECD-GOVAI-2025, p. 169); the landscape's "70% of 54 FTA members" comes from a different OECD report that I could not reopen.
- The Commission's ViDA page gives these dates: 14 Apr 2025 entry into force, 1 Jan 2027 OSS and IOSS clarifications, 1 Jul 2028 platform deemed-supplier rules and single VAT registration, 1 Jul 2030 digital reporting for cross-border B2B, 1 Jan 2035 alignment of domestic real-time systems (EC-VIDA-2025). The landscape's "OSS for energy" wording for January 2027 does not appear on that page.

---

## 2. Use cases

```yaml
- id: tax-indirect-tax-01
  title: Touchless sales and use tax return preparation with final human review and audit trail
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Corporate sales and use tax teams import transaction data, validate it, map it to state, county and city return lines and file, often in a manual cycle with last-minute scrambles. Fonoa's survey of 176 indirect tax leaders found 71% of teams have not fully automated a single workflow end to end."
  solution: "An agent handles data import, validation and mapping to returns, and files through the platform. A person keeps final review and sign-off, and the system keeps an audit trail of each automated decision. Thomson Reuters calls this 'touchless compliance'. Avalara describes a Returns agent that ingests transaction data, calls its returns APIs and files on behalf of the client once approved."
  outcomes:
  - lever: speed
    description: Reduction in time spent on routine reporting
    figure: "up to 65%"
    measures: "'time spent on routine reporting' as stated in the vendor release; baseline, sample and customer count not given"
    provenance: vendor-published
    source_ref: TR-SUTAI-2026
  - lever: speed
    description: Shorter compliance cycle for large enterprises
    figure: 30 days to 11 days
    measures: "length of the compliance cycle for 'large enterprises' as stated in the vendor release; number of customers and period not given"
    provenance: vendor-published
    source_ref: TR-SUTAI-2026
  - lever: risk
    description: Reduction in audit exposure reported by early customers
    figure: "up to 75%"
    measures: "'audit exposure' reduction reported by 'early customers' through automated validation and audit documentation; the metric definition and sample are not given"
    provenance: vendor-published
    source_ref: TR-SUTAI-2026
  prerequisites:
  - "Clean transaction and master data feeding the return engine (KPMG found 58% of 53 large multinationals name data quality as their biggest VAT/GST concern, and 23% say their ERP is fit for purpose)"
  - Current return forms and rates in the engine (the release says content updates monthly)
  - A named reviewer who signs off before filing
  risks_and_guardrails:
  - "Vendor figures are unverified: no baseline, sample or named customer is published (TR-SUTAI-2026)"
  - "57.4% of 176 respondents are not confident they could defend AI-assisted decisions to a tax authority, and only about a third run a formal documented human-in-the-loop sign-off (FONOA-BLOG-2026)"
  - Avalara says agents notify a person for novel situations and key decisions (ACCTODAY-AVALARA-2025)
  - IRS OPR Alert 2026-19 covers federal tax practice under Circular 230; it does not address state sales tax or VAT filings (IRS-OPR-2026)
  human_checkpoints:
  - Final review and approval of each return before e-filing
  - Review of exceptions where the agent has no established procedure
  - Sign-off on mapping changes
  role_evolution: "Thomson Reuters says professionals move from operations to advisory work while keeping final review and approval. KPMG's survey finds 58% of respondents expect indirect tax headcount to stay largely unchanged over five years as a result of AI."
  evidence_grade: C
  sources:
  - ref: TR-SUTAI-2026
    title: Thomson Reuters Launches AI Tax Compliance Solution That Saves Time and Reduces Risk (ONESOURCE Sales and Use Tax AI)
    publisher: Thomson Reuters
    type: vendor
    url: "https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk"
    date: '2026-01-15'
    access: full
    locator: "Launch release, bullet list 'delivers measurable impact' and the 'Touchless Compliance' paragraph"
  - ref: ACCTODAY-AVALARA-2025
    title: "Avalara launches 'always on, always ready' AI agents"
    publisher: Accounting Today (Arizent)
    type: press
    url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents"
    date: '2025-09-30'
    access: full
    locator: Paragraphs on the Returns AI agent and on human review of novel situations
  - ref: FONOA-BLOG-2026
    title: What 176 Tax Leaders Have to Say About AI Adoption in Indirect Tax
    publisher: Fonoa
    type: survey
    url: "https://www.fonoa.com/resources/blog/ai-adoption-indirect-tax-report"
    date: '2026-06-30'
    access: full
    locator: "Sections 'Most tax teams can't govern their AI outputs' and 'AI tax decisions face an audit defensibility gap'"
  - ref: KPMG-INDIRECT-2026
    title: "Benchmarking Indirect Tax in a data-driven era: 2026 KPMG Indirect Tax Benchmarking Survey"
    publisher: KPMG International
    type: survey
    url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf"
    date: 2026-05
    access: full
    locator: "Pages 5-7 (data quality, ERP fitness, headcount expectation)"
  last_reviewed: '2026-10-17'
  notes: "Grade C: the only outcome figures are vendor claims. 'Available now' per the release, but no named customer deployment was found. Avalara's own 9 Apr 2026 release (AI-executed workflows, exemption certificates) was not retrievable."
- id: tax-indirect-tax-02
  title: "Retrieval-grounded VAT place-of-supply and advisory assistant, verified by a tax adviser"
  archetype: tax
  module: indirect-tax
  function: service-delivery
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Clients describe VAT cases in free-text emails, and advisers must determine the place of supply and justify it from statute and guidance. The study's authors note that VAT applies to nearly all transactions and that errors in legal interpretation carry significant financial consequences."
  solution: "A language model answers the client inquiry using retrieved passages of Austrian and EU VAT law and returns a place-of-supply decision with a justification that cites the legal sources. A tax adviser checks the answer. The authors call this 'verified decision-making'."
  outcomes:
  - lever: quality
    description: "Place-of-supply accuracy on textbook cases: retrieval-augmented configuration versus the plain model"
    figure: "93.24% (RAG) versus 68.92% (plain GPT-4o)"
    measures: share of 74 textbook VAT cases where the predicted country of the place of supply matched the expected country
    provenance: independent
    source_ref: LUKETINA-VAT-2026
  - lever: quality
    description: Correct analyses on real client inquiries from a tax consultancy
    figure: "16 of 20 (80%) for RAG; 14 of 20 (70%) fine-tuned; 11 of 20 (55%) RAG plus fine-tuning; 13 of 20 (65%) long-context GPT-4.1"
    measures: number of 20 anonymised real-world VAT inquiries from ICON Wirtschaftstreuhand GmbH whose returned analysis was judged factually correct
    provenance: independent
    source_ref: LUKETINA-VAT-2026
  prerequisites:
  - "Indexed corpus of the relevant VAT statute, guidance and cases"
  - Anonymised case data for testing
  - Structured background on each client (the authors suggest a knowledge graph) because advisers rely on implicit client knowledge and attachments the model never saw
  risks_and_guardrails:
  - "The authors write that an error rate of 20-30% in VAT case decisions is unacceptable in practice and that LLM-only decision-making is insufficient (LUKETINA-VAT-2026, Sect. 9.2)"
  - "Justifications can cite the wrong paragraph or hallucinate added detail; automatic contradiction checks are not possible (LUKETINA-VAT-2026, Sect. 8.1 and 9.1)"
  - "Chain transactions were the hardest pattern for fine-tuned configurations (LUKETINA-VAT-2026, Sect. 8.2)"
  - Under the UK PCRT guidance a member remains responsible for work produced with AI and should be able to explain how a conclusion was reached (ICAEW-PCRT-2026)
  human_checkpoints:
  - Tax adviser approves the AI analysis before it reaches the client
  - Adviser checks every cited paragraph against the source
  role_evolution: "The authors describe the adviser as the human in the loop who verifies the assistant's answer and keeps ultimate responsibility; the tool supplies a first analysis and a cross-check."
  evidence_grade: A
  sources:
  - ref: LUKETINA-VAT-2026
    title: "Using Large Language Models for Legal Decision-Making in Austrian Value-Added Tax Law: A Comparative Study (arXiv 2507.08468 v2; Journal of Business Analytics 2026; v1 11 Jul 2025)"
    publisher: University of Applied Sciences Upper Austria and Johannes Kepler University Linz
    type: academic
    url: "https://arxiv.org/abs/2507.08468"
    date: '2026-09-02'
    access: full
    locator: "Sect. 4.2 (p. 14, real-world data); Sect. 8.1 Table 5 (p. 27); Sect. 8.2 (pp. 30-32); Sect. 9.2 (pp. 33-34)"
  - ref: ICAEW-PCRT-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW
    type: professional-body
    url: "https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax"
    date: 2026-01
    access: full
    locator: "'Key messages' and 'Fundamental principles' sections"
  last_reviewed: '2026-10-17'
  notes: "Grade A is for the measured outcome from a named academic team using real cases from a named consultancy. It is a research prototype on one country's law, not a deployed tool. Small real-world sample (20); RAG versus fine-tuning difference not significant (McNemar p = 0.683). Used GPT-4o and a naive RAG design, so the figures are dated by model generation."
- id: tax-indirect-tax-03
  title: Deterministic rule engine as validator and oracle around LLM agents for cross-border VAT determination (idea)
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - transaction-processing
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "LLM agents that classify, locate, rate, exempt and apply reverse charge can fail silently. In one study, retrieval-based and fine-tuned set-ups got 20-30% of real-world VAT analyses wrong."
  solution: "Idea: split cross-border VAT determination into auditable steps (classification, jurisdiction, rate, exemption, reverse charge), let model agents handle the language and lookup steps, and check every step against a deterministic rule engine. Both the Austrian VAT study's authors and an agent-design pilot point to combining language models with law-based rules for the final decision."
  outcomes:
  - lever: quality
    description: "None published from a deployment. A preprint pilot on synthetic, oracle-labelled cases found a tuned single agent at 0.755 accuracy and the best orchestrated set-ups at 0.830; one schema-valid hallucinated record degraded every set-up"
    figure: "0.755 (single agent) versus 0.830 (best orchestrated); 4,400 runs"
    measures: final-answer accuracy over 40 oracle-labelled synthetic cross-border VAT cases with five repeats per condition
    provenance: independent
    source_ref: SANTOS-VAT-2026
  prerequisites:
  - A maintained rule set that can act as oracle for the cases in scope
  - Step-level logging so errors can be localised to jurisdiction or reverse-charge steps
  risks_and_guardrails:
  - "The pilot is one workload, one model family and synthetic failure injection; the author calls the result directional (SANTOS-VAT-2026, abstract and Sect. 1)"
  - "Availability faults were absorbed at every granularity, but a single schema-conforming hallucinated record degraded all configurations and hit fragmented ones hardest (SANTOS-VAT-2026, abstract)"
  - "The VAT study's authors recommend using language models for natural-language processing and initial analysis, with law-based rules for the final decision (LUKETINA-VAT-2026, Sect. 9.2)"
  human_checkpoints:
  - Tax expert approves outputs the rule engine cannot confirm
  - Review of rule-set changes
  role_evolution: The function would own the rule oracle and its maintenance. No source describes role changes from a deployment.
  evidence_grade: D
  sources:
  - ref: SANTOS-VAT-2026
    title: "Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep (arXiv 2608.23395, preprint by an independent researcher)"
    publisher: arXiv (Pedro Santos)
    type: academic
    url: "https://arxiv.org/abs/2608.23395"
    date: '2026-08-24'
    access: full
    locator: Abstract; Sect. 1 (pp. 1-2); Table 1 (p. 16)
  - ref: LUKETINA-VAT-2026
    title: "Using Large Language Models for Legal Decision-Making in Austrian Value-Added Tax Law: A Comparative Study (arXiv 2507.08468 v2; Journal of Business Analytics 2026; v1 11 Jul 2025)"
    publisher: University of Applied Sciences Upper Austria and Johannes Kepler University Linz
    type: academic
    url: "https://arxiv.org/abs/2507.08468"
    date: '2026-09-02'
    access: full
    locator: Sect. 9.2 (p. 34)
  last_reviewed: '2026-10-17'
  notes: "Idea: labelled D because no deployment was found. The accuracy figures come from a research pilot on synthetic cases by an independent researcher (preprint, not peer reviewed as far as the page shows). Pattern 'other': a model proposes and a rule engine verifies each step."
- id: tax-indirect-tax-04
  title: Generative AI assistant for state tax agency staff answering sales and use tax enquiries
  archetype: tax
  module: indirect-tax
  function: customer-service
  work_types:
  - client-interaction
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "California's CDTFA runs 42 tax and fee programs, including sales and use tax, and its customer service staff must research complex laws to answer taxpayers by phone and live chat."
  solution: "CDTFA gave agents a generative AI tool that searches more than 16,000 pages of the department's reference material and cites the statute or publication it draws on. Agents choose when to use it and review the output before telling the taxpayer verbally. The department said it launched the tool on 22 Aug 2025."
  outcomes:
  - lever: quality
    description: "Accuracy change in the vendor's 2024 sandbox test, as reported from a December 2024 evaluation report"
    figure: "-6% in phase 1, +4% in phase 2"
    measures: "accuracy of the generative AI program's responses in the first and second sandbox phases, as worded in the Tax Notes report; the baseline and the question set are not stated"
    provenance: self-reported
    source_ref: TAXNOTES-CDTFA-2025
  prerequisites:
  - A curated corpus of agency publications and law guides
  - A sandbox period with agents testing accuracy before launch (CDTFA ran sandboxes with two vendors in 2024)
  - "Contract for the tool (the article gives $444,600 with SymSoft Solutions)"
  risks_and_guardrails:
  - "Taxpayers who rely on written advice are excused from liabilities, but CDTFA Publication 70 does not extend this to verbal advice, which is how agents deliver AI-assisted answers (TAXNOTES-CDTFA-2025, p. 2)"
  - "Testing agents worried that newer staff could not tell whether AI answers were wrong or incomplete (TAXNOTES-CDTFA-2025, p. 3)"
  - "An EFF adviser called the use case 'extremely high-risk' and urged that humans review responses and not rubber-stamp them (TAXNOTES-CDTFA-2025, pp. 1-4)"
  - "Werfel's risk register lists hallucination and unauthorised reliance on chatbot output as tax-authority risks, with controls such as source citations and escalation triggers (AICPA-WERFEL-2026, Appendix A, risks 1 and 4)"
  human_checkpoints:
  - Agent decides whether the AI answer is appropriate and reviews it before speaking to the taxpayer
  - "Taxpayers' Rights Advocate Office reviews disputed advice"
  role_evolution: Customer service agents become reviewers of retrieved answers. CDTFA says agents are not required to use the tool and can still ask colleagues or search manually.
  evidence_grade: A
  sources:
  - ref: TAXNOTES-CDTFA-2025
    title: "Experts Urge Caution as State Tax Agencies Deploy Generative AI (Tax Notes, DOC 2025-24791; copy hosted by American University Kogod School)"
    publisher: Tax Notes (Tax Analysts)
    type: press
    url: "https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf"
    date: '2025-08-26'
    access: full
    locator: "pp. 1-4: 'Among the First', 'Documented Material', 'Background', 'Risks, Taxpayer Protections'"
  - ref: TAXNOTESTALK-2025
    title: "Artificial Intelligence and State Tax Agencies (Tax Notes Talk; interview with Ryan Minnick, Federation of Tax Administrators)"
    publisher: Tax Notes Talk
    type: podcast
    url: "https://taxnotestalk.taxnotes.com/124942/episodes/17439828-artificial-intelligence-and-state-tax-agencies"
    date: '2025-07-04'
    access: full
    locator: Interview segment on the CDTFA project and the 2024 FTA/EY survey
  - ref: AICPA-WERFEL-2026
    title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and B (Danny Werfel)"
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf"
    date: 2026-06
    access: full
    locator: "Appendix A risk register, risks 1 (hallucination) and 4 (over-trust)"
  last_reviewed: '2026-10-17'
  notes: "Grade A for a named agency with a reported measurement and a production launch. The measure is thin: the wording of the sandbox result is ambiguous, and the source is a news report of an agency document obtained by public-records request. Production accuracy since 22 Aug 2025 was not found. FTA's 2024 survey (37 state agencies and two city departments) reports 15% piloting or using AI in core functions, but FTA's COO cautions this mainly reflects machine learning, not generative AI in production (TAXNOTESTALK-2025)."
- id: tax-indirect-tax-05
  title: Audit-ready decision records for AI-assisted indirect tax determinations and filings
  archetype: tax
  module: indirect-tax
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Indirect tax teams use AI without being able to show an authority which rule was applied, who reviewed the output and who approved it. In Fonoa's survey of 176 leaders, 57.4% would not be confident defending an AI-assisted decision to a tax authority."
  solution: "Log each AI-assisted determination, override and approval with the rule version, data inputs and reviewer, so the file can be assembled on demand when an authority asks. Fonoa and Sovos both describe products that record every recommendation, approval and action. Werfel's tax-authority case study lists a tamper-proof log of every output among the vendor questions to answer before signing."
  outcomes:
  - lever: risk
    description: Organisations with formal human-in-the-loop governance were more than twice as likely to be confident defending AI decisions as those with no defined process
    figure: more than 2x
    measures: "relative likelihood of confidence in defending AI-assisted decisions to a tax authority, formal human-in-the-loop versus no defined process, among 176 surveyed indirect tax leaders"
    provenance: vendor-published
    source_ref: FONOA-BLOG-2026
  - lever: capacity
    description: Compliance workload fell at eight times the rate of other respondents among organisations that reached full formalisation
    figure: "8x (2.8% of organisations reached full formalisation)"
    measures: "rate of decrease in compliance workload for the cohort with mandates, formal governance and measurement versus other respondents; the exact basis of the rate is not shown on the landing page or blog"
    provenance: vendor-published
    source_ref: FONOA-BLOG-2026
  prerequisites:
  - A defined validation process with named reviewers (only about a third of respondents have a formal documented sign-off)
  - "Specific AI KPIs set by leadership (12.5% have them)"
  - "Logging of inputs, model version and rationale"
  risks_and_guardrails:
  - The evidence is a vendor-sponsored survey and product claims; Fonoa sells an audit-trail product (FONOA-INDIRECT-2026)
  - "IRS OPR asks firms to document AI usage and verification and to show adherence to Circular 230 section 10.36, for federal tax practice (IRS-OPR-2026)"
  - The UK PCRT guidance expects members to be able to explain how a conclusion was arrived at (ICAEW-PCRT-2026)
  - "Werfel's vendor-diligence questions ask whether the department can access a tamper-proof log of every output without relying on the vendor (AICPA-WERFEL-2026, Appendix B, Case Study 1, Step 6)"
  human_checkpoints:
  - Named human owner for each AI-supported decision
  - Formal sign-off at defined risk points
  role_evolution: "Sovos says every recommendation, approval and action is documented for governance visibility. Fonoa's survey frames the tax leader's role as defining KPIs and accountability, not only using tools."
  evidence_grade: C
  sources:
  - ref: FONOA-BLOG-2026
    title: What 176 Tax Leaders Have to Say About AI Adoption in Indirect Tax
    publisher: Fonoa
    type: survey
    url: "https://www.fonoa.com/resources/blog/ai-adoption-indirect-tax-report"
    date: '2026-06-30'
    access: full
    locator: "Sections 'Most tax teams can't govern', 'audit defensibility gap' and 'AI accountability separates the leaders'"
  - ref: FONOA-INDIRECT-2026
    title: State of Indirect Tax in the AI Era 2026 (landing page; full report is form-gated)
    publisher: Fonoa
    type: survey
    url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026"
    date: '2026-06-17'
    access: full
    locator: "Sections on AI governance, diagnostic checklist and Fonoa Audit"
  - ref: SOVOS-SOVI-2026
    title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability"
    publisher: Sovos
    type: vendor
    url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/"
    date: '2026-03-24'
    access: full
    locator: "Capability list item 'Full Audit Transparency'"
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70"
    date: '2026-06-24'
    access: full
    locator: "Circular 230 section 10.36 discussion and 'Best Practices' list"
  - ref: ICAEW-PCRT-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW
    type: professional-body
    url: "https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax"
    date: 2026-01
    access: full
    locator: "'Fundamental principles', Integrity"
  - ref: AICPA-WERFEL-2026
    title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and B (Danny Werfel)"
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf"
    date: 2026-06
    access: full
    locator: "Appendix B, Case Study 1, Step 6 vendor-diligence questions (PDF pp. 20-21)"
  last_reviewed: '2026-10-17'
  notes: "Pattern 'other': decision logging and evidence assembly. Fonoa's full report is gated, so figures come from its landing page and blog. A UK Tax Adviser magazine article on 'actionability and auditability' for indirect tax was read but its date and author could not be confirmed, so it is not cited."
- id: tax-indirect-tax-06
  title: "Tax-authority machine-learning risk scoring on VAT, invoice and transaction data"
  archetype: tax
  module: indirect-tax
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Tax administrations hold large volumes of returns, invoices and customs data that overwhelm manual audit selection, and VAT fraud is a stated driver of the EU's move to transaction-level reporting."
  solution: "Models score cases across income, corporate and value added tax and customs data, and officers review flagged cases. Austria's Predictive Analytics Competence Centre has done this since 2014. The EU's ViDA directive will give tax administrations transaction-by-transaction invoice data for cross-matching, and HMRC plans real-time risking on VAT submissions that feeds prompts during filing."
  outcomes:
  - lever: cost
    description: Additional tax revenue attributed to Austrian risk models in 2023
    figure: approximately EUR 185 million
    measures: "additional tax revenue the Austrian finance ministry attributes to models run on about 6.5 million cases across income, corporate and value added tax and customs; not split out for VAT"
    provenance: self-reported
    source_ref: OECD-GOVAI-2025
  - lever: capacity
    description: Cases examined and flagged by the Austrian models in 2023
    figure: "nearly 27.5 million examined; 375,000 flagged"
    measures: "cases examined for compliance and cases flagged for further review because of implausible risk profiles, all tax types"
    provenance: self-reported
    source_ref: OECD-GOVAI-2025
  prerequisites:
  - "Accurate, complete, well-structured input data (the OECD says poor data quality is a significant risk to effective outcomes)"
  - A legal basis for use; Hadwick finds most EU Member States lack one
  - Structured e-invoice data from digital reporting requirements
  risks_and_guardrails:
  - "Skewed data can cause improper targeting of some groups for audit; the OECD lists explainability, taxpayer rights and trust as particular demands in tax administration (OECD-GOVAI-2025, pp. 173-174)"
  - "Hadwick counts at least 85 AI systems in 26 EU Member States and argues that AI Act Recital 59 lets administrative tax systems escape the law-enforcement high-risk category (HADWICK-EUAIACT, Sects. II.2 and III.2)"
  human_checkpoints:
  - Flagged cases go for further review (OECD Box 5.3)
  - "HMRC's roadmap describes an AI casework assistant for caseworkers, not automated assessment (Section 6.1)"
  role_evolution: "KPMG's 2026 survey foreword says authorities are moving to real-time, data-driven oversight and indirect tax professionals are likely to become data managers and gatekeepers of ERP changes. HMRC expects intermediaries and software to take on a larger role."
  evidence_grade: B
  sources:
  - ref: OECD-GOVAI-2025
    title: "Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions (chapter 5, AI in tax administration)"
    publisher: OECD
    type: regulator
    url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf"
    date: 2025-09
    access: full
    locator: "Chapter 5, Box 5.3 (p. 171) and pp. 173-174 on risks"
  - ref: EU-DIRECTIVE-2025-516
    title: Council Directive (EU) 2025/516 amending Directive 2006/112/EC as regards VAT rules for the digital age
    publisher: Council of the European Union
    type: regulator
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0516"
    date: '2025-03-11'
    access: full
    locator: "Recitals (4), (5), (11): transaction-by-transaction information and structured electronic invoices"
  - ref: EC-VIDA-2025
    title: "VAT in the Digital Age (ViDA) (page undated; adoption 11 Mar 2025, OJ 25 Mar 2025)"
    publisher: "European Commission, DG TAXUD"
    type: regulator
    url: "https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en"
    date: 2025-03
    access: full
    locator: Section on real-time digital reporting requirements (carousel fraud; fraud-reduction estimate)
  - ref: HMRC-ROADMAP-2025
    title: "HMRC's Transformation Roadmap"
    publisher: "HM Revenue & Customs"
    type: regulator
    url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap"
    date: '2025-07-21'
    access: full
    locator: Section 4.1 (real time risking for VAT); Section 6.1
  - ref: HADWICK-EUAIACT
    title: "Slipping Through the Cracks, the Carve-outs for AI Tax Enforcement Systems in the EU AI Act (European Papers, Vol. 9, No 3, pp. 936-955)"
    publisher: "European Papers (David Hadwick, University of Antwerp)"
    type: academic
    url: "https://www.europeanpapers.eu/e-journal/slipping-through-cracks-carve-outs-ai-tax-enforcement-systems-eu-ai-act"
    date: '2024-12-30'
    access: full
    locator: Sects. II.2 and III.2
  - ref: KPMG-INDIRECT-2026
    title: "Benchmarking Indirect Tax in a data-driven era: 2026 KPMG Indirect Tax Benchmarking Survey"
    publisher: KPMG International
    type: survey
    url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf"
    date: 2026-05
    access: full
    locator: Foreword
  last_reviewed: '2026-10-17'
  notes: "Grade capped at B: the Austrian figure covers income, corporate and value added tax and customs together, not VAT alone. The EU Commission estimates e-invoicing and reporting could cut VAT fraud by up to EUR 11 billion a year (EC-VIDA-2025), a projection not an AI measurement. This entry is the authority-side counterpart that taxpayers' own controls must meet."
- id: tax-indirect-tax-07
  title: AI diagnosis and approved remediation of e-invoicing and VAT filing errors
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "E-invoicing and digital reporting mandates are spreading (EU ViDA digital reporting for cross-border B2B from 1 Jul 2030; Member States may introduce mandatory domestic e-invoicing since ViDA entered into force on 14 Apr 2025), and ownership of e-invoicing is split: in KPMG's survey Finance owns it for 38%, Tax for 30% and IT for 11%."
  solution: "An in-platform assistant diagnoses root causes of compliance errors, proposes fixes and executes corrections once a user approves, and flags problems before filing deadlines. Sovos announced this as part of Sovi AI on 24 Mar 2026."
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: "no measured figure; Sovos describes capabilities and says they are 'available now or rolling out'"
    provenance: vendor-published
    source_ref: SOVOS-SOVI-2026
  prerequisites:
  - Invoices issued in a structured format that follows the European standard EN 16931 (the ViDA directive says electronic invoices should in principle comply with it)
  - "A clear owner across Finance, Tax and IT"
  - "ERP data fit for the purpose (23% of KPMG respondents say theirs is)"
  risks_and_guardrails:
  - "Corrections are executed by the vendor's AI after user approval, so the approval record is the control (SOVOS-SOVI-2026)"
  - Sovos says customer data stays inside its security perimeter and is not used to train external models (SOVOS-SOVI-2026)
  - "About a third of KPMG respondents still rely on country-specific e-invoicing tools, which fragments control (KPMG-INDIRECT-2026, p. 11)"
  human_checkpoints:
  - User approves each proposed correction before execution
  - Tax review of recurring root causes
  role_evolution: "KPMG expects indirect tax teams to take on e-invoicing (33% already own it) and data management; 30% of respondents place e-invoicing with Tax or Tax Technology."
  evidence_grade: C
  sources:
  - ref: SOVOS-SOVI-2026
    title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability"
    publisher: Sovos
    type: vendor
    url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/"
    date: '2026-03-24'
    access: full
    locator: "Capability list 'Problem-to-Resolution Guidance'; closing paragraph on availability"
  - ref: EU-DIRECTIVE-2025-516
    title: Council Directive (EU) 2025/516 amending Directive 2006/112/EC as regards VAT rules for the digital age
    publisher: Council of the European Union
    type: regulator
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0516"
    date: '2025-03-11'
    access: full
    locator: Recital (6) on EN 16931; digital reporting requirements from 1 Jul 2030
  - ref: EC-VIDA-2025
    title: "VAT in the Digital Age (ViDA) (page undated; adoption 11 Mar 2025, OJ 25 Mar 2025)"
    publisher: "European Commission, DG TAXUD"
    type: regulator
    url: "https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en"
    date: 2025-03
    access: full
    locator: Timeline paragraphs
  - ref: KPMG-INDIRECT-2026
    title: "Benchmarking Indirect Tax in a data-driven era: 2026 KPMG Indirect Tax Benchmarking Survey"
    publisher: KPMG International
    type: survey
    url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf"
    date: 2026-05
    access: full
    locator: Pages 6 and 11 (ERP fitness; e-invoicing ownership and solution approach)
  - ref: SOVOS-PRESS-2026
    title: Sovos press-release listing (France e-invoicing scale 23 Sep 2026; Flowie acquisition 1 Oct 2026; Cloud Security Alliance 15 Oct 2026); summaries only
    publisher: Sovos
    type: vendor
    url: "https://sovos.com/press-releases/"
    date: '2026-10-15'
    access: full
    locator: Listing item of 23 Sep 2026 on France e-invoicing
  last_reviewed: '2026-10-17'
  notes: "Vendor claim only. Sovos's 23 Sep 2026 release says it has more than 170,000 registrants three weeks into France's e-invoicing mandate (listing summary only, vendor claim); it does not report AI measures."
- id: tax-indirect-tax-08
  title: "Tax engines exposed to customers' own AI agents through governed MCP and agent-to-agent access"
  archetype: tax
  module: indirect-tax
  function: technology-it
  work_types:
  - software-systems
  - transaction-processing
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Tax calculation, classification, registration and filing sit inside tax applications, so enterprise AI agents and ERP or commerce systems need a controlled way to call them."
  solution: "Avalara describes 'have your agent call our agent': its agents and MCP servers let ERP, POS and commerce agents validate taxes, classify products, start registrations and file forms. Sovos is building an MCP gateway for governed access and expects to support agent-to-agent orchestration over time."
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: no measured figure in either vendor source
    provenance: vendor-published
    source_ref: SOVOS-SOVI-2026
  prerequisites:
  - Agent identity and access control
  - Logging of every agent call
  - "Configurations in the tax system that agents rely on ('those configurations still live in our system', per Avalara)"
  risks_and_guardrails:
  - "Sovos describes the MCP gateway as infrastructure being developed and A2A as expected to follow, not as shipped (SOVOS-SOVI-2026)"
  - "Sovos announced joining the Cloud Security Alliance on 15 Oct 2026 to give customers 'independently verifiable security' (vendor wording, listing summary) (SOVOS-PRESS-2026)"
  - "Werfel's vendor-diligence questions ask whether scope restrictions are enforced in the model and not only in the interface (AICPA-WERFEL-2026, Appendix B, Step 6)"
  - "NIST's AI RMF and its Generative AI Profile are voluntary frameworks for managing such risks (NIST-AIRMF-2023)"
  human_checkpoints:
  - Avalara says agents notify a human for novel situations and for key decisions that affect the compliance footprint
  role_evolution: Avalara describes agents as a new front door to its applications. No source describes role changes at customers.
  evidence_grade: C
  sources:
  - ref: ACCTODAY-AVALARA-2025
    title: "Avalara launches 'always on, always ready' AI agents"
    publisher: Accounting Today (Arizent)
    type: press
    url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents"
    date: '2025-09-30'
    access: full
    locator: "Paragraphs on 'Have your agent call our agent' and MCP servers"
  - ref: ITWIRE-AVALARA-2025
    title: "Avalara Launches Agentic Tax and Compliance: AI Agents That Work for You (company news)"
    publisher: iTWire / Avalara
    type: vendor
    url: "https://itwire.com/business-it-news/data/avalara-launches-agentic-tax-and-compliance-ai-agents-that-work-for-you"
    date: '2025-10-01'
    access: full
    locator: ALFA framework description and product list
  - ref: SOVOS-SOVI-2026
    title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability"
    publisher: Sovos
    type: vendor
    url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/"
    date: '2026-03-24'
    access: full
    locator: Paragraph on the Sovos MCP Gateway
  - ref: SOVOS-PRESS-2026
    title: Sovos press-release listing (France e-invoicing scale 23 Sep 2026; Flowie acquisition 1 Oct 2026; Cloud Security Alliance 15 Oct 2026); summaries only
    publisher: Sovos
    type: vendor
    url: "https://sovos.com/press-releases/"
    date: '2026-10-15'
    access: full
    locator: Listing item of 15 Oct 2026
  - ref: AICPA-WERFEL-2026
    title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and B (Danny Werfel)"
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf"
    date: 2026-06
    access: full
    locator: "Appendix B, Step 6"
  - ref: NIST-AIRMF-2023
    title: "AI Risk Management Framework (AI RMF 1.0, released 26 Jan 2023; Generative AI Profile NIST-AI-600-1, 26 Jul 2024)"
    publisher: NIST
    type: standard-setter
    url: "https://www.nist.gov/itl/ai-risk-management-framework"
    date: '2023-01-26'
    access: full
    locator: Overview
  last_reviewed: '2026-10-17'
  notes: "Pattern 'other': agent-callable compliance services. No customer or incident data was found."
- id: tax-indirect-tax-09
  title: Tax determination and tax-holiday rules applied at AI-agent-initiated checkout
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - transaction-processing
  - expert-judgment
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: emerging
  problem: "When an AI agent searches, compares and buys for a consumer, the human checkpoint at checkout disappears. It is unclear who must collect tax, and time-bound rules such as sales tax holidays must be resolved correctly in real time."
  solution: "Keep tax calculation in the merchant or marketplace transaction flow, and make tax-engine rules, product mappings and catalogue metadata machine-readable so agent checkout flows can use them. The Sales Tax Institute says Shopify has structured its agentic commerce so tax calculation stays in the transaction flow and uses the merchant's tax infrastructure. Where an AI commerce app takes payment and sends orders, Aleksandra Bal (Stripe) argues it is likely to meet EU deemed-supplier or US marketplace-facilitator tests."
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: no measured outcome; practitioner commentary and a forum statement only
    provenance: independent
    source_ref: BTAX-OECDVAT-2026
  prerequisites:
  - Machine-readable holiday rules and rates in the tax engine
  - Catalogue metadata that correctly marks holiday-eligible items and price thresholds
  - Confirmation from the platform provider of how tax is calculated in agent-initiated flows
  risks_and_guardrails:
  - AI systems have no legal personality; liability attaches to the company operating the agent (BTAX-BAL-2026)
  - Small differences in checkout flow or payment authorisation can change the marketplace analysis (BTAX-BAL-2026)
  - Automation can speed up errors if thresholds or mappings are stale (STI-AGENTIC-2026)
  - "The OECD's VAT forum (26-29 Jan 2026) called AI and the crypto economy 'emerging challenges' for VAT administration (BTAX-OECDVAT-2026)"
  human_checkpoints:
  - Tax team audits whether engine holiday rules are current and machine-readable before each holiday season
  - Review of how the platform handles tax in agent flows
  role_evolution: "Tax teams must evaluate checkout configurations designed for machine buyers, and the Sales Tax Institute says they should ask platform providers specific questions about agent flows."
  evidence_grade: B
  sources:
  - ref: STI-AGENTIC-2026
    title: Will Your AI Shopping Agent Catch Your Sales Tax Holiday Discount?
    publisher: Sales Tax Institute
    type: press
    url: "https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays"
    date: '2026-07-29'
    access: full
    locator: "Sections 'Where the Responsibility Actually Lands' and the closing checklist"
  - ref: BTAX-BAL-2026
    title: "Artificial Intelligence Goes Shopping, Creates Tax Challenges (commentary by Aleksandra Bal, global tax technology lead at Stripe)"
    publisher: Bloomberg Tax
    type: press
    url: "https://news.bloombergtax.com/tax-insights-and-commentary/artificial-intelligence-goes-shopping-creates-tax-challenges"
    date: '2026-02-24'
    access: full
    locator: "Sections on EU Value-Added Tax, US Sales Tax and Practical Takeaway"
  - ref: BTAX-OECDVAT-2026
    title: OECD Identifies Crypto and AI As Challenges to VAT Systems (opening paragraphs only; rest paywalled)
    publisher: "Bloomberg Tax, Daily Tax Report International"
    type: press
    url: "https://news.bloombergtax.com/daily-tax-report-international/oecd-identifies-crypto-and-ai-as-challenges-to-vat-systems"
    date: '2026-01-29'
    access: full
    locator: Opening paragraphs
  last_reviewed: '2026-10-17'
  notes: "Grade B rests on the named Shopify design described second-hand by the Sales Tax Institute; no measurement exists. The McKinsey figure of USD 3-5 trillion in agent-orchestrated sales by 2030 and the Gartner expectation are quoted in Bal's article and were not checked at source. STI also reports, without verifying, that Visa, Mastercard and American Express announced agentic commerce initiatives by April 2026."
- id: tax-indirect-tax-10
  title: "AI prediction of product and service tax codes (HSN, SAC, Harmonized System) with hierarchical constraints and cited rules"
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - transaction-processing
  - expert-judgment
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Free-text product and service descriptions must be mapped to the right code, which sets customs duty and tax treatment. Dell's authors call HSN and SAC code determination a major tax-compliance use case, and a customs paper says misclassification can bring duty adjustments, shipment holds and penalties."
  solution: Two designs appear in the research. Dell trained small encoder-decoder models that generate the hierarchical HSN or SAC code step by step with constrained decoding. A Shanghai Jiao Tong team with Chinese customs co-authors built a fixed-flow workflow in which model calls handle narrow stages and each decision cites section and chapter notes. Avalara lists Item Classification among its products with agents.
  outcomes:
  - lever: quality
    description: "Dell's best small model (T5) against codes assigned by tax and procurement experts"
    figure: "precision 70%, recall 61%, F1 65%"
    measures: "agreement of T5 predictions with expert-assigned HSN/SAC codes on a curated test set of 16,000 records; code level and averaging method not stated"
    provenance: self-reported
    source_ref: NATH-DELL-2025
  - lever: quality
    description: "Accuracy of the six-digit Harmonized System code on an e-commerce benchmark (customs setting, adjacent)"
    figure: "64.2% top-1; 78.3% top-3 at six digits; 75.0% top-1; 91.5% top-3 at four digits"
    measures: "share of the 632 HSCodeComp product entries for which the gold code appeared at rank 1 or within the top 3, using a frontier proprietary model"
    provenance: independent
    source_ref: ZHANG-HS-2026
  prerequisites:
  - Expert-labelled training and test records (Dell used codes assigned by tax and procurement experts)
  - Tariff text including section and chapter notes for the rule-citing design
  - Monitoring for data drift (Dell reports sensitivity in later months)
  risks_and_guardrails:
  - "Dell's best model reached 70% precision and 61% recall on its test set, so expert review stays necessary (NATH-DELL-2025, Sect. 3)"
  - "Dell reports fluctuating agreement with experts in later months and attributes it to sensitivity to data drift (NATH-DELL-2025, Sect. 3)"
  - "End-to-end prompting of language models fails by resolving one axis (material, form, function) and ignoring others (ZHANG-HS-2026, abstract)"
  - "The customs authors' manual audit of 226 disagreements suggests some benchmark labels may deviate from the general rules (ZHANG-HS-2026, abstract)"
  - "Frontier models compute fewer than a third of simplified US personal income tax returns correctly, which shows unaided models are weak at rule-heavy tax tasks (COLUMN-TAXCALCBENCH-2025, abstract; adjacent)"
  human_checkpoints:
  - Tax experts review predictions below a confidence threshold or in disputed headings
  - Customs officers or declarants audit the cited decision stages
  role_evolution: "Dell compares predictions with tax and procurement experts' labels; the customs authors say stage-wise outputs let officers and declarants audit decisions. Neither describes role changes."
  evidence_grade: A
  sources:
  - ref: NATH-DELL-2025
    title: Domain-Adaptive Small Language Models for Structured Tax Code Prediction (arXiv 2507.10880)
    publisher: "Dell Technologies (authors Nath, Wadhwa, Perez)"
    type: academic
    url: "https://arxiv.org/abs/2507.10880"
    date: '2025-07-19'
    access: full
    locator: "Abstract; Sect. 3 Table 1 and Cohen's kappa discussion"
  - ref: ZHANG-HS-2026
    title: "A Deterministic Agentic Workflow for HS Tariff Classification: Multi-Dimensional Rule Reasoning with Interpretable Decisions (arXiv 2605.14857)"
    publisher: Shanghai Jiao Tong University with Chinese customs (GACC) co-authors
    type: academic
    url: "https://arxiv.org/abs/2605.14857"
    date: '2026-05-14'
    access: full
    locator: Abstract; Table I (n = 632); Sect. IV
  - ref: COLUMN-TAXCALCBENCH-2025
    title: "TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126; personal income tax, adjacent to this module)"
    publisher: Column Tax
    type: academic
    url: "https://arxiv.org/abs/2507.16126"
    date: '2025-07-22'
    access: full
    locator: Abstract
  - ref: ITWIRE-AVALARA-2025
    title: "Avalara Launches Agentic Tax and Compliance: AI Agents That Work for You (company news)"
    publisher: iTWire / Avalara
    type: vendor
    url: "https://itwire.com/business-it-news/data/avalara-launches-agentic-tax-and-compliance-ai-agents-that-work-for-you"
    date: '2025-10-01'
    access: full
    locator: Product list
  last_reviewed: '2026-10-17'
  notes: "Grade A rests on Dell's measured test-set result for HSN/SAC code prediction (named company, tax-code determination). The paper does not say whether the model is in production; the Cohen's kappa of 0.47 for T5 over eight months suggests operational data, but that is not stated. The Zhang result is Harmonized System classification in a customs setting, adjacent to VAT taxability mapping, so it is context and not the basis for the grade. Related to a customs module if one exists."
- id: tax-indirect-tax-11
  title: "Sanctioned enterprise AI workspace for indirect tax research and exception handling, replacing unvetted public tools"
  archetype: tax
  module: indirect-tax
  function: risk-compliance-legal
  work_types:
  - research-synthesis
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Most indirect tax professionals use public generative AI tools, often without governance. When exception handling or rate research runs through an unvetted tool, the organisation loses sight of what data the tool touched and what oversight applied."
  solution: "Provide approved, grounded tools with logging and a use policy, so research and exception triage happen in an environment the tax function can see."
  outcomes:
  - lever: risk
    description: "Organisations relying primarily on individuals using public AI tools without governance, oversight or audit trail"
    figure: "60.8%"
    measures: share of 176 surveyed indirect tax organisations whose AI use rests mainly on individuals using public tools
    provenance: vendor-published
    source_ref: FONOA-BLOG-2026
  - lever: risk
    description: Corporate professionals using AI tools their organisation has not sanctioned
    figure: "36%"
    measures: "share of corporate professionals in Thomson Reuters' 2026 Future of Professionals data; the sample size is not stated in the blog"
    provenance: vendor-published
    source_ref: TR-INDIRECT-2026
  prerequisites:
  - "An approved-use policy and an owner for tax AI (at TEI's Tax Tech seminar, two hands of more than 50 said the tax function owns AI implementation at their company)"
  - Vetting of third-party AI tools
  risks_and_guardrails:
  - "Entering a client's data into a public model without consent is likely to breach confidentiality (ICAEW-PCRT-2026, Confidentiality)"
  - "IRS OPR asks practitioners to use secure, enterprise-approved AI and not to upload sensitive data to unsecured sites; the alert addresses federal tax return information (IRS-OPR-2026)"
  - "The EU AI Act requires providers and deployers to take measures to ensure sufficient AI literacy of staff (EU-AIACT-2024, Art. 4)"
  - "TEI attendees described silent hallucinations and the difficulty of reviewing growing volumes of 'polite, quiet, and technical' errors (TEI-TAXTECH-2026)"
  human_checkpoints:
  - Named owner approves tools and use cases
  - Reviewer checks AI research output against primary sources
  role_evolution: The TEI recap says tax rarely owns AI implementation; the survey sources suggest tax leaders need to take a design role in decision flows and guardrails.
  evidence_grade: C
  sources:
  - ref: FONOA-BLOG-2026
    title: What 176 Tax Leaders Have to Say About AI Adoption in Indirect Tax
    publisher: Fonoa
    type: survey
    url: "https://www.fonoa.com/resources/blog/ai-adoption-indirect-tax-report"
    date: '2026-06-30'
    access: full
    locator: "Section 'AI adoption pressure is near universal, clear targets are not'"
  - ref: TR-INDIRECT-2026
    title: What three years of data reveal about AI in corporate indirect tax
    publisher: "Thomson Reuters Tax & Accounting"
    type: vendor
    url: "https://tax.thomsonreuters.com/blog/what-three-years-of-data-reveal-about-ai-in-corporate-indirect-tax/"
    date: '2026-08-27'
    access: full
    locator: "Section '2026: The data caught up'"
  - ref: TEI-TAXTECH-2026
    title: "TEI Tax Tech 2026: the man behind the curtain (recap of the 27-29 Apr 2026 TEI Tax Technology Seminar)"
    publisher: Thomson Reuters Institute
    type: conference
    url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain"
    date: '2026-05-04'
    access: full
    locator: Passages on governance vacuums and the ownership poll
  - ref: ICAEW-PCRT-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW
    type: professional-body
    url: "https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax"
    date: 2026-01
    access: full
    locator: "Fundamental principles: Confidentiality"
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70"
    date: '2026-06-24'
    access: full
    locator: Circular 230 section 6713/7216 paragraph and best-practice list
  - ref: EU-AIACT-2024
    title: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act)
    publisher: European Parliament and Council
    type: regulator
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689"
    date: '2024-06-13'
    access: full
    locator: Article 4 (AI literacy)
  last_reviewed: '2026-10-17'
  notes: "Evidence is survey data from vendors and a trade recap, so grade C. The TR blog also reports that 65% of tax professionals use GenAI tools yet only 26% measure the resulting return; the denominators are not defined in the blog."
- id: tax-indirect-tax-12
  title: AI-assisted repair of tax-relevant master and transaction data before it reaches returns and e-invoices (idea)
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "In KPMG's survey of 53 large multinationals, 58% name data quality as their biggest VAT/GST concern (44% in 2021), 61% correct data predominantly manually, and 23% say their ERP is fit for purpose."
  solution: "Idea: use AI to detect and correct tax-relevant data errors at source, for example classification, party and registration data, so fewer manual corrections are needed. KPMG's respondents say AI is mainly a way to improve data quality and not to cut headcount. HMRC's roadmap says AI-enabled bookkeeping tools can now recommend tax categories using business context."
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: "no measured outcome; 49% of KPMG respondents said improving data quality 'will be' their primary AI use case, which is an intention"
    provenance: independent
    source_ref: KPMG-INDIRECT-2026
  prerequisites:
  - ERP and source-system integration
  - "Controls embedded at source (KPMG's recommended action)"
  - Technology specialists (about one third of respondents have none on the indirect tax team)
  risks_and_guardrails:
  - "Fragmented, legacy ERP data makes AI harder to apply (KPMG-INDIRECT-2026, p. 6)"
  - Fonoa finds AI use concentrated in research and drafting rather than the data reconciliation and return preparation where volume sits (FONOA-BLOG-2026)
  - "OECD warns that poor data quality undermines AI reliability in tax administration, a risk equally relevant to taxpayers' data (OECD-GOVAI-2025, p. 173)"
  human_checkpoints:
  - Tax team approves rule changes that alter tax codes or party data
  - Exception review
  role_evolution: "KPMG's foreword says indirect tax professionals are likely to become data managers and ERP-change gatekeepers."
  evidence_grade: D
  sources:
  - ref: KPMG-INDIRECT-2026
    title: "Benchmarking Indirect Tax in a data-driven era: 2026 KPMG Indirect Tax Benchmarking Survey"
    publisher: KPMG International
    type: survey
    url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf"
    date: 2026-05
    access: full
    locator: Pages 5-7 and the foreword (p. 2)
  - ref: HMRC-ROADMAP-2025
    title: "HMRC's Transformation Roadmap"
    publisher: "HM Revenue & Customs"
    type: regulator
    url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap"
    date: '2025-07-21'
    access: full
    locator: "Section 6.1 case study 'AI-enabled products for tax purposes'"
  - ref: FONOA-BLOG-2026
    title: What 176 Tax Leaders Have to Say About AI Adoption in Indirect Tax
    publisher: Fonoa
    type: survey
    url: "https://www.fonoa.com/resources/blog/ai-adoption-indirect-tax-report"
    date: '2026-06-30'
    access: full
    locator: "Section 'AI adoption hasn't reduced indirect tax workload'"
  - ref: OECD-GOVAI-2025
    title: "Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions (chapter 5, AI in tax administration)"
    publisher: OECD
    type: regulator
    url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf"
    date: 2025-09
    access: full
    locator: p. 173
  last_reviewed: '2026-10-17'
  notes: "Idea: labelled D because the sources show stated intentions and a regulator's observation, not a deployment. The 49% is the share of KPMG respondents reporting that their primary use case for AI will be to improve data quality."
- id: tax-indirect-tax-13
  title: Tax-authority chatbot with a language-model engine for taxpayer queries including GST
  archetype: tax
  module: indirect-tax
  function: customer-service
  work_types:
  - client-interaction
  pattern: service-agent-escalation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Taxpayer enquiries on VAT or GST and other taxes are handled through call centres and offices, which is labour intensive."
  solution: "Singapore's IRAS has run a chatbot since 2021 covering individual income tax, corporate tax, goods and services tax and other taxes, upgraded in 2023 with a language-model engine. It also handles authenticated transactions such as balance checks and payment plans."
  outcomes:
  - lever: capacity
    description: Transactional queries handled and taxpayer time saved in FY2024
    figure: "about 70,000 queries; an estimated 11,666 taxpayer hours"
    measures: "transactional queries handled by the IRAS chatbot in financial year 2024, with hours estimated at about 10 minutes saved per transaction versus other digital channels; not specific to GST"
    provenance: self-reported
    source_ref: OECD-GOVAI-2025
  prerequisites:
  - Government chat platform
  - Authentication for transactional services
  risks_and_guardrails:
  - "OECD notes tax decisions based on AI must stay explainable, transparent and accountable because taxpayers can challenge them (OECD-GOVAI-2025, p. 173)"
  - Grant Thornton Ireland reports South Korea routes sensitive chatbot queries to staff and the UK warns users that generative AI answers may be imperfect (GT-IE-OECD-2025)
  - "Werfel's register shows a chatbot telling a taxpayer she qualifies for a credit as a core hallucination scenario (AICPA-WERFEL-2026, Appendix A, risk 1)"
  - "CDTFA's gap between written and verbal advice shows a protection issue for AI answers (TAXNOTES-CDTFA-2025)"
  human_checkpoints:
  - "Escalation to staff for sensitive queries (Korea, per Grant Thornton Ireland)"
  role_evolution: "Not described for Singapore. HMRC's roadmap plans a generative AI chat trial (GOV.UK Chat) and AI features in its digital assistant."
  evidence_grade: B
  sources:
  - ref: OECD-GOVAI-2025
    title: "Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions (chapter 5, AI in tax administration)"
    publisher: OECD
    type: regulator
    url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf"
    date: 2025-09
    access: full
    locator: "Chapter 5, Box 5.4 (p. 172); pp. 173-174"
  - ref: GT-IE-OECD-2025
    title: "Governing with AI: The new face of tax authorities"
    publisher: Grant Thornton Ireland
    type: firm
    url: "https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/"
    date: '2025-09-19'
    access: full
    locator: "Sections 'Personalised and proactive taxpayer services' and 'The trust factor'"
  - ref: HMRC-ROADMAP-2025
    title: "HMRC's Transformation Roadmap"
    publisher: "HM Revenue & Customs"
    type: regulator
    url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap"
    date: '2025-07-21'
    access: full
    locator: Section 5.4 and Section 6.1
  - ref: AICPA-WERFEL-2026
    title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and B (Danny Werfel)"
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf"
    date: 2026-06
    access: full
    locator: "Appendix A, risk 1"
  last_reviewed: '2026-10-17'
  notes: "Grade capped at B: the published measure covers all transactional queries across tax types, not GST alone, and the measurement is the agency's own estimate relayed by the OECD."
- id: tax-indirect-tax-14
  title: Agent-managed exemption certificate collection and validation
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - transaction-processing
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Sellers must collect, validate and retain exemption certificates to support untaxed sales, and gaps surface in audits."
  solution: Avalara lists Exemption Certificate Management among products with agentic AI and says customers can ask an agent to run certificate validations. No source describes the steps in detail.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: no measured figure in the sources read
    provenance: vendor-published
    source_ref: ITWIRE-AVALARA-2025
  prerequisites:
  - Certificate repository linked to customer master data
  - State-specific acceptance rules (not retrieved in this run)
  risks_and_guardrails:
  - "Certificate acceptance and good-faith rules were not retrieved (see Gaps), so the control standard for automating acceptance is unknown"
  - Sales Tax Institute warns that agents cannot apply an exemption to products they cannot classify (STI-AGENTIC-2026)
  human_checkpoints:
  - Not stated; Avalara says agents ask a human for novel situations
  role_evolution: No source describes role changes.
  evidence_grade: C
  sources:
  - ref: ITWIRE-AVALARA-2025
    title: "Avalara Launches Agentic Tax and Compliance: AI Agents That Work for You (company news)"
    publisher: iTWire / Avalara
    type: vendor
    url: "https://itwire.com/business-it-news/data/avalara-launches-agentic-tax-and-compliance-ai-agents-that-work-for-you"
    date: '2025-10-01'
    access: full
    locator: "Product list and the 'From returns to tax calculations to certificate validations' passage"
  - ref: ACCTODAY-AVALARA-2025
    title: "Avalara launches 'always on, always ready' AI agents"
    publisher: Accounting Today (Arizent)
    type: press
    url: "https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents"
    date: '2025-09-30'
    access: full
    locator: Paragraph on asking an agent to do tax work
  - ref: STI-AGENTIC-2026
    title: Will Your AI Shopping Agent Catch Your Sales Tax Holiday Discount?
    publisher: Sales Tax Institute
    type: press
    url: "https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays"
    date: '2026-07-29'
    access: full
    locator: Closing checklist
  last_reviewed: '2026-10-17'
  notes: "Thin entry kept because certificate management is a core indirect-tax process. Avalara's 9 Apr 2026 release, which the landscape says names exemption certificates, could not be opened."
- id: tax-indirect-tax-15
  title: AI triage of invoice exceptions and nexus questions before human review
  archetype: tax
  module: indirect-tax
  function: finance-accounting
  work_types:
  - transaction-processing
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "High transaction volumes and short filing deadlines make exception handling and nexus screening time-consuming. Fonoa found only 6.8% of teams saw compliance workload fall in the past year, and 85.8% saw workload grow over two years."
  solution: Thomson Reuters says some indirect tax teams use AI to triage invoice exceptions or pre-screen nexus questions before they reach a human reviewer. Sovos describes proactive detection of compliance problems before filing deadlines.
  outcomes:
  - lever: capacity
    description: Teams whose compliance workload fell over the past year
    figure: "6.8%"
    measures: share of 176 surveyed indirect tax teams reporting a fall in compliance workload over the past year
    provenance: vendor-published
    source_ref: FONOA-BLOG-2026
  prerequisites:
  - Clean data and system integration (Fonoa says these are missing in most organisations)
  - Defined exception paths and override authority
  risks_and_guardrails:
  - Fonoa says AI often adds a review step before it removes a manual one (FONOA-BLOG-2026)
  - "Thomson Reuters notes that 44% of corporate professionals at organisations with a named AI strategy say day-to-day practice does not match it (TR-INDIRECT-2026)"
  human_checkpoints:
  - Human reviews triaged exceptions and nexus conclusions
  role_evolution: "Fonoa found 31.2% of teams grew headcount while 85.8% saw workload grow; AI had not yet absorbed the gap for most."
  evidence_grade: C
  sources:
  - ref: TR-INDIRECT-2026
    title: What three years of data reveal about AI in corporate indirect tax
    publisher: "Thomson Reuters Tax & Accounting"
    type: vendor
    url: "https://tax.thomsonreuters.com/blog/what-three-years-of-data-reveal-about-ai-in-corporate-indirect-tax/"
    date: '2026-08-27'
    access: full
    locator: "Section '2025: Strategy became the dividing line'"
  - ref: FONOA-BLOG-2026
    title: What 176 Tax Leaders Have to Say About AI Adoption in Indirect Tax
    publisher: Fonoa
    type: survey
    url: "https://www.fonoa.com/resources/blog/ai-adoption-indirect-tax-report"
    date: '2026-06-30'
    access: full
    locator: "Sections 'AI adoption hasn't reduced indirect tax workload' and 'Tax workload outgrew headcount'"
  - ref: SOVOS-SOVI-2026
    title: "Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability"
    publisher: Sovos
    type: vendor
    url: "https://sovos.com/press-releases/sovos-expands-sovi-ai/"
    date: '2026-03-24'
    access: full
    locator: "Capability item 'Proactive Issue Detection'"
  last_reviewed: '2026-10-17'
  notes: "The outcome is context, not a result of triage. The triage use itself is a vendor-owned blog's anecdotal statement with no named organisation."
- id: tax-indirect-tax-16
  title: Tax-authority guidance published for use by AI-powered accounting and tax products (idea)
  archetype: tax
  module: indirect-tax
  function: risk-compliance-legal
  work_types:
  - document-production
  - software-systems
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: workflow-automation
  maturity: emerging
  problem: Software that applies VAT rates and classifications can only be as right as the rules and guidance it can read. Errors enter returns when products interpret guidance inconsistently.
  solution: "Idea from HMRC's roadmap: work with the Government Digital Service on how business and third parties can use GOV.UK guidance in their own AI-powered products to reduce error, and expand real-time risking into VAT so customers receive prompts during submission. HMRC also observes that AI-enabled bookkeeping tools can now recommend tax categories using business context."
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: HMRC describes plans and exploration; no measured result
    provenance: self-reported
    source_ref: HMRC-ROADMAP-2025
  prerequisites:
  - "Machine-readable, versioned official guidance"
  - Stewardship of the software ecosystem (HMRC says it requires increased stewardship)
  risks_and_guardrails:
  - "Roadmap items are plans and trials, not deployments (HMRC-ROADMAP-2025, Sections 4.1 and 6.1)"
  - "Authority-side explainability and taxpayer-rights risks apply (OECD-GOVAI-2025, p. 173)"
  human_checkpoints:
  - Not specified
  role_evolution: HMRC expects intermediaries such as software providers to take a larger role in meeting tax obligations.
  evidence_grade: D
  sources:
  - ref: HMRC-ROADMAP-2025
    title: "HMRC's Transformation Roadmap"
    publisher: "HM Revenue & Customs"
    type: regulator
    url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap"
    date: '2025-07-21'
    access: full
    locator: Section 4.1 bullet on GOV.UK guidance and real time risking; Section 6.1
  - ref: OECD-GOVAI-2025
    title: "Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions (chapter 5, AI in tax administration)"
    publisher: OECD
    type: regulator
    url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf"
    date: 2025-09
    access: full
    locator: p. 173
  last_reviewed: '2026-10-17'
  notes: "Idea: a regulator's published intention. Labelled D because no deployment was found."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Product and service classification, taxability mapping** (transaction-processing, expert-judgment): mapping descriptions to HS, HSN, SAC or internal taxability codes (NATH-DELL-2025, ZHANG-HS-2026). HMRC notes that tax classification used to defy automation because two identical transactions can be treated differently, and says AI-enabled bookkeeping tools now recommend categories using business context (HMRC-ROADMAP-2025, Sect. 6.1).
- **Determination: jurisdiction or place of supply, rate, exemption, reverse charge** (transaction-processing, expert-judgment). The agent-design pilot splits it into classification, jurisdiction, rate, exemption and reverse charge, each independently scoreable (SANTOS-VAT-2026). The Austrian study treats place of supply as the central VAT question (LUKETINA-VAT-2026).
- **Exemption certificate collection and validation** (transaction-processing, review-assurance): only vendor product lists were found (ITWIRE-AVALARA-2025).
- **Return preparation, reconciliation, filing** (data-reporting, transaction-processing): Thomson Reuters cites more than 19,000 US jurisdictions and 1,200 signature-ready returns (TR-SUTAI-2026).
- **E-invoicing and digital reporting** (software-systems, data-reporting): ownership is split between Finance (38%), Tax or Tax Technology (30%) and IT (11%) among KPMG respondents (KPMG-INDIRECT-2026, p. 11).
- **Registration, nexus, marketplace and platform liability** (expert-judgment): the agentic-commerce question of who collects tax (BTAX-BAL-2026).
- **Technical research and advice** (research-synthesis, expert-judgment): VAT inquiries answered from statute and guidance (LUKETINA-VAT-2026).
- **Audit and authority interaction** (review-assurance): defending determinations, with records of rule, reviewer and approval (FONOA-BLOG-2026).
- **Authority-side steps:** risk scoring, taxpayer helpdesks and chatbots (OECD-GOVAI-2025, TAXNOTES-CDTFA-2025).

### Common pain points

- **Data quality and legacy ERP.** 58% of 53 large multinationals name data quality their biggest VAT/GST concern (44% in 2021); 61% correct data predominantly manually; 23% say their ERP is fit for purpose (KPMG-INDIRECT-2026, pp. 5-6).
- **Workload outruns headcount.** 85.8% of Fonoa respondents saw workload grow over two years; 31.2% grew headcount (FONOA-BLOG-2026). About 60% of KPMG respondents expect headcount to stay broadly unchanged for five years and about a third have no technology specialists (KPMG-INDIRECT-2026, p. 7).
- **AI lands on the wrong tasks.** Fonoa finds AI concentrated in research and drafting, while volume sits in reconciliation and return preparation; 71% have not fully automated one workflow end to end (FONOA-BLOG-2026).
- **Time-bound, state-specific rules.** Sales tax holidays depend on exact windows, product categories, price caps and destination rules; Connecticut's back-to-school threshold rose from $100 to $300 for 2026 (STI-AGENTIC-2026).
- **Fragmented ownership** of e-invoicing and country-specific tools (KPMG-INDIRECT-2026, p. 11).

### Metrics and benchmarks (with sources)

| Measure | Figure | What it counts | Source |
|---|---|---|---|
| Place-of-supply accuracy, textbook | 93.24% RAG; 68.92% plain GPT-4o | 74 textbook cases, correct country | LUKETINA-VAT-2026, Table 5 |
| Real-world VAT analyses correct | 16/20 RAG; 14/20 fine-tuned; 11/20 RAG+FT; 13/20 GPT-4.1 long context | 20 anonymised client inquiries from a consultancy | LUKETINA-VAT-2026, Sect. 8.2 |
| Agent-design VAT pilot | 0.755 single agent; 0.830 best orchestrated | 40 synthetic oracle-labelled cases x 5 repeats | SANTOS-VAT-2026, Table 1 |
| Tax-code prediction (HSN/SAC) | precision 70%, recall 61%, F1 65% (T5) | 16,000-record test set labelled by experts | NATH-DELL-2025, Sect. 3 |
| HS classification (customs) | 64.2% top-1, 78.3% top-3 at six digits | 632 e-commerce product entries | ZHANG-HS-2026, Table I |
| CDTFA sandbox accuracy | -6% phase 1, +4% phase 2 | agency report as relayed by Tax Notes; baseline unstated | TAXNOTES-CDTFA-2025, p. 3 |
| Personal income tax calculation (adjacent) | fewer than a third of simplified returns correct | frontier models on a benchmark | COLUMN-TAXCALCBENCH-2025 |
| Defensibility confidence | 57.4% not confident | 176 indirect tax leaders | FONOA-BLOG-2026 |
| Formal documented sign-off | about one third | same sample | FONOA-BLOG-2026 |
| Specific AI targets or KPIs | 12.5% | same sample | FONOA-BLOG-2026 |
| Have not fully automated a single workflow end to end | 71% | same sample | FONOA-BLOG-2026 |
| Unsanctioned AI use | 36% | corporate professionals, TR 2026 data, sample not stated | TR-INDIRECT-2026 |
| ROI measurement | 26% measure ROI; 65% use public GenAI | tax professionals; denominators not defined | TR-INDIRECT-2026 |
| VAT/GST control framework | 58% have one; 28% say controls ineffective | 53 large multinationals | KPMG-INDIRECT-2026, p. 8 |
| State agencies piloting or using AI in core functions | 15% | 37 state agencies and two city departments, FTA/EY 2024 survey; FTA says this mostly reflects machine learning | TAXNOTESTALK-2025 |
| OECD members using AI in tax administration | 29 of 38 | OECD 2024 Inventory of Tax Technology Initiatives | OECD-GOVAI-2025, p. 169 |
| Austria risk models, 2023 | about 6.5 million cases analysed; EUR 185 million additional revenue | income, corporate, VAT, customs together | OECD-GOVAI-2025, Box 5.3 |

**Absence of evidence, stated plainly.** No source gave error rates, override rates, parallel-run results, audit outcomes or an independent head-to-head test for Avalara, Sovos, Vertex, Thomson Reuters or other commercial indirect-tax tools. Thomson Reuters's 65%, 75% and 30-to-11-day figures are unsupported vendor claims (TR-SUTAI-2026). The only independent VAT measurements are academic and use GPT-4-class models from 2025.

### Guardrails and regulatory points

- **IRS OPR Alert 2026-19 (24 Jun 2026)** applies Circular 230 duties to AI use: due diligence (section 10.22), fees (10.27), competence (10.35), procedures for firms (10.36) and written advice (10.37), plus preparer-penalty rules on disclosing return information. It covers federal tax practice; it does not address state sales tax or VAT (IRS-OPR-2026).
- **UK PCRT topical guidance on AI (19 Jan 2026)** from seven bodies including CIOT, ATT and ICAEW: members stay responsible for AI-assisted work, should be able to explain how a conclusion was arrived at, and should not enter client data into a public model without consent (PCRT-AI-2026, ICAEW-PCRT-2026).
- **UK tax tribunal.** In *Omar Rafique v HMRC* [2026] TC09874, the First-tier Tribunal struck out a VAT-penalty appeal after repeated AI-generated submissions with fabricated case citations and unfilled placeholders; the judge said there is no bar on using AI but parties must ensure submissions are correct (ROSSMARTIN-RAFIQUE-2026, CITYAM-RAFIQUE-2026).
- **EU ViDA (Directive (EU) 2025/516, 11 Mar 2025).** E-invoices should in principle follow the European standard and carry the data tax authorities need in a structured format; digital reporting applies to cross-border B2B from 1 Jul 2030 (EU-DIRECTIVE-2025-516, recitals (5), (6), (11); EC-VIDA-2025). ECOFIN approved the package on 5 Nov 2024 (EU-VIDA-2024). The Commission expects fraud reductions of up to EUR 11 billion a year (EC-VIDA-2025).
- **EU AI Act.** Article 4 requires providers and deployers to take measures for a sufficient level of AI literacy among staff (EU-AIACT-2024). Recital 59 says AI used for administrative proceedings by tax and customs authorities should not be classed as high-risk law-enforcement AI; Hadwick argues this lets tax systems slip through the cracks, notes most Member States lack a legal basis for tax-administration AI, and cites the Dutch childcare benefits scandal (HADWICK-EUAIACT, Sect. III.2). I did not verify any Digital Omnibus changes to AI Act dates.
- **State agencies.** CDTFA Publication 70 excuses liabilities only for reliance on written advice; AI-assisted answers are delivered verbally (TAXNOTES-CDTFA-2025, p. 2). Werfel's tax-authority risk register lists hallucination, over-trust and policy drift among 20 risks and gives vendor-diligence questions, including a tamper-proof output log (AICPA-WERFEL-2026, Appendices A and B).
- **Voluntary frameworks.** NIST's AI RMF 1.0 (26 Jan 2023) and Generative AI Profile (26 Jul 2024) are voluntary (NIST-AIRMF-2023); the page notes the RMF is being revised.
- **Tax administration expectations.** OECD says tax decisions relying on AI must be explainable, transparent and accountable, because taxpayers can challenge them (OECD-GOVAI-2025, p. 173).

### Frontier signals (dated and sourced)

- **30 Sep-1 Oct 2025.** Avalara launches an agentic platform; says there are already dozens of agents and expects every product to have agents by the end of Q4 2025; human review for novel situations and key decisions (ACCTODAY-AVALARA-2025, ITWIRE-AVALARA-2025).
- **15 Jan 2026.** Thomson Reuters ONESOURCE Sales and Use Tax AI: "touchless by default, manual by exception" (TR-SUTAI-2026).
- **26-29 Jan 2026.** OECD VAT forum names AI and crypto emerging challenges for VAT administration (BTAX-OECDVAT-2026).
- **Feb-Jul 2026.** Agentic commerce: Bal (24 Feb) and the Sales Tax Institute (29 Jul) analyse who collects tax and how tax holidays work when an agent checks out; Shopify keeps tax calculation in the merchant flow (BTAX-BAL-2026, STI-AGENTIC-2026).
- **24 Mar 2026.** Sovos announces Ask Sovi, error remediation and an MCP gateway in development, with agent-to-agent orchestration expected over time (SOVOS-SOVI-2026).
- **May 2026.** KPMG benchmark: AI seen as a way to improve data quality; headcount largely unchanged (KPMG-INDIRECT-2026).
- **Jun-Sep 2026.** Fonoa survey (17 Jun), TR indirect-tax data (27 Aug): measurement and accountability become the stated gap (FONOA-INDIRECT-2026, TR-INDIRECT-2026). AICPA and Werfel launch the Council on AI Risk in Tax on 23 Sep 2026 (AICPA-CART-2026).
- **Aug-Sep 2026.** Research: a deterministic-oracle design for VAT agents (24 Aug) and a peer-reviewed VAT RAG study revised 2 Sep (SANTOS-VAT-2026, LUKETINA-VAT-2026).
- **Sep-Oct 2026.** Sovos reports France e-invoicing scale (23 Sep), acquires Flowie (1 Oct) and joins the Cloud Security Alliance (15 Oct); vendor claims, listing summaries only (SOVOS-PRESS-2026).
- **Feb 2026.** Vertex tells indirect tax leaders to track adoption of AI by auditors and other enforcement bodies (VERTEX-TRENDS-2026).
- **To 2028-2035.** HMRC plans AI-powered caseworker systems by the end of 2028 and 90% digital interactions by 2030; ViDA reaches cross-border digital reporting on 1 Jul 2030 and alignment of domestic real-time systems by 1 Jan 2035 (HMRC-ROADMAP-2025, EC-VIDA-2025).

### Workforce and role effects

- 58% of KPMG respondents expect VAT/GST headcount to stay largely unchanged over five years because of AI; 21% expect an increase and 21% a decrease. The foreword says indirect tax professionals will likely become data managers, ERP-change gatekeepers and leaders on AI in tax (KPMG-INDIRECT-2026, pp. 2, 7).
- Fonoa: 85.8% saw workload grow in two years and 31.2% grew headcount; AI has not yet closed the gap for most (FONOA-BLOG-2026).
- Thomson Reuters presents touchless compliance as moving professionals from operations to advisory (TR-SUTAI-2026). Treat as vendor positioning.
- At TEI Tax Tech 2026, attendees described the difficulty of reviewing growing volumes of quiet, technical AI errors, and said tax rarely owns AI (TEI-TAXTECH-2026).
- Authorities: HMRC expects intermediaries and software to play a larger role in fulfilling obligations (HMRC-ROADMAP-2025, Sect. 6).

### Objections and concerns practitioners raise

- **Hallucination and unacceptable error rates:** the Austrian study's authors say 20-30% errors are unacceptable (LUKETINA-VAT-2026). TEI attendees raised silent hallucinations (TEI-TAXTECH-2026).
- **Defensibility to authorities:** 57.4% not confident (FONOA-BLOG-2026).
- **Shadow AI:** 60.8% rely primarily on individuals using public tools (FONOA-BLOG-2026); 36% unsanctioned use (TR-INDIRECT-2026).
- **Accountability cannot be delegated:** AI has no legal personality, so the operating company bears collection liability (BTAX-BAL-2026); UK members stay responsible for AI-assisted work (ICAEW-PCRT-2026).
- **Taxpayer protection from agency AI:** experts warned that taxpayers may be unable to challenge wrong AI-assisted advice unless it is in writing (TAXNOTES-CDTFA-2025).
- **Stale configuration:** automation can accelerate errors if holiday thresholds or product mappings are wrong (STI-AGENTIC-2026).
- **Vendor claims without baselines:** the Thomson Reuters release gives no baseline or sample (TR-SUTAI-2026).

### Interview probes for an advisor

1. Pick your last AI-assisted indirect tax determination or filing. What record shows the rule version applied, who reviewed it and who approved it, and could you give that to an auditor within a day?
2. Which indirect tax workflows are fully automated end to end, and what are the measured exception and override rates? If you have none, what stops you measuring them?
3. Who owns AI in the tax function, and who owns e-invoicing: Tax, Finance or IT? What AI tools are people using today that the function has not sanctioned?
4. If an AI agent started a purchase from your site or marketplace, which of your tax engine rules (holidays, exemptions, product mappings) would it use, and who confirms those are machine-readable and current?
5. What would a tax authority with transaction-level invoice data see that your returns do not show, and how are you reconciling to it?

---

## 4. Routed to other modules

- **Cross-cutting professional responsibility and AI governance** (IRS OPR Alert 2026-19, UK PCRT guidance, AICPA/Werfel framework and CART, NIST AI RMF): apply across all tax modules; cited here only where they constrain indirect-tax work.
- **controversy:** *Rafique v HMRC* (VAT penalty appeal with hallucinated citations); the Tax Court *Clinco* matter and the IRS's own AI use (GAO-26-107522) are covered in the landscape file and were not re-read for indirect tax.
- **tax-authority AI (proposed module or controversy):** Austria's risk models, IRAS chatbot, HMRC's roadmap, OECD *Governing with AI* box on Brazil's litigation file clustering, EU AI Act Recital 59 and the Hadwick analysis (OECD-GOVAI-2025, HADWICK-EUAIACT).
- **compliance:** TaxCalcBench (personal income tax calculation) is adjacent evidence (COLUMN-TAXCALCBENCH-2025).
- **Customs and trade classification (landscape optional addition):** Harmonized System classification evidence (ZHANG-HS-2026) and the customs side of tariff-code prediction.
- **Tax policy of AI (landscape optional addition):** marketplace and deemed-supplier analysis of AI commerce apps and the OECD's VAT forum statement (BTAX-BAL-2026, BTAX-OECDVAT-2026).
- **tax-data-technology:** KPMG's ERP and data-quality findings, agent interoperability (MCP, A2A) and e-invoicing ownership (KPMG-INDIRECT-2026, SOVOS-SOVI-2026).
- **Pricing and business model:** OPR's guidance that cost savings should be passed on and AICPA's request for clarification on value pricing (IRS-OPR-2026, AICPA-CART-2026).

---

## 5. Sources

All 37 sources were opened. `access: full` means the page or document was opened and read; where only part could be read (paywall, gated report, listing page) the title says so. Types: vendor 7, press 7, regulator 6, academic 6, professional-body 4, survey 3, podcast 1, conference 1, firm 1, standard-setter 1.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| FONOA-INDIRECT-2026 | State of Indirect Tax in the AI Era 2026 (landing page; full report is form-gated) | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 | full |
| FONOA-BLOG-2026 | What 176 Tax Leaders Have to Say About AI Adoption in Indirect Tax | Fonoa | survey | https://www.fonoa.com/resources/blog/ai-adoption-indirect-tax-report | 2026-06-30 | full |
| KPMG-INDIRECT-2026 | Benchmarking Indirect Tax in a data-driven era: 2026 KPMG Indirect Tax Benchmarking Survey | KPMG International | survey | https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/05/benchmarking-indirect-tax-in-a-data-driven-era.pdf.coredownload.inline.pdf | 2026-05 | full |
| TR-INDIRECT-2026 | What three years of data reveal about AI in corporate indirect tax | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/what-three-years-of-data-reveal-about-ai-in-corporate-indirect-tax/ | 2026-08-27 | full |
| TR-SUTAI-2026 | Thomson Reuters Launches AI Tax Compliance Solution That Saves Time and Reduces Risk (ONESOURCE Sales and Use Tax AI) | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk | 2026-01-15 | full |
| SOVOS-SOVI-2026 | Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability | Sovos | vendor | https://sovos.com/press-releases/sovos-expands-sovi-ai/ | 2026-03-24 | full |
| SOVOS-PRESS-2026 | Sovos press-release listing (France e-invoicing scale 23 Sep 2026; Flowie acquisition 1 Oct 2026; Cloud Security Alliance 15 Oct 2026); summaries only | Sovos | vendor | https://sovos.com/press-releases/ | 2026-10-15 | full |
| ACCTODAY-AVALARA-2025 | Avalara launches 'always on, always ready' AI agents | Accounting Today (Arizent) | press | https://www.accountingtoday.com/news/avalara-launches-always-on-always-ready-ai-agents | 2025-09-30 | full |
| ITWIRE-AVALARA-2025 | Avalara Launches Agentic Tax and Compliance: AI Agents That Work for You (company news) | iTWire / Avalara | vendor | https://itwire.com/business-it-news/data/avalara-launches-agentic-tax-and-compliance-ai-agents-that-work-for-you | 2025-10-01 | full |
| BTAX-BAL-2026 | Artificial Intelligence Goes Shopping, Creates Tax Challenges (commentary by Aleksandra Bal, global tax technology lead at Stripe) | Bloomberg Tax | press | https://news.bloombergtax.com/tax-insights-and-commentary/artificial-intelligence-goes-shopping-creates-tax-challenges | 2026-02-24 | full |
| BTAX-OECDVAT-2026 | OECD Identifies Crypto and AI As Challenges to VAT Systems (opening paragraphs only; rest paywalled) | Bloomberg Tax, Daily Tax Report International | press | https://news.bloombergtax.com/daily-tax-report-international/oecd-identifies-crypto-and-ai-as-challenges-to-vat-systems | 2026-01-29 | full |
| STI-AGENTIC-2026 | Will Your AI Shopping Agent Catch Your Sales Tax Holiday Discount? | Sales Tax Institute | press | https://www.salestaxinstitute.com/resources/ai-shopping-agents-sales-tax-holidays | 2026-07-29 | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| TAXNOTES-CDTFA-2025 | Experts Urge Caution as State Tax Agencies Deploy Generative AI (Tax Notes, DOC 2025-24791; copy hosted by American University Kogod School) | Tax Notes (Tax Analysts) | press | https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf | 2025-08-26 | full |
| TAXNOTESTALK-2025 | Artificial Intelligence and State Tax Agencies (Tax Notes Talk; interview with Ryan Minnick, Federation of Tax Administrators) | Tax Notes Talk | podcast | https://taxnotestalk.taxnotes.com/124942/episodes/17439828-artificial-intelligence-and-state-tax-agencies | 2025-07-04 | full |
| EU-VIDA-2024 | EU Member States Approve the VAT in the Digital Age (ViDA) Package (reports the 5 Nov 2024 ECOFIN approval) | Fonoa | vendor | https://www.fonoa.com/resources/blog/eu-member-states-approve-vat-in-the-digital-age-vida-package | 2024-11-05 | full |
| EC-VIDA-2025 | VAT in the Digital Age (ViDA) (page undated; adoption 11 Mar 2025, OJ 25 Mar 2025) | European Commission, DG TAXUD | regulator | https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en | 2025-03 | full |
| EU-DIRECTIVE-2025-516 | Council Directive (EU) 2025/516 amending Directive 2006/112/EC as regards VAT rules for the digital age | Council of the European Union | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0516 | 2025-03-11 | full |
| EU-AIACT-2024 | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act) | European Parliament and Council | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 | 2024-06-13 | full |
| HADWICK-EUAIACT | Slipping Through the Cracks, the Carve-outs for AI Tax Enforcement Systems in the EU AI Act (European Papers, Vol. 9, No 3, pp. 936-955) | European Papers (David Hadwick, University of Antwerp) | academic | https://www.europeanpapers.eu/e-journal/slipping-through-cracks-carve-outs-ai-tax-enforcement-systems-eu-ai-act | 2024-12-30 | full |
| HMRC-ROADMAP-2025 | HMRC's Transformation Roadmap | HM Revenue & Customs | regulator | https://www.gov.uk/government/publications/hmrc-transformation-roadmap | 2025-07-21 | full |
| PCRT-AI-2026 | Professional bodies issue AI advice to members (PCRT topical guidance on AI) | Association of Taxation Technicians (for the seven PCRT bodies) | professional-body | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 | full |
| ICAEW-PCRT-2026 | Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax | ICAEW | professional-body | https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax | 2026-01 | full |
| LUKETINA-VAT-2026 | Using Large Language Models for Legal Decision-Making in Austrian Value-Added Tax Law: A Comparative Study (arXiv 2507.08468 v2; Journal of Business Analytics 2026; v1 11 Jul 2025) | University of Applied Sciences Upper Austria and Johannes Kepler University Linz | academic | https://arxiv.org/abs/2507.08468 | 2026-09-02 | full |
| SANTOS-VAT-2026 | Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep (arXiv 2608.23395, preprint by an independent researcher) | arXiv (Pedro Santos) | academic | https://arxiv.org/abs/2608.23395 | 2026-08-24 | full |
| ZHANG-HS-2026 | A Deterministic Agentic Workflow for HS Tariff Classification: Multi-Dimensional Rule Reasoning with Interpretable Decisions (arXiv 2605.14857) | Shanghai Jiao Tong University with Chinese customs (GACC) co-authors | academic | https://arxiv.org/abs/2605.14857 | 2026-05-14 | full |
| NATH-DELL-2025 | Domain-Adaptive Small Language Models for Structured Tax Code Prediction (arXiv 2507.10880) | Dell Technologies (authors Nath, Wadhwa, Perez) | academic | https://arxiv.org/abs/2507.10880 | 2025-07-19 | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126; personal income tax, adjacent to this module) | Column Tax | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full |
| AICPA-WERFEL-2026 | A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendices A and B (Danny Werfel) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 | full |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax (Council on AI Risk in Tax) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| TEI-TAXTECH-2026 | TEI Tax Tech 2026: the man behind the curtain (recap of the 27-29 Apr 2026 TEI Tax Technology Seminar) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| CITYAM-RAFIQUE-2026 | Tax judge criticises 'fabricated AI cases' cited in appeal against HMRC | City AM | press | https://www.cityam.com/?p=2425429 | 2026-05-18 | full |
| ROSSMARTIN-RAFIQUE-2026 | Individual persistently used illusory AI cases (summary of Omar Rafique v HMRC [2026] TC09874) | Ross Martin Tax | press | https://rossmartin.co.uk/sme-tax-news/8927-ai-hallucinates-at-the-ftt-again | 2026-05-13 | full |
| OECD-GOVAI-2025 | Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions (chapter 5, AI in tax administration) | OECD | regulator | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf | 2025-09 | full |
| GT-IE-OECD-2025 | Governing with AI: The new face of tax authorities | Grant Thornton Ireland | firm | https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/ | 2025-09-19 | full |
| NIST-AIRMF-2023 | AI Risk Management Framework (AI RMF 1.0, released 26 Jan 2023; Generative AI Profile NIST-AI-600-1, 26 Jul 2024) | NIST | standard-setter | https://www.nist.gov/itl/ai-risk-management-framework | 2023-01-26 | full |
| VERTEX-TRENDS-2026 | 2026 Indirect Tax Trends | Vertex Inc. | vendor | https://www.vertexinc.com/resources/resource-library/2026-indirect-tax-trends | 2026-02-03 | full |

---

## 6. Gaps

**Could not reach or confirm**
- Primary OECD material on VAT and AI: the OECD VAT forum news release was bot-blocked, so the 26-29 Jan 2026 statement rests on the opening paragraphs of a Bloomberg Tax article (BTAX-OECDVAT-2026). *Tax Administration 2025*, the OECD Tax Administration 3.0 pages and the IMF technical note on generative AI for compliance risk analysis could not be opened.
- The Fonoa report itself (form-gated), the Thomson Reuters Future of Professionals report and its corporate tax department reports (gated), and Avalara's 9 Apr 2026 release (404). Figures come from landing pages and blogs.
- The FTA generative-AI briefing paper and 2024 FTA/EY survey report; I have only the podcast discussion (TAXNOTESTALK-2025).
- Exemption-certificate governance: the Multistate Tax Commission and Streamlined Sales Tax Governing Board certificate pages were blocked or missing, so I could not establish the acceptance and good-faith rules that would constrain automated certificate validation (use case 14).
- A UK Tax Adviser magazine article on "actionability and auditability" for indirect tax was read but has no date or author in the version I could retrieve, so it is not cited.
- EU AI Act application dates and any Digital Omnibus delays were not verified. The ViDA directive was read in the original; national regimes (Poland KSeF, France, Belgium, Germany, Greece) and Peppol governance were not covered beyond a Poland portal landing page.
- Job postings (none searched), community discussion (none reachable) and conference proceedings for Avalara CRUSH, Sovos, Vertex and ITR indirect-tax forums.

**Searched and not found**
- Any error rate, override rate, parallel-run result or inspection finding for a commercial indirect-tax tool or agent.
- Any independent head-to-head benchmark of tax engines or tax agents on VAT or sales-tax determination.
- Any named customer case study with published indirect-tax AI outcomes (Thomson Reuters, Avalara, Sovos and Vertex publish claims without named customers in the sources read).
- Any enforcement action or court decision on AI-assisted indirect tax filings; the only VAT case found is a litigant-in-person appeal with fabricated citations (ROSSMARTIN-RAFIQUE-2026).
- Evidence on how state tax agencies use AI in sales-tax audit selection; the landscape lists a 2026 Tax Notes Talk episode that I did not open.

**Weaknesses in evidence I did use**
- The Austrian VAT study used GPT-4o and a naive RAG design, 20 real cases and one jurisdiction (LUKETINA-VAT-2026).
- The agent-design pilot is synthetic, single-workload and by an independent researcher (SANTOS-VAT-2026).
- The CDTFA accuracy figure is a news report of a December 2024 agency document, with no stated baseline (TAXNOTES-CDTFA-2025).
- Dell's test-set result does not state code level, averaging method or deployment status (NATH-DELL-2025).
- Surveys are vendor-sponsored (Fonoa, Thomson Reuters) or Big Four (KPMG, 53 respondents, mostly large multinationals); none is a probability sample.
