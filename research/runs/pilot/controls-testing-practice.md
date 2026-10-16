# Module deep dive: assurance / controls-testing / practice

- **Archetype:** assurance
- **Module:** controls-testing. Testing whether internal controls are well designed and operate effectively. Covers external ICFR/SOX 404 integrated audits (ISA 330, PCAOB AS 2201 and AS 2301), internal audit and SOX compliance programs, and SOC 1/SOC 2 examinations. Includes walkthroughs, ITGC and application controls testing, sampling, evidence gathering and tick-marking, deficiency evaluation, and documentation.
- **Angle:** practice. What audit firms, internal audit functions and SOX programs actually do with AI in controls testing today. Named deployments, firm platforms, vendor tools with named customers, measured outcomes, how work and roles changed, and what failed.
- **Prepared:** 2026-10-16
- **Method note:** Primary pages were fetched and read in full with curl (WebFetch failed on DNS). Some hosts refused automated access (see §5); items seen only in search extracts are marked `(search extract only)`. Almost every figure below is **self-reported**: published by the deploying organisation or by its vendor. No independent measurement of AI controls testing was found.

---

## 1. Summary

- **Agentic attribute testing is in production at named public companies, mostly on the internal audit / SOX side.**
  - **Reddit:** Internal Audit automated testing of 175 controls (about 40% of SOX scope) in 90 days on Midship (now Optro), with average testing time per control down 60%. It has since expanded to over 75% of SOX controls (S03, S04).
  - **Microsoft:** Internal Audit built a two-agent ITGC change-management tester on Copilot Studio. It reports 850 hours and $185K saved a year (S09, S10). The landscape's "50 hours" figure is a text-extraction artefact: the rendered PDF says 850.
  - **Others:** Klaviyo, Havertys, Navan and FJ Management are further named adopters. None of them publishes measured outcomes beyond quotes (S03, S05, S28, S38).
- **External auditors are earlier and vaguer on controls testing than on substantive work.**
  - **PwC:** says its controls-testing automation is still coming, modelled on Evidence Match (S16). A year into its programme, PwC's US assurance transformation leader says time savings are "not that drastic yet" (S17).
  - **KPMG:** promised in April 2025 that controls-testing agents would ship in KPMG Clara within 12 months. No confirmation of that release was found (S14).
  - **EY and Deloitte:** describe agents across all audit phases, but name no controls-testing outcome (S20, S21).
  - **The clearest firm-side figure is from SOC work:** KPMG UK reports about 18% less testing time on controls assurance (SOC 1/SOC 2/ISAE 3402) engagements using Clara AI agents, Copilot and DataSnipper (S13).
- **The work is moving from "tester" to "reviewer of agent output."** Practitioners and vendors describe the same five-layer design:
  1. An approved test plan.
  2. Evidence extraction with citations.
  3. Attribute-level conclusions with stated reasoning.
  4. Human review at set stages.
  5. Workpapers in the format the external auditor expects (S02, S32, S47).
  The new bottleneck is review effort. An Optro-sponsored survey found 46% of organisations say staff spend *more* time validating AI output (S40).
- **What went wrong is mostly reported as risk, not incidents.**
  - **Agent failures:** 34% of GRC and audit leaders say their organisation acted on an inaccurate agent output, and 25% report a control failure involving an agent (vendor survey, S40).
  - **Inspection findings:** IFIAR members keep finding that automated tools are not used as intended, and that ITGC testing is thin (S56).
  - **Planted instructions:** KPMG warns that control owners could hide instructions in evidence aimed at the testing agents (S11).
  - **No named public failure of an AI controls-testing deployment was found.**
- **Business-model signals.**
  - **Co-sourced testing is being displaced or repackaged.** Havertys is replacing outsourced ITGC testing with agents (S05). RSM and Riveron sell agent-delivered co-sourced testing (S01, S24).
  - **KPMG says external auditors' own full-population testing may reduce reliance on management's 25-item samples** (S11).

---

## 2. Use cases

