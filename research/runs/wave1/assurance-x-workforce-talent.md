# Assurance x workforce-talent: cross-cutting topic note

- **Archetype:** assurance (external audit and other assurance; overlapping in-house internal audit)
- **Topic:** workforce-talent. Staffing and the CPA pipeline (including licensure-path changes), graduate intake at large firms, offshoring and delivery centres, the pyramid/leverage model and the apprenticeship problem under AI, new roles, skills and training, retention and burnout, and internal audit talent.
- **Prepared:** 2026-10-16. Landscape read first: `research/runs/wave1/landscape-assurance.md`.
- **Method:** pages fetched with `curl` (PDFs with `pdftotext`; two sites via a text mirror or a public job-board API). 47 distinct sources opened across 8 types (press 25, survey 6, professional body 5, regulator 4, vendor 3, academic 2, job posting 2, government data 1; section 5). About half of the press items relay a primary report that was not itself opened. Landscape sources not reopened here are named as such.

**Evidence labels used throughout.**
- **[M]** observed or counted by a named party (regulator, statistician, researcher, professional body).
- **[S]** self-reported by a firm, vendor or survey sponsor; the sponsor has an interest.
- **[F]** forecast, plan or intention, with who made it.
- **[O]** commentary or opinion.
- A reference looks like `[REF, locator]`. Refs reuse the landscape's keys where one exists.

---

## 1. Summary

- **Large-firm graduate intake has fallen, but the measured numbers are a cut of roughly a sixth in the UK, not a collapse, and 2026 looks flat.**
  - [M, press-relayed] The UK Big Four's combined graduate-and-apprentice intake went from 6,500 (2023) to 5,400 (2025) (OMANOBS-GT-2026).
  - [S, leaked slide] PwC US's plan is a 32% cut in junior associate hiring by FY2028, which PwC did not confirm (ENTREPRENEUR-PWC-2025).
  - [S] EY and Deloitte UK say 2026 entry hiring is broadly flat, while Grant Thornton UK, Azets and Cooper Parry (all private-equity backed) are growing intake (OMANOBS-GT-2026).
- **The attribution to AI is mixed.**
  - PwC UK's chief tied its cut to AI and a weak economy (FORTUNE-PWCUK-2025).
  - PwC US cited "technological change" and low attrition (ENTREPRENEUR-PWC-2025).
  - Economy-wide payroll data show hiring of 22-25 year-olds in AI-exposed jobs, which include accountants, running 19% below peers. The authors call this descriptive, not causal, and not audit-specific (STANFORD-CANARIES-2026).
- **Pipeline supply is recovering while the licensure route is being rewritten.**
  - [M] US accounting undergraduate enrolment rose for a third straight year (+5.7% in spring 2026), and 2025 first-time CPA candidates were the highest since 2018 outside the 2023 pre-exam-change spike (JOFA-ENROLL-2026).
  - [M] By 29 Jun 2026, 39 US jurisdictions had signed alternative-pathway laws (bachelor's degree plus two years' experience in the typical form) and 23 were in effect (AT-150HOUR-2026).
  - No source yet shows whether this raises the number of licensed CPAs.
- **Shortage claims and intake cuts coexist, and the shortage is described mainly at the experienced, qualified layer.**
  - [S, vendor] 73% of 500 surveyed firms say they turn away work for lack of staff (CONSULTANCY-ADVANCETRACK-2026).
  - [M, firm-supplied to the FRC] The UK regulator's 2026 review reports "sustained workload pressures and elevated attrition among experienced staff" (FRC-ARAQ-2026, p. 22).
  - [S, relayed] In 2026 Deloitte UK reportedly offered auditors voluntary redundancy because staff turnover was low (RESULTSENSE-DELOITTEUK-2026).
- **The extended-team (offshore) model is the staffing change regulators are watching most.** In July 2026 the FRC said some firms are moving away from the pyramid and that remote teams are "increasingly" asked to exercise professional judgement, including on complex matters. It will monitor this for a year (FRC-ARAQ-2026, pp. 27-28).
- **The apprenticeship problem is acknowledged by regulators and firms. Audit-specific measurement of it does not exist.**
  - PCAOB's acting chair said "new and different paths" for juniors will be needed (NYSSCPA-BOTIC-2025).
  - KPMG says it is "lifting the pyramid" (CTRLCOUNCIL-WSJ-2026).
  - PwC's AI assurance leader forecasts first-years working "like fourth years" in three years (YAHOO-KOSAR-2025).
  - The only controlled evidence found is a non-audit experiment, on software developers, where AI help lowered a comprehension score by 17% (ARXIV-SKILL-2026).
- **New roles show up in postings and firm programmes before they show up in headcount data.**
  - [M, FT analysis] About 7% of Big Four job postings in 2025 required AI expertise (under 2% in 2022); audit roles were just under 3% (COMPUTERWORLD-FT-2026).
  - EY reports $448m on training and 5.2m hours of AI learning in FY26 (CPAPA-EY-2026).
  - AI-native entrants advertise "AI-native auditor" and "audit transformation" roles (MODUS-JOBS-2026; FIELDGUIDE-JOBS-2026).
  - No Big Four posting for an "agent evaluator" role was found (section 6).
- **Internal audit is resourced flat and is leaning on co-sourcing for AI skills.**
  - [S] 57% of 213 leaders held full-time headcount flat; 43% had unchanged budgets and 18% had cuts (OPTRO-FOF-2026).
  - [S] Only 28% are confident in auditing AI risks (OPTRO-FOF-2026).
  - [S] In a 47-leader Nordic survey, 57% rely on external consultants or other departments for AI initiatives (KPMG-NORDIC-2026).
- **Forecasts in circulation come from interested parties and are unproven.**
  - KPMG's audit digital chief expects "next to no human beings" in routine testing within two to three years.
  - Unnamed Big Four leaders estimate agents will do 20-30% of a typical audit by 2029 (CTRLCOUNCIL-WSJ-2026).
  - BLS projects 5% growth in accountant and auditor employment for 2025-35 (BLS-OOH-2026).

---

## 2. Findings

### 2.1 CPA pipeline and licensure path

**Degree supply, exam volume and firm hiring intent (US).**
- [M] Schools awarded 55,152 accounting bachelor's and master's degrees in 2023-24, down 6.6%. Master's degrees fell about 15% to 14,335 and bachelor's fell 3.3% to 40,817 (AICPA-TRENDS-2025, release body).
- [M] The rate of decline eased from 9.6% (2022-23) and 7.4% (2021-22) (AICPA-TRENDS-2025, release body; JOFA-PIPELINE-2025, paras 4-5).
- [M] New CPA Exam candidates were 42,626 in 2023 (the highest since 2016, a pre-exam-change surge) and 28,082 in 2024. In the first half of 2025 there were 16,448 new candidates (AICPA-TRENDS-2025, release body).
- [M] Participating firms reported 11,985 new graduate hires in 2024, 75% of them accounting majors. 75% of hiring firms expected to hire the same number or more in 2025 and 18% expected fewer (AICPA-TRENDS-2025, release body).
- The AICPA says low firm response in the last two editions prevents a reliable estimate of total graduate hires across all firms (JOFA-PIPELINE-2025, caveat paragraph).
- [M] Spring 2026 enrolment: four-year accounting programmes were up 8.9% to 205,180 (following +12.7% in 2025 and +4.8% in 2024). All undergraduate accounting enrolment was 281,992, up 5.7% against 1.3% across all majors (JOFA-ENROLL-2026, paras 2-5; AICPA-ENROLL-2026).
- [M] Two-year programmes fell 3.2% (JOFA-ENROLL-2026).
- [M] The AICPA says 2025 saw the highest first-time CPA Exam candidates since 2018 (excluding 2023) and the highest number passing all four sections since 2017 (JOFA-ENROLL-2026, para 3).
- The same AICPA sources note rising entry-level pay and licensure-barrier reductions as drivers (JOFA-PIPELINE-2025, Taylor quotation; JOFA-ENROLL-2026, Coffey quotation).
- [F, BLS] Employment of accountants and auditors is projected to grow 5% from 2025 to 2035 with about 115,300 openings a year, mostly replacement. BLS says technology will raise efficiency but "is not expected to reduce overall demand" (BLS-OOH-2026, Job Outlook and Employment Projections).

