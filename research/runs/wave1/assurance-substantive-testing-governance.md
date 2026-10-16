# Module deep dive: assurance / substantive-testing, angle: governance & evidence

- **Archetype:** assurance
- **Module:** substantive-testing. Substantive procedures on balances and transactions: journal-entry and fraud testing, substantive analytics, document matching and vouching, confirmations, revenue and inventory testing, support for testing accounting estimates, sampling versus full-population testing, contract review.
- **Angle:** governance & evidence. PCAOB technology-assisted analysis amendments (AS 1105, AS 2301) and staff guidance, IAASB ED-500/ED-520 (and ED-330) and the ISA 240 revision, FRC guidance and worked examples, IFIAR findings, academic studies and benchmarks, surveys with measured adoption.
- **Prepared:** 2026-10-16
- **Method note:** Primary documents were opened with `curl` through the session proxy (`pdftotext` for PDFs). The Federal Register copy stood in for the blocked PCAOB adopting release, and the Japan FSA site mirrored the three IFIAR reports that `ifiar.org` refused. Web search was used for three lookups before the shared budget ran out, so later leads could not be searched. All figures below were read in the source named beside them; where a figure is a vendor or firm claim it is labelled as such.

---

## 1. Summary

**Where the rules stand (16 October 2026).** No regulator or standard-setter read here prohibits AI in substantive testing, and none sets AI-specific requirements for it. What exists is guidance, plus standards that are being rewritten around "technology-assisted" evidence.
- **PCAOB.** The technology-assisted analysis amendments (AS 1105 and AS 2301) apply to audits of fiscal years beginning on or after 15 Dec 2025 (SEC-TAAORDER-2024, section II). They add duties on the reliability of external information the company supplies electronically (AS 1105.10A), on investigating items a tool flags (AS 2301.49-.50), on what counts as a test of details (AS 2301.48) and on achieving each purpose of a multi-purpose procedure (AS 1105.14). The Board says they do not address AI-specific matters or the appropriateness of tools under quality control (PCAOB-TAA-2024). Staff views on generative AI date from July 2024 (PCAOB-GENAI-2024).
- **IAASB.** Exposure drafts of ISA 500, 330 and 520 (5 Aug 2026; comments due 15 Dec 2026) deliberately add no technology requirement. The board judged it premature to write a model for tool inputs, operation and outputs because generative tools may make inputs impossible to evaluate (IAASB-ED500-2026, explanatory memorandum paragraphs 67-68). It offers an appendix of considerations and an automation-bias warning instead (IAASB-ED500-2026, Appendix 3). ISA 240 (Revised) takes effect for periods beginning on or after 15 Dec 2026 (IAASB-ISA240-2025).
- **FRC.** The most operational text read here, with worked substantive examples: a journal-testing example (June 2025) and a contract-review example for revenue testing (March 2026). The FRC says outputs of an AI-enabled procedure need not exactly match the persuasiveness of the procedure replaced, so long as the methodology does not overstate them (FRC-AIAUDIT-2025; FRC-GENAI-2026).

**What inspections and measurement show.**
- Tool-assisted journal-entry testing is the one mature use: 88% of IFIAR members answering in 2024 said they "frequently" saw automated tools in journal entry testing, against 55% for substantive procedures (IFIAR-TTF-2025, p.5). Substantive procedures rose to about 63% in 2025, read from an unlabelled chart (IFIAR-TTF-2026, p.10). These counts cover all tools, not only AI.
- 31% of the 2024 respondents reported findings that a tool was not used as intended (29% in 2023), mostly misread results and thin testing of outliers (IFIAR-TTF-2025, pp.5-6). IFIAR's 2025 survey of inspection findings has no AI-specific category; a new firm-level category, "Resources: technological, intellectual, service providers", shows at least one finding in 9% of inspected member firms (IFIAR-SURVEY-2026, Appendix A).
- No regulator, academic study or firm has published an independent measure of an AI substantive tool's error or override rate in live audits. The FRC found in 2025 that the six largest UK firms did no formal monitoring to quantify the audit-quality impact of automated tools (FRC-ATT-2025, p.20).
- Measured results come from benchmarks on synthetic or anonymised data. On FinancialAuditBench the best agent passed 69.17% of workpaper tasks in one attempt and 44.44% when all eight attempts were required, with large gaps by area (accounts receivable 4.17%, revenue 7.58%, journal-entry risk testing 16.86%, journal-entry completeness 94.51%) (ARXIV-FAB-2026, Tables 1 and 3). Its authors include employees of an AI-native audit venture.
- Firms' own statements are modest on savings: PwC's US assurance transformation leader said in Oct 2026 that time savings are "not that drastic yet" (CFODIVE-PWC-2026).
- Adoption among US small and mid-size firms is low: 11% had an automated solution for substantive analytics and 39% for confirmations (CPACOM-ATR-2025, p.10).

**Use cases.** Sixteen candidates: grade A 1, B 3, C 7, D 5. Journal-entry testing, item selection and evidence matching carry the strongest evidence. Agentic workpaper completion, contract review and substantive analytics rest on announcements, vendor claims or benchmarks.

