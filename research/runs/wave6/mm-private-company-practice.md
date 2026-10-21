# Private-company assurance at mid-market firms: practice angle

Researched 2026-10-21. Module `private-company` (archetype `assurance`, mid-market extension). Angle: practice, meaning what firms actually do: named deployments, firm and vendor announcements, product documentation, job postings, and the peer-review data that shows where the work goes wrong.

Read first: the mid-market landscape (`landscape-mid-market.md`), the controlled vocabulary, the assurance `ARCHETYPE.md`, and the titles of the existing use cases in planning-risk-assessment, substantive-testing, completion-reporting and quality-management. Items that an existing module already holds are listed in section 4 (with the new facts found) instead of being re-proposed.

Source keys follow the landscape file. One key differs from the archetype: the archetype's `CASEWARE-VERITY-2026` points at the CwX blog, while the landscape (and this file) use that key for the 20 May 2026 launch release and `CASEWARE-CWX-2026` for the blog.

## 1. Summary

- **What is real.** The named mid-market evidence is concentrated in a few places. (1) Methodology-plus-AI platforms: Withum (more than 1,000 active users, more than 6,000 engagements on the platform), EisnerAmper (more than 1,100 users, more than 1,500 engagements), Citrin Cooperman and PKF O'Connor Davies all run the AICPA-built Dynamic Assurance Solution (DAS) suite, which covers audits, preparation/compilation/review (PCR) and benefit plan audits in one system, with Caseware's Verity AI layer on top. (2) Research and document-analysis assistants in small and regional firms (Plante Moran pilot, Harris Hardy & Johnstone, three nonprofit-audit specialists, a two-CPA Oklahoma firm doing about 80 audits a year). (3) Excel-embedded agents at regional firms (Pattillo Brown & Hill, FGMK, Aprio, Perry & Associates). (4) Thomson Reuters Guided Assurance, where partner tools for lease recalculation, proof of cash and statement validation carry quotes from named audit partners.
- **No measured outcome, and no independent one.** Every outcome figure found is vendor-published or a firm quote inside a vendor case study. No grade A entry is supportable under the 2026-10-17 rule. The best figures are Caseware's beta averages and Thomson Reuters' pilot survey, and both are vendor-published.
- **The data problem is the mid-market problem.** In the CPA.com/AICPA survey of 54 firms, 60% named poor-quality client data and 53% named lack of access to client information and systems as top blockers [CPACOM-ATR-2025]. Grant Thornton's new platform "works with data from any ERP system" and starts with private-company audits [GT-GTAP-2026]. Small-entity clients on QuickBooks-type systems often will not grant API access, so the tools that matter use exports, templates and bank-statement conversion [CPAPA-ATLAB-2025].
- **Nothing found on AI in SSARS work.** DAS PCR (the preparation/compilation/review module) is described with automation and templates, with no AI claim on its own page [CASEWARE-DASPCR-2026]. No AI practice evidence for compilations, reviews or preparations was found anywhere. The single D entry says so.
- **Peer reviewers have published nothing about AI.** State peer-review annual reports show real nonconformance rates by engagement type, but contain no AI content [TSCPA-PEERREVIEW-2025; MNCPA-PEERREVIEW-2025; OKSCPA-PEERREVIEW-2025; ORSCPA-PEERREVIEW-2025]. The only "AI helps you pass peer review" material is vendor marketing [TR-PEERREVIEW-2026].
- **Roles are changing at the top of the practice first.** Firms are creating named AI/technology leaders (Citrin Cooperman, EisnerAmper, Withum, BPM) and managers who run "human plus AI agent" teams (BW&O CPAs posting). The junior-development effect is claimed by firms and flagged as a risk by Accountancy Europe; neither side has measured it.

Counts: 14 use cases (0 A, 8 B, 5 C, 1 D). 54 sources, of which 51 were opened and 3 are search-only (by type: vendor 23, press 10, professional-body 9, survey 4, firm 3, job-posting 2, conference 1, podcast 1, academic 1).

## 2. Use cases

