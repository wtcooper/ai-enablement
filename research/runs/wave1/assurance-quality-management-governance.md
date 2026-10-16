# Module deep dive: assurance / quality-management, angle: governance & evidence

- **Archetype:** assurance
- **Module:** quality-management. Firm-level quality management of AI (ISQM 1 / PCAOB QC 1000: tool certification and approval, governance, methodology, monitoring and remediation, resourcing) and engagement-level supervision and review of AI output (review control points, automation bias, documentation of AI use), plus interaction with inspectors.
- **Angle:** governance & evidence. What constrains and measures the work: the FRC thematic review and generative and agentic AI guidance, PCAOB QC 1000 and its inspection approach, IAASB technology work, IFIAR's technology report and survey, AICPA guidance, NFRA, CPAB and other inspectors, academic work on automation bias and review of AI output, and surveys.
- **Prepared:** 2026-10-16
- **Method note.** 56 sources are listed in section 5 and every one was opened and read with `curl` through the session proxy (`pdftotext` for PDFs). Where I opened only a landing page or a secondary report of a primary document, the source title says so. Nothing in this file rests on a search-result snippet. Long PDFs (the FRC guidance, the AFM report, the IFIAR survey, the two Deloitte UK transparency reports) were read for the relevant sections, not line by line. Web search was used six times, to find primary pages, and then the shared search quota ran out. Figures keep their source's denominators; where a source does not state one, the `measures` field says so.
- **Grade convention.** No entry reaches grade A, because no firm or regulator has published a measured outcome of AI tool governance or AI-output review at a named organisation. Grade B means a named firm describes the deployment without a measure. Grade C means a regulator observed or recommended the practice at firms it does not name; that is independent, but it cannot meet the named-organisation test for B. Grade D means an idea that regulators or researchers discuss and that no source shows in use. Entries whose evidence is a regulator's recommendation say so in `notes`.

---
## 1. Summary

