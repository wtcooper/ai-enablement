# Assurance / substantive-testing: discourse angle (wave 1 deep dive)

- **Archetype:** assurance
- **Module:** substantive-testing. Substantive procedures on balances and transactions: journal-entry and fraud testing, substantive analytics, document matching and vouching, confirmations, revenue and inventory testing, support for testing accounting estimates, sampling versus full-population testing, contract review.
- **Angle:** discourse. What practitioners say (last 12-18 months, roughly Apr 2025 to Oct 2026) in conference sessions, panels, podcasts, practitioner articles and vendor/analyst commentary.
- **Prepared:** 2026-10-16. **Landscape used:** `research/runs/wave1/landscape-assurance.md`. **Vocabulary:** `research/briefs/templates/vocabulary.md`.
- **Method note.** Pages were fetched with `curl` (PDFs with `pdftotext`). Where `curl` was refused (Controllers Council, Bloomberg Tax) the text mirror `r.jina.ai` was used for that specific URL and the source is marked accordingly. The web-search quota ran out after eight searches, so discovery after that point relied on links from pages already opened and on the landscape's URL list. Every source marked `access: full` was opened and read for the passages cited. Conference and podcast sources are mostly agendas, recaps and show notes; no session recordings or audio were available (see Gaps).

---

## 1. Summary

- **The practitioner conversation has split into two stories that rarely meet.**
  - Story one is the efficiency story: firms say agents will take over routine substantive tests (vouching, payroll, unrecorded liabilities, evidence matching). KPMG leaders were reported on 10 Apr 2026 as expecting "next to no human beings" in routine-transaction testing within two to three years, starting with a pilot in summer 2026 (CTRLCOUNCIL-WSJ-2026).
  - Story two is the evidence-integrity story ("audit in AI"): the same technology makes forged invoices, bank letters and receipts cheap, so documents that auditors vouch to can no longer be assumed authentic (TR-BANKCONF-2026; ISACA-EVIDENCE-2026; JOFA-APFRAUD-2026). Surveys of fraud and internal-audit professionals show low preparedness (SAS-ACFE-2026; IIA-AIFRAUD-2026).
- **Claims have outrun published evidence.** One year after PwC said end-to-end AI audit automation should arrive in calendar 2026 (PWC-AT-2025), its US assurance leader told CFO Dive that busy-season time savings were "not that drastic yet" (CFODIVE-PWC-2026). No source in this deep dive publishes error rates, override rates or parallel-run results for a substantive-testing tool. Parallel running is mentioned (CTRLCOUNCIL-WSJ-2026; TR-STATE-2026) but its results are not published.
- **Journal-entry testing is the one area where regulators confirm routine use.** IFIAR members reported frequently seeing technology in journal-entry testing in 88% of cases in the 2024 survey, against 55% for substantive procedures on accounts such as revenue or inventory (IFIAR-TTF-2025). The same report says 31% of members had findings that tools were not used as intended, most often misread results and thin testing of outliers.
- **Standard-setters are treating whole-population testing as a way to find items to investigate, not as a replacement for evidence rules.** The IAASB's draft ISA 520 says auditors commonly analyse entire populations of transactions with technological tools to sharpen risk identification (IAASB-ED520-2026, para 23). Its draft ISA 500 explains that the board chose guidance over a technology requirement because GenAI-enabled tools strain the "input-output model" of evidence (IAASB-ED500-2026, paras 67-69).
- **The worries cluster around five themes:** automation bias and erosion of skepticism (including the junior pipeline); probabilistic tools in a profession that wants repeatability; AI checking AI; authenticity of evidence; and fee/economic pressure (NYSSCPA-BOTIC-2025; ICAEW-FRCVIEW-2026; NYENRODE-QUALITY-2026; VERDANTIX-KPMGFEE-2026).
- **Confirmations and inventory are where standard-setters are most concrete.** SAS No. 150 (published 13 Jul 2026) adds a requirement to confirm third-party-held cash unless conditions exist and recognises direct access to a knowledgeable external source (JOFA-SAS150-2026). The IAASB's March 2026 project proposal names drones and camera systems for inventory attendance and weak authentication in electronic confirmation systems (IAASB-500SERIES-2026).
- **Use cases:** 18 (1 A, 6 B, 5 C, 6 D). Only one grade A, and it is a single practitioner's time saving published in a vendor release.

---

## 2. Use cases