```yaml
- id: assurance-private-company-01
  title: "Research and document-analysis assistant for audit teams at small and regional firms (board minutes, contracts, debt and grant agreements, technical questions)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Small teams lose time on technical research and on reading long unstructured documents (board minutes, leases, bond indentures, grant agreements). A small-firm owner described phoning another CPA to ask questions. Staff are scarce and cannot be added."
  solution: "A purpose-built audit research assistant with citation-backed answers, document upload and reusable prompt templates. Firms use conversation mode for questions, templates for structured checks (for example comparing footnote numbers to the statements) and workspaces for extraction across documents. Plante Moran piloted it with a large group, then widened access. Specialist nonprofit-audit firms use it on grant agreements and board minutes."
  outcomes:
    - {lever: speed, description: "Share of Plante Moran pilot respondents who said the tool was faster than traditional research methods", figure: "91%", measures: "of the 140+ participants in Plante Moran's pilot, those who reported it was faster than traditional research methods (anonymous internal survey of perceived speed, not a timed comparison)", provenance: vendor-published, source_ref: TR-CASESTUDIES-2026}
    - {lever: capacity, description: "Plante Moran widened access after the pilot", figure: "450% increase in user base", measures: "growth in the number of users on the platform after the pilot, as stated by Thomson Reuters; the starting and end user counts are not given", provenance: vendor-published, source_ref: TR-CASESTUDIES-2026}
    - {lever: speed, description: "Harris, Hardy & Johnstone (mid-sized firm) says document review that took an hour now takes about five minutes", figure: "about 1 hour to 5 minutes", measures: "the firm's own statement of time for document review tasks such as board minutes and contracts; no timing study or sample size published", provenance: vendor-published, source_ref: TR-CASESTUDIES-2026}
    - {lever: cost, description: "One of three nonprofit-focused audit firms reports holding revenue with fewer staff", figure: "same revenue, two fewer staff than a year earlier", measures: "an unnamed one of the three firms (Sam Brown CPA, Wells CPA, The Forde Firm) in a quote; tools used were CoCounsel Audit and Audit Intelligence Analyze together, so the effect is not specific to this use case", provenance: vendor-published, source_ref: TR-CASESTUDIES-2026}
  prerequisites:
    - "Enterprise-grade licence and written AI security protocols. Plante Moran says it set new AI security protocols and software controls with the vendor [TR-CASESTUDIES-2026]."
    - "Prompt and template tuning. The Oklahoma firm's board-minutes template did not summarise (no chronological order), and vendor support advised saving customised templates, naming date ranges and telling the tool to answer 'N/A' for missing information [TR-STPIERRE-2026]."
  risks_and_guardrails:
    - "Output quality depends on the template and prompt. The St. Pierre firm said its board-minutes template was 'not summarizing' until customised [TR-STPIERRE-2026]."
    - "Perceived-speed surveys and owner quotes are not error-rate measures. No false-positive or miss rate is published [TR-CASESTUDIES-2026]."
  human_checkpoints:
    - "The auditor reads the cited passages and decides what to rely on. The vendor describes citation-backed responses as the basis for audit trails [TR-CASESTUDIES-2026]."
  role_evolution: "Staff use the tool in place of asking colleagues or other CPAs; one small-firm owner says he now puts questions to it instead of calling another CPA [TR-STPIERRE-2026]. Plante Moran says giving every staff member the tool strengthened its reputation as an employer [TR-CASESTUDIES-2026]."
  evidence_grade: B
  sources:
    - {ref: TR-CASESTUDIES-2026, title: "Scaling audit practices with AI: 3 real-world case studies", publisher: Thomson Reuters, type: vendor, url: "https://tax.thomsonreuters.com/blog/scaling-your-audit-practice-with-ai-3-real-world-cocounsel-audit-case-studies/", date: 2026-06-16, access: full, locator: "Sections on Plante Moran, Harris Hardy & Johnstone, and the nonprofit firms; results paragraph on the 140+ pilot"}
    - {ref: TR-STPIERRE-2026, title: "How CoCounsel Audit modernizes nonprofit audits", publisher: Thomson Reuters, type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit", date: 2026, access: full, locator: "Opening profile (about 80 audits a year; two CPAs); template feedback section; results list"}
    - {ref: TR-NONPROFITFIRMS-2026, title: "Three nonprofit-focused firms modernize audits with CoCounsel and Audit Intelligence", publisher: Thomson Reuters Community, type: vendor, url: "https://community.thomsonreuters.com/tax-accounting/f/audit-and-accounting/35253/three-nonprofit-focused-firms-modernize-audits-with-cocounsel-and-audit-intelligence", date: 2026, access: full, locator: "Post summary paragraph"}
  last_reviewed: 2026-10-21
  notes: "Firm types: Plante Moran is one of the largest US firms (3,800+ professionals per the vendor's case page); Harris, Hardy & Johnstone is described as mid-sized; the other four are small local firms. TR-STPIERRE-2026 and TR-NONPROFITFIRMS-2026 pages carry no publication date; 2026 is inferred from product launches in 2025, a 2025 date range used in a prompt example, and the dated TR blog of 2026-06-16 that cites the same firms. Overlaps planning-risk-assessment-01 and -02 (board minutes, grounded chat); what is new here is who uses it (small and regional firms) and the nonprofit and government document set."

- id: assurance-private-company-02
  title: "One engagement platform for audits, preparation/compilation/review and benefit plan audits, with the vendor's AI layer on top (Withum, EisnerAmper, Citrin Cooperman, PKF O'Connor Davies)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Firms that do audits, reviews, compilations and benefit plan audits for private clients run disconnected tools and uneven methodology across engagement types and industries. Methodology and tool choice is itself a live decision for any firm with an audit department (a practitioner panel at ENGAGE 2026 was built around it)."
  solution: "Adopt the AICPA-built Dynamic Assurance Solution suite (DAS Audit, DAS PCR for preparation/compilation/review, DAS EBP for benefit plans) as the single system of record, then add Caseware Verity (engagement-aware assistant and agents) inside it. Rollouts are phased and supported by CPA.com for planning, data migration, training and change management."
  outcomes:
    - {lever: capacity, description: "Withum scale of use: users and engagements on the platform", figure: "more than 1,000 active users; more than 6,000 engagements completed to date", measures: "active users on the DAS platform and engagements completed on it to date, as stated in Caseware's release; no time, quality or cost measure given", provenance: vendor-published, source_ref: CASEWARE-WITHUM-2026}
    - {lever: capacity, description: "EisnerAmper scale of use after a phased rollout", figure: "more than 1,100 professionals; over 1,500 client engagements", measures: "professionals using the DAS suite and client engagements already completed with the new system, per Caseware's release; no efficiency measure given", provenance: vendor-published, source_ref: CASEWARE-EISNERDAS-2026}
    - {lever: speed, description: "Withum partner says tasks that took hours are being streamlined", figure: "none published", measures: "qualitative quote from Withum's audit partner and team leader, no figures", provenance: vendor-published, source_ref: CASEWARE-WITHUM-2026}
  prerequisites:
    - "Implementation partner for planning, data migration, training and change management. CPA.com played this role at Withum, EisnerAmper, Citrin Cooperman and PKF O'Connor Davies [CASEWARE-WITHUM-2026; CASEWARE-EISNERDAS-2026; CITRIN-DAS-2026; CASEWARE-PKF-2026]."
    - "Phased rollout with pilots and champions. EisnerAmper's leader says it put readiness ahead of speed [CASEWARE-EISNERDAS-2026]."
  risks_and_guardrails:
    - "Adoption counts are not outcome measures; none of the four releases publishes hours, review-note or inspection results [CASEWARE-WITHUM-2026; CASEWARE-EISNERDAS-2026; CITRIN-DAS-2026; CASEWARE-PKF-2026]."
    - "All four releases were written by the vendor. The DAS PCR product page describes templates, checklists and draft statements that populate from imported data, and makes no AI claim of its own [CASEWARE-DASPCR-2026]."
  human_checkpoints:
    - "Verity suggestions are citation-backed and the auditor accepts, edits or overrides them inside the engagement [CASEWARE-VERITY-2026]."
  role_evolution: "Withum says a first-year auditor can trace checklist requirements to evidence and build judgment sooner. Citrin Cooperman frames the platform as a way for staff to see the reasoning behind procedures [CASEWARE-WITHUM-2026; CITRIN-DAS-2026]. These are firm statements, not measured."
  evidence_grade: B
  sources:
    - {ref: CASEWARE-WITHUM-2026, title: "Withum Fully Adopts DAS Powered by the Caseware Verity AI Platform to Drive its Future-Ready Audit Practice", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/withum-fully-adopts-das-powered-by-the-caseware-verity-ai-platform-to-drive-its-future-ready-audit-practice", date: 2026-06-03, access: full, locator: "Paragraphs 2-3 (suite and user counts); partner quote"}
    - {ref: CASEWARE-EISNERDAS-2026, title: "EisnerAmper Leverages DAS Powered by Caseware to Unify Audit and Build an Agentic Future", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice", date: 2026-06-25, access: full, locator: "Opening paragraph (modules and counts); rollout quotes from Austin and Estrella"}
    - {ref: CITRIN-DAS-2026, title: "Citrin Cooperman Adopts AI-Enabled DAS Suite Powered by Caseware", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth", date: 2026-07-13, access: full, locator: "Paragraph 2 (DAS Audit, DAS PCR, DAS EBP); Kanter quotes"}
    - {ref: CASEWARE-PKF-2026, title: "PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program", date: 2026-10-08, access: full, locator: "Paragraphs 1-3"}
    - {ref: CASEWARE-DASPCR-2026, title: "DAS PCR (formerly OnPoint PCR)", publisher: Caseware, type: vendor, url: "https://www.caseware.com/us/products/das-pcr", date: 2026, access: full, locator: "Product description bullets; last paragraph links to Verity"}
    - {ref: CASEWARE-VERITY-2026, title: "Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly Into Assurance Engagements", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements", date: 2026-05-20, access: full, locator: "Paragraph on citation-backed, reviewable outputs; Disclosure Checklist Agent bullet"}
    - {ref: GRF-ENGAGE-2026, title: "2026 AICPA & CIMA Engage Conference (session list)", publisher: GRF CPAs & Advisors, type: conference, url: "https://www.grfcpa.com/?p=9081", date: 2025-11-17, access: full, locator: "Session abstract 'Methodology for Selecting a Methodology'"}
  last_reviewed: 2026-10-21
  notes: "Firm types per the releases: Withum 'Top 25', EisnerAmper 'Top 20' (CPA Practice Advisor called it 'top 15'), PKF O'Connor Davies 'Top 25'; Citrin Cooperman serves 'private, middle-market businesses'. GRF page publication date is 2025-11-17 (modified 2026-07-14). DAS is built by the AICPA, CPA.com and Caseware [CASEWARE-EISNERDAS-2026]. Cross-links: planning-risk-assessment-20 (methodology-embedded platform for mid-tier firms) already covers the platform idea; what this entry adds is named adoptions and the PCR and EBP modules sharing one system."

- id: assurance-private-company-03
  title: "Proof of cash and books-to-bank analytics for small-business clients without ERP data feeds (QuickBooks-type systems, exports, PDF bank statements)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Clients keep books in QuickBooks, Xero and similar systems, hand over inconsistent exports and PDF bank statements, and often refuse direct API access. Poor client data and limited system access are the top barriers firms name for audit transformation."
  solution: "A tool that sits over the firm's engagement platform and takes data by read-only connection (the podcast lists QuickBooks, Dynamics, Xero, NetSuite, Sage Intact and some lower-end packages) or by Excel/CSV templates with import guides. It converts PDF bank statements, rebuilds a complete general ledger and produces a proof-of-cash workpaper that reconciles every bank and book transaction. Thomson Reuters embeds the same vendor (Audit Sight) in its Guided Assurance methodology, and Suralink adds extraction of client documents into Excel workpapers."
  outcomes:
    - {lever: speed, description: "Holbrook & Manter partner says automated cash testing changed how the firm performs substantive testing", figure: "none published", measures: "qualitative partner quote in a Thomson Reuters post; no hours, error or sample figures", provenance: vendor-published, source_ref: TR-GUIDEDASSURANCE-2026}
    - {lever: risk, description: "Thomson Reuters says the cash analytics produce audit evidence that lets auditors reduce or eliminate substantive procedures", figure: "none published", measures: "vendor statement of capability; no firm result given", provenance: vendor-published, source_ref: TR-GUIDEDASSURANCE-2026}
  prerequisites:
    - "A period general ledger and bank statements in a usable form. The podcast says many clients will not give API access, so firms rely on templates, ERP-specific import guides and data-conversion services [CPAPA-ATLAB-2025]."
    - "Methodology that accepts the evidence. The Holbrook & Manter partner said recent PPC methodology updates make the approach practical and aligned with professional standards [TR-GUIDEDASSURANCE-2026]."
  risks_and_guardrails:
    - "The tool is not a methodology. The podcast hosts say it is a tactical tool that plugs into any methodology and creates workpapers for a separate container [CPAPA-ATLAB-2025]."
    - "Reliability of client-produced data still has to be evaluated. A CalCPA author cites AU-C 500 on information produced by the entity as input to automated tools [CALCPA-AIREG-2026]; secondary source."
  human_checkpoints:
    - "Auditor reviews exceptions and concludes; the vendor's output is a workpaper input, not the conclusion [CPAPA-ATLAB-2025]."
  role_evolution: "Staff time moves from keying and reformatting data to investigating unreconciled items. The podcast hosts also expect automation to reduce outsourced audit support [CPAPA-ATLAB-2025]; opinion, not measured."
  evidence_grade: B
  sources:
    - {ref: TR-GUIDEDASSURANCE-2026, title: "From Vision to Workflow: Thomson Reuters Advances AI-Enabled Audit Through Guided Assurance", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/thomson-reuters-advances-ai-enabled-audit-through-guided-assurance/", date: 2026-06-05, access: full, locator: "Audit Sight paragraph and Welp quote"}
    - {ref: CPAPA-ATLAB-2025, title: "Overview of Audit Sight - The Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/overview-of-auditsight-the-accounting-technology-lab-podcast-oct-2025/", date: 2025-10-24, access: full, locator: "Transcript: data intake, direct connections, proof of cash, data book"}
    - {ref: CPACOM-ATR-2025, title: "Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey)", publisher: CPA.com and AICPA, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "p. 7 barriers chart (60% poor-quality client data; 53% lack of access)"}
    - {ref: SURALINK-WSI-2026, title: "Suralink Unveils Workpaper Suite Intelligence", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/05/05/suralink-unveils-workpaper-suite-intelligence/182793/", date: 2026-05-05, access: full, locator: "Paragraphs 3-5 (Extract Links, Link Answers)"}
    - {ref: CALCPA-AIREG-2026, title: "AI Standard Setting, Regulation in Audit: Part 1", publisher: CalCPA, type: professional-body, url: "https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1", date: 2026, access: full, locator: "Section on AICPA guardrails, 'Data quality'"}
  last_reviewed: 2026-10-21
  notes: "Audit Sight claims it saves 80% of management-meeting prep time (podcast), a diligence feature rather than audit; not used as an outcome. A search summary said Auvana, an audit service center for CPA firms, uses Audit Sight for outsourced procedures; that page was not opened (search-only). CALCPA-AIREG-2026 has no publication date on the page; it refers to the PCAOB's early-2026 request for comment, so it is no earlier than March 2026. Cross-link substantive-testing-07 (data cleaning to the trial balance) and -17 (bank and third-party data)."

- id: assurance-private-company-04
  title: "Reusable Excel agents for clients that report in a common format, including single-audit compliance tests (Pattillo Brown & Hill, Perry & Associates, Aprio)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Regional firms with many similar clients (for example about 70 school districts) format trial balances, foot statements and prepare state data uploads by hand for each one. Client data arrives as large, inconsistently formatted PDFs, and single-audit compliance tests are long."
  solution: "An audit-focused Excel agent from DataSnipper extracts from differently formatted documents, formats trial balances, foots and cross-foots statements, selects payroll samples and runs multi-item compliance tests. Every result is tied to a source snip so a reviewer can verify it. PB&H is building agents tailored to the software its school-district clients use, to be shared across the firm."
  outcomes:
    - {lever: speed, description: "PB&H ran a multi-level grant compliance test on 63 items in about an hour", figure: "63 items in about an hour", measures: "number of items an Excel agent tested in one single-audit compliance test, with the time given by a staff member as 'about an hour'; no manual baseline or error check stated", provenance: vendor-published, source_ref: DATASNIPPER-PBH-2026}
    - {lever: speed, description: "Perry & Associates reports workpaper preparation time on a 50-fund grant engagement", figure: "80 hours to 25 hours", measures: "preparation of workpapers for one client with 50 funds and three years of data in six boxes, as reported by the firm in a DataSnipper case study (one engagement; OCR and Snips, not an agent)", provenance: vendor-published, source_ref: DATASNIPPER-PERRY-2025}
    - {lever: speed, description: "Perry & Associates headline for grant-review preparation", figure: "68% reduction", measures: "reduction in grant review preparation time as stated by the vendor for Perry & Associates; basis not stated beyond the 80-to-25-hour example", provenance: vendor-published, source_ref: DATASNIPPER-PERRY-2025}
  prerequisites:
    - "Enterprise tool that keeps firm data out of model training (FGMK says this was required [DATASNIPPER-FGMK-2026]); SOC 2 certification is the vendor's stated control."
    - "Repeatable client population, so one agent can be reused (about 70 school districts at PB&H) [DATASNIPPER-PBH-2026]."
  risks_and_guardrails:
    - "PB&H says Copilot in Excel cannot make snips, so output cannot be verified; the traceable snip is the control [DATASNIPPER-PBH-2026]."
    - "Figures are single examples told by the firm, with no sample size or error rate."
  human_checkpoints:
    - "Reviewer clicks a cell and sees the supporting document; results are 'traced and locked in' [DATASNIPPER-PBH-2026]."
  role_evolution: "PB&H says the agent repeats monotonous tasks like a staff member and also builds tests and checks compliance, which it called a more senior-level task. Perry says junior team members did the scanning. Aprio's assurance operations director says the impact is bigger for reviewers because each cell traces to its source [DATASNIPPER-PBH-2026; DATASNIPPER-PERRY-2025; DATASNIPPER-APRIO-2026]."
  evidence_grade: B
  sources:
    - {ref: DATASNIPPER-PBH-2026, title: "DataSnipper Success Stories - PB&H (Purpose-built for auditors: government audit work with Excel Agents)", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/pb-h-automation-excel-agents", date: 2026, access: full, locator: "Profile paragraph; Q&A on 70 school districts, 63 items in about an hour, payroll register sampling"}
    - {ref: DATASNIPPER-PERRY-2025, title: "DataSnipper Success Stories - Perry & Associates CPAs", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/perry-associates-cpas", date: 2025, access: full, locator: "Sections 'Audit Consultancy' (80 to 25 hours) and headline summary (68%)"}
    - {ref: DATASNIPPER-FGMK-2026, title: "FGMK Uses Alwin to Automate Larger, More Complex Audit Work Securely", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/fgmk-alwin-success-story", date: 2026, access: full, locator: "Q&A on SOC 2 and models not being trained on firm data"}
    - {ref: DATASNIPPER-APRIO-2026, title: "DataSnipper Success Stories - Aprio", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/aprio", date: 2026, access: full, locator: "Q&A from Connect '26 New York"}
  last_reviewed: 2026-10-21
  notes: "The three DataSnipper pages carry no visible publication date. The PB&H and Aprio dates are inferred from product names (Excel Agents, Alwin) and the Aprio page's reference to Connect '26; the Perry date comes from page metadata (2025-09-19) and may not be the publication date. PB&H is a regional firm (200+ professionals, Texas and New Mexico, begun using DataSnipper in summer 2024). Perry & Associates is a Marietta, Ohio firm. Aprio is a global advisory and accounting firm. FGMK is covered in entry 07 and in substantive-testing-11. This entry adds the repeated-client-format pattern and the single-audit test; the single-audit side also belongs to the future nonprofit-government module."

- id: assurance-private-company-05
  title: "Risk-focused sample selection documented as a workpaper, to justify smaller samples to peer reviewers at a small firm"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "A small firm relied on Excel templates and manual steps for sampling, testing and documentation. It over-audited and found it hard to justify leaner samples to peer reviewers."
  solution: "Transaction analytics embedded in the workflow (Thomson Reuters Audit Intelligence Analyze) focus procedures on higher-risk areas and record the selections as workpapers, so the firm can show peer reviewers why a sample is the size it is."
  outcomes:
    - {lever: capacity, description: "Sam Brown CPA, Inc. owner says staff time saved per audit", figure: "at least five to six man-hours per audit", measures: "owner's statement of hours saved per audit using Audit Intelligence Analyze, phrased 'at least'; an estimate, not a tracked metric", provenance: vendor-published, source_ref: TR-SAMBROWN-2026}
  prerequisites:
    - "Transaction data the tool can ingest; a firm methodology that allows risk-based selection."
  risks_and_guardrails:
    - "Smaller samples must still meet peer reviewers' documentation expectations. The firm's stated reason for the tool was defensibility [TR-SAMBROWN-2026]."
  human_checkpoints:
    - "Firm decides which selections to test; peer review of the file follows."
  role_evolution: "Routine sampling work moves off senior time; the firm credits the same suite with letting junior staff run advisory analyses [TR-SAMBROWN-2026]."
  evidence_grade: B
  sources:
    - {ref: TR-SAMBROWN-2026, title: "Small firm, big leverage: Sam Brown, CPA, Inc. scales advisory and streamlines audits with AI", publisher: Thomson Reuters, type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/small-firm-big-leverage-sam-brown-cpa-inc-scales-advisory-and-streamlines-audits-with-ai", date: 2026, access: full, locator: "Opening summary, challenge paragraph, solution paragraph on Audit Intelligence Analyze, results"}
  last_reviewed: 2026-10-21
  notes: "Sam Brown CPA, Inc. is a Troy, Ohio firm founded in 2015 that serves individuals, businesses and nonprofits. The case page has no publication date; 2026 is inferred (Audit Intelligence Analyze launched in 2025 and the firm is cited in the dated TR post of 2026-06-16). Cross-link substantive-testing-08 and -09 (technology-assisted selection; Cherry Bekaert on MindBridge). The mid-market difference is the peer-review rationale for the sample size."

- id: assurance-private-company-06
  title: "AI and embedded standards to link risk assessment to procedures and standardise workpapers, positioned against recurring peer-review findings (vendor claim)"
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Recent peer reviews, according to a CPE course description, show auditors failing to perform or document their risk assessment and to link it to substantive procedures, and documenting fraud consideration and analytical-procedure expectations poorly. SAS 145 raised the bar on risk assessment."
  solution: "Thomson Reuters argues that an audit platform with embedded research, standardised workpapers and traceable links from planning to risk to procedure to evidence to conclusion reduces the deficiencies reviewers look for. It also suggests tracking cycle time by phase, exception resolution time and documentation consistency."
  outcomes:
    - {lever: quality, description: "none published", figure: "none published", measures: "no firm reports peer-review results after using AI; the blog is marketing", provenance: vendor-published, source_ref: TR-PEERREVIEW-2026}
  prerequisites:
    - "A methodology and platform that capture the risk-to-procedure link (see entry 02)."
  risks_and_guardrails:
    - "No AICPA peer review guidance or finding on AI use was found. The AICPA's A&A Focus webcast noted draft peer-review checklists on the new quality management standards, which reviewers will use to evaluate firm implementation [JOFA-AAFOCUS-2025]."
  human_checkpoints:
    - "Reviewer sign-offs and change logs are listed by the vendor as the guardrails [TR-PEERREVIEW-2026]."
  role_evolution: "Not stated. The blog ties the tools to retention of staff during busy season [TR-PEERREVIEW-2026]."
  evidence_grade: C
  sources:
    - {ref: TR-PEERREVIEW-2026, title: "How to pass audit peer review with AI", publisher: Thomson Reuters, type: vendor, url: "https://tax.thomsonreuters.com/blog/passing-peer-review-with-ai/", date: 2026-01-23, access: full, locator: "Paragraphs on what reviewers look for; section on audit trails; metrics paragraph"}
    - {ref: NYSSCPA-PEERDEF-2026, title: "Avoiding Deficiencies in Peer Reviews: Focus on Engagement Quality (webcast listing)", publisher: NYSSCPA, type: professional-body, url: "https://nysscpa.org/catalog/events/1019842-avoiding-deficiencies-in-peer-reviews-focus-on-engagement-quality-webcast-2026-08-12", date: 2026-08-12, access: full, locator: "Course description, second sentence onward"}
    - {ref: JOFA-AAFOCUS-2025, title: "A&A Focus recap: AI considerations in A&A, GASB updates, and practical lease accounting challenges", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/newsletters/a-a-focus/aa-focus-recap-ai-considerations-in-aa-gasb-updates-and-practical-lease-accounting-challenges", date: 2025-09-19, access: full, locator: "Paragraph on draft SQMS peer-review checklists"}
  last_reviewed: 2026-10-21
  notes: "Grade C because the only source for the AI link is the vendor. The NYSSCPA page is a CPE listing dated by its session (2026-08-12); it is secondary evidence of what reviewers report. The state peer-review reports (module notes) give the nonconformance baseline and none mentions AI. Cross-link quality-management (peer review and AI governance)."

- id: assurance-private-company-07
  title: "Firm-built and co-developed audit agents on a vendor platform, with preparer and reviewer agents and overnight runs (FGMK, PKF O'Connor Davies)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Firms want agents tailored to their own procedures (cash testing, journal entry testing, statement checks) without sending client data to open tools, and without building software."
  solution: "FGMK built a base of agents in DataSnipper Excel Agents (cash testing, journal entry testing, financial statement testing), then tested Alwin, a web-based agent platform that works across PDF, Word and Excel and keeps running in the background so an evening job is ready for review the next morning. Preparer agents build workpapers; reviewer agents check consistency and roll-up of statements. FGMK's QC department runs statements through an agent alongside its own independent review. PKF O'Connor Davies joined Caseware's Agentic Pioneer Program to design and deploy its own agents (Agent Workbench, governed MCP interfaces, no-code Agent Studio)."
  outcomes:
    - {lever: capacity, description: "none published", figure: "none published", measures: "FGMK describes hundreds-of-pages general ledger extraction and overnight runs qualitatively; PKF has announced participation only", provenance: vendor-published, source_ref: DATASNIPPER-FGMK-2026}
  prerequisites:
    - "Vendor commitment that firm data does not train models, plus control over who can create and who can use agents (FGMK) [DATASNIPPER-FGMK-2026]."
    - "Governance for agents built by staff. A JofA article advises a review and change-management process for AI-built agents and automations, least-privilege access and human approval for higher-risk actions [JOFA-CYBER-2026]."
  risks_and_guardrails:
    - "Agents the firm builds carry the firm's responsibility. Caseware says agents built in its environment run with the same audit trail and methodology context as Verity [CASEWARE-PKF-2026]; vendor claim."
    - "Excel agents need skills (written procedures) and testing before they are shared; a JofA demonstration used a custom data-cleaning skill and a plan-approval step [JOFA-EXCELAGENT-2026]."
  human_checkpoints:
    - "Reviewer sees the agent's steps beside the workbook and leaves cell-level notes; FGMK keeps its own independent review [DATASNIPPER-FGMK-2026]."
  role_evolution: "Firms need people who can specify and test agents. PKF's chief executive says the programme gives it a seat at the table in developing AI capabilities [CASEWARE-PKF-2026]. See entry 12 for the new leadership roles."
  evidence_grade: B
  sources:
    - {ref: DATASNIPPER-FGMK-2026, title: "FGMK Uses Alwin to Automate Larger, More Complex Audit Work Securely", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/fgmk-alwin-success-story", date: 2026, access: full, locator: "Summary bullets; Q&A on agents for preparers and reviewers, QC use, governance"}
    - {ref: CASEWARE-PKF-2026, title: "PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and Joins the Caseware Agentic Pioneer Program", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program", date: 2026-10-08, access: full, locator: "Paragraphs 1 and 6-7 (Pioneer Program, Agent Builder suite)"}
    - {ref: CASEWARE-PIONEER-2026, title: "Caseware Launches Agentic Pioneer Program, Trusted by Majority of Top 30 U.S. Accounting Firms", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/trusted-by-the-majority-of-top-30-u-s-accounting-firms-caseware-launches-caseware-verity-agentic-pioneer-program", date: 2026-06-04, access: full, locator: "Program descriptions (Pioneer, Lighthouse, Advisory)"}
    - {ref: JOFA-CYBER-2026, title: "New checklist helps CPAs manage AI cyber risks", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/", date: 2026-10-01, access: full, locator: "Paragraphs on agent change management and technical guardrails"}
    - {ref: JOFA-EXCELAGENT-2026, title: "Using an Excel agent to clean, validate, and reconcile data", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/", date: 2026-10-01, access: full, locator: "Paragraphs on skills and the cleaning plan"}
  last_reviewed: 2026-10-21
  notes: "FGMK's page has no publication date; 2026 is inferred from the Alwin launch (Aprio refers to Alwin as introduced 'this year' at Connect '26). FGMK is already cited in substantive-testing-11; this entry adds the Alwin overnight pattern and the Caseware co-development route. PKF's role is announced, not yet in use; the Pioneer Program release lists Baker Tilly, CBIZ, Forvis Mazars, Plante Moran, CohnReznick, Citrin Cooperman, Wipfli, Carr Riggs & Ingram, Withum, PKF O'Connor Davies and Weaver among Caseware customers, not among program participants."

- id: assurance-private-company-08
  title: "AI validation of client PBC submissions before they reach the workpaper (Caseware Response Validation Agent, Suralink Extract Links)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [client-interaction, review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Time is lost between receiving client information and starting real work: chasing incomplete or wrong submissions, then retyping PDFs into Excel. Data access and quality are the leading barriers for firms."
  solution: "Caseware's AI-first Client Requests lets the auditor see what was asked and what came back, with a Response Validation Agent that checks submissions while the auditor decides whether to accept them, and a path from a client response to a populated workpaper. Suralink's Extract Links captures and structures data from client documents and Link Answers answers questions on lease and debt agreements, each tied to the source."
  outcomes:
    - {lever: speed, description: "none published", figure: "none published", measures: "announcements only; no customer, hours or accuracy figure for the validation agent or Suralink features", provenance: vendor-published, source_ref: CASEWARE-EXCEL-2026}
  prerequisites:
    - "A request-to-review workflow already in use (Suralink calls its product a request-to-review platform)."
  risks_and_guardrails:
    - "The auditor decides whether to accept every submission; the agent's findings inform review [CASEWARE-EXCEL-2026]."
  human_checkpoints:
    - "Accept or reject of each client response by the auditor [CASEWARE-EXCEL-2026]."
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - {ref: CASEWARE-EXCEL-2026, title: "Caseware Verity for Excel: Agentic AI Connects Client Requests to Audit Workpapers", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-puts-agentic-ai-inside-the-audit-connecting-client-requests-to-the-workpaper-with-caseware-verity-for-excel", date: 2026-09-09, access: full, locator: "Paragraphs on Client Requests and the Response Validation Agent"}
    - {ref: SURALINK-WSI-2026, title: "Suralink Unveils Workpaper Suite Intelligence", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/05/05/suralink-unveils-workpaper-suite-intelligence/182793/", date: 2026-05-05, access: full, locator: "Paragraphs 3-6"}
    - {ref: GT-GTAP-2026, title: "Grant Thornton launches gtap to transform audit delivery across U.S. practice", publisher: Grant Thornton US, type: firm, url: "https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us", date: 2026-05-07, access: full, locator: "Section 'A focus on quality and client benefits' (client data back and forth)"}
  last_reviewed: 2026-10-21
  notes: "Data and evidence acquisition has no module in the assurance archetype (value-chain section 4); this entry belongs to that gap. Grant Thornton says its platform reduces the back and forth in receiving client data, with no figure."

- id: assurance-private-company-09
  title: "Engagement-aware assistant inside the Excel workpaper that builds workpapers and automates controls tests, analytics and tests of details (Caseware Verity for Excel)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Auditors spend time searching for engagement information and transferring it into Excel workpapers."
  solution: "The assistant reads the connected Caseware engagement (client information, procedures, trial balance, materiality, samples, documents) from inside Excel and drafts workpapers and test steps. Suggestions are reviewed and approved before changes are applied. It is included in the Verity licence at no extra cost and was described as generally available on 9 Sep 2026."
  outcomes:
    - {lever: speed, description: "Caseware's testing to date", figure: "9 hours per engagement on average; 75% per task", measures: "average time saved in Caseware's testing to date per engagement and per task, as stated by the vendor; sample size, baseline and customers not given", provenance: vendor-published, source_ref: CASEWARE-EXCEL-2026}
  prerequisites:
    - "Caseware Verity licence and the engagement held in Caseware Cloud."
  risks_and_guardrails:
    - "Changes are applied only after approval [CASEWARE-EXCEL-2026]. Caseware states that engagement data is not used to train its models [CASEWARE-RISKAGENT-2026]."
  human_checkpoints:
    - "Approval of suggestions before they change the workpaper [CASEWARE-EXCEL-2026]."
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - {ref: CASEWARE-EXCEL-2026, title: "Caseware Verity for Excel: Agentic AI Connects Client Requests to Audit Workpapers", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-puts-agentic-ai-inside-the-audit-connecting-client-requests-to-the-workpaper-with-caseware-verity-for-excel", date: 2026-09-09, access: full, locator: "Opening paragraph (nine hours, 75%); paragraph on workpaper generation and audit test automation"}
    - {ref: CASEWARE-RISKAGENT-2026, title: "Caseware Verity-Powered Risk Suggestion Agent launches to Help Auditors Identify Engagement-Specific Risks", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/caseware-verity-powered-risk-suggestion-agent-launches-to-help-auditors-identify-engagement-specific-risks", date: 2026-10-06, access: full, locator: "Paragraph on governance and data not used to train models"}
  last_reviewed: 2026-10-21
  notes: "Vendor claim with no named customer, so grade C and maturity announced even though the vendor says generally available. Overlaps substantive-testing-11/12 (Excel-embedded tools); the difference is the link to the whole engagement file."

- id: assurance-private-company-10
  title: "Firm-built audit ecosystem for middle-market clients: grounded manual assistant, journal-entry visualisations, document-to-support matching and statement validation (RSM Luca)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Auditors serving middle-market clients need fast, firm-approved guidance in busy season and want to analyse more of the client's data."
  solution: "RSM added Ask Luca, a generative AI tool over its assurance manuals, practice aids and technical accounting guides, to RSM Luca, its digital audit ecosystem used by 4,000+ assurance professionals. The release says the ecosystem also uses AI for risk-focused data analysis, journal-entry visualisations for anomaly detection, matching source documents to support data, and financial statement review and validation."
  outcomes:
    - {lever: speed, description: "RSM says Ask Luca reduces research time", figure: "none published", measures: "no timing or accuracy figure in the release", provenance: self-reported, source_ref: RSM-ASKLUCA-2026}
  prerequisites:
    - "A curated corpus of firm manuals, aids and guides; a firm-level digital ecosystem to host it."
  risks_and_guardrails:
    - "RSM says its approach is built on human-in-the-loop principles and professional judgment [RSM-ASKLUCA-2026]."
  human_checkpoints:
    - "Auditors apply professional judgment and critical thinking to the outputs [RSM-ASKLUCA-2026]."
  role_evolution: "RSM describes Ask Luca as a foundation for future assurance-focused intelligent agents [RSM-ASKLUCA-2026]; a plan, not a result."
  evidence_grade: B
  sources:
    - {ref: RSM-ASKLUCA-2026, title: "RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit", publisher: RSM US, type: firm, url: "https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html", date: 2026-01-08, access: full, locator: "Paragraphs 2-3; bullet list of transformed audit steps"}
  last_reviewed: 2026-10-21
  notes: "RSM positions itself as the leading provider of assurance, tax and consulting services for the middle market. The release also states a $1 billion, three-year AI investment announced in June (2025). Ask Luca overlaps quality-management-12 (firm-grounded assistant); the other steps overlap substantive-testing-10 and completion-reporting-06. Kept here because it is the clearest published example of an ecosystem built for middle-market audits."

- id: assurance-private-company-11
  title: "Proprietary firm platforms and agents that start with private-company audits (Grant Thornton gtap, EisnerAmper audit design agent)"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Firms with large private-company audit books want one data foundation and consistent workpapers across engagements instead of fragmented tools."
  solution: "Grant Thornton announced gtap, a cloud platform that standardises how audit data is ingested, transformed and analysed, 'works with data from any ERP system', supports full-population analysis and automates workpapers, with agents to follow. It will be introduced first to private-company audits, then public-company audits the following year, as a phased rollout. EisnerAmper announced the EisnerAI Audit Design Agent (with Microsoft, on Microsoft Foundry) as a research and insight partner for auditors."
  outcomes:
    - {lever: quality, description: "none published", figure: "none published", measures: "Grant Thornton and EisnerAmper describe intent; neither gives a result", provenance: self-reported, source_ref: GT-GTAP-2026}
  prerequisites:
    - "A firm-scale data and cloud investment. Grant Thornton Ireland developed gtap first and the US firm extended it [GT-GTAP-2026]."
  risks_and_guardrails:
    - "Both firms stress that professionals supervise every step [GT-GTAP-2026; EISNER-AUDITAGENT-2026]."
  human_checkpoints:
    - "Auditors guide the process and keep oversight of agents [GT-GTAP-2026]."
  role_evolution: "Grant Thornton says automating the transactional parts frees teams for skepticism, judgment and risk assessment [GT-GTAP-2026]."
  evidence_grade: C
  sources:
    - {ref: GT-GTAP-2026, title: "Grant Thornton launches gtap to transform audit delivery across U.S. practice", publisher: Grant Thornton US, type: firm, url: "https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us", date: 2026-05-07, access: full, locator: "Paragraphs 2-5 (any ERP; private company audits first)"}
    - {ref: CPAPA-GTAP-2026, title: "Grant Thornton U.S. Launches In-House Audit Transformation Platform", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/05/08/grant-thornton-u-s-launches-in-house-audit-transformation-platform/183107/", date: 2026-05-08, access: full, locator: "Paragraph 5 (phased rollout)"}
    - {ref: EISNER-AUDITAGENT-2026, title: "EisnerAmper Rolls Out In-House AI Audit Design Agent", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/03/20/eisneramper-rolls-out-in-house-ai-audit-design-agent/180020/", date: 2026-03-20, access: full, locator: "Paragraphs 1-3 (announcement date 9 Mar)"}
  last_reviewed: 2026-10-21
  notes: "Grade C: announcements with no evidence of use or results. Larger-firm examples; included because they show what is reaching mid-market practice. The any-ERP claim does not say how non-ERP (QuickBooks-type) data is handled; the release names ERPs only. Already cited in substantive-testing-22 (gtap) and planning-risk-assessment-11; the new point is private-company-first sequencing. EisnerAmper also adopted Caseware DAS (entry 02); the press does not explain how the two fit. The article is partly behind a registration wall."

- id: assurance-private-company-12
  title: "New assurance technology leadership roles and AI-fluent audit managers at private-company firms (Citrin Cooperman, EisnerAmper, Withum, BPM, BW&O CPAs)"
  archetype: assurance
  module: private-company
  function: technology-it
  work_types: [coordination-scheduling, software-systems]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Tool adoption stalls without owners. Firms say staff training, data access and budget are the top blockers, and few have a written transformation plan."
  solution: "Firms name dedicated leaders (Citrin Cooperman: Assurance Innovation Leader; EisnerAmper: Assurance Technology and Innovation Leader, plus a National Office head who also serves as chief risk officer for assurance; Withum: Team Leader, Digital Audit Solutions). BPM advertised an Assurance (Audit AI) Technology Director to lead innovation, adoption, KPIs, change management and vendor budgets. BW&O CPAs advertised an Audit Manager role to help refine how audit professionals work with AI agents in engagement execution, supervising about half the audit team including local and global staff."
  outcomes:
    - {lever: capacity, description: "none published", figure: "none published", measures: "job postings and press-release titles show roles exist; no result is stated", provenance: self-reported, source_ref: BWO-JOB-2026}
  prerequisites:
    - "A budget owner and KPIs. BPM's posting lists KPIs for transformation success, audit efficiency and quality [BPM-JOB-2026]."
  risks_and_guardrails:
    - "A job posting is a firm's self-description. BW&O says it is 'already actively integrating AI' into methodology and execution; no independent confirmation [BWO-JOB-2026]."
  human_checkpoints:
    - "The BW&O role reviews workpapers, documentation and financial statements and ensures compliance with GAAP, GAAS and nonprofit reporting [BWO-JOB-2026]."
  role_evolution: "In the CPA.com/AICPA survey about a third of firms said they need at least one non-traditional skill and about 20% had hired people with non-traditional backgrounds (data analysts, IT specialists, developers, innovation leaders) [CPACOM-ATR-2025]. Accountancy Europe warns that more automation could affect how junior auditors build judgment [ACCTEU-GENAI-2026]."
  evidence_grade: B
  sources:
    - {ref: BWO-JOB-2026, title: "Audit Manager (AI-enabled audit delivery)", publisher: Beebout Williams & Olds CPAs (BW&O CPAs), type: job-posting, url: "https://beebout-williams-olds-cpas.careerplug.com/jobs/3439989", date: 2026-06-05, access: full, locator: "Opening paragraphs; responsibilities list; location line"}
    - {ref: BPM-JOB-2026, title: "Audit AI Technology Director (Assurance Technology Director)", publisher: BPM LLP via Built In Chicago, type: job-posting, url: "https://www.builtinchicago.org/job/assurance-ai-technology-director/9520987", date: 2026-07-04, access: full, locator: "Role summary and responsibilities list; page shows the job removed 10 Jul 2026"}
    - {ref: CITRIN-DAS-2026, title: "Citrin Cooperman Adopts AI-Enabled DAS Suite Powered by Caseware", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth", date: 2026-07-13, access: full, locator: "Kanter's title and quotes"}
    - {ref: CPACOM-ATR-2025, title: "Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey)", publisher: CPA.com and AICPA, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "p. 19 ('New approaches require new skills')"}
    - {ref: CASEWARE-WITHUM-2026, title: "Withum Fully Adopts DAS Powered by the Caseware Verity AI Platform to Drive its Future-Ready Audit Practice", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/withum-fully-adopts-das-powered-by-the-caseware-verity-ai-platform-to-drive-its-future-ready-audit-practice", date: 2026-06-03, access: full, locator: "Kevin McElgunn byline and quote"}
    - {ref: CASEWARE-EISNERDAS-2026, title: "EisnerAmper Leverages DAS Powered by Caseware to Unify Audit and Build an Agentic Future", publisher: Caseware, type: vendor, url: "https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice", date: 2026-06-25, access: full, locator: "Austin and Estrella titles in quotes"}
    - {ref: EISNER-AUDITAGENT-2026, title: "EisnerAmper Rolls Out In-House AI Audit Design Agent", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/03/20/eisneramper-rolls-out-in-house-ai-audit-design-agent/180020/", date: 2026-03-20, access: full, locator: "Austin title (National Office, chief risk officer of assurance)"}
    - {ref: ACCTEU-GENAI-2026, title: "Generative AI in audit and assurance (paper aimed at SMPs)", publisher: Accountancy Europe, type: professional-body, url: "https://accountancyeurope.eu/publications/generative-ai-in-audit-and-assurance/", date: 2026-09-21, access: full, locator: "Risk paragraph on professional scepticism, over-reliance and junior development"}
  last_reviewed: 2026-10-21
  notes: "Firm types: BPM is a Top 100 firm per Accounting Today's list; BW&O CPAs is a California firm (El Dorado Hills) whose posting names GAAP, GAAS and nonprofit reporting requirements and local and global staff. The BPM posting's title is 'Audit AI Technology Director' on the board and 'Assurance Technology Director' in the text. The ACCTEU paper is a European professional-body paper for small and medium-sized practices and is used only for the risk."

- id: assurance-private-company-13
  title: "Keep AI time savings as margin or capacity rather than cutting fees (small-firm claims)"
  archetype: assurance
  module: private-company
  function: strategy-planning
  work_types: [expert-judgment, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Efficiency gains in audits can be competed away through fees. Firms under staffing pressure want to protect margin while keeping clients."
  solution: "Small firms say they use freed time to hold revenue with fewer staff, keep or raise rates because the work delivers more value, and serve more clients without raising fees. Larger PE-backed and venture-backed models are being built around AI, but no audit-pricing result is published."
  outcomes:
    - {lever: cost, description: "Sam Brown CPA says the tools let the practice serve more clients without raising fees", figure: "none published", measures: "qualitative claim in a vendor case study", provenance: vendor-published, source_ref: TR-SAMBROWN-2026}
    - {lever: growth, description: "Perry & Associates says it can maintain or increase rates because it delivers more value", figure: "none published", measures: "quote in a vendor case study; no rate data", provenance: vendor-published, source_ref: DATASNIPPER-PERRY-2025}
  prerequisites:
    - "Clients who value the output rather than the hours, and a pricing model not tied to time."
  risks_and_guardrails:
    - "Clients in the survey expect technology use: 66% of firms said they communicate technology and methodology as a value differentiator [CPACOM-ATR-2025]."
  human_checkpoints:
    - "Partner pricing decisions."
  role_evolution: "Not stated."
  evidence_grade: C
  sources:
    - {ref: TR-SAMBROWN-2026, title: "Small firm, big leverage: Sam Brown, CPA, Inc. scales advisory and streamlines audits with AI", publisher: Thomson Reuters, type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/small-firm-big-leverage-sam-brown-cpa-inc-scales-advisory-and-streamlines-audits-with-ai", date: 2026, access: full, locator: "Closing paragraph of results"}
    - {ref: DATASNIPPER-PERRY-2025, title: "DataSnipper Success Stories - Perry & Associates CPAs", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/perry-associates-cpas", date: 2025, access: full, locator: "Quote paragraph ('maintain or even increase our rates')"}
    - {ref: CPACOM-ATR-2025, title: "Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey)", publisher: CPA.com and AICPA, type: survey, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: 2025-12, access: full, locator: "p. 11 (66% communicate technology as a differentiator)"}
  last_reviewed: 2026-10-21
  notes: "Grade C because the claims are quotes in vendor material with no pricing data. The landscape's single reported Big Four fee-cut case (KPMG, UK) was not re-read and is not used. Cross-link planning-risk-assessment-23 (efficiency gains negotiated into fees). Current (formerly Crete), a Thrive-backed network that says it plans to buy and upgrade CPA firms with AI, is an ownership model at the advisory and tax end; no audit result is stated [CURRENT-2026]."

- id: assurance-private-company-14
  title: "Idea: AI-assisted drafting and analytical review in preparation, compilation and review engagements (SSARS), including note disclosures"
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Compilation, preparation and review work is high volume at small firms and has real nonconformance in peer review (see module notes), yet no AI-specific public practice material was found for it."
  solution: "Practitioner discussion points to AI automating bank reconciliations, transaction coding, month-end close and reporting, which feeds the financial statements that firms prepare or compile. Platforms such as DAS PCR populate draft statements and disclosure libraries from imported trial balances, but the product page makes no AI claim of its own."
  outcomes:
    - {lever: capacity, description: "none published", figure: "none published", measures: "no SSARS-specific AI result found", provenance: self-reported, source_ref: JOFA-SMALLFIRMS-2026}
  prerequisites:
    - "Clean trial balance and a firm methodology for the engagement type."
  risks_and_guardrails:
    - "Firms in a small-firm article said they keep client data out of public AI platforms and have a human review output [JOFA-SMALLFIRMS-2026]."
  human_checkpoints:
    - "Firm's usual review of the compilation, preparation or review before issuance."
  role_evolution: "Not stated."
  evidence_grade: D
  sources:
    - {ref: JOFA-SMALLFIRMS-2026, title: "Real-life ways small firms use AI", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/news/2026/aug/real-life-ways-small-firms-use-ai.html", date: 2026-08-01, access: full, locator: "Introduction (quoting a 2025 CPA.com report on bank reconciliations, coding, close and reporting)"}
    - {ref: CASEWARE-DASPCR-2026, title: "DAS PCR (formerly OnPoint PCR)", publisher: Caseware, type: vendor, url: "https://www.caseware.com/us/products/das-pcr", date: 2026, access: full, locator: "Bullet on draft financial statements and note disclosures"}
    - {ref: NYSSCPA-SSARS-2026, title: "Annual Update and Practice Issues for Preparation, Compilation and Review Engagements (webcast listing)", publisher: NYSSCPA, type: professional-body, url: "https://nysscpa.org/catalog/events/1020413-annual-update-and-practice-issues-for-preparation-compilation-and-review-engagements-webcast-2026-23-07", date: 2026-07-23, access: search-only, locator: "Search-result summary only; lists SSARS 22 to 27 topics, no AI"}
  last_reviewed: 2026-10-21
  notes: "Idea only. Evidence is adjacent: the JofA reference is to a 2025 CPA.com report (not opened) on bookkeeping and close, not on SSARS engagements; no ARSC or AICPA guidance on AI in SSARS work was found. Course listings for SSARS 26 and 27 appeared in a search and mention no AI [NYSSCPA-SSARS-2026, search-only]. The accounting-side AI evidence (agentic bookkeeping, close) belongs to a future accounting archetype."
```

