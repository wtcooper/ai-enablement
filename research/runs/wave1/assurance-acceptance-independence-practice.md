# Deep dive: assurance / acceptance-independence / practice

- **Archetype:** assurance
- **Module:** acceptance-independence. Client and engagement acceptance and continuance, independence and ethics, KYC/AML, engagement letters, client risk profiling.
- **Angle:** practice. What firms actually do: tools, deployments, firm processes, vendor products with named customers, structural moves, outcomes.
- **Prepared:** 2026-10-16
- **Method note.** Pages were fetched with `curl` (PDFs with `pdftotext`). Four Intapp pages returned HTTP 403 to `curl` and were read through the text mirror the brief allows; each is marked in the source list. The web-search quota ran out before the last planned searches, so some directions were not followed (see Gaps). Every source in section 5 was opened (`access: full`). Items seen only in search snippets are mentioned in Gaps and are not used as evidence. Quotations are under 25 words.

---

## 1. Summary

- **Evidence of AI inside acceptance and independence work is thin, and almost all of it is vendor-published.**
  - The one named, in-use case is Crete Professionals Alliance, a private-equity-backed accounting network. It uses Intapp Conflicts with AI and predictive risk-scoring over a consolidated data warehouse to clear conflicts and independence across member firms (INTAPP-CRETE-2024, October 2024). No measured result is published.
  - Grant Thornton UK selected Fenergo's AI-powered client lifecycle platform in March 2026 to put KYC, due diligence and engagement acceptance into one process (FENERGO-GT-2026). The release gives "thousands of hours" with no baseline and does not say the system is live.
  - Intapp and Kingland sell risk-scored acceptance workflows. Kingland's own white paper describes rule-based routing and does not describe AI (KINGLAND-WP-2024).
- **The Big Four transparency reports describe independence and acceptance systems without describing AI in them.**
  - EY UK names its Global Independence System and Global Monitoring System (EY-TR-2025). Deloitte UK describes a central conflicts team, a formal take-on process and a global acceptance and continuance platform planned for UK implementation in FY2027 (DELOITTE-UKTR-2025). KPMG Australia describes a mandatory conflicts and independence checking system (KPMG-AUTR-2025).
  - None of those passages mentions AI. They show the baseline processes that AI vendors target.
- **The need is real and independently measured.**
  - In IFIAR's 2025 survey of inspection findings (released 1 April 2026), regulators reported at least one finding on independence and ethics requirements at 43 member firms (30%) and on acceptance and continuance at 25 (18%). Sub-categories include 11 findings on tracking business relationships, financial interests and corporate family trees, and 22 on monitoring personal independence (IFIAR-SURVEY-2026).
  - These counts are not about AI. They are the pain points tools claim to address.
- **The stronger evidence is on direction two: AI-driven structural change.**
  - Capital is funding AI audit platforms and AI-built audit firms: Grant Thornton US's Gtap under an alternative practice structure (GT-GTAP-2026), Modus ($85M, invests in audit firms, AT-MODUS-2026), Repodo (new authorised firm in Denmark, CFI-REPODO-2026) and Oath Verified (OATH-2026; AT-PEEC-2026).
  - Regulators tie private equity and AI together. The PCAOB said in December 2025 it will focus on independence, culture and resources at firms with private-equity or alternative-practice-structure changes, and on AI, in 2026 inspection work (AT-PCAOBPE-2025). The SEC's chief accountant said partnerships with AI companies and private-equity ownership add further complications to independence (STARLING-HOHL-2026, a secondary summary of a Wall Street Journal interview).
- **Independence rules are being rewritten, and the AI-vendor boundary is unresolved.**
  - The AICPA's exposure draft on alternative practice structures was issued 29 December 2025 and drew 81 comment letters (AICPA-APSED-2025; AICPA-APSCL-2026). PEEC agreed in August 2026 to continue discussing a second exposure draft at an interim October meeting (JOFA-PEEC-2026); the outcome was not found.
  - A former PCAOB board member, writing from an AI audit start-up, says it is unclear when licensing an AI audit tool becomes an independence issue (AICPA-APSCL-2026, CL 16; AT-PEEC-2026).
  - The AICPA has told SOC examiners that contract terms shifting control, fees or evidence access to a tool vendor can create independence threats, and that this may also apply to other attest work (JOFA-SOCETH-2026).
- **Acceptance now has a new input: the client's own AI use.** The AICPA practice aid (13 October 2026) says heavier client reliance on AI may call for more information at acceptance and continuance, including whether the auditor can gather evidence (AT-AICPAPA-2026). No firm deployment of this was found.
- **Checked against the landscape.**
  - The IESBA's AI-specific guidance, flagged "unverified" in the pilot, is confirmed as planned for Q4 2026, with an overarching technology guidance publication released 15 July 2026 (IESBA-SNAPSHOT-2026; IESBA-NAM-2026).
  - The PEEC comment deadline of 30 April 2026 is confirmed (AICPA-APSED-2025, cover).
  - The Gtap article is dated 11 May 2026 (the landscape gives 7 May; the opened page does not state that date).

---

## 2. Use cases

Grades: no entry reaches A. Entry 01 is the only B. Entries on AI-vendor relationships, tool-provider independence, AI-use disclosure and investor-data mapping are labelled "idea" (D) because they come from standard-setter guidance, comment letters or commentary, with no firm deployment found.