```yaml
- id: assurance-substantive-testing-01
  title: "Journal-entry testing on the full entry population with AI/ML anomaly detection, flagged entries followed up by auditors"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Ledgers hold very large numbers of journal entries, so sample-based or filter-only testing covers a small share of the population and leaves unusual entries to chance."
  solution: "Tools score or flag every entry in the population and the auditor investigates the flagged items and decides how far to test outliers. Regulators say this is the audit area where they most often see technology. EY says its Canvas platform processes more than 1.4 trillion lines of journal-entry data a year. A vendor (MindBridge) describes unsupervised models surfacing rare account pairings, volume spikes and unusual coding."
  outcomes:
    - lever: quality
      description: "Regulators frequently see technology used in journal-entry testing; this is a prevalence measure, not an accuracy or quality result."
      figure: "88%"
      measures: "Share of IFIAR members (48 responding, 2024 annual survey) reporting that automated tools and techniques are 'frequently observed' in journal entry testing in audit files; 86% of 49 members in 2023."
      provenance: independent
      source_ref: IFIAR-TTF-2025
    - lever: risk
      description: "Inspection findings on tool use across all audit areas, with misread results and limited testing of outliers the most frequent themes."
      figure: "31%"
      measures: "Share of IFIAR members reporting findings that the automated tool or technique was not used as intended in 2024 (29% in 2023). The source does not break this out by journal-entry testing."
      provenance: independent
      source_ref: IFIAR-TTF-2025
    - lever: capacity
      description: "Scale of journal-entry data processed on one Big Four platform."
      figure: "1.4 trillion lines per year"
      measures: "Lines of journal-entry data processed per year by the EY Canvas platform, as reported by CPA Practice Advisor from EY's 7 Apr 2026 release."
      provenance: self-reported
      source_ref: EY-CANVAS-2026
  prerequisites:
    - "A complete journal-entry and ledger extract reconciled to the trial balance (JOFA-EXCELAGENT-2026)."
    - "Access to client systems and usable client data; US small and mid-size firms cite poor client data (60%) and lack of access to client systems (53%) among top blockers (CPACOM-ATR-2025)."
  risks_and_guardrails:
    - "IFIAR members' most frequent technology findings were misinterpreting tool results and insufficient testing of outliers (IFIAR-TTF-2025)."
    - "Fraud is a rare event, which is hard for pattern-based tools; one academic commentator suggests pairing fraud specialists with data-driven tools (NYENRODE-QUALITY-2026)."
  human_checkpoints:
    - "Auditor decides which flagged entries to investigate and the extent of outlier testing (IFIAR-TTF-2025)."
    - "Fraud specialists on the team interpret signals (NYENRODE-QUALITY-2026)."
  role_evolution: "Less selecting and testing of sampled entries; more investigating flagged items and judging whether outlier follow-up is sufficient (IFIAR-TTF-2025)."
  evidence_grade: B
  sources:
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: 2025-03-27, access: full, locator: "Section 'IFIAR Members are seeing an increased use of technology in the audit', 2023 and 2024 tables and findings paragraph, pp. 5-6" }
    - { ref: EY-CANVAS-2026, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: 2026-04-07, access: full, locator: "Paragraphs 1-3 (1.4 trillion lines; 130,000 professionals)" }
    - { ref: MINDBRIDGE-FAKEINV-2025, title: "Fake Invoices, Real Risks: Why Auditors Must Rethink Their Approach in the Age of AI", publisher: MindBridge, type: vendor, url: "https://www.mindbridge.ai/blog/fake-invoices-real-risks-why-auditors-must-rethink-their-approach-in-the-age-of-ai", date: 2025-04-15, access: full, locator: "Section 'The Machine Learning Advantage'" }
    - { ref: NYENRODE-QUALITY-2026, title: "AI in auditing: balancing quality, professional skepticism, and responsibility", publisher: Nyenrode Business University, type: academic, url: "https://www.nyenrode.nl/en/news/n/ai-auditing-quality-skepticism-responsibility", date: 2026-06-18, access: full, locator: "Section 'Can AI detect fraud effectively?'" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: AICPA and CPA.com, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "Blockers chart (PDF p. 9)" }
    - { ref: JOFA-EXCELAGENT-2026, title: "Using an Excel agent to clean, validate, and reconcile data", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/", date: 2026-10-01, access: full, locator: "Introduction (journal-entry populations prepared for testing; completeness reconciled to trial balance)" }
  last_reviewed: 2026-10-16
  notes: "Grade B: regulator observation of use and a named platform, but no published measurement of detection quality. The 88% is observation frequency by inspectors, not an outcome. MindBridge material is vendor-published and used only to describe the technique."

- id: assurance-substantive-testing-02
  title: "Agents run routine substantive tests (expense vouching, unrecorded liabilities, payroll, receivables) with orchestration agents and human review"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Routine testing (payroll, expense vouching, cash, unrecorded liabilities, receivables) has been done by pulling a finite sample, extracting data to a spreadsheet, applying audit guidance and marking pass or fail, which absorbs junior staff time."
  solution: "KPMG announced agents in Clara in Apr 2025 for expense vouching and search for unrecorded liabilities and accrued expenses. In Apr 2026 KPMG leaders described a next step where orchestration agents manage several testing agents, starting with a pilot in summer 2026 and full deployment on certain tests the following year; humans would still review, collect data and assess risk."
  outcomes:
    - lever: capacity
      description: "No measured outcome published. Forecast only: some Big Four firm leaders estimate agents will contribute 20-30% of a typical financial audit by 2029."
      figure: "20-30% (forecast)"
      measures: "Estimated share of a typical financial audit's human effort removed by agents by 2029, attributed by the WSJ to 'some Big Four firm leaders' (not a measured result)."
      provenance: self-reported
      source_ref: CTRLCOUNCIL-WSJ-2026
  prerequisites:
    - "Evidence ingestion that copes with many document formats (PWC-AT-2025)."
    - "Parallel runs alongside human testing to compare results (CTRLCOUNCIL-WSJ-2026)."
  risks_and_guardrails:
    - "UK FRC guidance says the human auditor remains accountable (CTRLCOUNCIL-WSJ-2026)."
    - "Deloitte's public stance in the same reporting is more conservative: quality depends on human judgment, skepticism and accountability (CTRLCOUNCIL-WSJ-2026)."
  human_checkpoints:
    - "Humans review test results, handle data collection and risk assessment; only routine testing was shown with no human team within two to three years in a KPMG briefing slide (CTRLCOUNCIL-WSJ-2026)."
  role_evolution: "KPMG's audit chief digital officer said he would not hire a graduate to create workpapers and wants people who can understand a workpaper's findings with AI help (CTRLCOUNCIL-WSJ-2026)."
  evidence_grade: B
  sources:
    - { ref: CTRLCOUNCIL-WSJ-2026, title: "Why Audit Firms Are Rewriting the Role of the Modern Accountant (reproduces WSJ, 'In This Critical Part of Audits, the Accountant's Role Is Shrinking Fast', Mark Maurer, 2026-04-10)", publisher: Controllers Council, type: press, url: "https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/", date: 2026-05-08, access: full, locator: "KPMG paragraphs (orchestration agents, summer pilot, 'next year'), routine-testing definition paragraph, 20-30% by 2029 paragraph; read via text mirror, WSJ original not opened" }
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: 2025-04-22, access: full, locator: "Highlights and paragraph beginning 'The AI agents deployed in this announcement'" }
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "Paragraph on Evidence Match ('ingest 20 different kinds of documents')" }
  last_reviewed: 2026-10-16
  notes: "Tense matters: the Apr 2025 Clara agents were announced as deployed; the orchestration phase is described in Apr 2026 as a pilot with deployment on certain tests planned for 2027. WSJ also says AI agents have been used for testing in recent years but in a limited way, prompted by people. The WSJ text was read through a republished copy, so wording should be checked against the original before external use."

- id: assurance-substantive-testing-03
  title: "Evidence matching: AI extracts, matches and documents sampled items against supporting documents and bank activity"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Vouching sampled transactions to invoices, contracts and bank records means opening many differently formatted documents and tracing amounts by hand; a single customer payment may cover several invoices."
  solution: "PwC's Evidence Match extracts and matches evidence against documents for high-volume areas such as cash, receivables and payables and records an evidence trail. Thomson Reuters' Audit Intelligence Test (built with Valid8 Financial) matches samples to supporting evidence and traces recorded transactions to banking activity, including one payment matched to several invoices."
  outcomes:
    - lever: speed
      description: "A sole practitioner reports engagement time for organising client material and running tests falling from about two days to five or six hours."
      figure: "about 16 hours to 5-6 hours per engagement"
      measures: "Time for one named practitioner (Oberlander Financial Services PLLC) to organise client materials and run tests per engagement, before and after Audit Intelligence Test, quoted in the vendor's press release; single self-estimate."
      provenance: vendor-published
      source_ref: TR-AGENTIC-2025
    - lever: capacity
      description: "PwC statements about the evidence-matching tool's document coverage; the two accounts differ and are not easy to reconcile."
      figure: "20 document types (Oct 2025 account); 30 document types (Apr 2026 account)"
      measures: "Number of kinds of client document the Evidence Match tool can read, as stated by a PwC partner to Accounting Today (20) and by PwC's US assurance transformation leader to the WSJ (30; the WSJ adds the tool could only read basic PDFs six months earlier)."
      provenance: self-reported
      source_ref: CTRLCOUNCIL-WSJ-2026
  prerequisites:
    - "Client documents and bank data available electronically; the firm built the tool for messy real-world files ('the client may hand you a napkin' per a PwC partner) (PWC-AT-2025)."
  risks_and_guardrails:
    - "Matching evidence that looks right is weaker if the document is forged; practitioners urge corroboration with bank records and vendor data (MINDBRIDGE-FAKEINV-2025; TR-BANKCONF-2026)."
  human_checkpoints:
    - "Each match carries an evidence trail that the auditor can review (PWC-AT-2025)."
  role_evolution: "Not described in the sources beyond the tool taking over extraction and matching (PWC-AT-2025)."
  evidence_grade: A
  sources:
    - { ref: TR-AGENTIC-2025, title: "Thomson Reuters launches agentic AI solutions to transform tax, audit and accounting workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html", date: 2025-11, access: full, locator: "Section 'Audit Intelligence Test' and Oberlander quote; day not shown on the page, month from the URL" }
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: 2025-10-28, access: full, locator: "Paragraphs on Evidence Match (Maryanski)" }
    - { ref: CTRLCOUNCIL-WSJ-2026, title: "Why Audit Firms Are Rewriting the Role of the Modern Accountant", publisher: Controllers Council, type: press, url: "https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/", date: 2026-05-08, access: full, locator: "PwC paragraph on the evidence-match tool (30 types of documents)" }
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: 2026-10-07, access: full, locator: "Paragraph on Simplified Audit - Execute and the paragraph quoting 'It's not that drastic yet'" }
    - { ref: MINDBRIDGE-FAKEINV-2025, title: "Fake Invoices, Real Risks: Why Auditors Must Rethink Their Approach in the Age of AI", publisher: MindBridge, type: vendor, url: "https://www.mindbridge.ai/blog/fake-invoices-real-risks-why-auditors-must-rethink-their-approach-in-the-age-of-ai", date: 2025-04-15, access: full, locator: "Section 'What This Means for Auditors and the Audit Process'" }
    - { ref: TR-BANKCONF-2026, title: "Audit in an AI World: AI is raising the stakes for electronic bank confirmations", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/why-ai-is-raising-the-stakes-for-bank-confirmations/", date: 2026-09-02, access: full, locator: "Section 'Appearance is not authentication'" }
  last_reviewed: 2026-10-16
  notes: "Weak A: the only measured time saving is one sole practitioner's estimate in a vendor press release, with no accuracy or error data. PwC's own overall verdict a year on is 'some time savings' that are 'not that drastic yet' (CFODIVE-PWC-2026), stated for the AI-assisted audit overall rather than for this step. The 20 versus 30 document types and the 'basic PDFs six months ago' remark (WSJ) conflict on timing; the Accounting Today partner speaks in the past tense about what the team 'had to build'. PwC's Simplified Audit - Execute tool reads supporting documents and flags missing information (CFODIVE-PWC-2026); no outcome figures published. TR early adopters reported up to 70% faster preparation and review for a different product (CoCounsel Document Analysis), so that figure is not used here."

- id: assurance-substantive-testing-04
  title: "AI-targeted sample selection: risk-scoring a population so the sample concentrates on higher-risk items"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Random or judgmental samples may miss the items most likely to be misstated, and reading every contract or record to find them is not practical."
  solution: "In the FRC's illustrative example, an LLM-based workflow extracts risk indicators from each revenue contract, a computation step scores contracts, and contracts above a threshold form the sample the auditor tests. A practitioner using Thomson Reuters tools says Audit Intelligence Test used with Audit Intelligence Analyze significantly improves sample selection and testing."
  outcomes:
    - lever: quality
      description: "No measurement published. The practitioner statement is qualitative."
      figure: "none published"
      measures: "Not applicable; the customer says the tools 'significantly enhance' sample selection and testing (Oberlander Financial Services PLLC, in a vendor release)."
      provenance: vendor-published
      source_ref: TR-AGENTIC-2025
  prerequisites:
    - "Contracts or records in a form the tool can chunk and index; prewritten, tested prompts for each risk indicator; certification of the tool across sectors and contract types (FRC-GENAI-2026)."
  risks_and_guardrails:
    - "The FRC example expects the audit file to record that an AI-enabled tool was used to select the sample, the criteria for its use, which contracts were selected and the indicators present (FRC-GENAI-2026)."
    - "A risk-scored sample remains a sample; the FRC example shows AI improving targeting, not replacing the sample (FRC-GENAI-2026)."
  human_checkpoints:
    - "The auditor sees which risk indicators were present for each contract and tests the selected contracts (FRC-GENAI-2026)."
  role_evolution: "Not described in the sources; in the FRC example the auditor still tests the selected contracts (FRC-GENAI-2026)."
  evidence_grade: B
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "Illustrative example 2: Contract review, pp. 49-59" }
    - { ref: TR-AGENTIC-2025, title: "Thomson Reuters launches agentic AI solutions to transform tax, audit and accounting workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html", date: 2025-11, access: full, locator: "Oberlander quote" }
  last_reviewed: 2026-10-16
  notes: "The FRC example is an illustrative scenario written by the regulator, not a reported deployment. The named-deployment basis for grade B is the Oberlander testimonial, which is thin."

- id: assurance-substantive-testing-05
  title: "Contract and lease review at volume: AI reads many contracts and flags differences or missing terms for revenue and lease testing"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Checking many contracts (for example 100 leases of which 15 differ slightly) or contracts spanning hundreds of pages for revenue recognition is repetitive and slow."
  solution: "Thomson Reuters announced CoCounsel Document Analysis in Nov 2025 with early adopters, and its audit product head says AI can already do much of the lease-checking work. EY's assurance AI leader expects agents to catch inconsistencies in revenue contracts of hundreds of pages. The FRC's guidance gives a lease-detection tool as its example of a misinterpretation risk."
  outcomes:
    - lever: speed
      description: "Early adopters of a document-analysis product report faster preparation and review; not specific to contract testing."
      figure: "up to 70% faster"
      measures: "Early-adopter customers' time for audit workpaper preparation and review using CoCounsel Document Analysis, per Thomson Reuters' press release; unnamed customers; adjacent to contract review."
      provenance: vendor-published
      source_ref: TR-AGENTIC-2025
  prerequisites:
    - "Contracts digitised; prompts and checks tailored to contract types and terminology (FRC-GENAI-2026)."
  risks_and_guardrails:
    - "The FRC warns an auditor may take a tool's lease summary as complete and skip other procedures to find present obligations such as provisions (FRC-GENAI-2026)."
    - "An ICAEW technology-faculty chair says an auditor still has to apply judgement after AI contract checking (ICAEW-FRCVIEW-2026)."
  human_checkpoints:
    - "Auditor applies judgement to the AI's findings and decides what further procedures are needed (ICAEW-FRCVIEW-2026)."
  role_evolution: "Thomson Reuters product leaders say professionals' time shifts from hours of document review toward analysis and judgment (TR-STATE-2026; vendor view)."
  evidence_grade: C
  sources:
    - { ref: TR-STATE-2026, title: "The state of AI in audit in 2026: Interview with experts", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/", date: 2026-03-30, access: full, locator: "Question 2 (Cobbe: 100 leases, 15 slightly different)" }
    - { ref: TR-AGENTIC-2025, title: "Thomson Reuters launches agentic AI solutions", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html", date: 2025-11, access: full, locator: "Section on CoCounsel Document Analysis" }
    - { ref: CTRLCOUNCIL-WSJ-2026, title: "Why Audit Firms Are Rewriting the Role of the Modern Accountant", publisher: Controllers Council, type: press, url: "https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/", date: 2026-05-08, access: full, locator: "EY paragraphs (Jackson: contracts spanning hundreds of pages)" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: 2026-03-30, access: full, locator: "Misinterpretation of output risk, p. 18" }
    - { ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05-06, access: full, locator: "Section 'Misinterpretation or misuse will take the most work'" }
  last_reviewed: 2026-10-16
  notes: "Grade C: vendor statements and a firm leader's expectation; no named audit deployment with results found for contract review itself. EY's remark is a forward-looking expectation ('will improve'), not a reported result."

- id: assurance-substantive-testing-06
  title: "Agents test complex revenue (for example pharmaceutical rebates) beyond routine vouching"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Revenue with complex terms such as rebates needs judgment-heavy testing that routine tools did not cover."
  solution: "PwC's US assurance transformation leader said the firm was attempting to apply AI agents to assess whether US pharmaceutical rebate revenue was recorded properly, and expects agents to take on tasks with more judgment over time with human oversight."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: self-reported
      source_ref: CTRLCOUNCIL-WSJ-2026
  prerequisites:
    - "Tools that can ingest many client document types (CTRLCOUNCIL-WSJ-2026)."
  risks_and_guardrails:
    - "PwC's leader said humans would continue to provide oversight as agents take on more judgment (CTRLCOUNCIL-WSJ-2026)."
  human_checkpoints:
    - "Human oversight of agent testing (CTRLCOUNCIL-WSJ-2026)."
  role_evolution: "Not described beyond oversight (CTRLCOUNCIL-WSJ-2026)."
  evidence_grade: B
  sources:
    - { ref: CTRLCOUNCIL-WSJ-2026, title: "Why Audit Firms Are Rewriting the Role of the Modern Accountant", publisher: Controllers Council, type: press, url: "https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/", date: 2026-05-08, access: full, locator: "PwC paragraph (Panson, pharmaceutical rebates)" }
  last_reviewed: 2026-10-16
  notes: "Grade B is generous: one sentence from a named firm leader about an attempt, reported second-hand. The source says 'attempting', so maturity is piloting at most."

- id: assurance-substantive-testing-07
  title: "Auditor agents and client agents exchange evidence requests and supporting detail, with auditors reviewing the resulting workpapers"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Selecting items, requesting support from the client, chasing it and assembling workpapers is manual and slow."
  solution: "EY described pilots in which its agents make preliminary selections of financial statement data and requests for supporting information; clients' agents collect the support and send it back; EY's agents prepare workpapers that humans review. EY also embedded a multi-agent framework in Canvas, with end-to-end support expected by 2028."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: self-reported
      source_ref: CTRLCOUNCIL-WSJ-2026
  prerequisites:
    - "Clients with their own agents or digital evidence stores (CTRLCOUNCIL-WSJ-2026)."
  risks_and_guardrails:
    - "Agent-to-agent evidence exchange raises the authenticity questions practitioners raise about evidence generally (TR-BANKCONF-2026)."
  human_checkpoints:
    - "Humans review the workpapers the agents prepare (CTRLCOUNCIL-WSJ-2026)."
  role_evolution: "Not described beyond review (CTRLCOUNCIL-WSJ-2026)."
  evidence_grade: B
  sources:
    - { ref: CTRLCOUNCIL-WSJ-2026, title: "Why Audit Firms Are Rewriting the Role of the Modern Accountant", publisher: Controllers Council, type: press, url: "https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/", date: 2026-05-08, access: full, locator: "EY paragraphs (agents talking with clients' agents; 'changes being piloted now')" }
    - { ref: EY-CANVAS-2026, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: 2026-04-07, access: full, locator: "Paragraphs 3-4 (all phases now; end-to-end by 2028)" }
    - { ref: TR-BANKCONF-2026, title: "Audit in an AI World: AI is raising the stakes for electronic bank confirmations", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/why-ai-is-raising-the-stakes-for-bank-confirmations/", date: 2026-09-02, access: full, locator: "Section 'Appearance is not authentication'" }
  last_reviewed: 2026-10-16
  notes: "The WSJ text says the agent-to-agent exchange is in changes 'being piloted now'; EY's separate release says AI is embedded in all phases of the audit through Canvas and is expected to support all end-to-end activities by 2028. These are different claims and should not be merged."

- id: assurance-substantive-testing-08
  title: "Substantive analytics on whole populations with more precise expectations from detailed or unstructured data"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "High-level analytics lack the precision to detect a material misstatement, and most small and mid-size US firms have no automated substantive-analytics tool."
  solution: "Draft ISA 520 says auditors commonly analyse entire populations with technological tools, and its application material shows tools building a more precise expectation from industry reports or from seasonal revenue and cost patterns. Internal audit commentary (Deloitte Netherlands) and KPMG's SOX paper describe 100% transaction coverage 'where data quality allows' or 'where appropriate'."
  outcomes:
    - lever: quality
      description: "Adoption is low among US small and mid-size firms; this is a prevalence figure, not an outcome."
      figure: "11%"
      measures: "Share of the 54 US firms with complete data in the AICPA/CPA.com 2025 Audit Benchmark that report an automated solution for substantive analytics (22% had none, 89% said they were not using technology to enable substantive analytics)."
      provenance: independent
      source_ref: CPACOM-ATR-2025
  prerequisites:
    - "Data of sufficient quality and access to client systems (DELOITTE-NL-SAMPLE-2026; CPACOM-ATR-2025)."
  risks_and_guardrails:
    - "The IAASB says GenAI-enabled tools may make it impossible to fully evaluate inputs or confirm the tool operates as designed, and chose guidance rather than a requirement (IAASB-ED500-2026)."
    - "Deloitte Netherlands says tools and models must be validated and outputs traceable, and the underlying data must be of sufficient quality (DELOITTE-NL-SAMPLE-2026)."
  human_checkpoints:
    - "Auditor investigates unusual or unexpected relationships the tool surfaces (IAASB-ED520-2026)."
  role_evolution: "Deloitte Netherlands says AI reduces the mechanical workload and lets experienced auditors focus on judgement and investigation (internal-audit context) (DELOITTE-NL-SAMPLE-2026)."
  evidence_grade: C
  sources:
    - { ref: IAASB-ED520-2026, title: "Exposure Draft: Proposed ISA 520 (Revised), Analytical Procedures", publisher: IAASB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-520-Exposure-Draft.pdf", date: 2026-08, access: full, locator: "Explanatory memorandum paras 5 and 23 (pp. 6, 10); application material A20 (p. 22)" }
    - { ref: IAASB-ED500-2026, title: "Exposure Draft: Proposed ISA 500 (Revised), Audit Evidence", publisher: IAASB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf", date: 2026-08, access: full, locator: "Explanatory memorandum section 1-F, paras 65-69 (p. 20)" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: AICPA and CPA.com, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "Automated-solutions chart (PDF p. 10) and section 'Risk-driven approach and technology' (report p. 19)" }
    - { ref: DELOITTE-NL-SAMPLE-2026, title: "From sample to full-population examination: what AI changes for the third line", publisher: Deloitte Netherlands, type: firm, url: "https://www.deloitte.com/nl/en/Industries/financial-services/perspectives/from-sample-to-full-population-examination.html", date: 2026-09-16, access: full, locator: "Sections 'What broader coverage actually enables' and 'Transaction testing'" }
    - { ref: KPMG-SOX-2026, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: 2026-09-24, access: full, locator: "Point of view #4: Scalable, AI-enabled testing" }
  last_reviewed: 2026-10-16
  notes: "Grade C, with the Deloitte and KPMG items capped because they describe internal audit and SOX controls respectively (adjacent processes). The IAASB drafts are exposure drafts (comments due 15 Dec 2026 per the landscape), not final standards. The ED text frames whole-population analysis mainly as aiding risk identification and identifying items for further investigation; it does not say full-population testing replaces sufficient appropriate evidence."

- id: assurance-substantive-testing-09
  title: "An agent in Excel cleans, validates and reconciles client general-ledger data to the trial balance before substantive procedures"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Raw client data arrives with mixed fields, inconsistent dates, blank rows and irrelevant headers, and preparing it is repetitive, slow and error-prone."
  solution: "Two accounting academics built a ChatGPT-for-Excel agent with a written 'skill' that forces a plan, asks for approval before changing data, uses reviewable spreadsheet formulas, reconciles to the trial balance and writes plain-English documentation for the reviewer. They also name Claude for Excel and DataSnipper as similar tools."
  outcomes:
    - lever: speed
      description: "Simulated clean, validate and reconcile of a general ledger extract took about ten minutes against many hours manually, according to the authors."
      figure: "about 10 minutes (59,157 rows)"
      measures: "Average time for the Excel agent to clean, validate and reconcile 59,157 rows of simulated transaction-level general ledger data to a trial balance; simulation adapted from a published case study, not a live engagement."
      provenance: independent
      source_ref: JOFA-EXCELAGENT-2026
  prerequisites:
    - "Enterprise-level licences for audit use (JOFA-EXCELAGENT-2026)."
    - "Client data access; US firms cite poor client data (60%) and no access to client systems (53%) as blockers, and 19% have an automated data-ingestion solution (CPACOM-ATR-2025)."
  risks_and_guardrails:
    - "The authors require an agent-prepared plan and human approval before any data change, and reviewable formulas (JOFA-EXCELAGENT-2026)."
  human_checkpoints:
    - "Auditor approves the plan, reviews the reconciliation and the generated documentation (JOFA-EXCELAGENT-2026)."
  role_evolution: "Managers and partners refine the agent's 'skills' from staff feedback, comparable to maintaining a procedure manual (JOFA-EXCELAGENT-2026)."
  evidence_grade: C
  sources:
    - { ref: JOFA-EXCELAGENT-2026, title: "Using an Excel agent to clean, validate, and reconcile data", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/", date: 2026-10-01, access: full, locator: "Introduction and 'The simulated case'; Steps 1-5" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: AICPA and CPA.com, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "Blockers chart and automated-solutions chart (PDF pp. 9-10)" }
  last_reviewed: 2026-10-16
  notes: "Authors are Gang (Ernest) Pan and Li Wang, University of Akron. The result is a demonstration on simulated data, so it is capped at C; no firm deployment is named."

- id: assurance-substantive-testing-10
  title: "Authenticated electronic and direct-access confirmations replace PDFs, screenshots and paper replies as AI makes forgery cheap"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Much 'external' evidence reaches auditors as a screenshot, a PDF, an email or a scanned letter, any of which can now be forged or intercepted cheaply."
  solution: "Platforms authenticate the source of a confirmation response and the path it takes to the auditor. SAS No. 150 recognises direct access to information from a knowledgeable external source as a way to meet confirmation requirements and adds a requirement to confirm third-party-held cash unless conditions exist. A Thomson Reuters regional head (vendor) argues confirmation should be a planning-stage decision about where trust must be airtight."
  outcomes:
    - lever: risk
      description: "Adoption of confirmation automation among US small and mid-size firms; a prevalence figure."
      figure: "39%"
      measures: "Share of the 54 US firms with complete data in the AICPA/CPA.com 2025 Audit Benchmark that have an automated solution for confirmations."
      provenance: independent
      source_ref: CPACOM-ATR-2025
  prerequisites:
    - "Banks and other third parties responding through authenticated channels; Thomson Reuters says many banks eliminated paper confirmation responses (TR-BANKSTATE-2026)."
  risks_and_guardrails:
    - "The IAASB's Mar 2026 proposal notes electronic or automated confirmation systems may lack sufficient authentication and requests or responses may be intercepted or manipulated (IAASB-500SERIES-2026)."
    - "Negative confirmations get new conditions under SAS No. 150 (JOFA-SAS150-2026)."
  human_checkpoints:
    - "Auditor keeps control of the confirmation request and judges reliability of responses (IAASB-500SERIES-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: C
  sources:
    - { ref: TR-BANKCONF-2026, title: "Audit in an AI World: AI is raising the stakes for electronic bank confirmations", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/why-ai-is-raising-the-stakes-for-bank-confirmations/", date: 2026-09-02, access: full, locator: "Sections 'Screenshots, PDFs, and paper' and 'Why end-to-end validated electronic confirmation matters'" }
    - { ref: TR-BANKSTATE-2026, title: "The state of bank confirmations in 2026", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/the-state-of-bank-confirmations-2026/", date: 2026-03-02, access: full, locator: "Sections on PCAOB AS 2310 and 'The permanent shift from paper to electronic'" }
    - { ref: JOFA-SAS150-2026, title: "AICPA updates audit standards related to external confirmations", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/jul/aicpa-updates-audit-standards-related-to-external-confirmations/", date: 2026-07-14, access: full, locator: "Paragraphs 1-6 (SAS No. 150, effective for periods ending on or after 15 Dec 2028)" }
    - { ref: IAASB-500SERIES-2026, title: "Project proposal to revise audit evidence standards related to inventory and external confirmations (Agenda Item 4-D)", publisher: IAASB, type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/20260316-Agenda-Item-4D-500Series-Project-Proposal-%28Approved%29.pdf", date: 2026-03-16, access: full, locator: "Problem statement items (g), (h), (j), PDF p. 6" }
    - { ref: CPACOM-ATR-2025, title: "2025 Audit Transformation Report", publisher: AICPA and CPA.com, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "Automated-solutions chart (PDF p. 10)" }
  last_reviewed: 2026-10-16
  notes: "No named audit firm deployment appears in the opened sources; in-production maturity rests on the survey, the standard-setters' statements about increasing intermediary use and the vendor's product. Thomson Reuters is a confirmation vendor, so its fraud framing is advocacy. TR's page says AS 2310 permits direct access and legitimises electronic platforms (TR-BANKSTATE-2026); the PCAOB standard text itself was not opened. The vendor also cites TRI research that almost 43% of detected fraud attempts on financial institutions use AI and 29% of these succeed (TR-BANKCONF-2026); that statistic was not traced to the underlying research."

- id: assurance-substantive-testing-11
  title: "Corroborate documents against bank records, vendor master data and approval logs across the whole population to catch fabricated evidence"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "A clean-looking invoice or vendor file no longer signals legitimacy because generative tools produce convincing documents, W-9 forms and vendor websites."
  solution: "Practitioners advise matching invoice details against bank records, vendor histories, approval logs and system metadata, scanning vendor masters for suspicious entries (such as a P.O. box address or a bank account shared by apparent vendors), and testing full populations because fraud can be automated and widespread."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: vendor-published
      source_ref: MINDBRIDGE-FAKEINV-2025
  prerequisites:
    - "Access to bank, vendor-master and approval-log data; a tidy vendor master (JOFA-APFRAUD-2026)."
  risks_and_guardrails:
    - "Technological defences carry their own attack paths such as data poisoning and prompt injection (JOFA-APFRAUD-2026)."
  human_checkpoints:
    - "Out-of-band verification of suspicious items (JOFA-APFRAUD-2026)."
  role_evolution: "A BDO forensic practitioner says AI will not testify in court or sign off financial statements, so the CPA's value remains skepticism and judgment (JOFA-APFRAUD-2026)."
  evidence_grade: C
  sources:
    - { ref: MINDBRIDGE-FAKEINV-2025, title: "Fake Invoices, Real Risks: Why Auditors Must Rethink Their Approach in the Age of AI", publisher: MindBridge, type: vendor, url: "https://www.mindbridge.ai/blog/fake-invoices-real-risks-why-auditors-must-rethink-their-approach-in-the-age-of-ai", date: 2025-04-15, access: full, locator: "Section 'What This Means for Auditors and the Audit Process'" }
    - { ref: JOFA-APFRAUD-2026, title: "A guide to fighting AI-fueled AP/AR fraud", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/jul/a-guide-to-fighting-ai-fueled-ap-ar-fraud/", date: 2026-07-01, access: full, locator: "Sections 'More advanced vendor and customer impersonation', 'Maintain the master file', 'Embrace technology - appropriately'" }
  last_reviewed: 2026-10-16
  notes: "The JofA piece is written from the preparer and forensic-investigator side (management's controls), so it is adjacent to audit procedures. The MindBridge post is vendor marketing and dates from Apr 2025, at the start of the 18-month window."

- id: assurance-substantive-testing-12
  title: "Idea: forensic checks of document authenticity (metadata, provenance, AI-alteration signals) before documents are used as audit evidence"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Documents can be generated or altered with synthetic signatures and fabricated metadata, so evidence quality cannot be assumed."
  solution: "Practitioners propose a zero-trust starting point for documents: verify authenticity, metadata and provenance independently before relying on them. A forensic investigator notes that mainstream tools can be asked to look for watermarks showing AI alteration and expects this to appear in enterprise software."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: self-reported
      source_ref: ISACA-EVIDENCE-2026
  prerequisites:
    - "Independent routes to the originating system or party (ISACA-EVIDENCE-2026)."
  risks_and_guardrails:
    - "Detection tools still need governance and human review, per a search-result summary of a Wolters Kluwer article (WOLTERSKLUWER-EVIDENCE-2026; not opened)."
  human_checkpoints:
    - "Auditor decides whether evidence is authentic enough to rely on (ISACA-EVIDENCE-2026)."
  role_evolution: "Auditors must be equipped to challenge evidence that looks 'perfect' (ISACA-EVIDENCE-2026)."
  evidence_grade: D
  sources:
    - { ref: ISACA-EVIDENCE-2026, title: "The Audit Evidence Crisis: How AI Deepfakes Are Rewriting Assurance Standards", publisher: ISACA Now Blog, type: professional-body, url: "https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards", date: 2026-06-08, access: full, locator: "Introduction and 'Why a Zero-Trust Approach is Essential'" }
    - { ref: JOFA-APFRAUD-2026, title: "A guide to fighting AI-fueled AP/AR fraud", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/jul/a-guide-to-fighting-ai-fueled-ap-ar-fraud/", date: 2026-07-01, access: full, locator: "Section 'Embrace technology - appropriately' (Chee on watermark scanning)" }
    - { ref: WOLTERSKLUWER-EVIDENCE-2026, title: "AI-generated audit evidence: rethinking trust and authenticity", publisher: Wolters Kluwer, type: vendor, url: "https://www.wolterskluwer.com/en/expert-insights/ai-generated-audit-evidence-rethinking-trust-authenticity", date: 2026-05-06, access: search-only, locator: "Search-result summary only; page returned 403" }
  last_reviewed: 2026-10-16
  notes: "Idea label (grade D): discussed by practitioners as a needed direction; no firm deployment or measured result found. The ISACA author, a CPA/CIA/CISA, describes one anecdote of receiving an AI-generated document and does not give a measured result. The Wolters Kluwer item is search-only and supports nothing above grade D."

- id: assurance-substantive-testing-13
  title: "Idea: technology-assisted attendance at inventory counts (drone footage, scanners, camera systems) as audit evidence"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, physical-field]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "ISA 501 is unclear whether 'attendance' at inventory counting can include remote observation using technology, so auditors are uncertain whether such practices meet the requirements."
  solution: "The IAASB's Mar 2026 project proposal lists drones, scanners and camera systems as examples of remote observation tools and asks whether the standard should put more weight on sufficiency and appropriateness of evidence regardless of how it is obtained."
  outcomes:
    - lever: cost
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: independent
      source_ref: IAASB-500SERIES-2026
  prerequisites:
    - "Revised standards or clear guidance on whether remote observation meets attendance requirements (IAASB-500SERIES-2026)."
  risks_and_guardrails:
    - "The IAASB wants to reinforce professional skepticism for inventory evidence (IAASB-500SERIES-2026)."
  human_checkpoints:
    - "Auditor judges sufficiency and appropriateness of evidence obtained by alternative means (IAASB-500SERIES-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
    - { ref: IAASB-500SERIES-2026, title: "Project proposal to revise audit evidence standards related to inventory and external confirmations (Agenda Item 4-D)", publisher: IAASB, type: standard-setter, url: "https://www.iaasb.org/_flysystem/azure-private/2026-03/20260316-Agenda-Item-4D-500Series-Project-Proposal-%28Approved%29.pdf", date: 2026-03-16, access: full, locator: "Inventory in ISA 501, items (a) and (b), PDF p. 5" }
  last_reviewed: 2026-10-16
  notes: "Idea label (grade D): a standard-setter's problem statement, not an audit-firm deployment. No firm deployment of drones or computer vision for inventory was found in the opened sources."

- id: assurance-substantive-testing-14
  title: "Idea: auditors weigh AI-reliant valuation specialist advice when evaluating management's estimates"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Experienced auditors may discount specialist advice that relies heavily on AI, which in experiments led them to accept more aggressive management estimates."
  solution: "Specialists use AI to support advice on estimates such as a fair-value discount rate; the research asks how auditors react. A brief exercise reminding auditors of their strongest professional skills reduced the defensive discounting."
  outcomes:
    - lever: quality
      description: "none published for live use; an experiment found auditors who first reflected on their weakest skills discounted AI-reliant specialist advice and accepted more aggressive estimates."
      figure: "none published"
      measures: "Not applicable; no figures are given in the practitioner summary."
      provenance: independent
      source_ref: ICPAS-PEECHER-2026
  prerequisites:
    - "Auditor digital-skills development alongside affirmation of core audit skills (ICPAS-PEECHER-2026)."
  risks_and_guardrails:
    - "Defensive reactions weakened rather than strengthened skepticism in the experiment (ICPAS-PEECHER-2026)."
  human_checkpoints:
    - "Auditor evaluates the specialist's advice and management's estimate (ICPAS-PEECHER-2026)."
  role_evolution: "The authors argue the future is 'duality' of traditional accounting and digital expertise (ICPAS-PEECHER-2026)."
  evidence_grade: D
  sources:
    - { ref: ICPAS-PEECHER-2026, title: "What's Really Behind AI Aversion in Auditing?", publisher: Illinois CPA Society, type: academic, url: "https://www.icpas.org/information/copy-desk/insight/article/digital-exclusive-2026/what-s-really-behind-ai-aversion-in-auditing", date: 2026-05-13, access: full, locator: "Sections 'Research Overview' and 'How AI Aversion Can Undermine Audit Quality'" }
  last_reviewed: 2026-10-16
  notes: "Idea label (grade D): the evidence is an experiment on auditor reactions summarised by its authors (Peecher, Pietsch, Stirnkorb, Yamoah), not a reported use of AI in estimate testing. The underlying paper was not opened. Estimate testing was the thinnest part of this module's discourse; the landscape's SSRN field experiment on inventory valuation was not reachable."

- id: assurance-substantive-testing-15
  title: "Idea: a second AI tool checks whether a first AI tool performed an audit procedure correctly"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Human reviewers cannot re-perform everything an AI tool does, and review capacity is limited."
  solution: "The AICPA practice aid says one AI tool may be used to perform a procedure and another to review whether it was performed correctly and the result makes sense, without reducing the auditor's supervision and review duties."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: independent
      source_ref: AT-AICPAPA-2026
  prerequisites:
    - "Firm quality-management policies for authorising, monitoring and revalidating AI tools (AT-AICPAPA-2026)."
  risks_and_guardrails:
    - "A PIA Group technology leader warns that using AI to validate AI can create a closed system in which errors are hard to detect (NYENRODE-QUALITY-2026)."
  human_checkpoints:
    - "The second tool does not replace the auditor's responsibilities for supervision and review (AT-AICPAPA-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "Paragraph beginning 'The guidance also said that, in an audit of financial statements, one AI tool may be used'" }
    - { ref: NYENRODE-QUALITY-2026, title: "AI in auditing: balancing quality, professional skepticism, and responsibility", publisher: Nyenrode Business University, type: academic, url: "https://www.nyenrode.nl/en/news/n/ai-auditing-quality-skepticism-responsibility", date: 2026-06-18, access: full, locator: "Section 'When is AI reliable enough?'" }
  last_reviewed: 2026-10-16
  notes: "Idea label (grade D): described in guidance as permissible; no deployment found. The Nyenrode piece is an opinion discussion sponsored by PIA Group's chair at the university."

- id: assurance-substantive-testing-16
  title: "Idea: agents check that management's memos and analyses agree with the underlying data"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Management memos and analyses can describe something in a way the underlying data does not support, and checking by hand across long documents is hard."
  solution: "EY's global and Americas assurance AI leader said agents will improve at spotting inconsistencies, and called the ability to flag a memo not supported by the underlying data 'incredibly powerful'."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: self-reported
      source_ref: CTRLCOUNCIL-WSJ-2026
  prerequisites:
    - "Agents that ingest unstructured documents and structured data together (CTRLCOUNCIL-WSJ-2026)."
  risks_and_guardrails:
    - "Probabilistic tools may not give the same output every time; RSM UK's audit data analytics director advises building a rules-based tool alongside AI for data analysis (ICAEW-FRCVIEW-2026)."
  human_checkpoints:
    - "Auditor reviews flagged inconsistencies (CTRLCOUNCIL-WSJ-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
    - { ref: CTRLCOUNCIL-WSJ-2026, title: "Why Audit Firms Are Rewriting the Role of the Modern Accountant", publisher: Controllers Council, type: press, url: "https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/", date: 2026-05-08, access: full, locator: "EY paragraph (Jackson on inconsistencies)" }
    - { ref: ICAEW-FRCVIEW-2026, title: "How helpful is FRC's guidance on generative and agentic AI?", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai", date: 2026-05-06, access: full, locator: "Section 'Use the illustrative examples' (Bukowski-Kruszyna)" }
  last_reviewed: 2026-10-16
  notes: "Idea label (grade D): a firm leader's expectation reported second-hand; no reported deployment or result."

- id: assurance-substantive-testing-17
  title: "Idea: substantive testing of AI-generated entity information, or tests of controls over it, when the client's own AI produces journal entries or accruals"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "When a client uses AI to categorise expenses, prepare accruals or review entries for anomalies, the auditor may not be able to see how the output was produced."
  solution: "The AICPA practice aid says an auditor may be able to substantively test AI outputs, and if that alone cannot give sufficient evidence, should test controls; where the process is a black box the auditor may need to establish relationships between inputs and outputs and explore non-traditional evidence sources."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable."
      provenance: independent
      source_ref: AT-AICPAPA-2026
  prerequisites:
    - "Understanding of the AI mechanism behind a control or information source, including whether it is deterministic or probabilistic (AT-AICPAPA-2026)."
  risks_and_guardrails:
    - "Model drift, data governance and probabilistic outcomes mean testing strategies may differ from traditional automated controls (AT-AICPAPA-2026)."
    - "The practice aid notes AI-enabled fraud risks such as generating fictitious documents to support nonexistent transactions (AT-AICPAPA-2026)."
  human_checkpoints:
    - "Auditor decides whether substantive tests alone suffice or controls must be tested (AT-AICPAPA-2026)."
  role_evolution: "Not described in the sources."
  evidence_grade: D
  sources:
    - { ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: 2026-10-14, access: full, locator: "Paragraphs on responding to AI risks and on audit evidence ('AI black box')" }
  last_reviewed: 2026-10-16
  notes: "Idea label (grade D): published guidance on how to respond, not a reported audit. The full practice aid sits behind an AICPA login and was not opened; this summary relies on Accounting Today's account. The AICPA says later additions will cover risk of material misstatement and evidence evaluation."

- id: assurance-substantive-testing-18
  title: "Internal audit agent 'swarms' and continuous full-population testing replace sample-based point-in-time tests"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Internal audit samples activity to judge firm-wide control, leaving concentrated risks unseen, and analytics and testing take staff time."
  solution: "A PayPal data-science leader discussed prompt libraries, AI agents and 'swarm auditing' to streamline analytics and testing in internal audit (podcast description). Deloitte Netherlands and KPMG describe whole-population and continuous testing for internal audit and SOX respectively."
  outcomes:
    - lever: capacity
      description: "Most chief audit executives are piloting or using AI; this is adoption, not an outcome of a testing change."
      figure: "83%"
      measures: "Share of audit functions piloting or using AI, from a Gartner survey of 119 chief audit executives in Aug 2025 (a further 12% plan to within the year)."
      provenance: vendor-published
      source_ref: GARTNER-2026
  prerequisites:
    - "Data quality and skills; Gartner says poor data quality and limited skills limit realised benefits (GARTNER-2026)."
    - "Validated tools with traceable outputs (DELOITTE-NL-SAMPLE-2026)."
  risks_and_guardrails:
    - "The podcast description cites a 'bridge tax', and governance and risk concerns, as practical challenges (SRA-SWARM-2026)."
    - "KPMG names auditing the black box and meaningful human oversight as challenges (KPMG-SOX-2026)."
  human_checkpoints:
    - "Human-in-the-loop oversight as controls become more automated (KPMG-SOX-2026)."
  role_evolution: "The podcast description says AI will shift internal auditors toward judgment, ethics and strategic oversight (SRA-SWARM-2026)."
  evidence_grade: B
  sources:
    - { ref: SRA-SWARM-2026, title: "How AI Agents are transforming internal audit (Richard Chambers with Richard Penfill of PayPal)", publisher: Speaking of Risk and Audit podcast, type: podcast, url: "https://srapodcast.podbean.com/e/swarm-auditing-how-ai-agents-are-transforming-internal-audit", date: 2026-02-11, access: full, locator: "Episode description only; audio and transcript not available" }
    - { ref: DELOITTE-NL-SAMPLE-2026, title: "From sample to full-population examination: what AI changes for the third line", publisher: Deloitte Netherlands, type: firm, url: "https://www.deloitte.com/nl/en/Industries/financial-services/perspectives/from-sample-to-full-population-examination.html", date: 2026-09-16, access: full, locator: "Sections 'Examples from current industry practice' and 'The case for acting'" }
    - { ref: KPMG-SOX-2026, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: 2026-09-24, access: full, locator: "Point of view #4 and 'Challenges on the horizon' 1-2" }
    - { ref: GARTNER-2026, title: "Gartner Survey Shows Audit Departments Are Embracing AI and Data Analytics to Drive Innovation in 2026", publisher: Gartner, type: survey, url: "https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-01-27-gartner-survey-shows-audit-departments-are-embracing-ai-and-data-analytics-to-drive-innovation-in-2026", date: 2026-01-27, access: full, locator: "Section 'AI in Audit'" }
  last_reviewed: 2026-10-16
  notes: "Internal audit, so adjacent to external-audit substantive testing; grade capped at B. Grade B rests only on a podcast description naming PayPal; the audio was not heard. KPMG's paper is a point of view on SOX in 2030, so it is a vision statement rather than a deployment."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Journal-entry and fraud testing.** Obtain and reconcile the entry population; score or filter entries; investigate outliers; extend fraud procedures. Work types: `data-reporting`, `review-assurance`.
- **Vouching and tests of details.** Select items; get supporting documents; match amounts, dates and counterparties; document exceptions. Work types: `review-assurance`, `transaction-processing`.
- **Substantive analytical procedures.** Build an expectation; compare with recorded amounts; investigate differences. Work type: `data-reporting`.
- **External confirmations.** Design and send requests (cash and receivables most often); keep control of the channel; evaluate responses; follow non-replies. Work types: `review-assurance`, `transaction-processing`. SAS No. 150 changes this for US audits (effective for periods ending on or after 15 Dec 2028) (JOFA-SAS150-2026).
- **Revenue and contract testing.** Sample or target contracts; read terms; assess recognition. Work types: `review-assurance`, `research-synthesis`.
- **Inventory observation and testing.** Attend counts; test records. Work types: `physical-field`, `review-assurance`.
- **Accounting-estimate testing.** Evaluate management's method, data and assumptions, often with specialists. Work type: `expert-judgment`.
- **Sampling versus full-population testing.** Choose population coverage and extent of testing. Work type: `review-assurance`.

### Common pain points

- Staff time on routine testing: a sample, a spreadsheet extract, then pass/fail marking (CTRLCOUNCIL-WSJ-2026).
- Client data: poor quality (60%) and no system access (53%) among the top blockers for US small and mid-size firms (CPACOM-ATR-2025).
- Staff skills: not trained in advanced approaches, the top blocker at 66% (CPACOM-ATR-2025).
- Evidence that is easy to forge: screenshots, PDFs, emails and paper replies (TR-BANKCONF-2026).
- Partner succession and entry-level pipeline: a Thomson Reuters executive cites 75% of audit partners scheduled to retire within ten years (vendor claim) (TR-STATE-2026).
- Smaller firms' economics: a PIA Group technology leader says a tool built once serves about 1,500 accountants, but for a firm of fifty the business case "just doesn't hold up" (NYENRODE-SHIFTS-2026).

### Metrics and benchmarks (with sources and what they measure)

- **IFIAR 2024 survey, share of members "frequently" seeing technology in audit files:** journal-entry testing 88% (48 members); risk assessment 55% (47); substantive procedures on accounts such as revenue or inventory 55% (47); internal-controls testing 43% (46); IT applications and security configuration 39% (44). 31% of members reported findings that tools were not used as intended (IFIAR-TTF-2025).
- **AICPA/CPA.com 2025 benchmark (54 US firms with complete data), firms with an automated solution:** confirmations 39%; foot and proof 39%; trial-balance import 35%; risk assessment 22%; data ingestion 19%; substantive analytics 11%; none 22% (CPACOM-ATR-2025).
- **Gartner:** 83% of audit functions piloting or using AI (119 CAEs, Aug 2025) (GARTNER-2026).
- **ACFE/SAS 2026 (713 anti-fraud professionals):** 75% report an increase in generative-AI document fraud and forgery over two years; 55% expect it to rise significantly over the next 24 months; only 7% say their organisation is more than moderately prepared for AI-fuelled fraud; 25% use AI/ML in anti-fraud programmes (SAS-ACFE-2026).
- **IIA Foundation/AuditBoard (17 Feb 2026 per the IIA's PCAOB comment letter, footnote 9 (IIA-PCAOB-2026); 373 senior internal-audit leaders, North America):** 85% see AI-enabled fraud as a moderate to high risk; 65% name fabricated invoices or financial documents among top concerns (88% name AI-powered phishing); 62% say their function is unprepared or minimally prepared; barriers are lack of tools (57%) and skills (55%) (IIA-AIFRAUD-2026).
- **Vendor-published and firm-reported (unverified):** one practitioner's testing time of about 16 hours falling to 5-6 hours per engagement (TR-AGENTIC-2025); up to 70% faster workpaper preparation and review for early adopters of a document-analysis product (TR-AGENTIC-2025); PwC evidence-match tool reading 20 then 30 document types (PWC-AT-2025; CTRLCOUNCIL-WSJ-2026); a simulated GL clean-and-reconcile of 59,157 rows in about ten minutes (JOFA-EXCELAGENT-2026).
- **Time savings reality check:** PwC says whole-audit time savings are modest so far (CFODIVE-PWC-2026).
- **Quality evidence:** none published for any substantive-testing tool (no error rates, override rates or parallel-run results). Firms say parallel runs are used (CTRLCOUNCIL-WSJ-2026; TR-STATE-2026). The only independent measures are regulator observations (IFIAR-TTF-2025) and experiments on auditor behaviour (ICPAS-PEECHER-2026).

### Guardrails and regulatory points (as discussed by practitioners)

- **UK FRC guidance (30 Mar 2026)** frames three risks: deficient output, misinterpretation or misuse, and non-compliant methodology; its contract-review example documents the tool's role, sample criteria and selected contracts on the audit file (FRC-GENAI-2026, example 2). ICAEW's technology faculty chair criticises that automation bias gets one paragraph on p. 35 (ICAEW-FRCVIEW-2026).
- **IAASB (Aug 2026 EDs):** guidance rather than a technology requirement, because GenAI tools may make it impossible to evaluate inputs or confirm the tool works as designed (IAASB-ED500-2026, paras 67-69). Comments are due 15 Dec 2026 per the landscape.
- **IAASB 500-series project (Mar 2026):** modernise inventory (ISA 501) and confirmations (ISA 505) for technology (IAASB-500SERIES-2026).
- **AICPA:** SAS No. 150 (confirmations) and SAS No. 151 (fraud) were both approved in 2026 and are effective for periods ending on or after 15 Dec 2028 (JOFA-SAS150-2026; JOFA-SAS151-2026). The AI practice aid (13 Oct 2026) covers entity AI use and the firm's own AI use (AT-AICPAPA-2026).
- **SEC and PCAOB staff (Dec 2025):** AI is an inspection focus; an SEC Office of the Chief Accountant associate chief accountant said existing auditing standards "were not written with today's technology or AI or digital assets in mind" (DART-SECPCAOB-2025).
- **Client consent and data:** a Grant Thornton audit-standards director says clear engagement-letter terms about AI use build client confidence, and a few clients decline (ICAEW-POD-2025, transcript).

### Frontier signals (dated and sourced)

- 2025-10-28: PwC expected a tool for every audit step in calendar 2026 and one global agentic platform about 18 months later (PWC-AT-2025). 2026-10-07: the same leader says time savings are not drastic yet (CFODIVE-PWC-2026).
- 2026-03-16: IAASB approves a project to revise ISA 501 and ISA 505 for technology (IAASB-500SERIES-2026).
- 2026-04-07: EY embeds agents in all phases through Canvas, with end-to-end support expected by 2028 (EY-CANVAS-2026).
- 2026-04-10 (WSJ): KPMG orchestration-agent pilot in summer 2026; full deployment on certain tests the next year; humans absent from routine testing in two to three years; some Big Four leaders estimate agents will contribute 20-30% of a typical audit by 2029; EY piloting agent-to-agent evidence requests (CTRLCOUNCIL-WSJ-2026).
- 2026-06-24: Deloitte unifies agents in Omnia, with agents executing preliminary procedures and preliminary conclusions for professional review (DELOITTE-OMNIA-2026).
- SAS No. 150 published 13 Jul 2026 (reported 14 Jul) and SAS No. 151 published 19 Aug 2026 (reported 20 Aug) (JOFA-SAS150-2026; JOFA-SAS151-2026).
- 2026-08: IAASB EDs for ISA 330, 500 and 520 (IAASB-ED500-2026; IAASB-ED520-2026).
- 2026-09-02: Thomson Reuters frames the issue as "Audit in AI" as well as "AI in Audit" (TR-BANKCONF-2026).
- 2026-10-13: AICPA AI practice aid; more sections promised on risk assessment and evidence (AT-AICPAPA-2026).
- Thomson Reuters executives say they are watching whether adoption hits a "hockey stick" by end of 2026 or is delayed (TR-STATE-2026).

### Conference and podcast signals (agenda and recap level)

- The 2026 KU/Deloitte Auditing Symposium (7-9 May) had a PwC session, "The Future of AI in Auditing", and a CAQ-moderated panel with EY, PwC and an AI-audit start-up founder; a research session looked at how auditors judge AI-detected correlations (KU-SYMPOSIUM-2026). Agenda only.
- The AAA Auditing Section midyear workshop (15 Jan 2026) said AI was a particular focus and included a panel on junior auditors' use of generative AI in planning, internal control analysis and substantive testing (AAA-MIDYEAR-2026). Agenda only.
- The IIA's Great Audit Minds conference (9-11 Mar 2026) listed agentic AI and deepfake fraud among its themes (IIA-GAM-2026).
- At the Dec 2025 AICPA SEC/PCAOB conference, panels discussed preparer AI use cases such as validating invoices against contract terms and auditing expense reports; SEC staff said AI is a tool, not a replacement for human judgment, and that new fraud risks are emerging (RSM-SECPCAOB-2025, section 2.1; DART-SECPCAOB-2025). Deloitte's Will Bible said accountability rests with the person using the tool (DART-SECPCAOB-2025).
- The Synergy 2025 recap podcast (Nov 2025) says Audit Intelligence Analyze was released at the event and users reported large productivity gains; no figures given (CPAPA-SYNERGY-2025).
- ICAEW's Jan 2026 trends piece mixes optimism with doubt about returns on AI spend (ICAEW-TRENDS-2026).

### Workforce and role effects

- KPMG's audit chief digital officer: no longer hiring graduates to create workpapers; wants people who understand the findings with AI help; "audit know-how is still going to be gold" (CTRLCOUNCIL-WSJ-2026).
- PwC is hiring engineers it would not previously have hired into assurance and wants dual-track CPA and data-science profiles (PWC-AT-2025).
- PCAOB's Botic said firms and educators may need to find new paths for juniors to build foundational skills, citing research that AI can erode critical thinking and skepticism (NYSSCPA-BOTIC-2025).
- Thomson Reuters presents AI as a workforce-gap answer, with AI investment now spanning technology and human-capital budgets (vendor view) (TR-STATE-2026).
- A firm's perspective on pyramids: "we're lifting the pyramid up" (KPMG) rather than slicing the bottom off (CTRLCOUNCIL-WSJ-2026).
- Panels at the AAA Auditing Section midyear (Jan 2026) covered how junior auditors use generative AI across planning, internal control analysis and substantive testing; agenda only, content not available (AAA-MIDYEAR-2026).

### Objections and concerns practitioners raise

- **Automation bias and fluent output.** Tools are confident even when wrong, so auditors need equal confidence to challenge (ICAEW-FRCVIEW-2026); some skills may erode (NYENRODE-QUALITY-2026; NYSSCPA-BOTIC-2025).
- **Probabilistic by nature.** RSM UK's audit data analytics director says no tool will give the exact output every time and suggests a rules-based tool alongside AI for data analysis (ICAEW-FRCVIEW-2026). A Grant Thornton audit-standards director compares output to a first-year colleague's work needing review (ICAEW-POD-2025).
- **Explainability.** Deloitte's GenAI lead in its audit technical team says there may be billions of paths to an answer, so recreating it is hard (ICAEW-POD-2025).
- **AI validating AI** can form a closed loop (NYENRODE-QUALITY-2026).
- **Identity threat.** Experienced auditors lacking new digital skills may discount AI-reliant advice defensively; the authors say that weakens skepticism (ICPAS-PEECHER-2026). The authors cite a Caseware survey in which 88% of auditors believe AI tools risk undermining professional judgment (second-hand; the survey was not opened).
- **Evidence authenticity.** Forged documents, bank letters and receipts (TR-BANKCONF-2026; JOFA-APFRAUD-2026; ISACA-EVIDENCE-2026); internal-audit leaders feel underprepared (IIA-AIFRAUD-2026).
- **Fees and economic model.** KPMG reportedly argued to its own auditor that AI should lower fees; analysts split between 'human oversight still dominates' and a shift to continuous, subscription-style assurance (VERDANTIX-KPMGFEE-2026). Clients may ask whether fees should fall (NYENRODE-SHIFTS-2026).
- **Pace of change.** PwC's leader said the speed of technology change has been the biggest surprise (CFODIVE-PWC-2026).
- **Small-firm fit.** FRC guidance assumes specialist technology teams that small firms lack (ICAEW-FRCVIEW-2026).
- **Client-side governance.** Only 6% of audit partners rate their largest client's AI governance as advanced; AI governance is the top audit-committee challenge at 57% (BOARDMEMBER-CAQ-2026).
- **Hype.** A Grant Thornton audit-standards director says the profession has moved past a hype curve of 'AI does an audit at the click of a button' to a more realistic view (ICAEW-POD-2025).

### Interview probes for an advisor

1. Which substantive tests run today on 100% of a population, and which on a sample? For tests you moved to full population, what did you change in how you document sufficient appropriate evidence and treat the exceptions?
2. When an agent's vouching or matching result disagrees with a human's, who wins, how often does it happen, and where is that recorded? Have you run parallel tests, and would you share the results?
3. How do you decide a supporting document is authentic before you vouch to it? Which confirmations still arrive as PDFs, screenshots or email, and what is your plan for them?
4. How do juniors learn what a good test looks like if agents do the routine testing? What do reviewers check first on AI-produced workpapers, and how do you train for automation bias?
5. Where do your estimates and revenue judgments still depend on specialists or senior time, and what has changed there? How has AI changed what you tell audit committees and what you bill?

---

## 4. Routed to other modules

- **planning-risk-assessment:** AICPA practice aid on AI-enabled fraud risk and the effect of entity AI use on the risk assessment; SAS No. 151's fraud lens on risk assessment and the revenue fraud-risk presumption (AT-AICPAPA-2026; JOFA-SAS151-2026). Thomson Reuters' small-firm board-minutes summarisation template and its 750-page document reviews, reported without detail on the audit step (TR-WORKFLOW-2026, vendor-published).
- **controls-testing:** KPMG's SOX 2030 view on embedded and 'self-healing' controls, and on auditing AI itself (KPMG-SOX-2026); the AICPA practice aid on AI-operated controls and service-organisation reports (AT-AICPAPA-2026).
- **completion-reporting:** KPMG's Financial Report Analyzer feeding disclosure checklists (KPMG-CLARA-2025); Deloitte agents drafting documentation and preliminary conclusions (DELOITTE-OMNIA-2026); PwC tool analysing audit-committee communications (CFODIVE-PWC-2026).
- **quality-management:** certification, monitoring and training of AI tools (FRC-GENAI-2026); PIA Group's description of running hundreds to more than a thousand quality checks on one engagement file that previously went unperformed or ticked off (NYENRODE-QUALITY-2026); RSM's guidance copilot, general copilot and staffing tool (CAQ-RSM-2026); the AICPA's quality-management guidance for AI tools (AT-AICPAPA-2026).
- **specialists:** specialist use of AI in valuation, and auditors' reliance on it (ICPAS-PEECHER-2026, if the specialists module takes the research); AICPA comparison of heavy client AI reliance to complex valuation models (AT-AICPAPA-2026).
- **acceptance-independence:** KPMG's fee argument and the pricing question (VERDANTIX-KPMGFEE-2026); PCAOB and SEC remarks on private equity and AI (NYSSCPA-BOTIC-2025; DART-SECPCAOB-2025).
- **Cross-cutting (workforce and business model):** the junior-pipeline discussion and the 'lifting the pyramid' view (CTRLCOUNCIL-WSJ-2026; NYSSCPA-BOTIC-2025; PWC-AT-2025).

---

## 5. Sources

Access is `full` unless stated. Counts by type are in the table that follows.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| KU-SYMPOSIUM-2026 | 2026 Deloitte/University of Kansas Auditing Symposium (agenda) | KU School of Business | conference | https://business.ku.edu/research-and-faculty/accounting/deloitte-ku-auditing-symposium | 2026-05-07 (event date; page undated) | full (agenda only) |
| AAA-MIDYEAR-2026 | 2026 Auditing Section Midyear Meeting, Excellence in Auditing Education Workshop | American Accounting Association | conference | https://aaahq.org/Meetings/2026/Auditing-Section-Midyear-Meeting/Workshop | 2026-01-15 (event date; page undated) | full (agenda only) |
| IIA-GAM-2026 | The IIA's Great Audit Minds Conference to be Held March 9-11 | The IIA | conference | https://www.theiia.org/en/content/communications/press-releases/2026/the-institute-of-internal-auditors-great-audit-minds-conference-to-be-held-march-9-11-in-las-vegas/ | 2026-02-03 | full |
| RSM-SECPCAOB-2025 | Insights from the 2025 AICPA conference on current SEC and PCAOB developments | RSM US | conference | https://rsmus.com/content/dam/rsm/insights/financial-reporting/1pdf/insights-from-the-2025-aicpa-conference-on-current-sec-and-pcaob-developments-12-25.pdf | 2025-12 | full |
| DART-SECPCAOB-2025 | AICPA and CIMA conference on SEC and PCAOB developments: key takeaways | Deloitte DART | conference | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways | 2025-12 (month from the landscape; page undated) | full |
| ICAEW-POD-2025 | How should audit firms use AI? (Beyond Finance, with transcript) | ICAEW | podcast | https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai/transcript | 2025-11-11 | full |
| SRA-SWARM-2026 | How AI Agents are transforming internal audit | Speaking of Risk and Audit | podcast | https://srapodcast.podbean.com/e/swarm-auditing-how-ai-agents-are-transforming-internal-audit | 2026-02-11 | full (description only) |
| CPAPA-SYNERGY-2025 | Recap of the 2025 Thomson Reuters Synergy Conference (Accounting Technology Lab) | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/recap-of-the-2025-thomson-reuters-synergy-conference-the-accounting-technology-lab-podcast-dec-2025/ | 2025-11-26 | full |
| CTRLCOUNCIL-WSJ-2026 | Why Audit Firms Are Rewriting the Role of the Modern Accountant (reproduces WSJ, 2026-04-10) | Controllers Council | press | https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/ | 2026-05-08 | full (via text mirror; WSJ original not opened) |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 | full |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 | full |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| EY-CANVAS-2026 | EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 | full |
| NYSSCPA-BOTIC-2025 | PCAOB's Botic Flags Opportunities and Risks in AI | NYSSCPA | press | https://nysscpa.org/news/1051584-pcaobs-botic-flags-opportunities-and-risks-in-ai-2025-12-10 | 2025-12-10 | full |
| JOFA-APFRAUD-2026 | A guide to fighting AI-fueled AP/AR fraud | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/jul/a-guide-to-fighting-ai-fueled-ap-ar-fraud/ | 2026-07-01 | full |
| JOFA-EXCELAGENT-2026 | Using an Excel agent to clean, validate, and reconcile data | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/ | 2026-10-01 | full |
| JOFA-SAS150-2026 | AICPA updates audit standards related to external confirmations | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/jul/aicpa-updates-audit-standards-related-to-external-confirmations/ | 2026-07-14 | full |
| JOFA-SAS151-2026 | ASB approves standard on auditors' responsibilities relating to fraud | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/asb-approves-standard-on-auditors-responsibilities-relating-to-fraud/ | 2026-08-20 | full |
| VERDANTIX-KPMGFEE-2026 | What Goes Around Comes Around: KPMG's AI-Driven Fee Argument Raises Uncomfortable Questions About Audit Pricing Models | Verdantix | press | https://www.verdantix.com/venture/blog/what-goes-around-comes-around--kpmg-s-ai-driven-fee-argument-raises-uncomfortable-questions-about-audit-pricing-models | 2026-02-10 | full |
| ICAEW-FRCVIEW-2026 | How helpful is FRC's guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05-06 | full |
| ICAEW-TRENDS-2026 | Will 2026 be AI's year? AI adoption trends | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/jan-2026/will-2026-be-ais-year-ai-adoption-trends | 2026-01-01 | full (read for context; not cited in a use case) |
| ISACA-EVIDENCE-2026 | The Audit Evidence Crisis: How AI Deepfakes Are Rewriting Assurance Standards | ISACA | professional-body | https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards | 2026-06-08 | full |
| IIA-PCAOB-2026 | IIA comments on PCAOB standard setting, Release 2026-005 | The IIA | professional-body | https://www.theiia.org/globalassets/site/about-us/advocacy/iia-public-comment-letter-to-the-pcaob-standard-setting-project.pdf | 2026-08-07 | full (used to date the IIA fraud survey) |
| CAQ-RSM-2026 | Shaping the future of assurance: Advancing AI in the audit (RSM) | Center for Audit Quality | professional-body | https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit | 2026-08-25 | full |
| BOARDMEMBER-CAQ-2026 | What Audit Partners Are Seeing On AI And What It Means For Audit Committees | Corporate Board Member (CAQ author) | professional-body | https://boardmember.com/what-audit-partners-are-seeing-on-ai-and-what-it-means-for-audit-committees/ | 2026-07-15 | full |
| ICPAS-PEECHER-2026 | What's Really Behind AI Aversion in Auditing? | Illinois CPA Society (authors at UIUC and Erasmus University Rotterdam) | academic | https://www.icpas.org/information/copy-desk/insight/article/digital-exclusive-2026/what-s-really-behind-ai-aversion-in-auditing | 2026-05-13 | full |
| NYENRODE-SHIFTS-2026 | AI isn't just speeding up accounting, it's changing it fundamentally | Nyenrode Business University | academic | https://www.nyenrode.nl/en/news/n/ai-accounting-changing-fundamentally | 2026-05-19 | full |
| NYENRODE-QUALITY-2026 | AI in auditing: balancing quality, professional skepticism, and responsibility | Nyenrode Business University | academic | https://www.nyenrode.nl/en/news/n/ai-auditing-quality-skepticism-responsibility | 2026-06-18 | full |
| SAS-ACFE-2026 | Study: Deepfake fraud surges, and only 7% of organizations are firmly ready (2026 Anti-Fraud Technology Benchmarking Report) | SAS with ACFE | survey | https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html | 2026-03-25 | full (press release; full report not opened) |
| IIA-AIFRAUD-2026 | Internal Audit and AI-Enabled Fraud | Internal Audit Foundation with AuditBoard (Optro) | survey | https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf | 2026-02-17 | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report | AICPA and CPA.com | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| GARTNER-2026 | Gartner Survey Shows Audit Departments Are Embracing AI and Data Analytics | Gartner | survey | https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-01-27-gartner-survey-shows-audit-departments-are-embracing-ai-and-data-analytics-to-drive-innovation-in-2026 | 2026-01-27 | full |
| IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution | IFIAR (copy on Japan FSA site) | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 (date per landscape; PDF text does not print a date) | full |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full |
| IAASB-ED500-2026 | Exposure Draft: Proposed ISA 500 (Revised), Audit Evidence | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf | 2026-08 | full |
| IAASB-ED520-2026 | Exposure Draft: Proposed ISA 520 (Revised), Analytical Procedures | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-520-Exposure-Draft.pdf | 2026-08 | full |
| IAASB-500SERIES-2026 | Project proposal to revise audit evidence standards related to inventory and external confirmations | IAASB | standard-setter | https://www.iaasb.org/_flysystem/azure-private/2026-03/20260316-Agenda-Item-4D-500Series-Project-Proposal-%28Approved%29.pdf | 2026-03-16 | full |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04-22 | full |
| DELOITTE-OMNIA-2026 | Deloitte unveils connected agentic intelligence in Omnia | Deloitte Global | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 | full |
| KPMG-SOX-2026 | The Future of SOX: A point of view for 2030 and beyond | KPMG US | firm | https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html | 2026-09-24 | full |
| DELOITTE-NL-SAMPLE-2026 | From sample to full-population examination | Deloitte Netherlands | firm | https://www.deloitte.com/nl/en/Industries/financial-services/perspectives/from-sample-to-full-population-examination.html | 2026-09-16 | full |
| TR-AGENTIC-2025 | Thomson Reuters launches agentic AI solutions to transform tax, audit and accounting workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html | 2025-11 | full |
| TR-STATE-2026 | The state of AI in audit in 2026: Interview with experts | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/ | 2026-03-30 | full |
| TR-BANKCONF-2026 | Audit in an AI World: AI is raising the stakes for electronic bank confirmations | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/why-ai-is-raising-the-stakes-for-bank-confirmations/ | 2026-09-02 | full |
| TR-BANKSTATE-2026 | The state of bank confirmations in 2026 | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/the-state-of-bank-confirmations-2026/ | 2026-03-02 | full |
| TR-WORKFLOW-2026 | What does audit workflow transformation actually take? | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/what-does-audit-workflow-transformation-actually-take/ | 2026-10-14 | full |
| MINDBRIDGE-FAKEINV-2025 | Fake Invoices, Real Risks: Why Auditors Must Rethink Their Approach in the Age of AI | MindBridge | vendor | https://www.mindbridge.ai/blog/fake-invoices-real-risks-why-auditors-must-rethink-their-approach-in-the-age-of-ai | 2025-04-15 | full (via text mirror; curl returned 403) |
| WOLTERSKLUWER-EVIDENCE-2026 | AI-generated audit evidence: rethinking trust and authenticity | Wolters Kluwer | vendor | https://www.wolterskluwer.com/en/expert-insights/ai-generated-audit-evidence-rethinking-trust-authenticity | 2026-05-06 | search-only (403) |

**Source count by type** (48 listed; 47 opened, 1 search-only; one row, ICAEW-TRENDS-2026, was read for context and not cited in a use case):

| Type | Count |
|---|---|
| press | 11 |
| vendor | 7 (1 search-only) |
| professional-body | 6 |
| conference | 5 |
| firm | 4 |
| survey | 4 |
| podcast | 3 |
| academic | 3 |
| standard-setter | 3 |
| regulator | 2 |
| community | 0 |
| job-posting | 0 |

---

## 6. Gaps

- **No session content from conferences.** The KU/Deloitte symposium and AAA midyear pages give agendas only; the IIA GAM page is a press release; the BDO, RSM and Deloitte DART recaps cover the SEC/PCAOB conference but say little about auditors' AI use in substantive testing. No recordings, slides or transcripts were reached, so what panellists actually said on substantive testing is not captured. The AICPA ENGAGE 2026 agenda, ICAEW Audit & Assurance Conference (15 Jun 2026) and ACFE Global Fraud Conference sessions were not opened.
- **Podcasts.** Only the ICAEW Beyond Finance transcript was read in full. The Speaking of Risk and Audit episode (PayPal) is known only from its description; the CPA Practice Advisor Synergy recap says little about substantive testing; *The Audit Podcast*, *The Accounting Podcast*, IESBA *Decoding Ethics* and the ICAEW Accounting Insights episode on the FRC guidance (6 May 2026) were not reached.
- **Original sources not opened.** WSJ (10 Apr 2026) was read only through a republished copy; Bloomberg Tax's KPMG item (it returned a page with no usable text); Wolters Kluwer (403); the Caseware survey cited as 88% of auditors (second-hand via ICPAS); the AICPA practice aid full text (login) and AICPA TQA material; the ACFE/SAS full report (only the press release); the FT, Going Concern and Reddit (blocked or not tried).
- **No quality evidence.** No error rates, override rates, parallel-run results, inspection findings specific to AI substantive tools, or independent accuracy measures were found. IFIAR (observation frequency) and behavioural experiments are the only independent material.
- **Thin areas.** Accounting-estimate testing (one academic experiment summary); inventory (a standard-setter proposal only, no firm case); full-population versus sampling debate under ISA 530 and AS 2315 (standard-setter drafts discuss it, but no practitioner debate piece on ISA 530 was found); contract review (no named audit-firm result); SAS No. 151 or practice-aid text on AI-fabricated evidence beyond the Accounting Today summary.
- **Search quota.** Eight web searches were completed before the quota ran out. Further directions not searched: AICPA ENGAGE 2026 session titles; ISACA and IIA conference recaps on deepfakes; Caseware and DataSnipper customer case studies for independent evidence; the SSRN randomised experiment on inventory valuation (landscape lead A6); PCAOB technology-assisted-analysis amendments (AS 1105/2301) commentary.
- **Dating.** Conference pages (KU, AAA, DART) are undated, so event dates or the landscape's month are used. The IFIAR PDF has no printed date; 27 Mar 2025 is from the landscape. The Deloitte NL date (16 Sep 2026) is the page's published date. TR-AGENTIC-2025 shows the month only. IAASB EDs carry a month (August 2026); the landscape gives 5 Aug 2026.
- **Several sources are vendors or sponsors.** Thomson Reuters, MindBridge and Caseware material is marketing; the Nyenrode series is sponsored by PIA Group's chair; the Deloitte Netherlands and KPMG items are firm positioning. The grades above reflect that.
