# Deep dive: assurance / completion-reporting / practice

- **Archetype:** assurance (external audit and other assurance)
- **Module:** completion-reporting. Disclosure checklists and financial-statement review, subsequent events, going concern, written representations, summary of misstatements, engagement quality review, key/critical audit matters, audit committee communications, opinion and report drafting.
- **Angle:** practice. What firms actually do: named deployments, measured outcomes, workflow and role changes.
- **Prepared:** 2026-10-16. **Inputs:** `research/runs/wave1/landscape-assurance.md`, `research/briefs/templates/vocabulary.md`.
- **Method note.** Pages were opened with `curl` (PDFs with `pdftotext`) and about a dozen web searches were used. Every source in section 5 is `access: full` (opened and read) unless marked `search-only`. Search-only items appear only in `notes`, in section 3, or in Gaps. They support no outcome figure and no A or B grade.

---

## 1. Summary

- **Completion is where the first measurable, named evidence sits, and it is almost all in two steps: the disclosure checklist and the mechanical review of draft financial statements.**
  - Caseware says beta firms saved 2.7 hours per disclosure checklist run on average (CASEWARE-VERITY-2026, 28 Jul 2026).
  - Thomson Reuters launched Disclosure Review on 23 Sep 2026 and says roughly 30% of eligible Disclosure-module customers already use it, with close to 300 analyses a month (TR-DISCLOSURE-2026).
  - Two named firms published measured results for an AI tool that casts, cross-references and consistency-checks draft statements: HLB Mann Judd Perth (about 600 hours saved a year) and MHA (casting time 25 to 12 minutes, zero false positives in a pilot). Both are vendor-published case studies (CASEWARE-HLB-2025; CASEWARE-MHA-2025).
- **Almost every figure is vendor-published. No independent measurement of disclosure-agent accuracy, miss rate or reviewer override rate was found.**
  - The only independent evidence on tools in this module is a perception survey of auditors at an unnamed German Big 4 firm (FABIAN-2026), plus benchmark papers that show gaps (ARXIV-FINAUDITING-2025, ARXIV-LLMAUDIT-2025, ARXIV-FAB-2026).
- **Year-one time savings at the largest firms are modest by the firms' own account.** PwC's US assurance transformation leader said in Oct 2026 that the audit report still looks the same and that time savings are "not that drastic yet" (CFODIVE-PWC-2026).
- **Most of the module has no public evidence of AI use.**
  - Nothing public was found for subsequent events, written representations, summary of misstatements, engagement quality review, opinion drafting, or a current firm deployment for going concern.
  - Key audit matters appear only in a 2026 master's thesis (UNIGE-KAM-2026).
  - Audit committee communications appear in one firm statement (PwC, announced). These steps are listed as open questions in section 3, not filled with invented use cases.
- **Baselines show where completion errors are found today.** In IFIAR's 2025 survey of inspection findings, audit committee communications findings rose to 79 of 725 listed-PIE audits inspected (11%), from 24 of 593 (4%) a year earlier. Presentation and disclosure findings stood at 41 of 445 (9%) (IFIAR-SURVEY-2026).
- **Evidence count:** 17 use cases (A: 1, B: 4, C: 10, D: 2). 43 sources read in full across 9 types (vendor 11, press 10, academic 7, firm 5, regulator 3, survey 3, standard-setter 2, professional-body 1, job-posting 1), plus 2 search-only sources.

---

## 2. Use cases

Conventions used below:

- **Maturity.** `piloting` is used where use is evidenced only by vendor-reported beta or early-customer figures with unnamed customers. `in-production` is used only where a named organization is described as using the tool.
- **Grades.** Grades follow the vocabulary. Where the source is a firm's or vendor's own announcement of a product, the grade is C even when the vendor is large.
- **Dates.** A source date of `2026-10` marks a page that carries no publication date. In that case the date is the retrieval month (retrieved 2026-10-16) and the locator says so.
- **Cap rule.** Evidence from an adjacent process (internal audit) is capped at B.

