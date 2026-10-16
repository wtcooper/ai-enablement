# Assurance / completion-reporting: discourse angle

- **Archetype:** assurance
- **Module:** completion-reporting (disclosure checklists and financial-statement review, subsequent events, going concern, written representations, summary of misstatements, engagement quality review, key/critical audit matters, audit committee communications, opinion and report drafting)
- **Angle:** discourse (what practitioners, audit committee members and commentators have said in roughly the last 12-18 months)
- **Prepared:** 2026-10-16. Source landscape: `research/runs/wave1/landscape-assurance.md`. Controlled values: `research/briefs/templates/vocabulary.md`.
- **Method note.** Pages were fetched with `curl` (PDFs with `pdftotext`; Crossref for the academic record). Every source in section 5 was opened by this analyst unless marked `search-only`. Twenty-one web searches were used. Reddit, the Gartner August 2026 release, Wolters Kluwer, Trullion, PCAOB pages, MindBridge and the AAA journal page refused access. Quotations are under 25 words.

---

## 1. Summary

- **The public discourse about completion and reporting is narrow and lopsided.** It centres on one step, the disclosure checklist, plus the final tie-out. Two other threads are loud but are not about AI doing the work: audit committees asking how their auditor uses AI, and regulators restating that the human auditor stays accountable. Most other steps in the module have no public discussion of AI at all (see section 3, open questions).
- **Disclosure checklist agents are the one completion step with live, dated evidence, and all of it is vendor-published.**
  - Thomson Reuters launched Disclosure Review on 2026-09-23. It says about 30% of eligible Disclosure-module customers use it and the tool produces close to 300 analyses a month (TR-DISCLOSURE-2026).
  - Caseware reports an average 2.7 hours saved per checklist run in its beta, "varying by engagement" (CASEWARE-CWX-2026).
  - KPMG announced a Financial Report Analyzer to help complete checklists on 2025-04-22 (KPMG-CLARA-2025).
  - No published override rate, error rate, parallel-run result or inspection finding exists for any of them.
- **Practitioners frame the tools as moving work from "search" to "review", and they argue about what review then means.**
  - Fieldguide says review hours rise as preparation falls (FIELDGUIDE-REVIEW-2026).
  - DataSnipper's panel asked what a human attests to when one agent prepares, another reviews and the person signs (DS-CONNECT-2026).
  - In DataSnipper's own survey, 80% are comfortable with AI extracting data and 38% with AI signing off (DS-AIREPORT-2026).
  - The AICPA says a second AI tool checking the first does not reduce the auditor's supervision and review duties (AT-AICPAPA-2026).
- **Audit committees are now a source of discourse in their own right.**
  - CPAB's July 2026 summary of audit committee forums says committees want transparency on auditors' AI use, how professional scepticism is preserved, and the effect on fees and talent (CPAB-AC-2026).
  - Deloitte and the CAQ report that 75% of audit committee respondents ranked AI governance a top-three priority, up from 35%. Only 56% were confident they could oversee it (AT-ACRISK-2026).
  - The PCAOB added a research project on communications with audit committees on 2026-09-30 (TR-PCAOBAGENDA-2026).
- **What worries people:**
  - automation bias, with the FRC guidance criticised for burying it in one paragraph (ICAEW-FRCVIEW-2026);
  - erosion of junior auditors' skill-building (AT-PCAOBAI-2025);
  - liability when an AI-assisted output is wrong (DACB-2026);
  - the expectation gap and audit fees (CPAB-AC-2026);
  - fluent but wrong AI-drafted text, shown by hallucination retractions at Big Four firms, none of them audit opinions (BIG4NEWS-2026).
- **Quality evidence.** No independent measure of accuracy for a completion-stage tool in live use was found. The nearest items are one peer-reviewed perception survey of a disclosure-audit tool at a German Big 4 firm (FABIAN-2026) and two synthetic benchmarks that cover audit work but are not specific to completion (ARXIV-FINAUDITING-2025, ARXIV-FAB-2026).

---

## 2. Use cases

Twelve candidates. None is graded A. Grades by count: B 2, C 6, D 4. Ideas (D) are labelled "idea" in `notes`. Steps with no public evidence are not listed here; they are in section 3, "Open questions".

