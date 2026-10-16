# Module deep dive: assurance / acceptance-independence. Angle: governance & evidence

- **Archetype:** assurance
- **Module:** acceptance-independence. Client and engagement acceptance and continuance, independence and ethics (conflicts, prohibited non-audit services, financial relationships, rotation), KYC/AML, engagement letters and client risk profiling. Two directions: (1) AI tools used in acceptance, KYC/AML and independence monitoring; (2) AI-driven structural change creating acceptance risk and independence threats (private-equity investment in firms, alternative practice structures, firms' relationships with AI tool vendors, providing AI services or tools to audit clients).
- **Angle:** governance & evidence. Regulator and standard-setter positions (AICPA PEEC drafts, SEC OCA, PCAOB independence work and PE statements, IESBA technology and NAS provisions, FRC ethical standard, AML regulators), the AICPA AI practice aid's acceptance sections, academic work and surveys.
- **Prepared:** 2026-10-16
- **Method note.** Pages were fetched with `curl` through the session proxy and PDFs read with `pdftotext`. About 55 sources are listed in section 5; each carries an `access` value. Where a page was paywalled, member-gated or blocked, section 6 says so. The web-search quota ran out partway through the task, so the last planned searches (the AICPA practice aid's full text, acceptance-tool case studies) were not run. Source keys follow `PUBLISHER-SHORT-YYYY` and reuse the landscape's keys where the document is the same. Quotations are under 25 words.

---

## 1. Summary

**What the rules and regulators say (as of 16 Oct 2026).** No regulator or standard-setter read here prohibits AI in acceptance, KYC or independence work. Their attention is on two other things: the independence consequences of private capital and tool-vendor relationships, and the new acceptance question of how heavily a client relies on AI.

- **PEEC (AICPA).** The alternative-practice-structure (APS) project is on its way to a second exposure draft. PEEC discussed a revised network-firm definition and a new interpretation barring attest-client investment in firms (JOFA-PEEC-2026). The committee meets virtually on 19 Oct 2026 to decide on it (AICPA-PEECMEET-2026, AICPA-PEECWEBCAST-2026), three days after this report. One commentator, a former PCAOB board member who now works at an AI-native audit firm, says ambiguity remains on when licensing an AI audit tool becomes an independence issue, and that none of the 81 comment letters came from a technology company (AT-PEEC-2026).
- **SEC Office of the Chief Accountant.** Chief Accountant Kurt Hohl says the OCA is reviewing whether independence rules stay fit for purpose as private equity and AI arrive. The review starts with a refresh of independence FAQs, then a joint look with the PCAOB at the interim independence standards. He calls the SEC "in listening mode" and denies any plan to weaken the rules (TR-HOHL-2026, NYSSCPA-HOHL-2026). In an earlier interview he named partnerships with AI companies as a complication (STARLING-HOHLWSJ-2026).
- **PCAOB.** Independence is on the new standard-setting agenda (JOFA-PCAOBAG-2026). Inspections director Christine Gunia said in Dec 2025 that inspections would look at quality safeguards at firms that have taken, or are considering, PE deals (BLOOMBERG-PCAOBPE-2025, partly paywalled).
- **IESBA.** It decided in March 2026 to gather information on PE and other outside investment before deciding on a standard-setting project, and approved terms of reference in June 2026 (APESB-IESBACHAIR-2026, IESBA-HIGHLIGHTS-2026). On AI it has chosen no new Code changes for now. A staff publication on emerging technologies followed on 15 Jul 2026 (IESBA-NAM-2026), and an AI-specific publication is planned for Q4 2026 (IESBA-SNAPSHOT-2026).
- **UK.** The FRC's 2024 letter says it is not in principle against external private capital, and asks firms to engage with it early (FRC-PCLETTER-2024). ICAEW says an audit firm acquired by a PE fund may not audit the fund or its portfolio companies (ICAEW-PE-2024). The UK AML strategy published 15 Sep 2026 expects AI and digital ID to play a larger part in customer due diligence, and has the FCA publishing good and poor practice examples on AI in 2026-27 (UKGOV-AMLSTRAT-2026).
- **The AICPA practice aid (13 Oct 2026)** adds a new acceptance and continuance factor: the more a client relies on AI outputs in financial reporting, the more the auditor may need to know before accepting, for example whether evidence can be gathered when agents run without traceable workflows (AT-AICPAPA-2026).

**What is measured.** Almost nothing about AI inside acceptance, KYC or independence monitoring.
- No error rate, override rate, parallel-run result, inspection finding or independent benchmark was found for any AI tool used in these steps.
- The only quantitative item on a related step is a survey count: 26% of 54 firms with complete data said they have an automated solution for engagement letters, which is automation, not AI (CPACOM-ATR-2025, p. 10).
- Academic work is a 2024 prototype for client-acceptance scoring that is illustrated by one case study (CEBI-2024), a 2025 experiment summary on AI and liability perceptions (LIBBY-CIIA-2025), and a registered report on PE in audit firms that has no results yet (NYK-TAR-2024).

**Evidence grades.** Fourteen use cases: 0 grade A, 0 grade B, 6 grade C (vendor or firm claims, no measurement), 8 grade D (ideas that regulators, standard-setters or researchers actually discuss).

**Two most important insights.**
1. **The governance action is on structure and vendor relationships, not acceptance tooling.** PEEC, the SEC, the PCAOB and IESBA are all working on who may own firms and which relationships impair independence. The SEC links that work to AI explicitly, IESBA runs parallel PE and technology workstreams, and a commentator reads the PEEC draft as reaching AI tool licensing. Meanwhile the FRC's generative-AI guidance does not mention acceptance or independence at all (FRC-GENAI-2026). The open question for firms is practical: when an AI tool or platform comes from an affiliate, an investor-backed entity or a vendor, who reviews that relationship, using what test?
2. **AI in acceptance, KYC and independence monitoring is a claim, not a measured result.** Evidence is vendor pages (Kingland), a prototype paper and regulator encouragement (UK AML strategy). The regulators who do speak say responsibility stays with people: ICAEW says technology should support, not replace, professional judgement (ICAEW-AML-2026), and it warns that many electronic verification services screen for sanctions, politically exposed persons (PEPs) and adverse media rather than verify identity.

---

## 2. Use cases

Notes on reading this block:
- Use cases 07 to 14 are mostly direction 2. Where the AI belongs to the client, the vendor or an affiliate rather than the firm's own acceptance tool, the `ladder` value is `assist` only because the vocabulary needs a value, and the entry's `notes` say so.
- `function` is `risk-compliance-legal` for firm-internal independence, ethics and AML work, and `service-delivery` where the change is in client-facing engagement work.
- Every outcome is `none published` unless a figure is stated.

```yaml
- id: assurance-acceptance-independence-01
  title: "Acceptance and continuance workflow that routes risk, independence, conflict and KYC checks to reviewers (vendor platform)"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ review-assurance, coordination-scheduling ]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Acceptance and continuance decisions draw on independence, conflict, reputational and KYC information held in separate systems and reviewed by different people. The vendor describes the starting point as manual and spreadsheet-driven."
  solution: "Kingland describes a workflow that pulls client data into one case, applies firm-set questions, thresholds and decision logic with built-in risk indicators, embeds KYC activity, and routes the case to reviewers for sign-off, for initial acceptance and for continuance. The vendor's pages describe its AI framework (several foundation models, version control, confidence scoring, human-in-the-loop oversight) in general terms but do not say which acceptance steps use AI."
  outcomes:
    - { lever: risk, description: "Vendor says the workflow aggregates independence, conflicts and reputational risk signals in one place and gives regulators and internal stakeholders an audit trail. No measured result.", figure: "none published", measures: "not applicable: descriptive vendor claim only", provenance: vendor-published, source_ref: KINGLAND-ACCEPT }
  prerequisites:
    - "Firm-defined acceptance criteria, thresholds and decision logic (KINGLAND-ACCEPT)"
    - "Integration with the firm's existing systems so that acceptance is triggered at the right time (KINGLAND-ACCEPT)"
    - "Reliable entity and relationship data, see use case 02"
  risks_and_guardrails:
    - "IESBA staff say a vendor may update software or change algorithms without full transparency, and that this is new information requiring the accountant to re-evaluate the threat and the safeguards (IESBA-NAM-2026, PDF p. 10)"
    - "IESBA lists overreliance on vendor assurances and limited transparency into vendor controls among the circumstances that amplify threats where outputs are opaque (IESBA-NAM-2026, PDF p. 14, Appendix table)"
    - "No customer name, error rate or override rate is published, so decision quality is unverified (KINGLAND-ACCEPT)"
  human_checkpoints:
    - "Reviewer sign-off on each acceptance and continuance decision (KINGLAND-ACCEPT)"
    - "Higher-risk conflicts routed to appropriate reviewers (KINGLAND-PA-2026, Conflict Checking section)"
  role_evolution: "The vendor says the routing lets a firm focus attention where risk is highest. No source measures this (KINGLAND-ACCEPT)."
  evidence_grade: C
  sources:
    - { ref: KINGLAND-ACCEPT, title: "Client & Engagement Acceptance", publisher: Kingland, type: vendor, url: "https://www.kingland.com/client-engagement-acceptance", date: 2026-10-16, access: full, locator: "page body; the page is undated and the date given is the access date" }
    - { ref: KINGLAND-PA-2026, title: "Public Accounting", publisher: Kingland, type: vendor, url: "https://www.kingland.com/public-accounting", date: 2026-10-16, access: full, locator: "Conflict Checking and AI framework sections; undated page, access date given" }
    - { ref: IESBA-NAM-2026, title: "Emerging Technologies: A Characteristics-Based Approach to Ethical Considerations for Professional Accountants", publisher: IESBA, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-07/Emerging-Technologies-Ethical-Considerations-for-Professional-Accountants.pdf", date: 2026-07-15, access: full, locator: "PDF pp. 10 and 14" }
  last_reviewed: 2026-10-16
  notes: "Vendor claims only. The vendor's statement that it is trusted by top global firms and networks names no customer. Intapp, the other acceptance and conflicts vendor in the landscape, blocked access (HTTP 403) so was not read."

- id: assurance-acceptance-independence-02
  title: "AI extraction of client ownership and subsidiary structures from documents into relationship trees used for independence and conflict checks"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ data-reporting, review-assurance ]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Independence and conflict checks depend on a complete map of a client's affiliates and related entities, which is often built by hand from filings and client-supplied documents."
  solution: "Kingland says its client-data and family-tree tool draws on internal client databases, third-party providers and public sources such as SEC filings, and uses AI to read client documents (PDFs or images) describing subsidiary relationships, extracting ownership details into a family tree that the user then completes. Its restricted-list tool holds entity records, ownership structures and affiliate relationships for use across acceptance, conflicts and service approval."
  outcomes:
    - { lever: quality, description: "Vendor says a single source of truth for entity and affiliate records supports consistent identification of restrictions. No measured result.", figure: "none published", measures: "not applicable: descriptive vendor claim only", provenance: vendor-published, source_ref: KINGLAND-PA-2026 }
  prerequisites:
    - "Access to client documentation and third-party entity data (KINGLAND-PA-2026)"
    - "A firm restricted list and rules that the extracted structure feeds (KINGLAND-PA-2026)"
  risks_and_guardrails:
    - "A missed affiliate would pass through every downstream check. The vendor page states no extraction accuracy figure (KINGLAND-PA-2026)"
    - "SEC OCA says problems arise when firms partner with non-audit clients that also rely on audit clients, and that understanding how pervasive this is, and how firms monitor it, is top of mind (STARLING-HOHLWSJ-2026)"
  human_checkpoints:
    - "The tool walks professionals through building or updating a tree, so a person confirms the structure (KINGLAND-PA-2026)"
  role_evolution: "Independence staff move from assembling trees to checking extracted ones. This is inferred from the vendor's description and is not stated in the source (KINGLAND-PA-2026)."
  evidence_grade: C
  sources:
    - { ref: KINGLAND-PA-2026, title: "Public Accounting", publisher: Kingland, type: vendor, url: "https://www.kingland.com/public-accounting", date: 2026-10-16, access: full, locator: "Client Data and Family Tree Management and Restricted List Management sections; undated page, access date given" }
    - { ref: STARLING-HOHLWSJ-2026, title: "US SEC Weighs Audit Oversight Changes", publisher: Starling Insights, type: press, url: "https://insights.starlingtrust.com/content/observations/us-sec-weighs-audit-oversight-changes", date: 2026-01-22, access: full, locator: "second paragraph" }
  last_reviewed: 2026-10-16
  notes: "The Starling item summarises a Wall Street Journal interview with Mr Hohl published the month before (so Dec 2025); the interview itself was not read."

- id: assurance-acceptance-independence-03
  title: "Cross-system independence and risk monitoring dashboards with breach management"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ data-reporting, review-assurance ]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Independence is checked at points in time (acceptance, annual confirmations), so emerging issues surface late. Regulators now look at how firms monitor independence, and PCAOB inspection reports depend partly on what firms identify themselves."
  solution: "Kingland describes dashboards over a single data store that joins independence, risk and engagement data to show trends for independence and risk leaders, plus a breach workflow that centralises intake, assessment, remediation and regulatory reporting. The vendor's page says the dashboards support advanced analytics but does not say that AI drives these functions."
  outcomes:
    - { lever: risk, description: "Vendor says dashboards give real-time visibility of emerging issues instead of point-in-time review, and that breach records are auditable. No measured result.", figure: "none published", measures: "not applicable: descriptive vendor claim only", provenance: vendor-published, source_ref: KINGLAND-PA-2026 }
  prerequisites:
    - "Connected independence, risk and engagement data across the firm's business systems (KINGLAND-PA-2026)"
  risks_and_guardrails:
    - "A PCAOB inspection report states that the number of firm-identified independence instances may reflect the design and effectiveness of the firm's independence monitoring, and cautions against comparing firms on that number (PCAOB-BOULAY-2026, Part I.C)"
    - "Mr Hohl has said how firms monitor independence is top of mind at the SEC (STARLING-HOHLWSJ-2026)"
  human_checkpoints:
    - "Independence, risk and service-line leaders act on the trends shown (KINGLAND-PA-2026)"
  role_evolution: "Not stated in the sources."
  evidence_grade: C
  sources:
    - { ref: KINGLAND-PA-2026, title: "Public Accounting", publisher: Kingland, type: vendor, url: "https://www.kingland.com/public-accounting", date: 2026-10-16, access: full, locator: "Independence and Risk Monitoring and Breach Management sections; undated page, access date given" }
    - { ref: PCAOB-BOULAY-2026, title: "Final Report of Inspection, Boulay PLLP", publisher: PCAOB, type: regulator, url: "https://boulaygroup.com/wp-content/uploads/2026/09/PCAOB-Final-Inpection-Report-Boulay-PLLP-9-14-2026.pdf", date: 2026-09-14, access: full, locator: "Part I.C, Independence, pp. 5-6" }
    - { ref: STARLING-HOHLWSJ-2026, title: "US SEC Weighs Audit Oversight Changes", publisher: Starling Insights, type: press, url: "https://insights.starlingtrust.com/content/observations/us-sec-weighs-audit-oversight-changes", date: 2026-01-22, access: full, locator: "second paragraph" }
  last_reviewed: 2026-10-16
  notes: "The PCAOB report is used only to show how independence is reported to the regulator. It found no instance of non-compliance with Rule 3520 for that firm and says nothing about AI. The vendor page's personal-independence tool (new holdings checked against the restricted list within 24 hours of a trade, a vendor figure) is automation, not AI, as described; it is recorded here rather than as a separate use case."

- id: assurance-acceptance-independence-04
  title: "Partner rotation candidate matching that excludes people the independence rules bar"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ coordination-scheduling ]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Rotation planning has to balance experience, availability and career stage against independence-rule limits on who can take over a client."
  solution: "Kingland describes a rotation tool that combines data on professionals' experience, interests, time and billing, career stage and availability to surface suitable candidates, and applies independence rules to exclude people who cannot take the position."
  outcomes:
    - { lever: speed, description: "Vendor says the tool gives a clear view of top candidates. No measured result.", figure: "none published", measures: "not applicable: descriptive vendor claim only", provenance: vendor-published, source_ref: KINGLAND-PA-2026 }
  prerequisites:
    - "Staff experience, time-and-billing and availability data in one place (KINGLAND-PA-2026)"
  risks_and_guardrails:
    - "The source does not say whether AI or a rules engine does the matching, and gives no accuracy or acceptance data (KINGLAND-PA-2026)"
  human_checkpoints:
    - "Firm leaders make the rotation decision; the tool provides a view of candidates (KINGLAND-PA-2026)"
  role_evolution: "Not stated in the source."
  evidence_grade: C
  sources:
    - { ref: KINGLAND-PA-2026, title: "Public Accounting", publisher: Kingland, type: vendor, url: "https://www.kingland.com/public-accounting", date: 2026-10-16, access: full, locator: "Partner Rotation section; undated page, access date given" }
  last_reviewed: 2026-10-16
  notes: "Included because rotation is in the module scope. Pattern is `other` (matching and recommendation under rules). RSM's AI staffing tool in the landscape (CAQ-RSM-2026) concerns capacity planning and was not opened for this angle."

- id: assurance-acceptance-independence-05
  title: "Machine-learning client acceptance risk scoring as decision support (idea from research)"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ review-assurance, expert-judgment ]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Client acceptance involves subjective evaluations where managers' views meet the audit firm's expectations, which the authors say can lead to errors or misjudgments affecting audit time and cost."
  solution: "A 2024 paper proposes a decision support system for accepting or rejecting a client. It combines a logistic regression on financial ratios (the client's probability of being in a close-monitoring market, which holds listed firms struggling to meet financial indicators), fuzzy AHP weights for reputation criteria, a survey-based reputation score, and a fuzzy rule-based inference that outputs a client acceptance risk level. Earlier archival work on one large firm found that audit risk factors outweighed financial risk factors in its acceptance and continuance decisions."
  outcomes:
    - { lever: quality, description: "none published. The abstract says applicability is illustrated by a case study and reports no accuracy figure.", figure: "none published", measures: "not applicable", provenance: independent, source_ref: CEBI-2024 }
  prerequisites:
    - "Client financial data and a reputation survey (CEBI-2024)"
    - "Auditor-defined rules for the inference stage (CEBI-2024)"
  risks_and_guardrails:
    - "Only a single illustrative case study is reported in the abstract, so there is no accuracy, override or parallel-run result (CEBI-2024)"
    - "The Johnstone and Bedard finding that audit risk factors mattered more than financial risk factors in one large firm's decisions (JB-JAR-2004) is not shown to be reflected in the prototype's financial-ratio input. The comparison is the analyst's"
  human_checkpoints:
    - "The risk level guides the audit firm in deciding whether to engage; the decision stays with the firm (CEBI-2024)"
  role_evolution: "Not discussed in the sources."
  evidence_grade: D
  sources:
    - { ref: CEBI-2024, title: "Development of a decision support system for client acceptance in independent audit process", publisher: International Journal of Accounting Information Systems, type: academic, url: "https://avesis.cumhuriyet.edu.tr/yayin/cffa6431-8a21-4556-a92e-66d0ba2e1092/development-of-a-decision-support-system-for-client-acceptance-in-independent-audit-process", date: 2024-06, access: full, locator: "abstract (volume 53, article 100683); the full paper was not opened" }
    - { ref: JB-JAR-2004, title: "Audit firm portfolio management decisions", publisher: Journal of Accounting Research, type: academic, url: "https://academicnewsletter.sufe.edu.cn/info/413496", date: 2004-07-29, access: full, locator: "abstract, via a third-party index page" }
  last_reviewed: 2026-10-16
  notes: "Labelled an idea: a published prototype, no firm deployment found. JB-JAR-2004 is a foundation study, pre-AI, of one large audit firm; it is included to show what firms were found to weigh. Another paper on machine-learning litigation warning models for acceptance was seen in a search result but its page blocked access, so it is not used."

- id: assurance-acceptance-independence-06
  title: "Digital identity verification and AI-enabled customer due diligence at accountancy firm onboarding (idea; regulator-encouraged)"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ review-assurance, transaction-processing ]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "UK accountancy firms must carry out risk-based customer due diligence and ongoing monitoring. ICAEW reviewers say some firms do more checks than needed, and that simply collecting more documents does not mitigate a higher-risk situation."
  solution: "The UK AML and asset recovery strategy says digital identity and AI are expected to play a larger part in customer due diligence, and commits the FCA, HMRC and the Gambling Commission to encourage responsible use of AI in AML compliance. Government guidance of Feb 2026 says which digital identity providers can be relied on as a reliable and independent source. ICAEW says firms using electronic verification or AI-enabled tools remain responsible for a risk-based approach."
  outcomes:
    - { lever: cost, description: "none published for accountancy firms. The strategy's aim is to make customer due diligence quicker and easier while avoiding blanket or excessive checks.", figure: "none published", measures: "not applicable", provenance: independent, source_ref: UKGOV-AMLSTRAT-2026 }
  prerequisites:
    - "A digital identity service that meets the government's criteria for reliable and independent sources (UKGOV-AMLSTRAT-2026, para 84)"
    - "A firm-wide risk assessment, client risk assessments and verification evidence that connect to one another (ICAEW-AML-2026)"
  risks_and_guardrails:
    - "ICAEW says the Money Laundering Regulations do not permit reliance on Companies House identity verification for AML purposes (ICAEW-AML-2026, Companies House section)"
    - "ICAEW reviewers say many electronic verification services focus on sanctions, PEPs and adverse media rather than true identity verification, so firms must understand what a system provides (ICAEW-AML-2026, Identity verification section)"
    - "ICAEW says technology should support, not replace, professional judgement, and that firms should periodically review whether software remains suitable for their client base (ICAEW-AML-2026, Technology and AI section)"
    - "HMRC is to monitor implementation of a risk-based approach so supervised firms do not adopt disproportionate or blanket checks (UKGOV-AMLSTRAT-2026, para 71)"
  human_checkpoints:
    - "The money laundering reporting officer oversees compliance and decides on suspicious activity reports (ICAEW-AML-2026)"
  role_evolution: "ICAEW says AML works best when responsibility is embedded across the firm, not left to the reporting officer, and the officer need not be a qualified accountant (ICAEW-AML-2026)."
  evidence_grade: D
  sources:
    - { ref: UKGOV-AMLSTRAT-2026, title: "Anti-money laundering and asset recovery strategy: 2026 to 2029", publisher: HM Treasury and Home Office (GOV.UK), type: regulator, url: "https://www.gov.uk/government/publications/anti-money-laundering-and-asset-recovery-strategy-2026-to-2029", date: 2026-09-15, access: full, locator: "paras 64-66 (supervisory reform), 70-72 (supervisor commitments), 84-85 (digital ID and AI)" }
    - { ref: ICAEW-AML-2026, title: "AML latest updates and reviewer insights: key takeaways from our webinar", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/regulation/regulatory-news/regulatory-news-2026-06/aml-latest-updates-and-reviewer-insights-webinar", date: 2026-06, access: full, locator: "sections on Companies House verification, Identity verification and ongoing monitoring, Technology and AI" }
    - { ref: SPB-AML-2026, title: "A new strategy against money laundering", publisher: Squire Patton Boggs, type: press, url: "https://www.squirepattonboggs.com/media/xxcnvl2i/a-new-strategy-against-money-laundering.pdf", date: 2026-09-22, access: full, locator: "summary of the strategy's AI and digital identity points" }
    - { ref: TLT-AML-2026, title: "AML reform is accelerating: what firms should take from the UK's 2026-2029 strategy", publisher: TLT LLP, type: press, url: "https://www.tlt.com/insights-and-events/insight/aml-reform-is-accelerating-what-firms-should-take-from-the-uks-2026-2029-strategy", date: 2026-09-18, access: full, locator: "expected actions timeline" }
  last_reviewed: 2026-10-16
  notes: "Labelled an idea: regulators encourage it, but no accountancy firm's deployment, error rate or false-positive rate was found. The supervisory move to the FCA is expected to start in 2028/29 with legislation in 2027/28 (TLT-AML-2026), and ICAEW expects to stay supervisor likely through much of 2028 (ICAEW-AML-2026). The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 took effect 30 Jun 2026 and the ICAS summary of them does not mention AI (ICAS-MLR-2026). The FCA's AI good-practice examples are planned for 2026-27 and were not yet published when checked."

- id: assurance-acceptance-independence-07
  title: "Acceptance and continuance procedures extended to assess how heavily a client relies on AI in financial reporting (idea; guidance-driven)"
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "As clients put AI into financial reporting, auditors face a new question at the start of an engagement: can they obtain sufficient evidence, and does management understand its own outputs well enough to take responsibility for them?"
  solution: "The AICPA practice aid, as summarised by Accounting Today, discusses how an entity's AI use may affect acceptance and continuance decisions: the nature and circumstances of the engagement, management's integrity and ethical values, management's skills and competencies, and the engagement team's competence and capabilities. The more the entity relies on AI outputs in reporting, the more information the auditor may need, for example about the ability to gather evidence when agents run without traceable workflows. Heavy AI reliance may resemble reliance on external specialists and complex valuation models."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: AT-AICPAPA-2026 }
  prerequisites:
    - "An engagement team with a blend of auditing expertise, AI knowledge, data skills, professional skepticism and specialist support (AICPA-PA-2026)"
    - "A way to learn how the client uses AI, including AI used by vendors and third parties (AT-AICPAPA-2026)"
  risks_and_guardrails:
    - "The practice aid is nonauthoritative guidance and says more guidance on risk of material misstatement and audit evidence will be added to section one (AICPA-PA-2026)"
    - "The practice aid says that if management lacks the understanding needed to take responsibility for AI outputs, that may indicate a lack of appropriate skills and competencies (AT-AICPAPA-2026)"
  human_checkpoints:
    - "Engagement-level acceptance or continuance decision. The practice aid lists the factors to consider; it does not describe a tool (AT-AICPAPA-2026)"
  role_evolution: "Engagement teams need AI knowledge and data skills alongside audit expertise, and may need specialist support (AICPA-PA-2026)."
  evidence_grade: D
  sources:
    - { ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: AICPA & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "Considering an organization's use of AI section" }
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "paragraphs on acceptance or continuance decisions" }
    - { ref: JOFA-AIPA-2026, title: "AI and the audit: AICPA publishes practice aid to assist auditors", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/", date: 2026-10-13, access: full, locator: "whole article" }
  last_reviewed: 2026-10-16
  notes: "The practice aid itself is member-gated and was not read; this entry rests on the AICPA release and two trade summaries, and the acceptance wording is Accounting Today's paraphrase. The AI here is the client's, and the firm's acceptance step is a human judgment; ladder `assist` is used only to satisfy the vocabulary. The CAQ Audit Partner Pulse Spring 2026 (landscape CAQ-PULSE-2026: 6% of partners rate their largest client's AI governance advanced) is a related data point that was not opened for this angle."

- id: assurance-acceptance-independence-08
  title: "Engagement terms that address the firm's AI use and client-data consent (idea)"
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [ document-production, client-interaction ]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Firms use AI on client work, but it is unclear when the engagement letter or a consent must say so. State laws, contracts and firm policy may require disclosure even where the auditing standard does not."
  solution: "The AICPA practice aid says AU-C section 210 does not require the engagement letter to name AI tools, because AI is treated like other audit tools, but disclosure may be required by laws, regulations, contracts or firm policy, and some state laws require advance disclosure of certain AI uses by licensed professionals. AICPA ethics staff say that before client data goes into an AI tool the firm should ask whether it is confidential client information and whether consent is needed. IESBA says using client data for AI model training requires proper authorisation. In 2023 the South African regulator recommended engagement letters cover the use of AI tools in audits."
  outcomes:
    - { lever: risk, description: "none published for AI clauses. Adjacent survey figure: 26% of firms have an automated solution for engagement letters, which measures automation, not AI or disclosure.", figure: "26%", measures: "share of the 54 firms with complete data in the CPA.com and AICPA 2025 benchmark that answered yes to having an automated solution for engagement letters", provenance: independent, source_ref: CPACOM-ATR-2025 }
  prerequisites:
    - "A firm policy on approved AI tools and data handling (JOFA-ETHICSAI-2026)"
    - "Knowledge of applicable state disclosure laws (AT-AICPAPA-2026)"
  risks_and_guardrails:
    - "Pasting client data into a public AI tool may breach the Confidential Client Information Rule if consent was needed and not obtained (JOFA-ETHICSAI-2026)"
    - "Unauthorised use of client data for model training is a Code concern (IESBA-SNAPSHOT-2026, Q4)"
  human_checkpoints:
    - "Partner decides what the engagement letter says and whether consent has been obtained (AT-AICPAPA-2026, JOFA-ETHICSAI-2026)"
  role_evolution: "Not discussed in the sources."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "final paragraphs on AU-C section 210 and the engagement letter" }
    - { ref: JOFA-ETHICSAI-2026, title: "Accounting ethics in the age of AI", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: 2026-08-05, access: full, locator: "confidentiality section" }
    - { ref: IESBA-SNAPSHOT-2026, title: "IESBA Snapshot: Ethics and Independence Approach to the Use of Technology", publisher: IESBA, type: standard-setter, url: "https://www.ethicsboard.org/news-events/2026-06/iesba-snapshot-ethics-and-independence-approach-use-technology", date: 2026-06-11, access: full, locator: "Q4, Confidentiality" }
    - { ref: IRBA-AI-2023, title: "Artificial Intelligence Audit Risks Mitigation", publisher: Independent Regulatory Board for Auditors (South Africa), type: regulator, url: "https://www.irba.co.za/upload/report_files/02.-AI-Audit-Risks-Mitigation.pdf", date: 2023-01-12, access: full, locator: "recommendations list" }
    - { ref: CPACOM-ATR-2025, title: "Audit Transformation Report: 2025 CPA.com and AICPA Audit Benchmark Survey", publisher: CPA.com and AICPA, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "p. 10, chart of automated solutions; Appendix I for the sample" }
  last_reviewed: 2026-10-16
  notes: "The IRBA communique is older than 18 months and states that it was itself generated by AI and then reviewed; it is included as the only regulator text found that recommends engagement-letter language on AI. The 26% figure is capped as adjacent: it measures any automated engagement-letter solution. The survey was run by CPA.com, the AICPA's technology subsidiary, and the sample is small and self-selected."

- id: assurance-acceptance-independence-09
  title: "Pre-adoption independence review of AI tool-vendor arrangements (idea; derived from SOC tool-provider guidance)"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Firms increasingly sign contracts with technology vendors whose products they use on audits or whose customers are their audit clients. Terms that shift control, judgment, fees or access to evidence toward the vendor can threaten independence and objectivity."
  solution: "AICPA ethics staff describe, for SOC 2 examiners, the contract terms to test: control over scope and timing, financial dependence, cross-referral arrangements, vendor involvement in the examination, vendor-driven deadlines, bundled pricing where the vendor sets the fee, non-disparagement clauses that block required communications, and paying the vendor to access evidence. The article says the considerations may also apply to other audit and attest services. SEC OCA and IESBA have both named AI-company partnerships and commercial entanglement with technology providers as open questions."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: JOFA-SOCETH-2026 }
  prerequisites:
    - "An inventory of AI vendors and the firm's contracts with them, including vendors that also serve its attest clients (JOFA-SOCETH-2026)"
  risks_and_guardrails:
    - "If safeguards do not eliminate significant threats, performing or continuing the engagement is not appropriate (JOFA-SOCETH-2026)"
    - "A commentator says ambiguity remains in the PEEC draft on when licensing an AI audit tool crosses into an independence conflict, and that the lack of technology-company comment letters is a gap (AT-PEEC-2026). The commentator works at an AI-native audit firm"
  human_checkpoints:
    - "Documented evaluation and conclusion under the conceptual framework; documentation of safeguards is required when applying the Conceptual Framework for Independence (JOFA-SOCETH-2026)"
  role_evolution: "Not discussed in the sources."
  evidence_grade: D
  sources:
    - { ref: JOFA-SOCETH-2026, title: "SOC engagements: ethics risks with tool providers", publisher: Journal of Accountancy (AICPA ethics staff), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/", date: 2026-04-06, access: full, locator: "whole article; sections on threats and contract terms" }
    - { ref: STARLING-HOHLWSJ-2026, title: "US SEC Weighs Audit Oversight Changes", publisher: Starling Insights, type: press, url: "https://insights.starlingtrust.com/content/observations/us-sec-weighs-audit-oversight-changes", date: 2026-01-22, access: full, locator: "second paragraph" }
    - { ref: IESBA-EEA-2026, title: "Ethics is not the constraint on AI assurance. It is the foundation", publisher: IESBA, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-06/EAA_IESBA_Presentation_final.pdf", date: 2026-05, access: full, locator: "slide 5, research questions" }
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence rules", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: 2026-08-31, access: full, locator: "paragraphs 3 to 5" }
  last_reviewed: 2026-10-16
  notes: "Labelled an idea. The AICPA article is about SOC 2 tool providers, not audit AI vendors; the transfer is the article's own suggestion that it may apply to other attest work, plus the landscape's research lead. No firm describing its own vendor review was found. One of IESBA's six research questions asks how AI-driven commercial entanglement between firms and technology providers should be mapped."

- id: assurance-acceptance-independence-10
  title: "Non-audit-service approval gate for AI tools, systems or insights offered to audit clients (idea)"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ review-assurance, expert-judgment ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Firms sell technology-enabled services, including AI-based insights and licensed software, to clients that include audit clients. Self-review threats and the risk of assuming management responsibility arise when the output feeds the client's records or controls."
  solution: "IESBA's 2023 technology revisions (effective for audits of periods beginning on or after 15 Dec 2024) address when firms and network firms may provide a technology-related non-assurance service to an audit client. A joint IESBA and APESB guide works through hypothetical cases. For software licensed to an audit client it says the firm should check that a competent client employee evaluates outputs and runs controls, and that a black-box product the client had no part in developing makes that unlikely, so management responsibility may be assumed. For a PIE audit client, services that create a self-review threat are prohibited. AICPA ethics staff say developing or hosting an AI system for an attest client can raise independence concerns under the existing nonattest and information-systems rules. SEC rules prohibit financial information system design and implementation services unless the results will not be subject to audit procedures."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: IESBA-APESB-2023 }
  prerequisites:
    - "A firm approval process for new services to audit clients, with technology expertise in the review (IESBA-APESB-2023)"
    - "The audit client has competent employees who can evaluate outputs, and backtesting or parallel running can help them validate output (IESBA-APESB-2023, paras 43-44)"
  risks_and_guardrails:
    - "Frequent AI or analytics insights that the client relies on to form decisions or run internal controls risk the firm assuming management responsibility or creating a self-review threat (IESBA-APESB-2023, paras 26-28)"
    - "Indirect services through software licensed to non-audit clients can also create a self-review threat if the criteria are met (IESBA-APESB-2023, paras 19-20)"
    - "Holding client data analysed by AI engages the confidentiality and conflict-of-interest provisions (IESBA-APESB-2023, paras 29-30)"
    - "In the UK the IESBA non-assurance provisions do not apply because the FRC Ethical Standard governs auditors, and the FRC does not believe its requirements are less demanding (ICAS-IESBA-2026)"
  human_checkpoints:
    - "Audit partner evaluates threats and safeguards for each proposed non-audit service (IESBA-APESB-2023, Scenario 2)"
  role_evolution: "Not discussed in the sources."
  evidence_grade: D
  sources:
    - { ref: IESBA-APESB-2023, title: "Applying the Code's Conceptual Framework to Independence: Practical Guidance for Auditors in Technology-Related Scenarios", publisher: IESBA and APESB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2023-07/IESBA_APESB_Applying_the_Code_s_Conceptual_Framework_to_Independence_0.pdf", date: 2023-07-13, access: full, locator: "paras 19-20, 26-30; Scenario 2, paras 41-47" }
    - { ref: IESBA-TECHREV-2023, title: "Final Pronouncement: Technology-related Revisions to the Code", publisher: IESBA, type: standard-setter, url: "https://www.ethicsboard.org/publications/final-pronouncement-technology-related-revisions-code", date: 2023-04-11, access: full, locator: "summary and effective-date paragraph" }
    - { ref: JOFA-ETHICSAI-2026, title: "Accounting ethics in the age of AI", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: 2026-08-05, access: full, locator: "paragraph on AI-related nonattest services" }
    - { ref: SEC-REGSX-2-01, title: "17 CFR 210.2-01 Qualifications of accountants", publisher: US Securities and Exchange Commission (text via Cornell LII), type: regulator, url: "https://www.law.cornell.edu/cfr/text/17/210.2-01", date: 2020-12, access: full, locator: "paragraph (c)(4)(ii) financial information systems design and implementation; date is the last amendment listed on the page" }
    - { ref: ICAS-IESBA-2026, title: "IESBA issues snapshot on the ethical implications of using technology, including AI", publisher: ICAS, type: professional-body, url: "https://icas.com/news-insights-events/news/ethics/iesba-issues-snapshot-on-the-ethical-implications-of-using-technology-including-ai/", date: 2026-07-14, access: full, locator: "section on technology-related revisions to the Code" }
  last_reviewed: 2026-10-16
  notes: "Labelled an idea because the guide's cases are hypothetical and no firm describes its own gate. The question is live: IESBA's director asked in May 2026 what happens to the substance of independence when firms provide technology services that form a basis for, or input to, what they also assure (IESBA-EEA-2026, slide 4). The AICPA article that mentions AI-related nonattest services also points to a staff article, AI Through an Ethics Lens, which is member-gated and was not read."

- id: assurance-acceptance-independence-11
  title: "Investor, fund and portfolio-company independence screening at acceptance after outside investment (idea; obligation-driven)"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [ review-assurance, data-reporting ]
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "When private capital enters an audit firm or its non-attest affiliate, new relationships (investor, funds, portfolio companies, other investees) have to be tested against every audit client and prospect. Regulators say outside ownership brings threats to independence and to firm culture."
  solution: "Screening of prospective and continuing clients against the investor group's structure. In the UK, the FRC has confirmed an audit firm acquired by a PE fund may not audit the fund, its portfolio companies or significant affiliates, and the firm must assess whether the fund or its staff become covered persons. The AICPA exposure draft revises the APS interpretation, the network firm definition and the conceptual framework interpretations, and PEEC's earlier discussion memorandum treated the non-attest entity as a network firm and investor funds and portfolio companies as generally not network firms unless other circumstances apply. The AI link in the sources is the funding rationale: AICPA and SEC leaders say PE capital can pay for technology investment. How firms build and run the screening is not described."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: ICAEW-PE-2024 }
  prerequisites:
    - "A map of the investor, its funds, portfolio companies and the firm's attest and non-attest entities (ICAEW-PE-2024, JOFA-PE-2025)"
    - "A well-drafted administrative services agreement between the CPA firm and the non-attest entity (JOFA-NILSEN-2025)"
    - "Quality-management controls that monitor independence once the investor is in (JOFA-NILSEN-2025)"
  risks_and_guardrails:
    - "FRC says the legal control requirements must be met in substance and form, and asks firms to engage with it early and candidly (FRC-PCLETTER-2024)"
    - "PCAOB inspections staff say outside ownership introduces threats to independence and firm culture and that profit pressure could reduce audit staffing (BLOOMBERG-PCAOBPE-2025, opening paragraphs only; paywalled)"
    - "Accountancy Europe lists risks including short-term pressure, conflicts of interest, a drift toward non-PIE work and investor exit within three to seven years (ACCEU-PE-2025)"
    - "A PEEC proposal under discussion would bar attest-client investment in firms (JOFA-PEEC-2026)"
  human_checkpoints:
    - "Independence and risk leaders assess whether the investor or its staff are covered persons, and keep the assessment under review (ICAEW-PE-2024)"
  role_evolution: "Not discussed in the sources beyond culture and staffing concerns."
  evidence_grade: D
  sources:
    - { ref: FRC-PCLETTER-2024, title: "External private capital and UK audit firms (letter from the FRC CEO)", publisher: Financial Reporting Council, type: regulator, url: "https://www.frc.org.uk/documents/7733/Letter_on_private_capital_in_audit_firms.pdf", date: 2024-09-26, access: full, locator: "paras 3-8 and the request for early engagement" }
    - { ref: ICAEW-PE-2024, title: "Private equity investment in audit firms", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/regulation/working-in-the-regulated-area-of-audit/audit-regulations-and-guidance/private-equity-investment-in-audit-firms", date: 2024-10, access: full, locator: "FRC confirmation and covered-person paragraphs; page undated, month inferred from a linked ICAEW article of Oct 2024" }
    - { ref: AICPA-APSED-2025, title: "Alternative Practice Structures: Proposed Revisions to the AICPA Code (exposure draft landing page)", publisher: AICPA & CIMA, type: standard-setter, url: "https://www.aicpa-cima.com/resources/download/ethics-APS-ED", date: 2025-12, access: full, locator: "landing page list of proposed revisions; the PDF is member-gated and was not read. Comment period closed 30 Apr 2026" }
    - { ref: JOFA-PE-2025, title: "Independence rules and private equity (PEEC discussion memorandum)", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2025/mar/independence-rules-private-equity/", date: 2025-03-10, access: full, locator: "three-step process and network-firm paragraphs" }
    - { ref: JOFA-NILSEN-2025, title: "Navigating outside investors: Safeguarding ethics and independence in evolving practice structures", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2025/oct/navigating-outside-investors-safeguarding-ethics-and-independence-in-evolving-practice-structures/", date: 2025-10-24, access: full, locator: "paragraphs on due diligence, administrative services agreement and quality management" }
    - { ref: JOFA-PEEC-2026, title: "PEEC to continue discussions on alternative practice structures", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/", date: 2026-08-10, access: full, locator: "second paragraph" }
    - { ref: BLOOMBERG-PCAOBPE-2025, title: "US Audit Board to Examine Quality Safeguards at PE-Backed Firms", publisher: Bloomberg Tax, type: press, url: "https://news.bloomberglaw.com/daily-tax-report/us-audit-board-to-examine-quality-safeguards-at-pe-backed-firms", date: 2025-12-09, access: search-only, locator: "opening paragraphs; paywalled after that" }
    - { ref: ACCEU-PE-2025, title: "Beyond private equity: third party ownership in the accountancy and audit sector", publisher: Accountancy Europe, type: professional-body, url: "https://accountancyeurope.eu/wp-content/uploads/2025/11/251121-Beyond-Private-Equity-Third-Party-ownership-summary.pdf", date: 2025-11-21, access: full, locator: "risks section" }
    - { ref: TR-HOHL-2026, title: "SEC Chief Accountant Hohl Dispels Rumors of Weakening Auditor Independence Rules", publisher: Thomson Reuters Tax & Accounting, type: press, url: "https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/", date: 2026-06-05, access: full, locator: "paragraph 4: APS capital for new technologies and independence risk" }
  last_reviewed: 2026-10-16
  notes: "Labelled an idea: the screening duty comes from regulators, but no firm's tool or process, and no hit rate, was found. The PCAOB source is search-only because only the opening paragraphs were readable, so nothing here rests on it alone. The PEEC second exposure draft had not been issued at the time of writing; PEEC meets 19 Oct 2026 (AICPA-PEECMEET-2026). The AICPA Feb 2025 release states its date as 'Feb. 5, 2024' in its text, but the page is dated 5 Feb 2025 and is not cited here."

- id: assurance-acceptance-independence-12
  title: "AI-enabled audit platform launched by a firm operating in an alternative practice structure"
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [ review-assurance, data-reporting ]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Firms in an APS split attest and non-attest work into separate entities. A technology platform that originates in or is shared with the non-attest side raises the question of who provides it to the attest practice and whether independence rules reach that arrangement."
  solution: "Grant Thornton US launched Gtap, a cloud-based platform that embeds analytics, automation and AI into every audit stage, with AI agents that identify risks and anomalies. The article says the firm has operated in an APS since New Mountain Capital's 2024 acquisition (attest in Grant Thornton LLP, non-attest in Grant Thornton Advisors), that Grant Thornton Ireland originally developed Gtap, and that the platform combines the consulting capabilities of firms under Advisors while keeping accounting practices separate for regulatory reasons. The firm says it will use Gtap on private-company audits first."
  outcomes:
    - { lever: capacity, description: "none published. The article says the platform now spans nearly 25,000 people across the Americas, EMEA and APAC; that is a headcount of the combined Advisors platform, not an outcome.", figure: "nearly 25,000", measures: "people on the combined Grant Thornton platform across the Americas, Europe, Middle East and Africa and Asia-Pacific, per the article; not audit hours or quality", provenance: self-reported, source_ref: GT-GTAP-2026 }
  prerequisites:
    - "An APS with attest and non-attest entities and an administrative services agreement (GT-GTAP-2026, JOFA-NILSEN-2025)"
  risks_and_guardrails:
    - "The article does not say who owns or licenses Gtap or how the arrangement was assessed for independence (GT-GTAP-2026)"
    - "The PEEC discussion memorandum treated the non-attest entity as a network firm of the attest firm (JOFA-PE-2025)"
    - "A commentator says ambiguity remains on when licensing AI audit tools crosses into an independence conflict, and that this could favour firms that build AI in-house (AT-PEEC-2026). The commentator works at a competing AI-native firm"
    - "SEC OCA says APS can provide capital for new technology but introduce risk, particularly to independence (TR-HOHL-2026)"
  human_checkpoints:
    - "The CEO is quoted saying staff focus on professional skepticism and judgment (GT-GTAP-2026)"
  role_evolution: "The firm says automating transactional parts of the audit lets teams focus on skepticism, judgment and risk assessment (GT-GTAP-2026)."
  evidence_grade: C
  sources:
    - { ref: GT-GTAP-2026, title: "Grant Thornton launches AI platform for audit business", publisher: Consultancy.org (Consulting.us), type: press, url: "https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business", date: 2026-05-11, access: full, locator: "paragraphs 1 to 4" }
    - { ref: JOFA-PE-2025, title: "Independence rules and private equity (PEEC discussion memorandum)", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2025/mar/independence-rules-private-equity/", date: 2025-03-10, access: full, locator: "network-firm paragraph" }
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence rules", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: 2026-08-31, access: full, locator: "paragraphs 3 to 5" }
    - { ref: TR-HOHL-2026, title: "SEC Chief Accountant Hohl Dispels Rumors of Weakening Auditor Independence Rules", publisher: Thomson Reuters Tax & Accounting, type: press, url: "https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/", date: 2026-06-05, access: full, locator: "paragraph 4" }
    - { ref: JOFA-NILSEN-2025, title: "Navigating outside investors: Safeguarding ethics and independence in evolving practice structures", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2025/oct/navigating-outside-investors-safeguarding-ethics-and-independence-in-evolving-practice-structures/", date: 2025-10-24, access: full, locator: "administrative services agreement paragraph" }
  last_reviewed: 2026-10-16
  notes: "Grade C: a firm announcement relayed by trade press, with no evidence of use in audits yet. The platform entry is the independence-relevant fact; the independence analysis is the analyst's framing, and the source does not discuss it. The landscape dated the launch 7 May 2026 (GT-GTAP-2026 in the landscape); this page is dated 11 May 2026."

- id: assurance-acceptance-independence-13
  title: "AI-native attest entity built inside a venture-backed alternative practice structure"
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [ review-assurance ]
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "State rules require attest services to sit in a CPA-owned firm, so a venture-backed technology company that wants to offer audits has to create an APS, with attest and technology entities linked by agreements."
  solution: "Oath Verified's chief assurance officer, a former PCAOB board member, says the firm uses an APS because its platform company is venture-backed, builds an AI-native audit methodology from the ground up, hires what it calls accountant engineers, and describes its aim as an independent verification platform in which a machine checks a machine. The article reports about $10 million raised, including a $6.6 million seed round."
  outcomes:
    - { lever: growth, description: "none published. Funding is reported, not audit outcomes.", figure: "about $10 million raised", measures: "total funding raised by Oath Verified as reported by Accounting Today citing the Wall Street Journal", provenance: self-reported, source_ref: AT-PEEC-2026 }
  prerequisites:
    - "An attest entity formed under state requirements and an APS (AT-PEEC-2026)"
    - "A data environment per client that does not train the model, per the executive (AT-PEEC-2026)"
  risks_and_guardrails:
    - "The source for these statements is an executive of the firm, who also comments on the independence rules that govern it (AT-PEEC-2026)"
    - "PEEC's draft would treat entities closely aligned with an audit firm as possibly within the APS scope, which the executive says could reach technology companies (AT-PEEC-2026)"
  human_checkpoints:
    - "Not described in the source"
  role_evolution: "The firm hires accountant engineers to build the methodology (AT-PEEC-2026)."
  evidence_grade: C
  sources:
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence rules", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: 2026-08-31, access: full, locator: "paragraphs 3, 8 and 9 and the section on maintaining independence" }
  last_reviewed: 2026-10-16
  notes: "Grade C and maturity announced: the methodology is described as being built, not as used on audits. The landscape lists Modus ($85M, invests in audit firms) and Repodo (new AI-built Danish audit firm) as similar structural signals; neither was re-read here."

- id: assurance-acceptance-independence-14
  title: "Audit-committee communication on the auditor's AI use and its independence implications (idea)"
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [ client-interaction, document-production ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Audit committees are asking how companies use AI in financial reporting, how auditors use AI, and what the independence implications are. Regulators ask auditors the same questions."
  solution: "The SEC chief accountant says the OCA asks auditors how they use AI to improve engagement-level audit quality and to monitor quality control, and says audit committees are asking about the independence implications of auditors' AI use. A firm's answer becomes part of the continuing relationship and the communication with those charged with governance."
  outcomes:
    - { lever: experience, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: KPMG-HOHL-2026 }
  prerequisites:
    - "A firm-level inventory of AI tools and vendor relationships (see use cases 09 and 10)"
  risks_and_guardrails:
    - "Mr Hohl says independence rules need to stay fit for purpose when AI is integrated into audit service delivery (KPMG-HOHL-2026)"
  human_checkpoints:
    - "Engagement leader communicates with the audit committee (KPMG-HOHL-2026)"
  role_evolution: "Not discussed in the sources."
  evidence_grade: D
  sources:
    - { ref: KPMG-HOHL-2026, title: "Q&A with Kurt Hohl, SEC chief accountant", publisher: KPMG Board Leadership Center, type: firm, url: "https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html", date: 2026-05-27, access: full, locator: "answers on AI and auditor independence and on audit committees" }
    - { ref: TR-HOHL-2026, title: "SEC Chief Accountant Hohl Dispels Rumors of Weakening Auditor Independence Rules", publisher: Thomson Reuters Tax & Accounting, type: press, url: "https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/", date: 2026-06-05, access: full, locator: "paragraphs 2 and 3" }
  last_reviewed: 2026-10-16
  notes: "Labelled an idea: no firm describes a standard audit-committee communication on this topic. The KPMG page is a Q&A with a regulator hosted by a firm, so it reports the regulator's views, not KPMG's practice. The ICAS-reported Audit Trust Index (257 UK finance leaders, audit committee chairs and investors, Aug 2026) found 79% satisfied with how audit firms deploy AI and technology, and the biggest concern was auditors becoming over-reliant on AI. It is not about independence and is listed under frontier context, not as an outcome here (ICAS-ATI-2026)."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Client and engagement acceptance and continuance** (`review-assurance`, `expert-judgment`). Factors in the practice aid summary: nature of the engagement, management integrity and ethical values, management skills, team competence, and now the client's AI reliance (AT-AICPAPA-2026).
- **Independence and conflict checks, and service approval** (`review-assurance`, `data-reporting`). Entity and affiliate mapping, financial and business relationships, and a non-audit-service gate. SEC rules prohibit financial-information-system design and implementation unless results will not be subject to audit procedures (SEC-REGSX-2-01, para (c)(4)(ii)). The IESBA technology revisions cover technology-related non-assurance services (IESBA-TECHREV-2023).
- **KYC and customer due diligence, AML risk profiling** (`review-assurance`, `transaction-processing`). Risk-based identity verification, firm-wide and client risk assessments, ongoing monitoring that updates when circumstances change (ICAEW-AML-2026).
- **Engagement letters and consent** (`document-production`, `client-interaction`). AU-C 210 does not require naming AI tools, but state laws, contracts or firm policy may (AT-AICPAPA-2026).
- **Ongoing independence monitoring, breach management and rotation** (`data-reporting`, `coordination-scheduling`). Described for one vendor (KINGLAND-PA-2026); the PCAOB reports independence through Part I.C of inspection reports (PCAOB-BOULAY-2026).
- **Firm structure and ownership governance** (`expert-judgment`). APS design, administrative services agreements, investor due diligence and engagement with regulators (JOFA-NILSEN-2025, FRC-PCLETTER-2024).

### Common pain points

- Independence rules are complex in application, and the consequence of a wrong answer is significant for the company and the audit firm (TR-HOHL-2026).
- Firms partner with non-audit clients that also rely on audit clients, which makes enforcement harder, and monitoring of this is top of mind at the SEC (STARLING-HOHLWSJ-2026).
- Ambiguity on when licensing an AI audit tool becomes an independence problem (AT-PEEC-2026).
- The interim independence standards the PCAOB adopted from the AICPA over twenty years ago are now under review (TR-HOHL-2026).
- AML: firms over-collect documents, cannot rely on Companies House verification, and may misread what electronic verification tools do (ICAEW-AML-2026).
- Vendor pages describe replacing manual and spreadsheet-driven acceptance work (KINGLAND-ACCEPT); no independent source confirms the size of that burden.

### Metrics and benchmarks (all with what they measure)

| Figure | What it measures | Source |
|---|---|---|
| 26% | Share of 54 firms with complete data that have an automated solution for engagement letters (not AI) | CPACOM-ATR-2025, p. 10 |
| 74 registered, 54 complete | Firms in the 2025 CPA.com and AICPA benchmark sample; open June to August 2025 | CPACOM-ATR-2025, Appendix I |
| 81 | Comment letters on the AICPA APS exposure draft, per a commentator; none from technology companies | AT-PEEC-2026 |
| About 100 (2023), 200 (2024) | PE transactions recorded in the European accountancy sector; the paper says 60% involved non-audit firms and the rest included audit services | ACCEU-PE-2025, p. 1 |
| 25 to 3 | UK AML supervisors after the planned consolidation | UKGOV-AMLSTRAT-2026, para 64 |
| 9,500 | Firms ICAEW supervises for AML, per the speaker biography on the webinar page | ICAEW-AML-2026 |
| 79%, 67%, 14% | Of 257 UK stakeholders: satisfied with firms' AI deployment; greater confidence in AI-led review of large volumes of data or contracts; preferred human auditors for that task (adjacent, not about acceptance) | ICAS-ATI-2026 |

No error rate, override rate, false-positive rate, parallel-run result or inspection finding about AI in acceptance, KYC or independence monitoring was found.

### Guardrails and regulatory points

- **IESBA.** The Code applies to technology use; the 2023 technology revisions (effective 15 Dec 2024) cover use of technology outputs, automation bias, confidentiality over the data lifecycle and technology-related non-assurance services. No further Code changes are planned for now (IESBA-SNAPSHOT-2026, Q4 and Q5; IESBA-TECHREV-2023).
- **IESBA staff publication (15 Jul 2026).** Characteristics such as opacity, non-determinism, data dependence and third-party reliance can create or amplify self-review, self-interest, intimidation and other threats. It says new information such as vendor updates or model drift requires reassessment (IESBA-NAM-2026, PDF pp. 7, 10, 14).
- **AICPA.** Existing nonattest and information-systems rules apply to AI work for attest clients (JOFA-ETHICSAI-2026). Tool-provider contract terms that shift control, judgment, fees or evidence access can threaten independence (JOFA-SOCETH-2026). The APS exposure draft revises the APS interpretation, the network firm definition and the conceptual framework interpretations (AICPA-APSED-2025).
- **SEC and PCAOB.** SEC Rule 2-01 prohibits listed non-audit services and sets business-relationship limits (SEC-REGSX-2-01). PCAOB Rule 3520 requires independence including under Regulation S-X (PCAOB-BOULAY-2026, Part I.C).
- **FRC.** Private capital must preserve the legal control requirement in substance and form; a PE-owned audit firm may not audit the fund or its portfolio companies (FRC-PCLETTER-2024, ICAEW-PE-2024). Its generative AI guidance does not address acceptance or independence (a keyword search of the full text for acceptance, continuance, independence, ethical standard and conflict found none; FRC-GENAI-2026).
- **UK AML.** Firms must carry out their own risk-based due diligence; AI-enabled tools do not shift responsibility (ICAEW-AML-2026). The strategy asks the FCA to publish AI good and poor practice examples in 2026-27 (UKGOV-AMLSTRAT-2026, para 70).
- **Engagement letters.** AU-C 210 does not require disclosure of AI tools; state law may (AT-AICPAPA-2026).

### Frontier signals (dated and sourced)

- **19 Oct 2026:** PEEC virtual meeting, where the committee is expected to vote on releasing a second APS exposure draft (AICPA-PEECMEET-2026, AICPA-PEECWEBCAST-2026). Outcome unknown at writing.
- **Q4 2026:** IESBA AI-specific non-authoritative publication on key ethics and independence considerations (IESBA-SNAPSHOT-2026, Q6; APESB-IESBACHAIR-2026).
- **Sep and Dec 2026:** IESBA updates on its PE and other external investment workstream (September meeting) and its first trends and risks report (December meeting) (IESBA-HIGHLIGHTS-2026).
- **Dec 2025 to Jun 2026:** SEC OCA independence review, starting with refreshed FAQs and then a joint look with the PCAOB at the interim independence standards. Hohl said in Dec 2025 there were no immediate rulemaking plans, and repeated on 4 Jun 2026 that he is in listening mode (TR-HOHL-2026).
- **1 Oct 2026:** The PCAOB's agendas include a standard-setting project on auditor independence and a research project on data and technology (JOFA-PCAOBAG-2026).
- **2026-27:** FCA examples of good and poor practice on AI for AML (UKGOV-AMLSTRAT-2026, para 70). **2027/28 and 2028/29:** legislation and then transfer of accountancy AML supervision to the FCA (TLT-AML-2026).
- **13 Oct 2026:** The AICPA practice aid will gain further guidance on risk of material misstatement and audit evidence when a company uses AI (AICPA-PA-2026).
- **Dec 2025 onward:** PCAOB inspections to look at quality safeguards at firms with PE deals (BLOOMBERG-PCAOBPE-2025).
- **Research pipeline:** a registered report on whether PE investment in accounting firms affects perceived and actual audit quality, with no results yet (NYK-TAR-2024); a Current Issues in Auditing call for papers on PE and auditing, deadline 30 May 2026 (AAA-CIIA-2025); IESBA's six research questions of May 2026 (IESBA-EEA-2026).
- **Perception research:** a study summarised in Oct 2025 found that auditor AI use can limit the effect of the appearance of independence conflicts on juror negligence judgments (LIBBY-CIIA-2025).

### Workforce and role effects

- PE and APS structures raise concerns about culture, staffing and compensation, and the AAA call asks how the service mix and career paths change (AAA-CIIA-2025). PCAOB staff say profit pressure could reduce audit team staffing (BLOOMBERG-PCAOBPE-2025).
- Hohl says some PE-backed firms left public-company audits because it was too expensive, reducing choice (STARLING-HOHLWSJ-2026).
- An AI-native firm hires accountant engineers (AT-PEEC-2026). IESBA asks how AI adoption shapes the ethical formation of early-career accountants (IESBA-EEA-2026, slide 5).
- The AICPA says engagement teams may need a blend of audit, AI, data and specialist skills (AICPA-PA-2026). The ICAEW says the money laundering reporting officer need not be a qualified accountant (ICAEW-AML-2026).

### Objections and concerns practitioners raise

- Independence rules may be written about PE roll-ups and miss technology companies, favouring firms that build AI in-house over those licensing it (AT-PEEC-2026; the speaker has a commercial interest).
- Technology multiplies independence threats instead of neutralising them, and some regulators are considering adjusting independence rules (IESBA-EEA-2026, slide 4).
- Governance and oversight lag behind adoption, and shadow AI is a growing risk (IESBA-SNAPSHOT-2026, Q7).
- Over-reliance on AI is stakeholders' biggest concern about audit AI, though not specific to acceptance (ICAS-ATI-2026).
- AI can produce false evidence and fabricated working papers, which bears on client integrity at acceptance (IRBA-AI-2023).

### Interview probes for an advisor

1. "When a client's reporting depends heavily on AI agents, what do you check before accepting or continuing, and has an engagement ever been deferred or declined because evidence could not be obtained?"
2. "Which AI vendors, platforms or affiliates supply tools you use on audits or sell to your audit clients, and who reviews those relationships for independence (control, fees, referrals, access to evidence) before adoption?"
3. "If a PE investor, fund or portfolio company enters your structure, how does acceptance find overlaps with audit clients, and how often does a hit change a decision?"
4. "In KYC and independence checks, what does each tool actually do (identity verification or sanctions, PEP and adverse-media screening), what is the false-positive and override rate, and who reviews suitability?"
5. "What does your engagement letter say about AI use and client-data consent today, and what changes it: state law, a client request or firm policy?"

---

## 4. Routed to other modules

- **quality-management.** Mr Hohl's suggestion that the PCAOB shift inspections toward firms' systems of quality management (TR-HOHLAGENDA-2025, 10 Dec 2025); firm-level tool authorisation and revalidation in the AICPA practice aid's section two (AT-AICPAPA-2026); the PCAOB's QC 1000 amendments, effective 15 Dec 2026 pending SEC approval (JOFA-PCAOBQC-2026); IESBA's note that vendor updates and model drift require reassessment (IESBA-NAM-2026, PDF p. 10).
- **planning-risk-assessment.** The practice aid's guidance on understanding the entity's use of AI, AI-operated controls and AI risks (data, model drift, explainability) (AT-AICPAPA-2026); the client AI governance data in CAQ-PULSE-2026 (landscape, not re-opened).
- **specialists.** The PEEC revised "attest engagement team" definition, effective for attest engagements beginning on or after 15 Dec 2026, excludes internal auditors and the auditor's and practitioner's external specialists from the team (JOFA-PEECATTEST-2026). The practice aid's analogy between heavy client AI reliance and external specialists or complex valuation models (AT-AICPAPA-2026).
- **other-assurance (SOC and assurance over AI).** The SOC 2 tool-provider ethics article (JOFA-SOCETH-2026) is written for SOC 2 examiners and is the most developed independence text on tool-vendor arrangements. IESBA's May 2026 framing that ethics is the foundation of AI assurance (IESBA-EEA-2026). A search result on independence rules for frontier-AI auditors (arXiv 2601.11699) was seen but not opened.
- **completion-reporting.** Audit-committee communications about AI (see use case 14); the PCAOB research project on communications with audit committees (JOFA-PCAOBAG-2026).
- **Cross-cut: firm business model and workforce.** PE and APS structures, fee pressure and AI-native entrants (JOFA-PEEC-2026, AT-PEEC-2026, GT-GTAP-2026).

---

## 5. Sources

Access: `full` means opened and read (partly, for long documents; stated in the use-case locators). A page that was undated carries the access date or an inferred month, noted. Dates were taken from page metadata or bylines where available.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full (release; practice aid member-gated) |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 | full |
| JOFA-PEEC-2026 | PEEC to continue discussions on alternative practice structures | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/ | 2026-08-10 | full |
| JOFA-PEECATTEST-2026 | PEEC adopts revised definition of 'attest engagement team' | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/peec-adopts-revised-definition-of-attest-engagement-team/ | 2026-08-17 | full |
| AT-PEEC-2026 | AICPA weighs PE and tech impact on audit independence rules | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules | 2026-08-31 | full |
| JOFA-PE-2025 | Independence rules and private equity | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2025/mar/independence-rules-private-equity/ | 2025-03-10 | full |
| JOFA-NILSEN-2025 | Navigating outside investors: Safeguarding ethics and independence in evolving practice structures | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2025/oct/navigating-outside-investors-safeguarding-ethics-and-independence-in-evolving-practice-structures/ | 2025-10-24 | full |
| JOFA-SOCETH-2026 | SOC engagements: ethics risks with tool providers | Journal of Accountancy (AICPA ethics staff) | professional-body | https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 | full |
| JOFA-ETHICSAI-2026 | Accounting ethics in the age of AI | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 | full |
| JOFA-IESBAAPS-2026 | IESBA to assess need for standards on alternative practice structures | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/mar/iesba-to-assess-need-for-standards-on-alternative-practice-structures/ | 2026-03-27 | full |
| JOFA-PCAOBAG-2026 | PCAOB shares agendas for rulemaking, research | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/pcaob-shares-agenda-for-rulemaking-research/ | 2026-10-01 | full |
| AICPA-APSED-2025 | Alternative Practice Structures: Proposed Revisions to the AICPA Code (exposure draft landing page) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/download/ethics-APS-ED | 2025-12 | full (landing page; PDF gated) |
| AICPA-PEECWEBCAST-2026 | Webcast: PEEC's Q3 2026 Meeting | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/download/webcast-peecs-q3-2026-meeting | 2026-08-07 | full (landing page) |
| AICPA-PEECMEET-2026 | PEEC Meeting Materials and Information | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/article/peec-meeting-information | 2026-09-25 | full (landing page; lists the 19 Oct 2026 meeting) |
| IESBA-SNAPSHOT-2026 | IESBA Snapshot: Ethics and Independence Approach to the Use of Technology | IESBA | standard-setter | https://www.ethicsboard.org/news-events/2026-06/iesba-snapshot-ethics-and-independence-approach-use-technology | 2026-06-11 | full |
| IESBA-NAM-2026 | Emerging Technologies: A Characteristics-Based Approach to Ethical Considerations for Professional Accountants | IESBA | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-07/Emerging-Technologies-Ethical-Considerations-for-Professional-Accountants.pdf | 2026-07-15 | full |
| IESBA-HIGHLIGHTS-2026 | IESBA Meeting Highlights and Decisions, June 2026 (APESB copy) | IESBA | standard-setter | https://apesb.org.au/wp-content/uploads/2026/08/Agenda_Item_3_a_-Jun_2026_IESBA_Meeting_Highlights.pdf | 2026-06 | full |
| APESB-IESBACHAIR-2026 | IESBA Chair update (APESB meeting agenda item 6) | APESB (IESBA slides) | standard-setter | https://apesb.org.au/wp-content/uploads/2026/03/Agenda_Item_6_APESB_Meeting_March_26_Sydney_-IESBA_Chair_Update.pdf | 2026-03 | full |
| IESBA-EEA-2026 | Ethics is not the constraint on AI assurance. It is the foundation (EAA Congress presentation) | IESBA | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-06/EAA_IESBA_Presentation_final.pdf | 2026-05 | full |
| IESBA-APESB-2023 | Applying the Code's Conceptual Framework to Independence: Practical Guidance for Auditors in Technology-Related Scenarios | IESBA and APESB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2023-07/IESBA_APESB_Applying_the_Code_s_Conceptual_Framework_to_Independence_0.pdf | 2023-07-13 | full |
| IESBA-TECHREV-2023 | Final Pronouncement: Technology-related Revisions to the Code | IESBA | standard-setter | https://www.ethicsboard.org/publications/final-pronouncement-technology-related-revisions-code | 2023-04-11 | full |
| ICAS-IESBA-2026 | IESBA issues snapshot on the ethical implications of using technology, including AI | ICAS | professional-body | https://icas.com/news-insights-events/news/ethics/iesba-issues-snapshot-on-the-ethical-implications-of-using-technology-including-ai/ | 2026-07-14 | full |
| SEC-REGSX-2-01 | 17 CFR 210.2-01 Qualifications of accountants | SEC (text via Cornell LII) | regulator | https://www.law.cornell.edu/cfr/text/17/210.2-01 | 2020-12 | full |
| TR-HOHL-2026 | SEC Chief Accountant Hohl Dispels Rumors of Weakening Auditor Independence Rules | Thomson Reuters Tax & Accounting | press | https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/ | 2026-06-05 | full |
| NYSSCPA-HOHL-2026 | SEC chief accountant clarifies agency's approach to auditor independence | NYSSCPA (summarising Reuters) | professional-body | https://nysscpa.org/news/1048128-sec-chief-accountant-clarifies-agencys-approach-to-auditor-independence-2026-06-08 | 2026-06-08 | full |
| KPMG-HOHL-2026 | Q&A with Kurt Hohl, SEC chief accountant | KPMG Board Leadership Center | firm | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | 2026-05-27 | full |
| TR-HOHLAGENDA-2025 | SEC chief accountant unveils ambitious agenda for audit oversight standard setting | Thomson Reuters Tax & Accounting | press | https://tax.thomsonreuters.com/news/sec-chief-accountant-unveils-ambitious-agenda-for-audit-oversight-standard-setting/ | 2025-12-10 | full |
| STARLING-HOHLWSJ-2026 | US SEC Weighs Audit Oversight Changes | Starling Insights | press | https://insights.starlingtrust.com/content/observations/us-sec-weighs-audit-oversight-changes | 2026-01-22 | full |
| BLOOMBERG-PCAOBPE-2025 | US Audit Board to Examine Quality Safeguards at PE-Backed Firms | Bloomberg Tax | press | https://news.bloomberglaw.com/daily-tax-report/us-audit-board-to-examine-quality-safeguards-at-pe-backed-firms | 2025-12-09 | search-only (opening paragraphs; paywalled) |
| JOFA-PCAOBQC-2026 | PCAOB finalizes simplified quality control amendments | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/sep/pcaob-finalizes-simplified-quality-control-amendments/ | 2026-09-09 | full |
| PCAOB-BOULAY-2026 | Final Report of Inspection, Boulay PLLP | PCAOB | regulator | https://boulaygroup.com/wp-content/uploads/2026/09/PCAOB-Final-Inpection-Report-Boulay-PLLP-9-14-2026.pdf | 2026-09-14 | full |
| FRC-PCLETTER-2024 | External private capital and UK audit firms | Financial Reporting Council | regulator | https://www.frc.org.uk/documents/7733/Letter_on_private_capital_in_audit_firms.pdf | 2024-09-26 | full |
| ICAEW-PE-2024 | Private equity investment in audit firms | ICAEW | professional-body | https://www.icaew.com/regulation/working-in-the-regulated-area-of-audit/audit-regulations-and-guidance/private-equity-investment-in-audit-firms | 2024-10 | full |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full (keyword check for acceptance and independence terms; not read line by line) |
| UKGOV-AMLSTRAT-2026 | Anti-money laundering and asset recovery strategy: 2026 to 2029 | HM Treasury and Home Office | regulator | https://www.gov.uk/government/publications/anti-money-laundering-and-asset-recovery-strategy-2026-to-2029 | 2026-09-15 | full |
| ICAEW-AML-2026 | AML latest updates and reviewer insights: key takeaways from our webinar | ICAEW | professional-body | https://www.icaew.com/regulation/regulatory-news/regulatory-news-2026-06/aml-latest-updates-and-reviewer-insights-webinar | 2026-06 | full |
| SPB-AML-2026 | A new strategy against money laundering | Squire Patton Boggs | press | https://www.squirepattonboggs.com/media/xxcnvl2i/a-new-strategy-against-money-laundering.pdf | 2026-09-22 | full |
| TLT-AML-2026 | AML reform is accelerating: what firms should take from the UK's 2026-2029 strategy | TLT LLP | press | https://www.tlt.com/insights-and-events/insight/aml-reform-is-accelerating-what-firms-should-take-from-the-uks-2026-2029-strategy | 2026-09-18 | full |
| ICAS-MLR-2026 | Money Laundering Regulations 2026: What accountants need to know | ICAS | professional-body | https://icas.com/news-insights-events/news/practice/money-laundering-regulations-2026-what-accountants-need-to-know/ | 2026-09-28 | full |
| ACCEU-PE-2025 | Beyond private equity: third party ownership in the accountancy and audit sector | Accountancy Europe | professional-body | https://accountancyeurope.eu/wp-content/uploads/2025/11/251121-Beyond-Private-Equity-Third-Party-ownership-summary.pdf | 2025-11-21 | full |
| ICAS-PE-2025 | Private equity investment must respect need for audit quality | ICAS | professional-body | https://icas.com/news-insights-events/news/audit-assurance/private-equity-investment-must-respect-need-for-audit-quality | 2025-06-02 | full |
| NYK-TAR-2024 | Does Private Equity Investment in Accounting Firms Affect Perceived and Actual Audit Quality? (registered report proposal) | The Accounting Review (Borysoff, Conaway, Riedl) | academic | https://business.gwu.edu/sites/g/files/zaxdzs5326/files/2024-06/maria_nykyforovych.pdf | 2024-06 | full |
| AAA-CIIA-2025 | Call for Papers, Current Issues in Auditing: Private Equity Impact on Auditing | American Accounting Association | academic | https://aaahq.org/portals/0/documents/calls/2026/CIIA%20PE%20and%20Audit%20Firms.pdf | 2025-11 | full |
| WFU-CONAWAY-2025 | Exploring Private Equity in Accounting | Wake Forest University School of Business | academic | https://business.wfu.edu/stories/exploring-private-equity-in-accounting/ | 2025-11-26 | full |
| CEBI-2024 | Development of a decision support system for client acceptance in independent audit process | International Journal of Accounting Information Systems | academic | https://avesis.cumhuriyet.edu.tr/yayin/cffa6431-8a21-4556-a92e-66d0ba2e1092/development-of-a-decision-support-system-for-client-acceptance-in-independent-audit-process | 2024-06 | full (abstract) |
| JB-JAR-2004 | Audit firm portfolio management decisions | Journal of Accounting Research | academic | https://academicnewsletter.sufe.edu.cn/info/413496 | 2004-07-29 | full (abstract) |
| LIBBY-CIIA-2025 | Artificial Intelligence in Auditing: How Auditor AI Use Can Mitigate Legal Liability | Current Issues in Auditing (Libby and Witz) | academic | https://www.citedrive.com/en/discovery/artificial-intelligence-in-auditing-how-auditor-ai-use-can-mitigate-legal-liability | 2025-10-03 | full (summary abstract; date from DOI metadata 10.2308/ciia-2024-029) |
| CPACOM-ATR-2025 | Audit Transformation Report: 2025 CPA.com and AICPA Audit Benchmark Survey | CPA.com and AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full (date from PDF creation date 8 Dec 2025) |
| ICAS-ATI-2026 | Confidence in audit remains high, but stakeholder expectations are evolving (Audit Trust Index 2026) | ICAS (summarising CPIA research) | survey | https://icas.com/news-insights-events/news/audit-assurance/confidence-in-audit-remains-high-but-stakeholder-expectations-are-evolving/ | 2026-10-13 | full |
| IRBA-AI-2023 | Artificial Intelligence Audit Risks Mitigation | Independent Regulatory Board for Auditors | regulator | https://www.irba.co.za/upload/report_files/02.-AI-Audit-Risks-Mitigation.pdf | 2023-01-12 | full |
| KINGLAND-ACCEPT | Client & Engagement Acceptance | Kingland | vendor | https://www.kingland.com/client-engagement-acceptance | 2026-10-16 | full (undated page; access date) |
| KINGLAND-PA-2026 | Public Accounting | Kingland | vendor | https://www.kingland.com/public-accounting | 2026-10-16 | full (undated page; access date) |
| GT-GTAP-2026 | Grant Thornton launches AI platform for audit business | Consultancy.org (Consulting.us) | press | https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business | 2026-05-11 | full |

---

## 6. Gaps

**Not found, or could not be confirmed**
- **Any measured result for AI in acceptance, KYC or independence monitoring.** No error rate, override rate, false-positive rate, parallel run, time saved, inspection finding or independent benchmark, and no named customer for any acceptance or independence tool. The Kingland pages name none.
- **Any firm describing its own AI-use acceptance process,** and any regulator inspection finding about AI in acceptance or independence systems. The PCAOB inspection report read (Boulay) says nothing on AI.
- **The outcome of the PEEC meeting on 19 Oct 2026** and the second exposure draft; both are after the date of this report.
- **The AICPA practice aid text.** Member-gated. The acceptance and continuance material comes from the AICPA release and trade summaries; the practice aid's own wording, examples and any acceptance-specific questions were not read. The same applies to the AICPA exposure draft PDF, the PEEC August 2026 presentation, the AICPA staff article "AI Through an Ethics Lens" and the 81 comment letters (member or free-account gated).
- **IESBA documents.** The Staff Alert on private equity (Jul 2025) and the board papers were not opened; the PE position rests on the IESBA June 2026 highlights and the chair's March 2026 slides. IESBA's AI-specific publication (Q4 2026) is not yet published.
- **Other regulators' PE statements.** The APESB slide lists statements by IFIAR (2024), the AFM and Germany's WPK (2025), IOSCO (2026), the DFSA and NASBA (2025 white paper), but none of these was read. The NASBA blog on the PEEC draft returned HTTP 403. The CEAOB's Nov 2025 plenary discussion of PE was seen only in a search result.
- **PCAOB primary pages.** The auditor-independence standard-setting project page, the PCAOB Dec 2025 speeches and the PCAOB staff material on independence at PE-backed firms were not reachable (pcaobus.org returns 403); the Bloomberg report was paywalled. The SEC OCA refreshed independence FAQs were not found.
- **FRC.** The Ethical Standard text and the FRC's non-audit-services exemption decisions (31 Jul 2026 batch) were not read for technology services; the FRC's annual audit quality review was not reached. ISQM 1 and PCAOB QC 1000 text on acceptance and continuance was not retrieved (iaasb.org link had no PDF; pcaobus.org blocked).
- **Intapp** (named as an acceptance, conflicts and independence vendor in the pilot) blocked access (HTTP 403). Thomson Reuters and Big Four transparency-report material on acceptance systems was not reached.
- **Academic.** No published result yet on PE and audit quality. Machine-learning litigation-warning models for acceptance and a randomized-experiment paper seen in search extracts could not be opened. The underlying Libby and Witz (2024) study was not read, only a 2025 summary article. Large-scale surveys of auditors on AI in independence were not found; the BDO India piece (BDO-INDIA-2025, 23 Sep 2025) cites a survey figure without a source and was not relied on.
- **AML.** FATF guidance for accountants and the FCA Mills Review (Jul 2026) were not opened (FATF blocked access). No accountancy-firm deployment of AI for customer due diligence was found. EU AMLA material was not searched.
- **Low-authority items not used:** a promotional commentary on PEEC, APS and AI (learnformula, 11 Aug 2026) and an AI-generated regulator communique (IRBA, kept only as a 2023 foundation).

**Data conflicts and caveats**
- IESBA's snapshot is dated 11 Jun 2026 on IESBA's site, while ICAS published its summary on 14 Jul 2026; the staff publication on emerging technologies is dated 15 Jul 2026.
- The AICPA's Feb 2025 release text says "Feb. 5, 2024" while the page is dated 5 Feb 2025.
- The Hohl material spans an interview reported Jan 2026 (Starling), a Dec 2025 AICPA conference talk, a May 2026 Q&A (KPMG) and a 4 Jun 2026 speech (TR). The landscape's note that OCA review of independence "starts with refreshed FAQs" is confirmed (TR-HOHL-2026), but the FAQs themselves were not located.
- Oath Verified's chief assurance officer is the main source on PEEC ambiguity about AI tool licensing and on her own firm's structure; treat her statements as an interested party's view.
