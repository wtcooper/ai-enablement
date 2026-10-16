# Module deep dive: assurance / quality-management / practice

- **Archetype:** assurance
- **Module:** quality-management. Firm-level quality management of AI (ISQM 1 / PCAOB QC 1000: tool certification and approval, governance, methodology, monitoring and remediation, resourcing) and engagement-level supervision and review of AI output (review control points, automation bias, documentation of AI use), plus interaction with inspectors.
- **Angle:** practice. What firms actually do: AI tool governance and certification processes, firm AI policies, review workflows for AI output, AI-assisted file review and monitoring tools, resourcing tools, named examples and outcomes.
- **Prepared:** 2026-10-16
- **Method note.**
  - Pages were fetched with `curl` (PDFs through `pdftotext`). One preprint refused direct access and was read through the `r.jina.ai` text mirror. Every source in section 5 was opened and read for the parts cited, except `CAQ-RSM-2026`, which is marked `search-only`.
  - The web-search quota ran out partway through this task. Leads that needed a search (the CAQ post on RSM's resourcing tool, EY and PwC UK transparency reports, job postings) were not reached.
  - **Evidence grades in this file.** No entry reaches grade A. The measured figures that exist concern an adjacent process (platform adoption, inspection results) or are self-reported. Regulators describe firm practice without naming firms, so such entries are graded C (no named organization) rather than B. Grade B means a named firm deployment or mechanism with no published quality measurement.
  - **Independent measurement of AI-tool quality at firm level: none found.** No error rates, override rates or parallel-run results for any firm's AI tools are public. The FRC reported that the six largest UK firms did not formally quantify the audit-quality impact of their tools (FRC-ATT-2025).

---

## 1. Summary

- **Firms certify tools, but publish no measurement of what the tools do to quality.**
  - The FRC reviewed certification at the six largest UK firms (BDO, Deloitte, EY, Forvis Mazars, KPMG, PwC), using information requests issued in April 2024. Most had well-established pre-deployment certification. Some were less mature and had no documented policy. Firms were still adding AI-specific risks to certification and building monitoring (FRC-ATT-2025, section 1).
  - No firm formally quantified the audit-quality impact of its tools. Monitoring was mostly usage counts for licensing, and one firm reported usage against targets (FRC-ATT-2025, "Maintenance and monitoring").
  - IFIAR repeated the point in April 2026. Networks differ on whether the global network or the member firm monitors a tool, and IFIAR warned of fragmented coverage (IFIAR-TTF-2026, p. 8).
- **Named firm-level governance mechanisms are few and new.**
  - Deloitte UK set up a Technology Controls Board in April 2026. It reviews technology artefacts before approval for pilot and deployment, and the firm says its certification approach combines the FRC's 2025 thematic review with ISQM (UK) 1 (DELUK-TR-2026, p. 48).
  - KPMG announced ISO/IEC 42001 certification of its own AI management system in November 2025, and said it is the first Big Four firm to hold it (AT-KPMGISO-2025).
  - PwC US said staff were given AI training and access to LLMs for pre-approved work such as administrative tasks before its audit-specific AI launched in October 2025 (CFODIVE-PWC-2026).
  - For EY and PwC UK, the only evidence found is an academic reading of their 2024 UK transparency reports (PREPRINT-AIJGDI-2026).
- **Engagement-level review of AI output is mostly specified in guidance, not measured in practice.**
  - The FRC's March 2026 guidance sets out review of final outputs, oversight at control points, reviewer competence, and training on automation bias. Its worked examples are illustrative, not named firms (FRC-GENAI-2026, pp. 37-38, 43-54).
  - Deloitte UK says engagement teams critically assess, corroborate and approve agent results before use (DELUK-TR-2026, p. 48).
  - IFIAR found in 2024 that 31% of reporting members had findings that a tool was not used as intended, up from 29% (IFIAR-TTF-2025). CPAB's 2025 inspections saw one tool where testing was limited to flagged items, with none on items it rated low risk (CPAB-TECH-2025, p. 1).
- **AI-assisted file review exists at one named firm.** Deloitte UK reported full deployment of Smart Review, a GenAI-based review tool inside Omnia, "to drive consistency and quality" in controls testing. It gave no figures (DELUK-TR-2025, pp. 15, 94). KPMG says its agents can review engagement documentation (KPMG-TR-2025, p. 16).
- **AI-driven resourcing and inspection-side use are thin.** No firm resourcing case could be opened. The SEC Chief Accountant says the SEC asks auditors how they use AI to monitor their quality systems, but no firm answer is public (KPMG-HOHL-2026).
- **Standard-setters are catching up.** The IAASB approved an action plan in March 2026 to issue non-authoritative guides on ISQM 1 and ISA 220 (Revised) for AI-enabled tools, with drafting running to June 2027 (IAASB-TQMPLAN-2026, Table 2). The AICPA's October 2026 practice aid has a section on firms' own AI use under quality management (AICPA-PA-2026).

---

## 2. Use cases

Notes on the entries:

- Function is `risk-compliance-legal` for firm-level quality management and `service-delivery` where the change sits in engagement work.
- Governance entries use pattern `other` (a governance gate or control, not an AI-performed task); the description is in each `notes`.
- Entries graded D are labelled "Idea" in the title.

```yaml
- id: assurance-quality-management-01
  title: "Certify each AI tool in the context of a use case before engagement use (output testing, then limited deployment)"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Firms built certification for tools that are transparent and deterministic. GenAI tools are opaque and can give different outputs for similar inputs, and training data and model logic usually cannot be inspected."
  solution: "Certification treats the unit as a tool plus a use case. It evaluates inputs (library prompts and information sources), architecture and component logic, then tests outputs on default, edge, diverse and known-weakness cases using structured criteria. Tolerance for deficiencies is set together with the planned review. A tool may be released to a few teams before full certification, with fuller procedures run in parallel. Deloitte UK states that its Technology Controls Board reviews technology artefacts before approval for pilot and deployment."
  outcomes:
    - { lever: risk, description: "Deloitte UK created a Technology Controls Board in April 2026 to review technology before pilot and deployment; no result published", figure: "none", measures: "no measure published", provenance: self-reported, source_ref: DELUK-TR-2026 }
    - { lever: risk, description: "FRC found most of the six largest UK firms had well-established certification before AI-specific updates; some processes were less mature and undocumented", figure: "most firms (count not given)", measures: "six largest audit firms reviewed by the FRC; count of firms per observation not stated in the report", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "A central team and methodology team that sign off each certification"
    - "Test sets of representative cases from the target engagements"
    - "A defined list of use cases, because breadth of definition drives the number of certifications"
  risks_and_guardrails:
    - "Training data and component logic are often unavailable, which shifts weight to output testing (FRC-GENAI-2026, pp. 30-32)"
    - "FRC found only two firms captured tool limitations in certification templates, and some templates did not say users must assess input data (FRC-ATT-2025, 'Certification and implementation')"
    - "FRC findings are a snapshot of Q2 2024, when GenAI at these firms was limited to chatbots, so AI-specific certification practice had not been observed (FRC-ATT-2025, 'Emerging technology')"
  human_checkpoints:
    - "Tool owner, methodology and business sign-off on certification"
    - "Judgement on tolerance for output deficiencies, linked to the review that will follow"
  role_evolution: "Central technology and methodology teams take on certification as a defined role; methodology staff are asked to understand tool limits so guidance matches what outputs can support (FRC-GENAI-2026, p. 40)."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "Certification, pp. 30-33" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: "2025-06-26", access: full, locator: "sections 1 and 3" }
    - { ref: DELUK-TR-2026, title: "2026 Transparency Report, Deloitte LLP and Deloitte Limited", publisher: "Deloitte UK", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: "2026-09", access: full, locator: "Appendix 5, Technology Controls Board, p. 48" }
  last_reviewed: 2026-10-16
  notes: "Grade B: Deloitte UK is a named mechanism with no measurement. The FRC thematic review is of non-GenAI tools (adjacent), so it supports the base process only. The FRC HTML page carries a warning that it was converted from PDF by an AI tool and not human-verified; the PDF is the official version. Date for DELUK-TR-2026 is from PDF metadata (created 2026-09-29); the report covers the year ended 31 May 2026."

- id: assurance-quality-management-02
  title: "Central technology approval body and tool inventory that blocks unapproved or retired tools"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ coordination-scheduling, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "AI tools multiply faster than firms can approve them, engagement teams can reach tools outside firm channels, and firms generally did not monitor that teams used only authorised, current tools."
  solution: "A named governance body approves tools, a central inventory lists certified tools and live versions, and preventive controls restrict software downloads and remove outdated versions. Deloitte UK created a Technology Controls Board; an academic reading of 2024 UK transparency reports says EY routes technology concepts through a global committee and Deloitte uses use-case approval and risk thresholding."
  outcomes:
    - { lever: risk, description: "No outcome published. FRC observed that most firms keep central inventories of certified tools and rely on preventive controls rather than monitoring tool use", figure: "most firms (count not given)", measures: "six largest UK audit firms reviewed by the FRC; count per observation not stated", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "An owner for every tool, with certification records held centrally"
    - "Software distribution controls (repositories, removal of outdated versions, licence management)"
  risks_and_guardrails:
    - "FRC: firms generally relied on preventive controls and did not monitor that teams used only authorised and current tools (FRC-ATT-2025)"
    - "IFIAR asks for oversight programmes that also catch non-approved or decommissioned tools (IFIAR-TTF-2026, p. 6)"
    - "The IAASB's action plan lists engagement teams accessing tools outside the firm's approval channels as a case its guides will address (IAASB-TQMPLAN-2026, para 25(c))"
  human_checkpoints:
    - "Approval body decision before pilot and before deployment"
  role_evolution: "Firms add technology-risk roles to quality governance. Deloitte UK's Chief AI Officer is responsible for embedding responsible AI governance across client services and internal operations (DELUK-TR-2026, leadership biographies)."
  evidence_grade: B
  sources:
    - { ref: DELUK-TR-2026, title: "2026 Transparency Report, Deloitte LLP and Deloitte Limited", publisher: "Deloitte UK", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: "2026-09", access: full, locator: "Appendix 5, p. 48" }
    - { ref: PREPRINT-AIJGDI-2026, title: "Professional Judgment and AI Governance in Audit and Sustainability Assurance: Public Evidence from the UK Big Four", publisher: "Preprints.org (later published in Journal of Risk and Financial Management 2026, 19(9), 675)", type: academic, url: "https://www.preprints.org/manuscript/202607.1693/v1", date: "2026-07", access: full, locator: "sections 4.2 and 4.3" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: "2025-06-26", access: full, locator: "Certified tool repositories; Restricting access to unapproved or outdated ATTs" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: "2026-04-20", access: full, locator: "Network-wide and member firm-level considerations, p. 6" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: "2026-03", access: full, locator: "paras 25-31" }
  last_reviewed: 2026-10-16
  notes: "EY and Deloitte mechanisms come from the preprint's reading of 2024 UK transparency reports (EY 2024 pp. 36-37; Deloitte 2024 pp. 90-92, 108); those reports were not opened by this analyst. The preprint author used generative AI for language and drafting support, one coder, four firms, one reporting cycle."

- id: assurance-quality-management-03
  title: "Risk-tiered permitted-use policy: approved tools, pre-approved uses, barred uses, validation scaled to risk"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, document-production ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Staff will use general AI tools unless the firm says which are allowed and for what. Treating a translation aid and a tool that selects samples with the same scrutiny wastes effort or leaves risk uncovered."
  solution: "The firm lists permitted tools and uses, limits some uses (including barring GenAI on audit procedures at some firms), and scales validation to risk. PwC US gave staff AI training and LLM access for pre-approved work such as administrative tasks before launching audit-specific AI. NFRA says validation should be proportionate and distinguishes low-risk tools such as translation aids from agentic tools that select and test samples."
  outcomes:
    - { lever: risk, description: "No measured outcome. PCAOB staff outreach (July 2024) found some firms barred GenAI in audit or attest procedures and others allowed it for administrative tasks and initial drafts", figure: "some firms (count not given)", measures: "audit firms in PCAOB staff outreach, mainly larger firms; count not stated", provenance: independent, source_ref: PCAOB-GENAI-2024 }
  prerequisites:
    - "An approved-tool list and a data-handling rule on what may be uploaded"
    - "A risk classification for tools and uses"
  risks_and_guardrails:
    - "Data privacy and confidentiality: some firms restrict what information may be uploaded to firm GenAI tools (PCAOB-GENAI-2024, p. 4)"
    - "IRBA gives examples of firm policies: permit only certain tools, set minimum qualifications to use them, mandate training, specify the engagement partner's responsibilities (IRBA-SPA11-2025, section B)"
  human_checkpoints:
    - "Auditors are expected to comply with firm policy, for example by using only firm-approved tools, and the engagement partner is responsible for appropriate use (IRBA-SPA11-2025, paras 19-20)"
  role_evolution: "Not described in the sources beyond added training duties."
  evidence_grade: B
  sources:
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: "CFO Dive", type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: "2026-10-07", access: full, locator: "paragraph beginning 'Prior to last year's launch'" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting", publisher: "PCAOB", type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: "2024-07", access: full, locator: "Observations Related to GenAI Integration in Audits, pp. 4-5" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: "CAalley.com (reporting NFRA Staff Series)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: "2026-07-24", access: full, locator: "section 'Risk based governance for audit technology'" }
    - { ref: IRBA-SPA11-2025, title: "Staff Audit Practice Alert 11: integration of generative AI into the audit process", publisher: "Independent Regulatory Board for Auditors (South Africa)", type: regulator, url: "https://www.irba.co.za/upload/Staff%20Practice%20Alert%2011%20Sep%202025.pdf", date: "2025-09", access: full, locator: "section B, paras 14-21" }
  last_reviewed: 2026-10-16
  notes: "The PCAOB view is staff outreach from mid-2024 and not Board policy. The NFRA document is a staff series and not policy; NFRA's primary document was not reached, so the content is from a press report of it."

- id: assurance-quality-management-04
  title: "Recertification triggers and change control when models, vendors or prompts change"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, software-systems ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Approval of a tool before deployment says little about its later reliability when the underlying model or vendor changes. FRC found trigger identification at the six largest UK firms generally informal."
  solution: "Define triggers for recertification (material component or input change, a materially different use case, observed performance issues, changed standards or policies, elapsed time). Two firms had ATT owners confirm annually that no change needs recertification, and one firm enforced a minimum three-year recertification. NFRA says model updates, data-source changes and vendor changes should trigger revalidation."
  outcomes:
    - { lever: risk, description: "No outcome published. FRC observed formal recertification typically only on change, two firms with annual owner confirmation, and one firm with a three-year backstop", figure: "2 firms (annual confirmation); 1 firm (three-year backstop)", measures: "firms among the six largest UK audit firms reviewed by the FRC", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "Version control and change management that reach vendor and model updates"
    - "A named owner per tool"
  risks_and_guardrails:
    - "FRC: triggers were generally informal and relied on tool owners spotting them (FRC-ATT-2025, 'Recertification of ATTs already in use')"
    - "CPAB suggests a policy on how often tool effectiveness is reassessed, for example when a new version of the underlying large language model is introduced (CPAB-TECH-2025, p. 3)"
  human_checkpoints:
    - "Tool owner annual confirmation; quality leadership decision to recertify"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: "2025-06-26", access: full, locator: "Maintenance and monitoring" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "Recertification, p. 33" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: "CAalley.com (reporting NFRA Staff Series)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: "2026-07-24", access: full, locator: "section 'Governance must come before deployment'" }
    - { ref: CPAB-TECH-2025, title: "The evolving use of technology in the audit", publisher: "CPAB (Canada)", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: "2025-12", access: full, locator: "Firm and network-level considerations, p. 3" }
  last_reviewed: 2026-10-16
  notes: "Grade C: the practice is observed by a regulator at unnamed firms, and it concerns non-GenAI tools, so the evidence is adjacent for AI."

- id: assurance-quality-management-05
  title: "Allocate tool monitoring between the global network and member firms; add member-firm certification of globally certified tools"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ coordination-scheduling, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "ISQM 1 applies to each member firm, yet tools are built and certified by the network. IFIAR members saw unclear responsibility for monitoring globally developed tools, with fragmented coverage as a risk."
  solution: "Two of the six largest UK firms required a UK owner and UK-level certification for globally certified tools, relying partly on global steps. IFIAR asks networks to set clear policies that allocate monitoring risk and responsibility between network and member firm, and to feed local issues back to the global team. The IAASB's action plan says the firm keeps responsibility for approving tools and monitoring them wherever the activity occurs."
  outcomes:
    - { lever: risk, description: "No outcome published. Two firms required UK-level certification of global tools; the review describes a range of practice, from full UK-level certification to none", figure: "2 of the six firms reviewed", measures: "firms among the six largest UK audit firms reviewed by the FRC that required a UK owner and UK-level certification of globally certified ATTs", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "Network policy that names who monitors each tool"
    - "A feedback route from member firms to the global tool owner"
  risks_and_guardrails:
    - "IFIAR: some networks monitor at global level and others at member-firm level, so evaluation may be fragmented and incomplete (IFIAR-TTF-2026, p. 8)"
  human_checkpoints:
    - "Member-firm quality leader accepts the tool for the firm's system of quality management"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: "2025-06-26", access: full, locator: "Global versus UK certification" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits - observations, risks and further evolution", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "ISQM 1 perspectives, point 1" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: "2026-04-20", access: full, locator: "Strengthening oversight as technology evolves, p. 8" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: "2026-03", access: full, locator: "paras 28-29" }
  last_reviewed: 2026-10-16
  notes: "Firms are unnamed in the FRC report. Adjacent evidence (non-GenAI tools)."

- id: assurance-quality-management-06
  title: "Monitor AI-tool usage and audit-quality impact with defined metrics, dashboards and benchmarking against manual work"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ data-reporting, review-assurance ]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Firms tracked how many teams used a tool, mostly for licensing, but did not quantify how tools affect audit quality. They generally had no KPIs for tool use and monitoring."
  solution: "IFIAR lists emerging practices: thematic reviews across engagements with metrics (engagement coverage, false-positive and false-negative rates against a manual sample, rework rates, escalation incidence), dashboards of usage trends, and internal benchmarking of tool results against traditional methods. One firm reported usage rates against targets for key tools."
  outcomes:
    - { lever: quality, description: "No measured outcome. IFIAR's technology task force noted that some firms have started to establish oversight committees and protocols to validate tool effectiveness, with practices varying significantly", figure: "none", measures: "no measure published", provenance: independent, source_ref: IFIAR-TTF-2026 }
    - { lever: quality, description: "FRC found no formal monitoring by the six largest UK firms to quantify audit-quality impact; one firm reported usage against targets", figure: "0 firms quantified impact; 1 firm reported usage against targets", measures: "firms among the six largest UK audit firms reviewed by the FRC", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "Telemetry from the audit platform on tool use per engagement"
    - "Linkage to internal and external inspection findings and root cause analysis"
  risks_and_guardrails:
    - "IFIAR cautions that technology use should be assessed as part of the whole system of quality management, not standalone (IFIAR-TTF-2026, p. 8)"
    - "The metrics are IFIAR examples, not published firm results"
  human_checkpoints:
    - "Quality leadership reviews metrics and triggers recertification or retraining"
  role_evolution: "Quality and methodology teams need analysts able to run the metrics; not described in sources."
  evidence_grade: C
  sources:
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: "2026-04-20", access: full, locator: "Strengthening oversight as technology evolves, pp. 8-9" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: "2025-06-26", access: full, locator: "Monitoring the use and impact of ATTs" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits - observations, risks and further evolution", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "ISQM 1 perspectives, point 1" }
  last_reviewed: 2026-10-16
  notes: "Piloting is inferred only from IFIAR's statement that some firms have started to build oversight protocols; no firm is named. This is the absence-of-measurement finding for the module."

- id: assurance-quality-management-07
  title: "Idea: escalation pathways, user feedback loops and whistleblowing channels for AI tool anomalies"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, coordination-scheduling ]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Unexpected AI outputs or operational failures may be noticed by engagement teams but not reach the tool owner or quality function."
  solution: "IFIAR lists formal mechanisms for user feedback on whether tools are fit for purpose, formal escalation for unexpected outputs or failures, AI oversight committees, and whistleblowing procedures for ethical concerns about AI use. CPAB lists escalation and whistleblowing processes to identify anomalies in tools."
  outcomes:
    - { lever: risk, description: "none published", figure: "none", measures: "no measure published", provenance: independent, source_ref: IFIAR-TTF-2026 }
  prerequisites:
    - "A tool owner with authority to withdraw or restrict a tool"
  risks_and_guardrails:
    - "Presented by regulators as practices to consider, not as observed firm practice"
  human_checkpoints:
    - "Tool owner or oversight committee decides on withdrawal or recertification"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: "2026-04-20", access: full, locator: "Network-wide and member firm-level considerations, pp. 6-7" }
    - { ref: CPAB-TECH-2025, title: "The evolving use of technology in the audit", publisher: "CPAB (Canada)", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: "2025-12", access: full, locator: "Firm and network-level considerations, p. 3" }
  last_reviewed: 2026-10-16
  notes: "Idea: regulators list it; no firm adoption found."

- id: assurance-quality-management-08
  title: "GenAI-assisted review of engagement files and workpapers"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance, document-production ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Reviewers read workpapers for consistency and completeness against methodology, and review is a bottleneck. PCAOB staff outreach found firms saw potential in AI evaluating the completeness of audit documentation against documentation requirements."
  solution: "Deloitte UK reports that Smart Review, its in-house GenAI-based audit review tool embedded in the Omnia platform, was fully deployed in the year to 31 May 2025 to drive consistency and quality in testing of internal controls. KPMG says its agents can assist teams by reviewing engagement documentation. Neither source describes how human reviewers use the output."
  outcomes:
    - { lever: quality, description: "Deloitte UK reports full deployment of Smart Review for consistency and quality in controls testing; no figure published", figure: "none", measures: "no measure published", provenance: self-reported, source_ref: DELUK-TR-2025 }
  prerequisites:
    - "Methodology encoded so the tool can check work against it"
    - "A platform that holds the engagement file (Omnia, Clara)"
  risks_and_guardrails:
    - "No source reports false-positive or false-negative review comments"
    - "The FRC review standard still applies to the AI tool's own outputs (FRC-GENAI-2026, p. 37)"
  human_checkpoints:
    - "Human reviewer remains responsible for review conclusions (not described further in the sources)"
  role_evolution: "Not described. Deloitte says practitioners remain responsible for challenging and validating technology outputs (DELUK-TR-2026, p. 48)."
  evidence_grade: B
  sources:
    - { ref: DELUK-TR-2025, title: "2025 Transparency Report, Deloitte LLP and Deloitte Limited", publisher: "Deloitte UK", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf", date: "2025-09", access: full, locator: "PDF pp. 7, 15, 94" }
    - { ref: KPMG-TR-2025, title: "Transparency Report 2025", publisher: "KPMG International", type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/12/transparency-report-fy25.pdf", date: "2025-12", access: full, locator: "p. 16, 'AI in the audit now and in the future'" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting", publisher: "PCAOB", type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: "2024-07", access: full, locator: "pp. 4-5" }
  last_reviewed: 2026-10-16
  notes: "The Smart Review description is a file-review aid inside controls testing, so it sits between this module and controls-testing. Deloitte UK's reported period is the year ended 31 May 2025; date for DELUK-TR-2025 is from PDF metadata (created 2025-09-30). Nothing found on KPMG's review agents beyond the sentence cited."

- id: assurance-quality-management-09
  title: "Idea: AI-assisted internal inspections, root cause analysis and quality monitoring"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance, data-reporting ]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Inspectors find firms' own monitoring weak. IFIAR counted 21 findings in 2025 for failing to identify audit performance issues when performing internal inspections, against 6 in 2024, and 10 findings on root cause analysis or remedial actions."
  solution: "The SEC Chief Accountant says the SEC asks auditors how they use AI to improve engagement-level quality and how they use AI to monitor their system of quality control. No firm example was found."
  outcomes:
    - { lever: quality, description: "none published", figure: "none", measures: "no measure published", provenance: independent, source_ref: KPMG-HOHL-2026 }
  prerequisites:
    - "Structured inspection and root-cause data that AI could analyse"
  risks_and_guardrails:
    - "IFIAR's 2025 survey shows no AI-specific category in firm-wide quality management findings (IFIAR-SURVEY-2026, Appendix A)"
  human_checkpoints:
    - "Quality leadership owns conclusions on the system of quality management"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: KPMG-HOHL-2026, title: "Q&A with SEC Chief Accountant Kurt Hohl", publisher: "KPMG Board Leadership Center", type: firm, url: "https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html", date: "2026-05-27", access: full, locator: "answer on SEC OCA priorities" }
    - { ref: IFIAR-SURVEY-2026, title: "Survey of Inspection Findings 2025", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: "2026-04-01", access: full, locator: "Appendix A, Table A.3 (monitoring and remediation sub-categories)" }
  last_reviewed: 2026-10-16
  notes: "Idea: the regulator asks the question; nothing public on firm answers. The page date is 2026-05-27; the interview date is not stated on the opened page. IFIAR figures are counts of findings across member firms inspected, as reported by members. The PCAOB inspections council's AI pilots (landscape, secondary source) were not opened."

- id: assurance-quality-management-10
  title: "AI-assisted staffing and resourcing of engagements"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ coordination-scheduling ]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "Matching people to engagements by experience, budget and availability is a quality objective under ISQM 1 (human resources) and a bottleneck in busy season."
  solution: "The landscape file reports that RSM US has an AI staffing tool, Luca Resourcing, for initial staffing requests, budget planning and engagement-leader review (CAQ blog, 25 Aug 2026). That post was not opened here. IRBA's alert lists resource optimisation using AI to analyse staff profiles and experience as an example of AI in audit planning, sourced from the IAASB's digital technology market scan."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none", measures: "no measure published", provenance: self-reported, source_ref: CAQ-RSM-2026 }
  prerequisites:
    - "Staff skills and availability data in a structured system"
  risks_and_guardrails:
    - "Competence and capabilities are an ISQM 1 resourcing objective; IFIAR found human-resources findings at 24% of firms in 2025 (IFIAR-SURVEY-2026, Table A.2)"
  human_checkpoints:
    - "Engagement leader reviews the staffing proposal (per the landscape summary of RSM's tool)"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: CAQ-RSM-2026, title: "CAQ Audit in Action blog on RSM's AI tools (Ask Luca, Copilot, Luca Resourcing)", publisher: "Center for Audit Quality", type: professional-body, url: "https://www.thecaq.org/audit-in-action", date: "2026-08-25", access: search-only, locator: "not opened; carried from the landscape file, section 4 item P3" }
    - { ref: IRBA-SPA11-2025, title: "Staff Audit Practice Alert 11: integration of generative AI into the audit process", publisher: "Independent Regulatory Board for Auditors (South Africa)", type: regulator, url: "https://www.irba.co.za/upload/Staff%20Practice%20Alert%2011%20Sep%202025.pdf", date: "2025-09", access: full, locator: "section B table, 'Planning the audit'" }
    - { ref: IFIAR-SURVEY-2026, title: "Survey of Inspection Findings 2025", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: "2026-04-01", access: full, locator: "Table A.2" }
  last_reviewed: 2026-10-16
  notes: "The RSM tool rests on a search-only source (carried from the landscape), so it cannot support a higher grade. The CAQ audit-in-action page that was opened lists only three posts and not this one; the URL given is the listing page. The IFIAR 24% is the share of member firms inspected with at least one human-resources finding (32 firms); the denominator is not stated in the text."

- id: assurance-quality-management-11
  title: "Due diligence and contract terms for third-party AI tools and foundation models"
  archetype: assurance
  module: quality-management
  function: procurement-supply-chain
  work_types: [ review-assurance, coordination-scheduling ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Firms usually obtain a foundation model from a third party and cannot see its training data or internal logic. Smaller firms rely on vendors more than the largest firms do."
  solution: "All six largest UK firms considered vendor control environments, data security and confidentiality when selecting a third-party tool, using supplier questionnaires or assurance reports. One firm ran pilots with several vendors before choosing. NFRA says contracts should cover data protection, explainability documentation, audit rights and business continuity."
  outcomes:
    - { lever: risk, description: "No outcome published", figure: "none", measures: "no measure published", provenance: independent, source_ref: FRC-ATT-2025 }
  prerequisites:
    - "Procurement process with security and quality review"
  risks_and_guardrails:
    - "NFRA warns firms against relying on vendor accuracy claims without independent evaluation (NFRA-CAALLEY-2026)"
    - "FRC: third-party assurance on a component may inform testing, but the firm may still test it for the use case (FRC-GENAI-2026, p. 32)"
    - "IAASB stakeholders raised an uneven playing field where larger firms are better able than small and medium practices to govern such tools (IAASB-TQMPLAN-2026, para 11)"
  human_checkpoints:
    - "Procurement and quality sign-off before onboarding"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: "2025-06-26", access: full, locator: "Design or selection, 'Where firms opt to source an ATT from a third-party'" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: "CAalley.com (reporting NFRA Staff Series)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: "2026-07-24", access: full, locator: "section 'Greater scrutiny of technology vendors'" }
    - { ref: AFM-2025, title: "12 building blocks for controlled use of advanced (Gen)AI auditing tools", publisher: "Netherlands Authority for the Financial Markets", type: regulator, url: "https://www.afm.nl/en/sector/actueel/2025/dec/pb-12-bouwstenen-beheerst-gebruik-audit-tooling", date: "2025-12-11", access: full, locator: "press release text" }
    - { ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material", publisher: "IAASB", type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: "2026-03", access: full, locator: "paras 11, 25" }
  last_reviewed: 2026-10-16
  notes: "Adjacent evidence (FRC covers non-GenAI tools). The AFM press release says some larger firms lead on policies and risk management and there is room for improvement everywhere; the 12 building blocks PDF itself was not opened."

- id: assurance-quality-management-12
  title: "ISO/IEC 42001 certification of the firm's own AI management system"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Firms need external reference points for governing their own AI use, because no single authority or framework for AI governance exists."
  solution: "KPMG announced in November 2025 that it achieved ISO 42001 certification, which it described as independent validation that its internal AI management systems align with emerging global standards, and as a necessary precursor to providing AI assurance services. KPMG said it is the first Big Four firm to achieve it. The announcement does not say which KPMG entity was certified."
  outcomes:
    - { lever: risk, description: "Certification achieved; no quality measurement published", figure: "none", measures: "no measure published", provenance: self-reported, source_ref: AT-KPMGISO-2025 }
  prerequisites:
    - "An accredited certification body and a documented AI management system"
  risks_and_guardrails:
    - "A management-system certificate shows governance, not that any tool's output is reliable on an engagement"
    - "SEC staff said at the December 2025 conference that there is no single authority or framework for AI governance, so preparers should judge whether a framework is fit for purpose; that remark was about preparers, not audit firms (RSM-SECPCAOB-2025, section 2.1)"
  human_checkpoints:
    - "Not described"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: AT-KPMGISO-2025, title: "Tech News: KPMG hails ISO 42001 certification", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/list/tech-news-kpmg-hails-iso-42001-certification", date: "2025-11-21", access: full, locator: "first item" }
    - { ref: FIELDGUIDE-PCAOB-2026, title: "PCAOB AI oversight: where the Board stands on AI in audit", publisher: "Fieldguide", type: vendor, url: "https://www.fieldguide.io/resource-articles/pcaob-ai-audit-standards", date: "2026-08-06", access: full, locator: "section 'How firms should evaluate AI tools under PCAOB expectations'" }
    - { ref: RSM-SECPCAOB-2025, title: "Insights from the 2025 AICPA Conference on Current SEC and PCAOB Developments", publisher: "RSM US", type: conference, url: "https://rsmus.com/content/dam/rsm/insights/financial-reporting/1pdf/insights-from-the-2025-aicpa-conference-on-current-sec-and-pcaob-developments-12-25.pdf", date: "2025-12", access: full, locator: "section 2.1, 'Controls and governance'" }
  last_reviewed: 2026-10-16
  notes: "Fieldguide says it holds ISO 42001 certification (vendor statement). The 'first of Big Four' statement is KPMG's, reported by Accounting Today via a KPMG spokesperson."

- id: assurance-quality-management-13
  title: "Mandatory pre-access AI training and role-specific training for reviewers"
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [ coordination-scheduling, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Reviewers who cannot judge when AI output is wrong cannot review it. FRC warns that tools sound fluent and confident even when wrong, and that automation bias must be taught."
  solution: "FRC guidance says training should cover when and how to use a tool, how to review and oversee it, automation bias, and known tool weaknesses, and is ongoing. In practice, per an academic reading of 2024 UK transparency reports, PwC made GenAI fundamentals training mandatory before access to ChatPwC, and KPMG trained all auditors in prompt engineering at its 2024 Audit University. NFRA says training should differ by role: preparers on safe use, reviewers on critical evaluation and bias awareness, engagement partners on governance and disclosure judgement."
  outcomes:
    - { lever: quality, description: "No outcome published", figure: "none", measures: "no measure published", provenance: self-reported, source_ref: PREPRINT-AIJGDI-2026 }
  prerequisites:
    - "Access control that ties tool access to training completion"
  risks_and_guardrails:
    - "The preprint reports prompt skill alone is not professional competence; it is the author's view (PREPRINT-AIJGDI-2026, section 4.4)"
    - "IFIAR asks that training maps to competencies, with records and refresher intervals proportionate to risk (IFIAR-TTF-2026, p. 7)"
  human_checkpoints:
    - "Training completion gates tool access"
  role_evolution: "Deloitte UK describes an AI-fluency workstream and firm-wide AI learning covering critical judgement, human skills and responsible use (DELUK-TR-2026, risk response lists)."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "Staff education and governance, pp. 34-36" }
    - { ref: PREPRINT-AIJGDI-2026, title: "Professional Judgment and AI Governance in Audit and Sustainability Assurance: Public Evidence from the UK Big Four", publisher: "Preprints.org (later published in Journal of Risk and Financial Management 2026, 19(9), 675)", type: academic, url: "https://www.preprints.org/manuscript/202607.1693/v1", date: "2026-07", access: full, locator: "section 4.4" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: "CAalley.com (reporting NFRA Staff Series)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: "2026-07-24", access: full, locator: "section 'Audit documentation and training to change'" }
    - { ref: DELUK-TR-2026, title: "2026 Transparency Report, Deloitte LLP and Deloitte Limited", publisher: "Deloitte UK", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: "2026-09", access: full, locator: "risk response lists, 'Firmwide AI learning'" }
  last_reviewed: 2026-10-16
  notes: "PwC and KPMG details are second-hand: they come from the preprint's reading of PwC UK 2024 (pp. 110-112) and KPMG UK 2025 (pp. 36-37) transparency reports, which this analyst did not open."

- id: assurance-quality-management-14
  title: "In-workflow AI tutor for on-demand micro-training while doing the work"
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [ coordination-scheduling, research-synthesis ]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Classroom training reaches staff before the work and fades. Teams need help interpreting tool output and methodology at the point of use."
  solution: "Deloitte announced on 24 June 2026 that Omnia's agentic network includes a tutor mode giving Audit & Assurance professionals on-demand micro-training in the context of the work being performed. It also names the Deloitte AI Academy and Scout, an AI learning assistant, and says professionals will supervise, validate and work alongside AI."
  outcomes:
    - { lever: quality, description: "none published", figure: "none", measures: "no measure published", provenance: self-reported, source_ref: DELOITTE-OMNIA-2026 }
  prerequisites:
    - "Methodology and guidance content that the tutor can draw on"
  risks_and_guardrails:
    - "FRC says education is ongoing, not only at launch (FRC-GENAI-2026, p. 34)"
  human_checkpoints:
    - "Not described"
  role_evolution: "Deloitte says professionals will supervise, validate and work alongside AI (DELOITTE-OMNIA-2026)."
  evidence_grade: C
  sources:
    - { ref: DELOITTE-OMNIA-2026, title: "Deloitte unveils connected agentic intelligence in Deloitte Omnia to advance audit and assurance", publisher: "Deloitte", type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: "2026-06-24", access: full, locator: "section 'Investing in upskilling for an AI-enabled future'" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "Staff education, p. 34" }
  last_reviewed: 2026-10-16
  notes: "Announced only; no evidence of use found. The press release does not describe tutor mode in detail."

- id: assurance-quality-management-15
  title: "Human-in-the-loop control points built into agent workflows, with reviewers corroborating output against source"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Agents run multi-step procedures. Without defined review points, errors compound and reviewers either re-do everything or accept plausible output."
  solution: "FRC guidance places oversight at control points set by criteria (for example when an intermediate output is ready), and defines review of final outputs as evaluating completeness, accuracy and consistency with the reviewer's understanding of the entity, sometimes by forming an independent view. In its worked example the reviewer reads the board minutes themselves, with closer reading where output conflicts with prior understanding. Deloitte UK says its engagement teams critically assess, corroborate and approve agent results before they are used; KPMG describes human-in-the-loop under its Trusted AI framework."
  outcomes:
    - { lever: quality, description: "None published. Deloitte UK and KPMG describe the control; neither reports review results", figure: "none", measures: "no measure published", provenance: self-reported, source_ref: DELUK-TR-2026 }
  prerequisites:
    - "Agents that cite their sources, so reviewers can check them"
    - "Methodology that states what the review must include"
  risks_and_guardrails:
    - "FRC and NFRA name automation bias as a main risk in review and oversight (FRC-GENAI-2026, pp. 37-38; NFRA-CAALLEY-2026)"
    - "CPAB: stating that a human is in the loop is not enough; firms need a behaviour shift and clear articulation of involvement at each stage (CPAB-TECH-2025, p. 5)"
    - "IFIAR 2024 survey: 31% of reporting members had findings that a tool was not used as intended; common findings were misreading tool results and thin testing of outliers (IFIAR-TTF-2025, p. 5)"
  human_checkpoints:
    - "Review of final outputs by an engagement-team member with appropriate competence"
    - "Authorisation or review of intermediate steps at defined control points"
  role_evolution: "Staff move from preparing to reviewing. Holmstrom and Peters propose that this shift may reduce auditors' autonomy and skill-building (HOLMSTROM-2024, introduction); the paper is a proposal, with no results."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "Human in the loop review and oversight, pp. 37-38; example 1, p. 46; example 2, pp. 50-54" }
    - { ref: DELUK-TR-2026, title: "2026 Transparency Report, Deloitte LLP and Deloitte Limited", publisher: "Deloitte UK", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf", date: "2026-09", access: full, locator: "Appendix 5, Technology, p. 48" }
    - { ref: KPMG-TR-2025, title: "Transparency Report 2025", publisher: "KPMG International", type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/12/transparency-report-fy25.pdf", date: "2025-12", access: full, locator: "p. 16" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits - observations, risks and further evolution", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "Inspection findings related to technology, p. 5" }
    - { ref: CPAB-TECH-2025, title: "The evolving use of technology in the audit", publisher: "CPAB (Canada)", type: regulator, url: "https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf", date: "2025-12", access: full, locator: "Clearly defining the role of auditors, p. 5" }
    - { ref: HOLMSTROM-2024, title: "How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal)", publisher: "PCAOB registered reports conference materials (Holmstrom and Peters)", type: academic, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf", date: "2024-06", access: full, locator: "Introduction" }
  last_reviewed: 2026-10-16
  notes: "Grade B rests on Deloitte UK's statement of the control, with no measurement. The FRC examples are illustrative and not named firms. The IFIAR 31% is the share of IFIAR Members reporting findings; it covers tool use broadly, not GenAI review specifically. HOLMSTROM-2024 date is the PDF creation date (2024-06); the pilot dated the paper to the 2025 conference, so the date is uncertain. In the landscape this module is split from controls-testing; PwC's Evidence Match and similar agents are routed to substantive-testing."

- id: assurance-quality-management-16
  title: "Source citations and traces in agent output so reviewers can verify it"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance, document-production ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Fluent output without sources cannot be checked efficiently, which weakens review and the inspection trail."
  solution: "FRC's worked examples have the tool segment documents with stable identifiers and cite them for every extract, which both reduces fabrication and supports review. PwC describes each Evidence Match result as carrying a clear evidence trail. Fieldguide says each agent run produces a Trace of inputs, outputs and reasoning, kept with the engagement record. RSM and Andera say their platform generates annotated documentation with full traceability to source."
  outcomes:
    - { lever: quality, description: "No measured outcome. Vendor says the Trace record supports inspection conversations", figure: "none", measures: "no measure published", provenance: vendor-published, source_ref: FIELDGUIDE-PCAOB-2026 }
  prerequisites:
    - "Tool design that requires citations; reviewers trained to check them"
  risks_and_guardrails:
    - "A citation shows where text came from, not that the reading is right; FRC still expects review to compare against source (FRC-GENAI-2026, p. 37)"
    - "AFM expects GenAI results to be traceable or replicable (AFM-2025)"
  human_checkpoints:
    - "Reviewer checks cited sources, with more detail where output conflicts with prior understanding"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "example 1, p. 44; example 2, p. 51" }
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: "Accounting Today", type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: "2025-10-28", access: full, locator: "paragraph on Evidence Match" }
    - { ref: FIELDGUIDE-PCAOB-2026, title: "PCAOB AI oversight: where the Board stands on AI in audit", publisher: "Fieldguide", type: vendor, url: "https://www.fieldguide.io/resource-articles/pcaob-ai-audit-standards", date: "2026-08-06", access: full, locator: "final section" }
    - { ref: AFM-2025, title: "12 building blocks for controlled use of advanced (Gen)AI auditing tools", publisher: "Netherlands Authority for the Financial Markets", type: regulator, url: "https://www.afm.nl/en/sector/actueel/2025/dec/pb-12-bouwstenen-beheerst-gebruik-audit-tooling", date: "2025-12-11", access: full, locator: "'Humans remain ultimately responsible' paragraph" }
    - { ref: CPAPRACTICE-RSMANDERA-2026, title: "Andera and RSM US Partner to Create AI-Enabled Control Testing Platform for Internal Audit", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/", date: "2026-08-26", access: full, locator: "paragraph beginning 'By entering into this strategic alliance'" }
  last_reviewed: 2026-10-16
  notes: "Grade C: the named-customer evidence is a vendor description and PwC's tool is a substantive-testing tool (routed). The RSM and Andera capability is an announcement of an alliance (CPAPRACTICE-RSMANDERA-2026), and it concerns internal-audit control testing, so it is adjacent."

- id: assurance-quality-management-17
  title: "Document AI use on the engagement file: tool, purpose, how output informed the work, with central records for the rest"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ document-production, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Inspectors and senior reviewers cannot challenge AI-assisted work if the file does not show where AI was used and how the team responded. Without it, internal monitoring cannot find AI use either."
  solution: "In the FRC's worked examples the auditor records on the audit file that an AI-enabled tool was used, how its output informed further work, and the conclusion, while certification documentation stays central. IFIAR asks firms to identify uses of GenAI in critical audit areas, which helps seniors, internal monitoring and inspectors. NFRA wants a structured format showing which tool processed a balance and the extent of human review. An academic reading of PwC UK's 2024 report says PwC requires clear documentation where approved GenAI use cases are used."
  outcomes:
    - { lever: risk, description: "No outcome published", figure: "none", measures: "no measure published", provenance: independent, source_ref: PREPRINT-AIJGDI-2026 }
  prerequisites:
    - "File templates with a field for AI use; central retention of certification records"
  risks_and_guardrails:
    - "The preprint found none of the four UK firms' 2024 reports stated model-level performance, override frequency or drift monitoring; this is a limit of public disclosure, not proof of absence (PREPRINT-AIJGDI-2026, section 4.2)"
  human_checkpoints:
    - "Engagement team records use; senior team members reflect on the overall use of technology on the file (IFIAR-TTF-2026, p. 7)"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "example 1, p. 43; example 2, p. 50" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits - observations, risks and further evolution", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "GenAI governance, 'Transparency'" }
    - { ref: NFRA-CAALLEY-2026, title: "NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement", publisher: "CAalley.com (reporting NFRA Staff Series)", type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: "2026-07-24", access: full, locator: "section 'Audit documentation and training to change'" }
    - { ref: PREPRINT-AIJGDI-2026, title: "Professional Judgment and AI Governance in Audit and Sustainability Assurance: Public Evidence from the UK Big Four", publisher: "Preprints.org (later published in Journal of Risk and Financial Management 2026, 19(9), 675)", type: academic, url: "https://www.preprints.org/manuscript/202607.1693/v1", date: "2026-07", access: full, locator: "sections 4.2 and 4.3" }
  last_reviewed: 2026-10-16
  notes: "Grade B rests on PwC UK's stated requirement, read second-hand (PwC UK 2024 transparency report, pp. 110-112, per the preprint; the PwC UK 2025 report returned access denied). The FRC examples are illustrative."

- id: assurance-quality-management-18
  title: "Idea: engagement leader sets out planned AI use at the outset, and senior team members stand back and review it at the end"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ coordination-scheduling, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Under ISA 220 (Revised) the engagement partner is responsible for appropriate use of technological resources, yet teams may use AI in ways the partner has not planned or reviewed."
  solution: "IFIAR asks engagement leaders to set expectations for technology use at the outset and asks senior team members to reflect on overall use of technology in the file, including whether scepticism was maintained. The AICPA practice aid recommends planning the intended use of AI in specific engagements and sets out partner responsibilities to understand the tools, ensure they are firm-approved and check staff use them correctly. IRBA also places responsibility for appropriate use on the engagement partner."
  outcomes:
    - { lever: quality, description: "none published", figure: "none", measures: "no measure published", provenance: independent, source_ref: AICPA-PA-2026 }
  prerequisites:
    - "Partner training on the tools in use"
  risks_and_guardrails:
    - "Guidance only; no firm deployment found"
  human_checkpoints:
    - "Engagement partner sets and later reviews AI use"
  role_evolution: "Engagement partners take on explicit duties to understand and approve AI use (AICPA-PA-2026)."
  evidence_grade: D
  sources:
    - { ref: AICPA-PA-2026, title: "AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing", publisher: "AICPA & CIMA", type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: "2026-10-13", access: full, locator: "section 'Use of AI-related technological resources by audit firms'" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: "2026-04-20", access: full, locator: "Defining the role of auditors in a technology-enabled audit, p. 7" }
    - { ref: IRBA-SPA11-2025, title: "Staff Audit Practice Alert 11: integration of generative AI into the audit process", publisher: "Independent Regulatory Board for Auditors (South Africa)", type: regulator, url: "https://www.irba.co.za/upload/Staff%20Practice%20Alert%2011%20Sep%202025.pdf", date: "2025-09", access: full, locator: "section B, paras 18-21" }
  last_reviewed: 2026-10-16
  notes: "Idea: from guidance. Only the AICPA press release was opened; the practice aid text is behind a login."

- id: assurance-quality-management-19
  title: "Run fuller procedures in parallel during limited deployment of a new AI tool"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "A tool released to a few teams before certification is complete may produce more deficient outputs, because training, guidance and prompt libraries are not yet refined."
  solution: "The FRC says firms may release a tool to a limited number of teams for feedback before full certification, and that teams often perform the alternative procedures in full, in parallel with the AI-enabled procedure. The thematic review adds that pilots are often run on lower-risk non-PIE audits and on selected sectors before wider deployment."
  outcomes:
    - { lever: risk, description: "No results of parallel runs are published", figure: "none", measures: "no measure published", provenance: independent, source_ref: FRC-GENAI-2026 }
  prerequisites:
    - "Willingness to carry the cost of doing the work twice during the pilot"
  risks_and_guardrails:
    - "Parallel runs can give measurements of tool error against human work; none are public"
  human_checkpoints:
    - "Quality or methodology team decides when a pilot can end"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "Limited deployment, p. 33" }
    - { ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: "2025-06-26", access: full, locator: "Deployment" }
  last_reviewed: 2026-10-16
  notes: "Piloting rests on the FRC's statement that teams often do this. No firm is named and no parallel-run result is public. This is the main route to an independent error-rate measure."

- id: assurance-quality-management-20
  title: "Idea: one model reviews another model's work, or several models attempt a task and a reviewer selects"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "Human reviewers cannot catch every deficiency in high-volume AI output."
  solution: "FRC lists, as design mitigations, one LLM reviewing the work of another (a different model may have different biases, and the same model can be given different priorities) and multiple LLMs attempting a task with an LLM or human selecting. Output from a review LLM can feed human review or escalation. The FRC's contract example has the tool escalate to a human at extraction and evaluation steps."
  outcomes:
    - { lever: quality, description: "none published", figure: "none", measures: "no measure published", provenance: independent, source_ref: FRC-GENAI-2026 }
  prerequisites:
    - "A workflow engine that can route output to a second model and to a human"
  risks_and_guardrails:
    - "FRC says LLM review does not remove the need for human oversight (FRC-GENAI-2026, pp. 25-26)"
  human_checkpoints:
    - "Escalation to a human when the review model disagrees or is unsure"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "System design and development, p. 25" }
  last_reviewed: 2026-10-16
  notes: "Idea: described in regulator guidance as a design option. The AICPA practice aid reportedly says one AI tool may check another without reducing the auditor's duties (landscape R20); not verified here because only the press release was opened."

- id: assurance-quality-management-21
  title: "Early engagement with the regulator on AI adoption (FRC sandbox, IFIAR early engagement)"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [ client-interaction, coordination-scheduling ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Firms adopting AI face unclear regulatory expectations, and regulators say they will inspect AI use. Smaller firms and those relying on vendors have the least capacity to work this out alone."
  solution: "The FRC's Audit Tech & AI Sandbox gives selected UK-registered audit firms about three engagement meetings with FRC experts over three to four months to test adoption against ISQM 1 and FRC guidance. There is no endorsement or approval. First-round applications closed in July 2026. IFIAR encourages early engagement with local regulators and IFIAR when technology may significantly change the work. PCAOB staff said at the December 2025 AICPA conference that firms' AI adoption is a focus area for inspectors."
  outcomes:
    - { lever: risk, description: "No outcome published; participating firms not named", figure: "none", measures: "no measure published", provenance: independent, source_ref: FRC-SANDBOX-2026 }
  prerequisites:
    - "A technology ready for critical evaluation, testing or limited deployment, and time commitment from the firm"
  risks_and_guardrails:
    - "Participation gives no approval, endorsement or compliance guarantee (FRC-SANDBOX-2026)"
    - "PCAOB staff views are not Board policy (DART-SECPCAOB-2025)"
  human_checkpoints:
    - "Firm leadership decides what to bring to the regulator"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FRC-SANDBOX-2026, title: "Audit Tech and AI Sandbox", publisher: "Financial Reporting Council", type: regulator, url: "https://www.frc.org.uk/library/innovation-and-improvement-hub/sandbox-audit-tech-and-ai/", date: "2026-06", access: full, locator: "Overview; Participating in the sandbox; Eligibility" }
    - { ref: ICAS-SANDBOX-2026, title: "Driving audit innovation with FRC sandboxes and forums", publisher: "ICAS", type: professional-body, url: "https://icas.com/news-insights-events/news/audit-assurance/driving-audit-innovation-with-frc-sandboxes-and-forums/", date: "2026-07-07", access: full, locator: "section 'Audit tech and AI'" }
    - { ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality", publisher: "IFIAR", type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: "2026-04-20", access: full, locator: "Key findings and recommendations, p. 4" }
    - { ref: DART-SECPCAOB-2025, title: "Highlights of the 2025 AICPA & CIMA Conference on Current SEC and PCAOB Developments", publisher: "Deloitte DART", type: conference, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways", date: "2025-12-12", access: full, locator: "Executive summary, AI paragraph" }
  last_reviewed: 2026-10-16
  notes: "Sandbox page date is the month of launch (Accountancy Age headline dated 2026-06-08, not opened). Participants and outputs not found."

- id: assurance-quality-management-22
  title: "Standardised audit programmes on an AI-enabled platform, pushed firm-wide to remediate inspection findings and prepare for inspection"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance, coordination-scheduling ]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "A 20-person firm running a legacy platform found that its methodology limited it. Sample-heavy testing created bottlenecks at the partner and at engagement quality review, and QC 1000 was approaching."
  solution: "Sanville & Company built its audit programmes in Fieldguide, referencing PCAOB standards in each step, and sent templates to every engagement at once. Agentic testing handled sample-heavy tracing of incoming client support. After an earlier PCAOB exam flagged an issue, the partner updated the programme and pushed it to every open engagement the next morning. The firm's first PCAOB inspection on the platform had zero comment forms."
  outcomes:
    - { lever: quality, description: "First PCAOB inspection conducted entirely on the platform (a broker-dealer engagement) had zero comment forms", figure: "0 comment forms", measures: "comment forms on the firm's first PCAOB inspection on Fieldguide", provenance: vendor-published, source_ref: FIELDGUIDE-SANVILLE-2026 }
    - { lever: speed, description: "Platform and methodology overhaul completed in under a year, against an expected 18 to 24 months", figure: "under 1 year vs 18-24 months expected", measures: "time to complete the platform and methodology overhaul, per the partner", provenance: vendor-published, source_ref: FIELDGUIDE-SANVILLE-2026 }
    - { lever: growth, description: "Blended realization on the firm's lowest-margin engagements rose from $150-200 an hour to $250 or more", figure: "$150-200/hr to $250+/hr", measures: "blended realization per hour on the firm's lowest-margin engagements, per the vendor's customer story", provenance: vendor-published, source_ref: FIELDGUIDE-SANVILLE-2026 }
  prerequisites:
    - "A methodology-agnostic platform where the firm writes its own audit programmes"
    - "Small, aligned team willing to move to the platform at once"
  risks_and_guardrails:
    - "One inspection and one firm; a zero-comment result does not isolate AI as the cause, and the figures come from a vendor customer story"
    - "The PCAOB statement about the firm's AI use is quoted by the partner, not published by the PCAOB"
  human_checkpoints:
    - "Partners update programmes; reviewers approve work on the platform"
  role_evolution: "The partner says first-year staff now do complex revenue testing because reviewers have bandwidth to guide them (FIELDGUIDE-SANVILLE-2026)."
  evidence_grade: B
  sources:
    - { ref: FIELDGUIDE-SANVILLE-2026, title: "How Sanville & Co passed a PCAOB inspection with zero comment forms in under a year with Fieldguide", publisher: "Fieldguide", type: vendor, url: "https://www.fieldguide.io/case-studies/how-sanville-co-passed-a-pcaob-inspection-with-zero-comment-forms-in-under-a-year-with-fieldguide", date: "2026", access: full, locator: "Key Results at a Glance; sections 'A Methodology That Was Fighting the Firm' to 'A Clean Inspection and a Faster Path'" }
  last_reviewed: 2026-10-16
  notes: "Grade B, not A: the figures are named and measured but vendor-published and measure an adjacent change (platform and methodology overhaul), so the cap applies. The vendor page carries no publication date; 2026 is an inference from the page's current product banners and is unverified. Fieldguide also says (in a separate article) the 2024 PwC inspection report assessed PwC's use of AI technologies; that PCAOB report was not opened, so it is not used as evidence."

- id: assurance-quality-management-23
  title: "Idea: counter-arguing prompts and structured scepticism steps for reviewers of tool output"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "In an experiment, auditors relying on work done by automated tools were less sceptical than when relying on the same work done by a team member."
  solution: "A counter-arguing mindset intervention alleviated the negative effect on professional scepticism in the same experiment, and no spillover of reduced vigilance to later tasks was found. Regulators ask firms to train reviewers on automation bias, but no firm was found using such a prompt in review workflows."
  outcomes:
    - { lever: quality, description: "Experimental result without published figures in the abstract: auditors were less sceptical relying on automation, and the intervention reduced this effect", figure: "none in abstract", measures: "auditors in a single behavioural experiment; sample not stated in the abstract", provenance: independent, source_ref: PETERS-2022 }
  prerequisites:
    - "Reviewer templates that include a prompt to argue against the tool's output"
  risks_and_guardrails:
    - "Working paper abstract only; it predates GenAI tools and tests general automated tools and techniques"
  human_checkpoints:
    - "Reviewer completes the counter-arguing step before accepting output"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: PETERS-2022, title: "Auditor Automation Usage and Professional Skepticism", publisher: "Tilburg University (working paper, C. Peters)", type: academic, url: "https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/", date: "2022-12-09", access: full, locator: "abstract" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: "Financial Reporting Council", type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03-30", access: full, locator: "pp. 35, 37" }
  last_reviewed: 2026-10-16
  notes: "Idea: researchers discuss it. Evidence is adjacent (pre-GenAI automation), so no grade above D; the abstract page was read, not the full paper."
```

---

## 3. Module notes

### Processes and key steps (with work types)

Firm level (ISQM 1 / QC 1000 resources and monitoring components):

1. **Identify the need and approve the build or buy.** Ideas come from the global firm, innovation teams, audit teams and staff portals. A business case and approvals are required (FRC-ATT-2025). Work type: coordination-scheduling.
2. **Design or select.** Most firms prefer global-network or in-house tools; third-party tools go through procurement, vendor-control and confidentiality review (FRC-ATT-2025). Work type: software-systems.
3. **Certify.** Testing of function and outputs, methodology sign-off, limitations, training and the supporting IT controls. Work type: review-assurance. For GenAI, the unit is a tool in a use case (FRC-GENAI-2026, p. 30).
4. **Deploy.** Pilots, limited release, central inventory, training or guidance (FRC-ATT-2025).
5. **Monitor, recertify, retire.** Usage counts, change triggers, owner confirmations, retirement policies (FRC-ATT-2025). Work type: data-reporting.
6. **Resource and train.** Competence, staffing, mandatory training (IRBA-SPA11-2025; PREPRINT-AIJGDI-2026). Work types: coordination-scheduling, people development.
7. **Remediate and report to inspectors.** Root cause analysis, targeted remediation, measuring impact (IFIAR-SURVEY-2026, p. 2).

Engagement level (ISA 220 (Revised)):

1. **Plan AI use and confirm tools are approved** (AICPA-PA-2026; IFIAR-TTF-2026).
2. **Prompt or configure, within library or policy limits** (FRC-GENAI-2026, p. 36).
3. **Review final outputs and oversee agent steps at control points** (FRC-GENAI-2026, pp. 37-38). Work type: review-assurance.
4. **Document AI use and the team's response** (FRC-GENAI-2026, pp. 43, 50).
5. **Senior stand-back review of overall technology use** (IFIAR-TTF-2026, p. 7).

### Common pain points

- Certification processes were designed for deterministic tools. IAASB stakeholders named opacity, non-determinism and adaptivity as the characteristics that make ISQM 1 hard to apply (IAASB-TQMPLAN-2026, para 7).
- Monitoring responsibility between network and member firm is unclear (IFIAR-TTF-2025; IFIAR-TTF-2026).
- Firms cannot show how tools change quality (FRC-ATT-2025).
- Reviewers may accept fluent output, and the FRC warns that tools sound confident even when wrong (FRC-GENAI-2026, p. 46).
- Larger firms are better placed than small practices to govern AI tools, per IAASB stakeholders (IAASB-TQMPLAN-2026, para 11).
- Firm-level inspection effort already finds weak monitoring: IFIAR counted 21 findings for failing to identify audit performance issues during internal inspections in 2025 (6 in 2024) (IFIAR-SURVEY-2026, Table A.3).

### Metrics and benchmarks (with sources)

| Metric | Value | What it measures | Source |
|---|---|---|---|
| Members reporting tool-not-used-as-intended findings | 31% (2024), 29% (2023) | Share of IFIAR Members reporting findings that an ATT was not used as intended (survey of members) | IFIAR-TTF-2025, p. 5 |
| Growth in AI-enabled tools at the six GPPC networks | about 30% year over year in 2025 | Collective report from the networks to IFIAR's technology task force; differing reporting practices | IFIAR-TTF-2026, p. 5 |
| Firms with at least one finding, monitoring and remediation | 32% (42 firms) in 2025; 25% in 2024 | Member firms inspected with at least one finding in the theme, per Table A.2 | IFIAR-SURVEY-2026, Table A.2 |
| Firms with an EQR finding | 20% (26 firms) in 2025 | New category in 2025 | IFIAR-SURVEY-2026, Table A.2 |
| Firms with a technological-resources finding | 9% (11 firms) in 2025 | New category in 2025; no AI-specific category | IFIAR-SURVEY-2026, Table A.2 |
| Audits with findings | 35% in 2025 (26% in 2022) | "Percentage of audits with findings" in IFIAR's survey of the six GPPC networks | IFIAR-SURVEY-2026, printed p. 2 |
| Deloitte UK PairD use | 4,649 active users; over 75% of Audit & Assurance professionals; about two million prompts in the year | Firm-reported for the year ended 31 May 2025 | DELUK-TR-2025, pp. 15, 94 |
| IRBA survey, firms with an AI governance framework or building one | at least 56% | Firms that participated in IRBA's survey of auditors of publicly traded entities (sample size not stated in the text read) | IRBA-SPA11-2025, p. 8 (after para 17) |
| Time savings PwC US sees from AI in audit | "not that drastic yet" (qualitative) | PwC US assurance transformation leader, one year after launch | CFODIVE-PWC-2026 |
| Sanville realization | $150-200 to $250+ per hour | Vendor customer story; one firm | FIELDGUIDE-SANVILLE-2026 |

No published override rates, review-comment accuracy, or parallel-run error rates were found.

### Guardrails and regulatory points

- No regulator bans AI. The human auditor stays accountable (FRC-NEWS-2026; NFRA-CAALLEY-2026; AFM-2025).
- ISQM 1 requires firms to assess risks of technological resources, certify tools, apply IT general controls and train users. IFIAR says the same (IFIAR-TTF-2026, p. 6). The IAASB states that the firm remains responsible for tool approval and monitoring even when the network does the work (IAASB-TQMPLAN-2026, para 29).
- FRC (Mar 2026): guidance is aimed at central technical teams and does not alter accountability (FRC-GENAI-2026, p. 4; FRC-NEWS-2026).
- NFRA (staff series, Jul 2026): technology as a distinct risk area in the quality system, proportionate validation, revalidation on model or vendor change, documentation of tool and human review, root cause analysis of technology findings in the annual SoQM evaluation, vendor audit rights (NFRA-CAALLEY-2026).
- AFM (Dec 2025): traceability and data security; humans responsible (AFM-2025).
- PCAOB: staff say AI adoption by firms is an inspection focus (DART-SECPCAOB-2025). The Board has not issued an AI standard (FIELDGUIDE-PCAOB-2026, vendor commentary). QC 1000 text and inspection reports could not be opened (pcaobus.org blocked). PCAOB can make unaddressed QC criticisms public after 12 months (PCAOB-PRIORITIES-2024).
- SEC OCA: asks auditors how they use AI to monitor their system of quality control (KPMG-HOHL-2026).
- Confidentiality: some firms restrict uploads to GenAI tools (PCAOB-GENAI-2024).

### Frontier signals (dated, sourced)

- **2025-06-26:** FRC first AI-in-audit guidance and ATT thematic review (FRC-NEWS-2025).
- **2025-12:** AFM 12 building blocks (AFM-2025); CPAB notes auditors relying on tools as the primary source of evidence in some 2025 inspections (CPAB-TECH-2025, p. 1).
- **2026-03:** FRC GenAI and agentic guidance; IAASB approves action plan for ISQM 1 and ISA 220 guides (FRC-NEWS-2026; IAASB-TQMPLAN-2026).
- **2026-04:** Deloitte UK sets up the Technology Controls Board (DELUK-TR-2026, p. 48). IFIAR reports about 30% yearly growth in AI-enabled tools and emphasises oversight of agentic AI (IFIAR-TTF-2026, p. 5).
- **2026-06:** FRC Audit Tech & AI Sandbox; Deloitte unifies agents in Omnia, including tutor mode (FRC-SANDBOX-2026; DELOITTE-OMNIA-2026).
- **2026-07:** NFRA technology principles (NFRA-CAALLEY-2026).
- **2026-10-13:** AICPA practice aid, with more Q&A planned on the firm's AI use (AICPA-PA-2026).
- **To June 2027:** IAASB guide series on technology quality management drafted and approved in stages (IAASB-TQMPLAN-2026, Table 2).
- PwC expects tools for each audit step and a single global agentic platform about 18 months later (PWC-AT-2025; CFODIVE-PWC-2026). EY and Deloitte describe multi-agent platforms; these raise the stakes for network-level monitoring.

### Workforce and role effects

- Review becomes the main human task. Deloitte says professionals supervise, validate and work alongside AI (DELOITTE-OMNIA-2026). Holmstrom and Peters propose, without results, that moving from preparing to reviewing could lower motivation and judgement quality (HOLMSTROM-2024).
- Reviewer competence is a named control. FRC says reviewers need the competence to find deficiencies, and sometimes specialist expertise (FRC-GENAI-2026, p. 37). CPAB asks about the training needed to review output and to build junior auditors' critical thinking (CPAB-TECH-2025, p. 3).
- New roles: central AI-tool owners, technology controls boards, Chief AI Officers (DELUK-TR-2026). PwC says it now hires engineers it would not have hired into assurance before (PWC-AT-2025).
- Sanville's partner says reviewers now have bandwidth to guide first-year staff on complex revenue testing (FIELDGUIDE-SANVILLE-2026; vendor story).
- The IAASB's Technology QM Expert Group includes practitioners from KPMG, PwC, Deloitte, EY, BDO, Grant Thornton and Forvis Mazars, and regulators from the FRC, CPAB and PCAOB, so firm quality leaders are shaping the guides (IAASB-TQMWS-2026).
- Staff integrity: Deloitte UK told staff that using GenAI to cheat in assessments is gross misconduct (DELUK-TR-2025, p. 30).

### Objections and concerns practitioners raise

- Standards written for deterministic tools do not fit opaque, adaptive tools (IAASB-TQMPLAN-2026, para 6).
- Compliance burden falls unevenly on small firms (IAASB-TQMPLAN-2026, para 11).
- Public disclosure does not let outsiders judge validation or traceability: the preprint found these the least consistently disclosed safeguards in the 2024 UK Big Four reports (PREPRINT-AIJGDI-2026, section 4.2).
- Over-reliance: CPAB notes the risk rises when outputs look authoritative and cannot be challenged (CPAB-TECH-2025, p. 2).
- Real failure of review outside audit: Deloitte Australia partially refunded a government report with apparent AI-generated errors, including a fabricated court quote and non-existent references; Deloitte did not say whether AI caused the errors, and the revised report disclosed use of Azure OpenAI (BNN-AP-DELOITTE-2025). This is a consultancy engagement, not an audit; it is the clearest public failure of review of AI output at a Big Four firm.
- Gains are modest so far: PwC US reports time savings "not that drastic yet" (CFODIVE-PWC-2026).

### Interview probes for an advisor

1. "Which AI tools have been certified for which use cases, and what happens when the vendor updates the underlying model?" Probe recertification triggers and who owns them.
2. "What do you measure about a tool's effect on quality, beyond how many teams use it?" Probe override rates, false positives against a manual sample, rework, and who reads the results.
3. "When a reviewer signs off on AI output, what must they have looked at, and how is that visible on the file?" Probe reading the source, citations, and the documentation field.
4. "How do you keep partners and managers honest about automation bias when review time is short?" Probe training, reviewer competence, and counter-argument steps.
5. "What would you tell an inspector today about your AI tools, and what could you not show?" Probe inspection questions received, the evidence trail, and network versus member-firm responsibilities.

---

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| PwC Evidence Match (extracts and matches evidence for cash, receivables, payables) and KPMG agents for expense vouching and unrecorded liabilities | substantive-testing | PWC-AT-2025; ATKPMG-CLARA-2025 |
| CPAB 2025 inspection example: a tool tested only flagged or outlier items, with none on items rated low risk, and limited validation of data inputs | substantive-testing (also planning-risk-assessment) | CPAB-TECH-2025, p. 1 |
| PwC advanced walkthrough assistant and Simplified Audit - Execute (reads supporting documents, flags gaps) | controls-testing | CFODIVE-PWC-2026 |
| FRC illustrative example 1 (summarising board minutes for risk assessment) | planning-risk-assessment | FRC-GENAI-2026, pp. 43-48 |
| FRC illustrative example 2 (contract review to select revenue-recognition samples) | substantive-testing | FRC-GENAI-2026, pp. 49-54 |
| Deloitte UK plans for GenAI in disclosure assessment, tie-through, and forward-looking judgements such as going concern | completion-reporting | DELUK-TR-2025, p. 94 |
| KPMG Financial Report Analyzer feeding disclosure checklists; PwC audit-committee communications tool | completion-reporting | ATKPMG-CLARA-2025; CFODIVE-PWC-2026 |
| IFIAR 2025 findings on acceptance and continuance (18% of firms) and relevant ethical requirements (30% of firms); PCAOB focus on private equity and independence | acceptance-independence | IFIAR-SURVEY-2026, Table A.2; DART-SECPCAOB-2025 |
| IRBA example of AI analysing non-traditional sources for client acceptance | acceptance-independence | IRBA-SPA11-2025, section B table |
| IFIAR's repeated finding on insufficient testing of IT general controls | specialists (IT audit) / controls-testing | IFIAR-TTF-2025, p. 5 |
| Deloitte AI Assurance services and KPMG's ISO 42001 certification as a precursor to AI assurance services | other-assurance (assurance over AI) | DELOITTE-OMNIA-2026; AT-KPMGISO-2025 |
| PwC Australia pilot of an AI-native audit platform across five audit clients, rollout to all audit clients by 2028, 1,600 auditors | cross-cutting (business model and workforce) | ACCTIMES-PWCAU-2025 |
| PwC hiring engineers and dual-track CPA and data-science staff | cross-cutting (workforce) | PWC-AT-2025 |

---

## 5. Sources

All sources were opened unless marked otherwise. Dates are publication dates, or the best available (noted).

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| FRC-GENAI-2026 | Generative and Agentic AI Guidance | FRC | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 |
| FRC-ATT-2025 | Thematic Review: Certification of Automated Tools and Techniques (HTML version, AI-converted) | FRC | regulator | https://www.frc.org.uk/docs/8383/html/ | 2025-06-26 |
| FRC-NEWS-2025 | FRC publishes landmark guidance providing clarity to audit profession on the uses of AI | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/ | 2025-06-26 |
| FRC-NEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 |
| FRC-SANDBOX-2026 | Audit Tech and AI Sandbox | FRC | regulator | https://www.frc.org.uk/library/innovation-and-improvement-hub/sandbox-audit-tech-and-ai/ | 2026-06 |
| IFIAR-TTF-2025 | Use of technology in audits - observations, risks and further evolution | IFIAR | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 |
| IFIAR-TTF-2026 | Use of technology in audits - Innovation and audit quality | IFIAR | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf | 2026-04-20 |
| IFIAR-SURVEY-2026 | Survey of Inspection Findings 2025 | IFIAR | regulator | https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf | 2026-04-01 |
| CPAB-TECH-2025 | The evolving use of technology in the audit | CPAB (Canada) | regulator | https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2025-evolving-use-of-technology-in-the-audit-en.pdf | 2025-12 |
| AFM-2025 | 12 building blocks for controlled use of advanced (Gen)AI auditing tools (press release) | AFM (Netherlands) | regulator | https://www.afm.nl/en/sector/actueel/2025/dec/pb-12-bouwstenen-beheerst-gebruik-audit-tooling | 2025-12-11 |
| IRBA-SPA11-2025 | Staff Audit Practice Alert 11 | IRBA (South Africa) | regulator | https://www.irba.co.za/upload/Staff%20Practice%20Alert%2011%20Sep%202025.pdf | 2025-09 |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI | PCAOB | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 |
| PCAOB-PRIORITIES-2024 | Spotlight: Staff Priorities for 2025 Inspections | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf | 2024-12 |
| IAASB-TQMPLAN-2026 | Technology Quality Management Workstream: Action Plan (approved) | IAASB | standard-setter | https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf | 2026-03 |
| IAASB-TQMWS-2026 | Technology Quality Management Workstream (web page; roundtables, expert group) | IAASB | standard-setter | https://www.iaasb.org/consultations-projects/technology-quality-management-workstream | 2026-09 (page undated; latest linked item is Sept 2026) |
| AICPA-PA-2026 | AICPA releases guidance to help auditors address the use of AI | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 |
| DELUK-TR-2025 | 2025 Transparency Report | Deloitte UK | firm | https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report.pdf | 2025-09 (PDF metadata) |
| DELUK-TR-2026 | 2026 Transparency Report | Deloitte UK | firm | https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2026/deloitte-uk-annual-review-2026-audit-transparency-report.pdf | 2026-09 (PDF metadata) |
| KPMG-TR-2025 | Transparency Report 2025 | KPMG International | firm | https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/12/transparency-report-fy25.pdf | 2025-12 |
| DELOITTE-OMNIA-2026 | Deloitte unveils connected agentic intelligence in Deloitte Omnia | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 |
| KPMG-HOHL-2026 | Q&A with SEC Chief Accountant Kurt Hohl | KPMG Board Leadership Center | firm | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | 2026-05-27 |
| DART-SECPCAOB-2025 | Highlights of the 2025 AICPA & CIMA Conference on Current SEC and PCAOB Developments | Deloitte DART | conference | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways | 2025-12-12 |
| RSM-SECPCAOB-2025 | Insights from the 2025 AICPA Conference on Current SEC and PCAOB Developments | RSM US | conference | https://rsmus.com/content/dam/rsm/insights/financial-reporting/1pdf/insights-from-the-2025-aicpa-conference-on-current-sec-and-pcaob-developments-12-25.pdf | 2025-12 |
| NFRA-CAALLEY-2026 | NFRA sets 10 principles for technology use in audits (report of NFRA Staff Series; primary not reached) | CAalley.com | press | https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement | 2026-07-24 |
| ATKPMG-CLARA-2025 | KPMG builds AI agents into audit platform | Accounting Today | press | https://www.accountingtoday.com/news/kpmg-builds-ai-agents-into-audit-platform | 2025-04-24 |
| AT-KPMGISO-2025 | Tech News: KPMG hails ISO 42001 certification | Accounting Today | press | https://www.accountingtoday.com/list/tech-news-kpmg-hails-iso-42001-certification | 2025-11-21 |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 |
| CFOBREW-PWC-2025 | A look at PwC's 'next generation' audit | CFO Brew | press | https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit | 2025-11-05 |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 |
| ACCTIMES-PWCAU-2025 | PwC Australia rolls out pilot program for AI-assisted full audits | Accounting Times | press | https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits | 2025-10-27 |
| BNN-AP-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | Associated Press via BNN Bloomberg | press | https://www.bnnbloomberg.ca/business/artificial-intelligence/2025/10/07/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 |
| FIELDGUIDE-SANVILLE-2026 | How Sanville & Co passed a PCAOB inspection with zero comment forms | Fieldguide | vendor | https://www.fieldguide.io/case-studies/how-sanville-co-passed-a-pcaob-inspection-with-zero-comment-forms-in-under-a-year-with-fieldguide | 2026 (page undated; inferred) |
| FIELDGUIDE-PCAOB-2026 | PCAOB AI oversight: where the Board stands on AI in audit | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/pcaob-ai-audit-standards | 2026-08-06 |
| PREPRINT-AIJGDI-2026 | Professional Judgment and AI Governance in Audit and Sustainability Assurance: Public Evidence from the UK Big Four (published later as J. Risk Financial Management 2026, 19(9), 675) | Preprints.org | academic | https://www.preprints.org/manuscript/202607.1693/v1 | 2026-07 |
| PETERS-2022 | Auditor Automation Usage and Professional Skepticism | Tilburg University (C. Peters) | academic | https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/ | 2022-12-09 |
| HOLMSTROM-2024 | How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal) | PCAOB conference materials (Holmstrom and Peters) | academic | https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf | 2024-06 (PDF metadata; pilot dated it 2025) |
| ICAS-FRC-2026 | FRC issues new guidance to support audit firms using emerging AI technologies | ICAS | professional-body | https://icas.com/news-insights-events/news/audit-assurance/frc-issues-new-guidance-to-support-audit-firms-using-emerging-ai-technologies/ | 2026-03-30 |
| ICAS-SANDBOX-2026 | Driving audit innovation with FRC sandboxes and forums | ICAS | professional-body | https://icas.com/news-insights-events/news/audit-assurance/driving-audit-innovation-with-frc-sandboxes-and-forums/ | 2026-07-07 |
| CPAPRACTICE-RSMANDERA-2026 | Andera and RSM US Partner to Create AI-Enabled Control Testing Platform for Internal Audit | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/ | 2026-08-26 |
| CAQ-RSM-2026 | CAQ Audit in Action blog on RSM's AI tools (carried from the landscape; **search-only**, not opened) | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-in-action (listing page; the post was not located) | 2026-08-25 |

