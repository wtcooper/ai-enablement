# Advisory / risk-controls / discourse: what practitioners are saying

Run date: 2026-10-20. Wave 5. Archetype: `advisory`. Module: `risk-controls`. Angle: discourse.

Conventions: refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape file's refs where the document is the same. `access: full` means the page or PDF was opened and read. `access: search-only` means seen only in search results. Quotations are under 25 words. Provenance of every figure is marked `self-reported`, `vendor-published` or `independent`.

---

## 1. Summary

**What the discourse says.** In the last 12 months the risk-controls conversation has moved from "should we use genAI?" to "how do we scale it, prove it, and govern it?". The recurring points are consistent across firms, the IIA, analysts and practitioner communities:

1. **Use is near-universal, embedding is not.** Gartner's webinar poll of 743 audit professionals found 93% report some AI use and 38% an AI strategy (ACCTIMES-GARTNER-2026). Sikich's survey of 222 US audit leaders (fieldwork Jul 24 to Aug 19, 2026) found 90% use AI in the audit function (SIKICH-IAPRIORITIES-2026). KPMG's April 2026 webcast poll of about 3,900 audit and risk leaders describes SOX and internal audit AI as early stage and concentrated in planning and analysis, with limited use in testing (KPMG-REVCONTROLS-2026).
2. **Work is moving first where drafting and organizing happen**: risk and control matrices, test procedures, document request lists, observation language, scope challenge. Named firms (RSM, Baker Tilly, Cherry Bekaert, Aprio) describe these. Control-test workpaper preparation by an agent is described as live at RSM (ACCTODAY-RSMBEACON-2026). No firm publishes accuracy, override or parallel-run figures.
3. **Reliance is the open question.** Practitioner communities report that external auditors will not rely on pure AI output and that most are undecided about reliance on AI-executed internal audit testing (IAC-SOXRELIANCE-2026, informal poll, sample size not stated). PCAOB reliance rules are described as unchanged, with their application to AI still being worked out engagement by engagement.
4. **Governing client AI is the new advisory line.** COSO's February 2026 publication on internal control over generative AI is the anchor (COSO-GENAI-2026, DELOITTE-COSO-2026). Grant Thornton Advisors' CEO says AI is already driving demand for AI governance work and expects more (GT-CBIZ-2026). RSM's survey of 1,030 middle-market leaders reports 67% apply AI governance controls before pilot or production (RSM-MMAI-2026).
5. **Audit functions assess "safe" AI more than "effective" AI.** Of Sikich respondents auditing AI, 53% review operational effectiveness, 40% ethical use and bias, and 36% model validation (SIKICH-IAPRIORITIES-2026, p.30).
6. **Roles are shifting toward controls adviser and AI supervisor**, with a talent squeeze: 82% of Sikich respondents use external partners (60% of those cite access to specialized skills), and private organizations saw internal audit staff cuts rise from 11% to 28% (IIA-PULSE-2026).