## 3. Module notes

### Processes and key steps (with work types)

Private-company assurance here covers audits under AU-C and Government Auditing Standards, plus reviews, compilations and preparations under AR-C (SSARS). Peer review divides the work the same way: single audits, other Government Auditing Standards, ERISA, FDICIA, other audits, reviews, compilations and preparations with and without disclosures, SOC and agreed-upon procedures [TSCPA-PEERREVIEW-2025, section II.2(c)].

- Acceptance, engagement letter and planning. Engagement-letter drafting with AI appears at a small firm (route: acceptance-independence). Work types: document-production, review-assurance.
- Understanding the entity and risk assessment (SAS 145). Tools draft risks from the trial balance, prior-year file and board minutes (Caseware Risk Suggestion Agent; Thomson Reuters AI-powered risk identification). Review-assurance, research-synthesis.
- Client data intake (PBC lists, trial balance, general ledger, bank statements). Data-reporting. The step that differs most at mid-market scale because clients run QuickBooks-type systems.
- Fieldwork: tests of details, sampling, proof of cash, lease and debt recalculation, single-audit compliance tests. Review-assurance, data-reporting.
- Financial statement drafting, disclosure checklists, tie-out. Document-production, review-assurance (route to completion-reporting).
- Review and sign-off, including engagement quality review where required. Review-assurance.
- Preparation, compilation and review engagements: client acceptance, trial balance import, draft statements and notes, analytical inquiries. Document-production, review-assurance. No AI practice evidence.
- Firm-level quality management and peer review. Coordination-scheduling (route: quality-management).

