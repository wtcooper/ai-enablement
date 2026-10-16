# Module deep dive: assurance / planning-risk-assessment — angle: governance & evidence

- **Archetype:** assurance. External audit and other assurance services.
- **Module:** planning-risk-assessment. Understanding the entity and its environment (including its IT and AI use), risk assessment procedures and analytics for risk identification, fraud risk assessment and brainstorming, materiality, scoping (including group audits), audit strategy and planning, budgeting and staffing the engagement.
- **Angle:** governance & evidence. What constrains and measures AI use in this module: ISA 315 (Revised 2019) and AS 2110 as they touch AI, the IAASB exposure drafts (ED-520 on analytics), FRC worked examples and guidance, IFIAR and PCAOB inspection material on risk assessment, the AICPA practice aid on understanding the entity's AI use, academic studies and surveys.
- **Prepared:** 2026-10-16
- **Inputs:** `research/runs/wave1/landscape-assurance.md` (leads) and `research/briefs/templates/vocabulary.md` (controlled values). The pilot's `controls-testing-governance.md` was used only as a format and URL reference.
- **Method note.** Sources were fetched with `curl` through the session proxy; PDFs were read with `pdftotext`. About 58 distinct sources were opened. Primary documents were read for the relevant sections (the FRC guidance, IFIAR reports, ISA (UK) 315 and 240, PCAOB Release 2024-007 and AS 2110, the AFM report, the CPA.com report and the ICAEW test were read in the parts that bear on this module, not line by line). The web-search quota ran out partway through, so the later planned searches (PCAOB inspection observations on AS 2110, the CAQ Audit Partner Pulse) were not run.
- **Locators.** Page numbers are PDF page numbers unless marked "printed". For the UK standards and the PCAOB release they are the printed page numbers of the document. Paragraph references use the standard's own numbering. Source refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape file's keys where the same document appears there.
- **Grading convention used in this file.** The vocabulary reserves B for "a named real deployment". Where a regulator or inspector reports use at unnamed firms, the entry is graded C, not B, and the note says so. Maturity is then `piloting`, not `in-production`, because `in-production` requires a named organization. Measurements from an adjacent process cap the grade at B.

---

## 1. Summary

**What the rules say now (October 2026).** No standard or regulator reviewed prohibits AI in planning or risk assessment, and none sets AI-specific requirements for it. Existing standards apply and the human auditor stays accountable.

- **ISA 315 (Revised 2019).** The text read is the FRC's UK adoption (ISA (UK) 315, updated September 2025), whose numbering follows the IAASB text.
  - It lets the auditor use automated tools on large volumes of ledger and operational data for risk assessment (para 14, A21), and to analyse whole populations when identifying significant classes of transactions (A203).
  - It names AI once, in Appendix 5 para 5: when emerging technologies such as AI sit in the information system relevant to financial reporting, the auditor may include them when identifying IT applications subject to risks from IT, and the auditor's responsibilities "remain unchanged" (printed p.96).
  - Para 13 requires risk assessment procedures that are not biased toward corroborative evidence (printed p.7).
- **AS 2110.** The text contains no reference to AI, generative AI or machine learning (searched the full page text). The standard's relevant hooks are the understanding of the company and its IT use (.07, .28–.29, Appendix B), analytical procedures (.46–.48), the engagement team discussion and fraud brainstorming (.49–.53), inquiries (.54–.58) and revising the assessment as evidence arrives (.74).
  - PCAOB Release 2024-007 (technology-assisted analysis) amended AS 1105 so that a procedure's purpose decides whether it is a risk assessment procedure, test of controls or substantive procedure, and a multi-purpose procedure must achieve each objective (release p.25). It says evaluating the reliability of information used in risk assessment procedures takes less auditor effort than for substantive procedures and tests of controls (p.32). It states that it does not address AI (p.5).
- **IAASB exposure drafts (5 Aug 2026; comments due 15 Dec 2026).** ED-520 adds a requirement to consider how inconsistent results of risk-assessment analytical procedures affect the identification and assessment of risks (AUASB summary, Appendix 1 para 10(c)). ED-330 proposes removing the extant requirement to always perform substantive procedures for each material class, to reinforce the risk assessment under ISA 315 (para 2). The ED texts are login-gated, so what is reported here comes from the AUASB consultation paper's summary.
- **Fraud.** ISA (UK) 240 (Revised March 2026, effective for periods commencing on or after 15 December 2026) says automated tools may support the engagement team's fraud brainstorming, for example ratio benchmarking to identify fraud risk factors (A56, printed p.35), and flags AI or machine learning algorithms that initiate accounting entries as a source of heightened susceptibility (A101, printed p.47).
- **FRC (UK).** The *Generative and Agentic AI Guidance* (30 Mar 2026) includes a worked example for this module: summarising board minutes for risk assessment (pp.43–48). It names the misuse risk that matters most here: an auditor may not understand that an AI-enabled risk assessment tool's output was meant to inform their judgement and not to be the conclusion (p.18).
- **AICPA (13 Oct 2026).** The first practice aid for auditors on AI covers how an entity's own AI use affects the understanding of the entity, risk assessment, controls and acceptance. It says later sections on assessing the risk of material misstatement and on audit evidence when a company uses AI will be added.

**What inspections show.** There is no inspection finding specific to an AI risk-assessment tool in any source read.

- IFIAR's 2025 survey of inspection findings: the risk assessment theme had a finding in 44 of 770 inspected listed PIE audits (6%) and 53 findings in total, up from 39 audits (6%) and 49 findings in 2024 (pp.21–22). These are findings on risk assessment generally, not on tools.
- IFIAR members "frequently" observed automated tools in risk assessment in 55% of responses in 2024, against 88% for journal-entry testing. 31% of members reported findings that a tool was not used as intended, mostly misread results and thin follow-up of outliers (IFIAR-TTF-2025, p.5).
- The FRC's review of the six largest firms found no formal monitoring that quantified the audit quality impact of tools (FRC-ATT-2025).
- The FRC's 2026 annual review (reported by CPIA) names ineffective planning and over-reliance on prior-year approaches among the root causes it expects firms to remediate (CPIA-ARAQ-2026).

**What is measured.** Almost nothing about quality.

- Adoption figures exist: the AICPA/CPA.com benchmark found 22% of surveyed US firms (54 with complete data) had an automated solution for risk assessment (PDF p.10). The AFM found risk assessment accounted for 28% of average tool use across audit areas at six Dutch PIE firms (p.27).
- The nearest quality evidence is a single ICAEW test in which three general-purpose chatbots did not perform ISA 315 risk assessment as a human would, and one academic prototype that predicts restatements (AUROC 0.782).
- Named deployments (PwC, KPMG, Deloitte, MindBridge, Caseware) come with no outcome figures beyond a PwC statement that savings are "not that drastic yet".

**Use cases.** 17 entries: grade A 0, B 2, C 8, D 7. Source types are in section 5 (58 sources across 9 types).

**Two most important insights.**

1. **Risk assessment is where the standards are most permissive and where the tool most easily becomes the conclusion.** The evidentiary bar for information used in risk assessment is lower than for responses (PCAOB 2024-007 p.32). The risk assessment standards, however, require inquiries, observation and inspection and an unbiased approach (ISA 315 paras 13–14; AS 2110 .54), and the FRC, NFRA and IFIAR all warn against treating a tool's output as the judgement. India's NFRA says auditors should not accept a tool's low-risk classification without periodically testing it (NFRA-CAALLEY-2026, a press report of the staff paper). No one yet measures whether tool-assisted risk assessment is better: the FRC found no formal quality monitoring and the ICAEW test is a single run.
2. **Client AI use has become a planning topic in its own right.** ISA 315 Appendix 5, ISA (UK) 240 A101, IFIAR's 2026 report (p.10), ACRA's 2025 guidance and the AICPA practice aid all ask the auditor to understand how the entity uses AI, including deliberate misuse to fabricate documents and transactions. The AICPA says its guidance on assessing risks of material misstatement for AI-using companies is still to come, so the procedures are guidance only, with no deployment evidence.

---

## 2. Use cases

