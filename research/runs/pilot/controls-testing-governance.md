# Module deep dive: assurance / controls-testing — angle: governance & evidence

- **Archetype:** assurance
- **Module:** controls-testing. Testing the design and operating effectiveness of internal controls in external audits (ICFR/SOX 404 integrated audits, tests of controls under ISA 330 and PCAOB AS 2201/AS 2301), in internal audit and SOX/ICFR programs, and in SOC 1/SOC 2 examinations. Covers walkthroughs, ITGC and application controls testing, sampling, evidence gathering and tick-marking, deficiency evaluation and documentation.
- **Angle:** governance & evidence. What constrains and measures AI use in controls testing: regulators and standard-setters, inspection findings, professional-body guidance, academic studies and surveys.
- **Prepared:** 2026-10-16
- **Method note:** Unlike the landscape scan, this deep dive opened and read primary documents directly (curl through the session proxy; WebFetch itself failed on DNS). About 65 sources were opened and read, either in full or, for long PDFs, through their relevant sections. About 8 more were seen only as search results. Those are marked "(search result only)" in §4. Some hosts refused automated access (pcaobus.org HTML pages, gartner.com, sec.gov file paths, SSRN, businesswire.com, goingconcern.com, wolterskluwer.com). Workarounds are noted in §5. Source refs (S01…) point to §4.

---

## 1. Summary

**What the rules say now (October 2026).** No regulator or standard-setter prohibits AI in controls testing, and none has issued AI-specific requirements. Every body read here takes the same position: existing evidence and quality-management standards apply, the human auditor stays accountable, and firms must certify, monitor and supervise their tools. The positions differ in how much detail they give.

- **FRC (UK).** The most operational text is the FRC's *Generative and Agentic AI Guidance* (30 Mar 2026). It gives a three-part risk taxonomy: deficient output, misuse of output, and non-compliant methodology. It names five LLM output failures. It sets four mitigation families: system design, certification, staff education, and human-in-the-loop review/oversight at "control points". It explicitly warns that population-level AI outputs can be less conclusive per item than traditional work, so a methodology must not overstate their persuasiveness (S01).
- **IAASB.** The Audit Evidence & Risk Response exposure drafts (5 Aug 2026; comments due 15 Dec 2026) are the most consequential pending change for controls testing. ED-330 would:
  - permit a "tests of controls alone" response, but only where inherent risk is not at the higher end, the risk is not significant, and controls reduce risk to an acceptably low level
  - clarify how indirect controls, including GITCs, are treated
  - add application material (A59, A62–A63) on how emerging technologies affect the auditor's view of whether automated controls operate consistently
  - replace "automated tools and techniques" with "technological tools" and add a technology appendix to ED-500 (S21–S23).
- **PCAOB.** The technology-assisted analysis amendments are in force for fiscal years beginning on or after 15 Dec 2025. They stress that ITGCs and automated application controls matter to the reliability of electronic information, but they expressly do not cover AI (S06). The PCAOB is consulting on AI through its 2026 strategic-plan and standard-setting requests (S19, S20, S32).
- **US guidance.** AICPA practice aid (13 Oct 2026) (S27, S28); TQA 9561 on AI in SOC 1/SOC 2 examinations (11 Sep 2026) (S48); COSO's GenAI internal-control publication (23 Feb 2026), which sets ICFR-grade evidence for AI that management relies on (prompt, configuration and model version, sampling rationale) (S25).

**What inspections show.**
- Internal control testing remains the largest single source of engagement-level findings at the six largest networks. In 2025 it produced 213 findings in listed-PIE audits, ahead of accounting estimates at 166. 14% of listed-PIE audits where the area was inspected had at least one finding (S09).
- The specific failures are the ones AI tools aim at: insufficient evidence for reliance on manual controls (69 findings), insufficient testing of IPE/data (43) and insufficient ITGC testing (39) (S09).
- 31% of IFIAR members reported findings that an automated tool "was not used as intended", mostly misread outputs and thin follow-up of outliers (2024 survey) (S10).
- Regulators see ATTs used in controls testing far less often than in journal-entry testing: 43% of IFIAR members observed them "frequently" in controls testing, against 88% for JE testing (S10).

**What is measured.**
- Named, measured controls-testing outcomes are still self-reported or vendor-reported:
  - Microsoft's ITGC change-management agent: 850 hours and $185K a year (S53, S54)
  - Reddit's internal audit: 175 controls automated, over 40% of SOX scope, about 60% less testing time per control in three months (S55).
- No regulator, academic study or independent benchmark has yet measured the *quality* effect of AI-performed tests of controls.
- Academic evidence is mostly about the human side: automation bias reduces skepticism toward tool output (S63), algorithm aversion appears in estimates (S61), and GenAI may erode motivation and judgment (proposal, S64). The one controls-specific prototype study found that LLM agents interpret controls and evidence well, but sufficiency judgments needed auditor correction (S66).

**Two most important insights.**
1. **The binding constraint is moving from "may we use AI?" to "what evidence does an AI-performed control test produce, and how persuasive is it?"** Three sources are converging on the same evidentiary answer:
   - The FRC asks firms not to overstate the persuasiveness of population-level AI outputs (S01).
   - COSO defines when management "relies" on AI and what evidence that triggers (S25).
   - IAASB ED-500 requires auditors to evaluate (not just consider) the relevance and reliability of information (S23).

   The answer they share: logged prompts, model versions and configurations, risk-calibrated human checkpoints, and certification per use case.
2. **A two-sided reliance question is opening, and current standards do not answer it.** Auditors are starting to test controls *performed by* AI at clients. COSO, TQA 9561 and KPMG expect the first AI-related material weaknesses around 2027 (S25, S48, S49). Meanwhile, management and internal audit increasingly test controls *with* AI. The IIA told the PCAOB that AS 2605, the standard on using internal audit's work, has no framework for technology-generated internal-audit evidence (S32). KPMG argues that external-auditor reliance on management's testing could fall or rise depending on whose AI tools are better (S49). Firms should expect regulator attention on both sides, alongside a new risk: control evidence manipulated against AI testers, such as fabricated documents or hidden prompt instructions (S11, S15, S49).

---

## 2. Use cases