```yaml
- id: assurance-acceptance-independence-01
  title: AI-assisted conflicts and independence clearance across a multi-firm accounting platform
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "A private-equity-backed network has to clear conflicts and independence across services performed at other member firms. The network's general counsel describes firms relying on spreadsheets, manual processes and long completion times before an engagement letter goes out (INTAPP-CRETE-2024)."
  solution: "All member-firm data flows into a consolidated data warehouse. Intapp Conflicts uses applied AI and predictive risk-scoring to search for and analyse potential conflicts and independence impairments, so the compliance team concentrates on high-risk results (INTAPP-CRETE-2024). Intapp's product page describes AI to surface potential issues for analysts and escalation of independence issues to partners (INTAPP-CONFLICTS-2026)."
  outcomes:
    - lever: speed
      description: "Qualitative only. Crete PA executives say the approach will relieve staff and improve the firm's risk profile. No time, accuracy or error figure is published."
      figure: none published
      measures: "not applicable"
      provenance: vendor-published
      source_ref: INTAPP-CRETE-2024
  prerequisites:
    - "A central technology stack, so the tool does not have to be re-implemented for each new member firm (INTAPP-CRETE-2024)."
    - "Member-firm data consolidated into one warehouse (INTAPP-CRETE-2024)."
  risks_and_guardrails:
    - "The release states that compliance staff act on high-risk results and remediate them; it does not describe how missed conflicts are detected (INTAPP-CRETE-2024)."
    - "Independence checking relies on complete family-tree and relationship data. IFIAR counted 11 findings in 2025 on failing to keep a reliable tracking system for business relationships, financial interests and corporate family trees up to date (IFIAR-SURVEY-2026)."
  human_checkpoints:
    - "Compliance team reviews high-risk results and decides remediation (INTAPP-CRETE-2024)."
    - "Potential conflicts and independence issues are escalated to partners for review (INTAPP-CONFLICTS-2026)."
  role_evolution: "The compliance team moves from searching and clearing to reviewing high-risk results and remediating (INTAPP-CRETE-2024)."
  evidence_grade: B
  sources:
    - { ref: INTAPP-CRETE-2024, title: "Crete Professionals Alliance uses Intapp to drive innovation and rapid growth in the highly regulated accounting market", publisher: Intapp, type: vendor, url: "https://www.intapp.com/news/crete-pa-intapp-conflicts/", date: 2024-10-15, access: full, locator: "Addressing conflicts clearance; Multiplying success sections (read via text mirror)" }
    - { ref: INTAPP-CONFLICTS-2026, title: "Conflicts and independence management for accounting firms", publisher: Intapp, type: vendor, url: "https://intapp.com/accounting/conflicts", date: 2026-10-16, access: full, locator: "Opening description; 'AI-assisted review'; 'Independence tracking' (page undated; date is retrieval date; read via text mirror)" }
    - { ref: IFIAR-SURVEY-2026, title: "IFIAR Survey of Inspection Findings 2025", publisher: IFIAR (copy hosted by Japan FSA), type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01, access: full, locator: "Appendix A, Table A.3, p. A-3" }
  last_reviewed: 2026-10-16
  notes: "The deployment is announced in a vendor press release with customer quotes, dated October 2024, so it falls outside the 12 to 18 month window. It is kept because it is the only named, in-use AI acceptance or independence tool found. The IFIAR counts measure inspection findings and are not about AI. Intapp's claim of use at 16 of the top 20 accounting firms appeared only in a search snippet and is not verified."

- id: assurance-acceptance-independence-02
  title: One AI-enabled onboarding process that combines KYC, due diligence and engagement acceptance at an audit firm
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [transaction-processing, review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Client onboarding, due diligence and engagement acceptance at a large audit and advisory firm sit in separate steps. The firm wants to cut onboarding time and meet regulatory requirements consistently (FENERGO-GT-2026)."
  solution: "Grant Thornton UK selected Fenergo's AI-powered client lifecycle management platform to centralise onboarding, due diligence and compliance, bringing KYC, client due diligence and engagement acceptance into one process (FENERGO-GT-2026)."
  outcomes:
    - lever: capacity
      description: "The release says the new system removes thousands of hours of manual effort and lets clients start work faster. It gives no baseline, period or scope."
      figure: "thousands of hours"
      measures: "manual effort removed by the new system, as stated in the vendor release; baseline, period and scope are not stated"
      provenance: vendor-published
      source_ref: FENERGO-GT-2026
  prerequisites:
    - "Not stated in the source."
  risks_and_guardrails:
    - "The firm's COO refers to supporting regulatory readiness. The release states no AI-specific controls, accuracy checks or review rules (FENERGO-GT-2026)."
  human_checkpoints:
    - "Not stated in the source."
  role_evolution: "The release says teams are freed to focus on higher-value work (FENERGO-GT-2026)."
  evidence_grade: C
  sources:
    - { ref: FENERGO-GT-2026, title: "Grant Thornton UK Selects Fenergo to Streamline Client Onboarding and Drive Efficiency", publisher: Fenergo, type: vendor, url: "https://www.fenergo.com/newsroom/grant-thornton-uk-selects-fenergo-to-streamline-client-onboarding-and-drive-efficiency", date: 2026-03-04, access: full, locator: "Paragraphs 1 to 3 and quoted statements" }
  last_reviewed: 2026-10-16
  notes: "The firm is named but the release says only 'selected' and 'adoption'. Go-live and use are not stated, so the maturity is announced."

- id: assurance-acceptance-independence-03
  title: Risk-scored acceptance and continuance workflow with automated data pull, routing and AI request summaries
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, coordination-scheduling]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Acceptance and continuance data sits in several systems and is often handled in Excel and email. Kingland's white paper says hundreds or even thousands of hours a year can be wasted on poorly configured workflows (KINGLAND-WP-2024)."
  solution: "Vendors sell configurable questionnaires, risk scoring and automated routing. Intapp Intake combines integrated data, risk-based questionnaires and scoring models, AI request summaries for each role, and independence tracking (INTAPP-INTAKE-2026). Kingland's acceptance solution aggregates independence, conflicts and reputational risk signals, pulls data into the workflow, embeds KYC and routes decisions to reviewers (KINGLAND-ACCEPT-2026). Kingland describes its AI use as confidence-scored with human-in-the-loop oversight (KINGLAND-ACCEPT-2026). The white paper describes automatic escalation of risk and roll-forward of acceptance records for continuance, and does not describe AI (KINGLAND-WP-2024)."
  outcomes:
    - lever: speed
      description: "No customer result, time saving or error rate is published."
      figure: none published
      measures: "not applicable"
      provenance: vendor-published
      source_ref: KINGLAND-ACCEPT-2026
  prerequisites:
    - "Integration with the firm's existing systems so acceptance is triggered at the right time (KINGLAND-ACCEPT-2026)."
    - "Firm-defined questions, thresholds and decision logic (KINGLAND-ACCEPT-2026)."
  risks_and_guardrails:
    - "Kingland frames acceptance and continuance as part of the firm's system of quality management, with independence, risk, ethics and conflicts processes to be orchestrated together (KINGLAND-WP-2024)."
  human_checkpoints:
    - "Risk managers or risk teams review and approve when risk is detected in the workflow (KINGLAND-WP-2024)."
    - "Decisions route to reviewers for sign-off (KINGLAND-ACCEPT-2026)."
  role_evolution: "Intapp says partners' time is freed from routine acceptance tasks (INTAPP-INTAKE-2026)."
  evidence_grade: C
  sources:
    - { ref: INTAPP-INTAKE-2026, title: "Business acceptance and continuance solution for accounting firms", publisher: Intapp, type: vendor, url: "https://intapp.com/accounting/client-onboarding-continuance/", date: 2026-10-16, access: full, locator: "Opening description; 'AI request summaries'; 'Independence tracking' (page undated; date is retrieval date; read via text mirror)" }
    - { ref: KINGLAND-ACCEPT-2026, title: "Client & Engagement Acceptance", publisher: Kingland, type: vendor, url: "https://www.kingland.com/client-engagement-acceptance", date: 2026-10-16, access: full, locator: "Solution description; 'AI Ecosystem' (page undated; date is retrieval date)" }
    - { ref: KINGLAND-WP-2024, title: "Solving for Acceptance & Continuance", publisher: Kingland, type: vendor, url: "https://blog.kingland.com/hubfs/Whitepapers/Public%20Accounting/PA%20TL%20-%20Solving%20for%20Acceptance%20%26%20Continuance.pdf", date: 2024-12-03, access: full, locator: "Workflow Configurability; Risk Radar & Escalation; Roll-forward Continuance" }
  last_reviewed: 2026-10-16
  notes: "Product descriptions only; no named customer for either product in the opened material. Intapp's customer for the related conflicts product is entry 01."

- id: assurance-acceptance-independence-04
  title: Pricing and targeting engagements from historical firm data inside the acceptance process
  archetype: assurance
  module: acceptance-independence
  function: strategy-planning
  work_types: [data-reporting, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Intapp's white paper says firms have treated acceptance, continuance and independence checking as a cost centre. It argues the true cost of each engagement and its risk are not known well enough to price it (INTAPP-WP-2024)."
  solution: "Use historical firm data inside the automated acceptance process to set prices and terms to reflect expected value, to target high-value clients, and to steer partners with whitelists and blacklists (INTAPP-WP-2024)."
  outcomes:
    - lever: growth
      description: "The white paper lists 'potential revenue impact' ranges for automating acceptance, continuance and independence processes. They are estimates, not measured results."
      figure: "1.5 to 4% (informed pricing of engagements); 1 to 3% (strategic targeting); 0.05 to 1.5% (identifying ethical and business conflicts)"
      measures: "labelled 'potential revenue impact' of automating acceptance and independence processes; the revenue base and method are not stated in the extract"
      provenance: vendor-published
      source_ref: INTAPP-WP-2024
  prerequisites:
    - "Historical engagement cost and outcome data held in one place (INTAPP-WP-2024)."
  risks_and_guardrails:
    - "The white paper does not discuss how pricing from risk data interacts with independence rules on fees or with the 'ethical and business conflicts' check."
  human_checkpoints:
    - "Not stated in the source."
  role_evolution: "Not stated in the source."
  evidence_grade: C
  sources:
    - { ref: INTAPP-WP-2024, title: "Acceptance, continuance, and independence: Cost and compliance: necessity to revenue generator", publisher: Intapp, type: vendor, url: "https://intapp.com/wp-content/uploads/2024/02/Acceptance-continuance-independence-in-accounting.pdf", date: 2024-02, access: full, locator: "p. 5, 'Using the acceptance, continuance and independence processes to maximize revenue'" }
  last_reviewed: 2026-10-16
  notes: "Date taken from the file's upload path (2024/02); the PDF shows no publication date. The white paper is about automation in general; AI is not the stated mechanism. Vendor estimate only."

- id: assurance-acceptance-independence-05
  title: Automated engagement-letter production in the audit workflow
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Engagement letters are produced for every audit and must reflect the engagement's terms."
  solution: "Some firms use an automated solution for engagement letters (CPACOM-ATR-2025). The survey item asks about 'automated solutions' and does not say whether AI is used."
  outcomes:
    - lever: capacity
      description: "Share of surveyed firms with an automated engagement-letter solution."
      figure: "26%"
      measures: "share of respondents (54 US CPA firms with complete data) saying the firm has an automated solution for engagement letters; multi-select question"
      provenance: independent
      source_ref: CPACOM-ATR-2025
  prerequisites:
    - "Not stated in the source."
  risks_and_guardrails:
    - "Not stated in the source."
  human_checkpoints:
    - "Not stated in the source."
  role_evolution: "Not stated in the source."
  evidence_grade: C
  sources:
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: CPA.com (AICPA), type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "Theme 1, chart 'For which of the following does the firm have an automated solution?' (pp. 9 to 10)" }
  last_reviewed: 2026-10-16
  notes: "Unnamed firms, so the maturity is emerging rather than in-production. Included because engagement letters are in the module scope; the AI role is not evidenced. Nothing found on AI-drafted engagement terms tailored to client risk."

- id: assurance-acceptance-independence-06
  title: Deciding whether and how to disclose the firm's own AI use in engagement letters (idea)
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [document-production, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Auditors using AI tools must decide whether the engagement letter should say so."
  solution: "The AICPA practice aid says AU-C 210 does not require disclosure of specific tools, AI included, because the engagement letter covers what the auditor does and not how. It adds that applicable laws, regulations, contractual agreements or firm policies may require disclosure, and that some states require licensed professionals to disclose certain AI uses in advance, which may be done in the engagement letter (AT-AICPAPA-2026; CFODIVE-AICPAPA-2026). This is an idea: no firm practice was found."
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: AT-AICPAPA-2026
  prerequisites:
    - "An inventory of which AI tools are used on which engagements, and a check of state disclosure laws (AT-AICPAPA-2026)."
  risks_and_guardrails:
    - "Disclosure requirements depend on state law, contracts and firm policy, not on the auditing standard (CFODIVE-AICPAPA-2026)."
  human_checkpoints:
    - "Engagement partner and firm risk function decide the wording against firm policy (inferred from the guidance; not stated by the source)."
  role_evolution: "Not stated in the source."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "Paragraphs on AU-C section 210 and the engagement letter" }
    - { ref: CFODIVE-AICPAPA-2026, title: "AICPA issues guidance for AI-assisted auditing", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/", date: 2026-10-13, access: full, locator: "Frequently asked questions paragraph on engagement letters" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The practice aid's full text is behind an AICPA login and was not read; the position is taken from two press accounts that agree."

- id: assurance-acceptance-independence-07
  title: Assessing a client's AI reliance as an input to acceptance and continuance (idea)
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Clients increasingly use AI in financial reporting, sometimes in agent-run processes with no traceable workflow. The auditor may not be able to gather evidence, and management may not understand its own outputs (AT-AICPAPA-2026)."
  solution: "The AICPA practice aid says an entity's AI use may affect acceptance or continuance through the nature and circumstances of the engagement, management's integrity and ethical values, management's skills, and the engagement team's competence. The more the entity relies on AI outputs, the more information the auditor may need, such as whether evidence can be gathered. Heavy AI use may resemble reliance on external specialists and complex valuation models (AT-AICPAPA-2026). The SEC's chief accountant says some companies that say they are not using AI are doing so when asked (KPMG-HOHL-2026)."
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: AT-AICPAPA-2026
  prerequisites:
    - "Acceptance questionnaires and client-understanding steps that ask about AI in financial reporting (inferred; not stated by the source)."
    - "Team members able to assess AI-related risk, which the practice aid describes as a blend of audit, AI, data and specialist skills (AICPA-PA-2026)."
  risks_and_guardrails:
    - "The entity's use of AI does not change management's responsibility for the financial statements (AT-AICPAPA-2026)."
  human_checkpoints:
    - "Engagement partner and firm risk function make the acceptance or continuance decision (inferred; not stated by the source)."
  role_evolution: "Acceptance reviewers need to judge AI governance and AI-driven processes, not only management integrity and the client's industry (inferred from AT-AICPAPA-2026)."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "Paragraphs on acceptance or continuance and on external specialists and complex valuation models" }
    - { ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: AICPA, type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "Section one topics list" }
    - { ref: KPMG-HOHL-2026, title: "Q&A with Kurt Hohl, SEC chief accountant", publisher: KPMG Board Leadership Center (interview of an SEC official), type: regulator, url: "https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html", date: 2026-05-27, access: full, locator: "Answer on AI and audit committees" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). It is guidance issued three days before this scan. No firm was found that has changed its acceptance procedures for this, and no client-level data on how often it changes a decision. The practice aid's full text was not read."

- id: assurance-acceptance-independence-08
  title: Proprietary AI audit platform built and rolled out by an audit firm in an alternative practice structure
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Grant Thornton US operates with attest services in Grant Thornton LLP and non-attest services in Grant Thornton Advisors since New Mountain Capital's 2024 acquisition. The firm wants consistent, repeatable audit execution across a platform of nearly 25,000 people (GT-GTAP-2026)."
  solution: "Grant Thornton US launched Gtap, a cloud platform that embeds analytics, automation and AI into every stage of the audit lifecycle, with AI agents that identify risks, anomalies and insights. It was first developed by Grant Thornton Ireland, will be used on private-company audits first, and is expected to expand to public-company audits the next year (GT-GTAP-2026)."
  outcomes:
    - lever: quality
      description: "The CEO says automating transactional work lets teams focus on judgment and says the approach increases consistency. No measured result is published."
      figure: none published
      measures: "not applicable"
      provenance: self-reported
      source_ref: GT-GTAP-2026
  prerequisites:
    - "Acquisition and integration of country member firms; the practice built in Ireland was scaled up (GT-GTAP-2026)."
  risks_and_guardrails:
    - "Attest and non-attest entities are kept separate for regulatory reasons (GT-GTAP-2026)."
    - "The PCAOB said in December 2025 it will focus on independence, culture and resources at quality-control inspections of firms with private-equity or alternative-practice-structure changes (AT-PCAOBPE-2025)."
  human_checkpoints:
    - "The firm says professionals supervise every step (GT-GTAP-2026)."
  role_evolution: "Teams focus on professional skepticism, judgment and risk assessment rather than transactional steps, per the CEO (GT-GTAP-2026)."
  evidence_grade: C
  sources:
    - { ref: GT-GTAP-2026, title: "Grant Thornton launches AI platform for audit business", publisher: Consulting.us, type: press, url: "https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business", date: 2026-05-11, access: full, locator: "Paragraphs 2 to 8" }
    - { ref: AT-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe", date: 2025-12-09, access: full, locator: "Section 'PE warning'" }
  last_reviewed: 2026-10-16
  notes: "The firm announced the launch; the page does not state use on engagements, so the maturity is announced. The landscape gives 7 May 2026 as the launch date; the opened page is dated 11 May 2026. Independence is relevant because the platform's owner and the attest firm are under an alternative practice structure. This entry covers the structural point only; the platform's audit functions belong to the planning and substantive modules."

- id: assurance-acceptance-independence-09
  title: Investor-funded holding company that builds AI audit tooling and invests in audit firms
  archetype: assurance
  module: acceptance-independence
  function: strategy-planning
  work_types: [expert-judgment, coordination-scheduling]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Audit tools and workflows have not meaningfully changed in decades, according to Modus's CEO. Lightspeed's partners say public accounting has been underserved by technology (AT-MODUS-2026)."
  solution: "Modus raised $85 million in seed and Series A funding led by Lightspeed Venture Partners to invest in and partner with audit-first accounting firms and to build AI-enabled audit tooling. It has invested in one top-200 firm and, according to Lightspeed, has deployed seven AI workflows there (AT-MODUS-2026)."
  outcomes:
    - lever: capacity
      description: "Funding and deployment counts only. No audit-quality or efficiency result is published."
      figure: "$85 million raised; seven AI workflows deployed in one firm"
      measures: "round size as reported; number of AI workflows deployed in the one top-200 firm it has invested in, per Lightspeed; the firm is not named"
      provenance: vendor-published
      source_ref: AT-MODUS-2026
  prerequisites:
    - "An audit firm willing to take investment and share expertise to improve the tools (AT-MODUS-2026)."
  risks_and_guardrails:
    - "The article does not discuss independence. The AICPA's draft treatment of investors, upstream entities and network firms would apply to firms in this kind of structure (AICPA-APSED-2025)."
  human_checkpoints:
    - "Not stated in the source."
  role_evolution: "Not stated in the source."
  evidence_grade: C
  sources:
    - { ref: AT-MODUS-2026, title: "Modus raises $85M to invest in audit firms, tech", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/modus-raises-85m-to-invest-in-audit-firms-tech", date: 2026-04-08, access: full, locator: "Paragraphs 1 to 5" }
    - { ref: AICPA-APSED-2025, title: "Exposure draft: Proposed revisions related to alternative practice structures", publisher: AICPA Professional Ethics Division, type: standard-setter, url: "https://assets.ctfassets.net/rb9cdnjh59cm/3M0CFAUnOquO2oDNiH0VF5/b8adc950ef4775cbe359349dc706cbbe/ethics-ED-APS-2025.pdf", date: 2025-12-29, access: full, locator: "Explanatory material paras 16 to 23" }
  last_reviewed: 2026-10-16
  notes: "The deployment count is an investor's statement about an unnamed firm. Whether Modus's structure counts as an alternative practice structure under the AICPA draft is not addressed in any opened source."

- id: assurance-acceptance-independence-10
  title: New regulated audit firms built around AI from the start
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Auditing has been slower than other professions to absorb automation and still relies on manual collection, matching and documentation, according to coverage of Repodo's launch (CFI-REPODO-2026). Oath Verified says the audit model was built around human work and annual cycles (OATH-2026)."
  solution: "Repodo, a Copenhagen audit firm, raised EUR 8.2 million pre-seed, is authorised to issue statutory opinions through a licensed auditor co-founder, and plans to serve small and medium-sized Danish companies first. AI systems are meant to handle much of the repetitive work while qualified people keep judgment, oversight and the signature (CFI-REPODO-2026). Oath Verified describes itself as a modern audit firm running a continuous verification platform (OATH-2026). Its chief assurance officer says it uses an alternative practice structure because it is venture-backed and state regulators require one to create an attest entity (AT-PEEC-2026)."
  outcomes:
    - lever: growth
      description: "Funding figures only. No client, quality or independence result is published."
      figure: "EUR 8.2 million pre-seed (Repodo); about $10 million raised in total (Oath Verified)"
      measures: "amounts raised as reported by the press; not an outcome of audit work"
      provenance: vendor-published
      source_ref: CFI-REPODO-2026
  prerequisites:
    - "A licensed auditor who can sign opinions (CFI-REPODO-2026)."
    - "In the US, an attest entity set up inside an alternative practice structure when a technology company has venture investors (AT-PEEC-2026)."
  risks_and_guardrails:
    - "Under the AICPA draft, an attest firm would be barred from attesting for entities where an upstream entity of the nonattest entity is an affiliate. Oath's chief assurance officer argues this is disproportionate for passive venture investors (AICPA-APSCL-2026, CL 16)."
  human_checkpoints:
    - "Licensed professionals keep final responsibility for the opinion (CFI-REPODO-2026)."
  role_evolution: "Oath is hiring what it calls 'accountant engineers' (AT-PEEC-2026)."
  evidence_grade: C
  sources:
    - { ref: CFI-REPODO-2026, title: "Former Lunar Execs To Launch AI-enabled Audit Firm Repodo After Securing New Funding", publisher: Crowdfund Insider, type: press, url: "https://www.crowdfundinsider.com/2026/08/302190-former-lunar-execs-to-launch-ai-enabled-audit-firm-repodo-after-securing-new-funding/", date: 2026-08-27, access: full, locator: "Paragraphs 1 to 12" }
    - { ref: OATH-2026, title: "Oath | Swear by your numbers (company website)", publisher: Oath, type: firm, url: "https://www.oathverified.com/", date: 2026-10-16, access: full, locator: "'why oath' and 'services' sections (page undated; date is retrieval date)" }
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: 2026-08-31, access: full, locator: "Paragraphs on Oath's structure, funding and hiring" }
    - { ref: AICPA-APSCL-2026, title: "Comment Letters: Alternative Practice Structures", publisher: AICPA, type: standard-setter, url: "https://downloads.ctfassets.net/rb9cdnjh59cm/2k2SNDfzw8AbcvW0nfoiOs/bcfdc3e65de4e2c18a45be3e44e26900/Comment_letters_-_Alternative_practice_structures__APS_.pdf", date: 2026-05-14, access: full, locator: "CL 16 (dated 2026-04-22), section II" }
  last_reviewed: 2026-10-16
  notes: "Repodo's 'authorised' status rests on press coverage, not the Danish register, which was not checked. Oath's website describes the platform as a financial proof platform and does not state audit clients or results. Whether Repodo uses AI agents in production is not evidenced beyond the launch statements."

- id: assurance-acceptance-independence-11
  title: Technology vendors licensing AI audit tools to independent firms, with unclear independence classification (idea)
  archetype: assurance
  module: acceptance-independence
  function: strategy-planning
  work_types: [review-assurance]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: "A technology platform company that licenses AI-driven audit tools, workflow automation and evidence management to independent CPA firms on subscription would not be an alternative practice structure under a plain reading of the AICPA draft. As the platform adds data pipelines, AI-generated workpaper drafts and exception flagging that structure the engagement, the line becomes hard to draw (AICPA-APSCL-2026, CL 16)."
  solution: "The commenter proposes a safe harbour where pricing is by subscription with no revenue share, no personnel are leased, and the firm keeps governance, quality control and sign-off, and a list of factors that would cross the line, including platform contractual rights over client acceptance (AICPA-APSCL-2026, CL 16). Crete PA asks when investor-held technology contracts or investor-funded technology development become participation in delivering professional services (AICPA-APSCL-2026, CL 25). The Pennsylvania Institute of CPAs asks about added risks when a technology company in a PE portfolio offers financial reporting software used by audit clients of the attest firm (AICPA-APSCL-2026, CL 65). PwC proposes that capital that accelerates the nonattest entity's technology, which benefits the attest firm, could be a qualitative sign of close alignment (AICPA-APSCL-2026, CL 54). This is an idea: it is a regulatory-interpretation question, and no resolved case was found."
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: AICPA-APSCL-2026
  prerequisites:
    - "A decision by PEEC on how the interpretation treats technology vendors; PEEC discussed a second exposure draft in August 2026 (JOFA-PEEC-2026)."
  risks_and_guardrails:
    - "Ambiguity could favour incumbents that build AI in-house over firms and start-ups that license it, per the commenter (AT-PEEC-2026)."
    - "None of the 81 comment letters came from a technology company, according to the same commenter (AT-PEEC-2026). The comment-letter index lists firms, state boards, societies, IESBA and universities (AICPA-APSCL-2026, index)."
  human_checkpoints:
    - "Firms evaluate each vendor relationship under the conceptual framework when no interpretation applies (JOFA-OUTSIDEINV-2025)."
  role_evolution: "Not stated in the sources."
  evidence_grade: D
  sources:
    - { ref: AICPA-APSCL-2026, title: "Comment Letters: Alternative Practice Structures", publisher: AICPA, type: standard-setter, url: "https://downloads.ctfassets.net/rb9cdnjh59cm/2k2SNDfzw8AbcvW0nfoiOs/bcfdc3e65de4e2c18a45be3e44e26900/Comment_letters_-_Alternative_practice_structures__APS_.pdf", date: 2026-05-14, access: full, locator: "CL 16, section I; CL 25 'Additional Guidance Requested' on cooperation; CL 54 qualitative factors for close alignment; CL 65 answer to question (n)" }
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: 2026-08-31, access: full, locator: "Paragraphs 2 to 5" }
    - { ref: JOFA-PEEC-2026, title: "PEEC to continue discussions on alternative practice structures", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/", date: 2026-08-10, access: full, locator: "Paragraphs 1 to 3" }
    - { ref: JOFA-OUTSIDEINV-2025, title: "Navigating outside investors: Safeguarding ethics and independence in evolving practice structures", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/oct/navigating-outside-investors-safeguarding-ethics-and-independence-in-evolving-practice-structures/", date: 2025-10-24, access: full, locator: "Paragraphs on the conceptual framework" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The model is described by an insider who builds an audit technology firm (CL 16) and is not independently documented. The outcome of PEEC's October 2026 interim meeting was not found."

- id: assurance-acceptance-independence-12
  title: Independence analysis of AI tool-vendor contracts and relationships (idea)
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Tool vendors can shift control, judgment, fees, referrals or access to evidence away from the auditor, creating undue-influence and self-interest threats. The AICPA wrote this about SOC 2 tool providers and says the considerations may also be relevant to other audit and attest services (JOFA-SOCETH-2026)."
  solution: "Review vendor contracts for cross-referral concentration, vendor involvement in the work, vendor-driven deadlines, bundled fees, payment for evidence access, non-disparagement terms and marketing control (JOFA-SOCETH-2026). A commentator proposes documenting, for every tool that touches client work, who owns the vendor, whether it also serves the client, what the firm pays and whether any payment depends on volume or referrals, and whether the vendor can use client data to train models (ACCWEEKLY-INDEP-2026). This is an idea: it is guidance and opinion, and no firm was found that has published such a review process."
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: JOFA-SOCETH-2026
  prerequisites:
    - "A register of AI tools and vendor contracts across the firm (inferred from ACCWEEKLY-INDEP-2026)."
  risks_and_guardrails:
    - "If safeguards cannot eliminate significant threats, the firm should consider declining or discontinuing the engagement or the business arrangement (JOFA-SOCETH-2026)."
    - "The CIBA commentator says nobody has settled whether a vendor serving both firm and client creates a self-review or familiarity threat (ACCWEEKLY-INDEP-2026). That article is opinion by a trade-body staff member."
  human_checkpoints:
    - "The firm documents its evaluation and conclusion when safeguards are applied (JOFA-SOCETH-2026)."
  role_evolution: "Not stated in the sources."
  evidence_grade: D
  sources:
    - { ref: JOFA-SOCETH-2026, title: "SOC engagements: Ethics risks with tool providers", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/", date: 2026-04-06, access: full, locator: "Sections 'Common threats', 'Objectivity, conflicts of interest, and independence', 'Practical takeaways'" }
    - { ref: ACCWEEKLY-INDEP-2026, title: "AI Audit Tools and the Independence Gap Nobody Fixed", publisher: Accounting Weekly (CIBA author), type: press, url: "https://www.accountingweekly.com/trending-news/ai-audit-tools-and-the-independence-gap-nobody-fixed", date: 2026-09-01, access: full, locator: "Sections 'The question nobody has answered' and 'What to do about it'" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The AICPA article is about SOC 2 examinations; it states relevance to other attest work only as a possibility. The firm-level process is a proposal, not an observed practice."

- id: assurance-acceptance-independence-13
  title: Independence screening of firm alliances with AI model and cloud vendors (idea)
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Large audit networks have formal alliances with AI and cloud vendors. Deloitte announced an expanded alliance with Anthropic making Claude available to more than 470,000 people (ANTHROPIC-DELOITTE-2025). EY says its assurance agent framework runs on Microsoft technology and rests on a long-standing alliance with Microsoft (EY-CANVAS-2026). The SEC's chief accountant says problems arise when audit firms partner with non-audit clients that also rely on audit clients, and that partnerships with AI companies add complications (STARLING-HOHL-2026)."
  solution: "Independence functions would map commercial relationships with AI vendors against audit-client and affiliate lists, and monitor how pervasive such relationships are. The SEC official says how firms monitor independence is 'top of mind' (STARLING-HOHL-2026). This is an idea: no firm process was found, and none of the opened sources links a named alliance to an independence assessment."
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: STARLING-HOHL-2026
  prerequisites:
    - "A current register of audit clients, affiliates and commercial relationships, which IFIAR found some firms fail to maintain reliably (IFIAR-SURVEY-2026)."
  risks_and_guardrails:
    - "The SEC official said 'there's nothing in the works to loosen the independence rule' while the SEC assesses whether the rules remain fit for purpose (STARLING-HOHL-2026)."
    - "The SEC's chief accountant said independence rules must stay fit for purpose when AI is integrated into audit service delivery (KPMG-HOHL-2026)."
  human_checkpoints:
    - "Not stated in the sources."
  role_evolution: "Not stated in the sources."
  evidence_grade: D
  sources:
    - { ref: STARLING-HOHL-2026, title: "US SEC Weighs Audit Oversight Changes", publisher: Starling Insights (summary of a Wall Street Journal interview), type: press, url: "https://insights.starlingtrust.com/content/observations/us-sec-weighs-audit-oversight-changes", date: 2026-01-22, access: full, locator: "Paragraphs 2 to 3" }
    - { ref: KPMG-HOHL-2026, title: "Q&A with Kurt Hohl, SEC chief accountant", publisher: KPMG Board Leadership Center (interview of an SEC official), type: regulator, url: "https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html", date: 2026-05-27, access: full, locator: "Answer on AI and auditor independence" }
    - { ref: ANTHROPIC-DELOITTE-2025, title: "Deloitte brings Claude to 470,000 people", publisher: Anthropic, type: vendor, url: "https://www.anthropic.com/news/deloitte-anthropic-partnership", date: 2025-10-06, access: full, locator: "Paragraphs 1 to 2" }
    - { ref: EY-CANVAS-2026, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: 2026-04-07, access: full, locator: "Paragraphs on Microsoft integration and strategic alliances" }
    - { ref: IFIAR-SURVEY-2026, title: "IFIAR Survey of Inspection Findings 2025", publisher: IFIAR (copy hosted by Japan FSA), type: regulator, url: "https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf", date: 2026-04-01, access: full, locator: "Appendix A, Table A.3, p. A-3" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The Hohl remarks are known only through a secondary summary of a Wall Street Journal interview. One source is an announcement by Anthropic, whose model assisted this research. A claim that KPMG and PwC signed similar alliances with that vendor in 2026 appeared only in a page that returned HTTP 403 and was not verified."

- id: assurance-acceptance-independence-14
  title: Permissibility screening of AI-related services sold to audit and attest clients (idea)
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Firms are expanding AI services to the same clients they audit. Deloitte UK says it is expanding the scope of its AI assurance services (DELOITTE-UKTR-2025). KPMG Australia reports applying its Trusted AI Framework and receiving ISO AI accreditation, described by the firm as a world first (KPMG-AUTR-2025). The AICPA says developing or hosting an AI system for an attest client can raise independence concerns under the existing non-attest service rules (JOFA-ETHAI-2026)."
  solution: "At acceptance, screen each proposed AI-related service (build, host, assure) for self-review threats, assumption of management responsibility and commercial dependency (IESBA-SNAPSHOT-2026; JOFA-ETHAI-2026). Deloitte UK says it placed a strong emphasis in FY2025 on strengthening the assessment of independence considerations when taking on non-audit engagements, including testing the completeness of these processes (DELOITTE-UKTR-2025). That statement is not specific to AI. This is an idea: no AI-specific screening process was found."
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: IESBA-SNAPSHOT-2026
  prerequisites:
    - "A central independence team and a take-on approval step for every new engagement, as Deloitte UK describes (DELOITTE-UKTR-2025)."
  risks_and_guardrails:
    - "The IESBA says the Code's independence provisions were reinforced for self-review threats, assuming management responsibility and commercial dependencies when technology is used to deliver services to audit or assurance clients (IESBA-SNAPSHOT-2026)."
    - "The IESBA Code revisions were effective in December 2024, and the IESBA is not pursuing further Code changes for now (IESBA-SNAPSHOT-2026)."
  human_checkpoints:
    - "Independence and conflicts teams review before take-on approval (DELOITTE-UKTR-2025, Appendix 5)."
  role_evolution: "Not stated in the sources."
  evidence_grade: D
  sources:
    - { ref: DELOITTE-UKTR-2025, title: "2025 Transparency Report (Deloitte LLP and Deloitte Limited)", publisher: Deloitte UK, type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report-accessible.pdf", date: 2025-11, access: full, locator: "Executive summary paragraph on AI assurance; ethics section on non-audit engagements; Appendix 5 'Acceptance and continuance'" }
    - { ref: KPMG-AUTR-2025, title: "KPMG Australia Transparency Report 2025", publisher: KPMG Australia, type: firm, url: "https://assets.kpmg.com/content/dam/kpmgsites/au/pdf/2025/kpmg-australia-transparency-report-2025.pdf", date: 2025, access: full, locator: "Governance statement on the Trusted AI Framework and ISO AI accreditation" }
    - { ref: JOFA-ETHAI-2026, title: "Accounting ethics in the age of AI", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai/", date: 2026-08-05, access: full, locator: "Section 'AI services can raise independence concerns for attest clients'" }
    - { ref: IESBA-SNAPSHOT-2026, title: "IESBA Snapshot: Ethics and Independence Approach to the Use of Technology", publisher: IESBA, type: standard-setter, url: "https://www.ethicsboard.org/news-events/2026-06/iesba-snapshot-ethics-and-independence-approach-use-technology", date: 2026-06-11, access: full, locator: "Q3 to Q5" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The service offerings are real; the independence screening for them is the idea. The two transparency reports describe the offerings and do not discuss independence for them. Publication dates for the two transparency reports are not stated in the documents: Deloitte UK's is taken from file metadata (November 2025) and KPMG Australia's year-only date could not be refined."

- id: assurance-acceptance-independence-15
  title: Audit fee renegotiation justified by AI-enabled efficiency
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [client-interaction, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Audit has been priced on hours, seniority and review depth. If AI speeds execution, clients may expect lower fees (VERDANTIX-KPMGFEE-2026)."
  solution: "Verdantix reports that KPMG reportedly argued to its own auditor, Grant Thornton UK, that AI would make parts of the work cheaper and that fees should reflect this. Commentators split between holding fees because humans still validate and sign off, and moving to subscription or continuous 'audit as a service' pricing (VERDANTIX-KPMGFEE-2026)."
  outcomes:
    - lever: cost
      description: "No fee figure is given on the opened page."
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: VERDANTIX-KPMGFEE-2026
  prerequisites:
    - "Not stated in the source."
  risks_and_guardrails:
    - "The analyst warns that firms may normalise trade-offs in audit integrity in pursuit of efficiency (VERDANTIX-KPMGFEE-2026)."
    - "The PCAOB's acting chair said in December 2025 that private-equity-driven pressure on profitability could lead to cost-cutting and aggressive fee negotiations, citing Accountancy Europe research (AT-PCAOBPE-2025)."
  human_checkpoints:
    - "Not stated in the source."
  role_evolution: "Not stated in the source."
  evidence_grade: C
  sources:
    - { ref: VERDANTIX-KPMGFEE-2026, title: "What goes around comes around: KPMG's AI-driven fee argument raises uncomfortable questions about audit pricing models", publisher: Verdantix, type: press, url: "https://www.verdantix.com/venture/blog/what-goes-around-comes-around--kpmg-s-ai-driven-fee-argument-raises-uncomfortable-questions-about-audit-pricing-models", date: 2026-02-10, access: full, locator: "Paragraphs 1 to 5" }
    - { ref: AT-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe", date: 2025-12-09, access: full, locator: "Botic's remarks on private-equity risks" }
  last_reviewed: 2026-10-16
  notes: "The fee episode is reported with 'reportedly' and no primary source was found. The pilot's fee figure is not on the opened page. Analyst commentary, so grade C."

- id: assurance-acceptance-independence-16
  title: Mapping investor and upstream-entity relationships against attest clients during acceptance (idea)
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Under the AICPA draft, the attest firm would not be independent of upstream entities of the nonattest entity, and would be barred from attesting where an upstream entity is an affiliate of a financial statement attest client (AICPA-APSED-2025). Commenters say mapping an investment adviser's funds and portfolio is hard when investors do not disclose it (AICPA-APSCL-2026, CL 16; CL 77)."
  solution: "Firms would need ongoing, preferably real-time ownership and portfolio data from investors. One research-based comment letter suggests firms may need contractual rights to real-time ownership data from private-equity investors to comply with the upstream prohibition (AICPA-APSCL-2026, CL 77). Another commenter proposes that investors with significant influence or control disclose fund structure and portfolio holdings (AICPA-APSCL-2026, CL 16). Intapp markets tagging of audit clients and links to employee investment data (INTAPP-CONFLICTS-2026). This is an idea: no firm was found that does this with AI."
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable"
      provenance: independent
      source_ref: AICPA-APSCL-2026
  prerequisites:
    - "Contractual access to investor ownership data (AICPA-APSCL-2026, CL 77)."
    - "A current list of attest clients and affiliates (INTAPP-CONFLICTS-2026)."
  risks_and_guardrails:
    - "The draft's 'knows or has reason to believe' standard is not defined, and the commenter asks for a threshold for the duty to investigate (AICPA-APSCL-2026, CL 16)."
    - "The PCAOB said in December 2025 it will focus on independence at quality-control inspections of firms with private-equity changes (AT-PCAOBPE-2025)."
  human_checkpoints:
    - "Members apply the conceptual framework when a relationship is known or believed to exist (AICPA-APSCL-2026, CL 16)."
  role_evolution: "Not stated in the sources."
  evidence_grade: D
  sources:
    - { ref: AICPA-APSED-2025, title: "Exposure draft: Proposed revisions related to alternative practice structures", publisher: AICPA Professional Ethics Division, type: standard-setter, url: "https://assets.ctfassets.net/rb9cdnjh59cm/3M0CFAUnOquO2oDNiH0VF5/b8adc950ef4775cbe359349dc706cbbe/ethics-ED-APS-2025.pdf", date: 2025-12-29, access: full, locator: "Explanatory material paras 23 and 52 to 59; proposed .18b" }
    - { ref: AICPA-APSCL-2026, title: "Comment Letters: Alternative Practice Structures", publisher: AICPA, type: standard-setter, url: "https://downloads.ctfassets.net/rb9cdnjh59cm/2k2SNDfzw8AbcvW0nfoiOs/bcfdc3e65de4e2c18a45be3e44e26900/Comment_letters_-_Alternative_practice_structures__APS_.pdf", date: 2026-05-14, access: full, locator: "CL 16, section III.B; CL 77, recommendation on upstream relationships" }
    - { ref: INTAPP-CONFLICTS-2026, title: "Conflicts and independence management for accounting firms", publisher: Intapp, type: vendor, url: "https://intapp.com/accounting/conflicts", date: 2026-10-16, access: full, locator: "'Independence tracking' (page undated; date is retrieval date; read via text mirror)" }
    - { ref: AT-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe", date: 2025-12-09, access: full, locator: "Section 'PE warning'" }
  last_reviewed: 2026-10-16
  notes: "Idea (D). The need comes from the draft and commenters. The comment letter numbered CL 77 is from Florida State University per the AICPA index and draws on academic research about private-equity motives; it does not concern AI. The paragraph numbers for the explanatory material are as cited in the commenters' letters and the draft's own numbering."
```

