# Security x governance-risk: practice angle (wave 4)

Compiled 2026-10-17. Archetype `security`, module `governance-risk` (landscape name: security-governance-risk). Angle: practice. Method: pages opened with curl or the r.jina.ai text mirror; public job-board APIs (Greenhouse, Ashby) for postings; arXiv abs/PDF pages; 9 web searches (mostly unproductive, used only to find leads). Every source listed below was opened; none is search-only.

## 1. Summary

**What the practice evidence shows.** AI in security governance, risk and compliance (GRC) is concentrated in four places: (1) customer-facing security assurance (questionnaires, trust centres), (2) third-party (vendor) security assessment, (3) control mapping, evidence handling and continuous control monitoring, and (4) risk-register work. The only measured, named-customer outcomes are in vendor-published case studies for GRC platforms (Vanta, Conveyor, Hyperproof, Whistic). The most credible evidence of how in-house teams organise the work comes from job postings at AI-forward companies (Anthropic, OpenAI, Plaid, Cloudflare, Okta, GitLab, Figma), which describe "GRC engineering" teams that supervise agent-drafted work.

**Evidence quality.** There are no independent field measurements of AI in GRC (no published override rates, parallel runs, audit inspection findings or auditor reliance studies). The nearest independent quality evidence is academic and adjacent: one study of five LLMs against 50 human experts on CIS-Controls risk scenarios found the models consistently underestimated risk (`ARXIV-2605.05424`), and one study of natural-language access-control-policy to Rego translation found 50.3% end-to-end correctness against 15.3% for a single-prompt baseline (`ARXIV-2609.24036`). The only vendor-published precision figure for a GRC feature is Vanta's control-to-evidence mapping: below 35% precision at baseline, 78% after iteration (`VANTA-QUALITYEVAL-2026`).

**Use-case count.** 16 candidate use cases: 3 grade A, 8 grade B, 4 grade C, 1 grade D (idea). All grade-A outcome figures are vendor-published on the vendor's own site, quoting the customer; none is independent.

**Two things to know before using this file.**
- Customer-story dates: vendor case-study pages show no publication date. Where a sitemap gave a last-modified time, that date is used and flagged "(page last modified)". Treat it as an upper bound on age, not a publication date.
- Job postings show intent and the employer's own description of its work, not measured outcomes. Present-tense statements ("review agent-prefilled outputs") are treated as evidence of operation (grade B); "build/own AI-fluent" statements are treated as intent (grade C). Postings can change or be withdrawn. Anthropic and OpenAI are AI developers as well as employers; their postings may be aspirational.

## 2. Use cases

