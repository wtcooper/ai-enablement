# Nonprofit and government audits (with Form 990 and UBI work): combined deep dive

Archetype: assurance (mid-market extension). Module: nonprofit-government. Angle: combined (practice, discourse, governance and evidence). Researched 2026-10-21. Public sources only.

## 1. Summary

- **Evidence is thin and mostly vendor-authored.** The one real cluster of named practice is Thomson Reuters customer material: three small nonprofit-focused audit firms (Sam Brown CPA, Wells CPA, The Forde Firm), a small Oklahoma nonprofit and government audit firm (Robert St. Pierre, CPA), and Plante Moran's pilot [TR-NPCASE-2026; TR-STPIERRE-2026; TR-PLANTEMORAN-2025]. Every figure is a recollection or a vendor-published summary. No error rate, override rate, parallel run or inspection finding for any AI use in a single audit, a Yellow Book audit, a nonprofit financial statement audit, a Form 990 or a Form 990-T was found. No AI finding from AICPA peer review, the Governmental Audit Quality Center (GAQC) or the Government Accountability Office (GAO) on auditors' own use was found.
- **The sharpest new fact is on the counterparty side.** On 2026-05-21 HHS announced AERO, which it says is "powered by" AI analytical tools reviewing at least five years of single audit information across all 50 states, and which also examines whether audits are conducted with sufficient rigor [HHS-AERO-2026]. Auditors' past reports are now data for agency analytics. Cherry Bekaert reads it as single audit compliance turning from a year-end exercise into a continuous risk issue tied to funding [CBH-AERO-2026; see also FELDESMAN-AERO-2026].
- **The work itself is being made heavier by rule, not by AI.** The 2026 AICPA GAS/SA Guide moves the Appendix B single-audit content into Part II and raises expectations on risk assessment, IT testing and minimum sample sizes [BDO-GASSA-2026]. The 2026 Compliance Supplement was still unreleased as of the GAQC post of 2026-10-08 [GAQC-DEV-2026]. Staffing and margins are the stated reasons small firms adopt AI [TR-NPCASE-2026].
- **What AI is used for in practice is narrow and document-heavy:** reading board minutes, agreements and handbooks; selecting samples; technical research; footnote tie-out; first-draft risk assessment. Compliance testing of the federal program requirements themselves (eligibility, allowable costs, subrecipient monitoring, FFATA reporting) has no named AI deployment in public sources.
- **Form 990 and UBI: almost nothing.** The only AI feature found is an AI error check and chatbot in one e-file product [TAX990-2026]. AICPA's 990-T workshop description has no AI content [AICPA-NFPWORKSHOPS-2026]. IRS-side AI for exempt-organization referrals is a 2024 secondary report [EY-TEGE-2024].
- **Design question for the integrator.** The brief folds nonprofit tax into this assurance module. Nothing found argues against that, but the tax guardrails (Circular 230, section 7216) sit in the tax archetype, so cross-link rather than restate.
- **Counts.** 15 use cases: 0 grade A, 9 grade B, 4 grade C, 2 grade D. 40 source rows (38 distinct documents opened and read, one repost row, one search-only) across 10 of the 12 source types; no podcast or community source was reachable.

## 2. Use cases

Firm type is stated in each entry's `notes`. "Small firm" means a local or regional practice with a nonprofit or government niche; "national firm" means a top-100 firm.