```yaml
- id: assurance-controls-testing-01
  title: Agentic attribute testing of operating effectiveness for SOX key controls (internal audit)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  lens: delegate
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    Each SOX control test means a person opens PDFs, screenshots, spreadsheets and system exports for every
    sample, checks each attribute, then tick-marks and documents it in Excel/Word. KPMG's 2025 SOX survey puts
    average testing time at 16 hours per control (FY2024, up from 12 in FY2022), with ITGCs and transactional
    controls taking longest.
  solution: >-
    Agents read unstructured evidence, map it to samples and test attributes, run the attribute tests, annotate
    the source evidence and assemble workpapers in the format the external auditor expects. The internal audit
    team reviews and signs off. At Reddit, specialised agents (evidence extraction, testing, review,
    documentation) built on Midship, now Optro Autonomous Testing, covered business process, ITGC, interface
    and entity-level controls.
  outcomes:
    - {lever: capacity, description: "Reddit IA automated testing of 175 controls (>40% of SOX scope) in the first 3 months", figure: "175 controls; >40% of scope", source_ref: S03}
    - {lever: speed, description: "Reddit: average testing time per control reduced", figure: "-60% per control", source_ref: S04}
    - {lever: capacity, description: "Reddit later expanded agentic testing to most SOX controls and other recurring programmes", figure: ">75% of SOX controls", source_ref: S03}
    - {lever: risk, description: "Klaviyo moved from point-in-time testing to testing throughout the year, catching issues earlier (qualitative)", figure: null, source_ref: S03}
  prerequisites:
    - "Clean, structured prior-year test history and RCM in the GRC platform (Havertys: consistent data gave confidence to move)"
    - "Defined test attributes, evidence requirements and exception rules per control"
    - "External auditor engaged early on the workpaper format and the review trail"
  risks_and_guardrails:
    - "Every agent conclusion linked to cited evidence; human-in-the-loop review kept (Reddit post)"
    - "Non-determinism: the same test can return slightly different answers on rerun (S47)"
    - "Planted instructions in control evidence could steer testing agents (KPMG warning, S11)"
  human_checkpoints:
    - "Auditor approves the test plan before execution"
    - "Preparer/reviewer review of each agent-produced workpaper before sign-off"
  role_evolution: >-
    In-house testers become reviewers of agent output and work on exceptions, remediation and control design.
    Reddit's CAE describes HITL review as essential.
  evidence_grade: A
  sources:
    - {ref: S03, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14}
    - {ref: S04, title: "How we used agentic AI to crack automated SOX testing at scale... in 90 days (Martin Preedy, Reddit; mirror of r/RedditEng post)", publisher: "Tenu Tech Brief (mirror of reddit.com/r/RedditEng)", type: community, url: "https://cluster-site.onrender.com/posts/how-we-used-agentic-ai-to-crack-automated-sox-testing-at-scale...-in-90-days/", date: 2026-02-23}
    - {ref: S07, title: "Why autonomous controls testing will redefine internal audit", publisher: Optro, type: vendor, url: "https://optro.ai/blog/autonomous-controls-testing-internal-audit", date: 2026-06-15}
    - {ref: S11, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026}
  last_reviewed: 2026-10-16
  notes: >-
    Figures are self-reported by Reddit's CAE and republished by the vendor; quality (error rate vs human testers)
    is not disclosed. Original reddit.com post unreachable; read via mirror. Function is in-house internal
    audit rather than an audit firm.

- id: assurance-controls-testing-02
  title: Two-agent ITGC change-management testing (attribute extraction plus evidence tick-marking)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: document-to-decision
  lens: automate
  ladder: automate
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Testing SOX change-management controls means reading tickets across several ticketing systems to confirm
    testing, approval and timing relative to deployment. Attributes go into spreadsheets by hand and evidence is
    annotated sample by sample. Ticket formats are inconsistent.
  solution: >-
    Microsoft Internal Audit built two agents on Copilot Studio. An Attribute Extraction Agent ingests ticket
    data, extracts tester, approver and dates into a standard table and pre-populates pass/fail logic based on
    rules. An Evidence Annotation (tick-marking) Agent marks each extracted field in the source evidence so
    the reviewer sees where each attribute was validated.
  outcomes:
    - {lever: capacity, description: "Annual time saved", figure: "850 hours/year", source_ref: S09}
    - {lever: cost, description: "Annual cost saved", figure: "$185K/year", source_ref: S09}
    - {lever: speed, description: "Build time to launch", figure: "1-3 months", source_ref: S09}
  prerequisites:
    - "Ticket data accessible to the agent; rule-based pass/fail criteria defined per attribute"
    - "Low-code agent platform inside the enterprise tenant (Copilot Studio / M365)"
  risks_and_guardrails:
    - "Rules-based pass/fail pre-population still reviewed by auditors; exceptions handled by people"
  human_checkpoints:
    - "Auditor review of the audit table and annotated evidence; judgement on SOX exceptions"
  role_evolution: "Auditors shift from tick-and-tie to judgement on exceptions; built by the internal Finance/Finance IT teams."
  evidence_grade: A
  sources:
    - {ref: S09, title: "Innovation Story: SOX Change Management Testing Agent", publisher: Microsoft (Frontier Finance), type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf", date: FY2026}
    - {ref: S10, title: "AI solution overviews: Internal Audit", publisher: Microsoft (Frontier Finance), type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: FY2026}
  last_reviewed: 2026-10-16
  notes: >-
    Conflict in landscape (850 vs ~50 hours) resolved: both Microsoft PDFs say 850 hours when rendered; the
    "50" came from a dropped glyph in the PDF text layer. Self-reported by a company that also sells the platform.

- id: assurance-controls-testing-03
  title: In-sourcing previously outsourced SOX/ITGC testing to agents
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  lens: reinvent
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    Many SOX programmes buy testing hours from co-source providers. KPMG's 2025 survey found 58% say outsourced
    providers make up over 20% of SOX budget. Testers change every year, which hurts consistency.
  solution: >-
    Internal audit teams have agents run the tests that were outsourced, starting with IT general controls, then
    business-process controls. They keep their own review process. External spend is redirected to advisory work.
  outcomes:
    - {lever: cost, description: "Havertys starts with outsourced IT controls because ROI was clearest; target all IT SOX tests and part of business-process tests", figure: null, source_ref: S05}
    - {lever: cost, description: "A Petual customer (unnamed) told the investor they cut SOX budget to a quarter of its prior level", figure: "~75% budget reduction (anecdotal, unnamed)", source_ref: S27}
  prerequisites:
    - "Years of structured test history and documentation in the GRC platform"
    - "Ability to 'teach' tests the same way one would brief a rotating third-party tester"
  risks_and_guardrails:
    - "Same manager review and approval as before ('humans in the loop')"
    - "Turnover risk at co-source providers given as a reason to move"
  human_checkpoints:
    - "IT audit manager reviews every agent test result before acceptance"
  role_evolution: >-
    Co-source budget shifts from testing hours to advisory. Internal auditors take on complex and non-standard
    controls, remediation and programme design.
  evidence_grade: B
  sources:
    - {ref: S05, title: "Four years in, Havertys expands its use of Optro with agentic AI for controls testing", publisher: Optro, type: vendor, url: "https://optro.ai/blog/havertys-furniture-success-story", date: 2026}
    - {ref: S27, title: "Investing in Petual", publisher: Andreessen Horowitz, type: vendor, url: "https://a16z.com/announcement/investing-in-petual/", date: 2026-04-23}
    - {ref: S11, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026}
  last_reviewed: 2026-10-16
  notes: "Havertys has announced and begun the move; no measured outcome yet. Petual quote is from an unnamed customer via an investor."

- id: assurance-controls-testing-04
  title: Agent-delivered co-sourced and outsourced controls testing by advisory firms
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  lens: reinvent
  ladder: augment
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    Firms that sell SOX and internal audit testing as a labour-based service face fee pressure and client
    in-sourcing to agents (see -03).
  solution: >-
    Firms embed agents in their own delivery.
    - RSM Beacon (with Andera): upload evidence, automatic file and completeness validation, natural-language
      directed test steps, rules-based analysis such as user-access testing, standard outputs traced to source.
      Auditors approve, refine or intervene at key stages. Scope covers SOX, internal audit, SOC and ICFR testing.
    - Riveron: uses different agents at specific workflow steps in co-sourced and outsourced engagements.
      Every result is reviewed by its professionals before it enters the workpaper.
  outcomes:
    - {lever: growth, description: "RSM positions Beacon as a new service for middle-market internal audit functions", figure: null, source_ref: S01}
    - {lever: quality, description: "Riveron argues hours saved is not the main metric; measures include review-ready workpapers and earlier issue visibility", figure: null, source_ref: S24}
  prerequisites:
    - "Firm methodology encoded in prompts and templates ('RSM-embedded methodology and standard prompting')"
    - "Disciplined control metadata, test attributes, evidence requirements, sampling logic and exception rules"
  risks_and_guardrails:
    - "Distinguish missing support from true exceptions (e.g., a review done in a meeting without written record)"
    - "General-purpose LLMs alone said not to meet the 'audit-grade' standard for testing"
  human_checkpoints:
    - "Approval at key workflow stages (RSM); professional review of every test result (Riveron)"
  role_evolution: "Provider staff shift to review, challenge, exception analysis and stakeholder dialogue."
  evidence_grade: B
  sources:
    - {ref: S01, title: "Andera and RSM US Partner to Create AI-Enabled Control Testing Platform for Internal Audit", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/", date: 2026-08-26}
    - {ref: S02, title: "RSM Beacon | Automated control testing platform", publisher: RSM US, type: firm, url: "https://rsmus.com/services/risk-fraud-cybersecurity/automated-control-testing.html", date: 2026}
    - {ref: S24, title: "AI in Internal Audit and SOX: Applying Methods that Work", publisher: Riveron, type: firm, url: "https://riveron.com/ai-in-internal-audit-and-sox-applying-methods-that-work/", date: 2026-06-16}
  last_reviewed: 2026-10-16
  notes: "No named RSM Beacon client or measured outcome found. Andera says Fortune 500 firms use it, unnamed (S01)."

- id: assurance-controls-testing-05
  title: AI-assisted walkthrough preparation, transcription and process narratives
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Walkthroughs must be repeated every year to confirm nothing changed. Tracing a transaction from start to
    recording is hard in large organisations, and documenting it is tedious.
  solution: >-
    Several approaches are in use:
    - PwC Advanced Walkthrough Assistant: ingests prior-year walkthroughs and current documents, drafts a
      tailored work plan, flags what is missing or changed, and drafts documentation for review.
    - KPMG UK controls assurance: Clara AI reviews control wording before the walkthrough and produces the
      key attributes and a question list. Copilot transcribes the walkthrough into flowcharts and process maps.
    - AuditBoard (Optro): turns walkthrough notes into narratives.
  outcomes:
    - {lever: experience, description: "KPMG UK: fewer meetings and follow-up requests for control owners (qualitative)", figure: null, source_ref: S13}
    - {lever: speed, description: "PwC calls walkthroughs one of the more tedious steps the assistant targets; no figure published", figure: null, source_ref: S16}
  prerequisites:
    - "Prior-year walkthrough documentation in machine-readable form"
    - "Client consent to record/transcribe meetings ('where permitted', KPMG UK)"
  risks_and_guardrails:
    - "Transcription kept within the M365 tenant (KPMG UK)"
    - "Drafts are for review; auditor still has to confirm no change in the process"
  human_checkpoints:
    - "Auditor runs the walkthrough and approves the narrative and flowchart"
  role_evolution: "Less time on note-taking and re-documentation; more time on probing changes."
  evidence_grade: B
  sources:
    - {ref: S16, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28}
    - {ref: S17, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07}
    - {ref: S13, title: "Reimagining Controls Assurance with AI: Latest Insights for Leaders", publisher: KPMG in the UK, type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf", date: 2026-01}
    - {ref: S37, title: "AuditBoard Launches Accelerate, Delivering Enterprise-Grade AI Automation for GRC Teams", publisher: AuditBoard (now Optro), type: vendor, url: "https://auditboard.com/blog/auditboard-launches-accelerate-delivering-enterprise-grade-ai-automation-for-grc-teams", date: 2025-10-22}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-06
  title: Test-of-design support and AI-drafted control test plans
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: draft-review-loop
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Breaking control descriptions into testable attributes and writing test plans is manual and uneven.
    Badly worded controls lead to follow-up requests and exceptions later.
  solution: >-
    Several tools draft or score test plans and control descriptions:
    - KPMG UK Clara AI custom agents: capture controls and draft a test plan for review. They also score
      control descriptions against "what a good control looks like" as decision support, not a conclusion.
    - Fieldguide agents: draft test plans per control-matrix row.
    - Petual: imports the RCM and runs the firm's own test procedures.
    - PwC dynamic controls testing: generates test procedures that users review before execution (search
      extract only).
  outcomes:
    - {lever: quality, description: "KPMG UK: indicative control-wording score used as decision support; fuller attribute identification reduces follow-up requests", figure: null, source_ref: S13}
  prerequisites:
    - "Firm/IA methodology and 'good control' criteria written down for the model"
  risks_and_guardrails:
    - "Score is decision support only (KPMG UK); auditor owns ToD conclusion"
    - "Version control on AI-generated test instructions (PwC, search extract only)"
  human_checkpoints:
    - "Auditor approves the test plan before any testing runs"
  role_evolution: "Seniors edit and approve plans instead of writing them; juniors start from a structured draft."
  evidence_grade: B
  sources:
    - {ref: S13, title: "Reimagining Controls Assurance with AI: Latest Insights for Leaders", publisher: KPMG in the UK, type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf", date: 2026-01}
    - {ref: S32, title: "Field Agents for Testing", publisher: Fieldguide Help Center, type: vendor, url: "https://help.fieldguide.io/en/articles/12292640-field-agents-for-testing", date: 2026}
    - {ref: S29, title: "Petual - Automate SOX Testing with AI (homepage)", publisher: Petual, type: vendor, url: "https://www.petual.ai/", date: 2026}
    - {ref: S60, title: "What if controls testing could be done in a fraction of the time (dynamic controls testing) (search extract only)", publisher: PwC US, type: firm, url: "https://www.pwc.com/us/en/tech-effect/ai-analytics/dynamic-controls-testing.html", date: 2026}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-07
  title: AI-assisted testing in SOC 1/SOC 2 and ISAE 3402 controls assurance engagements
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, document-production, coordination-scheduling]
  pattern: document-to-decision
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Service-auditor engagements test high volumes of ITGC evidence, such as change tickets, and depend on
    control owners' time. Demand for controls assurance reports nearly doubled in a year (KPMG UK), without
    a matching rise in staff.
  solution: >-
    KPMG UK uses several tools across its controls assurance engagements:
    - Clara AI custom agents: walkthrough prep, test-plan drafting, and collating reviewer comments on the
      description of service.
    - DataSnipper: extracts details from high volumes of IT change tickets into testing tables.
    - M365 Copilot: meeting recaps, Excel analysis and workpaper drafting.
    - KPMG Clara Collaboration: an evidence portal.
    Fieldguide sells testing agents to SOC/HITRUST firms.
  outcomes:
    - {lever: speed, description: "KPMG UK engagements: testing time reduction from automating control analysis, evidence extraction and standard documentation", figure: "~18%", source_ref: S13}
    - {lever: speed, description: "KPMG UK engagement team using DataSnipper on controls testing", figure: "~15% less testing time", source_ref: S13}
    - {lever: speed, description: "Frazier & Deeter HITRUST controls testing with Fieldguide agents (search extract only)", figure: "~40% faster testing (71 hours returned)", source_ref: S61}
  prerequisites:
    - "Firm-approved tools in a secure environment; risk-based access to client evidence"
  risks_and_guardrails:
    - "Teams ensure outputs still reflect auditor judgement (KPMG UK)"
    - "AICPA TQA 9561 (Sep 2026) adds no AI-specific SOC criteria; scope follows how AI affects in-scope services"
  human_checkpoints:
    - "Service auditor reviews all extracted data and conclusions; opinion unchanged"
  role_evolution: "Analysts spend less time extracting from tickets and more on judgemental areas and sponsor communication."
  evidence_grade: A
  sources:
    - {ref: S13, title: "Reimagining Controls Assurance with AI: Latest Insights for Leaders", publisher: KPMG in the UK, type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf", date: 2026-01}
    - {ref: S61, title: "Frazier Deeter reclaims the judgment work at the heart of HITRUST (search extract only; page returned 404)", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/case-studies/frazier-deeter-reclaims-the-judgment-work-at-the-heart-of-hitrust", date: 2026}
  last_reviewed: 2026-10-16
  notes: "KPMG UK percentages are firm-reported for 'recent engagements' with no sample size given."

- id: assurance-controls-testing-08
  title: Drafting SOC system descriptions and management responses to deviations
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  lens: improve
  ladder: assist
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Service organisations and their advisers draft and update the Section 3 system description, map it to the
    Trust Services Criteria, and write management responses to deviations every cycle.
  solution: >-
    GenAI consolidates process and procedure documents into draft control descriptions and maps them against
    the TSC. It drafts structured management responses (root cause, remediation, timelines), turns meeting notes
    into action items and tracks evidence collection.
  outcomes:
    - {lever: capacity, description: "Live poll at the 2026 EY SOC conference: share of attendees using AI for evidence collection / Section 3 updates / deviation responses / project management", figure: "63% / 45% / 41% / 29%", source_ref: S41}
  prerequisites:
    - "Approved enterprise AI tool; prior SOC reports and policies as source material"
  risks_and_guardrails:
    - "EY: AI 'may invent details and fill in blanks' even when told not to; human oversight required"
  human_checkpoints:
    - "Management owns the description and responses; service auditor tests them"
  role_evolution: "Drafting moves to review; client-side GRC staff do more of the first draft."
  evidence_grade: C
  sources:
    - {ref: S41, title: "How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights)", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09}
  last_reviewed: 2026-10-16
  notes: "Poll of conference attendees, multiple selections allowed; not a representative survey. Mostly management-side work around the SOC exam."

- id: assurance-controls-testing-09
  title: Full-population testing of transactional and master-data controls instead of samples
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  lens: improve
  ladder: automate
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Sample-based tests (e.g., 1 of 25 vendor bank-detail changes) miss errors outside the sample. Manual
    comparison of account numbers and contract terms is error-prone.
  solution: >-
    Document extraction plus matching agents compare every change or invoice to its support and recalculate
    amounts, with every value linked to its source.
    - Armanino (with DataSnipper): validates vendor bank and payment-method changes monthly across the full
      population, ties invoice charges to contract terms, and matches deposits to reports. The auditor reviews
      each suggested match.
    - Microsoft IA: agents run full-population testing on high-risk data sets.
  outcomes:
    - {lever: quality, description: "Armanino tests 100% of vendor master changes rather than a sample", figure: "100% of population", source_ref: S42}
    - {lever: capacity, description: "Armanino estimate for a cash-receipts reconciliation test", figure: "25+ hours saved", source_ref: S42}
    - {lever: capacity, description: "Microsoft IA: automated assurance coverage expanded; internal QR effort cut", figure: "<30 to ~100 services automated; QR effort -~50%", source_ref: S10}
  prerequisites:
    - "Complete, reliable population data (incomplete population is a risk testing cannot fix)"
    - "Capacity to follow up the extra exceptions that full coverage surfaces"
  risks_and_guardrails:
    - "Do not market full-population testing as absolute assurance (expectation gap) (S46)"
    - "Deterministic code for calculations, agents for reading documents (S46)"
  human_checkpoints:
    - "Auditor reviews each flagged mismatch and suggested match before it stands"
  role_evolution: "Time moves from tick-and-tie to investigating exceptions and judging their significance."
  evidence_grade: A
  sources:
    - {ref: S42, title: "Three use cases for AI in internal audit (Armanino)", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/three-use-cases-for-ai-in-internal-audit", date: 2026-08-12}
    - {ref: S10, title: "AI solution overviews: Internal Audit", publisher: Microsoft (Frontier Finance), type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: FY2026}
    - {ref: S46, title: "Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/", date: 2026-10-15}
  last_reviewed: 2026-10-16
  notes: "Armanino is acting as a risk advisory provider on client SOX/IA engagements. Figures are practitioner estimates in a vendor story."

- id: assurance-controls-testing-10
  title: Continuous controls monitoring feeding SOX testing (test throughout the year)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  lens: improve
  ladder: automate
  runtime_class: background-agent
  maturity: in-production
  problem: >-
    Point-in-time testing finds failures months after they occur, often at year-end, when remediation costs
    most.
  solution: >-
    Scheduled queries and agents watch control data continuously and route exceptions to owners. Snowflake
    Internal Audit runs queries on Snowflake data through the Optro connector, with results shown in each
    control's view. Klaviyo tests throughout the year with Optro autonomous testing. Fieldguide agents can start
    automatically when evidence is uploaded.
  outcomes:
    - {lever: risk, description: "Klaviyo: catches issues earlier and fixes them sooner with control owners (qualitative)", figure: null, source_ref: S03}
    - {lever: speed, description: "Snowflake IA: reduced controls testing time and earlier remediation (qualitative)", figure: null, source_ref: S39}
  prerequisites:
    - "Control-relevant data in a queryable store; people who understand both the data and the risk design the queries"
    - "Start with one or two high-impact controls (Snowflake CAE advice)"
  risks_and_guardrails:
    - "Precision thresholds to avoid alert noise; named owners and SLAs for alerts (Grant Thornton)"
    - "Second/third-line independence: IA should test the first line's monitoring, not run it (KPMG)"
  human_checkpoints:
    - "Owner triage of each alert; auditor conclusion on operating effectiveness"
  role_evolution: "Internal audit moves toward testing the first line's monitoring rather than reperforming."
  evidence_grade: B
  sources:
    - {ref: S39, title: "How Snowflake Uses Continuous Monitoring to Proactively Identify Risk", publisher: Optro, type: vendor, url: "https://optro.ai/blog/snowflake-success-story", date: 2026}
    - {ref: S03, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14}
    - {ref: S23, title: "The power of AI in efficient SOX compliance", publisher: Grant Thornton, type: firm, url: "https://www.grantthornton.com/insights/articles/advisory/2025/the-power-of-ai-in-efficient-sox-compliance", date: 2025}
    - {ref: S32, title: "Field Agents for Testing", publisher: Fieldguide Help Center, type: vendor, url: "https://help.fieldguide.io/en/articles/12292640-field-agents-for-testing", date: 2026}
  last_reviewed: 2026-10-16
  notes: "Snowflake's CCM is query-based analytics more than GenAI. It is included because it is the data base agentic testing is built on."

- id: assurance-controls-testing-11
  title: AI secondary review of control-testing workpapers with multi-model cross-checks
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    CAE/manager review is a bottleneck, so small teams only re-review the riskiest workpapers. Completeness and
    consistency errors slip through ("the fiftieth workpaper").
  solution: >-
    FJ Management Internal Audit connects Claude to its Optro audit record through MCP. Versioned, activity-specific
    review prompts encode methodology, scope, severity taxonomy and evidence-sufficiency rules. Several models
    review the same walkthrough workpaper independently, and a reconciliation prompt flags where they disagree.
    A human checks the memo before it is attached to the workstep.
  outcomes:
    - {lever: quality, description: "Review memos attached to worksteps caught actual defects (qualitative); plan to move to 100% secondary review", figure: null, source_ref: S38}
  prerequisites:
    - "Audit record in structured fields, not Word/Excel attachments ('structured fields over attachments')"
    - "MCP or API access from enterprise AI tools to the audit system"
  risks_and_guardrails:
    - "Model disagreement treated as a signal for human investigation"
    - "Prompt versioning so the applied review standard is auditable"
    - "Rule: 'AI drafts and detects, but people decide' (FJ Management)"
  human_checkpoints:
    - "Human reviews each AI memo; severity, materiality and sign-off stay with auditors"
  role_evolution: "CAE review shifts from line-by-line checking to judgement calls; aim to remove the CAE review bottleneck."
  evidence_grade: B
  sources:
    - {ref: S38, title: "FJ Management advances its agentic audit strategy with Optro", publisher: Optro, type: vendor, url: "https://optro.ai/blog/fj-management-success-story", date: 2026}
    - {ref: S10, title: "AI solution overviews: Internal Audit", publisher: Microsoft (Frontier Finance), type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: FY2026}
  last_reviewed: 2026-10-16
  notes: "Microsoft IA separately reports internal quality review effort cut by about 50%, not attributed to a specific tool."

- id: assurance-controls-testing-12
  title: Matching client-provided evidence to selected samples during external-audit fieldwork
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  lens: improve
  ladder: automate
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Sample selections can run to hundreds of items. Each PBC document must be traced and vouched to its sample
    by hand, and this backs up partner and EQR review.
  solution: >-
    Agents trace incoming PBC documents to the requested samples, extract and validate values, and record
    match/exception status with links back to the source.
    - Products: PwC Evidence Match (PwC plans to model controls-testing automation on it), Thomson Reuters
      Audit Intelligence Test (with Valid8), Fieldguide Audit Testing Agent, and DataSnipper.
    - Firms using them: Sanville & Co, Oberlander Financial Services and RMF Audit & Control.
  outcomes:
    - {lever: speed, description: "Oberlander Financial Services (TR Audit Intelligence Test): sample-to-evidence testing per engagement", figure: "~16 hours to 5-6 hours", source_ref: S45}
    - {lever: speed, description: "Sanville & Co: sample selections of hundreds of transactions 'down to minutes' in many cases", figure: null, source_ref: S34}
    - {lever: growth, description: "Sanville & Co blended realization on lowest-margin engagements", figure: "$150-200/hr to $250+/hr", source_ref: S34}
    - {lever: quality, description: "Sanville's first PCAOB inspection on the platform (broker-dealer) returned zero comment forms", figure: "0 comment forms", source_ref: S34}
    - {lever: speed, description: "RMF Audit & Control: test-of-details samples (60+ invoices) take roughly half the time; also used for tests of controls", figure: "~50%", source_ref: S44}
  prerequisites:
    - "Clients upload PBC through a portal or tool the firm can read; methodology templates in the platform"
  risks_and_guardrails:
    - "Accuracy is a binary yes/no metric for matching tools, so PwC can measure it (S18)"
    - "Clean inspection cannot be attributed to AI alone; it followed a full methodology overhaul"
  human_checkpoints:
    - "Auditor reviews each exception and signs off the test"
  role_evolution: >-
    Reviewer bandwidth is freed. At Sanville, first-year staff now do complex revenue testing under guidance.
    PwC hires engineers into assurance.
  evidence_grade: A
  sources:
    - {ref: S45, title: "Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html", date: 2025-11-05}
    - {ref: S34, title: "How Sanville & Co passed a PCAOB inspection with zero comment forms in under a year with Fieldguide", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/case-studies/how-sanville-co-passed-a-pcaob-inspection-with-zero-comment-forms-in-under-a-year-with-fieldguide", date: 2026}
    - {ref: S44, title: "RMF Audit & Control success story", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/rmf-audit-&-control", date: 2026}
    - {ref: S16, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28}
    - {ref: S18, title: "A look at PwC's 'next generation' audit", publisher: CFO Brew, type: press, url: "https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit", date: 2025-11-05}
  last_reviewed: 2026-10-16
  notes: "Shared with the substantive-testing module; most cited figures are tests of details. Tests of controls use the same step."

- id: assurance-controls-testing-13
  title: Big Four audit-platform agents extending into tests of controls in integrated audits
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  lens: delegate
  ladder: augment
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: >-
    External auditors repeat walkthroughs and tests of controls every year across very large engagement
    portfolios, at fixed or falling fees.
  solution: >-
    Firm platforms are adding agents:
    - Deloitte Omnia: agents run preliminary procedures (data extraction, evidence analysis, draft
      documentation and preliminary conclusions) for review.
    - EY Canvas: multi-agent framework embedded in all audit phases.
    - KPMG Clara: agents for substantive procedures, with controls-testing agents announced as next.
    - PwC: controls-testing automation planned on the Evidence Match pattern.
    - Grant Thornton Gtap: agents, starting with private-company audits.
  outcomes:
    - {lever: speed, description: "PwC: year-one AI time savings in assurance are a 'shift' and 'not that drastic yet'", figure: null, source_ref: S17}
    - {lever: capacity, description: "EY: platform covers 130,000 assurance staff and 160,000 engagements; end-to-end support targeted by 2028", figure: "130,000 staff; 2028", source_ref: S20}
  prerequisites:
    - "Central platform, certified tools under ISQM 1 / QC 1000, global training"
  risks_and_guardrails:
    - "Firms call these preliminary conclusions; auditors keep the opinion"
    - "UK regulator found GenAI at the six largest firms limited to productivity aids, not certified ATTs, as of mid-2025 (S55)"
  human_checkpoints:
    - "Engagement team reviews every agent conclusion; partner signs"
  role_evolution: "Deloitte 'tutor mode' gives micro-training during work; firms hire engineers and dual-track CPA/data science staff."
  evidence_grade: B
  sources:
    - {ref: S21, title: "Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit & Assurance", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24}
    - {ref: S20, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: 2026-04-07}
    - {ref: S14, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: 2025-04}
    - {ref: S17, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07}
    - {ref: S22, title: "Grant Thornton launches AI platform for audit business", publisher: Consultancy.us, type: press, url: "https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business", date: 2026-05-11}
  last_reviewed: 2026-10-16
  notes: >-
    Platforms are deployed; their use in tests of controls specifically is announced or planned, not evidenced.
    KPMG's April 2025 promise of controls-testing agents "over the next 12 months" was not confirmed as shipped.
    EY "now vs 2028": agents are embedded in all phases now, with full end-to-end support targeted for 2028.

- id: assurance-controls-testing-14
  title: AI-native audit pilot where agents test controls and balances on full populations
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: end-to-end-case-agent
  lens: reinvent
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Sampling-based audits spend most hours on data gathering and documentation rather than judgement."
  solution: >-
    PwC Australia's AI-native audit platform has agents assess risk, design audit plans and workflows, and test
    balances and controls in real time on full populations. Auditors handle context, communication and final
    judgements. The pilot is part of a global programme.
  outcomes:
    - {lever: quality, description: "Pilot scope and rollout plan", figure: "5 audit clients initially; all clients by 2028; 1,600 auditors", source_ref: S19}
  prerequisites:
    - "Client data access for full populations; firm-level certification of the platform"
  risks_and_guardrails:
    - "Over-reliance on AI over professional judgement flagged as a quality risk by a commentator in the same article"
  human_checkpoints:
    - "Human auditors provide oversight and validation of all agent work"
  role_evolution: "Auditors move to insight and review; data gathering shrinks."
  evidence_grade: B
  sources:
    - {ref: S19, title: "PwC Australia rolls out pilot program for AI-assisted full audits", publisher: Accounting Times, type: press, url: "https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits", date: 2025-10-28}
  last_reviewed: 2026-10-16
  notes: "Pilot clients were described as lower-risk in the landscape. The fetched article does not say so, so that detail is not confirmed."

- id: assurance-controls-testing-15
  title: Testing ITGCs and controls over AI components and agents inside client processes
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  lens: improve
  ladder: assist
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Clients now use AI and agents in processes that matter to ICFR, such as matching, approvals and ERP agents.
    Audit programmes have mostly tested around the AI, and no accepted method exists for testing black-box
    controls.
  solution: >-
    Auditors scope the AI components (model, data pipelines, orchestration, agents, platforms) per use case.
    They decide whether management relies on AI output (the COSO "reliance" concept) and extend access,
    change-management and operations ITGCs to those components. For example, they check that ERP user
    access reviews cover native, UI-driven and headless agents. KPMG UK is introducing a SOC 2+ opinion on AI
    governance and controls.
  outcomes:
    - {lever: risk, description: "KPMG expects the first AI-related material weaknesses to appear in 2027", figure: "2027 (forecast)", source_ref: S11}
  prerequisites:
    - "Client AI inventory and use-case mapping; IT audit specialists who can read model/agent logs"
  risks_and_guardrails:
    - "Model drift can make an effective control ineffective with no visible system change (KPMG)"
    - "A human approval that rubber-stamps AI output adds no control value (KPMG)"
  human_checkpoints:
    - "IT audit specialist judgement on scoping and reliance"
  role_evolution: "IT auditors need to be as comfortable in configuration and model logs as in a ledger."
  evidence_grade: C
  sources:
    - {ref: S48, title: "Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls", publisher: BDO USA, type: firm, url: "https://www.bdo.com/insights/assurance/artificial-intelligence-it-audit-considerations-with-focus-on-information-technology-general-control", date: 2026-07-20}
    - {ref: S11, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026}
    - {ref: S13, title: "Reimagining Controls Assurance with AI: Latest Insights for Leaders", publisher: KPMG in the UK, type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf", date: 2026-01}
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': audit of an AI-enabled control (assurance over agents). It is a new test object, not AI used by the auditor."

- id: assurance-controls-testing-16
  title: AI review of third-party SOC reports for user-entity reliance
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: document-to-decision
  lens: improve
  ladder: assist
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    SOX programmes and auditors read many vendor SOC 1/SOC 2 reports to extract scope, exceptions, bridge
    letters and complementary user-entity controls, then compare them to their own risk assessments.
  solution: >-
    Agents extract control descriptions and test results from SOC reports, compare them with the user's risk
    assessment and prior periods, and flag deviations.
  outcomes:
    - {lever: speed, description: "Described as a current application by EY and KPMG; no deployment figures found", figure: null, source_ref: S41}
  prerequisites:
    - "Repository of vendor SOC reports and CUEC mapping"
  risks_and_guardrails:
    - "Traditional SOC review was not designed for vendor AI risk (KPMG)"
  human_checkpoints:
    - "Control owner/auditor concludes on reliance and CUEC coverage"
  role_evolution: "Less reading time; more vendor-risk judgement."
  evidence_grade: C
  sources:
    - {ref: S41, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09}
    - {ref: S12, title: "Seize the future: The agentic shift in SOX compliance", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html", date: 2025-08}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-17
  title: Agent-assisted evidence requests and PBC quality checks before testing starts
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [coordination-scheduling, client-interaction]
  pattern: intake-triage
  lens: improve
  ladder: augment
  runtime_class: background-agent
  maturity: piloting
  problem: >-
    Chasing evidence is a main source of SOX delay. One practitioner estimates that about one in five PBC
    requests comes back wrong the first time.
  solution: >-
    Agents draft requests, check submitted evidence for completeness, file integrity and format, flag gaps, and
    help preparers fix them before submission. KPMG argues automated evidence collection may pay back sooner
    than automated testing.
  outcomes:
    - {lever: speed, description: "Optro agent reduces evidence follow-up by clarifying requests before submission (vendor claim; automated evidence collection 'upcoming')", figure: null, source_ref: S03}
    - {lever: speed, description: "Frazier & Deeter: evidence requests faster with Fieldguide (search extract only)", figure: "~8% faster (19 hours)", source_ref: S61}
  prerequisites:
    - "Evidence embedded in workflows or standard repositories that tools can read (KPMG)"
  risks_and_guardrails:
    - "Completeness and accuracy of client-provided information remains the auditor's responsibility"
  human_checkpoints:
    - "Auditor accepts the evidence as sufficient before testing"
  role_evolution: "Less status-chasing; clients see live request status (Weaver, Sanville)."
  evidence_grade: C
  sources:
    - {ref: S03, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14}
    - {ref: S02, title: "RSM Beacon | Automated control testing platform", publisher: RSM US, type: firm, url: "https://rsmus.com/services/risk-fraud-cybersecurity/automated-control-testing.html", date: 2026}
    - {ref: S11, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026}
    - {ref: S47, title: "5 Questions to Ask Before Your SOX Team Adopts AI Agents", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188703", date: 2026-08-18}
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-18
  title: Risk-scored sample and coverage selection by an agent
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: intake-triage
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Sample and coverage choices rely on static lists and judgement that is hard to explain or adapt.
  solution: >-
    Microsoft IA's Sample Selection Agent (M365 Copilot) scores risk across revenue, discounts, country risk and
    control indicators to choose coverage. AuditBoard/Optro offers AI risk-based sample selection for control
    testing.
  outcomes:
    - {lever: capacity, description: "Microsoft IA Sample Selection Agent", figure: "weeks of analysis to one day; ~2K hours/year", source_ref: S10}
  prerequisites:
    - "Risk indicators available as data; documented selection rationale"
  risks_and_guardrails:
    - "Statistical sampling rules (e.g., AS 2315 / ISA 530) still govern external-audit samples; agent scoring is an input"
  human_checkpoints:
    - "Audit lead approves coverage and sample"
  role_evolution: "Planning judgement is documented as data rather than memory."
  evidence_grade: A
  sources:
    - {ref: S10, title: "AI solution overviews: Internal Audit", publisher: Microsoft (Frontier Finance), type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: FY2026}
    - {ref: S37, title: "AuditBoard Launches Accelerate, Delivering Enterprise-Grade AI Automation for GRC Teams", publisher: AuditBoard (now Optro), type: vendor, url: "https://auditboard.com/blog/auditboard-launches-accelerate-delivering-enterprise-grade-ai-automation-for-grc-teams", date: 2025-10-22}
  last_reviewed: 2026-10-16
  notes: "Microsoft's agent supports internal audit planning (partner audits), not SOX statistical sampling."

- id: assurance-controls-testing-19
  title: Orchestrated agent 'swarms' working alongside auditors in internal audit
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  lens: reinvent
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: >-
    Prompt libraries plateau. Nobody owns the prompts or measures their output, and one agent per task does not
    scale across an audit plan.
  solution: >-
    PayPal Internal Audit describes "swarm auditing". Teams of agents are orchestrated in parallel, with a
    defined framework for how agents and auditors collaborate. Scripts and agents built in audit are handed to
    first- and second-line owners, who own and modify them. The team keeps a separate bucket of hours for
    experimentation within the audit plan.
  outcomes:
    - {lever: capacity, description: "No figures published; experimentation hours budgeted separately from the audit plan", figure: null, source_ref: S49}
  prerequisites:
    - "Data science capability inside audit operations (PayPal analytics since 2016)"
  risks_and_guardrails:
    - "Independence: lines of defence blur when IA shares agents; handled by transferring ownership to the business"
    - "Vibe-coded tools skip basics, so ITGCs over audit's own AI matter more"
  human_checkpoints:
    - "Auditors remain the decision layer; agents not replacing the team near-term"
  role_evolution: "New roles such as data science manager in audit operations; auditors orchestrate agents."
  evidence_grade: B
  sources:
    - {ref: S49, title: "Preparing Audit Teams for Swarm Auditing (All Things Internal Audit podcast, with PayPal CAE and Data Science Manager)", publisher: The IIA, type: podcast, url: "https://www.theiia.org/en/content/podcast/all-things-internal-audit/2026/ep-0107/", date: 2026-01-28}
    - {ref: S47, title: "5 Questions to Ask Before Your SOX Team Adopts AI Agents", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188703", date: 2026-08-18}
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': multi-agent orchestration with a defined human-agent collaboration layer across audit work."

- id: assurance-controls-testing-20
  title: Encoding SOX testing judgement into agent evaluation sets (practitioner-in-the-loop development)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [software-systems, expert-judgment]
  pattern: other
  lens: improve
  ladder: assist
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    A model that is right 95% of the time is unusable if no one can tell which 5% to check. Agent conclusions
    must be repeatable and defensible under PCAOB review.
  solution: >-
    Vendors hire experienced SOX testers to write decision rules, run controls through agents, document failure
    modes, define ground truth per control type and build versioned evaluation sets. Engineers use those sets to
    run regression tests before changing prompts, models or tools.
  outcomes:
    - {lever: quality, description: "Fieldguide contract role: 8-12 weeks, $60-80/hour, requires 4+ years control testing", figure: null, source_ref: S50}
    - {lever: quality, description: "Nace.AI seeks ex-Big Four SOX managers to judge when AI output 'only looks right'", figure: null, source_ref: S52}
  prerequisites:
    - "Real workpapers and labelled outcomes across control types (reconciliations, MRCs, access reviews, SoD)"
  risks_and_guardrails:
    - "Same evidence should produce the same conclusion every time (Fieldguide engineering brief)"
  human_checkpoints:
    - "Expert sign-off on evaluation criteria before release"
  role_evolution: "New role: SOX practitioner as AI evaluator or prompt engineer, not client delivery."
  evidence_grade: B
  sources:
    - {ref: S50, title: "SOX AI Specialist (Contractor)", publisher: Fieldguide (via Built In), type: job-posting, url: "https://www.builtinla.com/job/sox-ai-specialist-contractor/10443759", date: 2026-08}
    - {ref: S51, title: "Software Engineer, Internal Audit (All Levels)", publisher: Fieldguide (via Jobicy), type: job-posting, url: "https://jobicy.com/jobs/154197-software-engineer-internal-audit-all-levels", date: 2026-10}
    - {ref: S52, title: "SOX Audit Expert", publisher: Nace.AI (General Catalyst job board), type: job-posting, url: "https://jobs.generalcatalyst.com/companies/nace-ai-2/jobs/74116857-sox-audit-expert", date: 2026}
    - {ref: S47, title: "5 Questions to Ask Before Your SOX Team Adopts AI Agents", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188703", date: 2026-08-18}
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': human-labelled evaluation harness for audit agents. Job pages carry AI-generated summaries; only the posting text was used."
```