---

## 3. Module notes

### Processes and key steps (work types)

- **Intake and client risk profiling** (`client-interaction`, `research-synthesis`). Questionnaires, scoring and data pulls from internal and third-party sources (INTAPP-INTAKE-2026; KINGLAND-WP-2024).
- **KYC, AML and client due diligence** (`transaction-processing`, `review-assurance`). Deloitte UK describes client due diligence including background checks inside a formal take-on process for every new engagement (DELOITTE-UKTR-2025, Appendix 5). Fenergo's release folds KYC, due diligence and engagement acceptance into one process (FENERGO-GT-2026).
- **Conflicts and independence clearance** (`review-assurance`). Deloitte UK has a dedicated central team reviewing conflicts, relationships and independence (DELOITTE-UKTR-2025, Appendix 5). EY UK's Global Independence System holds restricted entities, family-tree data validated by engagement teams, and notations on the restrictions that apply (EY-TR-2025, p. 49). KPMG Australia describes a mandatory conflicts and independence checking system (KPMG-AUTR-2025).
- **Approval and escalation** (`review-assurance`, `coordination-scheduling`). Deloitte UK lists take-on approvals, a separate Deal Review Board for statutory audit, assurance and equity capital market opportunities, and a global acceptance consultation for cross-border or listing cases (DELOITTE-UKTR-2025, Appendix 5).
- **Personal independence and financial interests** (`data-reporting`). EY UK's Global Monitoring System requires staff to enter securities held by them and their immediate families and notifies them when a security becomes proscribed (EY-TR-2025, p. 49). Intapp sells brokerage-linked monitoring and pre-clearance (INTAPP-EMPCOMP-2026).
- **Non-audit service approval and rotation** (`review-assurance`). EY UK describes key audit partner rotation after five years for UK public-interest entities (EY-TR-2025, Independence practices).
- **Engagement letters and terms** (`document-production`). AU-C 210 does not require naming AI tools (AT-AICPAPA-2026).
- **Continuance and roll-forward** (`review-assurance`). Kingland describes cloning acceptance records to fast-track continuance (KINGLAND-WP-2024).
- None of the transparency-report passages above describes AI in these steps. The AI mentions in these documents sit elsewhere (audit execution, AI assurance services).