```yaml
- id: assurance-completion-reporting-01
  title: "AI first pass of the disclosure checklist against a PDF financial statement, with cited Yes/No/N/A answers (Caseware Verity Disclosure Checklist Agent)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Disclosure checklists run to hundreds of questions that a reviewer answers by cross-referencing the client's financial statements by hand. Caseware's documentation says this typically takes several hours per engagement."
  solution: "The agent reads the financial statement PDF the user selects and works through the firm's checklist question by question. It drafts a Yes, No or N/A answer for each, gives its reasoning, and links to the passage that supports the answer. It flags a question for review when it cannot find enough evidence. Only answers the auditor approves are written to the engagement file."
  outcomes:
    - lever: speed
      description: "Average time saved per disclosure checklist run by firms in the beta programme, as reported by the vendor."
      figure: "2.7 hours per checklist run (average)"
      measures: "Caseware's wording: firms in the beta program saved 2.7 hours per disclosure checklist run on average. Number of firms, number of runs and the manual baseline are not stated."
      provenance: vendor-published
      source_ref: CASEWARE-VERITY-2026
  prerequisites:
    - "Caseware Cloud engagement platform and access to the agent. The documentation says it is not available to all users and depends on firm configuration and licensing (CASEWARE-DCA-DOCS-2026, section Availability)."
    - "At general availability: US GAAP disclosure checklists and PDF financial statements only. IFRS, FRS 102, AASB, ASPE and firm-authored checklists are listed as roadmap items for 2026 (CASEWARE-DCA-DOCS-2026, section Availability)."
  risks_and_guardrails:
    - "The documentation says nothing is written to the engagement without the auditor reviewing, accepting, editing or rejecting it (CASEWARE-VERITY-2026, section Why it matters for your team)."
    - "The documentation says the AI reasoning and citations do not persist in the engagement file after the engagement is locked (CASEWARE-DCA-DOCS-2026, section Governance and engagement documentation). See the interview probe on what evidence of review remains."
    - "No independent accuracy, miss-rate or override-rate figure was found."
  human_checkpoints:
    - "Auditor verifies the cited evidence for each suggested answer and approves or changes it (CASEWARE-DCA-DOCS-2026, section What it means for your engagement workflow)."
    - "Questions the agent cannot support with confidence are flagged for the auditor instead of answered (CASEWARE-DCA-DOCS-2026, section The Disclosure Review agent)."
  role_evolution: "Caseware says junior team members can reach standards and methodology in context, and senior staff can concentrate on higher-value review (CASEWARE-VERITY-2026, section Why it matters for your team)."
  evidence_grade: C
  sources:
    - {ref: CASEWARE-VERITY-2026, title: "From AiDA to agentic: How Caseware's AI has evolved", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved", date: 2026-07-28, access: full, locator: "section The Caseware Verity Agentic Suites; FAQ on time saved"}
    - {ref: CASEWARE-DCA-DOCS-2026, title: "What is Disclosure Checklist Agent?", publisher: Caseware Docs, type: vendor, url: "https://www.caseware.com/docs/en/cloud/caseware-verity/disclosure-checklist-agent/what-is-disclosure-checklist-agent", date: 2026-10, access: full, locator: "whole page; page undated, retrieved 2026-10-16"}
  last_reviewed: 2026-10-16
  notes: "Vendor and beta framing only; the beta firms are not named. One Caseware homepage variant retrieved on 2026-10-16 showed 78% time saving in select Reporting use cases, with the footnote that data came from firms using Verity in live engagements (CASEWARE-HOME-2026). A second retrieval of the homepage showed a different panel (107-167 hours total AI time saving per engagement), so the homepage is not a stable citation and no outcome is taken from it. A search summary of another Caseware documentation page (search-only, not opened) says the agent can be run up to three times per engagement and that a sample run covered 209 questions across 3 checklists; treat as unverified."

- id: assurance-completion-reporting-02
  title: "AI-assisted disclosure review inside the audit methodology platform, with rationale and citations (Thomson Reuters Disclosure Review)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "A fully completed Guided Assurance disclosure checklist can run 1,200 to 1,500 requirements. TR says many firms roll forward last year's checklist or spend senior and manager time redoing it, and that a missed disclosure can surface as a PCAOB inspection finding, a peer review deficiency or a restatement."
  solution: "Disclosure Review matches each requirement against what is present in the financial statements and marks it identified or not found. Each recommendation carries a plain-language rationale and a citation to the source. Where the AI and the auditor's own answer diverge, the discrepancy is flagged automatically."
  outcomes:
    - lever: capacity
      description: "Share of eligible customers using the feature at launch, after an extended customer beta."
      figure: "about 30% of eligible customers"
      measures: "TR's wording: roughly 30% of eligible Disclosure module customers are already using it. The denominator is eligible Disclosure-module customers of Guided Assurance; customers are not named."
      provenance: vendor-published
      source_ref: TR-DISCLOSURE-2026
    - lever: capacity
      description: "Monthly volume of analyses generated across mid-sized and large firms."
      figure: "close to 300 analyses a month"
      measures: "TR's wording: close to 300 disclosure review analyses a month, across mid-sized and large firms. It counts analyses run, not engagements or hours."
      provenance: vendor-published
      source_ref: TR-DISCLOSURE-2026
  prerequisites:
    - "Guided Assurance with the Disclosure module. TR says the feature is available to those customers at no additional cost (TR-DISCLOSURE-2026)."
  risks_and_guardrails:
    - "The AI and the auditor's answer are compared and divergences flagged, so review effort goes to disagreements rather than a full re-check (TR-DISCLOSURE-2026)."
    - "TR gives no accuracy, false-negative or override figures."
  human_checkpoints:
    - "Auditor's own checklist judgment remains the comparison point; flagged discrepancies are resolved by the team (TR-DISCLOSURE-2026)."
  role_evolution: "TR says showing why a requirement was marked as it was lets junior staff build understanding of the requirement and not only trust in the output (TR-DISCLOSURE-2026)."
  evidence_grade: C
  sources:
    - {ref: TR-DISCLOSURE-2026, title: "Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/", date: 2026-09-23, access: full, locator: "paragraphs on the 1,200 to 1,500 requirements, the launch, and the beta results"}
  last_reviewed: 2026-10-16
  notes: "Written by TR's general manager of audit, so vendor-authored. Launched the day of publication; usage figures come from the beta and early use."

- id: assurance-completion-reporting-03
  title: "Upload-and-scan disclosure checklist tools from other vendors (Ideagen Disclose AI feature; DataSnipper Disclosure Agents)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "DataSnipper lists the same pain points as other vendors: checklists treated as a formality, requirements not tied to evidence, heavy reliance on senior expertise for conditional requirements, inconsistent progress tracking, and time spent on routine matching."
  solution: "Ideagen's tool scans an uploaded financial statement PDF, identifies required disclosures and marks missing items as No for review. The user can apply the AI answers globally or selectively. DataSnipper describes Disclosure Agents that work inside Excel as part of its work with Microsoft and tie each requirement to a snippet of the statements."
  outcomes:
    - lever: speed
      description: "Vendor claim that checklist completion drops from days to hours."
      figure: "days to hours (no basis given)"
      measures: "Ideagen's marketing statement; no sample, firm or baseline stated."
      provenance: vendor-published
      source_ref: IDEAGEN-DISCLOSE
    - lever: capacity
      description: "Vendor claim about use of the Disclose checklist product, which is the product the AI feature sits in."
      figure: "9 of 10 top UK accounting firms"
      measures: "Ideagen's wording: used by 9 out of 10 top UK accounting firms. It describes use of the Disclose checklist solution, not of the AI feature."
      provenance: vendor-published
      source_ref: IDEAGEN-DISCLOSE
  prerequisites:
    - "Financial statements as PDF (Ideagen) or an Excel-based workflow (DataSnipper)."
    - "Ideagen states coverage of UK GAAP, IFRS and US GAAP checklists (IDEAGEN-DISCLOSE)."
  risks_and_guardrails:
    - "Ideagen says the user keeps control by choosing whether to apply AI answers globally or selectively (IDEAGEN-DISCLOSE)."
    - "DataSnipper says AI does not remove professional judgment (DATASNIPPER-DISCLOSURE-2025)."
  human_checkpoints:
    - "Reviewer reviews AI-generated answers before applying them (IDEAGEN-DISCLOSE)."
  role_evolution: "DataSnipper says junior staff can handle more of the process with AI-assisted suggestions while seniors focus on judgment and oversight (DATASNIPPER-DISCLOSURE-2025)."
  evidence_grade: C
  sources:
    - {ref: IDEAGEN-DISCLOSE, title: "Revolutionary AI now powers your financial disclosure process", publisher: Ideagen, type: vendor, url: "https://www.ideagen.com/ideagen/lp/demos/audit-and-risk/disclose", date: 2026-10, access: full, locator: "how-it-works steps and benefits; page undated, retrieved 2026-10-16"}
    - {ref: DATASNIPPER-DISCLOSURE-2025, title: "The 5 hidden risks of disclosure review", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/5-hidden-risks-in-disclosure-review", date: 2025, access: full, locator: "sections The 5 hidden risks; How automation and AI is changing disclosure reviews; The future of disclosure compliance: Agentic AI"}
  last_reviewed: 2026-10-16
  notes: "Neither page is dated. The DataSnipper page's earliest archived copy found is 2025-10-12, so 2025 is an upper-bound estimate of its date. The DataSnipper page describes Disclosure Agents in the future tense and links a webinar. No customer or measured result for either product was found. A DataSnipper page for the agents themselves returned 404."

- id: assurance-completion-reporting-04
  title: "Financial Report Analyzer engine feeding disclosure checklists inside the firm audit platform (KPMG Clara)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Auditors must complete required disclosure checklists against the financial report."
  solution: "KPMG announced a Financial Report Analyzer AI engine that gives AI-generated output to help auditors complete the required disclosure checklists. It was released alongside AI agents for expense vouching and unrecorded-liability searches in KPMG Clara."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "The release gives no usage, time or accuracy figure for the engine."
      provenance: self-reported
      source_ref: KPMG-CLARA-2025
  prerequisites:
    - "KPMG Clara smart audit platform. The release says the agents aim to reach more than 95,000 auditors globally (KPMG-CLARA-2025, opening paragraph); that figure refers to the agent deployment as a whole, not to this engine."
  risks_and_guardrails:
    - "KPMG states a human-in-the-loop approach and says auditors stay in control of decisions to maintain quality, accuracy and professional skepticism (KPMG-CLARA-2025, section AI and our audit quality imperative)."
  human_checkpoints:
    - "Auditors complete the checklists using the AI-generated output; the auditor makes the decisions (KPMG-CLARA-2025)."
  role_evolution: "KPMG says it is upskilling its professionals alongside the deployment (KPMG-CLARA-2025, opening paragraphs). No role change is described for completion work."
  evidence_grade: C
  sources:
    - {ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: 2025-04-22, access: full, locator: "heading Financial Report Analyzer AI engine supports auditors' ability to complete disclosure checklists"}
  last_reviewed: 2026-10-16
  notes: "Announcement only. The same release says more agents will be deployed over the next 12 months into controls testing and financial statement analysis; no later KPMG publication on completion tools was opened."

- id: assurance-completion-reporting-05
  title: "Embedded agents that assist evaluation of regulatory and disclosure requirements (Deloitte Omnia)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Professionals evaluate compliance with regulatory and disclosure requirements and document preliminary conclusions as part of the audit."
  solution: "Deloitte announced a unified network of agents in Omnia. Examples it lists include executing preliminary procedures (data extraction, evidence analysis, drafting documentation, developing preliminary conclusions for professionals to review) and assisting with evaluating compliance with regulatory and disclosure requirements."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "The release gives no usage, time or quality figure. It says the network is aimed at nearly 85,000 Audit & Assurance practitioners worldwide."
      provenance: self-reported
      source_ref: DELOITTE-OMNIA-2026
  prerequisites:
    - "Deloitte Omnia platform. Deloitte says its internal engineering teams built the agent network (DELOITTE-OMNIA-2026, section Scaling innovation across a global platform)."
  risks_and_guardrails:
    - "Deloitte says capabilities follow its Trustworthy AI framework and that professionals supervise, validate and work alongside AI (DELOITTE-OMNIA-2026, sections Scaling innovation and Investing in upskilling)."
  human_checkpoints:
    - "Preliminary conclusions are developed for professionals to review (DELOITTE-OMNIA-2026, list of agent examples)."
  role_evolution: "Deloitte describes a tutor mode that gives on-demand micro-training in the context of the work, and training through its AI Academy and the Scout learning assistant (DELOITTE-OMNIA-2026, section Investing in upskilling)."
  evidence_grade: C
  sources:
    - {ref: DELOITTE-OMNIA-2026, title: "Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit & Assurance", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24, access: full, locator: "section Transforming how audit and assurance work gets done"}
  last_reviewed: 2026-10-16
  notes: "The disclosure-evaluation agent is one of four examples in a platform announcement; Deloitte does not describe it further. Bloomberg Law coverage (search result, paywalled, not opened) is not used."

- id: assurance-completion-reporting-06
  title: "AI proposes 'No' and 'Not applicable' determinations on disclosure requirements, the harder judgment calls"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "DataSnipper notes that conditional requirements such as 'if material' or 'unless impracticable' call for professional judgment and so lean on senior staff. Today's tools mostly identify what is present."
  solution: "TR says future Disclosure Review capabilities will extend into the harder judgment calls, such as No and Not applicable determinations. Ideagen's tool already marks items it cannot find as No for the user to review."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Roadmap statement only; no result."
      provenance: vendor-published
      source_ref: TR-DISCLOSURE-2026
  prerequisites:
    - "A working first-pass disclosure tool (use cases 01 to 03) and a way to record the applicability judgment."
  risks_and_guardrails:
    - "TR itself describes these determinations as the place where auditor expertise matters most (TR-DISCLOSURE-2026, paragraph beginning Meeting the market)."
    - "A false 'not applicable' removes a disclosure from review; no source quantifies this risk."
  human_checkpoints:
    - "Not specified by TR for the future capability."
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - {ref: TR-DISCLOSURE-2026, title: "Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/", date: 2026-09-23, access: full, locator: "paragraph beginning Meeting the market, with room to grow"}
    - {ref: DATASNIPPER-DISCLOSURE-2025, title: "The 5 hidden risks of disclosure review", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/5-hidden-risks-in-disclosure-review", date: 2025, access: full, locator: "risk 3, Heavy reliance on senior expertise"}
    - {ref: IDEAGEN-DISCLOSE, title: "Revolutionary AI now powers your financial disclosure process", publisher: Ideagen, type: vendor, url: "https://www.ideagen.com/ideagen/lp/demos/audit-and-risk/disclose", date: 2026-10, access: full, locator: "step 2, AI analysis; page undated, retrieved 2026-10-16"}
  last_reviewed: 2026-10-16
  notes: "Graded C because the only evidence is a vendor roadmap statement and a vendor marketing description. Not a researcher's or practitioner's idea."

- id: assurance-completion-reporting-07
  title: "AI-assisted audit of the management report: linking text passages to statutory disclosure requirements (German Big 4 firm)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "The audit of management reports has traditionally relied on a manual, checklist-based approach."
  solution: "A task-specific AI system on a digital platform finds relevant passages in the management report and links them to the statutory disclosure requirements, in both directions. Auditors review and document targeted suggestions per passage. It also checks for calculation errors, highlights changes between report versions, and supports team collaboration with task allocation and review functions that follow the dual-control principle."
  outcomes:
    - lever: quality
      description: "Auditors' perceived audit quality and efficiency, measured by survey. Positive overall and strongest for standardised tasks; limits on complex qualitative issues such as discretionary leeway and linguistic nuance. Perception only, not a measured error rate."
      figure: "none published (perception survey)"
      measures: "Survey of experienced auditors at a German Big 4 audit firm on perceived audit quality and perceived efficiency gains; sample size is not in the university release."
      provenance: independent
      source_ref: FABIAN-2026
  prerequisites:
    - "A digital review platform with the requirement-to-text linkage built in (FABIAN-2026)."
    - "Training and clear communication about opportunities and risks; the authors give these as practical implications (FABIAN-2026)."
  risks_and_guardrails:
    - "Some auditors raised concern about over-reliance on AI results and possible loss of skills (FABIAN-2026)."
    - "Acceptance depends on professional position, work experience and involvement in digital transformation (FABIAN-2026)."
  human_checkpoints:
    - "The AI does not replace professional judgement; auditors review and document the suggestions, with dual-control review functions (FABIAN-2026)."
  role_evolution: "The study reports that routine tasks speed up and auditors gain time for more demanding analysis, and that perceptions differ by position and experience (FABIAN-2026)."
  evidence_grade: B
  sources:
    - {ref: FABIAN-2026, title: "AI in auditing: New study highlights opportunities and limitations (study by Fabian and Ratzinger-Sakel, Journal of Information Systems)", publisher: University of Hamburg Business School, type: academic, url: "https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html", date: 2026-03-20, access: full, locator: "whole news item; the paper (doi 10.2308/ISYS-2025-054) returned 403 and was not opened"}
  last_reviewed: 2026-10-16
  notes: "Graded B, not A, because the firm is not named in the source and no performance measure is reported. The management report is not the financial statements, but the task (disclosure completeness against requirements) is the same type of work. The release is a translated university summary of the paper."

- id: assurance-completion-reporting-08
  title: "Automated casting, cross-referencing and consistency checks on draft financial statements, with carry-forward of review marks across drafts (Caseware Validate at HLB Mann Judd Perth and MHA)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "HLB Mann Judd Perth reviews over 300 sets of financial statements a year. Its first review of a full-year set took 3 to 4 hours and a half-year set 1.5 to 2 hours, over a minimum of 4 to 5 drafts per engagement, about 1,200 hours a year on first-draft reviews. MHA says each set took close to an hour to cast, cross-check and reconcile, and processes varied by office."
  solution: "Validate is described as an AI-powered, cloud-based tool that runs thousands of checks in seconds, cross-referencing data points for consistency, accuracy and compliance. It carries forward earlier checks and markups so that later drafts need only the changes re-checked, and it exports marked-up PDFs with cross-reference links."
  outcomes:
    - lever: capacity
      description: "Hours saved per year at HLB Mann Judd Perth, as reported in the vendor's case study."
      figure: "about 600 hours saved a year; 40 to 50% efficiencies on subsequent drafts"
      measures: "Case study wording: significant time savings on first drafts and 40-50% efficiencies on subsequent drafts, resulting in approximately 600 hours saved annually. Baseline is the firm's own estimate of about 1,200 hours a year on first-draft reviews across over 300 sets of statements. First-draft saving is not quantified."
      provenance: vendor-published
      source_ref: CASEWARE-HLB-2025
    - lever: speed
      description: "Average casting time and full first-pass review time in MHA's pilot of two shortlisted tools."
      figure: "casting 25 to 12 minutes; first-pass review 58 to 42 minutes"
      measures: "Case study wording: Validate cut average casting time from 25 minutes to 12 minutes and reduced a full first-pass review from 58 minutes to 42. Measured in a head-to-head pilot between two shortlisted tools; the source does not say whether the comparison baseline is the other tool or manual work, and gives no sample size."
      provenance: vendor-published
      source_ref: CASEWARE-MHA-2025
    - lever: quality
      description: "False positives in MHA's pilot: cases where the tool says something is correct when it is wrong."
      figure: "zero false positives (pilot)"
      measures: "Case study wording: no false positives, defined as the tool saying an item is correct when it is wrong. Number of sets or items tested is not stated."
      provenance: vendor-published
      source_ref: CASEWARE-MHA-2025
  prerequisites:
    - "Financial statements in a form the tool can read; HLB cites better OCR as a benefit over its earlier Excel add-in (CASEWARE-HLB-2025, section Solution)."
    - "A firm-wide standard review workflow; MHA selected the tool to standardise review across offices (CASEWARE-MHA-2025, section Challenge)."
  risks_and_guardrails:
    - "MHA values the tool's indeterminate flag for items it cannot call, which prompts professional judgement and not reliance on the software (CASEWARE-MHA-2025, section Results)."
    - "HLB cites a clear audit trail of changes through the marked-up PDF export (CASEWARE-HLB-2025, section Results)."
  human_checkpoints:
    - "Managers and seniors review the output and focus on key risk areas and on compliance and completeness of disclosures (CASEWARE-HLB-2025, section Results)."
  role_evolution: "HLB's audit manager says initial input can be done by any team member, letting senior staff focus on disclosures and judgment areas (CASEWARE-HLB-2025, section Results). MHA's tool selection was led by a Technical Director for Audit Data Analytics, a role described in its case study (CASEWARE-MHA-2025, section Solution)."
  evidence_grade: A
  sources:
    - {ref: CASEWARE-HLB-2025, title: "HLB Mann Judd Perth: Australian firm reduces manual financial statement review time by up to 50 percent with Caseware Validate", publisher: Caseware, type: vendor, url: "https://www.caseware.com/au/resources/success-stories/hlb-mann-judd-perth", date: 2025-04-10, access: full, locator: "sections Challenge, Solution, Results"}
    - {ref: CASEWARE-MHA-2025, title: "UK Firm Cuts Financial Statement Review Times with Caseware Validate", publisher: Caseware, type: vendor, url: "https://www.caseware.com/au/resources/success-stories/uk-firm-cuts-financial-statement-review-times-with-caseware-validate", date: 2025-07-17, access: full, locator: "sections Challenge, Results"}
    - {ref: BOARDAGENDA-FRC-2026, title: "Auditors warned they remain accountable despite use of AI", publisher: Board Agenda, type: press, url: "https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/", date: 2026-03-31, access: full, locator: "paragraph listing the FRC's examples of AI in the audit process, including checking the accuracy of financial statements"}
  last_reviewed: 2026-10-16
  notes: "Graded A because two named firms publish measured outcomes, but both are vendor-published case studies written by the supplier, and neither firm's baseline is independently verified. The MHA comparison may be tool against tool, not tool against manual work. The Board Agenda article reports the FRC saying AI is already used to check the accuracy of financial statements; it is cited only for that general maturity point. HLB's page was reached through the real success-story URL after a short link resolved to the Caseware homepage."

- id: assurance-completion-reporting-09
  title: "Agents that draft the financial statements from the prior-year report and trial balance, tie them out, and roll forward disclosures (Fieldguide Field Financials)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Fieldguide says preparing financials takes a fragmented mix of reports and spreadsheets."
  solution: "Field Financials bundles three agents. The Drafting Agent produces a rolled-forward, formatted first draft from the prior-year report linked to current-year trial balance data. The Review and Tie-Out Agent runs continuous, deterministic validation and flags stale overrides when trial-balance adjustments change. The Disclosure Agent rolls forward footnote language and fills schedule-driven disclosures."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "The announcement gives no customer, time or accuracy figure."
      provenance: vendor-published
      source_ref: CPAPA-FIELDGUIDE-2026
  prerequisites:
    - "Fieldguide platform, the firm's own prior-year reports, and live trial balance data (CPAPA-FIELDGUIDE-2026)."
  risks_and_guardrails:
    - "Fieldguide describes the tie-out validation as deterministic, so it is not a language-model judgment (CPAPA-FIELDGUIDE-2026)."
    - "A vendor article on review says AI output survives review only if it carries its inputs, steps and sources into a file a human can challenge (FIELDGUIDE-QR-2026, section on agentic review)."
  human_checkpoints:
    - "Not specified in the announcement for the Financials agents. Fieldguide says other agents' output is reviewed by practitioners (CPAPA-FIELDGUIDE-2026)."
  role_evolution: "Not described for this product. Fieldguide's CEO framed the launch as a step toward an agentic firm where AI amplifies practitioner expertise (CPAPA-FIELDGUIDE-2026)."
  evidence_grade: C
  sources:
    - {ref: CPAPA-FIELDGUIDE-2026, title: "Fieldguide Rolls Out Field Financials and Fieldguide MCP", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/fieldguide-rolls-out-field-financials-and-fieldguide-mcp/188469/", date: 2026-08-13, access: full, locator: "paragraphs on Field Financials and its three agents"}
    - {ref: FIELDGUIDE-QR-2026, title: "Audit Quality Review in an AI World: What Reviewers Look At Now", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/audit-quality-review-ai-what-reviewers-look-at-now", date: 2026, access: full, locator: "section on agentic review and the reviewer's job; page undated, banner implies on or after Aug 2026"}
  last_reviewed: 2026-10-16
  notes: "The announcement says Field Financials is available to all customers, that the Drafting Agent is the first sub-agent available, and that the Review and Tie-Out Agent and the Disclosure Agent follow 'in the fall'. Whether they have shipped by 2026-10-16 was not confirmed. An audit firm drafting client financial statements is a non-attest service question; the sources do not discuss it (see interview probes)."

- id: assurance-completion-reporting-10
  title: "Financial-statement tie-out and fund-audit testing in the Audit Innovation Hub (PwC, asset and wealth management engagements)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Financial statement review and tie-out is the last step in PwC's list of audit steps for which it says a tool exists or soon will."
  solution: "The Audit Innovation Hub automates and streamlines financial statement tie-outs and various testing procedures for non-registered fund-to-fund audits under AICPA auditing standards. It extracts, organizes and tests financial data and documents."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "The source gives no result. It says the tool was being tested with certain asset and wealth management engagement teams."
      provenance: self-reported
      source_ref: PWC-AT-2025
  prerequisites:
    - "Fund audits under AICPA standards, in asset and wealth management engagement teams (PWC-AT-2025)."
  risks_and_guardrails:
    - "PwC's Oct 2026 follow-up says the audit report is unchanged and the firm is still subject to regulation and professional standards (CFODIVE-PWC-2026)."
  human_checkpoints:
    - "Not specified for this tool."
  role_evolution: "PwC says it is hiring engineers into assurance and looking for more dual-track CPA and data-science candidates (PWC-AT-2025, final paragraphs)."
  evidence_grade: B
  sources:
    - {ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraphs on financial statement review and tie-out and the Audit Innovation Hub"}
    - {ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "paragraphs on 2026 year-end tools and time savings"}
  last_reviewed: 2026-10-16
  notes: "The Oct 2026 CFO Dive article does not mention the Audit Innovation Hub, so its current status is unknown. PwC said in Oct 2025 that end-to-end AI automation was its hope for calendar 2026; the Oct 2026 article describes time savings as modest so far."

- id: assurance-completion-reporting-11
  title: "GenAI first drafts of audit memos and completion documentation, reviewed by the preparer"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Teams write memos, presentations and documentation that record procedures, preliminary conclusions and judgments."
  solution: "PCAOB staff reported in July 2024 that some firms let staff use GenAI for initial drafts of memos and presentations related to the audit. Deloitte's June 2026 announcement lists drafting documentation and developing preliminary conclusions for professionals to review among its agent examples."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No time or quality figure is given for memo or documentation drafting in the PCAOB or Deloitte sources."
      provenance: independent
      source_ref: PCAOB-GENAI-2024
  prerequisites:
    - "Firm safeguards on what data may be uploaded to GenAI tools (PCAOB-GENAI-2024, p. 4)."
  risks_and_guardrails:
    - "Some firms did not allow GenAI for audit or attest procedures because of data privacy and reliability concerns (PCAOB-GENAI-2024, p. 4)."
    - "FinancialAuditBench, a benchmark on synthetic engagements, found that agents sometimes produce incorrect documentation (ARXIV-FAB-2026, abstract)."
  human_checkpoints:
    - "Firms said a team member who uses GenAI remains responsible for the output and that some had not changed their supervision and review policies (PCAOB-GENAI-2024, pp. 4-5)."
  role_evolution: "PCAOB staff reported that firms expected GenAI to augment and not replace humans (PCAOB-GENAI-2024, p. 4)."
  evidence_grade: C
  sources:
    - {ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "pp. 4-5, Observations Related to GenAI Integration in Audits"}
    - {ref: DELOITTE-OMNIA-2026, title: "Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit & Assurance", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24, access: full, locator: "list of agent examples"}
    - {ref: ARXIV-FAB-2026, title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.32835", date: 2026-09-26, access: full, locator: "abstract"}
  last_reviewed: 2026-10-16
  notes: "The PCAOB evidence is independent but staff-level (not Board policy), from 2024, and does not name firms. It describes firms' staff use, not completion-phase memos specifically. Graded C because no named deployment or measurement exists for completion memos. FinancialAuditBench tasks are workpaper completion and review across synthetic engagements; the word 'completion' there refers to completing workpapers, not the completion phase of the audit."

- id: assurance-completion-reporting-12
  title: "Engagement-file review assistants: asking whether the team missed anything, and checking documentation completeness (Caseware Verity; Fieldguide Field Reviewer)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Fieldguide argues that manual review re-performs the engagement by hand and spreads scrutiny evenly. Reviewers also spend time chasing missing tickmarks and reconciling the file against methodology."
  solution: "In a scenario shown at CwX 2026, a reviewer opens a file and asks Caseware Verity whether the team missed anything. Verity pulls the trial balance, checks materiality, reviews logged risks, and surfaces a variance against board minutes that has no risk attached. Fieldguide lists a Field Reviewer agent as rolling out later in 2026. PCAOB staff listed evaluating the completeness of audit documentation against requirements as a potential GenAI area in 2024."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "A product demonstration and announcements only; no result."
      provenance: vendor-published
      source_ref: CASEWARE-VERITY-2026
  prerequisites:
    - "Engagement data held in the vendor platform so the assistant can read trial balance, risks and documents (CASEWARE-VERITY-2026)."
  risks_and_guardrails:
    - "Caseware says the review call stays with the reviewer and nothing is written in without a human accepting, editing or rejecting it (CASEWARE-VERITY-2026)."
    - "The documentation of the review, including how AI was used, remains a firm obligation. IAASB non-authoritative material of 2020 explains how automated tools and techniques may affect audit documentation under ISA 230 (IAASB-NAM-2020)."
  human_checkpoints:
    - "The reviewer decides what holds and what goes back; Fieldguide says the reviewer's job shifts from re-performance to judging the output (FIELDGUIDE-QR-2026)."
  role_evolution: "Fieldguide says the reviewer becomes the first real judgment applied to the work and goes deep on high-stakes calls such as revenue recognition and going concern (FIELDGUIDE-QR-2026). This is a vendor view of the intended role."
  evidence_grade: C
  sources:
    - {ref: CASEWARE-VERITY-2026, title: "From AiDA to agentic: How Caseware's AI has evolved", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved", date: 2026-07-28, access: full, locator: "section Meet Caseware Verity, planning review scenario at CwX 2026"}
    - {ref: CPAPA-FIELDGUIDE-2026, title: "Fieldguide Rolls Out Field Financials and Fieldguide MCP", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/fieldguide-rolls-out-field-financials-and-fieldguide-mcp/188469/", date: 2026-08-13, access: full, locator: "paragraph naming Field Planner and Field Reviewer as rolling out later this year"}
    - {ref: FIELDGUIDE-QR-2026, title: "Audit Quality Review in an AI World: What Reviewers Look At Now", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/audit-quality-review-ai-what-reviewers-look-at-now", date: 2026, access: full, locator: "sections Why Manual Quality Review Breaks Down; Redefining the Reviewer's Job in an AI World; page undated"}
    - {ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p. 4, list of potential areas"}
    - {ref: IAASB-NAM-2020, title: "Non-Authoritative Support Material: Audit Documentation When Using Automated Tools and Techniques", publisher: IAASB, type: standard-setter, url: "https://www.iaasb.org/publications/non-authoritative-support-material-audit-documentation-when-using-automated-tools-and-techniques", date: 2020-04-23, access: full, locator: "summary paragraph on the publication"}
  last_reviewed: 2026-10-16
  notes: "The Caseware scenario is a planning-stage review demo; it is included because the reviewer-assistant pattern carries across the file review steps of completion. The Fieldguide article cites a PCAOB deficiency rate for non-Big-Four firms (52% of engagements reviewed in 2024); that is the vendor's reading of an inspection report that was not opened here, so no outcome is taken from it. No source describes use of AI by an engagement quality reviewer."

- id: assurance-completion-reporting-13
  title: "Tool that analyzes audit committee communications to surface issues earlier in the audit preparation cycle (PwC)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [research-synthesis, client-interaction]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Audit committee communications findings in inspections rose in 2025: 79 of 725 listed-PIE audits inspected had at least one finding, against 24 of 593 in 2024 (IFIAR-SURVEY-2026). The same survey does not explain the rise in the pages read."
  solution: "In Oct 2026 PwC said that for 2026 year-end audits another tool analyzes audit committee communications to surface issues to be handled sooner in the audit preparation cycle. The source does not say which communications the tool reads or who uses its output."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No usage or result is given. The article says the firm 'will be using' the tool for 2026 year-end audits."
      provenance: self-reported
      source_ref: CFODIVE-PWC-2026
  prerequisites:
    - "Not described in the source."
  risks_and_guardrails:
    - "KPMG's 2026 audit committee guidance says committees should discuss with the external auditor how the auditor is using GenAI and AI agents in the audit, how quality is ensured, and the effect on audit strategy and resources (KPMG-AC-2026, section on audit committee oversight of the external auditor)."
  human_checkpoints:
    - "Not described in the source."
  role_evolution: "Not described. Demand-side data: in the Deloitte and CAQ survey, 75% of audit committee respondents named AI governance a top-three priority (35% a year earlier) and 56% were confident they could oversee it (DELOITTE-CAQAC-2026)."
  evidence_grade: C
  sources:
    - {ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "paragraph beginning For 2026 year-end audits"}
    - {ref: IFIAR-SURVEY-2026, title: "Survey of Inspection Findings 2025", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01, access: full, locator: "table 2021-2025 Survey Results: Audits Inspected with at Least One Finding by Inspection Theme"}
    - {ref: KPMG-AC-2026, title: "On the 2026 audit committee agenda", publisher: KPMG Board Leadership Center, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/boardleadership/pdf/2026/on-the-2026-audit-committee-agenda.pdf", date: 2025-12-05, access: full, locator: "section on the audit committee and the external auditor"}
    - {ref: DELOITTE-CAQAC-2026, title: "Enterprise Risk Management Takes the Lead, AI Governance Gains Urgency for Audit Committees: Deloitte, Center for Audit Quality Survey", publisher: Deloitte, type: survey, url: "https://www.deloitte.com/us/en/about/press-room/deloitte-caq-announce-2026-audit-committee-practices-report.html", date: 2026-09-22, access: full, locator: "highlights list"}
  last_reviewed: 2026-10-16
  notes: "The only firm statement found on AI in audit committee communications is one sentence in a trade article; the tool's function is ambiguous in the source and no other firm describes comparable use. Whether it reads the committee's own communications to the company or the auditor's required communications is not stated."

- id: assurance-completion-reporting-14
  title: "Machine-learning decision tree as supplemental evidence for the auditor's going-concern assessment (a Spanish audit firm, 2022)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "The paper says going-concern assessment is a matter of significant judgment, and regulators asked for more skepticism during the COVID-19 period."
  solution: "The authors built a decision tree from quantitative indicators such as Z-scores and qualitative factors such as partners' judgment and industry risk. An auditing firm in Spain used the model as a supplemental guide, and its suggested results were compared with the auditors' reports."
  outcomes:
    - lever: quality
      description: "Agreement between the model and the auditors' going-concern conclusions in the firm's test."
      figure: "not stated as a percentage in the abstract"
      measures: "Abstract wording: the model's predictions were significantly similar to the auditors' assessments, indicating a high level of accuracy. Number of engagements and the rate of agreement are not in the abstract; differences were investigated."
      provenance: independent
      source_ref: BERETTA-GC-2022
  prerequisites:
    - "Financial indicators for the entity plus partner-level qualitative inputs (BERETTA-GC-2022)."
  risks_and_guardrails:
    - "The model was used as additional audit evidence and a supplemental guide, not a replacement for the auditor's conclusion (BERETTA-GC-2022)."
  human_checkpoints:
    - "Differences between the model's proposed outcome and the auditors' final conclusion were investigated (BERETTA-GC-2022)."
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - {ref: BERETTA-GC-2022, title: "Decision Tree Tool for Auditors' Going Concern Assessment in Spain", publisher: International Journal of Digital Accounting Research (Universidad Pontificia Comillas repository record), type: academic, url: "https://repositorio.comillas.edu/items/17c90a44-9e11-4354-b05c-0875629bd585", date: 2022-10-01, access: full, locator: "abstract"}
  last_reviewed: 2026-10-16
  notes: "Pattern is other: a supervised predictive model whose output is compared with the auditor's own judgment as additional evidence. Older than the 12 to 18 month window and kept as the only firm-tested going-concern tool found. The firm is not named. It is classical machine learning, not generative AI. Graded B, not A, because the firm is unnamed and no figures appear in the abstract. No 2025 or 2026 firm deployment for going concern was found (a search returned only research papers and a student thesis)."

- id: assurance-completion-reporting-15
  title: "LLM identifies key audit matters from the annual report (research idea)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Auditors select key audit matters from the significant matters communicated to those charged with governance; the selection is a matter of professional judgment."
  solution: "A 2026 master's thesis at the University of Genoa tested a large language model's ability to identify key audit matters from the information in the company's annual report alone. Results were compared statistically and against the matters in the audit reports, then discussed in interviews with audit partners from three firms."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "The abstract gives no figures. It reports that the model can support identification of key audit matters, with limits on understanding client business context and on judgment-heavy assessments."
      provenance: independent
      source_ref: UNIGE-KAM-2026
  prerequisites:
    - "Not applicable; research design only."
  risks_and_guardrails:
    - "The thesis names limits on business-context understanding and judgment-heavy assessments (UNIGE-KAM-2026)."
  human_checkpoints:
    - "The thesis concludes AI can support the audit process without replacing the auditor's professional judgement (UNIGE-KAM-2026)."
  role_evolution: "The partners interviewed showed near-unanimous agreement on usefulness for standardised tasks and differing acceptance for discretionary ones (UNIGE-KAM-2026)."
  evidence_grade: D
  sources:
    - {ref: UNIGE-KAM-2026, title: "Artificial intelligence in auditing: an application to key audit matters (master's thesis)", publisher: Universita degli studi di Genova, type: academic, url: "https://unire.unige.it/handle/123456789/16396", date: 2026-07-16, access: full, locator: "abstract and metadata (dc.date.issued)"}
  last_reviewed: 2026-10-16
  notes: "Idea. A student thesis, not a firm deployment. Search summaries (search-only, not opened) also point to a preprint that tested four models on predicting auditor-identified critical audit matters from 10-K MD&A text, an Iowa State working paper comparing AI-generated and auditor-reported CAMs, and a Regensburg paper using FinBERT on KAMs; none was opened and none supports a figure here. No source on LLM drafting of the KAM or CAM wording was found."

- id: assurance-completion-reporting-16
  title: "ChatGPT used across audit preparation, fieldwork and audit reporting in an internal audit function (Uniper)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Internal audit teams draft engagement reports and related documents as part of every audit."
  solution: "The internal audit function of Uniper, a large multinational energy company, uses ChatGPT in audit preparation, fieldwork and audit reporting tasks. The authors also report key risks and challenges and the practices and rules Uniper adopted."
  outcomes:
    - lever: speed
      description: "The function's estimate of efficiency gains from initial tests across various processes, including reporting."
      figure: "50 to 80 percent (estimate)"
      measures: "Abstract wording: based on initial tests, the internal audit function estimates efficiency gains ranging from 50 to 80 percent for various processes. The figure is not split by process, so it is not a reporting-only figure, and the baseline is not stated in the abstract."
      provenance: self-reported
      source_ref: EULERICH-2025
  prerequisites:
    - "Rules and practices for using ChatGPT set by the function (EULERICH-2025)."
  risks_and_guardrails:
    - "The paper reports key risks and challenges of using ChatGPT in internal audit and the practices Uniper adopted (EULERICH-2025)."
  human_checkpoints:
    - "Not described in the abstract."
  role_evolution: "The study assessed internal auditors' perception of the effect on efficiency and effectiveness (EULERICH-2025)."
  evidence_grade: B
  sources:
    - {ref: EULERICH-2025, title: "Leveraging ChatGPT for Enhancing the Internal Audit Process: A Real-World Example from Uniper, a Large Multinational Company", publisher: Accounting Horizons (American Accounting Association), type: academic, url: "https://doi.org/10.2308/HORIZONS-2023-111", date: 2025-04-24, access: full, locator: "synopsis (abstract), from the Crossref record"}
    - {ref: IIA-RIDDLE-2024, title: "Solving the Riddle: Harnessing Generative AI for Internal Audit Activities", publisher: Internal Audit Foundation with Wolters Kluwer TeamMate, type: professional-body, url: "https://www.theiia.org/en/content/research/foundation/2024/solving-the-riddle-harnessing-generative-ai-for-internal-audit-activities/", date: 2024-10-21, access: full, locator: "summary: most respondents use GenAI extensively or often for the planning or reporting phases"}
  last_reviewed: 2026-10-16
  notes: "Capped at B: internal audit is adjacent to external audit completion, and the efficiency figure covers several processes. Only the abstract was read. The IIA survey page says most respondents use GenAI extensively or often for the planning or reporting phases, which supports the use but gives no outcome. A search summary (search-only) cites a UK Government Internal Audit Agency 'Writing Engine' built in-house with AI; the source seen does not say it drafts audit reports, so it is not used."

- id: assurance-completion-reporting-17
  title: "LLM review of financial statements for errors and standard violations, and cross-document consistency in XBRL filings (benchmark research)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "The benchmark authors say manual financial statement auditing is inefficient and error-prone, and that auditors frequently miss errors."
  solution: "Two benchmarks test whether LLMs can do the checking. One uses real financial tables with synthesized transaction data and a five-stage framework that maps statement errors to violated accounting standards. The other, FinAuditing, uses 1,102 instances built from real XBRL filings, averaging over 33,000 tokens, and tests 13 models on semantic matching, relationship extraction and mathematical reasoning."
  outcomes:
    - lever: quality
      description: "Capability findings, not deployment outcomes. Models found statement errors when given historical transaction data but were limited in explaining errors and citing the relevant accounting standards, and struggled to execute complete audits and make revisions. The 13 models in FinAuditing showed substantial gaps in concept retrieval, taxonomy-aware relation modelling and consistent cross-document reasoning."
      figure: "none published (qualitative in abstracts)"
      measures: "FinAuditing: 1,102 annotated instances, 13 LLMs. The five-stage benchmark: sample size not in the abstract."
      provenance: independent
      source_ref: ARXIV-LLMAUDIT-2025
  prerequisites:
    - "Not applicable; research only."
  risks_and_guardrails:
    - "The authors of the five-stage benchmark conclude there is a critical gap in domain-specific accounting knowledge (ARXIV-LLMAUDIT-2025)."
    - "FinancialAuditBench found agents completed substantial portions of staff-level workpaper tasks well but sometimes performed inappropriate procedures or wrote incorrect documentation (ARXIV-FAB-2026)."
  human_checkpoints:
    - "Not applicable."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - {ref: ARXIV-LLMAUDIT-2025, title: "Automating Financial Statement Audits with Large Language Models", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2506.17282", date: 2025-06-14, access: full, locator: "abstract"}
    - {ref: ARXIV-FINAUDITING-2025, title: "FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs", publisher: arXiv (accepted by SIGIR 2026 Resource Track), type: academic, url: "https://arxiv.org/abs/2510.08886", date: 2025-10-10, access: full, locator: "abstract; last revised 2026-05-17"}
    - {ref: ARXIV-FAB-2026, title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.32835", date: 2026-09-26, access: full, locator: "abstract"}
  last_reviewed: 2026-10-16
  notes: "Idea, with research results. These are model-capability benchmarks on synthetic or public data, not firm tools, so they show where an agent might fail and not how a firm's tool performs. Only abstracts were read."
```