**Use-case count by grade:** **A: 6** (01, 02, 07, 09, 12, 18) · **B: 10** (03, 04, 05, 06, 10, 11, 13, 14, 19, 20) · **C: 4** (08, 15, 16, 17) · **D: 0**. Every A-grade figure is self-reported by the deploying organisation, usually in vendor-published material.

---

## 3. Module notes

### Processes and key steps (with work types)

| Step | What happens | Work types | AI activity seen (use case) |
|---|---|---|---|
| Scoping / RCM | Select key controls, link risks, set attributes | expert-judgment | Test-plan drafting, control wording scores (06) |
| Walkthrough / test of design | Trace a transaction, confirm design and implementation, document narrative | research-synthesis, document-production | Walkthrough assistants, transcription, narratives (05) |
| Evidence request (PBC) | Request, chase and validate support | coordination-scheduling, client-interaction | Request drafting, completeness checks (17) |
| Sample selection | Statistical or judgemental selection, or full population | data-reporting, expert-judgment | Risk-scored coverage (18); full-population tests (09) |
| Test of operating effectiveness | Attribute testing per sample, tick-marking | review-assurance, transaction-processing | Agentic attribute testing (01, 02, 03, 04, 12) |
| ITGC testing | Access, change, operations; increasingly over AI components | review-assurance | Change-ticket agent (02); ITGCs over AI (15) |
| Deviation / deficiency evaluation | Exception vs missing support, severity, aggregation | expert-judgment | Mostly human; AI flags exceptions, drafts responses (08) |
| Documentation and review | Workpapers, secondary review, sign-off | document-production, review-assurance | Workpaper generation (01); AI secondary review (11) |
| SOC-specific | Section 3, CUECs, user-entity reliance | document-production, research-synthesis | (07, 08, 16) |

