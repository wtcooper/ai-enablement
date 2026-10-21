# Benefit plan audits (assurance, mid-market)

Sources checked 2026-10-21. Use cases live in `../use-cases/benefit-plans.yaml` (15 entries).
Ids are shortened here: `#05` means `assurance-benefit-plans-05`. Source keys in brackets resolve in the YAML or in §10.

**Read this first.** This is a low-evidence module. Public AI evidence for plan audits comes almost entirely from
software vendors and the firms in their case studies, and one platform (Autire) carries most of it. **No entry is
grade A**: every figure sits on a vendor page or in a vendor press release, and none says how it was measured. Seven
of 15 entries are grade B (named firms, no published measurement), six are C and two are ideas (D). Much of what is
sold as plan-audit "AI" is rules-based automation; the vendor with the most evidence says its full-population tests are
hard-coded logic, with AI used to group exceptions [AUTIRE-AI-2026]. This review found no statement on AI in plan
audits from a regulator, a peer review body or the AICPA's plan audit quality center. Use this module for **risk awareness,
interview probes and named examples**, not as proof that AI improves plan-audit quality.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Audits of employee benefit plans under ERISA (the US federal law governing private retirement and welfare plans),
mostly 401(k) and 403(b) defined contribution plans, done by regional, local, specialist and mid-market firms. The
report is filed with the plan's Form 5500 (the annual return a plan files with the Department of Labor), and the
Department of Labor's Employee Benefits Security Administration (DOL EBSA) and AICPA peer review both re-examine the
work [EBSA-AUDITQ-2023]. It covers what is different for this engagement type; general audit mechanics stay in the sibling modules
(full-population testing in substantive-testing, SOC report reading in controls-testing, AI governance in
quality-management).

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Acceptance and setup | Confirm the plan needs an audit (for defined contribution plans, generally 100 or more participants with account balances at the start of the plan year, after the shift away from counting eligible participants, with an 80-120 rule) [LEDGERLINE-SITE-2026; JOFA-AAFOCUS-2024] and its type (401(k), 403(b), ESOP, defined benefit, welfare, multiemployer, multiple-employer and pooled, governmental, church) [SIKICH-BROCHURE-2026]; contact the predecessor auditor [METZ-EBPAUDITAI-2026] | expert-judgment, coordination-scheduling | Initial audits (new auditor or newly audit-required plans) present quality challenges [JOFA-AAFOCUS-2024] |
| Planning and risk assessment | SAS 145 (the US risk-assessment standard) risk assessment, plan profile, understanding service providers and IT [JOFA-AAFOCUS-2024; CALCPA-EBP-2026] | expert-judgment, document-production | Practitioners grapple with applying SAS 145 to plans: controls, IT systems, related parties [JOFA-AAFOCUS-2024] |
| Document and data gathering | Plan document, amendments, adoption agreement, trust statements, payroll registers, census, recordkeeper files [AUTIRE-TRUSTREC-2026; LEDGERLINE-SITE-2026] | coordination-scheduling, data-reporting | Data in many formats, repeated requests, a busy season overlapping extension deadlines [SIKICH-BROCHURE-2026; AUDENZA-EBP-2026, vendor view] |
| Service-provider reliance | Read recordkeeper, TPA (third-party administrator) and payroll SOC 1 reports (independent reports on a service provider's controls) and the user entity controls they assume [AICPA-EBPAQC-TOOLS-2024] | review-assurance | Overreliance on service providers remained a deficiency theme in the 2023 DOL study [ICPAS-EBPQ-2024] |
| Investments and trust reconciliation | Trust report to trial balance to Form 5500; limited-scope (ERISA section 103(a)(3)(C)) versus full-scope audits [AICPA-ONPOINT-2020] | data-reporting, review-assurance | Each recordkeeper's PDF looks different; trial balances are built and tied out by hand [AUTIRE-TRUSTREC-2026] |
| Participant-data testing | Eligibility, deferrals and definition of compensation, match, vesting and forfeitures, loans, hardships, distributions, timely remittance [AICPA-EBP-2026] | transaction-processing, review-assurance | Participant data (15.6% of sampled audits) and contributions (15.3%) lead the deficient areas [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024] |
| Plan-document and compliance review | Operation against plan terms, SECURE 2.0 amendments, prohibited transactions [TR-KIMBERLIN-2026; AICPA-EBPAQC-TOOLS-2024] | expert-judgment, research-synthesis | Plan documents past 150 pages with several amendments; juniors ask seniors to confirm readings [TR-KIMBERLIN-2026] |
| Financial statements, disclosures, Form 5500 | Draft statements and notes under SAS 136 (the plan financial statement standard); tie the Form 5500 to audited balances [CASEWARE-DASEBP-2026; JOFA-AAFOCUS-2024] | document-production | Form 5500 errors "remain a frequent issue" (session abstract, not data) [CALCPA-EBP-2026] |
| Review, inspection and peer review readiness | Reviewer sign-off; DOL inspection; AICPA peer review, where ERISA audits are a must-select engagement type [EBSA-AUDITQ-2023; TSCPA-PEERREVIEW-2025] | review-assurance | The DOL said peer review and practice monitoring do not help identify deficient plan audits [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024] |

Defined benefit plans (actuarial work), health and welfare plans and multiemployer plans are separate audit types. No
AI evidence was found for any of them; the 2020 OnPoint EBP FAQ excluded them from that product [AICPA-ONPOINT-2020].

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or operating model changes). **Delegate has no
entry**: no source describes an agent owning a multi-step plan-audit outcome. Reinvent has one grade-C firm and two
cross-references. Several automate entries are workflow automation the sources do not call AI.