---

## 3. Module notes

### Processes and key steps, with work types

| Step | Work type | Public evidence of AI use found |
|---|---|---|
| Disclosure checklist completion | review-assurance | Yes: vendor products with usage or beta figures (use cases 01 to 06) |
| Casting, cross-referencing and tie-out of draft statements | review-assurance, data-reporting | Yes: two named firms with measured results (08); PwC fund tie-out pilot (10) |
| Review of other information and management report against requirements | review-assurance | One academic study at an unnamed Big 4 firm (07) |
| Subsequent events review | review-assurance, research-synthesis | None found (open question) |
| Going-concern evaluation | expert-judgment | A 2022 academic firm test (14); no current firm deployment found |
| Written representations | document-production | None found (open question) |
| Summary of misstatements and evaluation | review-assurance, data-reporting | None found (open question) |
| Manager and partner file review | review-assurance | Vendor demonstrations and announcements (12) |
| Engagement quality review | review-assurance | None found (open question) |
| Key or critical audit matters: selection and wording | expert-judgment, document-production | One master's thesis on identification (15); none on wording |
| Audit committee communications | client-interaction, document-production | One PwC statement (13) |
| Opinion and report drafting | document-production | None specific to external audit. Internal audit reporting at Uniper (16); drafting of memos (11) |