### Common pain points
- Testing hours per control rose from 12 (FY2022) to 16 (FY2024). SOX cost rose 45% between KPMG's 2023 and 2025 surveys. ITGCs and transactional controls take the most time (S11).
- Evidence arrives in mixed, unstructured formats: PDFs, merged-cell Excel, screenshots, scans. This "broke" RPA (S04, S47).
- Testers on co-sourced engagements change each year, which hurts consistency. Co-source spend is significant: 58% say it exceeds 20% of the SOX budget (S05, S11).
- Reviewer and EQR bottlenecks; CAE review limits how many workpapers get a second review (S34, S38).
- Distinguishing missing documentation from a real exception (S24).
- In SOC work: 90% of operating-effectiveness exceptions fall on manual controls, and 39% on system access and authorisation (KPMG UK benchmark of 180+ reports) (S13).

### Metrics and benchmarks
- **Baselines.**
  - KPMG 2025 SOX Survey: 16 testing hours per control. 52% of internal audit departments spend over 40% of their hours on SOX (S11).
  - Zanin, citing KPMG: average programme $2.3M and over 15,000 hours a year, about 40% of it on testing (S47).
  - a16z (investor claim): SOX testing is $8B a year of US spend (S27).
- **Measured outcomes (all self-reported):**
  - Reddit: -60% time per control; 175 controls in 90 days (S03, S04).
  - Microsoft: 850 hours and $185K a year from one ITGC agent (S09).
  - KPMG UK SOC engagements: ~18% less testing time; ~15% with DataSnipper alone (S13).
  - Oberlander: 16 hours to 5–6 hours for sample-to-evidence testing (S45).
  - Sanville: realisation up from $150–200 to $250+ an hour (S34).
  - Armanino: 25+ hours saved on one reconciliation test (S42).