```yaml
- id: assurance-planning-risk-assessment-01
  title: GenAI summary of board minutes and other entity documents to focus the understanding-of-the-entity review
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ research-synthesis, review-assurance ]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Auditors read board minutes and similar documents to understand the entity and spot risk indicators. The volume is large and the relevant passages are easy to miss."
  solution: "An LLM-based tool segments and indexes the minutes with stable identifiers, summarises each meeting, looks across the whole period for themes, then synthesises a summary in which each point cites its source. The auditor uses it to focus the review, and records on the file that the tool was used and how its output informed further work. The FRC's worked example is a hypothetical firm. Regulators report that real firms use chatbots for summarising meeting minutes without naming the firms."
  outcomes:
    - { lever: quality, description: "none published. The FRC example ties the tolerance for output deficiencies at certification to how much human review the methodology requires", figure: "none published", measures: "not applicable", provenance: independent, source_ref: FRC-GENAI-2026 }
  prerequisites:
    - "Minutes segmented and indexed with stable identifiers so the tool can cite sources (FRC-GENAI-2026 p.44)"
    - "Pre-written prompts held in a library and tested at certification, including across entities of different sizes and sectors (p.45)"
    - "Training that focuses on reviewing the output, because the auditor does not prompt the tool (p.46)"
    - "Tool documentation retained centrally, with the auditor recording use and effect on the file (p.43)"
  risks_and_guardrails:
    - "Omission, distortion and hallucination of information are the output risks the example addresses through workflow design, prompts, certification and review (FRC-GENAI-2026 p.44)"
    - "Misuse: auditors may read the summary as a complete account of the period and skip other risk assessment procedures. The firm's mitigation is training on the output's scope (FRC-GENAI-2026 p.48)"
    - "The FRC rates the non-compliant-methodology risk as relatively low because the tool enhances an existing procedure and the rest of the risk assessment methodology is unchanged (FRC-GENAI-2026 p.48)"
    - "The tool sounds fluent and confident even when it is wrong, and staff are trained on automation bias (FRC-GENAI-2026 p.46)"
  human_checkpoints:
    - "The auditor reads the minutes to corroborate the completeness and accuracy of the output (FRC-GENAI-2026 p.46)"
    - "A more detailed read of the cited sections where the output conflicts with the auditor's prior understanding or affects the risk assessment (FRC-GENAI-2026 p.46)"
    - "The FRC example suggests the review is done by a team member with an appropriate understanding of the entity (FRC-GENAI-2026 p.46)"
  role_evolution: "Team members become reviewers of a cited summary rather than first-pass readers of every minute. The FRC example moves the training emphasis to reviewing outputs and recognising automation bias (FRC-GENAI-2026 p.46)."
  evidence_grade: C
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "Illustrative example 1, pp.43-48" }
    - { ref: AFM-12BB-2025, title: "12 building blocks for controlled use of auditing tools", publisher: Autoriteit Financiele Markten, type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "p.31, use of (Gen)AI" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff update on outreach activities related to the integration of generative AI in audits and financial reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p.4, potential areas" }
    - { ref: BOARDAGENDA-FRC-2026, title: "Auditors warned they remain accountable despite use of AI", publisher: Board Agenda, type: press, url: "https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/", date: 2026-03-31, access: full, locator: "paragraph listing current AI uses, including summarising minutes" }
  last_reviewed: 2026-10-16
  notes: "Graded C by this file's convention: the FRC example is hypothetical, and the AFM (11 non-PIE and 2 PIE firms visited, plus a data request to six PIE firms) says nearly all firms use GenAI, for example chatbots to summarise meeting minutes, without naming firms. Board Agenda reports the FRC listing summarising minutes among current uses; that is a journalist's summary of the FRC statement. No named deployment or measurement found. PCAOB staff (July 2024) listed summarising accounting policy and legal documents among potential areas, with current use focused on administrative and research activities."

- id: assurance-planning-risk-assessment-02
  title: Engagement-aware agent that checks the planning file for gaps, for example a board-minutes variance with no risk attached
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Gaps in the risk assessment, such as a variance that no logged risk covers, are often found during fieldwork rather than at planning review."
  solution: "In a scenario Caseware's chief product officer demonstrated at CwX 2026, a reviewer opens a file for planning review and asks the Caseware Verity agent whether the team missed anything. The agent pulls the trial balance, checks materiality, reviews the risks already logged and surfaces a variance against the board minutes with no risk attached. Caseware states that suggestions are citation-backed and that nothing is written into the engagement without a human accepting, editing or rejecting it."
  outcomes:
    - { lever: quality, description: "none published for this scenario. Caseware reports 2.7 hours saved per run for a different agent (the Disclosure Checklist Agent), which belongs to completion-reporting", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: CASEWARE-VERITY-2026 }
  prerequisites:
    - "Trial balance, materiality, risk log and board minutes held in the platform the agent is embedded in (CASEWARE-VERITY-2026, scenario description)"
  risks_and_guardrails:
    - "Misinterpretation: a 'nothing missed' answer can be read as a complete risk assessment. The FRC lists misinterpretation of output and misunderstanding of methodology as distinct risks (FRC-GENAI-2026 p.18)"
    - "The tool's output informs the auditor's judgement and is not itself a conclusion (FRC-GENAI-2026 p.18)"
  human_checkpoints:
    - "Reviewer accepts, edits or rejects each suggestion before anything enters the engagement (CASEWARE-VERITY-2026, FAQ)"
  role_evolution: "Caseware says juniors can reach standards and methodology in context and seniors can spend more time on higher-value review (vendor statement)."
  evidence_grade: C
  sources:
    - { ref: CASEWARE-VERITY-2026, title: "From AiDA to agentic: How Caseware's AI has evolved", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved", date: 2026-07-28, access: full, locator: "section 'Meet Caseware Verity', CwX scenario" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp.18-19" }
  last_reviewed: 2026-10-16
  notes: "A vendor demonstration, not a customer deployment. No customer is named. Caseware says its longer-term aim is for AI to assist continuously with planning, risk identification, evidence collection and review (vendor blog, section 'What's next')."

- id: assurance-planning-risk-assessment-03
  title: Planning document pre-populated from prior-year audit information (PwC Simplified Audit for Private Business)
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ document-production ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Planning documentation is rebuilt every year and teams roll prior-year files forward. The FRC's 2026 annual review is reported to name over-reliance on prior-year approaches among the causes needing remediation."
  solution: "PwC says its planning tool for private-company audits ingests prior-year information and auto-populates a planning document that serves as a foundation for considering compliance with AICPA standards. PwC says it saves time and helps auditors ask better questions because they better understand what changed in the business since the last audit. 2025 was the first year PwC auditors used it in planning."
  outcomes:
    - { lever: speed, description: "PwC says the tool saves time. No figure is given", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: PWC-AT-2025 }
    - { lever: speed, description: "A PwC leader said in Oct 2026 that AI-related time savings across the firm's audit tools so far are 'more of a shift' and 'not that drastic yet'. This covers PwC's tools generally, not this tool", figure: "none published", measures: "qualitative statement; no numerator or denominator", provenance: self-reported, source_ref: CFODIVE-PWC-2026 }
  prerequisites:
    - "Prior-year audit information in a form the tool can ingest (PWC-AT-2025)"
  risks_and_guardrails:
    - "Roll-forward risk: in the CPA.com survey (74 firms registered, 54 with complete data), 85% say they prioritise rolling binders forward to save time and 60% carrying forward the prior-year risk assessment; 64% prioritise challenging last year's procedures in relation to risk assessment (CPACOM-ATR-2025 PDF p.14)"
    - "AS 2110 .08 requires the auditor to evaluate whether significant changes since prior periods affect the risks of material misstatement"
    - "ISA (UK) 315 para 13 requires risk assessment procedures not biased toward corroborative evidence (printed p.7)"
  human_checkpoints:
    - "The source does not describe review steps. PwC says the document is a foundation and that auditors ask better questions about changes"
  role_evolution: "In the same briefing PwC said it is hiring engineers into assurance and wants more dual-track CPA and data-science profiles (PWC-AT-2025). That statement concerns PwC's wider AI programme, not this tool."
  evidence_grade: B
  sources:
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraphs 3-4" }
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "section on where AI has an impact" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: CPA.com / AICPA, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "PDF p.14 (report p.13)" }
    - { ref: CPIA-ARAQ-2026, title: "Audit quality remains strong in 2026 - consistency is now the aim", publisher: CPIA, type: press, url: "https://www.cpia.org.uk/news/frc-audit-quality-2026/", date: 2026-07-24, access: full, locator: "section 'Turning systems into better audits'" }
    - { ref: ISAUK315-2025, title: "ISA (UK) 315 (Revised July 2020): Identifying and Assessing the Risks of Material Misstatement, updated September 2025", publisher: Financial Reporting Council, type: standard-setter, url: "https://media.frc.org.uk/documents/ISA_UK_315_Revised_July_2020_Updated_September_2025.pdf", date: 2025-09, access: full, locator: "para 13, printed p.7" }
  last_reviewed: 2026-10-16
  notes: "B because PwC is a named firm that describes the tool as in use. The Accounting Today article is a briefing report and PwC's statement is self-reported. The tool is designed for private-company audits under AICPA standards, not public-company audits. The CPA.com figures describe surveyed US firms' stated priorities (54 firms with complete data), not this tool."

- id: assurance-planning-risk-assessment-04
  title: Tool that analyses audit committee communications to surface issues earlier in audit preparation
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ research-synthesis ]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Issues raised by the audit committee reach the engagement team late, after the audit has been scoped."
  solution: "In Oct 2026 PwC said that for 2026 year-end audits one of its tools analyses audit committee communications to surface issues that need to be handled sooner in the audit preparation cycle."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: CFODIVE-PWC-2026 }
  prerequisites:
    - "Access to the audit committee communications the tool analyses. The source does not describe the inputs"
  risks_and_guardrails:
    - "AS 2110 .54 still requires the auditor to inquire of the audit committee, management, internal audit and others. ISA (UK) 315 para 14(a) requires inquiries of management and others. A document-analysis tool does not satisfy these inquiries"
    - "The source gives no guardrails for this tool"
  human_checkpoints:
    - "Not described in the source"
  role_evolution: "Not described in the source."
  evidence_grade: C
  sources:
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "paragraph beginning 'For 2026 year-end audits'" }
    - { ref: AS2110-PCAOB-2026, title: "AS 2110: Identifying and Assessing Risks of Material Misstatement", publisher: PCAOB, type: standard-setter, url: "https://pcaobus.org/oversight/standards/auditing-standards/details/AS2110", date: 2026-10-16, access: full, locator: "para .54" }
  last_reviewed: 2026-10-16
  notes: "The article says PwC 'will be using' AI in a number of areas for 2026 year-end audits and then describes the tool in the present tense, so the maturity is announced. The AS2110-PCAOB-2026 date is the access date because the page carries no publication date."

- id: assurance-planning-risk-assessment-05
  title: Whole-population analytics to identify significant classes of transactions, accounts and unusual flows when scoping
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ data-reporting, expert-judgment ]
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Significant classes, accounts and disclosures are often identified from summarised balances and prior-year scoping, so offsetting entries and unexpected flows stay hidden."
  solution: "ISA 315 application material describes analysing an entire population of transactions with automated tools to understand nature, source, size and volume. Examples are spotting a zero-balance account built from offsetting entries (a payroll clearing account that also carries expense reimbursements to management) and analysing whole revenue flows to find a significant class not previously identified (A203). IFIAR reports that regulators frequently see such tools in risk assessment at the six global networks."
  outcomes:
    - { lever: risk, description: "Share of IFIAR members that 'frequently' observed automated tools and techniques in risk assessment in the audit files of the six global networks", figure: "55% in 2024; 49% in 2023", measures: "Of 47 members responding in 2024 (45 in 2023), the share answering 'frequently observed' for the area 'risk assessment'. In 2024, 13% answered 'never' and 32% 'infrequently'. Covers all automated tools and techniques, not only AI. Directional, from members' inspection experience", provenance: independent, source_ref: IFIAR-TTF-2025 }
    - { lever: risk, description: "Average share of tool use by audit area across the six Dutch PIE firms: risk assessment, against tests of details", figure: "28% risk assessment; 51% tests of details", measures: "AFM chart 'use of audit tooling in each audit area (average)' from its data request to six PIE audit firms. Percentages do not total 100% because one tool can serve several areas. The source does not define the numerator more precisely", provenance: independent, source_ref: AFM-12BB-2025 }
    - { lever: risk, description: "US firms with an automated solution for risk assessment", figure: "22%", measures: "Share of surveyed firms that said they have an automated solution for risk assessment (74 firms registered; 54 with complete data were used for the statistical analysis; the report does not state the base for this chart). Survey run Jun-Aug 2025 by CPA.com and the AICPA; firms self-report", provenance: independent, source_ref: CPACOM-ATR-2025 }
  prerequisites:
    - "Access to complete ledger and sub-ledger data from the client's systems. The AICPA/CPA.com survey ranks poor quality client data (60%) and lack of access to client information and systems (53%) among the top perceived blockers to audit transformation (CPACOM-ATR-2025 PDF p.8, report p.7)"
    - "Evaluation of the relevance and reliability of the data used. AFM makes input data the second of its four layers of building blocks (AFM-12BB-2025 p.1)"
  risks_and_guardrails:
    - "31% of IFIAR members reported findings that a tool was not used as intended in 2024 (29% in 2023). Common findings were misinterpreted results and the extent of outlier testing (IFIAR-TTF-2025 p.5)"
    - "AFM bad practice: using a tool without evaluating the reliability of input data when the client's general IT controls are ineffective (AFM-12BB-2025 pp.16-17)"
    - "NFRA staff paper (as reported): do not accept a tool's low-risk classification without periodically testing it, and full-population testing does not remove the need for risk assessment (NFRA-CAALLEY-2026)"
    - "PCAOB: evaluating the reliability of information used in risk assessment takes less effort than for substantive procedures (PCAOB-TAA-2024 p.32). AS 1105.14 as amended requires a multi-purpose procedure to achieve each objective (PCAOB-TAA-2024 p.25)"
  human_checkpoints:
    - "Auditor interprets results and follows up outliers. Misreading results and thin outlier testing are IFIAR's most frequent technology findings (IFIAR-TTF-2025 p.5)"
    - "Senior team members reflect on the overall use of technology in the file and whether scepticism was maintained (IFIAR-TTF-2026 p.7)"
  role_evolution: "IFIAR expects training mapped to required competencies, covering how to evaluate outputs, understand limits and exercise judgement (IFIAR-TTF-2026 p.7)."
  evidence_grade: B
  sources:
    - { ref: ISAUK315-2025, title: "ISA (UK) 315 (Revised July 2020): Identifying and Assessing the Risks of Material Misstatement, updated September 2025", publisher: Financial Reporting Council, type: standard-setter, url: "https://media.frc.org.uk/documents/ISA_UK_315_Revised_July_2020_Updated_September_2025.pdf", date: 2025-09, access: full, locator: "A21 printed p.18; A31 p.20; A203 p.63" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution (2025)", publisher: IFIAR Technology Task Force, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "p.5, table of areas where ATTs are used; findings" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: innovation and audit quality 2026", publisher: IFIAR Technology Task Force, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "pp.7, 9, 12 (Appendix A, predictive data analytics)" }
    - { ref: AFM-12BB-2025, title: "12 building blocks for controlled use of auditing tools", publisher: Autoriteit Financiele Markten, type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "pp.16-17, 27" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: CPA.com / AICPA, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "PDF p.8 (blockers); p.10 (automated solutions); p.28 (method); report page = PDF page minus 1" }
    - { ref: PCAOB-TAA-2024, title: "Release No. 2024-007: Amendments related to aspects of designing and performing audit procedures that involve technology-assisted analysis", publisher: PCAOB, type: regulator, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/rulemaking/docket-052/2024-007-adoptingrelease.pdf", date: 2024-06-12, access: full, locator: "printed pp.25, 32" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: CAalley (reporting an NFRA staff paper), type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Professional scepticism cannot be delegated to technology'" }
  last_reviewed: 2026-10-16
  notes: "B, capped: the IFIAR and AFM figures measure how often tools are seen or used, not their effect on quality, and cover all automated tools and techniques, not only AI. The IFIAR 'six global networks' (GPPC) are not named in the pages read. The IFIAR 2026 report gives the 2025 frequencies only as an unlabelled chart and says frequent observations were largely unchanged or slightly higher. The NFRA material is a press report; the staff paper itself was not located."

- id: assurance-planning-risk-assessment-06
  title: Multi-agent entity-level risk scoring from MD&A text, financial ratios and critical audit matters (research idea)
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ data-reporting, expert-judgment ]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Entity-level risk signals come from several evidence streams (text, ratios, prior critical audit matters) that can disagree, and point predictions say nothing about how well the streams agree."
  solution: "An idea (labelled idea): three agents (an MD&A text agent, a financial ratio agent and a critical-audit-matter agent) each produce a risk score with calibrated uncertainty, and an aggregator based on Dempster-Shafer evidence theory fuses them while measuring conflict between agents. The pattern is a risk-signal producer, not an audit workflow."
  outcomes:
    - { lever: risk, description: "Restatement-prediction performance of the prototype on 10-K data", figure: "AUROC 0.782; PR-AUC 0.341; expected calibration error 0.052", measures: "3,200 US firm-year observations from SEC 10-K filings 2019-2023, with financial restatement as the label; compared with logistic regression, XGBoost, FinBERT and single- and dual-agent LLM baselines. Authors describe the output as offering 'potentially actionable' risk signals", provenance: independent, source_ref: ARXIV-UMAR-2026 }
  prerequisites:
    - "Public 10-K text and ratios, so as described it applies to listed US companies"
  risks_and_guardrails:
    - "The label is restatement, so the score predicts restatement, not the wider set of risks of material misstatement (reading of the abstract, not a source statement)"
    - "FRC: output used as a conclusion rather than as an input to judgement is a misuse risk (FRC-GENAI-2026 p.18)"
    - "NFRA staff paper (as reported): classification by a tool needs periodic testing (NFRA-CAALLEY-2026)"
  human_checkpoints:
    - "Not described in the abstract"
  role_evolution: "Not addressed."
  evidence_grade: D
  sources:
    - { ref: ARXIV-UMAR-2026, title: "Multi-Agent Framework for Audit Risk Assessment with Explicit Uncertainty and Evidence Conflict Modeling", publisher: arXiv (Wang et al.), type: academic, url: "https://arxiv.org/abs/2606.15640", date: 2026-06-14, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Idea. Researchers discuss it, and no firm deployment was found. Abstract page only; the full paper was not read. The grade is D because there is no deployment, even though the paper reports a measured result on public data."

- id: assurance-planning-risk-assessment-07
  title: Predictive and benchmark analytics to build expectations for risk-assessment analytical procedures and to surface fraud risk factors
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ data-reporting, expert-judgment ]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Analytical procedures at the risk assessment stage use aggregated or preliminary data and a limited set of expectations, so unusual relationships can be missed."
  solution: "An idea (labelled idea) drawn from the standards and regulators: automated tools build expectations and benchmark ratios to identify unusual relationships, supporting both the risk-assessment analytical procedures and the identification of fraud risk factors in the engagement team discussion. ISA (UK) 240 gives ratio benchmarking against the sector as an example. IFIAR lists predictive data analytics as usable in risk assessment and planning to inform where further procedures are needed."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: ISAUK240-2026 }
  prerequisites:
    - "Reliable data and a documented expectation (AS 2110 .48 requires expectations built from the auditor's understanding of the company)"
  risks_and_guardrails:
    - "AS 2110 .48 note: risk assessment analytics often use preliminary or highly aggregated data, so they are not designed with the precision needed for substantive analytical procedures"
    - "ED-520 would add a requirement to consider how inconsistent results of risk-assessment analytical procedures affect the identification and assessment of risks (AUASB-CPED-2026, Appendix 1 para 10(c); ED-520 para 7, A6-A7)"
    - "ISA (UK) 240 A9: automated tools do not replace the need to maintain scepticism and exercise judgement (printed p.22)"
    - "Japan FSA discussion paper: a GenAI tool might judge a transaction low risk when it is a significant fraud indicator (FSA-DP-2025 p.13)"
  human_checkpoints:
    - "Auditor evaluates unusual results and takes them into account in identifying risks (AS 2110 .48)"
  role_evolution: "Not addressed in the sources."
  evidence_grade: D
  sources:
    - { ref: ISAUK240-2026, title: "ISA (UK) 240 (Revised March 2026): The Auditor's Responsibilities Relating to Fraud in an Audit of Financial Statements", publisher: Financial Reporting Council, type: standard-setter, url: "https://www.frc.org.uk/documents/9305/ISA_UK_240_Revised_March_2026_xuvAkap9.pdf", date: 2026-04-30, access: full, locator: "A9 printed p.22; A56 p.35" }
    - { ref: AS2110-PCAOB-2026, title: "AS 2110: Identifying and Assessing Risks of Material Misstatement", publisher: PCAOB, type: standard-setter, url: "https://pcaobus.org/oversight/standards/auditing-standards/details/AS2110", date: 2026-10-16, access: full, locator: "paras .46-.48 and note" }
    - { ref: AUASB-CPED-2026, title: "Consultation Paper: IAASB Proposed International Standards on Audit Evidence & Risk Response", publisher: AUASB, type: standard-setter, url: "https://www.auasb.gov.au/media/fegpk4s5/auasb_cp_iaasbproposedintlstdonauditevidence__riskresponse1.pdf", date: 2026-08, access: full, locator: "Appendix 1, para 10(c)" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: innovation and audit quality 2026", publisher: IFIAR Technology Task Force, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p.12, Appendix A" }
    - { ref: FSA-DP-2025, title: "Study on the potential utilization of generative AI in audit practices and challenges related to audit quality (DP2025-3)", publisher: Financial Services Agency, Japan (Financial Research Center), type: regulator, url: "https://www.fsa.go.jp/frtc/english/seika/discussion/2025/DP2025-3_Eng.pdf", date: 2025-07, access: full, locator: "pp.8, 13" }
  last_reviewed: 2026-10-16
  notes: "Idea. The FSA discussion paper cites an FSA 2025 report saying traditional AI is used for anomaly detection in transaction and journal data and for identifying and assessing fraud risks; this is a secondary citation of a report not opened, so it does not lift the grade. The ED-520 text is login-gated, so whether its application material describes tool-built expectations could not be verified (the landscape file says it does)."

- id: assurance-planning-risk-assessment-08
  title: Agent that links evidence, analytics, assertions, materiality and methodology to support risk identification and scoping decisions
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ expert-judgment, data-reporting ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Risk identification and scoping depend on connecting analytics, evidence, assertions and materiality by hand, and the documentation of why a risk was or was not scoped in is thin."
  solution: "Vendors and firms have announced agent-style risk assessment. MindBridge (22 Sep 2026) announced an Agentic Risk Assessment capability that connects evidence, analytics, assertions, materiality and methodology to support audit planning decisions and integrates with customer-built and third-party workpaper tools. Deloitte (24 Jun 2026) said agents in Omnia can analyse information to identify potential risk factors. KPMG said in Apr 2025 that GenAI integrated into KPMG Clara in Jul 2024 helps teams refine risk assessments. PwC said in Oct 2025 it planned 'soon' to have a risk assessment tool to help decide what is scoped in."
  outcomes:
    - { lever: quality, description: "none published by any of the four", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: MINDBRIDGE-ARA-2026 }
  prerequisites:
    - "Integration with the firm's methodology and workpaper platform (MINDBRIDGE-ARA-2026: designed to integrate with customer-built and third-party workpaper solutions)"
    - "Certification and monitoring of the tool under the firm's system of quality management (IFIAR-TTF-2026 p.6)"
  risks_and_guardrails:
    - "ICAEW test: none of three general-purpose chatbots performed risk assessment procedures as a human auditor would, and none separated financial-statement-level from assertion-level risks (ICAEW-PIERPOINT-2025). The test concerned chatbots, not these tools"
    - "FRC: the auditor may not understand that the tool's output was meant to inform judgement and not be a conclusion (FRC-GENAI-2026 p.18)"
    - "NFRA staff paper (as reported): do not accept a tool's low-risk classification without periodically testing it (NFRA-CAALLEY-2026)"
    - "Japan FSA discussion paper: a GenAI tool might label a transaction low risk when it indicates significant fraud, leading to errors in planning (FSA-DP-2025 p.13)"
    - "ISA (UK) 315 para 13: risk assessment procedures must not be biased toward corroborative evidence (printed p.7)"
  human_checkpoints:
    - "MindBridge says the capability preserves auditor judgement and control (vendor statement)"
    - "Deloitte says preliminary conclusions are developed for professionals to review (DELOITTE-OMNIA-2026)"
  role_evolution: "Deloitte adds a tutor mode for on-demand micro-training in the context of the work (DELOITTE-OMNIA-2026). PwC says it is hiring engineers into assurance (PWC-AT-2025)."
  evidence_grade: C
  sources:
    - { ref: MINDBRIDGE-ARA-2026, title: "MindBridge advances financial oversight for the agentic era with new platform capabilities", publisher: MindBridge (Business Wire release), type: vendor, url: "https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/", date: 2026-09-22, access: full, locator: "bullet 'Agentic Risk Assessment for audit & assurance'" }
    - { ref: DELOITTE-OMNIA-2026, title: "Deloitte unveils connected agentic intelligence in Deloitte Omnia to advance audit & assurance", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24, access: full, locator: "list of what the agents can do" }
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: 2025-04-22, access: full, locator: "section 'Today's announcement builds on', July 2024 item" }
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "paragraph 4" }
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "section 'Analytical review and risk of material misstatement'" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p.18" }
    - { ref: FSA-DP-2025, title: "Study on the potential utilization of generative AI in audit practices and challenges related to audit quality (DP2025-3)", publisher: Financial Services Agency, Japan (Financial Research Center), type: regulator, url: "https://www.fsa.go.jp/frtc/english/seika/discussion/2025/DP2025-3_Eng.pdf", date: 2025-07, access: full, locator: "p.13" }
  last_reviewed: 2026-10-16
  notes: "All four are announcements. The MindBridge release does not say whether the capability is generally available. The Oct 2026 CFO Dive article on PwC names a planning tool, an evidence-reading tool, an audit-committee tool and a walkthrough assistant but no risk assessment tool, so PwC's Oct 2025 'soon' is not confirmed delivered. KPMG's release recaps the Jul 2024 GenAI integration for 90,000 auditors and does not describe use or results. No customer is named by MindBridge."

- id: assurance-planning-risk-assessment-09
  title: General-purpose chatbot drafts risk identification and assessment from the financial statements (tested, with weak results)
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ expert-judgment, research-synthesis ]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Identifying risks of material misstatement at the financial-statement and assertion levels takes time, and a chatbot can produce a polished draft in seconds."
  solution: "An idea (labelled idea), tested by ICAEW: give a general-purpose chatbot a set of financial statements and ask for analytical review, red flags, risk identification and assessment. ICAEW's technical manager ran the test with Copilot, Claude Sonnet 4 and Grok 3 on an AI-generated fictional retailer and concluded that the case for using chatbots to identify risks of material misstatement had not been made."
  outcomes:
    - { lever: quality, description: "ICAEW single test of three chatbots against ISA 315-style risk assessment", figure: "0 of 3 models separated financial-statement-level from assertion-level risks; 0 of 3 supplemented understanding through inquiry, observation and inspection; 1 of 3 (Copilot) did not treat revenue as a risk area despite the ISA 240 presumption; 3 of 3 did not round all year-on-year percentage changes correctly or consistently", measures: "Counts of the three models tested (Copilot, Claude Sonnet 4, Grok 3), one run each on one fictional company; the tester notes that prompt wording changes results and that a newer Grok version appeared after the test", provenance: independent, source_ref: ICAEW-PIERPOINT-2025 }
  prerequisites:
    - "None identified. The test used no client-specific knowledge"
  risks_and_guardrails:
    - "ISA (UK) 315 para 14 requires inquiries, analytical procedures and observation and inspection, and para 13 requires an unbiased approach (printed p.7). The test found the chatbots could not supplement their understanding through inquiry, observation or inspection"
    - "The tester notes that ISA 240 presumes revenue recognition is a fraud risk, and one model did not treat revenue as a risk area at all (ICAEW-PIERPOINT-2025)"
  human_checkpoints:
    - "ICAEW concludes human judgement is needed to interpret the output and decide the risks, because each model gave different answers (ICAEW-PIERPOINT-2025)"
  role_evolution: "Not addressed."
  evidence_grade: D
  sources:
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "sections 'Analytical review and risk of material misstatement' and 'Materiality'" }
    - { ref: ISAUK315-2025, title: "ISA (UK) 315 (Revised July 2020): Identifying and Assessing the Risks of Material Misstatement, updated September 2025", publisher: Financial Reporting Council, type: standard-setter, url: "https://media.frc.org.uk/documents/ISA_UK_315_Revised_July_2020_Updated_September_2025.pdf", date: 2025-09, access: full, locator: "paras 13-14, printed p.7" }
  last_reviewed: 2026-10-16
  notes: "Idea; a practitioner-body test, not a benchmark. Models were from mid-2025 and are not current. ICAEW also says simple chatbots are already used by auditors to enhance their understanding of entities through research (see use case 17), so the finding applies to the risk-identification step only."

- id: assurance-planning-risk-assessment-10
  title: GenAI proposes the materiality benchmark, percentage and performance materiality with a written rationale
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ expert-judgment, data-reporting ]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Setting overall and performance materiality needs a benchmark, a percentage and a rationale, and inspectors scrutinise year-on-year changes because fee pressure can push materiality up."
  solution: "An idea (labelled idea), tested by ICAEW in the same single test as use case 9: the chatbots were asked to propose materiality with their rationale. PCAOB staff said its 2025 inspections would evaluate significant year-over-year materiality changes and the scoping of multi-location audits, because fee pressure may lead auditors to look for ways to cut hours, for example by setting a higher materiality."
  outcomes:
    - { lever: quality, description: "ICAEW observed wide variation between models in overall materiality, and one model's rationale looked like a possible hallucination", figure: "none published as a measure. Claude proposed 5% of profit before tax (the lowest figure); Copilot proposed 0.75% of revenue with a vague rationale", measures: "Single run per model on one fictional retailer; the source's text on which model proposed which performance-materiality percentage is internally inconsistent (60% and 75% are both attributed to Claude), so those are not reported", provenance: independent, source_ref: ICAEW-PIERPOINT-2025 }
  prerequisites:
    - "A documented basis for benchmark and percentage. ISA 320 factors were cited by the tester for the Claude output"
  risks_and_guardrails:
    - "Variation by model means the answer depends on the tool chosen (ICAEW-PIERPOINT-2025)"
    - "A tool could make a higher materiality look supported. PCAOB staff flagged materiality changes and scoping as a fee-pressure inspection focus (PCAOB-PRIORITIES-2024 p.5)"
    - "The tester found one model assumed a long-standing auditor relationship meant lower risk and missed a new finance director and high staff turnover as control-weakness indicators (ICAEW-PIERPOINT-2025)"
  human_checkpoints:
    - "ICAEW concludes human judgement is required to decide the thresholds (ICAEW-PIERPOINT-2025)"
  role_evolution: "Not addressed."
  evidence_grade: D
  sources:
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "section 'Materiality'" }
    - { ref: PCAOB-PRIORITIES-2024, title: "Spotlight: Staff priorities for 2025 inspections and interactions with audit committees", publisher: PCAOB staff, type: regulator, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf", date: 2024-12, access: full, locator: "p.5, 'Audit execution challenges'" }
  last_reviewed: 2026-10-16
  notes: "Idea. No deployment of AI-set materiality was found in any source. The PCAOB staff statement is about fee pressure generally and does not mention AI-set materiality."

- id: assurance-planning-risk-assessment-11
  title: GenAI as a sounding board in fraud risk assessment and the engagement team discussion
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ expert-judgment, research-synthesis ]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Fraud risk assessment is vulnerable to cognitive bias, such as irrelevant information diluting the weight of relevant indicators, and brainstorming can miss scenarios."
  solution: "The AFM reports auditors using a GenAI tool as a sounding board in fraud risk assessment for a sector or typology: they first make their own assessment and then use the tool to challenge it and remove blind spots. ISA (UK) 240 says automated tools may support the engagement team discussion about susceptibility to fraud, for example by identifying fraud risk factors through ratio benchmarking."
  outcomes:
    - { lever: quality, description: "Conference experiment on auditors' fraud risk ratings with and without ChatGPT (mean rating on a 1-10 scale)", figure: "Without ChatGPT: 8.00 (relevant information only) against 6.42 (relevant plus irrelevant), p=0.007. With ChatGPT: 8.91 against 7.97", measures: "Mean fraud risk rating on a 10-point Likert scale (1 very low, 10 very high) from a single client vignette, 66 auditors enrolled in an Indonesian professional-institute programme, 2x2 design. Cell sizes (35 and 31) are the same in both ChatGPT conditions, which does not match the described between-subjects design, so treat as weak evidence", provenance: independent, source_ref: INDO-ICOBUSS-2025 }
  prerequisites:
    - "Auditors form their own assessment before consulting the tool (AFM-12BB-2025 p.31)"
    - "A policy on what client information may be entered into a GenAI tool (PCAOB-GENAI-2024 p.4 reports data privacy and security as areas of firm focus)"
  risks_and_guardrails:
    - "AS 2110 .49-.53 require the key engagement team members, including the engagement partner, to discuss susceptibility to fraud, setting aside any belief that management is honest. A tool does not replace that discussion"
    - "ISA (UK) 240 A9: automated tools do not replace scepticism and judgement (printed p.22)"
    - "Peters (working paper): auditors relying on work done by automated tools were less sceptical than when relying on the same work by a team member; a counterarguing mindset intervention reduced the effect (PETERS-2022)"
  human_checkpoints:
    - "Auditor makes the first assessment and uses the tool to test it (AFM-12BB-2025 p.31)"
  role_evolution: "Not addressed."
  evidence_grade: C
  sources:
    - { ref: AFM-12BB-2025, title: "12 building blocks for controlled use of auditing tools", publisher: Autoriteit Financiele Markten, type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "p.31, 'Good practice' box" }
    - { ref: ISAUK240-2026, title: "ISA (UK) 240 (Revised March 2026): The Auditor's Responsibilities Relating to Fraud in an Audit of Financial Statements", publisher: Financial Reporting Council, type: standard-setter, url: "https://www.frc.org.uk/documents/9305/ISA_UK_240_Revised_March_2026_xuvAkap9.pdf", date: 2026-04-30, access: full, locator: "para 29 printed p.8; A56 p.35" }
    - { ref: AS2110-PCAOB-2026, title: "AS 2110: Identifying and Assessing Risks of Material Misstatement", publisher: PCAOB, type: standard-setter, url: "https://pcaobus.org/oversight/standards/auditing-standards/details/AS2110", date: 2026-10-16, access: full, locator: "paras .49-.53" }
    - { ref: INDO-ICOBUSS-2025, title: "Artificial intelligence for fraud risk assessment in auditing", publisher: 5th International Conference on Business & Social Sciences (ICOBUSS), Surabaya, type: academic, url: "https://ojsicobuss.stiesia.ac.id/index.php/icobuss1st/article/download/684/618/1209", date: 2025-10, access: full, locator: "abstract; Tables 2 and 5" }
    - { ref: PETERS-2022, title: "Auditor automation usage and professional skepticism (working paper)", publisher: Tilburg University, type: academic, url: "https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/", date: 2022-12, access: full, locator: "abstract" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff update on outreach activities related to the integration of generative AI in audits and financial reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p.4" }
  last_reviewed: 2026-10-16
  notes: "C by this file's convention: the AFM observation covers unnamed firms. The experiment is a conference paper using a vignette and the authors conclude ChatGPT 'neutralized' the dilution effect, which the means support only loosely (the ChatGPT-condition gap is 0.94 against 1.58 without). Peters' paper is marked 'in preparation' (9 Dec 2022); abstract only."

- id: assurance-planning-risk-assessment-12
  title: Fraud risk assessment extended to AI-enabled fraud schemes and the authenticity of AI-generated evidence
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ expert-judgment, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Documents such as invoices and bank statements may now originate from or be altered by AI systems, and AI can be used to manipulate data or generate fictitious documents. Traditional fraud risk factors do not cover this."
  solution: "An idea (labelled idea) from regulators and professional bodies: the fraud risk assessment and engagement team discussion add AI-enabled schemes (altered training data, models edited to classify fraudulent transactions as legitimate, fabricated documents), consider the entity's use of AI or machine learning to initiate accounting entries, and plan authenticity checks, including document authenticity technology where authenticity is in doubt."
  outcomes:
    - { lever: risk, description: "Survey of senior internal audit leaders (internal audit, not external audit) on AI-enabled fraud", figure: "85% view AI-enabled fraud as a moderate to high risk; 62% say their internal audit function is unprepared or minimally prepared to detect it; 36% say moderately or very prepared", measures: "Share of 373 senior internal audit leaders responding to a Q4 2025 survey by the Internal Audit Foundation and Optro. An adjacent population, so it does not measure external-audit practice", provenance: independent, source_ref: IAF-AIFRAUD-2026 }
  prerequisites:
    - "Team members with skills to evaluate AI systems, with specialists where needed (ISA (UK) 240 A101 mentions forensic and IT experts)"
  risks_and_guardrails:
    - "IFIAR: auditors should be alert to deliberate or adversarial misuse of AI inside audited entities, including generating or manipulating data, documents or transactions to mislead or circumvent controls (IFIAR-TTF-2026 p.10)"
    - "ISA (UK) 240 A101: complex IT applications such as AI or machine learning algorithms that initiate accounting entries may raise susceptibility to management bias or other fraud risk factors (printed p.47)"
    - "ISA (UK) 240 A36: when a document may not be authentic, additional procedures may include document authenticity or integrity technology (printed p.30)"
    - "IRBA warned that new AI tools can create more convincing false evidence or fabricated working papers (IRBA-AIUPDATE-2024 p.1)"
  human_checkpoints:
    - "Engagement team discussion with the engagement partner (ISA (UK) 240 para 29; AS 2110 .49-.53)"
  role_evolution: "ISA (UK) 240 A101 says the auditor may assign forensic and IT specialists or more experienced individuals to the engagement where AI or ML algorithms initiate entries."
  evidence_grade: D
  sources:
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: innovation and audit quality 2026", publisher: IFIAR Technology Task Force, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p.10" }
    - { ref: ISAUK240-2026, title: "ISA (UK) 240 (Revised March 2026): The Auditor's Responsibilities Relating to Fraud in an Audit of Financial Statements", publisher: Financial Reporting Council, type: standard-setter, url: "https://www.frc.org.uk/documents/9305/ISA_UK_240_Revised_March_2026_xuvAkap9.pdf", date: 2026-04-30, access: full, locator: "A36 printed p.30; A101 p.47" }
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraph on AI-enabled fraud risk" }
    - { ref: IRBA-AIUPDATE-2024, title: "Artificial intelligence audit risks mitigation update", publisher: IRBA (South Africa), type: regulator, url: "https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf", date: 2024-09-19, access: full, locator: "p.1" }
    - { ref: IAF-AIFRAUD-2026, title: "Internal audit and AI-enabled fraud", publisher: Internal Audit Foundation and Optro, type: survey, url: "https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf", date: 2026, access: full, locator: "PDF p.3 (executive summary); p.13" }
  last_reviewed: 2026-10-16
  notes: "Idea. Regulators and the AICPA describe the risk and procedures; no firm deployment or measurement was found. The AICPA practice aid itself is member-gated; its content on AI-enabled fraud comes from the Accounting Today report. The IAF report page carries no publication month; the PDF says the survey ran in Q4 2025."

- id: assurance-planning-risk-assessment-13
  title: Structured understanding of the entity's own AI use in financial reporting as a risk assessment procedure
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ research-synthesis, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Clients use AI in accounting, controls and business processes, sometimes through agents or vendors with no traceable workflow. Auditors need to know where AI touches financial reporting before they can assess risk. No AI-specific step is in the AS 2110 text, and ISA 315 mentions AI once."
  solution: "An idea (labelled idea) drawn from published guidance: the auditor asks structured questions about the entity's AI use and governance, assesses how it affects the information system, controls and risks of material misstatement, and decides what that implies for team competence and responses. The AICPA practice aid (13 Oct 2026) covers this in its first part: AI versus ordinary automation, data quality, AI-specific risks (data, model, hallucination, explainability, bias), AI-operated controls and service-organisation reports. The CAQ's 2024 paper gives questions across governance, fraud and other risk areas."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: AICPA-PA-2026 }
  prerequisites:
    - "Team competence: the AICPA says practitioners may need a blend of auditing expertise, AI knowledge, data skills, scepticism and specialist support (AICPA-PA-2026)"
    - "Management able to explain its AI use. The AICPA compares heavy AI reliance with complex valuation models, where management that cannot understand the model may lack the needed skills (AT-AICPAPA-2026)"
  risks_and_guardrails:
    - "ISA (UK) 315 App 5 para 5: where emerging technologies such as AI are in the information system, the auditor may include them when identifying IT applications subject to risks from IT, and responsibilities for IT applications and general IT controls 'remain unchanged' (printed p.96)"
    - "AICPA (as reported): a one-to-one translation of risks to the AI context cannot always be applied, and the strategy for controls operated by AI may differ from that for traditional automated controls (AT-AICPAPA-2026)"
    - "The AICPA says deeper guidance on assessing the risk of material misstatement and evaluating audit evidence for companies using AI will be added later (AICPA-PA-2026)"
  human_checkpoints:
    - "Not applicable; the procedure is performed by the engagement team"
  role_evolution: "CAQ says teams may need extra training or an individual with the requisite GenAI knowledge (CAQ-GENAI-2024). The AICPA stresses team competence and specialist support (AICPA-PA-2026)."
  evidence_grade: D
  sources:
    - { ref: AICPA-PA-2026, title: "AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing", publisher: AICPA & CIMA, type: professional-body, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "section 'Considering an organization's use of AI'" }
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraphs on acceptance, understanding of the entity and AI-operated controls" }
    - { ref: ISAUK315-2025, title: "ISA (UK) 315 (Revised July 2020): Identifying and Assessing the Risks of Material Misstatement, updated September 2025", publisher: Financial Reporting Council, type: standard-setter, url: "https://media.frc.org.uk/documents/ISA_UK_315_Revised_July_2020_Updated_September_2025.pdf", date: 2025-09, access: full, locator: "Appendix 5 para 5, printed p.96" }
    - { ref: CAQ-GENAI-2024, title: "Auditing in the age of generative AI", publisher: Center for Audit Quality, type: professional-body, url: "https://thecaq.wpenginepowered.com/wp-content/uploads/2024/04/caq_auditing-in-the-age-of-generative-ai__2024-04.pdf", date: 2024-04, access: full, locator: "pp.11-14 (risk table), p.6" }
    - { ref: ACRA-APG1-2025, title: "Audit Practice Guidance No. 1 of 2025: Delivering quality audits in a technology-driven environment", publisher: ACRA (Singapore), type: regulator, url: "https://www.acra.gov.sg/news-events/news-announcements/906/", date: 2025-12-26, access: full, locator: "PDF p.14 (cybersecurity and emerging technologies checkpoint)" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: innovation and audit quality 2026", publisher: IFIAR Technology Task Force, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p.10" }
  last_reviewed: 2026-10-16
  notes: "Idea. The AICPA practice aid (51 pages per CFO Dive) is member-gated and was not opened; its content comes from the AICPA release, the Journal of Accountancy and Accounting Today reports, so statements are attributed 'as reported'. The 'idea' label reflects that these are guidance documents and no firm is reported as having rolled out an AI-use questionnaire or tool. The subject of the work is the client's AI, not an AI tool used by the auditor."

- id: assurance-planning-risk-assessment-14
  title: Tools that map user roles, access rights and activity across the client's IT environment to inform IT risk assessment and planning
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ data-reporting, review-assurance ]
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Understanding the entity's IT environment and general IT controls is a required part of risk assessment, but sampling user lists and access logs gives a partial picture."
  solution: "The AFM saw external auditors using tools to identify and evaluate roles, access rights, and user and control activity within the client's IT system. This gave an integrated view of expected user activity (for example superuser accounts) and unauthorised activity, supporting the overall risk assessment and the planning of further substantive procedures. The tools in question are analytics tools, not necessarily AI."
  outcomes:
    - { lever: risk, description: "Context, not an outcome of this use case: findings for insufficient testing of IT general and application controls in inspected listed PIE audits", figure: "29, 50, 65, 55 and 39 findings in the 2021 to 2025 surveys respectively", measures: "Number of findings in the supplementary detail some IFIAR members provided under the internal control testing theme ('failure to sufficiently test information technology general and application controls'); not all members gave this detail. Concerns controls testing, so it is adjacent to this use case", provenance: independent, source_ref: IFIAR-SURVEY-2026 }
  prerequisites:
    - "Reliable and relevant input data; an AFM footnote points to the Dutch adoption of ISA 315 (paras 25-26 and Annexes 5 and 6) on understanding IT and general IT controls (AFM-12BB-2025 p.16)"
    - "Follow-up of the IT auditor's findings before relying on a tool (AFM-12BB-2025 p.17)"
  risks_and_guardrails:
    - "AFM bad practice: insufficient follow-up of identified risks and of the IT auditor's findings, and no evaluation of the usability of input data where general IT controls are ineffective (AFM-12BB-2025 p.17)"
    - "ISA (UK) 315 requires understanding of the information system and the IT environment (paras 25-26); A57 says the auditor may use automated tools to understand flows of transactions (printed p.28)"
    - "ACRA: understanding of the audited entity's IT environment is a foundation for risk assessment and the design of responses (ACRA-APG1-2025 p.12)"
  human_checkpoints:
    - "Auditor evaluates tool results against the IT auditor's findings (AFM-12BB-2025 p.17)"
  role_evolution: "AFM sees tools taking over straightforward staff-auditor tasks, creating capacity for judgement work, and notes that at several firms a tool ambassador or specialist attended planning meetings (AFM-12BB-2025 p.21)."
  evidence_grade: C
  sources:
    - { ref: AFM-12BB-2025, title: "12 building blocks for controlled use of auditing tools", publisher: Autoriteit Financiele Markten, type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "pp.16-17, 21" }
    - { ref: IFIAR-SURVEY-2026, title: "Survey of inspection findings 2025", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01, access: full, locator: "Table B.4, PDF p.23" }
    - { ref: ISAUK315-2025, title: "ISA (UK) 315 (Revised July 2020): Identifying and Assessing the Risks of Material Misstatement, updated September 2025", publisher: Financial Reporting Council, type: standard-setter, url: "https://media.frc.org.uk/documents/ISA_UK_315_Revised_July_2020_Updated_September_2025.pdf", date: 2025-09, access: full, locator: "A57 printed p.28" }
    - { ref: ACRA-APG1-2025, title: "Audit Practice Guidance No. 1 of 2025: Delivering quality audits in a technology-driven environment", publisher: ACRA (Singapore), type: regulator, url: "https://www.acra.gov.sg/news-events/news-announcements/906/", date: 2025-12-26, access: full, locator: "PDF p.12" }
  last_reviewed: 2026-10-16
  notes: "C by this file's convention: AFM good practice at unnamed firms. The ISA (UK) 315 A57 example (printed p.28) says the auditor may use automated tools to understand flows of transactions. The IFIAR counts are controls-testing findings, so they are not evidence for this use case."

- id: assurance-planning-risk-assessment-15
  title: Engagement-level plan for AI and tool use, with team competence checked at planning
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ coordination-scheduling, document-production ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Tools are adopted ad hoc, it is not always clear where GenAI was applied in an audit, and teams may use tools they are not trained for."
  solution: "The audit plan states which tools will be used and for which risks or assertions, the engagement leader sets expectations for technology use at the outset, and the team's competence to use the tools is assessed at planning. The AFM saw audit plans at some firms stating which tools are used; IFIAR asks engagement leaders to set engagement-specific expectations at the outset; the AICPA practice aid recommends firm planning on intended AI use in specific engagements."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: AFM-12BB-2025 }
  prerequisites:
    - "A firm policy on which audit phases tools may be used in and which assertions or risks they address (AFM-12BB-2025 p.13)"
    - "Engagement partners who understand the tools, confirm they are firm-approved and check staff use them correctly (AICPA-PA-2026)"
  risks_and_guardrails:
    - "AFM: it is not always clear where and how GenAI has been applied in the audit process, and the auditor needs to know where it was used to take responsibility in review (AFM-12BB-2025 p.31)"
    - "AFM: conditions for using tools as part of risk assessment procedures may differ from those where audit evidence is obtained (AFM-12BB-2025 p.23)"
    - "NFRA staff paper (as reported): documentation should let an experienced auditor unconnected with the engagement see which tool processed a balance or assertion and the extent of human review (NFRA-CAALLEY-2026)"
  human_checkpoints:
    - "Engagement leader sets expectations at the outset; senior team members review the overall use of technology in the file (IFIAR-TTF-2026 p.7)"
  role_evolution: "Engagement partners take on responsibility for understanding the tools used and confirming approval and correct use (AICPA-PA-2026). NFRA differentiates training by role: preparers, reviewers and engagement partners (NFRA-CAALLEY-2026)."
  evidence_grade: C
  sources:
    - { ref: AFM-12BB-2025, title: "12 building blocks for controlled use of auditing tools", publisher: Autoriteit Financiele Markten, type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "pp.13, 23, 31" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: innovation and audit quality 2026", publisher: IFIAR Technology Task Force, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p.7" }
    - { ref: AICPA-PA-2026, title: "AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing", publisher: AICPA & CIMA, type: professional-body, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "section 'Use of AI-related technological resources by audit firms'" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: CAalley (reporting an NFRA staff paper), type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Audit documentation and training to change'" }
  last_reviewed: 2026-10-16
  notes: "C by this file's convention: AFM good practice at unnamed firms. This is a planning-governance step rather than AI doing the work; it is included because the module description covers audit strategy and planning and regulators ask for it."

- id: assurance-planning-risk-assessment-16
  title: Continuous reassessment of risk during the audit using predictive analytics or real-time data
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ data-reporting, expert-judgment ]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "The risk assessment is set at planning and revised only when the team notices contradicting evidence, although AS 2110 .74 requires it to continue throughout the audit."
  solution: "An idea (labelled idea): predictive analytics or real-time data feed the risk assessment through the audit so risk ratings and planned procedures update as evidence arrives. IFIAR names 'enhanced risk assessment that leverage[s] predictive analytics and/or real-time data' as an example of how a human-led approach can improve audit quality. Caseware says its long-term aim includes AI that continuously assists planning and risk identification."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: IFIAR-TTF-2026 }
  prerequisites:
    - "Data feeds from the client and a process that routes tool signals to the engagement team"
  risks_and_guardrails:
    - "AS 2110 .74: when evidence contradicts the basis of the original assessment, the auditor must revise it and modify planned procedures"
    - "NFRA staff paper (as reported): do not accept a tool's low-risk classification without periodically testing it (NFRA-CAALLEY-2026)"
    - "IFIAR: potential over-reliance on outputs without sufficient challenge (IFIAR-TTF-2026 p.3)"
  human_checkpoints:
    - "Engagement team decides whether to revise the risk assessment (AS 2110 .74)"
  role_evolution: "Not addressed."
  evidence_grade: D
  sources:
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: innovation and audit quality 2026", publisher: IFIAR Technology Task Force, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p.3, executive summary" }
    - { ref: AS2110-PCAOB-2026, title: "AS 2110: Identifying and Assessing Risks of Material Misstatement", publisher: PCAOB, type: standard-setter, url: "https://pcaobus.org/oversight/standards/auditing-standards/details/AS2110", date: 2026-10-16, access: full, locator: "para .74" }
    - { ref: CASEWARE-VERITY-2026, title: "From AiDA to agentic: How Caseware's AI has evolved", publisher: Caseware, type: vendor, url: "https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved", date: 2026-07-28, access: full, locator: "section 'What's next'" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: CAalley (reporting an NFRA staff paper), type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Professional scepticism cannot be delegated to technology'" }
  last_reviewed: 2026-10-16
  notes: "Idea. The IFIAR sentence is an example of potential benefit, not a report of firms doing it. No deployment found."

- id: assurance-planning-risk-assessment-17
  title: GenAI research assistant for industry, regulatory and entity background during the understanding-of-the-entity step
  archetype: assurance
  module: planning-risk-assessment
  function: service-delivery
  work_types: [ research-synthesis ]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Obtaining an understanding of the industry, regulatory environment and public information about the entity is time-consuming desk research. AS 2110 .07 and .11 expect it, including reading public information relevant to the likelihood of misstatement."
  solution: "Auditors use firm-approved or general chatbots to research the entity and its environment and to summarise accounting and legal documents. ICAEW says simple LLM chatbots are used by auditors to enhance their understanding of entities and their environments through research. PCAOB staff found in 2024 that firms' GenAI use focused on administrative and research activities. Japan's FSA discussion paper cites the JICPA expecting AI use in understanding the company during planning."
  outcomes:
    - { lever: speed, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: ICAEW-PIERPOINT-2025 }
  prerequisites:
    - "A policy on client confidentiality for tools that process client data (PCAOB-GENAI-2024 p.4: some firms limit what can be uploaded and some bar GenAI on audit procedures)"
  risks_and_guardrails:
    - "FSA discussion paper: hallucination can produce provisions that do not exist or differ from the source, a particular risk when interpreting law and accounting standards (FSA-DP-2025 p.13)"
    - "CPAB observed limited AI implementations in the public company audit files it had inspected as of Sep 2024 (CPAB-AI-2024 p.1)"
    - "Kokina et al. (22 interviews): simple AI such as key data extraction and OCR is widely used while complex AI tools are being developed (KOKINA-2025)"
  human_checkpoints:
    - "Auditor evaluates the information gathered. ICAEW says the tools cannot do the deep entity knowledge-building a human auditor does (ICAEW-PIERPOINT-2025)"
  role_evolution: "ICAEW expects human judgement to remain essential to interpret outputs (ICAEW-PIERPOINT-2025)."
  evidence_grade: C
  sources:
    - { ref: ICAEW-PIERPOINT-2025, title: "Testing Gen AI platforms: can they do audit work?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work", date: 2025-09-24, access: full, locator: "introduction" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff update on outreach activities related to the integration of generative AI in audits and financial reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p.4" }
    - { ref: FSA-DP-2025, title: "Study on the potential utilization of generative AI in audit practices and challenges related to audit quality (DP2025-3)", publisher: Financial Services Agency, Japan (Financial Research Center), type: regulator, url: "https://www.fsa.go.jp/frtc/english/seika/discussion/2025/DP2025-3_Eng.pdf", date: 2025-07, access: full, locator: "pp.8, 13" }
    - { ref: CPAB-AI-2024, title: "The use of artificial intelligence in the audit: balancing innovation and risk", publisher: CPAB (Canada), type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf", date: 2024-09, access: full, locator: "p.1" }
    - { ref: KOKINA-2025, title: "Challenges and opportunities for artificial intelligence in auditing: evidence from the field", publisher: International Journal of Accounting Information Systems 56 (Kokina et al.), type: academic, url: "https://ideas.repec.org/a/eee/ijoais/v56y2025ics1467089525000107.html", date: 2025, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "C by this file's convention: ICAEW and PCAOB staff report use without naming firms. The Kokina abstract page shows only the year. The PCAOB data are from outreach in 2024 and may be out of date; CPAB's observation dates from Sep 2024."
```

