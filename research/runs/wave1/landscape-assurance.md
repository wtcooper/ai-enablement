# Landscape scan: assurance (wave 1 rerun)

- **Archetype:** assurance. External audit and other assurance services: independent examination of financial statements and internal control over financial reporting (ICFR) for public and private companies, plus other assurance (SOC reports, sustainability/ESG assurance). Performed by audit firms of all sizes (Big Four, mid-tier, small practices). Also relevant to in-house internal audit functions whose work overlaps.
- **Proposed modules:** acceptance-independence · planning-risk-assessment · controls-testing (already researched in the pilot) · substantive-testing · specialists (IT audit, valuation and other specialists) · completion-reporting · quality-management · other-assurance (SOC, sustainability, other attest)
- **Prepared:** 2026-10-16. **Predecessor:** `research/runs/pilot/landscape-assurance.md` (search snippets only). This rerun opened the pages.
- **Method note.** Pages were fetched with `curl` through the session proxy (`pdftotext` for PDFs). Each source below carries a status:
  - `read`: the page or PDF was opened and the relevant parts read.
  - `read-secondary`: the primary host refused access (HTTP 403 or login wall), so a secondary report of it was read.
  - `snippet`: seen only in the pilot's search extracts or this run's search results and not opened. Treat as a lead, not a verified fact.
  - `blocked`: the page could not be opened.
  The web-search quota ran out before the last two planned searches (the FRC 2026 annual audit-quality review and Big Four transparency reports), so those stay at `snippet` or unreached. Source keys follow `PUBLISHER-SHORT-YYYY`. Quotations are under 25 words.

---

## 1. Summary

- **Big Four platforms now ship agents firm-wide, and the primary releases confirm the scale claims.**
  - EY embedded a multi-agent framework in EY Canvas on 7 Apr 2026: 130,000 assurance professionals, 160,000 engagements, 150+ countries, "all phases" now and end-to-end support expected by 2028 (EY-CANVAS-2026).
  - KPMG put agents into Clara for 95,000+ auditors on 22 Apr 2025, naming expense vouching and unrecorded-liability search, with controls-testing agents promised within 12 months (KPMG-CLARA-2025).
  - Deloitte unified its agents in Omnia on 24 Jun 2026 for nearly 85,000 practitioners (DELOITTE-OMNIA-2026).
  - PwC said in Oct 2025 that a tool for every audit step should exist in calendar 2026 (PWC-AT-2025) and restated its 2026 tooling in Oct 2026 (CFODIVE-PWC-2026).
  - Grant Thornton US launched Gtap on 7 May 2026, private-company audits first (GT-GTAP-2026). RSM and Andera followed on 26 Aug 2026 with a control-testing platform (RSM-BEACON-2026).
- **Regulators and standard-setters moved from observation to guidance, and none of them prohibits AI.**
  - The FRC issued the first regulator guidance on generative and agentic AI in audit on 30 Mar 2026 (FRC-GENAI-2026) and ran an Audit Tech and AI Sandbox with applications closing July 2026 (FRC-SANDBOX-2026).
  - The IAASB's ISA 330/500/520 exposure drafts (5 Aug 2026, comments due 15 Dec 2026) say in plain terms that GenAI tools strain the "input-output" model of audit evidence, and that the board chose guidance over a technology requirement because the area is premature (IAASB-ED500-2026, para 68 of the explanatory memorandum).
  - The AICPA published its first auditor practice aid on AI on 13 Oct 2026, covering acceptance and continuance, risk assessment, AI-operated controls and the firm's own AI use (AICPA-PA-2026). It also issued SOC-specific TQA 9561 on 11 Sep 2026.
  - The PCAOB updated its agendas on 30 Sep 2026: a data and technology research project, standard-setting projects on auditor independence, fraud, going concern and NOCLAR, and QC 1000 amendments approved 9 Sep 2026 (CPAPA-PCAOBAGENDA-2026).
- **The strongest new material is on modules the pilot rated thin.**
  - Independence: private-equity and AI-vendor relationships are now a live regulatory topic. AICPA PEEC is on a second exposure draft (JOFA-PEEC-2026). The SEC's chief accountant is reviewing independence rules (TR-HOHL-2026). The AICPA warned about SOC tool-provider arrangements (JOFA-SOCETH-2026).
  - Planning: IFIAR reports that 55% of members frequently see automated tools in risk assessment (IFIAR-TTF-2025), and an ICAEW test found chatbots do not perform ISA 315 risk assessment (ICAEW-PIERPOINT-2025).
  - Completion: three vendors shipped disclosure-checklist agents (TR-DISCLOSURE-2026, CASEWARE-VERITY-2026, KPMG-CLARA-2025).
- **Adoption is broad but shallow.**
  - Among US firms (54 complete responses), 75% have no documented transformation plan and 22% have no automated audit solution at all. Only 22% automate risk assessment and 11% substantive analytics (CPACOM-ATR-2025).
  - IFIAR members see tools "frequently" in 88% of journal-entry testing but only 43% of controls testing and 39% of IT application work (IFIAR-TTF-2025).
  - Audit partners rate their largest clients' AI governance as advanced in only 6% of cases (CAQ-PULSE-2026).
- **Business-model pressure is visible and now structural.**
  - AI-native audit ventures have capital: Modus raised $85M in Apr 2026 to build software and invest in audit firms (MODUS-2026). Repodo launched a new AI-built authorised audit firm in Denmark on 25 Aug 2026 (REPODO-2026).
  - Regulators tie private equity and AI together: PCAOB inspectors said in Dec 2025 that both are 2026 inspection focus areas (CAALLEY-PCAOBPE-2025).
- **Corrections to the pilot** are listed in section 14.

---

## 2. Conferences & events

Status codes are defined in the method note. Session titles and speaker organisations are given only where an opened page lists them.