- **Vendor claims (grade C):**
  - Petual: 68–80% efficiency gains (S28).
  - Andera: "save 70% of time on any control" (S26).
  - Fieldguide: up to 70% of financial audit testing automated (S33).
  - Midship/Optro: up to 87% of SOX programme management automated (S06).
- **Adoption benchmarks.**
  - IFIAR 2024: automated tools frequently seen in **internal controls testing** by only 43% of member regulators, against 88% for journal-entry testing (S56).
  - Gartner, Aug 2026: 30% of audit functions use AI for audit testing (search extract only, S62).
  - CPA.com, Dec 2025: about one-third of 54 US firms do not use AI at all, and 41% expect advanced technology to reduce the need for sampling (S57).
- **Recommended measures beyond hours:**
  - Baseline hours per control, PBC follow-up rate, rework, time to a final workpaper, and whether the old and new runs caught the same exceptions (S47).
  - Exception-detection rate and evidence completeness (S23).
  - Accuracy for binary matching tools (PwC, S18).

### Guardrails and regulatory points
- **Human review at set stages is universal in deployments.** Typical set-up: approve the plan, review extraction, then review conclusions and sign off. Examples: RSM, Riveron, Fieldguide's step-by-step mode, Havertys (S02, S24, S32, S05).
- **Evidence traceability.** Every attribute is linked to a location in the source document (Microsoft tick-marking agent; DataSnipper; Fieldguide citations). Zanin frames AS 1215 as the bar in the absence of PCAOB AI guidance (S47).
- **Tool certification.** UK firms certify automated tools before deployment and pilot them first, sometimes on lower-risk non-PIE audits. In mid-2025 the FRC found GenAI at the six largest firms limited to productivity aids and asked for AI-specific certification steps (S55).
- **Inspection findings:** automated tools not used as intended (31% of IFIAR members), misread outputs, weak outlier follow-up, and thin ITGC testing (S56).
- **New test object.** Under COSO's reliance concept, ITGCs over AI components and agents must be scoped. Example: do ERP user access reviews cover agent identities? (S48).
- **Adversarial evidence.** Testing agents need defences against instructions hidden in control evidence (S11).
- **No blanket approval of AI-driven SOX testing from external auditors or regulators.** Practitioners advise involving the external auditor early and running a parallel pilot (S23, S47).