**Open questions (steps with no public evidence of AI use).** Searches were run for each of these and returned only standards, exam material, or unrelated items.
- Subsequent events: only the DataSnipper checklist list names subsequent events as a disclosure item; no AI tool for the procedure surfaced.
- Written representations: searches returned ISA 580 material and templates only; no AI use or guidance on AI-drafted letters.
- Summary of misstatements and the evaluation of uncorrected misstatements: no source.
- Engagement quality review: no source on AI use by a reviewer. A search for the FRC's guidance found it does not address EQR reviewers specifically; a vendor article argues for the reviewer's changed role (12).
- Key and critical audit matters: identification is studied (15); drafting is not.
- Opinion and auditor's report drafting: no source on AI drafting of the opinion or on tool support for report wording. PwC says the final audit report looks the same (CFODIVE-PWC-2026).
- Going concern: the only firm-tested tool found is a 2022 classical ML model (14). The PCAOB has a going-concern standard-setting project (JOFA-PCAOBAGENDA-2026) with no technology reference found in the article read.
- Final analytical procedures and the completion memo as a document: no source.

### Common pain points

- Disclosure checklists run to 1,200 to 1,500 requirements in one methodology; TR says fatigue sets in and firms often roll forward the prior-year checklist (TR-DISCLOSURE-2026).
- Reviewing financial statements is repeated across drafts. HLB cites 4 to 5 drafts per engagement and about 1,200 hours a year on first-draft reviews across over 300 sets (CASEWARE-HLB-2025). MHA cites close to an hour to cast each set, with methods varying by office (CASEWARE-MHA-2025).
- Earlier review software had gaps: no half-year support, Excel add-in crashes and data loss, OCR errors, and no carry-forward of marks between drafts (CASEWARE-HLB-2025).
- DataSnipper (vendor view) lists five risks: treating the checklist as a formality, requirements not tied to evidence, reliance on senior expertise for conditional requirements, inconsistent progress tracking, and time drain (DATASNIPPER-DISCLOSURE-2025).
- Only 17% of the 54 US firms in the CPA.com benchmark have an automated solution for report production, against 39% for foot and proofing (CPACOM-ATR-2025, p. 10).

