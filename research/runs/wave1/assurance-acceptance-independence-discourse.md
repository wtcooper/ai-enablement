# Assurance / acceptance-independence: discourse angle (wave 1 deep dive)

- **Archetype:** assurance
- **Module:** acceptance-independence. Client and engagement acceptance and continuance, independence and ethics, KYC/AML, engagement letters and client risk profiling. Two directions: (1) AI tools used in acceptance, KYC/AML and independence monitoring; (2) AI-driven structural change creating acceptance risk and independence threats (private equity, alternative practice structures, firms' relationships with AI vendors, AI services or tools provided to audit clients).
- **Angle:** discourse. What practitioners and leaders have said in roughly the last 12 to 18 months (conference sessions, regulator speeches, practitioner articles, newsletters, podcasts, commentary).
- **Prepared:** 2026-10-16. **Window:** mainly April 2025 to October 2026. Older items are flagged as foundations.
- **Access method:** `curl` through the session proxy, `pdftotext` for PDFs, and the text mirror for two pages that refused `curl`. The web-search quota ran out partway through, so several planned leads (the Financial Times original on the Anthropic auditor story, Intapp, Kingland, other podcasts) were not reached. See section 6.

---

## 1. Summary

- **The discourse is almost entirely about direction 2, not direction 1.** I found a great deal of leader and practitioner commentary on how private equity (PE), alternative practice structures (APS) and AI relationships bear on independence. I found almost no practitioner discussion of AI being used inside acceptance, KYC or independence monitoring. What exists for direction 1 is two vendor or firm announcements (Grant Thornton UK with Fenergo, 4 Mar 2026; the Zygos AI-SENSE write-up, 10 Feb 2026) and nothing with error, override or parallel-run data.
- **Regulators and standard-setters tie PE and AI together and say they are still listening.**
  - PCAOB acting chair George Botic and inspections director Christine Gunia (speaking 9 Dec 2025) described PE and AI as the two areas to watch, and Gunia said inspectors would examine quality control at firms that took PE or APS structures (AT-PCAOBPE-2025).
  - SEC chief accountant Kurt Hohl said on 4 Jun 2026 that the SEC is in "listening mode" on PE and AI, is refreshing independence FAQs, and will review the interim independence standards with the PCAOB (TR-HOHL-2026). In Dec 2025 he said AI adds complications to the business-development relationships the independence rules govern (NYCPA-HOHL-2025).
  - The AICPA ethics committee (PEEC) discussed a second exposure draft of its APS revisions in Aug 2026 (JOFA-PEEC-2026). IESBA approved a PE terms of reference in Jun 2026 with an update due Sep 2026 (IESBA-HIGHLIGHTS-2026).
- **The AI-vendor independence question is being asked in public but has no rule or ruling.**
  - The AICPA's ethics staff warned in Apr 2026 that contract terms with SOC 2 tool providers can create independence threats, and said this may apply to other attest work (JOFA-SOCETH-2026).
  - A CIBA commentator wrote on 1 Sep 2026 that the case of a software vendor serving both the auditor and the audited client is unresolved (ACCWEEKLY-INDEP-2026).
  - Christina Ho, a former PCAOB board member now at Oath Verified, said in Aug 2026 that it remains unclear when licensing an AI audit tool becomes an independence issue (AT-PEEC-2026).
- **The sharpest new signal is commercial AI alliances limiting which clients the Big Four can accept.** Deloitte (6 Oct 2025) and KPMG (19 May 2026) announced Claude alliances with Anthropic covering their whole workforces. Press reports from Aug 2026, which cite the Financial Times and which I could not confirm at source, say this leaves EY as the likely auditor of Anthropic. Treat that as a reported, unconfirmed case (section 3, frontier signals).
- **The structural direction is large and measured by independent bodies.** IFAC counted more than 1,000 accountancy firms with PE investment in the past decade (2 Mar 2026). Accountancy Europe counted 385 transactions in 2025, of which 139 involved audit firms. Only a small share touch public-interest-entity audit (IFAC: nearly 100 firms, under 10% of PE-driven activity; Accountancy Europe: 15% of transactions).
- **Only one named firm shows a worked acceptance example.** Grant Thornton UK's chief executive said (22 Sep 2026) the firm would not audit a company in which its PE owner Cinven has invested, and that it consulted the FRC on one prospective client, agreed it was a "grey area", and did not proceed (IRISHTIMES-GT-2026).
- **Quality evidence:** none. No source reports error rates, override rates, parallel-run results, inspection findings or any independent measurement for an AI tool in acceptance, KYC or independence work.
- **Use cases:** 15 candidates (0 grade A, 4 grade B, 3 grade C, 8 grade D). Most carry a D or B grade because they are control steps created by AI-related change, not AI doing the task.

---

## 2. Use cases

Notes on reading the block:

- Several entries (04, 05, 08, 09, 10, 13, 14, 15) describe a **new human control step created by AI-related structural change**, not a task AI performs. `ladder: assist` and `pattern: other` are nominal for those, and each says so in `notes`.
- Grade D entries are labelled "idea" in the title. Each is something practitioners or standard-setters actually discuss in the cited source.
- Where a figure is a baseline or context measure and not an outcome of a tool, `description` says so.

```yaml
- id: assurance-acceptance-independence-01
  title: "AI-powered client lifecycle platform joining KYC/AML, due diligence and engagement acceptance"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [transaction-processing, review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Onboarding a new audit or advisory client passes through separate KYC, due diligence and acceptance steps with manual hand-offs, which slows the start of engagements."
  solution: "Grant Thornton UK announced a partnership with Fenergo to use an AI-powered client lifecycle management platform that brings KYC checks, due diligence and engagement acceptance into one place. The release does not describe which decisions the AI makes."
  outcomes:
    - lever: speed
      description: "Firm says the platform will speed up the start of new engagements and cut unnecessary steps and manual hand-offs while keeping regulatory controls. No figures published."
      figure: "none published"
      measures: "n/a"
      provenance: self-reported
      source_ref: GT-FENERGO-2026
  prerequisites:
    - "Not described in the release. A structured onboarding data layer looks necessary: Zygos found that most surveyed firms collected onboarding data by unstructured email (ZYGOS-AISENSE-2026)."
  risks_and_guardrails:
    - "Release says the aim is faster onboarding 'without compromising on risk or compliance' (GT-FENERGO-2026, opening paragraphs). No accuracy, false-positive or override data given."
  human_checkpoints:
    - "Not described in the release; ask who signs off the acceptance decision and how AI scores are overridden."
  role_evolution: "Not described. The firm's chief operating officer frames the change as removing friction for clients and teams (GT-FENERGO-2026)."
  evidence_grade: C
  sources:
    - { ref: GT-FENERGO-2026, title: "Faster starts, stronger safeguards: Grant Thornton upgrades client onboarding with Fenergo", publisher: "Grant Thornton UK", type: firm, url: "https://www.grantthornton.co.uk/news-centre/fenergo---march-2026/", date: "2026-03-04", access: full, locator: "press release, paragraphs 1-3" }
    - { ref: ZYGOS-AISENSE-2026, title: "Artificial Intelligence in AML Compliance", publisher: "Zygos (Softline Computer Systems)", type: vendor, url: "https://getzygos.com/?p=49476", date: "2026-02-10", access: full, locator: "section on what AI-SENSE set out to do" }
  last_reviewed: 2026-10-16
  notes: "Grade C: a press release announcing a partnership, with no evidence of production use and no measurements. Landscape file lists Kingland (acceptance workflow with confidence scoring) and Intapp (conflicts and independence); neither page was opened in this run."

- id: assurance-acceptance-independence-02
  title: "Structured digital onboarding with document capture, AI classification and risk scoring"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [transaction-processing, document-production]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Client onboarding information arrives by unstructured email and is often incomplete, so downstream AI or human screening works on poor data."
  solution: "A digital onboarding workflow replaces email exchanges with document upload, OCR and AI-based document classification, feeding a configurable client risk scoring model mapped to EU anti-money-laundering directives and Cyprus rules. The vendor describes a working prototype entering pilot with selected client firms (law, accounting and corporate-service practices, not audit-specific)."
  outcomes:
    - lever: quality
      description: "Baseline problem measure from vendor user research, not a result of the tool."
      figure: "93% and 87%"
      measures: "Of 15 surveyed compliance professionals and managing partners: 93% still gathered onboarding information through unstructured email; 87% said clients routinely submitted incomplete information."
      provenance: vendor-published
      source_ref: ZYGOS-AISENSE-2026
  prerequisites:
    - "Clean, structured intake data before any AI screening layer (vendor says it reshaped the architecture after the survey) (ZYGOS-AISENSE-2026, section on what AI-SENSE set out to do)."
  risks_and_guardrails:
    - "Prototype only; production release was planned after the write-up (ZYGOS-AISENSE-2026). Sample of 15 respondents is small."
  human_checkpoints:
    - "Compliance officer or managing partner reviews the risk score (vendor description). Specific override rules not given."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: ZYGOS-AISENSE-2026, title: "Artificial Intelligence in AML Compliance", publisher: "Zygos (Softline Computer Systems)", type: vendor, url: "https://getzygos.com/?p=49476", date: "2026-02-10", access: full, locator: "sections on what AI-SENSE set out to do and what was delivered" }
  last_reviewed: 2026-10-16
  notes: "Adjacent process: the vendor serves small professional practices in Cyprus, not audit firms specifically, which caps the grade. Page shows a later modified date of 2026-05-18."

- id: assurance-acceptance-independence-03
  title: "LLM triage of sanctions and PEP screening hits with a plain-language assessment"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Screening a prospective client or beneficial owner against sanctions and politically-exposed-person lists produces many false matches that staff clear by hand."
  solution: "A language-model pipeline filters false positives from third-party screening results and presents the remaining hits as a natural-language assessment with a confidence score, using a provider-agnostic model layer."
  outcomes:
    - lever: capacity
      description: "No accuracy, false-positive reduction or time-saving figure published; the vendor calls the false-positive filter its core innovation."
      figure: "none published"
      measures: "n/a"
      provenance: vendor-published
      source_ref: ZYGOS-AISENSE-2026
  prerequisites:
    - "A screening data provider and structured onboarding records (the vendor builds on a commercial screening API) (ZYGOS-AISENSE-2026)."
  risks_and_guardrails:
    - "Vendor states AI is meant to deliver cases already triaged and explainable, not replace the compliance officer (ZYGOS-AISENSE-2026, opening paragraphs). No validation data given."
  human_checkpoints:
    - "Compliance officer decides on each case."
  role_evolution: "Vendor positions the compliance officer as reviewing pre-reasoned cases (ZYGOS-AISENSE-2026)."
  evidence_grade: C
  sources:
    - { ref: ZYGOS-AISENSE-2026, title: "Artificial Intelligence in AML Compliance", publisher: "Zygos (Softline Computer Systems)", type: vendor, url: "https://getzygos.com/?p=49476", date: "2026-02-10", access: full, locator: "section on what was delivered (screening engine and agent)" }
  last_reviewed: 2026-10-16
  notes: "Vendor marketing about a pilot-stage product for professional practices generally. Same adjacency cap as entry 02."

- id: assurance-acceptance-independence-04
  title: "Idea: screen a prospective or continuing client's reliance on AI and the team's AI capability at acceptance and continuance"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Clients increasingly use AI in financial reporting and controls, which can raise engagement risk and demand skills the engagement team may not have."
  solution: "Add an early-engagement question on how far the client relies on AI in financial reporting and a check that the team has the blend of audit, AI, data and specialist skills needed. This is a new human assessment step, not AI performing the task."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: AICPA-PA-2026
  prerequisites:
    - "Firm criteria for what counts as significant client AI reliance; access to specialists (AICPA-PA-2026, section one summary)."
  risks_and_guardrails:
    - "AICPA release lists data, model, hallucination, explainability and bias risks to consider (AICPA-PA-2026)."
  human_checkpoints:
    - "Engagement partner and risk partner judgment at acceptance."
  role_evolution: "The release says practitioners may need a blend of auditing expertise, AI knowledge, data skills, professional skepticism and specialist support (AICPA-PA-2026)."
  evidence_grade: D
  sources:
    - { ref: AICPA-PA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: "AICPA & CIMA", type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: "2026-10-13", access: full, locator: "section 'Considering an organization's use of AI'" }
    - { ref: JOFA-AIPA-2026, title: "AI and the audit: AICPA publishes practice aid to assist auditors", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/", date: "2026-10-13", access: full, locator: "paragraphs 1-4" }
  last_reviewed: 2026-10-16
  notes: "Idea. The practice aid is nonauthoritative guidance and its full text needs an AICPA login. The landscape file reports that the practice aid names acceptance and continuance explicitly (management integrity, skills, team competence); the release I opened says only that auditors should address client AI reliance 'at the start of an engagement' and assess team capability, so the explicit acceptance wording is not confirmed here. Ladder and pattern are nominal."

- id: assurance-acceptance-independence-05
  title: "Idea: state AI use and obtain consent in engagement letters and acceptance conversations"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [document-production, client-interaction]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Clients differ on whether they accept AI use in their audits, and client data entered into some AI tools can be used to train models."
  solution: "Add AI-use disclosure and, where client data is involved, specific consent to the engagement letter and the acceptance dialogue. This is a client communication and terms change, not AI doing the work."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: JOFA-ETHAI-2026
  prerequisites:
    - "Approved AI tools with clear data-handling terms; a firm position on which AI uses are disclosed (JOFA-ETHAI-2026, confidentiality section)."
  risks_and_guardrails:
    - "AICPA ethics staff: before pasting client data into an AI system, ask whether consent is required and whether the client has specifically consented (JOFA-ETHAI-2026)."
  human_checkpoints:
    - "Partner explains AI use to the client; legal or ethics review of letter wording."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: JOFA-ETHAI-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division staff author)", type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "sections on confidentiality and closing paragraphs" }
    - { ref: IRISHTIMES-GT-2026, title: "Grant Thornton's UK boss defends private equity ownership", publisher: "The Irish Times (Financial Times syndication)", type: press, url: "https://www.irishtimes.com/business/2026/09/22/grant-thorntons-uk-boss-defends-private-equity-ownership/", date: "2026-09-22", access: full, locator: "final paragraphs on AI and graduate hiring" }
    - { ref: LEARNFORMULA-APS-2026, title: "The Governance Gap: How PEEC is Drafting the Ethical Playbook for Alternative Practice Structures and AI", publisher: "LearnFormula (CPE provider)", type: community, url: "https://cfe-cpe-us.learnformula.com/latest-intelligence/the-governance-gap-how-peec-is-drafting-the-ethical-playbook-for-alternative-practice-structures-and-ai", date: "2026-08-11", access: full, locator: "section 'Action Plan'" }
  last_reviewed: 2026-10-16
  notes: "Idea. Grant Thornton UK's chief executive said some clients did not want AI used in their audit and consulting projects (IRISHTIMES-GT-2026). The LearnFormula piece recommends revising engagement letters; it is a low-authority secondary commentary and says PEEC is 'zeroing in' on confidentiality, which I could not confirm in the PEEC reporting. The landscape file reports that the AICPA practice aid says AU-C 210 does not require naming AI tools in the engagement letter; I did not open that text."

- id: assurance-acceptance-independence-06
  title: "Independence and acceptance due diligence before taking PE or other external investment (APS structuring)"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "PE investment, mostly through APS structures, can create independence threats through investor holdings, network-firm status and shared services, and regulators want to be engaged early."
  solution: "Firms run a pre-transaction review with legal counsel and, where relevant, regulators: map which entities are network firms and which individuals are covered members, design the administrative services agreement, set quality-management controls and investor education, then monitor. PE is also the route by which firms say they fund AI investment (see notes). This is a control process, not AI doing the work."
  outcomes:
    - lever: risk
      description: "Context measure of how much structural change is occurring, not an outcome of the review step."
      figure: "385 transactions in 2025, 139 involving audit firms"
      measures: "Transactions (direct investments and roll-overs) involving accountancy and audit firms identified across Europe in 2025; 139 of them involved audit firms (36%)."
      provenance: independent
      source_ref: AE-PE-2026
  prerequisites:
    - "Counsel experienced in the Code and state or national law; stakeholder engagement with regulators and standard-setters; a draft administrative services agreement (JOFA-NILSEN-2025)."
  risks_and_guardrails:
    - "AICPA staff: where the Code does not address a structure, such as PE with significant influence but not control, apply the conceptual framework and document safeguards (JOFA-NILSEN-2025)."
    - "PEEC exposure draft (19 Dec 2025) would distinguish significant influence from control and widen the network firm definition; a second exposure draft was under discussion in Aug 2026 (JOFA-ED-2025; JOFA-PEEC-2026)."
    - "Accountancy Europe notes the FRC and the Dutch AFM called for engagement before PE transactions (AE-BEYONDPE-2025)."
  human_checkpoints:
    - "Firm governance vote and regulator engagement before closing; independence consultation on structure."
  role_evolution: "Ethics and independence leaders add transaction advisory to their role; Accountancy Europe says firms need expert legal, governance and transaction support (AE-BEYONDPE-2025)."
  evidence_grade: B
  sources:
    - { ref: JOFA-NILSEN-2025, title: "Navigating outside investors: Safeguarding ethics and independence in evolving practice structures", publisher: "Journal of Accountancy (AICPA staff author)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/oct/navigating-outside-investors-safeguarding-ethics-and-independence-in-evolving-practice-structures/", date: "2025-10-24", access: full, locator: "paragraphs on due diligence, administrative services agreement and multipronged approach" }
    - { ref: JOFA-ED-2025, title: "AICPA proposes changes to independence guidelines related to private equity", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2025/dec/aicpa-proposes-changes-to-independence-rules-related-to-private-equity/", date: "2025-12-19", access: full, locator: "paragraphs 1-4" }
    - { ref: AE-PE-2026, title: "Private Equity in European Accountancy and Audit Firms: an update on market activity, January 2025 - April 2026", publisher: "Accountancy Europe", type: professional-body, url: "https://accountancyeurope.eu/wp-content/uploads/2026/05/260629-Private-equity-investment-in-accountancy-and-audit-sector-in-EU-from-January-2025-to-April-2026.pdf", date: "2026-07", access: full, locator: "market overview and Grant Thornton case" }
    - { ref: AE-BEYONDPE-2025, title: "Beyond private equity: third party ownership in the accountancy and audit sector (summary)", publisher: "Accountancy Europe", type: professional-body, url: "https://accountancyeurope.eu/wp-content/uploads/2025/11/251121-Beyond-Private-Equity-Third-Party-ownership-summary.pdf", date: "2025-11", access: full, locator: "risks section" }
  last_reviewed: 2026-10-16
  notes: "Grade B: Grant Thornton UK's Cinven investment closed in early 2025 after regulatory approval, with the audit practice kept in its LLP and advisory and tax moved to a new entity (AE-PE-2026, 'Grant Thornton' section); the process is real but no measured outcome exists. Botic said (Dec 2025) PE capital can finance investment in technology including AI (AT-PCAOBPE-2025). The Accountancy Europe date is the cover's June/July 2026 label. Ladder is nominal."

- id: assurance-acceptance-independence-07
  title: "Screen prospective audit clients against investor holdings and consult the regulator on grey areas"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "When a firm's owner or its funds hold stakes in companies, taking those or related companies as audit clients can fall in independence grey areas."
  solution: "At acceptance the firm checks whether the prospective client is linked to the investor's holdings, declines where independence is doubtful, and consults the regulator where the answer is unclear. This is a control step, not AI doing the work."
  outcomes:
    - lever: risk
      description: "One reported case: a prospective client was taken to the FRC, the regulator agreed it was a grey area, and the firm decided not to proceed."
      figure: "1 case"
      measures: "Number of reported instances in the source in which the firm consulted the FRC about taking on a client (one, per the chief executive)."
      provenance: self-reported
      source_ref: IRISHTIMES-GT-2026
  prerequisites:
    - "A current map of the investor's holdings and a route to consult the regulator (inferred; tooling not described in the source)."
  risks_and_guardrails:
    - "The chief executive acknowledged complex ownership structures create uncertainty over how far independence restrictions extend (IRISHTIMES-GT-2026)."
    - "PEEC's discussion memorandum: a PE investor and its portfolio companies would generally not be network firms, so portfolio companies could provide non-attest services to attest clients, with exceptions (JOFA-PE-2025)."
    - "PCAOB inspections director said inspectors will look at quality control at firms that took PE or APS changes (AT-PCAOBPE-2025)."
  human_checkpoints:
    - "Partner and independence-function decision; regulator consultation."
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: IRISHTIMES-GT-2026, title: "Grant Thornton's UK boss defends private equity ownership", publisher: "The Irish Times (Financial Times syndication)", type: press, url: "https://www.irishtimes.com/business/2026/09/22/grant-thorntons-uk-boss-defends-private-equity-ownership/", date: "2026-09-22", access: full, locator: "paragraphs 2-3 and the paragraph on consulting the FRC" }
    - { ref: JOFA-PE-2025, title: "AICPA seeks feedback on independence rules related to private equity", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2025/mar/independence-rules-private-equity/", date: "2025-03-10", access: full, locator: "final two paragraphs" }
    - { ref: AT-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe", date: "2025-12-09", access: full, locator: "section 'PE warning'" }
    - { ref: BBT-FRC-2025, title: "UK Watchdog Says Private Equity Poised to Help Audit Quality", publisher: "Bloomberg Tax", type: press, url: "https://news.bloombergtax.com/financial-accounting/uk-watchdog-says-private-equity-poised-to-help-audit-quality", date: "2025-02-13", access: full, locator: "opening paragraphs (rest paywalled)" }
  last_reviewed: 2026-10-16
  notes: "Grade B: a named firm states the practice, but it is a policy statement from an interview and no tooling or measurement is described. The FRC statement is a Feb 2025 foundation item, just outside the 18-month window. The interview is a Financial Times piece syndicated by The Irish Times; I did not open the Financial Times original."

- id: assurance-acceptance-independence-08
  title: "Idea: screen attest clients for investment in the firm or its investors at acceptance and continuance"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "If attest clients can invest in firms, or in the funds that own firms, a new financial relationship can arise between auditor and audited."
  solution: "PEEC discussed adding an interpretation that prohibits attest client investment in firms, which would add a recurring client-to-owner linkage check. A proposal under discussion, not a rule."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: JOFA-PEEC-2026
  prerequisites:
    - "Ownership data on the firm, its investors and funds, and on clients."
  risks_and_guardrails:
    - "Not yet adopted. PEEC agreed to continue at an interim October 2026 meeting on a second exposure draft (JOFA-PEEC-2026). Ho reported the committee indicated re-exposure in October or November and adoption the following May (AT-PEEC-2026)."
  human_checkpoints:
    - "Independence function review of any hits."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: JOFA-PEEC-2026, title: "PEEC to continue discussions on alternative practice structures", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/", date: "2026-08-10", access: full, locator: "paragraph 1" }
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: "2026-08-31", access: full, locator: "paragraph on re-exposure and adoption" }
  last_reviewed: 2026-10-16
  notes: "Idea. The tooling to monitor this is not described anywhere; whether AI could help is not discussed. Date conflict: Accounting Today says comments are due 'by the end of this month' while the JofA says a second exposure draft was still to be issued after October (see Module notes, data conflicts)."

- id: assurance-acceptance-independence-09
  title: "Idea: independence and objectivity review of commercial arrangements with technology and AI vendors"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Firms contract with software vendors, including SOC 2 platforms and AI tools, that may also serve the firm's attest clients, supply referrals, or set terms that shift judgment or evidence access to the vendor. No rule says where such a relationship sits."
  solution: "Before adopting a vendor, document who owns it, whether it also serves audit clients, what is paid and whether payments depend on volume or referrals, and whether it can use client data to train models, then test the answers against the Code's conceptual framework. This is a new vendor-risk control, not AI doing the work."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: JOFA-SOCETH-2026
  prerequisites:
    - "Contract review; an inventory of vendors touching client work (ACCWEEKLY-INDEP-2026)."
  risks_and_guardrails:
    - "AICPA staff on SOC 2 tool providers: terms that shift control, judgment, financial dependency, promotion or evidence access can create threats; consider ending the arrangement or the engagement if safeguards fail; the article says it may be relevant to other audit and attest services (JOFA-SOCETH-2026)."
    - "IESBA's technology revisions strengthened independence provisions on self-review, assuming management responsibility and commercial dependencies (ICAS-IESBASNAP-2026)."
  human_checkpoints:
    - "Independence partner conclusion, documented; written disclosure to the client where the firm finds something uncomfortable (ACCWEEKLY-INDEP-2026)."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: JOFA-SOCETH-2026, title: "SOC engagements: Ethics risks with tool providers", publisher: "Journal of Accountancy (AICPA ethics staff)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/", date: "2026-04-06", access: full, locator: "opening paragraph; sections 'Use the conceptual framework' and 'Practical takeaways'" }
    - { ref: ACCWEEKLY-INDEP-2026, title: "AI Audit Tools and the Independence Gap Nobody Fixed", publisher: "Accounting Weekly (CIBA author)", type: professional-body, url: "https://www.accountingweekly.com/trending-news/ai-audit-tools-and-the-independence-gap-nobody-fixed", date: "2026-09-01", access: full, locator: "sections 'The question nobody has answered' and 'What to do about it'" }
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: "2026-08-31", access: full, locator: "paragraphs 1-3 (Ho on licensing AI audit tools)" }
    - { ref: ICAS-IESBASNAP-2026, title: "IESBA issues snapshot on the ethical implications of using technology, including AI", publisher: "ICAS", type: professional-body, url: "https://icas.com/news-insights-events/news/ethics/iesba-issues-snapshot-on-the-ethical-implications-of-using-technology-including-ai/", date: "2026-07-14", access: full, locator: "section on technology-related revisions, independence paragraph" }
  last_reviewed: 2026-10-16
  notes: "Idea. The AICPA article concerns SOC 2 tool providers and does not use the word AI; the AI extension is the commentators' (CIBA, Ho). The CIBA piece is an opinion piece by a professional-body staff member. Ho raised the point about when licensing an AI audit tool becomes a conflict and that licensing may favour firms that build AI in-house (AT-PEEC-2026)."

- id: assurance-acceptance-independence-10
  title: "Idea: clear firm alliances with AI developers before accepting those developers, or their customers, as audit clients"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Firm-wide commercial alliances with frontier AI developers, including co-developed client products, may conflict with auditing those developers or companies that use them in service delivery."
  solution: "Extend business-relationship and acceptance checks to cover strategic AI alliances and client-facing joint offerings, run at network level before signing and again at each acceptance or continuance. A control step created by AI alliances, not AI doing the work."
  outcomes:
    - lever: risk
      description: "Context measure of alliance scale, not an outcome of any clearance step."
      figure: "470,000 people (Deloitte, Oct 2025); more than 276,000 employees (KPMG, May 2026)"
      measures: "Number of each firm's people who will have access to Claude, per the announcements ('available to 470,000 people'; 'every one of KPMG's 276,000+ employees will gain access')."
      provenance: vendor-published
      source_ref: ANTHROPIC-KPMG-2026
  prerequisites:
    - "Network-level register of alliances and co-developed offerings; a defined independence policy for them (not described by any firm in the sources)."
  risks_and_guardrails:
    - "Hohl (Dec 2025): independence rules are fairly clear on direct business relationships with audit clients, but it becomes complicated when a firm partners with a non-audit client that uses an audit client in its service delivery; he said understanding how pervasive that is and how it affects firms' monitoring is a priority (NYCPA-HOHL-2025)."
    - "Press reports, citing the Financial Times and not confirmed at source, say Deloitte, PwC and KPMG alliances leave EY as the likely auditor of Anthropic, which the firms and Anthropic have not confirmed (CRYPTOBRIEFING-ANTHROPICEY-2026; FOURTHWEB-ANTHROPICEY-2026; BIG4NEWS-2026)."
  human_checkpoints:
    - "Global independence leadership sign-off; audit committee dialogue."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: NYCPA-HOHL-2025, title: "SEC's Chief Accountant Discusses Audit Inspections, Conflict-of-Interest Rule Changes", publisher: "New York State Society of CPAs", type: press, url: "https://nysscpa.org/news/1045145-secs-chief-accountant-discusses-audit-inspections-conflict-of-interest-rule-changes-2025-12-12", date: "2025-12-12", access: full, locator: "paragraphs on independence rules and AI partnerships" }
    - { ref: ANTHROPIC-DELOITTE-2025, title: "Deloitte will make Claude available to 470,000 people across its global network", publisher: "Anthropic", type: vendor, url: "https://www.anthropic.com/news/deloitte-anthropic-partnership", date: "2025-10-06", access: full, locator: "opening paragraphs" }
    - { ref: ANTHROPIC-KPMG-2026, title: "KPMG integrates Claude across its core business and workforce of more than 276,000 in strategic alliance", publisher: "Anthropic", type: vendor, url: "https://www.anthropic.com/news/anthropic-kpmg", date: "2026-05-19", access: full, locator: "opening paragraphs; section on KPMG Digital Gateway" }
    - { ref: CRYPTOBRIEFING-ANTHROPICEY-2026, title: "Anthropic likely to select EY as auditor amid Big Four conflicts", publisher: "Crypto Briefing", type: press, url: "https://cryptobriefing.com/anthropic-ey-auditor-big-four-conflicts/", date: "2026-08-12", access: full, locator: "sections 'The conflict web' and 'EY's accidental advantage' (read via text mirror; direct fetch returned 403)" }
    - { ref: BIG4NEWS-2026, title: "The Big Four AI Arms Race, Evergrande, Governance and Culture", publisher: "Big4News (newsletter)", type: community, url: "https://www.big4news.com/p/big-four-news-20-may-2026", date: "2026-05-20", access: full, locator: "section 'Anthropic & the Big Four' and the later update on EY" }
  last_reviewed: 2026-10-16
  notes: "Idea. The alliances are named, dated, firm-announced facts (primary Anthropic releases). That an independence consequence has occurred rests on secondary reports of a Financial Times article that I could not open, from low-authority outlets, and Anthropic has not named an auditor in anything I read. Anthropic's Deloitte release carries the standard note that Deloitte member firms are legally separate; whether that matters for where independence is assessed is my inference, not a source's statement. Hohl's Dec 2025 remarks predate the PwC and KPMG announcements."

- id: assurance-acceptance-independence-11
  title: "Pre-approval screen for AI-related non-audit services and business relationships with attest clients"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Firms and networks now sell or build AI tools and solutions for clients, which can create self-review or management-responsibility threats if the client is an attest client."
  solution: "Route every proposed service or business relationship through a pre-approval workflow backed by an entity database before work starts, with AI build, host or licence engagements flagged for independence review. The workflow described in the sources is not AI-specific; applying it to AI services is the change."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: self-reported
      source_ref: DELOITTE-IE-TR-2026
  prerequisites:
    - "A searchable entity database, a service-request workflow and a financial-relationship monitoring system (DELOITTE-IE-TR-2026, independence section)."
  risks_and_guardrails:
    - "AICPA ethics staff: building or hosting an AI system for an attest client can raise independence concerns, and existing non-attest services and information-systems rules still apply (JOFA-ETHAI-2026)."
    - "IESBA's technology revisions, effective in ICAS's Code from 1 Jan 2025, cover self-review, assuming management responsibility and commercial dependencies when technology is used to deliver services to audit clients (ICAS-IESBASNAP-2026)."
  human_checkpoints:
    - "Independence function approves or declines the request."
  role_evolution: "Independence staff need technical understanding of AI services to classify them; not stated directly in a source."
  evidence_grade: B
  sources:
    - { ref: DELOITTE-IE-TR-2026, title: "2026 Transparency Report, Deloitte Ireland", publisher: "Deloitte Ireland", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/ie/en/docs/about/2026/deloitte-transparency-report-2026.pdf", date: "2026-09", access: full, locator: "Independence section: DESC, SRM and GIMS descriptions" }
    - { ref: DELOITTE-LU-TR-2026, title: "2026 Transparency Report, Deloitte Audit (Luxembourg)", publisher: "Deloitte Luxembourg", type: firm, url: "https://www.deloitte.com/content/dam/assets-zone2/lu/en/docs/about/2026/lu_transparency_report-2026.pdf", date: "2026-09", access: full, locator: "Independence section: DESC, SRM and GIMS descriptions" }
    - { ref: JOFA-ETHAI-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division staff author)", type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "section 'AI services can raise independence concerns for attest clients'" }
    - { ref: ICAS-IESBASNAP-2026, title: "IESBA issues snapshot on the ethical implications of using technology, including AI", publisher: "ICAS", type: professional-body, url: "https://icas.com/news-insights-events/news/ethics/iesba-issues-snapshot-on-the-ethical-implications-of-using-technology-including-ai/", date: "2026-07-14", access: full, locator: "independence bullet under technology-related revisions" }
  last_reviewed: 2026-10-16
  notes: "Grade capped at B for scope: the named deployment is Deloitte's non-AI independence tooling (DESC and SRM are described as a global entity database and a pre-approval workflow integrated with it); no source shows these applied to AI services. The transparency reports do not describe AI inside the tools. The KPMG release says KPMG and Anthropic will build Claude-powered products for PE portfolio companies (ANTHROPIC-KPMG-2026), showing firms are moving into client AI offerings, but not whether any buyer is an audit client."

- id: assurance-acceptance-independence-12
  title: "AI-native attest firm built on an alternative practice structure with venture-funded technology entity"
  archetype: assurance
  module: acceptance-independence
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "A venture-backed audit start-up must keep the attest entity owned by licensed CPAs while the technology and advisory side raises outside capital, and must prove its independence to regulators."
  solution: "Oath Verified, a newly licensed audit firm, uses an APS because its platform company is venture-backed; outside funding goes only to the non-audit side and CPAs own the audit operations. It says it is building a methodology for an AI-native audit, with continuous verification connected to client data sources, starting with private companies."
  outcomes:
    - lever: growth
      description: "Funding raised, a growth measure; no audit-quality or efficiency result published."
      figure: "about $10 million"
      measures: "Total funding Oath Verified has raised to date, per Accounting Today (a $6.6 million seed round in December 2025 is reported as part of it)."
      provenance: self-reported
      source_ref: AT-PEEC-2026
  prerequisites:
    - "State-regulator licence for the attest entity; a compliant APS (Ho: state regulators require an APS for a venture-backed company to create an attest entity) (AT-PEEC-2026)."
  risks_and_guardrails:
    - "Ho said ambiguity remains about when licensing AI audit tools becomes a conflict and that technology businesses 'closely aligned' with audit firms could fall within APS scope (AT-PEEC-2026)."
    - "Client data is kept in separate per-client environments that do not train the model, per Ho (AT-PEEC-2026)."
  human_checkpoints:
    - "The opinion and final professional judgment stay with a human (FINSTORY-OATH-2026)."
  role_evolution: "Oath hires 'accountant engineers' (AT-PEEC-2026; FINSTORY-OATH-2026). The Finance Story notes that much of the work that would be automated is what junior auditors do in early years."
  evidence_grade: B
  sources:
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: "2026-08-31", access: full, locator: "paragraphs on Oath's structure and funding; sections on maintaining independence" }
    - { ref: FINSTORY-OATH-2026, title: "Ex-PCAOB regulator QUITS...joins AI Audit startup targeting 80% Automation", publisher: "The Finance Story", type: press, url: "https://thefinancestory.com/ex-pcaob-regulator-joins-ai-native-audit-firm-oath", date: "2026-06-03", access: full, locator: "paragraphs on what Oath is building and VC funding" }
  last_reviewed: 2026-10-16
  notes: "Grade B: a named, licensed firm with disclosed structure but no published measurements. 'Piloting' because no source shows it delivering audits at scale. The Finance Story, relaying the Wall Street Journal (not opened), says Oath aims to automate 80% of audit work by 2030; that target is kept here in notes because it is a secondary relay of a founder target. Landscape file lists Modus ($85M, invests in audit-first firms) and Repodo (new AI-built authorised audit firm in Denmark); I could not open their primary pages in this run."

- id: assurance-acceptance-independence-13
  title: "Idea: govern technology and AI platforms supplied across attest and non-attest entities under the administrative services agreement"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "In an APS the non-attest entity, often PE-backed, can supply the attest firm with staff, technology tools and services under an agreement, so a shared AI platform could create dependence and blur network boundaries."
  solution: "Treat AI and data platforms provided across the attest and non-attest entities as part of the independence assessment: who builds, owns and controls them, how they are paid for, and whether access and judgment stay with the attest firm. A control design step, not AI doing the task."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: APESB-PE-2025
  prerequisites:
    - "Written administrative services agreement that addresses current and future resource needs (JOFA-NILSEN-2025)."
  risks_and_guardrails:
    - "APESB paper, quoting the IESBA staff alert, says the administrative services agreement may cover leasing professional staff, technology tools and administrative services (APESB-PE-2025)."
    - "Accountancy Europe says questions remain about whether such agreements always protect independence (AE-BEYONDPE-2025)."
    - "PEEC's proposed network firm definition would add entities that control, or are controlled by, a network firm and cooperate to enhance its capabilities (JOFA-ED-2025)."
  human_checkpoints:
    - "Attest-firm leadership approval of any shared-technology arrangement; independence consultation."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: APESB-PE-2025, title: "Update on Private Equity Investment in Firms (agenda item 11)", publisher: "APESB (Australia)", type: standard-setter, url: "https://apesb.org.au/wp-content/uploads/2025/06/Agenda_Item_11_Update_on_Private_Equity_Investment_In_Firms.pdf", date: "2025-06", access: full, locator: "section describing the APS structure and administrative services agreement" }
    - { ref: AE-BEYONDPE-2025, title: "Beyond private equity: third party ownership in the accountancy and audit sector (summary)", publisher: "Accountancy Europe", type: professional-body, url: "https://accountancyeurope.eu/wp-content/uploads/2025/11/251121-Beyond-Private-Equity-Third-Party-ownership-summary.pdf", date: "2025-11", access: full, locator: "governance mechanisms section" }
    - { ref: JOFA-ED-2025, title: "AICPA proposes changes to independence guidelines related to private equity", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2025/dec/aicpa-proposes-changes-to-independence-rules-related-to-private-equity/", date: "2025-12-19", access: full, locator: "paragraph on network firm definition" }
    - { ref: AT-PEEC-2026, title: "AICPA weighs PE and tech impact on audit independence", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: "2026-08-31", access: full, locator: "paragraphs on technology companies considered closely aligned" }
  last_reviewed: 2026-10-16
  notes: "Idea. The AI link is Ho's argument that technology companies closely aligned with audit firms could be inside APS scope (AT-PEEC-2026). The landscape file reports Grant Thornton's Gtap platform operating under an APS (GT-GTAP-2026); I did not open that page, so it is not used as evidence here. APESB paper date is the June 2025 agenda; the IESBA staff alert's own date was not confirmed."

- id: assurance-acceptance-independence-14
  title: "Idea: safeguard audit partners' control of client selection and continuance in PE-backed firms"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [expert-judgment, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "New governance layers above the audit entity can dilute audit partners' influence over which clients to accept or keep, and PE-owned firms may drop public-company audits as too costly, reducing choice."
  solution: "Write acceptance and continuance authority for audit work into the firm's governance so investor or holding-company profit targets cannot decide client selection, and monitor portfolio-level exits from public-interest-entity audit. A governance safeguard, not AI doing the task."
  outcomes:
    - lever: risk
      description: "Context measure of PE reach into public-interest-entity audit, not an outcome of any safeguard."
      figure: "46 firms owned directly; 52 further firms rolled up (as of 30 Jun 2026)"
      measures: "Per IFAC: direct PE investment has resulted in equity ownership in 46 firms that provide audit services to public-interest entities, and 52 PIE audit firms were acquired or rolled up into those 46 surviving firms."
      provenance: independent
      source_ref: IFAC-AQ-2026
  prerequisites:
    - "Governance documents that reserve client acceptance authority to the audit entity."
  risks_and_guardrails:
    - "IFAC: new governance structures can dilute audit partners' influence and their control or oversight of client selection and engagement performance (IFAC-AQ-2026, challenges section)."
    - "Hohl said some PE-backed small firms decided to leave the public-company market because it is too expensive, and that auditor choice is a priority (NYCPA-HOHL-2025; TR-HOHL-2026)."
    - "Botic said PE roll-ups may reduce the number of firms auditing public companies (AT-PCAOBPE-2025)."
  human_checkpoints:
    - "Audit-entity leadership decides acceptance; independent oversight of the administrative services agreement."
  role_evolution: "Audit partners' standing in firm governance is the stated concern (IFAC-AQ-2026)."
  evidence_grade: D
  sources:
    - { ref: IFAC-AQ-2026, title: "Audit Quality: Considerations and Implications", publisher: "IFAC", type: professional-body, url: "https://www.ifac.org/private-equity-investment-accountancy/audit-quality-considerations-and-implications", date: "2026-06", access: full, locator: "intro data paragraph and 'Governance' challenge" }
    - { ref: NYCPA-HOHL-2025, title: "SEC's Chief Accountant Discusses Audit Inspections, Conflict-of-Interest Rule Changes", publisher: "New York State Society of CPAs", type: press, url: "https://nysscpa.org/news/1045145-secs-chief-accountant-discusses-audit-inspections-conflict-of-interest-rule-changes-2025-12-12", date: "2025-12-12", access: full, locator: "final three paragraphs of the Hohl interview summary" }
    - { ref: TR-HOHL-2026, title: "SEC Chief Accountant Hohl Dispels Rumors of Weakening Auditor Independence Rules", publisher: "Thomson Reuters Checkpoint News", type: press, url: "https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/", date: "2026-06-05", access: full, locator: "paragraph on auditor choice for multinationals" }
    - { ref: AT-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe", date: "2025-12-09", access: full, locator: "section 'Private equity issues'" }
  last_reviewed: 2026-10-16
  notes: "Idea. IFAC page is undated; 2026-06 is its stated data date and the research was released 2 Mar 2026 (IFAC-PE-2026). The statistic counts public information and the page says the 46 firms and the 'nearly 100' firms with PIE audit are under 10% of PE-driven activity."

- id: assurance-acceptance-independence-15
  title: "Idea: independence criteria for firms accepting assurance over AI developers' systems"
  archetype: assurance
  module: acceptance-independence
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "As firms launch AI assurance services, who may qualify as an independent external reviewer of an AI developer is unsettled, and firms already have partnerships with the largest AI providers."
  solution: "Define acceptance rules for AI-assurance clients, such as no paid consulting to the same developer, board-level appointment, rotation, and guaranteed access. These are proposals in commentary, not adopted rules."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "n/a"
      provenance: independent
      source_ref: GOPALAN-SUBSTACK-2026
  prerequisites:
    - "A standard for the AI assurance engagement itself (routed to other-assurance)."
  risks_and_guardrails:
    - "The Financial Times, as relayed by Consultancy.uk, reported UK government research that AI assurance is often provided by AI developers themselves, raising independence questions; and the Big Four have many partnerships with major AI tool providers (CONSULTANCY-BIG4AI-2025)."
    - "A commentator proposed separating auditing from selling, board-led appointment, a standards body with inspection power, defined access, rotation and executive certification (GOPALAN-SUBSTACK-2026)."
  human_checkpoints:
    - "Not defined."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: GOPALAN-SUBSTACK-2026, title: "AI Is About to Repeat Enron's Audit Problem", publisher: "Sriram Gopalan (Substack)", type: community, url: "https://sgopalanbtg.substack.com/p/ai-is-about-to-repeat-enrons-audit", date: "2026-10-07", access: full, locator: "sections 'The Fight Has Already Started' and 'What a SOX for AI Looks Like'" }
    - { ref: CONSULTANCY-BIG4AI-2025, title: "Big Four weighing up new AI audit offerings", publisher: "Consultancy.uk", type: press, url: "https://www.consultancy.uk/news/40424/big-four-weighing-up-new-ai-audit-offerings", date: "2025-06-10", access: full, locator: "paragraphs on PwC UK and independence" }
  last_reviewed: 2026-10-16
  notes: "Idea, and the source is an opinion piece by a technology commentator, not a practitioner. It relays a Washington Post report (not opened) that an AI adviser wants professional auditors for AI labs, and says EY confirmed working with a start-up called 8090; neither is verified here. Primary home for this topic is the other-assurance module; kept here only for the acceptance and independence angle."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Prospective client intake and identification** (transaction-processing, client-interaction). Pain: unstructured email and incomplete submissions (ZYGOS-AISENSE-2026, small sample).
- **KYC/AML due diligence** (review-assurance, transaction-processing): identity, beneficial ownership, sanctions and PEP screening, ongoing monitoring (ZYGOS-AISENSE-2026; GT-FENERGO-2026).
- **Client risk profiling and acceptance decision** (expert-judgment): integrity, capability, time and resources, portfolio risk appetite. Deloitte Ireland says its audit portfolio risk appetite statement is a basis on which acceptance and continuance decisions are debated and challenged (DELOITTE-IE-TR-2026, 'A focus on quality').
- **Independence and conflicts checks** (review-assurance, transaction-processing): client, engagement and business relationships, using an entity search database and a service-request pre-approval workflow; firm and personal financial relationships, using a monitoring system; employment relationships; confirmations; consultations; long-association rules for partners (DELOITTE-IE-TR-2026; DELOITTE-LU-TR-2026). None of the sources describes AI inside these tools.
- **Engagement letter and terms** (document-production). The AI-use disclosure question is new (entry 05).
- **Continuance reassessment** (monitor, expert-judgment). No source describes AI here.
- **Firm-structure independence assessment** for APS and PE deals: network firm determination, covered members, additional threats, conceptual framework (JOFA-PE-2025; JOFA-NILSEN-2025).
- **Consultation on grey areas**, including with the regulator (IRISHTIMES-GT-2026).

### Common pain points

- Complex ownership structures leave grey areas on how far independence restrictions extend; a firm leader said so openly (IRISHTIMES-GT-2026).
- No rule or ruling addresses a vendor that serves both auditor and client, or when licensing an AI audit tool becomes a conflict (ACCWEEKLY-INDEP-2026; AT-PEEC-2026).
- The AICPA's APS comment record had no technology-company voice: 81 letters, dozens from state boards of accountancy, none from technology companies, per Ho (AT-PEEC-2026).
- SEC independence FAQs had not been refreshed for about six years, and companies and firms need help on complex independence questions (TR-HOHL-2026).
- Auditor choice: Hohl relayed a company audit committee member's complaint that independence restrictions leave no choice beyond the largest firms for multinationals (TR-HOHL-2026).

### Metrics and benchmarks (with sources)

- PE reach (independent counts). IFAC: more than 1,000 accountancy firms with PE investment over ten years, fewer than 200 direct investments facilitating nearly 900 later transactions (IFAC-PE-2026). Accountancy Europe: 385 transactions in 2025 (139 with audit firms), 131 in Jan-Apr 2026 (62 with audit firms), 15% involving firms with public-interest-entity audits, and the Dutch AFM reporting about 30% of Dutch audit firms with PE investment (AE-PE-2026).
- PCAOB's Gunia: more than 90 significant PE-related transactions and mergers since 2020, more than half in 2025 (AT-PCAOBPE-2025). A JofA academic update cites CPA Trendlines: more than 53 significant PE-related transactions from 2020 to mid-2025, 24 in 2024, with PE stakes in 10 of the 30 largest US firms (JOFA-FACULTY-2025). The counts differ, likely by definition and period (data conflict, below).
- Ethics survey: 61% of 1,178 respondents in 135 countries named AI use among their top ethical challenges (32% in 2024), and 72% agreed AI tools improve the quality and efficiency of their work (ACCA-ETHICS-2026). Not audit-specific.
- Small-sample intake baseline: 93% and 87% of 15 respondents (ZYGOS-AISENSE-2026).
- **No error rate, false-positive rate, override rate, parallel-run result, inspection finding or independent measure exists in any source for AI in acceptance, KYC or independence monitoring.**

### Guardrails and regulatory points

- **AICPA Code and PEEC.** APS interpretation, network firm and conceptual framework apply; PEEC issued an exposure draft on 19 Dec 2025 (significant influence versus control; wider network firm definition; effective one year after adoption); comment closed 30 Apr 2026; PEEC discussed a second exposure draft in Aug 2026 and agreed to continue at an interim October meeting (JOFA-ED-2025; JOFA-PEEC-2026). Ho reported the committee indicated re-exposure in October or November and adoption the following May (AT-PEEC-2026).
- **AICPA staff on AI.** AI-related non-attest services such as developing or hosting an AI system for an attest client can raise independence concerns; existing rules apply (JOFA-ETHAI-2026). The staff article 'AI Through an Ethics Lens' exists in the members' ethics library (AICPA-PA-2026; not opened).
- **IESBA.** Technology-related Code revisions (effective in the ICAS Code from 1 Jan 2025) cover self-review, assuming management responsibility and commercial dependencies; IESBA decided not to add further Code changes for now and plans two non-authoritative guides (overarching technology, Q3 2026; AI-specific, Q4 2026) (ICAS-IESBASNAP-2026). In June 2026 it approved terms of reference for a PE and other external investment workstream, to coordinate with the IAASB, with an update due in September 2026 (IESBA-HIGHLIGHTS-2026; IESBA-PETOR-2026). A draft staff publication on emerging technologies lists dependence on third-party providers among the characteristics that stress the Code (IESBA-TECH4A-2026, a May 2026 agenda paper and draft).
- **SEC.** Independence FAQ refresh, public sharing of staff consultation answers, and a review with the PCAOB of interim independence standards; "listening mode" on PE and AI; no rulemaking proposal seen (TR-HOHL-2026; NYCPA-HOHL-2026).
- **PCAOB.** Inspectors said they will look at quality control at firms that have taken PE or APS changes and will keep focusing on AI (AT-PCAOBPE-2025).
- **UK and EU.** FRC Feb 2025 statement that outside investment can help audit quality if properly structured (BBT-FRC-2025). EU rules require auditor-majority control of audit firms (AE-BEYONDPE-2025).

### Frontier signals (dated, sourced)

- 2025-12-08/09: PCAOB acting chair and inspections director link PE and AI as the two areas to watch in 2026 inspections (AT-PCAOBPE-2025).
- 2026-03-02: IFAC publishes global PE research (IFAC-PE-2026). 2026-03-27: IESBA says it will gather information to decide whether to pursue a standard-setting project on APS (JOFA-IESBAAPS-2026). 2026-06-08/11: IESBA approves PE terms of reference (IESBA-HIGHLIGHTS-2026).
- 2026-05-08: Deloitte/KU symposium puts PE, ownership and independence on a panel of the same day as an AI panel (KU-SYMPOSIUM-2026). Day 2 included a Grant Thornton talk titled 'Private Equity in Accounting; Lots of Questions' and a panel on audit firm ownership, independence and audit quality moderated by the CAQ; day 3 included a research paper on studying PE investments in accounting firms (KU-SYMPOSIUM-2026; agenda only, no slides or recordings found).
- 2025-10-06 and 2026-05-19: Deloitte and KPMG announce firm-wide Claude alliances (ANTHROPIC-DELOITTE-2025; ANTHROPIC-KPMG-2026). 2026-08-12 to 14: press reports, citing the Financial Times, say these leave EY as the likely auditor of Anthropic (unconfirmed) (CRYPTOBRIEFING-ANTHROPICEY-2026; FOURTHWEB-ANTHROPICEY-2026).
- 2026-08-10: PEEC to continue APS work toward a second exposure draft (JOFA-PEEC-2026). 2026-08-31: Ho presses technology companies to comment (AT-PEEC-2026).
- 2026-09-01: practitioner commentary frames the AI-vendor independence gap (ACCWEEKLY-INDEP-2026).
- 2026-09-22: Grant Thornton UK chief executive describes declining a client after consulting the FRC (IRISHTIMES-GT-2026).
- 2026-10-07: commentary calls for 'SOX for AI' style independence rules for those auditing AI developers (GOPALAN-SUBSTACK-2026).
- 2026-10-13: AICPA practice aid on AI considerations; more sections promised (AICPA-PA-2026). 2026-10: ACCA ethics report puts AI first among ethical challenges (ACCA-ETHICS-2026).
- 2026-03-04: Grant Thornton UK announces an AI-powered onboarding and acceptance platform (GT-FENERGO-2026), the only named firm acceptance-tool announcement found.

### Workforce and role effects

- Botic warned that reliance on agentic AI may erode skepticism and that new paths will be needed for junior auditors to gain core skills (AT-PCAOBPE-2025).
- Oath hires 'accountant engineers' and says much of the automatable work is junior work (AT-PEEC-2026; FINSTORY-OATH-2026).
- Grant Thornton UK's chief executive said the firm is increasing graduate hiring and that AI creates opportunity, while some clients do not want AI in their audits (IRISHTIMES-GT-2026).
- An Earmark podcast episode (5 Mar 2026) on PE in accounting firms covers partner and staff reactions and says AI squeezes entry-level work (EARMARK-2026; show notes only).
- Independence and ethics staff are asked to take on vendor, alliance and structural reviews that did not exist as routine work (inferred from entries 09 to 13; no source describes staffing).

### Objections and concerns practitioners raise

- PE short-term incentives, a median PE holding period of about five years, secondary sales and capital leakage may pressure quality management (IFAC-AQ-2026); fewer specialists and reduced staffing, and threats to independence and culture (AT-PCAOBPE-2025).
- Consolidation may concentrate public-company audit among fewer firms (AT-PCAOBPE-2025; TR-HOHL-2026).
- AI alliances create operational dependence not covered by rules written for industrial companies (FOURTHWEB-ANTHROPICEY-2026, low-authority commentary).
- Standards written without tech-company input could favour large firms that build AI in-house (AT-PEEC-2026).
- Critics view the SEC review as deregulation; the SEC says no (MCKENNA-DIG-2026, free part only, opinion; TR-HOHL-2026).
- Automation bias is named as a threat to objectivity in the IESBA Code (ACCWEEKLY-INDEP-2026; ICAS-IESBASNAP-2026).

### Interview probes for an advisor

1. How does the firm decide that an AI alliance, tool licence or co-developed client product is clear of independence rules, who signs off, and has any acceptance or continuance decision changed because of one?
2. If the firm is PE-backed or in an APS, what has changed in who decides whether to accept or keep a client, and which AI or technology platforms does the non-attest entity supply to the audit practice under the administrative services agreement?
3. Where in onboarding, KYC, conflicts and independence checks is AI used today, and what are the false-positive, override and exception rates? (Expect no answer on rates; note whether anyone measures them.)
4. How does the firm tell clients, and record client consent, when AI touches their data or their audit, and have any clients refused?
5. Who in the independence function understands AI services well enough to classify a build, host or licence engagement, and what happens when the Code is silent?

### Data conflicts and caveats

- PE transaction counts differ across sources: PCAOB more than 90 since 2020 (Gunia) versus CPA Trendlines more than 53 from 2020 to mid-2025 (JOFA-FACULTY-2025). Definitions and periods are not stated to match.
- PEEC timeline: Accounting Today (31 Aug 2026) says comments are due 'by the end of this month', while JofA (10 Aug 2026) says a second exposure draft is still to be discussed in October and Ho says re-exposure in Oct or Nov. I report both and do not resolve them.
- The reported Anthropic auditor choice rests on secondary reports of an unopened Financial Times piece.
- The Irish Times item is a syndicated Financial Times article; direct quotation of the Grant Thornton chief executive is as the article reports it.

---

## 4. Routed to other modules

- **Assurance over AI systems and independence of AI auditors** (Big Four AI assurance services, who audits AI labs, ISO/IEC 42006 style competence and independence rules): target **other-assurance** (assurance-over-AI). Sources CONSULTANCY-BIG4AI-2025 and GOPALAN-SUBSTACK-2026.
- **SOC 2 tool-provider arrangements, bundled fees and referral terms** as SOC engagement independence: target **other-assurance** (SOC). Source JOFA-SOCETH-2026. Entry 09 keeps the generic vendor-independence step.
- **Firm AI tool governance, supervision and review, approved-tool lists, data-training rights in AI vendor contracts**: target **quality-management**. Sources AICPA-PA-2026 (Part 2 summary), JOFA-ETHAI-2026.
- **PCAOB quality-control inspection of PE and APS firms; Inspections Modernization Council**: target **quality-management**. Source AT-PCAOBPE-2025.
- **Client AI governance maturity and AI-operated controls as risk-assessment input**: target **planning-risk-assessment**. Source AICPA-PA-2026; the CAQ Spring 2026 pulse in the landscape file was not reopened.
- **Junior skill erosion, graduate intake and 'accountant engineer' roles**: target the cross-cutting **audit firm business model and workforce** lens. Sources AT-PCAOBPE-2025, FINSTORY-OATH-2026, EARMARK-2026.
- **AI-native audit firms and AI audit start-up funding** (Modus, Repodo, Oath, Clark): target the cross-cutting **audit firm business model and workforce** lens; the independence aspects are in entries 12 and 13.
- **Audit fee and pricing pressure from AI**: target the same cross-cutting lens; not found in my sources (the landscape file cites a Feb 2026 commentary that I did not reopen).

---

## 5. Sources

Access is `full` for every source below (opened and read), with notes where only part was readable. Types follow the vocabulary. No `regulator` primary documents were opened: regulator remarks are read through press reports.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| JOFA-ETHAI-2026 | Accounting ethics in the age of AI | Journal of Accountancy (AICPA ethics staff) | professional-body | https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 |
| JOFA-SOCETH-2026 | SOC engagements: Ethics risks with tool providers | Journal of Accountancy (AICPA ethics staff) | professional-body | https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 |
| JOFA-NILSEN-2025 | Navigating outside investors: Safeguarding ethics and independence in evolving practice structures | Journal of Accountancy (AICPA staff author) | professional-body | https://www.journalofaccountancy.com/issues/2025/oct/navigating-outside-investors-safeguarding-ethics-and-independence-in-evolving-practice-structures/ | 2025-10-24 |
| JOFA-PE-2025 | AICPA seeks feedback on independence rules related to private equity | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2025/mar/independence-rules-private-equity/ | 2025-03-10 |
| JOFA-ED-2025 | AICPA proposes changes to independence guidelines related to private equity | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2025/dec/aicpa-proposes-changes-to-independence-rules-related-to-private-equity/ | 2025-12-19 |
| JOFA-PEEC-2026 | PEEC to continue discussions on alternative practice structures | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/ | 2026-08-10 |
| JOFA-IESBAAPS-2026 | IESBA to assess need for standards on alternative practice structures | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/mar/iesba-to-assess-need-for-standards-on-alternative-practice-structures/ | 2026-03-27 |
| JOFA-FACULTY-2025 | What faculty should know about private equity in accounting | Journal of Accountancy (Academic Update) | professional-body | https://www.journalofaccountancy.com/newsletters/academic-update/what-faculty-should-know-about-private-equity-in-accounting | 2025-09-08 |
| AT-PEEC-2026 | AICPA weighs PE and tech impact on audit independence | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules | 2026-08-31 |
| AT-PCAOBPE-2025 | PCAOB warns auditors about AI and PE | Accounting Today | press | https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe | 2025-12-09 |
| AT-IFAC-2026 | IFAC: Over 1,000 firms have taken PE money | Accounting Today | press | https://www.accountingtoday.com/news/ifac-releases-private-equity-data | 2026-03-02 |
| CPAPA-IFAC-2026 | Over 1,000 Accounting Firms Globally Have Been Involved in Private Equity Investment in the Past Decade, IFAC Says | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/06/over-1000-accounting-firms-globally-have-seen-private-equity-investment-in-the-past-decade-ifac-says/ | 2026-03-06 |
| NYCPA-HOHL-2025 | SEC's Chief Accountant Discusses Audit Inspections, Conflict-of-Interest Rule Changes | NYSSCPA | press | https://nysscpa.org/news/1045145-secs-chief-accountant-discusses-audit-inspections-conflict-of-interest-rule-changes-2025-12-12 | 2025-12-12 |
| NYCPA-HOHL-2026 | SEC Chief Accountant Clarifies Agency's Approach to Auditor Independence | NYSSCPA | press | https://nysscpa.org/news/1048128-sec-chief-accountant-clarifies-agencys-approach-to-auditor-independence-2026-06-08 | 2026-06-08 |
| TR-HOHL-2026 | SEC Chief Accountant Hohl Dispels Rumors of Weakening Auditor Independence Rules | Thomson Reuters Checkpoint News | press | https://tax.thomsonreuters.com/news/sec-chief-accountant-hohl-dispels-rumors-of-weakening-auditor-independence-rules/ | 2026-06-05 |
| IRISHTIMES-GT-2026 | Grant Thornton's UK boss defends private equity ownership | The Irish Times (Financial Times syndication) | press | https://www.irishtimes.com/business/2026/09/22/grant-thorntons-uk-boss-defends-private-equity-ownership/ | 2026-09-22 |
| BBT-FRC-2025 | UK Watchdog Says Private Equity Poised to Help Audit Quality | Bloomberg Tax | press | https://news.bloombergtax.com/financial-accounting/uk-watchdog-says-private-equity-poised-to-help-audit-quality | 2025-02-13 |
| THEACCOUNTANT-ICAS-2025 | Private equity and its impact on audit quality | The Accountant (interview with ICAS) | press | https://www.theaccountant-online.com/features/private-equity-and-its-impact-on-audit-quality/ | 2025-08-14 |
| CONSULTANCY-BIG4AI-2025 | Big Four weighing up new AI audit offerings | Consultancy.uk | press | https://www.consultancy.uk/news/40424/big-four-weighing-up-new-ai-audit-offerings | 2025-06-10 |
| CRYPTOBRIEFING-ANTHROPICEY-2026 | Anthropic likely to select EY as auditor amid Big Four conflicts | Crypto Briefing | press | https://cryptobriefing.com/anthropic-ey-auditor-big-four-conflicts/ | 2026-08-12 |
| FOURTHWEB-ANTHROPICEY-2026 | Anthropic Can't Find an Auditor That Doesn't Use Claude | The Fourth Web | press | https://wire.fourthweb.ai/anthropic-cant-find-an-auditor-that-doesnt-use-claude/ | 2026-08-14 |
| FINSTORY-OATH-2026 | Ex-PCAOB regulator QUITS...joins AI Audit startup targeting 80% Automation | The Finance Story | press | https://thefinancestory.com/ex-pcaob-regulator-joins-ai-native-audit-firm-oath | 2026-06-03 |
| ACCWEEKLY-INDEP-2026 | AI Audit Tools and the Independence Gap Nobody Fixed | Accounting Weekly (CIBA) | professional-body | https://www.accountingweekly.com/trending-news/ai-audit-tools-and-the-independence-gap-nobody-fixed | 2026-09-01 |
| GOPALAN-SUBSTACK-2026 | AI Is About to Repeat Enron's Audit Problem | Sriram Gopalan (Substack) | community | https://sgopalanbtg.substack.com/p/ai-is-about-to-repeat-enrons-audit | 2026-10-07 |
| MCKENNA-DIG-2026 | Auditor independence: What's behind the SEC's latest push to relax the rules, again? Part 1 | The Dig (Francine McKenna, Substack) | community | https://thedig.substack.com/p/auditor-independence-whats-behind | 2026-05-26 |
| BIG4NEWS-2026 | The Big Four AI Arms Race, Evergrande, Governance and Culture | Big4News (newsletter) | community | https://www.big4news.com/p/big-four-news-20-may-2026 | 2026-05-20 |
| LEARNFORMULA-APS-2026 | The Governance Gap: How PEEC is Drafting the Ethical Playbook for Alternative Practice Structures and AI | LearnFormula | community | https://cfe-cpe-us.learnformula.com/latest-intelligence/the-governance-gap-how-peec-is-drafting-the-ethical-playbook-for-alternative-practice-structures-and-ai | 2026-08-11 |
| EARMARK-2026 | What Private Equity Really Changes Inside an Accounting Firm (Earmark Podcast, ep. 110) | Earmark Podcast via CastFox (show notes) | podcast | https://www.castfox.net/podcast/earmark-podcast-earn-free-accounting-cpe-3961413/episode/what-private-equity-really-changes-inside-an-accounting-firm-wiith-devin-mathews-239626 | 2026-03-05 |
| KU-SYMPOSIUM-2026 | 2026 Deloitte/University of Kansas Auditing Symposium (agenda) | University of Kansas School of Business | conference | https://business.ku.edu/research-and-faculty/accounting/deloitte-ku-auditing-symposium | 2026-05-08 |
| ACCA-ETHICS-2026 | Navigating ethics for trust | ACCA | survey | https://www.accaglobal.com/content/dam/gb/policy-and-insights/reports/2026/navigating-ethics-trust.pdf | 2026-10 |
| IFAC-PE-2026 | Private Equity Investment in Accountancy: IFAC Releases Research and Online Resource | IFAC | professional-body | https://www.ifac.org/news-events/2026-03/private-equity-investment-accountancy-ifac-releases-research-and-online-resource | 2026-03-02 |
| IFAC-AQ-2026 | Audit Quality: Considerations and Implications | IFAC | professional-body | https://www.ifac.org/private-equity-investment-accountancy/audit-quality-considerations-and-implications | 2026-06 |
| AE-BEYONDPE-2025 | Beyond private equity: third party ownership in the accountancy and audit sector (summary) | Accountancy Europe | professional-body | https://accountancyeurope.eu/wp-content/uploads/2025/11/251121-Beyond-Private-Equity-Third-Party-ownership-summary.pdf | 2025-11 |
| AE-PE-2026 | Private Equity in European Accountancy and Audit Firms: Jan 2025 - Apr 2026 | Accountancy Europe | professional-body | https://accountancyeurope.eu/wp-content/uploads/2026/05/260629-Private-equity-investment-in-accountancy-and-audit-sector-in-EU-from-January-2025-to-April-2026.pdf | 2026-07 |
| ICAS-IESBASNAP-2026 | IESBA issues snapshot on the ethical implications of using technology, including AI | ICAS | professional-body | https://icas.com/news-insights-events/news/ethics/iesba-issues-snapshot-on-the-ethical-implications-of-using-technology-including-ai/ | 2026-07-14 |
| IESBA-HIGHLIGHTS-2026 | June 2026 IESBA Meeting Highlights and Decisions | IESBA | standard-setter | https://www.ethicsboard.org/_flysystem/azure-private/2026-07/June%202026%20IESBA%20Meeting%20Highlights.pdf | 2026-07 |
| IESBA-PETOR-2026 | Private Equity and Other External Investment in Firms: Terms of Reference (approved) | IESBA | standard-setter | https://www.ethicsboard.org/_flysystem/azure-private/2026-06/Agenda%20Item%203A.2%20%28Approved%29%20-%20PE%20and%20Other%20External%20Investments%20in%20Firms%20Terms%20of%20Reference.pdf | 2026-06 |
| IESBA-TECH4A-2026 | Emerging Technologies: A Characteristic-based Approach to Ethical Considerations (draft, agenda item 4-A) | IESBA | standard-setter | https://www.ethicsboard.org/_flysystem/azure-private/2026-05/Agenda%20Item%204A%20-%20Emerging%20Technologies%20-%20A%20Characteristic-approach%20to%20Ethical%20Considerations%20for%20Professional%20Accountants.pdf | 2026-05 |
| APESB-PE-2025 | Update on Private Equity Investment in Firms (agenda item 11) | APESB | standard-setter | https://apesb.org.au/wp-content/uploads/2025/06/Agenda_Item_11_Update_on_Private_Equity_Investment_In_Firms.pdf | 2025-06 |
| ANTHROPIC-DELOITTE-2025 | Deloitte will make Claude available to 470,000 people across its global network | Anthropic | vendor | https://www.anthropic.com/news/deloitte-anthropic-partnership | 2025-10-06 |
| ANTHROPIC-KPMG-2026 | KPMG integrates Claude across its core business and workforce of more than 276,000 | Anthropic | vendor | https://www.anthropic.com/news/anthropic-kpmg | 2026-05-19 |
| GT-FENERGO-2026 | Faster starts, stronger safeguards: Grant Thornton upgrades client onboarding with Fenergo | Grant Thornton UK | firm | https://www.grantthornton.co.uk/news-centre/fenergo---march-2026/ | 2026-03-04 |
| ZYGOS-AISENSE-2026 | Artificial Intelligence in AML Compliance | Zygos (Softline Computer Systems) | vendor | https://getzygos.com/?p=49476 | 2026-02-10 |
| DELOITTE-IE-TR-2026 | 2026 Transparency Report, Deloitte Ireland | Deloitte Ireland | firm | https://www.deloitte.com/content/dam/assets-zone2/ie/en/docs/about/2026/deloitte-transparency-report-2026.pdf | 2026-09 |
| DELOITTE-LU-TR-2026 | 2026 Transparency Report, Deloitte Audit (Luxembourg) | Deloitte Luxembourg | firm | https://www.deloitte.com/content/dam/assets-zone2/lu/en/docs/about/2026/lu_transparency_report-2026.pdf | 2026-09 |

Notes on access:

- CRYPTOBRIEFING-ANTHROPICEY-2026: the direct page returned HTTP 403; I read it through the brief's permitted text mirror before the search quota ran out.
- BBT-FRC-2025 (Bloomberg Tax) and MCKENNA-DIG-2026 are paywalled; only the visible opening text was read.
- CPAPA-IFAC-2026 was read only in its opening paragraphs; its figures duplicate IFAC-PE-2026.
- EARMARK-2026: show notes only; the audio was not heard.
- AICPA-PA-2026: the press release was read; the practice aid itself needs an AICPA login.
- IESBA-TECH4A-2026 is a draft agenda paper for the June 2026 meeting; the highlights say the staff publication was expected in July 2026. The ICAS snapshot item dated 14 Jul 2026 reports the snapshot was issued.
- Total: 47 distinct sources: press 19, professional-body 10, standard-setter 5, community 4, firm 3, vendor 3, conference 1, survey 1, podcast 1. Academic 0, regulator 0 (primary), job-posting 0.

---

## 6. Gaps

- **Nothing on AI performance in acceptance, KYC or independence work.** No error, false-positive, override, parallel-run or inspection data exists in the sources. The only direction-1 evidence is a Grant Thornton UK partnership announcement and a vendor R&D write-up, neither with outcomes. The Landscape file's Kingland (acceptance workflow) and Intapp (conflicts and independence) leads were not opened; I could not get to the vendor pages, investor materials or any named firm case study.
- **Web-search quota ran out partway.** Leads I did not reach: the Financial Times original on Anthropic's likely auditor; the Washington Post piece on who audits AI; the Wall Street Journal article on Oath; the AICPA practice aid full text (to confirm its acceptance-and-continuance wording and the AU-C 210 position); the PEEC exposure draft text and the 81 comment letters; the IESBA staff alert on PE and its date; a second search on Intapp and independence tooling; AI-in-acceptance practitioner posts; additional podcast episodes (an Accounting Today Podcast episode of 2 Mar 2026 on PE and independence, the AccountingWEB 'No Accounting for Taste' episode on PE versus independence, a Behind the Buyouts episode of 24 Jun 2026 on accounting-firm M&A) known only from search results and not opened.
- **Conference coverage is thin.** I opened one agenda (the Deloitte/KU symposium) and found no slides, recordings or write-ups. The AICPA ENGAGE agenda page returned 403 and the Dec 2025 SEC/PCAOB conference was read only through press accounts. IIA, ISACA and ICAEW events were not checked for independence or PE sessions.
- **No regulator primary documents.** pcaobus.org, ifiar.org and sec.gov speech texts were not opened; PCAOB and SEC remarks come through Accounting Today, NYSSCPA and Thomson Reuters. The FRC Feb 2025 statement is seen only through a paywalled Bloomberg Tax excerpt.
- **No academic evidence.** The only academic item is a KU symposium paper title on studying PE investments in accounting firms (agenda only). I found no empirical result on PE, AI and audit quality or independence.
- **No job postings or community forum discussion** (Reddit, LinkedIn, Going Concern) were reachable.
- **Missing voices:** EY, PwC and the mid-tier firms on AI-alliance independence; any technology vendor on the PEEC proposal; Anthropic or any Big Four firm confirming the auditor story; audit committees on AI alliances.
- **Unverified landscape items:** Grant Thornton's Gtap platform under an APS, Modus ($85M), Repodo, the KPMG fee episode and CAQ Spring 2026 pulse figures come from the landscape file and were not reopened; I did not use them as evidence.