**Acceptance, business development and planning**
- Improve: `#13` AuditMiner Plan Research: Form 5500 search and analytics to scope engagements and find prospects
  (vendor, C). `#08` Autire generates a SAS 145 risk assessment from completed planning procedures; the auditor
  concludes (vendor, C).

**Data gathering and service-provider reliance**
- Improve: `#07` Kimberlin Company (specialist firm) prompts CoCounsel Audit to map SOC 1 controls to its testing
  areas; AuditMiner sells SOC toolkits (B). Idea `#14`: ask recordkeepers, TPAs and payroll providers whether AI sits
  in their service, using the AICPA's SOC AI Q&A (D).
- Automate: `#03` Sikich (mid-market firm in an alternative practice structure) uses payroll and recordkeeper platform
  relationships to cut manual requests; vendors offer direct pulls (B). `#10` request portals with reminders and
  status tracking at Sikich (Suralink) and Belfint (Autire) (B). `#05` Anders CPAs + Advisors turns recordkeeper and
  payroll reports into standard workpapers with AuditMiner, per the vendor's case study (B).

**Testing and reconciliation**
- Improve: `#02` Autire's Advanced AI groups flagged exceptions by root cause and shows whether an issue is isolated or
  systemic (vendor, announced, C). `#04` trust-statement PDFs extracted into a trial balance and tied to the Form 5500 (vendor, C).
- Automate: `#01` full-population testing of participant, payroll and contribution data at Belfint, Lyons & Shuman
  (regional) and Rea & Associates (Top 100), using Autire's rules-based tests (B; the module's anchor case).
- Idea `#15`: year-round plan-data monitoring shared between recordkeeper, TPA and auditor (D).

**Plan-document and compliance review**
- Improve: `#06` Kimberlin and Sensiba (Top 75) use CoCounsel Audit to read plan documents and amendments, check
  SECURE 2.0 adoption and answer trainees' routine questions, with page-and-section citations (B).

**File, reporting and quality**
- Improve: `#09` DAS EBP, a methodology-embedded plan-audit file that drafts statements from a plan profile, adopted by
  Citrin Cooperman (PE-backed), Withum, EisnerAmper and PKF O'Connor Davies (B; adoption only, no results). `#11`
  Autire's firm-level methodology configuration with vendor-included DOL inspection and peer review support (C).

**Reinvent (practice model)**
- `#12` Metz CPA (specialist plan-audit firm) markets a proprietary EBPAudit.ai platform with fixed three-year pricing
  and a service guarantee (C). Cross-references: `assurance-substantive-testing-25` (Ledgerline, a pre-launch
  specialist firm built on data pulls and whole-population testing) and `assurance-acceptance-independence-20`
  (AI-native start-up auditors; Oath lists employee benefit plans among its client types [OATH-2026]).

Covered in sibling modules, not repeated: firm AI governance and recording AI use on the file
(`assurance-quality-management-17`, `-23`); general third-party SOC report reading (`assurance-controls-testing-13`);
vendor due diligence scaled for smaller firms (`assurance-quality-management-06`).