### Metrics and benchmarks

| Metric | Value | Source and what it measures |
|---|---|---|
| Disclosure checklist time saved | 2.7 hours per run | CASEWARE-VERITY-2026; average for beta firms, vendor-published, baseline not stated |
| Disclosure Review adoption | about 30% of eligible customers; close to 300 analyses a month | TR-DISCLOSURE-2026; vendor-published |
| Full checklist size | 1,200 to 1,500 requirements | TR-DISCLOSURE-2026; in Guided Assurance |
| FS review time saved (HLB) | about 600 hours a year; 40 to 50% on subsequent drafts | CASEWARE-HLB-2025; vendor case study |
| Casting and first-pass time (MHA) | 25 to 12 minutes; 58 to 42 minutes; zero false positives | CASEWARE-MHA-2025; pilot of two tools, vendor case study |
| Internal audit efficiency gain (Uniper) | 50 to 80% estimated, across processes | EULERICH-2025; self-reported estimate |
| Automated foot and proofing / report production | 39% / 17% of 54 US firms | CPACOM-ATR-2025, p. 10; firms with an automated solution for each |
| Inspection baselines, listed-PIE audits, 2025 | Presentation and disclosure: 41 of 445 audits with at least one finding (9%). Audit committee communications: 79 of 725 (11%, up from 24 of 593, 4%, in 2024). Going concern: 11 of 232 (5%). Audit report: 24 of 758 (3%). Engagement quality control review: 10 of 341 (3%). Adequacy of review and supervision: 23 of 420 (5%) | IFIAR-SURVEY-2026, table of audits inspected with at least one finding; inspections of the six GPPC networks by members. Footnote-disclosure adequacy findings were 29 in 2025 against 57 in 2022 |
| Audit committee readiness | 75% put AI governance in their top three (35% a year earlier); 56% confident in oversight; 248 respondents | DELOITTE-CAQAC-2026; DART-CAQAC-2026 for the sample |
| Audit partners' view | AI governance the top audit committee challenge at 57% | BOARDMEMBER-CAQ-2026 |