```yaml
- id: assurance-nonprofit-government-01
  title: Board and governing-body minutes review for audit-relevant events
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Minutes of boards, councils and committees are long, unstructured and must be read for debt, grants, related-party items, contract commitments and policy changes that change audit procedures. The reading is manual and easy to skim."
  solution: "Staff upload a year of minutes to an audit AI assistant. A saved template returns a structured, dated summary of items an auditor would ask about. The firm tunes the template prompt (chronological order, short bullets, 'N/A' when missing, named date range). A person reads the flagged items against the minutes."
  outcomes:
    - {lever: speed, description: "Board minute and contract reviews reported as taking about 5 minutes instead of about 1 hour", figure: "1 hour to 5 minutes", measures: "Time per board-minute or contract review, as reported by Harris, Hardy & Johnstone (a mid-sized CPA firm serving commercial clients, not nonprofit-specific); not a tracked metric", provenance: vendor-published, source_ref: TR-SCALING-2026}
    - {lever: quality, description: "A nonprofit-focused firm owner says a minutes review surfaced debt a client had not mentioned", figure: "none (one anecdote)", measures: "One instance recounted by the firm owner; no count of reviews or misses", provenance: vendor-published, source_ref: TR-NPCASE-2026}
  prerequisites:
    - "Minutes available as documents the tool can read"
    - "An approved audit AI tool; all three nonprofit-focused firms already used the vendor's engagement and methodology products before adding the AI layer [TR-NPCASE-2026]"
    - "Template and prompt tuning: one small governmental and nonprofit firm used the stock template on every engagement and found it did not summarize until customized [TR-STPIERRE-2026]"
  risks_and_guardrails:
    - "Output quality depended on prompt design; the St. Pierre firm reported too many questions, irrelevant detail, repetitive summaries and no chronological order in the stock template [TR-STPIERRE-2026]"
    - "AICPA practice aid: the auditor remains responsible for supervision, review and conclusions when using AI tools [AICPA-PA-2026]"
    - "Donor and personal data in minutes raises the confidentiality worry practitioners cite for nonprofit work [AICPA-NFPAI-2026]"
  human_checkpoints:
    - "Auditor reads each flagged item against the minutes and decides whether it changes procedures"
  role_evolution: "Staff spend less time reading and more time deciding what a flagged item means for the audit. Forde says the tool lets staff act without a senior's involvement [TR-NPCASE-2026]."
  evidence_grade: B
  sources:
    - {ref: TR-SCALING-2026, title: "Scaling audit practices with AI: 3 real-world case studies", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/blog/scaling-your-audit-practice-with-ai-3-real-world-cocounsel-audit-case-studies/", date: 2026-06-16, access: full, locator: "Case 2 (Harris, Hardy & Johnstone), measurable results"}
    - {ref: TR-NPCASE-2026, title: "Three nonprofit-focused firms modernize audits with CoCounsel and Audit Intelligence", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/three-nonprofit-focused-firms-modernize-audits-with-thomson-reuters-audit-intelligence-and-cocounsel", date: 2026-04-10, access: full, locator: "Outcome section (Forde board-minutes example); Solution section"}
    - {ref: TR-STPIERRE-2026, title: "Modernizing nonprofit and government audits with CoCounsel Audit", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit", date: 2026-03-09, access: full, locator: "Challenges and solutions: governmental entities board minutes template"}
    - {ref: AICPA-PA-2026, title: "AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing", publisher: "AICPA & CIMA", type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "Use of AI-related technological resources by audit firms"}
    - {ref: AICPA-NFPAI-2026, title: "The untapped potential of AI in not-for-profit accounting", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/professional-insights/article/the-untapped-potential-of-ai-in-not-for-profit-accounting", date: 2026-09-10, access: full, locator: "Section on PII and data governance"}
  last_reviewed: 2026-10-21
  notes: "Firms: three small nonprofit-focused firms (Sam Brown CPA, Troy OH; Wells CPA, Columbus OH; The Forde Firm, Jacksonville FL); a small governmental and nonprofit firm (Robert St. Pierre, CPA, Stilwell OK, about 80 audits a year); a mid-sized commercial firm (Harris, Hardy & Johnstone). All outcome text is vendor-published customer material. The hour-to-five-minutes figure is not from a nonprofit or government engagement."

- id: assurance-nonprofit-government-02
  title: Population analysis, risk-based sample selection and linked documentation
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Small firms pick samples by hand across disconnected spreadsheets and tools, and then write the documentation peer reviewers expect. Both steps take hours and vary by staff member."
  solution: "An audit analytics module loads the population, splits it into smaller groups by risk, selects a statistically supported sample and writes the linked documentation. The auditor sets the strata and approves the sample. The pattern is population segmentation and sample selection, not whole-population testing."
  outcomes:
    - {lever: speed, description: "A firm owner says hand-picking a sample takes about three hours and the software does it in about five minutes", figure: "3 hours to 5 minutes", measures: "Time to select one sample, recalled by the owner of The Forde Firm; not a tracked metric. The vendor page also shows a '95% faster sample selection' tile derived from this quote", provenance: vendor-published, source_ref: TR-NPCASE-2026}
    - {lever: capacity, description: "Wells CPA says it is down two people on last year with revenue output unchanged", figure: "two fewer staff, same revenue output", measures: "Owner's own comparison with the prior year, as quoted; no baseline hours or revenue given", provenance: vendor-published, source_ref: TR-NPCASE-2026}
    - {lever: quality, description: "The firms say the generated documentation meets the standard and eased peer review; one owner says a peer reviewer then switched to the same vendor", figure: "none published", measures: "Qualitative statements by three firm owners; no peer review result given", provenance: vendor-published, source_ref: TR-NPCASE-2026}
  prerequisites:
    - "Population data (ledger or listing) exported into the tool"
    - "Existing methodology and engagement platform; firms 'layered AI onto workflows' they already used [TR-NPCASE-2026]"
    - "Some statistical sampling literacy; one owner says the tool 'almost tricks the staff into doing statistical sampling' [TR-NPCASE-2026]"
  risks_and_guardrails:
    - "The 2026 AICPA GAS/SA Guide revises suggested minimum sample sizes for control and compliance testing, and expects more granular risk assessment [BDO-GASSA-2026]. No source says any sampling tool has been updated or validated against those revised tables."
    - "AICPA runs a workshop on sampling in a Uniform Guidance compliance audit under Appendix B, so the rules are still being taught [AICPA-NFPWORKSHOPS-2026]"
    - "Peer review of single audits is where documentation is tested: 2 of 11 single audit engagements reviewed in one state's 2025 report were nonconforming [TSCPA-PEERREVIEW-2025]"
  human_checkpoints:
    - "Auditor defines risk strata and approves the sample"
    - "Reviewer inspects the generated documentation, since it is the evidence a peer reviewer reads"
  role_evolution: "Staff get statistical sampling embedded in the workflow without a top-down methodology change [TR-NPCASE-2026]. Owners describe protecting margins without backfilling departures."
  evidence_grade: B
  sources:
    - {ref: TR-NPCASE-2026, title: "Three nonprofit-focused firms modernize audits with CoCounsel and Audit Intelligence", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/three-nonprofit-focused-firms-modernize-audits-with-thomson-reuters-audit-intelligence-and-cocounsel", date: 2026-04-10, access: full, locator: "Key results; Outcome section"}
    - {ref: BDO-GASSA-2026, title: "More scrutiny, more documentation: the impact of the updated AICPA GAS/SA Guide to auditees", publisher: "BDO", type: firm, url: "https://www.bdo.com/insights/industries/nonprofit-education/more-scrutiny-more-documentation-the-impact-of-the-updated-aicpa-gas-sa-guide-to-auditees", date: 2026-10-15, access: full, locator: "Paragraphs on larger sample sizes and control testing"}
    - {ref: AICPA-NFPWORKSHOPS-2026, title: "Pre-conference workshops, AICPA Not-for-Profit Industry Conference (workshop 102)", publisher: "AICPA & CIMA", type: conference, url: "https://events.aicpa-cima.com/nfp/Program/Pre-Conference-Workshops", date: 2026-06-15, access: full, locator: "Workshop 102"}
    - {ref: TSCPA-PEERREVIEW-2025, title: "Annual Report on Peer Review Activities 2025", publisher: "Tennessee Society of CPAs", type: professional-body, url: "https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf", date: 2026-03-31, access: full, locator: "Section II.2.c, nonconforming engagements table"}
  last_reviewed: 2026-10-21
  notes: "Pattern other: population segmentation and sample selection. Small nonprofit-focused firms only. The tool is described as population analysis for audits generally; the sources do not show it applied to the Compliance Supplement sampling tables. The TSCPA figure is one state's report with 11 single audits reviewed; it is context, not a measure of any tool. The workshop page title reads 2027 but the workshop date given (Monday 15 June) matches 2026; treat the date as approximate."

- id: assurance-nonprofit-government-03
  title: Citation-backed technical research on ASC 958, GASB, Uniform Guidance and Yellow Book questions
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Small governmental and nonprofit audit teams answer technical questions by calling another CPA or a specialist, or by searching several libraries. This is slow and depends on who is available."
  solution: "Staff ask an AI research assistant grounded in accounting and audit literature and the firm's own templates and get an answer with citations and follow-up questions. The vendor lists governmental content such as GASB and says users can check Uniform Guidance, major program determination and questioned costs without calling a government audit specialist."
  outcomes:
    - {lever: speed, description: "Most pilot respondents at Plante Moran said the tool was faster than traditional research methods", figure: "91%", measures: "Respondents to an anonymous internal survey of the firm's 140+ pilot participants who reported CoCounsel was faster than traditional methods of research; respondent count not stated on the page", provenance: vendor-published, source_ref: TR-PLANTEMORAN-2025}
    - {lever: speed, description: "A subset reported significant efficiency and time savings in technical research", figure: "62%", measures: "Respondents to the same survey reporting significant efficiency and time savings during technical research", provenance: vendor-published, source_ref: TR-PLANTEMORAN-2025}
    - {lever: capacity, description: "A small governmental and nonprofit firm says it now asks the tool instead of calling another CPA", figure: "none published", measures: "Owner's own description in a vendor case study; no counts", provenance: vendor-published, source_ref: TR-STPIERRE-2026}
  prerequisites:
    - "An approved, secured tool; Plante Moran's case describes new AI security protocols and software controls [TR-PLANTEMORAN-2025]"
    - "Firm templates and methodology loaded so answers match firm practice"
  risks_and_guardrails:
    - "An interviewee in a Thomson Reuters piece says AI systems can still fail in hidden ways and that firms should test systems on their own work [TR-STATEAUDIT-2026]"
    - "AICPA practice aid: firm policies, competence and partner approval of tools [AICPA-PA-2026]"
    - "Under the 2024 Yellow Book a firm must have designed its system of quality management by 2025-12-15 and completed its initial evaluation by 2026-12-15; the FAQ does not mention AI [GAO-YBFAQ-2025]"
  human_checkpoints:
    - "Staff verify citations and apply the guidance to the client's facts; reviewer signs off"
  role_evolution: "Less reliance on a few specialists for routine questions; juniors reach a starting point faster [TR-STPIERRE-2026; TR-PLANTEMORAN-2025]."
  evidence_grade: B
  sources:
    - {ref: TR-PLANTEMORAN-2025, title: "Thomson Reuters CoCounsel at Plante Moran", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/thomson-reuters-cocounsel-at-plante-moran", date: 2025-11-20, access: full, locator: "Key outcomes"}
    - {ref: TR-STPIERRE-2026, title: "Modernizing nonprofit and government audits with CoCounsel Audit", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit", date: 2026-03-09, access: full, locator: "When to use conversations and workspaces; Outcomes"}
    - {ref: TR-COCOUNSEL-2025, title: "CoCounsel Audit & Accounting (product page)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/products/cocounsel-audit-accounting", date: 2025-08-25, access: full, locator: "Industry-specific and governmental audits"}
    - {ref: TR-STATEAUDIT-2026, title: "The state of AI in audit in 2026: seven questions", publisher: "Thomson Reuters Tax & Accounting", type: vendor, url: "https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/", date: 2026-03-30, access: full, locator: "Section on skepticism to trust"}
    - {ref: GAO-YBFAQ-2025, title: "Government Auditing Standards FAQ: establishing and maintaining a system of quality management (GAO-26-108710)", publisher: "GAO", type: standard-setter, url: "https://files.gao.gov/reports/GAO-26-108710/index.html", date: 2025-12, access: full, locator: "Section I, questions 1 and 2"}
    - {ref: AICPA-PA-2026, title: "AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing", publisher: "AICPA & CIMA", type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: 2026-10-13, access: full, locator: "Section two summary"}
  last_reviewed: 2026-10-21
  notes: "The Plante Moran survey is of general audit research, not a nonprofit or government engagement, so the grade is capped at B. Plante Moran is described by the vendor as one of the nation's largest audit and accounting firms. The St. Pierre firm is small. Governmental content claims (GASB, Uniform Guidance) come from the vendor product page."

- id: assurance-nonprofit-government-04
  title: Footnote-to-statement tie-out of nonprofit and government financial statements
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Auditors manually agree footnote numbers to the face statements and schedules. Copy-and-paste steps cause small differences that surface late."
  solution: "A saved reconciliation template reads the statements and notes and lists every number that does not agree, down to a dollar."
  outcomes:
    - {lever: quality, description: "The firm says the template catches differences in footnote and statement numbers, including a one-dollar difference, and reduces copy-and-paste mistakes", figure: "none published", measures: "Owner's description in a vendor case study; no count of differences found", provenance: vendor-published, source_ref: TR-STPIERRE-2026}
  prerequisites:
    - "Draft statements and notes in a readable format"
    - "Template saved and shared firmwide"
  risks_and_guardrails:
    - "The vendor notes accuracy improves when prompts name the sections to read [TR-STPIERRE-2026]"
    - "A tie-out template checks internal agreement, not whether the amounts are right"
  human_checkpoints:
    - "Preparer clears each listed difference"
  role_evolution: "Tie-out moves from a manual staff task to review of an exceptions list."
  evidence_grade: B
  sources:
    - {ref: TR-STPIERRE-2026, title: "Modernizing nonprofit and government audits with CoCounsel Audit", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit", date: 2026-03-09, access: full, locator: "Disclosures Reconciliation template; Outcomes"}
  last_reviewed: 2026-10-21
  notes: "Single small firm, vendor-authored. No error counts."

- id: assurance-nonprofit-government-05
  title: Key-term extraction from bond indentures, grant agreements and other long agreements
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Debt agreements, grant awards and amendments are long. Auditors need restrictions, reporting requirements, deadlines and covenants to design procedures."
  solution: "The auditor uploads the agreement and a template extracts terms into a report. For grants, the vendor says the tool identifies restrictions, reporting requirements and deadline obligations to help design procedures."
  outcomes:
    - {lever: speed, description: "A firm owner says a 750-page bond indenture produced a report in three to four minutes", figure: "3 to 4 minutes", measures: "Time for one document run, recalled by the firm owner; no comparison with manual time", provenance: vendor-published, source_ref: TR-STPIERRE-2026}
    - {lever: quality, description: "Grant agreement term extraction is described by the vendor; no firm or measure is named", figure: "none published", measures: "Vendor description of intended use", provenance: vendor-published, source_ref: TR-SCALING-2026}
  prerequisites:
    - "Agreements available as readable documents"
    - "Prompts that name the sections to read"
  risks_and_guardrails:
    - "Extraction summarizes sections before analysis, so accuracy depends on prompts naming sections [TR-STPIERRE-2026]"
    - "Missing information should return 'N/A' rather than a guess (vendor advice) [TR-STPIERRE-2026]"
    - "GAO's AI Accountability Framework stresses reliable data and a human in the loop [GAO-FRAUDAI-2026]"
  human_checkpoints:
    - "Auditor agrees extracted terms to the source before relying on them"
  role_evolution: "Reading moves to verification; specialists are consulted less for routine agreements."
  evidence_grade: B
  sources:
    - {ref: TR-STPIERRE-2026, title: "Modernizing nonprofit and government audits with CoCounsel Audit", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit", date: 2026-03-09, access: full, locator: "Debt Agreement Analysis template"}
    - {ref: TR-SCALING-2026, title: "Scaling audit practices with AI: 3 real-world case studies", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/blog/scaling-your-audit-practice-with-ai-3-real-world-cocounsel-audit-case-studies/", date: 2026-06-16, access: full, locator: "Case 3, nonprofit practice engagements"}
    - {ref: GAO-FRAUDAI-2026, title: "Fraud and improper payments: data quality and a skilled workforce are essential for realizing AI's benefits (GAO-26-108850)", publisher: "GAO", type: regulator, url: "https://www.gao.gov/assets/gao-26-108850-highlights.pdf", date: 2026-01, access: full, locator: "What GAO found"}
  last_reviewed: 2026-10-21
  notes: "Grade B rests on the bond indenture example at a small governmental firm. The grant-agreement part is a vendor description (grade C on its own). No source shows a firm testing a grant agreement's compliance terms against the Compliance Supplement with AI."

- id: assurance-nonprofit-government-06
  title: Disclosure checklist review agent inside the audit file
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Disclosure checklists for nonprofit and governmental statements are long and checked by hand late in the audit."
  solution: "An agent in the audit platform reviews the financial statements and returns citation-backed suggestions. The auditor accepts, edits or overrides each suggestion in the engagement."
  outcomes:
    - {lever: capacity, description: "Caseware says the agent saves 2.7 review hours per workflow on average", figure: "2.7 review hours per workflow", measures: "Average review hours saved per workflow, as stated by Caseware; basis, sample and engagement types not stated", provenance: vendor-published, source_ref: CASEWARE-VERITY-2026}
  prerequisites:
    - "Firm on the vendor's audit platform (Citrin Cooperman adopted it on 2026-07-13 [CITRIN-DAS-2026])"
    - "Firm-approved disclosure lists and prior statements as references (a TR customer-success suggestion for a similar template [TR-STPIERRE-2026])"
  risks_and_guardrails:
    - "Vendor figures are not independently checked"
    - "Nonprofit and governmental disclosure sets are not described in the release"
  human_checkpoints:
    - "Auditor accepts, refines or overrides each suggestion [CASEWARE-VERITY-2026]"
  role_evolution: "Reviewers check suggestions against the standards instead of reading the checklist line by line."
  evidence_grade: C
  sources:
    - {ref: CASEWARE-VERITY-2026, title: "Caseware launches Verity to bring workflow-native AI agents directly into assurance engagements", publisher: "Caseware", type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements", date: 2026-05-20, access: full, locator: "Agent list, Disclosure Checklist Agent"}
    - {ref: CITRIN-DAS-2026, title: "Citrin Cooperman adopts AI-enabled DAS Suite powered by Caseware", publisher: "Caseware", type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth", date: 2026-07-13, access: full, locator: "Paragraph 3"}
    - {ref: TR-STPIERRE-2026, title: "Modernizing nonprofit and government audits with CoCounsel Audit", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit", date: 2026-03-09, access: full, locator: "Innovation opportunity: missing financial statement disclosures"}
  last_reviewed: 2026-10-21
  notes: "General audit product. The release does not say the agent covers FASB ASC 958 or GASB disclosure sets; Citrin's release names the agent as an example of agents available but does not say Citrin runs it in production. Caseware also cites 94% accuracy on 'golden dataset' items from beta traces and a drop from 15-20 minutes to under two minutes per indicative manual workflow; both are vendor-published and not engagement measures."

- id: assurance-nonprofit-government-07
  title: First-draft inherent risk assessment to assertion level for newer staff
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Assessing inherent risk of material misstatement by assertion is a concept juniors need a senior to walk through; the knowledge sits with few people in small firms."
  solution: "Staff enter the client facts and ask the assistant for an inherent risk assessment by assertion. They must read, test and own the answer. The owner uses it as scaffolding so staff can start without a senior."
  outcomes:
    - {lever: experience, description: "The Forde Firm owner says staff can now engage with inherent risk at assertion level without her walking them through it", figure: "none published", measures: "Owner's statement in a vendor case study", provenance: vendor-published, source_ref: TR-NPCASE-2026}
  prerequisites:
    - "Staff trained to treat output as a draft"
    - "Risk assessment content in the tool aligned to the firm's methodology"
  risks_and_guardrails:
    - "The owner says staff still have to read and evaluate the output [TR-NPCASE-2026]"
    - "The 2026 GAS/SA Guide expects risk of material noncompliance to be assessed at a more granular level, for fraud and error separately, and discussed with management [BDO-GASSA-2026]; no source shows AI used for that single-audit step"
    - "Skill-formation risk is a general concern; Citrin's leader ties in-engagement reasoning to professional development [CITRIN-DAS-2026]"
  human_checkpoints:
    - "Manager reviews the risk assessment; partner approves"
  role_evolution: "Juniors take on risk-assessment work earlier; seniors review instead of explaining [TR-NPCASE-2026]."
  evidence_grade: B
  sources:
    - {ref: TR-NPCASE-2026, title: "Three nonprofit-focused firms modernize audits with CoCounsel and Audit Intelligence", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/three-nonprofit-focused-firms-modernize-audits-with-thomson-reuters-audit-intelligence-and-cocounsel", date: 2026-04-10, access: full, locator: "Opportunity section (Forde); Fear not section"}
    - {ref: BDO-GASSA-2026, title: "More scrutiny, more documentation: the impact of the updated AICPA GAS/SA Guide to auditees", publisher: "BDO", type: firm, url: "https://www.bdo.com/insights/industries/nonprofit-education/more-scrutiny-more-documentation-the-impact-of-the-updated-aicpa-gas-sa-guide-to-auditees", date: 2026-10-15, access: full, locator: "Paragraphs 3-4 on risk of material noncompliance"}
    - {ref: CITRIN-DAS-2026, title: "Citrin Cooperman adopts AI-enabled DAS Suite powered by Caseware", publisher: "Caseware", type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth", date: 2026-07-13, access: full, locator: "Strengthening professional development and audit quality"}
  last_reviewed: 2026-10-21
  notes: "Single small firm. Caseware's Risk Suggestion Agent launched later in 2026 (title seen on Caseware's news list; page not opened), so it is not used as evidence."

- id: assurance-nonprofit-government-08
  title: "Idea: management-side audit readiness (request-list triage, pre-review of draft statements, fluctuation analysis, estimate memos)"
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [data-reporting, document-production, review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Small nonprofit finance teams answer long audit request lists under time pressure. Sixty percent of nonprofits in one vendor survey rely on one full-time person for all financial management and accounting."
  solution: "A national firm's audit-readiness playbook gives finance teams prompts to sort an audit request list by owner and source, draft fluctuation explanations, check schedules for footing errors and draft estimate memos, in approved tools only. The playbook says outputs are drafts."
  outcomes:
    - {lever: capacity, description: "none published", figure: "none published", measures: "No outcome figures in the source", provenance: self-reported, source_ref: ARMANINO-NFPAI-2026}
  prerequisites:
    - "Approved AI tool and a written AI use policy for finance, with data classification and documentation rules [ARMANINO-NFPAI-2026]"
    - "Complete prior-year statements, trial balance and policies to feed the prompts"
  risks_and_guardrails:
    - "The deck warns AI may produce incorrect citations, facts or calculations and says not to upload donor, employee or grant data to unapproved tools [ARMANINO-NFPAI-2026]"
    - "Mason (Gemifi) says PII worries keep many on Microsoft tools [AICPA-NFPAI-2026]"
  human_checkpoints:
    - "Finance director validates every explanation against actual activity before it goes to auditors"
  role_evolution: "Nonprofit finance staff move from compiling to checking, per an AHRC finance leader [AICPA-NFPCONF-2026]. The deck puts a named partner as Audit AI Innovation Leader."
  evidence_grade: D
  sources:
    - {ref: ARMANINO-NFPAI-2026, title: "The Nonprofit Audit: Readiness, Risk and the Role of AI (webinar deck)", publisher: "Armanino", type: firm, url: "https://www.armanino.com/-/media/pdf/webinars/2026/nonprofit-audit-readiness-risk-ai.pdf", date: 2026-08-06, access: full, locator: "Slides 13-14, 16-29"}
    - {ref: MOMENTIVE-2026, title: "2026 Nonprofit Trends Report (press release)", publisher: "Momentive Software", type: survey, url: "https://aimagazine.com/globenewswire/3340332", date: 2026-08-06, access: full, locator: "Key finding 3"}
    - {ref: AICPA-NFPAI-2026, title: "The untapped potential of AI in not-for-profit accounting", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/professional-insights/article/the-untapped-potential-of-ai-in-not-for-profit-accounting", date: 2026-09-10, access: full, locator: "PII paragraph"}
    - {ref: AICPA-NFPCONF-2026, title: "NFP conference: new tools and insights for today's leaders", publisher: "AICPA & CIMA", type: conference, url: "https://www.aicpa-cima.com/professional-insights/article/nfp-conference-new-tools-and-insights-for-todays-leaders", date: 2026-02-17, access: full, locator: "AI as a strategic tool for NFP teams"}
  last_reviewed: 2026-10-21
  notes: "Idea. A firm-published playbook with no deployment or outcome reported. Armanino is a national firm. Also touches the advisory client-accounting-services space; kept here because it changes the auditor's inputs. The survey's headline says 65% rely on one person and its body says 60%; the source is inconsistent."

- id: assurance-nonprofit-government-09
  title: "Idea: review of the draft schedule of expenditures of federal awards against award documents and the ledger"
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "The schedule of expenditures of federal awards (SEFA) must match award notices, the general ledger, pass-through and subrecipient amounts, clusters and period of performance. Errors surface during the audit."
  solution: "A prompt asks the assistant to compare the draft SEFA with grant agreements, prior-year SEFAs and ledger detail. It lists missing programs, wrong Assistance Listing numbers, expenditures outside the period of performance, and possible duplicates. It separates confirmed errors from questions."
  outcomes:
    - {lever: quality, description: "none published", figure: "none published", measures: "No outcome figures in the source", provenance: self-reported, source_ref: ARMANINO-NFPAI-2026}
  prerequisites:
    - "Award documents, prior SEFAs, ledger detail and cash draw records in an approved tool"
  risks_and_guardrails:
    - "The prompt tells the model not to assume the SEFA is complete or to make unsupported corrections [ARMANINO-NFPAI-2026]"
    - "FFATA reporting procedures are expected for all major programs in the 2026 cycle, so more of the schedule is tested [GAQC-DEV-2026]"
  human_checkpoints:
    - "Management owns the SEFA; the auditor tests it independently"
  role_evolution: "Grant accountants spend less time on first-pass tie-outs."
  evidence_grade: D
  sources:
    - {ref: ARMANINO-NFPAI-2026, title: "The Nonprofit Audit: Readiness, Risk and the Role of AI (webinar deck)", publisher: "Armanino", type: firm, url: "https://www.armanino.com/-/media/pdf/webinars/2026/nonprofit-audit-readiness-risk-ai.pdf", date: 2026-08-06, access: full, locator: "Slide 26, SEFA analysis and rollforward"}
    - {ref: GAQC-DEV-2026, title: "Key developments affecting the governmental auditing environment", publisher: "AICPA Governmental Audit Quality Center", type: professional-body, url: "https://www.aicpa-cima.com/professional-insights/article/key-developments-affecting-the-governmental-auditing-environment", date: 2026-10-08, access: full, locator: "2026 Compliance Supplement: FFATA reporting requirement"}
  last_reviewed: 2026-10-21
  notes: "Idea. Client-side prompt, no named deployment. The brief's core single-audit compliance steps (eligibility, allowable costs, subrecipient monitoring testing) have no equivalent source."

- id: assurance-nonprofit-government-10
  title: Donor agreement and conditional-grant classification support (restricted, conditional, unrestricted)
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "Donor letters are often vague. Classifying gifts as purpose-restricted, time-restricted, conditional or endowment-related drives net asset presentation and later releases from restriction."
  solution: "A prompt asks the assistant to read donor correspondence and agreements and propose a classification with rationale and open questions for management. A vendor says three nonprofit-focused firms use its tool for donor restriction tracking."
  outcomes:
    - {lever: quality, description: "none published", figure: "none published", measures: "Vendor mention of use; no measure", provenance: vendor-published, source_ref: TR-SCALING-2026}
  prerequisites:
    - "Complete agreements and correspondence for material gifts"
  risks_and_guardrails:
    - "The deck says management must validate against ASC 958, UPMIFA and legal interpretation of donor intent [ARMANINO-NFPAI-2026]"
  human_checkpoints:
    - "Accounting and legal judgment on classification; auditor tests management's conclusion"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: TR-SCALING-2026, title: "Scaling audit practices with AI: 3 real-world case studies", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/blog/scaling-your-audit-practice-with-ai-3-real-world-cocounsel-audit-case-studies/", date: 2026-06-16, access: full, locator: "Case 3, nonprofit practice engagements"}
    - {ref: ARMANINO-NFPAI-2026, title: "The Nonprofit Audit: Readiness, Risk and the Role of AI (webinar deck)", publisher: "Armanino", type: firm, url: "https://www.armanino.com/-/media/pdf/webinars/2026/nonprofit-audit-readiness-risk-ai.pdf", date: 2026-08-06, access: full, locator: "Slide 21, prompt 4"}
  last_reviewed: 2026-10-21
  notes: "The vendor blog says the three firms' combination addresses donor restriction tracking, but the firms' own case study does not describe a donor-restriction use. Treat as a vendor claim."

- id: assurance-nonprofit-government-11
  title: Federal agency AI analysis of single audit history to target noncompliance (HHS AERO)
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Federal agencies must ensure audits are submitted on time and findings corrected, and HHS says repeat findings and delinquent audits went unaddressed for years."
  solution: "HHS's finance office says it is analyzing single audit information across all 50 states with AI tools covering at least five years, and it has written to governors and treasurers. It lists remedies that include withholding payments and disallowing costs. It also says it is examining whether audits are done with enough rigor."
  outcomes:
    - {lever: risk, description: "HHS reports many grantees have not submitted required audits, some by more than two years", figure: "'hundreds' of HHS grantees", measures: "HHS grantees that have not submitted their required audits, per HHS; no denominator and no AI performance measure given", provenance: self-reported, source_ref: HHS-AERO-2026}
  prerequisites:
    - "Single audit information for at least five years across all 50 states, held by HHS [HHS-AERO-2026]"
  risks_and_guardrails:
    - "Stakeholders have raised questions about transparency, methodology and procedural fairness [CBH-AERO-2026]; Thompson reports the effort is 'under fire' from some stakeholder organizations [THOMPSON-AERO-2026]"
    - "HHS says it is too early to estimate savings [HHS-AERO-2026]"
    - "GAO: AI for fraud and improper payments needs reliable data and a human in the loop [GAO-FRAUDAI-2026]"
  human_checkpoints:
    - "HHS staff send letters and decide on remedies; the press release does not describe review of AI outputs"
  role_evolution: "Auditors' reports become inputs to agency analytics; firms advise clients to fix repeat findings, timeliness and corrective action plans [CBH-AERO-2026; FELDESMAN-AERO-2026]. HHS's rigor review puts single audit quality itself under scrutiny."
  evidence_grade: B
  sources:
    - {ref: HHS-AERO-2026, title: "HHS cracks down on years of unchecked audit findings", publisher: "U.S. Department of Health and Human Services", type: regulator, url: "https://www.hhs.gov/press-room/asfr-aero-audit-enforcement-risk-oversight-initiative.html", date: 2026-05-21, access: full, locator: "Paragraphs 1-3"}
    - {ref: FELDESMAN-AERO-2026, title: "Client alert: HHS to use AI tools to track grantee compliance with audit requirements", publisher: "Feldesman", type: firm, url: "https://www.feldesman.com/hhs-to-use-artificial-intelligence-tools-to-track-grantee-compliance-with-audit-requirements/", date: 2026-05-22, access: full, locator: "Opening paragraphs"}
    - {ref: THOMPSON-AERO-2026, title: "Sneak preview: HHS using AI to enforce compliance with single audit requirements", publisher: "Thompson Grants", type: press, url: "https://www.thompsongrants.com/editorial-commentary/sneak-preview-hhs-using-ai-to-enforce-compliance-with-single-audit-requirements", date: 2026-05-27, access: full, locator: "Opening paragraph"}
    - {ref: CBH-AERO-2026, title: "HHS's AERO use of AI to enforce single audit compliance raises the stakes for grantees", publisher: "Cherry Bekaert", type: firm, url: "https://www.cbh.com/insights/articles/hhs-aero-ai-grantee-audit-readiness-step/", date: 2026-06-26, access: full, locator: "Why AI changes the conversation"}
    - {ref: GAO-FRAUDAI-2026, title: "Fraud and improper payments: data quality and a skilled workforce are essential for realizing AI's benefits (GAO-26-108850)", publisher: "GAO", type: regulator, url: "https://www.gao.gov/assets/gao-26-108850-highlights.pdf", date: 2026-01, access: full, locator: "What GAO found"}
  last_reviewed: 2026-10-21
  notes: "Counterparty use, not the auditor's own AI. One secondary report seen only in a search summary (not opened) said the tools include ChatGPT; HHS's release names no model, so that claim is not repeated here. The tools, accuracy and any error rate are unpublished. Included because it raises the quality bar for every nonprofit and government audit firm."

- id: assurance-nonprofit-government-12
  title: Government audit offices use AI to find anomalies in large spending datasets
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "State and local government audits involve large transaction sets, such as purchasing-card spending, and small audit teams."
  solution: "The North Carolina State Auditor says the office uses industry partners to apply AI to large datasets, then verifies findings with people. The Washington State Auditor publishes a policy for limited, governed AI use with a staff review requirement and an oversight committee."
  outcomes:
    - {lever: risk, description: "North Carolina's auditor says AI helps find a needle in a haystack and has made purchasing-card audits more efficient", figure: "none published", measures: "Official's interview statement; no counts, error rates or time measures", provenance: self-reported, source_ref: NCAUDITOR-2026}
  prerequisites:
    - "Industry partner or vendor tools; secure data handling"
    - "Written AI policy and oversight committee (Washington) [WASAO-AIPOLICY-2026]"
  risks_and_guardrails:
    - "The auditor says AI alone is not reliable enough to accept results without human verification [NCAUDITOR-2026]"
    - "Washington requires staff to review, verify and take responsibility for AI-assisted work [WASAO-AIPOLICY-2026]"
  human_checkpoints:
    - "Human verification of every finding before it is reported"
  role_evolution: "Teams point staff at the places where review is worth the effort [NCAUDITOR-2026]."
  evidence_grade: B
  sources:
    - {ref: NCAUDITOR-2026, title: "Boliek: jet fuel on computer technology, getting juice worth the squeeze", publisher: "The Center Square (via local papers)", type: press, url: "https://www.themountaineer.com/news/state/boliek-jet-fuel-on-computer-technology-getting-juice-worth-the-squeeze/article_f3ca886a-373c-58ee-aee8-0287a461188d.html", date: 2026-07-08, access: full, locator: "Quotes on partners, verification, procurement cards"}
    - {ref: WASAO-AIPOLICY-2026, title: "AI Use Policy", publisher: "Office of the Washington State Auditor", type: regulator, url: "https://sao.wa.gov/ai-use-policy", date: 2026-08, access: full, locator: "Full page"}
    - {ref: GAO-FRAUDAI-2026, title: "Fraud and improper payments: data quality and a skilled workforce are essential for realizing AI's benefits (GAO-26-108850)", publisher: "GAO", type: regulator, url: "https://www.gao.gov/assets/gao-26-108850-highlights.pdf", date: 2026-01, access: full, locator: "What GAO found"}
  last_reviewed: 2026-10-21
  notes: "Government audit organizations, not mid-market CPA firms. They show what local-government clients and competitors for government audit work may see. Oklahoma's newly elected auditor was reported as planning AI use but the page could not be read."

- id: assurance-nonprofit-government-13
  title: AI error check and chatbot inside Form 990 e-file software
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Form 990, 990-EZ, 990-PF and 990-T filings need schedules, support and consistency checks; errors cause rejections and penalties."
  solution: "The e-file product runs an AI-powered check for potential issues before submission and offers a chatbot for filing questions. The vendor says it is working on improvements to AI validation."
  outcomes:
    - {lever: quality, description: "none published", figure: "none published", measures: "Feature description only; no error rates", provenance: vendor-published, source_ref: TAX990-2026}
  prerequisites:
    - "Return data entered or imported into the product"
  risks_and_guardrails:
    - "IRS OPR Alert 2026-19 ties AI use by tax practitioners to due diligence, competence, fees and firm procedures under Circular 230; it is not specific to exempt organization returns [IRS-OPR-2026]"
    - "Whether sending return information to an AI tool needs section 7216 consent is unresolved for 1040-series returns; no source addresses exempt-organization returns [CPAPA-7216-2026]"
  human_checkpoints:
    - "Preparer reviews and signs; the check is not an approval"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: TAX990-2026, title: "New year, new start: get ahead on your 2025 Form 990 filing", publisher: "Tax990", type: vendor, url: "https://blog.tax990.com/2026/01/14/new-year-new-start-get-ahead-on-your-2025-form-990-filing/", date: 2026-01-14, access: full, locator: "What Tax990 achieved in the past year"}
    - {ref: IRS-OPR-2026, title: "Introductory guidelines for responsible AI use in federal tax practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory framework: Circular 230 provisions"}
    - {ref: CPAPA-7216-2026, title: "What to settle before client tax data touches AI", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/?p=191491", date: 2026-10-12, access: full, locator: "The consent question has no clean answer yet"}
  last_reviewed: 2026-10-21
  notes: "Pattern other: pre-submission validation. The only AI feature found for exempt-organization returns. A self-service filing product, not a CPA-firm preparation workflow; no named customer. The same vendor says AI dominated the AICPA Not-for-Profit conference sessions [TAX990-NFPCONF-2026]."

- id: assurance-nonprofit-government-14
  title: IRS exempt-organization examination screening and referral triage
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: "The IRS exempt organization examination unit receives public referrals and runs data-driven compliance exams based on Form 990 data."
  solution: "A TE/GE letter summarized by EY says TE/GE and its research unit built an AI tool to screen and prioritize public referrals, planned for launch in fiscal 2024. The same summary says data-driven exams based on Form 990 information found employment taxes, unrelated business income and underreported compensation as the most prominent issues."
  outcomes:
    - {lever: risk, description: "Exempt organization examinations: about 76% of closed exams resulted in a tax change in fiscal 2023", figure: "about 76%", measures: "Closed EO Examinations exams in FY2023 that resulted in a tax change, per the IRS letter as summarized by EY; not a measure of the AI tool", provenance: self-reported, source_ref: EY-TEGE-2024}
  prerequisites:
    - "Form 990 data in IRS systems"
  risks_and_guardrails:
    - "TIGTA found IRS return-selection models for other divisions produced a high percentage of exams with no change, and that the IRS lacked processes to evaluate whether AI models beat prior approaches [TIGTA-AISELECT-2025]; the audit did not cover TE/GE"
  human_checkpoints:
    - "Not described"
  role_evolution: "Practitioners should expect 990 data to be screened by the IRS; unrelated business income and compensation reporting were named issues [EY-TEGE-2024]."
  evidence_grade: C
  sources:
    - {ref: EY-TEGE-2024, title: "TE/GE Commissioner highlights strategic achievements in fiscal 2023 accomplishments letter, will be launching AI screening program in FY 2024", publisher: "EY Tax News", type: press, url: "https://taxnews.ey.com/news/2024-0350-te-ge-commissioner-highlights-strategic-achievements-in-fiscal-2023-accomplishments-letter-will-be-launching-ai-screening-program-in-fy-2024", date: 2024-02-06, access: full, locator: "Paragraphs on the AI tool and data-driven examinations"}
    - {ref: TIGTA-AISELECT-2025, title: "The IRS could leverage examination results in AI examination case selection models and improve processes to evaluate performance (2025-308-022)", publisher: "TIGTA", type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: 2025-05-19, access: full, locator: "Highlights, What TIGTA found"}
  last_reviewed: 2026-10-21
  notes: "Counterparty signal, older than 18 months and secondary; launch status after 2024 was not confirmed. The 76% figure is the exam outcome rate, not an AI result."

- id: assurance-nonprofit-government-15
  title: Screening grant documents for policy-restricted language before submission
  archetype: assurance
  module: nonprofit-government
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Grant writers must remove language that new federal or state policy restricts; manual review is slow and delays submissions."
  solution: "A university research office tool combines rule-based text matching with a language model in a private cloud to flag sensitive terms in a grant document and suggest alternatives."
  outcomes:
    - {lever: quality, description: "On five annotated grant documents the tool found most policy-sensitive terms with no false positives and beat general-purpose models", figure: "precision 1.00; recall 0.73 (16 of 22 terms); F1 0.84", measures: "Terms correctly flagged out of 22 policy-sensitive terms annotated by two reviewers across 5 grant proposals, compared with GPT-4o (F1 0.43) and Gemini 2.5 Pro (F1 0.72)", provenance: self-reported, source_ref: GRANTCHECK-2025}
    - {lever: experience, description: "Usability among faculty and staff scored high", figure: "mean SUS 85.9 (SD 13.4)", measures: "System Usability Scale score from 25 faculty and staff testers", provenance: self-reported, source_ref: GRANTCHECK-2025}
  prerequisites:
    - "Institution-hosted private environment; term dictionary maintained by the office"
  risks_and_guardrails:
    - "Recall of 0.73 means about a quarter of annotated terms were missed; the tool shows a notice that suggestions may be inaccurate [GRANTCHECK-2025]"
  human_checkpoints:
    - "Author accepts or rejects each suggestion"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - {ref: GRANTCHECK-2025, title: "GrantCheck: an AI solution for guiding grant language to new policy requirements: development study", publisher: "JMIR Formative Research (UMass Chan Medical School authors)", type: academic, url: "https://formative.jmir.org/2025/1/e79038", date: 2025-11-27, access: full, locator: "Abstract; Results"}
  last_reviewed: 2026-10-21
  notes: "Adjacent process: grant proposal writing at a university, not audit or compliance testing of awards, so the grade is capped at B. Small gold set (5 documents). Relevant as a research signal that grant-document policy checks can be built; no CPA-firm or audit use found."
```