```yaml
- id: security-governance-risk-01
  title: Inbound customer security questionnaires answered from an approved knowledge base
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [client-interaction, document-production]
  pattern: grounded-knowledge-assistant
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    Customer and prospect security reviews arrive as long spreadsheets or portal forms. Each answer is
    looked up by hand in policies, audit reports and past answers, so a small GRC team becomes a sales bottleneck.
  solution: >
    The questionnaire is read in any format, answers are drafted from the company's approved documents
    (audit reports, policies, product documentation), and only low-confidence or unmatched questions go to a
    person. Some tools attach a confidence score and sentence-level source citations to each answer.
  outcomes:
    - lever: speed
      description: GitHub reports automating most inbound questionnaires within six months of launching Copilot-driven demand
      figure: "93%"
      measures: "'93% of inbound questionnaires automated in 6 months' (GitHub goal was 12 months); preceded by 'more than 300 questionnaires in a short timeframe'. Source gives no definition of 'automated' and no error rate."
      provenance: vendor-published
      source_ref: VANTA-GITHUB-2026
    - lever: speed
      description: Carta reports less time spent on customer security reviews
      figure: "83% decrease"
      measures: "'decrease in time spent on customer security reviews' (baseline and method not stated)"
      provenance: vendor-published
      source_ref: CONVEYOR-CARTA-2026
    - lever: quality
      description: Carta reports AI accuracy on questionnaires
      figure: "95%"
      measures: "'AI accuracy when answering customer security questionnaires' (how accuracy was judged is not stated). Carta's GRC analyst separately says a 77-question spreadsheet had 72 answers that were right, and took 20 minutes instead of days."
      provenance: vendor-published
      source_ref: CONVEYOR-CARTA-2026
    - lever: capacity
      description: Carta reports fewer questionnaires reaching the team
      figure: "40% fewer"
      measures: "'fewer customer security questionnaires' (attributed on the page to the trust centre and self-serve access, not only to AI)"
      provenance: vendor-published
      source_ref: CONVEYOR-CARTA-2026
    - lever: capacity
      description: Adoption survey of 50+ B2B teams (vendor-run)
      figure: "88% / 46%"
      measures: "'88% of teams are using AI or plan to in next 12 months, but only 46% are advanced users' of 50+ B2B teams surveyed by Conveyor; '60% of teams are running customer security reviews with 2 or fewer FTEs'"
      provenance: vendor-published
      source_ref: CONVEYOR-BENCH-2026
  prerequisites:
    - A maintained library of approved source documents (audit reports, policies, product documentation); the Conveyor survey says 62% of teams are not using AI to maintain the knowledge base (CONVEYOR-BENCH-2026)
    - Integration with the CRM or sales workflow so reviewers can see deal context (CONVEYOR-CARTA-2026)
    - Carta's InfoSec team connected systems, cleaned up documentation and identified each product and report before the AI could answer accurately (CONVEYOR-CARTA-2026)
  risks_and_guardrails:
    - Answers can be wrong or overstate a control; Vanta's own evaluation work treats hallucinated detail in compliance answers as an audit risk (VANTA-QUALITYEVAL-2026)
    - Confidence scores and sentence-level citations are offered so a reviewer can check an answer (WHISTIC-CALASTONE-2025)
    - GitHub describes its programme as "human-reviewable" (VANTA-GITHUB-2026)
  human_checkpoints:
    - Questions the AI cannot answer or flags as uncertain go to an analyst (CONVEYOR-CARTA-2026)
    - Approved-content owners keep the knowledge base current (CONVEYOR-CARTA-2026)
  role_evolution: >
    Carta's CISO says the tool handles repetitive work so the team can focus on higher-value projects, and its
    GRC analyst says it helps the company grow without adding headcount (CONVEYOR-CARTA-2026). GitHub says its
    customer-assurance team is freed for higher-value work (VANTA-GITHUB-2026).
  evidence_grade: A
  sources:
    - { ref: VANTA-GITHUB-2026, title: "GitHub accelerates sales by automating 93% of security questionnaires with Vanta", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/github", date: 2026-03, access: full, locator: "TL;DR and 'Vanta impact' ROI list" }
    - { ref: CONVEYOR-CARTA-2026, title: "Carta cuts security review time by 83% with Conveyor", publisher: Conveyor, type: vendor, url: "https://www.conveyor.com/customers/carta-2", date: 2026-06, access: full, locator: "Header stats; 'Results: 95% AI accuracy'; Callie Dedinsky quote" }
    - { ref: CONVEYOR-BENCH-2026, title: "2026 Customer Trust Benchmark Report (landing page)", publisher: Conveyor, type: survey, url: "https://www.conveyor.com/landing-page/2026-customer-trust-benchmark", date: 2026-09, access: full, locator: "Headline statistics and 'Infosec/GRC teams are adopting AI' section" }
    - { ref: WHISTIC-CALASTONE-2025, title: "How Calastone Transformed TPRM with Whistic", publisher: Whistic, type: vendor, url: "https://www.whistic.com/resources/case-studies/calastone-customer-story", date: 2025-12, access: full, locator: "'AI-Driven Speed' and 'AI-Powered Insights'" }
    - { ref: VANTA-QUALITYEVAL-2026, title: "Vanta AI Quality Eval Maturity Model", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-ai-quality-evaluation-maturity-model", date: 2026-07, access: full, locator: "Opening section on hallucination risk" }
    - { ref: ARXIV-2412.13988, title: "RAG for Effective Supply Chain Security Questionnaire Automation", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2412.13988", date: 2024-12-18, access: full, locator: "Abstract (no accuracy figures in the abstract)" }
  last_reviewed: 2026-10-17
  notes: >
    Dates for the Vanta, Conveyor and Whistic pages are sitemap last-modified times, not publication dates.
    GitHub's 93% is described as a result of a Vanta product partnership; GitHub is also a Vanta customer since 2024.
    Several vendors (Loopio, Responsive, Conveyor) sell the same function; Loopio's customer index lists Allied Universal
    (questionnaires "up to 90% faster") and HedgeServ (DDQs from 3 days to 4 hours) but those are RFP/DDQ tools and were
    not opened in full, so they are not used for outcomes.

- id: security-governance-risk-02
  title: Self-serve trust centre with an AI agent that answers security questions before they reach the team
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [client-interaction]
  pattern: service-agent-escalation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    Customers ask for the same audit reports and policy documents by email, NDA and ticket, and then ask follow-up
    questions the documents already answer.
  solution: >
    A public or gated trust centre exposes audit reports, policies and FAQs with automated NDA and access rules,
    and an AI agent answers inbound security questions from that content. Questions it cannot answer fall back
    to the security team.
  outcomes:
    - lever: capacity
      description: Synthesia reports customer questions resolved without staff
      figure: "20-30%"
      measures: "'20-30% of customer questions resolved through self-service or AI agent' (not split between the trust centre and the agent); about 100 customers per month self-serve without submitting questions"
      provenance: vendor-published
      source_ref: VANTA-SYNTHESIA-2026
    - lever: speed
      description: Synthesia reports shorter sales cycles after launching its trust centre
      figure: "2 weeks"
      measures: "'2-week average reduction in sales cycles' (attribution to trust centre vs other changes not shown)"
      provenance: vendor-published
      source_ref: VANTA-SYNTHESIA-2026
    - lever: capacity
      description: Perforce reports share of inbound requests handled by the trust centre (alongside questionnaire automation)
      figure: "more than half"
      measures: "'More than half of all inbound requests are handled by the Trust Center'; also '60% less time spent on questionnaires' and '10x increase in Trust Center interactions'. The page does not say how much of this is AI."
      provenance: vendor-published
      source_ref: VANTA-PERFORCE-2026
  prerequisites:
    - Curated, current document set and tagging by industry or regulation (VANTA-SNOWFLAKE-2026 shows the document-distribution part; Snowflake's trust centre is not described as AI-based)
    - CRM integration to validate whether a requester is a customer or prospect and to handle NDAs (CONVEYOR-SUMO-2026)
  risks_and_guardrails:
    - Figures bundle non-AI self-service (document portal) with AI answering, so the AI contribution is not separable (VANTA-SYNTHESIA-2026)
  human_checkpoints:
    - Unanswered questions and non-standard requests still reach the security team (VANTA-SYNTHESIA-2026)
  role_evolution: >
    Synthesia's two-person security team says it runs six frameworks and fields customer questions without adding
    headcount to match company growth (VANTA-SYNTHESIA-2026). Sumo Logic's compliance lead describes the earlier manual
    request handling as a second full-time job (CONVEYOR-SUMO-2026).
  evidence_grade: B
  sources:
    - { ref: VANTA-SYNTHESIA-2026, title: "How Synthesia became the first AI video company certified against ISO 42001", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/synthesia", date: 2026-10, access: full, locator: "'Vanta impact': Trust Center Pro and Vanta AI bullets" }
    - { ref: VANTA-PERFORCE-2026, title: "Perforce unifies enterprise compliance, security, and risk with Vanta", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/perforce", date: 2026-03, access: full, locator: "ROI bullets under Trust Center Pro and Questionnaire Automation" }
    - { ref: VANTA-SNOWFLAKE-2026, title: "Snowflake's trust program speaks for itself", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/snowflake", date: 2026-03, access: full, locator: "Header stats and 'How Snowflake did it'" }
    - { ref: CONVEYOR-SUMO-2026, title: "Sumo Logic automates 100% of security requests with Conveyor Trust Center", publisher: Conveyor, type: vendor, url: "https://www.conveyor.com/customers/sumo-logic", date: 2026-07, access: full, locator: "Challenge and Results sections" }
  last_reviewed: 2026-10-17
  notes: >
    Graded B, not A: the measured results combine a document portal that does not need AI with the AI agent.
    Dates are sitemap last-modified times. Snowflake (2,000+ hours saved annually, 8,000+ interactions) and Sumo Logic
    (100% of document requests automated) are trust-centre results with no AI claim.

- id: security-governance-risk-03
  title: AI-drafted third-party (vendor) security assessments reviewed by an analyst
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    Each new vendor needs its SOC 2 report, pen test summary and questionnaire read against the buyer's standards.
    Volume grows faster than analysts, and reviews take weeks.
  solution: >
    An AI agent collects vendor documents, extracts exceptions and risk signals from SOC 2 reports, pen tests and
    questionnaires, drafts an evaluation against the buyer's criteria, and prepares follow-up questions. An analyst
    verifies the draft, decides inherent and residual risk, and drives findings to closure.
  outcomes:
    - lever: speed
      description: Samsara reports faster vendor reviews using a TPRM agent that analyses SOC 2 reports, pen tests and questionnaires
      figure: "up to 50% faster"
      measures: "'Up to 50% faster vendor review time' across about 600 vendors and about 130 reviews per month (baseline and method not stated)"
      provenance: vendor-published
      source_ref: VANTA-SAMSARA-2026
    - lever: speed
      description: Unnamed global payments company reports parallel AI-driven assessments
      figure: "150 assessments in under 2 weeks"
      measures: "'150 assessments' launched in parallel and completed 'in under two weeks' with RiskAI, 'a process that once took several months'; '1,000+ hours saved with RiskAI'. Customer is anonymous."
      provenance: vendor-published
      source_ref: HYPERPROOF-FINCO-2025
    - lever: speed
      description: Calastone's analyst reports vendor document review time
      figure: "report in minutes"
      measures: "analyst's statement that automated review matches vendor documents to compliance standards and 'generates an entire report in minutes' (no baseline given)"
      provenance: vendor-published
      source_ref: WHISTIC-CALASTONE-2025
  prerequisites:
    - Written vendor risk criteria and tiering the agent evaluates against (DRATA-TPRMAI-2026)
    - Intake integration with procurement so new vendors are discovered; Samsara integrates bi-directionally with Zip (VANTA-SAMSARA-2026)
    - Prompt development, questionnaire design and calibration against assessor decisions are ongoing work for a small team (ANTHROPIC-JOB-SUPPLIER-2026)
  risks_and_guardrails:
    - Agent output is a draft; Anthropic's posting has analysts "verify agent-drafted evaluations" and route to domain specialists (ANTHROPIC-JOB-SUPPLIER-2026)
    - Vendors describe human final decision as a design principle (DRATA-TPRMAI-2026)
    - A Cloud Security Alliance research note says any AI-generated finding that triggers a consequential action needs a named human reviewer and a defined review path; the note itself says it was generated with AI assistance and not formally CSA-reviewed (CSA-AGENTS-2026)
  human_checkpoints:
    - Analyst decides residual risk and approval (ANTHROPIC-JOB-SUPPLIER-2026)
    - Final decisions sit with humans in Drata's described flow (DRATA-TPRMAI-2026)
  role_evolution: >
    Anthropic describes supplier assurance analysts as reviewers of agent-prefilled outputs who also tune the Claude-powered
    assessment platform (ANTHROPIC-JOB-SUPPLIER-2026). Plaid's posting asks a third-party risk analyst to handle more
    reviews without adding headcount using AI-assisted workflows (PLAID-JOB-TPRM-2026). OpenAI's posting asks a vendor
    security programme manager to use Codex for scoping, evidence checks and routing (OPENAI-JOB-VENDOR-2026).
  evidence_grade: A
  sources:
    - { ref: VANTA-SAMSARA-2026, title: "Samsara realized $150M+ in influenced revenue while scaling its GRC program with Vanta", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/samsara", date: 2026-05, access: full, locator: "TPRM paragraph under 'Vanta impact'" }
    - { ref: HYPERPROOF-FINCO-2025, title: "How Hyperproof Helped a Global Financial Enterprise Revolutionize Third-Party Risk Management", publisher: Hyperproof, type: vendor, url: "https://hyperproof.io/case-studies/how-hyperproof-helped-a-global-financial-enterprise-revolutionize-third-party-risk-management/", date: 2025-11-08, access: full, locator: "Stat tiles; 'Scalability for enterprise'" }
    - { ref: WHISTIC-CALASTONE-2025, title: "How Calastone Transformed TPRM with Whistic", publisher: Whistic, type: vendor, url: "https://www.whistic.com/resources/case-studies/calastone-customer-story", date: 2025-12, access: full, locator: "'Streamlined Vendor Assessments'" }
    - { ref: DRATA-TPRMAI-2026, title: "Accelerate Third-Party Reviews with AI (product page, undated; retrieved 2026-10-17)", publisher: Drata, type: vendor, url: "https://drata.com/product/vendor-risk-management/ai-agent", date: 2026-10-17, access: full, locator: "Intro; 'Maintain Oversight'" }
    - { ref: ANTHROPIC-JOB-SUPPLIER-2026, title: "Supplier Security & Assurance, Security GRC (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5427893008", date: 2026-09-17, access: full, locator: "About the role; Key responsibilities" }
    - { ref: PLAID-JOB-TPRM-2026, title: "Security Analyst, Third-Party Ecosystem Risk Management (job posting)", publisher: Plaid, type: job-posting, url: "https://jobs.ashbyhq.com/plaid/94752cfc-4a62-48c9-bcc0-e5f7f1905be6", date: 2026-08-12, access: full, locator: "'Scale Through AI and Tooling'" }
    - { ref: OPENAI-JOB-VENDOR-2026, title: "Vendor Security Technical Program Manager (job posting)", publisher: OpenAI, type: job-posting, url: "https://jobs.ashbyhq.com/openai/3ae71c21-60dd-42b2-a913-58df05988976", date: 2026-10-02, access: full, locator: "Qualifications" }
    - { ref: CSA-AGENTS-2026, title: "The Agents You Didn't Choose: Embedded AI and Liability", publisher: Cloud Security Alliance (CSAI Foundation), type: standard-setter, url: "https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/10/CSA_research_note_embedded_third_party_agents_systemic_risk_20261012-csa-styled.pdf", date: 2026-10-12, access: full, locator: "Key Takeaways" }
  last_reviewed: 2026-10-17
  notes: >
    Grade A rests on Samsara (named, measured, vendor-published, "up to"). The Hyperproof customer is anonymous, so it
    supports the claim but not a named-organisation grade. Safe Security markets a "TPRM AI Co-Worker" with 100+ agents
    (SAFE-TPRM-2026) and Optro announced Agentic TPRM on 2026-10-14 (OPTRO-CRX-2026); neither page gives customer outcomes.
    Doctor On Demand (Whistic) reports about 90% of questionnaire grading done in-platform and review time cut from a few
    hours to 45 minutes, but that is rule-based auto-grading of yes/no answers, not AI (WHISTIC-DOD-2025).

- id: security-governance-risk-04
  title: Continuous vendor monitoring with trigger-based reassessment instead of annual reviews
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: >
    Vendor approvals are point-in-time. A new SOC 2 report, new subprocessor, data-classification change or vendor incident
    can change the risk without anyone reopening the review.
  solution: >
    The programme defines triggers (new SOC 2 report, new subprocessor, vendor incident, drift in SaaS configuration or use
    case). An agent watches for them, reopens the assessment, prepares the delta and queues a reassessment for an analyst.
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "no figures in any source; Anthropic's posting describes the practice, Vanta and Safe describe product features"
      provenance: self-reported
      source_ref: ANTHROPIC-JOB-SUPPLIER-2026
  prerequisites:
    - Inventory of vendors with data classification and use-case context (ANTHROPIC-JOB-SUPPLIER-2026)
    - Feeds for vendor documents, breaches and legal events (SAFE-TPRM-2026)
  risks_and_guardrails:
    - Alert fatigue or false triggers are not discussed in any source read; no quality data found
  human_checkpoints:
    - Analyst runs reassessment when a trigger fires (ANTHROPIC-JOB-SUPPLIER-2026)
  role_evolution: >
    Anthropic's posting adds post-approval work (contractual security terms, configuration baselines, continuous monitoring)
    to the analyst role (ANTHROPIC-JOB-SUPPLIER-2026).
  evidence_grade: B
  sources:
    - { ref: ANTHROPIC-JOB-SUPPLIER-2026, title: "Supplier Security & Assurance, Security GRC (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5427893008", date: 2026-09-17, access: full, locator: "Key responsibilities: 'Run continuous monitoring after approval'" }
    - { ref: VANTA-TPRMAGENT-2026, title: "Vanta Delivers: TPRM Agent", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-delivers-tprm-agent", date: 2026-06, access: full, locator: "Feature list: full vendor lifecycle from discovery to continuous monitoring" }
    - { ref: SAFE-TPRM-2026, title: "SAFE TPRM AI Co-Worker (product page, undated; retrieved 2026-10-17)", publisher: Safe Security, type: vendor, url: "https://safe.security/third-party-risk-management/", date: 2026-10-17, access: full, locator: "'How the SAFE TPRM AI Co-Worker Operates': Threat Intel Agent" }
  last_reviewed: 2026-10-17
  notes: >
    Graded B on one named, present-tense job posting; maturity "in-production" is inferred from that wording, not
    from a published result.

- id: security-governance-risk-05
  title: Mapping and rationalising controls and evidence across frameworks with an agent
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Organisations holding many frameworks (SOC 2, ISO 27001, ISO 42001, HITRUST, FedRAMP) keep duplicate controls and
    map evidence by hand, and every audit repeats interviews with the same subject experts.
  solution: >
    An agent proposes a common control framework, maps controls and evidence items to each framework's requirements,
    and matches control sets to a new framework's controls. A GRC owner approves the mapping.
  outcomes:
    - lever: quality
      description: Samsara reports consolidating controls across 10 frameworks
      figure: "820 to 260 controls (68% reduction)"
      measures: "'820 controls consolidated to 260 (68% reduction)'; '1,200 evidence items mapped across 10 frameworks' using the Compliance Agent"
      provenance: vendor-published
      source_ref: VANTA-SAMSARA-2026
    - lever: capacity
      description: Samsara reports less subject-matter-expert interview time per audit cycle
      figure: "70 to 40 hours (43% reduction)"
      measures: "'SME interview time reduced from 70 to 40 hours per audit cycle'"
      provenance: vendor-published
      source_ref: VANTA-SAMSARA-2026
    - lever: speed
      description: Synthesia reports a compressed HITRUST implementation using a Vanta MCP server integration for control matching
      figure: "18 months to about 3 months"
      measures: "'Reduced an 18-month manual implementation timeline to approximately 3 months'; control matching across '500+ HiTrust controls', 'a task that would have taken 1.5 months manually'"
      provenance: vendor-published
      source_ref: VANTA-SYNTHESIA-2026
    - lever: quality
      description: Vanta reports precision of its AI control-to-evidence mapping on an offline evaluation set
      figure: "below 35% to 78% precision"
      measures: "precision of AI evidence suggestions on 'thousands of evidence suggestions across an extensive range of control descriptions'; baseline 'below 35%' with high recall, later 'precision to 78%'"
      provenance: vendor-published
      source_ref: VANTA-QUALITYEVAL-2026
  prerequisites:
    - A common control framework as the base (ANTHROPIC-JOB-CONTROLS-2026 describes owning one mapped to SOC 2, ISO 27001/42001, HIPAA, FedRAMP and customer commitments)
    - Integrations that supply evidence from connected systems (Synthesia: 50-60 connected systems) (VANTA-SYNTHESIA-2026)
    - An offline evaluation set curated by GRC experts to tune mapping quality (VANTA-QUALITYEVAL-2026)
  risks_and_guardrails:
    - Baseline mapping precision was below 35%, meaning most suggestions were wrong before tuning; the page reports no current error rate for all customers (VANTA-QUALITYEVAL-2026)
    - Vendor says its "agent" is human-in-the-loop (VANTA-RISKAGENT-2026 states this for risk; the compliance agent page uses recommendations language) (VANTA-COMPLIANCEAGENT-2026)
  human_checkpoints:
    - GRC owner reviews and approves mappings; Anthropic's controls role "decid[es] where human judgment stays in the loop" (ANTHROPIC-JOB-CONTROLS-2026)
  role_evolution: >
    Anthropic's Controls Specialist posting makes drafting and mapping controls with Claude "a normal part of the job" and
    expects the person to design continuous monitoring (ANTHROPIC-JOB-CONTROLS-2026).
  evidence_grade: A
  sources:
    - { ref: VANTA-SAMSARA-2026, title: "Samsara realized $150M+ in influenced revenue while scaling its GRC program with Vanta", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/samsara", date: 2026-05, access: full, locator: "Header stats; 'Vanta's Agentic Trust Platform' ROI list" }
    - { ref: VANTA-SYNTHESIA-2026, title: "How Synthesia became the first AI video company certified against ISO 42001", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/synthesia", date: 2026-10, access: full, locator: "'MCP Server integration' bullet" }
    - { ref: VANTA-QUALITYEVAL-2026, title: "Vanta AI Quality Eval Maturity Model", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-ai-quality-evaluation-maturity-model", date: 2026-07, access: full, locator: "Example: AI-powered control-to-evidence mapping" }
    - { ref: VANTA-COMPLIANCEAGENT-2026, title: "Vanta Delivers: Compliance Agent", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-delivers-compliance-agent", date: 2026-06, access: full, locator: "Feature list" }
    - { ref: VANTA-RISKAGENT-2026, title: "Vanta Delivers: Agent for Risk", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-delivers-agent-for-risk", date: 2026-06, access: full, locator: "'Act with a human in the loop, always'" }
    - { ref: ANTHROPIC-JOB-CONTROLS-2026, title: "Controls Specialist, Security GRC (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5436826008", date: 2026-09-29, access: full, locator: "About the role; Key responsibilities" }
  last_reviewed: 2026-10-17
  notes: >
    Samsara's "estimated $300,000+ in ROI in year one" is the company's estimate and is not used as an outcome.
    The ISO 42001 certification at Samsara ("among the first 100 companies globally") and at Synthesia concerns governing
    the companies' own AI products and is routed to the ai-security module.

- id: security-governance-risk-06
  title: Agent-run evidence collection and continuous control monitoring in place of periodic audit preparation
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: >
    Control evidence is gathered by hand before each audit, so control failures are found late and staff spend a large
    share of their time on it.
  solution: >
    Connectors pull evidence from source systems, agents validate it against control descriptions, flag drift
    before an auditor does, and push issues to control owners. GRC engineers build the automated tests and the
    agent workflows.
  outcomes:
    - lever: capacity
      description: Synthesia reports share of evidence collection automated
      figure: "60%"
      measures: "'60% of evidence collection automated across 50-60 connected systems'; 'Five framework audit cycles condensed into a one-month window'. Source does not separate AI from non-AI integrations."
      provenance: vendor-published
      source_ref: VANTA-SYNTHESIA-2026
    - lever: capacity
      description: Perforce reports compliance work as a share of its team's time
      figure: "60% to 15%"
      measures: "'Manual compliance work dropped from 60% to 15% of the team's time' after consolidating onto a GRC platform; page also cites '75% reduction in compliance labor'. Platform consolidation, not AI alone."
      provenance: vendor-published
      source_ref: VANTA-PERFORCE-2026
  prerequisites:
    - Machine-readable control definitions (Figma posting: JSON control definitions and APIs) (FIGMA-JOB-COMPLIANCEENG-2026)
    - Engineers inside the GRC team who can build integrations (CLOUDFLARE-JOB-GRC-2026; PLAID-JOB-GRC-2026)
  risks_and_guardrails:
    - Anthropic's posting says the aim is to "challenge and evidence the performance of controls continuously rather than through periodic audits", with "the right humans in the loop" (ANTHROPIC-JOB-CONTROLS-2026)
    - The posting says monitoring work includes tuning out false positives, but no false-positive rate is published (ANTHROPIC-JOB-CONTROLS-2026)
  human_checkpoints:
    - Control owners drive findings to closure; auditors still receive the evidence (ANTHROPIC-JOB-CONTROLS-2026)
  role_evolution: >
    Postings at Anthropic, OpenAI, Okta, Plaid, Cloudflare and Figma ask for GRC "engineers" who build automations and
    agent workflows (ANTHROPIC-JOB-GRCPLATFORM-2026; OPENAI-JOB-AUDIT-2026; OKTA-JOB-GRC-2026; PLAID-JOB-GRC-2026;
    CLOUDFLARE-JOB-GRC-2026; FIGMA-JOB-COMPLIANCEENG-2026).
  evidence_grade: B
  sources:
    - { ref: VANTA-SYNTHESIA-2026, title: "How Synthesia became the first AI video company certified against ISO 42001", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/synthesia", date: 2026-10, access: full, locator: "ROI bullets under 'Multi-framework compliance management'" }
    - { ref: VANTA-PERFORCE-2026, title: "Perforce unifies enterprise compliance, security, and risk with Vanta", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/perforce", date: 2026-03, access: full, locator: "TL;DR; 'Vanta's Agentic Trust Platform' ROI" }
    - { ref: ANTHROPIC-JOB-CONTROLS-2026, title: "Controls Specialist, Security GRC (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5436826008", date: 2026-09-29, access: full, locator: "About the role" }
    - { ref: ANTHROPIC-JOB-GRCPLATFORM-2026, title: "Staff+ Software Engineer, GRC Platform (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5250091008", date: 2026-06-08, access: full, locator: "Role summary and responsibilities" }
    - { ref: OKTA-JOB-GRC-2026, title: "Senior Director, GRC (job posting)", publisher: Okta, type: job-posting, url: "https://www.okta.com/company/careers/opportunity/8130437?gh_jid=8130437", date: 2026-08-17, access: full, locator: "'Drive AI-first Transformation'" }
    - { ref: PLAID-JOB-GRC-2026, title: "Security Engineer, GRC (job posting)", publisher: Plaid, type: job-posting, url: "https://jobs.ashbyhq.com/plaid/587e83dd-1d1b-4f31-812a-74fc67d67fbe", date: 2026-07-16, access: full, locator: "'Shift Compliance Left with Code and AI'" }
    - { ref: CLOUDFLARE-JOB-GRC-2026, title: "GRC Engineer (job posting)", publisher: Cloudflare, type: job-posting, url: "https://boards.greenhouse.io/cloudflare/jobs/8045914?gh_jid=8045914", date: 2026-07-08, access: full, locator: "About the role" }
    - { ref: FIGMA-JOB-COMPLIANCEENG-2026, title: "Compliance Engineer (job posting)", publisher: Figma, type: job-posting, url: "https://boards.greenhouse.io/figma/jobs/6223155004?gh_jid=6223155004", date: 2026-10-16, access: full, locator: "Role summary and responsibilities" }
    - { ref: OPENAI-JOB-AUDIT-2026, title: "GRC Program Manager, Audit & Controls (job posting)", publisher: OpenAI, type: job-posting, url: "https://jobs.ashbyhq.com/openai/aeac2b78-1f4a-4dfe-b88f-25fc8adf5bb3", date: 2026-08-06, access: full, locator: "Role summary" }
  last_reviewed: 2026-10-17
  notes: >
    Maturity "piloting": Anthropic's wording is "We're building toward" continuous, Claude-directed control testing.
    Measurements are for platform automation in general, so the grade is capped at B.

- id: security-governance-risk-07
  title: Autonomous control testing that produces audit-ready workpapers
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >
    Control testing, such as user access reviews and reconciliations, is done by sampling and manual fieldwork, then
    written up as workpapers for internal and external auditors.
  solution: >
    Agents ingest unstructured evidence (PDFs, spreadsheets, video walkthroughs), run attribute tests on the full set
    of uploaded evidence, record each step, and assemble Excel workpapers linked back to source evidence for human review.
  outcomes:
    - lever: capacity
      description: none published
      figure: "none published"
      measures: "vendor describes 'full population coverage' and 'reduce manual effort' without figures"
      provenance: vendor-published
      source_ref: OPTRO-CRX-2026
  prerequisites:
    - Controls and evidence held in a system of record that agents can read (OPTRO-AUTOTEST-2026)
  risks_and_guardrails:
    - Optro says agent actions are logged, cited and reviewable (OPTRO-CRX-2026)
    - Anthropic's SOX role asks for "grounded, specific views" on which assurance workflows AI can run today and which it cannot yet (ANTHROPIC-JOB-SOX-2026)
  human_checkpoints:
    - Auditors review workpapers and exceptions (OPTRO-AUTOTEST-2026)
  role_evolution: >
    Optro says auditors' work "starts at the review" of documented workpapers (OPTRO-AUTOTEST-2026).
  evidence_grade: C
  sources:
    - { ref: OPTRO-CRX-2026, title: "GRC Intelligence takes the stage at CRX '26", publisher: Optro (formerly AuditBoard), type: vendor, url: "https://optro.ai/blog/grc-intelligence-takes-the-stage-crx-26", date: 2026-10-14, access: full, locator: "'Agentic capabilities extend across GRC'" }
    - { ref: OPTRO-AUTOTEST-2026, title: "Autonomous testing software (product page, undated; retrieved 2026-10-17)", publisher: Optro, type: vendor, url: "https://auditboard.com/product/autonomous-testing", date: 2026-10-17, access: full, locator: "Feature list and FAQ on the Midship acquisition" }
    - { ref: ANTHROPIC-JOB-SOX-2026, title: "Lead, Security Controls Assurance - SOX (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5415864008", date: 2026-09-08, access: full, locator: "Qualifications" }
  last_reviewed: 2026-10-17
  notes: >
    Optro's page and blog are about SOX and operational controls (user access reviews, bank reconciliations); this is
    adjacent to security-control testing. Optro acquired Midship (SOX testing; founded 2024) and FairNow (AI governance); acquisition dates not captured.

- id: security-governance-risk-08
  title: Policy drafting, upkeep and policy-to-practice consistency checks with AI
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Policies drift from what teams do and from what customer documents say, and policy sets must be updated for each new framework.
  solution: >
    AI drafts tailored policy documents, keeps a policy database current across frameworks, and compares policies
    with programme data or customer-facing reports to surface inconsistencies for a person to fix.
  outcomes:
    - lever: quality
      description: Calastone's analyst reports using AI to spot mismatches between its own policies and its SIG report
      figure: none published
      measures: "qualitative statement ('we noticed that our own policies didn't always align perfectly to what our SIG report was telling us'); no count"
      provenance: vendor-published
      source_ref: WHISTIC-CALASTONE-2025
    - lever: quality
      description: Independent test of LLM translation of natural-language access-control policies to executable policy code
      figure: "50.3% vs 15.3%"
      measures: "end-to-end policy correctness on 372 access-control statements (compile, lint, positive and negative tests) for a structured pipeline vs a single-prompt baseline; adjacent (access-control policy, not security GRC policy text)"
      provenance: independent
      source_ref: ARXIV-2609.24036
  prerequisites:
    - Policy repository connected to programme data (VANTA-COMPLIANCEAGENT-2026)
  risks_and_guardrails:
    - A single-prompt LLM got 15.3% of policies right in the access-control study, so structured pipelines and tests are needed before enforcing generated policy code (ARXIV-2609.24036)
    - A proof-of-concept on a simulated brute-force incident found LLM-assisted policy gap analysis useful but stresses continued human oversight; no accuracy figure (ARXIV-2601.03287)
  human_checkpoints:
    - Policy owners review flagged inconsistencies (VANTA-COMPLIANCEAGENT-2026)
  role_evolution: >
    GitLab's governance posting asks for AI-assisted workflows for policy management, evidence collection and control monitoring, working with a separate GRC Engineering team (GITLAB-JOB-GOV-2026).
  evidence_grade: B
  sources:
    - { ref: WHISTIC-CALASTONE-2025, title: "How Calastone Transformed TPRM with Whistic", publisher: Whistic, type: vendor, url: "https://www.whistic.com/resources/case-studies/calastone-customer-story", date: 2025-12, access: full, locator: "'AI-Powered Insights'" }
    - { ref: VANTA-SYNTHESIA-2026, title: "How Synthesia became the first AI video company certified against ISO 42001", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/synthesia", date: 2026-10, access: full, locator: "'Vanta AI' bullet: 'Policy database kept current across all six frameworks'" }
    - { ref: VANTA-COMPLIANCEAGENT-2026, title: "Vanta Delivers: Compliance Agent", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-delivers-compliance-agent", date: 2026-06, access: full, locator: "'Policy-to-program consistency checks'" }
    - { ref: ARXIV-2609.24036, title: "Structured Decomposition for Reliable LLM-Generated Access Control Policies", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.24036", date: 2026-09-21, access: full, locator: "Abstract" }
    - { ref: ARXIV-2601.03287, title: "Automated Post-Incident Policy Gap Analysis via Threat-Informed Evidence Mapping using LLMs", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2601.03287", date: 2026-01-04, access: full, locator: "Abstract" }
    - { ref: GITLAB-JOB-GOV-2026, title: "Staff Security Governance Engineer, Policies & Standards (job posting)", publisher: GitLab, type: job-posting, url: "https://job-boards.greenhouse.io/gitlab/jobs/8846277002", date: 2026-09-30, access: full, locator: "'Automation and AI' section" }
  last_reviewed: 2026-10-17
  notes: >
    The independent figure is from an adjacent process (access-control rules), which would cap this grade at B in any case.

- id: security-governance-risk-09
  title: Risk register upkeep, intake triage and first-draft risk analyses with AI
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [expert-judgment, research-synthesis, document-production]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >
    Risk analysts spend time classifying incoming risks, keeping the register clean, linking risks to assets, controls and
    vendors, and drafting analyses for leadership.
  solution: >
    AI classifies and triages incoming risks, drafts first-pass risk analyses, links each risk scenario to affected
    assets, relevant controls and vendors, and generates reports. Analysts own calibration and review.
  outcomes:
    - lever: quality
      description: Independent comparison of five LLMs with 50 human experts scoring cybersecurity risk scenarios
      figure: "LLMs consistently lower"
      measures: "the study reports that the five LLMs (ChatGPT 5, DeepSeek V3.1, Llama 4 Scout, Claude Opus 4.1, Gemini 2.5 Pro) 'consistently underestimated cybersecurity risks compared to human experts' on 18 CIS-Controls-based scenarios; abstract gives no numeric gap"
      provenance: independent
      source_ref: ARXIV-2605.05424
  prerequisites:
    - Asset, control and vendor data in one place so risks can be mapped (VANTA-RISKAGENT-2026)
    - Calibration and quality review owned by named analysts (ANTHROPIC-JOB-RISKANALYST-2026)
  risks_and_guardrails:
    - Models tended to underestimate risk compared with experts; the authors say LLMs should be complementary tools, not standalone assessors (ARXIV-2605.05424)
    - Vanta says program owners "review, adjust, and add additional context" to suggestions (VANTA-RISKAGENT-2026)
  human_checkpoints:
    - Analyst reviews AI outputs; Anthropic's analyst "own[s] the calibration and quality review" (ANTHROPIC-JOB-RISKANALYST-2026)
  role_evolution: >
    Anthropic says it is rebuilding risk management "to operate as an engineering function" and Plaid asks analysts to be "AI power users" who automate risk-program work (ANTHROPIC-JOB-RISKANALYST-2026; PLAID-JOB-RISK-2026).
  evidence_grade: B
  sources:
    - { ref: ANTHROPIC-JOB-RISKENG-2026, title: "Staff Security Engineer, Risk Engineering (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5250052008", date: 2026-06-08, access: full, locator: "'Risk platform and automation': AI-native risk tooling that uses Claude to classify incoming risks" }
    - { ref: ANTHROPIC-JOB-RISKANALYST-2026, title: "Security Risk Analyst, Risk Engineering (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5397704008", date: 2026-10-05, access: full, locator: "About the role; responsibilities" }
    - { ref: PLAID-JOB-RISK-2026, title: "Senior Security Analyst, Security Risk Management (job posting)", publisher: Plaid, type: job-posting, url: "https://jobs.ashbyhq.com/plaid/4c4af954-2c70-4a3c-acc2-97c58211f920", date: 2026-10-12, access: full, locator: "'Scale Through AI and Automation'" }
    - { ref: VANTA-RISKAGENT-2026, title: "Vanta Delivers: Agent for Risk", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-delivers-agent-for-risk", date: 2026-06, access: full, locator: "Risk to Asset, Control and Vendor Mapping" }
    - { ref: ARXIV-2605.05424, title: "Evaluating the Reliability of Multiple LLMs in Risk Assessment: A CIS Controls Based Approach", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2605.05424", date: 2026-05-06, access: full, locator: "Abstract; Methodology (50 respondents, five models)" }
  last_reviewed: 2026-10-17
  notes: >
    Grade B on named employer postings (Anthropic: "design and build" language; Plaid: "build AI skills and automations").
    No before/after metrics anywhere. Optro announced "AURA Risk Assessment" (evidence-backed risk scores) on 2026-10-14 (OPTRO-CRX-2026).

- id: security-governance-risk-10
  title: "Quantified cyber risk analysis (calibrated estimates, FAIR-style simulation) with AI assistance"
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [expert-judgment, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >
    Risk quantification needs frequency and loss estimates that take scarce expert time, and results go stale between
    reviews.
  solution: >
    Analysts use AI to speed scenario scoping and data gathering, then apply calibrated estimation or Monte Carlo
    simulation where it changes a resource or treatment decision. Vendors add automated control and exposure data
    feeds to update quantified exposure.
  outcomes:
    - lever: speed
      description: T-Mobile reports faster control assessment when NIST CSF was updated, using the vendor's integrations
      figure: "75% reduction in reporting time"
      measures: "'rapidly assess controls and prioritize remediation in just a week - a 75% reduction in reporting time' on updating control documentation for a new NIST CSF version using SAFE One integrations; the page does not say AI was responsible"
      provenance: vendor-published
      source_ref: SAFE-TMOBILE-2026
  prerequisites:
    - Quantified risk programme with outputs that change real resource decisions (ANTHROPIC-JOB-RISKENG-2026 asks for this experience)
  risks_and_guardrails:
    - LLMs underestimated risk against 50 experts in an independent study; calibration against expert judgment is needed (ARXIV-2605.05424)
  human_checkpoints:
    - Analysts own estimate calibration (ANTHROPIC-JOB-RISKENG-2026)
  role_evolution: >
    Anthropic's posting asks risk engineers to apply calibrated estimation and Monte Carlo simulation and to build the AI risk tooling (ANTHROPIC-JOB-RISKENG-2026).
  evidence_grade: C
  sources:
    - { ref: SAFE-TMOBILE-2026, title: "T-Mobile: Cutting the Cord on Subjective Risk Scores (customer story, undated; retrieved 2026-10-17)", publisher: Safe Security, type: vendor, url: "https://safe.security/resources/customer-stories/t-mobile-cutting-the-cord-on-subjective-risk-scores/", date: 2026-10-17, access: full, locator: "'The Moment of Truth' paragraph" }
    - { ref: ANTHROPIC-JOB-RISKENG-2026, title: "Staff Security Engineer, Risk Engineering (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5250052008", date: 2026-06-08, access: full, locator: "'Risk assessment and quantification'" }
    - { ref: FAIR-BOARD-2026, title: "The Board Understands Risk. Does the Business?", publisher: FAIR Institute, type: professional-body, url: "https://www.fairinstitute.org/blog/the-board-understands-risk.-does-the-business", date: 2026-10-17, access: full, locator: "Whole post; discusses the 2026 State of Cyber Risk Management Report and quantification, no AI content" }
    - { ref: ARXIV-2605.05424, title: "Evaluating the Reliability of Multiple LLMs in Risk Assessment: A CIS Controls Based Approach", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2605.05424", date: 2026-05-06, access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: >
    The FAIR Institute post carries no publication date in the text retrieved; date shown is the retrieval date. No source found describes an LLM-built FAIR analysis at a named company with results; the FAIR Institute's own blog index shows AI risk topics but not AI-assisted quantification practice. Kovrr's "AI Risk Quantification" quantifies the risk of AI systems and is routed (see section 4).

- id: security-governance-risk-11
  title: Board and executive risk reporting packs generated from live GRC and risk data
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [data-reporting, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    CISOs get five to ten minutes with the board, and reports are often "structured around cybersecurity, not around the business".
  solution: >
    Programme data (risk register, control status, vendor posture, quantified exposure) feeds a structured board
    pack that AI drafts; the CISO edits the narrative.
  outcomes:
    - lever: speed
      description: none published
      figure: "none published"
      measures: "Perforce 'plans to use Vanta for regular risk reviews and board-level reporting'; no result yet"
      provenance: vendor-published
      source_ref: VANTA-PERFORCE-2026
  prerequisites:
    - Stable, minimum set of indicators per report section, consistent over time (TECHTARGET-BOARD-2026)
  risks_and_guardrails:
    - Gartner analysts say board reports fail when structured around cybersecurity and not the business (TECHTARGET-BOARD-2026)
  human_checkpoints:
    - CISO owns the narrative section and requests to the board (TECHTARGET-BOARD-2026)
  role_evolution: >
    Gartner analysts say financial-report-style templates elevate the CISO's profile as a business leader (TECHTARGET-BOARD-2026).
  evidence_grade: C
  sources:
    - { ref: VANTA-PERFORCE-2026, title: "Perforce unifies enterprise compliance, security, and risk with Vanta", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/perforce", date: 2026-03, access: full, locator: "ROI bullet 'Vendor and Enterprise Risk Management'" }
    - { ref: TECHTARGET-BOARD-2026, title: "Lost in translation: Cybersecurity board reporting for CISOs", publisher: TechTarget SearchSecurity, type: press, url: "https://www.techtarget.com/cybersecurity/news/366643884/Lost-in-translation-Cybersecurity-board-reporting-for-CISOs", date: 2026-06-03, access: full, locator: "Gartner session summary: board report structure" }
    - { ref: PROOFPOINT-VOC-2026, title: "The risk has moved: what Proofpoint's 2026 Voice of the CISO reveals", publisher: Proofpoint, type: survey, url: "https://www.proofpoint.com/au/blog/corporate-news/risk-has-moved-what-proofpoints-2026-voice-ciso-reveals", date: 2026-09-09, access: full, locator: "'Board alignment is improving' section" }
  last_reviewed: 2026-10-17
  notes: >
    The Gartner session and the Proofpoint survey discuss board reporting but not AI drafting; this is the weakest entry on AI use.
    Safe Security and Kovrr market board-reporting features but those pages were not read for board packs, so they are not used.

- id: security-governance-risk-12
  title: Regulatory and framework obligations (EU AI Act, NIST AI RMF, ISO 42001) mapped into security policy and controls
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Security teams must reconcile overlapping AI-related and security rules and keep policy-to-regulation mappings current.
  solution: >
    Governance engineers use automation and AI-assisted workflows to monitor regulations, assess impact with Legal and update policy mappings.
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "no measured outcome; sources are postings and session summaries"
      provenance: self-reported
      source_ref: GITLAB-JOB-GOV-2026
  prerequisites:
    - Maintained mapping between policies and external standards (GITLAB-JOB-GOV-2026)
  risks_and_guardrails:
    - EU AI Act dates moved: obligations for Annex III high-risk systems apply from 2027-12-02, transparency rules from August 2026 (EC-AIACT-2026)
    - US SEC rules in this area face a rescission request from trade associations (SIFMA-SEC-2026)
  human_checkpoints:
    - Legal partnership on compliance deadlines (GITLAB-JOB-GOV-2026)
  role_evolution: >
    GitLab's governance engineer turns emerging regulations, including AI regulation, into requirements for engineering, product and legal (GITLAB-JOB-GOV-2026).
  evidence_grade: C
  sources:
    - { ref: GITLAB-JOB-GOV-2026, title: "Staff Security Governance Engineer, Policies & Standards (job posting)", publisher: GitLab, type: job-posting, url: "https://job-boards.greenhouse.io/gitlab/jobs/8846277002", date: 2026-09-30, access: full, locator: "'Regulatory and framework alignment'; 'Automation and AI'" }
    - { ref: OKTA-JOB-GRC-2026, title: "Senior Director, GRC (job posting)", publisher: Okta, type: job-posting, url: "https://www.okta.com/company/careers/opportunity/8130437?gh_jid=8130437", date: 2026-08-17, access: full, locator: "'Drive AI-first Transformation': intelligent policy mapping" }
    - { ref: EC-AIACT-2026, title: "AI Act: regulatory framework for AI (status page)", publisher: European Commission, type: regulator, url: "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai", date: 2026-10-17, access: full, locator: "Timeline section" }
    - { ref: SIFMA-SEC-2026, title: "Reforming Regulation S-K cybersecurity disclosures (joint trades letter)", publisher: SIFMA and joint trade associations, type: professional-body, url: "https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades", date: 2026-04-10, access: full, locator: "Opening and section I (rescind Item 106)" }
  last_reviewed: 2026-10-17
  notes: >
    Evidence of AI doing the mapping is intent in job postings only; the regulatory sources set context, not AI use.

- id: security-governance-risk-13
  title: "GRC engineering operating model: engineers build compliance automation and agent workflows inside the GRC team"
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [software-systems, review-assurance]
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >
    Compliance headcount scales with frameworks, vendors and customer requests, while expectations for continuous assurance rise.
  solution: >
    GRC teams hire software and automation engineers, define controls as machine-readable code, build internal
    platforms with LLM components, and expect analysts to build their own AI skills and automations.
  outcomes:
    - lever: capacity
      description: none published
      figure: "none published"
      measures: "no measured result; postings describe design intent"
      provenance: self-reported
      source_ref: ANTHROPIC-JOB-GRCPLATFORM-2026
  prerequisites:
    - Engineers with GRC knowledge and a platform to build on (ANTHROPIC-JOB-GRCPLATFORM-2026; CLOUDFLARE-JOB-GRC-2026)
    - Machine-readable control definitions and APIs (FIGMA-JOB-COMPLIANCEENG-2026)
  risks_and_guardrails:
    - Anthropic's posting asks for LLM components "reliable enough for high-stakes use" with evaluation of outputs (ANTHROPIC-JOB-GRCPLATFORM-2026)
    - Vanta's own work shows most of its AI teams started "deep in red and yellow" on its evaluation model (VANTA-QUALITYEVAL-2026)
  human_checkpoints:
    - Human-in-the-loop design stated in Anthropic's postings (ANTHROPIC-JOB-CONTROLS-2026)
  role_evolution: >
    Seven employers' postings (Anthropic, OpenAI, Plaid, Cloudflare, Okta, GitLab, Figma) ask for builder profiles in GRC; Plaid expects analysts to share AI automations with the team (PLAID-JOB-TPRM-2026; PLAID-JOB-RISK-2026). Vanta cites an Axipro study of 3,519 AI-related postings in eight EU countries: 3,004 builder roles to 446 governance roles, about 7 to 1, with fewer than 3 in 10 governance postings naming the EU AI Act (VANTA-AIGOVGAP-2026).
  evidence_grade: B
  sources:
    - { ref: ANTHROPIC-JOB-GRCPLATFORM-2026, title: "Staff+ Software Engineer, GRC Platform (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5250091008", date: 2026-06-08, access: full, locator: "Responsibilities and qualifications" }
    - { ref: OPENAI-JOB-ERM-2026, title: "Head of Enterprise Risk Management (job posting)", publisher: OpenAI, type: job-posting, url: "https://jobs.ashbyhq.com/openai/db40bc4f-c7fb-47d5-a7cc-918fb8b1f815", date: 2026-10-14, access: full, locator: "Role summary and qualifications" }
    - { ref: PLAID-JOB-GRC-2026, title: "Security Engineer, GRC (job posting)", publisher: Plaid, type: job-posting, url: "https://jobs.ashbyhq.com/plaid/587e83dd-1d1b-4f31-812a-74fc67d67fbe", date: 2026-07-16, access: full, locator: "Role summary" }
    - { ref: CLOUDFLARE-JOB-GRC-2026, title: "GRC Engineer (job posting)", publisher: Cloudflare, type: job-posting, url: "https://boards.greenhouse.io/cloudflare/jobs/8045914?gh_jid=8045914", date: 2026-07-08, access: full, locator: "About the role" }
    - { ref: FIGMA-JOB-COMPLIANCEENG-2026, title: "Compliance Engineer (job posting)", publisher: Figma, type: job-posting, url: "https://boards.greenhouse.io/figma/jobs/6223155004?gh_jid=6223155004", date: 2026-10-16, access: full, locator: "Role summary" }
    - { ref: PLAID-JOB-TPRM-2026, title: "Security Analyst, Third-Party Ecosystem Risk Management (job posting)", publisher: Plaid, type: job-posting, url: "https://jobs.ashbyhq.com/plaid/94752cfc-4a62-48c9-bcc0-e5f7f1905be6", date: 2026-08-12, access: full, locator: "Role summary" }
    - { ref: PLAID-JOB-RISK-2026, title: "Senior Security Analyst, Security Risk Management (job posting)", publisher: Plaid, type: job-posting, url: "https://jobs.ashbyhq.com/plaid/4c4af954-2c70-4a3c-acc2-97c58211f920", date: 2026-10-12, access: full, locator: "Role summary" }
    - { ref: ANTHROPIC-JOB-CONTROLS-2026, title: "Controls Specialist, Security GRC (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5436826008", date: 2026-09-29, access: full, locator: "About the role" }
    - { ref: VANTA-QUALITYEVAL-2026, title: "Vanta AI Quality Eval Maturity Model", publisher: Vanta, type: vendor, url: "https://www.vanta.com/resources/vanta-ai-quality-evaluation-maturity-model", date: 2026-07, access: full, locator: "'When we first ran this assessment'" }
    - { ref: VANTA-AIGOVGAP-2026, title: "The AI governance confidence gap", publisher: Vanta (citing Axipro 2026 State of AI Governance Hiring in Europe), type: vendor, url: "https://www.vanta.com/resources/ai-governance-confidence-gap", date: 2026-07, access: full, locator: "Data section" }
  last_reviewed: 2026-10-17
  notes: >
    Evidence is employer self-description only. The Axipro study is secondary, via a vendor blog; it counts AI governance hiring across
    all functions in eight EU countries, not security teams.

- id: security-governance-risk-14
  title: Security-owned policy and approval gates for AI use and AI agents (the security team as policy author and reviewer)
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [expert-judgment, document-production, review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Staff and teams adopt AI tools and agents faster than policy; security teams must decide what data agents may touch and
    which actions need human approval, while using AI themselves.
  solution: >
    The GRC function writes agent governance policies and standards, defines review and approval criteria (sensitive
    data, human-approval actions, least privilege), sits as GRC reviewer in engineering approval workflows, and monitors
    agent behaviour. Governance frameworks use fixed "action gates" and risk thresholds.
  outcomes:
    - lever: risk
      description: "Survey: security professionals involved in writing AI policy"
      figure: "56%"
      measures: "'56 percent of respondents say that they or someone from their team were involved in the development of a policy governing the use of AI in their organization' (ISACA 2026 State of Cybersecurity; more than 1,800 cybersecurity professionals)"
      provenance: independent
      source_ref: ISACA-SOC-2026
    - lever: risk
      description: "Survey: organisations restricting employee GenAI use"
      figure: "78%"
      measures: "'78% of organizations block or limit employee use of GenAI' (Proofpoint 2026 Voice of the CISO, 1,600 CISOs, 16 markets)"
      provenance: vendor-published
      source_ref: PROOFPOINT-VOC-2026
  prerequisites:
    - Inventory of which AI tools and agents are in use and what data they reach (PROOFPOINT-VOC-2026)
    - Deterministic action gates and predefined risk thresholds (CLOUDFLARE-JOB-GRC-2026)
  risks_and_guardrails:
    - Only 8% of organisations run regular AI-specific response exercises; 48% do not know of or lack AI incident playbooks (ISACA-SOC-2026)
    - 79% of CISOs say they are expected to manage AI risk without a proportional increase in resources (PROOFPOINT-VOC-2026)
    - AI-generated findings that drive consequential action need a named reviewer (CSA-AGENTS-2026)
    - A 2024 Splunk report found 34% of respondents lacked an acceptable-use policy for generative AI while 91% said security teams used public generative AI tools; this is older and vendor-run (SPLUNK-CISOPOLICY-2024)
  human_checkpoints:
    - Policy defines which agent actions need human approval (ANTHROPIC-JOB-AGENTSEC-2026)
  role_evolution: >
    ISACA reports 51% of respondents are now involved in developing, onboarding or implementing AI solutions, up from 40% in 2025 and 29% in 2024, and 45% see LLM SecOps as a skill gap (ISACA-SOC-2026). Anthropic's posting makes the GRC person "the security policy partner for AI agent governance" (ANTHROPIC-JOB-AGENTSEC-2026).
  evidence_grade: B
  sources:
    - { ref: ANTHROPIC-JOB-AGENTSEC-2026, title: "Security Risk & Compliance, Agent Security (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5443871008", date: 2026-10-05, access: full, locator: "Responsibilities" }
    - { ref: CLOUDFLARE-JOB-GRC-2026, title: "GRC Engineer (job posting)", publisher: Cloudflare, type: job-posting, url: "https://boards.greenhouse.io/cloudflare/jobs/8045914?gh_jid=8045914", date: 2026-07-08, access: full, locator: "'AI Governance' bullet" }
    - { ref: ISACA-SOC-2026, title: "Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds (State of Cybersecurity 2026)", publisher: ISACA, type: professional-body, url: "https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises", date: 2026-09-22, access: full, locator: "Paragraphs on AI incident response planning and AI governance" }
    - { ref: PROOFPOINT-VOC-2026, title: "The risk has moved: what Proofpoint's 2026 Voice of the CISO reveals", publisher: Proofpoint, type: survey, url: "https://www.proofpoint.com/au/blog/corporate-news/risk-has-moved-what-proofpoints-2026-voice-ciso-reveals", date: 2026-09-09, access: full, locator: "Paragraphs on GenAI risk and governance" }
    - { ref: CSA-AGENTS-2026, title: "The Agents You Didn't Choose: Embedded AI and Liability", publisher: Cloud Security Alliance (CSAI Foundation), type: standard-setter, url: "https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/10/CSA_research_note_embedded_third_party_agents_systemic_risk_20261012-csa-styled.pdf", date: 2026-10-12, access: full, locator: "Key Takeaways" }
    - { ref: SPLUNK-CISOPOLICY-2024, title: "A CISO's Guide to Generative AI Policy", publisher: Splunk, type: vendor, url: "https://www.splunk.com/en_us/blog/ciso-circle/ciso-gen-ai-policy.html", date: 2024-07-31, access: full, locator: "Opening findings from State of Security 2024" }
    - { ref: CISA-AGENTIC-2026, title: "Careful Adoption of Agentic AI Services (retrieved copy titled 'Agentic SI Services')", publisher: CISA with ASD's ACSC and partners, type: regulator, url: "https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services", date: 2026-05-01, access: full, locator: "Landing page summary only (the guide itself was not retrieved)" }
  last_reviewed: 2026-10-17
  notes: >
    Anthropic's and Cloudflare's postings are for named roles, so the grade is B, but no policy text was read. The CISA page
    opened via the text mirror shows "AI" replaced by "super intelligence (SI)" in the title and summary; the landscape file
    recorded the same anomaly. Only the landing page was read; its content is not relied on beyond the statement that it aligns AI risk
    management with existing cybersecurity frameworks.

- id: security-governance-risk-15
  title: Audit response drafting and audit-cycle consolidation with AI
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >
    Each external audit asks subject experts for the same walkthroughs and evidence, and several audits run in parallel.
  solution: >
    AI drafts responses to auditor requests from existing evidence, and one evidence set is mapped to several frameworks so audits can be run together.
  outcomes:
    - lever: capacity
      description: Synthesia reports consolidating audit cycles
      figure: "five framework audit cycles in one month"
      measures: "'Five framework audit cycles condensed into a one-month window' (frameworks listed: ISO 27001, ISO 27018, ISO 27701, ISO 42001, SOC 2, HITRUST); AI contribution not isolated"
      provenance: vendor-published
      source_ref: VANTA-SYNTHESIA-2026
    - lever: capacity
      description: Samsara reports less expert time per audit cycle
      figure: "70 to 40 hours"
      measures: "'SME interview time reduced from 70 to 40 hours per audit cycle'"
      provenance: vendor-published
      source_ref: VANTA-SAMSARA-2026
  prerequisites:
    - Common control framework and mapped evidence (VANTA-SAMSARA-2026)
  risks_and_guardrails:
    - Auditor reliance on AI-prepared evidence is not documented in any source read
  human_checkpoints:
    - Control owners and auditors review responses (ANTHROPIC-JOB-GRCPLATFORM-2026)
  role_evolution: >
    Anthropic's GRC platform role has engineers design workflows where Claude "generat[es] audit responses" (ANTHROPIC-JOB-GRCPLATFORM-2026).
  evidence_grade: B
  sources:
    - { ref: VANTA-SYNTHESIA-2026, title: "How Synthesia became the first AI video company certified against ISO 42001", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/synthesia", date: 2026-10, access: full, locator: "Multi-framework compliance bullet" }
    - { ref: VANTA-SAMSARA-2026, title: "Samsara realized $150M+ in influenced revenue while scaling its GRC program with Vanta", publisher: Vanta, type: vendor, url: "https://www.vanta.com/customers/samsara", date: 2026-05, access: full, locator: "ROI list" }
    - { ref: ANTHROPIC-JOB-GRCPLATFORM-2026, title: "Staff+ Software Engineer, GRC Platform (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5250091008", date: 2026-06-08, access: full, locator: "Responsibilities" }
  last_reviewed: 2026-10-17
  notes: >
    Overlaps with use cases 05 and 06; kept separate because the change is in the auditor-facing step. A-LIGN markets a
    compliance benchmark report on technology use in audits (A-LIGN-2026) but the figures did not render in the text retrieved.

- id: security-governance-risk-16
  title: Inventory and review of AI agents embedded in vendor products as part of third-party risk (idea)
  archetype: security
  module: governance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    Vendors ship agents inside renewals and platform updates; the customer's identity and governance programmes may not see them.
  solution: >
    Idea: extend the third-party inventory and reviews to include vendor-embedded agents, their credentials and logs, and assign named human reviewers to AI-generated findings.
  outcomes:
    - lever: risk
      description: none published
      figure: "none published"
      measures: "no deployment or measurement found; practitioner discussion only"
      provenance: independent
      source_ref: CSA-AGENTS-2026
  prerequisites:
    - Inventory that includes vendor-embedded agents (CSA-AGENTS-2026)
  risks_and_guardrails:
    - Gartner's Q2 2026 emerging-risk report advises strengthening third-party risk controls so vendors do not introduce new risk (GARTNER-EMERGING-2026)
    - The CSA note says vendor terms often limit vendor liability (CSA-AGENTS-2026)
  human_checkpoints:
    - Named human reviewer for AI-generated findings that trigger action (CSA-AGENTS-2026)
  role_evolution: >
    The CSA note says contracts and risk registers should not assume vendors bear liability for agent behaviour (CSA-AGENTS-2026).
  evidence_grade: D
  sources:
    - { ref: CSA-AGENTS-2026, title: "The Agents You Didn't Choose: Embedded AI and Liability", publisher: Cloud Security Alliance (CSAI Foundation), type: standard-setter, url: "https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/10/CSA_research_note_embedded_third_party_agents_systemic_risk_20261012-csa-styled.pdf", date: 2026-10-12, access: full, locator: "Key Takeaways and Background" }
    - { ref: GARTNER-EMERGING-2026, title: "Gartner Survey Finds AI Discovery of Cyber Vulnerabilities is Top Emerging Risk in Second Quarter of 2026", publisher: Gartner, type: survey, url: "https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-08-25-use-this-gartner-survey-finds-ai-discovery-vulnerabilities-top-emerging-risk", date: 2026-08-25, access: full, locator: "Recommendations paragraph" }
  last_reviewed: 2026-10-17
  notes: >
    Label: idea. The CSA note states it was "generated with AI assistance and has not undergone official CSA review"; its claim that many enterprises run
    agents they never chose is, by its own statement, from practitioner reporting with no survey data.
```