### Common pain points

- Manual, spreadsheet-and-email acceptance workflows and slow completion times (INTAPP-CRETE-2024; KINGLAND-WP-2024).
- Independence clearance across several firms and an investor's upstream relationships (INTAPP-CRETE-2024; AICPA-APSCL-2026, CL 16, CL 77).
- Weak independence data: 11 findings on tracking systems and 22 on monitoring personal independence in IFIAR's 2025 survey (IFIAR-SURVEY-2026).
- Uncertainty about where an AI tool vendor sits for independence purposes (AT-PEEC-2026; ACCWEEKLY-INDEP-2026).
- Clients using AI without telling the auditor, or without traceable workflows (KPMG-HOHL-2026; AT-AICPAPA-2026).

### Metrics and benchmarks (with sources)

| Metric | Value | What it measures | Source |
|---|---|---|---|
| Independence and ethics findings | 43 firms, 30% | Member firms with at least one finding in this theme, 2025 survey of 44 regulators' inspections of 161 member firms of six global networks. The survey gives no per-theme denominator | IFIAR-SURVEY-2026, Table A.2 |
| Acceptance and continuance findings | 25 firms, 18% | Same basis, theme 'Client Risk Assessment, Acceptance and Continuance'. The 2021 to 2024 percentages were 16%, 18%, 16%, 18% | IFIAR-SURVEY-2026, Table A.2 |
| Failure to implement a reliable system for tracking business relationships, financial interests and family trees | 11 findings (2021 to 2024: 6, 17, 3, 8) | Number of findings, not firms | IFIAR-SURVEY-2026, Table A.3 |
| Failure to monitor firm and partner personal independence | 22 findings (2021 to 2024: 21, 27, 18, 18) | Number of findings | IFIAR-SURVEY-2026, Table A.3 |
| Firms with an automated engagement-letter solution | 26% | Share of 54 US CPA firms with complete survey data | CPACOM-ATR-2025, pp. 9 to 10 |
| Significant PE-related deals and mergers | More than 90 since 2020, more than half in 2025 | As stated by the PCAOB's director of registration and inspections, Dec 2025 | AT-PCAOBPE-2025 |
| Large US firms with outside capital | About half of the 30 largest over five years | Bloomberg Law's statement, Jan 2026; the page also says more than 80 deals were announced in 2025 and quotes a consultant expecting a record in 2026 | BBL-PCAOBSTRAT-2026 |
| Deloitte UK matters taken to its Public Interest Review Group in FY2025 | 32 (FY2024: 38); 82% related to work that proceeded; 9% resulted in work declined (FY2024: 19%) | Formal consultations on matters with a public-interest component; not AI-specific, and not all are audits | DELOITTE-UKTR-2025 |
| Comment letters on the AICPA APS draft | 81 | Letters received, indexed by commenter | AICPA-APSCL-2026 |