**Licensure-path change (US).**
- The AICPA and NASBA amended the model legislation in 2025 to allow new pathways. The new route lets candidates qualify without additional coursework beyond a bachelor's degree, with two years of work experience plus the exam (CFOBREW-150-2026, paras 1-3).
- Kansas, Kentucky and Maryland passed such laws in April 2026 (CFOBREW-150-2026, para 2).
- Most states keep the older routes, such as a master's degree or 30 extra credit hours plus one year of experience (CFOBREW-150-2026).
- Counts depend on the date and definition.
  - [M] On 7 May 2026, 38 states had passed legislation or board rule changes since 2025, per the Minnesota Society of CPAs tracker as cited by CFO Brew (CFOBREW-150-2026, para 2).
  - [M] On 29 Jun 2026, Accounting Today reported that 49 jurisdictions had submitted bills, 39 had signed changes into law and 23 were in effect (AT-150HOUR-2026, lede).
- Ohio was first (signed 8 Jan 2025, effective 9 Apr 2025). Colorado's three pathways take effect 1 Jan 2027. North Dakota and Wyoming plan to draft legislation in 2027, and Maine will file a bill in December for a 2027 hearing (AT-150HOUR-2026, state entries).
- The stated aim is to replace the "costly, time-consuming fifth year" with work experience. The AICPA's state legislative director called it "a tremendous success for the profession in terms of creating access for candidates" (AT-150HOUR-2026, lede and Cox quotation).
- No source opened reports a change in licences issued attributable to the new pathways. The statement of success is about access and legislation, not licence counts.

**UK and Ireland.**
- [M] The FRC's 2025 edition (data for 2024) reported UK and ROI accountancy student numbers down 0.3% to under 155,000. Around 1,800 members were awarded the Audit Qualification in 2024 against 1,900 in 2023 (FRC-KFAT-2025, paras 12-15).
- [M] Registered statutory audit firms fell to 3,760 in 2024 from 5,007 in 2020 (FRC-KFAT-2025, para 18).
- [M] The 2026 edition (24th, data for 2025) reports UK and ROI students up 0.9% (154,905 to 156,367) and registered audit businesses down 9% to 3,421 (THEACCOUNTANT-KFAT-2026).
- The FRC's July 2026 review names "Audit Qualification 2030 and Beyond" as an initiative on resourcing (FRC-ARAQ-2026, p. 28).

**Vendor-voiced claim, no source given.** A Thomson Reuters executive said 75% of audit partners are scheduled to retire within ten years and entry-level interest has declined (TR-STATE-2026, Wells interview). [S/F: vendor; treat as unverified.]

### 2.2 Large-firm intake, headcount and revenue (measured vs claimed)

**UK graduate and entry-level intake.**
- [M, press-relayed] Deloitte, EY, KPMG and PwC cut 1,100 UK entry-level roles over two years. Combined graduate-and-apprentice intake fell from 6,500 (2023) to 5,400 (2025), "as previously reported" (OMANOBS-GT-2026, paragraph 3).
- Firm figures differ by what is counted, and both come from press accounts of earlier reporting.
  - Graduates, school leavers and apprentices (reported Feb 2025): Deloitte 2,150 (617 or about 22% fewer), EY 1,600 (about 11% lower), PwC 1,450 (about 9% lower), and KPMG about 33% fewer (SFN-LEANER-2025).
  - Graduate scheme (reported Jun 2025, citing the Telegraph): KPMG 1,399 (2023) to 942 (29% cut) with about 1,000 expected in 2025; Deloitte 1,700 to 1,400 (18% cut) (SFN-TELEGRAPH-2025).
- PwC UK's head said it was hiring 200 fewer entry-level people (1,300 against 1,500). He wrote that numbers were lower "reflecting the wider slowdown in investment, hiring and deal-making" and that AI is reshaping roles (FORTUNE-PWCUK-2025, paras 1-4).
- [S] For 2026, EY and Deloitte said UK entry-level hiring would be broadly in line with last year, at around 1,600 and 1,500. PwC and KPMG declined to comment (OMANOBS-GT-2026, paragraph 3).
- [S] Grant Thornton UK plans 340 graduates and school leavers in 2026, up 30%. Azets took 384 in 2025 (up 15%) and Cooper Parry 140+ trainees (up 40%); both are private-equity owned (OMANOBS-GT-2026, final paragraphs).
- [S] Grant Thornton UK's chief executive said the firm is increasing graduate hiring and that AI "creates a massive opportunity" (IRISHTIMES-GT-2026, final paragraphs).
- [S] Grant Thornton UK's chief public officer said the firm is redesigning its three-year graduate programme for AI and changing client expectations (OMANOBS-GT-2026, Fisher paragraph, paraphrased by the reporter).
- [S] Deloitte UK said it took on 3,500 new staff in the year to 31 May 2026 after a voluntary redundancy offer to auditors prompted by low staff turnover, which about 200 reportedly took (RESULTSENSE-DELOITTEUK-2026, paras 3-4).

**US.**
- [S, leaked slide] PwC US's slide shows junior associate hiring goals falling from 3,242 (fiscal year ending June 2025) to a projected 2,197 in FY2028, a 32% decrease. PwC confirmed it is "decreasing" campus hiring citing technological change and low attrition, but did not confirm the numbers (ENTREPRENEUR-PWC-2025, paras 2-4).
- [F/O] A Bloomberg Tax commentary lists the headline "KPMG to Cut 10% of US Audit Partners" (23 Apr 2026) and describes graduate hiring as "switched off at the bottom". The commentary is opinion, and the partner-cut story itself was not opened (BGOV-ODOWD-2026, opening paragraphs and related stories).

**Global headcount and revenue.**
- [M] PwC's global headcount was 364,000 at FY25, down 5,600 from the prior year. The 2021 pledge to add 100,000 net jobs was absent from the report (CPAPA-PWC-2025, paras 5-7; CFOBREW-PWC-2025).
- [S] PwC's global chair said "we continue to hire" and that over 315,000 people had been upskilled in AI (CPAPA-PWC-2025).
- PwC's FY26 results were not out as of 9 Oct 2026 (CPAPA-EY-2026, para 5).
- [M, firm-reported] EY FY26 assurance revenue was $18.9bn, up 5.8% in US dollars (CPAPA-EY-2026, service-line paragraph).
- [M, firm-reported] Deloitte FY26 audit and assurance revenue grew 5% in local currency, and Deloitte UK's grew 3% (CPAPA-DELOITTE-2026, service-line paragraph; RESULTSENSE-DELOITTEUK-2026, para 2).
- These figures show assurance revenue growing while intake is flat or lower. None of the sources links the two causally.

**Job postings.**
- [M, FT analysis relayed] The Big Four advertised more AI-related postings than traditional auditing positions in 2025. Nearly 7% required AI expertise against under 2% in 2022, and audit roles were just under 3%. One firm noted that a single posting can cover multiple positions (COMPUTERWORLD-FT-2026, paras 1-3).

**Economy-wide evidence on early-career hiring (not audit-specific).**
- [M] ADP payroll data through June 2026 show employment of 22-25 year-olds in AI-exposed occupations 19% below where it would be at the pace of less-exposed peers. Experienced workers show no comparable gap (STANFORD-CANARIES-2026, abstract).
- [M] The authors say the gap widened since August 2025 and "operates primarily through reduced hiring" rather than separations (STANFORD-CANARIES-2026, abstract).
- The authors state three limits. The patterns attenuate when controlling for education, show some trends predating generative AI, and are "early, descriptive indicators", not causal estimates (STANFORD-CANARIES-2026, abstract).
- "Accountants" appear in the top AI-exposure quintile of ADP occupations. "Accountants and Auditors" appear among example most-exposed occupations on the automation-usage metric (STANFORD-CANARIES-2026, Tables A.6 and A.9). The paper reports no accountant-specific effect size.