### Common pain points

- Poor client data (60%) and lack of access to client systems (53%) are top ranked blockers among 54 firms; staff not trained in advanced approaches (66%) and budget constraints (53%) rank alongside [CPACOM-ATR-2025, p. 7].
- Clients decline API access to their accounting data even when connections exist [CPAPA-ATLAB-2025].
- Hiring experienced staff and workload are leading issues for the small and mid-size groups in the AICPA PCPS survey; technology and AI change management is No. 1 for five-year impact in all six size groups [AICPA-TOPISSUES-2026].
- Peer reviewers report weak documentation of risk assessment, the link to substantive procedures, fraud consideration and analytical expectations [NYSSCPA-PEERDEF-2026].
- Heavy documents: board minutes, bond indentures (one firm cited a 750-page indenture), grant agreements and 1,200-1,500-line disclosure checklists [TR-STPIERRE-2026; TR-DISCLOSURE-2026].

### Metrics and benchmarks (what each figure measures)

Peer-review nonconformance (independent baseline, from state-society administering-entity annual reports for 2025; engagements are selected by reviewers and counts are small, so rates differ widely and are not comparable across societies):

| Report (date) | Engagements reviewed / nonconforming | Selected lines |
|---|---|---|
| Tennessee [TSCPA-PEERREVIEW-2025] (issued 2026-03-31) | 448 / 34 (8%) | reviews 13 of 99; compilations/preparations with disclosures 2 of 44, omitting disclosures 5 of 175; single audits 2 of 11; ERISA 2 of 21; other audits 8 of 53 |
| Minnesota and North Dakota [MNCPA-PEERREVIEW-2025] (file dated 2026-02) | 418 / 38 (9%) | reviews 14 of 75; compilations/preparations with disclosures 5 of 51, omitting disclosures 4 of 138; single audits 3 of 15; other audits 6 of 78 |
| Oklahoma, South Dakota, Kansas [OKSCPA-PEERREVIEW-2025] (file dated 2026-03) | 525 / 86 (16.38%) | OMB single audit 12 of 40; other audits under SAS 20 of 61; Government Auditing Standards other 18 of 43; reviews 8 of 40 plus a second row 7 of 41 |
| Oregon, Hawaii and territories [ORSCPA-PEERREVIEW-2025] (issued 2026-03-01) | 295 / 24 (8%) | OMB single audit 4 of 15; other audits under SAS 4 of 46; reviews of financial statements 5 of 27 |

