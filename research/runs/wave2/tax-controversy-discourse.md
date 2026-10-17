# Tax / controversy / discourse: what practitioners are saying about AI in audits, notices, appeals and disputes

- **Archetype:** tax
- **Module:** controversy (tax audits, notices, appeals and disputes from the taxpayer and practitioner side, plus tax-authority AI and its governance)
- **Angle:** discourse
- **Prepared:** 2026-10-17 (wave 2)
- **Method:** The landscape file's controversy leads were opened first (curl, `pdftotext`, `r.jina.ai` mirror), then followed to primary material (IRM 10.24.1, GAO, TIGTA, the National Taxpayer Advocate's reports, the Werfel risk-framework appendices). A short set of web searches added practitioner and law-firm commentary. The search budget ran out before the last two planned searches (the Khoja hearing and HMRC's annual report), and the sources that depend on them are marked. Reddit r/taxpros, TaxProTalk and the TEI and ABA member areas could not be reached, so practitioner community chatter is a gap and not a finding.

---

## 1. Summary

- **The discourse is about asymmetry.** Practitioners and the National Taxpayer Advocate (TAS) describe a tax authority that is raising the speed and volume of automated selection, matching and notices while its human capacity to resolve them falls. The IRS lost more than a quarter of its staff in 2025 and says headcount was flat at about 74,000 through 2026. Its CEO has told staff it will be "AI-first" (Nextgov, 2 Oct 2026). Commentators advise clients and firms to build notice-response workflows, document earlier and expect slower resolution. Some of that advice rests on weak sourcing (see the reliability notes in section 3).
- **Evidence of quality is thin and mostly independent when it exists.** TIGTA found the IRS had no process to show its AI examination-selection models beat prior methods, and one pilot model produced more dollars per exam hour but more no-change audits. TAS reports that the no-change rate for audited low-income filers fell sharply in FY2025 while the no-response rate rose by more than ten points. It also reports that 80% of survey responses called the IRS chatbot unhelpful. No source reports an override or error rate for practitioner-side AI in controversy work.
- **Practitioner-side AI governance is "existing duties apply", and three friction points are visible.** The first is hallucinated authorities. In *Clinco* (T.C. Memo. 2026-16) the court faulted the taxpayer's counsel, and in *Khoja* an IRS attorney's motion cited a non-existent case. The second is fees: the IRS Office of Professional Responsibility (OPR) says AI savings should be passed on, and the AICPA has asked for clarification because the language does not seem to allow value pricing. The third is privilege: *United States v. Heppner* held that AI documents a client generated alone were not privileged.
- **Where the field says it is heading.**
  - The IRS emphasises collection and automation over audits (Bloomberg Tax, Dec 2025).
  - The Tax Court is "feeling its way" on AI guardrails (Mar 2026).
  - The AICPA's new Council on AI Risk in Tax (Sep 2026) will test Danny Werfel's 20-risk framework through the year.
  - GAO's eight IRS recommendations have 180-day responses due in fall 2026.
  - TEI's annual conference (18–21 Oct 2026) has not yet produced recaps.
- **Candidate use cases:** 18 (1 at grade A, 6 at B, 5 at C, 6 at D). Most graded A to C describe tax-authority AI; the practitioner-side entries are mostly C or D because public deployments with measurements do not exist.

---

## 2. Use cases

```yaml
- id: tax-controversy-01
  title: AI-assisted IRS notice intake, summarisation and draft response
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Practitioners receive IRS and state notices (for example CP2000 underreporter notices) that carry strict response deadlines. Staff must read each notice, extract the deadline, amount and issue, and draft a response. Commentators say notice volume is rising while IRS human resolution capacity has shrunk, so firms need a structured intake, POA and tracking process.
  solution: A vendor tool analyses an uploaded notice, surfaces the key elements (deadline, amount due, underlying issue) and offers response options and draft communications for a reviewer. TEI's March 2026 programme included a hands-on "Managing Tax Notices with AI" lab. One practitioner article recommends a structured workflow of intake, POA filing, internal deadlines and client expectation-setting, and does not tie it to a specific AI tool.
  outcomes:
    - lever: speed
      description: Vendor says the path from receipt to action is shortened. No figure or customer is named.
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: WK-NOTICES-2026
  prerequisites:
    - A secure, enterprise-approved tool, because the OPR alert limits client data to such tools (IRC 6713 and 7216 exposure).
    - A notice intake and tracking process (POA filing, internal deadlines, client communication), which the Accounting Today author describes as the basis for handling more automated notices.
  risks_and_guardrails:
    - OPR Alert 2026-19 says a practitioner must review everything the tool produces and cannot rely solely on it (Circular 230 10.22, 10.37).
    - Confidentiality across clients is a named OPR concern.
    - The vendor article is marketing, and no independent evaluation of notice-response accuracy was found.
  human_checkpoints:
    - Practitioner reviews the extracted deadline, amount and issue against the notice before acting.
    - Practitioner approves and signs any response sent to the IRS.
  role_evolution: Accounting Today's author argues that as AI handles cross-matching and flagging, the practitioner's role moves toward interpretation, client preparation and year-round risk advice. This is the author's opinion and is not measured.
  evidence_grade: C
  sources:
    - { ref: WK-NOTICES-2026, title: "How to respond to IRS notices with a clear, structured workflow", publisher: Wolters Kluwer Tax & Accounting, type: vendor, url: "https://www.wolterskluwer.com/en/expert-insights/how-to-respond-to-irs-notices-with-a-clear-structured-workflow", date: 2026-07-06, access: full, locator: "Key points; section on CCH AnswerConnect Document Analysis" }
    - { ref: ACCTODAY-2026, title: "What does an AI-driven IRS mean for small accounting firms?", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms", date: 2026-07-02, access: full, locator: "Step 4: Implement a structured notice-response workflow" }
    - { ref: TEI-MIDYEAR-2026, title: "TEI Midyear Conference 2026 at-a-glance agenda", publisher: Tax Executives Institute, type: conference, url: "https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf", date: 2026-03-15, access: full, locator: "Breakout block 1:30-2:30 PM: TEI Tax Lab: Managing Tax Notices with AI (title only)" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework items 1, 5 and 6" }
  last_reviewed: 2026-10-17
  notes: The Wolters Kluwer page was reached through the r.jina.ai mirror because the direct request returned HTTP 403. The TEI entry gives a session title only, with no content.

- id: tax-controversy-02
  title: Pre-filing audit-risk review and contemporaneous substantiation, shaped by IRS AI selection patterns
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Commentators say IRS AI selection and data-matching flag statistical anomalies faster than manual review did, and the IRS does not disclose the selection criteria. They argue that documentation which satisfied a human reviewer may not satisfy a model.
  solution: Practitioners are advised to add a pre-filing review of client returns against published red-flag patterns, to raise the documentation bar (contemporaneous records, written business purpose, year-over-year consistency), and to reconcile third-party reporting (for example the new Form 1099-DA) before filing. PwC specialists, as reported by Reuters through NYSSCPA, say examiners are weighting business purpose and contemporaneous documentation. The sources describe a manual checklist and do not describe an AI tool performing the review.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: ACCTODAY-2026
  prerequisites:
    - Client records kept through the year.
    - Knowledge of the patterns the IRS publicly associates with AI selection (GAO and TIGTA publications).
  risks_and_guardrails:
    - The Accounting Today piece is an opinion article by an operations manager at a vendor and mixes sourced and unsourced claims (see section 3). Do not treat its audit-flag list as an IRS standard.
    - The IRS does not publish its selection criteria, so any pre-filing screen is a proxy.
  human_checkpoints:
    - Preparer decides which flags to resolve and how to document the position.
  role_evolution: Accounting Today argues small firms can reposition as year-round compliance-risk partners. NYSSCPA reports PwC specialists making a similar point about documentation. Neither source measures the effect.
  evidence_grade: D
  sources:
    - { ref: ACCTODAY-2026, title: "What does an AI-driven IRS mean for small accounting firms?", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms", date: 2026-07-02, access: full, locator: "Documentation standards have effectively increased; Steps 1-3 and 5" }
    - { ref: NYSSCPA-PWCWEBCAST-2026, title: "IRS Expands AI-Driven Enforcement While Adding New Taxpayer Relief", publisher: NYSSCPA (summarising Reuters and a PwC webcast), type: professional-body, url: "https://nysscpa.org/news/8725456-irs-expands-ai-driven-enforcement-while-adding-new-taxpayer-relief-2026-08-10", date: 2026-08-10, access: full, locator: "Paragraphs 1-3" }
    - { ref: BEANCOUNT-IRM-2026, title: "Audited by an Algorithm: What the IRS's New AI Governance Policy Means for Your Small Business", publisher: Beancount.io (hosted accounting vendor blog), type: vendor, url: "https://beancount.io/blog/2026/07/11/audited-by-algorithm-irs-ai-audit-selection-irm-10-24-1-guide", date: 2026-07-11, access: full, locator: "Sections on what raises the score and the resolution lag" }
  last_reviewed: 2026-10-17
  notes: Labelled idea. The NYSSCPA page carries no date, so 2026-08-10 is taken from the URL slug. The vendor blog's industry-ratio examples are unsourced and are not used.

- id: tax-controversy-03
  title: Mandatory authority verification for AI-assisted briefs, protests and memoranda in controversy matters
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Generative tools can produce plausible but non-existent case citations. In Clinco, three of four cases cited for the "wet signature" argument were nonexistent, and counsel repeated one after the IRS flagged it. In Khoja, the judge questioned an IRS attorney about a non-existent citation in a motion. The Tax Court has no Rule 11 equivalent, which complicates sanctions.
  solution: The Journal of Accountancy article and OPR recommend firm AI policies, treating AI text as draft, human verification of every citation and calculation, citation-verification logs or a second reviewer for briefs, and documentation of verification. Judge Holmes says the Tax Court's main existing penalty tool is IRC 6673 (up to $25,000) and that a certification rule "might" be considered, though he doubts it would make sense.
  outcomes:
    - lever: risk
      description: Judge Holmes says he has seen fewer than a dozen instances of hallucinated cases in Tax Court filings and has issued no sanctions himself (as of March 2026).
      figure: fewer than 12
      measures: Instances of hallucinatory cases cited that Judge Holmes has seen, as he stated in an interview. This is a count and not a rate.
      provenance: independent
      source_ref: BLOOMBERG-TAXCTAI-2026
  prerequisites:
    - Written firm AI policy with permitted tools, training and documentation procedures.
    - Access to authoritative databases against which citations can be checked.
  risks_and_guardrails:
    - OPR cites Circular 230 sections 10.22 (due diligence), 10.35 (competence), 10.36 (firm procedures) and 10.37 (written advice).
    - AICPA Statements on Standards for Tax Services section 1.4 (reliance on tools) keeps responsibility with the member, as described in the Journal of Accountancy article.
    - Over three-quarters of Tax Court cases are pro se, which complicates any disciplinary design.
  human_checkpoints:
    - Second reviewer or citation log before filing.
    - Attorney certifies the filing under Tax Court Rule 201(a) and the ABA Model Rules.
  role_evolution: The Journal of Accountancy article says AI may assist drafting and research, but the duty to verify authorities stays with the practitioner.
  evidence_grade: D
  sources:
    - { ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: 2026-09-01, access: full, locator: "Sections 'The apparitions in the briefing', 'Practical risk management for tax practitioners' and the firm-policy sidebar" }
    - { ref: BLOOMBERG-TAXCTAI-2026, title: "Tax Court Navigates AI Misuse Rules for Self-Represented Filers", publisher: Bloomberg Law / Bloomberg Tax, type: press, url: "https://news.bloomberglaw.com/insurance/tax-court-navigates-ai-misuse-rules-for-self-represented-filers", date: 2026-03-20, access: full, locator: "Sections 'Arrow in Quiver', 'Feeling Our Way', 'Protecting Taxpayers'; paywall after the visible portion" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework items 1-5; Best Practices" }
    - { ref: MC-JORDAN-2026, title: "Katherine Jordan Quoted on Emerging AI Issues in U.S. Tax Court Filings in Tax Notes", publisher: Miller & Chevalier, type: firm, url: "https://www.millerchevalier.com/publication/katherine-jordan-quoted-emerging-ai-issues-us-tax-court-filings-tax-notes", date: 2026-03-23, access: full, locator: "Summary paragraph" }
  last_reviewed: 2026-10-17
  notes: Labelled idea. The incidents show AI is already used in these filings, but no source describes a named firm's managed deployment or reports verification error rates. The Journal of Accountancy says some firms keep citation logs or use second reviewers and does not name them. The Khoja facts come from the Bloomberg Law article. The hearing took place on 11 March, and the article's date places it in 2026. The Tax Notes article behind the Miller & Chevalier item was not opened.

- id: tax-controversy-04
  title: Counsel-directed, enterprise-tool AI analysis to preserve privilege in controversy matters
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [expert-judgment, research-synthesis]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: In United States v. Heppner (S.D.N.Y., 17 Feb 2026) the court held that AI-generated reports a defendant made with a consumer tool, without counsel's direction, were neither privileged nor work product, even though they were later given to counsel. Controversy clients are likely to use consumer AI on their own matters.
  solution: Law-firm guidance advises treating public AI tools as third parties by default, using enterprise tools with limits on training, disclosure and retention for sensitive matters, having counsel direct AI work and documenting that direction, and logging AI outputs carefully. Miller & Chevalier's Sheri Dillon names AI ethics, privilege and confidentiality as a top 2026 challenge for tax practitioners and says they should educate clients.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: MOFO-HEPPNER-2026
  prerequisites:
    - Enterprise AI tools with contractual limits on training use, disclosure, retention and access.
    - Engagement-letter and client-instruction practice covering consumer AI use.
  risks_and_guardrails:
    - Heppner was a criminal case, not a tax case, and a different court (E.D. Mich., Warner) reached a different result on different facts, as noted in a search summary.
    - Privilege for AI-assisted work in tax controversy specifically has not been tested in the sources found.
  human_checkpoints:
    - Counsel decides what is run through AI and directs it.
  role_evolution: Dillon says practitioners must independently confirm any AI results and educate clients about appropriate AI use.
  evidence_grade: D
  sources:
    - { ref: MOFO-HEPPNER-2026, title: "Privilege in the Age of AI: SDNY Holds AI-Generated Documents Are Not Privileged", publisher: Morrison Foerster, type: firm, url: "https://www.mofo.com/resources/insights/260220-privilege-in-the-age-of-ai-sdny-holds", date: 2026-02-20, access: full, locator: "Practical Steps; Background; Key Holdings" }
    - { ref: BLOOMBERG-DILLON-2026, title: "Five Questions With Miller & Chevalier Tax Attorney Sheri Dillon", publisher: Bloomberg Tax Daily Tax Report, type: press, url: "https://news.bloombergtax.com/daily-tax-report/five-questions-with-miller-chevalier-tax-attorney-sheri-dillon", date: 2026-10-09, access: full, locator: "Answer on the top challenge for 2026" }
  last_reviewed: 2026-10-17
  notes: Labelled idea. The E.D. Mich. contrast comes from a search summary and was not opened.

- id: tax-controversy-05
  title: IRS machine-learning selection of returns and issues for examination
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: The IRS selects returns for examination, historically with the DIF scoring model. TIGTA reports a high share of examinations, particularly of non-individual returns, closing with no change to the return, which burdens compliant taxpayers and uses exam resources.
  solution: The IRS integrated statistical and machine-learning techniques into return selection, with models trained on current return data and not on historical exam results. The LB&I Division has a Corporate Line Anomaly Recommender and a Large Partnership Compliance model. The SB/SE Division piloted a Form 1040 selection model but made no deployment decision. IRM 10.24.1 now treats AI that informs or influences whether a taxpayer is audited as presumed high-impact, which triggers minimum risk-management practices including human oversight and consistent remedies or appeals.
  outcomes:
    - lever: quality
      description: TIGTA says the IRS had not established processes to evaluate whether the AI models beat prior methods, and data were not available to evaluate the LB&I models. In a Form 1040 pilot the model would yield a higher assessment per exam hour but also a higher no-change rate.
      figure: no performance figure published (pilot direction only)
      measures: Pilot test results for the SB/SE Form 1040 selection model, qualitative direction only, redacted in the public report.
      provenance: independent
      source_ref: TIGTA-2025
    - lever: quality
      description: In FY2025 the audit no-change rate for audited taxpayers with under $50,000 of total positive income was almost half the FY2024 rate, which was under half the FY2023 rate. The no-response rate for this group rose by more than ten percentage points from FY2024 to FY2025. TAS says AI may reduce the no-change rate but warns the decline may reflect selecting taxpayers unlikely to respond.
      figure: "almost half (FY2025 vs FY2024); no-response up more than 10 percentage points"
      measures: "IRS audit no-change rate for taxpayers with less than $50,000 of total positive income, FY2025 vs FY2024 (the report's words); no-response rate for the same audited group, FY2024 to FY2025. TAS does not attribute the change to AI."
      provenance: independent
      source_ref: NTA-AR-2025
  prerequisites:
    - Current return data and exam results fed back into model monitoring (TIGTA recommendation).
    - AI governance under IRM 10.24.1, with an impact assessment, pre-deployment testing and ongoing monitoring for high-impact use cases.
  risks_and_guardrails:
    - GAO (May 2024) found the Dependent Database had risk scores that varied by sex, had not been updated since 2001 and had not been comprehensively reviewed for demographic equity. It reported IRS research naming unintentional algorithmic bias as a possible source of racial audit disparities.
    - Werfel's authority risk register lists audit targeting bias and lack of auditability as risks.
    - The IRS does not publish selection criteria.
  human_checkpoints:
    - Examiners and classifiers review model output before a case is opened. This is the commonly described design, but no source publishes a human-override rate.
  role_evolution: TIGTA says historical exam results should feed model improvement. NTA says the IRS needs staff who can train AI in ways that protect taxpayer rights.
  evidence_grade: B
  sources:
    - { ref: TIGTA-2025, title: "The IRS Could Leverage Examination Results in AI Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022)", publisher: Treasury Inspector General for Tax Administration, type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: 2025-05-19, access: full, locator: "Highlights; report pdf pp. 11-13 (model descriptions, pilot test results, LB&I data gap)" }
    - { ref: NTA-AR-2025, title: "National Taxpayer Advocate 2025 Annual Report to Congress", publisher: Taxpayer Advocate Service, type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/01/ARC_Publication-2104_2025_Web.pdf", date: 2026-01, access: full, locator: "Preface, 'Taxpayer Service: Examination and Collection' (pdf p. 27)" }
    - { ref: IRM-10-24-1, title: "IRM 10.24.1 IRS Policy for Artificial Intelligence (AI) Governance", publisher: Internal Revenue Service, type: regulator, url: "https://www.irs.gov/irm/part10/irm_10-024-001r", date: 2026-02-10, access: full, locator: "10.24.1.4.2 item 16 (presumed high-impact); 10.24.1.4.3 (minimum practices); transmittal dated 2026-08-10 supersedes the 2026-02-10 text" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: US Government Accountability Office, type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: 2026-03-24, access: full, locator: "What GAO Found" }
    - { ref: FEDSCOOP-GAOBIAS-2024, title: "IRS's AI system to flag returns for audit may include unintended bias, report finds", publisher: FedScoop, type: press, url: "https://fedscoop.com/irs-ai-systems-bias-audits-racial-disparities-gao-report/", date: 2024-05-23, access: full, locator: "Paragraphs 1-6" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation (with Appendix A)", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08-31, access: full, locator: "Figure 1 items 7 and 18; Appendix A" }
  last_reviewed: 2026-10-17
  notes: Grade B and not A because TIGTA found no performance evaluation and the NTA figures are not attributed to AI. The TIGTA report is redacted in several places. The FedScoop GAO article is a 2024 foundation source. Accounting Today's claim that pilots show the models "outperform" prior methods is not supported by the TIGTA pilot description, which also reports higher no-change rates, and is not used.

- id: tax-controversy-06
  title: AI agents for case summarisation and search in IRS Chief Counsel, Appeals and the Taxpayer Advocate Service
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [research-synthesis, transaction-processing]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: The IRS lost about 25% of its workforce in 2025, and the units that resolve disputes (Chief Counsel, Appeals, TAS) face case backlogs.
  solution: The IRS announced Salesforce Agentforce for case summarisation and search in the Office of Chief Counsel, Taxpayer Advocate Service and Office of Appeals. Salesforce says the agents are built with guardrails and cannot make final decisions or disburse funds. An IRS technology counsel, quoted by Axios, said it would be negligent not to start using the tools so the IRS can compete with law firms.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: IRS-AGENTFORCE-2025
  prerequisites:
    - Modernised case-management platforms in each unit (the Axios piece says the IRS had worked on this for a few years).
  risks_and_guardrails:
    - Agents are described as unable to make final decisions or disburse funds, per the Salesforce executive.
    - The Treasury inventory (Jan 2026) lists one IRS agentic tool classed high-impact (a cloud-code compliance tool, pre-deployment), and this deployment is not described in the FedScoop article.
  human_checkpoints:
    - Staff make the decisions; agents summarise and search.
  role_evolution: The IRS counsel quoted by Axios says staff must adopt the change or leave.
  evidence_grade: C
  sources:
    - { ref: IRS-AGENTFORCE-2025, title: "Exclusive: IRS deploys AI agents", publisher: Axios, type: press, url: "https://www.axios.com/2025/11/21/irs-deploys-ai-agents", date: 2025-11-21, access: full, locator: "Driving the news; What they're saying; The bottom line (opened through the r.jina.ai mirror)" }
    - { ref: EISNER-IRSAI-2026, title: "AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services", publisher: EisnerAmper, type: firm, url: "https://eisneramper.com/insights/tax/ai-irs-transforming-0126", date: 2026-01-27, access: full, locator: "Section 'AI in Taxpayer Services'" }
    - { ref: TREAS-AIINV-2026, title: "IRS ramps up AI use amid staff cuts, Treasury inventory shows", publisher: FedScoop, type: press, url: "https://fedscoop.com/treasury-irs-ai-use-case-inventory/", date: 2026-01-29, access: full, locator: "Paragraphs 1-5" }
  last_reviewed: 2026-10-17
  notes: The Axios piece is an exclusive based on an announcement shared by Salesforce, with an IRS counsel quoted. No source shows use outcomes.

- id: tax-controversy-07
  title: AI-accelerated processing of amended individual returns at the IRS
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing]
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: The IRS receives about 5 million amended returns a year, and processing can take many weeks. In February 2026 the IRS put about 1,500 IT and HR employees on involuntary details to frontline service jobs, with duties that included reducing a backlog of amended returns.
  solution: The IRS CIO told employees the agency is using AI to speed processing of "hundreds of thousands" of amended returns.
  outcomes:
    - lever: speed
      description: The CIO said processing time for an amended individual return, typically 12, 14 or 16 weeks, fell to under three days through AI and automation. This is an official's remark at an all-staff meeting, reported by Nextgov from a transcript obtained by Government Executive.
      figure: from 12-16 weeks to under 3 days
      measures: "Time to process an amended individual return, per the IRS CIO's statement; scope limited to the hundreds of thousands of returns where AI is applied out of about 5 million received annually. The method of measurement is not stated."
      provenance: self-reported
      source_ref: IRS-AIFIRST-2026
  prerequisites:
    - IT and data staff to build and maintain the tools. GAO notes IRS AI-related staff reductions in 2025, including 63 in one analytics group.
  risks_and_guardrails:
    - TIGTA memo cited by FedScoop reports IT staffing down 16% since the start of the current administration, while at least 16 IRS use cases involve IT.
  human_checkpoints:
    - Not described in the source.
  role_evolution: The IRS CEO told staff AI will make the workforce more productive and is "not designed to eliminate jobs", per Nextgov's transcript-based report.
  evidence_grade: B
  sources:
    - { ref: IRS-AIFIRST-2026, title: "Tax chief pushes 'AI-first IRS' to get more out of agency's workforce", publisher: Nextgov/FCW, type: press, url: "https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/", date: 2026-10-02, access: full, locator: "Paragraphs on the all-staff meeting and the amended-returns remarks of CIO Kaschit Pandya" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: US Government Accountability Office, type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: 2026-03-24, access: full, locator: "What GAO Found, paragraph on the 63 lost AI-related staff" }
  last_reviewed: 2026-10-17
  notes: Graded B because the single figure is an official's remark with no method, no sample and no independent check. This is an authority-operations use case that sits next to controversy.

- id: tax-controversy-08
  title: IRS chatbots and voicebots for taxpayer questions and installment agreements
  archetype: tax
  module: controversy
  function: customer-service
  work_types: [client-interaction, transaction-processing]
  pattern: service-agent-escalation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: With IRS staffing about 25% lower and a budget about 20% lower in FY2026, the IRS expects to rely more on technology. Taxpayers in collection and notice situations need to reach the IRS.
  solution: The IRS operates authenticated and unauthenticated chatbots and voicebots for procedural and tax questions and for payment plans, and an international-taxpayer chatbot with live chat (August and December 2025). A taxpayer can ask to be connected to a live assistor during regular hours.
  outcomes:
    - lever: capacity
      description: Installment agreements completed with chatbots rose while total installment agreements fell.
      figure: "+68% chatbot IAs; -7% total IAs (FY2024 to FY2025)"
      measures: "Number of installment agreements completed with chatbots, and total installment agreements, FY2024 to FY2025, as reported by TAS."
      provenance: independent
      source_ref: NTA-AR-2025
    - lever: experience
      description: In survey responses from January to August 2025, users overwhelmingly said the IRS chatbot was not helpful. TAS says the IRS measures chatbot quality largely with a yes/no "was this useful" question and has no resolution or accuracy measure.
      figure: 80% negative response
      measures: "Share of end-of-session responses to the IRS chatbot's yes/no usefulness question that were negative, January-August 2025 (the report's words). Not an accuracy or resolution measure."
      provenance: independent
      source_ref: NTA-AR-2025
    - lever: experience
      description: For the international-taxpayer chatbot, 23 of 200 survey responses called it helpful.
      figure: 11.5%
      measures: "Responses indicating the information was helpful, out of 200 instances of the yes/no end-of-session question (TAS footnote 47)."
      provenance: independent
      source_ref: NTA-AR-2025
  prerequisites:
    - Authentication, a path to a live assistor and outcome-based quality measures, which TAS says the IRS lacks.
  risks_and_guardrails:
    - Werfel's authority register lists chatbot hallucination, drift, over-trust and estoppel-style reliance claims as risks. Its scenarios are illustrative.
    - TAS says the IRS should adopt a service metric covering chatbot and voicebot experience by the end of FY2026.
  human_checkpoints:
    - Escalation to a live assistor on request.
  role_evolution: TAS says reduced staffing may force taxpayers to use self-service tools, or their issues may remain unresolved.
  evidence_grade: A
  sources:
    - { ref: NTA-AR-2025, title: "National Taxpayer Advocate 2025 Annual Report to Congress", publisher: Taxpayer Advocate Service, type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/01/ARC_Publication-2104_2025_Web.pdf", date: 2026-01, access: full, locator: "Preface (pdf p. 27); 'The IRS Does Not Adequately Measure Chatbot and Voicebot Service' (pdf p. 74); international chatbot passage and footnote 47 (pdf p. 147)" }
    - { ref: BLOOMBERG-COLLECTION-2025, title: "IRS Modernizes Collection: What's Next for Tax Practitioners", publisher: Bloomberg Tax (Tax Management Memo), type: press, url: "https://news.bloombergtax.com/tax-management-memo/irs-modernizes-collection-whats-next-for-tax-practitioners", date: 2025-12-23, access: full, locator: "Section 'Enhancing IRS Collection with Tech'" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation (with Appendix A)", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08-31, access: full, locator: "Appendix A risks 1, 2, 4 and 5" }
  last_reviewed: 2026-10-17
  notes: Graded A because of the TAS measurements of IRS deployments. The measures are weak proxies for quality, which TAS itself says. A former IRS SB/SE commissioner (Guillot, Bloomberg Tax) says voicebots have handled millions of calls and that pay plans established were worth at least ten times the $13 million program cost. That is one practitioner's claim without a stated method and is not used as an outcome. The Taxpayer Advocate Service sits inside the IRS but reports independently to Congress.

- id: tax-controversy-09
  title: '"Archie", an AI-enabled Internal Revenue Manual research tool for IRS customer service representatives'
  archetype: tax
  module: controversy
  function: customer-service
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Customer service representatives must find the right Internal Revenue Manual guidance quickly to resolve taxpayer issues on first contact.
  solution: The IRS rolled out "Archie", an AI-enabled tool to help representatives research the IRM, available to about 12,000 representatives. TAS describes it as part of the broader Taxpayer 360 project, which had not yet delivered an integrated taxpayer view.
  outcomes:
    - lever: capacity
      description: Availability only; no outcome measures are given.
      figure: about 12,000 representatives with access
      measures: Number of customer service representatives to whom the tool was available, per TAS (as of the 2026 filing season review).
      provenance: independent
      source_ref: NTA-OBJ-2026
  prerequisites:
    - Searchable IRM content and CSR training.
  risks_and_guardrails:
    - TAS calls the Taxpayer 360 tools "promising steps" and "a work in progress".
  human_checkpoints:
    - The representative remains the one who advises the taxpayer.
  role_evolution: Not described beyond the tool's purpose.
  evidence_grade: B
  sources:
    - { ref: NTA-OBJ-2026, title: "National Taxpayer Advocate FY2027 Objectives Report to Congress (Review of the 2026 Filing Season)", publisher: Taxpayer Advocate Service, type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf", date: 2026-06, access: full, locator: "Taxpayer 360 passage (pdf p. 32); AI-assistance disclosure (pdf p. 2)" }
  last_reviewed: 2026-10-17
  notes: Only the AI mentions in this 5,000-line report were read. The report also states that parts of it were drafted with AI and reviewed by TAS staff.

- id: tax-controversy-10
  title: State tax agency machine-learning audit and return selection, and the oversight gap around it
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: State agencies use automated decision systems to flag returns for audit or collection. Tax Notes reporters describe weak outside review of these systems, and say a faster flagging side is not matched by faster taxpayer challenge channels.
  solution: California's Franchise Tax Board put machine-learning models into service in 2021 to vet returns and help decide which to pursue, as part of its Enterprise Data to Revenue project. New York's tax department runs the Case Identification and Selection System (CISS) for fraud detection and collections and says CISS uses business rules and data analytics and is not an AI system, which the reporters say others dispute.
  outcomes:
    - lever: risk
      description: In California's 2025 report under AB 302, no agency, including the Franchise Tax Board, reported using a high-risk automated decision system. Experts told the reporters this was not credible. The FTB has internal checks for over-selection but no outside review or formal evaluation provided to lawmakers.
      figure: 0 agencies reporting a high-risk system
      measures: "Number of California agencies that reported a high-risk automated decision system to the California Department of Technology, in the final report produced in 2025 (as described by Tax Notes reporters)."
      provenance: independent
      source_ref: NTT-BIAS-2026
  prerequisites:
    - Data pipelines and model-development contracts (the New York system was built under an IBM contract).
  risks_and_guardrails:
    - Reporters cite the earlier Stanford finding that IRS audit models picked disproportionately many Black EITC claimants, and the Dutch benefits scandal.
    - The reporters say demographic data may not be collected, which limits bias testing.
  human_checkpoints:
    - Flags go to staff review or further automated processing. The FTB reportedly says its output checks look for over-selection.
  role_evolution: An Electronic Frontier Foundation source told the reporters that agencies invested in a system may be institutionally biased against finding its problems.
  evidence_grade: B
  sources:
    - { ref: NTT-BIAS-2026, title: "How AI Bias Affects State Audit Selection", publisher: Tax Notes Talk (Tax Analysts), type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/19216367-how-ai-bias-affects-state-audit-selection", date: 2026-05-22, access: full, locator: "Transcript: New York and California case studies; discussion of mistakes and oversight laws" }
    - { ref: TAXNOTESTALK-2025, title: "Artificial Intelligence and State Tax Agencies", publisher: Tax Notes Talk (Tax Analysts), type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/17439828-artificial-intelligence-and-state-tax-agencies", date: 2025-07-04, access: full, locator: "Interview with Ryan Minnick (FTA), survey discussion" }
  last_reviewed: 2026-10-17
  notes: "The Tax Notes investigation \"Unwatched: How State Audit Selection Systems Bypass Oversight\" (14 Apr 2026) was not opened. The podcast gives no outcome figure for the models. A 2012 estimate that CISS helped collect more than $2 billion is cited for the New York system, whose AI status is disputed, so it is not treated as an AI outcome. The FTA's 2024 survey line about AI \"in core functions\" is caveated by the FTA itself as an overly broad question that predated generative AI."

- id: tax-controversy-11
  title: Generative-AI drafting of suggested answers for a state agency's taxpayer-service agents (California CDTFA)
  archetype: tax
  module: controversy
  function: customer-service
  work_types: [client-interaction]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: State agencies face call-centre load at peak filing periods.
  solution: California's tax and fee agency contracted SymSoft Solutions for a year to deploy a generative-AI tool trained on the department's manuals and guides. The tool generates potential responses that an agent can give to the taxpayer.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: TAXNOTESTALK-2025
  prerequisites:
    - Agency reference materials as the training and grounding base.
  risks_and_guardrails:
    - As of the July 2025 episode, the reporter understood the tool was not yet used in real time for taxpayer questions.
    - Critics cited in landscape material note that a taxpayer may only be able to challenge wrong AI advice if it was given in writing. That point is from a search result and was not opened.
  human_checkpoints:
    - The agent chooses whether to relay a generated response.
  role_evolution: FTA's chief operating officer expects training to be the main workforce need and says the technology is unlikely to take jobs soon.
  evidence_grade: B
  sources:
    - { ref: TAXNOTESTALK-2025, title: "Artificial Intelligence and State Tax Agencies", publisher: Tax Notes Talk (Tax Analysts), type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/17439828-artificial-intelligence-and-state-tax-agencies", date: 2025-07-04, access: full, locator: "Reporter's introduction on CDTFA and SymSoft; Minnick interview on training" }
  last_reviewed: 2026-10-17
  notes: Piloting as of July 2025. The status in 2026 was not checked.

- id: tax-controversy-12
  title: HMRC Connect analytics with AI-generated target lists for compliance investigations
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [data-reporting, transaction-processing]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: HMRC wants to narrow the tax gap using large data holdings (bank, marketplace, letting-agent, return and, since January 2026, crypto-provider data, per search-result coverage).
  solution: Per Pinsent Masons, HMRC's Connect platform has built up a large data store and HMRC can now use AI more to produce target lists of businesses and individuals to investigate. HMRC's annual report, as described by Pinsent Masons, says AI and advanced data analytics helped protect and record £10 billion of tax in 2025-26.
  outcomes:
    - lever: capacity
      description: HMRC reports AI and advanced analytics helped protect and record £10 billion in 2025-26, within a record £50.2 billion total compliance yield that narrowly missed the £50.4 billion target.
      figure: £10 billion
      measures: "Tax revenue 'protected and recorded' with the help of AI and advanced data analytics in 2025-26, per HMRC's annual report as described by Pinsent Masons. The report itself was not opened, and the attribution method is not stated."
      provenance: self-reported
      source_ref: PINSENT-HMRC-2026
  prerequisites:
    - Long-built data holdings (Connect) and data-sharing arrangements.
  risks_and_guardrails:
    - ICAS reports a freedom-of-information request about HMRC AI use in R&D compliance letters. HMRC told the FT that generative AI was not approved for generating taxpayer letters, but the FT reported suggestions that individual caseworkers might have used it without authorisation, raising confidentiality concerns.
    - ICAS stresses HMRC transparency and safeguards.
  human_checkpoints:
    - Not described in the sources.
  role_evolution: Pinsent Masons experts quoted expect greater scrutiny of sectors that HMRC's risk data emphasise, including construction.
  evidence_grade: B
  sources:
    - { ref: PINSENT-HMRC-2026, title: "UK firms warned following HMRC AI-powered tax crackdown", publisher: Pinsent Masons (Out-Law), type: firm, url: "https://www.pinsentmasons.com/out-law/news/uk-firms-warned-following-hmrc-ai-powered-tax-crackdown", date: 2026-07-14, access: full, locator: "Paragraphs 1-4" }
    - { ref: ICAS-HMRC-2025, title: "HMRC's plans for AI", publisher: ICAS, type: professional-body, url: "https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai", date: 2025-10-29, access: full, locator: "Section 'Potential pitfalls'" }
  last_reviewed: 2026-10-17
  notes: The £10 billion figure is a self-reported HMRC figure reported by a law firm and is a secondary source. The HMRC annual report was not opened, because the search budget ran out before it could be located. The crypto-data detail came from a search summary and is not used as a fact.

- id: tax-controversy-13
  title: Caseworker generative-AI and agentic case management at HMRC (roadmap)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [research-synthesis, transaction-processing]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: HMRC aims to reach at least 90% digital customer interactions by 2030 (about 76% at the time of the roadmap) while reducing the tax gap.
  solution: The HMRC Transformation Roadmap (21 Jul 2025), as summarised by ICAS, lists agentic AI for case management and intelligent automation. It plans to give caseworkers generative-AI systems that summarise case documents and answer queries, and to work with industry on principles for third parties' AI use in software that interacts with HMRC.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: ICAS-HMRC-2025
  prerequisites:
    - Responsible-AI controls aligned with government AI frameworks and HMRC's Charter (roadmap section 6, per ICAS).
  risks_and_guardrails:
    - ICAS flags HMRC's transparency about AI use as a concern, citing the R&D letters FOI episode.
  human_checkpoints:
    - Not described.
  role_evolution: Not described beyond caseworker support.
  evidence_grade: C
  sources:
    - { ref: ICAS-HMRC-2025, title: "HMRC's plans for AI", publisher: ICAS, type: professional-body, url: "https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai", date: 2025-10-29, access: full, locator: "Sections 'The strategic approach' and 'Specific examples from the roadmap'" }
  last_reviewed: 2026-10-17
  notes: The roadmap's gov.uk landing page was opened (publication date 21 July 2025) but the roadmap text itself was read only through the ICAS summary.

- id: tax-controversy-14
  title: Value-based pricing for AI-accelerated controversy and compliance work, against OPR's fee guidance
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: AI shortens research and drafting time. OPR says billing for manual time not actually spent, or double billing for AI-assisted tasks, may violate Circular 230 10.27 (unconscionable fees), depending on the facts, and that savings should be passed on and AI use disclosed in general or specific terms.
  solution: The AICPA has asked the IRS for clarification, saying OPR's language does not appear to allow a value-pricing model and overlooks the cost and risk of implementing the technology.
  outcomes:
    - lever: growth
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: AICPA-CART-2026
  prerequisites:
    - Engagement-letter language on AI use and fee basis (a Werfel framework control for liability and fee disputes).
  risks_and_guardrails:
    - OPR says fee risk depends on facts such as a pattern across clients and the size of billing differentials.
  human_checkpoints:
    - Practitioner decides fee basis and disclosure.
  role_evolution: The pyramid model is discussed in the broader landscape and was not evidenced in the sources for this module.
  evidence_grade: D
  sources:
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework item 2 (10.27(a) Fees)" }
    - { ref: AICPA-CART-2026, title: "AICPA, former IRS commissioner to lead initiative on AI in tax", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/", date: 2026-09-23, access: full, locator: "Paragraph on OPR guidelines and value pricing" }
    - { ref: ACCTODAY-OPR-2026, title: "IRS rolls out AI guidelines for tax pros", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/irs-rolls-out-introductory-ai-guidelines-for-tax-practitioners", date: 2026-06-24, access: full, locator: "Paragraphs on 10.27(a)" }
  last_reviewed: 2026-10-17
  notes: Labelled idea. This is a live dispute, not a deployed model. No firm is named as having changed its fee basis in the sources read. The Bloomberg Tax pricing article named in the landscape file was not re-read.

- id: tax-controversy-15
  title: Risk-register-based due diligence before deploying AI in tax administration or practice
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Tax practitioners and administrators say they do not know which questions to ask to assess their readiness for responsible AI adoption or to vet AI vendors.
  solution: Danny Werfel's framework gives a 20-risk register for tax authorities and a 15-risk register for preparers, an eight-step methodology in Appendix B (frame the deployment, screen for relevant risks, score, tier, controls, vendor questions, phased rollout, monitoring) and sample vendor contract requirements. It was presented at Duke on 26 Mar 2026 and published in The Tax Adviser (31 Aug 2026). The AICPA launched the Council on AI Risk in Tax on 23 Sep 2026 to test and refine it, with participants including the National Association of Enrolled Agents and the Federation of Tax Administrators.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: AICPA-WERFEL-2026
  prerequisites:
    - A named owner for AI governance. Appendix A names an enterprise governance gap as a risk.
  risks_and_guardrails:
    - Per The Tax Adviser and Werfel's text, the framework is a starting point and not a standard. Transparency can lower explainability risk while raising adversarial-manipulation risk.
  human_checkpoints:
    - Tier 1 risks must be addressed before a deployment launches (go/no-go).
  role_evolution: Not addressed.
  evidence_grade: D
  sources:
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation (with appendices)", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08-31, access: full, locator: "Text on registers and the three-tier system; Appendix A (authorities) and Appendix C (preparers)" }
    - { ref: AICPA-CART-2026, title: "AICPA, former IRS commissioner to lead initiative on AI in tax", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/", date: 2026-09-23, access: full, locator: "Paragraphs 1-6" }
    - { ref: DUKE-WERFEL-2026, title: "Werfel Presents Risk Framework for the Use of Artificial Intelligence in Tax Administration and Practice Today at Duke", publisher: TaxProf Blog, type: conference, url: "https://taxprofblog.aals.org/2026/03/26/werfel-presents-risk-framework-for-the-use-of-artificial-intelligence-in-tax-administration-and-practice-today-at-duke/", date: 2026-03-26, access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: Labelled idea. The framework is a published artifact, and no named organization is reported to have applied it. The scenarios in the appendices are illustrative, not incidents.

- id: tax-controversy-16
  title: Pro se taxpayers using AI to prepare Tax Court filings, with court-side guardrails under discussion
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [document-production, client-interaction]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: More than three-quarters of Tax Court cases are pro se. Practitioners expect more self-represented taxpayers to use AI to prepare or respond to filings, with more hallucinated citations, and the court's records contain Social Security and bank-account numbers that must not leak.
  solution: The Tax Court is weighing guardrails through its rules and disciplinary committees. Judge Holmes says a certification that AI was not used may make little sense because legitimate AI uses exist. Former DOJ Tax Division official Gilbert Rothenberg expects the court to let pro se filers remake their arguments before sanctioning. Chief Judge Urda says the judges are working through the topic and that internal training continues.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: independent
      source_ref: BLOOMBERG-TAXCTAI-2026
  prerequisites:
    - Court rules or standing orders. None had been adopted in the sources read.
  risks_and_guardrails:
    - Privacy of taxpayer information in court records (Holmes).
    - IRC 6673 penalty exposure for frivolous or groundless arguments (up to $25,000).
  human_checkpoints:
    - Judges and clerks review filings. Judge Holmes says the court is "feeling" its way.
  role_evolution: Rothenberg says AI misuse may add work for clerks.
  evidence_grade: D
  sources:
    - { ref: BLOOMBERG-TAXCTAI-2026, title: "Tax Court Navigates AI Misuse Rules for Self-Represented Filers", publisher: Bloomberg Law / Bloomberg Tax, type: press, url: "https://news.bloomberglaw.com/insurance/tax-court-navigates-ai-misuse-rules-for-self-represented-filers", date: 2026-03-20, access: full, locator: "Sections 'Feeling Our Way' and 'Protecting Taxpayers'" }
    - { ref: NTT-URDA-2026, title: "Tax Court Chief Judge Talks AI and Transparency", publisher: Tax Notes Talk (Tax Analysts), type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/18795544-tax-court-chief-judge-talks-ai-and-transparency", date: 2026-03-06, access: full, locator: "Transcript: closing exchange on generative AI and training" }
    - { ref: MC-JORDAN-2026, title: "Katherine Jordan Quoted on Emerging AI Issues in U.S. Tax Court Filings in Tax Notes", publisher: Miller & Chevalier, type: firm, url: "https://www.millerchevalier.com/publication/katherine-jordan-quoted-emerging-ai-issues-us-tax-court-filings-tax-notes", date: 2026-03-23, access: full, locator: "Summary paragraph (headline: 'Attorneys Anticipate More IRS Use of AI in Tax Court Filings')" }
  last_reviewed: 2026-10-17
  notes: Labelled idea. The expectation of growing pro se AI use is practitioners' forecast, with no measured prevalence in the sources.

- id: tax-controversy-17
  title: Generative-AI drafting of information document requests and examination reports by IRS revenue agents
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Revenue agents have heavy routine drafting and data-organisation work, and the IRS has fewer agents.
  solution: EisnerAmper reports that revenue agents are beginning to have access to generative-AI programmes for routine drafting such as IDRs and exam reports, with agents reviewing and finalising, and for data integration. It also reports that the IRS aims to run real-time AI checks at filing so taxpayers can correct issues before an amended return or full audit.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: EISNER-IRSAI-2026
  prerequisites:
    - Treasury- or IRS-approved GenAI products (IRM 10.24.1 prohibits unapproved tools and requires direct human review of outputs).
  risks_and_guardrails:
    - IRM 10.24.1.7.2 prohibits entering taxpayer information into unapproved AI systems and requires users to disclose AI-assisted content as appropriate.
    - A hallucinated IRS citation in Khoja shows the failure mode.
  human_checkpoints:
    - Agents review and finalise drafts (per EisnerAmper). The IRM requires direct human review of AI outputs used in government business.
  role_evolution: EisnerAmper says agents can focus on complex areas of the audit.
  evidence_grade: C
  sources:
    - { ref: EISNER-IRSAI-2026, title: "AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services", publisher: EisnerAmper, type: firm, url: "https://eisneramper.com/insights/tax/ai-irs-transforming-0126", date: 2026-01-27, access: full, locator: "Sections 'AI in Audits' and 'AI in Fraud Detection'" }
    - { ref: IRM-10-24-1, title: "IRM 10.24.1 IRS Policy for Artificial Intelligence (AI) Governance", publisher: Internal Revenue Service, type: regulator, url: "https://www.irs.gov/irm/part10/irm_10-024-001r", date: 2026-02-10, access: full, locator: "10.24.1.7.2 Prohibited Uses of GenAI" }
  last_reviewed: 2026-10-17
  notes: The IRS description is a practitioner firm's secondary account. No IRS source read confirms this use. The FedScoop inventory story lists IRS GenAI uses (a service-desk ticket tool, an employee-question NLP tool) and does not list exam drafting. The 2024 RFI for filing-time AI checks is older than the review window.

- id: tax-controversy-18
  title: Authority nudges, anomaly flags and AI-triaged correspondence at filing (ATO, Austria, France, Singapore, per OECD)
  archetype: tax
  module: controversy
  function: customer-service
  work_types: [transaction-processing, client-interaction]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Tax authorities hold large datasets and want to reduce errors and disputes before they occur.
  solution: Grant Thornton Ireland, summarising the OECD's Governing with Artificial Intelligence (Sep 2025), reports that Australia's tax office used real-time analytics to flag anomalies, Austria's predictive analytics centre found irregularities, Singapore's multilingual chatbot reduced call-centre inquiries, and France uses AI to triage taxpayer emails and draft replies that staff validate. It says France requires human validation and South Korea routes sensitive chatbot queries to staff.
  outcomes:
    - lever: cost
      description: Australia's flags generated close to AUD 80 million in revenue in one year. Austria's centre uncovered irregularities worth €185 million. Singapore's chatbot halved call-centre inquiries.
      figure: "about AUD 80 million; €185 million; 50% fewer call-centre inquiries"
      measures: "ATO: revenue generated from real-time analytics flags across more than 600,000 taxpayer interactions in one year. Austria: value of irregularities uncovered across income, corporate, VAT and customs taxes. Singapore: call-centre inquiries halved after the Ask Jamie chatbot. All as summarised by Grant Thornton Ireland from the OECD report, which was not opened."
      provenance: self-reported
      source_ref: GT-IE-OECD-2025
  prerequisites:
    - Anonymised training data, human validation and bias and leakage audits, per the same summary.
  risks_and_guardrails:
    - The summary says taxpayers should be able to understand and contest AI-driven decisions.
  human_checkpoints:
    - Human validation of AI-drafted communications (France); routing of sensitive queries to staff (South Korea).
  role_evolution: The summary suggests tax inspectors could become AI-augmented analysts. This is a forecast and not a measured change.
  evidence_grade: C
  sources:
    - { ref: GT-IE-OECD-2025, title: "Governing with AI: The new face of tax authorities", publisher: Grant Thornton Ireland, type: firm, url: "https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/", date: 2025-09-19, access: full, locator: "Sections 'Detecting tax fraud with algorithms', 'Personalised and proactive taxpayer services', 'The trust factor'" }
  last_reviewed: 2026-10-17
  notes: Graded C because the figures are second-hand from the OECD report, which was not opened. The OECD primary should be checked before any figure is reused.
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Selection and examination (authority side):**
  - Return and issue selection by DIF and ML models (transaction-processing, data-reporting).
  - Information document requests and exam reports (document-production).
  - Examination of substantiation (review-assurance).
  - Taxpayer-side steps: receive the IDR, gather records, respond, negotiate scope (coordination-scheduling, document-production).
- **Notices and underreporter cases (CP2000, math-error notices):**
  - Intake and triage (transaction-processing).
  - Reading the notice, extracting the issue and deadline (review-assurance).
  - Filing a POA (coordination-scheduling).
  - Drafting the response (document-production).
  - Tracking to resolution (coordination-scheduling).
- **Appeals, Fast Track and ADR:** protest drafting, settlement judgement (expert-judgment). PwC specialists, as reported through NYSSCPA, say Fast Track Settlement has resulted in agreements in roughly 80% of cases within about 100 days. This is a PwC statement and has no AI link.
- **Collection (CDP hearings, installment agreements, liens and levies):** automated notices and chatbot or voicebot self-service (transaction-processing, client-interaction), plus practitioner intervention at notice stages (expert-judgment).
- **Litigation (Tax Court, refund suits):** authority research and brief drafting (research-synthesis, document-production), verification (review-assurance).
- **Practice governance:** engagement letters, billing, confidentiality, privilege and AI policy (review-assurance).
- **Authority governance:** AI inventories, impact assessments, high-impact designation, waivers and monitoring under IRM 10.24.1 (review-assurance).

### Common pain points

- **Asymmetric speed.** Flagging and notices are automated and fast, while human resolution is slow and unevenly available. Tax Notes reporters call this an asymmetry (NTT-BIAS-2026), and Accounting Today's author reports longer resolution cycles (ACCTODAY-2026). TAS says reduced staffing may leave issues unresolved or push taxpayers to self-service (NTA-AR-2025).
- **Opacity of selection criteria.** The IRS does not publish them, so practitioners cannot see why a return was flagged (ACCTODAY-2026).
- **Non-existent authorities in filings,** by taxpayer counsel (*Clinco*) and by the IRS (*Khoja*).
- **Silent failure.** An AI agent told a TEI attendee it could not open the uploaded file and had been telling them what they wanted to hear (TEI-TAXTECH-2026).
- **Fee uncertainty** under OPR's §10.27 reading (IRS-OPR-2026, AICPA-CART-2026).
- **Privilege uncertainty** when clients use consumer AI (MOFO-HEPPNER-2026).
- **IRS inventory quality.** GAO found over 25% of IRS AI use cases lacked information on agency benefit and that contracted criminal-case tools were missing from the inventory (GAO-2026).

### Metrics and benchmarks

| Metric | Value | Measures | Source | Provenance |
|---|---|---|---|---|
| IRS active AI use cases | 126 (June 2025), up from 10 (Aug 2022); 65 withheld as sensitive or exempt R&D; 61% (77 of 126) in development | Use cases in the IRS inventory, per GAO | GAO-2026, What GAO Found | independent |
| IRS use cases in Treasury's public inventory | IRS 61 (up from 49); Treasury 129 (up from 54) | Treasury AI use case inventory (a different scope from GAO's 126) | TREAS-AIINV-2026 | self-reported |
| NTA's count | "over 65" AI projects | A different count again; the report does not define it | NTA-AR-2025, Preface (pdf p. 27) | independent |
| IRS headcount | Flat at about 74,000 across 2026 after losing more than a quarter of staff in 2025 | IRS CHCO statement | IRS-AIFIRST-2026 | self-reported |
| IRS compliance rate | About 85% now; CEO envisions mid-90s in five years | Voluntary compliance rate, as stated | IRS-AIFIRST-2026 | self-reported |
| Amended returns | 12-16 weeks to under 3 days (subset of about 5 million a year) | CIO's statement | IRS-AIFIRST-2026 | self-reported |
| Audit no-change rate, filers under $50,000 | FY2025 almost half FY2024, which was under half FY2023; no-response up more than 10 points | TAS | NTA-AR-2025, pdf p. 27 | independent |
| IRS chatbot usefulness | 80% negative (Jan-Aug 2025); international chatbot 11.5% helpful (23 of 200) | Yes/no end-of-session question | NTA-AR-2025, pdf pp. 74, 147 | independent |
| Chatbot installment agreements | +68% chatbot IAs; -7% total IAs, FY2024 to FY2025 | TAS | NTA-AR-2025 | independent |
| Archie rollout | Archie available to about 12,000 CSRs | TAS | NTA-OBJ-2026, pdf p. 32 | independent |
| Tax Court hallucinated citations | Fewer than a dozen instances seen by Judge Holmes; no sanctions by him | Judge's count, March 2026 | BLOOMBERG-TAXCTAI-2026 | independent |
| Tax Court pro se share | More than three-quarters of cases | Judge Holmes's statement | BLOOMBERG-TAXCTAI-2026 | independent |
| Tax gap context | $688 billion for TY2021, of which $542 billion (79%) from underreporting | TIGTA's citation of IRS estimates | TIGTA-2025, Highlights | independent |
| HMRC | £10 billion protected or recorded with AI and analytics; £50.2 billion compliance yield, 4.6% growth vs 15% and 23% in prior years | HMRC annual report as described by Pinsent Masons | PINSENT-HMRC-2026 | self-reported (secondary) |
| In-house tax ownership of AI | Two hands of more than 50 when asked whether the tax function owns AI implementation | A room poll at TEI Tax Tech Seminar, April 2026 | TEI-TAXTECH-2026 | self-reported |

**Quality evidence.** There is no independent measurement of error rates, override rates, parallel-run results or inspection outcomes for practitioner AI in controversy work. The nearest items are the judge's count of hallucinated citations, TIGTA's finding that the IRS cannot show its selection models beat earlier methods, GAO's 2024 finding of potential bias in the Dependent Database, and TAS's chatbot measures. No source publishes a rate at which IRS personnel override AI-based selection.

**Source reliability notes.**
- The Accounting Today opinion piece (ACCTODAY-2026) says GAO found the IRS lacks controls to document, validate and explain its models. The GAO highlights page does not say this; it covers skills, inventory quality and strategic management. The piece also cites TIGTA's FY2026 challenges report figures (101 projects as of April 2025) that were not verified.
- Its description of IRM 10.24.1 as setting "mandatory human review" and "documentation requirements for AI-generated referrals" paraphrases the policy loosely. The IRM text lists human oversight, intervention and accountability and consistent remedies or appeals among the minimum practices for high-impact AI.
- The Beancount blog repeats the IRM claim and adds unsourced industry ratios.
- Both are used only for practitioner opinion and not as fact sources.

### Guardrails and regulatory points

- **OPR Alert 2026-19 (24 Jun 2026)** applies Circular 230 §§10.22 (due diligence), 10.27(a) (fees), 10.35 (competence), 10.36 (firm procedures), 10.37 (written advice), 10.51(a)(15) and IRC §§6713 and 7216. It treats AI text as a draft, requires enterprise-approved tools for client data, and notes that Deloitte Australia reportedly agreed to a partial refund after a government report contained apparently AI-generated errors (IRS-OPR-2026).
- **UK PCRT guidance (19 Jan 2026)** applies the five fundamental ethical principles of the bodies' codes (the podcast walks through integrity, objectivity and confidentiality among them). ICAEW's regulatory-policy director says members were nervous about falling foul of body expectations and that objectivity (automation bias, biased outputs) is a key principle in this context (ICAEW-POD-2026).
- **IRM 10.24.1** (effective 10 Feb 2026, revised 10 Aug 2026) lists AI that informs or influences audit selection as presumed high-impact. High-impact AI requires pre-deployment testing, an impact assessment, monitoring, human training, human oversight, consistent remedies or appeals and consultation. Waivers need the Treasury Chief AI Officer. IRS users may not enter taxpayer information into unapproved AI, must review AI outputs directly and should disclose AI-assisted content (IRM-10-24-1).
- **GAO-26-107522** makes eight recommendations (skills plan, inventory quality assurance, communications, contracts, collaboration, strategic alignment, performance metrics). The IRS agreed with all; 180-day letters are expected in fall 2026 (GAO-2026).
- **Werfel framework / CART:** 20 authority risks and 15 preparer risks, with tiering. CART meets through the year (AICPA-CART-2026).
- **Courts:** IRC §6673 is the available penalty; no Tax Court AI certification rule exists. The Tax Court has a disciplinary committee and a rules committee (BLOOMBERG-TAXCTAI-2026).
- **Privilege:** *Heppner* (S.D.N.Y., 17 Feb 2026) (MOFO-HEPPNER-2026).

### Frontier signals

| Date | Signal | Source |
|---|---|---|
| 2025-11-21 | IRS announced Agentforce for Chief Counsel, TAS and Appeals; counsel says to compete "head-to-head" with law firms | IRS-AGENTFORCE-2025 |
| 2025-12-23 | A former SB/SE commissioner writes that the IRS is emphasising collection over audits (which are expected to decline) and expects AI to shorten notice-redesign cycles from months or years to days or weeks (opinion) | BLOOMBERG-COLLECTION-2025 |
| 2026-03 | Tax Court weighing guardrails; Chief Judge Urda says the topic is being worked through | BLOOMBERG-TAXCTAI-2026, NTT-URDA-2026 |
| 2026-03-26 | Werfel presents the framework at Duke | DUKE-WERFEL-2026 |
| 2026-04 | TEI Tax Tech: capability question "effectively settled"; ownership, silent failure and training are the hard problems | TEI-TAXTECH-2026 |
| 2026-06-24 | OPR Alert 2026-19 | IRS-OPR-2026 |
| 2026-09-23 | CART launched; AICPA seeks IRS clarification on value pricing | AICPA-CART-2026 |
| 2026-10-02 | IRS CEO sets "AI-first IRS" with a mid-90s compliance aspiration | IRS-AIFIRST-2026 |
| Fall 2026 | IRS responses to GAO recommendations due | GAO-2026 |
| 2026-10-18 | TEI annual conference starts (no recaps yet) | landscape-tax.md (TEI-ANNUAL-2026) |

### Workforce and role effects

- **IRS:** CEO says AI is not designed to eliminate jobs and flat headcount is 74,000 (IRS-AIFIRST-2026). GAO reports the loss of 63 AI-related staff in one analytics group and no skills plan (GAO-2026). An IRS counsel says staff must adopt or leave (IRS-AGENTFORCE-2025). Werfel's register flags workforce and expertise erosion as a risk.
- **Practitioners:** the commentary (ACCTODAY-2026, NYSSCPA-PWCWEBCAST-2026) shifts the role toward documentation readiness, notice workflows and year-round risk advice. Corporate tax: Michael Sala argues AI cannot hold culpability, so it will not shrink corporate tax teams much (SALA-TAXNOTES-2026).
- **Tax Court:** Rothenberg expects extra clerk work if pro se AI misuse grows.

### Objections and concerns practitioners raise

- Hallucinated authorities and the lack of a Tax Court Rule 11 equivalent.
- Silent, polite failure that evades review, and unclear ownership of AI in tax departments (TEI-TAXTECH-2026).
- Asymmetry between automated flagging and the ability to contest (NTT-BIAS-2026).
- Bias and opacity in audit selection, including whether older rule-based systems count as AI (NTT-BIAS-2026, FEDSCOOP-GAOBIAS-2024).
- Fee rules that seem to block value pricing (AICPA-CART-2026).
- Privilege loss when clients use consumer AI (MOFO-HEPPNER-2026).
- Confidentiality across clients and IRC §7216 exposure (IRS-OPR-2026).
- Unauthorised use by tax-authority staff (the HMRC R&D letters episode, ICAS-HMRC-2025).
- Chatbot quality (NTA-AR-2025).

### Interview probes

1. When an IRS or state notice lands, which steps from intake to signed response involve an AI tool, who reviews each step, and where have you caught a wrong deadline, amount or issue?
2. How do you document AI use and verification in controversy files (engagement letter, privilege, billing under §10.27), and has the AICPA/OPR fee debate changed how you price controversy work?
3. Since 2025, where have you seen resolution time lengthen (POA processing, exam assignment, Appeals, collection) and what have you changed in client expectations or staffing?
4. Who owns citation and authority verification for protests, briefs and memos, and have you seen a fabricated or misquoted authority from your side, opposing counsel or the IRS?
5. What would you want the IRS to disclose about AI-driven selection, and what do you tell clients today about it?

---

## 4. Routed to other modules

- **transfer-pricing:** the IRS LB&I treaty and transfer pricing director said in July 2026 that AI can support but not replace judgement and that the IRS wants to see formulas (IRS-LBI-TP-2026 in the landscape file; not re-read here). PwC specialists named transfer pricing, intercompany financing, economic substance and certain credits as exam focus areas, as reported through NYSSCPA-PWCWEBCAST-2026.
- **research-advisory:** hallucinated research (the OPR §10.37 reliance rule, *Clinco*), the AICPA SSTS §1.4 "reliance on tools" standard, and Sala's argument about corporate tax-team size (SALA-TAXNOTES-2026).
- **tax-data-technology:** TEI Tax Tech themes of silent hallucination, governance vacuums and rising token costs (TEI-TAXTECH-2026), and the ownership poll.
- **compliance:** HMRC R&D compliance-letter concerns (ICAS-HMRC-2025), and the OPR fee guidance for return preparation.
- **international-pillar-two and indirect-tax:** none found in the sources read.

---

## 5. Sources

Access is `full` unless noted. Every source in this list was opened and read, in part for the long reports.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 |
| IRM-10-24-1 | IRM 10.24.1 IRS Policy for Artificial Intelligence (AI) Governance | Internal Revenue Service | regulator | https://www.irs.gov/irm/part10/irm_10-024-001r | 2026-02-10 (revised 2026-08-10) |
| GAO-2026 | Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522) | US GAO | regulator | https://www.gao.gov/products/gao-26-107522 | 2026-03-24 |
| TIGTA-2025 | The IRS Could Leverage Examination Results in AI Examination Case Selection Models (2025-308-022) | TIGTA | regulator | https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf | 2025-05-19 |
| NTA-AR-2025 | National Taxpayer Advocate 2025 Annual Report to Congress | Taxpayer Advocate Service | regulator | https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/01/ARC_Publication-2104_2025_Web.pdf | 2026-01 |
| NTA-OBJ-2026 | National Taxpayer Advocate FY2027 Objectives Report to Congress | Taxpayer Advocate Service | regulator | https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf | 2026-06 |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 |
| BLOOMBERG-TAXCTAI-2026 | Tax Court Navigates AI Misuse Rules for Self-Represented Filers | Bloomberg Law / Bloomberg Tax | press | https://news.bloomberglaw.com/insurance/tax-court-navigates-ai-misuse-rules-for-self-represented-filers | 2026-03-20 |
| MC-JORDAN-2026 | Katherine Jordan Quoted on Emerging AI Issues in U.S. Tax Court Filings in Tax Notes | Miller & Chevalier | firm | https://www.millerchevalier.com/publication/katherine-jordan-quoted-emerging-ai-issues-us-tax-court-filings-tax-notes | 2026-03-23 |
| NTT-URDA-2026 | Tax Court Chief Judge Talks AI and Transparency | Tax Notes Talk | podcast | https://taxnotestalk.taxnotes.com/124942/episodes/18795544-tax-court-chief-judge-talks-ai-and-transparency | 2026-03-06 |
| NTT-BIAS-2026 | How AI Bias Affects State Audit Selection | Tax Notes Talk | podcast | https://taxnotestalk.taxnotes.com/124942/episodes/19216367-how-ai-bias-affects-state-audit-selection | 2026-05-22 |
| TAXNOTESTALK-2025 | Artificial Intelligence and State Tax Agencies | Tax Notes Talk | podcast | https://taxnotestalk.taxnotes.com/124942/episodes/17439828-artificial-intelligence-and-state-tax-agencies | 2025-07-04 |
| ICAEW-POD-2026 | How to use AI in tax ethically, and group audit best practice (transcript) | ICAEW Accountancy Insights | podcast | https://www.icaew.com/insights/podcast/accountancy-insights/how-to-use-ai-in-tax-ethically-and-group-audit-best-practice/transcript | 2026-02-04 |
| BLOOMBERG-COLLECTION-2025 | IRS Modernizes Collection: What's Next for Tax Practitioners | Bloomberg Tax (Tax Management Memo) | press | https://news.bloombergtax.com/tax-management-memo/irs-modernizes-collection-whats-next-for-tax-practitioners | 2025-12-23 |
| BLOOMBERG-DILLON-2026 | Five Questions With Miller & Chevalier Tax Attorney Sheri Dillon | Bloomberg Tax Daily Tax Report | press | https://news.bloombergtax.com/daily-tax-report/five-questions-with-miller-chevalier-tax-attorney-sheri-dillon | 2026-10-09 |
| ACCTODAY-2026 | What does an AI-driven IRS mean for small accounting firms? | Accounting Today | press | https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms | 2026-07-02 |
| ACCTODAY-OPR-2026 | IRS rolls out AI guidelines for tax pros | Accounting Today | press | https://www.accountingtoday.com/news/irs-rolls-out-introductory-ai-guidelines-for-tax-practitioners | 2026-06-24 |
| IRS-AIFIRST-2026 | Tax chief pushes 'AI-first IRS' to get more out of agency's workforce | Nextgov/FCW | press | https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/ | 2026-10-02 |
| TREAS-AIINV-2026 | IRS ramps up AI use amid staff cuts, Treasury inventory shows | FedScoop | press | https://fedscoop.com/treasury-irs-ai-use-case-inventory/ | 2026-01-29 |
| IRS-AGENTFORCE-2025 | Exclusive: IRS deploys AI agents | Axios | press | https://www.axios.com/2025/11/21/irs-deploys-ai-agents | 2025-11-21 |
| FEDSCOOP-GAOBIAS-2024 | IRS's AI system to flag returns for audit may include unintended bias, report finds | FedScoop | press | https://fedscoop.com/irs-ai-systems-bias-audits-racial-disparities-gao-report/ | 2024-05-23 |
| EISNER-IRSAI-2026 | AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services | EisnerAmper | firm | https://eisneramper.com/insights/tax/ai-irs-transforming-0126 | 2026-01-27 |
| MOFO-HEPPNER-2026 | Privilege in the Age of AI: SDNY Holds AI-Generated Documents Are Not Privileged | Morrison Foerster | firm | https://www.mofo.com/resources/insights/260220-privilege-in-the-age-of-ai-sdny-holds | 2026-02-20 |
| PINSENT-HMRC-2026 | UK firms warned following HMRC AI-powered tax crackdown | Pinsent Masons (Out-Law) | firm | https://www.pinsentmasons.com/out-law/news/uk-firms-warned-following-hmrc-ai-powered-tax-crackdown | 2026-07-14 |
| GT-IE-OECD-2025 | Governing with AI: The new face of tax authorities | Grant Thornton Ireland | firm | https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/ | 2025-09-19 |
| AICPA-WERFEL-2026 | A risk framework for AI use in tax administration and preparation (and appendices) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ ; appendices https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-08-31 |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 |
| NYSSCPA-PWCWEBCAST-2026 | IRS Expands AI-Driven Enforcement While Adding New Taxpayer Relief | NYSSCPA | professional-body | https://nysscpa.org/news/8725456-irs-expands-ai-driven-enforcement-while-adding-new-taxpayer-relief-2026-08-10 | 2026-08-10 (from URL) |
| ICAS-HMRC-2025 | HMRC's plans for AI | ICAS | professional-body | https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai | 2025-10-29 |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (abstract on TaxProf Blog) | Tax Notes State / TaxProf Blog | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 (page header) |
| TEI-MIDYEAR-2026 | TEI Midyear Conference 2026 at-a-glance agenda | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03-15 |
| DUKE-WERFEL-2026 | Werfel Presents Risk Framework ... Today at Duke | TaxProf Blog (Duke Tax Policy Seminar) | conference | https://taxprofblog.aals.org/2026/03/26/werfel-presents-risk-framework-for-the-use-of-artificial-intelligence-in-tax-administration-and-practice-today-at-duke/ | 2026-03-26 |
| BTAX-FORUM-2026 | Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk (press release) | Bloomberg Tax | conference | https://pro.bloombergtax.com/?p=17345 | 2026-06-10 |
| MILLER-CLE-2025 | Leveraging AI, Big Data, IRS Online Services & Emerging Technology for Tax Controversy Professionals (event page) | Miller & Chevalier | conference | https://www.millerchevalier.com/event/leveraging-ai-big-data-irs-online-services-emerging-technology-tax-controversy-professionals | 2025-06-25 |
| WK-NOTICES-2026 | How to respond to IRS notices with a clear, structured workflow | Wolters Kluwer Tax & Accounting | vendor | https://www.wolterskluwer.com/en/expert-insights/how-to-respond-to-irs-notices-with-a-clear-structured-workflow | 2026-07-06 |
| BEANCOUNT-IRM-2026 | Audited by an Algorithm: What the IRS's New AI Governance Policy Means for Your Small Business | Beancount.io | vendor | https://beancount.io/blog/2026/07/11/audited-by-algorithm-irs-ai-audit-selection-irm-10-24-1-guide | 2026-07-11 |

**Count: 37 sources.** By type: regulator 6, press 10, firm 5, podcast 4, professional-body 4, conference 5, academic 1, vendor 2 (one source, FEDSCOOP-GAOBIAS-2024, is a 2024 foundation item). Two conference entries (BTAX-FORUM-2026, MILLER-CLE-2025) are announcements with panel titles only, and are not used for claims in the use cases.

---

## 6. Gaps

- **Practitioner community discussion.** Reddit (r/taxpros) blocked both direct and mirror access, and TaxProTalk, TEI chapters and the ABA Tax Section task-force webinars are closed or login-gated. The discourse here is therefore from conferences, press, podcasts, firm commentary and professional-body publications, and it under-represents day-to-day practitioner sentiment.
- **Search budget exhausted.** Two planned lookups were not completed: the Khoja v. Commissioner order or hearing record (known only through the Bloomberg Law article), and HMRC's 2025-26 annual report (known only through Pinsent Masons). Neither was verified against a primary.
- **Paywalled or blocked:** the Tax Notes articles behind the Miller & Chevalier item and "Unwatched" (14 Apr 2026), Law360 and Bloomberg articles beyond their opening, Crowell, Morgan Lewis (PLI Tax Controversy 2026), BTCPA and Foster pages (Cloudflare blocks), the ABA Tax Section pages, the PwC webcast itself, and the Thomson Reuters "Clarity on Tech" audio.
- **Not yet available:** TEI Annual Conference (18–21 Oct 2026), CCH Connections (25–28 Oct 2026) and IFA Melbourne recaps. Re-check in November 2026.
- **Not found:**
  - Independent error, override or parallel-run data for practitioner AI in controversy.
  - Named firm case studies of AI-assisted notice response, protest drafting or Appeals preparation with metrics.
  - Any IRS or Treasury source confirming revenue-agent GenAI drafting.
  - Any Tax Court rule or standing order on AI.
  - Any disciplinary action under Circular 230 for AI misuse.
  - Insurer or malpractice-carrier discussion.
  - Evidence from non-US/UK/Australian controversy practice.
  - Whether IRS Appeals bypass or notice-of-deficiency trends are changing. One search summary mentioned this from a blog I could not open, so it is not used.
- **Unverified items.** The OECD figures (via Grant Thornton Ireland); the "TIGTA FY2026 challenges" statistics repeated by Accounting Today; GAO-24-106449 (cited by Accounting Today and not opened, though its findings are reported by FedScoop).
- **Date handling.** The TEI recap's date (2026-05-04) is read from the page header, and the NYSSCPA date from its URL slug. The NTA 2025 annual report date is given as 2026-01 because the exact release date came only from a search summary.
