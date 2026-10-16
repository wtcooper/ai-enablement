# Assurance / planning-risk-assessment / practice

- **Archetype:** assurance
- **Module:** planning-risk-assessment: understanding the entity and its environment (including its IT and AI use), risk assessment procedures and analytics for risk identification, fraud risk assessment and brainstorming, materiality, scoping (including group audits), audit strategy and planning, budgeting and staffing the engagement.
- **Angle:** practice (what audit firms and internal audit functions actually do)
- **Prepared:** 2026-10-16
- **Method note.** Pages were opened with `curl` through the session proxy (`pdftotext` for PDFs; two PDF pages were rendered and read as images). The shared web-search quota ran out partway through, so four planned searches did not run (internal-audit vendor customers, Big Four job postings, Uniper and Microsoft internal audit follow-ups). Those leads are listed in section 6. Figures from vendor and firm press material are labelled as such in each entry. A MindBridge technical whitepaper on assertion-level scoring was reachable by URL but is marked "Confidential for MindBridge Customers Only", so it was not used.

---

## 1. Summary

- **Planning is where AI is being added in earnest, but mostly as first drafts for a person to review, and almost all outcome evidence is self-reported or vendor-published.** No independent measurement of any tool's accuracy or effect on quality in live planning work was found, and no inspection finding specific to AI in risk assessment was found. Of 24 candidate use cases, none reaches grade A.
- **Named, in-use planning changes (grade B):**
  - Prior-year planning documents auto-populated (PwC, first year of use in the Oct 2025 briefing) [PWC-AT-2025].
  - Process narratives and flowcharts generated from client walkthrough meetings (KPMG, Copilot, deployed from Apr 2024) [KPMG-CLARA-2025].
  - Document review to flag risks, for example in meeting minutes (KPMG Clara) [KPMG-CLARA-2024].
  - Journal-entry visualisation for risk assessment (RSM) [CPAPA-ASKLUCA-2026].
  - Media-scanning agents and draft staff memos (Deloitte, launched Jun 2026) [BBL-DELOITTE-2026].
  - Standardised ERP data ingestion (Grant Thornton gtap) [GT-GTAP-2026].
  - A staffing and budget-planning tool (RSM Luca Resourcing) [CAQ-RSM-2026].
  - Engagement-specific risk suggestion drafts (Caseware Risk Suggestion Agent, launched worldwide 6 Oct 2026, with a named customer quote) [CASEWARE-RSA-2026; ITBRIEF-CASEWARE-2026].
- **Newest and least proven (grade C or D):**
  - Assertion-level risk scoring tied to materiality (MindBridge, 22 Sep 2026) [MINDBRIDGE-ARA-2026].
  - Agent-recommended starting risk scores for internal audit (Optro, 14 Oct 2026) [OPTRO-CRX-2026].
  - Risk-to-control mapping at scoping (Fieldguide, webinar 20 Oct 2026) [FIELDGUIDE-DEMO-2026].
  - PwC's risk-assessment tool, described in Oct 2025 as coming "soon". No launch was found in the Oct 2026 follow-up [PWC-AT-2025; CFODIVE-PWC-2026].
- **The one independent test of general-purpose chatbots on planning work was unfavourable.**
  - ICAEW tried three models on a fictional retailer. None performed ISA 315 risk assessment as a human would, none separated financial-statement-level from assertion-level risks, and materiality figures varied by model [ICAEW-PIERPOINT-2025]. It was a single test on fictional data.
  - The FRC's worked example for board-minutes summarisation reaches a different design: a bespoke tool, a library of fixed prompts, certification, and a reviewer who still reads the minutes [FRC-GENAI-2026].
- **Regulators track prevalence, not quality.**
  - IFIAR members said they frequently saw automated tools in risk assessment in 55% of responses in 2024 (49% in 2023) [IFIAR-TTF-2025]. The 2026 report's chart shows a similar level for 2025 [IFIAR-TTF-2026].
  - The six large networks reported about 30% year-over-year growth in AI-enabled tools in 2025, on figures IFIAR says are inconsistently reported [IFIAR-TTF-2026].
  - Smaller US firms lag: 22% of surveyed firms report an automated solution for risk assessment [CPACOM-ATR-2025].
- **Time savings are modest so far.**
  - PwC's lead said busy-season time savings are "not that drastic yet", though AI is good at pointing to where risks may lie [CFODIVE-PWC-2026].
  - Vendor figures are larger, and are labelled as vendor-published below.
- **Workflow and role changes reported:**
  - Planning review moves toward checking an AI draft against the file [CASEWARE-VERITY-2026].
  - Entry-level hiring is shifting toward dual CPA and data skills [PWC-AT-2025].
  - Staffing and budgeting are being pulled into tools [CAQ-RSM-2026].
  - Vendors are hiring audit practitioners as product and implementation staff [FIELDGUIDE-JOB-2026; CLARK-JOB-2026].
- **Thin or absent evidence:** group-audit scoping, materiality, and fraud brainstorming in external audit have no firm, regulator or standard-setter evidence of AI use in practice. The only practice evidence for fraud brainstorming is a local-government internal auditor's conference slides [VLGAA-NUCCIO-2026].

---

## 2. Use cases