## 3. Module notes

**Processes and key steps (work type)**

- Engagement planning and risk assessment: understand the entity and its grants portfolio, assess risk of material misstatement and, for single audits, risk of material noncompliance by compliance requirement (research-synthesis, expert-judgment). The 2026 GAS/SA Guide asks for granular risk of material noncompliance, for fraud and for error [BDO-GASSA-2026].
- Major program determination and Compliance Supplement use: pick programs and requirements; the 2026 Supplement adds five and removes nine programs in draft, realigns programs, flags Medicaid, CCDF and TANF as higher risk and requires FFATA procedures for all major programs [GAQC-DEV-2026] (expert-judgment, research-synthesis).
- SEFA: obtain and test the schedule of expenditures of federal awards (data-reporting, review-assurance).
- Financial statement audit of nonprofits: contributions, conditional grants, net assets with donor restrictions, functional expenses, estimates, board minutes and agreements [ARMANINO-NFPAI-2026] (review-assurance, expert-judgment).
- Controls and compliance testing: control sampling and compliance sampling using the Appendix B tables; deeper IT application testing [BDO-GASSA-2026] (review-assurance, data-reporting).
- Evaluation of deviations and noncompliance: cause, monetary impact, questioned costs; management support needed [BDO-GASSA-2026] (expert-judgment).
- Reporting: Yellow Book reports, schedule of findings and questioned costs, disclosure review (document-production, review-assurance).
- Quality: Yellow Book system of quality management, peer review, CPE (coordination-scheduling, review-assurance) [GAO-YBFAQ-2025].
- Form 990, 990-T and UBI preparation: organizer, public support test, program descriptions, schedules, compensation data; 990-T needs identification of unrelated activities, silos and NOL use [TAX990-2026; AICPA-NFPWORKSHOPS-2026] (data-reporting, document-production). No AI-specific process material was found for these steps.