```yaml
- id: assurance-controls-testing-01
  title: GenAI walkthrough assistant that drafts process and control documentation from prior-year files
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ document-production, review-assurance ]
  pattern: draft-review-loop
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Walkthroughs and understanding-of-controls documentation are tedious, repeated every year, and depend on reconciling prior-year narratives with current-year changes."
  solution: "PwC's Advanced Walkthrough Assistant ingests prior-year walkthroughs and current-year documents, generates a tailored work plan, flags what is missing or changed, and drafts control and risk documentation for auditor review. PwC said it is used on 2026 year-end audits."
  outcomes:
    - { lever: speed, description: "PwC reports time savings are real but 'not that drastic yet'; busy-season compression has been modest", figure: "no published figure", source_ref: S58 }
  prerequisites: [ "Prior-year walkthrough files in machine-readable form", "Firm-certified tool and methodology integration (ISQM 1 / QC 1000 technological resources)" ]
  risks_and_guardrails:
    - "FRC: an AI tool asked to evaluate controls one by one, then aggregate them, may miss shared weaknesses and overstate control-environment effectiveness. Task specification is a risk source (S01)"
    - "Misinterpretation risk: a draft narrative read as a complete understanding of the process (S01)"
  human_checkpoints: [ "Auditor still performs the walkthrough inquiry/observation and approves the documented understanding" ]
  role_evolution: "Junior staff move from transcribing narratives to verifying AI-drafted narratives against the walkthrough; reviewers check what changed versus prior year."
  evidence_grade: B
  sources:
    - { ref: S57, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28 }
    - { ref: S58, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07 }
    - { ref: S01, title: "Generative and Agentic AI Guidance: risks, mitigations and illustrative examples", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30 }
  last_reviewed: 2026-10-16
  notes: "The CFO Dive date is taken from page metadata. KPMG also describes agents that schedule, transcribe and document walkthroughs (S50), but gives no named deployment."

- id: assurance-controls-testing-02
  title: Two-agent ITGC change-management test (attribute extraction plus tick-marking against source tickets)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance, document-production ]
  pattern: full-population-testing
  lens: automate
  ladder: automate
  runtime_class: workflow-automation
  maturity: in-production
  problem: "SOX change-management testing requires auditors to open tickets across inconsistent ticketing systems, extract tester/approver/dates, check sequencing against deployment, annotate evidence and reconcile to spreadsheets for every sample."
  solution: "Microsoft Internal Audit built two Copilot Studio agents. One extracts required attributes from ticket data and pre-populates rule-based pass/fail logic in a standard table. The other applies visual tick-marks on the source evidence, showing where each attribute was validated."
  outcomes:
    - { lever: capacity, description: "Annual time saved on SOX change-management testing (self-reported)", figure: "850 hours/year", source_ref: S53 }
    - { lever: cost, description: "Annual cost saved (self-reported)", figure: "$185K/year", source_ref: S53 }
    - { lever: speed, description: "Time to build", figure: "launched in 1-3 months", source_ref: S53 }
  prerequisites: [ "Ticket data accessible to the agent", "Rule-based attribute criteria agreed with control owners and external auditor", "IPE/completeness of ticket population established" ]
  risks_and_guardrails:
    - "IFIAR: ITGC testing remains a recurring inspection finding (39 listed-PIE findings in 2025) (S09)"
    - "AFM: auditors often give insufficient attention to ineffective GITCs when concluding that tool input data are reliable (S14)"
    - "Rule-based pass/fail logic must itself be validated, in line with FRC's use of output schemas and deterministic rules alongside LLMs (S01)"
  human_checkpoints: [ "Auditor reviews exceptions and judgment-based deviations", "Reviewer samples the tick-marked evidence" ]
  role_evolution: "Testers shift from evidence handling to exception analysis; IT audit specialists own attribute rules."
  evidence_grade: A
  sources:
    - { ref: S53, title: "Microsoft Frontier Finance Innovation Story: SOX Change Management Testing Agent", publisher: Microsoft, type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf", date: 2026 (FY26) }
    - { ref: S54, title: "AI solution overviews: Internal Audit", publisher: Microsoft, type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: 2026 (FY26) }
  last_reviewed: 2026-10-16
  notes: "Resolves the landscape's 850-hour vs 50-hour conflict. The rendered PDF (S54, page 2) reads 850 hours. The '50 hours' came from a text extraction that drops glyphs. The figures are self-reported by the operating company."

- id: assurance-controls-testing-03
  title: Autonomous attribute testing across a large share of a SOX control population
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: full-population-testing
  lens: delegate
  ladder: delegate
  runtime_class: background-agent
  maturity: in-production
  problem: "SOX testing hours per control keep rising: KPMG's 2025 survey shows 12 hours in FY2022 and 16 hours in FY2024. Most of the effort sits in evidence review and documentation."
  solution: "Optro Autonomous Testing agents execute test steps against submitted evidence for many controls and log cited reasoning. People review conclusions. Reddit's internal audit team and Klaviyo are named users."
  outcomes:
    - { lever: capacity, description: "Controls automated in first three months (vendor-reported)", figure: "175 controls; >40% of SOX scope", source_ref: S55 }
    - { lever: speed, description: "Testing time per control (vendor-reported)", figure: "-60%", source_ref: S55 }
  prerequisites: [ "Standardised evidence repositories", "Test scripts approved per control", "External auditor engaged before reliance on management testing" ]
  risks_and_guardrails:
    - "KPMG: control owners aware of AI testers may hide instructions in evidence to steer the agent (prompt injection) (S49)"
    - "Zanin: a model that is right 95% of the time is useless if you cannot tell which 5% to check (S59)"
    - "COSO: where management relies on AI output, ICFR-grade evidence is needed: documented prompt, configuration and model version; sampling rationale (S25)"
  human_checkpoints: [ "Auditor approves the test plan before execution", "Reviewer signs off conclusions and every exception" ]
  role_evolution: "Internal audit staff become reviewers and exception handlers; the ratio of reviewers to preparers rises."
  evidence_grade: A
  sources:
    - { ref: S55, title: "Optro launches domain-trained agents for audit, compliance, third-party risk and AI governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14 }
    - { ref: S49, title: "The Future of SOX: a point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
    - { ref: S59, title: "5 Questions to Ask Before Your SOX Team Adopts AI Agents", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188703", date: 2026-08-18 }
  last_reviewed: 2026-10-16
  notes: "Graded A because a named organisation and a measured outcome are published, but the measurement is vendor-reported and covers effort, not test quality."

- id: assurance-controls-testing-04
  title: Agentic control-testing platform delivered by an audit/advisory firm (evidence-to-sample assignment with traceable annotations)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance, document-production ]
  pattern: document-to-decision
  lens: delegate
  ladder: delegate
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Co-sourced and outsourced SOX/IA testing is labour-intensive. Unstructured evidence of every file type has to be read, matched to samples, and documented with traceability."
  solution: "RSM US integrated Andera's agents into its audit platform (RSM Beacon). The agent reviews evidence of any file type, runs directed test steps, and produces annotated documentation traceable to source. PwC says its controls-testing automation will work like Evidence Match, its agent-led module that matches evidence to documents for high-volume areas."
  outcomes:
    - { lever: capacity, description: "Broader testing coverage and faster cycles claimed; no figures published", figure: "none", source_ref: S56 }
  prerequisites: [ "Firm certification of a third-party agent (FRC thematic: third-party components may not be open to logic review, so output testing carries more weight)", "Client data-sharing and confidentiality terms" ]
  risks_and_guardrails:
    - "FRC 2025 thematic: firms were still updating certification processes for AI-specific risks; only two of six firms recorded tool limitations in certification templates (S03)"
    - "NFRA: do not rely on vendor accuracy claims without independent evaluation (S17)"
  human_checkpoints: [ "Engagement team approves directed test steps", "Open items flagged to people for resolution" ]
  role_evolution: "Advisory staff manage agent runs and resolve open items; firms sell testing capacity as a platform plus review service."
  evidence_grade: B
  sources:
    - { ref: S56, title: "Andera and RSM US partner to create AI-enabled control testing platform for internal audit", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/", date: 2026-08-26 }
    - { ref: S57, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28 }
    - { ref: S03, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: Financial Reporting Council, type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-05
  title: Year-round (continuous) control testing instead of a single point-in-time cycle
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance, coordination-scheduling ]
  pattern: monitor-diagnose-act
  lens: reinvent
  ladder: automate
  runtime_class: background-agent
  maturity: in-production
  problem: "Testing bunched at interim and year-end surfaces deficiencies late, leaving little time to remediate before the assessment date."
  solution: "Agents test controls throughout the year as evidence arrives. Klaviyo's internal audit says it no longer bundles testing into one point in time. KPMG and Grant Thornton position continuous testing as the target SOX model."
  outcomes:
    - { lever: risk, description: "Earlier detection and remediation with control owners (named user, no figure)", figure: "none", source_ref: S55 }
  prerequisites: [ "Automated evidence collection embedded in workflows (KPMG: may give faster ROI than automated testing itself)", "Monitoring of model drift and configuration changes" ]
  risks_and_guardrails:
    - "Grant Thornton: external auditors and regulators have not given blanket approval for AI-driven SOX compliance (S52)"
    - "KPMG: model drift can make an effective control ineffective with no visible system change (S49)"
  human_checkpoints: [ "Quarterly human review of exceptions and of agent configuration changes" ]
  role_evolution: "The ICFR function shifts from cycle-based testers to monitors of a running control-health view."
  evidence_grade: B
  sources:
    - { ref: S55, title: "Optro launches domain-trained agents...", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: 2026-10-14 }
    - { ref: S49, title: "The Future of SOX: a point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
    - { ref: S52, title: "The power of AI in efficient SOX compliance", publisher: Grant Thornton, type: firm, url: "https://www.grantthornton.com/insights/articles/advisory/2025/the-power-of-ai-in-efficient-sox-compliance", date: 2026-07-21 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-06
  title: Full-population tests of controls replacing attribute sampling
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance, data-reporting ]
  pattern: full-population-testing
  lens: reinvent
  ladder: automate
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Sample-based tests (e.g., 25 items) leave the conclusion limited to the items examined; sampling findings recur in inspections."
  solution: "AI and analytics examine every in-scope transaction or control instance. KPMG calls this one of the biggest methodology advances since computerised accounting. Gartner says more mature internal audit teams are moving from samples to full populations."
  outcomes:
    - { lever: quality, description: "IFIAR records 24 'insufficient sample' findings and 11 'biased/non-representative sample' findings in 2025 listed-PIE inspections, the failure mode that full-population testing addresses", figure: "24 and 11 findings (2025)", source_ref: S09 }
  prerequisites: [ "Reliable, complete populations (IPE and ITGC reliance)", "Methodology that states how much evidence a population-level AI output provides" ]
  risks_and_guardrails:
    - "FRC: population-level AI outputs can be less conclusive per item; the methodology must not overstate their persuasiveness (S01)"
    - "NFRA: full-population testing through a tool does not remove the need for risk assessment; periodically test a tool's 'low-risk' classifications (S17)"
    - "PCAOB AS 1105/2301 amendments: items flagged in a test of details must be investigated; a procedure used for more than one purpose must meet each objective (S06)"
  human_checkpoints: [ "Auditor investigates every flagged item or a justified subset", "Engagement partner approves the evidential weight assigned" ]
  role_evolution: "Sampling expertise gives way to population-integrity and exception-investigation skills."
  evidence_grade: C
  sources:
    - { ref: S49, title: "The Future of SOX", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
    - { ref: S45, title: "Audit teams' AI use common but most lack strategy (Gartner poll)", publisher: Accounting Times, type: press, url: "https://www.accountingtimes.com.au/profession/audit-teams-ai-use-common-but-most-lack-strategy", date: 2026-08 }
    - { ref: S01, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30 }
    - { ref: S17, title: "NFRA sets 10 principles for technology use in audits", publisher: CAalley, type: press, url: "https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement", date: 2026-07-24 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-07
  title: AI risk-scored sample and coverage selection
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ data-reporting, expert-judgment ]
  pattern: intake-triage
  lens: improve
  ladder: augment
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Selection driven by static lists and judgment is slow and hard to explain or defend."
  solution: "Microsoft Internal Audit's Sample Selection Agent scores items on revenue, discounts, country risk and control indicators. The FRC's contract-review example shows a tool that scores contracts and samples those above a threshold, with the risk indicators visible to the auditor."
  outcomes:
    - { lever: capacity, description: "Annual hours saved; weeks of analysis cut to a day (self-reported)", figure: "2K hours/year", source_ref: S54 }
  prerequisites: [ "Documented scoring logic and threshold", "Audit file shows which items were selected and why" ]
  risks_and_guardrails:
    - "IFIAR: biased or non-representative samples remain a finding category (11 in 2025) (S09)"
    - "FRC: document that an AI tool selected the sample, the criteria for appropriate use, the indicators each item showed, and the testing performed (S01)"
  human_checkpoints: [ "Auditor approves the threshold and any untested residual population" ]
  role_evolution: "Planning time moves from building selections to challenging the risk model."
  evidence_grade: A
  sources:
    - { ref: S54, title: "AI solution overviews: Internal Audit", publisher: Microsoft, type: firm, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf", date: 2026 (FY26) }
    - { ref: S01, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30 }
  last_reviewed: 2026-10-16
  notes: "Microsoft's agent supports internal-audit coverage across audits, not only SOX. The PCAOB found all US global network firms already use tools to select samples (2023 inspection year, S06)."

- id: assurance-controls-testing-08
  title: Agent-assisted evidence requests (PBC) and automated evidence collection
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ coordination-scheduling, client-interaction ]
  pattern: intake-triage
  lens: improve
  ladder: augment
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Back-and-forth over evidence requests delays testing; one practitioner estimates about one in five PBC requests come back wrong the first time."
  solution: "Agents help control owners clarify requests and close gaps before submission, or pull evidence from systems and repositories. KPMG argues automated evidence collection may give faster ROI than automated testing."
  outcomes:
    - { lever: speed, description: "Less evidence follow-up claimed (vendor)", figure: "none", source_ref: S55 }
  prerequisites: [ "Evidence stored in standardised repositories or source systems" ]
  risks_and_guardrails:
    - "AICPA Peer Review Board: over-reliance on third-party compliance platforms that yield identical risk assessments, samples and tests across SOC 2 clients makes engagements 'nonconforming' (S30)"
    - "Evidence authenticity: AI-fabricated documents (S15, S36)"
  human_checkpoints: [ "Auditor determines sufficiency; the platform does not decide what evidence is enough" ]
  role_evolution: "Seniors spend less time chasing PBC lists."
  evidence_grade: C
  sources:
    - { ref: S49, title: "The Future of SOX", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
    - { ref: S59, title: "5 Questions to Ask Before Your SOX Team Adopts AI Agents", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188703", date: 2026-08-18 }
    - { ref: S30, title: "AICPA guides peer reviewers to address SOC 2 risks", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks.html", date: 2026-05-14 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-09
  title: Testing management's controls over GenAI used in financial reporting (AI-enabled controls as an ICFR test object)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  lens: reinvent
  ladder: assist
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Clients use GenAI for matching, reconciliations, postings and review controls. Auditors need to decide whether management 'relies' on AI output and what to test: prompts, thresholds, model versions, logs, overrides."
  solution: "COSO maps GenAI risks to the 17 principles and eight capability types (ingestion through human-AI interaction). It defines reliance and non-reliance, and supplies control-testing templates and metrics. The AICPA practice aid Part 1 helps auditors understand AI-affected controls. EY reports an in-house framework for when AI is in use at audit clients."
  outcomes:
    - { lever: risk, description: "KPMG expects the first wave of AI-related material weaknesses in 2027, as SOX programs stop testing 'around' AI", figure: "forecast", source_ref: S49 }
  prerequisites: [ "Client AI use-case inventory mapped to processes, assertions and key controls (COSO)", "ITGCs extended to prompts, thresholds and retrieval corpora (change control)" ]
  risks_and_guardrails:
    - "COSO: where reliance exists, require documented prompt/config/model version, sampling rationale and evidence retention (S25)"
    - "Segregation of duties: separate who configures AI from who approves its outputs (S25)"
    - "KPMG: a human approval step that rubber-stamps AI output is not a control (S49)"
  human_checkpoints: [ "Auditor's reliance decision on AI-dependent controls", "Specialist involvement for model validation evidence" ]
  role_evolution: "IT audit specialists add model governance, drift monitoring and prompt change control to ITGC scope."
  evidence_grade: C
  sources:
    - { ref: S25, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://www.coso.org/generative-ai", date: 2026-02-23 }
    - { ref: S27, title: "AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing", publisher: AICPA & CIMA, type: professional-body, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13 }
    - { ref: S31, title: "A new frontier: CPAs as AI system evaluators", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/nov/a-new-frontier-cpas-as-ai-system-evaluators/", date: 2025-11 }
    - { ref: S49, title: "The Future of SOX", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': the auditor tests an AI system's control behaviour (configuration, thresholds, logs), not an AI-performed test. A Kokina et al. (2025) field study found complex AI not yet in clients' financial reporting (S65); usage is still early."

- id: assurance-controls-testing-10
  title: SOC 1/SOC 2 scoping and testing of AI used inside service organisations
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: other
  lens: improve
  ladder: assist
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Service organisations embed AI in the services delivered to user entities. Before September 2026 no AICPA guidance existed, and service auditors improvised evidence requests."
  solution: "TQA 9561 says AI creates no separate SOC model or criteria. Scope follows whether AI affects in-scope services, systems and controls. The SOC 1 description must disclose the nature of AI that is relevant to user entities' ICFR, and third-party AI providers are analysed as subservice organisations (inclusive or carve-out). CSA reports auditors requesting evidence on model lineage, prompt/inference logging, drift monitoring and AI subprocessors."
  outcomes:
    - { lever: risk, description: "No measured outcome; guidance only", figure: "none", source_ref: S48 }
  prerequisites: [ "AI inventory against the system boundary", "Updated subservice-organisation roster and CSOCs" ]
  risks_and_guardrails:
    - "Avoid scope inflation: productivity AI outside the system boundary stays out (S48)"
    - "CSA: a clean SOC 2 Type II can carry zero tested controls on model accuracy or drift, because the TSC do not require them (S47)"
    - "Processing-integrity commitments make AI output validation and error correction directly relevant (S48)"
  human_checkpoints: [ "Service auditor's scoping judgment and description-criteria evaluation" ]
  role_evolution: "SOC teams need AI-literate IT auditors; CSA promotes its AI Controls Matrix and STAR for AI as interim baselines."
  evidence_grade: C
  sources:
    - { ref: S48, title: "AI in SOC Examinations: What the AICPA's New TQA Section 9561 Means for Service Organizations", publisher: Schneider Downs, type: firm, url: "https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/", date: 2026-09-30 }
    - { ref: S47, title: "The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted", publisher: Cloud Security Alliance, type: professional-body, url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/", date: 2026-08-30 }
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': scoping and testing an AI component of a system under examination. TQA 9561 issue date (11 Sep 2026) as reported by Schneider Downs; the AICPA text itself was not read."

- id: assurance-controls-testing-11
  title: GenAI in the SOC examination workflow (evidence collection, system-description updates, responses to deviations)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ document-production, coordination-scheduling ]
  pattern: draft-review-loop
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "SOC programs carry heavy documentation: Section 3 system descriptions, evidence gathering, and management responses to deviations."
  solution: "Live polling at EY's 14th SOC conference found AI used to support evidence collection, update Section 3 descriptions, draft management responses to deviations and manage projects. Speakers also list control-framework mapping against the TSC and continuous evidence snapshots."
  outcomes:
    - { lever: capacity, description: "Share of conference participants using AI for each task (live poll, not a random sample)", figure: "evidence collection 63%; Section 3 45%; deviation responses 41%; project management 29%", source_ref: S46 }
  prerequisites: [ "Approved enterprise AI tools; confidentiality controls over client evidence" ]
  risks_and_guardrails:
    - "EY speakers: AI may invent details and fill blanks even when told not to; agents may change behaviour to work around anomalies (S46)"
    - "Peer Review Board: templated SOC 2 work is nonconforming (S30)"
  human_checkpoints: [ "Management owns the description and responses; service auditor tests independently" ]
  role_evolution: "Drafting shifts to review; SOC managers check AI-drafted descriptions against the system as it actually operates."
  evidence_grade: C
  sources:
    - { ref: S46, title: "How AI assurance builds trust with SOC, attestation and certification (14th EY SOC conference highlights)", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-12
  title: AI review of SOC 1 reports for user-entity reliance (control descriptions, deviations, CUECs)
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance, research-synthesis ]
  pattern: document-to-decision
  lens: improve
  ladder: augment
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "User auditors and SOX teams read many SOC reports to extract control descriptions, test results, exceptions and complementary user entity controls, then map them to their own risks."
  solution: "AI reads SOC reports, compares them with the user's risk assessment, identifies changes from prior periods and calls out deviations (EY speakers). KPMG lists agents that manage SOC reports and extract control descriptions and test results."
  outcomes:
    - { lever: speed, description: "Claimed; no figures", figure: "none", source_ref: S46 }
  prerequisites: [ "Mapping of SOC controls to the user entity's control matrix" ]
  risks_and_guardrails:
    - "Omission/distortion risk in summaries (FRC taxonomy) (S01)"
    - "IFIAR: failure to assess reliance on the work of others is a recurring finding category (S09)"
  human_checkpoints: [ "Auditor evaluates deviations' effect on reliance and tests CUECs" ]
  role_evolution: "Third-party-risk and SOX staff move from extraction to evaluation."
  evidence_grade: C
  sources:
    - { ref: S46, title: "EY SOC conference highlights", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09 }
    - { ref: S50, title: "Seize the future: the agentic shift in SOX compliance", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html", date: 2025-07-31 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-13
  title: "Idea: AI-assisted test-of-design evaluation of controls against criteria, with aggregation across the control set"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ expert-judgment, review-assurance ]
  pattern: document-to-decision
  lens: improve
  ladder: assist
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Design evaluation and deficiency-severity judgments are judgment-heavy. IFIAR still records findings for failing to evaluate deficiency severity (11 in 2025) and failing to adjust testing after ineffective controls (6)."
  solution: "The FRC's guidance uses this task as its worked example of task-specification risk: an AI tool compares controls against design criteria and aggregates results into an overall view of the control environment. No public deployment found."
  outcomes:
    - { lever: quality, description: "No measured outcome", figure: "none", source_ref: S01 }
  prerequisites: [ "Explicit prompts for interdependencies and shared points of weakness" ]
  risks_and_guardrails:
    - "FRC: an aggregation that ignores interdependencies may overstate effectiveness (S01)"
    - "Misunderstanding of methodology: AI output informs judgment and is not itself a conclusion (S01)"
  human_checkpoints: [ "Auditor forms an independent view before comparing with tool output (FRC review guidance)" ]
  role_evolution: "Seniors challenge AI design assessments rather than draft them."
  evidence_grade: D
  sources:
    - { ref: S01, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30 }
    - { ref: S09, title: "2025 Survey of Inspection Findings", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-14
  title: "Idea: multi-agent evidence-sufficiency evaluation for IT controls (assessor, defender, judge) with auditor feedback"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: document-to-decision
  lens: improve
  ladder: augment
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Judging whether a bundle of policies, records and screenshots satisfies a semantic control is labour-intensive, needs scarce expertise, and has no public benchmark."
  solution: "IntelliAudit, a research prototype on ISO 27001, retrieves evidence and drafts an evidence-grounded assessment. A 'defender' agent seeks mitigating evidence for adverse findings, and a 'judge' agent resolves disagreements and absorbs auditor feedback. It produces cited recommendations, missing-evidence analysis and remediation steps, not certification."
  outcomes:
    - { lever: quality, description: "Practicing auditors rated explanations positively; sufficiency judgments were the weakest area and auditor feedback corrected overly permissive results", figure: "mean 3.92/5; 86% of ratings 4-5; judge invoked in 10.4% of cases, all revisions stricter", source_ref: S66 }
  prerequisites: [ "Expert-built benchmark of evidence bundles per control" ]
  risks_and_guardrails: [ "Treat as decision support, not autonomous certification (authors)" ]
  human_checkpoints: [ "Auditor calibrates sufficiency and can override" ]
  role_evolution: "IT auditors adjudicate rather than read every artefact."
  evidence_grade: D
  sources:
    - { ref: S66, title: "IntelliAudit: Using Large Language Models to Evaluate Audit Controls", publisher: arXiv (2608.07688), type: academic, url: "https://arxiv.org/html/2608.07688v1", date: 2026-08-07 }
  last_reviewed: 2026-10-16
  notes: "Simulated organisations (4) and 14 controls; small-sample evaluation; not peer reviewed."

- id: assurance-controls-testing-15
  title: "Idea: screening control evidence for AI fabrication and embedded prompt injection before AI or human testing"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: intake-triage
  lens: improve
  ladder: assist
  runtime_class: workflow-automation
  maturity: emerging
  problem: "GenAI makes convincing fake invoices, approvals and screenshots cheap to produce. Control owners who know auditors test with agents could hide instructions in evidence to steer the agent."
  solution: "Regulators and practitioners call for authenticity procedures over evidence and alertness to adversarial AI use. No public deployment of a dedicated screening step for controls evidence was found."
  outcomes:
    - { lever: risk, description: "65% of internal audit leaders cite fabricated invoices/documents as an AI-enabled fraud concern; 62% say their function is unprepared or minimally prepared", figure: "65%; 62%", source_ref: S36 }
  prerequisites: [ "Evidence obtained from source systems where possible", "Agent input sanitisation and output schemas" ]
  risks_and_guardrails:
    - "IRBA: establish procedures to verify the authenticity of evidence and working papers (S15)"
    - "IFIAR 2026: be alert to intentional generation or manipulation of documents designed to circumvent controls (S11)"
    - "IAASB ED: reliability attributes include authenticity (S23)"
  human_checkpoints: [ "Auditor escalates suspected manipulation under fraud standards" ]
  role_evolution: "Forensic and IT specialists get involved in routine controls testing."
  evidence_grade: D
  sources:
    - { ref: S15, title: "Artificial Intelligence Audit Risks Mitigation Update", publisher: IRBA (South Africa), type: regulator, url: "https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf", date: 2024-09-19 }
    - { ref: S11, title: "Use of technology in audits – Innovation and audit quality 2026", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20 }
    - { ref: S49, title: "The Future of SOX", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
    - { ref: S36, title: "Internal Audit and AI-Enabled Fraud", publisher: Internal Audit Foundation & AuditBoard, type: survey, url: "https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf", date: 2026-02-17 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-16
  title: "Idea: external auditor reliance on management's or internal audit's AI-enabled control testing"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ expert-judgment, review-assurance ]
  pattern: other
  lens: reinvent
  ladder: assist
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Internal audit spends a large share of its hours on SOX: KPMG's 2025 survey found 52% of IA departments spent over 40% of their hours on it, and the IIA cites over 60% for most respondents. Using that work is governed by AS 2605 (PCAOB) and ISA 610, which predate analytics and AI."
  solution: "Practitioners and the IIA are discussing reliance on AI-enabled testing performed by management or IA: parallel pilots with the external auditor, and equal criteria for supervising, documenting and evaluating AI-assisted work whoever performs it. KPMG argues the external auditor's own full-population tools could lower, or raise, the value of relying on management's tests."
  outcomes:
    - { lever: cost, description: "No measured outcome", figure: "none", source_ref: S49 }
  prerequisites: [ "Modernised reliance standard (IIA asks PCAOB to modernise AS 2605)", "Shared evidence standard for AI outputs (COSO reliance definition)" ]
  risks_and_guardrails:
    - "IIA: 'reliance is not delegation'; the external auditor alone is responsible for the opinion (S32)"
    - "IFIAR: inadequate assessment of reliance on others' work recurs in inspections (S09)"
  human_checkpoints: [ "External auditor evaluates competence, objectivity and the AI tool's certification" ]
  role_evolution: "If reliance grows, internal audit becomes the testing engine and the external auditor re-performs and oversees."
  evidence_grade: D
  sources:
    - { ref: S32, title: "IIA comments on PCAOB Release No. 2026-005 (standard setting)", publisher: The Institute of Internal Auditors, type: professional-body, url: "https://www.theiia.org/globalassets/site/about-us/advocacy/iia-public-comment-letter-to-the-pcaob-standard-setting-project.pdf", date: 2026-08-07 }
    - { ref: S49, title: "The Future of SOX", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
    - { ref: S59, title: "5 Questions to Ask Before Your SOX Team Adopts AI Agents", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188703", date: 2026-08-18 }
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': cross-party reliance on AI-generated assurance evidence."

- id: assurance-controls-testing-17
  title: "Idea: synthetic transaction data and simulation agents to stress-test controls before go-live or integration"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance, software-systems ]
  pattern: other
  lens: reinvent
  ladder: assist
  runtime_class: workflow-automation
  maturity: emerging
  problem: "ERP implementations and acquisitions leave windows where controls are untested against real volumes and edge cases."
  solution: "KPMG proposes synthetic populations mirroring real data, and agents that simulate users, transactions and adversarial conditions. Together they test access controls, approval workflows and automated rules before live data flows. COSO separately recommends test populations to validate AI accuracy and stress-test edge cases."
  outcomes:
    - { lever: risk, description: "No measured outcome", figure: "none", source_ref: S49 }
  prerequisites: [ "Representative synthetic data generation", "Test environment mirroring production configuration" ]
  risks_and_guardrails: [ "Synthetic data may miss real-world anomalies; it supplements but does not replace operating-effectiveness evidence" ]
  human_checkpoints: [ "ICFR lead approves scenarios and interprets failures" ]
  role_evolution: "Control testers work alongside data scientists."
  evidence_grade: D
  sources:
    - { ref: S49, title: "The Future of SOX", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026 }
    - { ref: S25, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://www.coso.org/generative-ai", date: 2026-02-23 }
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': simulation-based pre-implementation control testing."

- id: assurance-controls-testing-18
  title: "Idea: data-driven monitoring of AI testing tools' usage and audit-quality impact at firm level"
  archetype: assurance
  module: controls-testing
  function: quality-management
  work_types: [ data-reporting, review-assurance ]
  pattern: monitor-diagnose-act
  lens: improve
  ladder: assist
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Regulators find firms cannot show how ATTs affect quality. Monitoring is often manual, inconsistently performed, and unclear between global network and member firm."
  solution: "IFIAR asks for data-driven monitoring with defined metrics, such as engagement coverage %, plus root-cause analysis of technology findings. The SEC Chief Accountant says the SEC asks auditors how they use AI to monitor their quality systems. NFRA wants technology treated as a distinct risk area in the QC system."
  outcomes:
    - { lever: quality, description: "No measured outcome", figure: "none", source_ref: S11 }
  prerequisites: [ "Telemetry from audit platforms on tool use per engagement", "Linkage to inspection and internal review findings" ]
  risks_and_guardrails:
    - "FRC thematic: legacy ATTs in use without formal certification; firms still building usage and quality monitoring (S03)"
    - "Gartner/Accounting Times: adoption and hours-saved metrics alone understate or misstate value (S45)"
  human_checkpoints: [ "Quality leadership reviews trends and triggers recertification" ]
  role_evolution: "Central methodology and quality teams add analytics roles."
  evidence_grade: D
  sources:
    - { ref: S11, title: "Use of technology in audits – Innovation and audit quality 2026", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf", date: 2026-04-20 }
    - { ref: S18, title: "Q&A with SEC Chief Accountant Kurt Hohl", publisher: KPMG Board Leadership Center, type: firm, url: "https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html", date: 2026-05-27 }
    - { ref: S03, title: "Thematic Review: Certification of Automated Tools and Techniques", publisher: Financial Reporting Council, type: regulator, url: "https://www.frc.org.uk/docs/8383/html/", date: 2025-06-26 }
  last_reviewed: 2026-10-16
  notes: "Function 'quality-management' is used because this sits in the firm's quality system rather than in engagement delivery."

- id: assurance-controls-testing-19
  title: "Idea: structured skepticism prompts (counter-arguing) when reviewing tool-performed control tests"
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  lens: improve
  ladder: assist
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Auditors are less skeptical of work done by automated tools than of the same work by a colleague. Fluent GenAI output strengthens the 'halo effect'."
  solution: "Peters' experiment found a counter-arguing mindset intervention alleviated the loss of skepticism. The FRC, NFRA and AFM ask firms to train reviewers on automation bias. Holmstrom & Peters will test a motivation prompt to offset judgment effects of GenAI automation."
  outcomes:
    - { lever: quality, description: "Experimental: counter-arguing intervention reduced automation bias; no spillover to later tasks found", figure: "experimental effect, no field figure", source_ref: S63 }
  prerequisites: [ "Reviewer checklists and tool-specific known-failure briefings (FRC staff education)" ]
  risks_and_guardrails:
    - "ICAEW: the FRC guidance covers automation bias in a single paragraph; long-term judgment erosion is under-addressed (S38)"
    - "Algorithm aversion is the opposite risk: auditors discount contradictory AI evidence (S61)"
  human_checkpoints: [ "Reviewer forms an independent expectation before reading tool conclusions" ]
  role_evolution: "Review becomes a trained, distinct competence (NFRA: reviewers trained in critical evaluation and bias awareness)."
  evidence_grade: D
  sources:
    - { ref: S63, title: "Auditor automation usage and professional skepticism", publisher: Tilburg University (working paper, C. Peters), type: academic, url: "https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/", date: 2022 }
    - { ref: S64, title: "How Does Generative AI Automation Affect Auditors' Motivation and Judgment Quality? (registered report proposal)", publisher: PCAOB conference / Holmstrom & Peters, type: academic, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf", date: 2025 }
    - { ref: S14, title: "12 building blocks for controlled use of auditing tools", publisher: AFM (Netherlands), type: regulator, url: "https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf", date: 2025-12-11 }
  last_reviewed: 2026-10-16

- id: assurance-controls-testing-20
  title: SOC-style attestation over AI systems (assurance over AI) as an extension of controls-testing services
  archetype: assurance
  module: controls-testing
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: other
  lens: reinvent
  ladder: assist
  runtime_class: personal-assistant
  maturity: announced
  problem: "Enterprise buyers ask AI vendors for SOC 2, yet SOC 2 does not reliably attest to model-specific properties such as training-data provenance, drift detection or bias testing."
  solution: "Firms are extending SOC/attestation and certification offerings to cover AI system lifecycle controls. EY says it is updating SOC reports and attestation services across the AI lifecycle. CSA offers STAR for AI and an AICPA SOC 2+ bridge to its AI Controls Matrix (247 control objectives). AICPA staff describe developer-side functionality engagements and deployer-side governance engagements."
  outcomes:
    - { lever: growth, description: "No published revenue or volume figures", figure: "none", source_ref: S31 }
  prerequisites: [ "Suitable criteria (no AI-specific TSC yet)", "AI-competent engagement teams" ]
  risks_and_guardrails:
    - "Terminology: 'assurance' is regulated in some jurisdictions; some providers call it an 'evaluation report' (S31)"
    - "Scope negotiation without common criteria limits comparability (S31, S47)"
  human_checkpoints: [ "Practitioner's criteria-suitability and scoping judgment" ]
  role_evolution: "SOC practices add AI-specialist roles and credentials (e.g., CSA CCAA, ISACA AAIA)."
  evidence_grade: C
  sources:
    - { ref: S31, title: "A new frontier: CPAs as AI system evaluators", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/nov/a-new-frontier-cpas-as-ai-system-evaluators/", date: 2025-11 }
    - { ref: S46, title: "EY SOC conference highlights", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09 }
    - { ref: S47, title: "The SOC 2 AI Gap", publisher: Cloud Security Alliance, type: professional-body, url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/", date: 2026-08-30 }
  last_reviewed: 2026-10-16
  notes: "Pattern 'other': attestation whose subject matter is an AI system. Overlaps with the 'other assurance' module; included here because the work is SOC controls testing."
```