## 4. Interview probes

Ask plan-audit partners, managers, quality leaders and the people who run the season.

1. **"How many plan audits does the firm do a year, and is that a specialist practice or a sideline?"** Reveals the
   quality baseline. Firms with one or two plan audits had 70% deficient audits against 17% at firms with 100 or more
   [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024].
2. **"Which steps still run on samples, and for what share of plans could you test every participant?"** Reveals
   readiness for `#01`. Follow with: who triages exceptions, and what false-positive rate do you see? Rea's managing
   director recalls one file opening with 8,000 flags, mostly one pay-code issue [AUTIRE-REA-2026].
3. **"How does participant, payroll and recordkeeper data reach you today: portal, email or a direct connection?"**
   Reveals where `#03` and `#10` apply, and who checks completeness and accuracy of data a tool pulls.
4. **"How do you rely on recordkeeper and TPA SOC 1 reports, and do you review the user entity controls?"** Reveals the
   reliance step's maturity (`#07`); overreliance on providers is a DOL deficiency theme [ICPAS-EBPQ-2024].
5. **"Do any of your plans' recordkeepers, TPAs or payroll providers say they use AI in the service?"** Reveals exposure
   to idea `#14`; most teams will not have asked.
6. **"Who reads the plan document, and how do juniors confirm a provision?"** Reveals the senior-time drain `#06`
   targets, and whether answers are checked against the cited page.
7. **"What does a peer reviewer or DOL inspector see when a tool did part of the work? Has one ever asked?"** Reveals
   documentation readiness. No public inspector view of tool-generated plan files exists (`#11`).
8. **"Where are your plan-audit deficiencies or review notes concentrated?"** Reveals whether AI is aimed at the right
   steps. The DOL's top deficient areas are participant data, contributions and benefit payments [EBSA-AUDITQ-2023].
9. **"If hours per audit fell by a third, what would happen to fees, staffing and TPA referrals?"** Reveals the
   business case and the capacity choice (grow the book, as Belfint did, or cut hours) [AUTIRE-BELFINT-2026].
10. **"How would you explain new findings on an existing client after a switch to full-population testing?"** Reveals
    readiness for the prior-year question Rea worried about [AUTIRE-REA-2026].
11. **"Which plan types do you audit beyond 401(k): defined benefit, health and welfare, ESOP, multiemployer?"**
    Reveals how much of the book sits where no AI evidence exists [AICPA-ONPOINT-2020].
12. **"Where does participant personal data go when a tool processes it?"** Reveals data-handling controls; vendors'
    security statements are their own [AUTIRE-SECURITY-2026].

## 5. Metrics and benchmarks

**No independent measure of AI in plan audits was found**: no error, override, miss or parallel-run rate, and no
inspection finding that mentions AI. The quality baseline comes from the DOL's November 2023 study; dol.gov returns
403, so it was read in full through the r.jina.ai mirror and the figures below were checked against it
[EBSA-AUDITQ-2023].