```yaml
- id: assurance-completion-reporting-01
  title: "AI answers disclosure-checklist requirements against the draft financial statements, with citations"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "A fully completed disclosure checklist can run 1,200 to 1,500 requirements (Thomson Reuters, for its own Guided Assurance checklist). Thomson Reuters says fatigue sets in and that many firms roll last year's checklist forward or spend senior and manager time redoing it. A missed disclosure can surface as an inspection finding, peer review deficiency or restatement, per the same post."
  solution: "A tool reads the draft statements and marks each requirement identified or not found, with a plain-language rationale and a citation back to the place in the statements. The auditor reviews, refines, accepts or overrides each suggestion inside the engagement workflow. Thomson Reuters, Caseware and KPMG describe versions of this."
  outcomes:
    - { lever: speed, description: "Average review time saved per disclosure checklist run in beta", figure: "2.7 hours", measures: "average hours saved per disclosure checklist run, reported by firms in Caseware's CwX 2026 beta program results; the page says results vary by engagement. The launch press release gives the same figure as 'per workflow', so the unit is not consistent across Caseware's own documents", provenance: vendor-published, source_ref: CASEWARE-CWX-2026 }
    - { lever: capacity, description: "Adoption after an extended customer beta", figure: "roughly 30% of eligible customers; close to 300 analyses a month", measures: "share of eligible Disclosure-module customers already using Disclosure Review, and disclosure review analyses generated a month across mid-sized and large firms, in Thomson Reuters' words; no denominator for the analyses", provenance: vendor-published, source_ref: TR-DISCLOSURE-2026 }
  prerequisites:
    - "Checklist content held inside the platform, and draft statements in a readable form"
    - "Tool tested for its intended use and monitored for unexpected behaviour, as the FRC mitigations list describes (KN-FRC-2026)"
    - "Clear terms with the client on AI use and data (ICAEW-POD-2025)"
  risks_and_guardrails:
    - "FRC lists omissions and distortions among the ways an AI output can be deficient, and says reviewers need the competence to spot them (KN-FRC-2026)"
    - "A completed checklist proves coverage, not adequacy. Fieldguide notes segment-reporting comment letters kept rising after checklist rows were added (FIELDGUIDE-DISC-2026)"
    - "Caseware says suggestions can be reviewed, refined, accepted or overridden by the auditor inside the engagement workflow (CASEWARE-VERITY-2026)"
  human_checkpoints:
    - "Reviewer accepts, edits or rejects each identified or not-found call"
    - "Senior or manager still decides conditional requirements such as 'if material'"
  role_evolution: "Staff move from searching the statements to reviewing, validating and learning, in the words of Caseware's chief product officer (CASEWARE-CWX-2026). Thomson Reuters says the visible rationale helps junior staff learn the requirement (TR-DISCLOSURE-2026)."
  evidence_grade: C
  sources:
    - { ref: TR-DISCLOSURE-2026, title: "Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/", date: 2026-09-23, access: full, locator: "paragraphs 2-3 (checklist size, stakes) and the paragraph beginning 'We've spent months validating'" }
    - { ref: CASEWARE-CWX-2026, title: "CwX 2026: how agentic AI is transforming audit and assurance", publisher: Caseware, type: conference, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance", date: 2026-06, access: full, locator: "section on the Disclosure Checklist Agent" }
    - { ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements", date: 2026-05-20, access: full, locator: "paragraph listing the first workflow-embedded agents" }
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: 2025-04-22, access: full, locator: "paragraph on the Financial Report Analyzer AI engine" }
    - { ref: KN-FRC-2026, title: "Navigating Generative and Agentic AI: The FRC's Latest Expectations for Auditors", publisher: Kingsley Napley, type: press, url: "https://www.kingsleynapley.co.uk/insights/blogs/regulatory-blog/navigating-generative-and-agentic-ai-the-frcs-latest-expectations-for-auditors", date: 2026-04-22, access: full, locator: "risk categories and mitigations lists" }
    - { ref: FIELDGUIDE-DISC-2026, title: "The 2026 audit disclosure checklist: What to add, and where judgment takes over", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/audit-disclosure-checklist-2026", date: 2026-08-06, access: full, locator: "section 'A checklist confirms coverage while quality requires judgment'" }
    - { ref: ICAEW-POD-2025, title: "Behind the Numbers: How should audit firms use AI?", publisher: ICAEW, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "transcript, exchange on client data and engagement-letter terms" }
  last_reviewed: 2026-10-16
  notes: "No named audit firm was found confirming use of a checklist agent in a live engagement, so grade C. Caseware also reports 94% accuracy on 'golden dataset items captured from beta traces' and a reduction from 15-20 minutes to under two minutes per interaction (CASEWARE-VERITY-2026); these describe the whole Verity platform, not the checklist agent, and were not used as outcomes. KPMG's release gives no figures. The 'DAS' workflow named in the Caseware press release is not explained in the page."

- id: assurance-completion-reporting-02
  title: "AI second look on a checklist the team has already completed, flagging divergence"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "A signed checklist can hide questions answered wrongly because a requirement was misread, and re-checking everything by hand is what the tool is meant to avoid."
  solution: "The tool checks the AI's reading of each requirement against the auditor's own answer and flags where the two diverge, so reviewers look only at the differences. Caseware says beta firms also used its agent to review completed checklists."
  outcomes:
    - { lever: quality, description: "One reported case where the agent surfaced questions answered incorrectly because of misinterpretation and explained the correct reading", figure: "none published (single anecdote)", measures: "one instance described by Caseware from its beta program; no count of checklists reviewed, no rate", provenance: vendor-published, source_ref: CASEWARE-CWX-2026 }
    - { lever: speed, description: "Divergences flagged automatically so teams are not re-checking everything", figure: "none published", measures: "no figure given", provenance: vendor-published, source_ref: TR-DISCLOSURE-2026 }
  prerequisites:
    - "A first-pass checklist answered by a person, or by the first tool"
    - "A way to record each divergence and how it was resolved in the file"
  risks_and_guardrails:
    - "If reviewers over-trust the second look, the same misreading can pass both checks. The FRC guidance refers to automation bias and calls for reviewer competence (ICAEW-FRCVIEW-2026)"
  human_checkpoints:
    - "Auditor resolves every flagged divergence"
  role_evolution: "Senior and manager time shifts from re-doing the checklist to resolving flagged differences, per Thomson Reuters (TR-DISCLOSURE-2026)."
  evidence_grade: C
  sources:
    - { ref: TR-DISCLOSURE-2026, title: "Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/", date: 2026-09-23, access: full, locator: "paragraph beginning 'Where the AI and the auditor's own judgment diverge'" }
    - { ref: CASEWARE-CWX-2026, title: "CwX 2026: how agentic AI is transforming audit and assurance", publisher: Caseware, type: conference, url: "https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance", date: 2026-06, access: full, locator: "paragraph beginning 'Firms also found the agent useful as a quality check'" }
    - { ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05, access: full, locator: "section 'Misinterpretation or misuse will take the most work for audit firms'" }
  last_reviewed: 2026-10-16
  notes: "Both vendor sources are descriptions, not measurements."

- id: assurance-completion-reporting-03
  title: "AI proposes 'no' and 'not applicable' determinations on checklist items"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "The hardest checklist calls are the conditional ones ('if material', 'unless impracticable'). DataSnipper says they lean on experienced staff, which limits how much juniors can do."
  solution: "Thomson Reuters says future Disclosure Review capabilities will extend into the harder judgment calls such as 'no' and 'not applicable'. No release date or design was given."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none published", measures: "announcement of intent only", provenance: vendor-published, source_ref: TR-DISCLOSURE-2026 }
  prerequisites:
    - "Reliable 'identified or not found' matching first (use case 01)"
    - "A documented basis for materiality and applicability that the tool can cite"
  risks_and_guardrails:
    - "Fieldguide says a checklist cannot confirm a disclosure is right or catch a file that omits something material (FIELDGUIDE-DISC-2026)"
    - "FRC lists faulty reasoning among the ways an AI output can be deficient (KN-FRC-2026)"
  human_checkpoints:
    - "Senior or manager owns the applicability and materiality decision"
  role_evolution: "Not stated. DataSnipper argues AI-assisted suggestions let juniors handle more while seniors focus on judgment and oversight (DS-RISKS-2026)."
  evidence_grade: C
  sources:
    - { ref: TR-DISCLOSURE-2026, title: "Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/", date: 2026-09-23, access: full, locator: "paragraph beginning 'Future capabilities will extend further'" }
    - { ref: DS-RISKS-2026, title: "5 hidden risks in disclosure review", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/5-hidden-risks-in-disclosure-review", date: 2026, access: full, locator: "risk on judgment-heavy conditional requirements" }
    - { ref: FIELDGUIDE-DISC-2026, title: "The 2026 audit disclosure checklist: What to add, and where judgment takes over", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/audit-disclosure-checklist-2026", date: 2026-08-06, access: full, locator: "section 'A checklist confirms coverage while quality requires judgment'" }
  last_reviewed: 2026-10-16
  notes: "The DataSnipper page carries no byline date; the year comes from its reference to DataSnipper Connect New York 2026. Grade C because the only evidence is a vendor statement about a future feature."

- id: assurance-completion-reporting-04
  title: "AI matches narrative reports and other information to statutory disclosure requirements and checks them for errors"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Auditing a management report has been manual and checklist-based. Fieldguide describes the read of MD&A and other front-section text for inconsistencies with the statements as tedious, and says late-stage edits break cross-references and comparatives."
  solution: "A task-specific AI platform finds the passages in the management report, links each to the statutory requirement, checks for calculation errors, highlights changes between report versions, and supports review and documentation within the team. The study describes it as supporting key steps, not replacing professional judgement."
  outcomes:
    - { lever: quality, description: "Auditors' perception that the tool improves effectiveness and efficiency, less so for complex qualitative issues", figure: "none quantified in the abstract or release", measures: "auditors' perceptions of effectiveness and efficiency, from a survey of employees of a Big 4 audit firm in Germany; sample size not seen", provenance: independent, source_ref: FABIAN-2026 }
  prerequisites:
    - "Training, clear communication of opportunities and risks, and staff involvement in the change, which the authors name as conditions"
  risks_and_guardrails:
    - "Perceived deskilling and trust in outputs vary with role, expertise and involvement in digital transformation (FABIAN-2026)"
    - "The tool reaches its limits on discretionary leeway, linguistic nuance and strategic statements, per the university release (FABIAN-2026)"
  human_checkpoints:
    - "Auditor reviews and documents each suggestion; the tool supports dual-control review"
  role_evolution: "Perceptions of benefit depend on professional position and involvement in digital transformation; some auditors raise over-reliance and skill loss (FABIAN-2026)."
  evidence_grade: B
  sources:
    - { ref: FABIAN-2026, title: "Auditing Corporate Disclosures with the Assistance of Task-Specific Artificial Intelligence: Evidence on Effectiveness and Efficiency", publisher: Journal of Information Systems (AAA), type: academic, url: "https://doi.org/10.2308/ISYS-2025-054", date: 2026-03-03, access: full, locator: "abstract (Crossref record) and University of Hamburg news release; full paper not opened" }
    - { ref: FIELDGUIDE-DISC-2026, title: "The 2026 audit disclosure checklist: What to add, and where judgment takes over", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/audit-disclosure-checklist-2026", date: 2026-08-06, access: full, locator: "section 'The other-information read'" }
  last_reviewed: 2026-10-16
  notes: "Grade B is generous: the paper documents a real in-use tool at a Big 4 firm in Germany, but the firm is anonymised, so the 'named organization' test is not met; treat as C if applied strictly. The evidence is perception data, not an error rate. The management report is a German statutory document, so transfer to US MD&A is untested."

- id: assurance-completion-reporting-05
  title: "AI ties out the final financial statements (arithmetic, cross-statement, prior-year and version checks)"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Suralink describes tie-out as the last and most critical step of the audit, and says many firms still do it with lengthy manual procedures that are prone to human error."
  solution: "Software checks mathematical accuracy, internal consistency, prior-year consistency and version comparison of the final statements. PwC described a tool for statement review and tie-out being tested on certain asset and wealth management engagements."
  outcomes:
    - { lever: speed, description: "none published", figure: "none published", measures: "no time or error figures in the PwC briefing or the Suralink release", provenance: vendor-published, source_ref: SURALINK-2026 }
  prerequisites:
    - "Final draft statements in a machine-readable form"
    - "Prior-year statements and earlier draft versions available to compare"
  risks_and_guardrails:
    - "Exceptions still need a person. DataSnipper says its agents handle vouching, tie-outs and extraction while 'the auditor still holds the pen' (DS-CONNECT-2026)"
    - "A mechanical tie-out cannot show a disclosure is adequate (FIELDGUIDE-DISC-2026)"
  human_checkpoints:
    - "Preparer or reviewer clears each exception before the report is issued"
  role_evolution: "Not stated by PwC or Suralink."
  evidence_grade: B
  sources:
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraphs on financial statement review and tie-out and the Audit Innovation Hub" }
    - { ref: SURALINK-2026, title: "Suralink Launches Financial Statement Tie Out, Redefining the Final Mile of the Audit", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/08/suralink-launches-financial-statement-tie-out-redefining-the-final-mile-of-the-audit/181200/", date: 2026-04-08, access: full, locator: "paragraph listing the four validation areas" }
    - { ref: DS-CONNECT-2026, title: "The 6 Biggest Takeaways from DataSnipper Connect New York 2026", publisher: DataSnipper, type: conference, url: "https://www.datasnipper.com/resources/the-6-biggest-takeaways-from-datasnipper-connect-new-york-2026", date: 2026-09, access: full, locator: "section introducing Alwin" }
  last_reviewed: 2026-10-16
  notes: "Grade B rests on PwC's statement that the Audit Innovation Hub 'is currently being tested' on certain asset and wealth management engagement teams and that the pilot would expand. It covers non-registered fund-to-fund audits under AICPA standards, which is narrower than a general tie-out. Suralink is a vendor launch with no named firm. The DataSnipper page date is approximate (September 2026 per the page's listing data)."

- id: assurance-completion-reporting-06
  title: "AI checks the whole engagement file for open issues and sign-off readiness before partner review"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Reviewers and partners find gaps late. Caseware says managers need faster reviews and partners earlier visibility of sign-off readiness and inspection risks."
  solution: "Caseware says managers can use cross-file risk checks, unresolved-issue tracking and automated review pack generation, and partners get earlier visibility of sign-off readiness, inspection risks and engagement findings. Pattern 'other': a file-level completeness and readiness check across the engagement."
  outcomes:
    - { lever: quality, description: "none published for these functions", figure: "none published", measures: "capability list in a launch press release; the 94% and 85% figures in the same release describe the platform's beta interactions overall and are not used here", provenance: vendor-published, source_ref: CASEWARE-VERITY-2026 }
  prerequisites:
    - "Engagement file, prior year and review notes held in one platform"
    - "Firm methodology encoded in the platform"
  risks_and_guardrails:
    - "FRC says accountability stays with people and firms, and reviewers must be able to critically evaluate AI outputs (FRC-NEWS-2026)"
    - "Firms told the PCAOB that supervisors reviewing AI-assisted work should apply the same diligence as for other work (CPAPA-GENAI-2024)"
  human_checkpoints:
    - "Manager and partner decide whether each flagged item is resolved"
  role_evolution: "Caseware lists separate benefits for preparers, managers and partners (CASEWARE-VERITY-2026)."
  evidence_grade: C
  sources:
    - { ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements", date: 2026-05-20, access: full, locator: "paragraph beginning 'Caseware says the ecosystem is designed to deliver value across multiple roles'" }
    - { ref: CPAPA-GENAI-2024, title: "How Auditors Are Currently Using Generative AI", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=108316", date: 2024-07-23, access: full, locator: "list of potential areas, including completeness of audit documentation (reports PCAOB outreach from 2024; foundation only)" }
    - { ref: FRC-NEWS-2026, title: "Innovative new guidance supports audit firm adoption of emerging AI technologies", publisher: Financial Reporting Council, type: regulator, url: "https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/", date: 2026-03-30, access: full, locator: "paragraph on unchanged regulatory accountability" }
  last_reviewed: 2026-10-16
  notes: "Announced capability. The PCAOB outreach report is from July 2024, outside the 12-18 month window; it is cited only as the earliest regulator list of 'potential areas'."

- id: assurance-completion-reporting-07
  title: "AI agents for financial statement analysis and statement review at completion"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Final review of the draft statements, including analytical comparison with audited amounts, is manual."
  solution: "KPMG said further agents would be deployed over the following 12 months into controls testing, financial statement analysis and more. PwC said it plans tools to guide the financial statement review and tie-out portion of the audit."
  outcomes:
    - { lever: speed, description: "none published", figure: "none published", measures: "announcements only", provenance: self-reported, source_ref: KPMG-CLARA-2025 }
  prerequisites:
    - "Statements and audit-adjusted figures available to the tool"
  risks_and_guardrails:
    - "PCAOB-reported firm view that AI would augment, not replace, human review (CPAPA-GENAI-2024)"
  human_checkpoints:
    - "Reviewer concludes on any unexplained difference"
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: 2025-04-22, access: full, locator: "paragraph beginning 'Additional AI agents will be deployed over the next 12 months'" }
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraph beginning 'Panson said PwC is also planning to equip its auditors with tools'" }
  last_reviewed: 2026-10-16
  notes: "Whether either firm shipped a financial statement analysis agent was not found in the pages opened. KPMG's 12-month window ended in April 2026."

- id: assurance-completion-reporting-08
  title: "AI reads audit committee communications to surface issues earlier"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [research-synthesis, client-interaction]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Issues raised in audit committee communications can surface late in the audit cycle."
  solution: "PwC's assurance leader described a tool that analyzes audit committee communications to surface issues that need handling sooner in the audit preparation cycle, as one of several AI tools PwC will use for 2026 year-end audits."
  outcomes:
    - { lever: speed, description: "none published", figure: "none published", measures: "one sentence in a trade-press interview; no usage or time figures", provenance: self-reported, source_ref: CFODIVE-PWC-2026 }
  prerequisites:
    - "Access to audit committee papers and minutes in digital form"
  risks_and_guardrails:
    - "The same interview says PwC's audit report 'still looks the same' and professional standards still apply (CFODIVE-PWC-2026)"
  human_checkpoints:
    - "Engagement team decides what to raise with the audit committee"
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "paragraph beginning 'For 2026 year-end audits'" }
  last_reviewed: 2026-10-16
  notes: "The article does not say whether the tool reads communications sent to, or received from, the audit committee. The only public description is this one sentence. Context: the PCAOB opened a research project on communications with audit committees on 2026-09-30 (TR-PCAOBAGENDA-2026)."

- id: assurance-completion-reporting-09
  title: "Idea: a reviewing agent checks the preparing agent's work before the human reviewer"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "As agents prepare more of the file, human review becomes the bottleneck and the main control."
  solution: "The AICPA practice aid says one AI tool may be used to help the auditor judge whether another is performing correctly, without reducing supervision and review duties. The FRC guidance says reviews may be done by humans, other LLMs or rules-based protocols. A DataSnipper conference panel posed the case of one agent preparing, another reviewing and a human signing."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "no measurement found", provenance: self-reported, source_ref: AT-AICPAPA-2026 }
  prerequisites:
    - "A defined audit methodology the agents run inside, with traceable outputs"
    - "Evaluation sets to show the reviewer agent catches what a person would"
  risks_and_guardrails:
    - "The second tool does not take the place of the auditor's supervision and review (AT-AICPAPA-2026)"
    - "In DataSnipper's survey of 200+ audit and finance professionals, 80% were comfortable with AI extracting data and 38% with AI signing off (DS-AIREPORT-2026)"
    - "A reviewer agent trained on similar data may share the first agent's blind spots (analyst question, not stated in the sources)"
  human_checkpoints:
    - "The human reviewer and partner still sign"
  role_evolution: "Grant Thornton's director of audit and professional standards, on the ICAEW podcast, expected AI reviewing 'a few years down the line' as the direction of travel (ICAEW-POD-2025)."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraph beginning 'The guidance also said that, in an audit of financial statements, one AI tool may be used'" }
    - { ref: KN-FRC-2026, title: "Navigating Generative and Agentic AI: The FRC's Latest Expectations for Auditors", publisher: Kingsley Napley, type: press, url: "https://www.kingsleynapley.co.uk/insights/blogs/regulatory-blog/navigating-generative-and-agentic-ai-the-frcs-latest-expectations-for-auditors", date: 2026-04-22, access: full, locator: "mitigations list, first item" }
    - { ref: DS-CONNECT-2026, title: "The 6 Biggest Takeaways from DataSnipper Connect New York 2026", publisher: DataSnipper, type: conference, url: "https://www.datasnipper.com/resources/the-6-biggest-takeaways-from-datasnipper-connect-new-york-2026", date: 2026-09, access: full, locator: "2026 audit trends panel section" }
    - { ref: DS-AIREPORT-2026, title: "2026 AI Report: Everyone says AI is essential. Almost no one has embedded it.", publisher: DataSnipper, type: survey, url: "https://www.datasnipper.com/resources/ai-report-2026-ai-in-audit-and-finance", date: 2026-06, access: full, locator: "landing-page summary of findings" }
    - { ref: ICAEW-POD-2025, title: "Behind the Numbers: How should audit firms use AI?", publisher: ICAEW, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "section 'Understanding explainability and the need for human oversight'" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). Discussed by a standard-setter, a regulator, and practitioners, but no named deployment was found. The DataSnipper survey is a vendor survey; the landing page does not state its sample method beyond '200+ audit and finance professionals'."

- id: assurance-completion-reporting-10
  title: "Idea: a verification gate for AI-drafted memos and completion documentation"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "AI-drafted text can be fluent and wrong. Big4News reports that EY Canada withdrew a report after an outside check found 16 of 27 references hallucinated, and argues that partners' high-level review habits do not catch this."
  solution: "Source-checking of AI-drafted documentation before it enters the file or goes out, for example mandatory citation checks and disclosure of AI use, as Big4News proposes. The FRC guidance lists fabricated material and omissions among deficient-output risks, and the FinancialAuditBench authors found agents sometimes produce incorrect documentation."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "no measurement of a verification gate found", provenance: independent, source_ref: ARXIV-FAB-2026 }
  prerequisites:
    - "AI-drafted content is identifiable as such"
    - "Source citations kept with each drafted statement"
  risks_and_guardrails:
    - "The retractions were consulting and thought-leadership reports, not audit opinions; transfer to audit documents is an inference"
    - "Review checks that look only for presence, not truth, add cost without catching fabrication (analyst note)"
  human_checkpoints:
    - "Named person verifies each cited source before sign-off"
  role_evolution: "Big4News expects stronger partner accountability to be needed (BIG4NEWS-2026)."
  evidence_grade: D
  sources:
    - { ref: BIG4NEWS-2026, title: "The Big Four AI Arms Race, Evergrande, Governance and Culture", publisher: Big4News, type: press, url: "https://www.big4news.com/p/big-four-news-20-may-2026", date: 2026-05-20, access: full, locator: "section 'EY Canada Retracts Report after GPTZero Investigation'" }
    - { ref: KN-FRC-2026, title: "Navigating Generative and Agentic AI: The FRC's Latest Expectations for Auditors", publisher: Kingsley Napley, type: press, url: "https://www.kingsleynapley.co.uk/insights/blogs/regulatory-blog/navigating-generative-and-agentic-ai-the-frcs-latest-expectations-for-auditors", date: 2026-04-22, access: full, locator: "risk category 'deficient output'" }
    - { ref: ARXIV-FAB-2026, title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.32835", date: 2026-09-26, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The Big4News claim about the retraction is a newsletter's account of an outside investigation; the GPTZero report itself was not opened. A later passage says all four Big Four networks had experienced failures involving apparent AI-generated content by August 2026; not independently checked."

- id: assurance-completion-reporting-11
  title: "Idea: agents complete and review workpapers for staff-level audit tasks"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "Preparing and cleaning up workpapers consumes staff time before a reviewer can look at the file."
  solution: "A benchmark of 90 workpaper completion and review tasks across six synthetic engagements finds that agents complete substantial portions of staff-level tasks well but sometimes perform inappropriate procedures or produce incorrect documentation. Caseware has a Document Intelligence Agent in closed beta that extracts information from source documents into workpapers."
  outcomes:
    - { lever: capacity, description: "Agents complete substantial portions of staff-level tasks on synthetic engagements", figure: "90 tasks; eleven frontier models", measures: "number of tasks in the benchmark (workpaper completion and review across six synthetic audit engagements, about 179 files each) and models evaluated; the abstract gives no pass rates", provenance: independent, source_ref: ARXIV-FAB-2026 }
  prerequisites:
    - "Firm-specific evaluation sets, since a public synthetic benchmark does not show performance on the firm's own files"
  risks_and_guardrails:
    - "Inappropriate procedures and incorrect documentation were observed in the benchmark (ARXIV-FAB-2026)"
  human_checkpoints:
    - "Reviewer checks procedures performed and documentation produced"
  role_evolution: "Fieldguide argues review, not preparation, becomes the core of the job and that review hours rise at first (FIELDGUIDE-REVIEW-2026)."
  evidence_grade: D
  sources:
    - { ref: ARXIV-FAB-2026, title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.32835", date: 2026-09-26, access: full, locator: "abstract" }
    - { ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements", date: 2026-05-20, access: full, locator: "paragraph on the Document Intelligence Agent, currently in closed beta" }
    - { ref: FIELDGUIDE-REVIEW-2026, title: "Review Is the New Prepare: The Auditor's Job in an Agent-First World", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/review-is-the-new-prepare", date: 2026-07-29, access: full, locator: "paragraphs 5-6 (review hours) and developmental-objection section" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The benchmark tasks are generic workpaper tasks, not completion-stage steps, so any measurement from it is an adjacent-process figure and would cap a grade at B. The Fieldguide date is the on-page label; no machine-readable date was found."

- id: assurance-completion-reporting-12
  title: "Idea: AI checks tagging and cross-document consistency in filed statements"
  archetype: assurance
  module: completion-reporting
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Fieldguide says tagging errors such as sign flips on credit balances and custom tags where a standard tag existed still draw SEC comments, and that one person should own the tagging review. Auditors do not attest XBRL in that setting."
  solution: "Researchers built a benchmark of 1,102 instances from real XBRL filings to test whether LLMs can match concepts, model taxonomy relations and reason across documents. Thirteen state-of-the-art models showed substantial gaps."
  outcomes:
    - { lever: quality, description: "Substantial gaps in concept retrieval, taxonomy-aware relation modelling and cross-document reasoning", figure: "1,102 instances; 13 models", measures: "annotated instances in the benchmark (averaging over 33k tokens each) and number of LLMs evaluated; no overall accuracy given in the abstract", provenance: independent, source_ref: ARXIV-FINAUDITING-2025 }
  prerequisites:
    - "Structured filings and a taxonomy the tool can use"
  risks_and_guardrails:
    - "Current models fail on cross-document reasoning in the benchmark (ARXIV-FINAUDITING-2025)"
  human_checkpoints:
    - "Named reviewer owns the tagging review (FIELDGUIDE-DISC-2026)"
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - { ref: ARXIV-FINAUDITING-2025, title: "FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2510.08886", date: 2025-10-10, access: full, locator: "abstract" }
    - { ref: FIELDGUIDE-DISC-2026, title: "The 2026 audit disclosure checklist: What to add, and where judgment takes over", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/audit-disclosure-checklist-2026", date: 2026-08-06, access: full, locator: "section 'XBRL'" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The Fieldguide piece describes human review of tagging; it does not propose AI for it. The idea rests on the benchmark's framing of auditing as a structured extraction and consistency problem. The arXiv record shows v1 on 2025-10-10 and a revision in May 2026; it was accepted at SIGIR 2026 (Resource Track)."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Disclosure checklist and financial-statement review** (review-assurance, data-reporting). The one step with named products. Section 2, use cases 01-04.
- **Tie-out and consistency read of final statements and other information** (review-assurance, data-reporting). Use cases 04-05; Fieldguide describes the other-information read as the check that catches late edits (FIELDGUIDE-DISC-2026).
- **File completion and sign-off readiness** (review-assurance, coordination-scheduling). Use case 06.
- **Final analytical review of the statements** (review-assurance, data-reporting). Use case 07.
- **Audit committee communications** (client-interaction, document-production). Use case 08. Committees' own questions about the auditor's AI use are in the concerns list below.
- **Open questions: steps with no public evidence of AI use found.** Each was searched, and none turned up a firm, vendor or practitioner account of AI doing or assisting the step.
  - **Going concern evaluation** (expert-judgment). The PCAOB put a going concern project back on its standard-setting agenda on 2026-09-30 with no timing, and the agenda text quoted in the press does not mention AI (TR-PCAOBAGENDA-2026). The IAASB revised ISA 570, effective for periods beginning on or after 2026-12-15, according to a South African practitioner article (ACCWEEKLY-GC-2026). Search surfaced academic machine-learning prediction papers (2025) that were not opened (search-only). Fieldguide mentions a "second-stage going concern call" as human judgment (FIELDGUIDE-DISC-2026).
  - **Subsequent events** (research-synthesis). Only DataSnipper lists the disclosure in its example scope (DS-RISKS-2026). No account of AI reading post-year-end minutes, legal letters or interim figures was found.
  - **Written representations** (document-production, client-interaction). The ICAEW article on letters of representation (May 2026) discusses process failures and legal weight with no AI content (ICAEW-REPLETTER-2026). The only AI link found is the AICPA practice aid saying an auditor may need AI-related representations from management, such as identification of AI used by the entity (AT-AICPAPA-2026). That concerns client AI, not an AI-drafted letter. See section 4.
  - **Summary of misstatements and evaluation** (data-reporting, expert-judgment). Nothing found.
  - **Engagement quality review** (review-assurance, expert-judgment). A search on AI-assisted EQR found only background on ISQM 2. The only public statement is a vendor line that EQRs "maintain the same standards" (Fieldguide, `ai-audit-preparation-reporting` page, not cited because it carries no date and says little).
  - **Key/critical audit matters** (expert-judgment, document-production). A search found nothing on AI and CAMs or KAMs.
  - **Opinion and report drafting** (document-production). Fieldguide says its agents are not "ChatGPT writing audit opinions" and that all outputs need reviewer approval (not cited as a use case; the page is undated). A July 2024 PCAOB outreach report says some firms let staff use GenAI for initial drafts of memos and presentations (CPAPA-GENAI-2024). No firm described AI-drafted opinions or audit report text.

### Common pain points

- Checklists of 1,200 to 1,500 requirements, with fatigue "by question 200"; roll-forward of last year's checklist (TR-DISCLOSURE-2026).
- Evidence not linked to requirements, conditional requirements concentrated on seniors, inconsistent progress tracking, and hours-to-days of manual review for large entities (DS-RISKS-2026).
- A signed checklist that proves coverage but not adequacy, with SEC segment comments rising from 16% to 23% of reviews with comment letters in the Deloitte review Fieldguide cites (FIELDGUIDE-DISC-2026).
- Late-stage review burden and error risk in the final tie-out (SURALINK-2026).
- Representation letters sitting in an inbox rather than on the file, and deficiencies in how they are produced (ICAEW-REPLETTER-2026).
- Talent supply: Thomson Reuters says 75% of audit partners are scheduled to retire within ten years and entry-level interest is falling. This is a vendor executive's claim (TR-STATE-2026).

### Metrics and benchmarks

- 2.7 hours saved per checklist run, average, beta firms, vendor-published (CASEWARE-CWX-2026). The launch release says "per workflow" (CASEWARE-VERITY-2026).
- About 30% of eligible Disclosure-module customers use Thomson Reuters' tool; close to 300 analyses a month (TR-DISCLOSURE-2026).
- DataSnipper 2026 AI Report, 200+ audit and finance professionals, vendor survey: 73% call AI essential; 13% have it integrated into real workflows; 80% comfortable with AI extracting data, 38% with sign-off (DS-AIREPORT-2026). The page says trust fell sharply in 2026; the figures (78% to 55%; partners who review AI-assisted work at 79%, contributors who produce it at 50%) come from the Connect conference write-up (DS-CONNECT-2026), not the report page.
- CAQ Audit Partner Pulse, Spring 2026 (sample size not seen on pages opened): AI governance the top audit committee challenge at 57% (cybersecurity 51%, finance transformation 36%); at the partner's largest client AI governance maturity is advanced for 6%, developed but incomplete for 40%, early-stage or reactive for 46%; two-thirds say the audit committee raised AI in operations or reporting unprompted in the last 12 months (BOARDMEMBER-CAQ-2026). Accounting Today's report of the same survey says nearly 90% described governance maturity at their largest client as 'developing' or 'early stage' (AT-CAQPULSE-2026).
- Deloitte and CAQ Audit Committee Practices Report (248 chairs and members, published 2026-09-22; figures from Accounting Today, DELOITTE-CAQ-2026 gives the survey frame): 54% more focused on emerging risks; primary responsibility for AI governance rose from 20% to 29%; 82% of those overseeing it call their oversight emerging or limited; 75% rank AI governance top-three (35% last year); 56% confident in their ability to oversee it; 70% cite technology including AI as the skill that would most help (AT-ACRISK-2026; survey frame in DELOITTE-CAQ-2026).
- PwC US assurance leader, 2026-10-07: busy-season time saved so far is "not that drastic yet" (CFODIVE-PWC-2026).
- Benchmarks: FinAuditing 1,102 instances, 13 LLMs (ARXIV-FINAUDITING-2025); FinancialAuditBench 90 tasks, 11 models (ARXIV-FAB-2026). Neither is specific to completion.
- **Quality evidence is absent.** No override rate, error rate, parallel-run result, inspection finding or independent measure was found for any completion-stage tool. The nearest independent items are one perception survey (FABIAN-2026) and the two synthetic benchmarks above.

### Guardrails and regulatory points

- **FRC (UK), 2026-03-30:** the first guidance from any audit regulator on generative and agentic AI. It says it is not a response to quality deficiencies, that human accountability is unchanged, and that firms should consider ISQM (UK) 1 (FRC-NEWS-2026). Three risk categories (deficient output, misuse of output, non-compliant methodology) and mitigations covering design, testing, training and reviewer competence (KN-FRC-2026). The FRC lists AI uses including checking the accuracy of financial statements (BOARDAGENDA-2026).
- **AICPA practice aid, 2026-10-13:** the auditor remains responsible for the audit and opinion; a second AI tool does not reduce supervision and review duties; more guidance is planned on risk of material misstatement and audit evidence (JOFA-AIPA-2026, AT-AICPAPA-2026).
- **PCAOB:** inspectors will focus on AI in 2026 and many firms have invited them to see tools in pilot (AT-PCAOBAI-2025). The 2026-09-30 agendas add a research project on audit committee communications, keep going concern on the standard-setting agenda, and describe data and technology research as examining whether standards or staff guidance should change (TR-PCAOBAGENDA-2026, JOFA-PCAOBAGENDA-2026). No AI-specific auditing standard exists, per secondary sources (RSM-UAE-2026).
- **SEC Office of the Chief Accountant (Hohl, 2026-05-27):** asks auditors how they use AI to improve engagement-level quality and to monitor quality control, and says independence rules must stay fit for purpose as AI enters audit delivery (KPMG-HOHL-2026).
- **CPAB (Canada), July 2026:** audit committees want transparency about auditors' AI use (CPAB-AC-2026).
- **Liability:** a UK law firm says ordinary negligence principles apply and an erroneous AI output is unlikely by itself to excuse the auditor; documentation of professional judgement will be critical (DACB-2026).
- **Client consent and data:** the FRC head of assurance technology and two firm representatives discussed engagement-letter terms about AI use; Deloitte's representative said very few clients had asked them not to use GenAI (ICAEW-POD-2025). The AICPA aid says AU-C 210 does not require disclosing specific tools in the engagement letter, though state law, contracts or firm policy may (AT-AICPAPA-2026).

### Frontier signals (dated)

- 2025-10-28: PwC said it hoped for tools covering every audit step, including statement review and tie-out, in calendar 2026, then a single agentic platform (PWC-AT-2025).
- 2025-11-11: FRC's head of assurance technology said agentic AI is coming "quite quickly"; Grant Thornton's director of audit and professional standards expected AI reviewing "a few years down the line" (ICAEW-POD-2025).
- 2026-03-30: FRC said agentic AI is expected to follow generative AI (FRC-NEWS-2026).
- 2026-03: a Thomson Reuters audit executive said he would watch whether the adoption "hockey stick" came at the end of 2026 or kept slipping (TR-STATE-2026).
- 2026-04-07: EY embedded agents in all audit phases and expects support for all end-to-end audit activities by 2028 (EY-CANVAS-2026).
- 2026-05-20: Caseware set a goal of automating 50% of the engagement workflow across Prepare, Plan, Evaluate and Report suites (CASEWARE-VERITY-2026).
- 2026-09-23: Thomson Reuters said it would extend into "no" and "not applicable" calls (TR-DISCLOSURE-2026).
- 2026-09-30: PCAOB agendas include research on audit committee communications (TR-PCAOBAGENDA-2026).
- 2026-10-07: PwC said time savings are modest so far and expected more as the technology and adoption improve (CFODIVE-PWC-2026).
- 2026-10-13: AICPA promised later practice-aid sections on risk of material misstatement and audit evidence (JOFA-AIPA-2026).
- 2026-12-15: revised ISA 570 effective (secondary source, ACCWEEKLY-GC-2026).

### Workforce and role effects

- "Review is the new prepare" (Fieldguide): preparation time drops, review time rises at first, and the firm argues the apprenticeship objection is backwards because preparation was never the source of judgment. Vendor argument, not measured (FIELDGUIDE-REVIEW-2026).
- PCAOB acting chair Botic said firms and educators may need new paths for juniors to build skepticism and judgment (AT-PCAOBAI-2025, NYSSCPA-PCAOB-2025).
- The ICAEW Technology Faculty chair wants training on judgement and scepticism, not only tool mechanics (ICAEW-FRCVIEW-2026).
- In the German study, perceived deskilling and trust vary by role and involvement (FABIAN-2026).
- Caseware's beta partner at Withum said the tool resembles a partner walking a junior through a checklist, at scale (CASEWARE-CWX-2026).
- Reported job effects: a news report says PwC and KPMG announced plans to cut hundreds of audit positions, attributing them to fewer mid-level departures, and that the FRC's regulatory standards director dismissed "hand-wringing and panic" (RESULTSENSE-2026; secondary).
- CPAB audit committees want to know how AI will change staffing models, skills and recruitment (CPAB-AC-2026).

### Objections and concerns practitioners raise

- **Automation bias is under-weighted in guidance.** The ICAEW Technology Faculty chair was disappointed it sat in one paragraph on page 35 of the FRC guidance (ICAEW-FRCVIEW-2026).
- **Probabilistic output.** An RSM UK analytics director on the FRC working group said no tool gives the exact output every time and a rules-based tool should sit beside the AI (ICAEW-FRCVIEW-2026).
- **Small firms and vendors.** Smaller firms lack technology teams and lean on third parties, and the guidance says too little on vendor questions (ICAEW-FRCVIEW-2026).
- **Checklist is not judgment.** Speeding the checklist alone accelerates the half that never produced findings (FIELDGUIDE-DISC-2026).
- **What does the signer attest to?** DataSnipper's panel question (DS-CONNECT-2026).
- **Trust falls with use.** Trust fell most among those producing AI-assisted work (DS-AIREPORT-2026, via DS-CONNECT-2026).
- **Expectation gap and fees.** Audit committees noted a risk if perceptions of AI-enabled audits exceed auditors' responsibilities, and want to know the effect on fees (CPAB-AC-2026). A news report says KPMG pressed its own auditor for lower fees on the basis that AI would cut costs (RESULTSENSE-2026; secondary).
- **Fluent wrong text.** RSM UAE warns AI-drafted MD&A and footnotes can read plausibly while containing errors, and that unapproved consumer tools leave no validation trail (RSM-UAE-2026; low-authority firm blog).
- **Hallucination episodes at Big Four firms,** in consulting reports (BIG4NEWS-2026).
- **Liability and accountability.** Firms cannot blame the tool (BOARDAGENDA-2026, DACB-2026).
- **Audit committees want transparency.** They ask what the auditor does with AI, under what controls, and how AI-assisted judgments are documented (TCC-PCAOBQ-2026, CPAB-AC-2026). CAQ suggests committees ask whether internal audit can test AI-driven controls and how AI affects estimates and disclosures (CAQ-ACINSIGHTS-2026), and its action plan, summarised by TheCorporateCounsel.net, tells committees to learn where the external auditor uses AI, the benefits and limits (TCC-ACAGENDA-2026). The CAQ ran a March 2026 webinar for committees on how AI in financial reporting affects the audit and their oversight (CAQ-WEBINAR-2026).
- **Early benefits are modest.** PwC's own leader says the time saved is not dramatic yet (CFODIVE-PWC-2026).
- **Evaluation burden.** A Thomson Reuters audit executive says firms must build their own muscle to test systems and not rely on vendor demos (TR-STATE-2026).

### Interview probes for an advisor in this module

1. For the disclosure checklist, who owns the "not applicable" and "if material" calls today, and what would have to be true before you let a tool propose them?
2. When a tool marks a requirement "identified", what do reviewers check, and have you recorded how often the first pass and the AI differ? Do you hold any numbers on overrides?
3. What do your audit committee chairs ask about your use of AI, what do you currently tell them, and has it come up in fee conversations?
4. Which of going concern, subsequent events, engagement quality review, key or critical audit matters and opinion drafting is AI explicitly allowed or barred from, and what is the reason in each case?
5. If one agent prepares a workpaper and another checks it, what do you want the human reviewer and the engagement quality reviewer to attest to, and where is that written down?

---

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| How an entity's AI use in financial reporting affects acceptance and continuance (management integrity, skills, team competence) | acceptance-independence | AT-AICPAPA-2026 |
| SEC chief accountant on independence rules as AI enters audit delivery; PCAOB independence project | acceptance-independence | KPMG-HOHL-2026, TR-PCAOBAGENDA-2026 |
| Big Four alliances with Anthropic and the independence question raised for EY as the one firm without one | acceptance-independence | BIG4NEWS-2026 |
| Client-side AI governance maturity (6% advanced), AI-operated controls, AI in financial reporting, AI-related representations from management, AI oversight disclosures read as other information | assurance-over-ai (and controls-testing) | BOARDMEMBER-CAQ-2026, AT-AICPAPA-2026, FIELDGUIDE-DISC-2026 |
| Audit committee oversight of management's AI use (CAQ questions, CPAB forums, Deloitte/CAQ survey) | assurance-over-ai | CAQ-ACINSIGHTS-2026, CPAB-AC-2026, AT-ACRISK-2026 |
| Firm-level tool certification, monitoring, QC 1000, FRC mitigations; negligence and accountability commentary | quality-management | KN-FRC-2026, DACB-2026, FRC-NEWS-2026 |
| Reviewer competence and automation bias (engagement-level supervision) | quality-management | ICAEW-FRCVIEW-2026 |
| Risk Suggestion Agent and planning-review demo (board minutes, trial balance, prior-year file) | planning-risk-assessment | CASEWARE-CWX-2026 |
| Document Intelligence Agent, evidence matching, DataSnipper testing-time claims (30-45 minutes to about five per selection, FGMK, vendor-reported) | substantive-testing | CASEWARE-VERITY-2026, DS-CONNECT-2026 |
| KPMG pressing its auditor for fee cuts; Big Four and mid-tier fee and staffing pressure | quality-management (firm business model lens) | RESULTSENSE-2026 |

---

## 5. Sources

Refs follow `PUBLISHER-SHORT-YYYY`. Where the landscape file already uses a key for the same document, that key is used. "Access: full" means this analyst opened the page or PDF. Where only the abstract or part was read, the locators above say so.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 |
| TR-DISCLOSURE-2026 | Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence | Thomson Reuters | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/ | 2026-09-23 |
| TR-STATE-2026 | The state of AI in audit 2026: Seven questions shaping the future | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/ | 2026-03-30 |
| CASEWARE-VERITY-2026 | Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly Into Assurance Engagements | Caseware | vendor | https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements | 2026-05-20 |
| CASEWARE-CWX-2026 | CwX 2026: how agentic AI is transforming audit and assurance | Caseware | conference | https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance | 2026-06 |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04-22 |
| EY-CANVAS-2026 | EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 |
| SURALINK-2026 | Suralink Launches Financial Statement Tie Out, Redefining the Final Mile of the Audit | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/08/suralink-launches-financial-statement-tie-out-redefining-the-final-mile-of-the-audit/181200/ | 2026-04-08 |
| DS-RISKS-2026 | 5 hidden risks in disclosure review | DataSnipper | vendor | https://www.datasnipper.com/resources/5-hidden-risks-in-disclosure-review | 2026 (page undated) |
| DS-CONNECT-2026 | The 6 Biggest Takeaways from DataSnipper Connect New York 2026 | DataSnipper | conference | https://www.datasnipper.com/resources/the-6-biggest-takeaways-from-datasnipper-connect-new-york-2026 | 2026-09 (approximate) |
| DS-AIREPORT-2026 | 2026 AI Report: Everyone says AI is essential. Almost no one has embedded it. | DataSnipper | survey | https://www.datasnipper.com/resources/ai-report-2026-ai-in-audit-and-finance | 2026-06 (approximate) |
| FIELDGUIDE-DISC-2026 | The 2026 audit disclosure checklist: What to add, and where judgment takes over | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/audit-disclosure-checklist-2026 | 2026-08-06 |
| FIELDGUIDE-REVIEW-2026 | Review Is the New Prepare: The Auditor's Job in an Agent-First World | Fieldguide | vendor | https://www.fieldguide.io/blog/review-is-the-new-prepare | 2026-07-29 (on-page label) |
| FABIAN-2026 | Auditing Corporate Disclosures with the Assistance of Task-Specific Artificial Intelligence: Evidence on Effectiveness and Efficiency | Journal of Information Systems (AAA); University of Hamburg release | academic | https://doi.org/10.2308/ISYS-2025-054 | 2026-03-03 |
| ARXIV-FINAUDITING-2025 | FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs | arXiv | academic | https://arxiv.org/abs/2510.08886 | 2025-10-10 |
| ARXIV-FAB-2026 | FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors | arXiv | academic | https://arxiv.org/abs/2609.32835 | 2026-09-26 |
| ICAEW-POD-2025 | Behind the Numbers: How should audit firms use AI? (transcript) | ICAEW | podcast | https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript | 2025-11-11 |
| ICAEW-FRCVIEW-2026 | How helpful is FRC's guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05 |
| ICAEW-REPLETTER-2026 | Letters of representation: a key protection for auditors | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/letters-of-representation-a-key-protection-for-auditors | 2026-05 |
| FRC-NEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 |
| CPAB-AC-2026 | Audit Committee Insights: Perspectives from Across Canada | CPAB | regulator | https://cpab-ccrc.ca/docs/default-source/event-highlights/2026-audit-committee-insights-part-1-en.pdf | 2026-07 |
| KN-FRC-2026 | Navigating Generative and Agentic AI: The FRC's Latest Expectations for Auditors | Kingsley Napley | press | https://www.kingsleynapley.co.uk/insights/blogs/regulatory-blog/navigating-generative-and-agentic-ai-the-frcs-latest-expectations-for-auditors | 2026-04-22 |
| DACB-2026 | AI: the future of audit | DAC Beachcroft | press | https://www.dacbeachcroft.com/en/what-we-think/ai-the-future-of-audit | 2026-07-13 |
| BOARDAGENDA-2026 | Auditors warned they remain accountable despite use of AI | Board Agenda | press | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | 2026-03-31 |
| RESULTSENSE-2026 | UK Regulator Tells Auditors They Cannot Blame AI for Mistakes | Resultsense | press | https://www.resultsense.com/news/2026-03-31-frc-auditors-cannot-blame-ai-for-mistakes/ | 2026-03-31 |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 |
| AT-PCAOBAI-2025 | PCAOB warns auditors about AI and PE | Accounting Today | press | https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe | 2025-12-09 |
| NYSSCPA-PCAOB-2025 | PCAOB Officials Flag Opportunities and Risks as AI and Private Equity Expand in Audit Firms | NYSSCPA | professional-body | https://nysscpa.org/news/1047818-pcaob-officials-flag-opportunities-and-risks-as-ai-and-private-equity-expand-in-audit-firms-2025-12-10 | 2025-12-10 |
| TR-PCAOBAGENDA-2026 | PCAOB unveils first standard-setting, rulemaking agendas under chairman Logothetis | Thomson Reuters Tax & Accounting | press | https://tax.thomsonreuters.com/news/pcaob-unveils-first-standard-setting-rulemaking-agendas-under-chairman-logothetis/ | 2026-10-01 (agendas dated 2026-09-30) |
| JOFA-PCAOBAGENDA-2026 | PCAOB shares agenda for rulemaking, research | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/pcaob-shares-agenda-for-rulemaking-research/ | 2026-10-01 |
| KPMG-HOHL-2026 | Q&A with Kurt Hohl, SEC chief accountant | KPMG Board Leadership Center | firm | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | 2026-05-27 |
| CAQ-ACINSIGHTS-2026 | Audit Committee Insights, March 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-committee-insights-march-2026 | 2026-03-17 |
| CAQ-WEBINAR-2026 | AI in Financial Reporting and Audit: What Audit Committees Need to Know (webinar page) | Center for Audit Quality | conference | https://www.thecaq.org/event-ai-in-financial-reporting-and-audit | 2026-03-26 |
| DELOITTE-CAQ-2026 | Enterprise Risk Management Takes the Lead, AI Governance Gains Urgency for Audit Committees (media alert) | Deloitte | survey | https://www.deloitte.com/us/en/about/press-room/deloitte-caq-announce-2026-audit-committee-practices-report.html | 2026-09-22 |
| AT-ACRISK-2026 | Audit committees focusing on emerging risks like AI | Accounting Today | press | https://www.accountingtoday.com/news/audit-committees-focusing-on-emerging-risks-like-ai | 2026-09-22 |
| BOARDMEMBER-CAQ-2026 | What Audit Partners Are Seeing On AI And What It Means For Audit Committees | Corporate Board Member | press | https://boardmember.com/?p=50023 | 2026-07-15 |
| AT-CAQPULSE-2026 | Audit partners concerned about AI risks | Accounting Today | press | https://www.accountingtoday.com/news/audit-partners-concerned-about-ai-risks | 2026-07-15 |
| TCC-PCAOBQ-2026 | Audit Committees: PCAOB-Related Questions to Ask Your Auditor | TheCorporateCounsel.net | press | https://www.thecorporatecounsel.net/blog/2026/07/audit-committees-pcaob-related-questions-to-ask-your-auditor.html | 2026-07-09 |
| TCC-ACAGENDA-2026 | Your 2026 Audit Committee Agenda: ICFR During AI Transformations | TheCorporateCounsel.net | press | https://www.thecorporatecounsel.net/blog/2026/02/your-2026-audit-committee-agenda-icfr-during-ai-transformations.html | 2026-02-06 |
| RSM-UAE-2026 | Is AI already in your audit? The standards are still catching up | RSM UAE | firm | https://www.rsm.global/uae/node/274 | 2026-08-24 |
| BIG4NEWS-2026 | The Big Four AI Arms Race, Evergrande, Governance and Culture | Big4News | press | https://www.big4news.com/p/big-four-news-20-may-2026 | 2026-05-20 |
| ACCWEEKLY-GC-2026 | Bulletproof Your AFS for Audit: The New Rules of Going Concern | Accounting Weekly | press | https://www.accountingweekly.com/audit-accounting/bulletproof-your-afs-for-audit-the-new-rules-of-going-concern | 2025-05-16 (updated 2026-10-08) |
| CPAPA-GENAI-2024 | How Auditors Are Currently Using Generative AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=108316 | 2024-07-23 |

**Counts of the 45 sources above by type:** conference 3, regulator 2, standard-setter 0, professional-body 6, firm 3, vendor 6, academic 3, survey 2, press 19, podcast 1, community 0, job-posting 0. Not cited: Fieldguide `ai-audit-preparation-reporting` (undated), which was opened and used only as background for the engagement quality review search.

---

## 6. Gaps

- **No public discourse found on AI in** going concern evaluation, subsequent events, written representations drafting, summary of misstatements, engagement quality review, key or critical audit matters, or opinion and audit report drafting. Each had at least one targeted search. This is stated as absence of evidence in the pages reachable, not proof that no firm does it.
- **No quality evidence.** No override or error rates, parallel-run results, inspection findings, or independent measurement for a completion-stage tool. All measured outcomes are vendor-published, and the Caseware 2.7-hour unit differs between its own documents.
- **Community voices are missing.** Reddit (r/auditing, r/Accounting) returned 403 through the proxy. Going Concern's search page opened but gave only headline links, and Hacker News search returned unrelated items. No LinkedIn, Slack or forum discussion was read.
- **Conference content is thin on completion.** The KU/Deloitte symposium agenda (May 2026) lists no completion-specific AI session. The CAQ March 2026 webinar page gave questions but not the speakers or a recording. The AICPA SEC and PCAOB conference (Dec 2025) was read only through press and society recaps. AICPA ENGAGE 2026, the AAA midyear meeting and the ICAEW audit conference agendas were not re-opened.
- **Primary documents not read.** The FRC guidance itself (read through the FRC release, ICAEW, Kingsley Napley and DAC Beachcroft), the AICPA practice aid text (login needed), the full Fabian and Ratzinger-Sakel paper (abstract only), the Gartner August 2026 audit-team survey (DataSnipper quotes it as 93% of audit leaders using AI; the Gartner page was blocked), the GPTZero report on the EY Canada retraction, and PCAOB project pages (403).
- **Source quality.** Seven vendor items, two vendor-run conference write-ups, several secondary press items and a low-authority firm blog (RSM UAE) carry much of the AI-use narrative. Two secondary reports (RESULTSENSE-2026, ACCWEEKLY-GC-2026) were not verified against primary documents.
- **Dates approximated:** DS-RISKS-2026 (no date on the page), DS-CONNECT-2026 and DS-AIREPORT-2026 (month inferred from page listing data), FIELDGUIDE-REVIEW-2026 (on-page label), CASEWARE-CWX-2026 (month inferred from the text "launched last month" and the 2026-05-20 launch).
- **Not followed up:** Ideagen Disclose (vendor claim of use by 9 of 10 top UK firms, carried in the landscape; the page I tried returned 404), Wolters Kluwer's sign-off article (403), Trullion and Thomson Reuters financial statement review integration (403), academic machine-learning going-concern prediction papers surfaced by search (not opened), the CPA Journal September 2026 article on evaluating AI in financial statement audits (opened; generic, ChatGPT-focused, nothing specific to completion).