There is no published error rate, override rate, false-negative rate, parallel-run result or inspection finding for any AI tool used in acceptance, KYC or independence monitoring. The IFIAR figures describe the problems the tools address and are not evidence that tools reduce them.

### Guardrails and regulatory points

- **AICPA practice aid (13 October 2026).** Acceptance and continuance considerations for client AI use; AU-C 210 does not require naming AI tools in the engagement letter, but laws, contracts or firm policy may (AT-AICPAPA-2026; CFODIVE-AICPAPA-2026). More guidance on risk of material misstatement and evidence is planned (JOFA-AIPA-2026).
- **AICPA alternative practice structures project.** A discussion memorandum came first, in March 2025 (JOFA-PE-2025). The exposure draft (29 December 2025; comments closed 30 April 2026) separates significant influence from control by investors, adds an upstream-entity prohibition and revises the network-firm definition (AICPA-APSED-2025; JOFA-PEED-2025). It would be effective one year after adoption (JOFA-PEED-2025). In August 2026 PEEC also discussed a new interpretation prohibiting attest client investment in firms and agreed to continue discussions at an October interim meeting on a second exposure draft (JOFA-PEEC-2026).
- **AICPA attest engagement team definition.** Revised in August 2026 to exclude internal auditors, external specialists and referred-to auditors; effective for engagements beginning on or after 15 December 2026 (JOFA-PEECTEAM-2026).
- **AICPA ethics on tool providers.** Contract terms that shift control, fees or evidence access can create threats; if safeguards fail, consider declining or discontinuing (JOFA-SOCETH-2026).
- **IESBA.** Technology revisions effective December 2024, including a requirement to assess fitness for purpose of technology outputs and explicit naming of automation bias; independence reinforced for technology-enabled services (IESBA-SNAPSHOT-2026). Further Code changes are not planned for now; an overarching technology guidance was published 15 July 2026 and an AI-specific publication is planned for Q4 2026 (IESBA-SNAPSHOT-2026; IESBA-NAM-2026; IESBA-TECH-2026). On private equity, the IESBA decided in March 2026 to gather information and analyse whether a project or other initiative is needed (IESBA-APESB-2026; JOFA-IESBAAPS-2026).
- **PCAOB.** Inspectors will examine independence, culture and resources at firms with private-equity or alternative-practice-structure changes and will keep focusing on AI in 2026 inspection work (AT-PCAOBPE-2025; NYSSCPA-PCAOBPE-2025).
- **SEC Office of the Chief Accountant.** Asks auditors how they use AI and how they monitor quality control with it; says independence rules must stay fit for purpose when AI is integrated into audit delivery (KPMG-HOHL-2026). Said there is nothing in the works to loosen the independence rule (STARLING-HOHL-2026).