| Metric | Figure | What it measures | Provenance |
|---|---|---|---|
| Major GAAS deficiencies, 2020 filings (Nov 2023 study) | 30% | audits with one or more major deficiencies against relevant generally accepted auditing standards requirements; the study's text says 307 audits, its strata table totals 308 | regulator [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024; AAFCPA-DOLQ-2024] |
| Same, 2015 study (2011 filings) | 39% | same measure, 400 audits; the 30% and 39% are two studies, not a contradiction | [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024] |
| Trend | 23% (1989), 19% (1997), 33% (2004), 39% (2015), 30% (2023) | same measure across the five studies in the DOL's table | [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024] |
| By firm plan-audit volume, 2020 filings | 70.0% (1-2 plans), 51.2% (3-5), 50.1% (6-24), 38.0% (25-99), 17.0% (100+) | share of audits reviewed in each stratum with deficiencies (20, 23, 54, 74 and 137 audits reviewed) | [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024] |
| Deficiency areas | participant data 15.6%, contributions 15.3%, benefit payments 9.4%, internal controls 5.9%, planning and supervision 3.3% | share of the 307 sampled audits with a deficiency in that area (for example 48 of 307 for participant data) | [EBSA-AUDITQ-2023] |
| Market concentration | firms doing plan audits fell from 7,330 (2011 filings) to 4,300 (2020); audits rose from 81,162 to 86,863 | firms and audits in the study populations | [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024] |
| Quality-center membership | members had a significantly lower deficiency rate, yet nearly 80% (83 of 105) of deficient audits were by members | share of deficient audits performed by EBPAQC (AICPA Employee Benefit Plan Audit Quality Center) member firms; members did 90% (276 of 307) of the sampled audits | [EBSA-AUDITQ-2023; BELFINT-DOLQ-2024] |
| Peer review and deficient audits | 91% (96 of 105) | deficient audits whose firm had a "Pass" peer review report (the report covers three years, so not always the 2020 audit) | [EBSA-AUDITQ-2023] |
| Peer review, Tennessee 2025 | ERISA: 2 of 21 engagements nonconforming | one state, small sample; context, not a benchmark | [TSCPA-PEERREVIEW-2025] |
| Hours per audit, Belfint on Autire | 80 to 54; book grew from about 100 to 160-170 audits | preparer plus two reviewers, average; tracking method not stated | vendor-published [AUTIRE-BELFINT-2026] |
| Hours per audit, Rea on Autire | 40% fewer | since adoption, in the vendor's narration; baseline not given | vendor-published [AUTIRE-REA-2026] |
| Plan-document error check, Kimberlin | 60-90 minutes to about 15 | one auditor's estimate | vendor-published [TR-KIMBERLIN-2026] |
| Workpaper setup and SOC analysis, Anders | "hundreds of hours" saved | rough statement in the vendor's narration | vendor-published [AUDITMINER-ANDERS-2025] |
| Vendor-wide claims, Autire | 100+ to 30 hours per plan; 7,000+ audits; 120+ firms; zero findings attributed | not defined; unverified | vendor-published [AUTIRE-HOME-2026] |

The study says the deficient audits put $927 billion and 11.7 million plan participants and beneficiaries at risk
[EBSA-AUDITQ-2023; JRCPA-AUDITQ-2025]. The closest things to AI quality evidence are the 8,000 flags Rea's managing
director recalls in one file and Autire's June 2026 removal of the two largest categories of false failures in one test
[AUTIRE-REA-2026; AUTIRE-ADVAI-2026]. They show that whole-population tests throw false positives that need triage;
they do not measure misses.

**Suggested measures (no benchmark yet):** hours per plan by staff level; exceptions per plan and the share that are
false positives; review notes per file; peer review and DOL inspection findings on plan files; days from first
document to report.

## 6. Guardrails

**Standards and regulator**
- SAS 136 (plan financial statements, effective for periods ending on or after 15 Dec 2021) and SAS 145 (risk
  assessment) set the work [AICPA-ONPOINT-2020; JOFA-AAFOCUS-2024]. AICPA quality management standards took effect
  15 Dec 2025 [JOFA-AAFOCUS-2024].
- DOL EBSA's Office of the Chief Accountant studies plan audit quality. The 2023 study recommends that EBSA seek
  authority over registration, suspension and debarment of plan auditors, civil penalties for substandard audits and
  repeal of the limited-scope provision, and that it work with the AICPA to disclose peer review deficiencies and
  require an engagement review for plan-audit firms [EBSA-AUDITQ-2023]. Belfint, a plan-audit firm, disagrees on
  limited scope [BELFINT-DOLQ-2024].
- Peer review treats ERISA audits as a must-select engagement type [EBSA-AUDITQ-2023; TSCPA-PEERREVIEW-2025]. The EBPAQC's tool list
  answers the 2023 study: planning, timely remittance, plan document compliance, parties in interest, fraud, SOC 1
  reliance, limited-scope audits, specialists [AICPA-EBPAQC-TOOLS-2024].

**AI guidance (none plan-specific)**
- The AICPA's October 2026 practice aid covers a client's AI in reporting and a firm's own AI use (quality
  management, supervision, review, judgment, scepticism); the auditor remains responsible for the audit and the
  opinion. It is for financial statement audits generally [AICPA-PA-2026].
- TQA 9561 (11 Sep 2026) covers a service organisation's AI in SOC 1 and SOC 2 engagements, which bears on recordkeeper
  and TPA reliance (`#07`, `#14`) [AICPA-TQA9561-2026].
- A Forvis Mazars quality leader told an AICPA webcast in 2024 that AI tool use should be documented at firm and
  engagement level, including data completeness and accuracy testing [JOFA-AAFOCUS-2024]. A vendor expects tighter
  controls on AI-assisted and outsourced work and documentation of judgment against AI suggestions
  [AUDITMINER-PREDICT-2026]. The general mechanics are `assurance-quality-management-17` and `-23`.