---

## 3. Module notes

### Processes and key steps (with work types)

1. **Understand the entity, its environment and its use of IT** (ISA 315 paras 19–26; AS 2110 .07–.17, .28–.29, Appendix B): `research-synthesis`, `review-assurance`. Includes the entity's AI use (ISA 315 App 5 para 5; AICPA practice aid).
2. **Perform risk assessment procedures**: inquiries, analytical procedures, observation and inspection (ISA 315 para 14; AS 2110 .46–.48, .54–.58): `data-reporting`, `research-synthesis`.
3. **Engagement team discussion and fraud brainstorming** (AS 2110 .49–.53; ISA (UK) 240 para 29): `expert-judgment`.
4. **Identify and assess risks of material misstatement** at financial statement and assertion levels, including fraud risks and the revenue presumption (AS 2110 .59–.69): `expert-judgment`.
5. **Materiality and performance materiality**: `expert-judgment`, `data-reporting`.
6. **Scoping**: significant classes, accounts, disclosures and, for groups, components (ISA 315 A203): `expert-judgment`, `data-reporting`.
7. **Audit strategy and plan, planning documentation, planned use of tools**: `document-production`, `coordination-scheduling`.
8. **Budgeting and staffing**: `coordination-scheduling`. No governance or evidence material on AI here was found (see Gaps).
9. **Ongoing reassessment** as evidence arrives (AS 2110 .74): `expert-judgment`.