Peer-review report ratings: system reviews passed 40 of 46 (87%) in Tennessee, 41 of 44 (93%) in Minnesota, 35 of 55 (64%) in Oklahoma and 32 of 36 (89%) in Oregon. Engagement reviews (firms without audits) passed 87 of 97 (90%), 41 of 55 (74%), 75 of 87 (86%) and 42 of 51 (82%). The top system-review deficiency categories were engagement performance (6 of 16 in Tennessee; 19 of 45 in Oklahoma) and monitoring (5 of 16; 13 of 45). None of these reports mentions AI.

Other benchmarks:
- 54 firms (not representative): 75% have no formal transformation plan; nearly one-quarter report no AI or advanced automation (the report elsewhere says approximately one-third are not using AI); 22% have no automated solution; 11% have automation for substantive analytics, 22% for risk assessment, 39% each for foot-and-proof and confirmations; 89% do not use technology for substantive analytics; 83% name staff efficiency as a top-two technology ROI measure [CPACOM-ATR-2025, pp. 2, 3, 9, 10, 11, 19].
- Thomson Reuters pilot survey: 91% of 140+ Plante Moran pilot respondents said faster than traditional research; 77% more confident using generative AI; 87% said the firm should make it available to all staff [TR-CASESTUDIES-2026].
- Caseware beta: Disclosure Checklist Agent saved 2.7 review hours per workflow on average; Verity benchmark of 94% accuracy on golden-dataset items from beta traces, and 15-20 minutes to under two minutes for indicative manual workflows; Verity for Excel nine hours per engagement and 75% per task. All vendor-published, no sample sizes [CASEWARE-VERITY-2026; CASEWARE-EXCEL-2026].
- Thomson Reuters Disclosure Review: roughly 30% of eligible Disclosure-module customers use it, with close to 300 analyses a month across mid-sized and large firms [TR-DISCLOSURE-2026].
- Tax, audit and accounting firms (600 respondents): 63% of large firms versus 35% of small firms say they are in the proactive or optimized stage of technology development; 54% of small firms are ad hoc or reactive. Tax-side survey, used here for size context only [TR-SOTP-2026, key findings].
- UK mid-tier firm study: 74% said generative AI sped some tasks; 22% saw a marked rise in output; 72% feared incorrect output; 52% worried about client information (survey of 200+ staff at Beever and Struthers) [ICAS-AMBS-2025].
- Quality evidence: no error rate, override rate, parallel-run result or inspection or peer-review outcome for AI use in private-company engagements was found. The only quality-type statement is Caseware's beta note that a firm used the checklist agent to find answers on a completed checklist that had been misread [CASEWARE-CWX-2026].