## 3. Module notes

**Processes and key steps (with work types)**
- Customer assurance: receive questionnaire, find approved answers, draft, review, send; trust-centre document sharing (client-interaction, document-production).
- Third-party risk: intake and tiering, collect documents, assess against criteria, decide inherent and residual risk, remediation, continuous monitoring and reassessment (review-assurance, coordination-scheduling).
- Compliance and attestation: control framework design and mapping, evidence collection, control testing, audit coordination and response, remediation tracking (review-assurance, data-reporting).
- Risk management: register intake and triage, assessment and treatment decisions, quantification, appetite and metrics, leadership and board reporting (expert-judgment, data-reporting).
- Policy and standards: authoring, mapping to regulations and frameworks, exceptions, communication (document-production).
- AI governance by the security team: tool and agent inventory, acceptable-use policy, approval gates, incident readiness (expert-judgment).
- Security architecture is a lens in this module, mostly through approval gates in engineering workflows (Anthropic agent-security posting, Cloudflare "action gates"); no AI-specific architecture practice evidence was found for governance itself.

**Common pain points**
- Questionnaire volume with flat headcount: 60% of surveyed teams run reviews with 2 or fewer FTEs (CONVEYOR-BENCH-2026, 50+ B2B teams, vendor-run).
- Time on manual compliance: Perforce cited up to 60% of the team's time before consolidating (VANTA-PERFORCE-2026).
- Duplicate controls across frameworks: Samsara carried 820 controls across 10 frameworks (VANTA-SAMSARA-2026).
- Vendor review volume: about 130 reviews a month at Samsara (VANTA-SAMSARA-2026).
- Board communication: reports "structured around cybersecurity, not around the business" (TECHTARGET-BOARD-2026).
- Expectations without resources: 79% of CISOs say AI risk comes without proportional resources (PROOFPOINT-VOC-2026).