**Data and reliance**
- Plan audits hold participant personal data. Autire states US-only hosting, SOC 2 Type 2 controls and matching
  without Social Security numbers; these are vendor statements [AUTIRE-SECURITY-2026].
- Time pressure can tempt auditors to rely too heavily on automated tools, and overreliance on service providers
  remained a deficiency theme [ICPAS-EBPQ-2024].
- Testing every record does not make the audit a guarantee; an incomplete population sits outside the transaction
  data [LEDGERLINE-CPAPA-2026].

**Steps that stay with a person:** deciding what each flagged exception means and which go to the client (`#01`,
`#02`) [AUTIRE-AI-2026; AUTIRE-ADVAI-2026]; deciding on reliance on a SOC 1 report (`#07`) [AUDITMINER-SOC-2026];
checking a cited plan provision before relying on it (`#06`) [TR-KIMBERLIN-2026]; overriding the configured
methodology (`#11`) [AUTIRE-COMPLIANCE-2026]; the audit and the opinion [AICPA-PA-2026]. No source describes the
review of a generated risk assessment (`#08`).

## 7. Roles and how they evolve

- **Reviewers and managers** spend more time working out what is wrong and giving clients things they can fix, says
  Belfint's audit manager; supervisors moved to the platform first [AUTIRE-BELFINT-2026].
- **Trainees and juniors** answer routine plan and rule questions with a citation-backed tool, which reduces reliance
  on senior staff, says the vendor's Kimberlin case study [TR-KIMBERLIN-2026]. Sensiba wants staff to apply judgment, not rely blindly on AI
  [TR-SENSIBA-2026].
- **Staff experience:** the vendor's Anders case study reports better job satisfaction and retention after automating
  setup work [AUDITMINER-ANDERS-2025]; Belfint says new staff ask to work on Autire files [AUTIRE-BELFINT-2026].
- **Capacity:** Belfint grew from about 100 to 160-170 plan audits [AUTIRE-BELFINT-2026]; Autire's site menu card
  for the case study says without adding headcount (vendor statement) [AUTIRE-BELFINT-2026]. Rea's managing director says freed time
  can go to sit-down client conversations [AUTIRE-REA-2026].
- **Specialist positioning:** Metz says clients work with an experienced plan auditor, not a junior rotation
  [METZ-EBPAUDITAI-2026]; Sikich says all levels of its plan-audit team are dedicated [SIKICH-BROCHURE-2026].
- **Vendors take on support roles:** Autire says its support team is entirely former plan auditors, including DOL
  inspection and peer review support [AUTIRE-COMPLIANCE-2026; AUTIRE-ABOUT-2026].
- **Outsourced and offshore support** is growing, with supervision a concern (vendor views) [AUDITMINER-PREDICT-2026;
  AUDENZA-EBP-2026].

## 8. Frontier

- **2024-10-14** CPAmerica, an association of independent CPA firms, adds Autire as a preferred provider [AUTIRE-CPAMERICA-2024].
- **2024-12-02** Autire announces automated risk assessment for 401(k) audits (`#08`) [AUTIRE-RISK-2024].
- **2025-02-12** Sikich webinar lists "the role of AI in employee benefit plan audits" [SIKICH-WEBINAR-2025].
- **2026-01-23** AuditMiner predicts AI will touch plan audits even where firms do not adopt it, because sponsors and
  providers already use it (vendor view) [AUDITMINER-PREDICT-2026].
- **2026-03-03** Private-equity investor Serent Capital invests in Autire; terms not disclosed [SERENT-AUTIRE-2026].
- **2026-05-04 to 06** AICPA Employee Benefit Plans Conference markets "AI integration"; its agenda page did not load
  for this review [AICPA-EBP-2026].
- **2026-06-04** CalCPA's plan-audit conference closes with "Incorporating AI into EBP Audits: Balancing Risk and
  Reward"; only the abstract is public [CALCPA-EBP-2026].
- **2026-06-11** Autire ships AI exception analysis (`#02`) [AUTIRE-ADVAI-2026].
- **2026-06-03 to 10-08** Withum, EisnerAmper, Citrin Cooperman and PKF O'Connor Davies announce DAS suite adoptions
  that include plan-audit modules (`#09`) [CASEWARE-WITHUM-2026; CASEWARE-EISNERAMPER-2026; CASEWARE-CITRIN-2026; CASEWARE-PKF-2026].