**What the rules say (October 2026).** No regulator or standard-setter read here prohibits AI in audit, none has created AI-specific quality-management requirements, and every one says the firm and the signing auditor stay accountable.
- **The existing quality-management standards are the route.** ISQM 1 and its national versions (ISQM (UK) 1, CSQM 1, the Australian ASQM 1) require tools to be appropriately obtained or developed, implemented, maintained and used. The AUASB cites subparagraph 32(f) of ASQM 1 and CPAB cites CSQM 1 paragraph 32(f)-(g) (AUASB-AI-2025; CPAB-AI-2024, p. 2).
- **FRC (UK) is the most operational.** Its March 2026 guidance sorts audit-quality risk into deficient output, misuse of output and non-compliant methodology, and sets four mitigations: system design, certification, staff education and governance, and human review and oversight at control points (FRC-GENAI-2026, pp. 4-6, 21-40). It says it is "not a response to identified quality deficiencies" (FRC-GENAINEWS-2026). Its June 2025 thematic review of the six largest firms found certification processes in place but no formal monitoring of audit-quality impact (FRC-ATT-2025).
- **IFIAR (the regulators' forum) published a second technology report on 20 April 2026** that the landscape did not have. It says audits should stay "human-led", asks firms to define what that means in practice, and lists emerging monitoring metrics. The six networks together reported about 30% more AI-enabled tools in 2025 than in 2024, with the caveat that firms report differently (IFIAR-TTF-2026, pp. 5-9).
- **IAASB has a dated plan.** It approved non-authoritative material in December 2025 and an action plan in March 2026. A five-guide series on GenAI-enabled tools (including agentic) is to be drafted from mid-2026, with completed guides approved through to June 2027, and no new requirements (IAASB-MINDEC-2025, paras 33-39; IAASB-TQMPLAN-2026, paras 12-18, Table 2; IAASB-MINJUN-2026, paras 28-31). The decision followed roundtables in the second half of 2025 with more than 240 stakeholders (IAASB-TQM-2026). The workstream's working hypothesis is that the existing principles-based quality-management standards, with added support, can manage the risks of opaque tools (IAASB-TQMWS-2026), and the IAASB keeps a technology catalog of issues that it updates at least semi-annually (IAASB-CATALOG-2026).
- **PCAOB QC 1000** still takes effect on 15 December 2026. Amendments adopted on 9 September 2026 loosen role assignment, drop the external quality control function for larger firms and narrow when a deficiency must be evaluated across other engagements; they take effect at the same time only if the SEC approves them, and secondary sources as of 8 October 2026 still show approval pending (DART-QC1000-2026; EISNER-QC1000-2026). This settles the landscape's open question.
- **AICPA (13 October 2026)** added firm-level expectations in Part 2 of its practice aid: assign who builds or buys AI tools, authorise them, set acceptable-use policy, and revalidate and monitor them periodically (AICPA-PA-2026; AT-AICPAPA-2026).

**What inspections and surveys show.**
- **Certification exists; impact monitoring largely does not.** At the six largest UK firms there was no formal monitoring that quantified audit-quality impact, and only one firm reported tool usage against targets (FRC-ATT-2025). A Dutch review found usage for 74% of tools was estimated, 20% based on actual data and 6% unclear (AFM-12BB-2025, p. 15).
- **Regulators still find misuse.** 31% of IFIAR members reported findings that a tool was not used as intended in the 2024 survey (29% in 2023); the most common were misread results and thin testing of outliers (IFIAR-TTF-2025, pp. 5-6). CPAB's 2025 inspections found tools used as the primary source of evidence with limited validation of input data in some cases, and one tool where testing stopped at flagged items (CPAB-EVOLVING-2025, p. 1).
- **The firm-level technology theme is a small part of the inspected system.** In IFIAR's 2025 survey of firm-wide quality management, 11 member firms (9% as reported) had a finding under "Resources: technological, intellectual, service providers", against 42 (32%) under monitoring and remediation and 49 (37%) under engagement performance. 35% of listed PIE audits inspected had at least one finding, up from 26% in 2022 (IFIAR-SURVEY-2026, p. 2; Table A.2). Percentages use per-theme denominators the table does not state.
- **Inspectors are turning toward the firm's system.** The FRC says its revised supervision puts the firm's system of quality management "at the heart" of supervision, starting with the largest firms in April 2026 (FRC-SUPERVISION-2026). PCAOB staff discussion materials, as reported, would centre inspections on each firm's quality control system, with early AI pilots in inspection work (STARLING-IMC-2026). That makes the governance of AI tools the thing inspectors test.

**Quality evidence is absent, and what exists cuts both ways.** No firm or regulator has published an error rate, override rate, seeded-error test or parallel-run result for AI tool output or its review. The nearest independent evidence is a lab experiment where auditors were less sceptical relying on automated work than on a colleague's (PETERS-2022), an opposite finding of algorithm aversion where AI contradicted management's estimate (COMMERFORD-2022), a pre-generative-AI association between AI hiring and fewer restatements (FEDYK-2022), and a benchmark where agents sometimes wrote incorrect workpaper documentation (ARXIV-FAB-2026).

**Output.** 22 use cases: 0 grade A, 8 grade B, 8 grade C, 6 grade D (idea). By maturity: 12 in production, 3 piloting, 1 announced, 6 emerging. Only Deloitte UK, KPMG and RSM (and PIA Group, in one interview) are named as operating governed AI tools in this module; PwC and EY material on tool governance was not reached.

---
## 2. Use cases

```yaml
- id: assurance-quality-management-01
  title: "Certify GenAI and agentic audit tools per use case, with a central board that approves tools before pilot and recertifies on change"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Firm quality-management processes were built for transparent, deterministic tools. The IAASB's action plan describes opacity, non-determinism and adaptivity as the traits that make it hard to decide how much testing is enough before deployment and how to monitor afterwards (IAASB-TQMPLAN-2026). The FRC's review of the six largest UK firms found certification processes were generally in place for automated tools but were still being updated for AI-specific risks (FRC-ATT-2025)."
  solution: "The tool is certified in the context of a use case: inputs (prompts, information sources), architecture and component logic, and output testing on default, edge, diverse and known-weakness cases, often with structured criteria, are evaluated, and recertification is triggered by material changes to components or inputs, a materially different use case, observed performance issues, changed standards or elapsed time (FRC-GENAI-2026). At Deloitte UK a Technology Controls Board, set up in April 2026, reviews technology artefacts before they are approved for pilot and deployment, drawing on the FRC's 2025 thematic review and ISQM (UK) 1 (DELOITTE-UKTR-2026)."
  outcomes:
    - { lever: risk, description: "Deloitte UK states that all new tools are subject to quality assessment before deployment as part of its system of quality management, and that this enhances the quality of the deployed tool. No measure is given.", figure: "none published", measures: "n/a (qualitative statement)", provenance: self-reported, source_ref: DELOITTE-UKTR-2025 }
    - { lever: risk, description: "The FRC reported that most of the six largest UK firms had well-established certification processes for automated tools, with some less mature and not backed by documented policies. No count is given beyond 'most'.", figure: "no count beyond 'most firms'", measures: "firms among the six reviewed with an established ATT certification process", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "Inventory of tools and a named owner for each"
    - "Methodology-team sign-off built into the certification record"
    - "Test sets and structured scoring criteria for LLM outputs"
    - "A defined list of recertification triggers (model update, new use case, standards change)"
  risks_and_guardrails:
    - "LLM training data usually cannot be obtained by the firm, so the FRC says output testing may carry more weight in certification (FRC-GENAI-2026, pp. 30-32)"
    - "FRC's review snapshot is from Q2 2024 information requests, when generative AI at the six firms was limited to productivity aids such as chatbots rather than ATTs as defined in the review (FRC-ATT-2025, Emerging technology section)"
    - "NFRA principles, as reported, say pre-deployment approval is only a starting point and material changes such as model updates or vendor changes should trigger revalidation (NFRA-CAALLEY-2026)"
    - "Recertification triggers were generally identified informally by tool owners; two firms ran annual owner confirmations and one set a three-year backstop (FRC-ATT-2025, Maintenance and monitoring)"
  human_checkpoints:
    - "Tool owner, methodology team and business approvals before certification"
    - "Central board approval before pilot and again before deployment"
    - "Engagement team assesses engagement-specific tools on the file"
  role_evolution: "Methodology teams sign off in the certification record at most of the six firms (FRC-ATT-2025). The FRC guidance expects methodology and technology teams to work together through development (FRC-GENAI-2026, p. 40). Deloitte UK has created a dedicated board for technology risk (DELOITTE-UKTR-2026, PDF p. 48)."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 30-33 (Certification); p. 40 (methodology)" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Observations: Certification and implementation; Maintenance and monitoring; Appendix C" }
    - { ref: DELOITTE-UKTR-2026, title: "Deloitte UK annual review 2026: Audit transparency report (year ended 31 May 2026)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: 2026-09, access: full, locator: "PDF p. 48 (Technology Controls Board)" }
    - { ref: DELOITTE-UKTR-2025, title: "Deloitte UK annual review 2025: Audit transparency report (year ended 31 May 2025)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf", date: 2025-09, access: full, locator: "PDF p. 95 (quality assessment before deployment)" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F, approved March 2026)", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "paras 5-10 (characteristics and challenges), para 20" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened)", publisher: "CAalley (reproducing ET CFO)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Governance must come before deployment'" }
  last_reviewed: 2026-10-16
  notes: "Grade B rests on one named firm (Deloitte UK) with no published measure. The FRC findings are about ATTs generally and the firms are not named. The Deloitte UK description of the board's scope is one paragraph; its composition and decision record are not published."

- id: assurance-quality-management-02
  title: "Triage AI tool proposals by risk tier so that low-risk aids and agentic tools that select or test samples get different scrutiny"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance ]
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Most of the six largest UK firms applied one central certification process to every ATT regardless of its assessed risk or impact (FRC-ATT-2025). With generative tools proliferating, the same process would either slow low-risk aids or under-scrutinise high-risk agents."
  solution: "Deloitte UK describes GenAI use-case governance with risk thresholding, triage and a clearing house, within a globally consistent Trustworthy AI framework (DELOITTE-UKTR-2025). NFRA's principles, as reported, say validation, certification and review should be proportionate: translation aids are low risk, agentic tools that select and test samples are higher risk (NFRA-CAALLEY-2026). The FRC guidance says firms may be more prescriptive where an output deficiency would significantly harm audit quality or review is unlikely to catch it (FRC-GENAI-2026, p. 36)."
  outcomes:
    - { lever: risk, description: "No outcome published for tiering. Deloitte UK lists it among its responses to a rated GenAI risk.", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: DELOITTE-UKTR-2025 }
  prerequisites:
    - "A tier definition tied to the effect of a wrong output on audit evidence or conclusions"
    - "A clearing-house owner with authority to say no"
    - "Certification depth set per tier"
  risks_and_guardrails:
    - "FRC: narrow use-case lists make tools easier to design, test and teach, but cap the value obtained (FRC-GENAI-2026, p. 35)"
    - "Tiering relies on the firm correctly judging an output's role; the FRC notes that an LLM can play several roles at once depending on the prompt (FRC-GENAI-2026, p. 9)"
  human_checkpoints:
    - "Clearing-house decision on tier before build or purchase"
    - "Higher tiers add engagement-level approval and defined review activities"
  role_evolution: "A central risk or clearing-house function decides which proposals proceed and at what depth of testing (DELOITTE-UKTR-2025, PDF p. 101)."
  evidence_grade: B
  sources:
    - { ref: DELOITTE-UKTR-2025, title: "Deloitte UK annual review 2025: Audit transparency report (year ended 31 May 2025)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf", date: 2025-09, access: full, locator: "PDF p. 101 (Generative AI risk: key responses)" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened)", publisher: "CAalley (reproducing ET CFO)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Risk based governance for audit technology'" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Certification and implementation: Application of certification processes" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 35-36" }
  last_reviewed: 2026-10-16
  notes: "Single named firm, one line of description. NFRA is read through a press report; the NFRA text was not opened."

- id: assurance-quality-management-03
  title: "Pre-release evaluation sets, parallel runs and benchmark tests for audit agents (idea)"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, software-systems ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "Tolerance for deficient outputs is a professional judgement, tests of LLM outputs are often qualitative, and no public benchmark or firm result says how often an audit agent's output is wrong in live use (FRC-GENAI-2026, p. 32). An academic benchmark finds agents can write incorrect documentation or perform inappropriate procedures (ARXIV-FAB-2026)."
  solution: "Firms build representative test sets and score tool output against them before release and after each model change. IFIAR lists emerging practice such as benchmarking tool-driven results against traditional methods, with metrics like false-positive and false-negative rates versus a manual sample, rework rates and escalation incidence (IFIAR-TTF-2026, pp. 8-9). During limited deployment, the FRC says teams often perform the alternative procedures in full in parallel, and the AUASB suggests running a tool in parallel with other procedures in its first year on an engagement (FRC-GENAI-2026, p. 33; AUASB-AI-2025)."
  outcomes:
    - { lever: quality, description: "Independent benchmark, not a firm result: eleven frontier models on audit workpaper completion and review tasks complete substantial portions of staff-level work but sometimes perform inappropriate procedures or write incorrect documentation. No pass rate is quoted in the abstract.", figure: "no figure in abstract", measures: "90 tasks across six synthetic engagements, about 179 files each, eleven models evaluated", provenance: independent, source_ref: ARXIV-FAB-2026 }
  prerequisites:
    - "A held-out set of engagements or contracts with known answers (synthetic or de-identified)"
    - "Agreed scoring criteria written before testing"
    - "A rule for what failure rate blocks release"
  risks_and_guardrails:
    - "Synthetic tasks may not reflect live client data; the benchmark authors built theirs from differentially private statistics of historical audits (ARXIV-FAB-2026)"
    - "IFIAR cautions that its figures on AI-tool growth are subject to differing reporting practices across networks, and the same applies to any shared metric (IFIAR-TTF-2026, p. 5, footnote 1)"
    - "A passed test does not remove the need for review; the FRC ties tolerance for output deficiencies to the extent of human review (FRC-GENAI-2026, p. 32)"
  human_checkpoints:
    - "Methodology and technical audit specialists agree the pass criteria"
    - "Release decision by the certification body"
  role_evolution: "Evaluation becomes a standing task for technical audit specialists alongside methodology work; the FRC says outputs are often tested qualitatively with structured criteria (FRC-GENAI-2026, p. 32)."
  evidence_grade: D
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 32-33" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "pp. 8-9 (emerging practices)" }
    - { ref: AUASB-AI-2025, title: "Impact of AI on Auditors (web guidance)", publisher: "Auditing and Assurance Standards Board (Australia)", type: standard-setter, url: "https://www.auasb.gov.au/publications/impact-of-ai-on-auditors/", date: 2025-07, access: full, locator: "Considerations: Alternative procedures" }
    - { ref: ARXIV-FAB-2026, title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors", publisher: "arXiv", type: academic, url: "https://arxiv.org/abs/2609.32835", date: 2026-09-26, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Idea. Regulators describe the practice in general terms and one academic benchmark exists. No firm has published an evaluation result. The FRC statement that teams often run parallel procedures describes limited deployments in general, not a named firm."

- id: assurance-quality-management-04
  title: "Monitor tool usage and audit-quality impact through logs, dashboards and thematic reviews"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ data-reporting, review-assurance ]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Regulators report that firms rarely measure whether tools improve or harm audit quality. At the six largest UK firms, monitoring was mostly about usage counts for licensing and there was no formal monitoring to quantify audit-quality impact (FRC-ATT-2025). A Dutch review found usage estimated rather than measured for most tools (AFM-12BB-2025)."
  solution: "Tool logs and engagement metadata feed management information so a board can see where tools are used, how outliers they flag were handled, and whether staff fall back to old methods. IFIAR's examples of emerging practice include thematic reviews across engagements with defined metrics (engagement coverage, false-positive and false-negative rates against manual samples, rework, escalation), dashboards of tool use, and benchmarking against traditional methods (IFIAR-TTF-2026, pp. 8-9). In a good-practice example the AFM describes one (unnamed) audit firm using a dashboard that lets a board member see deviations and outliers found by an audit tool and how the auditor handled them (AFM-12BB-2025, p. 15)."
  outcomes:
    - { lever: quality, description: "AFM: for most auditing tools, engagement-level usage was estimated rather than measured.", figure: "74% estimated; 20% actual data; 6% unclear", measures: "share of audit tooling, by method of monitoring, across the tools in the AFM study (13 firms: 11 non-PIE, 2 PIE audit firms); the report labels the chart 'Method of monitoring in % of audit tooling'", provenance: independent, source_ref: AFM-12BB-2025 }
    - { lever: quality, description: "FRC: the six largest UK firms did not formally monitor audit-quality impact; generally no KPIs on ATT usage, and one firm reported usage against targets for certain key ATTs.", figure: "1 of 6 firms with usage targets", measures: "firms among the six reviewed that reported ATT usage against targets", provenance: independent, source_ref: FRC-ATT-2025 }
    - { lever: quality, description: "IFIAR: share of members reporting inspection findings that an automated tool was not used as intended (2024 survey; 29% in 2023). Common findings were misread results and thin testing of outliers.", figure: "31%", measures: "percentage of IFIAR members reporting such findings; the report does not state the denominator in the text read", provenance: independent, source_ref: IFIAR-TTF-2025 }
    - { lever: quality, description: "Academic, adjacent and pre-generative-AI: across the 36 largest audit firms, a one-standard-deviation change in recent AI investment (proxied by AI-worker employment) is associated with lower restatement likelihood.", figure: "-5.0% in the likelihood of an audit restatement; -0.9% audit fees", measures: "association from resume data on more than 310,000 individuals at 36 firms; not a measure of any one tool", provenance: independent, source_ref: FEDYK-2022 }
  prerequisites:
    - "Tools that log use and outputs by engagement"
    - "Defined KPIs agreed with quality leadership"
    - "A decision on whether network or member firm owns monitoring"
    - "Root-cause analysis capability for tool-related findings"
  risks_and_guardrails:
    - "IFIAR warns that monitoring split between networks and member firms can be fragmented, leaving incomplete coverage of tools and jurisdictions (IFIAR-TTF-2026, p. 8)"
    - "Usage monitoring is not impact monitoring: the FRC found firms mainly counted teams using a tool, typically for licensing (FRC-ATT-2025)"
    - "The Fedyk study measures AI-worker investment before generative AI and cannot be read as the effect of a given tool (FEDYK-2022)"
  human_checkpoints:
    - "Quality leadership reviews tool-impact metrics periodically"
    - "Technical experts review sampled engagements for incorrect use"
  role_evolution: "Quality and methodology staff gain a data-analysis task: reading tool telemetry alongside inspection findings (AFM-12BB-2025, p. 15)."
  evidence_grade: C
  sources:
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Maintenance and monitoring: Monitoring the use and impact of ATTs" }
    - { ref: AFM-12BB-2025, title: "12 Building blocks for controlled use of auditing tools", publisher: "Autoriteit Financiele Markten (Netherlands)", type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "pp. 14-15 (Building block 3)" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution (2025 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "p. 5-6 (findings; ISQM 1 factor 1)" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "pp. 8-9" }
    - { ref: FEDYK-2022, title: "Is artificial intelligence improving the audit process? (abstract page)", publisher: "Review of Accounting Studies (via RePEc)", type: academic, url: "https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html", date: 2022, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Grade C: regulator-observed practice at firms the regulators do not name, plus one unnamed good-practice dashboard. This cannot meet the named-organisation test for B, but it is independent observation rather than a vendor claim."

- id: assurance-quality-management-05
  title: "Allocate certification and monitoring duties between the global network and each member firm"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ coordination-scheduling, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Tools are often built or bought at network level, but ISQM 1 applies to each firm. IFIAR members said it is sometimes unclear whether monitoring belongs to the network that built a tool or the member firm using it (IFIAR-TTF-2025, p. 6), and found networks organised differently (IFIAR-TTF-2026, p. 8)."
  solution: "Firms define who certifies, who owns the tool, who monitors and how feedback flows back. In the UK review, two firms required globally certified tools to have a UK owner and UK-level certification (relying in part on global steps), while others did no extra UK testing (FRC-ATT-2025). The IAASB's planned guides map responsibilities across network, firm and engagement team and stress that the firm keeps responsibility for approving tools and monitoring them wherever the work is done (IAASB-TQMPLAN-2026, paras 28-29)."
  outcomes:
    - { lever: risk, description: "IFIAR observed differing approaches: monitoring led globally in some networks and by member firms in others, with a risk of fragmented, incomplete coverage. No count given.", figure: "none published", measures: "n/a", provenance: independent, source_ref: IFIAR-TTF-2026 }
  prerequisites:
    - "A responsibility matrix per tool (network, firm, engagement)"
    - "Channels for member-firm issues to reach the network tool owner"
    - "For group audits, a rule for reviewing component teams' certified tools"
  risks_and_guardrails:
    - "ISQM 1 requires the firm to consider the effect of network monitoring on its own monitoring; the firm remains responsible for its system of quality management (IAASB-TQMPLAN-2026, fn. 7 and para 29)"
    - "UK groups that find a component team used an uncertified tool were generally required to understand and review the component firm's certification (FRC-ATT-2025, Group audits)"
  human_checkpoints:
    - "Member-firm tool owner confirms local fit before use"
    - "Group engagement team reviews component use of tools"
  role_evolution: "Member firms take 'tool owner' roles for network-built tools (FRC-ATT-2025). The IAASB expects firms of different sizes to apply the guides proportionately (IAASB-TQMPLAN-2026, para 16)."
  evidence_grade: C
  sources:
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution (2025 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "p. 6 (factor 1)" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p. 8" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Global versus UK certification; Group audits" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F, approved March 2026)", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "paras 25-29, Table 1" }
  last_reviewed: 2026-10-16
  notes: "Regulator-observed, firms anonymised. The IAASB table is a plan, not observed practice."

- id: assurance-quality-management-06
  title: "Due diligence, contracting and revalidation for third-party AI tools and foundation models"
  archetype: assurance
  module: quality-management
  function: procurement-supply-chain
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Firms generally obtain the foundation model from a third party, and the FRC says training data and component logic often cannot be evaluated by the firm (IAASB-TQMPLAN-2026, para 25; FRC-GENAI-2026, pp. 30-31). The AFM found vendor management and information-security frameworks needed formalising at several firms (AFM-12BB-2025, p. 5)."
  solution: "Vendor checks go beyond functionality: control environment, data security, confidentiality and third-party assurance reports, with contract terms on data protection, IP, explainability documentation, audit rights and continuity. Where information cannot be obtained, the FRC says the firm may rely on independent assurance and may test more itself (FRC-AIAUDIT-2025, pp. 13-15; FRC-GENAI-2026, pp. 30-32). CPAB points to a SOC 2 report over IT general controls for off-the-shelf tools (CPAB-AI-2024, p. 2, fn. 3). NFRA's principles, as reported, call for contract terms on data protection, IP, explainability documentation, audit rights and business continuity, and for network-level due diligence to be demonstrable when tools are centrally contracted (NFRA-CAALLEY-2026)."
  outcomes:
    - { lever: risk, description: "In the FRC review all six firms considered vendor control environments, data security and confidentiality when selecting third-party ATTs. The AFM found formalised vendor management needed attention at several firms. Neither gives a count.", figure: "none published", measures: "n/a", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "A vendor questionnaire covering model changes, logging and sub-processors"
    - "A rule for when independent assurance is required"
    - "Contract right to notice of material model updates"
  risks_and_guardrails:
    - "NFRA, as reported, says a firm cannot rely on a vendor's terms of service, without validation, as a substitute for protecting client data (NFRA-CAALLEY-2026)"
    - "ICAEW's technology faculty chair noted the FRC guidance gives little on questions to put to vendors, though most audit AI tools are features added to existing products (ICAEW-FRCVIEW-2026)"
  human_checkpoints:
    - "Procurement, information security and methodology approve the vendor"
    - "Firm re-approves when the vendor changes the model"
  role_evolution: "Procurement and information-security teams join methodology and audit technology teams in tool approval (FRC-ATT-2025, Design or selection)."
  evidence_grade: C
  sources:
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Design or selection: Sourcing" }
    - { ref: FRC-AIAUDIT-2025, title: "AI in audit: Illustrative example and documentation guidance", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf", date: 2025-06-26, access: full, locator: "pp. 13-15 (third-party considerations)" }
    - { ref: AFM-12BB-2025, title: "12 Building blocks for controlled use of auditing tools", publisher: "Autoriteit Financiele Markten (Netherlands)", type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "p. 5" }
    - { ref: CPAB-AI-2024, title: "The use of artificial intelligence in the audit: balancing innovation and risk (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf", date: 2024-09-12, access: full, locator: "p. 2" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened)", publisher: "CAalley (reproducing ET CFO)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Greater scrutiny of technology vendors'" }
    - { ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC guidance on generative and agentic AI? (viewpoint)", publisher: "ICAEW", type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05, access: full, locator: "section 'Misinterpretation or misuse...'" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F, approved March 2026)", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "para 25" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 30-32" }
  last_reviewed: 2026-10-16
  notes: "Regulator-observed and principle-level; no named firm case."

- id: assurance-quality-management-07
  title: "Independent non-executive and executive oversight of AI risk inside the firm quality plan"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, coordination-scheduling ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "ISQM 1 places governance and leadership at the centre of the system of quality management, and the IAASB records that using AI-enabled tools reaches beyond the technological-resources objective into governance, resources, acceptance, ethics and engagement performance (IAASB-TQMPLAN-2026, para 9)."
  solution: "Deloitte UK's independent Audit Governance Board reviewed the firm's Single Quality Plan, which had evolved to cover AI, and discussed governance of increasing AI use in audit with a 'human in the loop' central to the approach (DELOITTE-UKTR-2026, PDF p. 7). The firm also has a UK Chief AI Officer responsible for embedding responsible AI governance across client services and internal operations (DELOITTE-UKTR-2026, PDF p. 27). IFIAR notes that some firms have begun to set up oversight committees and internal protocols to validate tool effectiveness, and suggests ethical governance structures such as AI oversight committees (IFIAR-TTF-2026, pp. 6-8)."
  outcomes:
    - { lever: risk, description: "No outcome published. The governance bodies and the board's AI-related discussions are described in the firm's transparency report.", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: DELOITTE-UKTR-2026 }
  prerequisites:
    - "A quality plan that names AI as a risk theme"
    - "Independent non-executives who can ask about tool governance"
    - "A standing agenda item and reporting metrics"
  risks_and_guardrails:
    - "IFIAR says practices vary significantly across jurisdictions and firms (IFIAR-TTF-2026, p. 8)"
    - "A board that sees only usage counts cannot judge quality impact (FRC-ATT-2025, Monitoring the use and impact of ATTs)"
  human_checkpoints:
    - "Board reviews AI governance themes in the quality plan"
    - "Escalation path from tool owners to the board"
  role_evolution: "A chief AI officer role appears in the firm's governance report (DELOITTE-UKTR-2026, PDF p. 27), and non-executives discuss AI governance in audit (DELOITTE-UKTR-2026, PDF p. 7)."
  evidence_grade: B
  sources:
    - { ref: DELOITTE-UKTR-2026, title: "Deloitte UK annual review 2026: Audit transparency report (year ended 31 May 2026)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: 2026-09, access: full, locator: "PDF pp. 7, 27, 48" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "pp. 6-8" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F, approved March 2026)", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "para 9" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Maintenance and monitoring: Monitoring the use and impact of ATTs" }
  last_reviewed: 2026-10-16
  notes: "One firm, descriptive. The Deloitte report is a firm-authored regulatory disclosure."

- id: assurance-quality-management-08
  title: "Role-differentiated AI training, competence records and a redesigned graduate programme"
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [ document-production, coordination-scheduling ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Staff who use or review AI tools need to know when a tool is appropriate, how to prompt it, how to review its output and the risk of automation bias; the FRC treats education as ongoing rather than a launch task (FRC-GENAI-2026, pp. 34-35). In a US small and mid-size firm benchmark, untrained staff was the most-cited barrier to adopting advanced approaches (CPACOM-ATR-2025)."
  solution: "Training is differentiated by user group and mapped to competencies, with records and refresher intervals set in proportion to risk (IFIAR-TTF-2026, p. 7). Deloitte UK describes AI fluency programmes with bespoke plans for different user groups (DELOITTE-UKTR-2025, PDF p. 101), a pilot reskilling programme in responsible AI use, and graduate training with audit simulations so trainees apply traditional methods alongside AI-assisted techniques (DELOITTE-UKTR-2026, PDF p. 5). NFRA's principles, as reported, call for preparers to be trained in safe use, reviewers in critical evaluation and bias awareness, and partners in governance and disclosure judgement (NFRA-CAALLEY-2026)."
  outcomes:
    - { lever: risk, description: "No outcome published. Small and mid-size firm survey for context: staff not trained in advanced approaches or methodologies was the top blocker.", figure: "66%", measures: "share of the 54 surveyed US CPA firms with complete data that ranked 'staff are not trained in advanced approaches or methodologies' among top blockers (chart 'Top ranked perceived blockers and risks the firm faces in moving forward with audit transformation'); the report says the survey is not representative", provenance: independent, source_ref: CPACOM-ATR-2025 }
  prerequisites:
    - "Role definitions for preparers, reviewers, partners"
    - "Training records tied to tool access"
    - "Known tool limitations from certification fed into training"
  risks_and_guardrails:
    - "FRC: training should include known performance issues of a tool, for example a tool that sounds confident when wrong (FRC-GENAI-2026, p. 35)"
    - "Researchers' registered-report design flags deskilling risk as audit work shifts from preparing to reviewing; no results are published (HOLMSTROM-2024)"
  human_checkpoints:
    - "Access to a tool conditional on completed training"
    - "Reviewer competence is matched to the use case (FRC-GENAI-2026, p. 37)"
  role_evolution: "Graduates start with AI-assisted work earlier but must still learn the underlying method; Deloitte UK describes simulations that combine both (DELOITTE-UKTR-2026, PDF p. 5)."
  evidence_grade: B
  sources:
    - { ref: DELOITTE-UKTR-2025, title: "Deloitte UK annual review 2025: Audit transparency report (year ended 31 May 2025)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf", date: 2025-09, access: full, locator: "PDF p. 101 (training plans)" }
    - { ref: DELOITTE-UKTR-2026, title: "Deloitte UK annual review 2026: Audit transparency report (year ended 31 May 2026)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: 2026-09, access: full, locator: "PDF p. 5" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p. 7" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened)", publisher: "CAalley (reproducing ET CFO)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Audit documentation and training to change'" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 34-35, 37" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report (CPA.com and AICPA 2025 Audit Benchmark Survey)", publisher: "CPA.com / AICPA", type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "PDF p. 8 (chart of top-ranked blockers); introduction (54 firms)" }
    - { ref: HOLMSTROM-2024, title: "How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal, PCAOB conference)", publisher: "PCAOB conference on auditing and capital markets (Holmstrom and Peters)", type: academic, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf", date: 2024-06, access: full, locator: "Introduction" }
  last_reviewed: 2026-10-16
  notes: "One named firm; no training-effect measure. The CPA.com figure is a barrier survey of small and mid-size firms, not a measure of training results."

- id: assurance-quality-management-09
  title: "Firm-approved guidance assistant for audit research and consultation, grounded in the firm's own manuals"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ research-synthesis ]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Auditors search methodology manuals, practice aids and technical guides for answers; inconsistent application of firm guidance is a quality risk, and generic chatbots can invent citations."
  solution: "RSM US launched Ask Luca in January 2026, a generative AI tool inside its RSM Luca audit ecosystem that gives guidance sourced from RSM assurance manuals, practice aids and technical accounting guides to its assurance professionals (RSM-ASKLUCA-2026). RSM's assurance digital leader says other firms deploying similar tools should ground them in firm-approved guidance with experienced human review (CAQ-RSM-2026). Deloitte UK launched a Research Assistant chatbot for audit research across its international content (DELOITTE-UKTR-2025, PDF p. 94). PCAOB staff heard in 2024 that some firms had built tools to research internal accounting and auditing guidance (PCAOB-GENAI-2024, p. 4)."
  outcomes:
    - { lever: capacity, description: "RSM says Ask Luca gives its assurance professionals access to firm-approved guidance; the release states reach but no time or quality measure.", figure: "4,000+ assurance professionals with access", measures: "number of RSM assurance professionals the release says the tool serves", provenance: self-reported, source_ref: RSM-ASKLUCA-2026 }
  prerequisites:
    - "Curated, version-controlled firm guidance as the retrieval source"
    - "Citations back to source passages"
    - "A route to escalate unanswered questions to technical consultation"
  risks_and_guardrails:
    - "CPAB expects auditors to verify the accuracy of any reference to professional standards or firm guidance obtained by querying a GPT model (CPAB-AI-2024, p. 3)"
    - "FRC lists hallucination, omission and distortion as output deficiencies of LLMs (FRC-GENAI-2026, p. 8)"
  human_checkpoints:
    - "Auditor checks cited source passages"
    - "Technical consultation remains the route for complex or novel questions"
  role_evolution: "Auditors spend less time searching and more on analysis, according to the firm (RSM-ASKLUCA-2026)."
  evidence_grade: B
  sources:
    - { ref: RSM-ASKLUCA-2026, title: "RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit (news release)", publisher: "RSM US", type: firm, url: "https://www.rsmus.com/newsroom/2026/rsm-launches-ask-luca.html", date: 2026-01-08, access: full, locator: "release text" }
    - { ref: CAQ-RSM-2026, title: "Shaping the future of assurance: Advancing AI in the audit (blog post by RSM's Assurance Digital Leader)", publisher: "Center for Audit Quality", type: professional-body, url: "https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit", date: 2026-08-25, access: full, locator: "section 'Ask Luca'" }
    - { ref: DELOITTE-UKTR-2025, title: "Deloitte UK annual review 2025: Audit transparency report (year ended 31 May 2025)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf", date: 2025-09, access: full, locator: "PDF p. 94" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", publisher: "PCAOB (staff)", type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p. 4" }
    - { ref: CPAB-AI-2024, title: "The use of artificial intelligence in the audit: balancing innovation and risk (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf", date: 2024-09-12, access: full, locator: "p. 3" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p. 8" }
  last_reviewed: 2026-10-16
  notes: "Two named firms, no measured effect on consistency or error rate. This sits on the boundary between quality management (methodology and consultation) and service delivery; the practice-angle analyst may also cover it."

- id: assurance-quality-management-10
  title: "AI-supported resourcing: staffing requests, budgets and engagement-leader review in one tool"
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [ coordination-scheduling ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "ISQM 1 requires firms to assign personnel with the competence and capacity to perform engagements. Manual staffing processes give limited visibility of engagement plans and resource fit."
  solution: "RSM describes Luca Resourcing as supporting initial staffing requests, budget planning and engagement-leader review, replacing manual processes with a connected tool (CAQ-RSM-2026). The post describes the tool's purpose and does not say how AI is used inside it."
  outcomes:
    - { lever: capacity, description: "No outcome published; the post says the tool improves visibility into engagement planning.", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: CAQ-RSM-2026 }
  prerequisites:
    - "Competence and skills data per person"
    - "Engagement risk and complexity indicators"
    - "Engagement leader sign-off"
  risks_and_guardrails:
    - "A resourcing tool must not assign unqualified staff to AI-heavy work; FRC says reviewers of AI output need appropriate competence, sometimes specialist expertise (FRC-GENAI-2026, p. 37)"
    - "The PCAOB's director of registration and inspections cited assigning personnel on the basis of the needs of the engagement as a feature of high-quality audits, per a Deloitte conference recap (DART-SECPCAOB-2025)"
  human_checkpoints:
    - "Engagement leader reviews and approves the staffing plan"
  role_evolution: "Engagement leaders review staffing and budgets inside a shared tool rather than through separate requests (CAQ-RSM-2026)."
  evidence_grade: B
  sources:
    - { ref: CAQ-RSM-2026, title: "Shaping the future of assurance: Advancing AI in the audit (blog post by RSM's Assurance Digital Leader)", publisher: "Center for Audit Quality", type: professional-body, url: "https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit", date: 2026-08-25, access: full, locator: "section 'RSM Luca Resourcing'" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p. 37" }
    - { ref: DART-SECPCAOB-2025, title: "Heads Up: 2025 AICPA & CIMA Conference on Current SEC and PCAOB Developments, key takeaways", publisher: "Deloitte DART", type: conference, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways", date: 2025-12, access: full, locator: "remarks of the PCAOB Division of Registration and Inspections director" }
  last_reviewed: 2026-10-16
  notes: "Single self-published source. The role of AI in the tool is not specified, so the ladder is set to assist as a floor."

- id: assurance-quality-management-11
  title: "Set out planned AI use and review expectations at engagement planning (idea)"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ coordination-scheduling, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Teams may use AI differently from one engagement to the next, and senior reviewers may not know where AI output sits in the file. IFIAR says firms need to make clear what a 'human-led' audit means in practice (IFIAR-TTF-2026, p. 7)."
  solution: "At the outset the engagement leader sets expectations for how technology will be used, including planned AI uses, and reviews them as the engagement progresses; at the end senior team members reflect on the overall use of technology and whether scepticism was maintained (IFIAR-TTF-2026, p. 7; CPAB-EVOLVING-2025, pp. 5-6). The AICPA's practice aid suggests teams may brainstorm at planning where AI could improve quality or efficiency (AT-AICPAPA-2026)."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "n/a", provenance: independent, source_ref: IFIAR-TTF-2026 }
  prerequisites:
    - "Firm policy listing approved tools per engagement type"
    - "Planning template with an AI-use section"
  risks_and_guardrails:
    - "AICPA: the engagement letter need not name AI tools under AU-C 210, but laws, contracts or firm policy may require disclosure (AT-AICPAPA-2026)"
    - "CPAB says firms often state the audit will remain human-led, but effective adoption needs a behaviour shift and clear articulation of involvement at each stage (CPAB-EVOLVING-2025, pp. 5-6)"
  human_checkpoints:
    - "Engagement leader approves the planned AI uses"
    - "Senior reviewer's end-of-audit reflection on technology use"
  role_evolution: "Engagement leaders take on an explicit planning duty for technology use; IFIAR and CPAB both describe engagement-leader and senior-team responsibilities for it (IFIAR-TTF-2026, p. 7; CPAB-EVOLVING-2025, p. 5)."
  evidence_grade: D
  sources:
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p. 7" }
    - { ref: CPAB-EVOLVING-2025, title: "The evolving use of technology in the audit (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: 2025-12-16, access: full, locator: "pp. 5-6" }
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "section on audit firms' use of AI" }
  last_reviewed: 2026-10-16
  notes: "Idea: regulator and professional-body expectations. No firm described this practice."

- id: assurance-quality-management-12
  title: "Human control points in agentic audit workflows, with dynamic escalation and approval before results are used"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "When agents run multi-step procedures, there is no single output to review: intermediate decisions, tool calls and escalations matter. The FRC identifies control-point decisions, including automation bias, as a source of deficient output (FRC-GENAI-2026, p. 16)."
  solution: "The FRC separates review of final outputs from oversight at control points, which occur when set criteria are met (for example an intermediate output is ready, the tool wants to act, or time passes), and its contract-review example lets the tool escalate when it is uncertain (FRC-GENAI-2026, pp. 38, 55). IFIAR asks firms to assign engagement personnel to decision checkpoints and to review autonomous decisions overall (IFIAR-TTF-2026, p. 7). Deloitte UK says its connected agentic network in Omnia runs workflows and engagement teams then assess, corroborate and approve results before use (DELOITTE-UKTR-2026, PDF p. 48). KPMG says AI agents in KPMG Clara perform audit tasks 'in concert with human review' under its Trusted AI framework (KPMG-TR-2025, PDF p. 16)."
  outcomes:
    - { lever: risk, description: "No outcome published. Firm statements describe design intent only.", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: KPMG-TR-2025 }
  prerequisites:
    - "Agent actions logged with stable references to source evidence"
    - "Defined escalation criteria and named decision owners"
    - "Reviewers trained on automation bias (FRC-GENAI-2026, p. 38)"
  risks_and_guardrails:
    - "IFIAR asks firms to consult members early where AI makes judgements or decisions without human involvement (IFIAR-TTF-2025, p. 8)"
    - "CPAB asks for alerts when technology makes decisions that could affect audit strategy and for a documented roadmap of steps taken (CPAB-EVOLVING-2025, pp. 5-6)"
    - "A control point can be defeated by automation bias in the person at it (FRC-GENAI-2026, p. 16)"
  human_checkpoints:
    - "Approval of preliminary conclusions before use"
    - "Dynamic escalation when the agent flags uncertainty"
    - "Senior review of overall use of technology"
  role_evolution: "Auditors move from preparing to overseeing agent work and deciding at control points (IFIAR-TTF-2026, p. 7; DELOITTE-UKTR-2026, PDF p. 48)."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 16, 38, 55" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p. 7" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution (2025 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "p. 8" }
    - { ref: CPAB-EVOLVING-2025, title: "The evolving use of technology in the audit (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: 2025-12-16, access: full, locator: "pp. 5-6" }
    - { ref: DELOITTE-UKTR-2026, title: "Deloitte UK annual review 2026: Audit transparency report (year ended 31 May 2026)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: 2026-09, access: full, locator: "PDF p. 48 (Technology)" }
    - { ref: KPMG-TR-2025, title: "KPMG International Transparency Report 2025: Building trust through quality and innovation", publisher: "KPMG International", type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/12/transparency-report-fy25.pdf", date: 2025-12, access: full, locator: "PDF p. 16" }
  last_reviewed: 2026-10-16
  notes: "Two named firms (Deloitte, KPMG) describe the design in transparency reports, with no published figure on control-point catches. The Deloitte agentic network is stated as integrated in early FY2027, that is, from June 2026. 'In production' reflects the firms' own wording of deployment and should be treated as self-reported."

- id: assurance-quality-management-13
  title: "Reviewer procedures for AI output: independent view first, source tie-back and mandatory validation steps"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "A confident, well-formatted AI output can pass review with less challenge than a junior's work; the AFM calls this a 'halo effect' and notes outputs can appear convincing (AFM-12BB-2025, pp. 31-32)."
  solution: "Review is built into the workflow. The FRC says review should assess whether output is appropriate for use, complete, accurate, internally consistent and consistent with the reviewer's understanding of the entity, and may start from an independent view (for example reading the source before accepting a summary) (FRC-GENAI-2026, p. 37). The FRC's board-minutes example makes the tool cite stable identifiers for every statement so reviewers can trace it (FRC-GENAI-2026, p. 44). CPAB's example has the auditor compare extracted contract data back to the original contract (CPAB-AI-2024, p. 4). The AFM saw good practice where each step in a fixed workflow can be completed only after the auditor confirms the output was reviewed and supported by underlying evidence (AFM-12BB-2025, pp. 31-32)."
  outcomes:
    - { lever: quality, description: "No measured detection or override rate has been published. The AFM calls out as bad practice a tool that presents a convincing conclusion that the auditor immediately includes in the file without clarity on data or reliability.", figure: "none published", measures: "n/a", provenance: independent, source_ref: AFM-12BB-2025 }
  prerequisites:
    - "Citations to source passages in tool output"
    - "Workflow gates that require reviewer confirmation"
    - "Defined review activities per tool in methodology"
  risks_and_guardrails:
    - "FRC: review effectiveness depends on reviewers having the competence to spot deficiencies, and the nature and extent of review is a judgement based on residual risk (FRC-GENAI-2026, p. 37)"
    - "FRC's contract-review example does not require the auditor to review every contract classification, only whether the output is consistent with their understanding of the entity (FRC-GENAI-2026, p. 55)"
  human_checkpoints:
    - "Reviewer confirmation gate on each AI-assisted step"
    - "Specialist review where the use case needs it"
  role_evolution: "Reviewers spend more time checking AI output against sources and less on drafting; PCAOB staff reported in 2024 that firms expected the same diligence in review whether or not GenAI was involved (PCAOB-GENAI-2024, p. 5)."
  evidence_grade: C
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 37, 44, 55" }
    - { ref: CPAB-AI-2024, title: "The use of artificial intelligence in the audit: balancing innovation and risk (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf", date: 2024-09-12, access: full, locator: "p. 4 (example)" }
    - { ref: AFM-12BB-2025, title: "12 Building blocks for controlled use of auditing tools", publisher: "Autoriteit Financiele Markten (Netherlands)", type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "pp. 30-32 (Building block 12)" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", publisher: "PCAOB (staff)", type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p. 5" }
  last_reviewed: 2026-10-16
  notes: "Grade C: the AFM good practice is observed but the firm is not named; FRC and CPAB examples are hypothetical."

- id: assurance-quality-management-14
  title: "Counter automation bias with structured prompts, forced independent judgement and psychological safety (idea)"
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Regulators and researchers expect auditors to over-rely on automated output. In an experiment, auditors relying on work done by automated tools were less sceptical than when relying on the same work done by a team member (PETERS-2022). A counter-bias also exists: auditors who received contradictory evidence from their firm's AI system proposed smaller adjustments to management's complex estimates than when it came from a human specialist (COMMERFORD-2022)."
  solution: "Prompts or workflow steps make the reviewer form a view first or argue against the tool's answer. In the Peters experiment a counterarguing mindset intervention reduced the effect, and no spill-over to a later task was found (PETERS-2022). The AFM saw auditors make their own fraud-risk assessment first and then use a GenAI tool to challenge it (AFM-12BB-2025, p. 31). A registered-report design tests whether an autonomous-motivation prompt offsets harm to judgement from GenAI automation; no results are published (HOLMSTROM-2024)."
  outcomes:
    - { lever: quality, description: "Independent experiment on automated tools in general (not generative AI): auditors were less sceptical relying on automated work than on a team member's; a counterarguing mindset intervention alleviated the effect. The abstract gives no effect size.", figure: "no figure in abstract", measures: "experiment with auditor participants; sample size not in the abstract read", provenance: independent, source_ref: PETERS-2022 }
  prerequisites:
    - "Reviewer training on automation bias (FRC-GENAI-2026, p. 35)"
    - "Tool UI that shows uncertainty or sources"
    - "A culture where challenging the tool is rewarded"
  risks_and_guardrails:
    - "The Peters work concerns automated tools and was not run on generative AI (PETERS-2022)"
    - "ICAEW's technology faculty chair said the FRC guidance covers automation bias in a single paragraph, despite long-term implications for professional judgement (ICAEW-FRCVIEW-2026)"
  human_checkpoints:
    - "Reviewer records an independent view before opening the AI output"
    - "Supervisor spot-checks the quality of challenge"
  role_evolution: "Reviewers are asked to challenge fluent output deliberately; the Nyenrode interview describes users needing to ask AI explicitly to challenge assumptions or it tends to agree (NYENRODE-2026)."
  evidence_grade: D
  sources:
    - { ref: PETERS-2022, title: "Auditor Automation Usage and Professional Skepticism (working paper)", publisher: "Tilburg University / SSRN", type: academic, url: "https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/", date: 2022-12-09, access: full, locator: "abstract" }
    - { ref: COMMERFORD-2022, title: "Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence (abstract page)", publisher: "Journal of Accounting Research (via RePEc)", type: academic, url: "https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html", date: 2022, access: full, locator: "abstract" }
    - { ref: HOLMSTROM-2024, title: "How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal, PCAOB conference)", publisher: "PCAOB conference on auditing and capital markets (Holmstrom and Peters)", type: academic, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf", date: 2024-06, access: full, locator: "Abstract and Introduction" }
    - { ref: AFM-12BB-2025, title: "12 Building blocks for controlled use of auditing tools", publisher: "Autoriteit Financiele Markten (Netherlands)", type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "p. 31 (good practice box)" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 35, 37" }
    - { ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC guidance on generative and agentic AI? (viewpoint)", publisher: "ICAEW", type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05, access: full, locator: "section 'Misinterpretation or misuse...'" }
    - { ref: NYENRODE-2026, title: "AI in auditing: balancing quality, professional skepticism, and responsibility (opinion; interview with the Group CIO of PIA Group and a Nyenrode professor)", publisher: "Nyenrode Business University", type: press, url: "https://www.nyenrode.nl/en/news/n/ai-auditing-quality-skepticism-responsibility", date: 2026-06-18, access: full, locator: "section 'What is automation bias...'" }
  last_reviewed: 2026-10-16
  notes: "Idea. The countermeasure is tested only in a lab setting. The Peters paper is a 2022 working paper on automation, and its status line reads 'in preparation'."

- id: assurance-quality-management-15
  title: "A second AI tool as critic of the first, with the auditor's supervision duty unchanged (idea)"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "Reviewing AI output at scale is slow, and the FRC lists 'critic' as one of the roles an LLM can play, including reviewing another LLM's output (FRC-GENAI-2026, p. 9)."
  solution: "One AI tool performs a procedure and another checks whether it was performed correctly and the result makes sense. The AICPA's practice aid says this is permitted but the second tool does not reduce or replace the auditor's responsibility for supervision and review (AT-AICPAPA-2026)."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "n/a", provenance: independent, source_ref: AT-AICPAPA-2026 }
  prerequisites:
    - "Different models or prompts for the two roles"
    - "Evidence of the checker's own performance from certification"
  risks_and_guardrails:
    - "A Group CIO interviewed by Nyenrode warns that using AI to validate AI can create a closed system in which errors become hard to detect (NYENRODE-2026)"
    - "FRC: combination risks include amplification, information distortion and interface errors between components (FRC-GENAI-2026, p. 14)"
  human_checkpoints:
    - "Auditor still supervises and reviews the outcome"
  role_evolution: "The auditor's review duties stay; the checker tool changes where review effort goes (AT-AICPAPA-2026)."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraph on one AI tool evaluating another" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 9, 14" }
    - { ref: NYENRODE-2026, title: "AI in auditing: balancing quality, professional skepticism, and responsibility (opinion; interview with the Group CIO of PIA Group and a Nyenrode professor)", publisher: "Nyenrode Business University", type: press, url: "https://www.nyenrode.nl/en/news/n/ai-auditing-quality-skepticism-responsibility", date: 2026-06-18, access: full, locator: "section 'When is AI reliable enough?'" }
  last_reviewed: 2026-10-16
  notes: "Idea: standard-setter permission plus practitioner caution; no named deployment of AI-on-AI review in audit found."

- id: assurance-quality-management-16
  title: "AI review of engagement files and working papers for omissions and inconsistencies before reviewer sign-off"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance, document-production ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Reviewers spend time on completeness and consistency checks that cost attention otherwise needed for judgemental areas. IFIAR's 2025 survey recorded 31 findings (2025) on failures to establish policies for sufficient, timely engagement supervision and review, up from 10 in 2024 (IFIAR-SURVEY-2026, Table A.3)."
  solution: "Deloitte UK has fully deployed Smart Review, an in-house GenAI-based audit review tool in its Omnia platform, to drive consistency and quality in internal-controls testing, and says all FTSE audits have access to it (DELOITTE-UKTR-2025, PDF pp. 7, 15, 94-95). KPMG says AI agents in KPMG Clara can review engagement documentation (KPMG-TR-2025, PDF p. 16). PIA Group's Group CIO describes AI running hundreds or more than a thousand checks on a single engagement file that previously went unperformed or were merely ticked off (NYENRODE-2026). PCAOB staff heard in 2024 that firms saw potential in evaluating audit documentation completeness against requirements (PCAOB-GENAI-2024, p. 4). FRC lists tools that review work for omissions or inconsistencies as 'other tools that use AI' needing documentation (FRC-AIAUDIT-2025, p. 6)."
  outcomes:
    - { lever: capacity, description: "Deloitte UK: reach of the tool within its audits. No accuracy or time measure.", figure: "all FTSE audits have access", measures: "audits in the firm's FTSE population with access to Smart Review, as the report states", provenance: self-reported, source_ref: DELOITTE-UKTR-2025 }
    - { lever: quality, description: "PIA Group's group CIO: checks that AI performs on one engagement file; offered as an interview claim, not a measured result.", figure: "hundreds, in some cases more than 1,000 checks per file", measures: "number of quality checks AI can run on a single engagement file, per the interviewee", provenance: self-reported, source_ref: NYENRODE-2026 }
  prerequisites:
    - "Workpapers in structured, machine-readable form"
    - "Firm-defined checklists of review criteria"
    - "A rule for how reviewer sign-off treats AI-found exceptions"
  risks_and_guardrails:
    - "The AICPA says a second AI tool does not reduce the auditor's supervision and review responsibility (AT-AICPAPA-2026)"
    - "The Nyenrode interviewee notes that perfect accuracy is not necessary for value but that AI-validates-AI risks a closed system (NYENRODE-2026)"
    - "Benchmark evidence shows agents sometimes produce incorrect documentation (ARXIV-FAB-2026)"
  human_checkpoints:
    - "Reviewer resolves every AI-raised exception"
    - "Reviewer still reviews judgemental areas"
  role_evolution: "Reviewers shift time from clerical completeness checks to judgemental areas (DELOITTE-UKTR-2025, PDF p. 95; NYENRODE-2026)."
  evidence_grade: B
  sources:
    - { ref: DELOITTE-UKTR-2025, title: "Deloitte UK annual review 2025: Audit transparency report (year ended 31 May 2025)", publisher: "Deloitte LLP (UK)", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf", date: 2025-09, access: full, locator: "PDF pp. 7, 15, 94-95" }
    - { ref: KPMG-TR-2025, title: "KPMG International Transparency Report 2025: Building trust through quality and innovation", publisher: "KPMG International", type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/12/transparency-report-fy25.pdf", date: 2025-12, access: full, locator: "PDF p. 16" }
    - { ref: NYENRODE-2026, title: "AI in auditing: balancing quality, professional skepticism, and responsibility (opinion; interview with the Group CIO of PIA Group and a Nyenrode professor)", publisher: "Nyenrode Business University", type: press, url: "https://www.nyenrode.nl/en/news/n/ai-auditing-quality-skepticism-responsibility", date: 2026-06-18, access: full, locator: "section 'More checks mean better quality, right?'" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", publisher: "PCAOB (staff)", type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p. 4" }
    - { ref: FRC-AIAUDIT-2025, title: "AI in audit: Illustrative example and documentation guidance", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf", date: 2025-06-26, access: full, locator: "p. 6" }
    - { ref: IFIAR-SURVEY-2026, title: "Survey of Inspection Findings 2025", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01, access: full, locator: "Appendix A, Table A.3 (Engagement Performance)" }
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraph on AI checking AI" }
    - { ref: ARXIV-FAB-2026, title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors", publisher: "arXiv", type: academic, url: "https://arxiv.org/abs/2609.32835", date: 2026-09-26, access: full, locator: "abstract" }
  last_reviewed: 2026-10-16
  notes: "Two named firms (Deloitte, KPMG) in transparency reports and one interview. No detection rate, false-positive rate or rework measure is published. Smart Review's scope in the Deloitte text is internal-controls testing. The IFIAR supervision-and-review finding count is a general baseline, not caused by or linked to AI."

- id: assurance-quality-management-17
  title: "Use AI in the firm's own monitoring and remediation: root-cause analysis and inspection-finding triage (idea)"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ data-reporting, review-assurance ]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "IFIAR's 2025 survey found 35% of listed PIE audits inspected with at least one finding and told networks to do thorough root-cause analysis, targeted remediation and impact measurement (IFIAR-SURVEY-2026, p. 2). Monitoring and remediation was the second most common firm-level theme: 42 firms (32%) had at least one finding (IFIAR-SURVEY-2026, Table A.2)."
  solution: "The SEC's chief accountant said the SEC asks auditors how they use AI to improve engagement-level quality and to monitor their system of quality control (KPMG-HOHL-2026). NFRA's principles, as reported, call for root-cause analysis of technology-related findings to feed the annual evaluation of the system of quality management (NFRA-CAALLEY-2026). No firm has described AI used in its own quality monitoring in the sources read."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "n/a", provenance: independent, source_ref: KPMG-HOHL-2026 }
  prerequisites:
    - "Structured inspection and internal-review findings data"
    - "Defined taxonomy for root causes"
  risks_and_guardrails:
    - "IFIAR says inspection results do not provide a complete measure of audit quality and are not 'balanced scorecards' (IFIAR-SURVEY-2026, p. 2)"
    - "PCAOB's own staff drafts say about 90% of registration and inspection data are unstructured, a limit on automation at the regulator too (STARLING-IMC-2026)"
  human_checkpoints:
    - "Quality leadership decides which root causes are real"
    - "Remediation owners sign off actions"
  role_evolution: "Quality staff would move from compiling findings to interpreting AI-surfaced patterns; the SEC's question suggests regulators will ask how firms use AI this way (KPMG-HOHL-2026)."
  evidence_grade: D
  sources:
    - { ref: IFIAR-SURVEY-2026, title: "Survey of Inspection Findings 2025", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01, access: full, locator: "p. 2; Table A.2" }
    - { ref: KPMG-HOHL-2026, title: "Q&A with Kurt Hohl, SEC chief accountant (Women Corporate Directors Audit Committee Peer Exchange, late March 2026)", publisher: "KPMG US Board Leadership Center", type: firm, url: "https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html", date: 2026-05-27, access: full, locator: "answer on AI and quality control monitoring" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened)", publisher: "CAalley (reproducing ET CFO)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Audit documentation and training to change'" }
    - { ref: STARLING-IMC-2026, title: "Modernizing US PCAOB Audit Inspections", publisher: "Starling Insights", type: press, url: "https://insights.starlingtrust.com/content/observations/modernizing-us-pcaob-audit-inspections", date: 2026-09-01, access: full, locator: "paragraph on technology" }
  last_reviewed: 2026-10-16
  notes: "Idea: a regulator question and a principle, not a deployment. IFIAR's 35% figure is the share of listed PIE audits inspected with at least one finding; it is baseline context, not an AI result."

- id: assurance-quality-management-18
  title: "Document AI use in two places: a central certification file and a structured record on the audit file"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ document-production, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Reviewers and inspectors need to see which tool processed which balance, with what version and extent of human review. The AFM found it not always clear or visible where GenAI had been applied in the audit process (AFM-12BB-2025, p. 31)."
  solution: "The FRC's June 2025 guidance splits documentation: the tool's purpose, development, certification, training and explainability are documented centrally, while the audit file holds a description, tool and model version (or a pointer to a control that limits use to the latest approved version), configuration, data or prompts, the team's assessment of fitness, approval evidence and how outputs informed conclusions; for AI tools that are not ATTs there may be no file requirement (FRC-AIAUDIT-2025, pp. 13-16). In the FRC's board-minutes example the auditor records on the file that a GenAI tool was used to focus review and how output informed further work (FRC-GENAI-2026, p. 43). NFRA's principles, as reported, move toward a structured format showing which tool processed a balance and the extent of human review (NFRA-CAALLEY-2026). IFIAR asks for policies to identify uses of GenAI in critical areas, including where evidence was prepared by AI (IFIAR-TTF-2025, p. 9)."
  outcomes:
    - { lever: risk, description: "In the FRC review, firms with processes for engagement-specific ATTs all required templates to be kept on the audit file, but some template wording made completion look optional.", figure: "none published beyond 'most firms'", measures: "firms (of six) with engagement-specific ATT templates retained on file", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "Central register of approved tool versions"
    - "File template with tool, version, configuration, inputs, review"
    - "Rule for what is central versus on file"
  risks_and_guardrails:
    - "FRC says over-documentation can divert time and resource from audit quality and expects proportion (FRC-AIAUDIT-2025, p. 6)"
    - "If outputs of an LLM-enabled research tool are all checked back to cited sources, the FRC says it may be appropriate to document less about the tool (FRC-AIAUDIT-2025, p. 6)"
  human_checkpoints:
    - "Engagement team completes the file record"
    - "Reviewer checks the record against the central register"
  role_evolution: "Documentation shifts from describing procedures to recording tool use and review; file records are shorter because the tool's design sits centrally (FRC-AIAUDIT-2025, p. 16)."
  evidence_grade: C
  sources:
    - { ref: FRC-AIAUDIT-2025, title: "AI in audit: Illustrative example and documentation guidance", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf", date: 2025-06-26, access: full, locator: "pp. 5-6, 13-16" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p. 43" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Documentation; Engagement-specific ATTs" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened)", publisher: "CAalley (reproducing ET CFO)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Audit documentation and training to change'" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution (2025 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "p. 9 (Transparency)" }
    - { ref: AFM-12BB-2025, title: "12 Building blocks for controlled use of auditing tools", publisher: "Autoriteit Financiele Markten (Netherlands)", type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "p. 31" }
  last_reviewed: 2026-10-16
  notes: "Regulator-observed for conventional ATTs; GenAI-specific file records are guidance, not observed practice. The AICPA release says the engagement letter need not name AI tools (AT-AICPAPA-2026), which is a separate question from file documentation."

- id: assurance-quality-management-19
  title: "Engage inspectors early on novel AI tools and keep an inspection-ready evidence file for each tool"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ client-interaction, document-production ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Inspectors are examining technology use and tool governance. PCAOB staff said in 2024 they would continue to inquire about the use of technology in audit procedures (PCAOB-PRIORITIES-2025, p. 6) and, at a December 2025 conference, that firms' AI adoption would be an area of focus for inspectors (DART-SECPCAOB-2025). CPAB found in its 2025 inspections that, where tools were the primary source of audit evidence, validation of input data was limited in some cases, and in one tool testing was generally limited to flagged items with none on transactions the algorithm rated low risk (CPAB-EVOLVING-2025, p. 1)."
  solution: "Firms consult regulators before using tools that materially change the work, and keep ready the central certification file, version history, test results and engagement-level use records. IFIAR encourages early engagement with local regulators and IFIAR where technology may significantly alter the work (IFIAR-TTF-2026, p. 4); CPAB asks firms to consider when to engage regulators (CPAB-EVOLVING-2025, p. 2). The FRC opened an Audit Tech and AI Sandbox on 4 June 2026 for firms of all sizes to work with the regulator on how standards apply to new technology, without endorsing products (FRC-SANDBOX-2026)."
  outcomes:
    - { lever: risk, description: "CPAB inspection observation (count not published): tools used as the primary evidence source with limited validation of data inputs in some instances.", figure: "no count published", measures: "instances in CPAB's 2025 inspections; number and denominator not stated in the paper", provenance: independent, source_ref: CPAB-EVOLVING-2025 }
  prerequisites:
    - "Central documentation per tool (FRC-AIAUDIT-2025, pp. 13-15)"
    - "Single owner for regulator queries"
    - "Version and approval history that can be produced on request"
  risks_and_guardrails:
    - "FRC says it will not develop or endorse specific products through the sandbox (FRC-SANDBOX-2026)"
    - "The FRC says its March 2026 guidance is not a response to identified quality deficiencies (FRC-GENAINEWS-2026)"
  human_checkpoints:
    - "Quality leadership decides what to bring to regulators"
    - "Tool owners answer inspector questions from the central file"
  role_evolution: "Quality and technology leaders add a regulator-engagement task; the FRC says its sandbox gives participants direct access to regulatory expertise on how standards apply to new technology (FRC-SANDBOX-2026)."
  evidence_grade: C
  sources:
    - { ref: FRC-SANDBOX-2026, title: "FRC invites firms and companies to experiment, innovate and reduce burdens through new sandbox programmes (news release)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/news-and-events/news/2026/06/frc-invites-firms-and-companies-to-experiment-innovate-and-reduce-burdens-through-new-sandbox-programmes/", date: 2026-06-04, access: full, locator: "news release" }
    - { ref: ICAS-SANDBOX-2026, title: "Driving audit innovation with FRC sandboxes and forums", publisher: "ICAS", type: professional-body, url: "https://icas.com/news-insights-events/news/audit-assurance/driving-audit-innovation-with-frc-sandboxes-and-forums/", date: 2026-07-07, access: full, locator: "section 'Audit tech and AI'" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p. 4" }
    - { ref: CPAB-EVOLVING-2025, title: "The evolving use of technology in the audit (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: 2025-12-16, access: full, locator: "pp. 1-2" }
    - { ref: PCAOB-PRIORITIES-2025, title: "Spotlight: Staff Priorities for 2025 Inspections and Interactions With Audit Committees", publisher: "PCAOB (staff)", type: regulator, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf", date: 2024-12, access: full, locator: "pp. 6-7" }
    - { ref: DART-SECPCAOB-2025, title: "Heads Up: 2025 AICPA & CIMA Conference on Current SEC and PCAOB Developments, key takeaways", publisher: "Deloitte DART", type: conference, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways", date: 2025-12, access: full, locator: "Summary: AI" }
    - { ref: FRC-GENAINEWS-2026, title: "Innovative new guidance supports audit firm adoption of emerging AI technologies (news release)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/", date: 2026-03-30, access: full, locator: "news release" }
  last_reviewed: 2026-10-16
  notes: "Grade C: regulator announcements and observations, no named participant outcome."

- id: assurance-quality-management-20
  title: "Detect and prevent engagement use of unapproved AI tools, with preventative controls and a clear permitted-use policy"
  archetype: assurance
  module: quality-management
  function: technology-it
  work_types: [ review-assurance, software-systems ]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Staff can reach public chatbots. In a Thomson Reuters Institute survey of tax and audit professionals, more than a third admitted using unauthorised AI tools (TRI-FOP-2026). The IAASB notes that engagement teams may use tools outside the firm's approval channels (IAASB-TQMPLAN-2026, para 25)."
  solution: "The FRC found firms do not generally monitor that teams use only authorised and current ATTs but rely on preventative controls: restricting downloads to authorised repositories, removing outdated versions, blocking unauthorised installs, remote removal, and licence management (FRC-ATT-2025, Maintenance and monitoring). IFIAR suggests oversight programmes that check non-approved or decommissioned tools are not used and ongoing coaching on proper use (IFIAR-TTF-2026, p. 6). PCAOB staff heard in 2024 that some firms did not allow GenAI for audit or attest procedures, citing data privacy and reliability (PCAOB-GENAI-2024, p. 4). The IAASB plan covers pre-use evaluation where teams propose tools the firm has not approved (IAASB-TQMPLAN-2026, Table 1)."
  outcomes:
    - { lever: risk, description: "More than a third of surveyed tax and audit professionals admit to using unauthorised AI tools.", figure: "more than one-third", measures: "share of professionals in the Thomson Reuters Institute survey who admit using unauthorised AI tools; page gives no exact figure or sample size", provenance: vendor-published, source_ref: TRI-FOP-2026 }
  prerequisites:
    - "Approved-tool catalogue with enterprise AI available"
    - "Endpoint and network controls"
    - "Clear policy on acceptable use and confidential data"
  risks_and_guardrails:
    - "Banning tools without approved alternatives pushes use out of sight; TRI says establishing governance, approving secure tools and giving usage guidance are essential (TRI-FOP-2026)"
    - "AFM asks firms to ensure confidential client data is processed, transferred and stored safely when used as tool input (AFM-12BB-2025, p. 3)"
  human_checkpoints:
    - "Exceptions approved by a named function"
    - "Periodic engagement reviews for incorrect or unapproved use"
  role_evolution: "IT and quality teams jointly enforce tool policy; engagement teams must be told what is approved (IFIAR-TTF-2026, p. 6)."
  evidence_grade: C
  sources:
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Maintenance and monitoring: Restricting access" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits: Innovation and audit quality (2026 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20, access: full, locator: "p. 6" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", publisher: "PCAOB (staff)", type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "p. 4" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F, approved March 2026)", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "para 25(c); Table 1" }
    - { ref: TRI-FOP-2026, title: "Future of Professionals Report 2026: what tax and audit firm leaders should be prioritizing now (action-paper summary page; the page carries no date, 2026-07 follows the landscape file)", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07, access: full, locator: "Universal priorities: Govern the tools being used" }
    - { ref: AFM-12BB-2025, title: "12 Building blocks for controlled use of auditing tools", publisher: "Autoriteit Financiele Markten (Netherlands)", type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12, access: full, locator: "p. 3" }
  last_reviewed: 2026-10-16
  notes: "The survey is vendor-published (Thomson Reuters sells to firms) and is a general tax and audit population, not audit-firm quality leaders. Its date is not shown on the page."

- id: assurance-quality-management-21
  title: "Embed methodology in AI-tool design and validate how much assurance an AI-enabled procedure contributes"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ expert-judgment, document-production ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "The FRC names non-compliant methodology as a risk: the firm's methodology may permit approaches that fail auditing standards even when the tool works and is used as specified (FRC-GENAI-2026, pp. 6, 18-19). IFIAR members' most frequent technology findings in 2023 and 2024 were misreading tool results and thin testing of outliers (IFIAR-TTF-2025, pp. 5-6)."
  solution: "Methodology teams join tool development and certification validates the supporting methodology against auditing standards (FRC-GENAI-2026, p. 40). In the FRC's contract-review example the assurance from the AI-enabled procedure is linked to confidence in the tool's risk indicators and sampling, which sets the substantive testing still needed (FRC-GENAI-2026, p. 56). NFRA's principles, as reported, say a tool's low-risk classification should be periodically tested and full-population testing does not remove risk assessment (NFRA-CAALLEY-2026). CPAB saw tools used as the primary evidence source with limited input validation, and one tool where substantive testing was limited to flagged items (CPAB-EVOLVING-2025, p. 1)."
  outcomes:
    - { lever: risk, description: "FRC: most of the six largest UK firms capture methodology-team input and sign-off in certification documents.", figure: "most of six", measures: "firms among the six reviewed whose certification documents capture methodology input", provenance: independent, source_ref: FRC-ATT-2025 }
    - { lever: risk, description: "IFIAR: members reporting findings that a tool was not used as intended.", figure: "31% (2024); 29% (2023)", measures: "percentage of IFIAR members reporting such findings; denominator not stated in the text read", provenance: independent, source_ref: IFIAR-TTF-2025 }
  prerequisites:
    - "Methodology representatives on the tool project team"
    - "A written statement of what the tool's output can and cannot support"
    - "Residual-testing rules for low-risk-rated items"
  risks_and_guardrails:
    - "NFRA, as reported, cautions against relying on vendor claims on accuracy without independent evaluation (NFRA-CAALLEY-2026)"
    - "NFRA, as reported, says technology-generated information has no separate, lower evidentiary bar and becomes evidence only after the auditor evaluates its relevance and reliability (NFRA-CAALLEY-2026)"
  human_checkpoints:
    - "Methodology team approves how tool output is used"
    - "Engagement team tests data inputs and a sample of low-risk-rated items"
  role_evolution: "A methodology specialist works alongside engineers at the design stage; RSM UK's audit data analytics director sat on the FRC technology working group and urged technology teams to secure auditor buy-in (ICAEW-FRCVIEW-2026)."
  evidence_grade: C
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 6, 18-19, 40, 55-56" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF)", publisher: "Financial Reporting Council (UK)", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26, access: full, locator: "Integration with audit methodology" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution (2025 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "pp. 5-6" }
    - { ref: CPAB-EVOLVING-2025, title: "The evolving use of technology in the audit (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: 2025-12-16, access: full, locator: "p. 1" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened)", publisher: "CAalley (reproducing ET CFO)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24, access: full, locator: "section 'Professional scepticism cannot be delegated to technology'" }
    - { ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC guidance on generative and agentic AI? (viewpoint)", publisher: "ICAEW", type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05, access: full, locator: "section 'Encouraging audit and tech teams to collaborate'" }
  last_reviewed: 2026-10-16
  notes: "The IFIAR and CPAB findings concern automated tools generally and are not specific to generative AI, so the grade is capped."

- id: assurance-quality-management-22
  title: "Redesign supervision, coaching and early-career development for AI-assisted work (idea)"
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [ review-assurance, coordination-scheduling ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "PCAOB staff heard in 2024 that firms' policies for supervision and review had not changed despite GenAI, with the same diligence expected from reviewers (PCAOB-GENAI-2024, pp. 4-5). IFIAR asks firms to prioritise supervision training and consider how supervision may need to change as AI is integrated (IFIAR-TTF-2025, p. 8). Researchers flag that automating early-career tasks may erode the on-the-job learning where judgement develops (HOLMSTROM-2024)."
  solution: "Supervision policies are rewritten so seniors know what AI work juniors did, the extent of review, and where judgement must still be exercised; graduate programmes keep tasks that build judgement. TRI's firm-leader paper says firms must ensure junior staff still get structured development and supervision before automation erodes these opportunities (TRI-FOP-2026). CPAB asks firms to consider how to develop junior auditors' critical thinking (CPAB-EVOLVING-2025, p. 3). A German Big 4 survey of auditors found concern about over-reliance and possible loss of skills alongside gains on standardised tasks (FABIAN-2026)."
  outcomes:
    - { lever: quality, description: "none published; IFIAR counted findings on firms failing to establish supervision and review policies as a baseline, not an AI measure.", figure: "31 findings in 2025; 10 in 2024", measures: "number of findings (not firms) on 'failure to establish and/or implement policies and procedures for sufficient, timely engagement supervision and review' reported to IFIAR", provenance: independent, source_ref: IFIAR-SURVEY-2026 }
  prerequisites:
    - "Visibility of which work is AI-produced"
    - "Revised direction and review policy under ISA 220 (Revised) or the local equivalent"
    - "Rotation or training that keeps early-career exposure to unautomated tasks"
  risks_and_guardrails:
    - "The IAASB notes AI tools complicate the engagement partner's responsibilities for direction, supervision and review where outputs are hard to explain or need specialised skills (IAASB-TQMPLAN-2026, para 10)"
    - "Registered-report designs on motivation and judgement quality report no results yet (HOLMSTROM-2024)"
  human_checkpoints:
    - "Engagement leader reviews how AI-assisted work was supervised"
    - "Coaching reviews for juniors"
  role_evolution: "Early-career staff move from preparing to reviewing and checking AI output; Fabian and Ratzinger-Sakel report that role and experience shape acceptance (FABIAN-2026)."
  evidence_grade: D
  sources:
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", publisher: "PCAOB (staff)", type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: 2024-07, access: full, locator: "pp. 4-5" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution (2025 report)", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "p. 8 (Supervision and oversight)" }
    - { ref: HOLMSTROM-2024, title: "How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal, PCAOB conference)", publisher: "PCAOB conference on auditing and capital markets (Holmstrom and Peters)", type: academic, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf", date: 2024-06, access: full, locator: "Introduction" }
    - { ref: TRI-FOP-2026, title: "Future of Professionals Report 2026: what tax and audit firm leaders should be prioritizing now (action-paper summary page; the page carries no date, 2026-07 follows the landscape file)", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07, access: full, locator: "Define the role of early-career professionals" }
    - { ref: CPAB-EVOLVING-2025, title: "The evolving use of technology in the audit (CPAB Exchange)", publisher: "Canadian Public Accountability Board", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: 2025-12-16, access: full, locator: "p. 3" }
    - { ref: FABIAN-2026, title: "AI in auditing: new study highlights opportunities and limitations (university news item on a Journal of Information Systems paper)", publisher: "University of Hamburg", type: academic, url: "https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html", date: 2026-03-20, access: full, locator: "news item" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F, approved March 2026)", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "para 10" }
    - { ref: IFIAR-SURVEY-2026, title: "Survey of Inspection Findings 2025", publisher: "International Forum of Independent Audit Regulators (copy hosted by Japan FSA)", type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01, access: full, locator: "Table A.3" }
  last_reviewed: 2026-10-16
  notes: "Idea. Regulators and researchers discuss it; no firm has published a revised supervision model."
```

---

## 3. Module notes

### Processes and key steps (with work types)

Work types use the vocabulary ids.
1. **Identify the need and approve a business case** (`coordination-scheduling`). Ideas come top-down from global forums or innovation teams and bottom-up from teams; a formal business case is needed before purchase or build at all six UK firms reviewed (FRC-ATT-2025, Planning and needs analysis).
2. **Design or select, with vendor due diligence** (`software-systems`, `review-assurance`). Firms prefer network-built tools; outside the largest firms third-party tools are more likely; foundation models are almost always third-party (FRC-ATT-2025, Design or selection; IAASB-TQMPLAN-2026, para 25).
3. **Certify and approve the tool in a use case** (`review-assurance`). Inputs, architecture and logic, output tests, methodology sign-off, supporting IT general controls; pilots on lower-risk non-PIE audits first at some firms (FRC-ATT-2025; FRC-GENAI-2026, pp. 30-33).
4. **Integrate with methodology; write guidance and training** (`document-production`). Methodology teams co-develop tools and certification validates the methodology (FRC-GENAI-2026, p. 40).
5. **Control deployment: inventory, access, version control, retirement** (`software-systems`). Mostly preventative controls rather than monitoring (FRC-ATT-2025, Maintenance and monitoring).
6. **Plan the engagement's use of tools and set expectations** (`coordination-scheduling`) (IFIAR-TTF-2026, p. 7; CPAB-EVOLVING-2025, pp. 5-6).
7. **Direct, supervise and review AI-assisted work, with control points for agents** (`review-assurance`) (FRC-GENAI-2026, pp. 37-38).
8. **Document AI use centrally and on the file** (`document-production`) (FRC-AIAUDIT-2025, pp. 13-16).
9. **Monitor usage and impact; run root-cause analysis; recertify or retire** (`data-reporting`) (IFIAR-TTF-2026, pp. 8-9; FRC-ATT-2025).
10. **Resource and train people** (`coordination-scheduling`, `document-production`) (IFIAR-TTF-2026, p. 7; CAQ-RSM-2026).
11. **Evaluate the system annually and respond to inspectors** (`review-assurance`, `client-interaction`). QC 1000 and ISQM 1 require an annual evaluation; the PCAOB amendments let firms pick the evaluation date (EISNER-QC1000-2026).

### Common pain points
- **Tool traits the standards did not anticipate.** The IAASB names opacity, non-determinism and adaptivity as what makes applying ISQM 1 and ISA 220 (Revised) hard: how to govern, how much to test before use, how to monitor, how to evaluate outputs (IAASB-TQMPLAN-2026, paras 6-7).
- **Unclear ownership across the network.** Who monitors a network-built tool, the network or the member firm, is "sometimes unclear" (IFIAR-TTF-2025, p. 6) and is fragmented in some networks (IFIAR-TTF-2026, p. 8).
- **Informal recertification triggers.** At the six UK firms triggers were generally identified informally by tool owners; legacy tools had not always been through formal certification; some engagement-specific tool templates read as optional (FRC-ATT-2025).
- **Usage counted for licences, not quality.** Monitoring mostly counted teams using a tool (FRC-ATT-2025); usage often estimated (AFM-12BB-2025, p. 15).
- **Uneven playing field.** The IAASB records that larger, better-resourced firms are better placed than small and medium practices to develop, govern and use these tools (IAASB-TQMPLAN-2026, para 11). The ICAEW's head of data analytics and technology says the FRC guidance assumes technology and methodology teams that smaller firms lack (ICAEW-FRCVIEW-2026). In a US benchmark of 54 firms, 75% had no documented transformation plan (CPACOM-ATR-2025, introduction).
- **Review capacity versus automation bias.** See the objections list below.

### Metrics and benchmarks (what each measures)
- **IFIAR frequency of ATT use in inspected audits, 2023 / 2024 (members answering "frequently observed"):** journal entry testing 86% / 88%; risk assessment 49% / 55%; internal controls testing 33% / 43%; substantive procedures 51% / 55%; IT applications and security configurations 33% / 39%. Response counts per row were 42-49 members (IFIAR-TTF-2025, p. 5). The 2026 report shows 2025 as a chart without data labels and describes continuous use in journal entries, controls and risk assessment and an increase in substantive procedures (IFIAR-TTF-2026, p. 9).
- **IFIAR: 31% of members reported findings of a tool not used as intended (2024; 29% in 2023)**; denominator not stated in the text (IFIAR-TTF-2025, pp. 5-6).
- **IFIAR: about 30% year-on-year increase in AI-enabled tools in 2025 across the six GPPC networks**, with differing firm reporting practices (IFIAR-TTF-2026, p. 5, fn. 1).
- **IFIAR survey 2025 (44 members; 161 member firms inspected):** firms with at least one finding by theme: engagement performance 49 (37%), monitoring and remediation 42 (32%), ethical requirements 43 (30%), human resources 32 (24%), EQR 26 (20%), acceptance and continuance 25 (18%), governance and leadership 22 (18%), risk assessment process 19 (16%), technological, intellectual and service-provider resources 11 (9%), information and communication 9 (9%). Percentages are per-theme; denominators differ (IFIAR-SURVEY-2026, Table A.2). Findings (not firms) on supervision and review policy: 31 in 2025, 10 in 2024 (Table A.3).
- **AFM: usage monitored by estimate 74%, actual data 20%, unclear 6%** of audit tooling in 13 firms (AFM-12BB-2025, p. 15).
- **FRC: 1 of 6 firms reported tool usage against targets; 2 of 6 ran annual owner confirmations; 1 of 6 set a three-year recertification backstop; 2 of 6 captured tool limitations in certification templates; 3 of 6 captured the supporting IT control environment** (FRC-ATT-2025).
- **Firm scale statements (self-reported):** KPMG says its Clara AI capabilities reach over 95,000 auditors (KPMG-TR-2025, PDF p. 16); Deloitte UK reports 4,649 active users of its GenAI tool PairD, over 75% of its Audit & Assurance staff, and about two million prompts in a year (DELOITTE-UKTR-2025, PDF p. 94); RSM says Ask Luca serves 4,000+ assurance professionals (RSM-ASKLUCA-2026).
- **Survey context, not audit firms:** ISACA's poll of 3,400+ digital-trust professionals found 38% of organisations have a formal, comprehensive AI policy (ISACA-PULSE-2026). It is a general-organisation figure and is included only to show governance lagging use.
- **Metrics IFIAR suggests firms define:** engagement coverage %, false-positive and false-negative rates against a manual sample, rework rates, escalation incidence (IFIAR-TTF-2026, pp. 8-9). No firm has published any of them.

### Guardrails and regulatory points
- **Accountability is unchanged.** The FRC says the human auditor is always accountable (FRC-GENAINEWS-2026). NFRA's principles, as reported, say the opinion belongs to an identified auditor and technology cannot be invoked to explain away a conclusion (NFRA-CAALLEY-2026).
- **FRC requirements stay the ISQMs and ISAs (UK); its AI material is not prescriptive** (FRC-AIAUDIT-2025, p. 6). The FRC says the June 2025 guidance was built with its Technology Working Group and is meant to show third-party providers what regulators expect of their audit-firm customers (FRC-AIAUDITNEWS-2025).
- **Where AI makes judgements without a human**, IFIAR asks firms to assess acceptability and consult members before widespread use (IFIAR-TTF-2025, p. 8).
- **Documentation:** FRC splits central and file documentation; NFRA moves toward structured records; the AICPA says AU-C 210 does not require naming AI tools in the engagement letter, but laws, contracts or firm policy may (AT-AICPAPA-2026). IRBA's September 2024 update recalls its January 2023 safeguards (an AI policy, procedures to verify the authenticity of evidence and working papers, a protocol to monitor AI use, and engagement-letter wording on AI use) and suggests firms consider a certification process before adopting tools (IRBA-AIRISK-2024).
- **Data and confidentiality** remain a first-order constraint: some firms did not allow GenAI for audit procedures for privacy and reliability reasons (PCAOB-GENAI-2024, p. 4); NFRA says a firm cannot rely on vendor terms without validation (NFRA-CAALLEY-2026).
- **AFM sequencing:** four preconditions, of which the lower three (risk management, input data, controlled tool implementation) must be in place before deploying (Gen)AI; the AFM says it will give this topic more attention in supervisory reviews (AFM-12BB-2025, p. 1 for the structure, p. 4 for supervision).
- **Singapore:** ACRA's Audit Practice Guidance No. 1 of 2025, announced 26 December 2025, covers risk assessment and monitoring processes for systems of quality management in a technology-driven environment (ACRA-APG-2025; the guidance itself was not opened).
- **AICPA Part 2** lists quality-management policies a CPA firm may adopt for AI tools used to obtain audit evidence (AT-AICPAPA-2026).

### Interaction with inspectors
- **UK:** supervision now keyed to the firm's system of quality management, with thematic reviews and corroborative inspections (FRC-SUPERVISION-2026). Board Agenda reports fewer formal inspections under the new approach (BOARDAGENDA-FRC-2026; secondary report). The FRC sandbox (4 June 2026) lets firms of any size explore how standards apply to new technology with the regulator (FRC-SANDBOX-2026; ICAS-SANDBOX-2026).
- **US:** PCAOB staff said in December 2025 that firms' AI adoption would be an area of focus for inspectors (DART-SECPCAOB-2025). The SEC's chief accountant said the SEC asks how auditors use AI to improve quality and to monitor their quality control, and expects inspections to shift toward how firm leadership supports engagement teams (KPMG-HOHL-2026; STARLING-HOHL-2026). The Inspections Modernization Council materials posted 25 August 2026 are staff drafts, not Board policy (DART-IMC-2026; STARLING-IMC-2026).
- **Canada and the Netherlands:** CPAB's 2025 inspections looked at tools used as primary evidence (CPAB-EVOLVING-2025, p. 1) and CPAB leads IFIAR's technology task force (CPAB-EVOLVING-2025, p. 2); the AFM says it will examine controlled use of tools in later supervisory reviews (AFM-12BB-2025, p. 4).
- **Fragmentation risk:** the IAASB names regulatory fragmentation, firms applying the standards differently, and an uneven playing field as the public-interest problems its guides are meant to reduce (IAASB-TQMPLAN-2026, para 11).

### Frontier signals (dated)
- **2026-10-13:** AICPA practice aid, with more material promised on risk of material misstatement and audit evidence (AICPA-PA-2026).
- **2026-09-09:** PCAOB adopts QC 1000 amendments, effective 2026-12-15 if the SEC approves (DART-QC1000-2026; EISNER-QC1000-2026).
- **2026-09-01 / 2026-08-25:** PCAOB staff discussion materials for the Inspections Modernization Council: inspections centred on the firm's quality control system, new severity frameworks, about 90% of registration and inspection data unstructured, early AI pilots (STARLING-IMC-2026; DART-IMC-2026).
- **2026-07-24:** NFRA (India) staff series on principles for technology adoption (NFRA-CAALLEY-2026).
- **2026-06 and 2026-09:** IAASB Board broadly supports a five-guide series focused on GenAI-enabled tools including agentic ones; drafts of Guide 1 and Guide 2 Part 1 (service-provider and foundation-model considerations) were planned for the September 2026 meeting (the outcome was not found); remaining guides are to go to the Board by June 2027 (IAASB-MINJUN-2026, paras 28-31; IAASB-TQMPLAN-2026, Table 2). The Board called the timetable ambitious.
- **2026-06-04:** FRC Audit Tech and AI Sandbox opens (FRC-SANDBOX-2026).
- **2026-04-20:** IFIAR 2026 technology report: agentic AI, human-led audit, metrics, early engagement (IFIAR-TTF-2026).
- **2026-04:** Deloitte UK sets up a Technology Controls Board (DELOITTE-UKTR-2026, PDF p. 48).
- **2026-03-30:** FRC generative and agentic AI guidance; **2026-03-25:** FRC revised supervision (FRC-GENAINEWS-2026; FRC-SUPERVISION-2026).
- **Research on auditability of agents:** a preprint argues no agent system can be accountable without auditability and proposes tamper-evident action records; it is generic, not audit-specific (ARXIV-AUDITABLE-2026).

### Workforce and role effects
- **Methodology teams move into tool design and certification;** a new technology-risk board and a chief AI officer appear in one firm's governance (FRC-ATT-2025; DELOITTE-UKTR-2026, PDF pp. 27, 48).
- **Reviewers shift from preparing to reviewing.** Researchers expect autonomy and competence needs to be hit as work moves from preparing to reviewing (HOLMSTROM-2024). A survey of experienced auditors at a German Big 4 firm found gains on standardised tasks, limits on complex judgements, and concerns about over-reliance and skill loss (FABIAN-2026). An interview study of 22 audit professionals at large firms found simple AI such as extraction and OCR widely used, complex AI still in development, and fear of overreliance among the main challenges (LIGOEL-2025).
- **Graduate programmes are being rebuilt.** Deloitte UK describes simulations combining traditional and AI-assisted methods and a reskilling pilot (DELOITTE-UKTR-2026, PDF p. 5).
- **Headcount:** a pre-generative-AI study associates a one-standard-deviation rise in AI investment with accounting employees 3.6% lower after three years and 7.1% lower after four (FEDYK-2022).
- **Training and the junior pipeline** are named by the TRI paper as a priority: more than a third of surveyed professionals admit using unauthorised AI tools and firms should keep junior staff supervised before automation erodes development (TRI-FOP-2026).

### Objections and concerns practitioners and regulators raise
- **Automation bias is under-weighted.** The ICAEW technology faculty chair said the FRC guidance covers automation bias in a single paragraph on page 35 despite long-term effects on judgement (ICAEW-FRCVIEW-2026).
- **Vendor questions missing.** Most audit AI tools are features added to existing products; the guidance says little on questions for vendors (ICAEW-FRCVIEW-2026).
- **Probabilistic tools need rules-based partners.** RSM UK's audit data analytics director, who sat on the FRC technology working group, says no tool can be guaranteed to give the needed output every time and that data analysis needs a rules-based tool alongside the AI (ICAEW-FRCVIEW-2026).
- **AI validating AI.** A Group CIO warns it can create a closed system in which errors are hard to detect (NYENRODE-2026); the AICPA allows it but keeps supervision duties (AT-AICPAPA-2026).
- **Premature rules.** The IAASB's observer from its public-interest oversight board said it would be premature to consider new requirements (IAASB-MINDEC-2025, para 44).
- **Guidance density.** Practitioners found the FRC guidance dense; the advice was to read the two illustrative examples first (ICAEW-FRCVIEW-2026).
- **Efficiency expectation gaps.** The IAASB Board asked staff to address expectation gaps where perceived efficiency gains could mislead regulators and investors (IAASB-MINDEC-2025, para 38).

### Interview probes for an advisor
1. "Walk me through the last AI tool you approved or turned down. Who sat on the panel, what test set did you use, what failed, and what would force recertification (a model update, a new use case, an inspector question)?"
2. "For one AI-assisted procedure, what exactly does the reviewer do, how long does it take, and how do you know review catches errors? Do you have seeded-error tests, override rates or parallel-run results?"
3. "If an inspector asked which engagements used which tool version last year and where AI output sits on the file, how long would it take to answer, and from where?"
4. "For tools built by your network, who monitors them, you or the network, and which quality metrics do you track beyond licence counts?"
5. "What has changed in your supervision and graduate programme since 2024, and what have inspectors asked about AI in the latest cycle?"

---

## 4. Routed to other modules

| Item | Target module | Why |
|---|---|---|
| CPAB 2025 inspection finding that a tool was the primary evidence source for a class of transactions, with testing limited to flagged items (CPAB-EVOLVING-2025, p. 1) | substantive-testing | Describes a testing design. Used here only for quality-management implications (use case 21). |
| IFIAR frequency of ATT use by area, especially journal entry testing (IFIAR-TTF-2025, p. 5) | substantive-testing; controls-testing; planning-risk-assessment | Area-level adoption data. |
| AICPA practice aid Part 1: entity's AI use, acceptance and continuance, AI-operated controls, service-organisation reports (AT-AICPAPA-2026; AICPA-PA-2026; JOFA-AIPA-2026) | planning-risk-assessment; acceptance-independence; controls-testing | Client-side AI, not the firm's own tools. |
| CAQ Spring 2026 Audit Partner Pulse: AI governance maturity at the largest client (6% advanced, 40% incomplete, 46% early or reactive); top client control gaps (BOARDMEMBER-CAQ-2026) | planning-risk-assessment | Client-side AI governance. Percentages are of audit partners' views of their largest client. |
| SEC chief accountant: AI partnerships and private-equity ownership complicate independence; independence rules reviewed for fit when AI is part of audit delivery (STARLING-HOHL-2026; KPMG-HOHL-2026) | acceptance-independence | Independence, not tool quality. |
| PCAOB focus on private equity and alternative practice structures in inspections (PCAOB-PRIORITIES-2025, p. 6; DART-SECPCAOB-2025) | acceptance-independence | Ownership structures. |
| IFIAR 2026: auditors must consider AI-originated audit evidence and adversarial misuse of AI by audited entities (IFIAR-TTF-2026, p. 10) | planning-risk-assessment; substantive-testing | Evidence reliability and fraud risk. |
| Fabian and Ratzinger-Sakel: AI platform for auditing management reports (FABIAN-2026) | completion-reporting | Disclosure review. |
| IFIAR 2026: transparency with those charged with governance about AI use in the audit (IFIAR-TTF-2026, pp. 7-8) | completion-reporting | Communication with audit committees. |
| Deloitte UK: automated impairment modelling found calculation inaccuracies across ten consumer entities (DELOITTE-UKTR-2025, PDF p. 94) | specialists; substantive-testing | Tool outcome, self-reported. |
| KPMG: AI transaction scoring on complete populations; agents designing and performing substantive tests (KPMG-TR-2025, PDF p. 16) | substantive-testing | Procedure, not quality management. |
| Deloitte UK and KPMG assurance over AI, AI assurance services (DELOITTE-UKTR-2026, PDF p. 5) | other-assurance | Assurance over clients' AI. |

---

## 5. Sources

56 sources by type: regulator 17, standard-setter 8, firm 8, academic 8, press 7, survey 4, professional-body 3, conference 1. All were opened and read (`access: full`); partial reads are flagged in the title. No community, job-posting or podcast sources were read.

| Ref | Title | Publisher | Type | Date | URL | Access |
|---|---|---|---|---|---|---|
| ACRA-APG-2025 | Audit Practice Guidance No. 1 of 2025: Delivering Quality Audits in a Technology-Driven Environment (announcement page; the PDF itself was not opened) | Accounting and Corporate Regulatory Authority (Singapore) | regulator | 2025-12-26 | https://www.acra.gov.sg/news-events/news-announcements/906/ | full |
| AFM-12BB-2025 | 12 Building blocks for controlled use of auditing tools | Autoriteit Financiele Markten (Netherlands) | regulator | 2025-12 | https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf | full |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing (news release on the practice aid 'AI Considerations for Financial Statement Auditors'; the practice aid itself needs a login and was not opened) | AICPA & CIMA | standard-setter | 2026-10-13 | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | full |
| ARXIV-AUDITABLE-2026 | Auditable Agents | arXiv (USC and others) | academic | 2026-04 | https://arxiv.org/abs/2604.05485 | full |
| ARXIV-FAB-2026 | FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors | arXiv | academic | 2026-09-26 | https://arxiv.org/abs/2609.32835 | full |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | 2026-10-14 | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | full |
| AUASB-AI-2025 | Impact of AI on Auditors (web guidance) | Auditing and Assurance Standards Board (Australia) | standard-setter | 2025-07 | https://www.auasb.gov.au/publications/impact-of-ai-on-auditors/ | full |
| BOARDAGENDA-FRC-2026 | Watchdogs issue guidance on AI in the audit process but warn that auditors remain accountable | Board Agenda | press | 2026-03-31 | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | full |
| BOARDMEMBER-CAQ-2026 | What Audit Partners Are Seeing On AI And What It Means For Audit Committees (on the CAQ Spring 2026 Audit Partner Pulse Survey) | Corporate Board Member (CAQ author) | survey | 2026-07-15 | https://boardmember.com/what-audit-partners-are-seeing-on-ai-and-what-it-means-for-audit-committees/ | full |
| CAQ-RSM-2026 | Shaping the future of assurance: Advancing AI in the audit (blog post by RSM's Assurance Digital Leader) | Center for Audit Quality | professional-body | 2026-08-25 | https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit | full |
| COMMERFORD-2022 | Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence (abstract page) | Journal of Accounting Research (via RePEc) | academic | 2022 | https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html | full |
| CPAB-AI-2024 | The use of artificial intelligence in the audit: balancing innovation and risk (CPAB Exchange) | Canadian Public Accountability Board | regulator | 2024-09-12 | https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf | full |
| CPAB-EVOLVING-2025 | The evolving use of technology in the audit (CPAB Exchange) | Canadian Public Accountability Board | regulator | 2025-12-16 | https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (CPA.com and AICPA 2025 Audit Benchmark Survey) | CPA.com / AICPA | survey | 2025-12 | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | full |
| DART-IMC-2026 | PCAOB Shares Discussion Materials Related to Inspection Modernization Council's Summer 2026 Meetings | Deloitte DART | firm | 2026-08-25 | https://dart.deloitte.com/USDART/home/news/all-news/2026/aug/pcaob-materials-inspection-modernization-council-summer-2026-meetings | full |
| DART-QC1000-2026 | PCAOB Releases Amendments to Quality Control Standard | Deloitte DART | firm | 2026-09-09 | https://dart.deloitte.com/USDART/home/news/all-news/2026/sep/pcaob-amendments-quality-control-standard | full |
| DART-SECPCAOB-2025 | Heads Up: 2025 AICPA & CIMA Conference on Current SEC and PCAOB Developments, key takeaways | Deloitte DART | conference | 2025-12 | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways | full |
| DELOITTE-UKTR-2025 | Deloitte UK annual review 2025: Audit transparency report (year ended 31 May 2025) | Deloitte LLP (UK) | firm | 2025-09 | https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf | full |
| DELOITTE-UKTR-2026 | Deloitte UK annual review 2026: Audit transparency report (year ended 31 May 2026) | Deloitte LLP (UK) | firm | 2026-09 | https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf | full |
| EISNER-QC1000-2026 | PCAOB QC 1000 Amendments: What Audit Committees Need to Know | EisnerAmper | firm | 2026-10-08 | https://www.eisneramper.com/insights/audit-assurance/pcaob-qc-1000-amendments-audit-committees-1026/ | full |
| FABIAN-2026 | AI in auditing: new study highlights opportunities and limitations (university news item on a Journal of Information Systems paper) | University of Hamburg | academic | 2026-03-20 | https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html | full |
| FEDYK-2022 | Is artificial intelligence improving the audit process? (abstract page) | Review of Accounting Studies (via RePEc) | academic | 2022 | https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html | full |
| FRC-AIAUDIT-2025 | AI in audit: Illustrative example and documentation guidance | Financial Reporting Council (UK) | regulator | 2025-06-26 | https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf | full |
| FRC-AIAUDITNEWS-2025 | FRC publishes landmark guidance providing clarity to audit profession on the uses of AI (news release) | Financial Reporting Council (UK) | regulator | 2025-06-26 | https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/ | full |
| FRC-ATT-2025 | Thematic Review: Certification of Automated Tools and Techniques (HTML version; the page warns it was machine-converted from the PDF) | Financial Reporting Council (UK) | regulator | 2025-06-26 | https://www.frc.org.uk/docs/8383/html/ | full |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples | Financial Reporting Council (UK) | regulator | 2026-03-30 | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | full |
| FRC-GENAINEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies (news release) | Financial Reporting Council (UK) | regulator | 2026-03-30 | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | full |
| FRC-SANDBOX-2026 | FRC invites firms and companies to experiment, innovate and reduce burdens through new sandbox programmes (news release) | Financial Reporting Council (UK) | regulator | 2026-06-04 | https://www.frc.org.uk/news-and-events/news/2026/06/frc-invites-firms-and-companies-to-experiment-innovate-and-reduce-burdens-through-new-sandbox-programmes/ | full |
| FRC-SUPERVISION-2026 | FRC introduces evolved approach to audit supervision (news release) | Financial Reporting Council (UK) | regulator | 2026-03-25 | https://www.frc.org.uk/news-and-events/news/2026/03/frc-introduces-evolved-approach-to-audit-supervision/ | full |
| HOLMSTROM-2024 | How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal, PCAOB conference) | PCAOB conference on auditing and capital markets (Holmstrom and Peters) | academic | 2024-06 | https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf | full |
| IAASB-CATALOG-2026 | Technology Catalog of Issues and Possible Actions (publication page; the catalog PDF was not opened) | IAASB | standard-setter | 2026-07-09 | https://www.iaasb.org/publications/technology-catalog-issues-and-possible-actions | full |
| IAASB-MINDEC-2025 | Minutes of the public session, December 2025 meeting (Agenda Item 8, Technology Quality Management) | IAASB | standard-setter | 2025-12 | https://www.iaasb.org/_flysystem/azure-private/2026-03/Approved%20Minutes%20of%20the%20Public-Session%20for%20December%202025_0.pdf | full |
| IAASB-MINJUN-2026 | Minutes of the 154th meeting, June 2026 (Agenda Item 7, Technology Quality Management) | IAASB | standard-setter | 2026-06 | https://www.iaasb.org/_flysystem/azure-private/2026-09/Approved-Minutes-of-the-Public-Session-for-June-2026.pdf | full |
| IAASB-TQM-2026 | Technology Quality Management Roundtables: Outcomes and Next Steps (publication page; the feedback-summary PDF behind it was not opened) | IAASB | standard-setter | 2026-02-10 | https://www.iaasb.org/publications/technology-quality-management-roundtables-outcomes-and-next-steps | full |
| IAASB-TQMPLAN-2026 | Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F, approved March 2026) | IAASB | standard-setter | 2026-03 | https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf | full |
| IAASB-TQMWS-2026 | Technology Quality Management Workstream (project page, launched June 2025; lists documents through the June 2026 minutes) | IAASB | standard-setter | 2025-06 | https://www.iaasb.org/consultations-projects/technology-quality-management-workstream | full |
| ICAEW-FRCVIEW-2026 | How helpful is FRC guidance on generative and agentic AI? (viewpoint) | ICAEW | professional-body | 2026-05 | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | full |
| ICAS-SANDBOX-2026 | Driving audit innovation with FRC sandboxes and forums | ICAS | professional-body | 2026-07-07 | https://icas.com/news-insights-events/news/audit-assurance/driving-audit-innovation-with-frc-sandboxes-and-forums/ | full |
| IFIAR-SURVEY-2026 | Survey of Inspection Findings 2025 | International Forum of Independent Audit Regulators (copy hosted by Japan FSA) | regulator | 2026-04-01 | https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf | full |
| IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution (2025 report) | International Forum of Independent Audit Regulators (copy hosted by Japan FSA) | regulator | 2025-03-27 | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | full |
| IFIAR-TTF-2026 | Use of technology in audits: Innovation and audit quality (2026 report) | International Forum of Independent Audit Regulators (copy hosted by Japan FSA) | regulator | 2026-04-20 | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf | full |
| IRBA-AIRISK-2024 | Artificial Intelligence Audit Risks Mitigation Update (communique) | Independent Regulatory Board for Auditors (South Africa) | regulator | 2024-09-19 | https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf | full |
| ISACA-PULSE-2026 | AI Use Accelerates, While Governance and ROI Lag, Says New ISACA Research (2026 AI Pulse Poll) | ISACA | survey | 2026-05-05 | https://isaca.org/about-us/newsroom/press-releases/2026/ai-use-accelerates-while-governance-and-roi-lag-says-new-isaca-research | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | 2026-10-13 | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | full |
| KPMG-HOHL-2026 | Q&A with Kurt Hohl, SEC chief accountant (Women Corporate Directors Audit Committee Peer Exchange, late March 2026) | KPMG US Board Leadership Center | firm | 2026-05-27 | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | full |
| KPMG-TR-2025 | KPMG International Transparency Report 2025: Building trust through quality and innovation | KPMG International | firm | 2025-12 | https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/12/transparency-report-fy25.pdf | full |
| LIGOEL-2025 | Adoption of AI in auditing by large public accounting firms: interview study (abstract page) | International Journal of Accounting Information Systems (via RePEc) | academic | 2025 | https://ideas.repec.org/a/eee/ijoais/v56y2025ics1467089525000107.html | full |
| NFRA-CAALLEY-2026 | NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (press report of NFRA staff series 'General Principles for Technology Adoption in Audit'; the NFRA document itself was not opened) | CAalley (reproducing ET CFO) | press | 2026-07-24 | https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement | full |
| NYENRODE-2026 | AI in auditing: balancing quality, professional skepticism, and responsibility (opinion; interview with the Group CIO of PIA Group and a Nyenrode professor) | Nyenrode Business University | press | 2026-06-18 | https://www.nyenrode.nl/en/news/n/ai-auditing-quality-skepticism-responsibility | full |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting | PCAOB (staff) | regulator | 2024-07 | https://pcaobus.org/documents/generative-ai-spotlight.pdf | full |
| PCAOB-PRIORITIES-2025 | Spotlight: Staff Priorities for 2025 Inspections and Interactions With Audit Committees | PCAOB (staff) | regulator | 2024-12 | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf | full |
| PETERS-2022 | Auditor Automation Usage and Professional Skepticism (working paper) | Tilburg University / SSRN | academic | 2022-12-09 | https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/ | full |
| RSM-ASKLUCA-2026 | RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit (news release) | RSM US | firm | 2026-01-08 | https://www.rsmus.com/newsroom/2026/rsm-launches-ask-luca.html | full |
| STARLING-HOHL-2026 | US SEC Weighs Audit Oversight Changes | Starling Insights | press | 2026-01-22 | https://insights.starlingtrust.com/content/observations/us-sec-weighs-audit-oversight-changes | full |
| STARLING-IMC-2026 | Modernizing US PCAOB Audit Inspections | Starling Insights | press | 2026-09-01 | https://insights.starlingtrust.com/content/observations/modernizing-us-pcaob-audit-inspections | full |
| TRI-FOP-2026 | Future of Professionals Report 2026: what tax and audit firm leaders should be prioritizing now (action-paper summary page; the page carries no date, 2026-07 follows the landscape file) | Thomson Reuters Institute | survey | 2026-07 | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | full |