### 2.3 Pyramid, leverage and offshoring (the extended-team model)

**What the UK regulator found.**
- [M] The FRC's Annual Review of Audit Quality 2026 says some firms are "moving away from the traditional pyramid staffing model". They are increasing use of offshore delivery platforms to bring remote teams into the onshore team, sometimes called the extended team model (FRC-ARAQ-2026, p. 27).
- [M] It says remote teams are "increasingly being asked to exercise professional judgement, including on complex audit matters", and that firms must keep adequate oversight (FRC-ARAQ-2026, p. 27).
- It cites rapid technological change, sustainability assurance, standards changes and cost pressure as drivers (FRC-ARAQ-2026, p. 27).
- It will monitor how the largest firms build and sustain "expanded resource models" for a year. It is laying groundwork for agreements with countries that support high education and training standards, and it will repeat its staff culture survey at the largest 12 firms (FRC-ARAQ-2026, p. 28).
- The review also flags offshore growth in a mid-tier firm's supervision plan. For Forvis Mazars the FRC will focus on consistent audit quality "especially as use of offshore teams increases" (FRC-ARAQ-2026, Appendix B, p. 69).
- The FRC states that private-equity effects on "fees and resourcing" remain uncertain and under monitoring (FRC-ARAQ-2026, private-equity risk table).
- The FRC lists a "recent spike in the demand for AI specialists across both audit and consultancy services" and says firms need auditors who are sceptical, curious and technically proficient across local and remote teams (FRC-ARAQ-2026, p. 28).

**Scale.**
- [S/M, press] The Financial Times, relayed by The Accountant, reported that KPMG UK's latest transparency report showed around a quarter of staff in its audit practice are based offshore. Two Big Four auditors told the FT they had concerns about some offshore work (TAO-OFFSHORE-2026, paras 5-7). The figure was not checked against the transparency report itself.
- The same coverage says the model was developed over more than a decade by the Big Four, notably in India, and that mid-tier firms have moved the same way as the UK market for qualified accountants tightened (TAO-OFFSHORE-2026, paras 4-5).
- [M] KPMG's US and UK entities paid $210m for a 33% stake in KPMG Global Services (India), a delivery arm serving 50 member firms across audit, tax, consulting and technology, and take control from the Indian partnership (VI-KGS-2025). The page is undated; a search extract placed it in April 2025.
- [O, anonymous, low authority] An unnamed KGS employee told a blog that some offshore teams are trained on "cookie-cutter and scripted testing" rather than professional judgement (TFS-OFFSHORE-2026). Treat as a lead only.
- No source opened gives audit-specific offshore headcount for Deloitte, EY or PwC (section 6).

**Leverage (staff per partner or responsible individual), UK audit practices.**
- [M, firm-supplied, FRC-published] Average audit staff managed by a partner or Responsible Individual, 2026 edition against 2024 edition: KPMG 19.2 against 22.6, Deloitte 15 against 16, EY 19 and 19, PwC 19 against 17 (FRC-METRICS-2026, section 6).
- Among others, BDO fell from 16.7 to 14.2 and Crowe from 15.1 to 13.0, while MHA rose from 9 to 15 (FRC-METRICS-2026, section 6).
- KPMG notes that offshore delivery centres and where IT auditors sit affect reported leverage, and PwC notes non-RI partners and directors also lead staff (FRC-METRICS-2026, section 6 narratives).
- The ratios do not show a uniform move away from the pyramid in UK audit practices. They are one metric, differently defined by firm, and they do not capture offshore teams.

**Leverage, pricing and the pyramid reshaping (claims and views).**
- [F, KPMG] KPMG's audit chief digital officer said "next to no human beings" will be in the routine-testing bubble in two to three years. A KPMG briefing listed routine testing as the only one of four audit areas with no human audit team within that time frame (CTRLCOUNCIL-WSJ-2026, opening paragraphs, reproducing WSJ 10 Apr 2026).
- [F, KPMG] The same officer said: "We're lifting the pyramid up", not slicing the bottom off (CTRLCOUNCIL-WSJ-2026).
- [F, unnamed] Some Big Four leaders estimate agents will contribute 20-30% of a typical financial audit by 2029 (CTRLCOUNCIL-WSJ-2026).
- [F/O] A vendor-sponsored article argues firms are shifting to a "diamond": a smaller entry layer, an expanded middle layer, and hiring that favours mid-career experts, AI specialists and data analysts (CPAPA-DIAMOND-2026, key takeaways). This is advocacy for a software vendor and not evidence.
- [O] The Bloomberg Tax commentary calls the result "K-shaped" and maps audit roles as partner "amplified", senior manager "divergent" and associate "substituted", borrowing a BCG labour classification (BGOV-ODOWD-2026, "K-shaped Remodeling").

### 2.4 The apprenticeship or learning-by-doing problem under AI

**What regulators say.**
- [M, statement] PCAOB acting chair Botic cited research that AI can erode critical thinking, judgement and skepticism. He said this will require "identification of new and different paths for junior auditors" to gain skills, from academia or employers (NYSSCPA-BOTIC-2025, closing paragraphs; 10 Dec 2025). The landscape records the same remarks (AICPA/PCAOB conference, 8-10 Dec 2025).
- [M] The FRC says firms have modified hiring to emphasise curiosity and the ability to challenge because of the risk of technology bias or over-reliance on automated outputs (FRC-ARAQ-2026, culture case study).
- The FRC says technology will change required skills and "impact firms' staffing structures, training models and recruitment" (FRC-ARAQ-2026, technology section, pp. 26-27).

**What firms say they are doing (all [S]).**
- PwC's AI assurance leader said new hires will do manager-level roles within three years because they will oversee AI doing routine tasks: "Three years from now, we will feel like the first years are functioning more like fourth years." PwC training is shifting to "back to basics" and brings critical thinking, negotiation and professional skepticism earlier (YAHOO-KOSAR-2025, paras 2-5; 8 Aug 2025). This is one executive's forecast about assurance staff.
- KPMG's Mackenzie said he will not hire a graduate "to create workpapers" but wants someone who understands a workpaper's findings with AI help. He said "audit know-how is still going to be gold" (CTRLCOUNCIL-WSJ-2026, final paragraphs).
- [S, relayed from City AM, Sep 2026] All four UK Big Four firms say they have overhauled or are overhauling graduate programmes. KPMG puts exams at the front and pairs trainees with experienced staff, and all four teach communication, resilience and teamwork directly (RESULTSENSE-GRADTRAIN-2026).
- [S] EY France's HR head said recruitment now assesses a candidate's ability to work with AI "ethically and responsibly" with a critical mind. KPMG and EY each recruit 1,000-1,200 graduates a year in France (LESSENTIEL-2026, paras 5-6).
- [S] RSM UK's audit data analytics director told a vendor conference that when AI flags a risk before a junior forms the thought, juniors "learn to confirm rather than to inquire". He argued that a reviewer lacking experienced scenarios is "a signature on a process" and that firms should match deterministic tools to early careers and probabilistic tools to experienced staff (DATASNIPPER-RSM-2026, sections 2-5). This is a practitioner talk on a vendor's site.
- [S, vendor survey] Thomson Reuters' action paper says firms must "define the role of early-career professionals" and secure structured development before automation erodes it (TRI-FOP-2026, universal priorities).