**Count by evidence grade:** A = 3 (02, 03, 07) · B = 3 (01, 04, 05) · C = 7 (06, 08, 09, 10, 11, 12, 20) · D ("idea") = 7 (13–19). Total 20.

---

## 3. Module notes

### Processes and key steps (work types)

- **Scoping and planning.** Identify significant accounts, relevant assertions and key controls; decide on reliance (combined vs substantive approach; IAASB ED-330 would allow "controls alone" in narrow cases). Work types: `expert-judgment`, `data-reporting`.
- **Walkthroughs and test of design.** Trace a transaction and confirm the control is designed to prevent or detect misstatement. Work types: `review-assurance`, `document-production`.
- **ITGC and application-control testing.** Access, change management and operations; automated controls, with benchmarking or "consistency of operation" arguments (ED-330 A59, A62–A63). Work type: `review-assurance`.
- **IPE / reliability of information.** Test the controls over reports used in controls (PCAOB AS 1105 amendments; ED-500 para 13 would require testing those controls "or other procedures"). Work types: `review-assurance`, `data-reporting`.
- **Sample selection and sampling.** Work type: `data-reporting`.
- **Evidence requests (PBC) and collection.** Work types: `coordination-scheduling`, `client-interaction`.
- **Attribute testing, tick-marking and workpapers.** Work types: `review-assurance`, `document-production`.
- **Deviation and deficiency evaluation.** Severity, aggregation, compensating controls, and adjusting the substantive response. Work type: `expert-judgment`.
- **Reliance on others.** SOC 1 reports and CUECs; internal audit's work (AS 2605, ISA 610). Work types: `review-assurance`, `research-synthesis`.
- **SOC examinations.** System description (Section 3), tests of controls, exceptions and management responses. Work types: `review-assurance`, `document-production`.
- **Review, supervision and documentation.** AS 1215 reperformance standard; FRC: central tool documentation retained centrally and engagement-level use documented on file. Work type: `review-assurance`.