### Requirement map: ISA 315 and AS 2110 as they touch AI

"Text says" is what the standard states. "Reading" is this file's interpretation.

| Requirement | Text says | Reading for AI use |
|---|---|---|
| ISA 315 para 13 (printed p.7) | Risk assessment procedures must not be biased toward corroborative evidence or away from contradictory evidence | A tool that echoes the auditor's prior view, or a roll-forward template, can introduce the bias the paragraph prohibits |
| ISA 315 para 14, A21, A31 (printed pp.7, 18, 20) | Procedures include inquiry, analytical procedures, observation and inspection. Automated tools may analyse large data volumes, and automated analytical procedures may be called data analytics | A tool can perform the analytics. It cannot perform the inquiry and observation (ICAEW test found chatbots could not) |
| ISA 315 A203 (printed p.63) | Whole populations may be analysed with automated techniques to identify significant classes, with examples | Whole-population scoping is explicitly contemplated |
| ISA 315 App 5 para 5 (printed p.96) | Emerging technologies including AI in the information system may be included when identifying IT applications subject to IT risks. Responsibilities for IT applications and general IT controls are unchanged | The only AI reference. It asks for understanding of client AI use without new requirements |
| AS 2110 .04 | Risk assessment procedures must be sufficient for a reasonable basis for identifying and assessing risks | Sets the sufficiency bar a tool-assisted procedure must meet |
| AS 2110 .07–.08 | Understand the company and evaluate significant changes since prior periods | The prior-year roll-forward tools and entity-document summarisers feed here |
| AS 2110 .28–.29, App B | Understand the information system and how IT affects the flow of transactions; manual and automated systems | Client AI inside the information system falls here by extension (no AI wording) |
| AS 2110 .46–.48 | Analytical procedures to enhance understanding and identify risk areas; expectations from the auditor's understanding; revenue analytics | Analytics-based and predictive tools. The note says these use preliminary or aggregated data and lack substantive precision |
| AS 2110 .49–.53 | Discussion among key engagement team members, including the engagement partner, with fraud brainstorming and a questioning mind | A tool can support the discussion but is not a participant (reading) |
| AS 2110 .54–.58 | Inquire of the audit committee, management, internal audit and others | Document-analysis tools do not replace the inquiries (reading) |
| AS 2110 .74 | Revise the assessment when evidence contradicts it | Basis for continuous reassessment tools |
| AS 1105.14 as amended (PCAOB 2024-007 p.25, App. 1 p.A1-4) | The purpose of a procedure determines whether it is a risk assessment procedure, test of controls or substantive procedure. A multi-purpose procedure must achieve each objective | A tool used for both risk assessment and substantive work must meet the higher bar for each |
| AS 2110 .05 and .41 | Amended, effective 15 Dec 2026 (the PCAOB page links the notice to Release 2024-005, QC 1000) | Conforming change from the quality control standard, not an AI change. Amended text not read |