**Common pain points**

- Delayed and shifting rules: the 2026 Compliance Supplement unreleased as of 2026-10-08; Uniform Guidance rewrite proposed on 2026-05-29 with no significant Subpart F audit changes proposed per GAQC [GAQC-DEV-2026; FR-OMB-2026].
- Heavier work: more audit requests, documentation, IT testing, larger samples and possibly higher fees [BDO-GASSA-2026].
- Staffing and margins in small nonprofit niches: owners cite a shrinking talent pool, clients that cannot afford high fees, and no backfilling [TR-NPCASE-2026].
- Auditee capacity: 60% of nonprofits surveyed rely on one full-time person for all financial management and accounting (the release headline says 65%) [MOMENTIVE-2026].
- Federal scrutiny of audit quality: HHS rigor review; Financial Management Risk Reduction Act review led by HHS with an OMB report to Congress due December 2027 [HHS-AERO-2026; GAQC-DEV-2026].

**Metrics and benchmarks (with sources)**

- Peer review (one state): 2 of 11 single audits and 1 of 29 other Government Auditing Standards engagements were nonconforming in 2025; no AI content in the report [TSCPA-PEERREVIEW-2025].
- Plante Moran pilot survey: 96% agreed the tool is useful for practice staff, 91% faster for research, 87% felt it should be bought for all staff, 77% more confident with generative AI, 62% significant research time savings, 58% used other tools less (all % of survey respondents; vendor-published) [TR-PLANTEMORAN-2025].
- Caseware (vendor, general audit): 94% accuracy on golden dataset items from beta traces; 15-20 minutes to under two minutes per indicative workflow; 2.7 review hours per disclosure checklist workflow [CASEWARE-VERITY-2026].
- Nonprofit sector (vendor survey of 500 executives): 91% use AI in some official capacity; 29% extensively; board support strongly linked to extensive use [MOMENTIVE-2026].
- GrantCheck: precision 1.00, recall 0.73 on 22 terms in 5 documents [GRANTCHECK-2025].
- No independent accuracy, override or inspection metric for any AI tool in this module was found.