### Common pain points

- **Rising hours and cost.**
  - KPMG's 2025 SOX survey: average testing hours per control rose from 12 (FY2022) to 16 (FY2024), and SOX control cost rose 45% between the 2023 and 2025 surveys. Transactional and ITGC controls take the longest to test (S49).
  - Zanin cites an average program of $2.3M and over 15,000 hours a year, about 40% of it on testing. The underlying survey is not named in the article (S59).
- **Persistent inspection findings.**
  - Internal control testing is the top finding theme by count in IFIAR's 2025 survey (213 findings in listed-PIE audits).
  - The main drivers: insufficient evidence for reliance on manual controls (69), IPE/data (43), ITGC/application controls (39) (S09).
- **Messy evidence.** Screenshots, PDFs, spreadsheets, emails and exports with no naming convention. About one in five PBC requests come back wrong first time (practitioner estimate, S59).
- **Input-data reliability for tools.**
  - The AFM frequently finds auditors give insufficient attention to ineffective GITCs when concluding that tool input data are reliable (S14).
  - The PCAOB amendments re-emphasise ITGCs and automated controls for electronic information (S06).
- **Tool governance immaturity.**
  - Some firms' certification processes are not backed by documented policies, and legacy tools are uncertified (S03).
  - Monitoring of tools' quality impact is often manual, and responsibility between network and member firm is unclear (S10, S11).