### Common pain points

- **Prior-year reliance.** In the CPA.com survey of US firms, 85% say they prioritise rolling binders forward to cut time, 79% assigning the same staff as last year, 60% carrying forward the prior-year risk assessment, and 64% challenging last year's procedures in relation to risk assessment (CPACOM-ATR-2025 PDF p.14). The FRC's 2026 review names ineffective planning, over-reliance on prior-year approaches, unclear responsibilities and late involvement of senior reviewers and specialists as root causes needing remediation (CPIA-ARAQ-2026).
- **Limited technology in risk-driven audit.** Fewer than a quarter of firms (22%) answered the question on benefits of automated risk assessment, and every respondent among those using it reported a positive impact (CPACOM-ATR-2025 PDF p.20). 89% of firms report they are not using technology to enable substantive analytics (same page).
- **Data access.** In the CPA.com survey, the top perceived blockers to audit transformation were staff not trained (66%), poor quality client data (60%), and lack of access to client information and systems (53%) and budget constraints (53%) (CPACOM-ATR-2025 PDF p.8).
- **Not knowing where GenAI was used.** The AFM found it is not always clear where and how GenAI has been applied in an audit (AFM-12BB-2025 p.31).
- **Fee pressure on materiality and scoping.** PCAOB staff said inspections would evaluate significant year-over-year materiality changes and the scoping of multi-location audits (PCAOB-PRIORITIES-2024 p.5).
- **Misread tool results.** The most frequent technology-related inspection findings are misinterpreting results and the extent of outlier testing (IFIAR-TTF-2025 p.5).