### Guardrails and regulatory points

- AICPA practice aid *AI Considerations for Financial Statement Auditors* (13 Oct 2026, nonauthoritative). Part 1 covers a client's AI in reporting and controls; part 2 covers the firm's own use: quality management policies, team competence, partner duty to understand tools, ensure firm approval and correct use, supervision and review. More content is to be added on risk of material misstatement and audit evidence [AICPA-AIPA-2026; JOFA-AIPA-2026]. The practice aid itself was not opened.
- Documentation. A CalCPA author reads AU-C 230 as requiring working papers that let an experienced auditor understand the AI procedures and judgments, and says a generic 'AI tool was used' note is not enough [CALCPA-AIREG-2026]; secondary and undated. The same piece reports PCAOB inspection findings on AI-assisted journal-entry testing without a source; do not repeat without confirming, and note that it concerns public-company audits.
- Peer review will test the system of quality management: the AICPA published draft SQMS peer-review checklists in 2025 [JOFA-AAFOCUS-2025]. The firms' quality-management deadline of 15 Dec 2025 is in the landscape file [AICPA-QMPR-2026 per landscape, search-only].
- Confidentiality. A Caseware speaker advised small firms to read licence terms, since a free tool may mean the data is the product [JOFA-AAFOCUS-2025]. Firms in the JofA small-firm piece use enterprise versions only [JOFA-SMALLFIRMS-2026]. FGMK required that data not train models [DATASNIPPER-FGMK-2026].
- Agent governance for small firms: a JofA article advises authorised tools, review of staff-built agents and sandboxed, least-privilege agent access [JOFA-CYBER-2026].
- Independence (probe, not a finding): several tools produce client-side schedules (lease schedules and journal entries from contracts in Guided Assurance via Crunchafi; approval workflows built by a firm for nonprofit clients). The sources do not discuss independence; ask [TR-GUIDEDASSURANCE-2026; JOFA-SMALLFIRMS-2026].

### Frontier signals (dated)

- 2026-10-13: AICPA practice aid issued; more on risk assessment and evidence to be added [AICPA-AIPA-2026].
- 2026-10-08: PKF O'Connor Davies joins Caseware's Agentic Pioneer Program (programme launched 2026-06-04) to build its own agents [CASEWARE-PKF-2026; CASEWARE-PIONEER-2026].
- 2026-10-06: Caseware Risk Suggestion Agent launched worldwide, included at no extra cost; GRF's partner is quoted on it [CASEWARE-RISKAGENT-2026].
- 2026-09-23: Thomson Reuters Disclosure Review launched; it says it plans to extend into 'no' and 'not applicable' determinations [TR-DISCLOSURE-2026].
- 2026-09-21: Accountancy Europe paper for small and medium practices groups use cases into knowledge management, administrative and drafting, and audit procedures, and says higher autonomy needs more governance [ACCTEU-GENAI-2026].
- 2026-09-09: Verity for Excel and Response Validation Agent [CASEWARE-EXCEL-2026].
- 2026-06-05: Thomson Reuters embeds Crunchafi, Audit Sight and Trullion in Guided Assurance [TR-GUIDEDASSURANCE-2026].
- 2026-05-07: Grant Thornton gtap, private-company audits first [GT-GTAP-2026].
- 2026-01-08: RSM Ask Luca, described as a base for future agents [RSM-ASKLUCA-2026].
- 2026 (date not stated): DataSnipper Alwin runs background jobs (FGMK evening job ready next morning) [DATASNIPPER-FGMK-2026].

### Workforce and role effects

- Named roles: Assurance Innovation Leader (Citrin Cooperman), Assurance Technology and Innovation Leader and National Office head (EisnerAmper), Team Leader Digital Audit Solutions (Withum), Assurance (Audit AI) Technology Director (BPM), and an audit manager role built around AI agents (BW&O CPAs) [CITRIN-DAS-2026; CASEWARE-EISNERDAS-2026; CASEWARE-WITHUM-2026; BPM-JOB-2026; BWO-JOB-2026].
- Non-traditional hires (data analyst, IT, developer, innovation leader, director of productivity) are more common at firms further along in transformation [CPACOM-ATR-2025, p. 19].
- Firms say explained, cited AI output teaches juniors (Withum, Citrin Cooperman); Accountancy Europe names junior development as a risk. Neither is measured.
- Top 100 strategy notes: Bennett Thrasher says it uses AI to move professionals from lower-level compliance work to consultative roles earlier [ATODAY-TOP100-2026].
- Outsourcing and offshore: BW&O supervises local and global staff [BWO-JOB-2026]; the podcast hosts expect automation to reduce outsourced audit support [CPAPA-ATLAB-2025].