- **Skills.** Protiviti's 2024 SOX poll: only one in five participants were highly confident they had the skills to use SOX technology (search result only). The ISACA 2026 poll finds 33% of organisations train all employees on AI (S42).

### Metrics and benchmarks (with sources)

**Regulator and inspection data**

| Metric | Figure | Source |
|---|---|---|
| Listed-PIE audits with ≥1 finding where internal control testing was inspected (2025) | 14% (88 of 641); 11% in 2021 | S09 |
| Internal-control-testing findings, listed PIE (2021→2025) | 203, 150, 206, 221, 213 | S09 |
| IFIAR members observing ATTs "frequently" in internal controls testing | 33% (2023) → 43% (2024); JE testing 86% → 88% | S10 |
| IFIAR members reporting findings that an ATT "was not used as intended" | 29% (2023) → 31% (2024) | S10 |
| GPPC networks' AI-enabled tools, year-over-year | ~30% increase in 2025 | S11 |
| US GNF tools using AI, blockchain or RPA (2023 inspection year) | <7%; all GNFs use tools to select samples; ~75% of tools built in-house | S06 |

**Adoption and governance surveys**

| Metric | Figure | Source |
|---|---|---|
| Internal audit GenAI use for audit testing vs drafting (Gartner webinar poll, 743 respondents) | 30% testing; 60% drafting issues/reports; 12% QA reviews; 93% any AI; 38% have a strategy | S45 |
| SOC conference live poll: AI use in SOC work | evidence collection 63%; Section 3 45%; deviation responses 41%; project management 29% | S46 |
| US CPA firms (CPA.com, 54 firms) | 75% no documented transformation plan; ~a quarter (elsewhere "approximately one-third") use no AI; ROI judged on staff efficiency 83%, quality 54%; 6% do not measure | S43 |
| Tax & audit professionals (TR, 2026) | 81% use AI regularly; more than a third use unauthorised AI tools | S44 |
| Digital-trust professionals (ISACA, 3,400+) | 38% have a formal comprehensive AI policy; 22% say AI ROI met expectations | S42 |