**Metrics and benchmarks (all with provenance)**
- 93% of inbound questionnaires automated in six months, GitHub (vendor-published) (VANTA-GITHUB-2026).
- 83% less time on customer security reviews; 95% accuracy on questionnaires; 40% fewer questionnaires, Carta (vendor-published) (CONVEYOR-CARTA-2026).
- Up to 50% faster vendor reviews, Samsara (vendor-published) (VANTA-SAMSARA-2026).
- 820 to 260 controls; SME interview hours 70 to 40 per audit cycle, Samsara (vendor-published) (VANTA-SAMSARA-2026).
- Control-to-evidence mapping precision: below 35% to 78% on an offline set (vendor-published) (VANTA-QUALITYEVAL-2026).
- Five LLMs underestimated cyber risk against 50 experts (independent) (ARXIV-2605.05424); NL access-control policy to Rego: 50.3% vs 15.3% correct (independent) (ARXIV-2609.24036).
- 56% involved in AI policy; 51% involved in AI solutions; 64% have run no AI incident exercise; 8% run them regularly; 13% do not use AI in security operations; 41% use AI to automate threat detection and response; 45% see LLM SecOps as a skill gap (ISACA, 1,800+ professionals) (ISACA-SOC-2026).
- ISC2 2025 (16,029 respondents): AI is the top skills need at 41%; GRC is a skills need at 27%; 28% have integrated AI tools, 19% are testing, 22% evaluating; 63% of active AI security tool users report a significant productivity boost (ISC2-WORKFORCE-2025).
- Gartner: AI-enabled discovery of cyber vulnerabilities top emerging risk Q2 2026; 316 senior executives and risk managers surveyed April-May 2026 (GARTNER-EMERGING-2026).
- Proofpoint (1,600 CISOs): 85% say board sees eye to eye (64% in 2025); 78% view GenAI as a security risk (60%); 85% say enabling safe AI is a top priority (PROOFPOINT-VOC-2026).
- Not found: override rates, parallel-run results, auditor reliance findings, regulator inspection outcomes, independent time-and-motion studies.

