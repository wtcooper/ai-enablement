# Module deep dive: assurance / quality-management / discourse

- **Archetype:** assurance
- **Module:** quality-management. Firm-level quality management of AI (ISQM 1 / PCAOB QC 1000: tool certification and approval, governance, methodology, monitoring and remediation, resourcing) and engagement-level supervision and review of AI output (review control points, automation bias, documentation of AI use), plus interaction with inspectors.
- **Angle:** discourse. What practitioners, quality leaders and regulators have been saying in the last 12–18 months (about April 2025 to October 2026) at conferences, roundtables and webinars and in speeches, commentary, podcasts and press.
- **Prepared:** 2026-10-16
- **Method note.**
  - About 57 pages and PDFs were opened and read with `curl` or, where a site refused `curl`, through the text mirror (`r.jina.ai`). This covers the pcaobus.org speeches, the IFIAR report and the Foley article. Those are marked "via text mirror" in the source list.
  - Primary documents read include the IFIAR April 2026 technology report (12 pages, read in full; new since the landscape scan), the IAASB roundtable outcome paper and its March 2026 action plan, and the FRC thematic review on certification. The FRC generative and agentic AI guidance (61 pages) was read for its quality management sections (risk mitigation, certification, review and oversight, pages 23–39) and searched for the rest.
  - Seven PCAOB Board and Chair speeches and statements were read for their sections on AI, quality control and inspections. They are the richest first-hand discourse on inspections and quality control.
  - The web-search quota ran out partway through. A few leads (Big Four transparency reports, the Swedish junior-auditor study, MindBridge's PCAOB letter) could not be opened and are listed in section 6.
  - Quotations are under 25 words. Figures from vendors are labelled as such. One item seen only in a search snippet is mentioned in a `notes` field and is not used as a source.

---

## 1. Summary

1. **The conversation moved from "may we use AI?" to "how do we run it inside the system of quality management?"**
   - The FRC's 30 March 2026 guidance tells firms to consider AI under ISQM (UK) 1 and says accountability for audit quality is unchanged (FRC-GENAINEWS-2026).
   - The IAASB's eight roundtables (243 participants, 93 of them from accounting firms) found ISQM 1 and ISA 220 (Revised) a strong base but asked for practical guidance on tool certification, monitoring and review of outputs (IAASB-TQM-2026, pp. 2–5). The IAASB approved an action plan in March 2026 under which remaining completed guides are planned to go to the Board by June 2027 (IAASB-TQMPLAN-2026, p. 9).
   - IFIAR (20 April 2026) lists practices networks should consider, from validation and re-approval to escalation pathways and AI oversight committees (IFIAR-TTF-2026, pp. 6–7). PCAOB board member Botic set out a lifecycle expectation in September 2026: approval, validation, monitoring, training, periodic reassessment and retirement, plus an inventory of tools (PCAOB-BOTICSF-2026).
2. **Supervisors are moving to inspect the firm's system, and AI governance sits inside that system.**
   - The FRC put firms' systems of quality management "at the heart" of supervision, starting April 2026 for the largest firms (FRC-SUPERVISION-2026), with fewer formal inspections where it has confidence in firms' self-review (BOARDAGENDA-SUP-2026).
   - The PCAOB adopted QC 1000 amendments on 9 September 2026. Its Chairman calls QC 1000 the foundation for a QC-centred inspection model (PCAOB-LOGOQC-2026). Staff discussion materials for the Inspections Modernization Council (IMC) propose that firm-level risk assessment sets the scope of QC testing and engagement reviews (STARLING-IMC-2026).
   - Not everyone agrees. In October 2026 Botic said he is wary of a staff idea that would cut file reviews at the largest "lower-risk" firms to well below 50% of 2025 levels (PCAOB-BOTICIOWA-2026). The SEC's chief accountant has said a QC-focused model may be tougher on firms (CAQ-HOHLWEBINAR-2026).
3. **Quality evidence is missing, and everyone says so.**
   - The FRC found no formal monitoring at the six largest UK firms that quantified how automated tools affect audit quality (FRC-ATT-2025, p. 20). IFIAR in April 2026 still only suggests metrics (false-positive and false-negative rates against a manual sample, rework rates, escalation incidence) and publishes no values (IFIAR-TTF-2026, pp. 8–9).
   - No override rates, reviewer error rates or parallel-run results were found. PwC's US assurance leader said after a year that time savings are "not that drastic yet" (CFODIVE-PWC-2026).
   - The six US networks' average Part I.A deficiency rate fell from 26% to 13% (312 audits), but no source attributes that to AI (CAQ-INSIDER-2026).
4. **The main worry is rubber-stamping, and practitioners think the guidance treats it too lightly.**
   - Regulators name automation bias: the FRC (p. 35), India's NFRA, and IFIAR, whose April 2026 report says over-reliance on outputs without sufficient challenge is a risk (IFIAR-TTF-2026, p. 3). KPMG says an approval step that rubber-stamps every AI recommendation has no real control value (KPMG-SOX-2026, p. 14).
   - ICAEW's technology faculty chair was disappointed that the FRC covers automation bias in a single paragraph (ICAEW-FRCVIEW-2026).
   - The remedies on offer (independent view first, control points, a named reviewer who records why they agreed, targeted training) have no published effectiveness data.
5. **Deskilling and the junior pipeline are the second worry.**
   - PCAOB acting chair Botic warned in December 2025 that over-reliance on AI may undermine skepticism, and that new paths for juniors to build skills will be needed (NYSSCPA-BOTIC-2025, CAALLEY-PCAOBPE-2025).
   - PwC's AI assurance leader said in August 2025 that new hires would act like managers within three years, and that skepticism and critical thinking were being taught earlier (BI-PWC-2025).
   - ICAEW reports the Big Four cut graduate intake by 6–29% in 2025, and a mid-tier partner says a prospective client asked for fewer junior hours and lower fees (ICAEW-EXPECT-2026).
   - The deskilling research regulators cite is an EEG study of essay writing, not audit work (KOSMYNA-2025).
6. **Smaller firms and third-party tools are a recurring gap.**
   - ICAEW notes the FRC guidance assumes technology and methodology teams that smaller firms lack, and says it says too little about vendors (ICAEW-FRCVIEW-2026).
   - The IAASB's plan names an "uneven playing field" between large firms and small and medium-sized practices (IAASB-TQMPLAN-2026, p. 3).
   - The FRC's head of assurance technology calls the market for assurance over AI tools fragmented and unregulated (ICAEW-POD-2025).
7. **Where the field says it is heading.**
   - Agentic orchestration with human checkpoints (IAASB-TQM-2026, p. 4; DELOITTE-OMNIA-2026).
   - AI reviewing AI, which a Grant Thornton UK director put "a few years down the line" (ICAEW-POD-2025).
   - Regulators using AI in inspections (PCAOB-BOTICIOWA-2026).
   - QC 1000 taking effect in December 2026 (FOLEY-PCAOB-2026).
8. **Yield.** 19 candidate use cases: none graded A, 5 graded B, 5 graded C, 9 graded D (ideas). 57 sources are listed in section 5.

---

## 2. Use cases

Notes on fields for this module:
- `ladder` describes the AI work being governed or reviewed. For example, "augment" means the governed tool gives a first pass that a person reviews. The governance process itself is run by people.
- `pattern: other` is used where the pattern is governance or evaluation of AI tools. Nothing in the vocabulary fits.
- Grade C is used where regulators or a firm announce a practice but no firm is named or no use is shown. Each such entry says so in `notes`.

```yaml
- id: assurance-quality-management-01
  title: Use-case-level certification, approval and recertification of AI tools within the firm's quality management system
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    Firm quality-management processes were built mainly for transparent, deterministic tools. IAASB staff describe
    AI tools as opaque (limited explainability), non-deterministic (outputs vary) and adaptive (behaviour changes over
    time), which makes it hard to decide how much testing is enough before deployment and how to monitor afterwards
    (IAASB-TQMPLAN-2026, paras 5-7).
  solution: >
    The firm treats the unit of certification as an AI tool in the context of a use case. Certification evaluates the
    tool's inputs and architecture and tests its outputs. The firm may recertify when components or inputs change, when
    the use case changes, when performance issues appear, when standards or policies change, or after a set time. A
    firm may release a tool to a few teams first, with alternative procedures performed in full in parallel
    (FRC-GENAI-2026, pp. 30, 33). IAASB roundtable participants described tiered certification, iterative testing,
    dynamic monitoring and escalation procedures, and said adoption varies significantly across firms (IAASB-TQM-2026, p. 4).
  outcomes:
    - {lever: risk, description: "The FRC found most of the six largest UK firms had well-established processes to certify automated tools before deployment, and that firms were still updating them for AI-specific risks", figure: "none (qualitative regulator finding)", measures: "FRC thematic review of certification processes at BDO, Deloitte, EY, Forvis Mazars, KPMG and PwC (UK)", provenance: independent, source_ref: FRC-ATT-2025}
  prerequisites:
    - "An inventory of tools and use cases, and a decision on what the unit of certification is (tool alone, or tool in a use case) (FRC-GENAI-2026, p. 30)"
    - "Information from vendors. LLM training data usually cannot be obtained from third-party providers, which may change the nature and extent of testing (FRC-GENAI-2026, p. 30)"
    - "Defined recertification triggers built into change management (FRC-ATT-2025, p. 21)"
  risks_and_guardrails:
    - "Recertification triggers appeared informal at most firms; the FRC encourages a recertification check inside change management (FRC-ATT-2025, p. 21)"
    - "The FRC says LLMs' inherent limitations mean some risk of deficient output always remains, so certification is paired with review or oversight by humans (FRC-GENAI-2026, p. 26)"
    - "Regulators expect the firm, not the network or vendor, to keep responsibility for approving tools and monitoring them (IAASB-TQMPLAN-2026, para 29)"
  human_checkpoints:
    - Firm-level decision to approve, restrict or retire a tool for a defined use case
    - Decision to recertify after a trigger event
  role_evolution: >
    Technology and methodology specialists run certification. The FRC guidance is aimed mainly at system managers at
    audit firms (ICAEW-FRCVIEW-2026).
  evidence_grade: B
  sources:
    - {ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/8383/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf", date: 2025-06, access: full, locator: "p. 4 (executive summary); p. 21 (recertification triggers)"}
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 26, 30, 33"}
    - {ref: IAASB-TQM-2026, title: "Technology Quality Management Roundtables: Outcomes and Next Steps", publisher: IAASB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-02/IAASB-Technology-Quality-Management-Roundtables-Feedback.pdf", date: 2026-02, access: full, locator: "p. 4 (emerging practices)"}
    - {ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F)", publisher: IAASB, type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "paras 5-7, 20, 29"}
    - {ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05-06, access: full, locator: "intro and 'Smaller firms' sections"}
  last_reviewed: 2026-10-16
  notes: >
    Grade B: the FRC thematic review names the six firms it reviewed but reports practice collectively, with no
    per-firm results and no measure of effect. The review covers automated tools in general; AI-specific certification
    was still being developed (FRC-ATT-2025, p. 4). Guidance (FRC, IAASB) is also cited for the design; it is not
    evidence of use.

- id: assurance-quality-management-02
  title: Authorised-tool inventory, access control and usage monitoring for audit tools
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [software-systems, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    A firm cannot show that only certified, current tools are used on engagements unless it knows which tools exist,
    who uses them and which version they run. The FRC found firms generally did not monitor that teams used only
    authorised and current tools (FRC-ATT-2025, p. 22).
  solution: >
    Firms keep directories or inventories of current certified tools and use preventive controls: authorised software
    repositories, removal of outdated versions, and online delivery that makes it easier to offer only the current
    certified version (FRC-ATT-2025, p. 22). IFIAR asks networks to ensure tools are deployed only on approved
    engagements and to have oversight programmes that catch non-approved or decommissioned tools in use (IFIAR-TTF-2026, p. 6).
    Botic lists maintaining an inventory of AI tools as part of governance (PCAOB-BOTICSF-2026).
  outcomes:
    - {lever: risk, description: "Most of the six firms had directories or inventories of current certified tools; usage monitoring covered a subset of widely used tools and mainly counted teams using them, typically for licensing", figure: "none (qualitative)", measures: "FRC observations at the six largest UK firms", provenance: independent, source_ref: FRC-ATT-2025}
  prerequisites:
    - "A central register of tools, versions and approved use cases (FRC-ATT-2025, p. 22)"
    - "Controls over software installation and access (FRC-ATT-2025, p. 22)"
  risks_and_guardrails:
    - "Monitoring was mostly for licensing, not quality, and most firms had no KPIs on tool usage (FRC-ATT-2025, p. 20)"
    - "IFIAR saw networks split on who monitors: global level in some, member firms in others. It warns this can fragment monitoring and leave incomplete coverage across tools and jurisdictions (IFIAR-TTF-2026, p. 8)"
  human_checkpoints:
    - Periodic review of the inventory by the firm's tool owner
    - Escalation when an unapproved or outdated tool is found in use
  role_evolution: >
    Roles for tool owners and system managers grow. The FRC asks firms to define where monitoring responsibility sits
    for globally deployed tools (FRC-ATT-2025, p. 20).
  evidence_grade: B
  sources:
    - {ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/8383/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf", date: 2025-06, access: full, locator: "pp. 20, 22"}
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "pp. 6, 8"}
    - {ref: PCAOB-BOTICSF-2026, title: "Smaller Audit Engagements, Significant Impact: Audit Quality, Investor Protection, and the Future of the Profession", publisher: PCAOB (G. Botic), type: regulator, url: "https://pcaobus.org/news-events/speeches/speech-detail/smaller-audit-engagements--significant-impact--audit-quality--investor-protection--and-the-future-of-the-profession", date: 2026-09-22, access: full, locator: "section 'Expanding Use of Technology in Audits'"}
  last_reviewed: 2026-10-16
  notes: >
    Grade capped at B: the evidence is from the FRC's review of automated tools generally, which predates most generative AI use
    (June 2025), so it is an adjacent process for AI. The speech is one board member's view, not Board policy.

- id: assurance-quality-management-03
  title: Monitoring the quality impact of AI tools with defined metrics and benchmarks (idea)
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    The FRC found no formal monitoring at the six largest UK firms that quantified how automated tools affect audit
    quality, though firms said they wanted to develop it (FRC-ATT-2025, p. 20). Without it, firms cannot tell which
    tools improve quality and which do not.
  solution: >
    Idea discussed by regulators. Firms define metrics and review them periodically. IFIAR's examples are engagement
    coverage percentage, false-positive and false-negative rates against a manual sample, rework rates and escalation
    incidence, plus dashboards of usage trends and internal benchmarking of tool results against traditional methods
    (IFIAR-TTF-2026, pp. 8-9). The FRC guidance says monitoring should cover output quality and consistency, patterns of failure and
    unexpected behaviour, and how this affects audit quality (FRC-GENAI-2026, p. 33).
  outcomes:
    - {lever: quality, description: "none published", figure: "none", measures: "n/a. IFIAR names metric types but no values; the FRC found no firm quantifying quality impact", provenance: independent, source_ref: IFIAR-TTF-2026}
  prerequisites:
    - "Logging of tool use and outputs by engagement (IFIAR-TTF-2026, pp. 8-9)"
    - "A manual or independent baseline to compare against (IFIAR-TTF-2026, p. 9)"
    - "Clear allocation of monitoring responsibility between network and member firm (FRC-ATT-2025, p. 20)"
  risks_and_guardrails:
    - "IFIAR says the metrics themselves should be reviewed periodically (IFIAR-TTF-2026, p. 9)"
    - "IFIAR says its observations rest on information shared with it and are not a comprehensive assessment of firms or tools (IFIAR-TTF-2026, p. 3)"
  human_checkpoints:
    - Quality function reviews metrics and decides whether to restrict, retrain or recertify a tool
  role_evolution: >
    Audit quality teams and data specialists take on tool performance reporting, an extension of the FRC's call for
    policies or metrics to evaluate impact (FRC-ATT-2025, p. 20).
  evidence_grade: D
  sources:
    - {ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/8383/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf", date: 2025-06, access: full, locator: "p. 20"}
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "pp. 8-9 ('Examples of emerging practices')"}
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p. 33 (Monitoring)"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. IFIAR calls these "emerging practices" but names no firm and publishes no result. The same report says some firms
    have begun to validate tool effectiveness through oversight committees and internal protocols, with practice varying
    widely (IFIAR-TTF-2026, p. 8).

- id: assurance-quality-management-04
  title: AI oversight committee, escalation pathway and whistleblowing channel for AI tool anomalies
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >
    When a tool behaves unexpectedly, a firm needs a defined path from the engagement team to someone who can
    investigate, restrict the tool and tell other teams. IAASB roundtable participants flagged ongoing monitoring and
    documentation as practical challenges (IAASB-TQM-2026, p. 4).
  solution: >
    IFIAR suggests formal escalation pathways for unexpected outputs or operational failures, ethical governance structures
    such as AI oversight committees, user feedback mechanisms and whistleblowing procedures covering AI use in audits
    (IFIAR-TTF-2026, pp. 6-7). IFIAR notes some firms have started to establish oversight committees (IFIAR-TTF-2026, p. 8).
    Roundtable participants described escalation procedures for anomalous tool behaviour as an emerging practice
    (IAASB-TQM-2026, p. 4).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: IFIAR-TTF-2026}
  prerequisites:
    - "A named owner and a cross-functional group covering methodology, technology, ethics and quality (IFIAR-TTF-2026, p. 7)"
    - "A channel for engagement teams to report issues and whether a tool is fit for purpose (IFIAR-TTF-2026, p. 6)"
  risks_and_guardrails:
    - "IFIAR notes practices vary significantly across jurisdictions and firms (IFIAR-TTF-2026, p. 8)"
  human_checkpoints:
    - Committee decision to pause, restrict or re-approve a tool after an incident
  role_evolution: >
    Audit quality and ethics leaders take on AI governance. IFIAR calls for such structures to monitor responsible use and
    adherence to professional standards (IFIAR-TTF-2026, p. 7).
  evidence_grade: C
  sources:
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "pp. 6-8"}
    - {ref: IAASB-TQM-2026, title: "Technology Quality Management Roundtables: Outcomes and Next Steps", publisher: IAASB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-02/IAASB-Technology-Quality-Management-Roundtables-Feedback.pdf", date: 2026-02, access: full, locator: "p. 4"}
  last_reviewed: 2026-10-16
  notes: >
    Grade C: regulators report that some firms have done this but name none, and give no figure on how many. The
    practices are listed as things firms may consider, not as requirements.

- id: assurance-quality-management-05
  title: Firm-approved, methodology-grounded GenAI copilot for audit guidance and consultation
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Auditors spend time finding and applying the firm's own assurance manuals, practice aids and technical accounting
    guides, and may apply them inconsistently. RSM links its launch to busy season, when speed and accurate guidance both
    matter (RSM-LUCA-2026).
  solution: >
    RSM US launched Ask Luca on 8 January 2026 within its RSM Luca audit ecosystem. It gives real-time guidance drawn
    from RSM's assurance manuals, practice aids and technical accounting guides for the firm's 4,000+ assurance
    professionals, and RSM says it lays a foundation for later assurance-focused agents (RSM-LUCA-2026; CPAPA-LUCA-2026).
    An RSM assurance digital leader writes that Ask Luca helps apply guidance more consistently, and that grounding
    comparable tools in firm-approved guidance and experienced human review is vital (CAQ-RSM-2026).
  outcomes:
    - {lever: speed, description: "RSM says Ask Luca reduces research time and delivers vetted guidance quickly; no measurement published", figure: "none", measures: "n/a (claim only)", provenance: self-reported, source_ref: RSM-LUCA-2026}
  prerequisites:
    - "A curated corpus of the firm's own manuals, practice aids and technical guides (RSM-LUCA-2026)"
    - "Experienced human review of how the tool is used (CAQ-RSM-2026)"
  risks_and_guardrails:
    - "Answers are limited to firm-approved material, which RSM presents as the control on quality (RSM-LUCA-2026; CAQ-RSM-2026)"
    - "No accuracy, usage or consistency results are published for the tool (RSM-LUCA-2026; CAQ-RSM-2026)"
  human_checkpoints:
    - The auditor still applies and documents the guidance and own judgment (CAQ-RSM-2026)
  role_evolution: >
    RSM says auditors can spend more attention on analysis, skepticism and judgment (CAQ-RSM-2026).
  evidence_grade: B
  sources:
    - {ref: RSM-LUCA-2026, title: "RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit", publisher: RSM US, type: firm, url: "https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html", date: 2026-01-08, access: full, locator: "paras 2-3"}
    - {ref: CPAPA-LUCA-2026, title: "RSM US Rolls Out 'Ask Luca' GenAI Tool for Firm's Auditors", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/01/09/rsm-us-rolls-out-ask-luca-genai-tool-for-firms-auditors/176104/", date: 2026-01-09, access: full, locator: "paras 1-4"}
    - {ref: CAQ-RSM-2026, title: "Shaping the future of assurance: Advancing AI in the audit", publisher: CAQ (Troy Merkel, RSM), type: professional-body, url: "https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit", date: 2026-08-25, access: full, locator: "section 'Ask Luca: trusted guidance where auditors work'"}
  last_reviewed: 2026-10-16
  notes: >
    Grade B: a named deployment with scale (4,000+ assurance professionals) but no published measurement. The tool serves
    methodology consistency; the sources do not describe a quality-management monitoring role for it.

- id: assurance-quality-management-06
  title: Engagement staffing and budget planning tool with engagement-leader review (RSM Luca Resourcing)
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Resourcing is a quality-management lever (right people, enough time) that firms typically run through manual
    processes. RSM describes replacing manual processes in staffing and budgeting (CAQ-RSM-2026).
  solution: >
    RSM Luca Resourcing is described as a connected collaboration tool supporting initial staffing requests, budget
    planning and engagement-leader review, giving teams visibility of engagement planning (CAQ-RSM-2026). The source lists it
    among RSM's recent AI-related investments but does not say what AI does inside it.
  outcomes:
    - {lever: capacity, description: "none published", figure: "none", measures: "n/a", provenance: self-reported, source_ref: CAQ-RSM-2026}
  prerequisites:
    - "Engagement planning, staffing and budget data in one place (CAQ-RSM-2026)"
  risks_and_guardrails:
    - "The source describes benefits only; it gives no data on staffing quality or time allowed for audits (CAQ-RSM-2026)"
    - "Botic told auditors in January 2026 to make sure teams have sufficient time, even if sign-off is delayed (JOFA-5IMP-2026)"
  human_checkpoints:
    - Engagement leader reviews staffing requests and budgets (CAQ-RSM-2026)
  role_evolution: >
    Not described in the source beyond workforce planning becoming more connected (CAQ-RSM-2026).
  evidence_grade: B
  sources:
    - {ref: CAQ-RSM-2026, title: "Shaping the future of assurance: Advancing AI in the audit", publisher: CAQ (Troy Merkel, RSM), type: professional-body, url: "https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit", date: 2026-08-25, access: full, locator: "section 'RSM Luca Resourcing: connecting people, projects and execution'"}
    - {ref: JOFA-5IMP-2026, title: "5 imperatives for auditors from the PCAOB chair", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/jan/5-imperatives-for-auditors-from-the-pcaob-chair/", date: 2026-01-12, access: full, locator: "imperative 4 ('Time isn't always of the essence')"}
  last_reviewed: 2026-10-16
  notes: >
    Grade B with a caution: the AI element is unspecified in the source, so treat this as an adjacent resourcing tool.
    The landscape file called it an AI staffing tool; the CAQ page itself says only that it replaces manual processes.

- id: assurance-quality-management-07
  title: Training for reviewers on AI limits and automation bias, including in-workflow micro-training
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [document-production, coordination-scheduling]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >
    Reviewers who do not know a tool's known weaknesses may accept fluent but wrong output. The FRC says if a tool is known
    to sound confident when it is wrong, staff must know this and apply skepticism (FRC-GENAI-2026, p. 35).
  solution: >
    The FRC says training on how to review or oversee a tool should cover its purpose, the risk of automation bias and
    strategies for avoiding it, and known performance issues, and that education is ongoing, not a launch event
    (FRC-GENAI-2026, p. 35). IFIAR asks firms to map training programmes to required competencies, keep training records and set
    refresher intervals proportionate to risk (IFIAR-TTF-2026, p. 7). Deloitte announced a "tutor mode" in Omnia that gives
    on-demand micro-training in the context of the work (DELOITTE-OMNIA-2026). EY says it has built a global training
    programme to upskill all global audit and technology risk professionals this year (EY-CANVAS-2026).
  outcomes:
    - {lever: quality, description: "none published", figure: "none", measures: "n/a", provenance: self-reported, source_ref: DELOITTE-OMNIA-2026}
  prerequisites:
    - "A catalogue of known tool performance issues, fed by testing and monitoring (FRC-GENAI-2026, p. 35)"
    - "Competency map and training records (IFIAR-TTF-2026, p. 7)"
  risks_and_guardrails:
    - "ICAEW's technology faculty chair says the FRC's automation-bias content is a single paragraph and the long-term judgment risk deserves more (ICAEW-FRCVIEW-2026)"
    - "ICAEW's chair stresses training on exercising judgment and skepticism over outputs, not only how to use the software (ICAEW-FRCVIEW-2026)"
  human_checkpoints:
    - Staff demonstrate competence before reviewing AI output on engagements (IFIAR-TTF-2026, p. 7)
  role_evolution: >
    Deloitte says professionals will supervise, validate and work alongside AI (DELOITTE-OMNIA-2026).
  evidence_grade: C
  sources:
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p. 35"}
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "p. 7"}
    - {ref: DELOITTE-OMNIA-2026, title: "Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24, access: full, locator: "section on talent development"}
    - {ref: EY-CANVAS-2026, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: 2026-04-07, access: full, locator: "final paragraphs on training"}
    - {ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05-06, access: full, locator: "section 'Misinterpretation or misuse will take the most work'"}
  last_reviewed: 2026-10-16
  notes: >
    Grade C: both firm items are announcements; neither publishes participation, test results or effect on review
    quality. Deloitte's page says tutor mode is part of the new agentic capabilities; its status of use is not stated.

- id: assurance-quality-management-08
  title: Redesign of junior development as juniors become reviewers of AI output (announced, with regulator concern)
  archetype: assurance
  module: quality-management
  function: people-hr
  work_types: [coordination-scheduling, document-production]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >
    If tools do the first-pass work juniors used to do, juniors lose the practice that built judgment, while firms lean on
    them to review tool output. Botic cited research that AI tools can erode critical thinking and skepticism and said
    new paths for juniors to gain these skills will be needed (NYSSCPA-BOTIC-2025; CAALLEY-PCAOBPE-2025).
  solution: >
    PwC's AI assurance leader said new hires would function like managers within three years because they would oversee AI
    performing routine tasks, and that PwC's assurance training is moving to "back to basics" fundamentals with more time
    for critical thinking, negotiation and professional skepticism that were previously taught later (BI-PWC-2025).
    Botic added critical thinking and communication to the attributes he wants entrants to build (PCAOB-BOTICIOWA-2026).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: self-reported, source_ref: BI-PWC-2025}
  prerequisites:
    - "Training content that teaches review and challenge of tool output (BI-PWC-2025)"
    - "A way for juniors to build skills the tools now perform, from academia or the firm (NYSSCPA-BOTIC-2025)"
  risks_and_guardrails:
    - "ICAEW reports the Big Four each cut graduate intake in 2025 by as much as 6% to 29%; a mid-tier partner said juniors complement AI rather than being replaced, as tools are not good enough yet (ICAEW-EXPECT-2026)"
    - "Large-firm partners worry AI shifts go too far too fast, leaving seniors doing remedial work for AI shortfalls and missing juniors (ICAEW-EXPECT-2026)"
    - "The research Botic cites is an EEG study of essay writing by 54 participants, not an audit study (KOSMYNA-2025)"
  human_checkpoints:
    - Senior review of work by juniors who are themselves reviewing AI output
  role_evolution: >
    Entry-level roles shift to review and supervision of AI work (BI-PWC-2025). The Accounting Podcast describes lean senior
    teams overseeing automated systems in place of large junior cohorts (PODWISE-ACCTPOD-2026).
  evidence_grade: C
  sources:
    - {ref: BI-PWC-2025, title: "PwC is training junior accountants to be like managers, because AI is going to be doing the entry-level work", publisher: Business Insider via Yahoo Finance, type: press, url: "https://finance.yahoo.com/news/pwc-training-junior-accountants-managers-170001522.html", date: 2025-08-08, access: full, locator: "paras 1-12"}
    - {ref: NYSSCPA-BOTIC-2025, title: "PCAOB's Botic Flags Opportunities and Risks in AI", publisher: NYSSCPA (summarising Accounting Today), type: professional-body, url: "https://nysscpa.org/news/1051584-pcaobs-botic-flags-opportunities-and-risks-in-ai-2025-12-10", date: 2025-12-10, access: full, locator: "paras 2-5"}
    - {ref: CAALLEY-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: CAalley (citing Accounting Today), type: press, url: "https://caalley.com/news-updates/international-news/pcaob-warns-auditors-about-ai-and-pe", date: 2025-12-09, access: full, locator: "paras 3-4"}
    - {ref: PCAOB-BOTICIOWA-2026, title: "The Role of the Financial Statement Auditor, and Thoughts on the PCAOB Inspection Process and Its Contemplated Transformation", publisher: PCAOB (G. Botic), type: regulator, url: "https://pcaobus.org/news-events/speeches/speech-detail/the-role-of-the-financial-statement-auditor--and-thoughts-on-the-pcaob-inspection-process-and-its-contemplated-transformation", date: 2026-10-05, access: full, locator: "section 'Attributes of an Effective Financial Statement Auditor'"}
    - {ref: ICAEW-EXPECT-2026, title: "Are businesses expecting too much of AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/feb-2026/are-businesses-expecting-too-much-of-ai", date: 2026-02-03, access: full, locator: "intro and 'How to address AI concerns'"}
    - {ref: PODWISE-ACCTPOD-2026, title: "The Accounting Podcast: 'When Financial Reports Used to Be Cool & AI's Microwave Moment' (AI-generated summary)", publisher: The Accounting Podcast via Podwise, type: podcast, url: "https://podwise.ai/episodes/9035550", date: 2026-10-01, access: full, locator: "episode summary"}
    - {ref: KOSMYNA-2025, title: "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task", publisher: arXiv (MIT Media Lab authors), type: academic, url: "https://arxiv.org/abs/2506.08872", date: 2025-06-10, access: full, locator: "abstract"}
  last_reviewed: 2026-10-16
  notes: >
    Grade C: PwC's statement is a forward-looking claim ("will") by a firm leader; no outcomes are published. The podcast item
    is an AI-generated summary of an episode, not the audio. A search snippet (not opened; blocked by an anti-bot page)
    described a small Swedish qualitative study of seven junior auditors suggesting firm culture affects how confidently
    juniors challenge AI; it is not used as a source here.

- id: assurance-quality-management-09
  title: Proactive engagement with inspectors and supervisors on AI tools, including demonstrations during piloting
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >
    Standards do not yet address AI directly, and regulators are still working out what they expect. A PCAOB board member
    told a director audience in 2026 that the regulator is still figuring out whether AI needs new standards or
    documentation rules (FOLEY-PCAOB-2026).
  solution: >
    The PCAOB's inspections director said inspectors meet firms, generally larger ones, to understand their AI use, that many
    firms invited inspectors to demonstrations while piloting, and that AI is an inspection focus for 2026 (CAALLEY-PCAOBPE-2025).
    PCAOB staff at the December 2025 AICPA conference said firms' AI adoption will be an area of focus for inspectors (DART-SECPCAOB-2025).
    IFIAR encourages early engagement with local regulators and IFIAR, particularly when technology may significantly alter the
    nature of audit work (IFIAR-TTF-2026, p. 4). The FRC's head of assurance technology said an overarching goal of its AI guidance was
    to show the regulator is fine in principle with firms using AI, provided it is done sensibly, and that the FRC works with firm
    representatives on a working group to learn what firms are doing (ICAEW-POD-2025).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: CAALLEY-PCAOBPE-2025}
  prerequisites:
    - "A firm view of which tools are in pilot and which are certified (CAALLEY-PCAOBPE-2025)"
    - "Ability to explain a tool and how it was validated (PCAOB-BOTICSF-2026)"
  risks_and_guardrails:
    - "Regulators' stated focus includes how firms' quality control addresses AI at firm level as well as what appears in selected files (CAALLEY-PCAOBPE-2025)"
    - "The PCAOB's July 2024 staff spotlight on GenAI reflects staff views, not binding rules (FIELDGUIDE-PCAOB-2026)"
  human_checkpoints:
    - Firm leadership decides what is shown to inspectors and when
  role_evolution: >
    Quality and regulatory-relations leaders add AI tool briefings to their inspection preparation (CAALLEY-PCAOBPE-2025).
  evidence_grade: C
  sources:
    - {ref: CAALLEY-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: CAalley (citing Accounting Today), type: press, url: "https://caalley.com/news-updates/international-news/pcaob-warns-auditors-about-ai-and-pe", date: 2025-12-09, access: full, locator: "paras 8-9 (Gunia remarks)"}
    - {ref: DART-SECPCAOB-2025, title: "Heads Up: Highlights of the 2025 AICPA & CIMA Conference on Current SEC and PCAOB Developments", publisher: Deloitte DART, type: conference, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways", date: 2025-12-12, access: full, locator: "Highlights section, AI paragraph"}
    - {ref: FOLEY-PCAOB-2026, title: "What Directors Should be Asking About the Audit and the Auditors Now", publisher: Foley & Lardner, type: firm, url: "https://www.foley.com/insights/publications/2026/07/what-directors-should-be-asking-about-the-audit-and-the-auditors-now/", date: 2026-07-02, access: full, locator: "section 'AI arrived before the rules did'"}
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "p. 4"}
    - {ref: ICAEW-POD-2025, title: "How should audit firms use AI? (podcast and transcript)", publisher: ICAEW Beyond Finance, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "transcript, McConnon answer on objectives for the guidance"}
    - {ref: PCAOB-BOTICSF-2026, title: "Smaller Audit Engagements, Significant Impact: Audit Quality, Investor Protection, and the Future of the Profession", publisher: PCAOB (G. Botic), type: regulator, url: "https://pcaobus.org/news-events/speeches/speech-detail/smaller-audit-engagements--significant-impact--audit-quality--investor-protection--and-the-future-of-the-profession", date: 2026-09-22, access: full, locator: "section 'Expanding Use of Technology in Audits'"}
    - {ref: FIELDGUIDE-PCAOB-2026, title: "PCAOB AI oversight: where the Board stands on AI in audit", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/pcaob-ai-audit-standards", date: 2026-08-06, access: full, locator: "section 'What the PCAOB Spotlight says about GenAI in audits'"}
  last_reviewed: 2026-10-16
  notes: >
    Grade C: the evidence is regulators' statements that firms do this; no firm is named. The Gunia quotes reach us through
    press summaries of her prepared remarks (Accounting Today), not the PCAOB text. The FRC sandbox (a landscape item) was not
    opened for this file.

- id: assurance-quality-management-10
  title: File documentation that shows how AI-assisted procedures were run and where the reviewer's judgment entered (idea)
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >
    A GenAI-drafted memo can read well while the file does not show which prompts or sources were used or where the reviewer
    applied judgment. A PCAOB board member, speaking to directors, said a machine may make a judgment but it must still be
    documented in a way that satisfies an auditing standard (FOLEY-PCAOB-2026).
  solution: >
    Idea discussed by regulators and practitioners. IFIAR asks firms to be able to explain key judgments, including how auditor
    judgment was applied, challenged or exercised in relation to AI outputs and critical human decision points (IFIAR-TTF-2026, p. 5).
    The FRC says outputs may be built to explain themselves, with references to the information considered (FRC-GENAI-2026, p. 39).
    Baker Tilly's synthesis of the IIA's March 2026 conference recommends treating AI output as a first draft with a named
    human reviewer who documents why they agreed or disagreed (BAKERTILLY-GAM-2026). A vendor article says the file should show
    prompts, source material and reviewer judgment (FIELDGUIDE-PCAOB-2026). A state CPA society author says a generic note that an AI
    tool was used would not meet AU-C 230 (CALCPA-AISTD-2026).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: IFIAR-TTF-2026}
  prerequisites:
    - "Logging of tool inputs, outputs and versions per engagement (FIELDGUIDE-PCAOB-2026)"
    - "A template that records the reviewer's reasons (BAKERTILLY-GAM-2026)"
  risks_and_guardrails:
    - "The CalCPA article says a PCAOB board member warned that demands to document every detail of AI models could make AI procedures costlier to defend than manual sampling; the article's account of inspection findings on AI could not be verified (CALCPA-AISTD-2026)"
    - "The PCAOB has issued no rule written specifically for AI, and its June 2024 technology amendments did not cover it (FIELDGUIDE-PCAOB-2026)"
  human_checkpoints:
    - Named reviewer records the conclusion and reasons for each AI-assisted procedure
  role_evolution: >
    Reviewers carry a documentation duty for AI-assisted work, as in Baker Tilly's named-reviewer protocol (BAKERTILLY-GAM-2026).
  evidence_grade: D
  sources:
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "p. 5 (agentic AI); pp. 7-8"}
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p. 39"}
    - {ref: FOLEY-PCAOB-2026, title: "What Directors Should be Asking About the Audit and the Auditors Now", publisher: Foley & Lardner, type: firm, url: "https://www.foley.com/insights/publications/2026/07/what-directors-should-be-asking-about-the-audit-and-the-auditors-now/", date: 2026-07-02, access: full, locator: "section 'AI arrived before the rules did'"}
    - {ref: BAKERTILLY-GAM-2026, title: "Strategy in motion: Internal audit's 2026 execution mandate", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate", date: 2026-04-10, access: full, locator: "takeaway 3, 'AI review protocol'"}
    - {ref: FIELDGUIDE-PCAOB-2026, title: "PCAOB AI oversight: where the Board stands on AI in audit", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/pcaob-ai-audit-standards", date: 2026-08-06, access: full, locator: "key insights; section 'What existing PCAOB expectations still require'"}
    - {ref: CALCPA-AISTD-2026, title: "AI Standard Setting, Regulation in Audit: Part 1", publisher: CalCPA (S. Gadzhieva), type: professional-body, url: "https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1", date: 2026-08-12, access: full, locator: "sections 'Inspection Findings: The Documentation Gap' and 'Documentation (meeting AU-C 230)'"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. Baker Tilly's recommendation concerns internal audit, and Fieldguide is a vendor with a commercial interest in
    documentation tooling. The CalCPA inspection-findings claim is search-grade practitioner commentary and is not used as
    evidence of what inspectors found.

- id: assurance-quality-management-11
  title: Defined human control points and oversight rules for agentic audit tools
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >
    As tools become more autonomous, "a person is in the loop" says little unless the firm defines where people intervene.
    KPMG says a human approval step that rubber-stamps every AI recommendation provides no real control value (KPMG-SOX-2026, p. 14).
  solution: >
    The FRC describes oversight of agentic tools at control points, set by criteria such as intermediary outputs being ready or the
    tool wishing to take certain actions, with the choice of control points an important professional judgment (FRC-GENAI-2026,
    p. 38). IFIAR asks firms to assign specific engagement personnel to decision checkpoints, to review autonomous decisions overall and
    to ensure accountability for all work (IFIAR-TTF-2026, p. 7). IAASB roundtable participants called human-in-the-loop oversight
    non-negotiable, even as systems become more autonomous (IAASB-TQM-2026, p. 4). Deloitte says Omnia agents carry out preliminary
    procedures and draft preliminary conclusions for professionals to review (DELOITTE-OMNIA-2026).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: self-reported, source_ref: DELOITTE-OMNIA-2026}
  prerequisites:
    - "Certification that shows the main risks of deficient output, which informs where control points go (FRC-GENAI-2026, p. 38)"
    - "Reviewers with competence in the use case; specialist expertise for some (FRC-GENAI-2026, p. 37)"
  risks_and_guardrails:
    - "The FRC says professional skepticism and an understanding of automation bias are important elements of oversight (FRC-GENAI-2026, p. 38)"
    - "KPMG says defining when human judgment adds real risk reduction, and designing oversight that captures it, needs careful thought and ongoing experimentation (KPMG-SOX-2026, p. 14)"
  human_checkpoints:
    - Authorising the agent to continue or take specified actions at control points
    - Review of intermediary and final outputs
  role_evolution: >
    Engagement team members become overseers of agentic work. IFIAR says effective integration may need a shift in behaviour and clear
    articulation of the auditor's involvement at each stage (IFIAR-TTF-2026, p. 7).
  evidence_grade: C
  sources:
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 37-38"}
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "p. 7"}
    - {ref: IAASB-TQM-2026, title: "Technology Quality Management Roundtables: Outcomes and Next Steps", publisher: IAASB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-02/IAASB-Technology-Quality-Management-Roundtables-Feedback.pdf", date: 2026-02, access: full, locator: "p. 4 (Future State)"}
    - {ref: KPMG-SOX-2026, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24, access: full, locator: "p. 14 ('The human-in-the-loop imperative')"}
    - {ref: DELOITTE-OMNIA-2026, title: "Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: 2026-06-24, access: full, locator: "capabilities list"}
  last_reviewed: 2026-10-16
  notes: >
    Grade C: Deloitte's announcement is the only named firm item, with no use or result stated. KPMG's remark is from a SOX and
    controls paper, so it concerns AI in controls, an adjacent area; the FRC, IFIAR and IAASB material is guidance, not a deployment.

- id: assurance-quality-management-12
  title: "Review designed to counter automation bias, with the reviewer forming an independent view before accepting AI output (idea)"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    India's NFRA says fluent, well-presented machine output invites automation bias, meaning plausible-looking results get less
    challenge than a human-prepared equivalent would (NFRA-CAALLEY-2026).
  solution: >
    Idea in regulator guidance. The FRC says review may involve forming an independent view to compare some or all of the output
    against, for example reading the source material to confirm a GenAI summary, or identifying risks of material misstatement
    oneself before comparing with an AI-generated list (FRC-GENAI-2026, p. 37). The FRC also says other components, such as
    rules-based checks, can evaluate LLM outputs (FRC-GENAI-2026, p. 26). NFRA says engagement teams and reviewers must consciously
    counter the tendency (NFRA-CAALLEY-2026).
  outcomes:
    - {lever: quality, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: FRC-GENAI-2026}
  prerequisites:
    - "Reviewers with the competence to form their own view (FRC-GENAI-2026, p. 37)"
    - "Time in the engagement plan for the extra work of independent review (JOFA-5IMP-2026)"
  risks_and_guardrails:
    - "Independent review adds time and may reduce the efficiency gain; the FRC says the nature and extent of review is a matter of professional judgment based on residual risk (FRC-GENAI-2026, p. 37)"
    - "ICAEW says automation bias poses risks to professional judgment in the long term and is given one paragraph on page 35 of the FRC guidance (ICAEW-FRCVIEW-2026)"
  human_checkpoints:
    - Reviewer's own assessment recorded before comparison with the tool output
  role_evolution: >
    Reviewers act as independent challengers rather than approvers (FRC-GENAI-2026, p. 37).
  evidence_grade: D
  sources:
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 26, 37"}
    - {ref: NFRA-CAALLEY-2026, title: "AI cannot replace auditor judgement, flags automation bias in audits: NFRA", publisher: CAalley (citing The Business Standard), type: press, url: "https://caalley.com/news-updates/indian-news/ai-cannot-replace-auditor-judgement-flags-automation-bias-in-audits-nfra", date: 2026-07-24, access: full, locator: "paras 3-4"}
    - {ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05-06, access: full, locator: "section 'Misinterpretation or misuse will take the most work'"}
    - {ref: JOFA-5IMP-2026, title: "5 imperatives for auditors from the PCAOB chair", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/jan/5-imperatives-for-auditors-from-the-pcaob-chair/", date: 2026-01-12, access: full, locator: "imperative 4"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. The FRC presents independent-view review as something review "may involve"; no firm reports using it or measuring
    whether it reduces missed errors. The NFRA article is a secondary report of NFRA's July 2026 paper; the paper was not opened.

- id: assurance-quality-management-13
  title: Engagement-leader planning of AI use at the outset, with whole-file reflection on skepticism at the end (idea)
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    ISA 220 (Revised) puts responsibility for direction, supervision and review on the engagement partner. IAASB stakeholders said tool
    outputs that are hard to explain, need specialised skills to evaluate or invite over-reliance complicate how partners discharge
    this (IAASB-TQMPLAN-2026, para 10, p. 2).
  solution: >
    Idea in regulator and professional-body guidance. IFIAR says engagement leaders should set expectations at the outset for how
    technology will be used, including engagement-specific planned uses of AI, and that senior team members should reflect on the overall
    use of technology in the file and whether skepticism was maintained (IFIAR-TTF-2026, p. 7). The AICPA's practice aid recommends firm
    planning of intended AI use in specific engagements and says partners must understand the tools, ensure the firm has approved them and that
    staff use them correctly (AICPA-PA-2026).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: IFIAR-TTF-2026}
  prerequisites:
    - "A firm-approved tool list the partner can check against (AICPA-PA-2026)"
    - "Partner training on the tools in use (AICPA-PA-2026)"
  risks_and_guardrails:
    - "The AICPA says the auditor remains responsible for the audit and the opinion (JOFA-AIPA-2026)"
    - "The practice aid's full text is behind a login and was not read; only the release and a JofA article were (AICPA-PA-2026)"
  human_checkpoints:
    - Engagement-leader planning decision on AI use
    - Senior team reflection on the file before sign-off
  role_evolution: >
    Engagement partners carry explicit responsibility for appropriate tool use and for staff using tools correctly (AICPA-PA-2026).
  evidence_grade: D
  sources:
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "p. 7"}
    - {ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: AICPA & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "'Use of AI-related technological resources by audit firms' section"}
    - {ref: JOFA-AIPA-2026, title: "AI and the audit: AICPA publishes practice aid to assist auditors", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/", date: 2026-10-13, access: full, locator: "quotes from AICPA chief auditor"}
    - {ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F)", publisher: IAASB, type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "para 10"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. The AICPA's practice aid was issued three days before this file's date and is not yet visible in practice.

- id: assurance-quality-management-14
  title: Cross-checking AI output with a second model or rules-based component, with a human at the end (idea)
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >
    Generative tools are probabilistic. The FRC's head of assurance technology notes the same prompt can give different outputs at
    different times (ICAEW-POD-2025), and an RSM UK analytics director says no tool can be guaranteed to give the right output every
    time (ICAEW-FRCVIEW-2026).
  solution: >
    Idea discussed by regulators and practitioners. The FRC's McConnon said letting multiple AI systems tackle a problem and comparing
    the answers, or having AI do the comparing, can reduce variability while keeping a human at the end (ICAEW-POD-2025). Grant Thornton
    UK's Jon Morris said AI reviewing AI may come "a few years down the line" and is the direction of travel (ICAEW-POD-2025). The FRC
    guidance says rules-based processing or predictive machine learning can evaluate LLM outputs, for example by checking a schema
    (FRC-GENAI-2026, p. 26). RSM UK's Konrad Bukowski-Kruszyna advises building a rules-based tool alongside GenAI when data must be
    analysed (ICAEW-FRCVIEW-2026).
  outcomes:
    - {lever: quality, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: ICAEW-POD-2025}
  prerequisites:
    - "Two or more independent components whose errors are not correlated (ICAEW-POD-2025)"
    - "Rules for what happens when components disagree (FRC-GENAI-2026, p. 26)"
  risks_and_guardrails:
    - "The sources do not test whether cross-checks catch more errors than single review; none is published (ICAEW-POD-2025; FRC-GENAI-2026, p. 26)"
    - "Morris agreed with the host that AI reviewing would require a high degree of confidence (ICAEW-POD-2025)"
  human_checkpoints:
    - Human review at the end of the process (ICAEW-POD-2025)
  role_evolution: >
    Reviewers handle disagreements between components rather than every item (ICAEW-POD-2025).
  evidence_grade: D
  sources:
    - {ref: ICAEW-POD-2025, title: "How should audit firms use AI? (podcast and transcript)", publisher: ICAEW Beyond Finance, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "transcript, segment after time code 13'49\" (oversight and explainability)"}
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "p. 26"}
    - {ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05-06, access: full, locator: "section 'Use the illustrative examples'"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. The podcast was recorded 7 November 2025 and first published 11 November 2025. The speakers describe it as future direction.

- id: assurance-quality-management-15
  title: Disclosure of AI use to clients and audit committees through engagement-letter terms and routine questions
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    Clients worry about where their data goes and whether it trains models. A Grant Thornton UK director said some clients were
    nervous and a few would not sign up (ICAEW-POD-2025).
  solution: >
    Grant Thornton UK's Jon Morris said the firm uses clear terms in the engagement letter about what AI will be used for, and in some cases
    ring-fences the work so it is not used to train other models (ICAEW-POD-2025). Deloitte's Martin Brown said very few clients had
    specifically asked the firm not to use GenAI, and that transparency and education matter (ICAEW-POD-2025). A Foley article, from a PCAOB
    event for directors, suggests audit committees ask what the auditor is doing with AI, under what controls and how AI-assisted judgments are
    documented (FOLEY-PCAOB-2026). IFIAR says communicating how technology is used supports audit committee oversight (IFIAR-TTF-2026, p. 8).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: self-reported, source_ref: ICAEW-POD-2025}
  prerequisites:
    - "Firm policy on data handling and model training, agreed with the technology function (ICAEW-POD-2025)"
    - "Standard wording for engagement letters and audit committee communications (ICAEW-POD-2025)"
  risks_and_guardrails:
    - "Some clients may decline; Morris said AI can still be used in a ring-fenced way (ICAEW-POD-2025)"
    - "The FRC guidance calls for appropriate authorisation from entities whose data is used, per the podcast host's reading; the guidance itself was not checked for this point (ICAEW-POD-2025)"
  human_checkpoints:
    - Engagement leader agrees AI use terms with the client and audit committee
  role_evolution: >
    Engagement leaders add AI use to client and audit committee conversations (FOLEY-PCAOB-2026).
  evidence_grade: B
  sources:
    - {ref: ICAEW-POD-2025, title: "How should audit firms use AI? (podcast and transcript)", publisher: ICAEW Beyond Finance, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "transcript, between time codes 04'50\" and 13'49\" (client data)"}
    - {ref: FOLEY-PCAOB-2026, title: "What Directors Should be Asking About the Audit and the Auditors Now", publisher: Foley & Lardner, type: firm, url: "https://www.foley.com/insights/publications/2026/07/what-directors-should-be-asking-about-the-audit-and-the-auditors-now/", date: 2026-07-02, access: full, locator: "'Five questions to take back to your auditor', question 2"}
    - {ref: IFIAR-TTF-2026, title: "Use of technology in audits - Innovation and audit quality (2026)", publisher: IFIAR, type: regulator, url: "https://www.ifiar.org/?wpdmdl=19893", date: 2026-04-20, access: full, locator: "pp. 7-8 ('Transparency of Use and for Those Charged with Governance')"}
  last_reviewed: 2026-10-16
  notes: >
    Grade B: Grant Thornton UK and Deloitte practices are described by named firm representatives, with no measurements. The
    evidence is spoken, from a 2025 podcast, and no figure on client refusals is given beyond "a very limited number".
    Routed in part to acceptance-independence.

- id: assurance-quality-management-16
  title: Proportionate AI governance for small and mid-size firms that buy third-party tools (idea)
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    ICAEW's head of data analytics says the FRC guidance talks a lot about technology and methodology specialists that smaller firms will
    not have, and that smaller firms lean heavily on third-party providers (ICAEW-FRCVIEW-2026). The IAASB names an uneven playing field
    where larger firms are better placed to develop, govern and use these tools (IAASB-TQMPLAN-2026, para 11, p. 3).
  solution: >
    Idea discussed by practitioners and standard-setters. Start small with granular, easily checked tasks, as Grant Thornton UK's Jon
    Morris advised, and ask providers what testing they have done for the use case (Deloitte's Martin Brown) (ICAEW-POD-2025). Botic
    said the question for smaller firms is whether a tool addresses a real audit need and can be governed effectively, not whether the firm can adopt
    every tool (PCAOB-BOTICSF-2026). The IAASB says its guides will aim to be scalable and proportionate for small and medium-sized practices
    (IAASB-TQMPLAN-2026, para 16, p. 3).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: IAASB-TQMPLAN-2026}
  prerequisites:
    - "Vendor evidence of testing for the specific use case (ICAEW-POD-2025)"
    - "A named owner for tool oversight even in a small firm (PCAOB-BOTICSF-2026)"
  risks_and_guardrails:
    - "ICAEW's technology faculty chair notes most AI tools in audit are features added to existing products, which raises questions about what to ask vendors (ICAEW-FRCVIEW-2026)"
    - "Botic says smaller firms lack the largest firms' investment resources (PCAOB-BOTICSF-2026)"
  human_checkpoints:
    - Partner decision on whether a tool is fit for a defined use case
  role_evolution: >
    Quality partners in small firms take on tool due diligence, sometimes with outside help (ICAEW-POD-2025).
  evidence_grade: D
  sources:
    - {ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05-06, access: full, locator: "section 'Smaller firms may have specific considerations'"}
    - {ref: IAASB-TQMPLAN-2026, title: "Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F)", publisher: IAASB, type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf", date: 2026-03, access: full, locator: "paras 11, 16"}
    - {ref: ICAEW-POD-2025, title: "How should audit firms use AI? (podcast and transcript)", publisher: ICAEW Beyond Finance, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "transcript, final third (off-the-shelf solutions)"}
    - {ref: PCAOB-BOTICSF-2026, title: "Smaller Audit Engagements, Significant Impact: Audit Quality, Investor Protection, and the Future of the Profession", publisher: PCAOB (G. Botic), type: regulator, url: "https://pcaobus.org/news-events/speeches/speech-detail/smaller-audit-engagements--significant-impact--audit-quality--investor-protection--and-the-future-of-the-profession", date: 2026-09-22, access: full, locator: "section 'Expanding Use of Technology in Audits'"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. The IAASB's guides are expected through mid-2027; none has been issued (IAASB-TQMPLAN-2026, p. 9). The CPA.com benchmark
    figure that 66% of US small and mid-size firms cite untrained staff as a blocker comes from the landscape file and was not
    re-opened here.

- id: assurance-quality-management-17
  title: Independent validation or assurance of audit firms' AI tools by third parties (idea)
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >
    Smaller firms without in-house expertise may want someone to confirm that a tool works as intended. The FRC's McConnon described
    the market for assurance over AI tools as fragmented, with many types of provider and no regulation in the traditional sense, like
    sustainability assurance a few years earlier (ICAEW-POD-2025).
  solution: >
    Idea discussed on the podcast. Deloitte's Martin Brown said third-party providers should be doing testing and evaluation for the use
    case. Grant Thornton UK's Jon Morris said smaller firms would probably take more comfort from a provider partnering with a large firm than
    from a SOX-type report, though it is early days (ICAEW-POD-2025).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: ICAEW-POD-2025}
  prerequisites:
    - "Recognised criteria for what a validation covers (ICAEW-POD-2025)"
    - "Providers with independence and competence to assess tools (ICAEW-POD-2025)"
  risks_and_guardrails:
    - "Morris expected the market to decide rather than any formal scheme, and called the situation early days (ICAEW-POD-2025)"
  human_checkpoints:
    - Firm decides what weight to give a third-party validation when approving a tool
  role_evolution: >
    New providers, including some audit firms and boutique assurers, are moving into assurance of AI tools, per the FRC's McConnon (ICAEW-POD-2025).
  evidence_grade: D
  sources:
    - {ref: ICAEW-POD-2025, title: "How should audit firms use AI? (podcast and transcript)", publisher: ICAEW Beyond Finance, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "transcript, final third (independent assurance question)"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. Assurance over AI tools for clients is covered by the other-assurance module; this entry concerns validation of the auditor's own
    tools. Only one source speaks to it.

- id: assurance-quality-management-18
  title: AI-enabled monitoring and root-cause analysis of the firm's own system of quality management (idea)
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [data-reporting, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    The PCAOB's Chairman says engagement-level deficiencies are often symptoms of earlier issues in training, supervision, methodology,
    governance or resource allocation (PCAOB-LOGOQC-2026). Finding those root causes across many files is manual.
  solution: >
    Idea raised by a regulator. The SEC's chief accountant said the SEC asks auditors how they use AI to improve engagement-level audit
    quality and how they use AI to monitor their system of quality control (KPMG-HOHL-2026). The FRC noted firms' tool use may sometimes be
    captured in other activities such as root cause analysis, without saying AI is used to do the analysis (FRC-ATT-2025, p. 20).
  outcomes:
    - {lever: quality, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: KPMG-HOHL-2026}
  prerequisites:
    - "Structured data from inspections, internal reviews and engagement files (PCAOB-BOTICIOWA-2026)"
  risks_and_guardrails:
    - "The PCAOB staff deck says about 90% of registration and inspection data is unstructured, and describes early AI pilots in the PCAOB's own inspection work; that is the regulator's data, and it shows how heavy the structuring job is (STARLING-IMC-2026)"
  human_checkpoints:
    - Quality leadership decides on remediation after root-cause findings
  role_evolution: >
    Audit quality and risk teams add data and AI skills to monitoring (KPMG-HOHL-2026).
  evidence_grade: D
  sources:
    - {ref: KPMG-HOHL-2026, title: "Q&A with Kurt Hohl, SEC chief accountant", publisher: KPMG, type: firm, url: "https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html", date: 2026-05-27, access: full, locator: "answers on AI and on the inspection process"}
    - {ref: PCAOB-LOGOQC-2026, title: "Statement on the Adoption of QC 1000 Amendments", publisher: PCAOB (Chairman D. Logothetis), type: regulator, url: "https://pcaobus.org/news-events/speeches/speech-detail/statement-on-the-adoption-of-qc-1000-amendments", date: 2026-09-09, access: full, locator: "section 'The Hinge Opening the Door to Inspection Modernization'"}
    - {ref: FRC-ATT-2025, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/8383/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf", date: 2025-06, access: full, locator: "p. 20"}
    - {ref: STARLING-IMC-2026, title: "Modernizing US PCAOB Audit Inspections", publisher: Starling Insights, type: press, url: "https://insights.starlingtrust.com/content/observations/modernizing-us-pcaob-audit-inspections", date: 2026-09-01, access: full, locator: "paras 1-5"}
    - {ref: PCAOB-BOTICIOWA-2026, title: "The Role of the Financial Statement Auditor, and Thoughts on the PCAOB Inspection Process and Its Contemplated Transformation", publisher: PCAOB (G. Botic), type: regulator, url: "https://pcaobus.org/news-events/speeches/speech-detail/the-role-of-the-financial-statement-auditor--and-thoughts-on-the-pcaob-inspection-process-and-its-contemplated-transformation", date: 2026-10-05, access: full, locator: "section 'The PCAOB: Inspection-related Developments'"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. Hohl asked how firms use AI for this; no firm reports doing it. The "90% unstructured" figure concerns PCAOB data and is
    reported secondhand by Starling from staff materials that the Board has not adopted.

- id: assurance-quality-management-19
  title: Curated use-case policy and prompt library for GenAI tools, set by the firm (idea)
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [document-production, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Free choice of prompts and use cases makes a tool harder to test and harder to train staff on. The FRC says a narrow set of permitted
    uses may be easier to design, test and teach, at the cost of value (FRC-GENAI-2026, p. 35).
  solution: >
    The FRC lays out options: curate a narrow range of use cases or leave staff to judge when to use a tool; control configuration and
    prompts centrally, require prompts from a library validated in certification, or let teams write their own. Prompts from a library may have
    been validated, but cannot match the diversity of bespoke prompts (FRC-GENAI-2026, pp. 35-36). Deloitte's Martin Brown spoke of firms
    working out how to approve tools and the balance of expectations between central functions and engagement teams (ICAEW-POD-2025).
  outcomes:
    - {lever: risk, description: "none published", figure: "none", measures: "n/a", provenance: independent, source_ref: FRC-GENAI-2026}
  prerequisites:
    - "Certification results showing sensitivity to prompt and configuration (FRC-GENAI-2026, p. 36)"
    - "A central owner of the prompt library (FRC-GENAI-2026, p. 36)"
  risks_and_guardrails:
    - "The FRC lists factors that may call for a more prescriptive approach, including testing that shows performance is sensitive to prompt variations and pilots showing teams do not use the tool consistently (FRC-GENAI-2026, p. 36)"
  human_checkpoints:
    - Methodology owner approves each permitted use case and prompt set
  role_evolution: >
    Specialists write and validate prompts that audit teams then use (FRC-GENAI-2026, p. 36).
  evidence_grade: D
  sources:
    - {ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: FRC, type: regulator, url: "https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "pp. 35-36"}
    - {ref: ICAEW-POD-2025, title: "How should audit firms use AI? (podcast and transcript)", publisher: ICAEW Beyond Finance, type: podcast, url: "https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript", date: 2025-11-11, access: full, locator: "transcript, Brown answer after the McConnon remarks on objectives"}
  last_reviewed: 2026-10-16
  notes: >
    Idea. These are options the FRC sets out; no firm is reported choosing one. The RSM Ask Luca entry (05) is the nearest named
    example of a grounded, curated tool.
```

---

## 3. Module notes

### Processes and key steps (work types)

**Firm level (ISQM 1 / QC 1000 components: governance, resources, information and technology, monitoring and remediation, acceptance)**

- **Needs analysis and prioritisation of tools:** `expert-judgment`, `coordination-scheduling`. IFIAR asks firms to prioritise wide deployment of tools that achieve defined, measurable objectives and have the most effect on audit quality (IFIAR-TTF-2026, p. 4).
- **Selection, build and third-party due diligence:** `research-synthesis`, `review-assurance`. The IAASB's plan separates network, firm and engagement-team responsibilities across tool lifecycle stages and says the firm keeps responsibility for approval and monitoring wherever a tool is built (IAASB-TQMPLAN-2026, paras 28–29, Table 1).
- **Certification (inputs, architecture, output testing) and limited deployment:** `review-assurance`, `software-systems`. FRC-GENAI-2026, pp. 30–33.
- **Authorisation, access control and version control:** `software-systems`. FRC-ATT-2025, p. 22.
- **Policy and methodology updates (when and how staff may use a tool; prompt libraries):** `document-production`. FRC-GENAI-2026, pp. 35–36.
- **Training and competence:** `coordination-scheduling`, `document-production`. FRC-GENAI-2026, p. 35; IFIAR-TTF-2026, p. 7.
- **Monitoring of tool use and quality impact, recertification, retirement:** `data-reporting`, `review-assurance`. FRC-ATT-2025, pp. 20–22; IFIAR-TTF-2026, pp. 8–9.
- **Root-cause analysis and remediation:** `expert-judgment`. The PCAOB says engagement deficiencies often trace to earlier training, supervision, methodology, governance or resourcing issues (PCAOB-LOGOQC-2026).
- **Resourcing and staffing:** `coordination-scheduling`. CAQ-RSM-2026.
- **Interaction with regulators:** `client-interaction`, `document-production`. CAALLEY-PCAOBPE-2025; IFIAR-TTF-2026, p. 4.

**Engagement level (ISA 220 (Revised): direction, supervision and review)**

- **Planning how AI will be used and what it can and cannot do:** `expert-judgment`. IFIAR-TTF-2026, p. 7.
- **Direction and supervision of staff using tools; reviewer competence:** `coordination-scheduling`. FRC-GENAI-2026, p. 37.
- **Review of tool outputs and, for agentic tools, oversight at control points:** `review-assurance`. FRC-GENAI-2026, pp. 37–38.
- **Documentation of AI-assisted procedures and the reviewer's judgment:** `document-production`. IFIAR-TTF-2026, p. 5.
- **Communication with the client and audit committee about AI use:** `client-interaction`. FOLEY-PCAOB-2026.

### Common pain points

- **Tools that do not fit processes built for deterministic software.** Opacity, non-determinism and adaptivity make it hard to decide how much testing is enough, how to monitor, and how to evaluate outputs (IAASB-TQMPLAN-2026, paras 6–7).
- **Recertification triggers handled informally.** The FRC found trigger identification generally informal and encouraged firms to build it into change management (FRC-ATT-2025, p. 21).
- **Monitoring that counts usage, not quality.** Monitoring was mostly for licensing and no firm quantified quality impact (FRC-ATT-2025, p. 20).
- **Split monitoring responsibility between networks and member firms.** IFIAR saw global monitoring in some networks and member-firm monitoring in others, with a risk of fragmented coverage (IFIAR-TTF-2026, p. 8).
- **Regulatory fragmentation.** The IAASB cites inconsistent regulator interpretation across jurisdictions, diverse firm practice and an uneven playing field for small and mid-size practices (IAASB-TQMPLAN-2026, para 11).
- **Reviewers facing fluent output.** NFRA and the FRC both note that output sounds confident even when wrong (NFRA-CAALLEY-2026; FRC-GENAI-2026, p. 35).
- **Uncertainty about inspector expectations.** An SEC accountant said existing auditing standards were not written with AI in mind (DART-SECPCAOB-2025), and a PCAOB board member said the regulator is still working out whether new standards or documentation rules are needed (FOLEY-PCAOB-2026). ICAEW says regulatory uncertainty is a barrier to adopting AI at scale (ICAEW-LANDMARK-2025).
- **Client pressure on junior hours and fees.** A mid-tier partner said a prospective client asked for fewer junior hours and lower fees because of AI (ICAEW-EXPECT-2026). KPMG reportedly argued to its own auditor that AI should lower its audit fee (VERDANTIX-KPMGFEE-2026).

### Metrics and benchmarks

| Metric | Figure | What it measures, in the source's words | Source |
|---|---|---|---|
| Growth in AI-enabled audit tools at the six global networks, 2025 | About 30% year over year | "approximate 30% year-over-year increase in AI-enabled tools" collectively reported by the GPPC networks; IFIAR notes firms report differently (firm-reported) | IFIAR-TTF-2026, p. 5 |
| Roundtable participation | 8 roundtables, 243 participants, of whom 93 accounting firms and 38 regulators and oversight authorities | Participants in the IAASB's technology quality management roundtables, second half of 2025 | IAASB-TQM-2026, p. 2 |
| Firm monitoring of AI/automated-tool quality impact | None quantified at the six largest UK firms | "no formal monitoring performed by the firms to quantify the audit quality impact" of automated tools | FRC-ATT-2025, p. 20 |
| Suggested monitoring metrics | Engagement coverage %, false-positive/negative rates vs manual sample, rework rates, escalation incidence | IFIAR's examples of emerging practice; no values published | IFIAR-TTF-2026, pp. 8–9 |
| PCAOB inspection results, six US global networks, 2025 | Average Part I.A deficiency rate 13% (26% in 2024); 312 audits reviewed; one restatement identified | As reported by the CAQ; no source links the change to AI | CAQ-INSIDER-2026 |
| Planned reduction in file reviews | Staff IMC deck suggests reviews at the largest firms could fall "well below 50%" of 2025 levels for firms judged lower risk | Botic's reading of the staff slide deck; not Board policy | PCAOB-BOTICIOWA-2026 |
| Size of PCAOB inspection sets | Big Four: 50 to 60 company audits reviewed a year; smaller firms about 30 | As described by the event hosts, from PCAOB guests; not checked against PCAOB data | FOLEY-PCAOB-2026 |
| Time saved after one year of enterprise GenAI at PwC | "Not that drastic yet"; no figure | PwC US assurance leader, October 2026 | CFODIVE-PWC-2026 |
| Graduate intake cuts, Big Four, 2025 | 6% to 29% | ICAEW's wording: all four "cut their graduate intake by as much as 6% to 29% in 2025" | ICAEW-EXPECT-2026 |
| Private-equity deals in accounting firms | More than 90 significant deals and mergers since 2020; more than half in 2025 | PCAOB inspections director's remarks, Dec 2025 (routed to acceptance-independence) | CAALLEY-PCAOBPE-2025 |
| Scale of RSM's guidance copilot | 4,000+ assurance professionals | Firm's headcount that Ask Luca serves; not usage | RSM-LUCA-2026 |

No override rates, reviewer error rates, false-pass rates or parallel-run results for AI-assisted audit work were found in any source.

### Guardrails and regulatory points

- **United States**
  - QC 1000 takes effect in December 2026 (FOLEY-PCAOB-2026). On 9 September 2026 the PCAOB adopted amendments that align the evaluation framework more closely to ISQM 1, including a firm-selected evaluation date. The same amendments rescind the external quality control function requirement and the design-only requirement for firms without engagements (PCAOB-LOGOQC-2026; PCAOB-BOTICNEB-2026).
  - Botic called the external quality control function rescission disappointing (PCAOB-BOTICNEB-2026).
  - The PCAOB has issued no AI-specific standard. Its technology-assisted-analysis amendments (AS 1105, AS 2301) did not address AI (FIELDGUIDE-PCAOB-2026; CALCPA-AISTD-2026).
  - Botic's lifecycle expectation for AI governance is a Board member's view, not a rule (PCAOB-BOTICSF-2026).
  - Big Four firms, the AICPA's Auditing Standards Board and the CAQ appear to back greater emphasis on firms' systems of quality control in inspections (TR-PCAOBPREVIEW-2026).
  - The SEC's Office of the Chief Accountant asks auditors how they use AI to improve audit quality and to monitor their system of quality control (KPMG-HOHL-2026).
  - The AICPA practice aid (13 October 2026) covers firms' AI use under quality management, supervision and review. The practice aid's full text was not read (AICPA-PA-2026).
- **United Kingdom**
  - The FRC guidance (30 March 2026) sets out three risks: deficient output, misinterpretation or misuse, and non-compliant methodology (FRC-GENAI-2026; ICAEW-FRCVIEW-2026). The FRC says it is "not a response to identified quality deficiencies" and that regulatory accountability is unchanged (FRC-GENAINEWS-2026).
  - The FRC's evolved supervision model begins in April 2026 for the largest firms (FRC-SUPERVISION-2026). Board Agenda reports it will rely more on firms' own quality management and carry out fewer inspections where the FRC has confidence in self-review (BOARDAGENDA-SUP-2026).
  - The FRC guidance says the risk of deficient output cannot be eliminated because of LLMs' inherent limitations, and notes that firms' own use of automated tools had, at the six largest firms, no formal monitoring of quality impact (BOARDAGENDA-FRC-2026, reporting the guidance and the 2025 review).
- **International**
  - ISQM 1 and ISA 220 (Revised) are judged resilient. The IAASB's non-authoritative guides will cover tool certification, monitoring and review of outputs, and are not new requirements (IAASB-TQM-2026, p. 4; IAASB-TQMPLAN-2026, paras 18–20).
  - The workstream's expert group includes the Big Four, BDO, Grant Thornton, Forvis Mazars, Caseware, Inflo, the FRC, the PCAOB, CPAB and IOSCO (IAASB-TQMPAGE-2026).
- **India:** NFRA's July 2026 principles ask for formal tool validation, monitoring and re-approval, and say a firm cannot rely on a vendor's terms of service for its own data-protection responsibility (NFRA-CAALLEY-2026).
- **Design guardrails that practitioners and regulators name**
  - Pair LLMs with rules-based components (FRC-GENAI-2026, p. 26).
  - Run alternative procedures in parallel during limited deployment (FRC-GENAI-2026, p. 33).
  - Keep a named reviewer who records why they agreed or disagreed (BAKERTILLY-GAM-2026).
  - Make reviewers competent in the use case, with specialist expertise where needed (FRC-GENAI-2026, p. 37).
  - Define control points for agentic tools in advance (FRC-GENAI-2026, p. 38).

### Frontier signals (dated)

| Date | Signal | Source |
|---|---|---|
| 2025-06 | FRC finds firms still adapting certification to AI risks and building ways to monitor tool usage and quality impact | FRC-ATT-2025 |
| 2025-08-08 | PwC's AI assurance leader says new hires will act like managers within three years, overseeing AI | BI-PWC-2025 |
| 2025-10-28 | PwC says end-to-end AI integration in the audit cycle should arrive within calendar 2026; a year later it says savings are "not that drastic yet" | PWC-AT-2025; CFODIVE-PWC-2026 |
| 2025-11-11 | FRC and firm guests: AI reviewing AI "a few years down the line"; assurance of AI tools is fragmented | ICAEW-POD-2025 |
| 2025-12-09 | PCAOB acting chair warns of skepticism erosion and need for new junior skill paths; inspections director says AI and private equity will be 2026 inspection focus | NYSSCPA-BOTIC-2025; CAALLEY-PCAOBPE-2025 |
| 2025-12 | IAASB approves development of non-authoritative material on quality management and emerging technology | IAASB-TQM-2026 |
| 2026-01-15 | AAA Auditing Section midyear workshop (15-17 Jan) has panels on how auditors and juniors use GenAI in fieldwork (agenda only) | AAA-MIDYEAR-2026 |
| 2026-01-08 | RSM launches Ask Luca for 4,000+ assurance professionals | RSM-LUCA-2026 |
| 2026-03-25 | FRC announces supervision model centred on firms' systems of quality management | FRC-SUPERVISION-2026 |
| 2026-03-30 | FRC issues first regulator guidance on generative and agentic AI in audit | FRC-GENAINEWS-2026 |
| 2026-03 | IAASB approves action plan for technology quality management guides | IAASB-TQMPLAN-2026 |
| 2026-04-20 | IFIAR report: practices for validation, re-approval, oversight committees, metrics; early engagement with regulators | IFIAR-TTF-2026 |
| 2026-05-08 | At the Deloitte/KU symposium (agenda: AI panels, a PE and independence panel) Botic calls PE and AI the most consequential issues facing the profession and asks for academic research | KU-SYMPOSIUM-2026; PCAOB-BOTICKU-2026 |
| 2026-05 | PCAOB launches Inspections Modernization Council to ground inspections in QC 1000 and use AI | PCAOB-LOGOSEIAG-2026; JOFA-IMC-2026 |
| 2026-06-24 | Deloitte announces agents in Omnia, including "tutor mode" | DELOITTE-OMNIA-2026 |
| 2026-07-13 | SEC chief accountant says the QC-focused inspection model may be tougher on firms | CAQ-HOHLWEBINAR-2026 |
| 2026-07-24 | NFRA issues principles on technology adoption: tool validation, monitoring, re-approval | NFRA-CAALLEY-2026 |
| 2026-09-01 | Staff IMC materials propose firm-level risk assessment to set the scope of QC testing and file reviews; AI pilots in inspections | STARLING-IMC-2026 |
| 2026-09-09 | PCAOB adopts QC 1000 amendments | PCAOB-LOGOQC-2026 |
| 2026-09-11 | Botic suggests revisiting a metric on technical resources because of AI, and notes small firms building whole audit operations around AI | PCAOB-BOTICNEB-2026 |
| 2026-09-22 | Botic sets out AI governance lifecycle expectations | PCAOB-BOTICSF-2026 |
| 2026-10-05 | Botic questions a possible cut in file reviews at the largest firms | PCAOB-BOTICIOWA-2026 |
| 2026-10-07 | PwC says savings "not that drastic yet" after year one | CFODIVE-PWC-2026 |
| 2026-10-13 | AICPA issues practice aid with firm-AI section | AICPA-PA-2026 |
| 2026-12 | QC 1000 takes effect | FOLEY-PCAOB-2026 |
| 2027-06 | IAASB target to present remaining completed guides to the Board | IAASB-TQMPLAN-2026, p. 9 |

### Workforce and role effects

- **Juniors become reviewers.** PwC says new hires will oversee AI performing routine tasks, and training now front-loads skepticism and critical thinking (BI-PWC-2025). Deloitte says professionals will supervise, validate and work alongside AI (DELOITTE-OMNIA-2026).
- **Pyramid pressure.** The Accounting Podcast describes lean senior teams overseeing automated systems (PODWISE-ACCTPOD-2026). ICAEW reports graduate intake cuts and fears of remedial senior work (ICAEW-EXPECT-2026).
- **New governance roles.** System managers, tool owners and oversight committees (FRC-GENAI-2026, p. 38; IFIAR-TTF-2026, p. 7). RSM UK's data analytics director sat on the FRC working group and says the guidance should get system designers talking with frontline auditors (ICAEW-FRCVIEW-2026).
- **Reviewer competence.** The FRC says reviewers need competence in the use case, sometimes specialist expertise (FRC-GENAI-2026, p. 37). The AICPA says teams may need a blend of audit expertise, AI knowledge, data skills and specialist support (AICPA-PA-2026).
- **Time as a quality input.** Botic told firm leaders in January 2026 that teams should know they can take more time even if sign-off is delayed (JOFA-5IMP-2026).
- **Regulator tools.** PCAOB staff describe early AI pilots to support inspection work (STARLING-IMC-2026). Botic backs investment in AI tools in the draft strategic plan (PCAOB-BOTICPLAN-2026).

### Objections and concerns practitioners raise

- **Rubber-stamping and automation bias.** KPMG says empty approval steps give no control value (KPMG-SOX-2026, p. 14). NFRA says fluent output invites automation bias (NFRA-CAALLEY-2026). ICAEW says the FRC covers it in one paragraph (ICAEW-FRCVIEW-2026).
- **Deskilling.** Botic cites research on erosion of critical thinking and skepticism, and calls for new paths to build junior skills (NYSSCPA-BOTIC-2025). Botic's October speech makes critical thinking a core attribute because AI produces more information and more sophisticated analysis (PCAOB-BOTICIOWA-2026).
- **Inspection reform may reduce a behavioural check.** Botic argues the prospect of file review affects partner behaviour, and warns against cutting reviews at the largest firms without a clear case (PCAOB-BOTICIOWA-2026). The Chairman's position is that audit quality is produced by systems, not isolated engagements, and that file reviews continue but may change in number and selection (PCAOB-LOGOUSC-2026).
- **Weakening independent challenge on quality control.** Botic called the rescission of the external quality control function disappointing. The Chairman said an external contractor chosen and paid by the firm may not reliably challenge it (PCAOB-BOTICNEB-2026; PCAOB-LOGOQC-2026).
- **Profit pressure on resourcing.** The PCAOB inspections director said private equity can lead to reduced staffing and fewer specialists, and that inspectors will examine QC at firms that took such investment (CAALLEY-PCAOBPE-2025). Botic also warned private equity may shift incentives so profitability outweighs audit quality (KING-BOTIC-2025).
- **Explainability.** The FRC's McConnon argues the right comparison is a human, not traditional code, so knowing what a tool does conceptually and how it performed in tests is enough for many uses (ICAEW-POD-2025).
- **Guidance thin on vendors and small firms.** ICAEW says the guidance should say more about vendor questions and about firms without technology teams (ICAEW-FRCVIEW-2026).
- **Probabilistic outputs.** RSM UK's analytics director says no tool can guarantee the right output every time (ICAEW-FRCVIEW-2026).
- **Uneven rules.** IAASB participants want global consistency; the IAASB notes risk of regulatory fragmentation (IAASB-TQM-2026, p. 3; IAASB-TQMPLAN-2026, para 11).
- **Documentation burden.** A CalCPA author reports, without verification, that a PCAOB board member warned against demanding every detail of AI model documentation (CALCPA-AISTD-2026).
- **Value not yet visible.** PwC says savings are modest so far (CFODIVE-PWC-2026). A podcast summary attributes a fall in EY's deficiency rates to technology investment; that is the podcast's view and no regulator says so (PODWISE-ACCTPOD-2026).
- **Fees.** Verdantix says responses to KPMG's reported fee argument split between "fees should not fall because humans still verify" and "AI should be repriced as continuous assurance" (VERDANTIX-KPMGFEE-2026).

### Interview probes

1. Walk me through how a new AI tool or use case gets approved for engagement use. Who signs off, what is tested, is the unit of certification the tool or the tool in a use case, what triggers recertification (model or vendor update, new use case), and has a tool ever been pulled?
2. What do you track after go-live: usage, error or false-positive rates, rework, reviewer disagreement? Has any number changed a decision, and does it feed your root-cause analysis and remediation?
3. For work an AI tool produced, what does the reviewer do differently? Do they form their own view first, or read the source? How would you detect rubber-stamping, and does the file show where the reviewer's judgment entered?
4. Now that tools do the first pass, how are juniors learning the craft? What changed in training, rotations and review duties, and what happens in busy season when seniors are reviewing more?
5. What has your regulator asked about AI tools, what did you show, and who owns monitoring of network-level tools? How do you handle clients or fee negotiations that assume fewer junior hours?

---

## 4. Routed to other modules

- **acceptance-independence**
  - Private equity and AI-driven structural change: the PCAOB inspections director's figures and warning that private equity may reduce staffing and specialists (CAALLEY-PCAOBPE-2025); Botic's remarks on firms restructuring around private equity and the single business decision of acceptance (PCAOB-BOTICNEB-2026); the SEC chief accountant's independence review (TR-HOHL-2026; CAQ-HOHLWEBINAR-2026).
  - Fee and junior-hours pressure from clients and the KPMG fee argument (ICAEW-EXPECT-2026; VERDANTIX-KPMGFEE-2026).
  - Client acceptance of AI use in engagement letters (ICAEW-POD-2025), partly covered in use case 15.
- **planning-risk-assessment**
  - ICAEW's test of three chatbots on risk assessment and materiality (ICAEW-PIERPOINT-2025).
  - Audit partners' view that only 6% of largest clients have advanced AI governance, and CAQ's account of audit committees raising AI (CAQ-TRENDS-2026). The CAQ pages differ on how many audit committees raised AI proactively: this page says nearly one quarter, while the landscape file records about two-thirds. Check against the CAQ survey itself.
- **completion-reporting**
  - Audit committee questions on AI: five questions for the auditor (FOLEY-PCAOB-2026).
  - PwC's tool for analysing audit committee communications (CFODIVE-PWC-2026).
- **controls-testing**
  - KPMG's points on human-in-the-loop for AI controls, model drift and prompt injection (KPMG-SOX-2026, p. 14).
- **other-assurance (assurance over AI)**
  - The fragmented, unregulated market for assurance over AI tools, and EY's and Deloitte's AI assurance offerings (ICAEW-POD-2025; EY-CANVAS-2026; DELOITTE-OMNIA-2026).
- **audit firm business model and workforce (cross-cutting lens)**
  - Graduate intake cuts, juniors as reviewers, lean senior teams, small firms building whole audit operations around AI (ICAEW-EXPECT-2026; BI-PWC-2025; PODWISE-ACCTPOD-2026; PCAOB-BOTICNEB-2026).
- **specialists**
  - FRC's point that some AI reviews may need specialist reviewers (FRC-GENAI-2026, p. 37).

---

## 5. Sources

"Access" is `full` for every item below: the page or PDF was opened and read. Items marked "via text mirror" refused `curl` and were read through `r.jina.ai`. Type labels follow the vocabulary.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples | FRC | regulator | https://www.frc.org.uk/documents/9256/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 |
| FRC-GENAINEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 |
| FRC-ATT-2025 | Thematic Review: Certification of Automated Tools and Techniques | FRC | regulator | https://www.frc.org.uk/documents/8383/Thematic_Review_on_the_Certification_of_Automated_Tools_and_Techniques.pdf | 2025-06 |
| FRC-SUPERVISION-2026 | FRC introduces evolved approach to audit supervision | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/frc-introduces-evolved-approach-to-audit-supervision/ | 2026-03-25 |
| IFIAR-TTF-2026 | Use of technology in audits: Innovation and audit quality (2026) (via text mirror; not in the landscape file) | IFIAR | regulator | https://www.ifiar.org/?wpdmdl=19893 | 2026-04-20 |
| IAASB-TQM-2026 | Technology Quality Management Roundtables: Outcomes and Next Steps | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-02/IAASB-Technology-Quality-Management-Roundtables-Feedback.pdf | 2026-02 |
| IAASB-TQMPLAN-2026 | Technology Quality Management Workstream: Action Plan to Develop Non-Authoritative Material (Agenda Item 3-F) | IAASB | standard-setter | https://www.iaasb.org/_flysystem/azure-private/2026-03/0260316-Agenda-Item-3F-Approved-Tech-QM-Action-Plan.pdf | 2026-03 |
| IAASB-TQMPAGE-2026 | Technology Quality Management Workstream (project page with expert group; page is undated, links to minutes posted Sept 2026) | IAASB | standard-setter | https://www.iaasb.org/consultations-projects/technology-quality-management-workstream | 2026 |
| PCAOB-BOTICIOWA-2026 | The Role of the Financial Statement Auditor, and Thoughts on the PCAOB Inspection Process and Its Contemplated Transformation (G. Botic; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/the-role-of-the-financial-statement-auditor--and-thoughts-on-the-pcaob-inspection-process-and-its-contemplated-transformation | 2026-10-05 |
| PCAOB-BOTICSF-2026 | Smaller Audit Engagements, Significant Impact (G. Botic; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/smaller-audit-engagements--significant-impact--audit-quality--investor-protection--and-the-future-of-the-profession | 2026-09-22 |
| PCAOB-BOTICNEB-2026 | Trust in the Markets: Audits, Accountability, and the PCAOB with Reflections on Metrics Disclosures and EQCF (G. Botic; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/trust-in-the-markets--audits--accountability--and-the-pcaob-with-reflections-on-metrics-disclosures-and-eqcf | 2026-09-11 |
| PCAOB-BOTICKU-2026 | Looking to the Future: Moving Forward while Staying on the Right Track (G. Botic, Deloitte/KU Auditing Symposium; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/looking-to-the-future---moving-forward-while-staying-on-the-right-track | 2026-05-08 |
| PCAOB-LOGOQC-2026 | Statement on the Adoption of QC 1000 Amendments (Chairman D. Logothetis; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/statement-on-the-adoption-of-qc-1000-amendments | 2026-09-09 |
| PCAOB-LOGOUSC-2026 | Remarks at the USC SEC Financial Reporting Conference (Chairman D. Logothetis; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/pcaob-chairman-logothetis-delivers-remarks-at-usc-sec-financial-reporting-conference | 2026-06-04 |
| PCAOB-LOGOSEIAG-2026 | Remarks at the Standards and Emerging Issues Advisory Group Meeting (Chairman D. Logothetis; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/chairman-logothetis-delivers-remarks-at-standards-and-emerging-issues-advisory-group-meeting | 2026-05-06 |
| PCAOB-BOTICPLAN-2026 | Statement in Support of Request for Public Comment on the PCAOB's Draft Five-Year Strategic Plan (2026-2030) (G. Botic; via text mirror) | PCAOB | regulator | https://pcaobus.org/news-events/speeches/speech-detail/statement-in-support-of-request-for-public-comment-on-the-pcaob-s-draft-five-year-strategic-plan-(2026-2030) | 2026-07-20 |
| KPMG-HOHL-2026 | Q&A with Kurt Hohl, SEC chief accountant | KPMG | firm | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | 2026-05-27 |
| TR-HOHL-2026 | SEC Chief Accountant Hohl dispels rumors of weakening auditor independence rules | Thomson Reuters Checkpoint | press | https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/ | 2026-06-05 |
| CAQ-HOHLWEBINAR-2026 | Conversation with SEC Leaders: 5 Takeaways for the Public Company Audit Profession (recaps the 13 July 2026 webinar) | CAQ | professional-body | https://www.thecaq.org/aia-conversation-with-sec-leaders-5-takeaways | 2026-07-23 |
| NFRA-CAALLEY-2026 | AI cannot replace auditor judgement, flags automation bias in audits: NFRA | CAalley (citing The Business Standard) | press | https://caalley.com/news-updates/indian-news/ai-cannot-replace-auditor-judgement-flags-automation-bias-in-audits-nfra | 2026-07-24 |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| BOARDAGENDA-FRC-2026 | Auditors warned they remain accountable despite use of AI | Board Agenda | press | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | 2026-03-31 |
| BOARDAGENDA-SUP-2026 | FRC unveils details of audit regulation changes | Board Agenda | press | https://boardagenda.com/2026/03/26/frc-unveils-details-of-audit-regulation-changes/ | 2026-03-26 |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://www.accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 |
| NYSSCPA-BOTIC-2025 | PCAOB's Botic Flags Opportunities and Risks in AI (summarising Accounting Today) | NYSSCPA | professional-body | https://nysscpa.org/news/1051584-pcaobs-botic-flags-opportunities-and-risks-in-ai-2025-12-10 | 2025-12-10 |
| KING-BOTIC-2025 | PCAOB Acting Chair Botic Delivers Remarks at the AICPA Conference | King & Spalding | firm | https://www.kslaw.com/blog-posts/pcaob-acting-chair-botic-delivers-remarks-at-the-aicpa-conference | 2025-12-12 |
| JOFA-5IMP-2026 | 5 imperatives for auditors from the PCAOB chair | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/jan/5-imperatives-for-auditors-from-the-pcaob-chair/ | 2026-01-12 |
| CAALLEY-PCAOBPE-2025 | PCAOB warns auditors about AI and PE (citing Accounting Today) | CAalley | press | https://caalley.com/news-updates/international-news/pcaob-warns-auditors-about-ai-and-pe | 2025-12-09 |
| DART-SECPCAOB-2025 | Heads Up: Highlights of the 2025 AICPA & CIMA Conference on Current SEC and PCAOB Developments | Deloitte DART | conference | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways | 2025-12-12 |
| FOLEY-PCAOB-2026 | What Directors Should be Asking About the Audit and the Auditors Now (via text mirror) | Foley & Lardner | firm | https://www.foley.com/insights/publications/2026/07/what-directors-should-be-asking-about-the-audit-and-the-auditors-now/ | 2026-07-02 |
| ICAEW-FRCVIEW-2026 | How helpful is FRC's guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05-06 |
| ICAEW-EXPECT-2026 | Are businesses expecting too much of AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/feb-2026/are-businesses-expecting-too-much-of-ai | 2026-02-03 |
| ICAEW-LANDMARK-2025 | FRC publishes landmark guidance on the uses of AI for audit | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/jul-2025/frc-publishes-landmark-guidance-on-the-uses-of-ai-for-audit | 2025-07-08 |
| ICAEW-PIERPOINT-2025 | Testing Gen AI platforms: can they do audit work? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09-24 |
| ICAEW-POD-2025 | How should audit firms use AI? (Beyond Finance podcast; transcript read; recorded 7 Nov 2025) | ICAEW | podcast | https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai | 2025-11-11 |
| CAQ-RSM-2026 | Shaping the future of assurance: Advancing AI in the audit (T. Merkel, RSM) | CAQ | professional-body | https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit | 2026-08-25 |
| RSM-LUCA-2026 | RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit | RSM US | firm | https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html | 2026-01-08 |
| CPAPA-LUCA-2026 | RSM US Rolls Out 'Ask Luca' GenAI Tool for Firm's Auditors | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/01/09/rsm-us-rolls-out-ask-luca-genai-tool-for-firms-auditors/176104/ | 2026-01-09 |
| STARLING-IMC-2026 | Modernizing US PCAOB Audit Inspections | Starling Insights | press | https://insights.starlingtrust.com/content/observations/modernizing-us-pcaob-audit-inspections | 2026-09-01 |
| CAQ-INSIDER-2026 | Audit Insider, July/August 2026 | CAQ | professional-body | https://www.thecaq.org/audit-insider-july-august-2026 | 2026-09-01 |
| TR-PCAOBPREVIEW-2026 | PCAOB set to consider draft strategic plan as stakeholders push competing priorities | Thomson Reuters Checkpoint | press | https://tax.thomsonreuters.com/news/pcaob-set-to-consider-draft-strategic-plan-as-stakeholders-push-competing-priorities/ | 2026-07-16 |
| JOFA-IMC-2026 | PCAOB works to form Inspections Modernization Council | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/may/pcaob-works-to-form-inspections-modernization-council/ | 2026-05-29 |
| CAQ-TRENDS-2026 | Three Trends Shaping Business Strategy in 2026: Insights from Audit Partners (Spring 2026 Audit Partner Pulse) | CAQ | survey | https://www.thecaq.org/aia-three-trends-shaping-business-strategy-in-2026-insights-from-audit-partners | 2026-07-21 |
| BI-PWC-2025 | PwC is training junior accountants to be like managers, because AI is going to be doing the entry-level work | Business Insider via Yahoo Finance | press | https://finance.yahoo.com/news/pwc-training-junior-accountants-managers-170001522.html | 2025-08-08 |
| DELOITTE-OMNIA-2026 | Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 |
| EY-CANVAS-2026 | EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 |
| KPMG-SOX-2026 | The Future of SOX: A point of view for 2030 and beyond | KPMG | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf | 2026-09-24 |
| BAKERTILLY-GAM-2026 | Strategy in motion: Internal audit's 2026 execution mandate (IIA GAM 2026 takeaways) | Baker Tilly | firm | https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate | 2026-04-10 |
| FIELDGUIDE-PCAOB-2026 | PCAOB AI oversight: where the Board stands on AI in audit | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/pcaob-ai-audit-standards | 2026-08-06 |
| CALCPA-AISTD-2026 | AI Standard Setting, Regulation in Audit: Part 1 | CalCPA | professional-body | https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1 | 2026-08-12 |
| VERDANTIX-KPMGFEE-2026 | What Goes Around Comes Around: KPMG's AI-Driven Fee Argument Raises Uncomfortable Questions About Audit Pricing Models | Verdantix | press | https://www.verdantix.com/venture/blog/what-goes-around-comes-around--kpmg-s-ai-driven-fee-argument-raises-uncomfortable-questions-about-audit-pricing-models | 2026-02-10 |
| PODWISE-ACCTPOD-2026 | The Accounting Podcast, 1 Oct 2026 and 25 Sep 2026 episodes (AI-generated Podwise summaries; audio not heard) | The Accounting Podcast via Podwise | podcast | https://podwise.ai/episodes/9035550 ; https://podwise.ai/episodes/8995231 | 2026-10-01 |
| KOSMYNA-2025 | Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task | arXiv (MIT Media Lab authors) | academic | https://arxiv.org/abs/2506.08872 | 2025-06-10 |
| KU-SYMPOSIUM-2026 | 2026 Deloitte/University of Kansas Auditing Symposium agenda ("The Future of Auditing", 7-9 May 2026; agenda only, no session content) | University of Kansas School of Business | conference | https://business.ku.edu/deloitte-ku-auditing-symposium | 2026-05-08 |
| AAA-MIDYEAR-2026 | 2026 Auditing Section Midyear Meeting: Excellence in Auditing Education workshop (15-17 Jan 2026; agenda only) | American Accounting Association | conference | https://aaahq.org/Meetings/2026/Auditing-Section-Midyear-Meeting/Workshop | 2026-01-15 |

**Source count by type (57 refs):** regulator 13 · press 13 · professional-body 12 · firm 7 · standard-setter 4 · conference 3 · podcast 2 · survey 1 · vendor 1 · academic 1. No community or job-posting source was found (see section 6).

Two agenda-only pages (KU-SYMPOSIUM-2026, AAA-MIDYEAR-2026) and the AI-generated podcast summary (PODWISE-ACCTPOD-2026) carry little content; they are listed because they show where the discourse is happening, and the use cases do not rely on them except where cited.

---

## 6. Gaps

- **Quality evidence:** No source gives error rates, false-pass rates, reviewer override or disagreement rates, parallel-run results or an independent measure of whether AI tools or AI review change audit quality. IFIAR names metrics but gives no values. The FRC found none quantified. The deficiency-rate fall (26% to 13%) has no stated link to AI.
- **Inspection findings on AI:** No PCAOB or FRC inspection finding specific to firms' AI tools was found. The CalCPA article claims recent inspection reports contain AI-related deficiencies in journal-entry testing; I could not verify this and did not use it as evidence. The same limit applies to its report of a board member's warning about over-documenting models.
- **Not reached or blocked:**
  - Big Four and other firm transparency reports (the web-search quota ran out before these were searched; no URL was known).
  - The FRC's 2026 audit quality annual review.
  - The Swedish junior-auditor study (University of Gothenburg): seen only in a search snippet; the repository showed an anti-bot page.
  - MindBridge's comment letter to the PCAOB (403 to `curl`).
  - The amended QC 1000 text and the PCAOB QC 1000 Q&A resource (the PCAOB news-release page returned 403; only speeches were read).
  - The staff IMC discussion materials themselves, which I know only through Starling Insights and Botic's speech.
  - NFRA's own paper, known through a secondary article.
  - The AICPA practice aid's full text (login).
  - Thomson Reuters Institute's *Future of Professionals 2026* (no URL known).
  - Reddit, LinkedIn and professional forums.
- **Primary text not read for two quotations:** The December 2025 Botic and Gunia remarks are quoted through press summaries (Accounting Today via NYSSCPA and CAalley, and King & Spalding). The PCAOB's own page for the Botic speech was not found.
- **Conference content:** Only agendas were read for the KU/Deloitte symposium and the AAA midyear workshop, so what panellists said about review and training is not available. Recordings of the IAASB roundtables are not public. The IAASB summary is the only record. The IAASB webinars on audit-evidence proposals and the ICAEW Audit & Assurance Conference were not covered.
- **Podcasts:** *The Accounting Podcast* was read only through AI-generated summaries on Podwise, which also credit EY's lower deficiency rates to agentic AI investment; I did not hear the audio and treat this as the podcast's claim.
- **Community and job postings:** None found. No job posting for AI quality, AI governance or tool-certification roles at audit firms was located, so the structure of firms' AI quality teams is described only from regulator and firm statements.
- **Engagement quality review:** No source describes how engagement quality reviewers handle AI-assisted work. Treat EQR as an open question for interviews.
- **Data conflicts to resolve:**
  - The CAQ pulse on whether audit committees proactively raised AI: "nearly one quarter" on the CAQ trends page, against "about two-thirds" in the landscape file.
  - Whether the PCAOB board's AI governance lifecycle view (Botic) reflects any staff or Board position; it was presented as his own.
  - The effective date of QC 1000 is given as December 2026 (Foley) and 15 December 2026 (landscape); the date was not confirmed on a PCAOB page.
- **Not in the landscape file:** The IFIAR April 2026 report and the IAASB action plan are new relative to the landscape scan (the landscape records the IFIAR 2025 report and the roundtable summary). The landscape's leads on the FRC sandbox, IFIAR's survey of inspection findings (April 2026) and the CPA.com benchmark were not re-opened here.