**What the evidence base is.**
- [M, non-audit] A randomised experiment (52 participants, 26 per arm) on developers learning an unfamiliar library found AI assistance lowered the evaluation score by 17% (Cohen's d 0.738, p = 0.010) with no significant speed gain. Participants who engaged cognitively kept their learning (ARXIV-SKILL-2026, abstract and introduction). It is a preprint in a different occupation.
- [M, audit-adjacent] The landscape lists a randomised audit field experiment on LLMs and audit quality, seen only as a search extract (SSRN-LLMAQ-2026), and Peters (2022) on automation and skepticism. Neither was reopened here, and no audit-specific measure of judgement formation under AI was found.
- The KPMG leader acknowledges the mechanism critics raise. A Bloomberg Tax commentary quotes it as "exposure to hundreds of small misstatements before forming a view on a material one" (BGOV-ODOWD-2026, apprenticeship paragraph). That quote is the commentators' own line, not a KPMG statement.

### 2.5 New roles, skills and training

- [M, FT analysis] Nearly 7% of Big Four postings required AI expertise in 2025 (COMPUTERWORLD-FT-2026).
- [M, firm-reported] EY says it spent $448m on training and development in FY26, with professionals completing 5.2m hours of formal AI learning and more than 40,000 AI accreditations through EY Badges. Total formal learning was 26.6m hours against 24.6m in FY25. 203,000 staff held Microsoft Copilot licences at year-end (CPAPA-EY-2026, learning paragraphs).
- [S] PwC says it has upskilled over 315,000 people in AI and is investing nearly $1.5bn in AI capabilities (CPAPA-PWC-2025).
- Landscape items, not reopened: Deloitte's Omnia "tutor mode" for micro-training (DELOITTE-OMNIA-2026) and EY Canvas's global training programme (EY-CANVAS-2026).
- [S] AI-native entrants use different job design.
  - Modus (a venture-backed firm-investment platform) posted an "AI-Native Auditor" role on 14 Jun 2026 for early-career auditors (about 0-4 years, CPA candidate or on track) to "complete audit workpapers end-to-end" with its AI platform (MODUS-JOBS-2026, posting dated 2026-06-14).
  - Modus's audit manager posting still asks the manager to "supervise, mentor, and develop staff at all levels" (MODUS-JOBS-2026, posting dated 2026-04-06).
  - Fieldguide's open roles include Audit Methodology Lead (18 Aug 2026), Director, Audit Transformation (2 Oct 2026, to lead the shift to an "agentic operating model"), Lead/Principal Product Manager, Audit Agents, and Software Engineer, Agents (Internal Audit) (FIELDGUIDE-JOBS-2026, Ashby board, 51 postings on 16 Oct 2026).
  - Fieldguide's posting claims 50%+ of the top-100 CPA firms as customers and up to 75% time saved (vendor figures) (FIELDGUIDE-JOBS-2026, Director posting).
- [S, vendor survey] Among tax and audit professionals, 81% use AI regularly. More than a quarter say they would not accept a job at a firm without professional-grade AI, and almost one in three would consider leaving if AI expectations are not met within two years (TRI-FOP-2026, key takeaways).
- [S] A Gartner survey of 119 CAEs (Aug 2025) reports low confidence in AI goals, with "poor data quality, lack of technical development skills" cited as limits (GARTNER-2026, via CIR coverage).
- [S, firm survey] A US small-firm benchmark (landscape, not reopened) lists "staff not trained" as the top blocker at 66% (CPACOM-ATR-2025).
- [M, firm-supplied to the FRC] FRC metrics show planned mandatory training hours per firm and grade. They are not split into AI training, and the firms define them differently (FRC-METRICS-2026, section 9 and narratives).

### 2.6 Retention, workload and burnout

**UK audit firms (FRC metrics, firm-supplied and unchanged by the FRC).** Periods differ by firm (for example Deloitte 1 May 2025-30 Apr 2026; EY 1 Jul 2024-27 Jun 2025; KPMG 1 Oct 2024-30 Sep 2025; PwC 1 Jul 2024-30 Jun 2025) (FRC-METRICS-2026, reporting periods).
- [M] Audit-practice attrition, latest period (2026 edition) for the Big Four (FRC-METRICS-2026, section 8):

| Grade group | Deloitte | EY | KPMG | PwC |
|---|---|---|---|---|
| Partners and directors | 6% | 4% | 6% | 9% |
| Managers and senior managers | 16% | 11% | 12% | 16% |
| Qualified, below manager | 32% | 19% | 33% | 39% |
| Unqualified | 14% | 11% | 12% | 14% |

- Notes: EY cannot split the two junior groups and reports "senior" and "staff". KPMG and PwC include staff who transferred to other practices. EY includes retirements (FRC-METRICS-2026, section 8 narratives).
- [M] Busy-period hours worked as a percentage of contracted hours, unqualified staff (2026 edition): Deloitte 114%, EY 121%, KPMG 108%, PwC 114%. For managers and senior managers: Deloitte 116%, EY 124%, KPMG 115%, PwC 123% (FRC-METRICS-2026, section 7b).
- [S] PwC states its average total working week is 41.3 hours, and 44.3 hours in the January-March peak (FRC-METRICS-2026, section 7a narrative).
- [M] The FRC summarises the metrics as showing "sustained workload pressures and elevated attrition among experienced staff", alongside positive external inspection results and continued investment in training (FRC-ARAQ-2026, p. 22).
- [M] The FRC also published, for 2026, 12 firms' people-survey results (FRC-METRICS-2026, section 1). They were not analysed here.

**Shortage, burnout and leaving (surveys by interested parties).**
- [S, outsourcing vendor, n about 500] 73% of firms say they turn away potential clients for lack of staff, and 73% rate the shortage's impact as severe. 45% say it is worse than three years ago. 74% believe sustained workloads "could push people out of the profession", and over a quarter had personally considered leaving (CONSULTANCY-ADVANCETRACK-2026, paras 2-5, 9). The sponsor sells outsourced accounting staff.
- [S, n over 350 corporate finance executives, North America] 61% report minor (46%) or significant (15%) shortages of accounting, finance and CPA talent, against 46% in 2025 (35% minor and 11% significant). 57% expect flat staffing and 38% plan to increase. Internal audit is the hardest role to fill for 13% of respondents, against 44% for controllers (CC-TALENT-2026, pp. 6-7). This covers corporate teams, not audit firms.
- [S] Optro's survey lists "workforce transformation and talent risks" as an emerging internal audit risk for 41% of leaders (OPTRO-FOF-2026, emerging-risk list).
- Analyst reading: firms that cite low attrition as a reason to hire fewer juniors (ENTREPRENEUR-PWC-2025; RESULTSENSE-DELOITTEUK-2026) and a regulator that reports elevated attrition among experienced staff (FRC-ARAQ-2026, p. 22) are describing different grades, so shortage language and entry-level cuts are not necessarily in conflict. No source reconciles them.

### 2.7 Mid-tier, private-equity-backed and AI-native firms

- [S] Private-equity-backed UK firms are growing entry intake (Grant Thornton UK, Azets, Cooper Parry) while directors and aspiring partners are reported leaving the Big Four for rivals (OMANOBS-GT-2026, final paragraphs).
- [S] Grant Thornton UK plans to add 160 managing directors to a 280-strong partnership in two years and says new partners get equity (OMANOBS-GT-2026).
- [M] The FRC says private equity may raise investment in technology and may affect fees, resourcing, leverage and culture; the effects are "uncertain" (FRC-ARAQ-2026, technology section and private-equity risk table).
- AI-native firms and funded platforms are hiring their own teams (section 2.5).
- Independence and alternative practice structures are covered in the landscape and the acceptance-independence module; they are not reanalysed here.

### 2.8 Internal audit talent

- [S] An Optro/Panterra survey of 213 internal audit leaders (North America and Europe, fielded 2025) found 43% of functions had no budget change in 2025 and 18% had reductions. 57% held full-time headcount flat despite expanding mandates (OPTRO-FOF-2026, resource section; CPAPA-OPTRO-2025).
- [S] Only 39% of leaders say AI will significantly transform the profession within five years, and only 28% are confident their teams can audit AI risks (OPTRO-FOF-2026, executive summary).
- [S] The skills leaders say technology cannot replace: professional skepticism and inquisitiveness (65%), relationship-building and communication (60%), ethical judgement (45%), critical thinking (41%) (OPTRO-FOF-2026, human-skills section). Optro sells audit software.
- [S] A Gartner survey of 119 CAEs (Aug 2025) found 83% of audit functions piloting or using AI and 12% planning to within the year. Leaders aim to expand coverage "amid resource constraints" (GARTNER-2026, via CIR coverage).
- [S] KPMG's first Nordic internal audit survey (June 2026, 47 leaders in five countries) found about 75% using or planning AI tools. Data access or quality is the top AI barrier (60%), ahead of lack of in-house expertise (38%). When expertise is missing, functions mainly co-source (KPMG-NORDIC-2026, executive summary and findings 3-4).
- [S] The same survey says 57% of organisations rely on external consultants or other departments for AI-related initiatives, and that "data literacy, AI understanding, and technology risk knowledge" are becoming core competencies (KPMG-NORDIC-2026, skills section). KPMG sells co-sourcing.
- [S] The Controllers Council study finds internal audit is a hard-to-fill role for 13% of corporate finance leaders (CC-TALENT-2026, p. 6).
- [M, statement] The IIA's comment letter to the PCAOB (landscape) asks for consistent treatment of AI-assisted work across external and internal auditors (IIA-PCAOB-2026, landscape, not reopened).
- No source opened describes a named internal audit function restructuring its team around AI or reducing headcount because of it. The reported pattern is flat headcount, automation of routine tasks and co-sourcing.

### 2.9 Measured data versus forecasts, side by side

| Claim | Type | Who | Source |
|---|---|---|---|
| UK Big Four graduate-and-apprentice intake 6,500 (2023) to 5,400 (2025) | M, press-relayed | Reported by FT/Telegraph lineage | OMANOBS-GT-2026 |
| PwC US junior associate hiring 3,242 to 2,197 by FY2028 | F, leaked slide | PwC (unconfirmed) | ENTREPRENEUR-PWC-2025 |
| Early-career employment 19% below in AI-exposed jobs | M, descriptive | Stanford/ADP authors | STANFORD-CANARIES-2026 |
| 23 US jurisdictions have alternative CPA pathways in effect | M | Accounting Today, 29 Jun 2026 | AT-150HOUR-2026 |
| Elevated attrition among experienced staff at UK audit firms | M, firm-supplied | FRC summary of firm metrics | FRC-ARAQ-2026, p. 22 |
| Routine testing with "next to no human beings" in two to three years | F | KPMG audit digital chief | CTRLCOUNCIL-WSJ-2026 |
| Agents do 20-30% of a typical audit by 2029 | F | Unnamed Big Four leaders | CTRLCOUNCIL-WSJ-2026 |
| First-years function like fourth years in three years | F | PwC AI assurance leader | YAHOO-KOSAR-2025 |
| Accountant and auditor employment +5% (2025-35) | F | BLS | BLS-OOH-2026 |
| 75% of audit partners to retire within ten years | S/F, unsourced | Vendor executive | TR-STATE-2026 |

---

## 3. What it means for an AI transformation conversation

### 3.1 Implications

1. **Frame talent as the operating-model question, not a headcount number.**
   - The evidence shows the entry layer shrinking or flat, offshore teams taking judgement work, and shortages at experienced levels (sections 2.2, 2.3, 2.6).
   - A leader who talks only about hours saved is missing the part regulators are already supervising.
2. **Process redesign changes who learns what.**
   - The routine testing that AI agents are being given is the work juniors learned on (CTRLCOUNCIL-WSJ-2026; DATASNIPPER-RSM-2026).
   - Any redesign proposal should say where the learning moves: structured review, scenario training, rotations, pairing.
3. **Review is now the scarce skill.**
   - The FRC puts weight on reviewers' competence and on human oversight at control points (landscape: FRC-GENAI-2026 certification and oversight sections).
   - The only controlled learning evidence points the same way: delegation costs skill, engagement preserves it (ARXIV-SKILL-2026).
   - Ask how reviewers are trained and how automation bias is monitored.
4. **Offshore and AI are two levers on the same pyramid.**
   - The FRC treats the extended-team model as a resourcing change needing quality-management adaptation (FRC-ARAQ-2026, p. 27).
   - A firm choosing between more AI and more offshore capacity should be asked how each affects supervision and accountability.
5. **The CPA licensure change is an input, not an outcome.**
   - It lowers cost and time to licence (AT-150HOUR-2026). It does not by itself change how many juniors firms hire.
   - A leader may be counting on it to fix a shortage that is described at the experienced layer.
6. **Internal audit is a capacity-constrained buyer.**
   - Flat headcount and low confidence in auditing AI mean the pitch is capacity plus capability, and co-sourcing is the current default (OPTRO-FOF-2026; KPMG-NORDIC-2026).
   - Data access and quality, not skills, is the first barrier named in the Nordic survey.
7. **Where there is no data, say so.**
   - Public evidence on audit-specific skill formation, on offshore quality, and on new-role headcount is thin (section 6).
   - A credible advisor separates the claims firms make from measurements and offers to help the client collect its own (review error rates, time-to-competence, attrition by cohort).

### 3.2 Interview probes

1. What did your entry-level intake do over the last three years, and how much of that change did you attribute to AI, offshore capacity, low attrition or the economy? (Press accounts split on cause: FORTUNE-PWCUK-2025; ENTREPRENEUR-PWC-2025.)
2. Which routine procedures have moved to agents or offshore teams, and what did a first- or second-year auditor do on that procedure before? Where does that learning now happen?
3. How do you train and test reviewers of AI-produced workpapers? Have you measured what they catch? (FRC emphasises reviewer competence; the landscape found no public override data.)
4. Where do offshore or remote team members exercise judgement today, and who is accountable for it? Are your supervision arrangements ready for the FRC's year of monitoring? (FRC-ARAQ-2026, pp. 27-28.)
5. How has attrition changed by grade, and are the people leaving the ones you most need? (FRC metrics show the biggest rates at qualified-below-manager grade: FRC-METRICS-2026.)
6. What new roles have you created (data, AI, agent design or evaluation, methodology-to-tool translators), who fills them, and how do they get audit judgement? (Only vendor and AI-native postings found: MODUS-JOBS-2026; FIELDGUIDE-JOBS-2026.)
7. What does your hiring screen now test for (curiosity, working with AI, scepticism)? What changed in the last year? (FRC-ARAQ-2026 culture case study; LESSENTIEL-2026.)
8. For internal audit: how many FTEs do you have against last year's plan, which routine tasks have you automated, and what do you co-source? (OPTRO-FOF-2026; KPMG-NORDIC-2026.)
9. What would you do differently if you assumed the entry layer would be half its current size in 2029? (Tests the pyramid-versus-diamond assumption; the 2029 estimate is an unnamed leaders' forecast: CTRLCOUNCIL-WSJ-2026.)

### 3.3 Objections and evidence-based responses

| Objection | Response from the evidence |
|---|---|
| "AI is not cutting graduate hiring; the economy is." | Both appear in the sources. PwC UK's chief cites the slowdown first and AI second (FORTUNE-PWCUK-2025). PwC US cites "technological change" and low attrition (ENTREPRENEUR-PWC-2025). Economy-wide payroll data show an early-career gap in AI-exposed jobs but call it descriptive (STANFORD-CANARIES-2026). EY and Deloitte UK say 2026 is flat and some firms are growing intake (OMANOBS-GT-2026). The honest answer is that attribution is unproven. |
| "We have a talent shortage, so AI cannot be a problem for talent." | The shortage and the cuts sit at different grades. Shortage claims are at experienced levels or from vendors selling staff (CONSULTANCY-ADVANCETRACK-2026), and the FRC reports elevated attrition among experienced staff (FRC-ARAQ-2026, p. 22). Entry-level intake was cut at the same firms (OMANOBS-GT-2026). |
| "Juniors will learn by reviewing AI output." | The firms say so (YAHOO-KOSAR-2025; RESULTSENSE-GRADTRAIN-2026). The regulator says new paths are needed (NYSSCPA-BOTIC-2025). The one controlled experiment found delegation lowered learning and engagement preserved it (ARXIV-SKILL-2026), in software rather than audit. A practitioner argues a reviewer without experience is "a signature on a process" (DATASNIPPER-RSM-2026). Treat as an open risk to design for, not a settled answer. |
| "The shorter CPA route will fix the pipeline." | Enrolment and first-time candidates were already rising before most laws took effect (JOFA-ENROLL-2026). Only 23 jurisdictions were effective in June 2026 (AT-150HOUR-2026), and the AICPA describes success as access. No licence-count outcome has been published yet. |
| "Offshore is just back-office, and quality is controlled." | The FRC says remote teams are increasingly asked to exercise professional judgement on complex matters and it will monitor (FRC-ARAQ-2026, pp. 27-28). A quarter of KPMG UK's audit staff are reported offshore (TAO-OFFSHORE-2026, relaying the FT). |
| "Our people do not want AI." | A Thomson Reuters Institute survey (vendor-run) says 81% of tax and audit professionals use AI regularly and almost a third would consider leaving if AI expectations are unmet in two years (TRI-FOP-2026). The same summary says more than a third admit to using unauthorised AI tools, which it flags as a liability risk (TRI-FOP-2026, universal priorities). |
| "Internal audit can simply hire the skills." | Flat budgets and headcount (57% flat FTEs) and low confidence (28%) point to co-sourcing as the practical route (OPTRO-FOF-2026; KPMG-NORDIC-2026). Data access came first as a barrier in the Nordic survey, ahead of skills. |
| "The pyramid becomes a diamond." | One executive says "lifting the pyramid" (CTRLCOUNCIL-WSJ-2026). Vendor and commentary pieces use the diamond (CPAPA-DIAMOND-2026). The FRC says only that some firms are moving away from the pyramid (FRC-ARAQ-2026, p. 27). The only measured shape indicator found is the FRC's UK staff-per-partner ratio, which moved in different directions by firm (section 2.3). |

---

## 4. Frontier signals

| Date | Signal | Who or type | Ref |
|---|---|---|---|
| 21 Aug 2025 | PwC US slide shows junior associate hiring falling 32% by FY2028; PwC confirms campus hiring is decreasing. | Leaked slide; firm statement | ENTREPRENEUR-PWC-2025 |
| 28 Oct 2025 | PwC global headcount 364,000, down 5,600; 100,000 net-jobs pledge absent. | Firm annual review (reported) | CPAPA-PWC-2025 |
| 10 Dec 2025 | PCAOB acting chair says new paths will be needed for juniors to build skills. | Regulator remarks | NYSSCPA-BOTIC-2025 |
| Jan 2026 | Gartner: 83% of audit functions piloting or using AI, with skills and data limits. | Analyst survey | GARTNER-2026 |
| 10 Apr 2026 | KPMG plans a summer 2026 orchestration-agent pilot and full agent deployment on certain tests in 2027; routine testing with "next to no human beings". | Firm plan (WSJ reproduction) | CTRLCOUNCIL-WSJ-2026 |
| 23 Apr 2026 | Headline: KPMG to cut about 10% of US audit partners (story not opened). | Bloomberg headline in commentary | BGOV-ODOWD-2026 |
| 19 May 2026 | FT: AI roles are about 7% of Big Four postings vs audit roles just under 3%. | Press analysis | COMPUTERWORLD-FT-2026 |
| 14 Jun 2026 | Modus posts "AI-Native Auditor" for early-career staff to do workpapers end to end with an AI platform. | Job posting | MODUS-JOBS-2026 |
| 29 Jun 2026 | 39 jurisdictions signed alternative CPA pathways, 23 effective; remainder expected by end of 2027. | Trade press tracker | AT-150HOUR-2026 |
| 21-22 Jul 2026 | TR survey: a third would consider leaving if AI expectations unmet (21 Jul). FRC says remote teams increasingly exercise judgement and it will monitor for a year (22 Jul). | Vendor survey; regulator | TRI-FOP-2026; FRC-ARAQ-2026; TAO-OFFSHORE-2026 |
| Aug 2026 | Stanford/ADP update: early-career gap in AI-exposed jobs widened to 19%. | Academic, descriptive | STANFORD-CANARIES-2026 |
| 2 Oct 2026 | Fieldguide advertises a Director, Audit Transformation to lead a shift to an "agentic operating model". | Job posting (vendor) | FIELDGUIDE-JOBS-2026 |
| 6 Oct 2026 | FRC KFAT 24th edition: UK and ROI student numbers +0.9%; registered audit businesses -9% to 3,421. | Regulator data via press | THEACCOUNTANT-KFAT-2026 |
| 9 Oct 2026 | EY reports $448m training spend and 5.2m AI-learning hours in FY26. | Firm results | CPAPA-EY-2026 |
| 1 Jan 2027 | Colorado's three CPA pathways take effect; North Dakota and Wyoming plan 2027 bills. | State law | AT-150HOUR-2026 |
| Next 12 months from Jul 2026 | FRC monitoring of the largest firms' extended-team models and a repeat culture survey at the largest 12 firms. | Regulator plan | FRC-ARAQ-2026, p. 28 |

---

## 5. Sources

All sources below were opened for this note unless marked. Types: regulator, professional-body, academic, government-data, press, survey, vendor, job-posting. Firm announcements were read through press coverage. Access: `full` = body text read; `partial` = a summary page or mirror; `mirror` = read through a text mirror.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| FRC-ARAQ-2026 | Annual Review of Audit Quality 2026 (PDF) | Financial Reporting Council | regulator | https://www.frc.org.uk/documents/9772/Annual_Review_of_Audit_Quality_2026_2eSTaw8P.pdf | Jul 2026 (22 Jul per press) | full (read resourcing, technology, culture, firm appendix) |
| FRC-ARAQ-REL-2026 | FRC Annual Review of Audit Quality equips investors and audit committees to make better decisions | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2026/07/frc-annual-review-of-audit-quality-equips-investors-and-audit-committees-to-make-better-decisions/ | Jul 2026 | full |
| FRC-METRICS-2026 | Audit Firm Metrics, July 2026 (PDF) | FRC | regulator | https://www.frc.org.uk/documents/9774/Firm_Metrics_July_2026_tA0lmUGa.pdf | Jul 2026 | full |
| FRC-KFAT-2025 | Key Facts and Trends in the Accountancy Profession 2025 (23rd edition) | FRC | regulator | https://www.frc.org.uk/library/supervision/professional-bodies-supervision/key-facts-and-trends-in-the-accountancy-profession/key-facts-and-trends-in-the-accountancy-profession-2025/ | Oct 2025 (15 Oct per search extract) | full |
| THEACCOUNTANT-KFAT-2026 | Report on the FRC Key Facts and Trends 24th edition | The Accountant (Verdict Media) | press | https://www.theaccountant-online.com/?p=30390 | 2026-10-06 | full |
| BLS-OOH-2026 | Occupational Outlook Handbook: Accountants and Auditors (2025-35 projections) | US Bureau of Labor Statistics | government-data | https://www.bls.gov/ooh/business-and-financial/accountants-and-auditors.htm | current edition (page undated) | mirror (bls.gov blocked curl; read via r.jina.ai) |
| AICPA-TRENDS-2025 | Accounting Firms Report Strong Hiring Outlook, AICPA Report Finds | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/accounting-firms-report-strong-hiring-outlook-aicpa-report-finds | 2025-10-27 | full |
| JOFA-PIPELINE-2025 | The accounting graduate pipeline: Where do things stand? | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2025/oct/the-accounting-graduate-pipeline-where-do-things-stand.html | 2025-10-27 | full |
| AICPA-ENROLL-2026 | U.S. Accounting Undergraduate Enrollment Continues to Outpace Growth Rate for Business Majors Overall | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/u-s-accounting-undergraduate-enrollment-continues-to-outpace-growth-rate-for-business-majors-overall | 2026-06-09 | full |
| JOFA-ENROLL-2026 | Student enrollment in accounting continues to rise | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/jun/student-enrollment-in-accounting-continues-to-rise/ | 2026-06-09 | full |
| AT-150HOUR-2026 | States overhaul 150-hour rule | Accounting Today | press | https://www.accountingtoday.com/list/states-overhaul-150-hour-rule | 2026-06-29 | full |
| CFOBREW-150-2026 | RIP, 150-hour rule | CFO Brew | press | https://www.cfobrew.com/stories/rip-150-hour-rule | 2026-05-07 | full |
| NYSSCPA-BOTIC-2025 | PCAOB's Botic Flags Opportunities and Risks in AI | NYSSCPA | professional-body | https://nysscpa.org/news/1051584-pcaobs-botic-flags-opportunities-and-risks-in-ai-2025-12-10 | 2025-12-10 | full |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (Aug 2026 version, PDF and abstract page) | Stanford Digital Economy Lab (Brynjolfsson, Chandar, Chen) | academic | https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine/ | Aug 2026 | full (abstract, Tables A.6 and A.9) |
| ARXIV-SKILL-2026 | How AI Impacts Skill Formation (arXiv 2601.20245) | arXiv (Shen, Tamkin) | academic | https://arxiv.org/abs/2601.20245 | Jan 2026 | full (abstract page and HTML v1) |
| CPAPA-PWC-2025 | PwC Reports Global Revenue of $56.9 Billion in 2025 | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/10/28/pwc-reports-global-revenue-of-56-9-billion-in-2025/171838/ | 2025-10-28 | full |
| CFOBREW-PWC-2025 | PwC cuts head count amid slowing revenue growth | CFO Brew | press | https://www.cfobrew.com/stories/2025/11/03/pwc-cuts-head-count-amid-slowing-revenue-growth | 2025-11-03 | full |
| CPAPA-EY-2026 | EY Global Revenue Grows to $57 Billion in FY 2026 | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/09/ey-global-revenue-grows-to-57-billion-in-fy-2026/191353/ | 2026-10-09 | full |
| CPAPA-DELOITTE-2026 | Deloitte Sees 5.7% Increase in Global Revenue During FY 2026 | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=190714 | 2026-09-29 | full |
| RESULTSENSE-DELOITTEUK-2026 | Deloitte UK returns to growth as its new boss says AI can't replace people (relays City AM) | Resultsense | press | https://www.resultsense.com/news/2026-09-30-deloitte-uk-results-graves-ai/ | 2026-09-30 | full (secondary) |
| RESULTSENSE-GRADTRAIN-2026 | Big Four rebuild graduate training as AI takes first-year work (relays City AM) | Resultsense | press | https://www.resultsense.com/news/2026-09-23-big-four-graduate-training-ai/ | 2026-09-23 | full (secondary) |
| IRISHTIMES-GT-2026 | Grant Thornton's UK boss defends private equity ownership (FT syndication) | The Irish Times | press | https://www.irishtimes.com/business/2026/09/22/grant-thorntons-uk-boss-defends-private-equity-ownership/ | 2026-09-22 | full |
| OMANOBS-GT-2026 | Major accountancy firm plans 30% graduate hiring (FT-lineage wire syndication) | Oman Observer | press | https://www.omanobserver.om/article/1190636/opinion/business/major-accountancy-firm-plans-30-graduate-hiring | 2026-06-03 | full (secondary; original not opened) |
| YAHOO-KOSAR-2025 | PwC is training junior accountants to be like managers, because AI is going to be doing the entry-level work (Business Insider) | Yahoo Finance | press | https://finance.yahoo.com/news/pwc-training-junior-accountants-managers-170001522.html | 2025-08-08 | full |
| ENTREPRENEUR-PWC-2025 | A Big 4 Firm Is Cutting Back on Entry-Level Hiring, According to a Leaked Slideshow (Business Insider lineage) | Entrepreneur | press | https://www.entrepreneur.com/business-news/pwc-plans-to-reduce-entry-level-hiring-over-the-next-3-years/496198 | 2025-08-21 | full |
| FORTUNE-PWCUK-2025 | PwC's U.K. chief admits he's cutting entry-level jobs and watching to see how AI changes work | Fortune | press | https://fortune.com/2025/09/08/pwc-uk-chief-cutting-entry-level-junior-gen-z-jobs-ai-economic-headwinds-like-amazon-salesforce | 2025-09-08 | full |
| SFN-TELEGRAPH-2025 | Big Four slash graduate jobs as AI takes over entry-level tasks (relays Telegraph) | Scottish Financial News | press | https://www.scottishfinancialnews.com/articles/big-four-slash-graduate-jobs-as-ai-takes-over-entry-level-tasks | 2025-06-23 | full (secondary) |
| SFN-LEANER-2025 | Leaner times for Big Four as graduate hiring plummets | Scottish Financial News | press | https://www.scottishfinancialnews.com/articles/leaner-times-for-big-four-as-graduate-hiring-plummets | 2025-02-03 | full (secondary) |
| COMPUTERWORLD-FT-2026 | The Big Four accounting firms are now hiring more AI specialists than accountants (relays FT analysis) | Computerworld | press | https://www.computerworld.com/article/4173296/the-big-four-accounting-firms-are-now-hiring-more-ai-specialists-than-accountants.html | 2026-05-19 | full (secondary) |
| CTRLCOUNCIL-WSJ-2026 | Why Audit Firms Are Rewriting the Role of the Modern Accountant (reproduces WSJ, Mark Maurer, 10 Apr 2026) | Controllers Council | press | https://controllerscouncil.org/why-audit-firms-are-rewriting-the-role-of-the-modern-accountant/ | 2026-05-08 | full |
| BGOV-ODOWD-2026 | AI Is Taking Over Audit Functions. Accounting Needs to Get Ready (commentary) | Bloomberg Tax / Bloomberg Law | press | https://news.bloomberglaw.com/esg/ai-is-taking-over-audit-functions-accounting-needs-to-get-ready | 2026-04-28 | full (opinion) |
| TAO-OFFSHORE-2026 | UK regulator raises concerns over Big Four offshore audit teams (relays FT) | The Accountant (Verdict Media) | press | https://www.theaccountant-online.com/?p=28660 | 2026-07-23 | full (secondary) |
| TFS-OFFSHORE-2026 | Big 4 offshoring high-risk audit work... UK regulator upset | The Finance Story | press | https://thefinancestory.com/big-4-offshoring-audit-work-to-india-uk-regulator-upset | 2026-07-31 | full (low authority; anonymous source) |
| VI-KGS-2025 | Big Four captive divestiture: KPMG US, UK units buy 33% stake in India's KGS for $210-M | Venture Intelligence | press | https://news.ventureintelligence.com/ma/big-four-captive-divestiture%3A-kpmg-us%2C-uk-units-buy-33%25-stake-in-india%E2%80%99s-kgs-for-%24210-m | 2025 (page undated; April per search extract) | full |
| LESSENTIEL-2026 | Audit: le "deal" de carriere des Big Four a l'epreuve des nouvelles generations | L'Essentiel de l'Eco | press | https://lessentieldeleco.fr/7031-audit-deal-de-carriere-des-big-four-a-lepreuve-des-nouvelles-generations/ | 2026-05-18 | full |
| CONSULTANCY-ADVANCETRACK-2026 | Three-in-four accounting firms struggle to take on new work amid hiring challenges (Advancetrack 2026 Accounting Talent Index) | Consultancy.uk | survey | https://www.consultancy.uk/news/44502/three-in-four-accounting-firms-struggle-to-take-on-new-work-amid-hiring-challenges | 2026-06-16 | full (sponsor is an outsourcing vendor) |
| CC-TALENT-2026 | 2026 Corporate Finance and Accounting Talent Study | Controllers Council | survey | https://controllerscouncil.org/wp-content/uploads/2026/07/2026-Corporate-Finance-Accounting-Talent-Study-626.pdf | 2026-07 (per URL) | full |
| KPMG-NORDIC-2026 | 2026 Nordic Internal Audit Survey | KPMG | survey | https://assets.kpmg.com/content/dam/kpmgsites/se/pdf/2026/KPMG-2026-Nordic-Internal-Audit-Survey.pdf | 2026-06 | full |
| OPTRO-FOF-2026 | Focus on the Future 2026: new risks for internal audit in a hypervolatile decade (Panterra survey, n=213) | Optro (formerly AuditBoard) with Richard Chambers | survey | https://resources.optro.ai/rs/961-ZQV-184/images/AB-EB-focus-on-the-future-2026-new-risks-for-internal-audit-in-a-hypervolatile-decade.pdf | 2025-11 (coverage 19 Nov 2025) | full |
| CPAPA-OPTRO-2025 | Report Says Internal Audit Profession Requires 'Superhuman' Skills to Survive Era of Hypervolatility | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/11/19/report-says-internal-audit-profession-requires-superhuman-skills-to-survive-era-of-hypervolatility/173476/ | 2025-11-19 | full |
| GARTNER-2026 | Gartner CAE survey (119 CAEs, Aug 2025), as reported by CIR Magazine | CIR Magazine (Gartner release 27 Jan 2026 per landscape) | survey | https://cirmagazine.com/cir/c2026013002.php | 2026-01 | full (secondary; Gartner release not reopened) |
| TRI-FOP-2026 | What the "2026 Future of Professionals Report" says tax and audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey / vendor | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full (summary page; full report not opened) |
| TR-STATE-2026 | The state of AI in audit in 2026: Interview with experts | Thomson Reuters Tax and Accounting | vendor | https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/ | 2026-03-30 | full |
| DATASNIPPER-RSM-2026 | Audit's AI Strategy Is Missing a Talent Development Chapter (Connect '26 London session write-up) | DataSnipper | vendor | https://www.datasnipper.com/resources/audit-ai-strategy-talent-development-junior-auditors | 2026 (page undated) | full |
| CPAPA-DIAMOND-2026 | Diamonds May Be a Firm's Best Strategy: How AI Is Rewriting the Structure of Modern Practice | CPA Practice Advisor (vendor-authored) | press / vendor | https://www.cpapracticeadvisor.com/2026/08/05/diamonds-may-be-a-firms-best-strategy-how-ai-is-rewriting-the-structure-of-modern-practice/188060/ | 2026-08-05 | full |
| MODUS-JOBS-2026 | Modus job board (AI-Native Auditor, Audit Manager, others) | Modus via Ashby public API | job-posting | https://api.ashbyhq.com/posting-api/job-board/modus | postings 2026-04-06 to 2026-06-14 | full (12 postings) |
| FIELDGUIDE-JOBS-2026 | Fieldguide job board (51 postings on 16 Oct 2026) | Fieldguide via Ashby public API | job-posting | https://api.ashbyhq.com/posting-api/job-board/fieldguide | postings 2026-01 to 2026-10-14 | full (titles; three descriptions read) |

**Landscape sources referenced but not reopened in this run** (carried at their landscape status): DELOITTE-OMNIA-2026, EY-CANVAS-2026, CPACOM-ATR-2025, IIA-PCAOB-2026, FRC-GENAI-2026, SSRN-LLMAQ-2026, PETERS-2022.

---

## 6. Gaps

**Not found, or not publicly measured.**
- **Audit-specific, independent measures of learning and judgement under AI.** The only controlled evidence is in software development (ARXIV-SKILL-2026). The audit field experiment on LLMs and audit quality (SSRN-LLMAQ-2026) was not reachable.
- **Big Four graduate intake for audit specifically.** All figures are firm-wide or UK-wide for graduate, school-leaver and apprentice intake combined. The KPMG UK and Deloitte UK numbers differ between two press accounts because of different counting.
- **2026 intake for PwC and KPMG.** Both declined to comment (OMANOBS-GT-2026). PwC's FY26 global headcount was not published as of 9 Oct 2026, and KPMG's FY26 results are due in December.
- **Offshore audit headcount by firm and its trend.** The only figure is KPMG UK's "around a quarter" of audit staff, relayed from the FT and not checked against the transparency report. No India audit headcount for Deloitte, EY or PwC was found. A 2025 US PwC "AC integration" driver appears only in search extracts of the leaked slide, not on a page opened (ENTREPRENEUR-PWC-2025 does not contain it).
- **New roles.** No Big Four posting or organisation chart for "agent evaluation", "AI assurance engineer" or similar was opened. Big Four job boards were not queried. Only an FT posting count and two AI-native vendors' boards were read.
- **Grade-mix (pyramid shape) data over time.** Only the FRC's staff-per-partner ratio (UK, three years, firm-defined) was found; no grade-mix series or US equivalent.
- **Licensure outcomes.** No licence-count or first-time-licensure data attributable to the new pathways. Counts of states differ by source and date (38 on 7 May and 39 signed on 29 Jun 2026 are different measures).
- **Internal audit restructuring.** No named function reducing headcount or reorganising because of AI. IIA/IAF 2026 Pulse of Internal Audit figures were not reached (only the Optro landing page: OPTRO-PULSE-2026 gave no figures, and is not cited above). Protiviti's latest capability survey was not found (a 2023 edition exists and was not used).
- **Smaller firms.** The US small-firm picture rests on the landscape's 54-firm benchmark (CPACOM-ATR-2025). The FRC data cover UK PIE auditors only.
- **Offshore and graduate accounts in other jurisdictions** (US PCAOB, Canada, Australia) were not found beyond the FRC's report.

**Blocked or unusable.**
- Wolters Kluwer's 2026 internal audit survey page, Going Concern, Accountancy Today UK and Cayman Compass returned 403. `bls.gov` blocked curl and was read via a text mirror. The Telegraph, FT, WSJ and Business Insider originals were not opened; figures from them are secondary and say so.
- A Thomson Reuters figure that 49% of professionals expect entry-level roles to decrease within two to three years appeared in a search extract. The opened summary page has no such figure, so it is excluded.
- Two figures in search extracts were not verified and are excluded: a 44% fall in UK accountancy graduate job adverts (Indeed or Adzuna, depending on the article) and a High Fliers 2026 projection of 3.5% fewer graduates (the latter appears in OMANOBS-GT-2026 as reported, so it is included there only as relayed).
- A Bloomberg Tax analysis of BLS data showing a 17% fall in "audit professionals" from a 2019 peak is quoted by a vendor (DATASNIPPER-RSM-2026) and was not found or checked. It is not used above.

**Conflicts left open.**
- KPMG UK intake: about 33% fewer (SFN-LEANER-2025, graduates, school leavers and apprentices) versus a 29% scheme cut from 1,399 to 942 (SFN-TELEGRAPH-2025). Different bases, same underlying press lineage.
- Whether KPMG US and UK now fully own KGS: one blog says so, while the more direct report describes a 33% purchase that gives control to the overseas entities (VI-KGS-2025). The note follows the latter.
- Attrition and "low turnover": the FRC reports elevated attrition among experienced staff at UK audit firms, while PwC US and Deloitte UK cite low attrition or turnover as a reason for cutting entry hiring or offering redundancy. The sources are different geographies, grades and periods and were not reconciled.
- UK student numbers: the 2025 edition reported a small fall, the 2026 edition a rise (FRC-KFAT-2025; THEACCOUNTANT-KFAT-2026).