**Guardrails and regulatory points**

- Yellow Book (2024 revision): system of quality management designed by 2025-12-15; initial evaluation by 2026-12-15 [GAO-YBFAQ-2025]. GAQC lists "emerging ethics, quality management, and AI-related guidance" as a watch item, so no Yellow Book AI guidance yet [GAQC-DEV-2026].
- AICPA practice aid (2026-10-13): firm quality management for AI tools, team competence, planning of AI use per engagement, partner responsibility for approved tools; auditor remains responsible; more risk and evidence material expected [AICPA-PA-2026].
- Federal oversight: HHS AERO remedies under the Uniform Guidance (withholding, disallowing costs, suspension, debarment) [HHS-AERO-2026].
- GAO: AI for fraud and improper-payment work needs reliable data and a human in the loop [GAO-FRAUDAI-2026].
- Tax-side: Circular 230 duties (due diligence 10.22, fees 10.27(a), competence 10.35, procedures 10.36) apply to AI use [IRS-OPR-2026]; section 7216 consent for AI use unresolved for 1040-series returns [CPAPA-7216-2026]. Nothing found on exempt-organization returns.
- Confidentiality: donor and employee data; firms advise approved tools only and a written policy [ARMANINO-NFPAI-2026; AICPA-NFPAI-2026].