**Quality evidence.** Absent. There is no published error rate, override rate, parallel-run result or independent measurement of AI-assisted internal audit or SOX work. The nearest items are qualitative (RSM's user-acceptance-testing observations on its RCM agent), self-defined ROI (82% of Sikich AI users say targeted ROI is achieved, with respondents defining ROI themselves), and an informal poll on external-auditor reliance. Gartner reports 54% of CAEs have not started measuring AI value (HELPNET-GARTNER-2026).

**Grades.** No entry earns A. Six entries are B, ten are C and two are D (ideas).

---

## 2. Use cases

```yaml
- id: advisory-risk-controls-01
  title: AI first draft of risk and control matrices from process documents
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Building a risk and control matrix (RCM) from notes, flowcharts and architecture diagrams takes an auditor days at the start of an internal audit or SOX readiness engagement."
  solution: "An agent (reached through a chat interface such as Microsoft Teams) reads uploaded process documents, identifies process areas, risks and controls, and populates an RCM-format draft with control reference, type and frequency. The auditor reviews, corrects and confirms details with the auditee before testing starts."
  outcomes:
    - lever: speed
      description: "RSM director says the agent produces a first draft in minutes for work that typically takes one to two days."
      figure: "minutes versus one to two days"
      measures: "Time to a first-draft RCM from uploaded process documents, agent versus typical manual effort, as stated by an RSM director in a webinar write-up; not a tracked metric"
      provenance: self-reported
      source_ref: RSM-AGENTICIA-2025
    - lever: quality
      description: "During user acceptance testing the agent sometimes used individual names instead of roles and combined multiple controls into one, so human review is required."
      figure: "none published"
      measures: "Qualitative observation from user acceptance testing; no error rate given"
      provenance: self-reported
      source_ref: RSM-AGENTICIA-2025
  prerequisites:
    - "Process documentation in a form the agent can read (narratives, flowcharts, architecture diagrams)"
    - "A secure enterprise environment; RSM says agents should operate inside the enterprise security framework"
    - "Formal approvals for changes to the agent workbench and user training on its limits"
  risks_and_guardrails:
    - "Human-in-the-loop review of every RCM draft before the testing phase (RSM-AGENTICIA-2025, section on RCMs)"
    - "Auditors confirm details with auditees; output quality depends on input quality (RSM-AGENTICIA-2025, governance section)"
  human_checkpoints:
    - "Auditor reviews and refines the RCM, then confirms with auditees, before testing"
  role_evolution: "RSM describes treating the agent like a digital employee that can make intern-like mistakes, so the auditor moves from drafting to supervising and validating (RSM-AGENTICIA-2025, section on mindset)."
  evidence_grade: B
  sources:
    - { ref: RSM-AGENTICIA-2025, title: "Reimagine internal audit with agentic AI to drive value", publisher: RSM US, type: firm, url: "https://rsmus.com/insights/services/digital-transformation/agentic-ai-for-internal-audit.html", date: 2025-12-22, access: full, locator: "Section 'Creating risk and control matrices' and 'Agentic AI solutions and use cases'" }
    - { ref: IIA-CAEBULLETIN-2026, title: "CAE Bulletin Issue: January 20, 2026 (RSM item on agentic AI)", publisher: The IIA, type: professional-body, url: "https://www.theiia.org/en/content/newsletter/cae-bulletin/cae-bulletin-issue-january-20-2026/", date: 2026-01-20, access: full, locator: "First item, RSM summary" }
  last_reviewed: 2026-10-20
  notes: "Firm type: RSM US, top-10 US firm with a middle-market focus. Independence: internal audit outsourcing is restricted for a firm's own SEC audit clients (general background, unverified in this run; confirm against SEC, AICPA and PCAOB rules). The article date 2025-12-22 is the date printed on the RSM page; the IIA bulletin of 2026-01-20 calls it recently published. Grade B because the speed figure is a director's statement, not a tracked metric. Maturity is piloting because the source describes user acceptance testing, not production use."

- id: advisory-risk-controls-02
  title: Agent-drafted test procedures, sample sizes and document request lists
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "After the RCM is agreed, writing design and operating-effectiveness test steps, choosing sample sizes and listing the evidence to request from control owners is repetitive manual work."
  solution: "The agent reads each control description and generates step-by-step test procedures, applies a sampling methodology to population sizes, and produces a document request list naming the reports, reconciliations and approvals needed."
  outcomes:
    - lever: capacity
      description: "RSM director says that when inputs are reviewed first, the agent saves auditors several hours of manual work."
      figure: "several hours"
      measures: "Manual hours saved per set of test procedures and document requests, as stated by an RSM director; not a tracked metric"
      provenance: self-reported
      source_ref: RSM-AGENTICIA-2025
  prerequisites:
    - "Accurate control descriptions and data fields before prompting the agent"
    - "An approved sampling methodology the agent can apply"
  risks_and_guardrails:
    - "RSM says auditors must verify control descriptions and data fields before the agent builds testing strategies (RSM-AGENTICIA-2025, section 'Testing strategy and generating document request lists')"
  human_checkpoints:
    - "Auditor reviews procedures and request list before issue to control owners"
  role_evolution: "Auditors spend less time translating control text into test steps and more time on verification and on follow-up with control owners (RSM-AGENTICIA-2025)."
  evidence_grade: B
  sources:
    - { ref: RSM-AGENTICIA-2025, title: "Reimagine internal audit with agentic AI to drive value", publisher: RSM US, type: firm, url: "https://rsmus.com/insights/services/digital-transformation/agentic-ai-for-internal-audit.html", date: 2025-12-22, access: full, locator: "Section 'Testing strategy and generating document request lists (DRLs)'" }
  last_reviewed: 2026-10-20
  notes: "Firm type: RSM US, top-10 US firm with a middle-market focus. Webinar write-up; the source does not say how many engagements used the agent. The article lists 'testing and validation agents' and 'remediation management agents' only as additional opportunities, not as live."

- id: advisory-risk-controls-03
  title: Agent reads evidence, tests each control attribute and prepares a review-ready workpaper
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Preparing control-test workpapers means reading evidence files (Excel workbooks with embedded files, screenshots, tick marks), allocating evidence to samples and testing each attribute by hand."
  solution: "RSM Beacon takes the control description, attributes and evidence; allocates evidence to samples; tests each attribute; and writes an annotated workpaper with a reasoning log. Ambiguous items go to a human as open items. Tests run in the background so auditors can queue several controls, then review."
  outcomes:
    - lever: capacity
      description: "No figures published. The article says the platform is live and in use by RSM professionals and covers high-volume, multi-sample controls."
      figure: "none published"
      measures: "No time, accuracy or override measure published"
      provenance: self-reported
      source_ref: ACCTODAY-RSMBEACON-2026
  prerequisites:
    - "Control description, testing attributes and evidence files; optional prior-year workpapers and policies for context"
    - "RSM's own testing methodology embedded in the platform; Andera's technology integrated into RSM's audit platform"
  risks_and_guardrails:
    - "The AI does not make judgment calls; anything ambiguous is flagged for a human (ACCTODAY-RSMBEACON-2026, paragraph on the agent workflow)"
    - "Reviewers see the full reasoning log beside the evidence"
    - "RSM states client data in Beacon is segregated from Andera's commercial product and not used to train it"
  human_checkpoints:
    - "Auditor reviews AI conclusions, resolves open items and applies professional judgment"
  role_evolution: "Auditors move from preparing workpapers to queuing controls and reviewing completed ones (ACCTODAY-RSMBEACON-2026)."
  evidence_grade: B
  sources:
    - { ref: ACCTODAY-RSMBEACON-2026, title: "RSM launches AI-guided internal audit platform 'Beacon' with Andera", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/rsm-launches-ai-guided-internal-audit-platform-beacon-with-andera", date: 2026-08-28, access: full, locator: "Paragraphs 2 to 5 and closing paragraph" }
  last_reviewed: 2026-10-20
  notes: "Firm type: RSM US, top-10 US firm with a middle-market focus, with a vendor partner (Andera). RSM says it is evaluating Beacon for SOC, NIST, PCI and operational audits beyond SOX; that extension is not live per the source. Independence: internal audit outsourcing is restricted for a firm's own SEC audit clients (unverified general background). Trade-press report of a firm announcement, so no independent confirmation of use."

- id: advisory-risk-controls-04
  title: Agentic information-request management and completeness checks in co-sourced audits
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Repeated, loosely worded information requests and long waits for data add friction for process owners and slow internal audit fieldwork."
  solution: "In a co-sourced billing and collections audit, Baker Tilly used an AI platform's agents to prepare and organize information requests, link them to audit objectives and track status. Another agent reviews responses for completeness and alerts the business owner if more data is needed, and approved agents then support defined testing steps where source data is structured."
  outcomes:
    - lever: speed
      description: "Baker Tilly says AI reduced coordination and processing time and improved testing coverage on the engagement."
      figure: "none published"
      measures: "No quantity published; the article lists request turnaround, duplicate requests, cycle time and population coverage as measures to define, not results"
      provenance: self-reported
      source_ref: BAKERTILLY-AIIA-2026
  prerequisites:
    - "An engagement platform that holds requests, documents, walkthroughs, risks, controls, population references, testing and sign-off together"
    - "Confirmed completeness and accuracy of populations before AI testing"
  risks_and_guardrails:
    - "Team confirms population completeness and accuracy, reviews AI results, inspects supporting records and decides whether exceptions are isolated or systemic (BAKERTILLY-AIIA-2026, client example)"
    - "Retain approved procedure, source information, AI output, exceptions, review and sign-off (BAKERTILLY-AIIA-2026, closing lessons)"
  human_checkpoints:
    - "Auditor remains responsible for procedure, evidence, analysis and conclusion"
  role_evolution: "Baker Tilly says freed time goes to business context, root cause and practical recommendations; the engagement stays auditor-led (BAKERTILLY-AIIA-2026)."
  evidence_grade: B
  sources:
    - { ref: BAKERTILLY-AIIA-2026, title: "Start with stakeholder value when using AI in internal audit", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/ai-in-internal-audit", date: 2026-09-08, access: full, locator: "Section 'A client example: Billing and collections'" }
    - { ref: IIA-UPSKILL-2026, title: "Internal Audit Upskilling for Critical AI Capabilities", publisher: The IIA, type: professional-body, url: "https://www.theiia.org/en/content/articles/global-best-practices/2026/internal-audit-upskilling-for-critical-ai-capabilities/", date: 2026-07-22, access: full, locator: "Section 'Internal Audit and Agentic AI' (John Romano, Baker Tilly)" }
  last_reviewed: 2026-10-20
  notes: "Firm type: Baker Tilly, large US accounting and advisory firm (US ranking not checked in this run). The platform is named in the Baker Tilly article as Fieldguide. The client is not named. Independence: co-sourced internal audit is restricted for a firm's own SEC audit clients (unverified general background). The IIA article date (2026-07-22) is the date printed on the page."

- id: advisory-risk-controls-05
  title: AI challenge reviews of audit scope, risk-control mapping and draft findings
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Scope, risk-control mapping and draft findings are reviewed late and by whoever has time; gaps in risk themes or unsupported findings can reach the client."
  solution: "Baker Tilly uses approved custom GPTs as structured challenge tools: review a proposed scope for missing risk themes, question whether a risk-control mapping is complete, compare planned procedures with objectives, and test whether a draft finding is supported by the work performed."
  outcomes:
    - lever: quality
      description: "No measure published. The firm says the output is a challenge record, not audit evidence, and does not set risk ratings."
      figure: "none published"
      measures: "No error, gap-found or override measure published"
      provenance: self-reported
      source_ref: BAKERTILLY-AIIA-2026
  prerequisites:
    - "Approved tools and data sources only"
    - "Proprietary prompts and an audit methodology to challenge against"
  risks_and_guardrails:
    - "Output does not become audit evidence, determine a risk rating or replace reviewer judgment (BAKERTILLY-AIIA-2026, section on controls around AI-supported work)"
    - "Validate generated content against source evidence and correct or reject unsupported output"
  human_checkpoints:
    - "Assigned auditor owns the procedure, evidence and conclusion; reviewer judgment is unchanged"
  role_evolution: "Reviewers get a structured second look before sign-off; accountability stays with the named auditor (BAKERTILLY-AIIA-2026)."
  evidence_grade: B
  sources:
    - { ref: BAKERTILLY-AIIA-2026, title: "Start with stakeholder value when using AI in internal audit", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/ai-in-internal-audit", date: 2026-09-08, access: full, locator: "Section beginning 'At Baker Tilly, Fieldguide ...' and 'We also use approved custom GPTs'" }
    - { ref: ACCTIMES-GARTNER-2026, title: "Audit teams' AI use common but most lack strategy", publisher: Accounting Times, type: press, url: "https://www.accountingtimes.com.au/profession/audit-teams-ai-use-common-but-most-lack-strategy", date: 2026-08-16, access: full, locator: "Paragraph on use cases (12% use AI for quality assurance reviews)" }
  last_reviewed: 2026-10-20
  notes: "Firm type: Baker Tilly, large US accounting and advisory firm (US ranking not checked). Context figure: in Gartner's poll of 743 audit professionals, 12% reported using AI for quality assurance reviews (a small fraction), measured as share of poll respondents."

- id: advisory-risk-controls-06
  title: AI drafting of audit observations, root cause, impact and recommendations
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Writing structured observation language (finding detail, root cause, impact, recommendation) after testing is slow and varies by author."
  solution: "RSM's agent drafts structured observation language from documented test results. Auditors follow up with auditees to validate findings and root cause before the report is final. Gartner's poll shows this is among the most common genAI uses in audit."
  outcomes:
    - lever: speed
      description: "60% of polled audit professionals use genAI to draft audit issues, ratings or reports."
      figure: "60%"
      measures: "Share of 743 audit professionals in a Gartner webinar poll who reported using genAI to draft audit issues, ratings or reports; self-selected webinar audience"
      provenance: independent
      source_ref: ACCTIMES-GARTNER-2026
  prerequisites:
    - "Detailed test data; RSM says output quality depends on it"
  risks_and_guardrails:
    - "Auditor follows up with auditees to validate findings and root cause before finalizing (RSM-AGENTICIA-2025, section on reportable observation language)"
    - "Gartner reports lack of clarity on expected AI tool use is the most common obstacle (48%) (HELPNET-GARTNER-2026)"
  human_checkpoints:
    - "Auditor validates each draft finding with the auditee"
  role_evolution: "Auditors shift from writing first drafts to validating facts and root cause with auditees (RSM-AGENTICIA-2025)."
  evidence_grade: B
  sources:
    - { ref: RSM-AGENTICIA-2025, title: "Reimagine internal audit with agentic AI to drive value", publisher: RSM US, type: firm, url: "https://rsmus.com/insights/services/digital-transformation/agentic-ai-for-internal-audit.html", date: 2025-12-22, access: full, locator: "Section 'Generating reportable observation language'" }
    - { ref: ACCTIMES-GARTNER-2026, title: "Audit teams' AI use common but most lack strategy", publisher: Accounting Times, type: press, url: "https://www.accountingtimes.com.au/profession/audit-teams-ai-use-common-but-most-lack-strategy", date: 2026-08-16, access: full, locator: "Paragraph 'The poll found that generative AI use cases ...'" }
    - { ref: HELPNET-GARTNER-2026, title: "Most chief audit executives can't tell you what AI is worth yet", publisher: Help Net Security, type: press, url: "https://www.helpnetsecurity.com/2026/09/15/gartner-ai-in-internal-audit/", date: 2026-09-15, access: full, locator: "Section 'The barriers are people and process'" }
  last_reviewed: 2026-10-20
  notes: "Firm type: RSM US (top-10 US firm, middle-market focus). The Gartner figure covers internal audit teams in general, not outsourced providers specifically. Gartner press releases (2026-08-10 and 2026-09-10) were blocked; figures come from press coverage. Base discrepancy: Accounting Times attributes the 93% use and 38% strategy figures to the 743-person poll; Help Net Security attributes the 38% strategy figure to 161 CAEs polled in May 2026. Both are reported with their stated bases."

- id: advisory-risk-controls-07
  title: Assistive AI across SOX and internal audit routine tasks (walkthrough notes, sample selection, first-draft procedures)
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [document-production, data-reporting]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "SOX and internal audit staff spend time on meeting summaries, walkthrough notes, sample selection, template population and QA reviews."
  solution: "Practitioners on a May 2026 SOX leaders' panel described assistive uses: meeting summaries, walkthrough notes, code analysis, sample selection, reporting automation, populating SOC 1 templates, first-draft test procedures and documentation, and accelerating QA reviews. Few examples of autonomous AI were reported."
  outcomes:
    - lever: capacity
      description: "In Sikich's survey, more than half of respondents use AI for analytics, planning, reporting and evidence review, or control testing. No time saved is published."
      figure: "more than half"
      measures: "Share of surveyed US audit leaders (n=222) using AI for each named audit activity; Sikich reports 'more than half' without per-activity figures in the text"
      provenance: vendor-published
      source_ref: SIKICH-IAPRIORITIES-2026
  prerequisites:
    - "Approved tools; clear expectations for validation, documentation, human review and data protection (SIKICH-IAPRIORITIES-2026, p.27)"
  risks_and_guardrails:
    - "Sikich says that as AI influences scope, procedures and conclusions, functions need clear expectations for validation, documentation, human review and data protection (p.27)"
  human_checkpoints:
    - "Human review of all AI outputs; panelists reported few autonomous uses (IAC-SOXCHANGE-2026, section 1)"
  role_evolution: "SOX teams use freed capacity for advisory work; two-thirds of polled SOX leaders were asked to add value in operational, process and technology audits (IAC-SOXCHANGE-2026, section 2)."
  evidence_grade: C
  sources:
    - { ref: IAC-SOXCHANGE-2026, title: "How SOX Is Changing in 2026", publisher: Internal Audit Collective, type: community, url: "https://www.internalauditcollective.com/newsletters/how-sox-is-changing-in-2026", date: 2026-06-04, access: full, locator: "Section 1, paragraph on current SOX use cases" }
    - { ref: SIKICH-IAPRIORITIES-2026, title: "2026 Internal audit priorities annual survey", publisher: Sikich, type: survey, url: "https://go.sikich.com/rs/345-ICF-683/images/Sikich%202026%20Internal%20Audit%20Priorities%20Survey%20Report.pdf?version=0", date: 2026-10, access: full, locator: "p.27 'AI is moving into core audit work'" }
  last_reviewed: 2026-10-20
  notes: "Grade C: the panelists' employers are not named in the page text, so no named deployment. Sikich date is the PDF creation date (2026-10-16); fieldwork was Jul 24 to Aug 19, 2026; 54% of respondents were public companies and 35% private. The webinar was May 14, 2026; the newsletter is dated 2026-06-04."

- id: advisory-risk-controls-08
  title: Continuous controls monitoring and full-population testing in place of samples
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Periodic, sample-based testing leaves blind spots that surface at year end or during external audit."
  solution: "Grant Thornton describes AI that monitors a growing share of transactions continuously, with anomaly detection and alerts, and multi-agent systems orchestrating control-testing workflows. KPMG tells SOX teams to design controls to withstand full-population analytics by external auditors. Gartner says more mature audit teams move from samples to full populations."
  outcomes:
    - lever: risk
      description: "None published for this module. In KPMG's webcast poll about 28% say their main AI use in SOX and internal audit is analysis of large data sets."
      figure: "about 28%"
      measures: "Share of about 3,900 audit and risk leaders in an April 2026 KPMG webcast poll naming 'analysis of large data sets' as their primary AI use in SOX, internal controls or internal audit"
      provenance: vendor-published
      source_ref: KPMG-REVCONTROLS-2026
  prerequisites:
    - "Mappings from risks to controls to data sources (GT-SOX-2026)"
    - "Precision thresholds tied to true anomalies (GT-SOX-2026)"
    - "Integrated data architecture (KPMG-REVCONTROLS-2026)"
  risks_and_guardrails:
    - "Grant Thornton says external auditors and regulators have not given blanket approval for AI-driven SOX compliance (GT-SOX-2026, introduction)"
    - "Human-approved control logic that sets when AI can auto-clear versus route to review; segregation of duties across AI-assisted workflows (GT-SOX-2026, 'AI as a co-pilot')"
  human_checkpoints:
    - "Control owners triage exceptions; reviewers sign off"
  role_evolution: "Grant Thornton expects roles to move toward analysis, control design and stakeholder engagement while AI handles repetitive testing and documentation (GT-SOX-2026, 'Upskilling')."
  evidence_grade: C
  sources:
    - { ref: GT-SOX-2026, title: "The power of AI in efficient SOX compliance", publisher: Grant Thornton, type: firm, url: "https://www.grantthornton.com/insights/articles/advisory/2026/the-power-of-ai-in-efficient-sox-compliance", date: 2026-07-21, access: full, locator: "Sections 'Continuous controls, continuous assurance' and 'AI as a co-pilot, not an autopilot'" }
    - { ref: KPMG-REVCONTROLS-2026, title: "Revolutionizing internal controls: The impact of technology and automation (April 2026 Future of SOX webcast)", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls-new.pdf", date: 2026-05, access: full, locator: "Slides 2 and 12 ('Design for 100% Population Scrutiny')" }
    - { ref: ACCTIMES-GARTNER-2026, title: "Audit teams' AI use common but most lack strategy", publisher: Accounting Times, type: press, url: "https://www.accountingtimes.com.au/profession/audit-teams-ai-use-common-but-most-lack-strategy", date: 2026-08-16, access: full, locator: "Paragraph beginning 'He said more mature audit teams ...'" }
  last_reviewed: 2026-10-20
  notes: "Firm types: Grant Thornton Advisors (PE-backed platform; Grant Thornton LLP holds the attest practice) and KPMG (Big Four). Both are advocacy pieces. Gartner says only 30% of poll respondents use AI for audit testing. KPMG date is the PDF creation date (2026-05-20); the webcast was in April 2026. Independence: for audit clients, a firm's attest arm cannot also run management's controls monitoring (unverified general background)."

- id: advisory-risk-controls-09
  title: SOX and internal audit repositioned as controls advisers, with controls embedded in first-line processes
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "SOX and internal audit teams spend most capacity testing controls after the fact, while stakeholders ask for advice before controls fail."
  solution: "KPMG's SOX leader says external-auditor reliance 'is going to go away' and the role becomes controls adviser, with automation built into the first line. KPMG's path forward: embed controls in first-line workflows, build audit-ready evidence by design, and shift SOX and internal audit to controls advisory. SOX leaders on a May 2026 panel describe splitting teams into a forward-looking advisory group and a run-the-business group."
  outcomes:
    - lever: growth
      description: "None published. Poll data show the mandate is widening: two-thirds of polled SOX leaders were asked to add value in operational, process and technology audits; 13% are still fully SOX-focused."
      figure: "two-thirds; 13%"
      measures: "Share of SOX leaders polled during a May 14, 2026 webinar (sample size not stated) asked to add value in operational, process or technology audits; share still 100% focused on SOX"
      provenance: independent
      source_ref: IAC-SOXCHANGE-2026
  prerequisites:
    - "First-line process owners who will embed controls and automation"
    - "Execution burden reduced by automation to free advisory capacity (IAC-SOXCHANGE-2026, section 2)"
  risks_and_guardrails:
    - "Independence: advising on control design and later testing the same controls needs separation (general background, unverified); Sikich raises the same issue for audit owning AI governance (SIKICH-IAPRIORITIES-2026, p.31)"
  human_checkpoints:
    - "Controller or process owner owns control design; SOX and internal audit advise and test"
  role_evolution: "Teams move from testers to advisers before controls fail; interviewers look for curiosity and holistic risk thinking (IAC-SOXCHANGE-2026, sections 2 and 4)."
  evidence_grade: C
  sources:
    - { ref: KPMG-REVCONTROLS-2026, title: "Revolutionizing internal controls: The impact of technology and automation (April 2026 Future of SOX webcast)", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls-new.pdf", date: 2026-05, access: full, locator: "Slide 7 (Sue King quote) and slide 12 ('The Path Forward')" }
    - { ref: IAC-SOXCHANGE-2026, title: "How SOX Is Changing in 2026", publisher: Internal Audit Collective, type: community, url: "https://www.internalauditcollective.com/newsletters/how-sox-is-changing-in-2026", date: 2026-06-04, access: full, locator: "Section 2 'SOX Teams' Scope Is Expanding'" }
  last_reviewed: 2026-10-20
  notes: "Pattern is 'other': a service-model repositioning, not an agent pattern. Firm type for KPMG: Big Four. Grade C: a firm's recommendation plus practitioner testimony with unnamed employers."

- id: advisory-risk-controls-10
  title: AI governance advisory for clients using the COSO generative AI roadmap
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Middle-market clients deploy AI faster than they build governance, and are asking their CPAs which tools, risks and use cases make sense."
  solution: "Firms advise clients on governing their own AI: use-case inventory, ownership and escalation, risk-tiered human review, control building blocks, monitoring and metrics. COSO's February 2026 publication supplies the structure; Deloitte describes its six-step roadmap (govern, inventory, assess, design, implement, monitor) as convertible into a management workplan."
  outcomes:
    - lever: growth
      description: "Grant Thornton Advisors' CEO says AI is already driving demand for AI governance work and he predicts demand will grow."
      figure: "none published"
      measures: "No revenue or engagement count published; statement by the CEO to Bloomberg Tax"
      provenance: self-reported
      source_ref: GT-CBIZ-2026
    - lever: risk
      description: "67% of surveyed middle-market organizations apply AI governance controls before pilot or production stages."
      figure: "67%"
      measures: "Share of 1,030 US and Canadian middle-market senior business leaders in RSM's 2026 survey who say they apply AI governance controls before pilot or production stages"
      provenance: vendor-published
      source_ref: RSM-MMAI-2026
  prerequisites:
    - "Cross-functional governance with defined roles, accountability and escalation, including shadow AI (DELOITTE-COSO-2026)"
    - "A maintained AI use-case inventory mapped to processes, assertions and key controls"
  risks_and_guardrails:
    - "COSO says generative AI risks include prompt manipulation, opaque reasoning, model drift and frequent configuration changes (COSO-GENAI-2026; IIA-COSO-2026)"
    - "Deloitte says COSO's guidance builds on the 2013 framework and is not a prescriptive rulebook (DELOITTE-COSO-2026)"
  human_checkpoints:
    - "Management owns governance; advisers design and challenge it"
  role_evolution: "Advisory teams need AI-literate risk specialists; ENGAGE 2026 listed a session on giving CPAs the language to discuss AI tools and risks with clients (KARBON-ENGAGE-2026)."
  evidence_grade: C
  sources:
    - { ref: GT-CBIZ-2026, title: "Grant Thornton CEO Says CBIZ Merger Is Key to Unlocking AI Value", publisher: Bloomberg Tax, type: press, url: "https://news.bloomberglaw.com/financial-accounting/grant-thornton-ceo-says-cbiz-merger-is-key-to-unlocking-ai-value", date: 2026-09-02, access: full, locator: "Paragraphs on AI governance demand (fetched via text mirror)" }
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://www.coso.org/generative-ai", date: 2026-02-23, access: full, locator: "Release summary page" }
    - { ref: DELOITTE-COSO-2026, title: "COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up)", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: 2026-04-03, access: full, locator: "Opening paragraphs and 'six actions' list" }
    - { ref: RSM-MMAI-2026, title: "The Middle Market Has Embraced AI. Now Comes the Hard Part (RSM Middle Market AI Survey 2026)", publisher: CPA Practice Advisor, type: survey, url: "https://www.cpapracticeadvisor.com/2026/07/22/the-middle-market-has-embraced-ai-now-comes-the-hard-part/187171/", date: 2026-07-22, access: full, locator: "Final paragraph on governance controls" }
    - { ref: KARBON-ENGAGE-2026, title: "AICPA & CIMA ENGAGE 2026 (curated session list)", publisher: Karbon, type: conference, url: "https://karbonhq.com/resources/aicpa-cima-engage-2026/", date: 2026-05-21, access: full, locator: "Session 'AI conversations and integration: A practical guide for CPAs and their clients'" }
  last_reviewed: 2026-10-20
  notes: "Firm types: Grant Thornton Advisors (PE-backed platform), Deloitte (Big Four), RSM (top-10, middle-market). COSO's release date (2026-02-23) is from Deloitte DART; the JofA report is dated 2026-02-26. The Karbon page is a preview dated 2026-05-21 for an event held Jun 8 to 11, 2026; the session is listed, not observed. Independence: when a firm audits the client, designing the client's AI governance raises management-responsibility threats (general background, unverified in this run). No firm publishes engagement outcomes."

- id: advisory-risk-controls-11
  title: Internal audit engagements that assess client AI governance, inventories and model effectiveness
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Boards and audit committees want assurance that AI is governed and delivering value, and internal audit plans have to cover a new risk area."
  solution: "Co-sourced and in-house internal audit teams add AI governance, AI inventory, shadow AI, targeted high-risk AI assessments and ongoing monitoring reviews to audit plans. The IIA provides AI Framework Support Tools with questionnaires for management, ERM, the audit committee and the board."
  outcomes:
    - lever: risk
      description: "77% of audit plans include AI assessments, but only 53% of those auditing AI review operational effectiveness."
      figure: "77%; 53%; 40%; 36%"
      measures: "77% of 222 US audit leaders' plans include AI assessments; of respondents auditing AI, 53% review operational effectiveness, 40% ethical use and bias, 36% model validation (Sikich 2026 survey)"
      provenance: vendor-published
      source_ref: SIKICH-IAPRIORITIES-2026
    - lever: capacity
      description: "63% of healthcare internal audit respondents say they are already performing AI governance engagements."
      figure: "63%"
      measures: "Share of respondents in the 2026 Protiviti and AHIA healthcare internal audit survey (sample size not captured in this read) reporting AI governance engagements"
      provenance: vendor-published
      source_ref: PROTIVITI-AHIA-2026
  prerequisites:
    - "AI inventory including shadow AI"
    - "AI-literate auditors; Sikich finds cyber and AI are the hardest skills to develop and retain (41% for AI)"
  risks_and_guardrails:
    - "Sikich warns safe is not the same as effective: a governed model can still produce inaccurate or biased decisions (p.26, p.30)"
    - "Internal audit should not design, own and later assure the same AI governance structure; internal audit is primary AI risk owner in 27% of smaller organizations versus 6% of larger ones (SIKICH-IAPRIORITIES-2026, p.31)"
  human_checkpoints:
    - "Auditor judgment on scope and conclusions; management retains AI ownership"
  role_evolution: "Audit leaders hire for AI and cyber but compete with the technology market; 82% use external partners to supply specialized skills (SIKICH-IAPRIORITIES-2026, pp.17, 24)."
  evidence_grade: C
  sources:
    - { ref: SIKICH-IAPRIORITIES-2026, title: "2026 Internal audit priorities annual survey", publisher: Sikich, type: survey, url: "https://go.sikich.com/rs/345-ICF-683/images/Sikich%202026%20Internal%20Audit%20Priorities%20Survey%20Report.pdf?version=0", date: 2026-10, access: full, locator: "pp.8, 17, 24, 26, 29-31" }
    - { ref: PROTIVITI-AHIA-2026, title: "Reimagining Healthcare Internal Audit Survey (2026 plan priorities, Protiviti and AHIA)", publisher: Protiviti, type: survey, url: "https://www.protiviti.com/sites/default/files/2026-08/ahia26-healthcareinternalaudit-surveyreport-0826-na-en.pdf", date: 2026-08, access: full, locator: "Section 04 'Artificial intelligence and other emerging technologies' and 'In Closing'" }
    - { ref: IIA-AIKC-2026, title: "IIA AI Knowledge Center: New Tools for Internal Auditors", publisher: IIA Belgium, type: professional-body, url: "https://www.iiabelgium.org/news-publications/iia-ai-knowledge-center-new-tools-for-internal-auditors", date: 2026-08, access: full, locator: "Sections 'New AI Framework Support Tools' and 'AI Prompting for Internal Auditors'" }
  last_reviewed: 2026-10-20
  notes: "Grade C: prevalence is measured by vendor surveys of unnamed respondents. No named deployment and no outcome measure, so not B. Maturity is in-production on the strength of survey-measured prevalence. Protiviti-AHIA is healthcare-specific (adjacent sector); the PDF creation date is 2026-08-12 and the sample size was not captured. Sikich date is the PDF creation date (2026-10-16). The IIA Belgium page is undated; it says the prompting resource was published in August 2026. Independence: internal audit outsourcing is restricted for a firm's own SEC audit clients (unverified general background)."

- id: advisory-risk-controls-12
  title: Third-party and vendor AI risk assurance, including SOC report review, in co-sourced internal audit
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Clients obtain AI through vendors and subcontractors, and internal audit must assess vendor AI governance, SOC reports and downstream dependencies. The IIA's Third-Party Topical Requirement takes effect Sep 15, 2026."
  solution: "Internal audit teams review vendor AI governance, read SOC 1 and SOC 2 reports for what they cover, and use contract terms and own testing to cover gaps where reports are silent on AI components."
  outcomes:
    - lever: risk
      description: "40% of surveyed audit functions now evaluate vendor AI governance (new in 2026) and 50% review SOC reports; only 19% evaluate Nth-party risk."
      figure: "40%; 50%; 19%"
      measures: "Shares of 222 US audit leaders in Sikich's 2026 survey who evaluate vendor AI governance, review SOC reports, and evaluate Nth-party risks"
      provenance: vendor-published
      source_ref: SIKICH-IAPRIORITIES-2026
  prerequisites:
    - "Vendor inventory and contract rights; mapping of SOC coverage to AI components"
  risks_and_guardrails:
    - "CPA Practice Advisor commentary says SOC 1 and SOC 2 reports may say little about model behavior, retraining or prompt controls, so gaps need contract terms, complementary user entity controls and own validation (CPAPA-AGENTSCLOSE-2026, item 4)"
    - "Source conflict: that commentary (2026-08-13) says the AICPA has not published SOC guidance on AI use, while the JofA (2026-10-13) says the AICPA issued guidance on service organizations' AI and SOC 1 and SOC 2 earlier in 2026 (AICPA-AUDITAID-2026)"
  human_checkpoints:
    - "Auditor judgment on reliance on vendor reports"
  role_evolution: "Third-party risk work widens from periodic vendor audits to AI governance and downstream dependencies (SIKICH-IAPRIORITIES-2026, p.14)."
  evidence_grade: C
  sources:
    - { ref: SIKICH-IAPRIORITIES-2026, title: "2026 Internal audit priorities annual survey", publisher: Sikich, type: survey, url: "https://go.sikich.com/rs/345-ICF-683/images/Sikich%202026%20Internal%20Audit%20Priorities%20Survey%20Report.pdf?version=0", date: 2026-10, access: full, locator: "p.14 'Third-party risk is absorbing new technology risks'" }
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: CPA Practice Advisor (author A. Fulmore, Texas A&M Central Texas), type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: 2026-08-13, access: full, locator: "Control 4, 'Third-party assurance, read closely'" }
    - { ref: AICPA-AUDITAID-2026, title: "AI and the audit: AICPA publishes practice aid to assist auditors", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/", date: 2026-10-13, access: full, locator: "Paragraph beginning 'In addition to the practice aid ...'" }
  last_reviewed: 2026-10-20
  notes: "The SOC report itself is attest work and belongs to assurance; only the client-side review of vendor reports is in scope here. The Third-Party Topical Requirement effective date is stated in SIKICH-IAPRIORITIES-2026 (p.14) and BAKERTILLY-GAM-2026 (item 4)."

- id: advisory-risk-controls-13
  title: Control design and validation for client finance agents (agent inventory, replayable evidence, sign-off gates, exit thresholds)
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Finance teams deploy reconciliation and close agents faster than they document controls; vendor match-rate and time-saving figures are marketing until tested on the client's own data."
  solution: "Advisers help clients put five controls in writing before an agent touches a production close: agent inventory with a named owner; evidence the auditor can replay; sign-off gates scaled to risk; third-party assurance mapping; and monitoring with metrics and an exit threshold. A validation period is built into rollout."
  outcomes:
    - lever: risk
      description: "KPMG's survey reports fewer than half (42%) of finance leaders are fully assurance ready and only 29% track where AI adoption fails."
      figure: "42%; 29%"
      measures: "Share of 1,013 senior finance leaders (organizations with revenue of at least US$250 million, US$500 million in the US; fieldwork March 2026) fully assurance-ready for AI-enabled finance processes; share tracking where AI adoption fails"
      provenance: vendor-published
      source_ref: KPMG-AIFINANCE-2026
  prerequisites:
    - "Client willingness to define normal match rates, exception volumes and error rates before go-live"
  risks_and_guardrails:
    - "Deloitte says monitoring should track indicators such as transaction volume, size and override percentages to detect model drift, and that 'set-and-forget' does not work (DELOITTE-COSO-2026)"
    - "CPA Practice Advisor commentary cites Deloitte Australia's October 2025 partial fee refund over fabricated citations as a lesson about unreviewed output (CPAPA-AGENTSCLOSE-2026, control 3)"
  human_checkpoints:
    - "Named human sign-off on agent output that feeds the financial statements; controller signs the memo"
  role_evolution: "Advisers move from implementing tools to writing and testing the control framework around them (CPAPA-AGENTSCLOSE-2026)."
  evidence_grade: C
  sources:
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: CPA Practice Advisor (author A. Fulmore, Texas A&M Central Texas), type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: 2026-08-13, access: full, locator: "Controls 1 to 5" }
    - { ref: KPMG-AIFINANCE-2026, title: "AI adoption in finance doubles, but assurance readiness determines who wins, KPMG finds", publisher: KPMG International, type: survey, url: "https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html", date: 2026-05-11, access: full, locator: "Section 'Assurance readiness powers AI performance'" }
    - { ref: DELOITTE-COSO-2026, title: "COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up)", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: 2026-04-03, access: full, locator: "Paragraph on monitoring KPIs" }
  last_reviewed: 2026-10-20
  notes: "Resolves a landscape note: the KPMG release states both that fewer than half (42%) are fully assurance-ready and that 42% of assurance-ready organizations are confident in scaling AI (versus 14% of others); the two 42% figures measure different things. The KPMG sample is large organizations (revenue thresholds above) and 58% technology and financial services, so it does not describe private middle-market clients. Grade C: practitioner commentary plus a vendor survey; no named deployment."

- id: advisory-risk-controls-14
  title: SOX scoping and evaluation of AI embedded in client controls
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Business teams put AI inside revenue, procure-to-pay, close and access workflows, and SOX teams have no agreed way to scope or test those controls."
  solution: "SOX teams ask about AI use and reliance during walkthroughs, send control owners quarterly questionnaires on current and planned AI, hold human-in-the-loop discussions for key controls, write baseline human-in-the-loop requirements, and align with the external auditor on documentation and evidence."
  outcomes:
    - lever: risk
      description: "An informal webinar poll reported by the community publisher implies 95% of SOX programs lack a defined framework for evaluating AI in controls."
      figure: "95%"
      measures: "Share of poll respondents in a May 2026 Internal Audit Collective webinar poll (sample size not stated in the text) without a defined framework for evaluating AI inside business controls, as the article states it"
      provenance: independent
      source_ref: IAC-SOXRELIANCE-2026
  prerequisites:
    - "Control-owner inventory of AI use; COSO's generative AI publication as a starting framework"
  risks_and_guardrails:
    - "Panelists cite evidence retention, access management, data privacy and security, monitoring and non-deterministic outputs as concerns (IAC-SOXCHANGE-2026, section 1)"
    - "Vendor commentary says AI controls are assessed by analogy to existing standards and that precision, false-negative rate and drift are undefined for AI controls (FINREP-SOXRELIANCE-2026; vendor claim)"
  human_checkpoints:
    - "Control owners document human-in-the-loop procedures; SOX team confirms with external audit"
  role_evolution: "SOX teams become the first reviewer of how business controls use AI and negotiate evidence expectations with external audit (IAC-SOXRELIANCE-2026)."
  evidence_grade: C
  sources:
    - { ref: IAC-SOXCHANGE-2026, title: "How SOX Is Changing in 2026", publisher: Internal Audit Collective, type: community, url: "https://www.internalauditcollective.com/newsletters/how-sox-is-changing-in-2026", date: 2026-06-04, access: full, locator: "Section 1, subsection 'Assessing SOX-Relevant Business Controls'" }
    - { ref: IAC-SOXRELIANCE-2026, title: "AI Use in SOX: What Will External Audit Rely On?", publisher: Internal Audit Collective, type: community, url: "https://www.internalauditcollective.com/newsletters/ai-use-in-sox-what-will-external-audit-rely-on-and-how-can-sox-teams-get-ahead-of-the-game", date: 2026-06-11, access: full, locator: "Section 'Management's Use of AI in Internal Controls'" }
    - { ref: FINREP-SOXRELIANCE-2026, title: "SOX Reliance on AI Controls: What the Guidance Actually Says (2026)", publisher: Finrep, type: vendor, url: "https://www.finrep.ai/blog/sox-reliance-on-ai-controls-what-the-guidance-actually-says-2026", date: 2026-07-13, access: full, locator: "Sections 'The Precision Problem' and 'Model Drift as a Control Deficiency'" }
  last_reviewed: 2026-10-20
  notes: "The IAC newsletter promotes its own paid playbook and program. The chart behind the 95% was not in the page text; the figure is the article's own reading of the poll. The vendor blog also claims no PCAOB AI-specific standards or staff guidance exist as of July 2026; that is a single vendor claim, not checked against PCAOB sources."

- id: advisory-risk-controls-15
  title: AI-supported risk research and audit planning
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Pre-planning research, risk brainstorming and scoping consume engagement time before testing begins."
  solution: "Audit teams use genAI for engagement pre-planning research and risk brainstorming, engagement planning and departmental risk assessment. Practitioners say this upstream use is where AI is concentrated today."
  outcomes:
    - lever: speed
      description: "60% of polled audit professionals use genAI for engagement pre-planning; 44% for engagement planning."
      figure: "60%; 44%"
      measures: "Shares of 743 audit professionals in a Gartner webinar poll reporting genAI use for engagement pre-planning (research, brainstorming risks) and engagement planning"
      provenance: independent
      source_ref: ACCTIMES-GARTNER-2026
    - lever: speed
      description: "33% of KPMG webcast respondents name research, planning, scoping and risk assessment as their primary AI use."
      figure: "33%"
      measures: "Share of about 3,900 audit and risk leaders in KPMG's April 2026 Future of SOX webcast poll naming research, planning, scoping and risk assessment as their primary AI use"
      provenance: vendor-published
      source_ref: KPMG-REVCONTROLS-2026
  prerequisites:
    - "Clear AI-use expectations; Gartner says unclear expectations are the top obstacle (48%)"
  risks_and_guardrails:
    - "Gartner says the high adoption is not generally transforming audit processes and that productivity and adoption metrics are too narrow (ACCTIMES-GARTNER-2026)"
  human_checkpoints:
    - "Auditor validates AI-surfaced risks before they enter the plan"
  role_evolution: "Gartner says audit leaders feel pressure to show AI results and often jump to use cases without a strategy (ACCTIMES-GARTNER-2026)."
  evidence_grade: C
  sources:
    - { ref: ACCTIMES-GARTNER-2026, title: "Audit teams' AI use common but most lack strategy", publisher: Accounting Times, type: press, url: "https://www.accountingtimes.com.au/profession/audit-teams-ai-use-common-but-most-lack-strategy", date: 2026-08-16, access: full, locator: "Paragraphs on use cases and on Gartner analyst commentary" }
    - { ref: KPMG-REVCONTROLS-2026, title: "Revolutionizing internal controls: The impact of technology and automation (April 2026 Future of SOX webcast)", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls-new.pdf", date: 2026-05, access: full, locator: "Slide 2" }
    - { ref: HELPNET-GARTNER-2026, title: "Most chief audit executives can't tell you what AI is worth yet", publisher: Help Net Security, type: press, url: "https://www.helpnetsecurity.com/2026/09/15/gartner-ai-in-internal-audit/", date: 2026-09-15, access: full, locator: "Paragraph beginning 'Drafting and planning dominate'" }
  last_reviewed: 2026-10-20
  notes: "Covers internal audit teams in general, not only outsourced providers. Poll audiences are self-selected (webinar attendees). Gartner's 15% of departments with formal, routinely run use cases and 54% of CAEs not yet measuring value (n=142 CAEs polled) are from HELPNET-GARTNER-2026."

- id: advisory-risk-controls-16
  title: Fraud-risk and AI-enabled fraud readiness advisory for client internal audit and risk functions
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Internal audit leaders see AI-enabled fraud (fabricated documents, deepfakes, synthetic identities) as a growing risk, and few feel prepared."
  solution: "Idea discussed by practitioners: advisers help client audit and risk teams assess exposure to AI-enabled fraud, build skills and tools, and update fraud risk assessments. The IIA's March 2026 GAM program listed deepfakes and agile fraud risk management as a theme."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "No outcome of an advisory service published. Context: 85% of 373 senior internal audit leaders view AI-enabled fraud as a moderate to high risk and fewer than four in 10 believe their function is adequately prepared (Internal Audit Foundation and Optro survey)"
      provenance: independent
      source_ref: IAF-AIFRAUD-2026
  prerequisites:
    - "Tools, skills and budget; the survey lists these as the main barriers"
  risks_and_guardrails:
    - "Concern focuses on visible threats such as AI-powered phishing, while synthetic identity fraud is less widely recognized (IAF-AIFRAUD-2026, executive summary)"
  human_checkpoints:
    - "Fraud-risk conclusions remain with management and audit leadership"
  role_evolution: "The report says internal audit's own AI use builds the hands-on understanding needed to spot AI-enabled fraud (IAF-AIFRAUD-2026, section on current and future use of AI)."
  evidence_grade: D
  sources:
    - { ref: IAF-AIFRAUD-2026, title: "Internal Audit and AI-Enabled Fraud", publisher: Internal Audit Foundation with Optro, type: survey, url: "https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf", date: 2026-07, access: full, locator: "Executive summary, p.3; p.13-14" }
    - { ref: IIA-GAM-2026, title: "The IIA's Great Audit Minds Conference to be Held March 9-11 in Las Vegas", publisher: The IIA, type: conference, url: "https://www.theiia.org/en/content/communications/press-releases/2026/the-institute-of-internal-auditors-great-audit-minds-conference-to-be-held-march-9-11-in-las-vegas/", date: 2026-02-03, access: full, locator: "Key themes list" }
  last_reviewed: 2026-10-20
  notes: "Evidence grade D, labelled idea: the sources show demand and concern, not a deployed advisory service. Forensic and fraud-investigation work belongs to forensic-disputes (see section 4). IAF PDF date is the creation date (2026-07-28). The IIA release text prints 'February 3, 2025' although it announces the March 9-11, 2026 conference; 2026-02-03 is assumed to be a typo."

- id: advisory-risk-controls-17
  title: Continuous AI-assisted risk sensing for enterprise risk management and audit planning
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [data-reporting, research-synthesis]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Enterprise risk registers and annual audit plans lag real conditions; Baker Tilly describes a 'signal gap' where data infrastructure cannot identify risks in real time."
  solution: "Idea discussed by practitioners: share risk registers and compliance monitoring results across the three lines and use AI to sense risk themes between planning cycles. Baker Tilly's GAM recap says 71% of CAEs now hold responsibilities beyond internal audit, including second-line functions such as ERM."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "No outcome published; the 71% figure is a stated share of CAEs with responsibilities beyond internal audit, with the survey behind it not named in the Baker Tilly recap"
      provenance: self-reported
      source_ref: BAKERTILLY-GAM-2026
  prerequisites:
    - "Documented governance that preserves independence while sharing risk intelligence (BAKERTILLY-GAM-2026, item 2)"
    - "Data infrastructure able to surface risk signals in real time"
  risks_and_guardrails:
    - "Baker Tilly flags a governance gap and independence concerns when internal audit takes on second-line functions (BAKERTILLY-GAM-2026, item 2)"
  human_checkpoints:
    - "CAE and risk leaders decide what enters the risk register and audit plan"
  role_evolution: "The CAE moves from controlling every move to cultivating an environment where innovation can grow, in Baker Tilly's words (BAKERTILLY-GAM-2026, item 6)."
  evidence_grade: D
  sources:
    - { ref: BAKERTILLY-GAM-2026, title: "Strategy in motion: Internal audit's 2026 execution mandate", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate", date: 2026-04-10, access: full, locator: "Items 1, 2 and 6" }
    - { ref: PROTIVITI-TOPRISKS-2026, title: "Top Risks 2026: Insights for Internal Audit Teams", publisher: Protiviti, type: survey, url: "https://www.protiviti.com/us-en/survey/top-risks-cae-internal-audit-2026", date: 2026-01-22, access: full, locator: "Paragraph on CAE integration concerns (48%)" }
  last_reviewed: 2026-10-20
  notes: "Evidence grade D, labelled idea. Baker Tilly's recap presents several statistics without naming sources (for example 95% of genAI projects failing to scale; about 40% of auditor time on data collection); these are not used as outcomes. Protiviti and NC State survey of 1,540 board members and executives: 48% of CAEs cite integrating AI into existing technology, processes and workforce as a top concern."

- id: advisory-risk-controls-18
  title: Single AI-native engagement platform for co-sourced internal audit, SOC and audit delivery
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance, document-production]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Planning, testing, review and reporting are spread across files and tools; firms face a capacity squeeze as the CPA pipeline thins."
  solution: "Cherry Bekaert consolidates SOC, financial audit and internal audit delivery on Fieldguide after an existing deployment in its Risk and Cybersecurity practice. Aprio standardizes SOC, ISO, HITRUST and PCI engagements on the same platform and is co-developing role-specific agents. Baker Tilly runs internal audit delivery on it."
  outcomes:
    - lever: capacity
      description: "No measured result published. Firms describe the expected gain as capacity and consistency; the vendor cites a CPA-pipeline shortage."
      figure: "none published"
      measures: "No hours, cost or quality measure published by Cherry Bekaert, Aprio or Baker Tilly"
      provenance: self-reported
      source_ref: CB-FIELDGUIDE-2026
  prerequisites:
    - "Firm methodology configured into the platform; open APIs to the firm's other systems"
    - "AI governance certification of the platform (Fieldguide cites AIUC-1 and ISO 42001)"
  risks_and_guardrails:
    - "Cherry Bekaert says the platform keeps full human oversight and end-to-end traceability (CB-FIELDGUIDE-2026, paragraph 3)"
    - "Aprio says each workflow is built to comply with AICPA, PCAOB and GAAS standards with human oversight at every stage (APRIO-FIELDGUIDE-2026, paragraph 2)"
  human_checkpoints:
    - "Human oversight at every stage of the engagement lifecycle"
  role_evolution: "Aprio says its own professionals build and refine the agents, and that people spend more time on interpretation and advice (APRIO-FIELDGUIDE-2026)."
  evidence_grade: B
  sources:
    - { ref: CB-FIELDGUIDE-2026, title: "Cherry Bekaert Expands AI Audit With Fieldguide", publisher: Cherry Bekaert, type: firm, url: "https://www.cbh.com/newsroom/cherry-bekaert-expands-ai-audit-with-fieldguide/", date: 2026-06-03, access: full, locator: "Paragraphs 1 to 3" }
    - { ref: APRIO-FIELDGUIDE-2026, title: "Aprio and Fieldguide Co-Build the Future of Audit with Agentic AI", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188025", date: 2026-08-05, access: full, locator: "Paragraphs 1, 2 and 5 (timeline of pilot to platform)" }
    - { ref: BAKERTILLY-AIIA-2026, title: "Start with stakeholder value when using AI in internal audit", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/ai-in-internal-audit", date: 2026-09-08, access: full, locator: "Paragraph beginning 'At Baker Tilly, Fieldguide ...'" }
    - { ref: FIELDGUIDE-SERIESC-2026, title: "Fieldguide Raises $75M Series C Round", publisher: CPA Practice Advisor, type: vendor, url: "https://www.cpapracticeadvisor.com/2026/02/02/fieldguide-raises-75m-series-c-round-to-boost-audit-and-advisory-firms-agentic-ai-capabilities/177323", date: 2026-02-03, access: full, locator: "Paragraphs on the capacity shortfall and customers" }
  last_reviewed: 2026-10-20
  notes: "Firm types: Cherry Bekaert (self-described top 20), Aprio (20th largest per CPA Practice Advisor), Baker Tilly (large US firm, ranking not checked), all mid-market accounting and advisory firms with attest practices. Independence: these firms also audit financial statements, so internal audit outsourcing to their own SEC audit clients is restricted (unverified general background). Cherry Bekaert's announcement is dated by the page as June 3, 2026. Vendor claims (platform used by half of the top 100 firms; capacity-shortfall estimates) are single-source vendor statements. Maturity in-production: Aprio says its Risk Advisory expansion to the platform was in December 2025; the financial audit extension is May 2026."
```

---

## 3. Module notes

**Processes and key steps (with work types)**
- Internal audit co-sourcing and outsourcing: risk assessment and planning (`research-synthesis`); scoping and walkthroughs (`document-production`); RCM build, test design and request lists (`document-production`); evidence collection and testing (`review-assurance`); findings, root cause and reporting (`document-production`); follow-up and remediation tracking (`coordination-scheduling`).
- SOX readiness and ongoing compliance: scoping and controls rationalization (`expert-judgment`); walkthroughs and test of design (`review-assurance`); operating-effectiveness testing (`review-assurance`); deficiency evaluation and external-auditor coordination (`expert-judgment`).
- Enterprise risk: risk identification and registers (`research-synthesis`); monitoring and reporting (`data-reporting`).
- Advising clients on governing AI: inventory, ownership, control design, monitoring, vendor assurance mapping (`expert-judgment`, `review-assurance`).

**Common pain points**
- Time and resources are the primary obstacle for AI in SOX and internal audit, cited by about 26% of KPMG's webcast respondents (KPMG-REVCONTROLS-2026, slide 8); 43% of Sikich respondents cite limited time, budget and resources as the main barrier to implementing IIA Topical Requirements (SIKICH-IAPRIORITIES-2026, p.9).
- Skills: technical skills are the top hiring and retention challenge (64%); cyber (42%) and AI (41%) are hardest to develop (SIKICH-IAPRIORITIES-2026, pp.22-23).
- Unclear expectations for AI tool use are the most common obstacle in Gartner's poll (48%) (HELPNET-GARTNER-2026).
- Reliance uncertainty with external auditors (IAC-SOXRELIANCE-2026).
- Data quality: 36% of KPMG's finance leaders cite it as the biggest barrier and opportunity (KPMG-AIFINANCE-2026).

**Metrics and benchmarks (with sources)**
- AI use in audit: 93% some use, 38% have an AI strategy (743-person Gartner poll; ACCTIMES-GARTNER-2026); 15% have formal use cases run routinely, 54% of 142 polled CAEs have not started measuring AI value (HELPNET-GARTNER-2026).
- 90% of 222 US audit leaders use AI; 82% of users say targeted ROI is achieved (self-defined ROI; SIKICH-IAPRIORITIES-2026, p.29). 84% use internal-audit-specific software.
- Where AI is used: 60% pre-planning and 60% drafting issues or reports; 30% audit testing; 12% QA reviews (ACCTIMES-GARTNER-2026).
- 94% of healthcare internal audit respondents use AI; 59% for interview-note summarization, 47% for workpaper and report drafting; 80% use Microsoft Copilot (PROTIVITI-AHIA-2026, Appendix A).
- Internal audit generative AI use rose from 15% to 40% in one year, per the IIA, as cited by Baker Tilly (BAKERTILLY-AIIA-2026). A related Foundation text gives 41% (IAF-AIFRAUD-2026, p.5); treat 40% to 41% as one reported figure.
- 83% of internal audit leaders expect to increase AI use in the next year (IAF-AIFRAUD-2026, p.14).
- Staffing: 18% of CAEs had staff reductions in 2025, up from 11% in 2024; for privately held organizations cuts rose from 11% to 28% and growth fell from 30% to 17% (IIA-PULSE-2026, Staff sections). Work mix is about three-quarters assurance and one-quarter advisory (IIA-PULSE-2026, section 3).
- General genAI use among professionals 40% (22% a year earlier); only 18% track AI ROI (TR-AIPS-2026).
- Quality evidence: none published. See Summary.

**Guardrails and regulatory points**
- COSO, Achieving Effective Internal Control Over Generative AI (released 2026-02-23): maps the five COSO components to eight capability types and a six-step roadmap (COSO-GENAI-2026; JOFA-COSO-2026; DELOITTE-COSO-2026). Practitioners call it the only formal guidance so far (IAC-SOXCHANGE-2026).
- IIA Topical Requirements: Cybersecurity effective Feb 5, 2026; Third-Party effective Sep 15, 2026; Organizational Behavior effective Dec 15, 2026 (BAKERTILLY-GAM-2026, item 4). IIA also published an AI Auditing Framework with support tools (IIA-AIKC-2026).
- AICPA practice aid on AI for financial statement auditors (2026-10-13) covers client AI in financial reporting and controls, and auditors' own AI use (AICPA-AUDITAID-2026). Source conflict on whether AICPA SOC guidance for AI exists (see use case 12).
- Baker Tilly states the EU AI Act classifies audit AI as high risk (BAKERTILLY-GAM-2026, item 3); this was not checked against the Act and is treated as a firm claim.
- Independence: internal audit outsourcing and designing client controls are restricted for a firm's own audit clients (general background, unverified in this run). Sikich flags independence concerns where internal audit owns AI governance (SIKICH-IAPRIORITIES-2026, p.31).
- Hallucination liability: Deloitte Australia's October 2025 partial fee refund over fabricated citations is cited as the cautionary case (CPAPA-AGENTSCLOSE-2026, control 3; secondhand, original report not opened).

**Frontier signals (dated and sourced)**
- 2026-02-23: COSO publishes the generative AI internal control roadmap (DELOITTE-COSO-2026).
- 2026-03 (GAM, Mar 9 to 11): the IIA's lead theme includes frameworks for safely piloting and scaling agentic AI in audit workflows (IIA-GAM-2026); KPMG sessions on AI in internal audit and technology-enabled controls (KPMG-GAM-2026, sponsor page).
- 2026-04-23: Deloitte calls agentic AI the 'mega hot topic' for internal audit in 2026 (DELOITTE-IAHOT-2026, landing-page text).
- 2026-04 (webcast): KPMG leaders predict no one will work without agentic and AI technologies in five or six years; also say the concept of auditor reliance is going away (KPMG-REVCONTROLS-2026, slides 1 and 7).
- 2026-08-28: RSM announces Beacon as live for internal audit control testing (ACCTODAY-RSMBEACON-2026).
- 2026-09-02: Grant Thornton Advisors' CEO expects AI governance advisory demand to grow as regulators provide guidance (GT-CBIZ-2026).
- 2026-09-15: Third-Party Topical Requirement takes effect (SIKICH-IAPRIORITIES-2026, p.14).
- 2026-10-13 and 2026-10-19: AICPA practice aid, then the AICPA and AIUC joint SOC 2 plus AIUC-1 offering, piloting with full launch expected in early 2027 (AICPA-AUDITAID-2026; AICPA-AIUC-2026; both assurance, see section 4).

**Workforce and role effects**
- Role shift from preparer to supervisor of AI output (RSM-AGENTICIA-2025; BAKERTILLY-AIIA-2026); from tester to controls adviser (KPMG-REVCONTROLS-2026; IAC-SOXCHANGE-2026).
- Hardest profile to hire is someone who is both auditor and technologist; newer staff have technical skills but lack organizational context, experienced auditors need AI and analytics development (SIKICH-IAPRIORITIES-2026, p.21).
- Auditors who built careers on well-crafted workpapers must accept handing that work to the technology, per Jones Lang LaSalle's CAE (IIA-UPSKILL-2026).
- Younger auditors may need coaching on face-to-face skills (IAC-SOXCHANGE-2026, section 4).
- Graduate-pipeline and junior-depletion concerns sit with professional-services (see section 4).

**Objections and concerns practitioners raise**
- External auditors will not rely on pure AI output; most are uncertain about reliance on AI-executed testing (IAC-SOXRELIANCE-2026).
- AI governance lags implementation; evidence retention, access management, data privacy, monitoring and non-deterministic outputs (IAC-SOXCHANGE-2026).
- Speed is a poor measure; faster requests or reports can be worse (BAKERTILLY-AIIA-2026).
- Vendor match-rate and time-saving claims are marketing until reproduced on client data (CPAPA-AGENTSCLOSE-2026).
- Safe AI versus effective AI: governance and privacy get audited more than accuracy and bias (SIKICH-IAPRIORITIES-2026, p.30).
- Pilot-to-scale gap: Protiviti's AI Pulse reports only 1 in 10 organizations have AI embedded in repeatable workflows (PROTIVITI-AHIA-2026, Appendix A).
- Cost-pressure: among middle-market firms increasing AI spend, 40% report reallocating budget from external consulting (RSM-MMAI-2026); not specific to advisory demand, but relevant to fee pressure.

**Interview probes for an advisor**
1. When your team uses an AI agent on control testing or workpapers, what do you measure (override rate, errors found in review, rework), and has anyone run it in parallel with manual work?
2. Has your external auditor said what they will rely on when AI prepares or executes tests, and how do you document that conversation?
3. Who owns AI governance at your clients and at your own firm, and how do you keep internal audit from designing and then assuring the same structure?
4. Which steps do you refuse to hand to AI (ratings, conclusions, deficiency evaluation), and why?
5. How are junior staff learning the work if AI drafts the RCM, the request list and the first findings?

---

## 4. Routed to other modules

| Item | Target module or archetype | Why | Source ref |
|---|---|---|---|
| Enterprise Assurance Services with provisional AIUC-1 accreditation (SOC, ISO, AI assurance) | assurance archetype | Attest and certification work | GT-EAS-2026 |
| AICPA and AIUC joint SOC 2 plus AIUC-1 offering (announced 2026-10-19; piloting, full launch expected early 2027) | assurance archetype | SOC reports stay with assurance | AICPA-AIUC-2026 |
| AICPA practice aid for financial statement auditors on AI (2026-10-13) | assurance archetype | Audit standards and auditor AI use | AICPA-AUDITAID-2026 |
| KPMG UK SOC and ISAE controls assurance with AI (firm reports testing time reductions of about 18% on recent engagements; KPMG Clara AI, DataSnipper, Copilot) | assurance archetype | SOC engagement; the 18% figure is an adjacent-process measure capped at B | KPMG-UKCONTROLS-2026 (PDF, foreword and p.5) |
| AI-enabled fraud investigation, deepfake evidence, fraud technology benchmarks | forensic-disputes | Investigations and evidence work | IAF-AIFRAUD-2026; ACFE items in the landscape |
| AI audit mentor agent for onboarding and training (in-house team) | professional-services | Firm training and operations | IIA-PODCAST-2026 |
| Fieldguide funding, Grant Thornton and CBIZ deal, PE ownership, junior-talent pipeline, pricing pressure | professional-services | Firm operations and ownership | FIELDGUIDE-SERIESC-2026; GT-CBIZ-2026; CPAPA-TECHLAB-2026 |
| Finance-function AI results (forecast accuracy, decision speed) | fpa-performance | Finance performance, not controls | KPMG-AIFINANCE-2026 |
| AI in the monthly close for CAS clients | client-accounting-services | Controllership delivery | CPAPA-AGENTSCLOSE-2026 |

---

## 5. Sources

Types: conference, regulator, standard-setter, professional-body, firm, vendor, academic, survey, press, podcast, community, job-posting. All entries below were opened and read (`access: full`) unless marked.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| KPMG-GAM-2026 | KPMG at the IIA's 2026 GAM conference (sponsor page, sessions Mar 10-11) | KPMG US | conference | https://kpmg.com/us/en/events/2026/kpmg-iias-2026-gam-conference.html | 2026-02-24 |
| IIA-GAM-2026 | The IIA's Great Audit Minds Conference to be Held March 9-11 | The IIA | conference | https://www.theiia.org/en/content/communications/press-releases/2026/the-institute-of-internal-auditors-great-audit-minds-conference-to-be-held-march-9-11-in-las-vegas/ | 2026-02-03 (page prints 2025; see use case 16) |
| BAKERTILLY-GAM-2026 | Strategy in motion: Internal audit's 2026 execution mandate | Baker Tilly | firm | https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate | 2026-04-10 |
| KARBON-ENGAGE-2026 | AICPA & CIMA ENGAGE 2026 (curated session list; event Jun 8-11, 2026) | Karbon | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 |
| CPAPA-TECHLAB-2026 | Thought Leader & 40 Under 40 AICPA Think Tank, Accounting Technology Lab podcast | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/thought-leader-40-under-40-aicpa-think-tank-accounting-technology-lab-podcast-july-2026/ | 2026-07-01 |
| IIA-PODCAST-2026 | Building an AI Audit Mentor (All Things Internal Audit Tech, ep. 135) | The IIA | podcast | https://www.theiia.org/en/content/podcast/all-things-internal-audit/2026/ep-0135/ | 2026-08-12 (date printed on page) |
| IIA-UPSKILL-2026 | Internal Audit Upskilling for Critical AI Capabilities | The IIA | professional-body | https://www.theiia.org/en/content/articles/global-best-practices/2026/internal-audit-upskilling-for-critical-ai-capabilities/ | 2026-07-22 (date printed on page) |
| IIA-CAEBULLETIN-2026 | CAE Bulletin Issue: January 20, 2026 | The IIA | professional-body | https://www.theiia.org/en/content/newsletter/cae-bulletin/cae-bulletin-issue-january-20-2026/ | 2026-01-20 |
| IIA-AIKC-2026 | IIA AI Knowledge Center: New Tools for Internal Auditors | IIA Belgium | professional-body | https://www.iiabelgium.org/news-publications/iia-ai-knowledge-center-new-tools-for-internal-auditors | 2026-08 (undated page) |
| IIA-COSO-2026 | COSO Issues GenAI Guidance | The IIA (Internal Auditor) | professional-body | https://internalauditor.theiia.org/en/articles/2026/march/coso-issues-genai-guidance/ | 2026-03 |
| IIA-PULSE-2026 | 2026 North American Pulse of Internal Audit | Internal Audit Foundation | survey | https://www.theiia.org/globalassets/site/resources/research-and-reports/pulse-of-internal-audit/2026-iia-pulse-of-internal-audit-report.pdf | 2026-02 (PDF creation date; fieldwork Oct 23 to Dec 2, 2025) |
| IAF-AIFRAUD-2026 | Internal Audit and AI-Enabled Fraud | Internal Audit Foundation with Optro | survey | https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf | 2026-07 (PDF creation date) |
| COSO-GENAI-2026 | Achieving Effective Internal Control Over Generative AI | COSO | standard-setter | https://www.coso.org/generative-ai | 2026-02-23 |
| JOFA-COSO-2026 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02-26 |
| DELOITTE-COSO-2026 | COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up) | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 |
| DELOITTE-IAHOT-2026 | Internal Audit Hot Topics 2026 (landing page) | Deloitte US | firm | https://www.deloitte.com/us/en/services/audit-assurance/articles/internal-audit-hot-topics-2026.html | 2026-04-23 |
| KPMG-REVCONTROLS-2026 | Revolutionizing internal controls (April 2026 Future of SOX webcast) | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls-new.pdf | 2026-05 (PDF creation date) |
| KPMG-UKCONTROLS-2026 | Reimagining Controls Assurance with AI: Latest Insights for Leaders | KPMG UK | firm | https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf | 2026-01 |
| KPMG-AIFINANCE-2026 | AI adoption in finance doubles, but assurance readiness determines who wins | KPMG International | survey | https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html | 2026-05-11 |
| GT-SOX-2026 | The power of AI in efficient SOX compliance | Grant Thornton | firm | https://www.grantthornton.com/insights/articles/advisory/2026/the-power-of-ai-in-efficient-sox-compliance | 2026-07-21 |
| GT-EAS-2026 | Grant Thornton launches Enterprise Assurance Services practice | Grant Thornton LLP | firm | https://www.grantthornton.com/insights/press-releases/2026/september/gt-launches-first-of-its-kind-enterprise-assurance-services | 2026-09-23 |
| GT-CBIZ-2026 | Grant Thornton CEO Says CBIZ Merger Is Key to Unlocking AI Value | Bloomberg Tax | press | https://news.bloomberglaw.com/financial-accounting/grant-thornton-ceo-says-cbiz-merger-is-key-to-unlocking-ai-value | 2026-09-02 (read via text mirror) |
| RSM-AGENTICIA-2025 | Reimagine internal audit with agentic AI to drive value | RSM US | firm | https://rsmus.com/insights/services/digital-transformation/agentic-ai-for-internal-audit.html | 2025-12-22 (date printed on page) |
| ACCTODAY-RSMBEACON-2026 | RSM launches AI-guided internal audit platform 'Beacon' with Andera | Accounting Today | press | https://www.accountingtoday.com/news/rsm-launches-ai-guided-internal-audit-platform-beacon-with-andera | 2026-08-28 |
| RSM-MMAI-2026 | The Middle Market Has Embraced AI. Now Comes the Hard Part | CPA Practice Advisor (RSM survey) | survey | https://www.cpapracticeadvisor.com/2026/07/22/the-middle-market-has-embraced-ai-now-comes-the-hard-part/187171/ | 2026-07-22 |
| BAKERTILLY-AIIA-2026 | Start with stakeholder value when using AI in internal audit | Baker Tilly | firm | https://www.bakertilly.com/insights/ai-in-internal-audit | 2026-09-08 |
| CB-FIELDGUIDE-2026 | Cherry Bekaert Expands AI Audit With Fieldguide | Cherry Bekaert | firm | https://www.cbh.com/newsroom/cherry-bekaert-expands-ai-audit-with-fieldguide/ | 2026-06-03 |
| APRIO-FIELDGUIDE-2026 | Aprio and Fieldguide Co-Build the Future of Audit with Agentic AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=188025 | 2026-08-05 |
| FIELDGUIDE-SERIESC-2026 | Fieldguide Raises $75M Series C Round | CPA Practice Advisor | vendor | https://www.cpapracticeadvisor.com/2026/02/02/fieldguide-raises-75m-series-c-round-to-boost-audit-and-advisory-firms-agentic-ai-capabilities/177323 | 2026-02-03 |
| SIKICH-IAPRIORITIES-2026 | 2026 Internal audit priorities annual survey | Sikich | survey | https://go.sikich.com/rs/345-ICF-683/images/Sikich%202026%20Internal%20Audit%20Priorities%20Survey%20Report.pdf?version=0 | 2026-10 (PDF creation date) |
| ACCTIMES-GARTNER-2026 | Audit teams' AI use common but most lack strategy (Gartner poll) | Accounting Times | press | https://www.accountingtimes.com.au/profession/audit-teams-ai-use-common-but-most-lack-strategy | 2026-08-16 |
| HELPNET-GARTNER-2026 | Most chief audit executives can't tell you what AI is worth yet (Gartner) | Help Net Security | press | https://www.helpnetsecurity.com/2026/09/15/gartner-ai-in-internal-audit/ | 2026-09-15 |
| PROTIVITI-TOPRISKS-2026 | Top Risks 2026: Insights for Internal Audit Teams | Protiviti | survey | https://www.protiviti.com/us-en/survey/top-risks-cae-internal-audit-2026 | 2026-01-22 |
| PROTIVITI-AHIA-2026 | Reimagining Healthcare Internal Audit Survey | Protiviti with AHIA | survey | https://www.protiviti.com/sites/default/files/2026-08/ahia26-healthcareinternalaudit-surveyreport-0826-na-en.pdf | 2026-08 (PDF creation date) |
| TR-AIPS-2026 | 2026 AI in Professional Services Report | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/reports/2026-ai-in-professional-services-report | 2026-02-09 (page publishDate field) |
| IAC-SOXCHANGE-2026 | How SOX Is Changing in 2026 | Internal Audit Collective | community | https://www.internalauditcollective.com/newsletters/how-sox-is-changing-in-2026 | 2026-06-04 |
| IAC-SOXRELIANCE-2026 | AI Use in SOX: What Will External Audit Rely On? | Internal Audit Collective | community | https://www.internalauditcollective.com/newsletters/ai-use-in-sox-what-will-external-audit-rely-on-and-how-can-sox-teams-get-ahead-of-the-game | 2026-06-11 |
| FINREP-SOXRELIANCE-2026 | SOX Reliance on AI Controls: What the Guidance Actually Says | Finrep | vendor | https://www.finrep.ai/blog/sox-reliance-on-ai-controls-what-the-guidance-actually-says-2026 | 2026-07-13 |
| CPAPA-AGENTSCLOSE-2026 | Before You Let the Agents Run the Close: Five Controls to Put in Writing First | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/ | 2026-08-13 (read via text mirror) |
| AICPA-AUDITAID-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| AICPA-AIUC-2026 | AICPA partners on new offering that assures AI systems and agents | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/ | 2026-10-19 |