The IFIAR figures are baselines for the steps where AI would act; the sources do not link any finding to AI use. No inspection finding about AI use in these steps was found.

### Guardrails and regulatory points

- The FRC's March 2026 guidance, as reported by Board Agenda, says accountability for audit quality stays with the firms and responsible individuals, and the FRC lists AI uses including checking the accuracy of financial statements (BOARDAGENDA-FRC-2026). The guidance itself defines LLM roles such as writer and summariser; its worked examples are board-minute summarisation and contract review, none in completion (FRC-GENAI-2026, role table and examples).
- The AICPA practice aid, released 13 Oct 2026, says the auditor remains responsible for the audit and the opinion (AICPA-PA-2026).
- PCAOB staff, in 2024, listed completeness of financial statement disclosures and comparing statement amounts with audited amounts among potential GenAI areas, and noted some firms barred GenAI for audit procedures (PCAOB-GENAI-2024, p. 4). This is a staff view, not Board policy.
- The PCAOB's updated agendas (30 Sep 2026) include standard-setting on going concern and research on communications with audit committees and on data and technology (JOFA-PCAOBAGENDA-2026).
- IAASB's 2020 non-authoritative material explains how automated tools may affect ISA 230 documentation (IAASB-NAM-2020).
- Caseware's agent does not keep the AI reasoning and citations once the engagement is locked (CASEWARE-DCA-DOCS-2026).
- KPMG's 2026 audit committee guidance tells committees to ask the external auditor how it uses GenAI and AI agents and how it ensures quality (KPMG-AC-2026).
- An adjacent warning on advisory reports: Deloitte Australia partially refunded the Australian government for a 237-page report with apparent AI-generated errors including a fabricated court quote and nonexistent references (BNN-DELOITTEAU-2025, 2025-10-07). It is not an audit report.

### Frontier signals (dated)