### Frontier signals (dated and sourced)

- 2026-10: PEEC interim meeting on a second APS exposure draft; outcome not found (JOFA-PEEC-2026).
- 2026-Q4: IESBA AI-specific non-authoritative guidance planned (IESBA-SNAPSHOT-2026).
- 2026-10-13: AICPA practice aid issued with acceptance and continuance considerations for client AI use (AICPA-PA-2026).
- 2026-08-27: Repodo announces a new AI-built authorised audit firm (CFI-REPODO-2026).
- 2026-08-31: A former PCAOB board member from an AI audit start-up says technology companies have not commented on the APS draft and ambiguity remains on AI tool licensing (AT-PEEC-2026).
- 2026-05-11: Grant Thornton US launches Gtap, with private-company audits first (GT-GTAP-2026).
- 2026-04-08: Modus raises $85 million to invest in audit firms and build AI audit technology (AT-MODUS-2026).
- 2026-03-04: Grant Thornton UK selects an AI-powered client lifecycle platform covering engagement acceptance (FENERGO-GT-2026).
- FY2027: Deloitte UK plans UK implementation of a global end-to-end acceptance and continuance platform; AI is not mentioned (DELOITTE-UKTR-2025).
- 2026-01-22: SEC chief accountant, via a Wall Street Journal interview, says AI partnerships and private-equity ownership complicate independence (STARLING-HOHL-2026).