### Frontier signals (dated, sourced)
- **2026-10-14:** Optro extends autonomous testing beyond SOX to operational audit across all control types. Automated evidence collection is announced as upcoming (S03).
- **2026-10-08:** Optro survey of 417 GRC and audit leaders:
  - 38% let agents approve or reject transactions.
  - 34% let agents modify controls or policies.
  - Only 9% have redesigned workflows for agents (S40).
- **2026-10-07:** PwC enters 2026 year-end audits with AI tools for document review and walkthroughs. Savings so far are modest (S17).
- **2026-09-15:** Workiva launches evidence, attribute and testing agents for internal audit and GRC (S36).
- **2026-08-26:** RSM Beacon with Andera launches, with SOC and ICFR testing in scope (S01, S02).
- **2026 (KPMG Future of SOX):**
  - The first AI-related material weaknesses are expected in 2027.
  - External auditors' own full-population testing may reduce reliance on management's tests, or increase it if management's AI testing is stronger (S11).
- **2026-06/05/04/02 (funding and consolidation):**
  - Andera $37M (S25).
  - Midship acquired by Optro four months after its $4.15M seed round (S06, S08).
  - Petual $20M (S28).
  - Fieldguide $75M (S30).
  - Arden (YC, 2026) launches as an "AI-native internal audit firm" (S54).