---

## 6. Gaps

**Not reached or only partly read**
- **PCAOB primary pages.** `pcaobus.org` returned 403 for the QC 1000 amendments release and the Inspections Modernization Council release, so the amendments' text and the council materials were read through Deloitte DART, EisnerAmper and Starling Insights only. The PCAOB's 2026 staff inspection priorities were not found.
- **SEC notice on the QC 1000 amendments** returned 403. Approval status rests on secondary sources dated to 8 October 2026.
- **QC 1000 technological-resources requirement text** was not opened, so this file does not quote QC 1000's own wording on technological resources.
- **IAASB:** the December 2025 feedback paper, the roundtable summary PDF and the Technology Catalog PDF were not located or opened. The action plan, the project page and two sets of minutes were read.
- **NFRA's own document** and **ACRA's guidance PDF** were not opened. NFRA is read only through a press report; ACRA only through its announcement.
- **AICPA practice aid** needs a login. Part 2's quality-management content comes from Accounting Today and the AICPA release.
- **FRC 2026 Annual Review of Audit Quality**: not reached, so FRC inspection findings specific to AI tools in 2025-26 were not found. **CPAB's 2025 interim inspection report** (cited by CPAB for significant technology findings) was not opened. **CEAOB's October 2024 report** was not tried.
- **Firm transparency reports:** Deloitte UK (2025, 2026) and KPMG International (2025) were read. The PwC UK and US reports returned access denied; EY and others were not tried.
- **SSRN** (a randomised field experiment on LLMs and audit quality, found as a search extract in the landscape) is blocked; it is not used here.

