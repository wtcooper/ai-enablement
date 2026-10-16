# Module deep dive: assurance / soc-attestation / discourse

- **Archetype:** assurance
- **Module:** soc-attestation. SOC 1 / SOC 2 / SOC 3 and ISAE 3402 / ISAE 3000 service-organization examinations and other attestation engagements, end to end: scoping, system descriptions, readiness, testing, deviations, reporting, bridge letters; compliance-automation platforms and continuous compliance; quality concerns about commoditized SOC 2. (Individual control tests belong to the controls-testing module; this file stays on the SOC/attest service as a whole.)
- **Angle:** discourse. What practitioners, buyers and commentators have said in the last 12-18 months (about Apr 2025 to Oct 2026): conferences, webinars, podcasts, practitioner articles and community discussion about AI in SOC work, "SOC 2 mills", continuous assurance, trust centers, and where SOC reporting is heading.
- **Prepared:** 2026-10-16
- **Method note:** 40 distinct pages, PDFs, threads and repositories were opened with `curl` (a few through Hacker News's item API) or read from scratch copies left by the landscape scan. Source refs follow `PUBLISHER-SHORT-YYYY`, and a ref matches the landscape file where the document is the same. The shared web-search budget ran out part-way through, so several planned searches (the KPMG SOC webcast, trust-center discourse, ISAE 3402 commentary, academic work on SOC quality) were not run. Quotations are under 25 words. Allegations about Delve are reported as allegations: Delve denies them, and I found no independent verification of the leaked-data analysis.

---

## 1. Summary

1. **The SOC conversation in the last 12 months is mostly about quality and commoditization, and only secondarily about AI as a productivity tool.**
   - The AICPA's SOC 2 Working Group chair said in the *Journal of Accountancy* on 1 Feb 2026 that "fast and easy" may come at the expense of quality and objectivity (JOFA-FAST-2026).
   - The AICPA ethics staff followed on 6 Apr 2026 with contract-term warnings for tool-provider arrangements (JOFA-SOCETH-2026).
   - On 14 May 2026 the Peer Review Board told reviewers how to spot "nonconforming" high-volume SOC 2 practices, with outreach starting 1 Jun 2026 (JOFA-PEER-2026).
   - The AICPA's SOC page now carries a notice that it is looking into anonymous allegations about a compliance vendor (AICPA-SOC-LANDING-2026).
2. **The Delve allegations (19 Mar 2026) gave the debate a case.**
   - An anonymous author alleged that Delve generated near-identical SOC 2 reports and pre-written auditor conclusions, routed through a few audit firms (DEEPDELVER-2026, TC-DELVE-2026). Delve denies this and says it only supplies templates and a platform.
   - The aftermath was visible in buyer behaviour: at least three named Delve customers said they were re-certifying or re-examining (TC-DELVE2-2026), and vendor-risk advisers published checklists for vetting auditors and platforms (IANS-DELVE-2026, WHISTIC-DELVE-2026).
3. **Practitioner consensus: automation is welcome, but not where it shapes scope, evidence or conclusions.**
   - Baker Tilly's line is that efficiency can support a SOC 2 examination but cannot create assurance (BAKERTILLY-TRUST-2026).
   - KPMG's white paper warns that platforms "confirm control existence" more easily than effectiveness, and tells buyers to look for over-reliance on inquiry and "test of one" procedures (KPMG-BEYOND-2026).
   - The AICPA's own podcast says some vendors "automate the service entirely" at exceedingly low flat prices (JOFA-PODCAST-2026).
4. **Where AI is actually named in SOC work, the uses are drafting and evidence handling, with human review, and nothing is measured.**
   - An EY conference poll lists top uses: evidence collection 63%, drafting the Section 3 system description 45%, drafting management responses to deviations 41%, project management 29% (EY-SOC-2026, p.5).
   - Vanta, the largest platform, markets an AI agent that saves "an average of four hours per week" (vendor figure) (VANTA-HNS-2025).
   - **No error rate, override rate, parallel run or inspection outcome for AI in SOC work was found.** Peer-review results are not published.
5. **Standards have not changed for AI.**
   - AICPA TQA 9561 (Sep 2026) says AI creates no separate SOC model and no new criteria. Relevance depends on how the service organisation uses AI (SCHNEIDER-TQA-2026).
   - The Cloud Security Alliance's AI-assisted note says auditors are improvising AI evidence overlays, and that no AI-specific Trust Services Criteria exist (CSA-SOC2-2026). That note is secondary and not CSA-reviewed.
   - The AICPA is also exploring a "SOC Quality Center" badge (JOFA-FAST-2026).
6. **New entrants are testing a different model, and it is more transparent than the incumbents'.**
   - Chiaro, a new AI-built CPA firm, published its testing method on 4 Aug 2026, defaults to testing complete populations instead of samples, and sells readiness software and the audit as one product (HN-CHIARO-2026, CHIARO-METHOD-2026, CHIARO-BUNDLE-2026). It reports one Type I issued, no Type II yet. It is an interested party.
   - The bundle model it uses is the same one the AICPA's ethics guidance warns about when the vendor controls fee, scope or timing (JOFA-SOCETH-2026).
7. **Two themes in the brief produced thin or no discourse evidence:** bridge letters and ISAE 3402 / 3000 outside the US. Trust centers appear mainly as vendor products and as an allegation (see Gaps).

---

## 2. Use cases

Thirteen use cases are listed. Themes where AI is the subject of the examination rather than the tool (AI in SOC scope under TQA 9561, AI-specific evidence overlays, agent accountability) are kept in the module notes and in section 4 and not forced into the "how much does AI do" scale.

```yaml
- id: assurance-soc-attestation-01
  title: Drafting and refreshing the SOC system description (Section 3) and control descriptions from process documentation
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Management owns the Section 3 description and the control descriptions, and they must fit the
    organisation's own system. Template-driven descriptions are the most visible sign of a weak
    report: practitioners say two companies in different industries should never share the same
    Section 3.
  solution: >
    An AI assistant consolidates process and procedure documents into draft control descriptions,
    harmonises terminology and checks completeness against the AICPA Trust Services Criteria.
    Management reviews and adopts the text. EY lists this as one of six areas where AI can help
    "today".
  outcomes:
    - {lever: speed, description: "Share of poll selections naming AI use for updating the Section 3 system description", figure: "45%", measures: "share of selections in a live poll of attendees at EY's 2026 SOC, Attestation and Certification Conference, multiple selections allowed; number of respondents not stated", provenance: self-reported, source_ref: EY-SOC-2026}
  prerequisites:
    - Documented, current processes and a named management owner for the description
    - An inventory of AI tools in use (EY says organisations starting out should begin with governance and an AI inventory)
  risks_and_guardrails:
    - "AI may invent details and fill blanks even when told not to (EY-SOC-2026, p.5)"
    - "A generic description that does not describe this company's architecture and processes signals a template (CHIARO-VIBE-2026; KPMG-BEYOND-2026, p.5 on tailored reports)"
    - "Management must adopt the exact saved text; an AI's statement is not management's decision (CHIARO-METHOD-2026, method/readiness-and-independence)"
  human_checkpoints:
    - Management reviews, edits and adopts the description
    - The service auditor evaluates the description against the criteria and its own understanding of the system
  role_evolution: "Readiness leads move from writing to editing and verifying drafts against real processes; EY says judgment-heavy or nuanced work is a poor fit for AI (EY-SOC-2026, p.5)."
  evidence_grade: C
  sources:
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights)", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "pp.4-5 (six areas, poll chart)"}
    - {ref: CHIARO-VIBE-2026, title: "What is vibe compliance?", publisher: Chiaro (Y Assurance PLLC), type: firm, url: "https://chiarohq.com/soc-2/vibe-compliance", date: 2026-05-02, access: full, locator: "section 'Why it passes a first glance and fails real scrutiny'"}
    - {ref: KPMG-BEYOND-2026, title: "Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports?", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf", date: 2026-07, access: full, locator: "p.5"}
  last_reviewed: 2026-10-16
  notes: "Grade C: a firm-run poll of unnamed attendees and firm statements; no named deployment and no measured outcome. The poll covers both service organisations and examiners, so the split is unknown. The EY PDF's publication month comes from its file name and metadata (created 24 Sep 2026)."

- id: assurance-soc-attestation-02
  title: AI mapping of controls and customer commitments to the Trust Services Criteria, other frameworks and regulations
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >
    Service organisations hold several frameworks at once (SOC 2, ISO 27001, HIPAA, EU rules) and
    customers write their own commitments into contracts. Mapping each to controls is repetitive
    and a place where scope gaps arise.
  solution: >
    AI compares the organisation's control data sets with frameworks, laws and regulations (EY).
    Vanta's release describes a "Customer Commitments" feature that maps customer obligations to
    controls and automates follow-through, plus AI-powered scoping for multi-entity organisations.
  outcomes:
    - {lever: quality, description: "None published. Sources describe the capability, not a measured result", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: VANTA-HNS-2025}
  prerequisites:
    - A maintained control library and an inventory of customer commitments
    - Integration of the platform with the systems in scope
  risks_and_guardrails:
    - "Standardised mappings may not reflect an organisation's own data flows and logic without configuration and interpretation (KPMG-BEYOND-2026, p.3)"
    - "Scope accuracy is a human decision; automation collects against whatever scope was defined, correctly or not (SCRUT-EVIDENCE-2026, evidence-quality table)"
  human_checkpoints:
    - Management decides the scope and the controls to adopt
    - The auditor evaluates whether the mapped controls address the service commitments
  role_evolution: "Compliance staff configure and review mappings rather than build spreadsheets by hand."
  evidence_grade: C
  sources:
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.5, paragraph on framework and control mapping"}
    - {ref: VANTA-HNS-2025, title: "Vanta's Agentic Trust Platform redefines how enterprises earn, prove, and scale trust", publisher: Help Net Security (Vanta release), type: press, url: "https://www.helpnetsecurity.com/2025/11/19/vanta-agentic-trust-platform/", date: 2025-11-19, access: full, locator: "Organizations Center and Customer Commitments paragraphs"}
    - {ref: SCRUT-EVIDENCE-2026, title: "Automated evidence collection: How it actually works and where it fails", publisher: Scrut, type: vendor, url: "https://www.scrut.io/post/how-automated-evidence-collection-works", date: 2026-05-11, access: full, locator: "evidence-quality table; steps 2-4"}
  last_reviewed: 2026-10-16
  notes: "Announced only. No customer is named for this feature."

- id: assurance-soc-attestation-03
  title: Compliance-platform AI agent for audit readiness (evidence collection and validation, policy drafting, gap guidance)
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [data-reporting, document-production, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: >
    Readiness is dominated by chasing evidence, keeping policies in step with practice and answering
    auditors' follow-ups; the work is repetitive and falls on small security teams.
  solution: >
    A platform agent collects and validates evidence, drafts and updates policies, flags programme
    gaps and takes coordinated actions, with people deciding. Vanta's agent launched in July 2025
    and was relaunched as "AI Agent 2.0" in Nov 2025. Snyk's lead compliance manager is quoted as
    using Vanta to drive continuous compliance and liking the agent.
  outcomes:
    - {lever: capacity, description: "Average time saved per customer per week from automating evidence collection and streamlining policy management", figure: "4 hours per week (average)", measures: "average weekly time saved per customer by the Vanta AI Agent as stated by Vanta; sample and method not stated", provenance: vendor-published, source_ref: VANTA-HNS-2025}
    - {lever: capacity, description: "Evidence collection was the most-selected AI use among poll respondents", figure: "63%", measures: "share of selections in a live poll of attendees at EY's 2026 SOC conference, multiple selections allowed; respondent count not stated", provenance: self-reported, source_ref: EY-SOC-2026}
  prerequisites:
    - API integrations to cloud, identity, developer and ticketing systems
    - Controls actually implemented; tools "can't remediate controls for clients" (LINFORD-FAQ-2022)
  risks_and_guardrails:
    - "Tools confirm that configuration exists for the assets they monitor; additional governance is needed to know the right assets are monitored and exceptions are acted on (KPMG-BEYOND-2026, p.3)"
    - "Dashboards do not show that access reviews used the correct population or that exceptions were resolved (BAKERTILLY-TRUST-2026)"
    - "A tool cannot operate controls for management, validate design, determine operating effectiveness or form conclusions (BAKERTILLY-TRUST-2026)"
  human_checkpoints:
    - Management owns controls and decides remediation
    - The auditor evaluates sufficiency and appropriateness of the evidence
  role_evolution: "VantaCon 2026 speaker titles include 'GRC Engineer' at AI start-ups and a 'Sr. Director, GRC Engineering' at Vanta, which points to a security-engineering flavour of the compliance role (VANTACON-2026)."
  evidence_grade: B
  sources:
    - {ref: VANTA-HNS-2025, title: "Vanta's Agentic Trust Platform redefines how enterprises earn, prove, and scale trust", publisher: Help Net Security (Vanta release), type: press, url: "https://www.helpnetsecurity.com/2025/11/19/vanta-agentic-trust-platform/", date: 2025-11-19, access: full, locator: "Vanta AI Agent 2.0 section; Snyk quote"}
    - {ref: FORTUNE-VANTA-2026, title: "Exclusive: Vanta hits $300 million ARR as 'shadow AI' explodes across corporate America", publisher: Fortune, type: press, url: "https://fortune.com/2026/04/29/exclusive-vanta-arr-300-million-sequoia-shadow-ai-claude-cursor/", date: 2026-04-29, access: full, locator: "opening paragraphs (ARR, customer count)"}
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.5 poll"}
    - {ref: VANTACON-2026, title: "VantaCon 2026: The AI governance event", publisher: Vanta, type: conference, url: "https://www.vanta.com/vantacon", date: 2026-11-12, access: full, locator: "speaker list"}
  last_reviewed: 2026-10-16
  notes: "Grade B because Snyk is named as a user, but the only figure is a vendor average with no stated method. Fortune reports, from the company, that Vanta passed $300M ARR and serves more than 16,000 customers (scale, not outcome). The event date of VantaCon is 12 Nov 2026 (upcoming)."

- id: assurance-soc-attestation-04
  title: Continuous control monitoring and real-time compliance snapshots between examinations
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    A SOC 2 Type II tests a period, but controls drift between annual cycles and teams discover gaps
    at fieldwork. Buyers also want a current signal, not a report that is months old.
  solution: >
    Platforms integrate with cloud and SaaS systems, monitor hundreds of technical controls
    continuously and keep a live snapshot of compliance. EY speakers describe continuous evidence
    collection for "real-time compliance snapshots"; KPMG describes ongoing monitoring that lets
    companies "maintain a state of continuous compliance".
  outcomes:
    - {lever: risk, description: "No measured outcome published; sources describe the benefit qualitatively (gaps found earlier, less fieldwork scramble)", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: KPMG-BEYOND-2026}
  prerequisites:
    - Complete integrations with every in-scope system; a broken connection leaves stale data (LINFORD-FAQ-2022)
    - A risk assessment that is current and specific; without one the metrics "may be unreliable" (KPMG-BEYOND-2026, p.3)
  risks_and_guardrails:
    - "A scoping error shows as green on the dashboard while the evidence covers the wrong population, for example human users only when the control applies to service accounts (SCRUT-EVIDENCE-2026, steps section)"
    - "'Continuous compliance' is not continuous assurance: the examiner still has to test operation over the period (BAKERTILLY-TRUST-2026)"
    - "'Compliance' is a term never used in SOC 2 examinations, and a SOC 2 report is not a certification (JOFA-FAST-2026; JOFA-PODCAST-2026)"
  human_checkpoints:
    - Control owners decide on flagged exceptions and document the rationale
    - The auditor re-evaluates scope, population completeness and exceptions at fieldwork
  role_evolution: "Evidence chasing shrinks; reviewing exception queues and documenting rationale becomes the main manual task (SCRUT-EVIDENCE-2026, step 6)."
  evidence_grade: B
  sources:
    - {ref: KPMG-BEYOND-2026, title: "Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports?", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf", date: 2026-07, access: full, locator: "p.3 (benefits and areas of consideration)"}
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.4, area 4"}
    - {ref: VANTA-HNS-2025, title: "Vanta's Agentic Trust Platform redefines how enterprises earn, prove, and scale trust", publisher: Help Net Security (Vanta release), type: press, url: "https://www.helpnetsecurity.com/2025/11/19/vanta-agentic-trust-platform/", date: 2025-11-19, access: full, locator: "Snyk quote"}
    - {ref: BAKERTILLY-TRUST-2026, title: "Why trust in SOC 2 still comes down to more than efficiency", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/trust-in-soc-2-report-efficiency", date: 2026-05-26, access: full, locator: "'What you need to know' section"}
    - {ref: SCRUT-EVIDENCE-2026, title: "Automated evidence collection: How it actually works and where it fails", publisher: Scrut, type: vendor, url: "https://www.scrut.io/post/how-automated-evidence-collection-works", date: 2026-05-11, access: full, locator: "steps 2-6"}
    - {ref: LINFORD-FAQ-2022, title: "AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor", publisher: Linford & Co, type: firm, url: "https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs", date: 2022-06-15, access: full, locator: "sections on integrations and risks"}
  last_reviewed: 2026-10-16
  notes: "Grade B rests on Snyk's quoted use of Vanta for continuous compliance (a named user, no measurement). Linford is a 2022 foundation source, used only for the integration-risk point. The 'AI' in this use case is largely rules-based monitoring; discourse treats it as the first step toward continuous assurance but I found no one claiming assurance is continuous."

- id: assurance-soc-attestation-05
  title: Drafting management responses to SOC deviations (root cause, remediation, timelines, monitoring commitments)
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    When testing finds a deviation, management writes a response for the report. Responses are often
    thin on root cause and remediation, and they take time late in the cycle. Logical access is the
    commonest source: EY's review of more than 2,000 SOC reports found it behind 52% of SOC 1
    deviations and 40% of SOC 2 deviations.
  solution: >
    AI drafts structured responses that address root cause analysis, remediation actions, timelines
    and ongoing monitoring commitments, which management edits and owns.
  outcomes:
    - {lever: speed, description: "Share of poll selections naming AI use for drafting management responses to deviations", figure: "41%", measures: "share of selections in a live poll of attendees at EY's 2026 SOC conference, multiple selections allowed; respondent count not stated", provenance: self-reported, source_ref: EY-SOC-2026}
  prerequisites:
    - A root-cause process owned by management
    - A clear line between the auditor's findings and management's response
  risks_and_guardrails:
    - "Management's responses are management's; an auditor or tool vendor that writes them creates objectivity and independence questions (JOFA-SOCETH-2026, 'Objectivity, conflicts of interest, and independence')"
    - "AI outputs still need human oversight and may invent details (EY-SOC-2026, p.5)"
  human_checkpoints:
    - Management approves every response
    - The service auditor reads responses for consistency with the findings
  role_evolution: "Control owners spend less time writing and more time confirming that the remediation is real."
  evidence_grade: C
  sources:
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.4 area 2; p.5 poll"}
    - {ref: EY-SOC-2025, title: "How to build trust and confidence in technology through assurance reporting (13th annual EY SOC Reporting Conference highlights)", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-ch/insights/technology-risk/documents/ey-13th-annual-soc-reporting-conference-highlights.pdf", date: 2025-08, access: full, locator: "p.4 (survey of more than 2,000 SOC reports)"}
    - {ref: JOFA-SOCETH-2026, title: "SOC engagements: Ethics risks with tool providers", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/", date: 2026-04-06, access: full, locator: "section on objectivity and independence"}
  last_reviewed: 2026-10-16
  notes: "The EY deviation shares are a count of deviations in SOC reports 'supporting customers' 2024 and 2025 financial audits' (the page does not give the denominator beyond that); they are context for the problem, not an outcome of this use case."

- id: assurance-soc-attestation-06
  title: AI-supported project management of readiness and the examination (meeting notes to action items, evidence and escalation tracking)
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [coordination-scheduling, document-production]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    A SOC engagement runs for months with many owners, requests and follow-ups, and slips when
    nobody tracks what is outstanding.
  solution: >
    AI turns meeting notes into structured action items and audit documentation, clarifies control
    areas, and powers dashboards that track evidence collection, escalations and completion.
    The pattern is described as "other": it is coordination support rather than one of the listed
    agent patterns.
  outcomes:
    - {lever: capacity, description: "Share of poll selections naming AI for project management support", figure: "29%", measures: "share of selections in a live poll of attendees at EY's 2026 SOC conference, multiple selections allowed; respondent count not stated", provenance: self-reported, source_ref: EY-SOC-2026}
  prerequisites:
    - A shared tracker and a single list of requests
  risks_and_guardrails:
    - "The distinction between evidence 'submitted' and 'accepted' must stay explicit, because an upload does not show the evidence is complete or reliable (CHIARO-AINATIVE-2026)"
  human_checkpoints:
    - Engagement lead confirms status and what is open
  role_evolution: "Coordinators supervise the tracker instead of chasing by email."
  evidence_grade: C
  sources:
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.4 areas 3 and 6; p.5 poll"}
    - {ref: CHIARO-AINATIVE-2026, title: "What does AI-native SOC 2 actually mean?", publisher: Chiaro (Y Assurance PLLC), type: firm, url: "https://chiarohq.com/soc-2/ai-native-auditor", date: 2026-09-11, access: full, locator: "table 'What to watch'"}
  last_reviewed: 2026-10-16
  notes: "Lowest-risk use in the EY poll and the least discussed in the wider discourse."

- id: assurance-soc-attestation-07
  title: First-pass drafting of customer security-questionnaire answers from issued SOC reports and approved past answers
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [client-interaction, document-production]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >
    A SOC report is meant to reduce the stream of customer questionnaires, but sales deals still
    trigger long questionnaires that security teams answer by hand.
  solution: >
    AI drafts tailored responses, learning from issued SOC reports and previously approved answers
    (EY). Vanta's release says its agent "takes the first pass at questionnaires" with verified
    answers and flags gaps before reviews stall.
  outcomes:
    - {lever: speed, description: "None published. Vanta's release claims faster deal closing but gives no figure", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: VANTA-HNS-2025}
  prerequisites:
    - A library of approved answers tied to the current report and controls
  risks_and_guardrails:
    - "Answers must agree with the report and with what the controls actually do; trust pages and questionnaire answers should be spot-checked against reality (IANS-DELVE-2026, recommendations)"
    - "AI may invent details (EY-SOC-2026, p.5)"
  human_checkpoints:
    - Security owner approves answers before they go to the customer
  role_evolution: "Security and sales-engineering staff review drafts instead of writing them."
  evidence_grade: C
  sources:
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.4 area 5"}
    - {ref: VANTA-HNS-2025, title: "Vanta's Agentic Trust Platform redefines how enterprises earn, prove, and scale trust", publisher: Help Net Security (Vanta release), type: press, url: "https://www.helpnetsecurity.com/2025/11/19/vanta-agentic-trust-platform/", date: 2025-11-19, access: full, locator: "'Automate security questionnaires' bullet"}
    - {ref: IANS-DELVE-2026, title: "Delve Allegations Expose Weak Points in Compliance Services", publisher: IANS Research, type: press, url: "https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/19/delve-allegations-expose-weak-points-in-modern-compliance", date: 2026-03-24, access: full, locator: "'If you are not a Delve customer'"}
  last_reviewed: 2026-10-16
  notes: "Announced only. The IANS page URL exists in two date-stamped variants (2026/03/30 and 2026/04/19); the byline reads 24 March 2026."

- id: assurance-soc-attestation-08
  title: Trust center as the buyer-facing front end for the SOC report and control documentation
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    Buyers ask each vendor for the report, policies and answers by email and NDA; vendors answer
    repeatedly. At the same time, public trust pages can overstate what is in place.
  solution: >
    A maintained trust center publishes the report, certifications, policies and questionnaire
    answers from a single source. Whistic sells one for vendors and says it lets customers see real
    material "not just a claim". Chiaro gives a trust center free with any audit.
  outcomes:
    - {lever: experience, description: "None published. Sources describe the capability and the risk but no figure", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: WHISTIC-DELVE-2026}
  prerequisites:
    - A current report and documentation to publish
    - A rule that nothing on the page claims more than the report supports
  risks_and_guardrails:
    - "The Delve whistleblower alleges trust pages listed measures that were never implemented; Delve disputes the broader claims (DEEPDELVER-2026; TC-DELVE-2026)"
    - "IANS advises narrowing or removing security claims on trust pages until they are validated (IANS-DELVE-2026, 'If you are a Delve customer')"
  human_checkpoints:
    - Security owner approves each published claim
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - {ref: WHISTIC-DELVE-2026, title: "Your Vendor Has a SOC 2 Report. Now What?", publisher: Whistic, type: vendor, url: "https://www.whistic.com/resources/blog/your-vendor-has-a-soc-2-report-now-what", date: 2026-03, access: full, locator: "'How Whistic helps'"}
    - {ref: CHIARO-BUNDLE-2026, title: "Is there a SOC 2 platform that includes the audit itself?", publisher: Chiaro (Y Assurance PLLC), type: firm, url: "https://chiarohq.com/soc-2/platform-that-includes-the-audit", date: 2026-10-05, access: full, locator: "'Chiaro covers readiness, the audit and a Trust Center'"}
    - {ref: DEEPDELVER-2026, title: "Delve - Fake Compliance as a Service - Part I", publisher: "DeepDelver (Substack, anonymous)", type: community, url: "https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service", date: 2026-03-19, access: full, locator: "Introduction; appendix on public trust pages"}
    - {ref: IANS-DELVE-2026, title: "Delve Allegations Expose Weak Points in Compliance Services", publisher: IANS Research, type: press, url: "https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/19/delve-allegations-expose-weak-points-in-modern-compliance", date: 2026-03-24, access: full, locator: "recommendations"}
  last_reviewed: 2026-10-16
  notes: "The Whistic page has no printed date; its footnotes cite items dated 19-23 Mar 2026, so 2026-03 is an inference. No survey data on trust-centre adoption or buyer use was found."

- id: assurance-soc-attestation-09
  title: User-entity review of vendors' SOC reports with AI (comparison to risk assessments, prior-period changes, deviations, uniform-language flags), and bulk re-assessment after an industry event
  archetype: assurance
  module: soc-attestation
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >
    Vendor-risk teams receive hundreds of SOC reports, and most are read for an auditor logo and a
    clean opinion. After the Delve allegations, advisers say a report is a starting point and that
    uniform language and thin operational detail are warning signs.
  solution: >
    EY says report recipients can use AI to review SOC reports, compare them to their own risk
    assessments, identify changes from prior periods and call out control deviations. Whistic says
    its AI surfaces overly uniform language, thin operational detail and gaps between policy and
    questionnaire answers, and that its bulk assessment reaches a whole vendor portfolio with
    targeted questions.
  outcomes:
    - {lever: risk, description: "None published. No detection rate or false-positive figure was found", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: WHISTIC-DELVE-2026}
  prerequisites:
    - A vendor inventory with the named auditor and report period for each SOC report
    - A tiering of vendors by risk, because a clean report from a credible auditor may be enough for low-risk vendors (WHISTIC-DELVE-2026)
  risks_and_guardrails:
    - "Whistic's checklist tells buyers to flag two audit-firm names that the whistleblower alleged were certification mills; the allegation is unproven and Delve disputes it (WHISTIC-DELVE-2026)"
    - "A clean report does not answer every risk question; a report with findings can say more (KPMG-BEYOND-2026, p.5)"
  human_checkpoints:
    - Analyst decides on follow-up with the vendor
    - Higher-risk vendors get a conversation and an operational answer to a specific control question (WHISTIC-DELVE-2026)
  role_evolution: "KPMG says the responsibility for assessing report quality rests with the vendor-risk function: receiving a report is the beginning of due diligence (KPMG-BEYOND-2026, p.5)."
  evidence_grade: C
  sources:
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.5, paragraph on SOC report recipients"}
    - {ref: WHISTIC-DELVE-2026, title: "Your Vendor Has a SOC 2 Report. Now What?", publisher: Whistic, type: vendor, url: "https://www.whistic.com/resources/blog/your-vendor-has-a-soc-2-report-now-what", date: 2026-03, access: full, locator: "'How Whistic helps'; 'What to do right now'"}
    - {ref: KPMG-BEYOND-2026, title: "Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports?", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf", date: 2026-07, access: full, locator: "pp.4-5"}
    - {ref: IANS-DELVE-2026, title: "Delve Allegations Expose Weak Points in Compliance Services", publisher: IANS Research, type: press, url: "https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/19/delve-allegations-expose-weak-points-in-modern-compliance", date: 2026-03-24, access: full, locator: "vetting checklist"}
  last_reviewed: 2026-10-16
  notes: "Announced by a vendor that sells the product. The same capability is described by EY without a named user. This is the buyer-side counterpart of use case 11."

- id: assurance-soc-attestation-10
  title: Service auditor pulls evidence from client systems through tool integrations instead of screenshots and spreadsheets
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    Clients used to submit dozens of screenshots and Excel files per examination, and examiners
    spent weeks collecting and organising them.
  solution: >
    Examiners connect to the client's systems through the compliance tool and pull data and
    evidence into a central real-time dashboard. KPMG describes this as letting the tool handle
    collection while the auditor concentrates on control execution and management oversight.
  outcomes:
    - {lever: speed, description: "SOC examiners say the tools make the process quicker and more efficient; no figure given", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: JOFA-FAST-2026}
  prerequisites:
    - Understanding of what data each integration returns and whether it works as intended (LINFORD-FAQ-2022)
    - Independence of the examiner from the tool provider (JOFA-SOCETH-2026)
  risks_and_guardrails:
    - "If a connection breaks, the auditor may rely on outdated data; .csv exports can be modified after generation; an auditor who does not understand how a report was generated should not rely on it (LINFORD-FAQ-2022)"
    - "A firm cannot simply download a report from the tool and issue it; due diligence on the data is required (LINFORD-FAQ-2022)"
    - "Requiring the examiner to pay the tool provider for access to evidence raises doubts about sufficient appropriate evidence (JOFA-SOCETH-2026)"
    - "Rushed or overly automated work may rely too heavily on inquiry (JOFA-FAST-2026, 'What can clients do?')"
  human_checkpoints:
    - Examiner validates source, completeness and accuracy of data from the tool, going to the source system for higher-risk controls
  role_evolution: "SOC examiners incorporate tool data into client interactions 'assuming they maintain quality' (JOFA-FAST-2026)."
  evidence_grade: C
  sources:
    - {ref: JOFA-FAST-2026, title: "Promises of 'fast and easy' threaten SOC credibility", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/", date: 2026-02-01, access: full, locator: "'The rise of SOC tool vendors'"}
    - {ref: KPMG-BEYOND-2026, title: "Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports?", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf", date: 2026-07, access: full, locator: "p.4 'From Data to Judgment'"}
    - {ref: LINFORD-FAQ-2022, title: "AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor", publisher: Linford & Co, type: firm, url: "https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs", date: 2022-06-15, access: full, locator: "risk sections"}
    - {ref: JOFA-SOCETH-2026, title: "SOC engagements: Ethics risks with tool providers", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/", date: 2026-04-06, access: full, locator: "'Obtaining sufficient evidence and meeting SSAE requirements'"}
    - {ref: AICPA-FAQ-2026, title: "FAQs - Effect of the use of software tools on SOC 2 examinations", publisher: AICPA & CIMA, type: professional-body, url: "https://www.aicpa-cima.com/resources/article/faqs-effect-of-the-use-of-software-tools-on-soc-2-r-examinations", date: 2026-03-31, access: search-only, locator: "landing page only; document behind a free login"}
  last_reviewed: 2026-10-16
  notes: "Market-wide practice described by the AICPA's magazine and KPMG; no named firm's own deployment or measurement. Linford is a 2022 foundation source (it describes the 2021 AICPA FAQ). The AICPA FAQ page is dated 31 Mar 2026 but the content was not readable, so it supports nothing here beyond its existence."

- id: assurance-soc-attestation-11
  title: Service auditor uses AI in fieldwork (population analysis, sampling, control mapping, evidence synthesis, workpaper drafting)
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types: [review-assurance, document-production, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >
    Experienced SOC staff are scarce and expensive, evidence sets are large and varied, and months
    can pass between fieldwork and the report as environments change.
  solution: >
    One advisory firm says many firms already use AI and advanced analytics to speed risk assessment,
    test selection and evidence organisation, with scoping, evidence evaluation and the opinion
    still done by people. EY speakers say AI can already help across the SOC lifecycle. The AICPA's
    TQA 9561 addresses the case where the auditor uses AI: responsibility for procedures, evidence
    evaluation and the opinion does not transfer.
  outcomes:
    - {lever: speed, description: "None published for SOC fieldwork. PKF argues AI can compress cycle time by normalising evidence and drafting consistent workpapers; no figure", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: PKF-AI-2025}
  prerequisites:
    - Governance assigning accountability for AI outputs, validating models and embedding oversight in quality control (PKF-AI-2025)
    - Corroboration of AI results by inquiry, observation, inspection and reperformance (PKF-AI-2025)
  risks_and_guardrails:
    - "AI cannot decide scope or materiality, evidence sufficiency, skepticism or independence (PKF-AI-2025, 'Limitations and challenges')"
    - "An auditor that uses AI stays accountable for the work and the opinion (SCHNEIDER-TQA-2026, section on auditor use of AI)"
    - "Entering client evidence in a generative AI tool can share it with the tool's owners; no professional standard requires telling the client (CHIARO-WHO-2026)"
  human_checkpoints:
    - Engagement lead evaluates sufficiency and appropriateness and signs the opinion
  role_evolution: "PKF frames AI as capturing institutional knowledge so new staff ramp faster and experienced staff concentrate on higher-judgment areas (PKF-AI-2025, business case)."
  evidence_grade: C
  sources:
    - {ref: PKF-AI-2025, title: "AI in SOC 2 Audits: Efficiency, Accuracy, and the Road Ahead", publisher: PKF Antares, type: firm, url: "https://www.pkfantares.com/insights/cybersecurity/ai-in-soc-2-audits-efficiency-accuracy-and-the-road-ahead/", date: 2025-11-30, access: full, locator: "Introduction; 'Business case'; 'Limitations and challenges'"}
    - {ref: SCHNEIDER-TQA-2026, title: "AI in SOC Examinations: What the AICPA's New TQA Section 9561 Means for Service Organizations", publisher: Schneider Downs, type: firm, url: "https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/", date: 2026-09-30, access: full, locator: "'When the Auditor Uses AI: Responsibility Does Not Transfer'"}
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: conference, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "p.4"}
    - {ref: CHIARO-WHO-2026, title: "Who actually looks at your SOC 2 evidence?", publisher: Chiaro (Y Assurance PLLC), type: firm, url: "https://chiarohq.com/soc-2/who-sees-your-evidence", date: 2026-10-14, access: full, locator: "section 'AI tools can see your evidence too'"}
  last_reviewed: 2026-10-16
  notes: "PKF says many firms use AI without naming any. The PKF article includes secondary statistics from McKinsey and AuditBoard/Panterra that I did not verify and did not use."

- id: assurance-soc-attestation-12
  title: AI-native audit firm that bundles readiness and the examination, tests complete populations and publishes its method (Chiaro / Y Assurance PLLC)
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types: [review-assurance, data-reporting, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >
    A buyer holding two SOC 2 reports often cannot tell whether one auditor inspected evidence and
    the other collected screenshots, because the firms' testing methods are private. Founders also
    carry evidence between tools and auditors by hand.
  solution: >
    The firm publishes its control library, test attributes, pass criteria, evidence standards and
    Type II method as machine-readable files, plus worked judgment calls used to calibrate AI. The
    customer's own AI tool connects through MCP, collects records within the permissions the
    customer grants, preserves provenance and submits them. The firm examines the evidence and signs
    the report. The default is a census of each event population, with sampling kept as a disclosed
    fallback, on the argument that AI makes looking at everything cheap.
  outcomes:
    - {lever: quality, description: "Author states that for most sample-typed attributes a proper sample would have been most of the population anyway, so the method defaults to complete populations", figure: "79 sample-typed attributes (at post time)", measures: "count of attributes in the published methodology that were sample-typed, per the author's post of 4 Aug 2026; the repository later grew from 86 controls and 355 attributes to 89 controls and 387 attributes", provenance: self-reported, source_ref: HN-CHIARO-2026}
  prerequisites:
    - Recorded retrieval for every population (exact query or command and unedited output); reconciliation against an independent second source where one exists; a management representation where none does (CHIARO-METHOD-2026, method/type2-testing)
    - Management owns controls; the examining firm separately decides conclusions (CHIARO-METHOD-2026, readiness-and-independence)
  risks_and_guardrails:
    - "The author's own caveat: a flawless census of an incomplete population proves nothing (CHIARO-METHOD-2026, method/type2-testing)"
    - "Without calibration examples a model grades itself generously (HN-CHIARO-2026, author's post)"
    - "The firm is new: one Type I issued, no Type II yet, enrolled in peer review with the first review due 2027 (HN-CHIARO-2026, author's post)"
    - "Bundling readiness with the examination touches AICPA independence rules for non-attest services (ET 1.295), which the firm says it addresses in the engagement letter (CHIARO-BUNDLE-2026)"
    - "All Chiaro sources are the firm's own marketing or a founder's post; there is no independent assessment"
  human_checkpoints:
    - Licensed CPA firm evaluates the evidence and signs the report
    - Customer decides every control choice
  role_evolution: "The founder, a CPA with five years of SOC 2 fieldwork at Deloitte, says the testing layer should be public the way standards are. Fieldwork staff are replaced in part by AI-run collection with CPA review (HN-CHIARO-2026)."
  evidence_grade: B
  sources:
    - {ref: HN-CHIARO-2026, title: "Show HN: Ex-Deloitte auditor open-sourced the whole SOC 2 method for your AI", publisher: Hacker News, type: community, url: "https://news.ycombinator.com/item?id=49171140", date: 2026-08-04, access: full, locator: "author's top-level comment; 36 points, 14 comments"}
    - {ref: CHIARO-METHOD-2026, title: "Chiaro methodology (README; method/type2-testing.md; method/readiness-and-independence.md)", publisher: Chiaro (Y Assurance PLLC), type: firm, url: "https://github.com/Chiaro-HQ/methodology", date: 2026-10, access: full, locator: "README; type2-testing sections 'Populations' and opening"}
    - {ref: CHIARO-BUNDLE-2026, title: "Is there a SOC 2 platform that includes the audit itself?", publisher: Chiaro (Y Assurance PLLC), type: firm, url: "https://chiarohq.com/soc-2/platform-that-includes-the-audit", date: 2026-10-05, access: full, locator: "TL;DR; 'Our prices are published up front'"}
    - {ref: CHIARO-AINATIVE-2026, title: "What does AI-native SOC 2 actually mean?", publisher: Chiaro (Y Assurance PLLC), type: firm, url: "https://chiarohq.com/soc-2/ai-native-auditor", date: 2026-09-11, access: full, locator: "TL;DR; table"}
  last_reviewed: 2026-10-16
  notes: "Grade B because a named firm has issued at least one Type I using the method (author statement, unverified), but there is no measurement of quality or cost and the sources are interested parties. The repository page is a live document; its date is the access month."

- id: assurance-soc-attestation-13
  title: Platform-orchestrated "bundled" SOC delivery (readiness software plus a referred CPA firm network, fixed fee and timeline), and the controversy around it
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types: [review-assurance, document-production, transaction-processing]
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    SOC 2 became a gate for enterprise sales, so buyers want it fast and cheap. A traditional
    examination takes months and tens of thousands of dollars.
  solution: >
    Tool vendors number in the dozens, promise results in weeks or hours, and act as a front door or
    intermediary, sometimes through networks of small CPA firms, with referral marketing that
    alludes to thousands of reports a year. The AICPA warns that some vendors "automate the service entirely".
    Delve is the named case: an anonymous whistleblower alleges it generated evidence and auditor
    conclusions before independent review, routed customers to a few audit firms, and hosted
    inaccurate trust pages. Delve denies the allegations and says it supplies templates and a
    platform and that licensed auditors issue the opinions.
  outcomes:
    - {lever: cost, description: "Median ballpark Type 2 price quoted to AI companies by listed firms, Q3 2026", figure: "$9,500 median (middle half $7,000 to $13,500)", measures: "median of ballparks that listed firms sent to buyers who requested SOC 2 Type 2 quotes through the directory in Jul-Sep 2026, before scoping; not final fees; AI-company row groups buyers by what their own company does", provenance: vendor-published, source_ref: SOC2AUD-AI-2026}
    - {lever: speed, description: "Shortest fieldwork-to-report time listed by any firm in the directory", figure: "1 week minimum", measures: "shortest listed fieldwork-to-report time among the 26 firms compared; a listing, not an observed result", provenance: vendor-published, source_ref: SOC2AUD-AI-2026}
  prerequisites:
    - A licensed CPA firm enrolled in peer review that sets its own scope, timing, fee and evidence access
  risks_and_guardrails:
    - "Contract terms that shift control, judgment, fees or evidence access to the tool provider can create independence and objectivity threats, including cross-referral concentration, vendor-set deadlines, bundled fees and non-disparagement clauses (JOFA-SOCETH-2026)"
    - "Engagements with identical reports, risk assessments, sample sizes and testing procedures are 'nonconforming'; reviewers may compare about five engagements from different partners (JOFA-PEER-2026)"
    - "Unlicensed signatories or firms outside peer review who sign boilerplate reports violate state law, per the AICPA's Assurance and Advisory Innovation VP (JOFA-PODCAST-2026)"
    - "A report rejected by a savvy partner is 'not worth the paper it's on' (JOFA-FAST-2026, quoting a working-group member)"
    - "Several named Delve customers are re-certifying or re-examining after the allegations (TC-DELVE2-2026)"
  human_checkpoints:
    - The licensed CPA firm performs and signs the examination
  role_evolution: "Middle-market firms face intense fee pressure and must be able to tell clients why a properly scoped and executed SOC 2 costs more (JOFA-FAST-2026). The working-group chair says the response sets a precedent for how the profession handles tool vendors if they go after financial audits (JOFA-FAST-2026)."
  evidence_grade: B
  sources:
    - {ref: JOFA-FAST-2026, title: "Promises of 'fast and easy' threaten SOC credibility", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/", date: 2026-02-01, access: full, locator: "'What's the issue?'; 'Risks for CPAs'"}
    - {ref: JOFA-SOCETH-2026, title: "SOC engagements: Ethics risks with tool providers", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/", date: 2026-04-06, access: full, locator: "'Common threats'; 'Objectivity, conflicts of interest, and independence'"}
    - {ref: JOFA-PEER-2026, title: "AICPA guides peer reviewers to address SOC 2 risks", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/", date: 2026-05-14, access: full, locator: "'A heightened focus on SOC 2 quality'; 'Responding when elevated risks are identified'"}
    - {ref: JOFA-PODCAST-2026, title: "The risks of quick-turn SOC engagements and what CPAs should know", publisher: Journal of Accountancy podcast (AICPA), type: podcast, url: "https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick‑turn-soc-engagements-and-what-cpas-should-know/", date: 2026-04-30, access: full, locator: "transcript, Pawlicki's answers on vendor automation and on state law"}
    - {ref: AICPA-SOC-LANDING-2026, title: "System and Organization Controls: SOC Suite of Services (page with notice)", publisher: AICPA & CIMA, type: professional-body, url: "https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services", date: 2026-10, access: full, locator: "'Notice' box; 'What's New' list"}
    - {ref: DEEPDELVER-2026, title: "Delve - Fake Compliance as a Service - Part I", publisher: "DeepDelver (Substack, anonymous)", type: community, url: "https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service", date: 2026-03-19, access: full, locator: "'Analyzing the leaked reports'"}
    - {ref: TC-DELVE-2026, title: "Delve accused of misleading customers with 'fake compliance'", publisher: TechCrunch (Yahoo-hosted copy), type: press, url: "https://finance.yahoo.com/sectors/technology/articles/delve-accused-misleading-customers-fake-170005937.html", date: 2026-03-21, access: full, locator: "body"}
    - {ref: TC-DELVE2-2026, title: "Another customer of troubled startup Delve suffered a big security incident", publisher: TechCrunch, type: press, url: "https://techcrunch.com/2026/04/23/another-customer-of-troubled-startup-delve-suffered-a-big-security-incident/", date: 2026-04-23, access: full, locator: "paragraphs on LiteLLM, Context AI and Lovable"}
    - {ref: IANS-DELVE-2026, title: "Delve Allegations Expose Weak Points in Compliance Services", publisher: IANS Research, type: press, url: "https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/19/delve-allegations-expose-weak-points-in-modern-compliance", date: 2026-03-24, access: full, locator: "'Key Points'; recommendations"}
    - {ref: SOC2AUD-AI-2026, title: "SOC 2 auditors for AI companies: 26 firms compared (October 2026)", publisher: SOC2Auditors.org, type: vendor, url: "https://soc2auditors.org/soc-2-auditors-ai/", date: 2026-10-09, access: full, locator: "'What firms quoted' chart and summary strip"}
  last_reviewed: 2026-10-16
  notes: "Grade B because named platforms and customers exist (TechCrunch confirmed Delve performed certifications for Context AI and that LiteLLM and Lovable were or had been customers), but the practices alleged are unproven and contested, and no outcome is independently measured. The anonymous author's analysis (575 files in the leaked dump, 494 attributed as SOC 2 reports, a sample Section 3 sentence present in 493 of them, 259 Type II reports) comes from DEEPDELVER-2026 and is unverified; IANS and others repeat it. A different restatement (533 reports across 455 companies) appears in CHIARO-VIBE-2026. The directory (SOC2Auditors.org) is a lead-generation site; its figures are asking prices. The pricing figures above describe the market, not Delve, which is reported at $6,000-$15,000 only in secondary sources I did not open."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Scoping and readiness**: choose report type (SOC 1, 2, 3, ISAE 3402), Trust Services Criteria categories, system boundary and subservice organisations (carve-out or inclusive method). `expert-judgment`, `coordination-scheduling`. Under TQA 9561 management inventories AI use against the boundary and decides what is in or out (SCHNEIDER-TQA-2026).
- **System description and management assertion** (Section 3): `document-production`. The description is management's; practitioners treat a generic one as the clearest template tell (CHIARO-VIBE-2026; KPMG-BEYOND-2026, p.5).
- **Control design, risk assessment and gap assessment**: `review-assurance`. KPMG says dashboards can mislead without a robust risk assessment (KPMG-BEYOND-2026, p.3).
- **Engagement acceptance and independence** (including any tool-provider relationship): `review-assurance`. Routed to acceptance-independence.
- **Planning**: examination period, procedures, sample sizes. `expert-judgment`. The Peer Review Board flags identical risk assessments and sample sizes across clients (JOFA-PEER-2026).
- **Evidence collection**: requests, platform integrations, screenshots. `data-reporting`, `coordination-scheduling`. The most automated step (EY poll 63%; JOFA-FAST-2026).
- **Testing**: inquiry, observation, inspection, reperformance, sampling. `review-assurance`. Individual tests belong to controls-testing. KPMG warns against over-reliance on inquiry and "test of one" procedures (KPMG-BEYOND-2026, p.5).
- **Deviations and management responses**: evaluate, root-cause, respond, assess effect on the opinion. `expert-judgment`, `document-production`.
- **Reporting**: opinion, Sections 3 and 4, distribution. `document-production`. EY says a cyber incident may lead an auditor to modify an opinion, restrict distribution or withdraw an issued report (EY-SOC-2025, p.10).
- **Post-issuance**: customer questionnaires, trust center, annual renewal. `client-interaction`. The AICPA notes the service should be repeated annually because things change (JOFA-PODCAST-2026).
- **Firm quality and peer review**: `review-assurance`. Routed to quality-management.

### Common pain points

- Evidence arrives as screenshots and Excel files; user access reviews are highly manual and approvers rubber-stamp them (EY-SOC-2025, p.5).
- Pressure to match the speed and price of high-volume "SOC shops", which conflicts with independence, skepticism, competent staff, partner involvement and tailored procedures (JOFA-FAST-2026, 'How can SOC examiners respond?').
- Buyers treating SOC 2 as a pass/fail credential, and a report that satisfies an intake checklist but fails legal or vendor-risk review (CERTPRO-QUALITY-2026; BAKERTILLY-TRUST-2026).
- Tool vendors dominating online search for SOC 2 services through search-engine investment (JOFA-FAST-2026).
- Evidence gaps because of poor scoping: a test scoped to human users misses service accounts, so the dashboard is green while the auditor is not satisfied (SCRUT-EVIDENCE-2026).
- Shadow AI and informal AI vendors outside the system description (SCHNEIDER-TQA-2026; FORTUNE-VANTA-2026).

### Metrics and benchmarks

| Figure | What it measures (source's words) | Source | Provenance |
|---|---|---|---|
| 63% / 45% / 41% / 29% | Evidence collection / updating Section 3 / drafting management responses to deviations / project management, share of selections in a live poll of conference attendees, multiple selections allowed (n not stated) | EY-SOC-2026, p.5 | self-reported |
| 71% | Share of conference participants ranking their risk management maturity as 7 or lower out of 10 | EY-SOC-2026, p.7 | self-reported |
| 52% and 40% | Share of SOC 1 deviations and of SOC 2 deviations that were logical-access related, in an EY survey of more than 2,000 SOC reports supporting customers' 2024 and 2025 financial audits | EY-SOC-2025, p.4 | self-reported (firm) |
| 4 hours per week | Average time saved per customer by the Vanta AI Agent, per Vanta | VANTA-HNS-2025 | vendor-published |
| $300M ARR; 16,000+ customers | Vanta, per Fortune, from the company | FORTUNE-VANTA-2026 | vendor-published |
| $9,500 median | Ballpark SOC 2 Type 2 price quoted to AI companies, Jul-Sep 2026, before scoping | SOC2AUD-AI-2026 | vendor-published |
| about 5 engagements | Number a peer-review team will often select from different partners when risk is elevated | JOFA-PEER-2026 | independent (standard-setter staff guidance) |
| 493 of 494 | Delve allegation: files containing one sample Section 3 sentence in the anonymous author's dump (unverified; disputed) | DEEPDELVER-2026 | self-reported (anonymous) |
| 23 responses, closed 30 Jun 2026 | AICPA ASB exposure draft revising AT-C 105, 205, 210 (issued 26 Feb 2026), per a secondary source | BRIGHT-ATC-2026 | vendor-published (secondary) |

**Quality evidence: none of the independent kind was found.** No error rate, override rate, parallel-run result or inspection outcome exists in public sources for AI in SOC work. AICPA peer-review outcomes for SOC 2 practices have not been published. The only measurements are firm polls, a firm's deviation survey, vendor averages and asking prices.

### Guardrails and regulatory points

- SOC 2 is an examination-level attestation by a licensed CPA under AICPA attestation standards (AT-C 205), not a certification; the same level of assurance as a financial statement audit, per the AICPA's VP (JOFA-PODCAST-2026).
- Unlicensed signatories, or firms not enrolled in peer review that sign SOC reports, violate state law; the AICPA says it will act against members and assist state boards (JOFA-PODCAST-2026; AICPA-SOC-LANDING-2026).
- Tool-provider arrangements are judged under the AICPA Code (independence, objectivity, compliance with standards, fees); where safeguards cannot remove a significant threat, performing the examination is not appropriate (JOFA-SOCETH-2026).
- TQA 9561 (11 Sep 2026): AI creates no separate SOC model and no new criteria; relevance depends on whether AI is in the services delivered or only in internal processes; third-party AI providers go through the subservice-organisation (inclusive or carve-out) analysis; auditors using AI remain responsible; avoid scope inflation (SCHNEIDER-TQA-2026; DART-TQA-2026, which dates its note 21 Sep 2026). The full text is behind a login and was not read. The AICPA's 13 Oct 2026 practice-aid coverage lists the TQA among AI resources issued earlier in 2026 (JOFA-AIPA-2026).
- No AI-specific Trust Services Criteria or points of focus exist, per the Cloud Security Alliance's AI-assisted note, which also says auditors request model-lineage, inference-logging, drift-monitoring and AI-subprocessor evidence on their own initiative (CSA-SOC2-2026). That is secondhand and not CSA-reviewed.
- The 2026 sequence of SOC 2 quality actions (1 Feb, 6 Apr, 30 Apr, 14 May, 1 Jun) is consistent across secondary summaries (BRIGHT-QUALITY-2026).
- ASB exposure drafts revising AT-C 105, 205 and 210 (26 Feb 2026) are at the "discuss comment letters" stage and not final (BRIGHT-ATC-2026, secondary; I could not confirm on an AICPA page).
- Entering client evidence in generative AI tools may share it with the tool's owners; the AICPA Code's confidentiality guidance on outside service providers applies, and no standard specifically requires disclosing AI use (CHIARO-WHO-2026).
- AI scoping example: Fabasoft's ISAE 3402 Type 2 report covering its Fabasphere AI Core was issued by PricewaterhouseCoopers GmbH in April 2026 for 1 Jan-31 Dec 2025 (FABASOFT-ISAE-2026). It shows an AI product inside an ISAE 3402 examination; it says nothing about how AI was tested.

### Frontier signals (dated)

- 2025-11-19: Vanta's "Agentic Trust Platform" and AI Agent 2.0, an agent positioned as a 24/7 GRC engineer (VANTA-HNS-2025).
- 2026-02-01: AICPA SOC 2 Working Group chair warns of "fast and easy"; AICPA is exploring a SOC Quality Center as a quality badge; the Working Group is producing user education and assessing SOC 2 report usability (JOFA-FAST-2026).
- 2026-01-09: an Ask HN thread repeats a rumour about fraudulent SOC 2 certifications through Delve and participating audit firms, two months before the whistleblower post (HN-DELVE-2026).
- 2026-03-19: DeepDelver's allegations. By 2026-04-23 TechCrunch reports that Y Combinator, where Delve graduated, had severed ties (TC-DELVE2-2026).
- 2026-04-06 / 2026-04-13: AICPA ethics article and staff insights on tool-provider arrangements (JOFA-SOCETH-2026; AICPA-SOC-LANDING-2026).
- 2026-05-14 and 2026-06-01: Peer Review Board reviewer alert and outreach to team captains of scheduled reviews of firms with SOC 2 practices; enhanced oversight continues (JOFA-PEER-2026).
- 2026-05-02: the term "vibe compliance" appears in practitioner writing, defined as compliance that "looks done on paper but was never tested" (CHIARO-VIBE-2026).
- 2026-08-04: an AI-native audit firm publishes its method and defaults to complete-population testing (HN-CHIARO-2026); 2026-10-05: it markets a platform that includes the audit (CHIARO-BUNDLE-2026).
- 2026-08-30: CSA note says the AICPA should treat AI-specific criteria as a priority alongside its SOC 2 quality work (CSA-SOC2-2026, secondary and AI-assisted).
- 2026-09-11 / 2026-09-24: TQA 9561; EY's 14th conference centred on AI assurance, with the poll above (SCHNEIDER-TQA-2026; EY-SOC-2026).
- 2026-11-12 (upcoming): VantaCon 2026, billed as "the AI governance event" for 650+ practitioners (VANTACON-2026).
- Direction of travel stated by the AICPA: use of tools is fine; the process must remain independent, tailored and tested (JOFA-PODCAST-2026; JOFA-PEER-2026).

### Workforce and role effects

- Compliance staff move from evidence chasers toward "GRC engineers" and exception reviewers (VANTACON-2026 speaker titles; SCRUT-EVIDENCE-2026 step 6).
- Examiners must resist pressure to cut hours and explain to clients why quality costs more; middle-market firms face fee pressure (JOFA-FAST-2026).
- Junior-heavy examination teams, outsourced or offshore evidence review and AI tools raise confidentiality questions that buyers are being told to ask (CHIARO-WHO-2026; JOFA-FAST-2026 on firms in tool-vendor networks, "sometimes with overseas operations").
- Vendor-risk teams are told to treat a report as the start of due diligence and to vet the signing CPA and firm (KPMG-BEYOND-2026; WHISTIC-DELVE-2026).
- EY has named "chief data strategy officers" as a rising hire for AI governance (EY-SOC-2026, p.6).

### Objections and concerns practitioners raise

- Dashboard extraction substitutes for inquiry, inspection and testing (CSA-SOC2-2026, citing the SOC 2 Working Group; BAKERTILLY-TRUST-2026).
- Tool-provider referral, fee and deadline control creates independence threats (JOFA-SOCETH-2026).
- Templated reports: the Working Group's O'Brien said five of some firms' reports differ only by logo (JOFA-FAST-2026). The Peer Review Board calls this nonconforming (JOFA-PEER-2026).
- "SOC 2 certification" and "compliance" are misleading labels (JOFA-PODCAST-2026; JOFA-FAST-2026).
- AI may invent details, rewrite itself or work around anomalies; human oversight is still required (EY-SOC-2026, p.5).
- Scope inflation: adding an "AI section" to every report is the wrong reaction to TQA 9561 (SCHNEIDER-TQA-2026).
- AI marketing versus reality: the whistleblower says Delve's product was practically devoid of real AI, which Delve did not address (DEEPDELVER-2026; TC-DELVE-2026).
- Regulators are unlikely to step in, so buyers must reassess due diligence themselves (CPN-WEEDS-2026, show notes).
- The standards gap for AI-vendor reports: two clean SOC 2 reports may test different AI controls (CSA-SOC2-2026, secondary).
- One bad report goes viral on LinkedIn and damages the whole service (JOFA-FAST-2026, quoting a Baker Tilly principal).

### Interview probes for an advisor

1. "What share of your SOC 2 work arrives through a tool-vendor referral or a bundled package, and who sets the fee, scope and timeline when it does?"
2. "How do you decide that evidence pulled by a compliance platform is complete and unaltered? What do you re-perform at the source system, and for which controls?"
3. "Where do you draw the line on AI-drafted text, such as Section 3, deviation responses or test conclusions? What would you need to see before an AI-run census counts as sufficient appropriate evidence?"
4. "When a client says it puts an LLM in the product or uses foundation-model providers, what changes in your scoping, system description and carve-out analysis under TQA 9561?"
5. "On the user-entity side, what has changed in how you read a vendor's SOC report since March 2026, and who does the reading?"

---

## 4. Routed to other modules

- **Assurance over AI systems (the other-assurance split, module name not yet set):**
  - JOFA-NEWFRONTIER-2025 (1 Nov 2025): AI "audits" are expected to resemble SOC engagements; one commentator prefers "assurance over AI" or "evaluation report"; EY says it is updating SOC reports and attestation offerings across the AI lifecycle; practitioners predict narrow-scope, technology-specific criteria if no US standard appears.
  - EY-SOC-2026 pp.2-3: AI is not a checklist of control points, so attestation is more complex; providers may need to show lifecycle controls and monitoring.
  - CSA-SOC2-2026: practitioner overlays, "STAR for AI" and a combined SOC 2 + AI Controls Matrix attestation idea (secondary). A named ISO 42001 / AIUC-1 cluster (for example Schellman's "Decoding AI Assurance" article) surfaced on a listing page and was not opened.
  - TQA 9561 scoping advice for AI in SOC scope (SCHNEIDER-TQA-2026, DART-TQA-2026) and the Fabasoft ISAE 3402 example (FABASOFT-ISAE-2026).
- **Controls-testing:** EY-SOC-2025 p.4-5 (access-related deviations, manual user access reviews, IAM automation for de-provisioning and review); SCRUT-EVIDENCE-2026 six-step evidence chain; the pilot already covers platform-fed examiners (use case 10 overlaps with its platform use case).
- **Acceptance-independence:** JOFA-SOCETH-2026 in full (cross-referral, bundled fees, tool provider in a network firm or alternative practice structure); readiness-versus-examination independence under ET 1.295 (CHIARO-BUNDLE-2026, CHIARO-METHOD-2026).
- **Quality-management:** JOFA-PEER-2026 (single file review often insufficient; follow-up actions include revising the system of quality management or outside review of completed engagements; enhanced oversight by a subject-matter expert).
- **Completion-reporting:** EY-SOC-2025 p.10 (cyber incident effects on opinions and distribution).
- **Sustainability assurance:** the AICPA ASB exposure draft adds sustainability-specific provisions (BRIGHT-ATC-2026, secondary).
- **Planning / substantive testing:** JOFA-TRANSFORM-2026 (1 Feb 2026) quotes a Citrin Cooperman partner describing agents that fill workpapers from ledger data and send and review cash confirmations; the article is about financial statement audits.

---

## 5. Sources

Counts: 40 sources. Conference 3; professional-body 9; firm 12; vendor 6; press 5; podcast 2; community 3. No regulator, standard-setter (primary text), academic or job-posting sources were found (see Gaps). Access is `full` unless marked.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| EY-SOC-2026 | How AI assurance builds trust with SOC, attestation and certification (14th annual EY SOC, Attestation and Certification Conference highlights) | EY | conference | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf | 2026-09 |
| EY-SOC-2025 | How to build trust and confidence in technology through assurance reporting (13th annual EY SOC Reporting Conference highlights) | EY | conference | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-ch/insights/technology-risk/documents/ey-13th-annual-soc-reporting-conference-highlights.pdf | 2025-08 (PDF metadata) |
| VANTACON-2026 | VantaCon 2026: The AI governance event | Vanta | conference | https://www.vanta.com/vantacon | 2026-11-12 (event date) |
| AICPA-SOC-LANDING-2026 | System and Organization Controls: SOC Suite of Services (page with notice and What's New list) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services | 2026-10 (accessed) |
| AICPA-FAQ-2026 | FAQs - Effect of the use of software tools on SOC 2 examinations (landing page only; document behind login) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/article/faqs-effect-of-the-use-of-software-tools-on-soc-2-r-examinations | 2026-03-31 (`search-only`) |
| JOFA-FAST-2026 | Promises of 'fast and easy' threaten SOC credibility | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/ | 2026-02-01 |
| JOFA-SOCETH-2026 | SOC engagements: Ethics risks with tool providers | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 |
| JOFA-PEER-2026 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| JOFA-NEWFRONTIER-2025 | A new frontier: CPAs as AI system evaluators | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2025/nov/a-new-frontier-cpas-as-ai-system-evaluators/ | 2025-11-01 |
| JOFA-TRANSFORM-2026 | How AI is transforming the audit and what it means for CPAs | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/how-ai-is-transforming-the-audit-and-what-it-means-for-cpas/ | 2026-02-01 |
| CSA-SOC2-2026 | The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted (AI-assisted, not CSA-reviewed) | Cloud Security Alliance | professional-body | https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/08/CSA_research_note_soc2_ai_controls_gap_20260830-csa-styled.pdf | 2026-08-30 |
| DART-TQA-2026 | AICPA Releases TQAs on a Service Organization's Use of AI | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/news/all-news/2026/sep/aicpa-releases-tqas-service-organization-use-ai | 2026-09-21 |
| KPMG-BEYOND-2026 | Beyond the Checkbox: How Confident Are You in Your SOC 2 Reports? | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/beyond-checkbox.pdf | 2026-07 (PDF metadata; cites 14 May 2026) |
| BAKERTILLY-TRUST-2026 | Why trust in SOC 2 still comes down to more than efficiency | Baker Tilly | firm | https://www.bakertilly.com/insights/trust-in-soc-2-report-efficiency | 2026-05-26 |
| SCHNEIDER-TQA-2026 | AI in SOC Examinations: What the AICPA's New TQA Section 9561 Means for Service Organizations | Schneider Downs | firm | https://schneiderdowns.com/our-thoughts-on/ai-in-soc-examinations-what-the-aicpas-new-tqa-section-9561-means-for-service-organizations/ | 2026-09-30 |
| PKF-AI-2025 | AI in SOC 2 Audits: Efficiency, Accuracy, and the Road Ahead | PKF Antares | firm | https://www.pkfantares.com/insights/cybersecurity/ai-in-soc-2-audits-efficiency-accuracy-and-the-road-ahead/ | 2025-11-30 |
| CERTPRO-QUALITY-2026 | SOC 2 Audit Quality in 2026: What Recent Industry Scrutiny Means for Buyers | CertPro CPA | firm | https://certpro.com/soc-2-report-quality-in-2026/ | 2026-06-19 |
| LINFORD-FAQ-2022 | AICPA FAQs on SOC 2 Automation Tools: Insights from an Auditor (foundation only) | Linford & Co | firm | https://linfordco.com/blog/soc-2-automation-tools-aicpa-faqs | 2022-06-15 |
| CHIARO-VIBE-2026 | What is vibe compliance? | Chiaro (Y Assurance PLLC) | firm | https://chiarohq.com/soc-2/vibe-compliance | 2026-05-02 |
| CHIARO-AINATIVE-2026 | What does AI-native SOC 2 actually mean? | Chiaro (Y Assurance PLLC) | firm | https://chiarohq.com/soc-2/ai-native-auditor | 2026-09-11 |
| CHIARO-BUNDLE-2026 | Is there a SOC 2 platform that includes the audit itself? | Chiaro (Y Assurance PLLC) | firm | https://chiarohq.com/soc-2/platform-that-includes-the-audit | 2026-10-05 |
| CHIARO-WHO-2026 | Who actually looks at your SOC 2 evidence? | Chiaro (Y Assurance PLLC) | firm | https://chiarohq.com/soc-2/who-sees-your-evidence | 2026-10-14 |
| CHIARO-METHOD-2026 | Chiaro methodology repository (README; type2-testing; readiness-and-independence) | Chiaro (Y Assurance PLLC) | firm | https://github.com/Chiaro-HQ/methodology | 2026-10 (accessed; live document) |
| SCRUT-EVIDENCE-2026 | Automated evidence collection: How it actually works and where it fails | Scrut | vendor | https://www.scrut.io/post/how-automated-evidence-collection-works | 2026-05-11 |
| WHISTIC-DELVE-2026 | Your Vendor Has a SOC 2 Report. Now What? | Whistic | vendor | https://www.whistic.com/resources/blog/your-vendor-has-a-soc-2-report-now-what | 2026-03 (inferred from footnotes dated 19-23 Mar 2026) |
| SOC2AUD-AI-2026 | SOC 2 auditors for AI companies: 26 firms compared (October 2026) | SOC2Auditors.org | vendor | https://soc2auditors.org/soc-2-auditors-ai/ | 2026-10-09 (updated; first dated 2026-05-19) |
| FABASOFT-ISAE-2026 | ISAE 3402 Type 2 | Fabasoft | vendor | https://www.fabasoft.com/en/certifications/isae-3402-type-2 | 2026-04 (report issue date) |
| BRIGHT-ATC-2026 | AICPA Advances 2026 Attestation Changes for SOC 2 (secondary) | Bright Defense | vendor | https://www.brightdefense.com/news/aicpa-advances-2026-attestation-changes-for-soc-2/ | 2026-08-27 |
| BRIGHT-QUALITY-2026 | SOC 2 Audit Quality Faces New Pressure As Vendor Risk Grows (secondary; timeline only) | Bright Defense | vendor | https://www.brightdefense.com/news/soc-2-audit-quality-faces-new-pressure-as-vendor-risk-grows/ | 2026-06-21 |
| VANTA-HNS-2025 | Vanta's Agentic Trust Platform redefines how enterprises earn, prove, and scale trust | Help Net Security (Vanta release) | press | https://www.helpnetsecurity.com/2025/11/19/vanta-agentic-trust-platform/ | 2025-11-19 |
| FORTUNE-VANTA-2026 | Exclusive: Vanta hits $300 million ARR as 'shadow AI' explodes across corporate America | Fortune | press | https://fortune.com/2026/04/29/exclusive-vanta-arr-300-million-sequoia-shadow-ai-claude-cursor/ | 2026-04-29 |
| TC-DELVE-2026 | Delve accused of misleading customers with 'fake compliance' | TechCrunch (Yahoo-hosted copy) | press | https://finance.yahoo.com/sectors/technology/articles/delve-accused-misleading-customers-fake-170005937.html | 2026-03-21 (original; copy dated 2026-03-22) |
| TC-DELVE2-2026 | Another customer of troubled startup Delve suffered a big security incident | TechCrunch | press | https://techcrunch.com/2026/04/23/another-customer-of-troubled-startup-delve-suffered-a-big-security-incident/ | 2026-04-23 |
| IANS-DELVE-2026 | Delve Allegations Expose Weak Points in Compliance Services | IANS Research | press | https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/19/delve-allegations-expose-weak-points-in-modern-compliance | 2026-03-24 |
| JOFA-PODCAST-2026 | The risks of quick-turn SOC engagements and what CPAs should know (podcast with transcript) | Journal of Accountancy podcast (AICPA) | podcast | https://www.journalofaccountancy.com/podcast/2026/apr/the-risks-of-quick‑turn-soc-engagements-and-what-cpas-should-know/ | 2026-04-30 |
| CPN-WEEDS-2026 | Compliance into the Weeds: AI-Driven SOC Audits and the Growing Trust Gap (show notes only; audio not heard) | Compliance Podcast Network | podcast | https://compliancepodcastnetwork.net/compliance-into-the-weeds-ai-driven-soc-audits-and-the-growing-trust-gap/ | 2026-04-01 |
| DEEPDELVER-2026 | Delve - Fake Compliance as a Service - Part I (anonymous allegations; unverified) | DeepDelver (Substack) | community | https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service | 2026-03-19 |
| HN-DELVE-2026 | Ask HN: Delve AI Audit Fraud | Hacker News | community | https://news.ycombinator.com/item?id=46549252 | 2026-01-09 |
| HN-CHIARO-2026 | Show HN: Ex-Deloitte auditor open-sourced the whole SOC 2 method for your AI | Hacker News | community | https://news.ycombinator.com/item?id=49171140 | 2026-08-04 |

---

## 6. Gaps

**Not found or not run (search budget exhausted partway):**
- No academic or working-paper work on SOC report quality, tool-vendor effects or AI in SOC examinations. None was searched for after the budget ran out.
- No job-posting evidence. VantaCon speaker titles are the only role-structure signal.
- No regulator source (a state board of accountancy action, for example). The AICPA says it refers matters to state boards but no referral outcome is public.
- No independent quality measurement: no error, override or parallel-run data; no published peer-review results for SOC 2 practices; no accuracy test of any AI SOC tool.
- ISAE 3402 / ISAE 3000 outside the US: no practitioner discourse found. One named AI-in-scope ISAE 3402 report (Fabasoft, PwC GmbH, Apr 2026) only.
- Bridge (gap) letters, SOC 3, SOC for Cybersecurity, SOC for Supply Chain and "other attestation engagements": no discourse located in this pass.
- Trust centers: only vendor products (Whistic, Chiaro), an allegation about inaccurate trust pages, and IANS's advice. No buyer survey or usage data.
- Conference coverage is thin: only EY's SOC conference (14th and 13th) and VantaCon (upcoming) were read. The AICPA ENGAGE 2026 agenda was not reachable, and no SOC-specific session list was found there. The KPMG US SOC webcast named in the landscape (KPMG-SOC-2026) was not re-opened because its URL was not available.

**Blocked or unreadable:**
- 403: Reddit (the r/soc2 thread referenced from the Hacker News post), Corporate Compliance Insights ("SOC 2 Is Broken", cited in the pilot), Drata, A-LIGN (State of Compliance 2026), Schneider Downs' "What compliance automation can't tell you", Benzinga, Sprinto. The Vanta State of Trust 2025 press release failed on connection.
- AICPA TQA 9561 text, the AICPA FAQ on software tools, and the AICPA ethics staff insights document were not readable (login or not found). They are known only through JofA, Deloitte DART and Schneider Downs.
- Audio for the Compliance into the Weeds episode and the JofA podcast were not heard; the JofA transcript was read, the CPN show notes only.

**Source-quality limits:**
- Delve allegations are unproven and disputed. The 493-of-494 analysis is the anonymous author's and I did not verify it. Counts differ between sources (575 files with 494 attributed as SOC 2 in the original; 533 reports across 455 companies in Chiaro's restatement).
- The CSA note says it was AI-assisted and not CSA-reviewed and relies on references I did not open (SOC2Auditors.org, Baker Tilly 2025, CSA's own documents).
- Bright Defense pieces appear to be vendor-site summaries; the ASB exposure-draft dates and the 23 comment letters were not confirmed on an AICPA page.
- SOC2Auditors.org is a lead-generation directory; its price medians are asking prices from the directory's own users, not paid fees.
- Chiaro, Whistic, Scrut and Vanta are interested parties. Their statements about their own products are claims.
- A Fieldguide article on automating SOC evidence collection was read but is undated, so it is not cited.
- The EY poll sizes are not stated.

**Overlap with the pilot:** the pilot's controls-testing discourse file already contains several SOC quality items (S25-S32). This file confirms those by direct reading and adds Baker Tilly, KPMG, the AICPA notice, TQA 9561 commentary, the AICPA podcast, the EY 13th and 14th conferences, the Chiaro material and the Delve source set.