### Workforce and role effects

- Compliance teams spend time on high-risk results instead of searching (INTAPP-CRETE-2024). Partners are meant to spend less time on routine acceptance tasks (INTAPP-INTAKE-2026).
- Private equity may increase pressure on profitability, which can reduce staffing and specialists on audit engagements, according to the PCAOB (AT-PCAOBPE-2025).
- Oath Verified hires 'accountant engineers' (AT-PEEC-2026).
- Independence and ethics professionals need to evaluate AI-related services and vendor arrangements as well as financial interests (JOFA-ETHAI-2026; JOFA-SOCETH-2026).

### Objections and concerns practitioners raise

- Private-equity incentives could shift profitability above audit quality (AT-PCAOBPE-2025).
- Independence rules were drafted around private-equity roll-ups; start-ups and vendors may be affected without noticing, and incumbents building AI in-house may be favoured (AT-PEEC-2026).
- A vendor that serves both firm and client may create self-review or familiarity threats; nobody has settled the point (ACCWEEKLY-INDEP-2026, opinion).
- Vendors pressing for speed may push firms to cut corners (JOFA-SOCFAST-2026, in the SOC context; routed below).
- Automation bias and over-reliance on AI outputs (IESBA-SNAPSHOT-2026; JOFA-ETHAI-2026).
- Client data used for AI model training requires authorisation and consent (IESBA-SNAPSHOT-2026; JOFA-ETHAI-2026).

### Interview probes for an advisor

1. Walk me through your last escalated acceptance decision. Which data came from which system, which steps are still spreadsheets, where does automation or AI touch it, and how would you know it missed a conflict?
2. How does your independence function treat commercial relationships with AI vendors and model providers, including any that are audit clients or affiliates of audit clients? Who signs off, and what do you document?
3. If you operate in or are considering an alternative practice structure, how do you map investor and upstream relationships to your attest client list today, and what data would you need to ask the investor for?
4. What do you ask clients about their own AI use at acceptance and continuance, and has the answer ever changed a decision, a fee or the team?
5. Do you sell AI build, hosting or assurance services to clients you also audit, and what test do you apply before accepting? Do you disclose your own AI use in engagement letters, and what drove that choice?

---

## 4. Routed to other modules

| Item | Target module | Why |
|---|---|---|
| SOC tool vendors as intermediaries that route clients to examiners; peer review alert on nonconforming SOC 2 engagements; template reports (JOFA-SOCFAST-2026; JOFA-PEERREV-2026; JOFA-SOCETH-2026) | other-assurance (SOC and attestation) | The independence thread is relevant here, but the engagements and quality risks are SOC-specific. JOFA-SOCETH-2026 is used in entry 12 for its independence reasoning |
| Gtap, EY Canvas agent framework, Modus workflows as audit execution tools (GT-GTAP-2026; EY-CANVAS-2026; AT-MODUS-2026) | planning-risk-assessment; controls-testing; substantive-testing | This note covers only the structural and independence angle |
| Practice aid Part 1 on AI-operated controls, risk of material misstatement and evidence when a client uses AI (AT-AICPAPA-2026) | planning-risk-assessment; controls-testing | Acceptance is one input; the rest is audit design |
| AI assurance and AI governance services as products (DELOITTE-UKTR-2025; KPMG-AUTR-2025) | other-assurance (assurance over AI systems) | The service design and standards belong there; entry 14 covers only independence screening |
| Firm approval, certification and monitoring of AI tools; SEC question on using AI to monitor quality control (AT-AICPAPA-2026; KPMG-HOHL-2026) | quality-management | Firm-level tool governance |
| AI-driven fee pressure, private-equity investment and AI-native entrants (VERDANTIX-KPMGFEE-2026; AT-PCAOBPE-2025; AT-MODUS-2026) | cross-cutting lens: audit firm business model and workforce | Landscape section 10 proposes this lens |
| Regulators' own use of AI in inspections | quality-management | Not an acceptance topic |

---

## 5. Sources