- **2026-01:** KPMG UK introduces a reasonable-assurance "SOC 2+" opinion over AI governance and controls (S13).
- **2025-10:** PwC Australia AI-native audit pilot with agents testing controls on full populations; rollout to all clients by 2028 (S19).

### Workforce and role effects
- **Testers become reviewers.**
  - "Human review... is where most of the auditor's time now goes" (S47).
  - The Fieldguide Agent Review Experience packages outputs, citations and sign-off per control (S32).
- **Co-source economics change.** Havertys plans to move external spend from testing hours to advisory (S05). One Petual customer said they cut budget "to a quarter" (S27).
- **New roles:**
  - SOX practitioners hired by vendors to write evaluation criteria and document failure modes (S50, S52).
  - Data science managers inside audit operations (PayPal, S49).
  - Engineers hired into assurance at PwC, which also seeks dual-track CPA plus data/computer science profiles (S16, S18).
- **Faster progression for juniors.** At Sanville, first-year staff now do complex revenue testing because reviewers have time to guide them (S34).
- **Training at point of work.** Deloitte's "tutor mode" gives micro-training in context (S21). EY runs a global upskilling programme (S20).
- **Long-run talent model (KPMG).** The current approach (recruit accounting graduates, then train for years) "will not produce" the hybrid professionals needed (S11).

### Objections and concerns practitioners raise
- **Reliability and non-determinism:** "a model that is right 95% of the time is useless if you cannot tell which 5% to check" (S47).
- **Rubber-stamp human-in-the-loop:** an approval step that accepts every AI recommendation "provides no real control value" (S11).
- **Review burden can rise rather than fall:** 46% say staff spend more time validating AI output (S40).
- **Overselling full-population testing:** it is still reasonable assurance. It also surfaces more exceptions, which need follow-up capacity (S46).
- **External auditor acceptance is uncertain:** there is no PCAOB AI standard, and the staff's 2024 observations never became guidance (S47, S23).
- **Savings slower than promised:** PwC's year-one savings are "not that drastic yet" (S17).
- **Independence:** internal audit sharing agents or scripts with the first and second lines (S49). Internal audit running first-line monitoring instead of testing it (S11).
- **Messy evidence and data quality** decide success: "Agentic capability is only as good as your field discipline" (S38).

### Interview probes for an advisor
1. **Pilot design:**
   - Which controls did you pilot agents on first, and why those?
   - Did you run old and new testing in parallel on the same controls?
   - Did both runs catch the same exceptions?
2. **External auditor reliance:** Has your external auditor relied on agent-produced workpapers for any key control? What did they ask to see: plan, extraction trail, reasoning, reviewer sign-off?
3. **Review effort:** What share of reviewer time now goes to checking agent output? Has total review time per control gone up or down? How do you decide which agent conclusions to re-perform?
4. **Co-sourcing:** How has your co-source or outsourcing spend changed, and which work did you bring in-house first (ITGCs, business-process controls)?
5. **Agent failures:** What failure modes have you seen, such as missing support treated as an exception, wrong sample mapping or misleading evidence? How do you log them and feed them back into prompts or evaluation sets?

---

## 4. Sources

Read in full unless marked `(search extract only)`.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| S01 | Andera and RSM US Partner to Create AI-Enabled Control Testing Platform for Internal Audit | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/ | 2026-08-26 |
| S02 | RSM Beacon: Automated control testing platform | RSM US | firm | https://rsmus.com/services/risk-fraud-cybersecurity/automated-control-testing.html | 2026 (undated page) |
| S03 | Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance | Optro | vendor | https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance | 2026-10-14 |
| S04 | How we used agentic AI to crack automated SOX testing at scale... in 90 days (M. Preedy, Reddit; mirror of r/RedditEng post) | Tenu Tech Brief / Reddit | community | https://cluster-site.onrender.com/posts/how-we-used-agentic-ai-to-crack-automated-sox-testing-at-scale...-in-90-days/ (original: https://www.reddit.com/r/RedditEng/comments/1rcnk7d/) | 2026-02-23 |
| S05 | Four years in, Havertys expands its use of Optro with agentic AI for controls testing | Optro | vendor | https://optro.ai/blog/havertys-furniture-success-story | 2026 (undated page) |
| S06 | Optro Leads the Global Audit Transformation with the Acquisition of AI-Native Midship | Optro | vendor | https://optro.ai/blog/optro-leads-the-global-audit-transformation-with-the-acquisition-of-ai-native-midship | 2026-05-06 |
| S07 | Why autonomous controls testing will redefine internal audit (K. Taylor) | Optro | vendor | https://optro.ai/blog/autonomous-controls-testing-internal-audit | 2026-06-15 |
| S08 | Midship Raises $4.15M to Automate SOX Testing with Agentic AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/01/27/midship-raises-4-15m-to-automate-sox-testing-with-agentic-ai/176932/ | 2026-01-27 |
| S09 | Innovation Story: SOX Change Management Testing Agent | Microsoft (Frontier Finance) | firm | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf | FY2026 |
| S10 | AI solution overviews: Internal Audit | Microsoft (Frontier Finance) | firm | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf | FY2026 |
| S11 | The Future of SOX: A point of view for 2030 and beyond | KPMG LLP | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf | 2026 |
| S12 | Seize the future: The agentic shift in SOX compliance | KPMG LLP | firm | https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html | 2025-08 |
| S13 | Reimagining Controls Assurance with AI: Latest Insights for Leaders | KPMG in the UK | firm | https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf | 2026-01 |
| S14 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04 |
| S15 | KPMG builds AI agents into audit platform | Accounting Today | press | https://www.accountingtoday.com/news/kpmg-builds-ai-agents-into-audit-platform | 2025-04-24 |
| S16 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 |
| S17 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 |
| S18 | A look at PwC's 'next generation' audit | CFO Brew | press | https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit | 2025-11-05 |
| S19 | PwC Australia rolls out pilot program for AI-assisted full audits | Accounting Times | press | https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits | 2025-10-28 |
| S20 | EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 |
| S21 | Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit & Assurance | Deloitte Global | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 |
| S22 | Grant Thornton launches AI platform for audit business | Consultancy.us | press | https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business | 2026-05-11 |
| S23 | The power of AI in efficient SOX compliance | Grant Thornton | firm | https://www.grantthornton.com/insights/articles/advisory/2025/the-power-of-ai-in-efficient-sox-compliance | 2025 |
| S24 | AI in Internal Audit and SOX: Applying Methods that Work | Riveron | firm | https://riveron.com/ai-in-internal-audit-and-sox-applying-methods-that-work/ | 2026-06-16 (upd. 2026-09-17) |
| S25 | Andera raises $37m to automate internal audit | FinTech Global | press | https://fintech.global/2026/06/22/andera-raises-37m-to-automate-internal-audit/ | 2026-06-22 |
| S26 | Andera: Automate your controls testing with AI (homepage) | Andera | vendor | https://www.andera.ai/ | accessed 2026-10-16 |
| S27 | Investing in Petual | Andreessen Horowitz | vendor | https://a16z.com/announcement/investing-in-petual/ | 2026-04-23 |
| S28 | Petual raises $20m for AI-powered SOX compliance | FinTech Global | press | https://fintech.global/2026/04/24/petual-raises-20m-for-ai-powered-sox-compliance/ | 2026-04-24 |
| S29 | Petual: Automate SOX Testing with AI (homepage) | Petual | vendor | https://www.petual.ai/ | accessed 2026-10-16 |
| S30 | Fieldguide raises $75M on $700M valuation to scale agentic AI for audit and advisory firms | SiliconANGLE | press | https://siliconangle.com/2026/02/02/fieldguide-raises-75m-700m-valuation-scale-agentic-ai-audit-advisory-firms/ | 2026-02-02 |
| S31 | AI in Internal Controls Testing: A Practical Framework | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/ai-internal-controls-audit-automation | 2026 (undated) |
| S32 | Field Agents for Testing | Fieldguide Help Center | vendor | https://help.fieldguide.io/en/articles/12292640-field-agents-for-testing | accessed 2026-10-16 |
| S33 | Increase Capacity and Audit Quality with Field Agents for Financial Audit | Fieldguide | vendor | https://www.fieldguide.io/blog/increase-capacity-and-audit-quality-with-field-agents-for-financial-audit | 2025-06 |
| S34 | How Sanville & Co passed a PCAOB inspection with zero comment forms in under a year with Fieldguide | Fieldguide | vendor | https://www.fieldguide.io/case-studies/how-sanville-co-passed-a-pcaob-inspection-with-zero-comment-forms-in-under-a-year-with-fieldguide | 2026 (undated) |
| S35 | Weaver scales GRC services with Fieldguide to deliver transparency and accelerate growth | Fieldguide | vendor | https://www.fieldguide.io/case-studies/weaver-scales-grc-services-with-fieldguide-to-deliver-transparency-and-accelerate-growth | 2026 (undated) |
| S36 | Workiva Advances Regulatory Work with AI Innovation | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/09/15/workiva-advances-regulatory-work-with-ai-innovation/190227/ | 2026-09-15 |
| S37 | AuditBoard Launches Accelerate, Delivering Enterprise-Grade AI Automation for GRC Teams | AuditBoard (now Optro) | vendor | https://auditboard.com/blog/auditboard-launches-accelerate-delivering-enterprise-grade-ai-automation-for-grc-teams | 2025-10-22 |
| S38 | FJ Management advances its agentic audit strategy with Optro | Optro | vendor | https://optro.ai/blog/fj-management-success-story | 2026 (undated) |
| S39 | How Snowflake Uses Continuous Monitoring to Proactively Identify Risk | Optro | vendor | https://optro.ai/blog/snowflake-success-story | undated |
| S40 | One in Three Organizations Say They Have Acted on Wrong Decisions Made by AI Agents (Authority without oversight: 2026 agentic enterprise report) | Optro | survey | https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds | 2026-10-08 |
| S41 | How AI assurance builds trust with SOC, attestation and certification (14th EY SOC conference highlights) | EY | conference | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf | 2026-09 |
| S42 | Three use cases for AI in internal audit (Armanino) | DataSnipper | vendor | https://www.datasnipper.com/resources/three-use-cases-for-ai-in-internal-audit | 2026-08-12 |
| S43 | The ODP Corporation success story | DataSnipper | vendor | https://www.datasnipper.com/resources/the-odp-corporation | undated |
| S44 | RMF Audit & Control success story | DataSnipper | vendor | https://www.datasnipper.com/resources/rmf-audit-&-control | undated |
| S45 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html | 2025-11-05 |
| S46 | Testing Every Transaction Changes the Audit: What Firms Should Know Before They Sell It (T. Adewole, Ledgerline) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/ | 2026-10-15 |
| S47 | 5 Questions to Ask Before Your SOX Team Adopts AI Agents (A. Zanin) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=188703 | 2026-08-18 |
| S48 | Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls | BDO USA | firm | https://www.bdo.com/insights/assurance/artificial-intelligence-it-audit-considerations-with-focus-on-information-technology-general-control | 2026-07-20 |
| S49 | Preparing Audit Teams for Swarm Auditing (All Things Internal Audit, with PayPal) | The IIA | podcast | https://www.theiia.org/en/content/podcast/all-things-internal-audit/2026/ep-0107/ | 2026-01-28 |
| S50 | SOX AI Specialist (Contractor) | Fieldguide via Built In | job-posting | https://www.builtinla.com/job/sox-ai-specialist-contractor/10443759 | 2026 (removed 2026-08-26) |
| S51 | Software Engineer, Internal Audit (All Levels) | Fieldguide via Jobicy | job-posting | https://jobicy.com/jobs/154197-software-engineer-internal-audit-all-levels | 2026 |
| S52 | SOX Audit Expert | Nace.AI via General Catalyst job board | job-posting | https://jobs.generalcatalyst.com/companies/nace-ai-2/jobs/74116857-sox-audit-expert | 2026 |
| S53 | Midship company page | Y Combinator | vendor | https://www.ycombinator.com/companies/midship | 2024–2025 |
| S54 | Arden: AI-native internal audit firm | Y Combinator | vendor | https://www.ycombinator.com/companies/arden | 2026 |
| S55 | Thematic Review: Certification of Automated Tools and Techniques | Financial Reporting Council (UK) | regulator | https://www.frc.org.uk/docs/8383/html/ | 2025-06-26 |
| S56 | Use of technology in audits: observations, risks and further evolution (IFIAR Technology Task Force) | IFIAR (hosted by Japan FSA) | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03 |
| S57 | 2025 Audit Transformation Report (CPA.com and AICPA Audit Benchmark Survey) | CPA.com / AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 |
| S58 | The Audit Podcast: episode listing (incl. Ep 291 "Pioneering in the AI Front w/ Martin Preedy (Reddit)"; Ep 296 Richard Penfil) | The Audit Podcast (via Deezer) | podcast | https://www.deezer.com/us/show/1001041832 | 2026 |
| S59 | How Helvetia Baloise gave internal audit room to focus on risk | Optro | vendor | https://optro.ai/blog/helvetia-baloise-success-story | 2026 (undated) |
| S60 | Dynamic controls testing (search extract only; pwc.com blocked) | PwC US | firm | https://www.pwc.com/us/en/tech-effect/ai-analytics/dynamic-controls-testing.html | 2026 |
| S61 | Frazier Deeter reclaims the judgment work at the heart of HITRUST (search extract only; page 404) | Fieldguide | vendor | https://www.fieldguide.io/case-studies/frazier-deeter-reclaims-the-judgment-work-at-the-heart-of-hitrust | 2026 |
| S62 | Gartner Survey Finds Audit Teams' AI Use Is Common but Most Lack Strategy (search extract only; 403) | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2026-08-10-gartner-survey-finds-audit-teams-ai-use-is-common-but-most | 2026-08-11 |