### Objections and concerns practitioners raise

- Wrong output and client data: 72% and 52% in the UK mid-tier study [ICAS-AMBS-2025].
- Poor past technology experience, poor integration and hesitancy [CPACOM-ATR-2025, p. 10].
- Analytics are hard to validate and should not be the first use case; start with board minutes, memos and routine documentation [JOFA-AAFOCUS-2025].
- Over-reliance and persuasive output [ACCTEU-GENAI-2026].
- Template quality: the Oklahoma firm said the board-minutes template did not summarise [TR-STPIERRE-2026].
- Documentation burden: a PCAOB board member, as paraphrased by a CalCPA author, warned inspectors could demand extensive model documentation [CALCPA-AIREG-2026]; secondary.
- Vendor claims: Caseware says no competitor has built a fully governed end-to-end platform [CASEWARE-VERITY-2026]; treat as marketing.

### Interview probes for an advisor

1. "Where does your client data actually come from: ERP exports, QuickBooks, PDFs from the bank? What share of your audits start with data you have to rebuild before you can test?" (entries 03, 04, 08)
2. "Which one engagement type (audit, review, compilation, benefit plan) do you run on which system, and which tool or methodology did you choose and why?" (entry 02; ask for the selection criteria and who decided)
3. "When a peer reviewer opens a file where AI helped, what would they see: tool, version, who reviewed, what the AI got wrong? Has your system of quality management named AI yet?" (entry 06; route to quality-management)
4. "Who owns AI in the assurance practice by name, what do they report on, and what is their time allocation?" (entry 12)
5. "If hours per audit fell, what happens to price, staffing and the junior pipeline in your firm?" (entry 13; ask for any measurement)

## 4. Routed to other modules

Existing use cases that already cover the idea; new facts found this run are noted.