**Source counts (distinct, all opened):** 40 sources. By primary type: firm 10 (KPMG-GAM is counted under conference), survey 9, press 6, professional-body 7, conference 3, community 2, vendor 2, podcast 2, standard-setter 1. That is nine types; no regulator, academic or job-posting sources were used in this angle. Search-only items: none are cited in entries; Gartner's two press releases (2026-08-10, 2026-09-10) and Tanner's AI and Business Systems Advisory launch were seen only as search results or were blocked, and are used nowhere as evidence (`access: search-only`).

---

## 6. Gaps

- **No quality evidence.** No error rates, override rates, parallel-run results or independent measurement of AI-assisted internal audit or SOX work were found. The IIA, Gartner, Sikich, KPMG and Protiviti publish adoption and intent figures only.
- **Web search budget.** The shared WebSearch budget was exhausted partway through, so the query that targeted quality evidence was never run, and the podcast, Going Concern, AccountingWEB and ISACA community searches were not completed. Before learning this, I used DuckDuckGo's HTML page through curl for about a dozen discovery queries (it began returning blocks and I stopped). I did not use any search engine after the budget message. Results found that way were opened and are cited as full sources.
- **Blocked or unreadable.** Gartner press releases (Cloudflare, mirror returned a tracker stub); Reddit (403, including via mirror); Tanner's AI and Business Systems Advisory page (403); internalaudit360.com (406). The Gartner 743-person poll and 161-CAE poll are cited through press coverage; their base discrepancy is flagged in use case 6.
- **Members-only or registration content.** IIA webinar playback on agentic AI; the IIA Audit Podcast sessions beyond episode text; ENGAGE, DCPA and GAM session catalogues (only sponsor and curated lists were read); the Internal Audit Collective's AI Playbook (the poll charts behind the 95% and 48% figures were not visible).
- **Not opened.** Protiviti's 'The Next Phase: AI and Human Collaboration Powering Internal Audit' (July 2025) and AI Pulse volumes; KPMG's July 2025 paper 'The Agentic Shift in SOX Compliance'; Deloitte's AI risk governance service page; the Deloitte Australia refund primary report; Crowe, Forvis Mazars and BDO internal audit AI pages; ISACA material; any PCAOB staff view on AI (a vendor claims none exists; unchecked).
- **Dates.** Several dates are PDF creation dates (Sikich, KPMG webcast, IAF report, Protiviti-AHIA, IIA Pulse). The IIA GAM release prints 2025 for a 2026 event. The IIA upskilling article and podcast dates are taken from text printed on the page. The Audit Podcast episode 224 (EY) was discarded because no date could be confirmed.
- **Scope limits.** Legal-sector events named in the brief (Legalweek, ILTACON, CLOC, Legal Geek) and PMI and MCA events are outside this module's practitioner base and were not researched. Sample sizes were not captured for the Protiviti-AHIA survey or the Internal Audit Collective polls. ENGAGE session content is known only from titles and descriptions, not from attendance.
- **Thin areas.** Cyber and IT risk advisory AI evidence, ERM-specific AI use, and pricing or fee effects for outsourced internal audit (only the RSM survey's budget-reallocation figure and the Thomson Reuters 'conflicting client guidance' point touch it).