```yaml
- id: assurance-planning-risk-assessment-01
  title: Summarise board minutes and other entity documents to focus risk identification
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Auditors read an entity's board minutes in full to understand it and spot risk indicators. This is slow, and relevant items can be missed."
  solution: "A tool built around a language model segments and indexes the minutes with stable identifiers, summarises each meeting, reviews all meetings together for period-wide themes, and synthesises a cited summary. Auditors use prewritten prompts from a library and record on the file how the output informed further work. KPMG describes Clara AI assistants that review documents, for example meeting minutes, to flag possible accounting and financial risks."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none"
      measures: "No usage, accuracy or time figures are given. The FRC example is a hypothetical firm. KPMG's statement describes a capability without figures."
      provenance: self-reported
      source_ref: KPMG-CLARA-2024
  prerequisites:
    - "Tool certified before use, with testing across entities of different sizes and sectors, and prompts refined after early deficiencies (FRC example) [FRC-GENAI-2026]"
    - "A central library of prewritten prompts maintained by a specialist team, so auditors do not write their own [FRC-GENAI-2026]"
    - "Training on how to review the output, not only how to use the tool [FRC-GENAI-2026]"
    - "Access to the engagement documents inside the firm platform [KPMG-CLARA-2024]"
  risks_and_guardrails:
    - "Output may omit, distort or hallucinate; the FRC example mitigates this with source citation, a staged summarisation design and certification [FRC-GENAI-2026]"
    - "Auditors may treat the summary as complete and skip other risk assessment procedures; training must explain the scope of the output [FRC-GENAI-2026]"
    - "The FRC example does not require perfect accuracy for certification, because a human reads the minutes [FRC-GENAI-2026]"
  human_checkpoints:
    - "The auditor reads the minutes to corroborate completeness and accuracy, with a closer read where output conflicts with prior understanding or bears on risk [FRC-GENAI-2026]"
    - "The reviewer should be a team member who understands the entity [FRC-GENAI-2026]"
  role_evolution: "In the FRC example, staff training centres on reviewing outputs and resisting automation bias, because the auditor does not prompt the tool [FRC-GENAI-2026]."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "Illustrative example 1, pp. 43-48; misunderstanding-of-methodology risk, p. 18" }
    - { ref: KPMG-CLARA-2024, title: "KPMG announces AI integration into global smart audit platform, KPMG Clara", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2024/07/kpmg-announces-ai-integration-into-global-smart-audit-platform-kpmg-clara.html", date: 2024-07-29, access: full, locator: "bullet 'Refine risk assessments'" }
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG US (Newsfile Corp.), type: firm, url: "https://www.newsfilecorp.com/release/249535/KPMG-Advances-AI-Integration-in-KPMG-Clara-Smart-Audit-Platform", date: 2025-04-23, access: full, locator: "recap paragraph beginning 'In July 2024'" }
  last_reviewed: 2026-10-16
  notes: "Grade B rests on KPMG's own statements that the capability is embedded for its auditors (announced for 90,000 in Jul 2024 and restated in the present tense in Apr 2025). The firm gives no data on use of this feature. The FRC example is a regulator illustration, not a deployment. Date check: the Newsfile copy of the KPMG release is dated 23 Apr 2025; the landscape file gives 22 Apr."

- id: assurance-planning-risk-assessment-02
  title: Draft engagement-specific risk suggestions from trial balance, prior-year file and board minutes
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Risk assessment starts from a blank page or from last year's risks, and is time-consuming (a customer's words)."
  solution: "Caseware's Verity-powered Risk Suggestion Agent uses current and prior-year financial information, existing risks, controls and selected supporting documents to suggest engagement-specific risks with rationale. Auditors review, edit or reject each suggestion, and nothing enters the engagement file without a deliberate decision."
  outcomes:
    - lever: quality
      description: "In a CwX 2026 preview demonstration the agent surfaced five risks for review, one being a gap between the trial balance and net profit reported in board minutes."
      figure: "5 risks; one $118,000 discrepancy"
      measures: "Risks surfaced in one vendor demonstration on a sample engagement (trial balance, board minutes, prior-year file). Not a live-engagement result."
      provenance: vendor-published
      source_ref: CASEWARE-VERITY-2026
    - lever: speed
      description: "A customer partner says it gives teams a strong starting point and saves time for testing and follow-up. No figure given."
      figure: "none published"
      measures: "Testimonial from a partner at GRF CPAs & Advisors, supplied by Caseware; no measurement"
      provenance: vendor-published
      source_ref: ITBRIEF-CASEWARE-2026
  prerequisites:
    - "Engagement data held in the firm's Caseware environment (Verity runs inside it, and Caseware says engagement data is not used to train models) [CASEWARE-RSA-2026]"
    - "Prior-year financials, logged risks and controls, plus qualitative documents such as board minutes [CASEWARE-LAUNCH-2026]"
    - "A Caseware Verity licence; the agent is included at no extra charge [CASEWARE-RSA-2026]"
  risks_and_guardrails:
    - "Suggestions are drafts for independent review and cannot be incorporated without an explicit practitioner decision [CASEWARE-RSA-2026]"
    - "Risk of anchoring on the suggested list and under-weighting risks the agent did not raise; the FRC names this kind of misuse (output taken as complete) in its guidance [FRC-GENAI-2026]"
  human_checkpoints:
    - "Auditor accepts, edits or rejects every suggested risk [ITBRIEF-CASEWARE-2026]"
  role_evolution: "Caseware says the goal is to give auditors more time for the testing and follow-up that the identified risks require (customer quote) [ITBRIEF-CASEWARE-2026]."
  evidence_grade: B
  sources:
    - { ref: CASEWARE-RSA-2026, title: "Caseware Verity-powered Risk Suggestion Agent launches to help auditors identify engagement-specific risks", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-verity-powered-risk-suggestion-agent-launches-to-help-auditors-identify-engagement-specific-risks", date: 2026-10-06, access: full, locator: "paragraphs 1-2 and 'Rather than beginning each engagement' section" }
    - { ref: ITBRIEF-CASEWARE-2026, title: "Caseware launches AI agents for audit risk and disclosure", publisher: IT Brief UK, type: press, url: "https://itbrief.co.uk/story/caseware-launches-ai-agents-for-audit-risk-disclosure", date: 2026-10-13, access: full, locator: "paragraphs 1-4 and GRF CPAs quote" }
    - { ref: CASEWARE-LAUNCH-2026, title: "Caseware launches Caseware Verity to bring workflow-native AI agents directly into assurance engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements", date: 2026-05-20, access: full, locator: "paragraph on Risk Suggestion Agent (described as advancing through alpha)" }
    - { ref: CASEWARE-VERITY-2026, title: "CwX 2026: How agentic AI is transforming audit and assurance", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance", date: 2026-06-17, access: full, locator: "paragraph on the Risk Suggestion Agent preview" }
  last_reviewed: 2026-10-16
  notes: "Grade B rests on a launch (6 Oct 2026) plus one named customer statement, with no measured outcome. The May 2026 release called the agent 'advancing through alpha'; the Oct 2026 release says launched worldwide. The demo figure is a demonstration, not a live result, and is kept out of any claim of effect."

- id: assurance-planning-risk-assessment-03
  title: Planning review with an in-file assistant that checks the engagement for gaps
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Gaps found in planning review, such as a variance with no risk attached, otherwise surface during fieldwork."
  solution: "In a CwX 2026 demonstration, a reviewer asks Verity whether the team missed anything in planning. Verity loads the trial balance, retrieves materiality, reviews logged risks and flags a variance against the board minutes that has no associated risk. Caseware describes it as a second set of eyes; the reviewer decides."
  outcomes:
    - lever: speed
      description: "Caseware reports that early beta deployments cut indicative manual workflows from 15-20 minutes to under two minutes."
      figure: "15-20 min to under 2 min (up to 85% per interaction)"
      measures: "Time for indicative manual workflows versus the same interaction with Verity in beta deployments; not specific to planning review"
      provenance: vendor-published
      source_ref: CASEWARE-LAUNCH-2026
    - lever: quality
      description: "Caseware reports 94% accuracy on golden dataset items captured from beta traces."
      figure: "94%"
      measures: "Accuracy on golden dataset items captured from beta traces, in the vendor's words; dataset size and scoring method not stated; not specific to planning"
      provenance: vendor-published
      source_ref: CASEWARE-LAUNCH-2026
  prerequisites:
    - "Engagement file (trial balance, materiality, logged risks, board minutes) held in the same platform as the assistant [CASEWARE-AIDA-2026]"
    - "Firm methodology configured so the assistant follows it [CASEWARE-VERITY-2026]"
  risks_and_guardrails:
    - "Suggestions are citation-backed and traceable, and nothing is written into the engagement without review, per Caseware [CASEWARE-AIDA-2026]"
    - "Accuracy and time figures are vendor-reported and not planning-specific [CASEWARE-LAUNCH-2026]"
  human_checkpoints:
    - "The reviewer decides on every review point [CASEWARE-VERITY-2026]"
  role_evolution: "Caseware says junior staff can reach standards and methodology in context and seniors can focus on higher-value review [CASEWARE-AIDA-2026]. Three partners from Withum, Citrin Cooperman and EisnerAmper piloted Verity on live engagements in the 2025 busy season [CASEWARE-VERITY-2026]."
  evidence_grade: C
  sources:
    - { ref: CASEWARE-VERITY-2026, title: "CwX 2026: How agentic AI is transforming audit and assurance", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance", date: 2026-06-17, access: full, locator: "planning review scenario paragraph; beta partner fireside chat" }
    - { ref: CASEWARE-AIDA-2026, title: "From AiDA to agentic: How Caseware's AI has evolved", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved", date: 2026-07-28, access: full, locator: "sections 'Meet Caseware Verity' and 'Why it matters for your team'" }
    - { ref: CASEWARE-LAUNCH-2026, title: "Caseware launches Caseware Verity to bring workflow-native AI agents directly into assurance engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements", date: 2026-05-20, access: full, locator: "paragraph beginning 'Early beta deployments'" }
  last_reviewed: 2026-10-16
  notes: "The planning review scenario is a conference demonstration. The named partners piloted Verity generally, not this scenario specifically. Caseware also states a goal of automating up to 50% of the engagement workflow across prepare, plan, validate and report (vendor goal, not a result) [CASEWARE-LAUNCH-2026]."

- id: assurance-planning-risk-assessment-04
  title: Auto-populate the planning document from prior-year information
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Planning documents are rebuilt each year from prior-year files, and auditors may not notice what has changed in the business."
  solution: "PwC's Simplified Audit for Private Business ingests prior-year information and auto-populates a planning document that serves as a base for considering compliance with AICPA standards. It is built for private-company audits under AICPA standards. PwC says it saves time and helps auditors ask better questions by showing what changed since the last audit."
  outcomes:
    - lever: speed
      description: "PwC says the tool saves time. No figure given."
      figure: "none published"
      measures: "Qualitative statement by PwC's US assurance transformation leader at an Oct 2025 briefing; no measurement"
      provenance: self-reported
      source_ref: PWC-AT-2025
    - lever: quality
      description: "PwC says it enables better questions because auditors see what changed since the last audit."
      figure: "none published"
      measures: "Qualitative statement; no measurement"
      provenance: self-reported
      source_ref: PWC-AT-2025
  prerequisites:
    - "Prior-year audit information available in a structured form [PWC-AT-2025]"
  risks_and_guardrails:
    - "Risk of carrying forward last year's view; the AICPA/CPA.com survey notes some firms struggle to move from reliance on prior-year workpapers to risk-driven work [CPACOM-ATR-2025]"
  human_checkpoints:
    - "The document is a foundation for the auditor to consider; the planning judgments stay with the team [PWC-AT-2025]"
  role_evolution: "PwC's lead says the firm is hiring engineers it would not previously have hired into assurance and hopes for dual-track CPA and data-science entrants [PWC-AT-2025]."
  evidence_grade: B
  sources:
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraphs 3-4 (Simplified Audit for Private Business)" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: CPA.com (AICPA), type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "section 'A risk-driven approach is not yet fully leveraged'" }
  last_reviewed: 2026-10-16
  notes: "The source says this was the first year PwC auditors used the tool in planning. Tool was for private company audits under AICPA standards, not public-company audits."

- id: assurance-planning-risk-assessment-05
  title: Draft walkthrough documentation from client meetings and prior-year walkthroughs
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Walkthroughs are tedious, and in large organisations following a transaction from start to recording is hard. Teams ask why they repeat them yearly (PwC's AI assurance leader)."
  solution: "KPMG says engagement teams use Copilot and Audit Chat to generate process narratives and flowcharts from meetings with clients. PwC describes an Advanced Walkthrough Assistant that takes prior-year walkthroughs and current documentation, builds a tailored work plan, flags what is missing or changed, captures documentation of controls and risks, and generates documentation for review."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none"
      measures: "KPMG gives no time or quality figure for this step. PwC gives none for the Advanced Walkthrough Assistant."
      provenance: self-reported
      source_ref: KPMG-CLARA-2025
  prerequisites:
    - "Enterprise Copilot deployed to audit staff (KPMG began deploying it to audit partners and professionals in Apr 2024) [KPMG-CLARA-2025]"
    - "Prior-year walkthrough files and current-year documentation in a form the tool can read [PWC-AT-2025]"
  risks_and_guardrails:
    - "Generated narratives need checking against what the client said; the FRC names automation bias and fluent but wrong output as risks [FRC-GENAI-2026]"
  human_checkpoints:
    - "Documentation is produced 'for review' by the team [PWC-AT-2025]"
  role_evolution: "PwC's CFO Dive interview says the assistant documents business processes to help auditors prepare for discussions [CFODIVE-PWC-2026]."
  evidence_grade: B
  sources:
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG US (Newsfile Corp.), type: firm, url: "https://www.newsfilecorp.com/release/249535/KPMG-Advances-AI-Integration-in-KPMG-Clara-Smart-Audit-Platform", date: 2025-04-23, access: full, locator: "recap paragraph beginning 'In April 2024'" }
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraph on Advanced Walkthrough Assistant" }
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "paragraph on 2026 year-end audit tools" }
  last_reviewed: 2026-10-16
  notes: "Grade B rests on KPMG's statement that teams 'are already' using Copilot this way. For PwC's tool the sources say it exists (Oct 2025) and will be used for 2026 year-end audits (Oct 2026), so that half is announced. Walkthroughs also sit in the controls-testing module; kept here because they are part of understanding the entity's processes."

- id: assurance-planning-risk-assessment-06
  title: Full-population journal-entry analytics to inform risk assessment and focus
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Sample-based, rule-based tests give an incomplete view of where risk sits in a ledger, so risk assessment leans on prior-year judgment."
  solution: "Firms run analytics over whole ledgers during risk assessment. RSM says its auditors review intelligent visualisations of journal entries for risk-assessment insight and anomaly detection. KPMG says Clara includes Transaction Scoring (from a 2023 alliance with MindBridge) over 100% of populations, and Databricks analysis across thousands of audits. Grant Thornton's gtap is built to enable full-population analysis."
  outcomes:
    - lever: quality
      description: "Adoption signal, not a quality measure: IFIAR members frequently saw automated tools in risk assessment in 2024 (49% in 2023)."
      figure: "55%"
      measures: "Share of 47 IFIAR members answering the 2024 annual survey who said they frequently observed automated tools and techniques in risk assessment in audit files (13% never, 32% infrequently)"
      provenance: independent
      source_ref: IFIAR-TTF-2025
    - lever: quality
      description: "Adoption signal among smaller US firms: few have automated risk assessment."
      figure: "22%"
      measures: "Share of surveyed firms reporting an automated solution for risk assessment; the report's analysis covers 54 firms with complete data"
      provenance: independent
      source_ref: CPACOM-ATR-2025
    - lever: quality
      description: "Among firms using automated risk assessment, every respondent reported a positive impact, many significant or transformational (number of respondents not stated)."
      figure: "every respondent"
      measures: "Respondents using technology for automated risk assessment who reported a positive impact; the report says fewer than one-quarter of firms answered this question"
      provenance: independent
      source_ref: CPACOM-ATR-2025
  prerequisites:
    - "Client ledger data in a usable form; surveyed US firms name poor client data (60%) and no access to client systems (53%) as top blockers [CPACOM-ATR-2025]"
    - "Standardised ingestion from the client's ERP [GT-GTAP-2026]"
  risks_and_guardrails:
    - "IFIAR members' most common technology findings are misreading tool results and thin testing of outliers; 31% of members reported findings that a tool was not used as intended in 2024 [IFIAR-TTF-2025]"
    - "IFIAR warns of over-reliance on outputs without enough challenge [IFIAR-TTF-2026]"
  human_checkpoints:
    - "Auditors interpret results and test outliers; firms are expected to monitor tool use and quality impact [IFIAR-TTF-2025]"
  role_evolution: "In the AICPA/CPA.com survey, firms furthest along in transformation spend the highest share of time in planning and less in fieldwork [CPACOM-ATR-2025]."
  evidence_grade: B
  sources:
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution", publisher: IFIAR Technology Task Force (FSA Japan copy), type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "section 'Insights from IFIAR Members', table and inspection findings, p. 5" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality", publisher: IFIAR Technology Task Force (FSA Japan copy), type: regulator, url: "https://www.fsa.go.jp/ifiar/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "Executive Summary; trend chart, p. 10" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: CPA.com (AICPA), type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "'For which of the following does the firm have an automated solution?' chart; section 'Risk-driven approach and technology'" }
    - { ref: CPAPA-ASKLUCA-2026, title: "RSM US rolls out 'Ask Luca' GenAI tool for firm's auditors", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/01/09/rsm-us-rolls-out-ask-luca-genai-tool-for-firms-auditors/176104/", date: 2026-01-09, access: full, locator: "bullet 'Enhanced risk assessment'" }
    - { ref: KPMG-CLARA-2024, title: "KPMG announces AI integration into global smart audit platform, KPMG Clara", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2024/07/kpmg-announces-ai-integration-into-global-smart-audit-platform-kpmg-clara.html", date: 2024-07-29, access: full, locator: "recap bullet on the 2023 MindBridge alliance (Transaction Scoring)" }
  last_reviewed: 2026-10-16
  notes: "IFIAR figures count how many regulators say they frequently see tools, not the share of audits using them, and IFIAR calls its observations directional. The 2026 report's chart has no data labels; the 2025 bar for risk assessment reads visually at roughly the low 50s. The ATR's 22% appears in the chart and also in the sentence on who answered the benefits question; the chart wording is used here. Journal-entry testing itself (88% in 2024) belongs to substantive testing."

- id: assurance-planning-risk-assessment-07
  title: Evidence-linked, assertion-level risk assessment tied to materiality and methodology
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Risk scores from analytics often sit outside the workpaper tools and are hard to tie to assertions, materiality and firm methodology."
  solution: "MindBridge announced Agentic Risk Assessment, which connects evidence, analytics, assertions, materiality and methodology to support audit planning decisions. It is meant to work with customer-built and third-party workpaper tools, with an MCP server so compatible AI assistants can query results."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none"
      measures: "The 22 Sep 2026 release gives no usage or accuracy figures and does not say whether the capability is generally available"
      provenance: vendor-published
      source_ref: MINDBRIDGE-ARA-2026
  prerequisites:
    - "Full-population transaction data analysed in the MindBridge platform [MINDBRIDGE-ARA-2026]"
    - "Integration with the firm's workpaper tools [MINDBRIDGE-ARA-2026]"
  risks_and_guardrails:
    - "MindBridge says auditor judgment and control are preserved [MINDBRIDGE-ARA-2026]"
  human_checkpoints:
    - "Auditor judgment retained over the risk assessment [MINDBRIDGE-ARA-2026]"
  role_evolution: "none stated in the sources."
  evidence_grade: C
  sources:
    - { ref: MINDBRIDGE-ARA-2026, title: "MindBridge advances financial oversight for the agentic era with new platform capabilities", publisher: MindBridge (Business Wire via BNN Bloomberg), type: vendor, url: "https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/", date: 2026-09-22, access: full, locator: "paragraph 'Agentic Risk Assessment for audit & assurance'" }
    - { ref: CPAPA-MINDBRIDGE-2026, title: "MindBridge launches new AI capabilities for finance and audit", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=190850", date: 2026-09-30, access: full, locator: "paragraph on Agentic Risk Assessment" }
  last_reviewed: 2026-10-16
  notes: "Announcement only. Named audit-firm customer stories for MindBridge's earlier analytics were not opened (the site returned 403) and are not dated. Not used: a customer-marked technical whitepaper on assertion-level scoring."

- id: assurance-planning-risk-assessment-08
  title: Agent-recommended starting risk scores for internal audit planning and prioritisation
  archetype: assurance
  module: planning-risk-assessment
  function: risk-compliance-legal
  work_types: [data-reporting, expert-judgment]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Internal audit teams score risks by hand for planning and prioritisation, with inconsistent results."
  solution: "Optro announced Agentic Risk Assessment Scoring. It analyses selected data in the Optro platform and recommends starting scores with supporting evidence, for a faster and more consistent view of risk for planning and prioritisation."
  outcomes:
    - lever: speed
      description: "none published for this agent"
      figure: "none"
      measures: "The 14 Oct 2026 release gives no figure for risk scoring. Reddit's internal audit results in the same release relate to controls testing (routed)."
      provenance: vendor-published
      source_ref: OPTRO-CRX-2026
  prerequisites:
    - "Risk and control data held in the Optro platform [OPTRO-CRX-2026]"
  risks_and_guardrails:
    - "Optro says agents run within team-defined guardrails and risk appetites, with every action logged and cited [OPTRO-CRX-2026]"
  human_checkpoints:
    - "Scores are starting recommendations; the team decides [OPTRO-CRX-2026]"
  role_evolution: "none stated for this feature."
  evidence_grade: C
  sources:
    - { ref: OPTRO-CRX-2026, title: "Optro launches domain-trained agents for audit, compliance, third-party risk and AI governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14, access: full, locator: "bullet 'Agentic Risk Assessment Scoring'" }
  last_reviewed: 2026-10-16
  notes: "Announced at Optro's CRX conference. Applies to in-house internal audit and GRC teams as well as audit firms."

- id: assurance-planning-risk-assessment-09
  title: Map risks to controls and score them at scoping for internal audit engagements
  archetype: assurance
  module: planning-risk-assessment
  function: risk-compliance-legal
  work_types: [expert-judgment, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Scoping is where internal audit teams lose the most time, mapping risks to controls by hand before testing starts (Fieldguide's framing)."
  solution: "Fieldguide's Field Agents map risks to controls and score them to give a scoped starting point, while the auditor makes the final call. BDO's Risk Advisory Services practice announced a collaboration to roll the platform out to member firms, starting with internal audit and third-party assurance, led by BDO Belgium."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none"
      measures: "The webinar listing and the BDO article give no figure for scoping or risk mapping"
      provenance: vendor-published
      source_ref: FIELDGUIDE-DEMO-2026
  prerequisites:
    - "Engagement data and methodology configured in the Fieldguide platform [BDO-FIELDGUIDE-2026]"
  risks_and_guardrails:
    - "Fieldguide says agents run under full human supervision, with methodology applied consistently and traceability built in [BDO-FIELDGUIDE-2026]"
  human_checkpoints:
    - "The auditor reviews the result and makes the final call [FIELDGUIDE-DEMO-2026]"
  role_evolution: "BDO says it is building a revised operating model that weaves AI agents into routine delivery, targeting labour-intensive and administrative work [BDO-FIELDGUIDE-2026]."
  evidence_grade: C
  sources:
    - { ref: FIELDGUIDE-DEMO-2026, title: "See Field Agents execute internal audit engagements live", publisher: Fieldguide, type: vendor, url: "https://info.fieldguide.io/fieldguide-live-demo-internal-audit-mar17", date: 2026-10-20, access: full, locator: "bullet 'Scoping and risk assessment'; date is the scheduled webinar" }
    - { ref: BDO-FIELDGUIDE-2026, title: "BDO expands AI use in risk advisory through Fieldguide tie-up", publisher: International Accounting Bulletin (via Yahoo Finance), type: press, url: "https://finance.yahoo.com/sectors/technology/articles/bdo-expands-ai-risk-advisory-113450007.html", date: 2026-03-25, access: full, locator: "paragraphs 1-6" }
    - { ref: SILICONANGLE-FIELDGUIDE-2026, title: "Fieldguide raises $75M on $700M valuation to scale agentic AI for audit and advisory firms", publisher: SiliconANGLE, type: press, url: "https://siliconangle.com/2026/02/02/fieldguide-raises-75m-700m-valuation-scale-agentic-ai-audit-advisory-firms/", date: 2026-02-02, access: full, locator: "paragraphs 1-3" }
  last_reviewed: 2026-10-16
  notes: "BDO's deployment is platform-wide; no source confirms BDO uses the risk-mapping feature. That is why this is grade C rather than B. The date is the scheduled demo (4 days after today); the listing itself was live on 2026-10-16."

- id: assurance-planning-risk-assessment-10
  title: Agents that scan media for emerging threats and draft staff memos
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Keeping up with news and events that bear on an audited entity's risk is manual and uneven."
  solution: "Bloomberg Law reports that Deloitte auditors worldwide gained access to a suite of agents that can scan media reports for emerging threats and produce first drafts of staff memos. Deloitte's Omnia release describes a unified agent network for nearly 85,000 audit and assurance practitioners, with agents running preliminary procedures (extraction, evidence analysis, draft documentation, preliminary conclusions for review) and context-aware responses."
  outcomes:
    - lever: speed
      description: "A Deloitte leader expects the time from client documents arriving to being populated in working papers to shorten. This is an expectation, not a result."
      figure: "none published"
      measures: "Stated expectation by a Deloitte US partner quoted by Bloomberg Law; no measurement"
      provenance: self-reported
      source_ref: BBL-DELOITTE-2026
  prerequisites:
    - "Omnia platform upgrades to host the agent network [BBL-DELOITTE-2026]"
    - "Governance under Deloitte's Trustworthy AI framework [DELOITTE-OMNIA-2026]"
  risks_and_guardrails:
    - "Agents produce preliminary conclusions for professionals to review [DELOITTE-OMNIA-2026]"
  human_checkpoints:
    - "Practitioners supervise and validate agent output [DELOITTE-OMNIA-2026]"
  role_evolution: "Deloitte's release describes a 'tutor mode' that gives on-demand micro-training in the context of the work, plus an AI Academy and an AI learning assistant [DELOITTE-OMNIA-2026]."
  evidence_grade: B
  sources:
    - { ref: BBL-DELOITTE-2026, title: "Deloitte adopts advanced AI to power corporate audits globally", publisher: Bloomberg Law, type: press, url: "https://news.bloomberglaw.com/financial-accounting/deloitte-adopts-advanced-ai-to-power-corporate-audits-globally", date: 2026-06-29, access: full, locator: "paragraphs 1-4" }
    - { ref: DELOITTE-OMNIA-2026, title: "Deloitte unveils connected agentic intelligence in Omnia to advance audit and assurance", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24, access: full, locator: "paragraphs 1-6" }
  last_reviewed: 2026-10-16
  notes: "The media-scanning capability is reported by Bloomberg Law; Deloitte's own release does not name it. The release speaks of enhanced insights and deep risk analysis. No figures are published."

- id: assurance-planning-risk-assessment-11
  title: Orchestrated agent frameworks inside the firm platform covering planning, risk assessment and procedures
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Separate point tools leave planning, risk assessment and testing disconnected, so risk views are not updated as work proceeds."
  solution: "EY embedded a multi-agent framework in EY Canvas, saying it immediately puts AI in all audit phases and addresses risks more dynamically, with end-to-end support expected by 2028. Deloitte unified its agents in Omnia. KPMG said in Apr 2026 it would pilot orchestration agents, starting as soon as that summer, on asset valuation and revenue-process testing. PwC expects a global agentic platform about 18 months after 2026. Grant Thornton calls gtap the foundation for agents that orchestrate audit activity."
  outcomes:
    - lever: capacity
      description: "Reach, not effect: EY's platform covers the daily workflows of 130,000 assurance professionals across 160,000 audit engagements in more than 150 countries and territories."
      figure: "130,000 professionals; 160,000 engagements"
      measures: "Population and engagements covered by the EY Canvas platform per EY's release; not a measure of agent use or results"
      provenance: self-reported
      source_ref: EY-CANVAS-2026
    - lever: capacity
      description: "Adoption signal: the six large networks collectively reported about 30% year-over-year growth in AI-enabled tools in 2025."
      figure: "about 30%"
      measures: "Year-over-year increase in AI-enabled tools reported collectively by the GPPC networks; IFIAR says reporting practices differ by network"
      provenance: independent
      source_ref: IFIAR-TTF-2026
  prerequisites:
    - "A single global platform and data foundation (EY Canvas on Microsoft Azure, Foundry and Fabric) [EY-CANVAS-2026]"
    - "A global training programme for audit and technology-risk staff [EY-CANVAS-2026]"
  risks_and_guardrails:
    - "IFIAR says that as systems become more autonomous, auditors must retain responsibility to evaluate, validate and challenge decisions made by AI, and explain key judgements [IFIAR-TTF-2026]"
    - "IFIAR members saw unclear division of monitoring responsibility between networks and member firms in 2025 [IFIAR-TTF-2025]"
  human_checkpoints:
    - "EY says the approach keeps human judgment, skepticism and insight [EY-CANVAS-2026]"
  role_evolution: "EY says its approach will reduce administrative burden for clients and improve risk assessments while keeping human judgment [EY-CANVAS-2026]."
  evidence_grade: B
  sources:
    - { ref: EY-CANVAS-2026, title: "EY launches enterprise-scale agentic AI to redefine the audit experience for the AI era", publisher: EY, type: firm, url: "https://www.ey.com/en_ca/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era", date: 2026-04-07, access: full, locator: "paragraphs 1-4 of the release" }
    - { ref: DELOITTE-OMNIA-2026, title: "Deloitte unveils connected agentic intelligence in Omnia to advance audit and assurance", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24, access: full, locator: "paragraphs 1-3" }
    - { ref: BBL-KPMG-2026, title: "KPMG to test advanced AI agents in next phase for audits", publisher: Bloomberg Law, type: press, url: "https://news.bloomberglaw.com/financial-accounting/kpmg-to-test-advanced-ai-agents-in-next-phase-for-audits", date: 2026-04-01, access: full, locator: "opening paragraphs (page is paywalled after the first section)" }
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraph on global agentic platform within about 18 months" }
    - { ref: GT-GTAP-2026, title: "Grant Thornton launches gtap", publisher: Grant Thornton LLP, type: firm, url: "https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us", date: 2026-05-07, access: full, locator: "paragraph beginning 'Grant Thornton built gtap to grow'" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality", publisher: IFIAR Technology Task Force (FSA Japan copy), type: regulator, url: "https://www.fsa.go.jp/ifiar/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "section 'Emergence of Agentic AI', p. 5, and footnote 1" }
  last_reviewed: 2026-10-16
  notes: "Planning-specific agents inside these frameworks are not itemised in any source except EY's 'improve risk assessments' and Deloitte's 'deep risk analysis' wording. Grade B rests on named deployments with scale claims but no measurements. EY says all phases now and end-to-end by 2028; KPMG's orchestration is a pilot, not in production, and its details come from an opening section only. Regulator IFIAR also relays that firms plan to explore agentic systems."

- id: assurance-planning-risk-assessment-12
  title: AI-supported staffing requests, budget planning and engagement-leader review
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [coordination-scheduling]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Manual staffing and budgeting processes give leaders little visibility into engagement planning and resourcing."
  solution: "RSM Luca Resourcing replaces manual processes with a connected collaboration tool that supports initial staffing requests, budget planning and engagement-leader review. The pattern is 'other': a planning workflow tool; the source does not say what AI features it contains."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none"
      measures: "RSM gives no figure and does not state what share of engagements use the tool"
      provenance: self-reported
      source_ref: CAQ-RSM-2026
  prerequisites:
    - "Engagement planning data and staffing requests captured in one tool [CAQ-RSM-2026]"
  risks_and_guardrails:
    - "none stated in the source"
  human_checkpoints:
    - "Engagement-leader review is a step in the tool [CAQ-RSM-2026]"
  role_evolution: "RSM's assurance digital leader says the tool helps leaders make faster, more informed staffing decisions and streamlines workforce planning [CAQ-RSM-2026]. Fieldguide's demo listing also mentions real-time budget and workload visibility in its agent platform [FIELDGUIDE-DEMO-2026]."
  evidence_grade: B
  sources:
    - { ref: CAQ-RSM-2026, title: "Shaping the future of assurance: Advancing AI in the audit", publisher: Center for Audit Quality (author: RSM assurance digital leader), type: professional-body, url: "https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit", date: 2026-08-25, access: full, locator: "section 'RSM Luca Resourcing'" }
    - { ref: FIELDGUIDE-DEMO-2026, title: "See Field Agents execute internal audit engagements live", publisher: Fieldguide, type: vendor, url: "https://info.fieldguide.io/fieldguide-live-demo-internal-audit-mar17", date: 2026-10-20, access: full, locator: "bullet 'Findings and reporting, always current'" }
  last_reviewed: 2026-10-16
  notes: "The source does not describe how much of the tool uses AI; it presents it as one of three AI-related innovations added to RSM's digital audit ecosystem in the past year. Treat the AI content as unconfirmed."

- id: assurance-planning-risk-assessment-13
  title: Enterprise chat assistants for entity and industry research and for summarising client documents
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Building an understanding of an entity and its industry takes research and document reading before risk assessment can start."
  solution: "RSM says Microsoft 365 Copilot supports everyday tasks such as summarising information, drafting communications, preparing meeting notes and analysing documents. KPMG began deploying Copilot to audit partners and professionals in Apr 2024 and reported more than 2.175 million Audit Chat conversations since its Oct 2023 launch, covering database search, contract extraction, document analysis and research. ICAEW notes that auditors use simple chatbots to enhance their understanding of entities and their environments via research."
  outcomes:
    - lever: capacity
      description: "Usage figure: KPMG partners and professionals held more than 2.175 million Audit Chat conversations."
      figure: "more than 2.175 million"
      measures: "Audit Chat conversations by KPMG partners and professionals since the Oct 2023 launch, as stated in a May 2024 announcement recapped in the Apr 2025 release; not planning-specific; not a quality or time measure"
      provenance: self-reported
      source_ref: KPMG-CLARA-2025
    - lever: capacity
      description: "Adoption signal: tax and audit professionals using AI regularly."
      figure: "81%"
      measures: "Share of tax and audit professionals in Thomson Reuters Institute's 2026 Future of Professionals survey who say they use AI tools regularly (sample size not given in the summary page)"
      provenance: independent
      source_ref: TRI-FOP-2026
  prerequisites:
    - "Approved enterprise tool under a use policy [CAQ-RSM-2026]"
    - "Safeguards on what client information may be entered; PCAOB staff found some firms limit staff use on audit procedures for data privacy and reliability reasons [PCAOB-GENAI-2024]"
  risks_and_guardrails:
    - "More than one-third of tax and audit professionals admit to using unauthorised AI tools [TRI-FOP-2026]"
    - "RSM says the tool is used with human oversight [CAQ-RSM-2026]"
  human_checkpoints:
    - "The auditor owns the understanding of the entity; ICAEW's test found chatbots cannot do inquiry, observation or inspection [ICAEW-PIERPOINT-2025]"
  role_evolution: "RSM says tools like this free capacity for time spent understanding client risks and asking better questions [CAQ-RSM-2026]. TR's paper urges firms to define early-career roles and keep supervision in place before automation erodes development opportunities [TRI-FOP-2026]."
  evidence_grade: B
  sources:
    - { ref: CAQ-RSM-2026, title: "Shaping the future of assurance: Advancing AI in the audit", publisher: Center for Audit Quality (author: RSM assurance digital leader), type: professional-body, url: "https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit", date: 2026-08-25, access: full, locator: "section on Microsoft M365 Copilot" }
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG US (Newsfile Corp.), type: firm, url: "https://www.newsfilecorp.com/release/249535/KPMG-Advances-AI-Integration-in-KPMG-Clara-Smart-Audit-Platform", date: 2025-04-23, access: full, locator: "recap paragraphs 'In May 2024' and 'In April 2024'" }
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "introduction" }
    - { ref: TRI-FOP-2026, title: "What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07-21, access: full, locator: "paragraphs 3-9" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff update on outreach activities related to the integration of generative AI in audits and financial reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "Observations related to GenAI integration in audits, p. 4" }
  last_reviewed: 2026-10-16
  notes: "The PCAOB spotlight is staff outreach from mid-2024 and is a foundation source. The 2.175 million count is dated to May 2024 and mixes all Audit Chat uses. The ICAEW observation comes from an article intro and names no firm."

- id: assurance-planning-risk-assessment-14
  title: Analyse audit-committee communications to surface issues earlier in planning
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Issues raised in communications with those charged with governance can surface late in audit preparation."
  solution: "PwC says another of its 2026 year-end tools analyses audit-committee communications to surface issues that need handling sooner in the audit preparation cycle."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none"
      measures: "The CFO Dive interview gives no figure for this tool"
      provenance: self-reported
      source_ref: CFODIVE-PWC-2026
  prerequisites:
    - "Access to audit-committee communications in a form the tool can read [CFODIVE-PWC-2026]"
  risks_and_guardrails:
    - "none stated in the source"
  human_checkpoints:
    - "none stated in the source"
  role_evolution: "none stated for this tool."
  evidence_grade: C
  sources:
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "paragraph beginning 'For 2026 year-end audits'" }
  last_reviewed: 2026-10-16
  notes: "The source says PwC 'will be' using these tools for 2026 year-end audits, so this is announced, not confirmed in use."

- id: assurance-planning-risk-assessment-15
  title: Standardised ERP data ingestion as the base for planning analytics
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [data-reporting, software-systems]
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Fragmented tools and client data in many formats block analytics at the start of the audit. Poor client data (60%) and no access to client systems (53%) are top blockers for surveyed US firms."
  solution: "Grant Thornton's gtap is a cloud-based infrastructure that standardises how audit data is ingested, transformed and analysed from any ERP system, replacing fragmented tools. It supports full-population analysis and is the base for intelligent agents that surface risks and anomalies. It started with private-company audits, with public companies planned for the next year."
  outcomes:
    - lever: quality
      description: "Grant Thornton says it increases consistency across engagements and reduces variability and manual steps. No figure given."
      figure: "none published"
      measures: "Qualitative statement by Grant Thornton's CEO; no measurement"
      provenance: self-reported
      source_ref: GT-GTAP-2026
    - lever: capacity
      description: "Adoption signal: surveyed firms with automated trial-balance import and data ingestion."
      figure: "35% (trial-balance import); 19% (data ingestion)"
      measures: "Share of surveyed firms reporting an automated solution for trial balance taxonomy and import, and for data ingestion; the report's analysis covers 54 firms with complete data"
      provenance: independent
      source_ref: CPACOM-ATR-2025
  prerequisites:
    - "Client ERP access and data in a form that can be ingested; surveyed firms cite no access to client systems (53%) [CPACOM-ATR-2025]"
  risks_and_guardrails:
    - "Grant Thornton says professionals supervise every step [GT-GTAP-2026]"
  human_checkpoints:
    - "Auditors maintain oversight of the agents' flagged risks and anomalies [GT-GTAP-2026]"
  role_evolution: "Grant Thornton's CEO says teams will spend more time on professional skepticism, assessing risk and delivering insights [GT-GTAP-2026]."
  evidence_grade: B
  sources:
    - { ref: GT-GTAP-2026, title: "Grant Thornton launches gtap", publisher: Grant Thornton LLP, type: firm, url: "https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us", date: 2026-05-07, access: full, locator: "paragraphs 1-4" }
    - { ref: CPAPA-GT-2026, title: "Grant Thornton U.S. launches in-house audit transformation platform", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/05/08/grant-thornton-u-s-launches-in-house-audit-transformation-platform/183107/", date: 2026-05-08, access: full, locator: "article body" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: CPA.com (AICPA), type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "automated-solutions chart; blockers chart" }
  last_reviewed: 2026-10-16
  notes: "The release says gtap 'opens the door to' agents that surface risks and anomalies, so agent features are prospective. The launch itself is the named deployment."

- id: assurance-planning-risk-assessment-16
  title: Methodology-embedded, risk-based engagement platform with in-context AI guidance for mid-tier firms
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Mid-tier firms use disconnected tools and prior-year habits. Many surveyed firms say they have trouble fully using a risk-driven approach."
  solution: "EisnerAmper, Citrin Cooperman and PKF O'Connor Davies adopted the Dynamic Assurance Solution (DAS) suite, a risk-focused methodology built by the AICPA, CPA.com and Caseware that connects risk assessment, workpapers and reporting, now with Verity. PKF also joined an agentic pioneer programme to co-develop its own agents. The firms phased roll-out with training."
  outcomes:
    - lever: capacity
      description: "EisnerAmper reports platform adoption: users and completed engagements. This measures DAS adoption, not an AI effect."
      figure: "more than 1,100 professionals; over 1,500 engagements"
      measures: "EisnerAmper professionals using the DAS suite to execute audits, and client engagements completed on it, as of the 25 Jun 2026 release"
      provenance: vendor-published
      source_ref: CASEWARE-EISNERAMPER-2026
  prerequisites:
    - "Migration of data and methodology to the platform; each firm used CPA.com as implementation partner for planning, data migration, training and change management [CASEWARE-CITRIN-2026]"
    - "A phased rollout with pilots and training; EisnerAmper says professional readiness came before speed [CASEWARE-EISNERAMPER-2026]"
  risks_and_guardrails:
    - "Caseware says AI outputs are traceable and explainable, with firm control and engagement boundaries [CASEWARE-VERITY-2026]"
  human_checkpoints:
    - "Suggestions can be accepted, refined or overridden by the auditor [CASEWARE-LAUNCH-2026]"
  role_evolution: "Citrin Cooperman's assurance innovation leader says seeing the reasoning behind procedures and conclusions helps staff build technical knowledge and judgment [CASEWARE-CITRIN-2026]."
  evidence_grade: B
  sources:
    - { ref: CASEWARE-EISNERAMPER-2026, title: "EisnerAmper leverages DAS powered by Caseware to unify audit and build an agentic future", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice", date: 2026-06-25, access: full, locator: "paragraphs 1-6" }
    - { ref: CASEWARE-CITRIN-2026, title: "Citrin Cooperman adopts AI-enabled DAS suite powered by Caseware", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth", date: 2026-07-13, access: full, locator: "paragraphs 1-6" }
    - { ref: CASEWARE-PKF-2026, title: "PKF O'Connor Davies adopts AI-enabled DAS suite powered by Caseware Verity and joins the Agentic Pioneer Program", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program", date: 2026-10-08, access: full, locator: "paragraphs 1-4" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: CPA.com (AICPA), type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "section 'Reported challenges of adopting a risk-driven approach'" }
  last_reviewed: 2026-10-16
  notes: "Grade B is capped: the figures measure platform adoption, and the three press releases are vendor-published about vendor customers. Whether each firm uses the Verity risk features in planning is not stated; PKF's release describes the platform generally."

- id: assurance-planning-risk-assessment-17
  title: Guided IT-environment risk identification for auditors without IT specialists
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "ISA 315 raises expectations for identifying IT risks, but mid-tier firms often lack formal IT audit teams."
  solution: "An ICAEW viewpoint by a vendor co-founder says purpose-built agentic AI platforms can map risks to controls, analyse documents and system outputs and produce audit-ready documentation aligned with ISA 315, with human-in-the-loop review. It pairs this with structured engagement documentation that prompts generalists to consider the IT environment, training, and designated tech champions."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none"
      measures: "The article is a viewpoint and gives no figures"
      provenance: vendor-published
      source_ref: ICAEW-315-2025
  prerequisites:
    - "ISA 315 requirements embedded in firm methodology with prompts and frameworks [ICAEW-315-2025]"
    - "Training that gives generalists the ability to read system flows rather than producing full IT auditors [ICAEW-315-2025]"
  risks_and_guardrails:
    - "The article points to the FRC's guidance that tools must be certified, documented and periodically reassessed [ICAEW-315-2025]"
  human_checkpoints:
    - "Auditors review, validate and challenge flagged issues and drafted documentation [ICAEW-315-2025]"
  role_evolution: "The article urges tech champions or innovation task forces within teams to support colleagues [ICAEW-315-2025]."
  evidence_grade: C
  sources:
    - { ref: ICAEW-315-2025, title: "Meeting ISA 315 requirements without specialist IT teams", publisher: ICAEW (author: co-founder of Platformed, a vendor), type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/oct-2025/meeting-isa-315-requirements-without-specialists-it-teams", date: 2025-10, access: full, locator: "paragraphs on purpose-built agentic AI platforms and 'human-in-the-loop'" }
  last_reviewed: 2026-10-16
  notes: "Authored by a vendor and published by ICAEW; treated as a vendor claim. Exact day of publication not shown on the page."

- id: assurance-planning-risk-assessment-18
  title: GenAI-drafted fraud risk brainstorming (schemes, likely perpetrators, expected controls, audit tests)
  archetype: assurance
  module: planning-risk-assessment
  function: risk-compliance-legal
  work_types: [expert-judgment, research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Fraud risk brainstorming depends on the team's knowledge of schemes that have occurred elsewhere."
  solution: "A City of Charlotte internal auditor, presenting in a personal capacity at a state auditors' conference, shows a GenAI chatbot used in audit planning to list real cemetery and burial fraud cases (2018-2026), then draft a table of fraud schemes by likelihood, likely perpetrator, expected controls and audit tests for a cemetery-operations audit."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none"
      measures: "The slides show outputs but no measure of quality, time or whether the outputs were used in an engagement"
      provenance: self-reported
      source_ref: VLGAA-NUCCIO-2026
  prerequisites:
    - "Access to a general-purpose chatbot and well-structured prompts (context, task, guidelines, output format) [VLGAA-NUCCIO-2026]"
  risks_and_guardrails:
    - "ICAEW's test found one model did not treat revenue recognition as a fraud risk, which ISA 240 presumes, and another cited presumed fraud risk without explaining why some risks were significant and others not [ICAEW-PIERPOINT-2025]"
  human_checkpoints:
    - "The auditor judges which schemes matter; the presenter's slides ask whether the model applied COSO and the answer shown was that it did not explicitly [VLGAA-NUCCIO-2026]"
  role_evolution: "none stated."
  evidence_grade: B
  sources:
    - { ref: VLGAA-NUCCIO-2026, title: "Using Generative AI in Internal Audit (conference slides)", publisher: Virginia Local Government Auditors Association (speaker, City of Charlotte NC), type: conference, url: "https://vlgaa.starchapter.com/images/downloads/Documents/day_1___2___using_generative_ai_in_internal_audit___d._nuccio.pdf", date: 2026-04, access: full, locator: "slides 49-52 (Audit Planning: Fraud Brainstorming)" }
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "section on risk assessment (ISA 240 revenue recognition)" }
  last_reviewed: 2026-10-16
  notes: "A named practitioner's demonstration, not a firm programme; the presenter says the views are his own and not the City's. The date is the PDF's creation date (13 Apr 2026); the conference date is not shown. Applies to local-government internal audit, not external audit; no external-audit firm evidence on fraud brainstorming was found."

- id: assurance-planning-risk-assessment-19
  title: GenAI-drafted risk considerations from prior audit findings and peer audits for internal audit planning
  archetype: assurance
  module: planning-risk-assessment
  function: risk-compliance-legal
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Internal audit planning needs a view of the risk areas for an auditable unit, built from prior findings and comparable audits."
  solution: "The same City of Charlotte presenter shows the chatbot finding peer local-government audit reports on a topic, grouping their findings into themes, and drafting a table of risk considerations with level, prior-finding flags and descriptions for a cemetery-operations audit. One slide notes that the model did not explicitly map risks to the COSO framework."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none"
      measures: "No time or quality measure in the slides"
      provenance: self-reported
      source_ref: VLGAA-NUCCIO-2026
  prerequisites:
    - "Prior audit findings and operational context supplied to the model [VLGAA-NUCCIO-2026]"
  risks_and_guardrails:
    - "The slides show the model built risk considerations from prior findings, operational context and peer audits, not from a control framework [VLGAA-NUCCIO-2026]"
  human_checkpoints:
    - "The auditor checks the output against frameworks the model did not apply [VLGAA-NUCCIO-2026]"
  role_evolution: "none stated."
  evidence_grade: B
  sources:
    - { ref: VLGAA-NUCCIO-2026, title: "Using Generative AI in Internal Audit (conference slides)", publisher: Virginia Local Government Auditors Association (speaker, City of Charlotte NC), type: conference, url: "https://vlgaa.starchapter.com/images/downloads/Documents/day_1___2___using_generative_ai_in_internal_audit___d._nuccio.pdf", date: 2026-04, access: full, locator: "slides 42-48 (Audit Planning: Identifying Risk Considerations)" }
  last_reviewed: 2026-10-16
  notes: "Same caveats as the fraud brainstorming entry: a named practitioner demonstration in a personal capacity, no outcome measures. Slide text for the risk table was read from rendered images."

- id: assurance-planning-risk-assessment-20
  title: General-purpose chatbot drafts risks of material misstatement from financial statements
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [expert-judgment]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Auditors may ask a chatbot to identify risks of material misstatement directly from financial statements."
  solution: "Idea (tested by ICAEW, not a deployment): give a chatbot the financial statements and ask for risks, red flags and an ISA-referenced risk assessment. ICAEW tried Copilot, Grok 3 and Claude on a fictional retailer."
  outcomes:
    - lever: quality
      description: "None of the three models performed risk assessment as a human auditor would, and none separated financial-statement-level from assertion-level risks. Copilot did not treat revenue recognition as a risk area, though ISA 240 presumes it is a fraud risk. Grok tied risks to assertions and ISAs and flagged going concern."
      figure: "3 models; 0 of 3 separated FS-level from assertion-level risk"
      measures: "Single test by one ICAEW faculty technical manager on fictional company data generated by Copilot; not a benchmark; models have since changed"
      provenance: independent
      source_ref: ICAEW-PIERPOINT-2025
  prerequisites:
    - "Prompts shaped with ICAEW's prompt guidance and a prompt enhancer; added detail on materiality rationale and output format [ICAEW-PIERPOINT-2025]"
  risks_and_guardrails:
    - "Models could not supplement understanding through inquiry, observation and inspection as ISA 315 requires [ICAEW-PIERPOINT-2025]"
    - "Polished output arrives fast (under 20 seconds for Copilot), which can mask gaps [ICAEW-PIERPOINT-2025]"
  human_checkpoints:
    - "ICAEW concludes human judgment is required to interpret the output and decide on risks [ICAEW-PIERPOINT-2025]"
  role_evolution: "none stated."
  evidence_grade: D
  sources:
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "sections on risk assessment and conclusion" }
  last_reviewed: 2026-10-16
  notes: "idea. Graded D because the source is a test of an idea on fictional data, not a deployment. It is independent evidence of limits. Publication date taken from the search listing (24 Sep 2025) and the URL path (sep-2025)."

- id: assurance-planning-risk-assessment-21
  title: General-purpose chatbot proposes materiality benchmarks and performance materiality
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [expert-judgment, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Setting materiality and performance materiality requires judgment about benchmark, percentage and risk factors."
  solution: "Idea (tested by ICAEW, not a deployment): ask a chatbot to calculate financial-statement and performance materiality from the financial statements. The pattern is 'other': a calculation with rationale."
  outcomes:
    - lever: quality
      description: "Materiality figures varied widely across the three models. Copilot chose a revenue benchmark at 0.75% with a vague rationale and did not consider whether the entity was a public interest entity. All three were good at linking performance materiality to entity understanding, risk assessment and prior misstatements; Claude suggested 60%."
      figure: "Copilot 0.75% of a revenue benchmark; Claude 60% performance materiality"
      measures: "Percentage Copilot applied to its chosen benchmark; performance-materiality percentage Claude suggested; one test on fictional data with no prior-period misstatement information supplied"
      provenance: independent
      source_ref: ICAEW-PIERPOINT-2025
  prerequisites:
    - "Rationale for materiality calculations and output format supplied in the prompt [ICAEW-PIERPOINT-2025]"
  risks_and_guardrails:
    - "Models rounded year-on-year percentage changes inconsistently (Copilot worst) [ICAEW-PIERPOINT-2025]"
    - "A rationale may be a hallucination (ICAEW's wording for Copilot's claim that revenue is less open to manipulation than operating profit) [ICAEW-PIERPOINT-2025]"
  human_checkpoints:
    - "Human judgment to pick the benchmark and thresholds [ICAEW-PIERPOINT-2025]"
  role_evolution: "none stated."
  evidence_grade: D
  sources:
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "section 'Materiality'" }
    - { ref: MINDBRIDGE-ARA-2026, title: "MindBridge advances financial oversight for the agentic era with new platform capabilities", publisher: MindBridge (Business Wire via BNN Bloomberg), type: vendor, url: "https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/", date: 2026-09-22, access: full, locator: "paragraph 'Agentic Risk Assessment' (materiality listed among linked inputs)" }
  last_reviewed: 2026-10-16
  notes: "idea. No firm, vendor or regulator source describes AI setting materiality in practice. MindBridge lists materiality as an input connected to its risk assessment, not a calculation it performs."

- id: assurance-planning-risk-assessment-22
  title: Multi-agent restatement-risk scoring from MD&A text, financial ratios and critical audit matters
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "Audit risk assessment combines different evidence streams but usually gives single point predictions without showing how well the streams agree."
  solution: "Idea (research prototype): UMAR uses three specialised agents (MD&A text, financial ratios, critical audit matters), each giving a risk score with a calibrated uncertainty estimate, fused by an aggregator based on Dempster-Shafer evidence theory that also measures conflict between agents. The pattern is 'other': multi-agent score fusion."
  outcomes:
    - lever: quality
      description: "On the authors' test set UMAR beat logistic regression, XGBoost, FinBERT and single- and dual-agent LLM baselines, with the lowest calibration error."
      figure: "AUROC 0.782; PR-AUC 0.341; ECE 0.052"
      measures: "Discrimination (AUROC, PR-AUC) and expected calibration error on 3,200 US 10-K firm-year observations (2019-2023), with financial restatement as the label; authors' own evaluation, not a live audit"
      provenance: independent
      source_ref: ARXIV-UMAR-2026
  prerequisites:
    - "Public-company filings with text and ratios; a restatement label for training [ARXIV-UMAR-2026]"
  risks_and_guardrails:
    - "The authors describe the output as potentially actionable and interpretable risk signals; the abstract reports no field test [ARXIV-UMAR-2026]"
  human_checkpoints:
    - "none stated in the abstract"
  role_evolution: "none stated."
  evidence_grade: D
  sources:
    - { ref: ARXIV-UMAR-2026, title: "Multi-Agent Framework for Audit Risk Assessment with Explicit Uncertainty and Evidence Conflict Modeling", publisher: arXiv (Wang et al.), type: academic, url: "https://arxiv.org/abs/2606.15640", date: 2026-06-14, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "idea. A preprint, abstract read only. The label is restatement, which is an adjacent outcome to audit risk. The PR-AUC of 0.341 shows the precision ceiling. Companion benchmark: FinancialAuditBench (90 workpaper completion and review tasks across six synthetic engagements, 11 frontier models) found agents complete much staff-level work but sometimes perform inappropriate procedures or write incorrect documentation; it covers workpaper work generally, not planning [ARXIV-FAB-2026]."

- id: assurance-planning-risk-assessment-23
  title: Continuous, predictive risk reassessment that adapts procedures as new data arrives
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [data-reporting, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "Risk assessment is a point-in-time planning step, so changes in the entity during the audit are picked up late."
  solution: "Idea (discussed by firms and regulators): agents continuously assess risk and adapt procedures as new data emerges. Grant Thornton designed gtap as the foundation for such an agentic model. Caseware describes engagements where AI continuously assists with planning, risk identification, evidence collection and review. IFIAR lists predictive data analytics, usable in risk assessment and planning to inform where further procedures are needed, among technologies firms are exploring."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No source reports a deployment or measurement"
      provenance: self-reported
      source_ref: GT-GTAP-2026
  prerequisites:
    - "Continuous, standardised client data feeds [GT-GTAP-2026]"
  risks_and_guardrails:
    - "IFIAR warns that increasingly autonomous systems raise oversight and over-reliance risks, and says auditors must keep responsibility [IFIAR-TTF-2026]"
  human_checkpoints:
    - "Grant Thornton says professionals supervise every step [GT-GTAP-2026]"
  role_evolution: "none stated."
  evidence_grade: D
  sources:
    - { ref: GT-GTAP-2026, title: "Grant Thornton launches gtap", publisher: Grant Thornton LLP, type: firm, url: "https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us", date: 2026-05-07, access: full, locator: "paragraph beginning 'Grant Thornton built gtap to grow'" }
    - { ref: CASEWARE-AIDA-2026, title: "From AiDA to agentic: How Caseware's AI has evolved", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved", date: 2026-07-28, access: full, locator: "section 'What's next'" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality", publisher: IFIAR Technology Task Force (FSA Japan copy), type: regulator, url: "https://www.fsa.go.jp/ifiar/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "Appendix A, row 'Predictive Data Analytics'" }
  last_reviewed: 2026-10-16
  notes: "idea. Forward-looking statements only. Keep separate from use case 11, where agent frameworks are in production but their planning-specific functions are not itemised."

- id: assurance-planning-risk-assessment-24
  title: AI-supported scoping decisions on what is in and out of the audit
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Deciding which accounts, processes and locations to scope in is a judgment call made largely from prior-year files and team knowledge."
  solution: "PwC said in Oct 2025 it plans soon to have a risk-assessment tool that helps people make smarter decisions about what is and is not scoped in the audit. PCAOB staff reported in 2024 that firms saw scoping the audit as a potential area for GenAI. Fieldguide's demo pairs scoping with risk assessment for internal audit."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none"
      measures: "No source reports use or measurement; the PwC tool was described as planned, and the Oct 2026 follow-up article does not mention it"
      provenance: self-reported
      source_ref: PWC-AT-2025
  prerequisites:
    - "Risk-assessment data feeding the scoping decision [PWC-AT-2025]"
  risks_and_guardrails:
    - "ICAEW notes regulators have criticised firms for raising materiality levels to reduce scope without adequate justification; any tool-driven scoping would need to be justified (no AI link made in the source) [ICAEW-GROUP-2025]"
  human_checkpoints:
    - "none stated in the PwC source"
  role_evolution: "none stated."
  evidence_grade: C
  sources:
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraph beginning 'He added that PwC plans to soon have a tool'" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff update on outreach activities related to the integration of generative AI in audits and financial reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p. 4, list of potential areas" }
    - { ref: FIELDGUIDE-DEMO-2026, title: "See Field Agents execute internal audit engagements live", publisher: Fieldguide, type: vendor, url: "https://info.fieldguide.io/fieldguide-live-demo-internal-audit-mar17", date: 2026-10-20, access: full, locator: "paragraph 1 and bullet 'Scoping and risk assessment'" }
    - { ref: ICAEW-GROUP-2025, title: "Auditing groups: a risk-based approach to component scoping", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/aug-2025/auditing-groups-a-risk-based-approach-to-component-scoping", date: 2025-08-29, access: full, locator: "article body (context only; no AI content)" }
  last_reviewed: 2026-10-16
  notes: "No source on group-audit scoping mentions AI. The ICAEW and CPA Practice Advisor group-audit articles (and the ISA 600 shift to risk-based scoping) are context only. PCAOB staff material is from Jul 2024, a foundation source, and reports potential areas, not use."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Understand the entity and its environment** (industry, business model, regulation, systems, internal control, use of IT and AI). Research-synthesis and review-assurance.
  - Document reading is where most AI drafting lands: board minutes [FRC-GENAI-2026], walkthrough narratives [KPMG-CLARA-2025], media scanning [BBL-DELOITTE-2026], audit-committee communications [CFODIVE-PWC-2026].
  - New work created by client AI use: the AICPA practice aid says auditors should assess the extent to which an entity relies on AI in financial reporting at the start of the engagement, along with data quality, new risk types (data, model, hallucination, explainability, bias) and the team's capabilities [AICPA-PA-2026]. IFIAR adds that documents used as evidence may originate from AI systems and that auditors must watch for deliberate misuse of AI by entities [IFIAR-TTF-2026].
- **Risk assessment procedures** (inquiry, analytical procedures, observation, inspection, walkthroughs). Data-reporting and review-assurance. Whole-ledger analytics and scoring [CPAPA-ASKLUCA-2026; KPMG-CLARA-2024].
- **Identify and assess risks of material misstatement** at financial-statement and assertion level, and significant risks. Expert-judgment. Draft risk lists [CASEWARE-RSA-2026] and assertion-linked scoring [MINDBRIDGE-ARA-2026].
- **Fraud risk assessment and team brainstorming.** Expert-judgment and coordination. Practice evidence is limited to an internal-audit demonstration [VLGAA-NUCCIO-2026].
- **Materiality and performance materiality.** Expert-judgment and data-reporting. No practice evidence of AI setting it; one independent test shows variation across models [ICAEW-PIERPOINT-2025].
- **Scoping** (accounts, processes, locations, components). Expert-judgment. PwC's planned tool [PWC-AT-2025].
- **Overall strategy and plan, planning review.** Document-production and review-assurance [PWC-AT-2025; CASEWARE-VERITY-2026].
- **Budgeting, staffing, scheduling.** Coordination-scheduling [CAQ-RSM-2026].
- **Planning communications with those charged with governance.** Client-interaction. PwC's audit-committee tool [CFODIVE-PWC-2026].

### Common pain points

- Re-documenting walkthroughs and planning from prior-year files each year; PwC's AI assurance leader reports teams asking why they must repeat walkthroughs [PWC-AT-2025].
- Firms still struggle to move from reliance on prior-year workpapers to a risk-driven approach, citing training cost, documentation, planning time, senior involvement and client pushback [CPACOM-ATR-2025].
- Client data: surveyed US firms name poor client data (60%) and no access to client systems (53%) as top blockers [CPACOM-ATR-2025].
- IT-risk identification under ISA 315 in firms without IT specialists [ICAEW-315-2025].
- Disconnected tools between risk analytics, workpapers and methodology [MINDBRIDGE-ARA-2026; GT-GTAP-2026].
- Late discovery of unrisked variances (Caseware's framing of why planning review needs a second look) [CASEWARE-VERITY-2026].

### Metrics and benchmarks (with sources and provenance)

- IFIAR members frequently seeing automated tools in risk assessment: 55% of 47 members in 2024, 49% of 45 in 2023 (13% never and 32% infrequently in 2024) [IFIAR-TTF-2025]. Independent but directional; counts regulators, not audits.
- IFIAR 2026: GPPC networks collectively reported about 30% year-over-year growth in AI-enabled tools in 2025, with caveats on reporting practice [IFIAR-TTF-2026].
- IFIAR 2024: 31% of members reported findings that a tool was not used as intended, up from 29% in 2023; common findings were misreading results and limited testing of outliers [IFIAR-TTF-2025]. Not specific to risk assessment.
- US firms (54 with complete data): 22% have an automated solution for risk assessment, 19% for data ingestion, 11% for substantive analytics, 22% have none; 39% have workflow management [CPACOM-ATR-2025]. Firms furthest along spend the highest share of time in planning [CPACOM-ATR-2025].
- Caseware (vendor-published): 94% accuracy on golden-dataset items from beta traces; 15-20 minutes to under two for indicative workflows [CASEWARE-LAUNCH-2026].
- PwC (self-reported): time savings "not that drastic yet" in the first busy season of enterprise tools [CFODIVE-PWC-2026].
- EisnerAmper (vendor-published): 1,100+ professionals and 1,500+ engagements on DAS [CASEWARE-EISNERAMPER-2026]. Platform adoption, not AI effect.
- Research: UMAR AUROC 0.782, PR-AUC 0.341, ECE 0.052 on 3,200 10-K firm-years [ARXIV-UMAR-2026]. FinancialAuditBench: 90 tasks, 11 frontier models [ARXIV-FAB-2026].
- Usage surveys: 81% of tax and audit professionals use AI regularly; over one-third admit using unauthorised tools [TRI-FOP-2026].

### Guardrails and regulatory points

- **FRC guidance (30 Mar 2026).** Names risks of deficient output, misuse of output and non-compliant methodology, with a worked example for board-minutes summarisation (certification, prompt library, human review, training on automation bias) [FRC-GENAI-2026]. The guidance warns that an auditor may misread an AI-enabled risk-assessment output as a conclusion rather than an input to judgment [FRC-GENAI-2026].
- **IFIAR.** Encourages firms to monitor tool use and quality impact, notes unclear network versus member-firm responsibility for monitoring [IFIAR-TTF-2025], and in 2026 stresses governance, oversight, ethics and over-reliance [IFIAR-TTF-2026].
- **AICPA practice aid (13 Oct 2026).** Two parts: entity AI use and firms' own AI use. A deeper treatment of risk of material misstatement and audit evidence is promised later [AICPA-PA-2026; JOFA-AIPA-2026]. An earlier AICPA practice aid (Aug 2023 RSM summary) covers automated tools in risk assessment under AU-C 315 [RSM-AICPATECH-2023].
- **PCAOB staff (Jul 2024).** Firms did not see PCAOB standards as impediments; some barred GenAI on audit procedures for privacy and reliability reasons [PCAOB-GENAI-2024].
- **IAASB.** Exposure drafts of ISA 330, 500 and 520 (comments due 15 Dec 2026) address technology; the ISA 520 PDF text layer could not be read, so its risk-assessment relevance was not checked [IAASB-EDPAGE-2026].
- **Vendor positions.** Every vendor and firm source says outputs are citation-backed or traceable and that the auditor decides [CASEWARE-RSA-2026; MINDBRIDGE-ARA-2026; OPTRO-CRX-2026; GT-GTAP-2026].

### Frontier signals (dated and sourced)

- 2026-10-20: Fieldguide schedules a demo of agents mapping and scoring risks at internal audit scoping [FIELDGUIDE-DEMO-2026].
- 2026-10-14: Optro announces Agentic Risk Assessment Scoring [OPTRO-CRX-2026].
- 2026-10-13: AICPA practice aid issued; risk of material misstatement guidance planned [AICPA-PA-2026].
- 2026-10-08: PKF O'Connor Davies joins a programme to co-develop its own agents on Caseware's platform [CASEWARE-PKF-2026].
- 2026-10-06: Caseware's Risk Suggestion Agent launches worldwide [CASEWARE-RSA-2026].
- 2026-09-22: MindBridge announces Agentic Risk Assessment [MINDBRIDGE-ARA-2026].
- 2026-06-24 and 2026-06-29: Deloitte unifies agents in Omnia [DELOITTE-OMNIA-2026; BBL-DELOITTE-2026].
- 2026-05-07: Grant Thornton launches gtap [GT-GTAP-2026].
- 2026-04-07: EY embeds multi-agent framework in EY Canvas, end-to-end support expected by 2028 [EY-CANVAS-2026].
- 2026-04-01: KPMG says it will pilot orchestration agents from summer 2026 [BBL-KPMG-2026].
- 2025-10-28: PwC plans a risk-assessment tool, a tool for each audit step in 2026, and a global agentic platform about 18 months after [PWC-AT-2025].

### Workforce and role effects

- PwC is hiring engineers it would not have hired into assurance and hopes for dual-track CPA and data-science entrants [PWC-AT-2025].
- Caseware beta partners describe tasks going from hours to minutes, with in-context guidance acting as a learning aid for juniors [CASEWARE-VERITY-2026]. Citrin Cooperman's innovation leader makes the same point about reasoning being visible [CASEWARE-CITRIN-2026].
- Deloitte adds a tutor mode with on-demand micro-training in the flow of work [DELOITTE-OMNIA-2026].
- Planning staff move from drafting toward reviewing AI drafts (FRC example requires a reviewer who reads the source) [FRC-GENAI-2026].
- Thomson Reuters Institute urges firms to define early-career roles and keep supervision before automation erodes development [TRI-FOP-2026].
- Vendors are recruiting audit practitioners: Fieldguide's Agent Architect and Audit Engineer postings ask for end-to-end audit experience including planning and risk assessment [FIELDGUIDE-JOB-2026; FIELDGUIDE-JOB-ENG-2026], and Clark's Audit Engineer role manages customer workflow discovery and adoption [CLARK-JOB-2026].
- RSM's staffing tool changes how leaders plan and deploy people [CAQ-RSM-2026].

### Objections and concerns practitioners raise

- Chatbots cannot do inquiry, observation or inspection; model-to-model variation in risks and materiality shows judgment cannot be handed off [ICAEW-PIERPOINT-2025].
- Automation bias and fluent, confident wrong answers [FRC-GENAI-2026]; over-reliance without challenge [IFIAR-TTF-2026].
- Risk of misusing a partial summary as a complete one [FRC-GENAI-2026].
- Data privacy limits on what may be uploaded; some firms bar GenAI on audit procedures [PCAOB-GENAI-2024].
- Gains are real but small so far [CFODIVE-PWC-2026]; vendor time-saving figures lack published method (no independent test found).
- Staff use of unapproved tools [TRI-FOP-2026].
- Cost and change management for smaller firms [CPACOM-ATR-2025].

### Interview probes (for an advisor to ask someone in this module)

1. Which planning outputs now start from an AI draft (risk list, planning document, walkthrough narrative, board-minutes summary), and do you record how often reviewers change or reject what the tool proposed?
2. What do you put on the file to show a person reviewed an AI-suggested risk, and what have inspectors or quality reviewers asked about it?
3. Has planning time, budget or staffing mix changed since these tools arrived, and who decided how to rebase fees or hours?
4. What client data do you actually get at planning (trial balance, ledger, minutes), and how often does lack of access stop you using analytics?
5. How are juniors learning risk assessment now that drafts arrive pre-written, and has the manager or partner planning review changed?

---

## 4. Routed to other modules

- **completion-reporting:** Caseware's Disclosure Checklist Agent (2.7 hours saved per run on average in beta, vendor-published; run time about 18 minutes down to two to three; UK availability on 6 Oct 2026) [CASEWARE-VERITY-2026; ITBRIEF-CASEWARE-2026]. KPMG's Financial Report Analyzer for disclosure checklists [KPMG-CLARA-2025]. FinancialAuditBench workpaper tasks [ARXIV-FAB-2026].
- **substantive-testing:** KPMG expense-vouching and unrecorded-liability agents, and KPMG's orchestration pilots for physical-asset valuation and revenue-process testing [KPMG-CLARA-2025; BBL-KPMG-2026]. PwC Evidence Match and Audit Innovation Hub [PWC-AT-2025]. AuditCopilot, LLM anomaly detection in journal entries on synthetic and anonymised real ledgers [ARXIV-AUDITCOPILOT-2025]. Journal-entry testing prevalence (88% in 2024) [IFIAR-TTF-2025].
- **controls-testing:** KPMG agents planned for controls testing [KPMG-CLARA-2025]. Reddit's internal audit automating 175 controls and cutting testing time per control by 60% on average (vendor release) [OPTRO-CRX-2026]. Klaviyo and FJ Management quotes in the same release [OPTRO-CRX-2026].
- **quality-management:** RSM Ask Luca, a firm-approved-guidance copilot used by 4,000-plus assurance professionals [CPAPA-ASKLUCA-2026]. IFIAR's monitoring-responsibility point between networks and member firms [IFIAR-TTF-2025].
- **specialists (IT audit) and other-assurance (assurance over AI):** the AICPA practice aid's treatment of entity AI use and AI-operated controls [AICPA-PA-2026]. EY's AI assurance services launched alongside its Canvas agents [EY-CANVAS-2026]. The ISA 315 IT-risk viewpoint [ICAEW-315-2025].
- **acceptance-independence / audit business model:** Clark's claim that AI performs audit fieldwork for more than 35 CPA firms [CLARK-JOB-2026]; Fieldguide's $75M raise and BDO tie-up [SILICONANGLE-FIELDGUIDE-2026; BDO-FIELDGUIDE-2026]; Grant Thornton's platform build [GT-GTAP-2026].

---

## 5. Sources

| # | Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|---|
| 1 | EY-CANVAS-2026 | EY launches enterprise-scale agentic AI to redefine the audit experience for the AI era | EY | firm | https://www.ey.com/en_ca/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era | 2026-04-07 | full |
| 2 | KPMG-CLARA-2024 | KPMG announces AI integration into global smart audit platform, KPMG Clara | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2024/07/kpmg-announces-ai-integration-into-global-smart-audit-platform-kpmg-clara.html | 2024-07-29 | full |
| 3 | KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG US (Newsfile Corp.) | firm | https://www.newsfilecorp.com/release/249535/KPMG-Advances-AI-Integration-in-KPMG-Clara-Smart-Audit-Platform | 2025-04-23 | full |
| 4 | BBL-KPMG-2026 | KPMG to test advanced AI agents in next phase for audits | Bloomberg Law | press | https://news.bloomberglaw.com/financial-accounting/kpmg-to-test-advanced-ai-agents-in-next-phase-for-audits | 2026-04-01 | full (opening section only) |
| 5 | DELOITTE-OMNIA-2026 | Deloitte unveils connected agentic intelligence in Omnia | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 | full |
| 6 | BBL-DELOITTE-2026 | Deloitte adopts advanced AI to power corporate audits globally | Bloomberg Law | press | https://news.bloomberglaw.com/financial-accounting/deloitte-adopts-advanced-ai-to-power-corporate-audits-globally | 2026-06-29 | full |
| 7 | PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 | full |
| 8 | CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 | full |
| 9 | GT-GTAP-2026 | Grant Thornton launches gtap | Grant Thornton LLP | firm | https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us | 2026-05-07 | full |
| 10 | CPAPA-GT-2026 | Grant Thornton U.S. launches in-house audit transformation platform | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/08/grant-thornton-u-s-launches-in-house-audit-transformation-platform/183107/ | 2026-05-08 | full |
| 11 | CAQ-RSM-2026 | Shaping the future of assurance: Advancing AI in the audit | Center for Audit Quality (RSM author) | professional-body | https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit | 2026-08-25 | full |
| 12 | CPAPA-ASKLUCA-2026 | RSM US rolls out 'Ask Luca' GenAI tool for firm's auditors | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/01/09/rsm-us-rolls-out-ask-luca-genai-tool-for-firms-auditors/176104/ | 2026-01-09 | full |
| 13 | RSM-LUCA-2026 | RSM Luca: our dynamic digital audit ecosystem | RSM US | firm | https://rsmus.com/services/audit-services/ai-digital-audit-technology.html | 2026-10-16 (living page, accessed; no publication date shown) | full |
| 14 | MINDBRIDGE-ARA-2026 | MindBridge advances financial oversight for the agentic era | MindBridge (Business Wire via BNN Bloomberg) | vendor | https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/ | 2026-09-22 | full |
| 15 | CPAPA-MINDBRIDGE-2026 | MindBridge launches new AI capabilities for finance and audit | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=190850 | 2026-09-30 | full |
| 16 | CASEWARE-LAUNCH-2026 | Caseware launches Verity to bring workflow-native AI agents directly into assurance engagements | Caseware | vendor | https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements | 2026-05-20 | full |
| 17 | CASEWARE-VERITY-2026 | CwX 2026: How agentic AI is transforming audit and assurance | Caseware | vendor | https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance | 2026-06-17 | full |
| 18 | CASEWARE-AIDA-2026 | From AiDA to agentic: How Caseware's AI has evolved | Caseware | vendor | https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved | 2026-07-28 | full |
| 19 | CASEWARE-RSA-2026 | Verity-powered Risk Suggestion Agent launches | Caseware | vendor | https://www.caseware.com/news/caseware-verity-powered-risk-suggestion-agent-launches-to-help-auditors-identify-engagement-specific-risks | 2026-10-06 | full |
| 20 | ITBRIEF-CASEWARE-2026 | Caseware launches AI agents for audit risk and disclosure | IT Brief UK | press | https://itbrief.co.uk/story/caseware-launches-ai-agents-for-audit-risk-disclosure | 2026-10-13 | full |
| 21 | CASEWARE-EISNERAMPER-2026 | EisnerAmper leverages DAS powered by Caseware | Caseware | vendor | https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice | 2026-06-25 | full |
| 22 | CASEWARE-CITRIN-2026 | Citrin Cooperman adopts AI-enabled DAS suite | Caseware | vendor | https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth | 2026-07-13 | full |
| 23 | CASEWARE-PKF-2026 | PKF O'Connor Davies adopts DAS suite powered by Verity | Caseware | vendor | https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program | 2026-10-08 | full |
| 24 | SILICONANGLE-FIELDGUIDE-2026 | Fieldguide raises $75M on $700M valuation | SiliconANGLE | press | https://siliconangle.com/2026/02/02/fieldguide-raises-75m-700m-valuation-scale-agentic-ai-audit-advisory-firms/ | 2026-02-02 | full |
| 25 | BDO-FIELDGUIDE-2026 | BDO expands AI use in risk advisory through Fieldguide tie-up | International Accounting Bulletin (via Yahoo Finance) | press | https://finance.yahoo.com/sectors/technology/articles/bdo-expands-ai-risk-advisory-113450007.html | 2026-03-25 | full |
| 26 | FIELDGUIDE-DEMO-2026 | See Field Agents execute internal audit engagements live | Fieldguide | vendor | https://info.fieldguide.io/fieldguide-live-demo-internal-audit-mar17 | 2026-10-20 (scheduled webinar) | full |
| 27 | FIELDGUIDE-JOB-2026 | Agent Architect, Audit (job posting) | Fieldguide (via Built In Boston) | job-posting | https://www.builtinboston.com/job/agent-architect-audit/10693122 | 2026-10-16 (accessed; no posting date shown) | full |
| 28 | FIELDGUIDE-JOB-ENG-2026 | Audit Engineer (job posting) | Fieldguide (via Simplify) | job-posting | https://simplify.jobs/p/8ef72a02-994d-4b53-929f-b83e353d753e/Audit-Engineer | 2026-10-16 (accessed; no posting date shown) | full |
| 29 | CLARK-JOB-2026 | Audit Engineer (job posting) | Clark (via Built In NYC) | job-posting | https://www.builtinnyc.com/job/audit-engineer/11352965 | 2026-10-16 (accessed; no posting date shown) | full |
| 30 | OPTRO-CRX-2026 | Optro launches domain-trained agents for audit, compliance, third-party risk and AI governance | Optro | vendor | https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance | 2026-10-14 | full |
| 31 | FRC-GENAI-2026 | Generative and Agentic AI Guidance | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full |
| 32 | FRC-NEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 | full |
| 33 | IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution | IFIAR (FSA Japan copy) | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 | full |
| 34 | IFIAR-TTF-2026 | Use of technology in audits: Innovation and audit quality | IFIAR (FSA Japan copy) | regulator | https://www.fsa.go.jp/ifiar/2026TTFReport.pdf | 2026-04-20 | full |
| 35 | PCAOB-GENAI-2024 | Spotlight: Staff update on outreach activities related to integration of generative AI in audits | PCAOB staff | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 | full |
| 36 | AICPA-PA-2026 | AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing | AICPA and CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full (release only; practice aid is member-only) |
| 37 | JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 | full |
| 38 | RSM-AICPATECH-2023 | AICPA issues practice aid on use of technology during risk assessment | RSM US | firm | https://rsmus.com/insights/financial-reporting/aicpa-issues-practice-aid-use-technology-during-risk-assessment.html | 2023-08-11 | full (summary of the AICPA document; foundation) |
| 39 | IAASB-EDPAGE-2026 | Proposed revisions: audit evidence and risk response (ISA 330, 500, 520) | IAASB | standard-setter | https://www.iaasb.org/publications/proposed-revisions-audit-evidence-risk-response-isa-330-isa-500-isa-520 | 2026-08 | full (landing page; ED-520 PDF text unreadable) |
| 40 | ICAEW-PIERPOINT-2025 | Testing Gen AI platforms: can they do audit work? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09-24 | full |
| 41 | ICAEW-315-2025 | Meeting ISA 315 requirements without specialist IT teams | ICAEW (vendor author) | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/oct-2025/meeting-isa-315-requirements-without-specialists-it-teams | 2025-10 | full |
| 42 | ICAEW-GROUP-2025 | Auditing groups: a risk-based approach to component scoping | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/aug-2025/auditing-groups-a-risk-based-approach-to-component-scoping | 2025-08-29 | full |
| 43 | CPAPA-GROUP-2026 | Group audits: why complexity persists and why judgment still matters most | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/15/group-audits-why-complexity-persists-and-why-judgment-still-matters-most/183479/ | 2026-05-15 | full |
| 44 | CPACOM-ATR-2025 | 2025 Audit Transformation Report | CPA.com (AICPA) | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| 45 | TRI-FOP-2026 | What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full |
| 46 | ARXIV-UMAR-2026 | Multi-Agent Framework for Audit Risk Assessment with Explicit Uncertainty and Evidence Conflict Modeling | arXiv | academic | https://arxiv.org/abs/2606.15640 | 2026-06-14 | full (abstract) |
| 47 | ARXIV-FAB-2026 | FinancialAuditBench | arXiv | academic | https://arxiv.org/abs/2609.32835 | 2026-09-26 | full (abstract) |
| 48 | ARXIV-AUDITCOPILOT-2025 | AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping | arXiv | academic | https://arxiv.org/abs/2512.02726 | 2025-12-02 | full (abstract) |
| 49 | ICAEW-POD-2025 | How should audit firms use AI? (Beyond Finance) | ICAEW | podcast | https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai | 2025-11 | full (show notes only; no transcript read) |
| 50 | SRA-SWARM-2026 | How AI agents are transforming internal audit (Speaking of Risk and Audit) | Richard Chambers and Associates | podcast | https://SRApodcast.podbean.com/e/swarm-auditing-how-ai-agents-are-transforming-internal-audit/ | 2026-02-11 | full (episode blurb only) |
| 51 | VLGAA-NUCCIO-2026 | Using Generative AI in Internal Audit (slides) | Virginia Local Government Auditors Association | conference | https://vlgaa.starchapter.com/images/downloads/Documents/day_1___2___using_generative_ai_in_internal_audit___d._nuccio.pdf | 2026-04 (PDF creation date) | full |

**Count by type (51 sources):** press 12, vendor 10, firm 7, regulator 5, professional-body 4, job-posting 3, academic 3, standard-setter 2, survey 2, podcast 2, conference 1, community 0.

**Source notes.**
- EY-CANVAS-2026 and KPMG-CLARA-2025 use the same refs as the landscape file. I read EY's own release rather than the secondary report the landscape used.
- The KPMG release is dated 23 Apr 2025 on Newsfile; the landscape file says 22 Apr.
- The EY Canada page carries JSON-LD dates of 7 and 10 Apr 2026; the 7 Apr date matches the trade-press coverage.
- Grade rules were applied by source tense: present-tense use claims by a named firm give B; "will be using" or "plans" give C or maturity "announced".

---

## 6. Gaps

- **No independent quality measure.** No tool-accuracy study, override rate, parallel-run result or inspection finding specific to AI in planning or risk assessment was found. The only independent measures are IFIAR's prevalence counts, the CPA.com survey and one ICAEW test on fictional data. The one named-firm effect statement (PwC: modest time savings so far) is qualitative [CFODIVE-PWC-2026].
- **No override or acceptance data** for AI-suggested risks from any vendor or firm, including Caseware's Risk Suggestion Agent.
- **PwC's risk-assessment tool.** Described as coming soon in Oct 2025; the Oct 2026 CFO Dive article does not name it, so its status is unconfirmed [PWC-AT-2025; CFODIVE-PWC-2026].
- **KPMG.** The primary KPMG announcement of orchestration pilots (Apr 2026) was not read (only the opening of a paywalled Bloomberg Law page; a Going Concern copy returned 403). No KPMG statement on risk-assessment agents specifically was found beyond Jul 2024 and Apr 2025.
- **EY.** The release states "improve risk assessments" but no source describes which Canvas agents work on planning.
- **MindBridge.** Named customer case studies (for example Cherry Bekaert) returned 403 or were seen only in search results; a customer-marked whitepaper was reachable but excluded.
- **Materiality, group-audit scoping, fraud brainstorming (external audit).** No firm, regulator or standard-setter evidence of AI use in practice. Group-audit articles read contain no AI content.
- **Internal audit named cases.** PayPal "swarm auditing" (podcast blurb only), Uniper ChatGPT study (bibliographic page only), Microsoft Internal Audit and Optro customers beyond the CRX release were not retrieved. Planned searches for these did not run when the shared web-search quota was exhausted.
- **Job postings.** Only vendor-side roles (Fieldguide, Clark) were found. No Big Four or mid-tier firm posting that reveals planning-stage AI use was retrieved, and no posting dates are shown on the pages read.
- **Conference sessions** (Deloitte/KU Auditing Symposium, AAA midyear junior-auditor panel, ICAEW AuditBot session) were listed in the landscape but their pages were not opened here; only one practitioner slide deck was read.
- **Community discussion.** None opened (Reddit is blocked; no other forum read).
- **Standards text.** The ED-520 PDF has no readable text layer, so its application material on analytics in risk assessment was not checked. The AICPA practice aid full text is member-only; only the release and JofA coverage were read. ISA 315 (Revised 2019) and AS 2110 were not re-read.
- **IFIAR 2026 figures.** The 2025 risk-assessment frequency is shown only as a chart without data labels; no exact number is stated here.
- **Preprint on ISA 240 and AI** (preprints.org) returned 403 and appears in search results only; it is not used.
- **Dates.** The ICAEW articles show a month only or no day on the page; the ICAEW podcast date (Nov 2025) is from the page's neighbouring-episode links and the landscape file. The CAQ blog date (25 Aug 2026) comes from the page.