**Not found**
- **Quality evidence for AI output review:** no published error rate, override rate, seeded-error test, parallel-run result or detection rate for reviewers of AI output at any firm; no regulator count of AI-specific inspection findings (CPAB gives instances without numbers).
- **Named-firm evidence on firm-level tool certification** exists only for Deloitte UK (and KPMG, RSM and Deloitte for tool descriptions). No evidence on how EY, PwC, BDO, Grant Thornton or Forvis Mazars govern AI tools.
- **EQR and AI:** no public source describes AI in engagement quality review; IFIAR's survey records only that 26 firms (20%) had an EQR finding in the new 2025 theme.
- **AI in a firm's own quality monitoring or root-cause analysis:** only a regulator question and a principle (use case 17).
- **Job postings, community discussion, podcasts and conference sessions:** none read for this angle; the only conference material is a Deloitte recap of the December 2025 SEC and PCAOB conference. The search quota ran out, so these leads were not pursued.
- **Small and mid-size firm governance:** only the CPA.com benchmark (54 firms), the ICAEW comment and the IAASB's proportionality language.

**Updates to the landscape file**
- IFIAR's second technology report (20 April 2026) is new; the 2025 survey of inspection findings (1 April 2026) is now read in full and its firm-level themes are in section 3.
- The IAASB March 2026 action plan outcome, listed as not found in the landscape, is found: approved, five guides, timetable to June 2027.
- QC 1000 amendments: adopted 9 September 2026, effective 15 December 2026 if the SEC approves, so the landscape's open question is answered as "pending".
- The FRC thematic review of ATT certification covered information requests issued in April 2024; generative AI at the firms was then limited to productivity aids and was outside the review's definition of ATTs (FRC-ATT-2025, Emerging technology; Appendix B).
- The FRC revised supervision approach (25 March 2026) and the Deloitte UK Technology Controls Board (April 2026) are new.
- The AFM report, shown as a 404 in the landscape, opens at the PDF address above.

**Data conflicts and cautions**
- The FRC sandbox "opened" on 4 June 2026 (landscape: June 2026); first-round close dates were not on the release read.
- The Thomson Reuters Institute page has no date; 2026-07 follows the landscape.
- Deloitte's "Single Quality Plan" and "Technology Controls Board" are described only in the firm's own report; no regulator has commented on them in the sources read.