**Guardrails and regulatory points**
- EU AI Act applicable 2026-08-02; Annex III high-risk obligations 2027-12-02; Annex I products 2028-08-02; "AI Omnibus" in force 2026-07-27 (EC-AIACT-2026).
- US SEC cyber disclosure (Reg S-K Item 106 and Form 8-K Item 1.05): trade associations asked on 2026-04-10 for rescission or narrowing; no final SEC action found (SIFMA-SEC-2026). Disclosure duties differ by jurisdiction.
- CISA with ASD's ACSC published guidance on adopting agentic AI (2026-05-01) that aligns AI risk with existing frameworks; the retrieved copy uses "SI" in place of "AI" (CISA-AGENTIC-2026).
- Human review of any AI finding that triggers action; named reviewer and review path (CSA-AGENTS-2026).
- NIST CSF 2.0 "Govern" and NIST COSAiS overlays are the reference frames per the landscape file (not re-read here).

**Frontier signals (dated)**
- 2026-10-14: Optro (formerly AuditBoard) introduced "GRC Intelligence", Agentic Compliance, Autonomous Testing, Agentic TPRM and AURA Risk Assessment, and said its AI Governance product is strengthened by the FairNow acquisition (OPTRO-CRX-2026). Announced, not measured.
- 2026-06: Vanta described TPRM, Compliance and Risk "agents" and "24/7 GRC engineers" (VANTA-TPRMAGENT-2026, VANTA-COMPLIANCEAGENT-2026, VANTA-RISKAGENT-2026).
- 2026-07 to 2026-10: AI developers and AI-forward firms post GRC roles that build agent workflows (OpenAI 2026-08-06; Anthropic 2026-09/10; Plaid 2026-07 to 10) including FedRAMP 20x "machine-readable continuous compliance" (PLAID-JOB-GRC-2026).
- 2026-08-25: Gartner names AI-enabled vulnerability discovery the top emerging risk, with third-party risk controls among four recommendations (GARTNER-EMERGING-2026).
- 2026-10-12: Cloud Security Alliance note on vendor-embedded agents and liability (AI-assisted, unreviewed) (CSA-AGENTS-2026).
- 2026-09-22: ISACA finds AI-specific incident readiness lags AI use (ISACA-SOC-2026).