### Metrics and benchmarks (with sources)

| Metric | Value | What it measures (source's words or close paraphrase) | Source |
|---|---|---|---|
| ATTs frequently observed in risk assessment | 55% (2024); 49% (2023) | Share of 47 (45) IFIAR members answering "frequently observed" for risk assessment; also 13% never, 32% infrequently (2024) | IFIAR-TTF-2025 p.5 |
| ATTs frequently observed, journal entry testing | 88% (2024) | Same question, 48 members | IFIAR-TTF-2025 p.5 |
| Members reporting findings that a tool was not used as intended | 31% (2024); 29% (2023) | Share of IFIAR members reporting such findings; not specific to risk assessment | IFIAR-TTF-2025 p.5 |
| Year-on-year increase in AI-enabled tools | about 30% (2025) | Collectively reported by the six global networks; subject to differing reporting practices | IFIAR-TTF-2026 p.5 |
| Risk assessment inspection theme | 44 of 770 listed PIE audits with at least one finding (6%); 53 findings (2025). 39 of 696 (6%); 49 findings (2024). 37, 33, 39 findings in 2021–2023 | Listed PIE audits inspected for the theme, six global networks, IFIAR members | IFIAR-SURVEY-2026 pp.21–22 |
| Same, for internal control testing | 88 of 641 audits (14%); 213 findings (2025) | Same basis, for comparison | IFIAR-SURVEY-2026 pp.21–22 |
| Failure to perform sufficient risk assessment procedures, within accounting estimates | 25 findings (2025); 21 (2024) | Supplementary detail provided by some members | IFIAR-SURVEY-2026 p.23 |
| Failure to develop a group audit plan (scoping) | 3 findings in each of 2024 and 2025 | Supplementary detail provided by some members | IFIAR-SURVEY-2026 p.23 |
| Average share of tool use in risk assessment | 28% (tests of details 51%) | Average across six Dutch PIE firms of how often tools are used in an area; areas overlap | AFM-12BB-2025 p.27 |
| AI as a share of tool types available to staff | 3% (data analytics 32%) | Average percentage across PIE firms for each type of tool available to staff | AFM-12BB-2025 p.27 |
| US firms with an automated solution for risk assessment | 22% | Share of surveyed firms (74 registered, 54 with complete data; base for the chart not stated), self-reported | CPACOM-ATR-2025 PDF p.10 |
| US firms with automated substantive analytics | 11% | Same | CPACOM-ATR-2025 PDF p.10 |
| Firms with a formal monitoring of tool quality impact | none among six largest UK firms | FRC found no formal monitoring performed to quantify the audit quality impact of tools | FRC-ATT-2025, section "Monitoring the use and impact of ATTs" |
| Restatement prediction by multi-agent risk scorer | AUROC 0.782; PR-AUC 0.341; ECE 0.052 | 3,200 US firm-years, label is restatement | ARXIV-UMAR-2026 |
| AI investment and restatement likelihood (pre-GenAI, observational) | one standard deviation of recent AI investment associated with 5.0% lower likelihood of an audit restatement | 36 largest audit firms, resume-based AI-worker measure, plus 17 partner interviews. Adjacent to this module (all audit AI), so capped | FEDYK-2022 |
| Chatbot ISA 315-style test | see use case 9 | Three models, one run each | ICAEW-PIERPOINT-2025 |

No independent measure was found of error rates, override rates or parallel-run results for any AI risk-assessment tool in live audits.

### Guardrails and regulatory points

- **FRC risk taxonomy.** Deficient output, misuse of output (misinterpretation, misunderstanding of methodology) and non-compliant methodology; mitigated by system design, certification, staff education and human-in-the-loop review (FRC-GENAI-2026 pp.18–19). Outputs need not match the persuasiveness of the procedure they replace as long as the methodology does not overstate it (p.19).
- **Certification and monitoring.** The six largest UK firms mostly had certification processes but were still updating them for AI and developing ways to monitor tool use and quality impact (FRC-ATT-2025).
- **IFIAR.** Four asks to firms: monitor impact, prioritise high-impact tools, govern GenAI, keep humans in control (IFIAR-TTF-2025 pp.6–8). The 2026 report adds suggested monitoring metrics (engagement coverage, false-positive and false-negative rates against a manual sample, rework rates, escalation incidence) and benchmarking of tool-driven results against traditional methods (IFIAR-TTF-2026 pp.8–9). It also asks for early engagement with regulators where technology may significantly alter the work (p.4).
- **AFM.** Twelve building blocks. The lower three layers (foundation, input data, controlled implementation of tools) must be in place before deploying GenAI (AFM-12BB-2025 p.1). Tool conditions for risk assessment may differ from those for evidence (p.23).
- **NFRA (as reported).** No lower evidentiary bar for technology-generated information; do not accept a tool's low-risk classification without periodic testing; vendor claims need independent evaluation; revalidate on material model or vendor change (NFRA-CAALLEY-2026).
- **PCAOB.** Staff outreach in 2024 found firms did not view PCAOB standards as an impediment to GenAI (PCAOB-GENAI-2024 p.4). Release 2024-007 says it does not address AI (p.5).
- **AICPA.** Part 1 of the practice aid on the entity's AI use; Part 2 on firm use of AI tools under quality management; disclosure of AI use in the engagement letter is not required by AICPA standards but may be by state law or firm policy (CFODIVE-AICPA-2026).
- **IAASB.** Roundtables with 240+ participants judged ISQM 1 and ISA 220 (Revised) a sound base; non-authoritative technology material approved in Dec 2025; the Mar 2026 action plan outcome was not found (IAASB-TQM-2026).

### Frontier signals (dated and sourced)

- **2026-08-05:** IAASB exposure drafts on ISA 330, 500 and 520; ED-520 adds a requirement on results of risk-assessment analytical procedures and ED-330 proposes removing the always-substantive requirement; comments due 2026-12-15 (IAASB-EDPAGE-2026; AUASB-CPED-2026).
- **2026-04-30:** FRC publishes ISA (UK) 240 (Revised March 2026), effective for periods commencing on or after 2026-12-15, with explicit application material on automated tools in fraud brainstorming and AI/ML-driven entries (ISAUK240-2026).
- **2026-03-30:** FRC publishes the generative and agentic AI guidance, "the first from any audit regulator globally" per the FRC (FRC-GENAINEWS-2026). **2026-06-04:** FRC opens an Audit Tech & AI Sandbox and a research project on barriers to technology adoption for smaller firms (FRC-SANDBOX-2026).
- **2026-04-20:** IFIAR reports an approximate 30% year-over-year increase in AI-enabled tools at the six networks, flags agentic AI as moving from task automation toward orchestration of several activities, and asks for clear explanation of key judgements made with AI outputs (IFIAR-TTF-2026 p.5).
- **2026-10-13:** AICPA says it will add guidance on risk-of-material-misstatement assessment and audit evidence for AI-using companies (AICPA-PA-2026).
- **2026-09-22:** MindBridge announces Agentic Risk Assessment (MINDBRIDGE-ARA-2026). **2026-06-24:** Deloitte unifies agents in Omnia, including agents that analyse information to identify potential risk factors (DELOITTE-OMNIA-2026). **2026-07-28:** Caseware shows a planning-review agent scenario (CASEWARE-VERITY-2026).
- **2025-10-28 and 2026-10-07:** PwC said it planned a risk assessment tool "soon" (Oct 2025); the Oct 2026 article lists other tools and names no risk assessment tool (PWC-AT-2025; CFODIVE-PWC-2026).
- **2026-07-24:** NFRA staff paper on technology principles, including planning and risk assessment (NFRA-CAALLEY-2026).
- **2026-05-08:** a research session at the Deloitte/KU Auditing Symposium covered how the apparent size of an effect changes auditors' causal and sceptical judgements of AI-detected correlations (agenda title only; the paper was not read) (KU-SYMPOSIUM-2026).
- **2026-09-26:** FinancialAuditBench (90 workpaper completion and review tasks across six synthetic engagements, 11 frontier models) reports that agents complete much staff-level work well but sometimes perform inappropriate procedures or write incorrect documentation (ARXIV-FAB-2026). It covers workpaper completion and review, not risk assessment specifically.

### Workforce and role effects

- Planning root causes in the FRC's 2026 review include unclear responsibilities and late senior involvement, which tool-based checks at planning could target but no source says they do (CPIA-ARAQ-2026).
- AFM saw tools taking over straightforward staff tasks, shifting staff to judgement work, and "tool ambassadors" attending planning meetings at several firms (AFM-12BB-2025 p.21).
- PwC says it hires engineers into assurance and seeks dual-track CPA and data-science profiles (PWC-AT-2025).
- IFIAR expects training mapped to competencies, with refresh intervals proportionate to risk (IFIAR-TTF-2026 p.7). NFRA (as reported) differentiates training for preparers, reviewers and engagement partners.
- Observational evidence from before GenAI links more AI investment at audit firms to fewer accounting employees (3.6% after three years and 7.1% after four years per standard deviation of AI investment) (FEDYK-2022). This is a cross-firm correlation.
- Experimental evidence on judgement is mixed. Automation reduced scepticism in one study (PETERS-2022), auditors discounted AI advice that contradicted management's estimate more than identical human advice in another (COMMERFORD-2022, complex estimates), and a registered report proposes testing whether GenAI use lowers motivation and later judgement quality (HOLMSTROM-2024).
- 81% of tax and audit professionals say they use AI regularly, and more than a quarter would not accept a job at a firm without professional-grade AI (TRI-FOP-2026). A survey of 3,400+ digital trust professionals found 38% of organisations have a formal comprehensive AI policy (ISACA-PULSE-2026), which bears on how much AI governance an auditor will find at a client.

### Objections and concerns practitioners raise

- Chatbots cannot do what a risk assessment requires: no inquiry, observation or deep entity knowledge, and their answers differ by model (ICAEW-PIERPOINT-2025).
- Automation bias and over-reliance. The chair of ICAEW's Technology Faculty Board said he was disappointed that the FRC guidance gives automation bias a single paragraph on page 35 (ICAEW-FRCVIEW-2026). The guidance also mentions it in its training and oversight passages and in example 1 (FRC-GENAI-2026 pp.38 and 46). IFIAR flags a decline in professional scepticism as a GenAI risk (IFIAR-TTF-2025 p.7).
- Smaller firms lack central technology and methodology teams and depend on vendors; the FRC guidance gives them little (ICAEW-FRCVIEW-2026).
- Many tools are features added to existing products, so firms need questions to ask vendors (ICAEW-FRCVIEW-2026).
- The probabilistic nature of GenAI means no tool can be guaranteed to give the needed output every time, so a rules-based tool may be needed alongside it (RSM UK's audit data analytics director, in ICAEW-FRCVIEW-2026).
- Data confidentiality limits what can be uploaded, and some firms bar GenAI from audit procedures (PCAOB-GENAI-2024 p.4).

### Interview probes for an advisor

1. At planning, which risk assessment procedures (inquiry, analytics, observation and inspection) now use a tool, and what does the file say the output was used for: to focus the review or to reach a conclusion?
2. After a summarisation or document tool, how do you evidence that someone read the underlying source, and what triggers a deeper read?
3. When a tool classifies an account, class of transactions or entity as lower risk, who tests that classification, how often, and what do you do when the model or vendor changes?
4. How do you find out and record how the client uses AI in financial reporting and controls, and what happens when management cannot explain it?
5. What do you measure about whether tool-assisted risk assessment is better (false negatives against a manual assessment, rework, inspection findings), and has any result changed how a tool is used?

---

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| Heavy client reliance on AI treated like reliance on complex valuation models, and the effect on acceptance and continuance (management integrity, skills, team competence) | acceptance-independence | AT-AICPAPA-2026; AICPA-PA-2026 |
| Walkthrough assistants that draft process narratives and flowcharts (PwC Advanced Walkthrough Assistant; KPMG Copilot for walkthrough narratives) | controls-testing | PWC-AT-2025; KPMG-CLARA-2025 |
| AI-operated controls, how to test controls that learn or drift, COSO's definition of management reliance on AI, general IT controls for AI components | controls-testing (and specialists for IT audit) | AT-AICPAPA-2026; COSO-GENAI-2026 |
| Reliance on service-organisation reports where the provider uses AI | other-assurance (SOC) and controls-testing | AT-AICPAPA-2026 |
| Journal-entry anomaly detection with LLMs; whole-document irregularity detection (167 items, 74–96% correctness at the basic-prompt stage, five models, one capital group) | substantive-testing | ARXIV-AUDITCOPILOT-2025; PL-YOAA-2025 |
| Agent benchmarks on workpaper completion and review, XBRL multi-document reasoning, five-stage statement-audit benchmark | substantive-testing and completion-reporting | ARXIV-FAB-2026; ARXIV-FINAUDITING-2025; ARXIV-LLMAUDIT-2025 |
| Disclosure checklist agents (KPMG Financial Report Analyzer; Caseware Disclosure Checklist Agent, 2.7 hours per run, vendor figure) | completion-reporting | KPMG-CLARA-2025; CASEWARE-VERITY-2026 |
| Tool certification, recertification on model change, monitoring metrics, ISQM 1 and QC 1000 duties, FRC sandbox | quality-management (firm level) | FRC-ATT-2025; IFIAR-TTF-2026; FRC-SANDBOX-2026; ACRA-APG1-2025 |
| Supervision and review of AI output, automation-bias training, algorithm aversion, motivation and judgement effects | quality-management (engagement level) | PETERS-2022; COMMERFORD-2022; HOLMSTROM-2024; FABIAN-2026 |
| IT-audit evidence evaluation with multi-agent systems | controls-testing and specialists | not read in full; abstract in the pilot (arXiv 2608.07688) |
| Cost and fee effect of AI, workforce displacement | cross-cutting (firm business model and workforce) | FEDYK-2022; TRI-FOP-2026 |

---

## 5. Sources

All sources were opened unless noted. `access: full` means the page or document was opened and the relevant parts read (abstract pages for papers, as noted). No source in this list is `search-only`. Dates are publication dates from the page or document, except where marked.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 |
| FRC-GENAINEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 |
| FRC-AIAUDIT-2025 | FRC publishes landmark guidance providing clarity to audit profession on the uses of AI | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/ | 2025-06-26 |
| FRC-ATT-2025 | Thematic Review: Certification of Automated Tools and Techniques (HTML version, machine-converted) | Financial Reporting Council | regulator | https://www.frc.org.uk/docs/8383/html/ | 2025-06-26 |
| FRC-SANDBOX-2026 | FRC invites firms and companies to experiment, innovate and reduce burdens through new sandbox programmes | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/06/frc-invites-firms-and-companies-to-experiment-innovate-and-reduce-burdens-through-new-sandbox-programmes/ | 2026-06-04 |
| ISAUK315-2025 | ISA (UK) 315 (Revised July 2020), updated September 2025 (UK adoption of ISA 315 (Revised 2019)) | Financial Reporting Council | standard-setter | https://media.frc.org.uk/documents/ISA_UK_315_Revised_July_2020_Updated_September_2025.pdf | 2025-09 |
| ISAUK240-2026 | ISA (UK) 240 (Revised March 2026) | Financial Reporting Council | standard-setter | https://www.frc.org.uk/documents/9305/ISA_UK_240_Revised_March_2026_xuvAkap9.pdf | 2026-04-30 |
| AS2110-PCAOB-2026 | AS 2110: Identifying and Assessing Risks of Material Misstatement | PCAOB | standard-setter | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2110 | 2026-10-16 (access date; the page shows no publication date) |
| PCAOB-TAA-2024 | Release No. 2024-007: amendments related to technology-assisted analysis | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/rulemaking/docket-052/2024-007-adoptingrelease.pdf | 2024-06-12 |
| PCAOB-GENAI-2024 | Spotlight: staff update on outreach activities related to the integration of GenAI in audits and financial reporting | PCAOB staff | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 |
| PCAOB-PRIORITIES-2024 | Spotlight: staff priorities for 2025 inspections and interactions with audit committees | PCAOB staff | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf | 2024-12 |
| IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution (2025) | IFIAR Technology Task Force | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 |
| IFIAR-TTF-2026 | Use of technology in audits: innovation and audit quality 2026 | IFIAR Technology Task Force | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf | 2026-04-20 |
| IFIAR-SURVEY-2026 | Survey of inspection findings 2025 | IFIAR | regulator | https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf | 2026-04-01 |
| AFM-12BB-2025 | 12 building blocks for controlled use of auditing tools | Autoriteit Financiele Markten | regulator | https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf | 2025-12 |
| CPAB-AI-2024 | The use of artificial intelligence in the audit: balancing innovation and risk | CPAB (Canada) | regulator | https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf | 2024-09 |
| IRBA-AIUPDATE-2024 | Artificial intelligence audit risks mitigation update | IRBA (South Africa) | regulator | https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf | 2024-09-19 |
| ACRA-APG1-2025 | Audit Practice Guidance No. 1 of 2025: delivering quality audits in a technology-driven environment | ACRA (Singapore) | regulator | https://www.acra.gov.sg/news-events/news-announcements/906/ (PDF linked from page) | 2025-12-26 |
| FSA-DP-2025 | Study on the potential utilization of generative AI in audit practices and challenges related to audit quality (DP2025-3) | Financial Services Agency, Japan | regulator | https://www.fsa.go.jp/frtc/english/seika/discussion/2025/DP2025-3_Eng.pdf | 2025-07 |
| IAASB-EDPAGE-2026 | Proposed revisions for audit evidence and risk response: ISA 330, ISA 500 and ISA 520 (landing page; ED texts login-gated) | IAASB | standard-setter | https://www.iaasb.org/publications/proposed-revisions-audit-evidence-risk-response-isa-330-isa-500-isa-520 | 2026-08-05 |
| AUASB-CPED-2026 | Consultation paper: IAASB proposed standards on audit evidence and risk response | AUASB | standard-setter | https://www.auasb.gov.au/media/fegpk4s5/auasb_cp_iaasbproposedintlstdonauditevidence__riskresponse1.pdf | 2026-08 |
| IAASB-TQM-2026 | Technology quality management roundtables: outcomes and next steps | IAASB | standard-setter | https://www.iaasb.org/publications/technology-quality-management-roundtables-outcomes-and-next-steps | 2026-02-10 |
| COSO-GENAI-2026 | Achieving effective internal control over generative AI | COSO | standard-setter | https://www.coso.org/generative-ai (text read from a copy at https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf) | 2026-02 |
| ICAEW-PIERPOINT-2025 | Testing Gen AI platforms: can they do audit work? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09-24 |
| ICAEW-FRCVIEW-2026 | How helpful is FRC's guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05-06 |
| AICPA-PA-2026 | AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| CAQ-GENAI-2024 | Auditing in the age of generative AI | Center for Audit Quality | professional-body | https://thecaq.wpenginepowered.com/wp-content/uploads/2024/04/caq_auditing-in-the-age-of-generative-ai__2024-04.pdf | 2024-04 |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 |
| CFODIVE-AICPA-2026 | AICPA issues guidance for AI-assisted auditing | CFO Dive | press | https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/ | 2026-10-13 |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report | CPA.com / AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 |
| IAF-AIFRAUD-2026 | Internal audit and AI-enabled fraud | Internal Audit Foundation and Optro | survey | https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf | 2026 (month not shown; survey ran Q4 2025) |
| ISACA-PULSE-2026 | AI use accelerates while governance and ROI lag (2026 AI Pulse Poll) | ISACA | survey | https://isaca.org/about-us/newsroom/press-releases/2026/ai-use-accelerates-while-governance-and-roi-lag-says-new-isaca-research | 2026-05-05 |
| TRI-FOP-2026 | What the 2026 Future of Professionals report says tax and audit firm leaders should be prioritizing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04-22 |
| DELOITTE-OMNIA-2026 | Deloitte unveils connected agentic intelligence in Deloitte Omnia to advance audit and assurance | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 |
| BDO-ARAQ-2026 | ARAQ (Annual Review of Audit Quality) report | BDO UK | firm | https://www.bdo.co.uk/en-gb/news/2026/araq-report | 2026-07-22 |
| MINDBRIDGE-ARA-2026 | MindBridge advances financial oversight for the agentic era with new platform capabilities | MindBridge (Business Wire release) | vendor | https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/ | 2026-09-22 |
| CASEWARE-VERITY-2026 | From AiDA to agentic: how Caseware's AI has evolved | Caseware | vendor | https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved | 2026-07-28 |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 |
| BOARDAGENDA-FRC-2026 | Auditors warned they remain accountable despite use of AI | Board Agenda | press | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | 2026-03-31 |
| NFRA-CAALLEY-2026 | NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (report of an NFRA staff paper) | CAalley | press | https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement | 2026-07-24 |
| CPIA-ARAQ-2026 | Audit quality remains strong in 2026: consistency is now the aim (commentary on the FRC Annual Review of Audit Quality) | CPIA | press | https://www.cpia.org.uk/news/frc-audit-quality-2026/ | 2026-07-24 |
| ARXIV-UMAR-2026 | Multi-agent framework for audit risk assessment with explicit uncertainty and evidence conflict modeling (abstract page) | arXiv | academic | https://arxiv.org/abs/2606.15640 | 2026-06-14 |
| INDO-ICOBUSS-2025 | Artificial intelligence for fraud risk assessment in auditing (Sari and Noviyanti) | ICOBUSS 2025, Surabaya | academic | https://ojsicobuss.stiesia.ac.id/index.php/icobuss1st/article/download/684/618/1209 | 2025-10 |
| PETERS-2022 | Auditor automation usage and professional skepticism (working paper, abstract page) | Tilburg University | academic | https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/ | 2022-12 |
| COMMERFORD-2022 | Man versus machine: complex estimates and auditor reliance on artificial intelligence (abstract page) | Journal of Accounting Research 60(1) | academic | https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html | 2022-03 |
| FEDYK-2022 | Is artificial intelligence improving the audit process? (abstract page) | Review of Accounting Studies 27(3) | academic | https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html | 2022-09 |
| KOKINA-2025 | Challenges and opportunities for artificial intelligence in auditing: evidence from the field (abstract page) | International Journal of Accounting Information Systems 56 | academic | https://ideas.repec.org/a/eee/ijoais/v56y2025ics1467089525000107.html | 2025 (month not shown) |
| FABIAN-2026 | AI in auditing: new study highlights opportunities and limitations (university summary of a Journal of Information Systems article) | University of Hamburg Business School | academic | https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html | 2026-03-20 |
| HOLMSTROM-2024 | How does generative AI automation affect auditors' motivation and judgment quality? (registered report proposal) | PCAOB / Management Science registered reports conference | academic | https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf | 2024-06 (PDF creation date; the pilot listed 2025) |
| ARXIV-AUDITCOPILOT-2025 | AuditCopilot: leveraging LLMs for fraud detection in double-entry bookkeeping (abstract page) | arXiv | academic | https://arxiv.org/abs/2512.02726 | 2025-12-02 |
| ARXIV-FAB-2026 | FinancialAuditBench: benchmark construction under differential privacy using real-world priors (abstract page) | arXiv | academic | https://arxiv.org/abs/2609.32835 | 2026-09-26 |
| ARXIV-FINAUDITING-2025 | FinAuditing: a financial taxonomy-structured multi-document benchmark for evaluating LLMs (abstract page; v3 revised May 2026) | arXiv | academic | https://arxiv.org/abs/2510.08886 | 2025-10-10 |
| ARXIV-LLMAUDIT-2025 | Automating financial statement audits with large language models (abstract page) | arXiv | academic | https://arxiv.org/abs/2506.17282 | 2025-06-14 |
| PL-YOAA-2025 | Use of large language models in auditing as a tool to reduce information asymmetry and fraud risk (Graczyk, Majek, Modzelewski) | Yearbook of Auditing and Accounting (PANA, Poland) | academic | https://pana.gov.pl/wp-content/uploads/2026/04/6.-YoAA_Use-of-large-language-models-LLMs-in-auditing-as-a-tool-o-reduce-information-asymmetry-and-fraud-risk-in-the-hareholder-management-relationship.pdf | 2025 (posted 2026-04) |
| KU-SYMPOSIUM-2026 | 2026 Deloitte/KU Auditing Symposium agenda (includes the research session "Small Seems Plausible: effects of magnitude appearance on auditors' causal and skeptical judgments of AI-detected correlations") | University of Kansas / Deloitte | conference | https://business.ku.edu/research-and-faculty/accounting/deloitte-ku-auditing-symposium | 2026-05-08 |

**Count by type (58 sources):** regulator 16, standard-setter 7, professional-body 5, survey 4, firm 3, vendor 2, press 7, academic 13, conference 1.

Notes on reading depth. The FRC guidance, IFIAR reports, ISA (UK) 315 and 240, PCAOB Release 2024-007, AS 2110, the AFM and CPA.com reports, ACRA and CAQ papers, and the ICAEW test were read in the sections that bear on this module. Papers marked "abstract page" were not read beyond the abstract. KU-SYMPOSIUM-2026 was read as an agenda only. FRC-AIAUDIT-2025, FRC-GENAINEWS-2026, FRC-SANDBOX-2026, IAASB-EDPAGE-2026, IAASB-TQM-2026, JOFA-AIPA-2026, BDO-ARAQ-2026, COSO-GENAI-2026, ISACA-PULSE-2026, TRI-FOP-2026, FABIAN-2026, ARXIV-AUDITCOPILOT-2025, ARXIV-FAB-2026, ARXIV-FINAUDITING-2025, ARXIV-LLMAUDIT-2025, PL-YOAA-2025 and KU-SYMPOSIUM-2026 support context, frontier signals or routed items rather than use-case outcomes.

---

## 6. Gaps

**Could not reach or verify**

- **ED-520 and ED-330 texts.** The IAASB exposure drafts are login-gated. What this file says about ED-520 (the new requirement on results of risk-assessment analytical procedures, paras 7 and A6–A7) and ED-330 (removal of the always-substantive requirement) comes from the AUASB consultation paper's summary. The landscape file says ED-520 application material describes tools analysing whole populations or unstructured external data to build sharper expectations. That was not verified.
- **International ISA 315 (Revised 2019).** The IAASB PDF was not reachable. The UK adoption (ISA (UK) 315, updated September 2025) was read instead, and its numbering matches the IAASB text. Any difference in wording between the UK and international text was not checked.
- **AS 2110.** pcaobus.org returned HTTP 403, so the standard text was read through a text-mirror fetch of the same page (the route the brief allows). The "as amended" version effective 15 Dec 2026 was not read.
- **AICPA practice aid.** The 51-page document is member-gated. Everything on its content comes from the AICPA release, the Journal of Accountancy, Accounting Today and CFO Dive.
- **NFRA staff paper.** Read only through a press report (CAalley, which cites ET CFO). The paper itself was not located.
- **FRC Annual Review of Audit Quality 2026 (22 Jul 2026).** Read only through a CPIA commentary and a BDO release. The FRC report was not opened, so the planning root causes are second-hand and are not stated to concern AI.
- **CAQ Audit Partner Pulse (Spring 2026), PCAOB inspection observations on AS 2110, and Big Four transparency reports.** Planned searches were not run because the search quota ran out. The landscape's CAQ pulse figures were not re-verified here.
- **FRC thematic review.** Read as an HTML version the FRC says was machine-converted without human verification.

**Not found**

- **Any inspection finding specific to an AI risk-assessment tool.** The only inspection data on risk assessment are the general IFIAR theme counts and the general "tool not used as intended" figure.
- **Independent quality measurement of any AI risk-assessment tool in live audits** (error rates, override rates, parallel-run results). The nearest items are the FRC's observation that no firm quantified quality impact, a single ICAEW chatbot test and one academic prototype.
- **Evidence on AI for budgeting and staffing the engagement.** The landscape lists RSM's AI staffing tool (CAQ-RSM-2026, "Luca Resourcing"). The CAQ blog URL could not be recovered and the post was not re-opened here, so no use case was written. No governance or evidence-angle source on AI in budgeting was found.
- **Evidence on AI in group audit scoping and component risk.** No source reported AI use here. IFIAR's group-audit scoping findings are small (3 in each of 2024 and 2025) and unrelated to AI.
- **Named customers for MindBridge Agentic Risk Assessment** and any firm using a risk assessment agent in production. PwC's Oct 2025 "soon" was not confirmed.

**Corrections and cautions on the landscape and pilot**

- The landscape treats IFIAR-SURVEY-2026 as a snippet. It was opened here and the risk assessment theme counts are reported above.
- The pilot dated the Holmstrom and Peters registered report 2025. The PDF creation date is June 2024.
- The ICAEW article's performance-materiality text is internally inconsistent (60% and 75% both attributed to Claude), so those figures are not reported.
- The Indonesian fraud-risk experiment has a cell-size pattern that conflicts with its stated between-subjects design, so it is weak evidence.
- IAF-AIFRAUD-2026 and KOKINA-2025 carry year-only dates because the pages show no month.