**Count by type (S01–S62):**

| Type | Count |
|---|---|
| vendor | 24 |
| press | 15 |
| firm (incl. in-house teams) | 13 |
| job-posting | 3 |
| survey | 3 |
| podcast | 2 |
| regulator | 2 |
| conference | 1 |
| community | 1 |
| professional-body | 0 |
| academic | 0 |

59 sources were read in full or in substance. 3 were seen in search extracts only (S60–S62). A few others were seen in search results only and are not listed. Among them: the Protiviti 2025 SOX poll, the CSA SOC 2 AI gap note, the Midship–Reddit details on usebead.ai, and the Podcast Addict description of Ep 291 (which says Reddit automates "70% of recurring SOX testing").

---

## 5. Gaps

**Unreachable (technical):**
- **pwc.com:** HTTP 403 by curl, DNS failure by WebFetch, and blocked by the r.jina.ai reader. The PwC dynamic controls testing page, including its claimed 30–40% effort reduction, was seen only in search extracts.
- **gartner.com newsroom:** 403 on both the main domain and the mirror. The Aug and Sep 2026 figures come from search extracts.
- **reddit.com:** 403. Reddit's own r/RedditEng post was read only through a third-party mirror, which carried the summary and opening section. The full "lessons learned" text was not reachable.
- **Other refusals:**
  - blog.protiviti.com and tcblog.protiviti.com (403): the 2025 SOX poll and the Copilot-for-internal-audit post.
  - businesswire.com (403): the Workiva 2025 StoneX quote.
  - accountingweb.co.uk (403): the FGMK/DataSnipper Alwin story.
  - goingconcern.com (403).
  - labs.cloudsecurityalliance.org (403).
  - podcastaddict.com (403).
  - web.archive.org (connection reset).
- **Broken page:** Fieldguide's Frazier Deeter and LSL case-study pages returned 404.

**Not found:**
- **Independent measurement.** No grade-A outcome comes from anyone other than the deploying organisation or its vendor. There are no error rates or precision figures for agent testing against human testers, and no audit-quality outcomes.
- **External auditor reliance on AI-tested work.** No public case was found where an external auditor stated it relied on management's or internal audit's AI-agent workpapers. Reliance remains the key open question.
- **Big Four controls-testing launches.** No confirmation that KPMG's announced Clara controls-testing agents shipped (promised within 12 months of April 2025). No PwC controls-testing release confirmed beyond the "planned" status in Oct 2025. EY and Deloitte do not name controls testing specifically.
- **Named failures.** No public case of an AI controls-testing deployment failing or being rolled back. Failure evidence is limited to vendor survey data (S40), IFIAR's general findings on automated tools (S56) and practitioner warnings.
- **SOC firms.** Little evidence on how specialist SOC firms (e.g., Schellman, A-LIGN, BARR) use AI in their own testing. Only KPMG UK and Fieldguide/Frazier Deeter (search extract) were found.
- **Small practices.** Beyond Sanville, Oberlander and RMF (all vendor stories), there is little on firms outside the top 100.
- **Workiva customer outcomes.** No named customer outcome for Workiva's testing agents. Newell Brands' CAE quote is about change management, not results.
- **Supporting sources.** Academic studies of LLM-based tests of controls were not pursued (governance/evidence angle). A Polish yearbook study (8 tests on 167 items) was seen in search only.

**Landscape conflicts resolved:**
- **Microsoft "850 vs 50 hours":** 850 in both PDFs. The 50 came from a text-extraction artefact.
- **EY "now vs 2028":** agents are embedded in all phases from April 2026; full end-to-end support is targeted by 2028.
- **Reddit:** the vendor's 175 controls and 60% figures match the CAE's own post. Expansion to over 75% of SOX controls is reported only by Optro.