**Workforce and role effects**
- GRC "engineer" profiles replace pure program-manager profiles at several tech employers (see use case 13). Plaid expects analysts to handle more vendor reviews without adding headcount (PLAID-JOB-TPRM-2026).
- Analysts shift to verifying agent drafts and calibrating the tooling (ANTHROPIC-JOB-SUPPLIER-2026, ANTHROPIC-JOB-RISKANALYST-2026).
- 51% of ISACA respondents help develop, onboard or implement AI (up from 29% in 2024) (ISACA-SOC-2026). ISC2 respondents expect AI to create specialised roles: 73% (ISC2-WORKFORCE-2025).
- Hiring ratio: Axipro (via Vanta) counts about 7 AI builder postings per governance posting in eight EU countries (VANTA-AIGOVGAP-2026).
- No data on entry-level GRC hiring or on analysts' override rates.

**Objections and concerns practitioners raise**
- Tools "casting too wide a net": the mapping baseline had precision below 35% (VANTA-QUALITYEVAL-2026).
- LLMs may understate risk (ARXIV-2605.05424).
- Hype in "agentic" labels: Vanta says a raw LLM integration is "a coin flip" on compliance tasks, which is a vendor claim for its own product (VANTA-QUALITYEVAL-2026); weigh accordingly.
- Review burden shifting: the CSA note links unreviewed AI-generated findings to liability and a triage-cost asymmetry (CSA-AGENTS-2026).
- Role definition: fewer than 3 in 10 AI governance postings name the EU AI Act (VANTA-AIGOVGAP-2026).
- Over-restriction: Proofpoint stresses guardrails cannot be the whole strategy even though 78% block or limit GenAI (PROOFPOINT-VOC-2026).