**Named outcomes**

| Metric | Figure | Source |
|---|---|---|
| Microsoft ITGC change-management agent (self-reported) | 850 h and $185K a year; Sample Selection Agent 2K h a year | S53, S54 |
| Reddit internal audit via Optro (vendor-reported) | 175 controls (>40% of SOX scope), −60% testing time per control, in 3 months | S55 |

**Research benchmarks**

| Metric | Figure | Source |
|---|---|---|
| LLM accuracy on 8 audit tests, 167 items (5 models, basic prompts) | 74%–96%, with hallucination risk on complex clauses | S68 |
| IntelliAudit (ISO 27001, 14 controls, 4 simulated organisations) | 91.7% of final statuses matched assessor-only; judge invoked 10.4%, all revisions stricter | S66 |
| Pre-GenAI archival study | +1 s.d. AI investment linked to 5.0% lower restatement likelihood, 0.9% lower fees | S62 |

- No public benchmark for AI-performed tests of controls (accuracy of attribute conclusions or deviation detection) was found.

### Guardrails and regulatory points

**Accountability**
- Universal position: the human auditor stays accountable. FRC (S01, S60); NFRA, "no separate, lower evidentiary bar for technology generated information" (S17); AICPA (S27); AFM (S14); IFIAR (S11); CPAB (S12).

**Firm-level certification and monitoring (ISQM 1 / CSQM 1 / QC 1000)**
- **Unit of certification:** the tool in the context of a use case (S01).
- **What certification covers:**
  - evaluating inputs, architecture and component logic, and outputs, with output testing weighted more heavily for LLMs
  - testing on default, edge and diverse cases
  - recertification on material model or data changes (S01, S17)
- **Pilots:** often run in parallel with full alternative procedures (S01). AUASB staff suggest parallel use in a tool's first year (S26).
- **CPAB:** certification applies whether a tool is global, local or third-party. For off-the-shelf tools, consider a SOC 2 report over ITGCs (S12).
- **IAASB:** ED conforming amendments add ISQM 1 material on approving technological tools (S23).

**Agentic systems**
- **Control points.** Define where a human authorises, reviews or stops the system, based on the main deficiency risks (S01). Assign named engagement personnel to decision checkpoints and review autonomous decisions overall (S11). Have the auditor approve the testing plan before an agent runs (practitioner, S59).
- **Rules-based protocols.** Input/output schemas, scope and authority boundaries, escalation rules, and version control of models and components (S01).

**Documentation**
- **Engagement file (FRC):** state that an AI tool was used, the criteria for appropriate use, what it selected or produced, and the further work performed. Central certification evidence stays centrally (S01, S03).
- **NFRA:** documentation should let an experienced auditor see which tool processed which balance or assertion and how much human review it received (S17).
- **US view:** AS 1215 is the de facto bar in the absence of PCAOB AI guidance (S59).

**Client AI controls (COSO)**
- **Reliance vs non-reliance:** distinguish them; where management relies on AI output, retain prompt, configuration and model version, sampling rationale and exception resolution.
- **Control design:** separate configuration rights from review/approval rights, and put change control on prompts, thresholds and retrieval corpora.
- **Human oversight:** HITL ranges from full reperformance to risk-based sampling of exceptions (S25).

**PCAOB (US)**
- The technology-assisted analysis amendments apply to FY2026 audits, but they exclude AI and tool appropriateness (S06).
- The Board is gathering input on AI through the 2026 strategic-plan and standard-setting RFCs. Former acting chair George Botic invited comment on possible standards updates for AI (S19, S20).
- Chairman Logothetis ordered a supplemental request for comment on QC 1000 provisions, aiming at harmonisation with ISQM 1. QC 1000 is effective 15 Dec 2026 per landscape; not re-verified here (S19).

**SOC**
- TQA 9561: AI does not change SOC criteria; scope follows the system boundary (S48).
- The Peer Review Board treats templated, platform-driven SOC 2 work (identical risk assessments, samples and tests across clients) as "nonconforming" (S30).

**Data protection**
- Firms cannot rely on vendor terms of service without validation (NFRA, S17).
- The PCAOB's 2024 outreach found some firms barred GenAI from audit or attest procedures over privacy and reliability concerns (S07).

### Frontier signals (dated, sourced)

- **2026-02-23:** COSO GenAI internal-control publication defines "AI reliance" for ICFR and supplies control-testing templates (S25, S51).
- **2026-03-30:** FRC issues the first regulator guidance on GenAI and agentic AI in audit, including orchestrator risks (goal drift, invented integrations) and control-point oversight (S01, S02).
- **2026-04-20:** IFIAR's 2026 technology report flags agentic AI moving "from task automation toward an orchestration of multiple audit activities", and asks firms to define what "human-led" means in practice (S11).
- **2026-06-04:** FRC opens the Audit Tech & AI Sandbox and a "barriers to audit tech" research project for smaller firms (S05).
- **2026-06-23 to 2026-08-07:** PCAOB Release 2026-005 asks about AI (Questions 8 and 10). The IIA urges modernising AS 2605 because it has no framework for technology-generated IA evidence (S20, S32).
- **2026-07:** NFRA (India) issues ten principles explicitly covering agentic tools that select and test samples (S17).
- **2026-08-05:** IAASB EDs propose "tests of controls alone", GITC/indirect-control clarifications, emerging-technology material on automated controls, and "technological tools" terminology. Comments are due 15 Dec 2026; AUASB comments are due 16 Nov 2026 (S21–S23).
- **2026-09-11:** AICPA TQA 9561 on AI in SOC 1/SOC 2 (S48). **2026-10-13:** AICPA practice aid, with more risk-assessment and audit-evidence content promised (S27).
- **2027 (forecast):** KPMG expects the first wave of AI-related material weaknesses (S49).
- **Late 2025 to 2026:** other regulators issued guidance: AFM (Dec 2025, S14); ACRA Singapore Audit Practice Guidance No. 1 of 2025 (26 Dec 2025, search result only); IRBA updates (S15).

### Workforce and role effects

- **Preparer to reviewer.**
  - Testing staff move from evidence handling to exception review and agent oversight (S53, S55, S59).
  - Holmstrom & Peters warn that the move from preparing to reviewing may reduce autonomy, competence-building and motivation (S64).
  - TR's 2026 report asks firms to protect junior staff's structured development before automation removes it (S44).
- **New skill mix.**
  - KPMG: future ICFR professionals need fluency in both accounting standards and AI systems, and firms are trying out audit data scientists and dual-credentialed hires (S49).
  - NFRA: role-differentiated training. Preparers learn safe use, reviewers learn critical evaluation and bias awareness, and partners learn governance (S17).
  - New credentials include ISACA AAIA (search result only) and CSA CCAA (S47).
- **Labour substitution evidence (pre-GenAI).** Accounting headcount fell 3.6% after three years and 7.1% after four, per one-s.d. increase in AI investment (S62).
- **Internal audit capacity.** SOX consumes much of IA's capacity: KPMG's 2025 survey found 52% of IA departments spent more than 40% of their hours on SOX (S49), and the IIA cites over 60% for most respondents (S32). Automation is pitched as freeing that capacity rather than cutting it.

### Objections and concerns practitioners raise

- **Over-reliance and automation bias.** Raised by regulators (S01, S14, S17), research (S63) and interviewees (S65). ICAEW calls the FRC's coverage of automation bias too thin (S38).
- **Black-box and non-determinism.** The same test run twice can differ (S59); outputs must be verifiable or replicable (AFM, S14); there are no accepted methods for auditing black-box controls (S49).
- **Rubber-stamp human approval.** It adds no control value (S49).
- **Vendor claims vs independent evaluation.** NFRA (S17); practitioners advise bringing your own "ugliest evidence" to demos (S59).
- **Regulatory uncertainty.** No PCAOB AI guidance (S59). Regulators have not given blanket approval for AI-driven SOX compliance (S52). PwC: "An audit is what it is" (S58).
- **Evidence manipulation.** Includes prompt injection against testing agents (S49) and AI-fabricated documents (S15, S36).
- **Templating and commoditisation in SOC work** (S30, S47).
- **ROI unproven.** 22% say AI ROI met expectations (S42). PwC reports busy-season time savings are "not that drastic yet" (S58).

### Interview probes for an advisor

1. Which control tests (by type: ITGC, manual review controls, automated controls, IPE) do your AI tools execute today? For each, what does the file show about the tool, its version, the human checkpoint and the reviewer's independent work, and would it survive an AS 1215 or FRC-style review?
2. How did you certify or approve the tool for this use case? What edge-case testing, parallel running and recertification triggers apply, and who monitors its quality impact: network, member firm, or nobody yet?
3. Where do your clients' (or your own) controls now depend on AI output? Have you distinguished reliance from non-reliance in COSO's sense, and what evidence (prompts, thresholds, logs, model versions) do you retain or request?
4. If management or internal audit tests controls with AI, has the external auditor agreed in advance how, or whether, they will rely on it? Have you run a parallel pilot comparing exceptions caught?
5. What would you measure to show AI improved *test quality*, not just hours (missed deviations, rework, review notes, inspection findings)? Do you have a pre-AI baseline?