**Frontier signals (dated)**

- 2026-05-21: HHS AERO launched with AI analysis of single audit history and a review of audit rigor [HHS-AERO-2026].
- 2026-05-20 and 2026-06-04: Caseware Verity and Customer Acceleration Programs; named customers include Plante Moran, CohnReznick, Forvis Mazars, Wipfli, Citrin Cooperman, Weaver, Carr Riggs & Ingram and PKF O'Connor Davies (vendor list) [CASEWARE-VERITY-2026; CASEWARE-PIONEER-2026].
- 2026-07-13 and 2026-10-08: Citrin Cooperman and PKF O'Connor Davies announce DAS Suite adoption [CITRIN-DAS-2026; PKF-DAS-2026 (search-only)].
- 2026-08-06: Armanino publishes AI prompts for nonprofit audit readiness, including SEFA review [ARMANINO-NFPAI-2026].
- 2026-09-23 webcast, rebroadcast scheduled 2026-12-18: AICPA "Practical AI Techniques for CPAs Serving Not-for-profits" on strategy versus policy and vetting embedded AI [AICPA-NFPWEBCAST-2026].
- 2026-10-13: AICPA practice aid; 2026-10-15: BDO on GAS/SA Guide changes [AICPA-PA-2026; BDO-GASSA-2026].
- 2026-07-08 and 2026-08: state auditors in North Carolina and Washington describe governed AI use [NCAUDITOR-2026; WASAO-AIPOLICY-2026].
- Scheduled: 2026-12-15 Yellow Book initial quality-management evaluation due [GAO-YBFAQ-2025].