**Two most important insights.**
1. **The governing question has shifted from "may we use AI?" to "how persuasive is the evidence, and who can show it?"** The FRC says outputs need not exactly match the persuasiveness of the procedure replaced if the methodology does not overstate them (FRC-GENAI-2026, risk of non-compliant methodology). The IAASB declines to require tool-input and tool-output evaluation because it may be impossible for generative tools (IAASB-ED500-2026, paragraph 68). The Board said it was not prescribing the nature, timing or extent of procedures on external information (SEC-TAAORDER-2024, section III). Evidence of how persuasive any tool is rests with each firm, and regulators say firms are not yet measuring it (FRC-ATT-2025, p.20; IFIAR-TTF-2025, p.6).
2. **Data reliability, not model capability, is where regulators see the live weakness.** AFM found auditors often do not verify the relevance and reliability of input data, especially under ineffective IT general controls (AFM-BB-2025, Precondition 2). The PCAOB wrote that duty into AS 1105.10A. The benchmark failures are the same shape: agents vouched to client-prepared documents instead of third-party evidence (ARXIV-FAB-2026, section 6.3). On this evidence (the analyst's inference), whole-population testing moves the audit risk to the completeness and integrity of the population rather than the matching step.

---

## 2. Use cases

Sixteen candidate use cases. Grades: A 1, B 3, C 7, D 5. Entries graded D are labelled "idea".

```yaml
- id: assurance-substantive-testing-01
  title: Whole-population journal-entry testing with analytics and machine-learning anomaly scoring
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'Fraud procedures over journals often filter the ledger with rules-based criteria such as posting times or values, which can miss subtler patterns (FRC-AIAUDIT-2025, p.8). Rules-based filters can also flood the team with exceptions: in one research benchmark a rules-based journal-entry test produced 942 false positives on 5,000 posting IDs (ARXIV-AUDITCOPILOT-2025, Table 1).'
  solution: A tool scores every journal in the general ledger. The FRC's hypothetical example combines an AI model (unsupervised or deep learning) with traditional rules-based routines in one tool, weights them, sets a threshold above which the team must follow up, and shows which features made an item unusual (FRC-AIAUDIT-2025, pp.8-11). Testing the appropriateness of journals is a required fraud response under ISA 240 (Revised), paragraphs 47-48 (IAASB-ED330-2026, A25 and its footnote 26).
  outcomes:
  - lever: quality
    description: IFIAR members seeing automated tools 'frequently' in journal entry testing in audit files
    figure: 88% (2024); 86% (2023); about 86% (2025, read from a chart without data labels)
    measures: Share of IFIAR members answering the annual survey that reported 'frequently observed' use of automated tools and techniques (AI and non-AI) in journal entry testing in GPPC-network audit files; 48 members responded in 2024 and 49 in 2023.
    provenance: independent
    source_ref: IFIAR-TTF-2025
    locator: p.5 table; 2025 value from IFIAR-TTF-2026 p.10 chart
  - lever: quality
    description: All six U.S. global network firms reported tools to identify and select journal entries to PCAOB staff
    figure: 6 of 6 firms (2023 inspection year)
    measures: U.S. global network firms (BDO, Deloitte, EY, Grant Thornton, KPMG, PwC) reporting tools that assist in identifying and selecting journal entries; adoption, not a quality measure.
    provenance: self-reported
    source_ref: PCAOB-TAA-2024
    locator: Economic analysis, current practice of technology-assisted analysis
  prerequisites:
  - Complete and accurate general-ledger data with date, time, poster, description, value and account references (FRC-AIAUDIT-2025, p.11).
  - Methodology and technology teams building the tool together, certification before use, and version control so only the latest approved version runs (FRC-AIAUDIT-2025, pp.10-11).
  - Evaluation of the reliability of electronic information that the company obtained from external sources and gives the auditor, under new AS 1105.10A, effective for fiscal years beginning on or after 15 Dec 2025 (SEC-TAAORDER-2024, section II).
  risks_and_guardrails:
  - 31% of IFIAR members reported findings that an automated tool was not used as intended in the 2024 survey (29% in 2023); the most common technology findings were misinterpreting results and the extent of testing of outliers, alongside insufficient testing of IT general controls (IFIAR-TTF-2025, pp.5-6).
  - An unsupervised model flags only items that are unusual relative to the population, so transactions consistently posted to unusual accounts may not be flagged; the FRC example therefore runs rules-based routines alongside the AI tool (FRC-AIAUDIT-2025, p.10).
  - The PCAOB amendments (AS 2301.49-.50) cover investigation of items identified by auditor-set criteria; as proposed, the investigation considers whether items contradict the risk assessment, indicate a new risk, show a misstatement or control deficiency, or call for changed procedures, and the Board adopted the paragraphs with modifications (PCAOB-TAA-2024, discussion of AS 2301.49-.50).
  - The FRC expects central documentation of the tool and a record on the audit file that the tool was used and why its use criteria were met (FRC-AIAUDIT-2025, pp.11 and 13-14).
  human_checkpoints:
  - The team decides whether use criteria are met (data quality sufficient; fraud risk not already reduced to an acceptably low level by other procedures) and documents it (FRC-AIAUDIT-2025, p.11).
  - The team follows up each high-risk item, considers why it was flagged, and stays alert to signs that the tool is systematically flawed for the engagement (FRC-AIAUDIT-2025, p.11).
  role_evolution: In the FRC example, central technical and methodology teams own certification, calibration and documentation, while engagement teams decide when to use the tool and interpret and follow up its output (FRC-AIAUDIT-2025, pp.9-11).
  evidence_grade: B
  sources:
  - ref: FRC-AIAUDIT-2025
    title: 'AI in Audit: illustrative example and documentation guidance'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/AI_in_Audit.pdf
    date: '2025-06-26'
    access: full
    locator: Illustrative example pp.8-11; documentation guidance pp.13-14
  - ref: IFIAR-TTF-2025
    title: 'Use of technology in audits: observations, risks and further evolution'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf
    date: '2025-03-27'
    access: full
    locator: p.5 table of frequency of ATT observation; pp.5-6 inspection findings
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf
    date: '2026-04-20'
    access: full
    locator: p.10 trend chart (2023-2025)
  - ref: PCAOB-TAA-2024
    title: Notice of Filing of Proposed Rules on Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 54922; carries the Board's adopting-release text, Release 2024-007)
    publisher: PCAOB; SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14488.pdf
    date: '2024-07-02'
    access: full
    locator: Economic analysis (current practice); discussion of AS 2301.49-.50
  - ref: SEC-TAAORDER-2024
    title: Order Granting Approval of Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 68218)
    publisher: SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-08-23/pdf/2024-18986.pdf
    date: '2024-08-23'
    access: full
    locator: Section II.A-B (summary of amendments; effective date)
  - ref: IAASB-ED330-2026
    title: 'Exposure Draft: Proposed ISA 330 (Revised), The Auditor''s Responses to Assessed Risks, with explanatory memorandum'
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-330-Exposure-Draft.pdf
    date: '2026-08-05'
    access: full
    locator: A25 and footnote 26
  - ref: ARXIV-AUDITCOPILOT-2025
    title: 'AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping (Kadir, Vasu, Nair, Sonntag; DFKI)'
    publisher: arXiv 2512.02726
    type: academic
    url: https://arxiv.org/abs/2512.02726
    date: '2025-12-02'
    access: full
    locator: Section 4, Table 1 (JET false positives)
  last_reviewed: '2026-10-16'
  notes: The IFIAR frequency covers all automated tools including non-AI analytics, so it shows how mature tool-assisted journal-entry testing is, not how mature AI is. The FRC example is hypothetical (XYZ LLP, ABC PLC); its remark that the final tool usually flagged similar or smaller numbers of high-risk transactions than the earlier approach is a design observation, not a measurement. No published parallel-run or error-rate result for an AI journal-entry tool at a named firm was found.
- id: assurance-substantive-testing-02
  title: Language-model anomaly detection layered on journal-entry tests (idea, research stage)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Auditors rely on journal entry tests to find anomalies, but rule-based methods generate many false positives and struggle with subtle irregularities (ARXIV-AUDITCOPILOT-2025, abstract).
  solution: Researchers prompt large language models with each ledger record plus dataset statistics and an Isolation Forest hint, and ask for a yes/no anomaly flag with a natural-language explanation; the authors prefer open-weight models because ledger data is confidential (ARXIV-AUDITCOPILOT-2025, sections 2-3).
  outcomes:
  - lever: quality
    description: 'Synthetic ledger: false positives for the best language model versus rules-based journal entry testing (JET)'
    figure: 'Mistral-8B: 48 true positives, 12 false positives, 2 false negatives; JET: 50 true positives, 942 false positives, 0 false negatives; GPT-5-mini: 50 true positives, 466 false positives'
    measures: Counts of ledger posting IDs flagged against simulator-defined labels in a random subset of 5,000 posting IDs with 50 seeded anomalies. The paper's printed precision and recall columns (e.g. JET precision 0.53) do not match these counts and appear to be averaged over both classes.
    provenance: independent
    source_ref: ARXIV-AUDITCOPILOT-2025
    locator: Section 4, Table 1
  - lever: quality
    description: 'Real anonymised ledger: Gemma-7B with the full prompt versus Isolation Forest, scored against pseudo-labels'
    figure: 'Gemma-7B: 256 true positives, 32 false positives, 73 false negatives; Isolation Forest: 315 true positives, 719 false positives, 14 false negatives; removing the Isolation Forest hint raised Gemma-7B false positives from 32 to 1,973'
    measures: Counts of transaction records flagged against 329 pseudo-labelled anomalies. The pseudo-labels were made by applying journal entry testing rules to the ledger, so rules-based JET is the reference, not a competitor, on this dataset.
    provenance: independent
    source_ref: ARXIV-AUDITCOPILOT-2025
    locator: Section 3 (labels); Section 4, Table 2
  prerequisites:
  - Structured ledger fields (amounts, accounts, users, dates) plus free-text memo fields, with global statistics and a classical anomaly-detector score added to the prompt (ARXIV-AUDITCOPILOT-2025, section 2).
  - Certification and testing of the model and an explainability approach suited to how the output is used (FRC-AIAUDIT-2025, p.9).
  risks_and_guardrails:
  - 'The authors list limits: one anonymised ledger plus a synthetic benchmark, pseudo-labels that may inherit rule-based biases, prompt sensitivity, explanations that may not reflect the decision boundary, and risks of hallucination, automation bias, prompt injection through free-text fields and non-reproducibility (ARXIV-AUDITCOPILOT-2025, Limitations).'
  - The FRC example notes that a model's explanations can be approximate or post hoc and still be appropriate depending on use (FRC-AIAUDIT-2025, p.14).
  human_checkpoints:
  - Auditors review flagged entries together with the model's explanation (ARXIV-AUDITCOPILOT-2025, abstract).
  role_evolution: The authors describe human auditors collaborating with foundation models; no change in roles is studied (ARXIV-AUDITCOPILOT-2025, abstract).
  evidence_grade: D
  sources:
  - ref: ARXIV-AUDITCOPILOT-2025
    title: 'AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping (Kadir, Vasu, Nair, Sonntag; DFKI)'
    publisher: arXiv 2512.02726
    type: academic
    url: https://arxiv.org/abs/2512.02726
    date: '2025-12-02'
    access: full
    locator: Abstract; sections 2-4; Limitations
  - ref: FRC-AIAUDIT-2025
    title: 'AI in Audit: illustrative example and documentation guidance'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/AI_in_Audit.pdf
    date: '2025-06-26'
    access: full
    locator: pp.9 and 14 (explainability)
  last_reviewed: '2026-10-16'
  notes: 'Labelled idea: a research prototype with measured benchmark results but no deployment found. Authors are at DFKI (Germany); the industry partner is not named. The paper''s Table 1 is internally inconsistent (JET lists recall 0.90 yet 0 false negatives), so only counts are reported here.'
- id: assurance-substantive-testing-03
  title: Evidence matching and automated vouching of test-of-details samples to supporting documents and bank data
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Matching each sampled item to invoices, contracts, bank records and other support is slow manual work; a Thomson Reuters customer describes it as about two full days per engagement before the tool (TR-AGENTIC-2025, Audit Intelligence Test section).
  solution: Tools extract data from varied supporting documents, match each sampled item to evidence, keep an evidence trail and flag gaps. PwC describes Evidence Match as an agent-led module that extracts and matches validating evidence against documents for areas such as cash, receivables and payables (PWC-AT-2025). Thomson Reuters' Audit Intelligence Test traces transactions to banking activity and can match one payment to several invoices (TR-AGENTIC-2025). KPMG lists expense vouching among agents deployed in Clara (KPMG-CLARA-2025).
  outcomes:
  - lever: speed
    description: One Thomson Reuters customer's time to organise client materials and run tests, before and after Audit Intelligence Test
    figure: about 16 hours (two full days) to five or six hours per engagement
    measures: One practitioner's own estimate, quoted in a vendor press release, of hours per engagement; no sample size, scope or quality measure is given.
    provenance: vendor-published
    source_ref: TR-AGENTIC-2025
    locator: Audit Intelligence Test section (Oberlander Financial Services PLLC quote)
  - lever: quality
    description: 'Five general-purpose chat models on document-based audit tests (adjacent evidence: tests included internal audit and anti-corruption reviews)'
    figure: 74-96% correct with basic prompts; 76-100% correct after prompt optimisation
    measures: Correct pass/fail answers divided by 167 assigned document samples across eight audit-type tests (sales and cost documents in several languages from one capital group), with the audit team's result as ground truth; samples a model rejected for file size or format count as not answered; the optimised prompts were written from phase-one errors on the same samples.
    provenance: independent
    source_ref: GRACZYK-2025
    locator: Tables 3 and 5
  prerequisites:
  - 'Access to client systems and usable client data: 53% of surveyed US firms name lack of access to client information and systems, and 60% poor-quality client data, among top blockers (CPACOM-ATR-2025, barriers section).'
  - Evaluation of the reliability of external information held by the company in electronic form (AS 1105.10A) (SEC-TAAORDER-2024, section II).
  - 'Ingestion of many document types: PwC says the tool had to handle about 20 different kinds of documents (PWC-AT-2025).'
  risks_and_guardrails:
  - IRBA warned in Sept 2024 that generative tools can produce realistic false evidence and fabricated working papers, and recommended procedures to verify the authenticity of evidence (IRBA-AI-2024, p.1).
  - AFM reported that auditors do not always perform adequate procedures to verify the relevance and reliability of data fed to tools and often give insufficient attention to ineffective general IT controls (AFM-BB-2025, Precondition 2).
  - In FinancialAuditBench failure analysis, agents vouched receivables to a client-prepared cash receipts report instead of a bank statement, and sometimes analysed only the most obvious source document (ARXIV-FAB-2026, section 6.3).
  - In the Polish study, ChatGPT passed 19 defective samples out of 167 with basic prompts, and models ignored alternative evidence when a signature was missing (GRACZYK-2025, section 4).
  human_checkpoints:
  - PwC says each match carries an evidence trail, which a reviewer can check against the documents (PWC-AT-2025).
  - Caseware says nothing is written into the engagement until a human reviews, accepts, edits or rejects it, and its suggestions are citation-backed (CASEWARE-VERITY-2026).
  role_evolution: PwC's US assurance transformation leader said the firm is hiring engineers it would not previously have hired into assurance and looking for dual-track CPA and data-science candidates (PWC-AT-2025).
  evidence_grade: A
  sources:
  - ref: TR-AGENTIC-2025
    title: Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows (press release)
    publisher: Thomson Reuters
    type: vendor
    url: https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows
    date: '2025-11-05'
    access: full
    locator: Audit Intelligence Test section
  - ref: PWC-AT-2025
    title: PwC expects end-to-end AI audit automation within 2026 (Accounting Today)
    publisher: Accounting Today
    type: press
    url: https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026
    date: '2025-10-28'
    access: full
    locator: Evidence Match paragraphs; hiring remarks
  - ref: KPMG-CLARA-2025
    title: KPMG advances AI integration in KPMG Clara smart audit platform (press release)
    publisher: KPMG International
    type: firm
    url: https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html
    date: '2025-04-22'
    access: full
    locator: Paragraph on AI agents deployed in this release
  - ref: GRACZYK-2025
    title: Use of large language models (LLMs) in auditing as a tool to reduce information asymmetry and fraud risk in the shareholder-management relationship (Graczyk, Majek, Modzelewski)
    publisher: Yearbook of Auditing and Accounting 2025
    type: academic
    url: https://pana.gov.pl/wp-content/uploads/2026/04/6.-YoAA_Use-of-large-language-models-LLMs-in-auditing-as-a-tool-o-reduce-information-asymmetry-and-fraud-risk-in-the-hareholder-management-relationship.pdf
    date: '2025'
    access: full
    locator: Abstract; sections 3-5, Tables 3, 5, 6
  - ref: ARXIV-FAB-2026
    title: 'FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors (Huang, Babu et al.; UIUC, Stanford, Modus Audit Inc.)'
    publisher: arXiv 2609.32835
    type: academic
    url: https://arxiv.org/abs/2609.32835
    date: '2026-09-26'
    access: full
    locator: Section 6.3 failure analysis
  - ref: AFM-BB-2025
    title: 12 Building blocks for controlled use of auditing tools
    publisher: AFM (Netherlands)
    type: regulator
    url: https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf
    date: 2025-12
    access: full
    locator: Precondition 2, building blocks 4-6
  - ref: IRBA-AI-2024
    title: Artificial Intelligence Audit Risks Mitigation Update (communique)
    publisher: IRBA (South Africa)
    type: regulator
    url: https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf
    date: '2024-09-19'
    access: full
    locator: p.1
  - ref: CPACOM-ATR-2025
    title: 2025 Audit Transformation Report (Audit Benchmark Survey, 54 US firms with complete data)
    publisher: CPA.com / AICPA
    type: survey
    url: https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf
    date: 2025-12
    access: full
    locator: Barriers to overcome (pp.7-8)
  - ref: SEC-TAAORDER-2024
    title: Order Granting Approval of Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 68218)
    publisher: SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-08-23/pdf/2024-18986.pdf
    date: '2024-08-23'
    access: full
    locator: Section II.A-B; section III on AS 1105.10A
  - ref: CASEWARE-VERITY-2026
    title: 'From AiDA to agentic: How Caseware''s AI has evolved (Caseware Verity)'
    publisher: Caseware
    type: vendor
    url: https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved
    date: '2026-07-28'
    access: full
    locator: Section on human review of suggestions
  last_reviewed: '2026-10-16'
  notes: Grade A rests on one practitioner figure in a vendor release. No independent measure of match accuracy in live audits was found. The Polish study uses general chat models, not audit products, and some of its tests were not external-audit procedures, so it is adjacent evidence.
- id: assurance-substantive-testing-04
  title: Full-population matching of transactions to independent third-party data in place of sample-based tests of details
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: A practitioner commentary argues that sampling was the practical limit of what people could test in the hours an engagement allows (CPAPA-FULLPOP-2026).
  solution: PwC Australia said on 28 Oct 2025 that it was rolling out an 'AI-native' audit platform as part of a global pilot, with agents that test balances and controls on full population sets, including against trusted third-party data (PWCAU-2025). The IAASB's exposure draft gives the example of agreeing all sales invoices of an online retailer to independent carrier shipping data (IAASB-ED500-2026, Appendix 2, paragraph 3).
  outcomes:
  - lever: speed
    description: PwC's US assurance transformation leader on time savings after one year of enterprise generative AI tools in assurance
    figure: none published; described as 'not that drastic yet'
    measures: Qualitative statement about the busy-season time shift, covering PwC's firm-wide generative AI tools rather than full-population testing specifically.
    provenance: self-reported
    source_ref: CFODIVE-PWC-2026
    locator: Interview section on time savings
  prerequisites:
  - A complete population and reliable data, with procedures to verify relevance and reliability of the information used (AFM-BB-2025, building blocks 4-6; SEC-TAAORDER-2024, section II).
  - Independent third-party data to reconcile against, such as carrier tracking or bank activity (IAASB-ED500-2026, Appendix 2, paragraph 3; TR-AGENTIC-2025).
  risks_and_guardrails:
  - The FRC says AI-enabled procedures may produce outputs on whole populations but insights on each item may be less conclusive than in traditional substantive work; outputs need not match the persuasiveness of the procedure they replace if the methodology does not overstate it (FRC-GENAI-2026, risk of non-compliant methodology).
  - Under ED-500, when tools analyse a whole population to find items with risk characteristics, testing those items gives evidence only about them and misstatements found cannot be projected to the rest (IAASB-ED500-2026, Appendix 2, paragraph 7).
  - PCAOB commenters asked whether sampling may be applied to items identified for investigation and whether evidence is sufficient when whole-population analysis identifies nothing; the Board described the final requirements as principles-based and applicable to all means of selecting items (PCAOB-TAA-2024, discussion of AS 2301.49-.50).
  - A practitioner commentary warns that marketing 'we test everything' widens the expectation gap and recommends running automation in shadow mode on completed engagements, then cutting over gradually (CPAPA-FULLPOP-2026).
  - IFIAR suggests benchmarking exercises that compare technology-driven results with traditional methods (IFIAR-TTF-2026, p.9).
  human_checkpoints:
  - Investigation of every item the analysis identifies, with auditor judgement on what a finding means (PCAOB-TAA-2024, discussion of AS 2301.49-.50).
  - A stand-back review by the engagement team of whether the tool achieved the overall objective (IFIAR-TTF-2025, p.8).
  role_evolution: PwC Australia says AI moves auditors' time from data gathering and documentation toward analysis, and it expects 1,600 auditors to use the platform (PWCAU-2025); an RSM partner cautions that over-reliance could lower audit quality (PWCAU-2025).
  evidence_grade: B
  sources:
  - ref: PWCAU-2025
    title: PwC Australia rolls out pilot program for AI-assisted full audits (Accounting Times)
    publisher: Accounting Times
    type: press
    url: https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits
    date: '2025-10-28'
    access: full
    locator: 'Whole article (pilot scope: five clients initially, all clients by 2028)'
  - ref: IAASB-ED500-2026
    title: 'Exposure Draft: Proposed ISA 500 (Revised), Audit Evidence, with explanatory memorandum'
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf
    date: '2026-08-05'
    access: full
    locator: Appendix 2, paragraphs 3 (sales-invoice example) and 6-8
  - ref: FRC-GENAI-2026
    title: 'Generative and Agentic AI Guidance: risks, mitigations and illustrative examples'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
    date: '2026-03-30'
    access: full
    locator: 'Risks: risk of non-compliant methodology'
  - ref: PCAOB-TAA-2024
    title: Notice of Filing of Proposed Rules on Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 54922; carries the Board's adopting-release text, Release 2024-007)
    publisher: PCAOB; SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14488.pdf
    date: '2024-07-02'
    access: full
    locator: Discussion of AS 2301.48-.50
  - ref: CPAPA-FULLPOP-2026
    title: 'Testing Every Transaction Changes the Audit: Here''s What Firms Should Know Before They Sell It (Tunde Adewole, CEO of Ledgerline)'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/
    date: '2026-10-15'
    access: full
    locator: Sections on what full-population testing changes, the trap, and rollout
  - ref: CFODIVE-PWC-2026
    title: PwC exec ushers in AI-assisted audits, awaits bigger time savings (CFO Dive)
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/
    date: '2026-10-07'
    access: full
    locator: Time-savings passage
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf
    date: '2026-04-20'
    access: full
    locator: p.9 emerging practices
  - ref: IFIAR-TTF-2025
    title: 'Use of technology in audits: observations, risks and further evolution'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf
    date: '2025-03-27'
    access: full
    locator: p.8
  - ref: AFM-BB-2025
    title: 12 Building blocks for controlled use of auditing tools
    publisher: AFM (Netherlands)
    type: regulator
    url: https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf
    date: 2025-12
    access: full
    locator: Building blocks 4-6
  - ref: SEC-TAAORDER-2024
    title: Order Granting Approval of Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 68218)
    publisher: SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-08-23/pdf/2024-18986.pdf
    date: '2024-08-23'
    access: full
    locator: Section II
  - ref: TR-AGENTIC-2025
    title: Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows (press release)
    publisher: Thomson Reuters
    type: vendor
    url: https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows
    date: '2025-11-05'
    access: full
    locator: Audit Intelligence Test section
  last_reviewed: '2026-10-16'
  notes: PwC Australia's description is a press statement; no results, error rates or inspection outcome have been published. The ED-500 example is application material in an exposure draft, not a deployment. Grade B reflects a named pilot without published measurements.
- id: assurance-substantive-testing-05
  title: LLM contract review to target or support revenue-recognition testing
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: When auditing revenue, auditors often test a sample of contracts; the sample selection is usually risk-based and the FRC example assumes AI can improve how well it targets contracts at higher risk of misstatement (FRC-GENAI-2026, illustrative example 2).
  solution: In the FRC's hypothetical tool, an LLM extracts risk indicators from each contract, separate prompts evaluate the judgemental ones (such as whether performance obligations are distinct or variable consideration is constrained), a computation step scores each contract, and contracts above a threshold form the sample the auditor tests; the auditor sees which indicators were present (FRC-GENAI-2026, illustrative example 2). Thomson Reuters reports an early-adopter programme for CoCounsel Document Analysis, which lets auditors delegate client document review (TR-AGENTIC-2025).
  outcomes:
  - lever: speed
    description: Thomson Reuters early adopters on preparation and workpaper review with CoCounsel Document Analysis
    figure: up to 70% faster
    measures: Vendor-stated speed-up in preparation and workpaper review across early-adopter customers; no sample size, baseline or contract-review-specific measure is given.
    provenance: vendor-published
    source_ref: TR-AGENTIC-2025
    locator: CoCounsel Document Analysis paragraph
  - lever: quality
    description: 'Contract-verification test in the Polish study: models misread automatic-renewal clauses with basic prompts'
    figure: ChatGPT erred in 5 cases; Gemini and Claude erred or over-flagged in 3 cases each
    measures: Cases in test one (contract validity) where model results differed from the audit team's, within a 167-sample study; counts are as described in the paper's text.
    provenance: independent
    source_ref: GRACZYK-2025
    locator: Section 4, error analysis (contract clauses)
  prerequisites:
  - A model chosen for audit and accounting knowledge, sector and language coverage, and a context window large enough for whole contracts, with a token budget that avoids omitted content (FRC-GENAI-2026, illustrative example 2).
  - Contracts chunked and indexed with stable identifiers so the tool can cite the source of each extract (FRC-GENAI-2026, illustrative example 2).
  - Certification on contracts from different sectors, with differing terminology, with each risk indicator present, and with deliberately ambiguous cases to test escalation (FRC-GENAI-2026, illustrative example 2).
  risks_and_guardrails:
  - 'The FRC lists four deficient-output risks for this design: an unfit extraction prompt, failure to extract all and only the specified content, misevaluation of extracted content, and inappropriate indicator weights or score threshold (FRC-GENAI-2026, illustrative example 2).'
  - 'An auditor may misread a tool''s lease-clause summary as a complete summary of the contracts and skip other procedures (FRC-GENAI-2026, risks: misinterpretation of output).'
  - The Polish study found models over-cautious or wrong on automatic-renewal clauses and, for ChatGPT, treating partial-period coverage as valid (GRACZYK-2025, section 4).
  human_checkpoints:
  - The tool escalates to a human at extraction and evaluation steps when uncertain (FRC-GENAI-2026, illustrative example 2).
  - The auditor records on the file that an AI tool selected the sample, the criteria met for its use, the contracts selected, the indicators and the testing performed (FRC-GENAI-2026, illustrative example 2).
  role_evolution: The FRC example has the auditor testing the contracts the tool selects, supported by training on when the tool is appropriate; technical audit and accounting teams set indicator weights and thresholds (FRC-GENAI-2026, illustrative example 2).
  evidence_grade: C
  sources:
  - ref: FRC-GENAI-2026
    title: 'Generative and Agentic AI Guidance: risks, mitigations and illustrative examples'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
    date: '2026-03-30'
    access: full
    locator: Risks (misinterpretation); illustrative example 2, pp.49-56
  - ref: TR-AGENTIC-2025
    title: Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows (press release)
    publisher: Thomson Reuters
    type: vendor
    url: https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows
    date: '2025-11-05'
    access: full
    locator: CoCounsel Document Analysis paragraph
  - ref: GRACZYK-2025
    title: Use of large language models (LLMs) in auditing as a tool to reduce information asymmetry and fraud risk in the shareholder-management relationship (Graczyk, Majek, Modzelewski)
    publisher: Yearbook of Auditing and Accounting 2025
    type: academic
    url: https://pana.gov.pl/wp-content/uploads/2026/04/6.-YoAA_Use-of-large-language-models-LLMs-in-auditing-as-a-tool-o-reduce-information-asymmetry-and-fraud-risk-in-the-hareholder-management-relationship.pdf
    date: '2025'
    access: full
    locator: Section 4 error analysis
  - ref: CPACOM-ATR-2025
    title: 2025 Audit Transformation Report (Audit Benchmark Survey, 54 US firms with complete data)
    publisher: CPA.com / AICPA
    type: survey
    url: https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf
    date: 2025-12
    access: full
    locator: AI and audit section (firms use AI to analyse contracts, leases and debt agreements)
  last_reviewed: '2026-10-16'
  notes: The FRC example is hypothetical and the tool targets sample selection; it does not replace testing. Vendor speed figure is a claim; the Polish evidence is adjacent (general chat models, not audit products). CPA.com's survey says some firms use AI to analyse client contracts, leases and debt agreements without naming them.
- id: assurance-substantive-testing-06
  title: Electronic confirmations and direct access to external bank and counterparty data
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - transaction-processing
  - review-assurance
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: The PCAOB's confirmation standard was written over 30 years ago and changed little after 2003, while electronic communication and third-party intermediaries have spread; the Board also cites continued inspection findings and enforcement actions on auditors' control of the confirmation process (PCAOB-CONFIRM-2023, background).
  solution: Auditors use electronic platforms or direct access to information maintained by a knowledgeable external source instead of paper requests. The PCAOB's new principles-based standard applies to paper and electronic methods and requires confirming cash held by third parties or otherwise obtaining evidence by directly accessing external information (PCAOB-CONFIRM-2023, summary). ED-500 lists external confirmation through an electronic platform as an example of a technological tool (IAASB-ED500-2026, Appendix 3, paragraph 3).
  outcomes:
  - lever: capacity
    description: US firms with an automated solution for confirmations
    figure: 39%
    measures: Share of the 54 US firms with complete data in the 2025 Audit Benchmark Survey that answered that the firm has an automated solution for confirmations (the survey was marketed to firms and is not a random sample).
    provenance: independent
    source_ref: CPACOM-ATR-2025
    locator: p.10 chart
  prerequisites:
  - Controls over how requests are sent and responses received so the auditor keeps control of the process (PCAOB-CONFIRM-2023, background).
  - A platform or data connection to the confirming party that the auditor can evaluate for reliability (IAASB-ED500-2026, Appendix 3).
  risks_and_guardrails:
  - The PCAOB notes inspection findings and enforcement cases where auditors failed to maintain control over the confirmation process (PCAOB-CONFIRM-2023, background).
  - The Board determined that the new standard takes effect for fiscal years ending on or after 15 June 2025, subject to SEC approval; this run did not confirm the approval (PCAOB-CONFIRM-2023, effective date).
  human_checkpoints:
  - The new standard stresses the auditor's responsibility for obtaining relevant and reliable audit evidence through the confirmation process, and says negative confirmation requests alone do not provide sufficient appropriate evidence (PCAOB-CONFIRM-2023, summary).
  role_evolution: The surveyed firms do not describe role changes for confirmations; the CPA.com report notes staff training is the most cited blocker to audit transformation (CPACOM-ATR-2025, barriers section).
  evidence_grade: C
  sources:
  - ref: PCAOB-CONFIRM-2023
    title: Notice of Filing of Proposed Rules on the Auditor's Use of Confirmation, and Other Amendments to Related PCAOB Standards (Federal Register, Board action of 28 Sep 2023)
    publisher: PCAOB; SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2023-10-17/pdf/2023-22491.pdf
    date: '2023-10-17'
    access: full
    locator: Background; summary of new standard; effective date
  - ref: CPACOM-ATR-2025
    title: 2025 Audit Transformation Report (Audit Benchmark Survey, 54 US firms with complete data)
    publisher: CPA.com / AICPA
    type: survey
    url: https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf
    date: 2025-12
    access: full
    locator: p.10 chart of automated solutions
  - ref: IAASB-ED500-2026
    title: 'Exposure Draft: Proposed ISA 500 (Revised), Audit Evidence, with explanatory memorandum'
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf
    date: '2026-08-05'
    access: full
    locator: Appendix 3, paragraph 3 table
  last_reviewed: '2026-10-16'
  notes: Confirmation automation is mostly platform and data-connection work rather than AI; the module description includes it, so it is kept. The survey does not name firms, so no named deployment was confirmed here; vendor material on confirmation platforms was not opened in this run.
- id: assurance-substantive-testing-07
  title: Substantive analytical procedures with technology-built expectations from disaggregated and unstructured data
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Standards say substantive analytical procedures alone are unlikely to be sufficient and that tests of details are required for significant risks, so whether a technology-assisted procedure is a test of details or an analytical procedure matters; practice has diverged on how the categories apply (PCAOB-TAA-2024, discussion of AS 2301.48; IAASB-EDOVERALL-2026, paragraph 37).
  solution: ED-520's application material says tools may turn unstructured industry reports into structured information, or model the relationship between revenue and cost of sales with seasonal, price and volume variables, to build a more precise expectation (IAASB-ED520-2026, A20). The exposure drafts also recognise whole-population analytical procedures at a disaggregated level as a risk assessment aid (IAASB-EDOVERALL-2026, paragraph 39).
  outcomes:
  - lever: quality
    description: US firms with an automated solution for substantive analytics
    figure: 11% (and 89% not currently using technology to enable substantive analytics)
    measures: Share of the 54 US firms with complete data in the 2025 Audit Benchmark Survey with an automated solution for substantive analytics (11%); the report separately states 89% of firms are not currently leveraging technology to enable substantive analytics.
    provenance: independent
    source_ref: CPACOM-ATR-2025
    locator: p.10 chart; p.19
  prerequisites:
  - Disaggregated, reliable data and the ability to access client data; firms using analytics still cite client data access as a difficulty (CPACOM-ATR-2025, p.19).
  - 'Updated definitions: ED-330 and ED-520 propose new definitions of tests of details and substantive analytical procedures (IAASB-EDOVERALL-2026, paragraphs 37 and 40).'
  risks_and_guardrails:
  - Firm commenters on the PCAOB amendments preferred not to compare tests of details with analytical procedures, and the Board's separate substantive analytical procedures project was still pending when the amendments were approved (SEC-TAAORDER-2024, footnote 19; PCAOB-TAA-2024, discussion of AS 2301.48).
  - In the 2025 IFIAR survey, 15 of 331 inspected listed PIE audits had a finding on substantive analytical procedures (5%); the figure is a baseline and says nothing about AI (IFIAR-SURVEY-2026, Table B.2).
  human_checkpoints:
  - Auditor evaluates whether the expectation is precise enough and investigates differences, obtaining evidence for management's explanations (IAASB-ED520-2026, A21-A23).
  role_evolution: Not described by the standard-setters; CPA.com's respondents who use technology for substantive analytics mention visualisation, full-population testing, AI anomaly detection and ratio analysis without naming firms (CPACOM-ATR-2025, p.19).
  evidence_grade: C
  sources:
  - ref: IAASB-ED520-2026
    title: 'Exposure Draft: Proposed ISA 520 (Revised), Analytical Procedures, with explanatory memorandum'
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-520-Exposure-Draft.pdf
    date: '2026-08-05'
    access: full
    locator: A20-A23
  - ref: IAASB-EDOVERALL-2026
    title: Explanatory Memorandum to the Exposure Drafts for the Audit Evidence and Risk Response Project (overall)
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-Overall-Project-Exposure-Draft.pdf
    date: '2026-08-05'
    access: full
    locator: Paragraphs 37, 39-40
  - ref: PCAOB-TAA-2024
    title: Notice of Filing of Proposed Rules on Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 54922; carries the Board's adopting-release text, Release 2024-007)
    publisher: PCAOB; SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14488.pdf
    date: '2024-07-02'
    access: full
    locator: Discussion of AS 2301.48 (test of details vs analytical procedures)
  - ref: SEC-TAAORDER-2024
    title: Order Granting Approval of Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 68218)
    publisher: SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-08-23/pdf/2024-18986.pdf
    date: '2024-08-23'
    access: full
    locator: Section III; footnote 19
  - ref: CPACOM-ATR-2025
    title: 2025 Audit Transformation Report (Audit Benchmark Survey, 54 US firms with complete data)
    publisher: CPA.com / AICPA
    type: survey
    url: https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf
    date: 2025-12
    access: full
    locator: p.10 chart; p.19
  - ref: IFIAR-SURVEY-2026
    title: Survey of Inspection Findings 2025 (14th annual survey)
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf
    date: '2026-04-01'
    access: full
    locator: Appendix B, Table B.2
  last_reviewed: '2026-10-16'
  notes: Evidence is survey adoption and standard-setting application material; no named firm case or measured result was found. The two CPA.com figures come from different questions.
- id: assurance-substantive-testing-08
  title: Technology-assisted selection of items for testing (all items, specific items, or a sample)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Existing PCAOB standards specify responsibilities for audit samples but not for items identified when testing specific items or all items in a population, and the Board's research found auditors using technology to identify such items (PCAOB-TAA-2024, background).
  solution: 'Tools identify and select journal entries, specific high-risk items or samples for testing; the amended AS 2301 applies its test-of-details and investigation requirements to all means of selecting items: all items, specific items, or audit sampling (PCAOB-TAA-2024, discussion of AS 2301.48-.50).'
  outcomes:
  - lever: capacity
    description: All six U.S. global network firms reported tools to select samples for testing; average tools per engagement team rose from about 13 to about 18
    figure: 6 of 6 firms; about 13 to about 18 tools (about 38%) between 2018 and 2023
    measures: U.S. global network firms reporting tools that assist in selecting samples; average number of tools used by engagement teams per firm as reported to the PCAOB, 2018 versus 2023. About 90% of the tools were used for visualisation, summarisation, tabulation or modelling, and under 7% used AI, blockchain or RPA.
    provenance: self-reported
    source_ref: PCAOB-TAA-2024
    locator: Economic analysis, current practice
  prerequisites:
  - Clear criteria for item selection tied to the objective of the procedure (PCAOB-TAA-2024, discussion of AS 2301.48).
  - Reliable data and, where relevant, controls over the information used (SEC-TAAORDER-2024, section II).
  risks_and_guardrails:
  - Selecting specific items is not audit sampling and results cannot be projected to the rest of the population (IAASB-ED500-2026, Appendix 2, paragraphs 6-7).
  - IFIAR members' most common technology findings include insufficient extent of testing of outliers (IFIAR-TTF-2025, pp.5-6).
  - In the 2025 IFIAR survey, 46 of 420 inspected listed PIE audits where audit sampling was inspected had a finding (11%) (IFIAR-SURVEY-2026, Table B.2).
  human_checkpoints:
  - Auditor applies procedures appropriate to the objective to each selected item and investigates identified items (PCAOB-TAA-2024, discussion of AS 2301.48-.50).
  role_evolution: The PCAOB's data show a growing toolset per firm but do not describe role changes (PCAOB-TAA-2024, economic analysis).
  evidence_grade: B
  sources:
  - ref: PCAOB-TAA-2024
    title: Notice of Filing of Proposed Rules on Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 54922; carries the Board's adopting-release text, Release 2024-007)
    publisher: PCAOB; SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14488.pdf
    date: '2024-07-02'
    access: full
    locator: Background; discussion of AS 2301.48-.50; economic analysis
  - ref: SEC-TAAORDER-2024
    title: Order Granting Approval of Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 68218)
    publisher: SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-08-23/pdf/2024-18986.pdf
    date: '2024-08-23'
    access: full
    locator: Section II
  - ref: IAASB-ED500-2026
    title: 'Exposure Draft: Proposed ISA 500 (Revised), Audit Evidence, with explanatory memorandum'
    publisher: IAASB
    type: standard-setter
    url: https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf
    date: '2026-08-05'
    access: full
    locator: Appendix 2, paragraphs 1-9
  - ref: IFIAR-TTF-2025
    title: 'Use of technology in audits: observations, risks and further evolution'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf
    date: '2025-03-27'
    access: full
    locator: pp.5-6
  - ref: IFIAR-SURVEY-2026
    title: Survey of Inspection Findings 2025 (14th annual survey)
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf
    date: '2026-04-01'
    access: full
    locator: Appendix B, Table B.2
  last_reviewed: '2026-10-16'
  notes: Named firms are the six U.S. global networks as listed by the PCAOB; the data are firm-reported to the regulator for the 2023 inspection year and mostly describe non-AI analytics.
- id: assurance-substantive-testing-09
  title: Agentic completion of staff-level substantive workpapers (vouching, reconciliation, calculation, documentation)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Staff-level fieldwork on balances such as cash, payables, receivables, revenue and journal entries takes hours per workpaper; a benchmark team estimated 2-12 hours of manual completion per workpaper (ARXIV-FAB-2026, Table 3, excluding senior review and rework).
  solution: Agents receive the audit plan, assessed risks, supporting documents and a workpaper template, then perform the procedures and write the workpaper. Deloitte says agents in Omnia execute preliminary procedures, including data extraction, evidence analysis, drafting documentation and preliminary conclusions for professionals to review (DELOITTE-OMNIA-2026). KPMG announced agents for substantive procedures such as expense vouching (KPMG-CLARA-2025), and EY announced a multi-agent framework in EY Canvas covering all audit phases, with end-to-end support expected by 2028 (EY-CANVAS-2026).
  outcomes:
  - lever: quality
    description: Best model on workpaper-completion tasks in a benchmark of synthetic engagements
    figure: 69.17% strict pass in one attempt (Claude Opus 5.5); 44.44% passing all eight attempts; partial credit 95.84%
    measures: Share of workpaper-completion tasks, averaged over tasks and eight runs each, in which every applicable rubric criterion was met (about ten scored checks per workpaper, all-or-nothing); synthetic engagements, auditor-written rubrics.
    provenance: vendor-published
    source_ref: ARXIV-FAB-2026
    locator: Section 6.2, Table 1; Figure 3
  - lever: quality
    description: Strict pass rate by workpaper area, averaged over eleven models and eight runs
    figure: accounts receivable 4.17%; revenue 7.58%; journal-entry risk testing 16.86%; cash 56.06%; accounts payable 68.18%; journal-entry completeness 94.51%
    measures: Average strict (all-criteria) pass rate across all evaluated models and runs on synthetic workpapers of that area.
    provenance: vendor-published
    source_ref: ARXIV-FAB-2026
    locator: Table 3
  - lever: speed
    description: Median agent runtime versus estimated manual completion time
    figure: 7-12 minutes versus 2-12 hours
    measures: Median runtime by workpaper area versus auditors' approximate manual time estimates; the authors say the estimates exclude senior review and corrective rework and do not establish equivalent time savings.
    provenance: vendor-published
    source_ref: ARXIV-FAB-2026
    locator: Section 6.4; Table 3
  prerequisites:
  - An organised engagement binder with the supporting documents and a workpaper template that specifies the procedures (ARXIV-FAB-2026, section 3).
  - Certification of each model and prompt, with testing against cases that probe known weaknesses (FRC-GENAI-2026, certification section).
  - Engagement leaders setting expectations at the outset for how technology will be used and reviewing whether its scope and limits are understood (IFIAR-TTF-2026, p.7).
  risks_and_guardrails:
  - 'Benchmark failure analysis found four recurring errors: failing to consider downstream effects of changes, insufficient retrieval, inadequate evaluation of evidence sources, and reluctance to leave items open when information was missing (ARXIV-FAB-2026, section 6.3).'
  - The benchmark's authors conclude that deploying agents without professional oversight is ill-advised (ARXIV-FAB-2026, section 6.2).
  - IFIAR asks firms to assess carefully, and consult IFIAR members early, where AI makes judgements or decisions without human involvement (IFIAR-TTF-2025, p.8).
  - IFIAR says auditors must keep responsibility for evaluating, validating and challenging decisions made by AI systems, and that firms should be able to say what 'human-led' means in practice (IFIAR-TTF-2026, pp.5 and 7).
  human_checkpoints:
  - Oversight at control points, such as when intermediate outputs are ready or the agent wants to take certain actions, set by professional judgement (FRC-GENAI-2026, human in the loop oversight, p.38).
  - Professionals review preliminary conclusions drafted by agents (DELOITTE-OMNIA-2026).
  role_evolution: Deloitte's Omnia adds 'tutor' agents that give on-demand micro-training in the context of the work (DELOITTE-OMNIA-2026); benchmark authors observed agents over-documenting and writing in fragments, which raises reviewer effort (ARXIV-FAB-2026, section 7).
  evidence_grade: C
  sources:
  - ref: ARXIV-FAB-2026
    title: 'FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors (Huang, Babu et al.; UIUC, Stanford, Modus Audit Inc.)'
    publisher: arXiv 2609.32835
    type: academic
    url: https://arxiv.org/abs/2609.32835
    date: '2026-09-26'
    access: full
    locator: Sections 3, 6.2-6.4, 7; Tables 1 and 3; Figure 3
  - ref: DELOITTE-OMNIA-2026
    title: Deloitte unveils connected agentic intelligence in Deloitte Omnia to advance audit and assurance (CPA Practice Advisor)
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/06/24/deloitte-unveils-connected-agentic-intelligence-in-deloitte-omnia-to-advance-audit-assurance/185652/
    date: '2026-06-24'
    access: full
    locator: Paragraphs on what the agents can do and tutor agents
  - ref: KPMG-CLARA-2025
    title: KPMG advances AI integration in KPMG Clara smart audit platform (press release)
    publisher: KPMG International
    type: firm
    url: https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html
    date: '2025-04-22'
    access: full
    locator: Highlights and paragraph on substantive procedures
  - ref: EY-CANVAS-2026
    title: EY rolls out agentic AI in assurance across its global network of accounting firms (CPA Practice Advisor, summarising the EY release of 7 Apr 2026)
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/
    date: '2026-04-07'
    access: full
    locator: Opening paragraphs (scale and 2028 target)
  - ref: FRC-GENAI-2026
    title: 'Generative and Agentic AI Guidance: risks, mitigations and illustrative examples'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
    date: '2026-03-30'
    access: full
    locator: 'Mitigation sections: certification; human in the loop review and oversight (pp.37-38)'
  - ref: IFIAR-TTF-2025
    title: 'Use of technology in audits: observations, risks and further evolution'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf
    date: '2025-03-27'
    access: full
    locator: p.8
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf
    date: '2026-04-20'
    access: full
    locator: pp.5 and 7
  last_reviewed: '2026-10-16'
  notes: Firm items are announcements; no firm has published error rates or override rates for substantive agents. The benchmark is the only measured result; its authors include Modus Audit Inc. employees, the engagements are synthetic, and model names are as reported in the paper. Graded C because deployments are announced rather than shown in use.
- id: assurance-substantive-testing-10
  title: AI review of completed substantive workpapers to find omissions and errors (idea)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Senior auditors review staff workpapers, which takes time and can miss errors; the FRC lists 'tools that can review work to identify omissions or inconsistencies' among AI tools that may be deployed on an engagement (FRC-AIAUDIT-2025, p.6).
  solution: An agent reviews a completed workpaper against the supporting files and corrects errors while preserving correct work (ARXIV-FAB-2026, section 6.5).
  outcomes:
  - lever: quality
    description: Review of agent-completed synthetic workpapers by the best model
    figure: strict pass 28.89% before review, 62.22% after review (Claude Opus 5.5); partial credit 87.34% to 94.57%
    measures: Share of 45 review tasks in which all rubric criteria were met; every reviewing model started from the same workpaper (written by a randomly chosen model) and was run once; the paper says some individual workpapers scored lower after review.
    provenance: vendor-published
    source_ref: ARXIV-FAB-2026
    locator: Section 6.5; Table 4
  prerequisites:
  - Access to the same supporting files the preparer used and a rubric or checklist of what the review must cover (ARXIV-FAB-2026, section 6.5 and Appendix D.2).
  risks_and_guardrails:
  - The authors say agent review improves workpaper quality but does not reliably resolve all errors (ARXIV-FAB-2026, section 6.5).
  - The FRC says reviewers need the competence to find deficiencies, should apply scepticism, and should be aware of automation bias; for an AI-generated list of risks the reviewer may form an independent view (FRC-GENAI-2026, human in the loop review, p.37).
  human_checkpoints:
  - A human reviewer remains responsible for the reviewed workpaper (FRC-GENAI-2026, p.37).
  role_evolution: Not studied; the benchmark treats agent review as a co-pilot role under professional oversight (ARXIV-FAB-2026, section 7).
  evidence_grade: D
  sources:
  - ref: ARXIV-FAB-2026
    title: 'FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors (Huang, Babu et al.; UIUC, Stanford, Modus Audit Inc.)'
    publisher: arXiv 2609.32835
    type: academic
    url: https://arxiv.org/abs/2609.32835
    date: '2026-09-26'
    access: full
    locator: Section 6.5; Table 4; section 7
  - ref: FRC-AIAUDIT-2025
    title: 'AI in Audit: illustrative example and documentation guidance'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/AI_in_Audit.pdf
    date: '2025-06-26'
    access: full
    locator: p.6 (scope of AI tools)
  - ref: FRC-GENAI-2026
    title: 'Generative and Agentic AI Guidance: risks, mitigations and illustrative examples'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
    date: '2026-03-30'
    access: full
    locator: p.37
  last_reviewed: '2026-10-16'
  notes: 'Labelled idea: benchmark results exist but no deployment of AI workpaper review in an audit firm was found. Synthetic engagements; authors include Modus Audit Inc. employees.'
- id: assurance-substantive-testing-11
  title: Agent search for unrecorded liabilities and accrued expenses
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - transaction-processing
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: KPMG's release names search for unrecorded liabilities and accrued expenses among substantive procedures it is standardising and automating with agents; it does not describe the current pain (KPMG-CLARA-2025).
  solution: KPMG announced on 22 Apr 2025 that agents in Clara include search for unrecorded liabilities and accrued expenses, as part of agents for substantive procedures, to support more than 95,000 auditors, with a human in the loop (KPMG-CLARA-2025).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: KPMG's release gives no performance, time or error measures for the agents.
    provenance: self-reported
    source_ref: KPMG-CLARA-2025
    locator: Highlights and body
  prerequisites:
  - Access to engagement data and documents inside the firm's audit platform (KPMG-CLARA-2025).
  risks_and_guardrails:
  - KPMG says auditors stay in control of decisions to maintain quality, accuracy and professional scepticism (KPMG-CLARA-2025).
  - 'Adjacent benchmark evidence: a synthetic accounts-payable workpaper had a strict pass rate of 68.18% averaged over models, and agents sometimes documented work on whatever information was available even when subsequent-period information was missing (ARXIV-FAB-2026, Table 3 and section 6.3).'
  human_checkpoints:
  - Human-in-the-loop decisions by auditors (KPMG-CLARA-2025).
  role_evolution: KPMG says AI handling routine tasks lets auditors spend more time on high-risk areas and sector-specific challenges (KPMG-CLARA-2025).
  evidence_grade: C
  sources:
  - ref: KPMG-CLARA-2025
    title: KPMG advances AI integration in KPMG Clara smart audit platform (press release)
    publisher: KPMG International
    type: firm
    url: https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html
    date: '2025-04-22'
    access: full
    locator: Highlights; paragraphs on AI agents and human-in-the-loop
  - ref: ARXIV-FAB-2026
    title: 'FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors (Huang, Babu et al.; UIUC, Stanford, Modus Audit Inc.)'
    publisher: arXiv 2609.32835
    type: academic
    url: https://arxiv.org/abs/2609.32835
    date: '2026-09-26'
    access: full
    locator: Table 3; section 6.3
  last_reviewed: '2026-10-16'
  notes: Single firm announcement; no evidence of use beyond the release and no measures. The benchmark data are adjacent, not about KPMG's agent.
- id: assurance-substantive-testing-12
  title: Drone and imaging tools for inventory counts and remote-asset observation (idea)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - physical-field
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Observing inventory counts and inspecting geographically dispersed or remote assets requires auditors to attend physically; inventory procedures had a finding in 26 of 279 inspected listed PIE audits (9%) in IFIAR's 2025 survey (IFIAR-SURVEY-2026, Table B.2).
  solution: IFIAR lists drones and imaging tools among technologies audit firms continue to explore and deploy, for physical observation, inventory counts, inspection of remote assets and collection of visual and geospatial data (IFIAR-TTF-2026, Appendix A, p.12).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: IFIAR gives no usage rate, named firm or result for drone-based observation.
    provenance: independent
    source_ref: IFIAR-TTF-2026
    locator: Appendix A, p.12
  prerequisites:
  - Industries with dispersed operations, where visual and geospatial data collection helps (IFIAR-TTF-2026, Appendix A, p.12).
  risks_and_guardrails:
  - IFIAR states the technology examples are illustrative and not exhaustive, and its ATT usage observations are directional (IFIAR-TTF-2026, Appendix A and p.9 footnote 3).
  - PCAOB staff flagged inventory valuation risk for technology hardware and semiconductor issuers in its 2025 inspection priorities (PCAOB-PRIORITIES-2024, p.5); this concerns valuation, not observation.
  human_checkpoints:
  - Not described in the sources.
  role_evolution: Not described in the sources.
  evidence_grade: D
  sources:
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf
    date: '2026-04-20'
    access: full
    locator: Appendix A, p.12; p.9 footnote 3
  - ref: IFIAR-SURVEY-2026
    title: Survey of Inspection Findings 2025 (14th annual survey)
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf
    date: '2026-04-01'
    access: full
    locator: Appendix B, Table B.2
  - ref: PCAOB-PRIORITIES-2024
    title: 'Spotlight: Staff Priorities for 2025 Inspections and Interactions With Audit Committees'
    publisher: PCAOB (staff)
    type: regulator
    url: https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf
    date: 2024-12
    access: full
    locator: p.5 (technology sector)
  last_reviewed: '2026-10-16'
  notes: 'Labelled idea: the only source is a regulator''s list of technologies firms explore; no named firm, case or measurement was found. A search-only landscape lead on an LLM field experiment for inventory valuation could not be opened (see Gaps).'
- id: assurance-substantive-testing-13
  title: AI-generated independent expectations and challenge for management's accounting estimates (idea)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - expert-judgment
  - review-assurance
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: 'Accounting estimates, including fair value, had the highest finding rate among inspection themes in the 2025 IFIAR survey: 112 of 498 inspected listed PIE audits (22%) (IFIAR-SURVEY-2026, Table B.2). Researchers note firms are investing in AI to help auditors with challenging tasks such as evaluating complex estimates (COMMERFORD-2022, abstract).'
  solution: An AI system supplies contradictory evidence or an alternative estimate that the auditor weighs against management's estimate (COMMERFORD-2022, abstract).
  outcomes:
  - lever: quality
    description: 'Experiment: auditors receiving contradictory evidence from their firm''s AI system rather than a human specialist'
    figure: proposed smaller adjustments to management's complex estimates (no percentage in the abstract)
    measures: Direction of effect in a controlled experiment on auditor judgements; stronger when management used relatively objective inputs.
    provenance: independent
    source_ref: COMMERFORD-2022
    locator: Abstract
  prerequisites:
  - A firm-specific AI system and a task setting in which its evidence can be compared with management's inputs (COMMERFORD-2022, abstract).
  risks_and_guardrails:
  - 'Algorithm aversion: auditors discounted AI advice relative to identical human-specialist advice, which could be costly for the profession and users of financial statements (COMMERFORD-2022, abstract).'
  - IFIAR says AI tools tend to generalise on complex estimates and new or unprecedented events, so human context-specific judgement and scepticism matter most there (IFIAR-TTF-2025, p.8).
  human_checkpoints:
  - Auditor judges the evidence and decides on adjustments (COMMERFORD-2022, abstract).
  role_evolution: Not studied beyond auditors' reliance behaviour (COMMERFORD-2022, abstract).
  evidence_grade: D
  sources:
  - ref: COMMERFORD-2022
    title: 'Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence (Commerford, Dennis, Joe, Ulla)'
    publisher: Journal of Accounting Research 60(1)
    type: academic
    url: https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html
    date: 2022-03
    access: full
    locator: Abstract
  - ref: IFIAR-TTF-2025
    title: 'Use of technology in audits: observations, risks and further evolution'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf
    date: '2025-03-27'
    access: full
    locator: p.8 (complex estimates)
  - ref: IFIAR-SURVEY-2026
    title: Survey of Inspection Findings 2025 (14th annual survey)
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf
    date: '2026-04-01'
    access: full
    locator: Appendix B, Table B.2
  last_reviewed: '2026-10-16'
  notes: 'Labelled idea: discussed by researchers and a regulator; no firm deployment for estimates testing was found. Commerford et al. is a 2022, pre-generative-AI experiment. A search-only landscape lead on an LLM field experiment for inventory valuation could not be opened (see Gaps). Use of valuation specialists is routed to the specialists module.'
- id: assurance-substantive-testing-14
  title: Authenticity checks on evidence that may be AI-generated or AI-altered (idea)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: IRBA warned in Sept 2024 that AI tools can create more realistic false evidence or fabricated working papers, undermining the reliability of the audit (IRBA-AI-2024, p.1). IFIAR notes that order forms, shipment details, invoices, payment records and bank statements may originate from AI systems and be used as audit evidence, and that auditors should watch for deliberate manipulation of data, documents or transactions (IFIAR-TTF-2026, p.10).
  solution: Firms add procedures to verify the authenticity of evidence, as IRBA recommends (IRBA-AI-2024, p.1). Whether firms use automated authenticity-detection tools in substantive testing was not found.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No source reports usage or detection rates.
    provenance: independent
    source_ref: IRBA-AI-2024
    locator: p.1
  prerequisites:
  - Firm policy on AI use and a protocol to monitor it, as IRBA recommended in January 2023 (IRBA-AI-2024, p.1).
  risks_and_guardrails:
  - IFIAR says auditors need to evaluate the source and nature of information used as evidence, taking account of the potential for unreliable output generated by some forms of AI (IFIAR-TTF-2026, p.10).
  - AFM found auditors do not always verify the reliability of input data used in tools (AFM-BB-2025, Precondition 2).
  human_checkpoints:
  - Auditor evaluates source and nature of evidence (IFIAR-TTF-2026, p.10).
  role_evolution: Not described in the sources.
  evidence_grade: D
  sources:
  - ref: IRBA-AI-2024
    title: Artificial Intelligence Audit Risks Mitigation Update (communique)
    publisher: IRBA (South Africa)
    type: regulator
    url: https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf
    date: '2024-09-19'
    access: full
    locator: p.1
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf
    date: '2026-04-20'
    access: full
    locator: p.10
  - ref: AFM-BB-2025
    title: 12 Building blocks for controlled use of auditing tools
    publisher: AFM (Netherlands)
    type: regulator
    url: https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf
    date: 2025-12
    access: full
    locator: Precondition 2
  last_reviewed: '2026-10-16'
  notes: 'Labelled idea: regulators describe the risk and recommend procedures, but no detection tooling or case in audit practice was found. Touches vouching (use cases 03 and 04).'
- id: assurance-substantive-testing-15
  title: Evidence-linked exception triage and explanation for items flagged by whole-population tests
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Whole-population tests surface more exceptions to follow up; the PCAOB amendments require the auditor to investigate items identified by criteria, and IFIAR members' common findings include thin testing of outliers (PCAOB-TAA-2024, discussion of AS 2301.49-.50; IFIAR-TTF-2025, pp.5-6).
  solution: MindBridge announced on 22 Sep 2026 an Agentic Risk Assessment capability that links evidence, analytics, assertions, materiality and methodology, and says its platform combines full-population analysis with explainable risk detection (MINDBRIDGE-ARA-2026). The FRC's journal example requires teams to understand why each high-risk item was flagged and to look for items the tool may have missed (FRC-AIAUDIT-2025, p.11).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: The MindBridge release gives no performance figure.
    provenance: vendor-published
    source_ref: MINDBRIDGE-ARA-2026
    locator: Announcements list
  prerequisites:
  - Integration with the firm's workpaper tools; MindBridge says the capability works with customer-built and third-party workpaper solutions (MINDBRIDGE-ARA-2026).
  risks_and_guardrails:
  - The FRC example finds that an item flagged as unusual may be correct while similar unflagged items are the risky ones, so follow-up must go beyond the flagged list (FRC-AIAUDIT-2025, p.11).
  - IFIAR's 2026 report suggests monitoring false-positive and false-negative rates against a manual sample, rework rates and escalation incidence (IFIAR-TTF-2026, pp.8-9).
  human_checkpoints:
  - Auditor investigates and documents the rationale for concluding on flagged and additional items (FRC-AIAUDIT-2025, p.11).
  role_evolution: MindBridge says judgement stays with the auditor (MINDBRIDGE-ARA-2026); the FRC example has teams documenting rationale for follow-up conclusions (FRC-AIAUDIT-2025, p.11).
  evidence_grade: C
  sources:
  - ref: MINDBRIDGE-ARA-2026
    title: MindBridge Advances Financial Oversight for the Agentic Era with New Platform Capabilities (press release)
    publisher: MindBridge Analytics
    type: vendor
    url: https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/
    date: '2026-09-22'
    access: full
    locator: Announcements list; Augmented Assurance paragraph
  - ref: FRC-AIAUDIT-2025
    title: 'AI in Audit: illustrative example and documentation guidance'
    publisher: FRC (UK)
    type: regulator
    url: https://media.frc.org.uk/documents/AI_in_Audit.pdf
    date: '2025-06-26'
    access: full
    locator: Illustrative example p.11
  - ref: PCAOB-TAA-2024
    title: Notice of Filing of Proposed Rules on Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 54922; carries the Board's adopting-release text, Release 2024-007)
    publisher: PCAOB; SEC (Federal Register)
    type: regulator
    url: https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14488.pdf
    date: '2024-07-02'
    access: full
    locator: Discussion of AS 2301.49-.50
  - ref: IFIAR-TTF-2025
    title: 'Use of technology in audits: observations, risks and further evolution'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf
    date: '2025-03-27'
    access: full
    locator: pp.5-6
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf
    date: '2026-04-20'
    access: full
    locator: pp.8-9
  last_reviewed: '2026-10-16'
  notes: Vendor announcement and regulator illustration only. Customer names, accuracy and time-saving figures were not found for exception triage. Planning-stage use of the same product is covered in the planning-risk-assessment module.
- id: assurance-substantive-testing-16
  title: Generative AI assistant for designing substantive procedures from engagement documentation
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Teams must tailor substantive procedures to assessed risks and the entity; PCAOB staff found firms' use of generative AI focused mainly on administrative and research tasks, with potential uses in risk assessment and scoping (PCAOB-GENAI-2024, pp.4-5).
  solution: KPMG announced in July 2024 the integration of generative AI into Clara for 90,000 auditors, interacting with engagement documentation and methodology to help refine risk assessments and develop substantive testing procedures (KPMG-CLARA-2025, background paragraph).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: KPMG's release gives no usage or quality measure for this capability.
    provenance: self-reported
    source_ref: KPMG-CLARA-2025
    locator: Background paragraph on July 2024
  prerequisites:
  - Firm-approved tools with data privacy and confidentiality safeguards on what can be uploaded (PCAOB-GENAI-2024, p.4).
  risks_and_guardrails:
  - Some firms barred generative AI in audit or attest procedures because of data privacy and reliability concerns, and noted hallucinations (PCAOB-GENAI-2024, p.4).
  - In ICAEW's single test, three general chatbots did not separate financial-statement-level from assertion-level risk and none performed risk assessment as a human auditor would (ICAEW-PIERPOINT-2025, risk of material misstatement section).
  - Most IFIAR member inspections had seen minimal use of generative AI applications in public company audits (IFIAR-TTF-2025, p.7).
  human_checkpoints:
  - Engagement team member using the tool stays responsible for results and documentation, and reviewers apply the same diligence as for other work (PCAOB-GENAI-2024, pp.4-5).
  role_evolution: PCAOB staff reported firms expecting generative AI to augment, not replace, auditors, with supervision and review policies unchanged (PCAOB-GENAI-2024, pp.4-5).
  evidence_grade: C
  sources:
  - ref: KPMG-CLARA-2025
    title: KPMG advances AI integration in KPMG Clara smart audit platform (press release)
    publisher: KPMG International
    type: firm
    url: https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html
    date: '2025-04-22'
    access: full
    locator: Background paragraph (July 2024 integration)
  - ref: PCAOB-GENAI-2024
    title: 'Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting'
    publisher: PCAOB (staff)
    type: regulator
    url: https://pcaobus.org/documents/generative-ai-spotlight.pdf
    date: 2024-07
    access: full
    locator: pp.4-5
  - ref: ICAEW-PIERPOINT-2025
    title: 'Testing Gen AI platforms: can they do audit work? (Helen Pierpoint)'
    publisher: ICAEW
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work
    date: '2025-09-24'
    access: full
    locator: Analytical review and risk of material misstatement sections
  - ref: IFIAR-TTF-2025
    title: 'Use of technology in audits: observations, risks and further evolution'
    publisher: IFIAR (read via the Japan FSA mirror)
    type: regulator
    url: https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf
    date: '2025-03-27'
    access: full
    locator: p.7
  last_reviewed: '2026-10-16'
  notes: Firm announcement; no named engagement result. The PCAOB staff observations are from 2024 outreach to mostly larger firms and are staff views, not Board policy. ICAEW's test used a fictional retailer and three models and is not a benchmark.
```

---

## 3. Module notes

### Processes and key steps (with work types)
- **Decide the substantive response and how to select items:** all items, specific items, or audit sampling (work types: expert-judgment, review-assurance). The ED-330 and ED-500 drafts list the three approaches and say the technology does not change the auditor's objectives (IAASB-ED330-2026, A82; IAASB-ED500-2026, Appendix 2, paragraph 1 and Appendix 3 introduction).
- **Journal-entry and fraud-response testing** (review-assurance, data-reporting). ISA 240 (Revised), paragraphs 47-48, requires testing the appropriateness of journals and other adjustments (IAASB-ED330-2026, A25 and footnote 26); the revised standard is effective for periods beginning on or after 15 Dec 2026 (IAASB-ISA240-2025).
- **Tests of details: vouching, tracing, recalculation, cut-off** (review-assurance, transaction-processing). The PCAOB now describes a test of details as procedures on items included in an account or disclosure (AS 2301.48) (PCAOB-TAA-2024, discussion of AS 2301.48).
- **External confirmations** (transaction-processing), under the PCAOB's new confirmation standard (PCAOB-CONFIRM-2023).
- **Substantive analytical procedures** (data-reporting), under ED-520's proposed definitions (IAASB-ED520-2026, A20-A23).
- **Revenue, inventory and estimates** (expert-judgment, physical-field), including contract review, observation of counts and challenge of management estimates (FRC-GENAI-2026, example 2; IFIAR-TTF-2026, Appendix A; COMMERFORD-2022).
- **Investigate identified items and evaluate misstatements** (expert-judgment), including the PCAOB's AS 2301.49-.50 investigation considerations (PCAOB-TAA-2024).
- **Document the work and the tool's use** (document-production): the FRC expects a record on the audit file that a tool was used and the criteria for its use were met (FRC-GENAI-2026, example 2; FRC-AIAUDIT-2025, p.11).

### Common pain points
- **Client data and system access.** 60% of the surveyed US firms name poor client data and 53% lack of access to client systems among top blockers; 66% name untrained staff (CPACOM-ATR-2025, barriers section; 54 firms with complete data).
- **Manual matching time.** One Thomson Reuters customer put it at about 16 hours per engagement before the tool (TR-AGENTIC-2025). Benchmark authors estimated 2-12 hours of manual completion per synthetic workpaper, excluding senior review (ARXIV-FAB-2026, Table 3).
- **False positives from rules-based tests.** A rules-based journal test produced 942 false positives on 5,000 posting IDs in one research benchmark (ARXIV-AUDITCOPILOT-2025, Table 1).
- **Unclear classification of technology-assisted procedures** as tests of details or analytical procedures, which affects sample sizes and extent (IAASB-EDOVERALL-2026, paragraph 37).
- **No measurement of tool impact.** Six UK firms did no formal monitoring to quantify audit-quality impact of automated tools and mostly lacked usage KPIs (FRC-ATT-2025, p.20).

### Metrics and benchmarks (with sources)
- **Regulator-observed tool use (IFIAR members saying "frequently observed").** Journal entry testing 86% (2023), 88% (2024), about 86% (2025, chart); risk assessment 49%, 55%, about 53%; substantive procedures 51%, 55%, about 63%; internal controls testing 33%, 43%, about 44%; IT applications 33%, 39%, about 38% (IFIAR-TTF-2025, p.5; IFIAR-TTF-2026, p.10; 2025 values read from an unlabelled chart). Respondents were 42-49 members per row in 2023 and 2024.
- **GPPC networks' AI tools.** The six networks collectively reported an approximate 30% year-over-year increase in AI-enabled tools in 2025; IFIAR cautions that firms report on differing bases (IFIAR-TTF-2026, p.5 and footnote 1).
- **PCAOB-reported tool counts (2023 inspection year).** The six U.S. global network firms averaged about 18 tools per firm, up from about 13 in 2018; about 90% of tools were for visualisation, summarisation, tabulation or modelling; under 7% used AI, blockchain or RPA; non-affiliated firms averaged about six tools (seven firms) (PCAOB-TAA-2024, economic analysis).
- **Inspection finding rates, 2025 survey (listed PIE audits where the topic was inspected, at least one finding).** Accounting estimates 112 of 498 (22%); audit sampling 46 of 420 (11%); inventory procedures 26 of 279 (9%); revenue recognition 53 of 635 (8%); substantive analytical procedures 15 of 331 (5%); fraud procedures 25 of 714 (4%). Overall, 35% of listed PIE audits inspected had a finding in 2025, up from 26% in 2022 (IFIAR-SURVEY-2026, section 1 and Table B.2). None of these is AI-specific.
- **US small and mid-size firms (54 firms).** Automated solutions: foot and proof 39%, confirmations 39%, trial-balance import 35%, risk assessment 22%, data ingestion 19%, substantive analytics 11%, none 22%; 89% not using technology to enable substantive analytics (CPACOM-ATR-2025, pp.10 and 19).
- **Internal audit (adjacent).** 83% of audit functions piloting or using AI, 12% planning to within a year (Gartner survey of 119 chief audit executives, Aug 2025) (GARTNER-2026); of 743 webinar respondents, 93% use some AI, 38% have a strategy, and 30% use AI for audit testing against 60% for drafting reports (GARTNER-AUG-2026). Not external audit.
- **Model benchmarks.** FinancialAuditBench (90 tasks, six synthetic engagements, eleven models) (ARXIV-FAB-2026); AuditCopilot journal-entry anomaly detection (ARXIV-AUDITCOPILOT-2025); a 167-sample document-testing study (GRACZYK-2025). Related benchmarks on completion-stage tasks: FinAuditing found gaps in concept retrieval and cross-document reasoning across 13 LLMs on 1,102 instances (ARXIV-FINAUDITING-2025, abstract); a five-stage benchmark found LLMs identify statement errors given transaction history but struggle to explain errors, cite standards and complete audits (ARXIV-LLMAUDIT-2025, abstract).
- **Monitoring metrics regulators suggest.** Engagement coverage percentage, false-positive and false-negative rates against a manual sample, rework rates, escalation incidence, plus internal benchmarking of tool results against traditional methods (IFIAR-TTF-2026, pp.8-9).

### Guardrails and regulatory points
- **PCAOB amendments (AS 1105, AS 2301).** Effective for fiscal years beginning on or after 15 Dec 2025 (SEC-TAAORDER-2024, section II). Scope: technology-assisted analysis only; AI and tool appropriateness under quality control are excluded, and QC 1000 carries the firm-level duties on technological resources (PCAOB-TAA-2024, background and footnote 20). The Board chose not to require technology use (PCAOB-TAA-2024, comments discussion).
- **How the amendments were received.** Six comment letters (Deloitte, KPMG, PwC, RSM, CAQ, EY). Commenters said AS 1105.10A(b) could be read as requiring tests of every external item or of controls in all cases. PwC said it could not support the amendments without further amendment or interpretive guidance, and all commenters said implementation guidance was warranted. The SEC said the concern may be misplaced because the Board stated it was not prescribing the nature, timing or extent of procedures (SEC-TAAORDER-2024, section III). A Board project on substantive analytical procedures was still pending (SEC-TAAORDER-2024, footnote 19).
- **PCAOB staff.** July 2024 outreach found generative AI used mainly for administrative and research tasks, firms saying standards were not an impediment, and some firms barring it from audit procedures (PCAOB-GENAI-2024, pp.4-5). Staff said in Dec 2024 they would keep inquiring about technology used to respond to identified risks and that its nature, timing and extent should fit the engagement (PCAOB-PRIORITIES-2024, pp.5-6). These are staff views, not Board policy.
- **PCAOB confirmations.** The new standard covers paper and electronic methods and takes effect, subject to SEC approval, for fiscal years ending on or after 15 June 2025 (PCAOB-CONFIRM-2023).
- **IAASB.** ED-500, ED-330 and ED-520 (5 Aug 2026; comments due 15 Dec 2026) replace "automated tools and techniques" with "technological tools", add application material and an Appendix 3 on tool use, and propose no technology requirement (IAASB-EDPAGE-2026; IAASB-EDOVERALL-2026, paragraphs 44-45 and 61; IAASB-ED500-2026, paragraphs 67-69). Appendix 3 lists factors for evaluating information used by a tool (volume, complexity, structuredness, integrity) and warns that automation bias may rise when procedures are complex or transparency is low (IAASB-ED500-2026, Appendix 3, paragraphs 5-8). ED-500 also says specific-item testing cannot be projected to a population (IAASB-ED500-2026, Appendix 2, paragraph 7).
- **FRC.** Its March 2026 guidance is the first from any audit regulator on generative and agentic AI and is not a response to identified deficiencies; accountability stays with the human auditor (FRC-GENAINEWS-2026). It sets three risks (deficient output, misuse of output, non-compliant methodology) and mitigations (system design, certification, staff education, human-in-the-loop review and oversight) (FRC-GENAI-2026, introduction and mitigation sections).
- **IFIAR and other regulators.** IFIAR wants firms to keep auditors in control, monitor tool impact at network and member-firm level, and consult regulators early where AI decides without a human (IFIAR-TTF-2025, p.8; IFIAR-TTF-2026, pp.3-4). AFM published 12 building blocks after reviewing 13 firms (11 non-PIE, 2 PIE) and two files each (AFM-BB-2025, introduction). CPAB expects policies, certification testing and monitoring and reported limited AI in inspected files in Sept 2024 (CPAB-AI-2024, p.1). AUASB cites ASQM 1 paragraph 32(f), which requires AI audit tools to be appropriate and appropriately implemented, maintained and used (AUASB-AI-2025). ACRA issued audit practice guidance on technology in Dec 2025 (ACRA-APG-2025, announcement only). IRBA recommends procedures to verify authenticity of evidence (IRBA-AI-2024, p.1).
- **US profession.** The AICPA practice aid of 13 Oct 2026 covers an entity's AI use and the firm's own AI use under quality management; it says auditors stay responsible for supervision, review and conclusions, and more content on risk of material misstatement and evidence is planned (AICPA-PA-2026). The CAQ's April 2024 paper notes that where substantive procedures alone are not sufficient, tests of controls are required, which matters when a client's AI cannot be independently verified (CAQ-GENAI-2024, section on future state, citing AS 2301.17).

### Frontier signals (dated)
- **2026-08-05:** IAASB exposure drafts on audit evidence and risk response; comments due 2026-12-15; non-authoritative technology guidance flagged for later (IAASB-EDPAGE-2026; IAASB-EDOVERALL-2026, paragraph 45).
- **2026-04-20:** IFIAR reports firms told its task force they plan to explore agentic AI, moving from task automation toward orchestrating multiple audit activities, and asks firms to explain what "human-led" means (IFIAR-TTF-2026, pp.5 and 7).
- **2026-03-30:** FRC guidance on generative and agentic AI, with a contract-review example for revenue testing (FRC-GENAINEWS-2026).
- **2026-04-07 and 2026-06-24:** EY says its multi-agent framework in EY Canvas covers all audit phases for 130,000 assurance professionals, with end-to-end support expected by 2028, on a platform processing 1.4 trillion journal-entry lines a year (EY-CANVAS-2026); Deloitte says agents in Omnia execute preliminary procedures for professionals to review (DELOITTE-OMNIA-2026). Both are announcements.
- **2025-10-28 and 2026-10-07:** PwC Australia says its AI-native pilot starts with five clients and aims at all clients by 2028 (PWCAU-2025); a year on, PwC US says time savings are modest so far (CFODIVE-PWC-2026).
- **2026-09-26:** FinancialAuditBench shows agents completing much staff-level work but failing strict criteria often enough that its authors advise against unsupervised use (ARXIV-FAB-2026, section 6.2).
- **2026-10-13:** First AICPA practice aid on AI for financial statement auditors (AICPA-PA-2026).
- **2026-09-22:** MindBridge announces an agentic risk-assessment capability and a preview of an agent that configures analyses (MINDBRIDGE-ARA-2026).
- **2025-12:** AFM's building blocks include a base layer of risk management, then input-data reliability, then tool implementation, before generative AI (AFM-BB-2025, summary diagram).
- **2025-12-15 and 2026-12-15:** PCAOB amendments take effect for fiscal years beginning on or after the first date (SEC-TAAORDER-2024); ISA 240 (Revised) for periods beginning on or after the second (IAASB-ISA240-2025).
- **2026-02-12:** A secondary report, citing Financial Times and Going Concern items, says KPMG pressed Grant Thornton UK for a fee cut because of AI and got about 14% (THEFINANCESTORY-KPMGFEE-2026). The underlying reports were not opened.

### Workforce and role effects
- **Pre-GenAI firm-level evidence.** Across the 36 largest audit firms, a one-standard-deviation change in recent AI investment was associated with a 5.0% lower likelihood of an audit restatement, 0.9% lower audit fees and 3.6% fewer accounting employees after three years (7.1% after four) (FEDYK-2022, abstract). The study predates generative AI and measures AI-worker hiring from resumes.
- **Reliance behaviour.** Auditors who got contradictory evidence from their firm's AI system proposed smaller adjustments to complex estimates than those who got it from a human specialist (COMMERFORD-2022, abstract).
- **Field interviews.** Of 22 experienced audit professionals interviewed, "simple AI" such as key-data extraction and OCR is widely used while "complex AI" is still being developed; challenges include explainability, bias, over-reliance and a need for guidance (KOKINA-2025, abstract).
- **Skills and hiring.** PwC is hiring engineers into assurance and seeking dual-track CPA and data-science entrants (PWC-AT-2025). Deloitte adds tutor agents for on-demand training (DELOITTE-OMNIA-2026). Training gaps are the top US blocker at 66% (CPACOM-ATR-2025, barriers section).
- **Skepticism and supervision.** IFIAR lists decline of professional skepticism as a risk and asks firms to adjust supervision training as AI use grows (IFIAR-TTF-2025, pp.7-8). A university release on a study of AI-assisted management-report audits found acceptance depends on position, experience and involvement in digital transformation, with some auditors worried about over-reliance and loss of skills (FABIAN-2026).

### Objections and concerns practitioners and regulators raise
- **Premature to prescribe.** The IAASB judged it premature to set a single workable model for technology requirements (IAASB-ED500-2026, paragraph 68).
- **Ability to evaluate inputs and operation.** Generative tools may make it impossible to fully evaluate inputs or confirm the tool operates as designed (IAASB-ED500-2026, paragraph 68).
- **Over-selling certainty.** A practitioner warns "test everything" marketing widens the expectation gap, since some risks sit outside transaction data (CPAPA-FULLPOP-2026).
- **Interpretive uncertainty.** Firms and the CAQ asked for guidance on AS 1105.10A and on classifying technology-assisted procedures (SEC-TAAORDER-2024, section III; PCAOB-TAA-2024, discussion of AS 2301.48).
- **Fragmented monitoring.** IFIAR sees a risk that monitoring is fragmented across networks and member firms (IFIAR-TTF-2026, p.8; IFIAR-TTF-2025, p.6).
- **Data confidentiality and file limits.** Firms cite privacy and security of client data (PCAOB-GENAI-2024, p.4); the Polish study's models rejected files over size or format limits (GRACZYK-2025, section 4).
- **Fake evidence.** Regulators warn about AI-generated or manipulated documents (IRBA-AI-2024, p.1; IFIAR-TTF-2026, p.10).
- **Adoption is broad but shallow in internal audit.** Gartner says AI use there is common but mostly for isolated tasks, not transformation (GARTNER-AUG-2026).

### Interview probes for an advisor
1. For your three largest substantive procedures, what share of items is now covered by a tool versus sampled, and who decided the output was persuasive enough to replace or reduce a sample? What did the file record? (FRC says outputs need not match the persuasiveness of the old procedure if not overstated; FRC-GENAI-2026.)
2. How do you evidence completeness and reliability of client data before whole-population analysis, including for external information the client holds electronically? Have reviews or inspections raised this? (AS 1105.10A; AFM-BB-2025.)
3. What shadow-mode or parallel-run results do you hold: false positives and negatives against a manual sample, override and rework rates? Who monitors, the network or the member firm? (IFIAR-TTF-2026, pp.8-9; FRC-ATT-2025, p.20.)
4. When a tool flags more exceptions than the old test, who follows them up, how is that time budgeted, and has any time or fee budget been cut because of the tool? (CFODIVE-PWC-2026; THEFINANCESTORY-KPMGFEE-2026.)
5. How are reviewers trained to challenge tool output (automation bias), and which tasks do juniors still do by hand to build judgement? (IAASB-ED500-2026, Appendix 3, paragraph 8; IFIAR-TTF-2025, p.8.)

---

## 4. Routed to other modules

- **completion-reporting.** Disclosure-checklist and tie-out agents (KPMG's Financial Report Analyzer, KPMG-CLARA-2025; Caseware's Disclosure Checklist Agent, where beta firms saved 2.7 hours per run, a vendor figure, CASEWARE-VERITY-2026); the AI-assisted management-report audit study (FABIAN-2026); the FinAuditing and LLM-audit benchmarks (ARXIV-FINAUDITING-2025; ARXIV-LLMAUDIT-2025).
- **planning-risk-assessment.** MindBridge's Agentic Risk Assessment as a planning tool (MINDBRIDGE-ARA-2026); ICAEW's chatbot test on ISA 315 risk assessment (ICAEW-PIERPOINT-2025); ED-520 risk-assessment analytics (IAASB-ED520-2026, paragraphs on risk assessment analytical procedures).
- **controls-testing and specialists (client AI).** AS 2301.17 on tests of controls when substantive procedures alone are insufficient, as clients rely on AI (CAQ-GENAI-2024); AICPA practice aid Part 1 on AI-operated controls (AICPA-PA-2026); IFIAR's point that evidence such as invoices may originate from AI systems (IFIAR-TTF-2026, p.10).
- **specialists.** Valuation and other specialists on estimates; algorithm aversion in estimates (COMMERFORD-2022) is kept here only as the evidence for use case 13.
- **quality-management.** Certification, recertification and monitoring of tools (FRC-ATT-2025; IFIAR-TTF-2026, pp.6-9; AFM-BB-2025; CPAB-AI-2024; AUASB-AI-2025); skills and supervision research (FABIAN-2026).
- **Business-model and workforce lens (cross-cutting).** Fee pressure from AI efficiency (THEFINANCESTORY-KPMGFEE-2026); AI-native audit ventures such as Modus Audit Inc., whose staff co-authored the benchmark used here (ARXIV-FAB-2026); the Gartner internal-audit surveys (GARTNER-2026; GARTNER-AUG-2026) belong to the internal-audit view of this archetype.

---

## 5. Sources

Refs follow `PUBLISHER-SHORT-YYYY`. All sources below were opened in this run (`access: full`) unless the note says only a page or abstract was read. Notes on partial reads are in the last column.

| Ref | Title | Publisher | Type | URL | Date | Note |
|---|---|---|---|---|---|---|
| ARXIV-AUDITCOPILOT-2025 | AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping (Kadir, Vasu, Nair, Sonntag; DFKI) | arXiv 2512.02726 | academic | https://arxiv.org/abs/2512.02726 | 2025-12-02 | full read |
| ARXIV-FAB-2026 | FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors (Huang, Babu et al.; UIUC, Stanford, Modus Audit Inc.) | arXiv 2609.32835 | academic | https://arxiv.org/abs/2609.32835 | 2026-09-26 | Authors include employees of Modus Audit Inc., an AI-native audit venture. |
| ARXIV-FINAUDITING-2025 | FinAuditing: A Financial Taxonomy-Structured Multi-Document Benchmark for Evaluating LLMs | arXiv 2510.08886 | academic | https://arxiv.org/abs/2510.08886 | 2025-10-10 | Abstract read; v3 revised 17 May 2026. |
| ARXIV-LLMAUDIT-2025 | Automating Financial Statement Audits with Large Language Models | arXiv 2506.17282 | academic | https://arxiv.org/abs/2506.17282 | 2025-06-14 | Abstract read. |
| COMMERFORD-2022 | Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence (Commerford, Dennis, Joe, Ulla) | Journal of Accounting Research 60(1) | academic | https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html | 2022-03 | Abstract page read. |
| FABIAN-2026 | Auditing Corporate Disclosures with the Assistance of AI (Fabian, Ratzinger-Sakel), as summarised in the University of Hamburg release | Journal of Information Systems; University of Hamburg Business School | academic | https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html | 2026-03-20 | University release read, not the article. |
| FEDYK-2022 | Is artificial intelligence improving the audit process? (Fedyk, Hodson, Khimich, Fedyk) | Review of Accounting Studies 27(3) | academic | https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html | 2022-09 | Abstract page read; pre-GenAI. |
| GRACZYK-2025 | Use of large language models (LLMs) in auditing as a tool to reduce information asymmetry and fraud risk in the shareholder-management relationship (Graczyk, Majek, Modzelewski) | Yearbook of Auditing and Accounting 2025 | academic | https://pana.gov.pl/wp-content/uploads/2026/04/6.-YoAA_Use-of-large-language-models-LLMs-in-auditing-as-a-tool-o-reduce-information-asymmetry-and-fraud-risk-in-the-hareholder-management-relationship.pdf | 2025 | full read |
| KOKINA-2025 | Challenges and opportunities for artificial intelligence in auditing: Evidence from the field (Kokina, Blanchette, Davenport, Pachamanova) | International Journal of Accounting Information Systems 56 | academic | https://ideas.repec.org/a/eee/ijoais/v56y2025ics1467089525000107.html | 2025 | Abstract page read; month not stated. |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform (press release) | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04-22 | full read |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings (CFO Dive) | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 | full read |
| CPAPA-FULLPOP-2026 | Testing Every Transaction Changes the Audit: Here's What Firms Should Know Before They Sell It (Tunde Adewole, CEO of Ledgerline) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/ | 2026-10-15 | Opinion piece by the founder of a benefit-plan audit firm. |
| DELOITTE-OMNIA-2026 | Deloitte unveils connected agentic intelligence in Deloitte Omnia to advance audit and assurance (CPA Practice Advisor) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/06/24/deloitte-unveils-connected-agentic-intelligence-in-deloitte-omnia-to-advance-audit-assurance/185652/ | 2026-06-24 | full read |
| EY-CANVAS-2026 | EY rolls out agentic AI in assurance across its global network of accounting firms (CPA Practice Advisor, summarising the EY release of 7 Apr 2026) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 | Secondary report; EY's own release was not opened. |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 (Accounting Today) | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 | full read |
| PWCAU-2025 | PwC Australia rolls out pilot program for AI-assisted full audits (Accounting Times) | Accounting Times | press | https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits | 2025-10-28 | full read |
| THEFINANCESTORY-KPMGFEE-2026 | KPMG forced auditor for a 14% AI discount: will the billable hour die? (TheFinanceStory) | TheFinanceStory | press | https://thefinancestory.com/kpmg-forced-auditor-for-a-14-ai-discount-will-the-billable-hour-die | 2026-02-12 | Secondary report of Financial Times and Going Concern items; the underlying reports were not opened. |
| CAQ-GENAI-2024 | Auditing in the Age of Generative AI | Center for Audit Quality | professional-body | https://thecaq.wpenginepowered.com/wp-content/uploads/2024/04/caq_auditing-in-the-age-of-generative-ai__2024-04.pdf | 2024-04 | full read |
| ICAEW-PIERPOINT-2025 | Testing Gen AI platforms: can they do audit work? (Helen Pierpoint) | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09-24 | full read |
| ACRA-APG-2025 | Audit Practice Guidance No. 1 of 2025: Delivering Quality Audits in a Technology-Driven Environment (announcement page) | ACRA (Singapore) | regulator | https://www.acra.gov.sg/news-events/news-announcements/906/ | 2025-12-26 | Announcement page only; the guidance PDF was not opened. |
| AFM-BB-2025 | 12 Building blocks for controlled use of auditing tools | AFM (Netherlands) | regulator | https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf | 2025-12 | full read |
| AUASB-AI-2025 | Impact of AI on Auditors | AUASB (Australia) | regulator | https://www.auasb.gov.au/publications/impact-of-ai-on-auditors/ | 2025-07 | full read |
| CPAB-AI-2024 | The use of artificial intelligence in the audit: balancing innovation and risk | CPAB (Canada) | regulator | https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf | 2024-09 | full read |
| FRC-AIAUDIT-2025 | AI in Audit: illustrative example and documentation guidance | FRC (UK) | regulator | https://media.frc.org.uk/documents/AI_in_Audit.pdf | 2025-06-26 | full read |
| FRC-ATT-2025 | Thematic Review: Certification of Automated Tools and Techniques | FRC (UK) | regulator | https://media.frc.org.uk/documents/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf | 2025-06-26 | full read |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: risks, mitigations and illustrative examples | FRC (UK) | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full read |
| FRC-GENAINEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies (news release) | FRC (UK) | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 | full read |
| IFIAR-SURVEY-2026 | Survey of Inspection Findings 2025 (14th annual survey) | IFIAR (read via the Japan FSA mirror) | regulator | https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf | 2026-04-01 | The landscape held this at snippet level; the full PDF was read here. |
| IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution | IFIAR (read via the Japan FSA mirror) | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 | full read |
| IFIAR-TTF-2026 | Use of technology in audits: Innovation and audit quality | IFIAR (read via the Japan FSA mirror) | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf | 2026-04-20 | New since the landscape scan, which listed only the 2025 report. |
| IRBA-AI-2024 | Artificial Intelligence Audit Risks Mitigation Update (communique) | IRBA (South Africa) | regulator | https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf | 2024-09-19 | full read |
| PCAOB-CONFIRM-2023 | Notice of Filing of Proposed Rules on the Auditor's Use of Confirmation, and Other Amendments to Related PCAOB Standards (Federal Register, Board action of 28 Sep 2023) | PCAOB; SEC (Federal Register) | regulator | https://www.govinfo.gov/content/pkg/FR-2023-10-17/pdf/2023-22491.pdf | 2023-10-17 | full read |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting | PCAOB (staff) | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 | full read |
| PCAOB-PRIORITIES-2024 | Spotlight: Staff Priorities for 2025 Inspections and Interactions With Audit Committees | PCAOB (staff) | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf | 2024-12 | full read |
| PCAOB-TAA-2024 | Notice of Filing of Proposed Rules on Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 54922; carries the Board's adopting-release text, Release 2024-007) | PCAOB; SEC (Federal Register) | regulator | https://www.govinfo.gov/content/pkg/FR-2024-07-02/pdf/2024-14488.pdf | 2024-07-02 | The PCAOB adopting-release PDF returned 404; this Federal Register copy was read instead. |
| SEC-TAAORDER-2024 | Order Granting Approval of Amendments Related to Aspects of Designing and Performing Audit Procedures That Involve Technology-Assisted Analysis of Information in Electronic Form (89 FR 68218) | SEC (Federal Register) | regulator | https://www.govinfo.gov/content/pkg/FR-2024-08-23/pdf/2024-18986.pdf | 2024-08-23 | full read |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing (release on the practice aid Artificial Intelligence (AI) Considerations for Financial Statement Auditors) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | Release read; the practice aid itself needs a login. |
| IAASB-ED330-2026 | Exposure Draft: Proposed ISA 330 (Revised), The Auditor's Responses to Assessed Risks, with explanatory memorandum | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-330-Exposure-Draft.pdf | 2026-08-05 | full read |
| IAASB-ED500-2026 | Exposure Draft: Proposed ISA 500 (Revised), Audit Evidence, with explanatory memorandum | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf | 2026-08-05 | full read |
| IAASB-ED520-2026 | Exposure Draft: Proposed ISA 520 (Revised), Analytical Procedures, with explanatory memorandum | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-520-Exposure-Draft.pdf | 2026-08-05 | full read |
| IAASB-EDOVERALL-2026 | Explanatory Memorandum to the Exposure Drafts for the Audit Evidence and Risk Response Project (overall) | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-Overall-Project-Exposure-Draft.pdf | 2026-08-05 | full read |
| IAASB-EDPAGE-2026 | Proposed Revisions for Audit Evidence & Risk Response: ISA 330, ISA 500 & ISA 520 (consultation page) | IAASB | standard-setter | https://www.iaasb.org/publications/proposed-revisions-audit-evidence-risk-response-isa-330-isa-500-isa-520 | 2026-08-05 | full read |
| IAASB-ISA240-2025 | IAASB Revises Fraud Standard to Enhance Public Trust (press release on ISA 240 (Revised)) | IAASB | standard-setter | https://www.iaasb.org/news-events/2025-07/iaasb-revises-fraud-standard-enhance-public-trust | 2025-07-08 | Final ISA 240 (Revised) text was not reachable (mirror returned 403); only the press release and cross-references in the 2026 exposure drafts were read. |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (Audit Benchmark Survey, 54 US firms with complete data) | CPA.com / AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full read |
| GARTNER-2026 | Gartner Survey Shows Audit Departments Are Embracing AI and Data Analytics to Drive Innovation in 2026 (survey of 119 chief audit executives, Aug 2025) | Gartner | survey | https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-01-27-gartner-survey-shows-audit-departments-are-embracing-ai-and-data-analytics-to-drive-innovation-in-2026 | 2026-01-27 | Internal audit functions, not external audit. |
| GARTNER-AUG-2026 | Gartner Survey Finds Audit Teams' AI Use is Common, But Most Teams are Lacking Strategic Adoption and Application (webinar poll, 743 audit professionals) | Gartner | survey | https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-08-10-gartner-survey-finds-audit-teams-ai-use-is-common-but-most | 2026-08-11 | Internal audit audience; the landscape held this at snippet level. |
| CASEWARE-VERITY-2026 | From AiDA to agentic: How Caseware's AI has evolved (Caseware Verity) | Caseware | vendor | https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved | 2026-07-28 | full read |
| MINDBRIDGE-ARA-2026 | MindBridge Advances Financial Oversight for the Agentic Era with New Platform Capabilities (press release) | MindBridge Analytics | vendor | https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/ | 2026-09-22 | full read |
| TR-AGENTIC-2025 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows (press release) | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows | 2025-11-05 | full read |

---

## 6. Gaps

- **No independent measurement of AI substantive-tool quality in live audits.** No regulator, academic study or named firm published error rates, override rates, parallel-run results or inspection findings specific to AI tools in substantive testing. IFIAR's 2025 survey of inspection findings has no AI-specific category; its new firm-level category on technological resources is not AI-specific either (IFIAR-SURVEY-2026, Appendix A).
- **The randomized field experiment on LLMs and audit quality (inventory valuation task, 100 professional auditors, SSRN 6095166, from the landscape) could not be opened.** SSRN presented a bot check and the web-search budget ran out before another route could be found. It is not used as evidence anywhere in this file.
- **PCAOB sources.** The adopting-release PDF for Release 2024-007 returned 404; the Federal Register copies were used. The staff Spotlights on 2020-2022 inspection observations that the Board cites for technology-assisted analysis deficiencies (PCAOB-TAA-2024, footnote 19) were not opened, so the specific noncompliance findings behind AS 1105.10A and AS 2301.49-.50 are second-hand. A 2026 PCAOB inspection-priorities Spotlight and the outputs of the Board's data and technology research project were not found. The status of the substantive analytical procedures project after Aug 2024 was not checked. The SEC's approval of the confirmation standard was not confirmed (PCAOB-CONFIRM-2023 is the Board's filing).
- **ISA 240 (Revised) final text and basis for conclusions** were not opened (the mirror returned 403); technology content is known only from the press release and the 2026 drafts' cross-reference to paragraph A129 (IAASB-ISA240-2025; IAASB-ED500-2026, application material A15 and footnote 17). IAASB comment letters (due 2026-12-15), webinar recordings and future non-authoritative technology guidance do not exist yet.
- **IFIAR 2025 values** for each area are read from a chart without data labels (IFIAR-TTF-2026, p.10); only 2023 and 2024 are tabulated.
- **Benchmarks are on synthetic or pseudo-labelled data.** FinancialAuditBench uses synthetic engagements and has Modus Audit Inc. co-authors; AuditCopilot's real-data labels come from the rules-based test it is compared with, and its printed precision and recall columns do not reconcile to its counts; the Polish study uses one capital group, general chat models and prompts tuned on the same 167 samples. None is an independent field measure.
- **Vendor and firm figures are single claims.** The 16-hour to five-or-six-hour figure is one practitioner's estimate in a vendor release (TR-AGENTIC-2025); "up to 70% faster" has no sample or baseline. DataSnipper, Circit, Fieldguide and other vendors were not opened here; those belong to the practice angle. EY and Deloitte items were read through a trade-press copy, not the firms' own releases.
- **Not reached or not opened:** ACRA's guidance PDF (announcement page only); the CEAOB October 2024 report cited by AFM; NFRA India's principles (from the landscape); Big Four transparency reports and the FRC's annual audit-quality review; the AICPA practice aid text (login).
- **Absent source types for this angle.** No conference proceedings, podcasts, community discussions or job postings were collected here (the angle is regulators, standard-setters, academics and surveys). A registered-report proposal on generative AI automation and auditor motivation (Holmstrom and Peters, PCAOB research conference) was read but is undated on the document and reports no results, so it is not cited.
- **Data conflicts carried forward from the landscape:** whether EY's "all phases now" and "end-to-end by 2028" describe the same state (EY-CANVAS-2026 says both); the KPMG fee figures, which appear only in a secondary report (THEFINANCESTORY-KPMGFEE-2026).