**Interview probes for an advisor**
1. When your team or a vendor's tool drafts a questionnaire answer or vendor assessment, what share is accepted unchanged, and how do you know? Do you log overrides?
2. Which source documents is the AI allowed to answer from, who keeps them current, and what happens when they disagree with a customer's contract or an audit report?
3. Do your auditors accept AI-prepared evidence or workpapers? What did they ask for (sampling of AI outputs, access to prompts, logs)?
4. Who in the security team writes the policy on staff and agent use of AI, who approves agent actions on sensitive data, and have you rehearsed an AI-related incident?
5. If vendor reviews or customer requests doubled next quarter, what would you automate first, and what would you refuse to automate?

## 4. Routed to other modules

- **ai-security**: Samsara and Synthesia ISO 42001 certification and Vanta's own ISO 42001 audit lessons (governing a company's own AI products) (VANTA-SAMSARA-2026, VANTA-SYNTHESIA-2026, `4-lessons-learned-during-our-iso-42001-audit` page read: lastmod 2026-06-17); Kovrr "AI Risk Quantification" and shadow-AI discovery (KOVRR-2026); Optro AI Governance (FairNow) and OneTrust AI governance (customers GOL Airlines, Air Canada listed on the OneTrust customer page, not read in depth); EU AI Act obligations (EC-AIACT-2026).
- **incident-response**: ISACA AI-specific response exercises and playbooks (ISACA-SOC-2026); the post-incident policy gap proof-of-concept (ARXIV-2601.03287).
- **vulnerability-exposure**: Gartner's top emerging risk of AI-driven vulnerability discovery and its link to patch and remediation governance (GARTNER-EMERGING-2026).
- **human-risk / data-security-privacy**: Proofpoint finding that misuse or misconfiguration of AI tools caused 37% of material data loss cases (PROOFPOINT-VOC-2026); Splunk and Proofpoint data on employee GenAI use restrictions.
- **security-operations**: Optro/Vanta "service account detection" and access-review automation features are SOC-adjacent identity hygiene (VANTA-COMPLIANCEAGENT-2026).
- Coinbase compliance-agent postings (Group PM Compliance Agent Experience; Forward Deployed Engineer, Compliance) concern financial-crime/regulatory compliance, not security GRC; not used.

## 5. Sources

Ref | Title | Publisher | Type | URL | Date | Access

**Vendors and firms**
- VANTA-GITHUB-2026 | GitHub accelerates sales by automating 93% of security questionnaires with Vanta | Vanta | vendor | https://www.vanta.com/customers/github | 2026-03 (page last modified) | full
- VANTA-SYNTHESIA-2026 | How Synthesia became the first AI video company certified against ISO 42001 | Vanta | vendor | https://www.vanta.com/customers/synthesia | 2026-10 (page last modified) | full
- VANTA-SAMSARA-2026 | Samsara realized $150M+ in influenced revenue while scaling its GRC program with Vanta | Vanta | vendor | https://www.vanta.com/customers/samsara | 2026-05 (page last modified) | full
- VANTA-PERFORCE-2026 | Perforce unifies enterprise compliance, security, and risk with Vanta | Vanta | vendor | https://www.vanta.com/customers/perforce | 2026-03 (page last modified) | full
- VANTA-SNOWFLAKE-2026 | Snowflake's trust program speaks for itself | Vanta | vendor | https://www.vanta.com/customers/snowflake | 2026-03 (page last modified) | full
- VANTA-TPRMAGENT-2026 | Vanta Delivers: TPRM Agent | Vanta | vendor | https://www.vanta.com/resources/vanta-delivers-tprm-agent | 2026-06 | full
- VANTA-COMPLIANCEAGENT-2026 | Vanta Delivers: Compliance Agent | Vanta | vendor | https://www.vanta.com/resources/vanta-delivers-compliance-agent | 2026-06 | full
- VANTA-RISKAGENT-2026 | Vanta Delivers: Agent for Risk | Vanta | vendor | https://www.vanta.com/resources/vanta-delivers-agent-for-risk | 2026-06 | full
- VANTA-QUALITYEVAL-2026 | Vanta AI Quality Eval Maturity Model | Vanta | vendor | https://www.vanta.com/resources/vanta-ai-quality-evaluation-maturity-model | 2026-07 | full
- VANTA-AIGOVGAP-2026 | The AI governance confidence gap | Vanta | vendor | https://www.vanta.com/resources/ai-governance-confidence-gap | 2026-07 | full
- WHISTIC-CALASTONE-2025 | How Calastone Transformed TPRM with Whistic | Whistic | vendor | https://www.whistic.com/resources/case-studies/calastone-customer-story | 2025-12 (page last modified) | full
- WHISTIC-DOD-2025 | How Doctor On Demand manages its entire vendor risk management process through Whistic | Whistic | vendor | https://www.whistic.com/resources/case-studies/how-doctor-on-demand-manages-its-entire-vendor-risk-management-process-through-whistic | 2025-12 (page last modified) | full
- HYPERPROOF-FINCO-2025 | How Hyperproof Helped a Global Financial Enterprise Revolutionize Third-Party Risk Management | Hyperproof | vendor | https://hyperproof.io/case-studies/how-hyperproof-helped-a-global-financial-enterprise-revolutionize-third-party-risk-management/ | 2025-11-08 | full
- CONVEYOR-CARTA-2026 | Carta cuts security review time by 83% with Conveyor | Conveyor | vendor | https://www.conveyor.com/customers/carta-2 | 2026-06 (page last modified) | full
- CONVEYOR-SUMO-2026 | Sumo Logic automates 100% of security requests with Conveyor Trust Center | Conveyor | vendor | https://www.conveyor.com/customers/sumo-logic | 2026-07 (page last modified) | full
- CONVEYOR-BENCH-2026 | 2026 Customer Trust Benchmark Report (landing page) | Conveyor | survey | https://www.conveyor.com/landing-page/2026-customer-trust-benchmark | 2026-09 (page last modified) | full
- DRATA-TPRMAI-2026 | Accelerate Third-Party Reviews with AI (product page) | Drata | vendor | https://drata.com/product/vendor-risk-management/ai-agent | 2026-10-17 (retrieval date; undated page) | full
- SAFE-TPRM-2026 | SAFE TPRM AI Co-Worker (product page) | Safe Security | vendor | https://safe.security/third-party-risk-management/ | 2026-10-17 (retrieval date; undated page) | full
- SAFE-TMOBILE-2026 | T-Mobile: Cutting the Cord on Subjective Risk Scores | Safe Security | vendor | https://safe.security/resources/customer-stories/t-mobile-cutting-the-cord-on-subjective-risk-scores/ | 2026-10-17 (retrieval date; undated page) | full
- OPTRO-CRX-2026 | GRC Intelligence takes the stage at CRX '26 | Optro (formerly AuditBoard) | vendor | https://optro.ai/blog/grc-intelligence-takes-the-stage-crx-26 | 2026-10-14 | full
- OPTRO-AUTOTEST-2026 | Autonomous testing software (product page) | Optro | vendor | https://auditboard.com/product/autonomous-testing | 2026-10-17 (retrieval date; undated page) | full
- KOVRR-2026 | Kovrr: AI Security and Governance for the Agentic Era (home page) | Kovrr | vendor | https://www.kovrr.com/ | 2026-10-17 (retrieval date; undated page) | full
- SPLUNK-CISOPOLICY-2024 | A CISO's Guide to Generative AI Policy | Splunk | vendor | https://www.splunk.com/en_us/blog/ciso-circle/ciso-gen-ai-policy.html | 2024-07-31 | full
- A-LIGN-2026 | 2026 Compliance Benchmark Report (landing page; figures did not render) | A-LIGN | firm | https://www.a-lign.com/resources/2026-compliance-benchmark-report | 2026 (page undated) | full
- LOOPIO-CASES-2026 | Loopio customers index (Allied Universal, HedgeServ, Research Affiliates headlines; not used for outcomes) | Loopio | vendor | https://loopio.com/customers/ | 2026-10-17 (retrieval date) | full