**Workforce and role effects**

- Small firms say AI lets them hold output with fewer staff and push work to juniors; one owner reports being down two people with the same revenue output (self-reported) [TR-NPCASE-2026].
- Citrin Cooperman's innovation leader links in-workflow reasoning to staff learning (vendor-published) [CITRIN-DAS-2026].
- Pipeline concerns: GAQC lists public sector CPA pipeline initiatives as a watch item [GAQC-DEV-2026].
- Hiring signal: an Aprio senior manager posting for tax-exempt and single audit work lists "experience with data analytics or audit automation tools" as a qualification (posted 2026-09-18) [APRIO-JOB-2026]. The posting read is not an AI-specific role.
- Finance leaders at nonprofits say AI moves staff from reconciling to analyzing [AICPA-NFPCONF-2026].

**Objections and concerns practitioners raise**

- Data privacy and donor PII keep teams on Microsoft tools [AICPA-NFPAI-2026].
- Hallucination, incorrect citations and calculations; treat outputs as drafts [ARMANINO-NFPAI-2026].
- Transparency and fairness of agency AI (AERO) [CBH-AERO-2026; THOMPSON-AERO-2026].
- Counter-argument to "AI cannot audit itself": a Top 100 firm's not-for-profit partner says auditors test the information management gives them, whatever tool produced it [ATODAY-DAVIS-2026].
- Skills ceiling: Gemifi's cofounder says few professionals are near the AI skill ceiling [AICPA-NFPAI-2026].
- Rule instability (Supplement delay, Uniform Guidance rewrite) is the backdrop for any AI claim on single audit steps [GAQC-DEV-2026; FR-OMB-2026]. The Wolters Kluwer government-audit AI course (2 CPE, May 2026) shows teaching demand, not practice [WK-GOVAI-2026].

**Interview probes**

1. Walk through your last single audit's compliance and control sampling. How will the revised Appendix B minimum sample sizes change it, and does any tool touch sample selection?
2. Which documents do staff read end to end (minutes, grant agreements, donor letters, bond indentures)? Which would you hand to a tool first, and who re-reads the output?
3. HHS is analyzing five years of single audit history and reviewing rigor. What does your file show about how you evidenced the work, and would AI use be visible on it?
4. How do clients hand over data when one person runs finance? Do you accept AI-assisted SEFAs or pre-audit schedules, and what do you test differently?
5. Who prepares the 990 and 990-T, does any step use AI, and where did you draw the line on client data and consent?

## 4. Routed to other modules

- Citrin Cooperman DAS Audit, DAS PCR and DAS EBP on one AI platform (2026-07-13); PKF O'Connor Davies DAS and Agentic Pioneer Program (2026-10-08, search-only): proposed `private-company-assurance` and `benefit-plan-audits` [CITRIN-DAS-2026; PKF-DAS-2026].
- Firm-built proprietary agents (Agent Builder, Agent Studio) and Caseware platform governance: `quality-management` and proposed `private-company-assurance` [CASEWARE-PIONEER-2026].
- AICPA practice aid on firms' AI use and Yellow Book system of quality management: existing `quality-management` [AICPA-PA-2026; GAO-YBFAQ-2025].
- Plante Moran pilot survey on general audit research: existing `substantive-testing` and `quality-management` [TR-PLANTEMORAN-2025].
- Prager Metis argument on auditing AI-assisted work: existing `assurance-over-ai` [ATODAY-DAVIS-2026].
- OPR Alert 2026-19 and the section 7216 consent question: tax archetype guardrails [IRS-OPR-2026; CPAPA-7216-2026].
- IRS exempt-organization AI and TIGTA findings: tax `controversy` [EY-TEGE-2024; TIGTA-AISELECT-2025].
- Management-side readiness prompts for nonprofit finance teams: advisory `client-accounting-services` [ARMANINO-NFPAI-2026].
- Form 990-T and UBI preparation as a tax service: tax `compliance-corporate` if the integrator keeps nonprofit tax out of this module.

## 5. Sources