- 2026-09-23: TR says future Disclosure Review capabilities will cover No and Not applicable calls (TR-DISCLOSURE-2026).
- 2026-08-13: Fieldguide's Review and Tie-Out Agent and Disclosure Agent were due "in the fall" (CPAPA-FIELDGUIDE-2026).
- 2026-07-28: Caseware lists IFRS, FRS 102, AASB, ASPE and firm-authored checklists as roadmap for the Disclosure Checklist Agent (CASEWARE-DCA-DOCS-2026; page undated).
- 2026-04-07: EY says its agents are embedded in all audit phases now and are expected to support all end-to-end audit activities by 2028 (EY-CANVAS-2026).
- 2025-10-28: PwC hoped for a tool for every audit step, including financial statement review and tie-out, for calendar 2026, and one global agentic platform about 18 months after that (PWC-AT-2025). In Oct 2026 PwC said efficiencies are still modest (CFODIVE-PWC-2026).
- 2026-10-01: PCAOB agendas add going-concern standard-setting and research on communications with audit committees (JOFA-PCAOBAGENDA-2026).
- 2026-09-26: FinancialAuditBench shows agents completing much staff-level work but sometimes producing incorrect documentation (ARXIV-FAB-2026).

### Workforce and role effects

- Reviewers: vendors describe a shift from re-performing checks to judging AI output (FIELDGUIDE-QR-2026; CASEWARE-HLB-2025). This is vendor and customer description, not measured.
- Juniors and seniors: HLB says any team member can run the first-pass check so seniors focus on disclosures and judgment (CASEWARE-HLB-2025). TR and Caseware say rationale and in-context standards help juniors learn (TR-DISCLOSURE-2026; CASEWARE-VERITY-2026). The Fabian study reports concerns about over-reliance and skill loss (FABIAN-2026).
- New roles: MHA's audit data analytics lead chose the tool (CASEWARE-MHA-2025). PwC says it hires engineers it would not have hired into assurance before (PWC-AT-2025; CFOBREW-PWC-2025).
- Hiring expectations: a Deloitte manager posting (Cairo, posted 17 May 2026) asks for ability to validate AI outputs for accuracy and completeness before they enter workpapers, and to use firm-approved tools (DELOITTE-JOBCAIRO-2026).
- Supervision: PCAOB staff found some firms had not changed supervision and review policies despite GenAI (PCAOB-GENAI-2024, p. 4).

### Objections and concerns raised

- Evidence is vendor-authored and baselines are not stated (observed across sources 01 to 03 and 08).
- Over-reliance and skill loss (FABIAN-2026).
- Limits on complex qualitative judgments such as discretion, linguistic nuance and strategic statements (FABIAN-2026).
- Reliability and data privacy led some firms to bar GenAI from audit procedures (PCAOB-GENAI-2024, p. 4).
- Audit committees feel under-prepared on AI governance (DELOITTE-CAQAC-2026; AT-ACFOCUS-2026).
- Time savings are not yet dramatic even at a Big Four firm (CFODIVE-PWC-2026).

### Interview probes for an advisor

1. For disclosure checklists, what share of AI answers do reviewers change, and has anyone measured missed disclosures in a parallel run against a manual checklist? (No override or miss rate is public.)
2. What evidence of AI-assisted review stays in the file after lock, and does it meet your documentation policy and inspectors' expectations?
3. Who owns the No and Not applicable calls when a tool proposes them, and how are those calls recorded?
4. Which of subsequent events, representations, summary of misstatements, engagement quality review, key audit matters and report drafting use any AI today, and what stopped the others?
5. If your firm's tools draft or roll forward client financial statements or footnotes, how does that sit with independence and non-attest service rules, and who reviews it?

---

## 4. Routed to other modules

| Item | Target module | Note |
|---|---|---|
| Fieldguide Audit Testing Agent: automates testing end to end; vendor claim of "up to 70%" of testing automated (FIELDGUIDE-AGENTS-2025, 2025-06-04) | substantive-testing | Vendor claim, no named customer in the page read |
| Johnson Lambert and Provectus: document-to-structure pipeline for tie-outs in financial risk audits; reported 60-80 to 12-16 hours per audit, also stated as 20% efficiency and 50% document-processing reduction on the same page (PROVECTUS-JL-2026, 2026-04-20) | substantive-testing | Figures inside the page disagree with each other; vendor-published |
| Ally internal audit: AI-generated risk and control matrices in planning; estimate of more than 60 hours per audit; over 75% rated Good or Great by the audit team (ALLY-2024, 2024-10-24) | planning-risk-assessment | Self-reported pilot; internal audit |
| PwC Evidence Match, Advanced Walkthrough Assistant, Simplified Audit planning tool (PWC-AT-2025) | substantive-testing; controls-testing; planning-risk-assessment | Same briefing as use case 10 |
| EY Canvas multi-agent framework: 130,000 assurance professionals, 160,000 engagements, 1.4 trillion journal-entry lines a year (EY-CANVAS-2026) | cross-cutting context | No completion-specific content found in the release |
| Workiva automated testing for internal audit and GRC, 7 Apr 2026, and regulatory-reporting agents (CPAPA-WORKIVA-2026, 2026-09-15) | controls-testing | The page read describes regulatory surveys and testing agents, not auditor completion work |
| KPMG audit committee guidance on questions to ask the auditor about AI use (KPMG-AC-2026) | quality-management (and acceptance-independence) | Also used in use case 13 |
| IFIAR 2025 findings for engagement quality control review (10 of 341), adequacy of review and supervision (23 of 420) (IFIAR-SURVEY-2026) | quality-management | Baseline for review steps |
| Deloitte Australia refund over apparent AI errors in an advisory report (BNN-DELOITTEAU-2025) | quality-management | Guardrail example; not an audit |
| Clark "Material Intelligence" (agent that tracks missing information and requests it from the client); Fieldguide Field Planner (announced, later 2026) | planning-risk-assessment; substantive-testing | Seen in a trade-news summary and a press item; not read in full |

---

## 5. Sources