| # | Event (organizer) | Date / edition | AI-related sessions, tracks, keynotes, panels (speaker organisations) | Key | Status | Why it matters |
|---|---|---|---|---|---|---|
| C1 | **Deloitte/University of Kansas Auditing Symposium** (KU School of Business, Deloitte) | 7–9 May 2026, Lawrence KS. Theme "The Future of Auditing" | Day 2 (8 May): "The Audit of the Future" (Matt Wangard, Deloitte); PCAOB update (George Botic, PCAOB); "The Future of AI in Auditing" (Tim Persons, PwC); panel "Artificial Intelligence in the Audit", moderated by Erin Cromwell (CAQ), with Jason Guthrie (EY), Tim Persons (PwC) and Payton Baran (AuditPro.ai); "Private Equity in Accounting" (Jeff Hughes, Grant Thornton); panel "Audit Firm Ownership, Auditor Independence, and Audit Quality" (Emily Lucas, CAQ, moderating; Maria Borysoff, George Mason; Jere Shawver, Private Company Council). Research session paper on how auditors judge AI-detected correlations (authors at USC and UIUC). | KU-SYMPOSIUM-2026 | read | Only conference found that pairs AI with ownership and independence. Corrects the pilot, which found no AI session. |
| C2 | **AAA Auditing Section Midyear Meeting** (American Accounting Association) | Jan 2026 (dates 15–17 Jan, San Antonio, per pilot; the opened page does not state them) | AI was a focus of the workshop. Panel "How is Technology (AI, in particular) Changing the Audit Environment?" (David Knibbs, CBIZ; Mike Sawyer, KPMG US audit AI and innovation leader). Panel "How do Junior Auditors utilize Generative AI in Different Phases of Audit Fieldwork (e.g., planning, internal control analysis, substantive testing)?" (staff from PwC, Grant Thornton, EY). Workshop practice chair from the CAQ. | AAA-MIDYEAR-2026 | read | Shows how juniors use GenAI phase by phase, which maps to the module split. |
| C3 | **AICPA & CIMA Conference on Current SEC and PCAOB Developments** | 8–10 Dec 2025, Washington DC | SEC OCA and PCAOB staff covered AI in financial reporting (governance, explainability, fraud) and flagged firms' AI adoption as an inspection focus. PCAOB acting chair George Botic said AI can already improve risk assessment and evidence gathering by analysing whole populations, but warned about erosion of skepticism and junior skill-building. PCAOB inspections director Christine Gunia said inspectors will focus on AI and on private-equity deals in 2026. Recaps from Deloitte DART, RSM, BDO. | DART-SECPCAOB-2025; RSM-SECPCAOB-2025; BDO-SECPCAOB-2025; CAALLEY-PCAOBPE-2025 | read | Where regulators state positions. The Dec 2026 edition is the next checkpoint. |
| C4 | **IIA Great Audit Minds** (The IIA) | 9–11 Mar 2026, Las Vegas; pre-conference AI workshop 8 Mar | More than 30 sessions by more than 50 leaders (per the organiser's press release), from PayPal, Meta, Reddit, Verizon, Barclays, EY, PwC, KPMG, Deloitte. Themes: the rise of agentic AI (frameworks for safely piloting and scaling it in audit workflows), deepfake fraud, evolving audit function. | IIA-GAM-2026 | read | Internal-audit leadership stage. Pilot's "1,700 attendees, 70+ speakers" is not on the opened page. |
| C5 | **IIA International Conference** | 21–24 Jun 2026, Singapore | 40+ sessions. Track "AI Transformation and Generative AI" (AI-powered audit automation, GenAI in audit and risk, upskilling). Speakers from Google, Meta, HSBC, BMW Group, Singapore ministries. | IIA-INTL-2026 | read | Asia-Pacific internal audit and AI. |
| C6 | **ISACA North America Conference** | 6–8 May 2026, Las Vegas and virtual | Pre-conference workshops 4–5 May: AAIA (Advanced in AI Audit) and AAIR exam prep. Sessions on AI governance. | ISACA-NA-2026 | read | IT-audit specialist community. |
| C7 | **ICAEW Audit & Assurance Conference** | 2026 (15 Jun per pilot) | Optional breakfast "Improving audit quality through AI with AuditBot"; "The role of the auditor in a changing world" (skills and AI); SME audit session on FRC Practice Note 28. | ICAEW-AAC-2026 | read | UK profession venue. The other two ICAEW events (AI Assurance Conference 6 Jul 2026; Internal Audit Conference 5 Nov 2026) were not opened. |
| C8 | **Rutgers World Continuous Auditing & Reporting Symposium (WCARS)** | 69th: 7–8 Nov 2025. 75th: 6–7 Nov 2026, Newark | 69th: professional day on AI in audit, digital twins, autonomous systems and regulatory perspectives; research day on GenAI and continuous assurance. 75th: professional update on AI governance, assurance and agentic systems; research day on AI and continuous assurance. Call for papers open. | WCARS-2025; WCARS-2026 | read | Longest-running continuous-auditing forum. Session list for 2026 not posted on the opened page. |
| C9 | **World Congress of Accountants** (IFAC, KICPA) | 17–19 Nov 2026, Seoul; 600+ professionals expected | Themes include technological disruption; named speakers include Shin Je-yoon (Samsung), Tom Hood (AICPA) and Wes Bricker (organisation line truncated on the page). No AI session list found. | IFAC-WCOA-2026 | read | Biennial global profession meeting. |
| C10 | **IAASB webinar series on audit-evidence proposals** | Part 1: 29–30 Sep 2026. Part 2: 5 and 7 Oct 2026 | Walkthroughs of proposed ISA 500, 330, 520 (evidence, risk response, analytical procedures), which address technology use. | IAASB-EDPAGE-2026 | read | Recordings are the best plain-language explanation of the technology positions. |
| C11 | **Digital CPA Conference (DCPA)** (CPA.com, AICPA) | 7–10 Dec 2025, Gaylord National and online | 50+ speakers and sessions; audit and tax tracks expanded; keynotes by Zack Kass (AI futurist) and Pascal Finette. Audit-specific session titles not on the opened page (see pilot). | CPACOM-DCPA-2025 | read | Main US firm-technology event. |
| C12 | **Thomson Reuters SYNERGY** | 5–8 Nov 2025, Orlando | Launch of Audit Intelligence Test and CoCounsel Document Analysis, shown to 1,600+ customers. | TR-AGENTIC-2025; CPAPA-SYNERGY-2025 | read | Methodology-user base of many mid-size US firms. |
| C13 | **Workiva Amplify 2026** | Sep 2026 | Agent Studio and testing agents; Newell Brands' CAE quoted. | WORKIVA-AMPLIFY-2026 | read | SOX and sustainability on one platform. |
| C14 | **Optro CRX (formerly Audit & Beyond)** | 13–15 Oct 2026, San Diego | Domain-trained agents launched 14 Oct; Autonomous Testing extended beyond SOX. | OPTRO-CRX-2026 | read | Three days before this scan. |
| C15 | **EY SOC, Attestation and Certification Conference** (14th annual) | Highlights published Sep 2026 | Centred on AI assurance. Live poll of attendees on AI use in SOC work. Speakers named: Natalie Deak Jaros, Brandon Miller, Yvonne Zhu, Jatin Sehgal, John McLain, Ryan Ward (EY). | EY-SOC-2026 | read | Only SOC-specific AI usage data. |
| C16 | **Caseware CwX 2026** | 2026, Florida | Andrew Smith (Caseware) demonstrated a planning-review scenario for the Verity agent. | CASEWARE-VERITY-2026 | read | Planning-stage agent demo. |
| C17 | **ACFE Global Fraud Conference** (37th) | 12–17 Jul 2026, Boston | Session by Hany Farid (UC Berkeley, GetReal Security) on navigating AI and deepfakes. | CAQ-INSIDER-2026 | read-secondary | Evidence authenticity and fraud risk. |
| C18 | **IVSC AGM & Conference** | 16–18 Nov 2026, Cologne | Valuation standards body; AI perspectives paper is current. | IVSC-AI-2025 | read | Valuation-specialist lead. |
| C19 | **AICPA & CIMA ENGAGE 2026** | 8–11 Jun 2026, Las Vegas | AAFCPAs' Ryan Wolff on practical approaches to applying emerging technologies in audit work. Other session titles (ethics and oversight, vendor sessions) came from the pilot and were not re-opened. Official agenda 403. | AAFCPA-ENGAGE-2026 | read (partial) | Largest US practitioner conference. |
| C20 | **PCAOB Conference on Auditing and Capital Markets; PCAOB/Management Science Registered Reports** | 26–27 Sep 2025; 10–11 Sep 2026 | "Audit Technology and Innovation" topic area in 2026, per pilot. | PCAOB-CONF-2026 | snippet (pcaobus.org blocked) | Regulator-sponsored research pipeline. |
| C21 | **AICPA ENGAGE 2025; AICPA/CPA.com AI Symposium; IIA International 2025; Circit Connects 2026; MAARC AI Conference 2026; World Audit Analytics & AI Summit** | 2025–2026 | Details carried from the pilot. The Circit Connects campaign page now returns 404. | (pilot items C1, C5, C7, C21–C23) | snippet | Lower priority; not re-verified. |

Public proceedings and decks found: Deloitte DART, RSM and BDO recaps of the Dec 2025 SEC/PCAOB conference; EY SOC conference highlights PDF; IAASB webinar recordings (not yet posted when scanned); CPA Practice Advisor "Accounting Technology Lab" SYNERGY recap podcast.

---

## 3. Regulators & standard-setters

| # | Item (body) | Type | Date | Key | Status | Why it matters for AI |
|---|---|---|---|---|---|---|
| R1 | **FRC Generative and Agentic AI Guidance** (UK) | regulator | 30 Mar 2026 | FRC-GENAI-2026 | read (full PDF) | Three risk categories: deficient output (hallucination, omission, distortion, faulty reasoning, inconsistency), misuse of output (misinterpretation, misunderstanding of methodology), non-compliant methodology. Mitigations: system design, certification and recertification, staff education, human-in-the-loop review and oversight at control points. Defines an LLM's roles (researcher, reasoner, writer, summariser, critic, orchestrator). Two worked examples: summarising board minutes for risk assessment, and contract review for revenue-recognition testing. States that outputs need not match the persuasiveness of the procedure replaced, if the methodology does not overstate it. First such guidance from any audit regulator, per the FRC. |
| R2 | **FRC AI in Audit guidance** and thematic review of ATT certification at the six largest firms | regulator | 26 Jun 2025 | FRC-AIAUDIT-2025; FRC-ATT-2025 | read | Thematic review: most firms had established certification processes, some less mature and undocumented; firms were still updating certification for AI-specific risks and building ways to monitor tool usage and its quality impact. Certification lifecycle: needs analysis, design and development, certification, maintenance and monitoring. |
| R3 | **FRC Audit Tech & AI Sandbox** | regulator | Opened Jun 2026; first-round applications closed Jul 2026 | FRC-SANDBOX-2026 | read | About three engagement meetings over three to four months with FRC experts; UK-registered firms of any size; no endorsement of tools; third-party providers may join later. |
| R4 | **FRC final ISA (UK) 620 and ISAE (UK) 3000 revisions** and feedback statement | regulator | Consultation Jun 2026, closed 10 Jul 2026 (11 responses) | FRC-620-2026 | read (page notes it was machine-converted to HTML) | Adopts the IAASB narrow-scope amendments on using an auditor's expert, approved by the PIOB Dec 2025, effective 15 Dec 2026. Makes explicit that an expert cannot be used if competence or objectivity threats cannot be reduced to an acceptable level. Specialists-module anchor. |
| R5 | **IFIAR, *Use of technology in audits: observations, risks and further evolution*** | regulator | 27 Mar 2025 | IFIAR-TTF-2025 | read (full PDF) | Members' frequency of seeing automated tools in audit files, 2024: journal-entry testing 88%, risk assessment 55%, substantive procedures 55%, internal-controls testing 43%, IT applications and security configurations 39%. 31% of members reported findings that tools were not used as intended (29% in 2023); common findings were misread results, thin testing of outliers and weak ITGC testing. Four asks to firms: monitor impact, prioritise high-impact tools, govern GenAI, keep humans in control. Most inspections had seen minimal GenAI in public-company audits. |
| R6 | **IFIAR 2025 survey of inspection findings** | regulator | 1 Apr 2026 | IFIAR-SURVEY-2026 | snippet (ifiar.org 403) | Figures carried from the pilot (35% of engagements with a finding). |
| R7 | **IAASB exposure drafts: ISA 330, ISA 500, ISA 520** (audit evidence and risk response) | standard-setter | 5 Aug 2026; comments due 15 Dec 2026 | IAASB-EDPAGE-2026; IAASB-ED500-2026; IAASB-ED330-2026; IAASB-ED520-2026 | read (page and the three EDs) | ED-500 explanatory memorandum: respondents wanted more on technology; the board considered a conditional requirement on inputs, tool operation and outputs and rejected it because GenAI tools may make it impossible to evaluate inputs or confirm the tool operates as designed; it chose application material and future non-authoritative guidance. ED-520 application material shows technological tools analysing whole populations or unstructured external data to build sharper expectations. ED-330 has a section on automated controls and general IT controls. |
| R8 | **IAASB Technology Quality Management roundtables** and Technology focus area | standard-setter | Roundtables H2 2025 (240+ participants); summary 10 Feb 2026; initiative launched Jun 2025 | IAASB-TQM-2026; IAASB-TECH-2026 | read | Participants judged ISQM 1 and ISA 220 (Revised) a sound base. Board approved non-authoritative material in Dec 2025; a March 2026 action plan was to be discussed (outcome not found). |
| R9 | **IESBA technology and independence page** | standard-setter | Items dated Jun–Jul 2026 | IESBA-TECH-2026 | read | Lists "Emerging Technologies: NAM" (Jul 2026), a Snapshot on how the Code responds to AI (Jun 2026) and a technology agenda item at the June 2026 board meeting. Describes a three-pillar approach: Code revisions already in force, a permanent expert group, practical guidance. Underlying documents not opened. |
| R10 | **IAASB ISSA 5000 adoption and applicability FAQs** | standard-setter | Effective December 2026 (periods beginning on or after 15 Dec 2026, per search extracts) | IAASB-ISSA5000-2026 | read (FAQ page; adoption page 404) | Framework-neutral baseline for sustainability assurance; no AI-specific content found. |
| R11 | **PCAOB staff spotlight on GenAI outreach** | regulator | Jul 2024 | PCAOB-GENAI-2024 | read | Baseline: firms used GenAI mostly for admin and research; potential areas listed included risk assessment, scoping, disclosure completeness and tie-outs; some firms barred GenAI on audit procedures; firms said supervision policies had not changed. Staff view, not Board policy. |
| R12 | **PCAOB agendas update** (standard-setting, research, rulemaking) and amended QC 1000 | regulator | 30 Sep 2026; QC 1000 amendments approved 9 Sep 2026, effective 15 Dec 2026 | CPAPA-PCAOBAGENDA-2026 | read-secondary | Standard-setting: negative assurance on comfort letters, auditor independence, fraud, NOCLAR, going concern. Research: data and technology, firm and engagement metrics, audit-committee communications. Amendments to QC 1000 include more flexible role assignment and aligning with other quality-management standards. |
| R13 | **PCAOB draft 2026–2030 strategic plan** | regulator | Voted 20 Jul 2026 | TR-PCAOBPLAN-2026 | read-secondary | Objective 5.2 is to build the PCAOB's own technology, data and AI capabilities. 71 comment letters on the March request produced five themes, one being clear guidance on practical use of technology and AI in audit. |
| R14 | **PCAOB Inspections Modernization Council discussion materials** | regulator | Council launched May 2026; 12 members named 9 Jul 2026; materials posted Aug 2026 | STARLING-IMC-2026; CAQ-INSIDER-2026; DART-IMC-2026 | read-secondary | Staff draft moves to a firm-system-of-quality-control-centred inspection approach; about 90% of registration and inspection data is unstructured; early AI pilots for inspections. Staff drafts, not Board policy. |
| R15 | **PCAOB request for comment on standard setting (Release 2026-005)** | regulator | 23 Jun 2026; closed 7 Aug 2026 | IIA-PCAOB-2026 | read (the IIA's comment letter) | The IIA letter shows Questions 8 and 10 address AI; it supports handling AI through the Data and Technology research project first, wants consistent treatment of AI-assisted work across external and internal auditors, and says AS 2605 is not fit for an AI environment. |
| R16 | **PCAOB staff spotlight on using specialists** | regulator | Feb 2025 (date per search extract) | PCAOB-SPECIALISTS-2025 | read | Inspection deficiencies in testing company data used by specialists and evaluating specialists' work. No AI content. Shows the baseline against which AI use by specialists would be judged. |
| R17 | **PCAOB technology-assisted-analysis amendments** (AS 1105, AS 2301); policy statement | regulator | Effective for fiscal years beginning on or after 15 Dec 2025 | PCAOB-TAA-2024 | snippet (pcaobus.org 403; Federal Register notice page was too short to use) | Carried from the pilot. |
| R18 | **PCAOB remarks on AI and private equity** (Botic; Gunia) | regulator | Dec 2025 | CAALLEY-PCAOBPE-2025 | read-secondary | More than 90 significant PE-related deals and mergers since 2020, over half in 2025. Inspectors will examine QC at firms that took PE or alternative practice structures. |
| R19 | **SEC Office of the Chief Accountant: Kurt Hohl** | regulator | Dec 2025; 4 Jun 2026 | KPMG-HOHL-2026; TR-HOHL-2026 | read | OCA asks auditors how they use AI to improve audit quality and to monitor quality control, and says independence rules must stay fit for purpose when AI is integrated into audit delivery. In June 2026 he denied the SEC is weakening independence rules. The OCA review starts with refreshed independence FAQs and public sharing of staff answers to common consultation questions, then a look with the PCAOB chair at the interim independence standards; on AI and private equity he said the SEC is in listening mode. |
| R20 | **AICPA practice aid: *AI Considerations for Financial Statement Auditors*** | standard-setter | 13 Oct 2026 | AICPA-PA-2026; JOFA-AIPA-2026; AT-AICPAPA-2026 | read (release, JofA, Accounting Today) | Part 1: entity's AI use, covering acceptance and continuance (management integrity, skills, team competence; a heavy AI reliance may resemble use of complex valuation models), understanding of the entity, AI-enabled fraud risk, AI-operated controls, reliance on service-organisation reports. Part 2: the firm's own AI use under quality management, supervision and review; one AI tool may check another without reducing the auditor's duties; AU-C 210 does not require naming AI tools in the engagement letter, though state laws or firm policy may. Later additions planned on risk of material misstatement and audit evidence. |
| R21 | **AICPA TQA section 9561** (AI in SOC 1 and SOC 2) | standard-setter | 11 Sep 2026 | AICPA-TQA9561-2026; DART-TQA-2026 | read (landing page, Deloitte DART note); full text behind login | Covers effect of a service organisation's AI use on SOC 1 (AT-C 320) and SOC 2 (AT-C 205) engagements. Secondary reports (pilot) say no new criteria and scope follows the system boundary. |
| R22 | **AICPA PEEC alternative-practice-structure project** | standard-setter | Discussion memo Mar 2025; exposure draft Dec 2025 (comment deadline 30 Apr 2026 per search extracts); PEEC discussed revisions Aug 2026 and agreed to take a second exposure draft to an interim October meeting | JOFA-PE-2025; JOFA-PEEC-2026; AT-PEEC-2026 | read | Draft separates significant influence from control by investors and treats linked non-attest entities as possible network firms. An 81-letter comment record had none from technology companies; ambiguity remains on when licensing an AI audit tool becomes an independence issue (commentary by former PCAOB board member Christina Ho). |
| R23 | **AICPA ethics: SOC 2 tool-provider arrangements** | standard-setter | 6 Apr 2026 | JOFA-SOCETH-2026 | read | Contract terms that shift control, judgment, fees or evidence access to a SOC 2 tool vendor can create independence and objectivity threats; the article notes it may apply to other attest work. |
| R24 | **COSO, *Achieving Effective Internal Control Over Generative AI*** | standard-setter | Feb 2026 (JofA piece 26 Feb) | COSO-GENAI-2026 | read | Eight capability types (ingestion, transformation, posting, orchestration, judgment, monitoring, regulatory intelligence, human-AI interaction), each with minimum control expectations and metrics. |
| R25 | **NFRA (India), *General Principles for Technology Adoption in Audit*** | regulator | Jul 2026 | NFRA-CAALLEY-2026 | read-secondary | Ten principles covering planning and risk assessment, substantive and controls testing, evidence evaluation and reporting. Technology-generated information gets no lower evidentiary bar; applies to in-house, vendor and network tools. |
| R26 | **CPAB (Canada), *The use of AI in the audit*** | regulator | Sep 2024 | CPAB-AI-2024 | read | Limited AI use in inspected files at that date; expects firms to test and certify tools and monitor their quality impact. |
| R27 | **Japan FSA Financial Research Center DP2025-3** (GenAI and audit) | regulator | Jul 2025 | FSA-DP-2025 | read (introduction only) | Academic discussion paper (Hitotsubashi University); not read beyond the introduction. |
| R28 | **IRBA Staff Practice Alert 10** (acceptance and continuation of client relationships) | regulator | Undated on the PDF | IRBA-PA-10 | read | Acceptance factors include assessing the client's IT environment; no AI content. Baseline for acceptance. |
| R29 | **AUASB submission on ED ISA 500 (2022 draft)** | regulator | Undated | AUASB-ED500 | read (skim) | Notes the undefined term "automated tools and techniques" and asks for a definition. |
| R30 | **BSI, BS ISO/IEC 42006:2025** (bodies certifying AI management systems) | standard-setter | 21 Jul 2025 | BSI-42006-2025 | read | First international standard for the certifiers of ISO/IEC 42001; says Big Four firms are understood to be launching AI audit programmes. |
| R31 | **EU AI Act as applied to audit; CNCC guidance; AFM building blocks; AICPA SAS 142; TQA references** | regulator / standard-setter | 2025–2026 | (pilot items R21, R24–R27) | snippet | Not re-opened. AFM page returned 404. |

---

## 4. Professional bodies

| # | Item (body) | Date | Key | Status | Why it matters |
|---|---|---|---|---|---|
| P1 | **CAQ Audit Partner Pulse, Spring 2026** | Released 15 Jul 2026 | CAQ-PULSE-2026 | read-secondary (Corporate Board Member article by a CAQ author; CAQ page is script-only) | Fills the pilot's gap. See section 9. |
| P2 | **CAQ Audit Insider Jul–Aug 2026 newsletter** | 1 Sep 2026 | CAQ-INSIDER-2026 | read | Roundup of PCAOB moves (IMC, strategic plan, 2025 inspection reports for the six US networks: average Part I.A deficiency rate 13%, down from 26% in 2024), the Pulse survey and an RSM blog. |
| P3 | **CAQ blog: RSM on Ask Luca, M365 Copilot and Luca Resourcing** | 25 Aug 2026 | CAQ-RSM-2026 | read | RSM's firm-approved-guidance copilot, general copilot and an AI staffing tool (initial staffing requests, budget planning, engagement-leader review): a quality-management and acceptance-capacity example. |
| P4 | **AICPA and CPA.com, *2025 Audit Transformation Report*** | Dec 2025 | CPACOM-ATR-2025 | read (full PDF) | Best US small and mid-size practice baseline. See section 9. |
| P5 | **ICAEW, Helen Pierpoint, "Testing Gen AI platforms: can they do audit work?"** | Sep 2025 | ICAEW-PIERPOINT-2025 | read | Tested Copilot, Grok and Claude on a fictional retailer. None did ISA 315 risk assessment as a human would; none separated financial-statement-level from assertion-level risk; materiality figures varied widely by model; percentage rounding was inconsistent. Single test, not a benchmark. |
| P6 | **ICAEW viewpoint on the FRC generative and agentic AI guidance** | May 2026 | ICAEW-FRCVIEW-2026 | read | Faculty chair stresses staff training on judgement and scepticism, not just tool mechanics. |
| P7 | **IIA comment letter to the PCAOB** | Aug 2026 | IIA-PCAOB-2026 | read | AS 2605 modernisation; AI treated consistently across external and internal audit. |
| P8 | **IIA Netherlands with ISACA NL, *Internal Audit in the Age of Generative AI*** | 2026 | IIANL-GENAI-2026 | read (landing page) | Five-level maturity model from prompting to agents; reusable for journey markers. Full guide members-only. |
| P9 | **ISACA, AI Pulse Poll 2026** | 2026 | ISACA-PULSE-2026 | read | See section 9. |
| P10 | **ACCA and EY, *AI assessments: enhancing confidence in AI*** | 2025 | ACCA-EY-2025 | read (taxonomy section) | Separates governance assessments, conformity assessments and performance assessments of AI; notes inconsistent use of "audit" for any third-party evaluation. Feeds assurance over AI. |
| P11 | **Accountancy Europe comments on the CAQ GenAI paper** | Nov 2024 | ACCTEU-CAQ-2024 | read | Training needs; EU AI Act documentation duties; ESAP data as AI input. |
| P12 | **IVSC perspectives paper, *Navigating the Rise of AI in Valuation*** | 2025 | IVSC-AI-2025 | read (page; paper not downloaded) | AI as a support, not a replacement, for valuers; flags model governance and explainability as future standards work. |
| P13 | **CAQ *Auditing in the Age of Generative AI*; CAQ *Role of the Auditor in AI*** | 2024; undated | CAQ-GENAI-2024; CAQ-ROTA-2026 | snippet (both pages returned only navigation text) | Pilot items; not verified. |
| P14 | **Cloud Security Alliance research note: SOC 2 and AI controls gap** | 30 Aug 2026 | CSA-SOC2-2026 | read | Argues the AICPA has published no AI-specific Trust Services Criteria, so auditors improvise evidence requests on model lineage, logging, drift and AI subprocessors; says SOC 2 Type II reliably covers conventional IT general controls on the infrastructure, not model-specific properties. Cites the SOC 2 working group warning on "fast and easy" platforms and the Peer Review Board alert (May 2026). Industry body, not a standard-setter. |
| P15 | **Cloud Security Alliance research note: third-party AI assurance standards** | 27 Sep 2026 | CSA-AIASSURE-2026 | read | ISO/IEC 42006 sets competence and independence rules for AI-management-system auditors; AIUC-1 named Schellman its first accredited auditor in Feb 2026; EU AI Act conformity-assessment bodies were slow to be designated. The document says it was generated with AI assistance and not CSA-reviewed, so treat as a lead. |
| P16 | **ISACA AAIA certification; CPA Australia AI in Audit Playbook; CPA Canada series; IFAC Knowledge Gateway; ICAS commentary** | 2025–2026 | (pilot items P9, P13–P16) | snippet | Not re-opened. |

---

## 5. Academic

**Main journals and centres** (unchanged from the pilot; not re-verified): *Auditing: A Journal of Practice & Theory*, *Contemporary Accounting Research*, *The Accounting Review*, *Journal of Accounting Research*, *Review of Accounting Studies*, *Accounting Horizons*, *Journal of Emerging Technologies in Accounting*, *Journal of Information Systems*, *International Journal of Accounting Information Systems*. Centres: Rutgers CAR Lab, University of Duisburg-Essen (IRCG, MAARC), BYU, Hamburg, Tilburg, PCAOB Office of Economic and Risk Analysis.

| # | Work | Venue / date | Key | Status | Why it matters |
|---|---|---|---|---|---|
| A1 | Fedyk, Hodson, Khimich & Fedyk, "Is artificial intelligence improving the audit process?" | *Review of Accounting Studies*, 2022 | FEDYK-2022 | read (abstract page) | Anchor empirical study; pre-GenAI. |
| A2 | Commerford et al., "Man versus machine: complex estimates and auditor reliance on AI" | *Journal of Accounting Research*, 2022 | COMMERFORD-2022 | read (abstract) | Algorithm aversion in auditor judgments of complex estimates; relevant to specialists and valuation. |
| A3 | Peters, "Auditor automation usage and professional skepticism" | Working paper 2022; ESB article 2023 | PETERS-2022 | read (abstract) | Regulators worry auditors over- or under-rely on automation. |
| A4 | Fabian & Ratzinger-Sakel, AI-assisted audit of management reports at a German Big 4 firm | *Journal of Information Systems*, 2026 (university release 20 Mar 2026) | FABIAN-2026 | read | Survey of experienced auditors; mixed picture: gains on standardised tasks, limits on complex qualitative judgments; role and experience shape acceptance. Completion-and-reporting evidence. |
| A5 | Eulerich, Emett, Lipinski, Prien & Wood, ChatGPT in internal audit at Uniper | *Accounting Horizons*, 2025 (DOI 10.2308/HORIZONS-2023-111) | EULERICH-2025 | read (citation page only) | Named in-house case; efficiency figures in the pilot not re-verified. |
| A6 | Jezierski et al., "The Effect of LLMs on Audit Quality: Causal Evidence from a Randomized Field Experiment" | SSRN 6095166 (date not seen) | SSRN-LLMAQ-2026 | snippet (SSRN 403) | Search extract: 100 professional auditors at a global firm did an inventory-valuation task with or without a firm-specific LLM. Closest thing to a causal audit-quality result; valuation-specialist and substantive relevance. Author attribution inconsistent in the extract. |
| A7 | "Multi-Agent Framework for Audit Risk Assessment with Explicit Uncertainty and Evidence Conflict Modeling" (UMAR) | arXiv 2606.15640, Jun 2026 | ARXIV-UMAR-2026 | read (abstract) | Three agents (MD&A text, financial ratios, critical audit matters) fused by evidence theory; AUROC 0.782 on 3,200 10-K firm-years with restatement as the label. Planning-stage prototype. |
| A8 | "AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping" | arXiv 2512.02726, Dec 2025 | ARXIV-AUDITCOPILOT-2025 | read (abstract) | LLMs beat rule-based journal-entry tests and ML baselines on synthetic and anonymised real ledgers while giving explanations. A search extract adds that real-data precision falls sharply without a statistical hint (`snippet`). |
| A9 | "FinancialAuditBench" | arXiv 2609.32835, Sep 2026 | ARXIV-FAB-2026 | read (abstract) | 90 workpaper completion and review tasks across six synthetic engagements (about 179 files each), 11 frontier models: agents complete much staff-level work but sometimes perform inappropriate procedures or write incorrect documentation. First agent benchmark on whole-engagement audit work. |
| A10 | "FinAuditing" (XBRL multi-document benchmark) | arXiv 2510.08886, Oct 2025 | ARXIV-FINAUDITING-2025 | read (abstract) | 1,102 instances; 13 LLMs show gaps in concept retrieval, relation modelling and cross-document reasoning. Completion-and-reporting evidence. |
| A11 | "Automating Financial Statement Audits with LLMs" | arXiv 2506.17282, Jun 2025 | ARXIV-LLMAUDIT-2025 | read (abstract) | Five-stage benchmark mapping statement errors to standard violations. |
| A12 | "Small Seems Plausible: Effects of Magnitude Appearance on Auditors' Judgments of AI-Detected Correlations" | KU/Deloitte symposium research session, May 2026 | KU-SYMPOSIUM-2026 | read (agenda only) | Experimental research on how auditors weigh AI-detected patterns. |
| A13 | "Artificial Intelligence in Sustainability Assurance" (conceptual framework) | *MDPI*, 2026 (volume 2, issue 3) | MDPI-SUSAI-2026 | snippet (MDPI 403) | Search extract: proposes graded reliance ceilings and non-delegable judgments, tied to ISSA 5000; requires data lineage and tool lineage. |
| A14 | Generative AI in discounted-cash-flow valuation (paper) | Reference Global, Jul 2026 | REFGLOBAL-DCF-2026 | read (abstract page only) | Flags look-ahead leakage and unsupported factual claims in LLM valuation. |
| A15 | Holmstrom & Peters registered report; Li & Goel (IJAIS 2025); Torroba et al.; Emett-type reviews; "Auditable Agents" (arXiv 2604.05485) | 2024–2026 | (pilot items A4, A12, A13, A15) | snippet | Not re-opened. |

---

## 6. Firms

| # | Firm / item | Date | Key | Status | What the opened page says |
|---|---|---|---|---|---|
| F1 | **EY**: agentic AI in EY Canvas | 7 Apr 2026 | EY-CANVAS-2026 | read-secondary (CPA Practice Advisor; EY page not opened) | Multi-agent framework on Microsoft Azure, Foundry and Fabric; 1.4 trillion journal-entry lines a year; all phases now, end-to-end support expected by 2028; global training programme; assurance services over AI diagnostics, governance and controls. |
| F2 | **KPMG**: AI agents in KPMG Clara; Financial Report Analyzer | 22 Apr 2025 | KPMG-CLARA-2025 | read | Agents for expense vouching, unrecorded liabilities and accrued expenses; FRA output feeds disclosure checklists; more agents over 12 months into controls testing and financial statement analysis. Earlier steps: GenAI in Clara for 90,000 auditors (Jul 2024) helping refine risk assessments and design substantive procedures; Copilot used for walkthrough narratives and flowcharts (Apr 2024). |
| F3 | **KPMG**: *The future of SOX 2030* | 24 Sep 2026 | KPMG-SOX-2026 | read | Continuous, automated, predictive testing; synthetic data; 100% transaction coverage; new mandate to assure AI systems; black-box and human-in-the-loop challenges. Controls-testing source (pilot module). |
| F4 | **KPMG UK**: *Reimagining controls assurance with AI*; AI Governance Assurance; AI Trust | Jan 2026; 2026 | KPMGUK-CONTROLS-2026; KPMGUK-GOVAI-2026; KPMGUK-AITRUST-2026 | read | Reasonable-assurance opinion over AI governance and controls under ISAE (UK) 3000, using SOC principles and a Trusted AI framework informed by ISO/IEC 42001 and the EU AI Act; the controls-assurance paper cites about 18% testing-time reductions. AI Trust PDF opened but had little extractable text. |
| F5 | **KPMG Nederland**: AI Assurance added to Responsible AI services | Sep 2025 | KPMGNL-AI-2025 | read | Independent checks of AI systems, algorithms and data analytics. |
| F6 | **Deloitte**: connected agentic intelligence in Omnia | 24 Jun 2026 | DELOITTE-OMNIA-2026; BBL-DELOITTE-2026 | read | Agents execute preliminary procedures (extraction, evidence analysis, draft documentation, preliminary conclusions for review), assist with compliance and disclosure evaluation, tutor mode for micro-training; separate AI Assurance offering. Bloomberg Law adds agents scanning media for emerging threats and drafting staff memos. |
| F7 | **PwC**: Oct 2025 briefing; Oct 2026 follow-up | 28 Oct 2025; 7 Oct 2026 | PWC-AT-2025; CFODIVE-PWC-2026 | read | Tools by step: Simplified Audit for Private Business (planning), Advanced Walkthrough Assistant, risk-assessment tool "soon", Evidence Match (extracts and matches evidence; cash, receivables, payables), controls-testing automation modelled on it, Audit Innovation Hub (fund tie-outs). Oct 2026: Simplified Audit - Execute reads supporting documents and flags gaps; a tool analyses audit-committee communications; global agentic platform about 18 months after 2026. |
| F8 | **Grant Thornton US**: Gtap | 7 May 2026 | GT-GTAP-2026 | read | Analytics and automation platform with AI agents that flag risks and anomalies; built originally by GT Ireland; private audits first, public next year; operates under an alternative practice structure since New Mountain Capital's 2024 acquisition (attest services in the licensed firm, non-attest in a separate advisory entity); the article says the combined platform now spans nearly 25,000 people. Relevant to independence. |
| F9 | **RSM US**: Beacon with Andera; Ask Luca; Luca Resourcing | 26 Aug 2026; 25 Aug 2026 | RSM-BEACON-2026; CAQ-RSM-2026 | read | Control-testing alliance; assurance guidance copilot; staffing tool. |
| F10 | **BDO USA**: *AI: IT audit considerations with a focus on ITGCs* | 2026 (undated PDF; cites COSO's 2026 guidance) | BDO-ITGC-2026 | read | ITGCs may need to extend to AI components; distinguishes COSO "reliance" (management depends on AI output without re-performing) from non-reliance. Specialists and controls source. |
| F11 | **Deloitte DART, RSM, BDO recaps** of the Dec 2025 SEC/PCAOB conference | Dec 2025 | DART-SECPCAOB-2025; RSM-SECPCAOB-2025; BDO-SECPCAOB-2025 | read | Firms' summaries of regulator statements on AI. |
| F12 | **KPMG audit-fee episode** (KPMG argued its own auditor's fee should reflect AI) | Feb 2026 | VERDANTIX-KPMGFEE-2026 | read | Commentary only; the page gives no fee figures (the pilot's $416k to $357k figure is not confirmed). Flags a pricing-model question. |
| F13 | **Modus** (AI-native audit technology platform and holding company) | 7 Apr 2026 | MODUS-2026 | read-secondary | $85M seed and Series A led by Lightspeed; invests in audit-first accounting firms (one unnamed top-200 firm with $30M+ revenue). Structural model that raises independence questions. |
| F14 | **Repodo** (Denmark, new AI-built authorised audit firm) | 25 Aug 2026 | REPODO-2026 | read | €8.2M pre-seed; SME audits first; ex-Lunar founders. |
| F15 | **Oath Verified** (venture-backed assurance firm using an alternative practice structure; chief assurance officer is a former PCAOB board member) | 2026 | AT-PEEC-2026 | read-secondary | Building an "AI-native audit" methodology; hires "accountant engineers"; about $10M raised. |
| F16 | Clark (formerly uiAgent) | Jun 2026 | (search extract) | snippet | Rebranded; says 35+ CPA firm clients. A "Material Intelligence" product trade headline was not confirmed. |
| F17 | **KPMG US webcast: SOC reporting, AI risks and the changing Trust Services Criteria** | 2026 (date not captured) | KPMG-SOC-2026 | read | Agenda: when a service organisation's AI use is relevant to a SOC 1 or SOC 2 examination, effect on system description, risk assessment, governance and team competence, and the expected restructuring of the Trust Services Criteria. |
| F18 | **In-house**: Microsoft Internal Audit; Reddit Internal Audit; Uniper; PayPal | 2024–2026 | (pilot F17–F19); OPTRO-CRX-2026 | read (Reddit via Optro release); others snippet | Reddit automated 175 controls in the first three months (vendor release). |

---

## 7. Vendors

| # | Vendor | Recent AI news | Key | Status | Modules touched |
|---|---|---|---|---|---|
| V1 | **MindBridge** | Agentic Risk Assessment (22 Sep 2026): evidence-linked risk assessment tied to assertions, materiality and methodology; Analysis Designer Agent preview; MCP server; works with customer-built and third-party workpaper tools. | MINDBRIDGE-ARA-2026 | read | Planning; journal-entry testing |
| V2 | **Caseware** | AiDA (2024) became Verity (agentic); Disclosure Checklist Agent (beta firms saved 2.7 hours per checklist run, vendor figure); nothing written into the engagement without human acceptance. | CASEWARE-VERITY-2026 | read | Planning review; completion |
| V3 | **Thomson Reuters** | Audit Intelligence Test (with Valid8 Financial) matches samples to evidence and bank activity; CoCounsel Document Analysis (early adopters: up to 70% faster preparation and review); Disclosure Review (23 Sep 2026: about 30% of eligible customers using it, close to 300 analyses a month, checklists of 1,200–1,500 requirements). | TR-AGENTIC-2025; TR-DISCLOSURE-2026; TR-STATE-2026 | read | Substantive; completion |
| V4 | **DataSnipper** | AI agents with Microsoft (2025); DocuMine; claims 600,000+ users in 175 countries and "$1.4B productivity savings" (vendor claims). | DATASNIPPER-2026 | read | Substantive; controls |
| V5 | **Circit** | $22M growth equity (10 Feb 2026) for confirmations and bank-verified data; claims 400+ audit firms and 30,000+ evidence providers. | CIRCIT-2026 | read | Substantive (confirmations) |
| V6 | **Optro (ex-AuditBoard)** | Domain-trained agents; Autonomous Testing beyond SOX; agentic stakeholder management for evidence requests; AI governance agents (14 Oct 2026). | OPTRO-CRX-2026 | read | Controls; internal audit |
| V7 | **Fieldguide** | $75M Series C, $700M valuation (2 Feb 2026); platform spans risk assessment, financial audits and compliance. | FIELDGUIDE-2026 | read-secondary | Planning through reporting |
| V8 | **Petual** | $20M (Apr 2026); claims 68–80% efficiency gains. | PETUAL-2026 | read-secondary | Controls |
| V9 | **Andera** | $37M Series A (Jun 2026); control testing across SOX, operational, compliance. | ANDERA-2026 | read-secondary | Controls |
| V10 | **Workiva** | Agent Studio; evidence, attribute and testing agents; Tie Out and Sustainability Disclosure agents (Jul 2026, per search extract). | WORKIVA-AMPLIFY-2026; VERDANTIX-AMPLIFY-2026 | read | Controls; completion; sustainability |
| V11 | **Ideagen Disclose** | AI scans PDFs and pre-fills disclosure checklists; claims use by 9 of 10 top UK firms (vendor claim). | IDEAGEN-DISCLOSE | read | Completion |
| V12 | **Kingland** | Acceptance and continuance workflow with independence, KYC and risk checks; AI with confidence scoring and human-in-the-loop. | KINGLAND-ACCEPT | read | Acceptance and independence |
| V13 | **Intapp** | Intake, conflicts and independence monitoring (pilot claims use at 10+ top-25 firms). Pages return 403. | INTAPP-2026 | blocked | Acceptance and independence |
| V14 | **Thomson Reuters acceptance and continuance guidance** | Process article tying acceptance to QC 1000. Not an AI product page. | TR-ACCEPT-2025 | read | Acceptance and independence |
| V15 | **Vanta, Drata; Delve allegations** | Client-side SOC readiness; contested practices. | (pilot V15) | snippet | Other assurance |
| V16 | **Verdantix Green Quadrant for ESG assurance (2024)** | 14 assurance providers benchmarked; analyst note says Deloitte's offer is streamlined by AI-enabled digital tools. | VERDANTIX-GQ-2024 | read (summary page) | Sustainability assurance |
| V17 | **Gartner** (CAE surveys; SOX testing guide) | Gated analyst research. | GARTNER-2026 | read (Jan 2026 release); Aug 2026 release blocked | All |

---

## 8. Press, podcasts & communities

**Trade press (items opened this run)**

| # | Outlet | Representative item | Key | Status |
|---|---|---|---|---|
| N1 | Accounting Today | PwC end-to-end plan (28 Oct 2025); AICPA practice guide (14 Oct 2026); AICPA PE and tech independence (31 Aug 2026); PCAOB specialists consultation (2015) | PWC-AT-2025; AT-AICPAPA-2026; AT-PEEC-2026 | read |
| N2 | Journal of Accountancy (AICPA) | AICPA practice aid (Oct 2026); COSO GenAI (Feb 2026); SOC tool-provider ethics (6 Apr 2026); PEEC (Aug 2026); PE independence (Mar 2025) | JOFA-AIPA-2026; COSO-GENAI-2026; JOFA-SOCETH-2026; JOFA-PEEC-2026 | read |
| N3 | CPA Practice Advisor | EY (7 Apr 2026), RSM/Andera, Workiva, Circit, Modus, PCAOB agendas; Accounting Technology Lab podcast | EY-CANVAS-2026; CPAPA-PCAOBAGENDA-2026 | read |
| N4 | CFO Dive | PwC one year on (7 Oct 2026) | CFODIVE-PWC-2026 | read |
| N5 | Bloomberg Law / Bloomberg Tax | Deloitte agents (Jun 2026); headline list shows EY (6 Apr 2026) and "KPMG to Test Advanced AI Agents in Next Phase" (1 Apr 2026) | BBL-DELOITTE-2026 | read (KPMG item headline only) |
| N6 | Corporate Board Member | CAQ pulse for audit committees | BOARDMEMBER-CAQ-2026 | read |
| N7 | CAalley | NFRA principles; PCAOB on AI and PE | NFRA-CAALLEY-2026; CAALLEY-PCAOBPE-2025 | read |
| N8 | Thomson Reuters Tax & Accounting news | PCAOB strategic plan; SEC Hohl | TR-PCAOBPLAN-2026; TR-HOHL-2026 | read |
| N9 | Starling Insights | PCAOB inspection modernisation | STARLING-IMC-2026 | read |
| N10 | Verdantix blog | KPMG fee argument | VERDANTIX-KPMGFEE-2026 | read |
| N11 | Accounting Weekly (CIBA author) | AI audit tools and the independence gap (1 Sep 2026). Opinion piece; low authority. | ACCWEEKLY-INDEP-2026 | read |
| N12 | MYCPE Insights | SEC independence framework speculation (24 Nov 2025). Low authority; superseded by the Hohl remarks. | MYCPE-SEC-2025 | read |
| N13 | ICAEW viewpoints | AI adoption trends (Jan 2026), FRC guidance, audit reform | ICAEW-FRCVIEW-2026 | read |
| N14 | Financial Times, Going Concern, Accountancy Age | Not opened (paywall or 403). | — | blocked |

**Podcasts**

| # | Show | Episode | Key | Status |
|---|---|---|---|---|
| D1 | ICAEW *Beyond Finance* | "How should audit firms use AI?" with Ramana McConnon (Head of Assurance Technology, FRC), Jon Morris (Grant Thornton) and Martin Brown (Deloitte GenAI lead, audit technical team); topics include smaller-firm use cases, explainability and human oversight, off-the-shelf tools. Date 11 Nov 2025 per pilot. | ICAEW-POD-2025 | read (show notes) |
| D2 | CPA Practice Advisor *Accounting Technology Lab* | Recap of SYNERGY 2025 audit and accounting announcements | CPAPA-SYNERGY-2025 | read (transcript) |
| D3 | Richard Chambers, "swarm auditing" with PayPal | 11 Feb 2026 | SRA-SWARM-2026 | snippet (page opened but near-empty) |
| D4 | IESBA *Decoding Ethics*; TR *Clarity on Tech*; *The Audit Podcast*; *The Accounting Podcast* | Listed on pilot or IESBA page | (pilot D1, D5, D6) | snippet |

**Communities.** ISACA chapters and the IIA's AuditSphere (not opened); CAQ's "Audit in Action" blog (read; includes RSM post); Reddit r/Accounting and r/auditing (blocked, 403); LinkedIn (not used).

---

## 9. Surveys & benchmarks

| # | Survey | Date / sample | AI finding | Key | Status |
|---|---|---|---|---|---|
| S1 | **CAQ Audit Partner Pulse, Spring 2026** | 15 Jul 2026 | AI and data analytics ranked a top strategic priority of audit partners' largest clients for the first time since 2022. On AI governance at the largest client: 6% advanced, 40% developed but incomplete or inconsistent, 46% early-stage or reactive. AI governance is the top audit-committee challenge (57%, ahead of cybersecurity 51% and finance transformation 36%). Top AI-related control gaps: in-house expertise 33%, missing governance frameworks 27%, thin model documentation 26%. About two-thirds say the audit committee raised AI use in operations or reporting. | CAQ-PULSE-2026 | read-secondary |
| S2 | **AICPA and CPA.com, 2025 Audit Benchmark** (in the Audit Transformation Report) | Survey Jun–Aug 2025; 74 firms registered, 54 with complete data | 75% have no documented transformation plan; about one in four use no AI or advanced automation (the report also says about one-third use no AI at all). Firms with an automated solution for: workflow management 39%, foot and proofing 39%, confirmations 39%, trial-balance import 35%, engagement letters 26%, risk assessment 22%, data ingestion 19%, report production 17%, substantive analytics 11%, none 22%. Top blockers: staff not trained 66%, poor client data 60%, no access to client systems 53%, budget 53%. ROI priority: staff efficiency 83%, quality 54%. 66% tell clients about their technology as a differentiator. | CPACOM-ATR-2025 | read |
| S3 | **IFIAR members' observations of automated tools** | 2023 and 2024 annual survey (about 44–49 members answering) | See R5: journal entries 88%, risk assessment 55%, substantive 55%, controls testing 43%, IT applications 39% "frequently" seen in 2024. | IFIAR-TTF-2025 | read |
| S4 | **Gartner CAE survey** | 119 CAEs, Aug 2025; released 27 Jan 2026 | 83% of audit functions piloting or using AI, 12% plan to within the year; over 70% rank GenAI and analytics as important priorities but report low confidence in achieving them (data quality, skills). | GARTNER-2026 | read |
| S5 | **Gartner webinar poll** | 743 respondents; 11 Aug 2026 | Figures carried from the pilot: 93% use some AI, 38% have a strategy, 30% use GenAI for testing versus 60% for drafting. | GARTNER-AUG-2026 | snippet (403) |
| S6 | **ISACA AI Pulse Poll 2026** | 3,400+ digital-trust professionals | 38% have a formal, comprehensive AI policy (28% in 2025); 22% say AI ROI met expectations; 90% believe employees use AI; 56% do not know how long it would take to halt an AI system after a security incident. | ISACA-PULSE-2026 | read |
| S7 | **Thomson Reuters Institute, *Future of Professionals 2026*: tax and audit** | Jul 2026 | 81% of tax and audit professionals use AI regularly; over a quarter would not take a job at a firm without professional-grade AI; about a third would consider leaving if AI expectations are unmet within two years. (Pilot's 35% unapproved-AI and 49% entry-level figures not on the opened page.) | TRI-FOP-2026 | read (summary page) |
| S8 | **EY SOC conference live poll** | Sep 2026; multiple answers allowed | AI uses in SOC work: evidence collection 63%, drafting Section 3 system description 45%, drafting management responses to deviations 41%, project management 29%. | EY-SOC-2026 | read |
| S9 | **Reuters Events, *Sustainability Reporting Outlook 2025*** (via TR Institute) | 2025 | Of organisations reporting Scope 1–3 emissions with assurance, 37% use AI in reporting versus 22% without assurance; nearly 90% expect material AI impact; data quality is a concern for 50%. Preparer-side, not assurance providers. | TRI-SUSTAIN-2025 | read-secondary |
| S10 | **KPMG Q2 2026 AI Pulse** | 29 Sep 2026; US companies, cross-industry | Agent deployment 53% (55% prior quarter); firms orchestrating several agents 9% to 18%. Not audit-specific; context for client-side AI. | KPMG-PULSE-2026 | read |
| S11 | Wolters Kluwer internal audit survey; IIA/AuditBoard pulse; Protiviti agentic pulse; KPMG 2024 financial reporting survey; IIA Risk in Focus 2026; CAQ audit-committee report | 2024–2026 | Carried from the pilot. | (pilot S6–S14) | snippet |

**Model-capability benchmarks (read):** FinAuditing (ARXIV-FINAUDITING-2025), FinancialAuditBench (ARXIV-FAB-2026), the five-stage LLM audit benchmark (ARXIV-LLMAUDIT-2025), AuditCopilot (ARXIV-AUDITCOPILOT-2025). No public benchmark of controls testing was found.

---

## 10. Module check

**Evidence density per module** (judged by how much specific, opened public material exists; strength of independent versus vendor evidence is noted separately):

| Module | Density | Basis (opened sources) | Gaps that limit it | Suggested deep-dive allocation |
|---|---|---|---|---|
| acceptance-independence | **Medium** | The AICPA practice aid's acceptance and continuance section; a live regulatory thread on AI and independence (PEEC second draft, SEC OCA review, PCAOB independence project, SOC tool-provider ethics article, IESBA NAM); PCAOB statements on private equity; a KU conference panel; structural cases (Gtap under an alternative practice structure, Modus, Repodo, Oath); acceptance workflow vendors. | Almost no evidence of AI making acceptance decisions in practice; Intapp pages blocked; IESBA documents not opened; no named firm case study. | Full deep dive, framed as two questions: AI tools in acceptance and independence checks, and AI creating acceptance risk and independence threats. |
| planning-risk-assessment | **High** | FRC worked example; IFIAR 55% frequency; ICAEW model test; MindBridge, PwC, KPMG, Deloitte, EY, Caseware, Fieldguide tool descriptions; AICPA understanding-the-entity section; IAASB ED-520 on risk-assessment analytics; CPA.com 22% automation; an agent prototype paper. | Almost all outcome figures are vendor or firm claims; no inspection finding specific to AI risk-assessment tools. | Full deep dive. |
| controls-testing | (pilot) High | Verified in the pilot module; this scan adds IFIAR 43%, IAASB ED-330 sections, KPMG SOX 2030, vendor funding. | — | Already done. |
| substantive-testing | **High** | KPMG agents; TR Audit Intelligence Test; DataSnipper; Caseware; Circit; MindBridge; EY journal-entry scale; FRC contract-review example; IFIAR 88% and 55%; IAASB EDs on evidence and analytics; CPA.com confirmations 39% and substantive analytics 11%; two LLM benchmarks; an audit-quality field experiment (abstract only). | No independent measure of tool accuracy in live audits; vendor time-saving claims dominate. | Full deep dive; split journal-entry and fraud testing from document-matching and confirmations if time allows. |
| specialists | **Medium for IT-audit specialists; Low for valuation, actuarial and other specialists** | IT audit: BDO ITGC paper, COSO reliance definition, AICPA practice aid on AI-operated controls and service reports, IFIAR IT-application findings, ISACA AAIA. Others: IVSC paper, ISA 620 revision (effective 15 Dec 2026), PCAOB specialists spotlight (no AI), one valuation field experiment (abstract unreachable), Commerford. | No firm announcement or regulator statement on AI use by valuation or actuarial specialists was found; PCAOB specialists material predates GenAI. | One combined deep dive for valuation and other specialists, merged with a short IT-audit pass; or fold IT audit into controls-testing and "assurance over AI". |
| completion-reporting | **Medium** | Three disclosure-checklist agents with usage figures (TR, Caseware, KPMG), Ideagen; one peer-reviewed field study on management-report audits; two benchmarks; PCAOB going-concern project; PwC audit-committee communications tool; CAQ audit-committee data. | Nothing public on going-concern assessment, subsequent events, engagement quality review, key audit matters or opinion drafting with AI. | Full deep dive centred on disclosure review, representations, audit-committee communication and report drafting; list the unevidenced steps as open questions. |
| quality-management | **High** | FRC thematic review and two guidance documents (read in full); IFIAR report; IAASB roundtables; PCAOB QC 1000 amendments, strategic plan and inspection modernisation; AICPA practice aid Part 2; NFRA, CPAB; SEC OCA; CAQ pulse; firm resourcing tool. | Big Four transparency reports blocked or not searched; 2025–2026 inspection findings specific to AI tools not found. | Full deep dive; split firm-level (tool governance) from engagement-level (supervision and review). |
| other-assurance | **Medium overall: High for SOC and assurance over AI; Low for sustainability** | SOC: TQA 9561 (landing page, secondary), EY SOC highlights with poll data, KPMG UK controls paper, tool-provider ethics article, CSA notes. Assurance over AI: KPMG UK and NL services, EY and Deloitte offers, BSI 42006, ACCA/EY taxonomy. Sustainability: ISSA 5000 date, Verdantix note, preparer survey. | Sustainability assurance has almost no AI-in-practice evidence from assurance providers; TQA 9561 full text behind a login. | Two deep dives: SOC plus assurance over AI; sustainability as a short add-on. |

**Is the module list right?** It follows the ISA and PCAOB lifecycle and the pilot's changes remain sound. The opened evidence supports these changes:

1. **Split other-assurance into three** (SOC and attestation; sustainability; assurance over AI systems). Evidence density differs sharply, and the assurance-over-AI work (KPMG UK ISAE (UK) 3000 service, BSI 42006, ACCA/EY taxonomy) has its own standards and buyers.
2. **Reframe acceptance-independence around two directions**: AI tools used for acceptance and independence monitoring, and AI-driven structural change (private equity, alternative practice structures, tool-vendor relationships) that creates independence and acceptance risk. The second direction has the stronger evidence.
3. **Narrow specialists** to using the work of experts (ISA 620, AS 1210) and add "AI as a specialist-like input" (the AICPA practice aid compares heavy client AI reliance with complex valuation models). Keep IT-audit work for AI components under controls-testing or a new assurance-over-AI cross-cut, where the BDO, COSO and AICPA material sits.
4. **Add a cross-cutting "data and evidence acquisition" theme.** The strongest US small-firm finding is that poor client data (60%) and lack of system access (53%) block transformation; confirmations, trial-balance import and foot-and-proof are the most automated steps.
5. **Add "assurance over AI-enabled controls and financial reporting" as a cross-cutting theme.** The AICPA practice aid Part 1, COSO and KPMG all frame it; the pilot's controls-testing module already holds one sub-topic of it.
6. **Split quality management** into firm-level tool governance (certification, monitoring, resourcing; QC 1000, ISQM 1) and engagement-level supervision and review of AI output (FRC control points, automation bias research). The FRC documents treat them separately.
7. **Name journal-entry and fraud testing** as a sub-area of substantive testing. It is the most mature use (IFIAR 88%) and AI-enabled fraud is a recurring theme (AICPA, GAM, ACFE).
8. **Add "audit firm business model and workforce" as a cross-cutting lens** rather than a module: fee pressure, private-equity capital, graduate-intake changes, AI-native entrants.

---

## 11. Journey-stage markers

Markers are written for audit firms and internal audit functions, drawing on opened evidence where possible.

| Stage | Observable markers |
|---|---|
| **Curious** | No documented transformation plan (75% of US firms, CPACOM-ATR-2025). No automated audit solution (22%) or no AI use (about a quarter to a third). Staff use public chatbots outside policy while leaders attend vendor sessions at ENGAGE, GAM or DCPA. No inventory or certification process for tools, the gap the FRC flagged at weaker firms (FRC-ATT-2025). |
| **Experimenting** | An enterprise assistant under a use policy (Copilot, firm-approved guidance copilot such as RSM's Ask Luca, CAQ-RSM-2026). Point tools on a few engagements: confirmations, foot-and-proof, trial-balance import, document extraction (39%, 39%, 35% in CPACOM-ATR-2025). GenAI used for research, summaries and drafting more than for testing. Early maturity levels in the IIA NL model (IIANL-GENAI-2026). |
| **Adopting** | Tools certified per use case and recertified on change (FRC-GENAI-2026 certification section). Human control points written into methodology; reviewers trained on how to review AI output. Risk-assessment and disclosure-checklist agents used by default on defined engagement types (TR-DISCLOSURE-2026, CASEWARE-VERITY-2026). AI use explained to audit committees, which now ask first (CAQ-PULSE-2026). |
| **Scaling** | Agents across phases on a central platform (EY Canvas, KPMG Clara, Deloitte Omnia). Monitoring of tool use and quality impact at network and member-firm level, which IFIAR said was unclear in many networks (IFIAR-TTF-2025). Engagement with regulators through sandboxes or comment letters. Staffing and resourcing tools tied to AI (RSM Luca Resourcing). |
| **AI-native** | Methodology designed around whole-population work with sampling by exception (KPMG-SOX-2026). Firms or platforms built around AI from the start (Repodo, Modus-backed firms, Oath Verified, PwC Australia pilot per pilot). Ownership or fee models that depend on AI economics, with independence rules being rewritten around them (JOFA-PEEC-2026, TR-HOHL-2026). New services that assure AI itself (KPMGUK-GOVAI-2026). |

---

## 12. Frontier signals (next 12–36 months)

| # | Date | Signal | Key |
|---|---|---|---|
| FS1 | 5 Aug 2026 (comments due 15 Dec 2026) | IAASB's ED-500 states that GenAI challenges the input-output model of audit evidence and chooses guidance over a technology requirement; non-authoritative material on technology to follow. Final standards likely 2027–2028 (inference). | IAASB-ED500-2026 |
| FS2 | 13 Oct 2026 | AICPA issues its first AI practice aid for financial statement auditors; more sections on risk of material misstatement and evidence are promised. | AICPA-PA-2026 |
| FS3 | 30 Sep 2026 | PCAOB agendas: data and technology research project continues; independence, fraud, going concern and NOCLAR standard-setting projects; QC 1000 amendments approved 9 Sep, effective 15 Dec 2026. | CPAPA-PCAOBAGENDA-2026 |
| FS4 | May–Aug 2026 | PCAOB's Inspections Modernization Council: inspections to centre on firm quality-control systems, with early AI pilots in inspection work. Firms' QC of AI tools becomes the inspected object. | STARLING-IMC-2026 |
| FS5 | 30 Mar 2026; Jun–Jul 2026 | FRC publishes generative and agentic AI guidance, then runs a sandbox; first regulator co-design of firm AI adoption. Sandbox outputs likely late 2026 or 2027 (inference). | FRC-GENAI-2026; FRC-SANDBOX-2026 |
| FS6 | 7 Apr 2026 | EY embeds agents in all audit phases for 130,000 staff and targets end-to-end support by 2028. | EY-CANVAS-2026 |
| FS7 | 24 Jun 2026 | Deloitte unifies agents in Omnia for about 85,000 practitioners; agents produce preliminary conclusions for human review. | DELOITTE-OMNIA-2026 |
| FS8 | 28 Oct 2025; 7 Oct 2026 | PwC targets a tool for every audit step in 2026 and a global agentic platform about 18 months later. | PWC-AT-2025; CFODIVE-PWC-2026 |
| FS9 | 7 May 2026 | Grant Thornton US launches Gtap, private-company audits first and public companies the next year, under an alternative practice structure. | GT-GTAP-2026 |
| FS10 | 7 Apr 2026; 25 Aug 2026 | Venture capital funds AI-native audit: Modus ($85M, invests in firms) and Repodo (new AI-built audit firm). | MODUS-2026; REPODO-2026 |
| FS11 | Dec 2025 – Oct 2026 | Independence rules are being revised for private equity and AI: PEEC second draft (October interim meeting), SEC OCA review starting with FAQs and nonbinding guidance, PCAOB independence project. | JOFA-PEEC-2026; TR-HOHL-2026; CPAPA-PCAOBAGENDA-2026 |
| FS12 | 2026 | SOC and AI assurance become distinct products: TQA 9561 (11 Sep 2026), KPMG UK's reasonable-assurance opinion over AI governance (ISAE (UK) 3000), EY's AI assurance conference focus. | AICPA-TQA9561-2026; KPMGUK-GOVAI-2026; EY-SOC-2026 |
| FS13 | 15 Dec 2026 | ISA 620 revisions (use of experts) and ISSA 5000 both take effect; QC 1000 also takes effect. | FRC-620-2026; IAASB-ISSA5000-2026 |
| FS14 | Sep 2026 | Agent benchmarks on whole audit engagements show partial competence with inappropriate procedures and documentation errors; expect firm-specific evaluation sets to become a differentiator. | ARXIV-FAB-2026 |
| FS15 | 15 Jul 2026 | Audit partners report immature client AI governance (6% advanced) and audit committees ask about AI first: client-side AI creates new risk assessment, controls and acceptance work. | CAQ-PULSE-2026 |
| FS16 | 23 Sep 2026; 28 Jul 2026 | Disclosure-checklist agents ship at scale (about 300 TR analyses a month; Caseware beta 2.7 hours saved per run) and extend toward harder "not applicable" judgments. | TR-DISCLOSURE-2026; CASEWARE-VERITY-2026 |
| FS17 | 14 Oct 2026 | Evidence-request and testing agents extend beyond SOX to operational audit; evidence collection agents "upcoming". | OPTRO-CRX-2026 |

---

## 13. Research leads per module

### acceptance-independence
1. **AICPA-PA-2026 Part 1** (acceptance and continuance section). Obtain the full practice aid (free AICPA login) and extract the acceptance considerations, the AU-C 210 engagement-letter position and the state-law AI disclosure point.
2. **AICPA PEEC second exposure draft** after the October 2026 interim meeting, plus the 81 comment letters on the first draft (JOFA-PEEC-2026, AT-PEEC-2026). Focus on tool-vendor relationships and network-firm definitions.
3. **SEC OCA independence review** (TR-HOHL-2026, KPMG-HOHL-2026): track the refreshed FAQs and any guidance on AI in audit delivery.
4. **PCAOB auditor-independence standard-setting project** (CPAPA-PCAOBAGENDA-2026) and Gunia's QC-inspection focus on private-equity firms (CAALLEY-PCAOBPE-2025).
5. **JOFA-SOCETH-2026** and the AICPA ethics staff article "AI through an ethics lens": test whether the SOC tool-provider reasoning transfers to audit AI vendors.
6. **IESBA emerging-technologies non-authoritative material (Jul 2026), snapshot (Jun 2026) and the June 2026 board agenda item** (IESBA-TECH-2026): open the underlying documents.
7. **Structural cases:** Grant Thornton Gtap and its alternative practice structure (GT-GTAP-2026), Modus (MODUS-2026), Repodo (REPODO-2026), Oath Verified; the KU panel on ownership and independence (KU-SYMPOSIUM-2026), whose organisers may share materials.
8. **Acceptance tools:** Kingland (KINGLAND-ACCEPT), Intapp (blocked; try investor materials), PwC UK's acceptance and continuance system described in its transparency report; look for any named firm case with measured effect.
9. Search directions: "client risk scoring audit firm machine learning", "predecessor auditor communication AI", "audit fee AI pricing" (VERDANTIX-KPMGFEE-2026), "engagement letter AI disclosure state law".

### planning-risk-assessment
1. **FRC-GENAI-2026 illustrative example 1** (board-minutes summarisation): the full mitigation table and its documentation expectations.
2. **ICAEW-PIERPOINT-2025**: repeat the test with current models and with the ISA 315 and ISA 240 requirements as the scoring frame; look for a follow-up article.
3. **MINDBRIDGE-ARA-2026**: documentation of assertion and materiality mapping; customer names; the planned MCP server.
4. **PwC tool stack** (PWC-AT-2025, CFODIVE-PWC-2026): the promised risk-assessment tool, Advanced Walkthrough Assistant, the audit-committee communications tool.
5. **KPMG Clara**: July 2024 GenAI for risk assessment (KPMG-CLARA-2025) and the April 2026 Bloomberg item on the next agent phase (BBL list headline).
6. **Caseware Verity planning-review agent** and Fieldguide risk-assessment workflows (CASEWARE-VERITY-2026, FIELDGUIDE-2026); the Clark "Material Intelligence" claim needs verification.
7. **IFIAR-TTF-2025 risk-assessment row (55%)** and the IFIAR 2025 survey (blocked): find what regulators say about weaknesses in tool-assisted risk assessment.
8. **ISA 315 (Revised 2019) and AS 2110** alongside IAASB-ED520-2026 (analytics in risk assessment) and the AICPA practice aid's understanding-the-entity section.
9. **Academic:** ARXIV-UMAR-2026; EULERICH-2025 (Uniper, risk identification and scoping); FEDYK-2022.
10. Search directions: "audit planning" with "LLM" and "materiality"; "risk of material misstatement" with "agent"; Optro scoping memos.

### substantive-testing
1. **KPMG Clara agents** for expense vouching and unrecorded liabilities (KPMG-CLARA-2025): find any measured results or regulator comments.
2. **TR Audit Intelligence Test and CoCounsel Document Analysis** (TR-AGENTIC-2025): named customer cases beyond the one practitioner quote; Valid8 Financial's methodology.
3. **IAASB-ED500-2026 explanatory memorandum, section 1-F, and ED-520 application material**: map exactly what the standards would require of tool-assisted evidence; read comment letters after 15 Dec 2026.
4. **Journal-entry testing**: FRC illustrative example (FRC-AIAUDIT-2025), IFIAR's 88% (IFIAR-TTF-2025), ARXIV-AUDITCOPILOT-2025, MindBridge case studies.
5. **Confirmations and bank data:** Circit (CIRCIT-2026), TR Confirmation; CPA.com's 39% confirmations automation (CPACOM-ATR-2025).
6. **FRC-GENAI-2026 example 2** (contract review for revenue recognition) and the PCAOB technology-assisted-analysis amendments (PCAOB-TAA-2024, blocked; try the Federal Register and SEC releases).
7. **SSRN-LLMAQ-2026** randomized field experiment: retrieve the abstract or paper via another route.
8. **Benchmarks:** ARXIV-FAB-2026, ARXIV-FINAUDITING-2025, ARXIV-LLMAUDIT-2025: what tasks agents fail, and whether firms publish internal equivalents.
9. **DataSnipper and Caseware Validate/Extractly**: independent evidence for productivity claims.
10. Search directions: "full population testing" with "ISA 530"; "inventory observation" with "drone" or "computer vision"; "AI analytical procedures expectation" with "ISA 520".

### specialists
1. **BDO-ITGC-2026**: full read; extract recommended ITGC extensions for AI components and how COSO "reliance" changes testing.
2. **AICPA-PA-2026**: AI-operated controls, third-party AI and reliance on service-organisation reports.
3. **COSO-GENAI-2026**: capability taxonomy and evidence expectations; AI as an input to control testing.
4. **ISA 620 revision** (FRC-620-2026) and the IAASB narrow-scope amendments: how competence and objectivity threats apply to AI-enabled experts and vendors.
5. **IVSC-AI-2025** paper and the Cologne conference (16–18 Nov 2026): model governance and explainability proposals for valuation standards.
6. **PCAOB-SPECIALISTS-2025** inspection themes as the baseline; monitor whether the PCAOB data and technology project touches specialists.
7. **SSRN-LLMAQ-2026** (inventory valuation) and COMMERFORD-2022 (reliance on AI for complex estimates); REFGLOBAL-DCF-2026 (LLM valuation failure modes).
8. **IFIAR-TTF-2025** IT application and security configuration findings (39% frequency) and ITGC testing findings.
9. **ISACA AAIA and AI audit toolkit** (pilot item; blocked source): curriculum and job-task analysis show what IT auditors are expected to do with AI.
10. Search directions: "IT audit specialist" with "agent" (Surgent, Crowe programmes seen in search results, not opened), "actuarial specialist" with "AI" and IFRS 17, "forensic specialist" with "deepfake evidence".

### completion-reporting
1. **TR-DISCLOSURE-2026**: usage and accuracy data; the planned extension to "no" and "not applicable" calls.
2. **CASEWARE-VERITY-2026** Disclosure Checklist Agent (2.7 hours per run) and KPMG Financial Report Analyzer (KPMG-CLARA-2025); Ideagen Disclose (IDEAGEN-DISCLOSE).
3. **FABIAN-2026** (management-report audit with AI) and ARXIV-FINAUDITING-2025 for the failure modes in cross-document consistency.
4. **PCAOB going-concern standard-setting project** (CPAPA-PCAOBAGENDA-2026): any reference to technology.
5. **Audit-committee communications**: PwC's tool (CFODIVE-PWC-2026), CAQ pulse data (CAQ-PULSE-2026), CAQ and Deloitte audit-committee practices report (pilot).
6. **Deloitte memo-drafting agents** (BBL-DELOITTE-2026) and Gartner's 60% drafting figure (GARTNER-AUG-2026, blocked).
7. **Unevidenced steps to probe in interviews:** going concern, subsequent events, representation letters, engagement quality review, key audit matters, opinion drafting.
8. Search directions: "engagement quality review" with "AI tool", "key audit matters" with "generative AI", "management representation letter" with "AI".

### quality-management
1. **FRC-ATT-2025** (full thematic review): lifecycle practices, good-practice examples, monitoring gaps.
2. **FRC-GENAI-2026** certification, recertification, training and oversight sections.
3. **IFIAR-TTF-2025** (monitoring responsibility between network and member firms; recertification when models update) and IFIAR-SURVEY-2026 (blocked).
4. **IAASB Technology Quality Management summary report** and the March 2026 action plan (IAASB-TQM-2026): retrieve both.
5. **PCAOB QC 1000** amendments (Sep 2026), Q&A resource and Inspections Modernization Council materials (CPAPA-PCAOBAGENDA-2026, STARLING-IMC-2026): open the primary pages by another route.
6. **AICPA-PA-2026 Part 2** quality-management policy list and the SQMS No. 1 link (CPACOM-ATR-2025).
7. **NFRA-CAALLEY-2026**, **CPAB-AI-2024**, **FSA-DP-2025** (finish reading): comparative regulator expectations.
8. **Firm resourcing and training:** CAQ-RSM-2026 (Luca Resourcing), Deloitte tutor mode (DELOITTE-OMNIA-2026), EY training programme (EY-CANVAS-2026); Big Four transparency reports (not reached).
9. **Academic angle:** PETERS-2022, FABIAN-2026, KU-SYMPOSIUM-2026 research paper on AI-detected correlations.

### other-assurance
1. **AICPA-TQA9561-2026**: full text via free AICPA account; DART-TQA-2026 summary.
2. **EY-SOC-2026** (read in full) and the **KPMG SOC webcast** (KPMG-SOC-2026): AI in SOC lifecycle and updated Trust Services Criteria.
3. **KPMGUK-CONTROLS-2026, KPMGUK-GOVAI-2026, KPMGNL-AI-2025**: scope, criteria and any issued opinion for AI governance assurance.
4. **JOFA-SOCETH-2026** and the AICPA "fast and easy" SOC credibility article (JofA 1 Feb 2026; URL not found), plus CSA research notes (CSA-SOC2-2026, CSA-AIASSURE-2026; the second says it was generated with AI assistance and not CSA-reviewed).
5. **Assurance over AI:** BSI-42006-2025, ACCA-EY-2025, PwC Canada ISO 42001 service (page blocked), Deloitte AI Assurance (DELOITTE-OMNIA-2026), EY's offer (EY-CANVAS-2026).
6. **Sustainability:** IAASB ISSA 5000 material (IAASB-ISSA5000-2026), VERDANTIX-GQ-2024, Workiva sustainability agents (WORKIVA-AMPLIFY-2026, VERDANTIX-AMPLIFY-2026), the MDPI conceptual framework (MDPI-SUSAI-2026, blocked).
7. Search directions: "ISSA 5000" with "automated tools"; "limited assurance" with "AI-generated data"; "AIUC-1 audit"; "EU AI Act conformity assessment auditor".

---

## 14. Gaps

**Corrections to the pilot (items checked against opened pages):**
- IIA GAM 2026: the organiser's release says more than 30 sessions and over 50 leaders; the pilot's 1,700 attendees and 70+ speakers are not confirmed.
- Deloitte/KU Auditing Symposium 2026 does include AI sessions (the pilot found none).
- A CAQ Audit Partner Pulse with AI figures exists (Spring 2026); the pilot reported none.
- The pilot's figure for KPMG's fee episode ($416k to $357k) does not appear on the opened commentary page.
- PCAOB QC 1000 was amended (approved 9 Sep 2026); effective date remains 15 Dec 2026.
- IFIAR's 2024 table (frequency of tools by area) is now read directly and matches the pilot's 43% and 88%.
- The AICPA practice aid, TQA 9561, FRC 30 Mar 2026 release, EY 7 Apr 2026 scale figures, KPMG 22 Apr 2025 agent list, Deloitte 24 Jun 2026 and IAASB ED dates are confirmed on opened pages.

**Blocked or not reachable:**
- `pcaobus.org` pages (403, except two PDFs): standard-setting projects page, TAA implementation page, QC 1000 postponement release, IMC release.
- `ifiar.org`, `gartner.com` (August 2026 release), `intapp.com`, `mindbridge.ai`, `schneiderdowns.com`, `agenda.aicpastore.com`, `events.icaew.com`, `pwc.com/ca`, `pwc.co.uk` transparency report, `bvresources.com`, `papers.ssrn.com`, `mdpi.com`, `nasba.org`, `crowe.com`, Reddit, Going Concern, Financial Times, BusinessWire direct pages.
- The AICPA TQA 9561 text and AICPA practice aid full text (login needed).
- CAQ pages `rota-ai` and Audit Partner Pulse render without text; the pulse figures came from a CAQ author's article.
- Web-search quota ran out before searches on the FRC 2026 audit-quality annual review and Big Four UK transparency reports.

**Under-documented in public sources:**
- AI use in acceptance and continuance decisions and in independence monitoring beyond vendor descriptions.
- AI use by valuation, actuarial, forensic and tax specialists in audits.
- Going-concern assessment, subsequent events, engagement quality review, key audit matters and report drafting with AI.
- Sustainability assurance providers' use of AI.
- Measured, independent accuracy or quality results for any audit AI tool in live use; inspection findings specific to AI tools (none found for 2025–2026).
- Smaller practices beyond the CPA.com benchmark (54 firms) and a few playbooks; non-Big-Four audit-AI launches (a search for BDO, Forvis Mazars, Baker Tilly and Crowe returned nothing audit-specific; BDO's ITGC paper is the exception).

**Data conflicts to resolve in deep dives:**
- EY "all phases now" versus "end-to-end by 2028"; PwC 2026 versus later global platform.
- CPA.com report: about one-quarter versus about one-third using no AI.
- Whether the PCAOB QC 1000 amendments still await SEC approval (secondary sources differ).
- Date and edition numbering of some conferences (ICAEW, IIA International, WCARS).

---

## 15. Source count by type

Counted as distinct sources with a key in sections 2–9. Sources listed under several headings are counted once, under the type in the first column. "Opened" means status `read` or `read-secondary` (including partial reads); the remainder are `snippet` or `blocked`.

COUNT_TABLE_PLACEHOLDER