**Count by type (opened):** regulator 13, standard-setter 3, firm 5, conference 2, press 9, vendor 2, academic 3, professional-body 2 = 39 opened. One further source (CAQ-RSM-2026) is search-only. Of the opened sources, 26 are primary documents (regulator, standard-setter, firm, vendor, academic) and 13 are press, professional-body or conference recaps.

---

## 6. Gaps

**Not found or not reachable**
- **Independent measurement of AI tool quality in practice.** No error rate, review override rate, false-positive rate or parallel-run result for any firm's AI tools. The only independent figures are IFIAR's share of members with findings (31% in 2024) and CPAB's single inspection example. IFIAR's 2025 inspection survey has no AI-specific category.
- **Inspection findings on AI-specific quality management.** None found for 2025-2026. Fieldguide says the PCAOB's 2024 PwC inspection report assessed PwC's AI use; the report was not reached (pcaobus.org returned 403), so that claim stays unverified.
- **EY and PwC UK/US firm documents.** PwC UK 2025 transparency report returned access denied; EY UK and KPMG UK reports not located; EY and PwC AI governance is known only from the preprint's reading of 2024 reports. BDO, Grant Thornton, Forvis Mazars and other mid-tier firms: nothing on AI quality-management practice found. Smaller practices: only the landscape's CPA.com benchmark (not re-opened) and Sanville's vendor story.
- **Resourcing tools.** RSM's Luca Resourcing could not be verified (the CAQ post was not located and the search quota ran out). No other firm resourcing case found.
- **AI in engagement quality review, consultation, going concern review.** Nothing public. IFIAR counted 26 firms with an EQR finding in 2025, and 20 findings of insufficient depth or extent of EQCR, but without reference to AI.
- **Job postings, podcasts, community discussion.** None opened for this angle. The AI-team structure at firms was not evidenced beyond Deloitte UK's Chief AI Officer and Technology Controls Board and the IAASB expert-group membership.
- **Primary documents.** NFRA's Staff Series (only a press report read). AICPA practice aid full text (behind login). IAASB December 2025 feedback paper and the February 2026 roundtable summary. PCAOB QC 1000 text and the Inspections Modernization Council materials (pcaobus.org blocked). FRC "AI in Audit" documentation guidance PDF (only the news release read). The AFM 12 building blocks PDF. EY's UK transparency report. CPAB 2024 paper (only the introduction read).
- **IFIAR frequency chart.** The 2025 percentages by audit area appear in a chart that did not extract; none are used. The 2024 table figures are in the landscape (IFIAR-TTF-2025).
- **Web search.** The quota ran out after about five searches, so leads that required discovery (firm transparency reports, job postings, academic follow-ups) were not pursued.

**Dating caveats**
- Fieldguide's Sanville page has no date; 2026 is an inference.
- Deloitte UK reports are dated from PDF metadata (2025-09-30 and 2026-09-29).
- HOLMSTROM-2024 is dated from PDF metadata (2024-06); the pilot dated it 2025.
- IAASB-TQMWS-2026 is undated; the date given is the latest linked item.
- FRC-SANDBOX-2026 is dated by launch month, not by a date on the page.
- KPMG-HOHL-2026 is dated by the page (2026-05-27); the interview date is not stated.

**Conflicts to resolve in synthesis**
- KPMG says it is the first Big Four firm with ISO 42001 certification (AT-KPMGISO-2025), but does not name the entity; Fieldguide says it holds it too (a vendor).
- The landscape reported IFIAR 2025 survey figures as "35% of engagements with a finding". The report words it "percentage of audits with findings"; the unit of measure is the inspected audit.
- The landscape grouped PCAOB QC 1000 amendments as approved 9 Sep 2026 (secondary); the primary was not reached here.
- FRC thematic HTML warns of AI conversion; check figures against the PDF before final use.