**Job postings (live postings read 2026-10-17 via Greenhouse and Ashby public job-board APIs)**
- ANTHROPIC-JOB-SUPPLIER-2026 | Supplier Security & Assurance, Security GRC | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5427893008 | 2026-09-17 | full
- ANTHROPIC-JOB-CONTROLS-2026 | Controls Specialist, Security GRC | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5436826008 | 2026-09-29 | full
- ANTHROPIC-JOB-GRCPLATFORM-2026 | Staff+ Software Engineer, GRC Platform | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5250091008 | 2026-06-08 | full
- ANTHROPIC-JOB-RISKENG-2026 | Staff Security Engineer, Risk Engineering | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5250052008 | 2026-06-08 | full
- ANTHROPIC-JOB-RISKANALYST-2026 | Security Risk Analyst, Risk Engineering | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5397704008 | 2026-10-05 | full
- ANTHROPIC-JOB-AGENTSEC-2026 | Security Risk & Compliance, Agent Security | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5443871008 | 2026-10-05 | full
- ANTHROPIC-JOB-SOX-2026 | Lead, Security Controls Assurance - SOX | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5415864008 | 2026-09-08 | full
- OPENAI-JOB-AUDIT-2026 | GRC Program Manager, Audit & Controls | OpenAI | job-posting | https://jobs.ashbyhq.com/openai/aeac2b78-1f4a-4dfe-b88f-25fc8adf5bb3 | 2026-08-06 | full
- OPENAI-JOB-VENDOR-2026 | Vendor Security Technical Program Manager | OpenAI | job-posting | https://jobs.ashbyhq.com/openai/3ae71c21-60dd-42b2-a913-58df05988976 | 2026-10-02 | full
- OPENAI-JOB-ERM-2026 | Head of Enterprise Risk Management | OpenAI | job-posting | https://jobs.ashbyhq.com/openai/db40bc4f-c7fb-47d5-a7cc-918fb8b1f815 | 2026-10-14 | full
- PLAID-JOB-GRC-2026 | Security Engineer, GRC | Plaid | job-posting | https://jobs.ashbyhq.com/plaid/587e83dd-1d1b-4f31-812a-74fc67d67fbe | 2026-07-16 | full
- PLAID-JOB-TPRM-2026 | Security Analyst, Third-Party Ecosystem Risk Management | Plaid | job-posting | https://jobs.ashbyhq.com/plaid/94752cfc-4a62-48c9-bcc0-e5f7f1905be6 | 2026-08-12 | full
- PLAID-JOB-RISK-2026 | Senior Security Analyst, Security Risk Management | Plaid | job-posting | https://jobs.ashbyhq.com/plaid/4c4af954-2c70-4a3c-acc2-97c58211f920 | 2026-10-12 | full
- CLOUDFLARE-JOB-GRC-2026 | GRC Engineer | Cloudflare | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8045914?gh_jid=8045914 | 2026-07-08 | full
- GITLAB-JOB-GOV-2026 | Staff Security Governance Engineer, Policies & Standards | GitLab | job-posting | https://job-boards.greenhouse.io/gitlab/jobs/8846277002 | 2026-09-30 | full
- GITLAB-JOB-RISK-2026 | Senior Security Risk Engineer (AI risk management to support ISO 42001) | GitLab | job-posting | https://job-boards.greenhouse.io/gitlab/jobs/8846304002 | 2026-09-29 | full
- OKTA-JOB-GRC-2026 | Senior Director, GRC | Okta | job-posting | https://www.okta.com/company/careers/opportunity/8130437?gh_jid=8130437 | 2026-08-17 | full
- FIGMA-JOB-COMPLIANCEENG-2026 | Compliance Engineer | Figma | job-posting | https://boards.greenhouse.io/figma/jobs/6223155004?gh_jid=6223155004 | 2026-10-16 | full
- FIGMA-JOB-GRCDIR-2026 | Director, Governance Risk & Compliance (AI governance, risk and compliance initiatives) | Figma | job-posting | https://boards.greenhouse.io/figma/jobs/6211088004?gh_jid=6211088004 | 2026-10-14 | full
- COINBASE-JOB-GRC-2026 | Manager, GRC (one line on responsible generative AI use; not used) | Coinbase | job-posting | https://www.coinbase.com/careers/positions/8167666?gh_jid=8167666 | 2026-08-31 | full

**Academic**
- ARXIV-2605.05424 | Evaluating the Reliability of Multiple Large Language Models in Risk Assessment: A CIS Controls Based Approach | arXiv | academic | https://arxiv.org/abs/2605.05424 | 2026-05-06 | full
- ARXIV-2609.24036 | Structured Decomposition for Reliable LLM-Generated Access Control Policies | arXiv | academic | https://arxiv.org/abs/2609.24036 | 2026-09-21 | full
- ARXIV-2412.13988 | RAG for Effective Supply Chain Security Questionnaire Automation | arXiv | academic | https://arxiv.org/abs/2412.13988 | 2024-12-18 | full
- ARXIV-2601.03287 | Automated Post-Incident Policy Gap Analysis via Threat-Informed Evidence Mapping using LLMs | arXiv | academic | https://arxiv.org/abs/2601.03287 | 2026-01-04 | full

**Surveys, professional bodies, standard-setters, regulators, press**
- ISACA-SOC-2026 | Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises (State of Cybersecurity 2026) | ISACA | professional-body | https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises | 2026-09-22 | full
- ISC2-WORKFORCE-2025 | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full
- PROOFPOINT-VOC-2026 | The risk has moved: what Proofpoint's 2026 Voice of the CISO reveals | Proofpoint | survey | https://www.proofpoint.com/au/blog/corporate-news/risk-has-moved-what-proofpoints-2026-voice-ciso-reveals | 2026-09-09 | full
- GARTNER-EMERGING-2026 | Gartner Survey Finds AI Discovery of Cyber Vulnerabilities is Top Emerging Risk in Second Quarter of 2026 | Gartner | survey | https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-08-25-use-this-gartner-survey-finds-ai-discovery-vulnerabilities-top-emerging-risk | 2026-08-25 | full (via Gartner mirror host; main site returned a bot check)
- TECHTARGET-BOARD-2026 | Lost in translation: Cybersecurity board reporting for CISOs | TechTarget | press | https://www.techtarget.com/cybersecurity/news/366643884/Lost-in-translation-Cybersecurity-board-reporting-for-CISOs | 2026-06-03 | full
- FAIR-BOARD-2026 | The Board Understands Risk. Does the Business? | FAIR Institute | professional-body | https://www.fairinstitute.org/blog/the-board-understands-risk.-does-the-business | 2026-10-17 (retrieval date; undated text) | full
- CSA-AGENTS-2026 | The Agents You Didn't Choose: Embedded AI and Liability | Cloud Security Alliance | standard-setter | https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/10/CSA_research_note_embedded_third_party_agents_systemic_risk_20261012-csa-styled.pdf | 2026-10-12 | full
- CISA-AGENTIC-2026 | Careful Adoption of Agentic AI Services | CISA with ASD's ACSC | regulator | https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services | 2026-05-01 | full (landing page only, via text mirror)
- EC-AIACT-2026 | AI Act: regulatory framework for AI (status page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-17 (status page checked) | full
- SIFMA-SEC-2026 | Reforming Regulation S-K cybersecurity disclosures (joint trades letter) | SIFMA and trade associations | professional-body | https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades | 2026-04-10 | full

Source count by type (59 distinct refs, all read in full): vendor 23, job-posting 20, academic 4, professional-body 4, survey 3, regulator 2, firm 1, press 1, standard-setter 1. Ten of the vendor refs are Vanta pages.

## 6. Gaps

- **No independent outcome data.** No published override rates, parallel-run results, auditor-reliance statements, regulator inspection findings or independent time studies for AI in security GRC. The only independent quality measures are two academic studies, both small and adjacent (risk scoring vs 50 experts; access-control policy translation).
- **Case-study dates.** Vendor customer stories show no publication dates; sitemap last-modified times were used. Drata and Safe pages are undated.
- **Blocked or unreadable.** Drata customers and sitemap (403), SafeBase (403), Gartner main site (bot check; the mirror host worked for one release), CISA guide body (only landing page read), SANS/GIAC 2026 Workforce Report (404), ISACA full report (JS page; press release read instead), Microsoft Security/Purview and Big Four pages (not reached; search found no GRC-specific Big Four launch), A-LIGN benchmark figures (did not render), Optro customer outcomes (none published).
- **Not found:** named security-team policy texts for AI use (only surveys and role postings), AI-assisted board-pack deployments with results, LLM-based FAIR analysis at a named company, Big Four security-GRC AI offerings, auditor use of AI in SOC 2 testing (a search found only directory-site claims, not used), risk-quantification vendor customer results that credit AI.
- **Search yield.** Nine web searches produced little beyond leads (surveys, Gartner mirror, ISACA press release); most evidence came from direct fetches.
- **Postings are intent.** All job-posting evidence is the employer's own description and may change. AI developers (Anthropic, OpenAI) may describe practice they are still building.
- **Not covered:** non-US regulators beyond the EU AI Act, ISO/IEC 42001 text, NIST Cyber AI Profile, sector regulators (banking, health), cyber insurance and underwriting, small and mid-size security teams outside vendor case studies.