All are `access: full` unless marked. Refs follow `PUBLISHER-SHORT-YYYY` and match the landscape file where the document is the same.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| TR-DISCLOSURE-2026 | Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence | Thomson Reuters | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/ | 2026-09-23 | full |
| CASEWARE-VERITY-2026 | From AiDA to agentic: How Caseware's AI has evolved | Caseware | vendor | https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved | 2026-07-28 | full |
| CASEWARE-DCA-DOCS-2026 | What is Disclosure Checklist Agent? | Caseware Docs | vendor | https://www.caseware.com/docs/en/cloud/caseware-verity/disclosure-checklist-agent/what-is-disclosure-checklist-agent | 2026-10 (undated; retrieved 2026-10-16) | full |
| CASEWARE-HLB-2025 | HLB Mann Judd Perth (success story) | Caseware | vendor | https://www.caseware.com/au/resources/success-stories/hlb-mann-judd-perth | 2025-04-10 | full |
| CASEWARE-MHA-2025 | UK Firm Cuts Financial Statement Review Times with Caseware Validate | Caseware | vendor | https://www.caseware.com/au/resources/success-stories/uk-firm-cuts-financial-statement-review-times-with-caseware-validate | 2025-07-17 | full |
| CASEWARE-HOME-2026 | Caseware homepage (Verity results panels) | Caseware | vendor | https://www.caseware.com/ | 2026-10 (retrieved 2026-10-16; volatile) | full |
| IDEAGEN-DISCLOSE | Revolutionary AI now powers your financial disclosure process | Ideagen | vendor | https://www.ideagen.com/ideagen/lp/demos/audit-and-risk/disclose | 2026-10 (undated; retrieved 2026-10-16) | full |
| DATASNIPPER-DISCLOSURE-2025 | The 5 hidden risks of disclosure review | DataSnipper | vendor | https://www.datasnipper.com/resources/5-hidden-risks-in-disclosure-review | 2025 (undated; earliest archive 2025-10-12) | full |
| FIELDGUIDE-QR-2026 | Audit Quality Review in an AI World: What Reviewers Look At Now | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/audit-quality-review-ai-what-reviewers-look-at-now | 2026 (undated) | full |
| FIELDGUIDE-AGENTS-2025 | Increase Capacity and Audit Quality with Field Agents for Financial Audit | Fieldguide | vendor | https://www.fieldguide.io/blog/increase-capacity-and-audit-quality-with-field-agents-for-financial-audit | 2025-06-04 | full |
| PROVECTUS-JL-2026 | Reinventing Auditing in Insurance with Generative AI (Johnson Lambert) | Provectus | vendor | https://provectus.com/case-studies/reinventing-auditing-insurance-generative-ai | 2026-04-20 | full |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04-22 | full |
| DELOITTE-OMNIA-2026 | Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit & Assurance | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 | full |
| EY-CANVAS-2026 | EY launches enterprise-scale agentic AI to redefine the audit experience for the AI era | EY | firm | https://www.ey.com/en_ca/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era | 2026-04-07 | full |
| KPMG-AC-2026 | On the 2026 audit committee agenda | KPMG Board Leadership Center | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/boardleadership/pdf/2026/on-the-2026-audit-committee-agenda.pdf | 2025-12-05 | full |
| ALLY-2024 | Auditors are Innovators: Using AI to Realize the Future of Audit | Ally Financial | firm | https://www.ally.com/tech/auditors-are-innovators-using-ai-to-realize-the-future-of-audit/ | 2024-10-24 | full |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 | full |
| CFOBREW-PWC-2025 | A look at PwC's next-generation audit | CFO Brew | press | https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit | 2025-11-05 | full |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 | full |
| CPAPA-FIELDGUIDE-2026 | Fieldguide Rolls Out Field Financials and Fieldguide MCP | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/13/fieldguide-rolls-out-field-financials-and-fieldguide-mcp/188469/ | 2026-08-13 | full |
| CPAPA-WORKIVA-2026 | Workiva advances regulatory work with AI innovation | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/09/15/workiva-advances-regulatory-work-with-ai-innovation/190227/ | 2026-09-15 | full |
| BOARDAGENDA-FRC-2026 | Auditors warned they remain accountable despite use of AI | Board Agenda | press | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | 2026-03-31 | full |
| JOFA-PCAOBAGENDA-2026 | PCAOB shares agenda for rulemaking, research | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/pcaob-shares-agenda-for-rulemaking-research/ | 2026-10-01 | full |
| DART-CAQAC-2026 | CAQ Releases Audit Committee Practices Report | Deloitte DART | press | https://dart.deloitte.com/USDART/home/news/all-news/2026/oct/caq-audit-committee-practices-robot | 2026-10-08 | full |
| AT-ACFOCUS-2026 | Audit committees focusing on emerging risks like AI | Accounting Today | press | https://www.accountingtoday.com/news/audit-committees-focusing-on-emerging-risks-like-ai | 2026-09-22 | full |
| BNN-DELOITTEAU-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | BNN Bloomberg (Associated Press) | press | https://www.bnnbloomberg.ca/business/artificial-intelligence/2025/10/07/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| FABIAN-2026 | AI in auditing: New study highlights opportunities and limitations | University of Hamburg Business School | academic | https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html | 2026-03-20 | full (release only; paper 403) |
| BERETTA-GC-2022 | Decision Tree Tool for Auditors' Going Concern Assessment in Spain | International Journal of Digital Accounting Research (Comillas repository) | academic | https://repositorio.comillas.edu/items/17c90a44-9e11-4354-b05c-0875629bd585 | 2022-10-01 | full (abstract) |
| UNIGE-KAM-2026 | Artificial intelligence in auditing: an application to key audit matters (master's thesis) | Universita degli studi di Genova | academic | https://unire.unige.it/handle/123456789/16396 | 2026-07-16 | full (abstract) |
| EULERICH-2025 | Leveraging ChatGPT for Enhancing the Internal Audit Process: A Real-World Example from Uniper | Accounting Horizons | academic | https://doi.org/10.2308/HORIZONS-2023-111 | 2025-04-24 | full (abstract via Crossref) |
| ARXIV-LLMAUDIT-2025 | Automating Financial Statement Audits with Large Language Models | arXiv | academic | https://arxiv.org/abs/2506.17282 | 2025-06-14 | full (abstract) |
| ARXIV-FINAUDITING-2025 | FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs | arXiv | academic | https://arxiv.org/abs/2510.08886 | 2025-10-10 | full (abstract) |
| ARXIV-FAB-2026 | FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors | arXiv | academic | https://arxiv.org/abs/2609.32835 | 2026-09-26 | full (abstract) |
| IFIAR-SURVEY-2026 | Survey of Inspection Findings 2025 | IFIAR | regulator | https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf | 2026-04-01 | full (overview and results tables) |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting | PCAOB staff | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 | full |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples | FRC | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full (searched for completion-relevant content; read the role table and examples) |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full (release; practice aid itself not opened) |
| IAASB-NAM-2020 | Non-Authoritative Support Material: Audit Documentation When Using Automated Tools and Techniques | IAASB | standard-setter | https://www.iaasb.org/publications/non-authoritative-support-material-audit-documentation-when-using-automated-tools-and-techniques | 2020-04-23 | full (summary page) |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report | AICPA and CPA.com | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| DELOITTE-CAQAC-2026 | Enterprise Risk Management Takes the Lead, AI Governance Gains Urgency for Audit Committees (media alert on the Audit Committee Practices Report) | Deloitte with the Center for Audit Quality | survey | https://www.deloitte.com/us/en/about/press-room/deloitte-caq-announce-2026-audit-committee-practices-report.html | 2026-09-22 | full |
| BOARDMEMBER-CAQ-2026 | What Audit Partners Are Seeing On AI And What It Means For Audit Committees (Spring 2026 Audit Partner Pulse) | Corporate Board Member | survey | https://boardmember.com/?p=50023 | 2026-07-15 | full (article about the CAQ survey) |
| IIA-RIDDLE-2024 | Solving the Riddle: Harnessing Generative AI for Internal Audit Activities | Internal Audit Foundation with Wolters Kluwer TeamMate | professional-body | https://www.theiia.org/en/content/research/foundation/2024/solving-the-riddle-harnessing-generative-ai-for-internal-audit-activities/ | 2024-10-21 | full (summary page) |
| DELOITTE-JOBCAIRO-2026 | Manager, Audit, Audit & Assurance, Cairo, FSI (job posting) | Deloitte Middle East | job-posting | https://middleeastjobs.deloitte.com/careersME/PipelineDetail/Cairo-Egypt-Manager-Audit-Audit-Assurance-Cairo-FSI/254184 | 2026-05-17 | full |
| GIAA-BLOG-2024 | Sharing our AI expertise (mentions Insights, Writing and Risk Engines) | UK Government Internal Audit Agency | firm | https://giaa.blog.gov.uk/2024/12/11/sharing-our-ai-expertise | 2024-12-11 (from URL) | search-only |
| ICAEW-AAC-2026 | Audit and Assurance Conference 2026 (optional breakfast: Improving audit quality through AI with AuditBot) | ICAEW | conference | https://www.icaew.com/learning-and-development/events/audit-and-assurance-conference | 2026-06-15 (event date, from search summary) | search-only |

**Counts.** 43 sources read in full: vendor 11, press 10, academic 7, firm 5, regulator 3, survey 3, standard-setter 2, professional-body 1, job-posting 1. Two search-only sources (firm 1, conference 1). No podcast or community source was used.

---

## 6. Gaps

**No evidence found:**
- Independent measurement of disclosure-agent or FS-review-tool quality: no accuracy, miss rate, false-negative rate, reviewer override rate or parallel-run result beyond MHA's pilot (a vendor case study with no sample size).
- Inspection or peer-review findings about AI in completion steps; the IFIAR tables carry no AI linkage and the reason for the 2025 rise in audit committee communications findings was not found in the pages read.
- Any public use of AI for subsequent events, written representations, summary of misstatements, engagement quality review, key or critical audit matter wording, or the auditor's opinion and report (see open questions in section 3).
- A current (2025 to 2026) firm deployment for going concern.
- Named customers for Caseware's beta, Thomson Reuters Disclosure Review, Ideagen's AI feature and KPMG's Financial Report Analyzer; any usage or quality figure for KPMG's engine.
- What PwC's audit committee communications tool reads and who uses its output.
- Outcomes from the Big Four on completion (the only EY, KPMG and Deloitte items are announcements).

**Blocked or not opened:**
- The Fabian paper (publications.aaahq.org, 403): only the university release was read, so sample size and quantitative results are unknown.
- Bloomberg Law items on KPMG and Deloitte agents (paywalled); Gartner's 2024 internal-audit survey page (403); AccountingWeb pages (403); Trullion (403); BDO Belgium innovation job (410); DataSnipper Disclosure Agents page (404); a CPA Practice Advisor guess for the PCAOB agenda (404, replaced by the Journal of Accountancy article).
- Several Caseware documentation pages (FAQ, usage caps, release notes) returned navigation only; the agent's FAQ and sample-run details are unconfirmed.
- The PCAOB going-concern project page and the AICPA practice aid full text (login) were not opened.

**Dates not found:** Ideagen page; Caseware documentation page; Fieldguide quality-review article (banner implies on or after Aug 2026); DataSnipper page (earliest archive 2025-10-12). Dates for these are retrieval or upper-bound dates and are marked as such.

**Discrepancies to resolve:**
- Board Agenda says the FRC's earlier thematic review found none of six large firms monitored the quality impact of their tools; the landscape file describes firms as still building monitoring. The FRC review itself was not opened here, so this is not used as a fact.
- The Deloitte and CAQ audit committee report appears dated 22 Sep 2026 (press and Accounting Today) and 8 Oct 2026 (DART).
- The Provectus page gives three different efficiency figures for the same engagement.
- Caseware's homepage shows different results panels on different retrievals.

**Search-only leads (not opened):** an arXiv preprint predicting CAMs from 10-K MD&A text with four models; an Iowa State working paper on AI-generated versus auditor CAMs; a Regensburg FinBERT study of KAM informativeness; the GIAA Writing Engine (GIAA-BLOG-2024); the ICAEW AuditBot breakfast (ICAEW-AAC-2026); Nace.AI and BDO Belgium audit-innovation postings; ICANN audit committee minutes in which an audit firm said it uses AI.

**Searches used:** about 14 of the rationed searches. Remaining directions: the full AICPA practice aid; the Caseware, TR and Ideagen customer references; PCAOB inspection reports for 2026 on disclosure and audit committee findings; KPMG and EY on audit committee communications tooling.