---

## 4. Sources

Type uses the controlled vocabulary. "Read" means the document was opened and its relevant content read (full text or, for long PDFs, the relevant sections). Items marked "(search result only)" were not opened.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| S01 | Generative and Agentic AI Guidance: risks, mitigations and illustrative examples | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 |
| S02 | Innovative new guidance supports audit firm adoption of emerging AI technologies | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 |
| S03 | Thematic Review: Certification of Automated Tools and Techniques | Financial Reporting Council | regulator | https://www.frc.org.uk/docs/8383/html/ | 2025-06-26 |
| S04 | FRC publishes landmark guidance providing clarity to audit profession on the uses of AI | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/ | 2025-06-26 |
| S05 | FRC invites firms and companies to experiment, innovate and reduce burdens through new sandbox programmes | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/06/frc-invites-firms-and-companies-to-experiment-innovate-and-reduce-burdens-through-new-sandbox-programmes/ | 2026-06-04 |
| S06 | PCAOB Release No. 2024-007: Amendments related to aspects of designing and performing audit procedures that involve technology-assisted analysis | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/rulemaking/docket-052/2024-007-adoptingrelease.pdf | 2024-06-12 |
| S07 | Spotlight: Staff update on outreach activities related to the integration of GenAI in audits and financial reporting | PCAOB staff | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 |
| S08 | Spotlight: Staff priorities for 2025 inspections and interactions with audit committees | PCAOB staff | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/2025-priorities-spotlight_v3.pdf | 2024-12 |
| S09 | 2025 Survey of Inspection Findings (report) | IFIAR | regulator | https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf | 2026-04-01 |
| S10 | Use of technology in audits – observations, risks and further evolution (2025) | IFIAR Technology Task Force | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 |
| S11 | Use of technology in audits – Innovation and audit quality 2026 | IFIAR Technology Task Force | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2026TTFReport.pdf | 2026-04-20 |
| S12 | The use of artificial intelligence in the audit — balancing innovation and risk | CPAB (Canada) | regulator | https://cpab-ccrc.ca/docs/default-source/thought-leadership-publications/2024-use-of-artificial-intelligence-in-the-audit-en.pdf | 2024-09 |
| S13 | Technology in the audit (web page) | CPAB (Canada) | regulator | https://cpab-ccrc.ca/insights/technology-in-the-audit | n.d. (accessed 2026-10-16) |
| S14 | 12 building blocks for controlled use of auditing tools | AFM (Netherlands) | regulator | https://www.afm.nl/~/profmedia/files/rapporten/2025/12-building-blocks-for-controlled-use-of-auditing-tools.pdf | 2025-12-11 |
| S15 | Artificial Intelligence Audit Risks Mitigation Update | IRBA (South Africa) | regulator | https://www.irba.co.za/upload/40_%20Artificial%20Intelligence%20Audit%20Risks%20Mitigation%20Update.pdf | 2024-09-19 |
| S16 | Study on the potential utilization of generative AI in audit practices and challenges related to audit quality (DP2025-3; abstract and front matter read) | Japan FSA, Financial Research Center | regulator | https://www.fsa.go.jp/frtc/english/seika/discussion/2025/DP2025-3_Eng.pdf | 2025-07 (English Dec 2025) |
| S17 | NFRA sets 10 principles for technology use in audits, says AI cannot replace auditor judgement (coverage of NFRA staff paper) | CAalley | press | https://caalley.com/news-updates/indian-news/nfra-sets-10-principles-for-technology-use-in-audits-says-ai-cannot-replace-auditor-judgement | 2026-07-24 |
| S18 | Q&A with SEC Chief Accountant Kurt Hohl | KPMG Board Leadership Center | firm | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | 2026-05-27 |
| S19 | PCAOB requests public comment on strategic priorities in first open meeting under Chairman Logothetis | WilmerHale | firm | https://www.wilmerhale.com/en/insights/blogs/keeping-current-disclosure-and-governance-developments/20260408-pcaob-requests-public-comment-on-strategic-priorities-in-first-open-meeting-under-chairman-logothetis | 2026-04-08 |
| S20 | PCAOB seeks public input on standard-setting priorities for the first time | Thomson Reuters Tax & Accounting | press | https://tax.thomsonreuters.com/news/pcaob-seeks-public-input-on-standard-setting-priorities-for-the-first-time/ | 2026-06 |
| S21 | Proposed revisions for audit evidence & risk response: ISA 330, ISA 500 & ISA 520 | IAASB | standard-setter | https://www.iaasb.org/publications/proposed-revisions-audit-evidence-risk-response-isa-330-isa-500-isa-520 | 2026-08-05 |
| S22 | Request for comments: AE&RR exposure drafts response form (all EM questions) | IAASB (hosted by IRBA) | standard-setter | https://irba.co.za/wp-content/uploads/2026/08/IAASB-Audit-Evidence-Risk-Response-Integrated-Response-Form.docx | 2026-08 |
| S23 | Consultation Paper: IAASB proposed standards on audit evidence & risk response | AUASB (Australia) | standard-setter | https://www.auasb.gov.au/media/fegpk4s5/auasb_cp_iaasbproposedintlstdonauditevidence__riskresponse1.pdf | 2026-08 |
| S24 | Technology Quality Management roundtables: outcomes and next steps | IAASB | standard-setter | https://www.iaasb.org/publications/technology-quality-management-roundtables-outcomes-and-next-steps | 2026-02-10 |
| S25 | Achieving Effective Internal Control Over Generative AI (Emett, Eulerich, Guthrie, Pikoos, Wood) | COSO | standard-setter | https://www.coso.org/generative-ai (text read from copy at https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf) | 2026-02-23 |
| S26 | Impact of AI on auditors (staff guidance page) | AUASB (Australia) | standard-setter | https://www.auasb.gov.au/publications/impact-of-ai-on-auditors/ | n.d. (accessed 2026-10-16) |
| S27 | AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 |
| S28 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| S29 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02 |
| S30 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks.html | 2026-05-14 |
| S31 | A new frontier: CPAs as AI system evaluators | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2025/nov/a-new-frontier-cpas-as-ai-system-evaluators/ | 2025-11 |
| S32 | IIA comments in response to PCAOB Release No. 2026-005 (standard setting) | The Institute of Internal Auditors | professional-body | https://www.theiia.org/globalassets/site/about-us/advocacy/iia-public-comment-letter-to-the-pcaob-standard-setting-project.pdf | 2026-08-07 |
| S33 | IIA public comment on PCAOB strategic plan (PCAOB No. 2026-001) | The Institute of Internal Auditors | professional-body | https://www.theiia.org/globalassets/site/about-us/advocacy/iia-public-comment-on-pcaob-strategic-plan.pdf | 2026-05-15 |
| S34 | Modernizing the Sarbanes-Oxley Act | The Institute of Internal Auditors | professional-body | https://www.theiia.org/globalassets/site/about-us/advocacy/us-advocacy/modernizing-the-sarbanes-oxley-act.pdf | 2026-03-17 |
| S35 | The IIA's Artificial Intelligence Auditing Framework (page) | The Institute of Internal Auditors | professional-body | https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/ | 2024-09-13 |
| S36 | Internal Audit and AI-Enabled Fraud | Internal Audit Foundation & AuditBoard | survey | https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf | 2026-02-17 |
| S37 | Testing Gen AI platforms: can they do audit work? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09-24 |
| S38 | How helpful is FRC guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05-06 |
| S39 | Practice guide: Internal Audit in the age of Generative AI (page) | IIA Netherlands & ISACA NL | professional-body | https://www.iia.nl/publicaties/practice-guide-internal-audit-generative-ai | 2026 (rev. 25 Sep) |
| S40 | Auditing in the Age of Generative AI | Center for Audit Quality | professional-body | https://thecaq.wpenginepowered.com/wp-content/uploads/2024/04/caq_auditing-in-the-age-of-generative-ai__2024-04.pdf | 2024-04 |
| S41 | Your 2026 audit committee agenda: ICFR during AI transformations (CAQ action plan) | TheCorporateCounsel.net | press | https://www.thecorporatecounsel.net/blog/2026/02/your-2026-audit-committee-agenda-icfr-during-ai-transformations.html | 2026-02 |
| S42 | AI use accelerates while governance and ROI lag (2026 AI Pulse Poll) | ISACA | survey | https://isaca.org/about-us/newsroom/press-releases/2026/ai-use-accelerates-while-governance-and-roi-lag-says-new-isaca-research | 2026-05-05 |
| S43 | 2025 Audit Transformation Report | CPA.com / AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 |
| S44 | What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 |
| S45 | Audit teams' AI use common but most lack strategy (Gartner webinar poll) | Accounting Times | press | https://www.accountingtimes.com.au/profession/audit-teams-ai-use-common-but-most-lack-strategy | 2026-08 |
| S46 | How AI assurance builds trust with SOC, attestation and certification (14th EY SOC conference highlights) | EY | firm | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf | 2026-09 |
| S47 | The SOC 2 AI gap: auditors improvise where AICPA has not acted | Cloud Security Alliance | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/ | 2026-08-30 |
| S48 | AI in SOC examinations: what the AICPA's new TQA Section 9561 means for service organizations | Schneider Downs | firm | https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/ | 2026-09-30 |
| S49 | The Future of SOX: a point of view for 2030 and beyond | KPMG LLP | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf | 2026 |
| S50 | Seize the future: the agentic shift in SOX compliance | KPMG LLP | firm | https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html | 2025-07-31 |
| S51 | Heads Up: COSO releases publication on internal controls related to generative AI | Deloitte (DART) | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 |
| S52 | The power of AI in efficient SOX compliance | Grant Thornton | firm | https://www.grantthornton.com/insights/articles/advisory/2025/the-power-of-ai-in-efficient-sox-compliance | 2026-07-21 |
| S53 | SOX Change Management Testing Agent (Frontier Finance innovation story) | Microsoft | firm | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf | 2026 (FY26) |
| S54 | AI solution overviews: Internal Audit | Microsoft | firm | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/Internal-Audit.pdf | 2026 (FY26) |
| S55 | Optro launches domain-trained agents for audit, compliance, third-party risk and AI governance | Optro | vendor | https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance | 2026-10-14 |
| S56 | Andera and RSM US partner to create AI-enabled control testing platform for internal audit | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/26/andera-and-rsm-us-partner-to-create-ai-enabled-control-testing-platform-for-internal-audit/189130/ | 2026-08-26 |
| S57 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 |
| S58 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 (page metadata) |
| S59 | 5 questions to ask before your SOX team adopts AI agents (Alexey Zanin) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=188703 | 2026-08-18 |
| S60 | Auditors warned they remain accountable despite use of AI | Board Agenda | press | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | 2026-03-31 |
| S61 | Commerford, Dennis, Joe & Ulla, "Man versus machine: complex estimates and auditor reliance on artificial intelligence" (abstract) | Journal of Accounting Research 60(1) | academic | https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html | 2022 |
| S62 | Fedyk, Hodson, Khimich & Fedyk, "Is artificial intelligence improving the audit process?" (abstract) | Review of Accounting Studies 27(3) | academic | https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html | 2022 |
| S63 | Peters, "Auditor automation usage and professional skepticism" (abstract) | Tilburg University working paper | academic | https://research.tilburguniversity.edu/en/publications/auditor-automation-usage-and-professional-skepticism/ | 2022 |
| S64 | Holmstrom & Peters, "How does generative AI automation affect auditors' motivation and judgment quality?" (registered report proposal) | PCAOB / Management Science registered reports conference | academic | https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf | 2025 |
| S65 | Kokina, Blanchette, Davenport & Pachamanova, "Challenges and opportunities for artificial intelligence in auditing: evidence from the field" (abstract) | International Journal of Accounting Information Systems 56 | academic | https://ideas.repec.org/a/eee/ijoais/v56y2025ics1467089525000107.html | 2025 |
| S66 | IntelliAudit: using large language models to evaluate audit controls | arXiv 2608.07688 | academic | https://arxiv.org/html/2608.07688v1 | 2026-08-07 |
| S67 | Fabian & Ratzinger-Sakel, task-specific AI in the audit of management reports (Journal of Information Systems; university summary) | University of Hamburg Business School | academic | https://www.bwl.uni-hamburg.de/en/ueber-die-fakultaet/aktuelles/2026/0320-ki-loesungen-in-der-wirtschaftspruefung-jette-fabian-nicole-ratzinger-sakel.html | 2026-03-20 |
| S68 | Graczyk, Majek & Modzelewski, "Use of large language models in auditing as a tool to reduce information asymmetry and fraud risk" | Yearbook of Auditing and Accounting (PANA, Poland) | academic | https://pana.gov.pl/wp-content/uploads/2026/04/6.-YoAA_Use-of-large-language-models-LLMs-in-auditing-as-a-tool-o-reduce-information-asymmetry-and-fraud-risk-in-the-hareholder-management-relationship.pdf | 2025 (posted 2026-04) |
| S69 | Audit Practice Guidance No. 1 of 2025: Delivering quality audits in a technology-driven environment (search result only) | ACRA (Singapore) | regulator | https://www.acra.gov.sg/news-events/news-announcements/906/ | 2025-12-26 |
| S70 | Gartner survey finds 93 percent of audit functions use AI but 60 percent lack… (search result only; 161 CAEs, May 2026) | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2026-09-10-gartner-survey-finds-93-percent-of-audit-functions-use-ai-but-60-percent-lack | 2026-09-10 |
| S71 | Empowering the progress of SOX innovation with analytics and automation (poll page opened; percentages not rendered) | Protiviti | survey | https://www.protiviti.com/gl-en/survey/the-evolution-of-sox-tech-adoption-and-cost-focus-amid-business-changes-cyber-and-esg-mandates | 2024-08-28 |
| S72 | Auditors limit Gen AI to administrative tasks, regulator says (paywalled; lede only) | Bloomberg Tax | press | https://news.bloombergtax.com/artificial-intelligence/auditors-limit-gen-ai-to-administrative-tasks-regulator-says | 2024-07 |