- **Disclosure checklist agents** (Caseware Verity Disclosure Checklist Agent: 2.7 review hours per workflow on average, beta, vendor; Withum took part in testing; used by one firm as a second look at a completed checklist [CASEWARE-WITHUM-2026; CASEWARE-CWX-2026]. Thomson Reuters Disclosure Review: roughly 30% of eligible customers, about 300 analyses a month, no cost to Guided Assurance Disclosure customers [TR-DISCLOSURE-2026]) -> completion-reporting-01, -03.
- **Risk Suggestion Agent** (demo found five risks including a $118,000 gap between trial balance and board-minutes profit; GRF partner quoted on launch, 2026-10-06 [CASEWARE-CWX-2026; CASEWARE-RISKAGENT-2026]) -> planning-risk-assessment-09.
- **Excel agent cleans and reconciles a general ledger to the trial balance** (JofA, 2026-10-01: a simulated 59,157-row ledger took about 10 minutes on average; demonstration, not a firm deployment [JOFA-EXCELAGENT-2026]) -> substantive-testing-07.
- **FGMK agents; DataSnipper in regional firms** -> substantive-testing-11, -12 (see entries 04 and 07 for what is added).
- **Financial statement validation (Trullion, quoted partner at Bennett Thrasher) and lease recalculation (Crunchafi, quoted partner at Hutchinson & Bloodgood)** in Guided Assurance [TR-GUIDEDASSURANCE-2026] -> completion-reporting-06 and substantive-testing-14.
- **Firm-grounded assistant over manuals** (RSM Ask Luca) -> quality-management-12 (kept as part of entry 10).
- **Firm AI use governance, practice aid part 2, engagement-level AI plan** [AICPA-AIPA-2026] -> quality-management-17, -21, -23.
- **Engagement letter drafting with citation-backed language** (Sam Brown CPA: half an hour to an hour saved per letter, owner's estimate [TR-SAMBROWN-2026]) -> acceptance-independence.
- **Walkthrough to draft process documentation and risk-and-control matrix** (illustrative example in Accountancy Europe's paper; confidentiality of recording is flagged [ACCTEU-GENAI-2026]) -> controls-testing (walkthrough assistant).
- **Benefit plan audits** (DAS EBP is part of the Citrin, Withum, EisnerAmper and PKF suites; a Maine/New Hampshire/Vermont survey respondent named Autire for EBP audits and a pilot of ChatGPT with limited licences, open-text, anecdotal [MECPA-TECHSURVEY-2025]) -> future benefit-plan-audits module.
- **Single audit and nonprofit audits** (PB&H single-audit test; three nonprofit specialists; Guided Assurance Single Audit with OMB Compliance Supplement content [TR-GAFEATURES-2026]) -> future nonprofit-government module.
- **Tax-side items found in the same sources** (Ready to Advise at a small firm; Blue J research at a seven-person firm [TR-SAMBROWN-2026; JOFA-SMALLFIRMS-2026]) -> tax archetype, research-advisory.
- **Risk advisory and SOC** (Baker Tilly expanded Fieldguide use across SOC, PCI, HITRUST, ISO, FedRAMP, SOX and internal audit, 2026-05-27; known from a search summary only [BAKERTILLY-FIELDGUIDE-2026]) -> soc-attestation.
- **Ownership and structure** (Current, formerly Crete, Thrive-backed network, $500 million plan announced 2025, 2026-06-02 rebrand [CURRENT-2026]; PE and alternative practice structures in the landscape) -> disruption.md and economics.md.

## 5. Sources

Ref, title, publisher, type, URL, date, access. 54 sources: 51 opened (full), 3 search-only.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AICPA-AIPA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors.html | 2026-10-13 | full |
| GT-GTAP-2026 | Grant Thornton launches gtap to transform audit delivery across U.S. practice | Grant Thornton US | firm | https://www.grantthornton.com/insights/press-releases/2026/may/grant-thornton-launches-gtap-audit-transformation-us | 2026-05-07 | full |
| CPAPA-GTAP-2026 | Grant Thornton U.S. Launches In-House Audit Transformation Platform | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/08/grant-thornton-u-s-launches-in-house-audit-transformation-platform/183107/ | 2026-05-08 | full |
| RSM-ASKLUCA-2026 | RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit | RSM US | firm | https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html | 2026-01-08 | full |
| EISNER-AUDITAGENT-2026 | EisnerAmper Rolls Out In-House AI Audit Design Agent | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/20/eisneramper-rolls-out-in-house-ai-audit-design-agent/180020/ | 2026-03-20 | full (partial; registration wall) |
| CITRIN-DAS-2026 | Citrin Cooperman Adopts AI-Enabled DAS Suite Powered by Caseware | Caseware | vendor | https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth | 2026-07-13 | full |
| CASEWARE-VERITY-2026 | Caseware Launches Caseware Verity to Bring Workflow-Native AI Agents Directly Into Assurance Engagements | Caseware | vendor | https://www.caseware.com/news/caseware-launches-verity-to-bring-workflow-native-ai-agents-directly-into-assurance-engagements | 2026-05-20 | full |
| CASEWARE-CWX-2026 | How Agentic AI Is Transforming Audit: Inside Caseware Verity (CwX 2026) | Caseware | vendor | https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance | 2026-06 (page undated; landscape gives 17 Jun) | full |
| CASEWARE-WITHUM-2026 | Withum Fully Adopts DAS Powered by the Caseware Verity AI Platform | Caseware | vendor | https://www.caseware.com/news/withum-fully-adopts-das-powered-by-the-caseware-verity-ai-platform-to-drive-its-future-ready-audit-practice | 2026-06-03 | full |
| CASEWARE-EISNERDAS-2026 | EisnerAmper Leverages DAS Powered by Caseware to Unify Audit and Build an Agentic Future | Caseware | vendor | https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice | 2026-06-25 | full |
| CASEWARE-PKF-2026 | PKF O'Connor Davies Adopts AI-Enabled DAS Suite ... and Joins the Caseware Agentic Pioneer Program | Caseware | vendor | https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program | 2026-10-08 | full |
| CASEWARE-PIONEER-2026 | Caseware Launches Agentic Pioneer Program, Trusted by Majority of Top 30 U.S. Accounting Firms | Caseware | vendor | https://www.caseware.com/news/trusted-by-the-majority-of-top-30-u-s-accounting-firms-caseware-launches-caseware-verity-agentic-pioneer-program | 2026-06-04 | full |
| CASEWARE-RISKAGENT-2026 | Caseware Verity-Powered Risk Suggestion Agent launches to Help Auditors Identify Engagement-Specific Risks | Caseware | vendor | https://www.caseware.com/news/caseware-verity-powered-risk-suggestion-agent-launches-to-help-auditors-identify-engagement-specific-risks | 2026-10-06 | full |
| CASEWARE-EXCEL-2026 | Caseware Verity for Excel: Agentic AI Connects Client Requests to Audit Workpapers | Caseware | vendor | https://www.caseware.com/news/caseware-puts-agentic-ai-inside-the-audit-connecting-client-requests-to-the-workpaper-with-caseware-verity-for-excel | 2026-09-09 | full |
| CASEWARE-DASPCR-2026 | DAS PCR (formerly OnPoint PCR) | Caseware | vendor | https://www.caseware.com/us/products/das-pcr | 2026 (page undated; mentions Verity, so after 2026-05) | full |
| GRF-ENGAGE-2026 | 2026 AICPA & CIMA Engage Conference (session list) | GRF CPAs & Advisors | conference | https://www.grfcpa.com/?p=9081 | 2025-11-17 | full |
| TR-CASESTUDIES-2026 | Scaling audit practices with AI: 3 real-world case studies | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/scaling-your-audit-practice-with-ai-3-real-world-cocounsel-audit-case-studies/ | 2026-06-16 | full |
| TR-STPIERRE-2026 | How CoCounsel Audit modernizes nonprofit audits | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/modernizing-nonprofit-and-government-audits-with-cocounsel-audit | 2026 (page undated; inferred) | full |
| TR-SAMBROWN-2026 | Small firm, big leverage: Sam Brown, CPA, Inc. ... | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/small-firm-big-leverage-sam-brown-cpa-inc-scales-advisory-and-streamlines-audits-with-ai | 2026 (page undated; inferred) | full |
| TR-NONPROFITFIRMS-2026 | Three nonprofit-focused firms modernize audits with CoCounsel and Audit Intelligence | Thomson Reuters Community | vendor | https://community.thomsonreuters.com/tax-accounting/f/audit-and-accounting/35253/three-nonprofit-focused-firms-modernize-audits-with-cocounsel-and-audit-intelligence | 2026 (page undated; inferred) | full |
| TR-PEERREVIEW-2026 | How to pass audit peer review with AI | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/passing-peer-review-with-ai/ | 2026-01-23 | full |
| TR-DISCLOSURE-2026 | Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence | Thomson Reuters | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/ | 2026-09-23 | full |
| TR-GUIDEDASSURANCE-2026 | From Vision to Workflow: Thomson Reuters Advances AI-Enabled Audit Through Guided Assurance | Thomson Reuters | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/thomson-reuters-advances-ai-enabled-audit-through-guided-assurance/ | 2026-06-05 | full |
| TR-GAFEATURES-2026 | Guided Assurance features | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/products/checkpoint-engage/features | 2026 (page undated) | full |
| SURALINK-WSI-2026 | Suralink Unveils Workpaper Suite Intelligence | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/05/suralink-unveils-workpaper-suite-intelligence/182793/ | 2026-05-05 | full |
| CPAPA-ATLAB-2025 | Overview of Audit Sight - The Accounting Technology Lab Podcast | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/overview-of-auditsight-the-accounting-technology-lab-podcast-oct-2025/ | 2025-10-24 | full |
| DATASNIPPER-PBH-2026 | DataSnipper Success Stories - PB&H | DataSnipper | vendor | https://www.datasnipper.com/resources/pb-h-automation-excel-agents | 2026 (page undated; inferred) | full |
| DATASNIPPER-FGMK-2026 | FGMK Uses Alwin to Automate Larger, More Complex Audit Work Securely | DataSnipper | vendor | https://www.datasnipper.com/resources/fgmk-alwin-success-story | 2026 (page undated; inferred) | full |
| DATASNIPPER-APRIO-2026 | DataSnipper Success Stories - Aprio | DataSnipper | vendor | https://www.datasnipper.com/resources/aprio | 2026 (refers to Connect '26) | full |
| DATASNIPPER-PERRY-2025 | DataSnipper Success Stories - Perry & Associates CPAs | DataSnipper | vendor | https://www.datasnipper.com/resources/perry-associates-cpas | 2025 (page metadata only) | full |
| JOFA-SMALLFIRMS-2026 | Real-life ways small firms use AI | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/real-life-ways-small-firms-use-ai.html | 2026-08-01 | full |
| JOFA-EXCELAGENT-2026 | Using an Excel agent to clean, validate, and reconcile data | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/ | 2026-10-01 | full |
| JOFA-CYBER-2026 | New checklist helps CPAs manage AI cyber risks | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/ | 2026-10-01 | full |
| JOFA-AAFOCUS-2025 | A&A Focus recap: AI considerations in A&A, GASB updates, and practical lease accounting challenges | Journal of Accountancy | press | https://www.journalofaccountancy.com/newsletters/a-a-focus/aa-focus-recap-ai-considerations-in-aa-gasb-updates-and-practical-lease-accounting-challenges | 2025-09-19 | full |
| CALCPA-AIREG-2026 | AI Standard Setting, Regulation in Audit: Part 1 | CalCPA | professional-body | https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1 | 2026 (page undated; after March 2026) | full |
| BWO-JOB-2026 | Audit Manager (AI-enabled audit delivery) | Beebout Williams & Olds CPAs | job-posting | https://beebout-williams-olds-cpas.careerplug.com/jobs/3439989 | 2026-06-05 | full |
| BPM-JOB-2026 | Audit AI Technology Director | BPM LLP via Built In Chicago | job-posting | https://www.builtinchicago.org/job/assurance-ai-technology-director/9520987 | 2026-07-04 | full |
| CPACOM-ATR-2025 | Audit Transformation Report (2025 CPA.com and AICPA Audit Benchmark Survey) | CPA.com and AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| AICPA-TOPISSUES-2026 | AICPA Survey Cites Change Management for Technology and AI as Top Long-Term Issue Facing Accounting Firms | CPA Practice Advisor | survey | https://www.cpapracticeadvisor.com/2026/06/23/aicpa-survey-cites-change-management-for-technology-and-ai-as-top-long-term-issue-facing-accounting-firms/185547/ | 2026-06-23 | full (figures by group not shown) |
| TSCPA-PEERREVIEW-2025 | Annual Report on Peer Review Activities 2025 | Tennessee Society of CPAs | professional-body | https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf | 2026-03-31 | full |
| MNCPA-PEERREVIEW-2025 | 2025 Annual Report on Peer Review Activities | Minnesota Society of CPAs | professional-body | https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf | 2026-02 (file date) | full |
| OKSCPA-PEERREVIEW-2025 | 2025 Annual Report on Peer Review Activities | Oklahoma Society of CPAs | professional-body | https://prod.oscpa.com/storage/assets/Peer%20Review/Annual%20Report/2025%20OSCPA%20Peer%20Review%20Activities.pdf | 2026-03 (file date) | full |
| ORSCPA-PEERREVIEW-2025 | Annual Report 2025 (peer review) | Oregon Society of CPAs | professional-body | https://www.orcpa.org/storage/assets/Pages/About/Peer%20Review/Annual%20Report%202025.pdf | 2026-03-01 | full |
| NYSSCPA-PEERDEF-2026 | Avoiding Deficiencies in Peer Reviews: Focus on Engagement Quality (webcast listing) | NYSSCPA | professional-body | https://nysscpa.org/catalog/events/1019842-avoiding-deficiencies-in-peer-reviews-focus-on-engagement-quality-webcast-2026-08-12 | 2026-08-12 | full |
| ATODAY-TOP100-2026 | Accounting Today Top 100 Firms (print PDF) | Accounting Today | press | https://arizent.brightspotcdn.com/68/01/115c3908493183df05d3879ed2e5/act0326-top100.pdf | 2026-03 | full |
| CURRENT-2026 | Crete rebrands as Current | Accounting Today | press | https://www.accountingtoday.com/news/crete-professionalls-alliance-rebrands-as-current | 2026-06-02 | full (via mirror) |
| ICAS-AMBS-2025 | ICAS study finds widespread concern over genAI accounting errors (Beever and Struthers study) | The Accountant | academic | https://www.theaccountant-online.com/news/icas-study-finds-widespread/ | 2026-03-17 | full |
| ACCTEU-GENAI-2026 | Generative AI in audit and assurance | Accountancy Europe | professional-body | https://accountancyeurope.eu/publications/generative-ai-in-audit-and-assurance/ (PDF: https://accountancyeurope.eu/wp-content/uploads/2026/09/260921-GenAI-in-Audit-firms.pdf) | 2026-09-21 | full |
| MECPA-TECHSURVEY-2025 | Maine, New Hampshire and Vermont State CPA Societies Technology Survey, open-text poll results | MECPA | survey | https://mecpa.org/wp-content/uploads/2026/01/Survey-Results-MECPA-Dec-2025-1.pdf | 2025-12 (poll 6 Oct to 19 Dec 2025) | full |
| TR-SOTP-2026 | 2026 State of Tax Professionals Report | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2026/06/2026-State-of-Tax-Professionals-Report.pdf | 2026-06-09 | full (tax-side; used only for size context in landscape) |
| BAKERTILLY-FIELDGUIDE-2026 | Baker Tilly Advances AI-Enabled Assurance and Advisory Delivery with Fieldguide | Business Wire (via Baker Tilly) | firm | https://www.bakertilly.com/news/baker-tilly-advances-ai-enabled-assurance-with-fieldguide | 2026-05-27 | search-only |
| AUVANA-AUDITSIGHT-2026 | Auvana audit service center uses Audit Sight (CEO quote) | Audit Sight / Citybiz | vendor | https://www.citybiz.co/?p=253100 | 2026 (summary only) | search-only |
| NYSSCPA-SSARS-2026 | Annual Update and Practice Issues for Preparation, Compilation and Review Engagements (webcast listing) | NYSSCPA | professional-body | https://nysscpa.org/catalog/events/1020413-annual-update-and-practice-issues-for-preparation-compilation-and-review-engagements-webcast-2026-23-07 | 2026-07-23 | search-only |

Source count by type (from the table): vendor 23 (one of them search-only), press 10, professional-body 9 (one search-only), survey 4, firm 3 (one search-only), job-posting 2, conference 1, podcast 1, academic 1.

Used from the landscape without re-opening here: AICPA-QMPR-2026 (search-only in the landscape). It appears only in one guardrails bullet in section 3 and supports no outcome.

## 6. Gaps

- **No AI evidence for SSARS work.** No ARSC or AICPA guidance, firm case, vendor customer or peer-review finding on AI in preparation, compilation or review engagements. DAS PCR's page describes automation, not AI. CPE listings for SSARS 26 and 27 (search results) mention no AI.
- **No independent measurement of any tool.** No error rate, override rate, parallel run, reviewer-note count or inspection or peer-review outcome for AI use in private-company engagements. All figures are vendor-published or quotes in vendor case studies. The Caseware golden-dataset accuracy (94%) comes from a vendor's beta traces, with no description of the dataset.
- **No AI content in any peer-review annual report read** (Tennessee, Minnesota/North Dakota, Oklahoma/South Dakota/Kansas, Oregon). AICPA Peer Review Board materials and the practice aid's part 2 were not reached beyond the news releases. Four reports is a small and uneven sample; the other state societies' reports (Connecticut, Virginia, California, Missouri, Georgia) were not read.
- **Non-ERP data handling is described, not proven.** Grant Thornton's "any ERP" does not address QuickBooks-type systems; the Audit Sight evidence is a podcast and a partner quote. Validis (extracts from 27 accounting packages per a 2024 announcement, search summary) and Inflo were not examined.
- **Undated pages.** Four DataSnipper pages, three Thomson Reuters case pages and the Caseware PCR page have no visible publication date; the year used is inferred and flagged. The DataSnipper Perry page carries metadata for 2025-09-19 that may not be its publication date.
- **Not reached or search-only:** Auvana/Audit Sight customer page (Cloudflare block); Baker Tilly's Fieldguide release (one URL returned 404; details from a search summary; it concerns risk advisory); the Sensiba CoCounsel Audit case study (named in a Thomson Reuters page, not opened); the 2025 CPA.com AI in Accounting report cited by JofA; the AICPA practice aid text itself; the CPA.com "AI Solution Due Diligence Guide for Accounting Firms" cited by CalCPA; ENGAGE 2026 session recordings.
- **Job postings:** only two firm postings (BW&O, BPM) were found that describe real AI work in an audit practice. A third-party job-search summary flagged the MindBridge small-firm spotlight (Garbelman Winslow) as current; the page itself is dated 2017-11-22, so it was not used.
- **In-house teams:** this module concerns external private-company assurance; no in-house deployment bears on it.
- **Firm sizes** for several named examples (Harris, Hardy & Johnstone; Holbrook & Manter; Hutchinson & Bloodgood; GRF; FGMK; Aprio) are not stated in the sources and are not asserted here.