Access is `full` unless marked. Dates are ISO.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| HHS-AERO-2026 | HHS cracks down on years of unchecked audit findings | HHS | regulator | https://www.hhs.gov/press-room/asfr-aero-audit-enforcement-risk-oversight-initiative.html (read via mirror; direct fetch denied) | 2026-05-21 |
| GAO-FRAUDAI-2026 | Fraud and improper payments (GAO-26-108850), highlights | GAO | regulator | https://www.gao.gov/assets/gao-26-108850-highlights.pdf | 2026-01 |
| TIGTA-AISELECT-2025 | IRS AI examination case selection models (2025-308-022) | TIGTA | regulator | https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf | 2025-05-19 |
| FR-OMB-2026 | Regulation for Federal Financial Assistance (proposed rule, docket OMB-2026-0034) | OMB, Federal Register | regulator | https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance | 2026-05-29 |
| IRS-OPR-2026 | OPR Alert 2026-19, responsible AI use in federal tax practice | IRS OPR | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 |
| WASAO-AIPOLICY-2026 | AI Use Policy | Washington State Auditor | regulator | https://sao.wa.gov/ai-use-policy | 2026-08 |
| GAO-YBFAQ-2025 | Government Auditing Standards FAQ on quality management (GAO-26-108710) | GAO | standard-setter | https://files.gao.gov/reports/GAO-26-108710/index.html | 2025-12 |
| AICPA-PA-2026 | AICPA releases guidance on AI in financial reporting and auditing | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 |
| GAQC-DEV-2026 | Key developments affecting the governmental auditing environment | AICPA GAQC | professional-body | https://www.aicpa-cima.com/professional-insights/article/key-developments-affecting-the-governmental-auditing-environment | 2026-10-08 |
| AICPA-NFPAI-2026 | The untapped potential of AI in not-for-profit accounting | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/professional-insights/article/the-untapped-potential-of-ai-in-not-for-profit-accounting | 2026-09-10 |
| TSCPA-PEERREVIEW-2025 | Annual Report on Peer Review Activities 2025 | Tennessee Society of CPAs | professional-body | https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf | 2026-03-31 |
| AICPA-NFPCONF-2026 | NFP conference: new tools and insights for today's leaders | AICPA & CIMA | conference | https://www.aicpa-cima.com/professional-insights/article/nfp-conference-new-tools-and-insights-for-todays-leaders | 2026-02-17 |
| AICPA-NFPWORKSHOPS-2026 | NFP Industry Conference pre-conference workshops (sampling; Form 990-T deep dive) | AICPA & CIMA | conference | https://events.aicpa-cima.com/nfp/Program/Pre-Conference-Workshops | 2026-06-15 (workshop date; page title says 2027) |
| AICPA-NFPWEBCAST-2026 | Practical AI techniques for CPAs serving not-for-profits (rebroadcast of 2026-09-23 webcast) | AICPA & CIMA | conference | https://www.aicpa-cima.com/cpe-learning/webcast/practical-ai-techniques-for-cpas-serving-not-for-profits | 2026-09-23 |
| TAX990-NFPCONF-2026 | Tax990 at the AICPA Not-for-Profit Industry Conference: what we learned | Tax990 | vendor | https://blog.tax990.com/?p=2865 | 2026-07-02 |
| TR-NPCASE-2026 | Three nonprofit-focused firms modernize audits with CoCounsel and Audit Intelligence | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/three-nonprofit-focused-firms-modernize-audits-with-thomson-reuters-audit-intelligence-and-cocounsel | 2026-04-10 |
| TR-NONPROFITFIRMS-2026 | Same story, community post (landscape key; undated, "6 months ago") | Thomson Reuters Community | vendor | https://community.thomsonreuters.com/tax-accounting/f/audit-and-accounting/35253/three-nonprofit-focused-firms-modernize-audits-with-cocounsel-and-audit-intelligence | 2026 (page undated) |
| TR-STPIERRE-2026 | Modernizing nonprofit and government audits with CoCounsel Audit | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit | 2026-03-09 |
| TR-SCALING-2026 | Scaling audit practices with AI: 3 real-world case studies | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/scaling-your-audit-practice-with-ai-3-real-world-cocounsel-audit-case-studies/ | 2026-06-16 |
| TR-PLANTEMORAN-2025 | Thomson Reuters CoCounsel at Plante Moran | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/thomson-reuters-cocounsel-at-plante-moran | 2025-11-20 |
| TR-COCOUNSEL-2025 | CoCounsel Audit & Accounting (product page) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/products/cocounsel-audit-accounting | 2025-08-25 (page metadata) |
| TR-STATEAUDIT-2026 | The state of AI in audit in 2026: seven questions | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/ | 2026-03-30 |
| CASEWARE-VERITY-2026 | Caseware launches Verity (press release; landscape key) | Caseware | vendor | https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements | 2026-05-20 |
| CASEWARE-PIONEER-2026 | Caseware launches Verity Agentic Pioneer Program | Caseware | vendor | https://www.caseware.com/news/trusted-by-the-majority-of-top-30-u-s-accounting-firms-caseware-launches-verity-agentic-pioneer-program | 2026-06-04 |
| CITRIN-DAS-2026 | Citrin Cooperman adopts AI-enabled DAS Suite | Caseware | vendor | https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth | 2026-07-13 |
| TAX990-2026 | New year, new start: get ahead on your 2025 Form 990 filing | Tax990 | vendor | https://blog.tax990.com/2026/01/14/new-year-new-start-get-ahead-on-your-2025-form-990-filing/ | 2026-01-14 |
| WK-GOVAI-2026 | Using AI in a Government Audit (self-study course) | Wolters Kluwer CPELink | vendor | https://www.cchcpelink.com/self-study/using-ai-in-a-government-audit/34745/ | 2026-05 |
| BDO-GASSA-2026 | More scrutiny, more documentation: impact of the updated AICPA GAS/SA Guide | BDO | firm | https://www.bdo.com/insights/industries/nonprofit-education/more-scrutiny-more-documentation-the-impact-of-the-updated-aicpa-gas-sa-guide-to-auditees | 2026-10-15 |
| CBH-AERO-2026 | HHS's AERO use of AI to enforce single audit compliance | Cherry Bekaert | firm | https://www.cbh.com/insights/articles/hhs-aero-ai-grantee-audit-readiness-step/ | 2026-06-26 |
| ARMANINO-NFPAI-2026 | The Nonprofit Audit: Readiness, Risk and the Role of AI | Armanino | firm | https://www.armanino.com/-/media/pdf/webinars/2026/nonprofit-audit-readiness-risk-ai.pdf | 2026-08-06 |
| FELDESMAN-AERO-2026 | Client alert: HHS to use AI tools to track grantee compliance | Feldesman | firm | https://www.feldesman.com/hhs-to-use-artificial-intelligence-tools-to-track-grantee-compliance-with-audit-requirements/ | 2026-05-22 |
| PKF-DAS-2026 | PKF O'Connor Davies adopts AI-enabled DAS Suite and joins the Agentic Pioneer Program | PKF O'Connor Davies | firm | https://www.pkfod.com/?p=23897 (access: search-only; only title and date confirmed through the mirror, body unread) | 2026-10-08 |
| THOMPSON-AERO-2026 | Sneak preview: HHS using AI to enforce compliance with single audit requirements | Thompson Grants | press | https://www.thompsongrants.com/editorial-commentary/sneak-preview-hhs-using-ai-to-enforce-compliance-with-single-audit-requirements | 2026-05-27 |
| NCAUDITOR-2026 | Boliek: jet fuel on computer technology | The Center Square | press | https://www.themountaineer.com/news/state/boliek-jet-fuel-on-computer-technology-getting-juice-worth-the-squeeze/article_f3ca886a-373c-58ee-aee8-0287a461188d.html | 2026-07-08 |
| ATODAY-DAVIS-2026 | "AI cannot audit itself" - a response (Scott Davis, Prager Metis) | Accounting Today | press | https://www.accountingtoday.com/opinion/ai-cannot-audit-itself-a-response | 2026-06-05 |
| CPAPA-7216-2026 | What to settle before client tax data touches AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=191491 | 2026-10-12 |
| EY-TEGE-2024 | TE/GE Commissioner highlights fiscal 2023 accomplishments, AI screening program | EY Tax News | press | https://taxnews.ey.com/news/2024-0350-te-ge-commissioner-highlights-strategic-achievements-in-fiscal-2023-accomplishments-letter-will-be-launching-ai-screening-program-in-fy-2024 | 2024-02-06 |
| GRANTCHECK-2025 | GrantCheck: AI for guiding grant language to new policy requirements | JMIR Formative Research | academic | https://formative.jmir.org/2025/1/e79038 | 2025-11-27 |
| MOMENTIVE-2026 | 2026 Nonprofit Trends Report (press release, 500 executives) | Momentive Software | survey | https://aimagazine.com/globenewswire/3340332 | 2026-08-06 |
| APRIO-JOB-2026 | Senior Manager, Non-Profit (assurance) job posting | Aprio | job-posting | https://jobs.lever.co/Aprio/705d6e91-0dd0-4097-bae2-768a2c252f1d | 2026-09-18 |

By type: regulator 6, standard-setter 2, professional-body 3, conference 3, vendor 13, firm 5 (1 search-only), press 5, academic 1, survey 1, job-posting 1 (40 rows). TR-NONPROFITFIRMS-2026 repeats TR-NPCASE-2026 (same story, different page), so 38 distinct documents were opened and read; PKF-DAS-2026 is search-only. Podcast and community: none reached.

## 6. Gaps

- **No measured outcome.** No error rate, override rate, parallel run, inspection result or independent test of any AI tool in a single audit, Yellow Book audit, nonprofit audit, Form 990 or UBI return. Every figure is a recollection or vendor-published.
- **No AI finding from regulators or bodies on auditors' use:** nothing from AICPA peer review, GAQC, GAO's Yellow Book or the Compliance Supplement on AI. The GAQC post lists AI-related guidance only as a watch item [GAQC-DEV-2026].
- **Single audit compliance testing by requirement** (eligibility, allowable costs, subrecipient monitoring, procurement and suspension checks, cash management): no named AI deployment. Major program determination and findings drafting: none.
- **Form 990, 990-T and UBI:** only one e-file product's AI feature and conference themes; no firm case study or AI preparation workflow. The WK CCH Axcess 990 page was blocked.
- **Blocked or unread:** PKF O'Connor Davies release body (Cloudflare block; title and date only); Becker's article and a Wolters Kluwer ENGAGE release (blocked or mirror stub); Wiss, Marcum and the California State Controller AI paper (Cloudflare); AICPA GovNFP agenda (page now shows the 2027 edition); Oklahoma auditor article (stub). A session on GAO's AI oversight framework (speakers from GAO) is on an AICPA conference page whose year could not be confirmed, so it is not cited as a source.
- **Unverified secondary claims:** reports that AERO uses ChatGPT (not in HHS's release) were not repeated. The Momentive release has a 60% versus 65% inconsistency for one-person finance teams.
- **No podcast, community or nonprofit-sector AI survey of audit firms** was reachable. The AICPA NFP webcast and the TR-NONPROFITFIRMS-2026 community post are the nearest items; the community post is undated on the page.
- **Mid-market view:** most named firms are small or national (Plante Moran, Armanino, Cherry Bekaert, BDO). No middle-market PE-backed platform describing its nonprofit or government practice was found.