**Count by type (S01–S72):**
- regulator 17 (S01–S16, S69)
- standard-setter 6 (S21–S26)
- professional-body 14 (S27–S35, S37–S40, S47; JofA items are counted here)
- academic 8 (S61–S68)
- survey 6 (S36, S42–S44, S70, S71; EY live polling sits inside the firm item S46)
- firm 10 (S18, S19, S46, S48–S54)
- vendor 1 (S55)
- press 10 (S17, S20, S41, S45, S56–S60, S72)
- Total: 72 across 8 types.

Approximately 64 sources were opened and read (full text or relevant sections). About 8 more were seen only through search results or a paywalled lede: S69, S70, the Protiviti percentages in S71, S72, ISACA AAIA, the Gartner Jan 2026 CAE release, the EDGAR full-text hit list, and the IAASB ED PDFs themselves.

---

## 5. Gaps

**Unreachable or partly reachable**

- **PCAOB.** pcaobus.org HTML pages returned HTTP 403, including the TAA implementation page, Release 2026-005 itself and the staff-publications index. The 2024-007 release, spotlights and conference papers were read via assets.pcaobus.org and pcaobus.org/documents. The exact text of Release 2026-005 Questions 8 and 10 was not read; their content is known only via the IIA letter (S32) and Thomson Reuters (S20). The QC 1000 effective date (15 Dec 2026) and the supplemental QC 1000 RFC status were not re-verified on the primary source.
- **IAASB exposure drafts.** The ED PDFs are login-gated on iaasb.org. The AUASB-hosted copies are image-only (printed to PDF), so the text was not extractable. Paragraph-level content (ED-330 paras 16–20, A59, A62–A63; ED-500 Appendix 3) comes from the IAASB response form (S22) and the AUASB consultation paper (S23), not from the ED text.
- **AICPA primary texts.** The practice aid and TQA 9561 were not read directly; coverage came from the AICPA press release, JofA and Schneider Downs. The AICPA ASEC SOC 2 Working Group warning about "fast and easy" platforms is known only through CSA (S47).
- **Gartner** (gartner.com 403): figures came via Accounting Times. Also unreached: SSRN (403), businesswire (403; ISACA AAIA launch), goingconcern.com (403), wolterskluwer.com (403), sec.gov file paths (403).
- **Paywalled or members-only:** Bloomberg Tax, IIA Global Practice Guide on analytics/GenAI, IIA NL guide body, ICAEW members-only material, Gartner *AI Implementation Guide: SOX Testing*.
- **NFRA staff paper:** read through CAalley (S17); the NFRA PDF itself was not located.

**Not found**

- **AI-related material weaknesses.** No 2025–2026 10-K disclosing one was found. An EDGAR full-text query returned about 1,000 filings mentioning both "material weakness" and "generative AI" but needed manual review beyond this scope.
- **AI-specific inspection findings.** No 2025–2026 PCAOB, FRC, CPAB or IFIAR inspection finding specific to an AI-performed test of controls. IFIAR's technology findings are about ATTs in general.
- **Independent quality benchmarks.** No peer-reviewed study or independent benchmark measures the *accuracy or quality* of AI-performed attribute tests, deviation detection or deficiency evaluation. All named outcomes (S53–S55) measure effort and are self- or vendor-reported.
- **Recent survey figures.** No 2025–2026 CAQ audit-partner survey on AI in controls testing; no Protiviti 2025/2026 SOX survey AI percentages (page did not render figures).
- **Further reading.** IFIAR 2026's list of member resources includes CPAB's *Evolving use of technology in the audit* and IRBA's *The Use of Generative AI Tools and Emerging Technologies in Audits*. Neither was opened.

**Landscape claims checked**

| Landscape claim | Result |
|---|---|
| IFIAR "31% ATT not used as intended" | **Confirmed.** Source is the IFIAR 2025 technology report on the 2024 survey (S10), not the 2025 findings survey. |
| Microsoft 850 vs 50 hours | **Resolved: 850.** "50" is a PDF text-extraction artifact (S54, rendered page). |
| COSO date | **Confirmed** 23 Feb 2026 (S51). |
| AICPA practice aid date | **Confirmed** 13 Oct 2026 (S27). |
| IAASB ED date | **Confirmed** 5 Aug 2026, comments due 15 Dec 2026 (S21, S22). |
| NFRA principles | **Confirmed** July 2026 (S17). |
| CPA.com "nearly a quarter use no AI" | **Internally inconsistent in the source.** The report says about a quarter in one place and about one-third in another (S43). The sample is 54 firms and not representative. |
| AS 2201/AS 2101 changes effective 15 Dec 2026 | **Not confirmed.** No primary or reliable secondary source found. |