All entries were opened (`access: full`) unless stated. Dates follow the byline or page metadata. Where a page is undated, the date is the retrieval date (2026-10-16), and this is stated.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 |
| CFODIVE-AICPAPA-2026 | AICPA issues guidance for AI-assisted auditing | CFO Dive | press | https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/ | 2026-10-13 |
| KPMG-HOHL-2026 | Q&A with Kurt Hohl, SEC chief accountant | KPMG Board Leadership Center (interview of an SEC official) | regulator | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | 2026-05-27 |
| STARLING-HOHL-2026 | US SEC Weighs Audit Oversight Changes | Starling Insights (summary of a Wall Street Journal interview) | press | https://insights.starlingtrust.com/content/observations/us-sec-weighs-audit-oversight-changes | 2026-01-22 |
| BBL-PCAOBSTRAT-2026 | Audit Oversight Board Set for Renewed Industry-Friendly Strategy | Bloomberg Law / Bloomberg Tax | press | https://news.bloombergtax.com/financial-accounting/audit-oversight-board-set-for-renewed-industry-friendly-strategy | 2026-01-16 |
| AT-PCAOBPE-2025 | PCAOB warns auditors about AI and PE | Accounting Today | press | https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe | 2025-12-09 |
| NYSSCPA-PCAOBPE-2025 | PCAOB Officials Flag Opportunities and Risks as AI and Private Equity Expand in Audit Firms | NYSSCPA | professional-body | https://nysscpa.org/news/1047818-pcaob-officials-flag-opportunities-and-risks-as-ai-and-private-equity-expand-in-audit-firms-2025-12-10 | 2025-12-10 (from URL) |
| JOFA-PE-2025 | AICPA seeks feedback on independence rules related to private equity | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2025/mar/independence-rules-private-equity/ | 2025-03-10 |
| JOFA-OUTSIDEINV-2025 | Navigating outside investors: Safeguarding ethics and independence in evolving practice structures | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2025/oct/navigating-outside-investors-safeguarding-ethics-and-independence-in-evolving-practice-structures/ | 2025-10-24 |
| JOFA-PEED-2025 | AICPA proposes changes to independence guidelines related to private equity | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2025/dec/aicpa-proposes-changes-to-independence-rules-related-to-private-equity/ | 2025-12-19 |
| AICPA-APSED-2025 | Exposure draft: Proposed revisions related to alternative practice structures | AICPA Professional Ethics Division | standard-setter | https://assets.ctfassets.net/rb9cdnjh59cm/3M0CFAUnOquO2oDNiH0VF5/b8adc950ef4775cbe359349dc706cbbe/ethics-ED-APS-2025.pdf | 2025-12-29 |
| AICPA-APSCL-2026 | Comment Letters: Alternative Practice Structures (81 letters; index page dated 14 May 2026) | AICPA | standard-setter | https://downloads.ctfassets.net/rb9cdnjh59cm/2k2SNDfzw8AbcvW0nfoiOs/bcfdc3e65de4e2c18a45be3e44e26900/Comment_letters_-_Alternative_practice_structures__APS_.pdf | 2026-05-14 |
| JOFA-IESBAAPS-2026 | IESBA to assess need for standards on alternative practice structures | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/mar/iesba-to-assess-need-for-standards-on-alternative-practice-structures/ | 2026-03-27 |
| JOFA-PEEC-2026 | PEEC to continue discussions on alternative practice structures | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/ | 2026-08-10 |
| JOFA-PEECTEAM-2026 | PEEC adopts revised definition of 'attest engagement team' | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/aug/peec-adopts-revised-definition-of-attest-engagement-team/ | 2026-08-17 |
| AT-PEEC-2026 | AICPA weighs PE and tech impact on audit independence | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules | 2026-08-31 |
| ACCWEEKLY-INDEP-2026 | AI Audit Tools and the Independence Gap Nobody Fixed | Accounting Weekly (CIBA author) | press | https://www.accountingweekly.com/trending-news/ai-audit-tools-and-the-independence-gap-nobody-fixed | 2026-09-01 |
| JOFA-SOCETH-2026 | SOC engagements: Ethics risks with tool providers | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 |
| JOFA-PEERREV-2026 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 |
| JOFA-SOCFAST-2026 | Promises of 'fast and easy' threaten SOC credibility | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/ | 2026-02-01 |
| JOFA-ETHAI-2026 | Accounting ethics in the age of AI | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 |
| IESBA-SNAPSHOT-2026 | IESBA Snapshot: Ethics and Independence Approach to the Use of Technology | IESBA | standard-setter | https://www.ethicsboard.org/news-events/2026-06/iesba-snapshot-ethics-and-independence-approach-use-technology | 2026-06-11 |
| IESBA-NAM-2026 | Emerging Technologies: A Characteristics-Based Approach to Ethical Considerations for Professional Accountants (landing page; PDF not downloaded) | IESBA | standard-setter | https://www.ethicsboard.org/publications/emerging-technologies-characteristics-based-approach-ethical-considerations-professional-accountants | 2026-07-15 |
| IESBA-TECH-2026 | Technology: Ethics and Independence Considerations (focus-area page; undated, date is retrieval date) | IESBA | standard-setter | https://www.ethicsboard.org/focus-areas/technology-ethics-independence-considerations | 2026-10-16 |
| IESBA-APESB-2026 | IESBA Update, APESB Board Meeting (slides by the IESBA Chair) | IESBA presentation hosted by APESB | standard-setter | https://apesb.org.au/wp-content/uploads/2026/03/Agenda_Item_6_APESB_Meeting_March_26_Sydney_-IESBA_Chair_Update.pdf | 2026-03-26 |
| IFIAR-SURVEY-2026 | IFIAR Survey of Inspection Findings 2025 | IFIAR (copy hosted by Japan FSA) | regulator | https://www.fsa.go.jp/ifiar/2025SurveyReport.pdf | 2026-04-01 |
| GT-GTAP-2026 | Grant Thornton launches AI platform for audit business | Consulting.us | press | https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business | 2026-05-11 |
| AT-MODUS-2026 | Modus raises $85M to invest in audit firms, tech | Accounting Today | press | https://www.accountingtoday.com/news/modus-raises-85m-to-invest-in-audit-firms-tech | 2026-04-08 |
| CFI-REPODO-2026 | Former Lunar Execs To Launch AI-enabled Audit Firm Repodo After Securing New Funding | Crowdfund Insider | press | https://www.crowdfundinsider.com/2026/08/302190-former-lunar-execs-to-launch-ai-enabled-audit-firm-repodo-after-securing-new-funding/ | 2026-08-27 |
| OATH-2026 | Oath: Swear by your numbers (company website; undated, date is retrieval date) | Oath | firm | https://www.oathverified.com/ | 2026-10-16 |
| ANTHROPIC-DELOITTE-2025 | Deloitte brings Claude to 470,000 people | Anthropic | vendor | https://www.anthropic.com/news/deloitte-anthropic-partnership | 2025-10-06 |
| EY-CANVAS-2026 | EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 |
| FENERGO-GT-2026 | Grant Thornton UK Selects Fenergo to Streamline Client Onboarding and Drive Efficiency | Fenergo | vendor | https://www.fenergo.com/newsroom/grant-thornton-uk-selects-fenergo-to-streamline-client-onboarding-and-drive-efficiency | 2026-03-04 |
| INTAPP-CRETE-2024 | Crete Professionals Alliance uses Intapp to drive innovation and rapid growth in the highly regulated accounting market | Intapp | vendor | https://www.intapp.com/news/crete-pa-intapp-conflicts/ | 2024-10-15 |
| INTAPP-CONFLICTS-2026 | Conflicts and independence management for accounting firms (product page; undated, date is retrieval date; read via text mirror) | Intapp | vendor | https://intapp.com/accounting/conflicts | 2026-10-16 |
| INTAPP-INTAKE-2026 | Business acceptance and continuance solution for accounting firms (product page; undated; read via text mirror) | Intapp | vendor | https://intapp.com/accounting/client-onboarding-continuance/ | 2026-10-16 |
| INTAPP-EMPCOMP-2026 | Financial interest compliance software for accounting firms (product page; undated; read via text mirror) | Intapp | vendor | https://intapp.com/accounting/employee-compliance/ | 2026-10-16 |
| INTAPP-WP-2024 | Acceptance, continuance, and independence: Cost and compliance: necessity to revenue generator (white paper) | Intapp | vendor | https://intapp.com/wp-content/uploads/2024/02/Acceptance-continuance-independence-in-accounting.pdf | 2024-02 (from upload path) |
| KINGLAND-ACCEPT-2026 | Client & Engagement Acceptance (product page; undated, date is retrieval date) | Kingland | vendor | https://www.kingland.com/client-engagement-acceptance | 2026-10-16 |
| KINGLAND-WP-2024 | Solving for Acceptance & Continuance (white paper) | Kingland | vendor | https://blog.kingland.com/hubfs/Whitepapers/Public%20Accounting/PA%20TL%20-%20Solving%20for%20Acceptance%20%26%20Continuance.pdf | 2024-12-03 |
| EY-TR-2025 | EY UK 2025 Transparency Report | EY UK | firm | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-uk/about-us/documents/ey-uk-2025-transparency-report.pdf | 2025-10 |
| DELOITTE-UKTR-2025 | 2025 Transparency Report (Deloitte LLP and Deloitte Limited; year ended 31 May 2025) | Deloitte UK | firm | https://www.deloitte.com/content/dam/assets-zone2/uk/en/docs/about/2025/deloitte-uk-annual-review-2025-audit-transparency-report-accessible.pdf | 2025-11 (file metadata; publication date not stated) |
| KPMG-AUTR-2025 | KPMG Australia Transparency Report 2025 (1 July 2024 to 30 June 2025) | KPMG Australia | firm | https://assets.kpmg.com/content/dam/kpmgsites/au/pdf/2025/kpmg-australia-transparency-report-2025.pdf | 2025 (publication date not stated) |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (Audit Benchmark Survey) | CPA.com (AICPA) | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 (from URL path) |
| VERDANTIX-KPMGFEE-2026 | What goes around comes around: KPMG's AI-driven fee argument raises uncomfortable questions about audit pricing models | Verdantix | press | https://www.verdantix.com/venture/blog/what-goes-around-comes-around--kpmg-s-ai-driven-fee-argument-raises-uncomfortable-questions-about-audit-pricing-models | 2026-02-10 |

Distinct sources: 47 (the five Intapp items and the two Kingland items count separately).

Sources by type: regulator 2, standard-setter 7, professional-body 12, firm 4, vendor 9, press 12, survey 1. Academic, conference, podcast, community and job-posting sources: none found for this angle. Seven types are represented.

---

## 6. Gaps

**What the evidence does not show**
- No measured result for any AI tool in acceptance, KYC, conflicts or independence monitoring: no time, accuracy, override or missed-conflict figure from a firm, regulator or independent party.
- No inspection finding or regulator statement specific to AI tools in acceptance or independence work. The IFIAR counts and PCAOB remarks cover independence and AI separately.
- No Big Four, mid-tier or small-firm case where AI changed an acceptance decision, a client risk score or a fee. No job postings were found for independence or acceptance technology roles.
- Independence-monitoring tools described by firms (EY GIS and GMS, KPMG's checking system, Deloitte's central team) are not described as using AI. Intapp's employee-compliance page does not describe AI features either.
- No AI-specific KYC/AML case from an accounting firm other than Grant Thornton UK's announcement. A KYC case study found in search (Glaisyers with Thirdfort) is a law firm and was excluded.

**Not reached or not opened**
- The web-search quota ran out partway through. Not searched: PwC's and other firms' transparency-report passages on acceptance technology (the PwC Germany report returned HTTP 403), mid-tier and Big Four statements on private equity plus AI, conference and podcast material for this module, and a second AML/KYC vendor case in accounting.
- Intapp: `intapp.com` pages returned HTTP 403 to `curl`; they were read through the text mirror. Intapp's investor materials also returned 403. Its claim of use at 16 of the top 20 accounting firms appeared only in a search snippet and is not used.
- A claim that KPMG and PwC signed expanded alliances with an AI model vendor in May 2026 appeared only in a page that returned HTTP 403 (cryptobriefing.com) and could not be verified.
- Full text of the AICPA practice aid and of the AICPA ethics staff article 'AI Through an Ethics Lens' (login required). The practice-aid positions come from press accounts, which agree.
- The IESBA overarching technology guidance PDF (landing page only), its June 2026 board-meeting update on private equity, and any IESBA AI-specific publication.
- The outcome of PEEC's October 2026 interim meeting, and a second exposure draft if issued.
- The 81 AICPA comment letters were keyword-searched (AI, technology, software, vendor, platform) across the combined PDF, not read in full. The letters cited here are the ones that matched. Baker Tilly, CLA, Plante & Moran, Deloitte, EY, KPMG and Grant Thornton letters had no technology-related independence content in that search.
- Official Grant Thornton and Business Wire releases for Gtap and Modus (Business Wire returned an empty reply), and the Bech-Bruun Repodo page (403). The Danish register was not checked for Repodo's authorisation.
- The KU Auditing Symposium panel on ownership and independence, the CAQ audit partner pulse and Thomson Reuters' acceptance guidance (landscape leads not retrieved).

**Date uncertainties**
- Deloitte UK and KPMG Australia transparency reports do not state publication dates; the Deloitte date is file metadata and the KPMG date remains year-only.
- Intapp, Kingland and Oath pages are undated; retrieval date used. Intapp's white paper date comes from its upload path.
- The landscape's 7 May 2026 Gtap launch date is not on the opened article (11 May 2026).

**Disclosure.** The analyst model that did this research is made by Anthropic, and entry 13 cites an Anthropic announcement as evidence of a Deloitte alliance. It is used only for the fact of the alliance.