- **2026-08-06** Thomson Reuters publishes the Kimberlin plan-document case (`#06`) [TR-KIMBERLIN-2026].
- **2026-09-11 and 10-13** AICPA issues TQA 9561 and the AI practice aid [AICPA-TQA9561-2026; AICPA-PA-2026].
- **2026-10-15** Ledgerline's CEO writes on whole-population plan testing; the firm's site lists availability from
  1 Dec 2026 (`assurance-substantive-testing-25`) [LEDGERLINE-CPAPA-2026; LEDGERLINE-SITE-2026].
- **Direction:** from samples to whole-population tests, from request lists to data pulls, from reading documents to
  analysing exceptions. No regulator has endorsed or restricted any of it.

## 9. Common objections

- **"Testing everything means we can't miss anything."** Not so: reasonable assurance is not absolute, some risks sit
  outside the transaction data, and "we test everything" can widen the expectation gap [LEDGERLINE-CPAPA-2026].
- **"Full-population testing will bury us in exceptions."** It can at first: Rea's managing director recalls one file
  opening with 8,000 flags, mostly one pay-code issue [AUTIRE-REA-2026], and the vendor has had to remove false-failure categories
  [AUTIRE-ADVAI-2026]. Plan for triage time and a learning curve; Belfint saw benefits late in year one and into year
  two [AUTIRE-BELFINT-2026].
- **"New findings will make clients ask why we missed them before."** Rea's managing director raised exactly this worry
  [AUTIRE-REA-2026]. Prepare the client conversation before the first run.
- **"The savings are hype."** The named figures (80 to 54 hours; 40% fewer hours) sit in the vendor's narration of
  its case studies and have no stated method [AUTIRE-BELFINT-2026; AUTIRE-REA-2026]. Rea warns that 100 hours to 30 is not realistic
  overnight. Treat them as a range to test in a pilot, not a promise.
- **"AI is too unpredictable for plan testing, where accuracy is non-negotiable."** The leading vendor agrees and uses
  deterministic rules for the tests and uses AI to group exceptions [AUTIRE-AI-2026].
- **"Using the AICPA's tools and quality center keeps us safe."** Members do better, but nearly 80% of deficient audits
  were still by members [EBSA-AUDITQ-2023].
- **"We're too small for this."** Small plan practices are where quality is weakest (70% deficient at one or two plan
  audits) [EBSA-AUDITQ-2023]. Ask whether to invest, specialise or refer the work; Belfint gets referrals from
  five to ten local TPAs [AUTIRE-BELFINT-2026].
- **"Participant data can't go into a third-party tool."** Vendors publish hosting and data controls, but these are
  their own statements; do vendor due diligence (`assurance-quality-management-06`) [AUTIRE-SECURITY-2026].

## 10. Sources

Full details for entry sources are in the YAML. Keys cited here that are not in the YAML:
- EBSA-AUDITQ-2023 is also in the YAML (entries 01, 09, 11, 12): US Department of Labor, EBSA, *Audit Quality Study*,
  2023-11, read in full through the r.jina.ai mirror because dol.gov returned 403,
  https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/publications/november-2023-audit-quality-study.pdf
- JRCPA-AUDITQ-2025: Jones & Roth CPAs & Business Advisors, *ERISA Covered Employee Benefit Plans Audit Quality*
  (firm summary of the 2023 study), 2025-12-03, https://www.jrcpa.com/?p=24899
- AAFCPA-DOLQ-2024: AAFCPAs, *DOL Audit Quality Study Underscores the Need for Specialized EBP CPA*, 2024-01-25,
  https://www.aafcpa.com/?p=24524
- SERENT-AUTIRE-2026: Serent Capital (Business Wire release), *Serent Capital Invests in Autire*, 2026-03-03,
  https://serentcapital.com/insights/serent-capital-announces-investment-in-autire-a-cloud-based-and-ai-powered-platform-supporting-cpa-firms-in-employee-benefit-plan-audits-2/
- SIKICH-WEBINAR-2025: Sikich, *Roses are Red, Audits are Due* (webinar listing), 2025-02-12,
  https://go.sikich.com/roses-are-red-audits-are-due-webinar-february2025.html
