# Nonprofit and government audits, with Form 990 (assurance, mid-market)

Last reviewed 2026-10-21; sources checked 2026-10-21. Use cases live in `../use-cases/nonprofit-government.yaml`
(16 entries: 0 A, 10 B, 4 C, 2 D). Ids are shortened here: `#07` means `assurance-nonprofit-government-07`; other
modules' ids are in full. Source keys in brackets are in the YAML or in §10.
**No outcome in this module is measured.** Every firm figure is a recollection or vendor-published; no error rate,
override rate, parallel run or peer-review or inspection finding on AI use in this work was found. Use the module for
risk awareness and interview probes, and quote its examples as early signals.

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

Audits of nonprofits and state and local governments at small, regional and top-100 firms: financial statement audits
under FASB ASC 958 (the not-for-profit standard) or GASB (the government standard), single audits of federal awards
under the Uniform Guidance, and other Yellow Book work (Government Auditing Standards, issued by GAO). It also folds
in the nonprofit tax work the same firms do: Form 990 (the exempt-organization information return) and Form 990-T
(tax on unrelated business income, or UBI). General audit patterns live in other modules; this one keeps what differs
for this engagement type: grant compliance, federal scrutiny of audit quality, and very small firms and finance teams.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Planning and risk assessment | Understand the entity and its grants; assess risk of material misstatement and, for single audits, risk of material noncompliance by compliance requirement | research-synthesis, expert-judgment | The 2026 GAS/SA Guide (the AICPA audit guide for Yellow Book and single audits) asks for more granular risk of material noncompliance, for fraud and error separately [BDO-GASSA-2026] |
| Major programs and Compliance Supplement | Pick programs and requirements to test, using OMB's annual Compliance Supplement | expert-judgment, research-synthesis | 2026 Supplement unreleased as of September 2026; draft adds five and removes nine programs, flags Medicaid, CCDF and TANF as higher risk, and requires FFATA (subaward reporting) procedures for all major programs [GAQC-DEV-2026] |
| SEFA | Obtain and test the schedule of expenditures of federal awards (SEFA, the list of federal awards and spending) | data-reporting, review-assurance | Must match awards, ledger, pass-through amounts and periods of performance; errors surface during the audit (`#08`) |
| Nonprofit financial statement audit | Contributions, conditional grants, net assets with donor restrictions, functional expenses, estimates, minutes and agreements [ARMANINO-NFPAI-2026] | review-assurance, expert-judgment | Long unstructured documents; vague donor letters |
| Controls and compliance testing | Control and compliance sampling to the guide's minimum sample sizes; deeper IT application testing [BDO-GASSA-2026] | review-assurance, data-reporting | Larger samples, more documentation and requests, possibly higher fees [BDO-GASSA-2026] |
| Deviations and noncompliance | Cause, monetary impact, questioned costs; management support needed [BDO-GASSA-2026] | expert-judgment | No AI evidence found |
| Reporting | Yellow Book reports, schedule of findings and questioned costs, disclosure review | document-production, review-assurance | Footnote tie-out and checklists done by hand |
| Quality | Yellow Book system of quality management, peer review, CPE [GAO-YBFAQ-2025] | coordination-scheduling, review-assurance | Government Auditing Standards engagements are a peer-review "must-select" training area [AICPA-PEERCONF-2026] |
| Form 990, 990-T and UBI | Organizer, public support test, program descriptions, schedules, compensation; for 990-T, identify unrelated activities, separate them ("silos") and use losses [TAX990-2026; AICPA-NFPWORKSHOPS-2026] | data-reporting, document-production | No AI-specific process material found |

Cross-cutting pains: rules in flux (Compliance Supplement delay; a Uniform Guidance rewrite proposed 2026-05-29 with
no significant change to Subpart F, the audit requirements, per the AICPA's Governmental Audit Quality Center, GAQC,
and barred from finalization through 2026-12-11) [GAQC-DEV-2026; FR-OMB-2026; OMB-UG-2026]; small firms citing a
shrinking talent pool and clients that cannot afford high fees [TR-NPCASE-2026]; auditees where 60% of nonprofits
surveyed rely on one full-time person for all financial management and accounting (the release subtitle says 65%,
for "all financial operations") [MOMENTIVE-2026]; and federal scrutiny of audit quality
(HHS's rigor review; an HHS-led review under the Financial Management Risk Reduction Act with an OMB report to
Congress due December 2027) [HHS-AERO-2026; GAQC-DEV-2026].

## 3. Where AI is changing the work

Lenses: improve (assist or augment), automate (no person on the normal path), delegate (an agent owns a multi-step
outcome), reinvent (`change_scope: model`). **Delegate has no evidence; reinvent has only a signal, not an entry
(below).** Automate has one entry. Most named practice is one vendor's customer material at small firms (Thomson
Reuters CoCounsel and Audit Intelligence) plus one regional firm on DataSnipper.

**Planning and document reading**
- Improve: `#01` minutes of boards and councils summarized for debt, grants and related parties (small local nonprofit
  and government firms; the stock template needed prompt tuning). See `assurance-planning-risk-assessment-01`.
- Improve: `#02` terms pulled from bond indentures and grant agreements (750 pages in three to four minutes, owner's
  recollection, small local firm). See `assurance-substantive-testing-14`.
- Improve: `#04` first-draft inherent risk by assertion so juniors start without a senior (small local firm).
  Nothing shows AI used for the single-audit risk of material noncompliance step.
- Improve: `#05` citation-backed research on ASC 958, GASB, Uniform Guidance and Yellow Book questions (Plante Moran
  pilot survey, top-100 firm; a small firm that asks the tool instead of calling another CPA). See `assurance-quality-management-12`.
- Improve (vendor claim): `#03` donor-restriction and conditional-grant classification support.

**Testing**
- Automate: `#06` population analysis, risk-based sample selection and linked documentation at three small local
  nonprofit-focused firms; the auditor sets strata and approves. See `assurance-substantive-testing-08` and `-09`.
- Improve (process): `#07` Excel agents run a single-audit grant compliance test (63 items in about an hour) and
  payroll sampling at a regional firm with government clients; a local firm cut one grant consultancy engagement's
  workpaper preparation from 80 to 25 hours (text recognition, not an agent). The only named AI use on single-audit testing.
- Idea: `#08` SEFA review against awards and the ledger (a top-100 firm's prompt for client finance teams).

**Completion and reporting**
- Improve: `#09` footnote-to-statement tie-out down to a dollar (small local firm). See `assurance-completion-reporting-06`.
- Improve (vendor claim): `#10` disclosure checklist agent; ASC 958 and GASB disclosure sets not described.
  See `assurance-completion-reporting-01` and `-03`.

**Auditee side (changes what auditors receive)**
- Idea: `#11` audit-readiness prompts for nonprofit finance teams (Armanino, top-100 firm; no outcomes).
- Improve: `#12` grant-document screening for policy-restricted terms at a university (precision 1.00, recall 0.73).

**Counterparties and government audit offices**
- Improve (process): `#13` HHS AERO: AI analysis of at least five years of single audit information across all 50
  states, plus a review of audit rigor. Auditors' past reports are now data for agency analytics.
- Improve (process): `#14` North Carolina's state auditor applies AI to large spending datasets, with people verifying
  results; Washington's publishes a governed-use AI policy.

**Form 990 and exempt-organization tax**
- Improve (vendor claim): `#15` AI error check and chatbot inside one 990 e-file product, the only AI feature found.
- Counterparty (vendor-level evidence): `#16` IRS Tax Exempt and Government Entities (TE/GE) AI screening of public
  referrals (planned for fiscal 2024; status not confirmed).

**Gaps.** No named AI deployment for testing specific compliance requirements (eligibility, allowable costs,
subrecipient monitoring, procurement and suspension checks, cash management), major program determination, findings
drafting, or 990 and 990-T preparation. A vendor lists Single Audit content with the OMB Compliance Supplement in its
Guided Assurance methodology; its AI role is not stated [TR-GAFEATURES-2026].

**Reinvent signal (no entry; see `assurance-quality-management-28`).** Oath, an AI-native audit firm, lists non-profits
among its client types and says it verifies every record on an ongoing basis; no client or result is published [OATH-2026].

## 4. Interview probes

Ask in the person's setting: engagement partner, single-audit or nonprofit practice lead, quality partner, 990 preparer.

1. **"Walk me through your last single audit's compliance and control sampling. How will the 2026 GAS/SA Guide's revised
   minimum sample sizes change it, and does any tool touch selection?"** Reveals whether `#06` exists and whether any
   tool has been checked against the revised tables (no source says one has).
2. **"Which documents do staff read end to end: minutes, grant agreements, donor letters, bond indentures? Which would
   you hand to a tool first, and who re-reads the output?"** Reveals the quickest start (`#01`, `#02`) and the review step.
3. **"Did you use the vendor's stock templates or tune them? What went wrong first?"** Reveals prompt maturity; the
   St. Pierre firm said its stock minutes template was "not summarizing" and then customized it.
4. **"HHS is analyzing five years of single audit history and reviewing rigor. What does your file show about how
   the work was evidenced, and would AI use be visible on it?"** Reveals exposure to `#13` and documentation readiness
   (`assurance-quality-management-23`).
5. **"How many clients report in the same format (school districts, housing authorities, a grantor's template)?"**
   Reveals whether a reusable agent like `#07` pays back.
6. **"Which single-audit step eats the most senior time: risk of material noncompliance, major programs, questioned
   costs or findings?"** Reveals where demand exists with no public AI evidence; frame anything there as a pilot.
7. **"When one person runs the client's finance, how do client-prepared (PBC) items and the SEFA arrive? Do you accept AI-assisted
   schedules, and what do you test differently?"** Reveals auditee readiness (`#08`, `#11`) and independence questions.
8. **"Is your Yellow Book system of quality management ready for its 2026-12-15 evaluation, and does it name AI tools?"**
   Reveals whether tool governance sits in the system peer reviewers will test.
9. **"What did your last peer review say about single audits or Yellow Book engagements?"** Reveals the baseline that
   any documentation or sampling tool must improve on (§5).
10. **"Where does client data, including donor and employee data, go when staff use AI, and what is approved?"**
    Reveals the confidentiality block practitioners name most often.
11. **"Who prepares the 990 and 990-T, does any step use AI, and how did you decide on consent for return data?"**
    Reveals tax-side exposure (Circular 230, section 7216) and the near-absence of AI in 990 work.
12. **"Since adding AI, have you backfilled departures, changed fees or taken on more clients?"** Reveals the capacity
    story; Wells CPA says it is two people down with the same revenue output (owner's comparison).

## 5. Metrics and benchmarks

**Peer review is the only independent baseline, and none of these reports mentions AI.** Counts are small and
reviewer-selected, so rates are not comparable across societies.
- Tennessee 2025: single audits 2 of 11 nonconforming; other Government Auditing Standards 1 of 29 [TSCPA-PEERREVIEW-2025].
- Minnesota and North Dakota 2025: single audits 3 of 15 [MNCPA-PEERREVIEW-2025].
- Oklahoma, South Dakota, Kansas 2025: OMB single audits 12 of 40; other Government Auditing Standards 18 of 43
  [OKSCPA-PEERREVIEW-2025].
- Oregon, Hawaii, Guam and Northern Mariana Islands 2025: OMB single audits 4 of 15 [OSCPA-PR-2026].

**Firm figures (all recollections or vendor summaries; none tracked).**
- Sample selection about three hours to about five minutes, The Forde Firm (vendor tile: "95% faster") (`#06`); a
  750-page bond indenture summarized in three to four minutes, St. Pierre firm (`#02`).
- Board-minute or contract review about one hour to about five minutes, Harris, Hardy & Johnstone, a commercial firm (`#01`).
- Single-audit grant compliance test of 63 items in about an hour, PB&H; workpaper preparation 80 to 25 hours on a
  50-fund grant engagement, Perry & Associates (vendor headline 68%) (`#07`).
- Wells CPA: two fewer staff than last year, same revenue output (`#06`). Sam Brown CPA: at least five to six hours
  saved per audit from the same sampling tool, not nonprofit-specific [TR-SAMBROWN-2026].
- Plante Moran pilot survey (140+ participants; general audit research): 96% found it useful for practice staff, 91%
  faster than traditional research, 87% said buy it for all staff, 77% more confident with generative AI, 62%
  significant research time savings, 58% used other tools less (`#05`).

**Vendor and sector figures.**
- Caseware (general audit, vendor): 2.7 review hours saved per disclosure checklist workflow; 94% accuracy on "golden
  dataset" items from beta traces; 15-20 minutes to under two minutes per indicative workflow (`#10`).
- Nonprofit sector survey (500 executives, vendor): 91% use AI in some official capacity, 29% extensively; board
  support strongly linked to extensive use [MOMENTIVE-2026].
- GrantCheck: precision 1.00, recall 0.73 on 22 terms in 5 documents; usability 85.9 of 100 (`#12`). Counterparties: HHS says "hundreds" of grantees have not submitted required audits (`#13`); about 76% of closed IRS
  exempt-organization exams changed tax in fiscal 2023, an exam rate, not an AI result (`#16`).

**What to measure (recommend these; no one publishes them yet)**: hours per minutes review, agreement or sample
before and after; share of AI-flagged items a reviewer rejects; differences found by tie-out per draft; peer-review
comments on AI-assisted workpapers; SEFA errors found by the auditor after client pre-review; time to absorb a new
Compliance Supplement; repeat findings and late submissions among clients (the data HHS now analyzes).

## 6. Guardrails

**Standards and regulators.** None has issued AI-specific rules for this work; GAQC lists "emerging ethics, quality
management, and AI-related guidance" only as a watch item [GAQC-DEV-2026].
- **Yellow Book quality management.** Under the 2024 revision a firm had to design its system by 2025-12-15 and
  complete its initial evaluation by 2026-12-15; the GAO FAQ does not mention AI [GAO-YBFAQ-2025].
- **AICPA practice aid (2026-10-13).** Firm quality management for AI tools, team competence,
  planning AI use per engagement, partner responsibility for approved tools; the auditor stays responsible for
  supervision, review and conclusions; more risk and evidence material to come [AICPA-PA-2026].
- **2026 GAS/SA Guide.** More granular risk of material noncompliance, revised minimum sample sizes, deeper IT testing
  [BDO-GASSA-2026]. Any sampling or risk tool must be checked against it; no source shows one has been.
- **Federal oversight.** HHS lists Uniform Guidance remedies: withholding payments, disallowing costs, suspension and
  debarment [HHS-AERO-2026]. GAO says AI for fraud and improper payments needs reliable data and a human in the loop
  [GAO-FRAUDAI-2026].
- **Tax side.** Circular 230 duties (due diligence 10.22, fees 10.27(a), competence 10.35, procedures 10.36) apply to AI
  use [IRS-OPR-2026]; the IRS has not said whether sending return data to an AI tool is a section 7216
  disclosure, and nothing found addresses exempt-organization returns [CPAPA-SETTLE-2026]. Detail sits in [tax guardrails](../../tax/guardrails.md).
- **Confidentiality.** Donor, employee and grant data go to approved tools only, under a written policy [ARMANINO-NFPAI-2026].
- **Independence (probe, not a finding).** `#08` and `#11` are client-side prompts; management owns the SEFA. No source
  discusses independence when an auditor's firm supplies such prompts; check against
  [acceptance-independence](acceptance-independence.md).

**Design guardrails seen in practice**: tune templates and name the sections to read; return "N/A" rather than verbose output
[TR-STPIERRE-2026]; tie every agent result to a source snip a reviewer can open (`#07`); keep AI output as drafts
[ARMANINO-NFPAI-2026]; have staff verify and take responsibility for AI-assisted work, as Washington's state auditor
requires [WASAO-AIPOLICY-2026].

**Steps that stay with a person**: risk of material noncompliance and major program determination; sample design
and approval; judging noncompliance, questioned costs and findings; donor-restriction classification (management,
then auditor testing); reliance on extracted agreement terms; the opinion; signing a 990.

## 7. Roles and how they evolve

- **Small-firm owners hold output with fewer staff.** Wells CPA reports two fewer people and the same revenue output;
  the vendor frames this as not backfilling departures (vendor-published) [TR-NPCASE-2026].
- **Juniors start earlier.** The Forde Firm owner says staff engage with inherent risk by assertion without her
  walking them through it, and that the tool lets staff "act without me having to be involved" (`#04`). The St. Pierre firm asks the tool
  instead of calling another CPA (`#05`). Citrin Cooperman's innovation leader links in-workflow reasoning to staff
  learning (vendor-published) [CASEWARE-CITRIN-2026].
- **Agents take staff tasks and some senior ones.** PB&H says its agent repeats monotonous staff tasks and also builds
  tests and checks compliance, which it called more senior-level work (`#07`).
- **Hiring.** An Aprio posting for tax-exempt and single audit work asks for "experience with data analytics or audit
  automation tools" (2026-09-18); not an AI role [APRIO-JOB-2026].
- **Pipeline and clients.** GAQC lists public-sector CPA pipeline initiatives as a watch item [GAQC-DEV-2026]. An AHRC
  finance leader says AI moves nonprofit finance staff from reconciling to analyzing [AICPA-NFPCONF-2026].
- **Advisers to grantees.** Cherry Bekaert (top-100 firm) and Feldesman (law firm) advise clients to fix repeat
  findings, timeliness and corrective action plans as AERO starts (`#13`).

## 8. Frontier

- **2024-02-06** EY reports IRS TE/GE plans an AI tool to screen exempt-organization referrals in fiscal 2024 (`#16`).
  **2025-12-15** GAO Yellow Book quality-management FAQ; systems due that day [GAO-YBFAQ-2025].
- **2026-05** Wolters Kluwer course "Using AI in a Government Audit" (two hours): teaching demand, not practice [WK-GOVAI-2026].
- **2026-05-20 and 2026-06-04** Caseware Verity launch and its Agentic Pioneer Program; Caseware customers include Plante
  Moran, CohnReznick, Forvis Mazars, Wipfli, Citrin Cooperman, Weaver, Carr Riggs & Ingram and PKF O'Connor Davies
  (vendor list) [CASEWARE-LAUNCH-2026; CASEWARE-PIONEER-2026].
- **2026-05-21** HHS launches AERO, AI analysis of single audit history with a review of audit rigor [HHS-AERO-2026].
- **2026-05-29** OMB proposes a Uniform Guidance rewrite; comments closed 2026-07-13 [FR-OMB-2026]. **2026-09-02** a
  continuing resolution bars OMB from finalizing it through 2026-12-11 [OMB-UG-2026].
- **2026-06-15 to 17** AICPA Not-for-Profit Industry Conference; a vendor says AI dominated its sessions
  [AICPA-NFPCONF-2026; TAX990-NFPCONF-2026].
- **2026-07-09 and 2026-08** North Carolina and Washington state auditors describe governed AI use (`#14`).
  **2026-07-13 and 2026-10-08** Caseware announces Citrin Cooperman and PKF O'Connor Davies DAS Suite adoption
  [CASEWARE-CITRIN-2026; CASEWARE-PKF-2026].
- **2026-08-06** Armanino publishes AI prompts for nonprofit audit readiness, including SEFA review (`#08`, `#11`).
- **2026-09-23** AICPA webcast "Practical AI Techniques for CPAs Serving Not-for-profits"; rebroadcast scheduled
  2026-12-18 [AICPA-NFPWEBCAST-2026].
- **2026-10-08** GAQC: 2026 Compliance Supplement still unreleased; AI guidance only a watch item [GAQC-DEV-2026].
  **2026-10-13 / 10-15** AICPA AI practice aid; BDO on the heavier GAS/SA Guide [AICPA-PA-2026; BDO-GASSA-2026].
- **2026-10-19 to 21** AICPA Governmental and Not-for-Profit Conference, Dallas, with an AI session by Gemifi's
  cofounder [AICPA-NFPAI-2026]. Agenda not retrieved; check for recordings.
- **Scheduled: 2026-12-15** Yellow Book initial quality-management evaluation due [GAO-YBFAQ-2025]. **2027-12** OMB
  report to Congress on the single-audit quality review [GAQC-DEV-2026]. Watch for the first peer-review or GAQC
  comment on AI-assisted single-audit workpapers (none found).

## 9. Common objections

- **"Donor and client data can't go into AI."** A real concern: Gemifi's cofounder says worries over personal data
  (PII) keep many teams on Microsoft tools [AICPA-NFPAI-2026]. Response: approved tools and a written policy first, as
  Armanino's playbook sets out [ARMANINO-NFPAI-2026].
- **"It makes things up."** Armanino warns of incorrect citations, facts and calculations [ARMANINO-NFPAI-2026].
  Response: use cited output, verify against the source, and tie results to source snips (`#07`); treat output as a draft.
- **"The stock tools don't fit government work."** The St. Pierre firm agrees: its stock minutes template was "not
  summarizing" until it applied vendor prompt advice (`#01`). Response: budget for template tuning, naming sections and "N/A" rules.
- **"Peer reviewers won't accept it."** No peer-review finding on AI exists either way. The three small firms say
  generated documentation eased peer review, and one says a peer reviewer then switched to the same vendor (`#06`,
  vendor-published). Response: the generated documentation is what a peer reviewer reads, so review it as evidence.
- **"AI cannot audit itself."** A Prager Metis (top-100) not-for-profit partner says auditors test the information
  management gives them, whatever tool produced it [ATODAY-DAVIS-2026]. See [assurance-over-ai](assurance-over-ai.md).
- **"The rules keep moving, so why invest now?"** True: the Supplement is late and a Uniform Guidance rewrite is
  proposed, though barred from finalization through 2026-12-11 [GAQC-DEV-2026; OMB-UG-2026]. Response: start with steps that do not depend on the Supplement (minutes,
  agreements, tie-out, research), and recheck sampling tools against the new guide.
- **"Agencies using AI on us is unfair."** Stakeholders have raised transparency, methodology and fairness questions
  about AERO [CBH-AERO-2026; THOMPSON-AERO-2026]. Response: HHS is reading single audit information auditors produced, and Cherry
  Bekaert and Feldesman advise grantees to fix repeat findings, timeliness and corrective action plans (`#13`).
- **"We're too small."** The best-documented users are small local firms, one doing about 80 audits a year (`#01`,
  `#06`). Response: the three nonprofit-focused firms layered AI onto platforms they already used [TR-NPCASE-2026].
- **"Our people lack the skills."** Gemifi's cofounder says no one is "anywhere near the skill ceiling"
  [AICPA-NFPAI-2026]. Response: the documented small firms work through saved, shared templates (`#01`, `#09`).

## 10. Sources

Full details (title, publisher, type, URL, date, access, locator) are in the YAML.
- **In the YAML:** TR-NPCASE-2026, TR-STPIERRE-2026, TR-SCALING-2026, TR-PLANTEMORAN-2025, TR-CCAUDITPAGE-2025,
  TR-STATE-2026, DATASNIPPER-PBH-2026, DATASNIPPER-PERRY-2025, CASEWARE-LAUNCH-2026, CASEWARE-CITRIN-2026, AICPA-PA-2026,
  AICPA-NFPAI-2026, AICPA-NFPCONF-2026, AICPA-NFPWORKSHOPS-2026, GAQC-DEV-2026, GAO-YBFAQ-2025, GAO-FRAUDAI-2026,
  BDO-GASSA-2026, TSCPA-PEERREVIEW-2025, ARMANINO-NFPAI-2026, MOMENTIVE-2026, GRANTCHECK-2025, HHS-AERO-2026,
  FELDESMAN-AERO-2026, THOMPSON-AERO-2026, CBH-AERO-2026, NCAUDITOR-2026, WASAO-AIPOLICY-2026, TAX990-2026,
  IRS-OPR-2026, CPAPA-SETTLE-2026, EY-TEGE-2024, TIGTA-2025, TAX990-NFPCONF-2026.
- **Not in the YAML (cited in this file only; opened unless marked):**
  - FR-OMB-2026: OMB, *Regulation for Federal Financial Assistance* (proposed rule; date and comment close read from the Federal Register API, page blocked), Federal Register, 2026-05-29, https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance
  - OMB-UG-2026: UNC School of Government, *2026 Proposed Updates to the Uniform Guidance* (slides; timing slide), 2026-09, https://www.sog.unc.edu/sites/default/files/2026%20Uniform%20Guidance%20Proposed%20Updates-1.pdf
  - MNCPA-PEERREVIEW-2025: Minnesota Society of CPAs, *2025 Annual Report on Peer Review Activities*, 2026-02, https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf
  - OKSCPA-PEERREVIEW-2025: Oklahoma Society of CPAs, *2025 Annual Report on Peer Review Activities*, 2026-03, https://prod.oscpa.com/storage/assets/Peer%20Review/Annual%20Report/2025%20OSCPA%20Peer%20Review%20Activities.pdf
  - OSCPA-PR-2026: Oregon Society of CPAs, *Annual Report on Peer Review Activities for 2025*, 2026-03-01, https://www.orcpa.org/storage/assets/Pages/About/Peer%20Review/Annual%20Report%202025.pdf
  - AICPA-PEERCONF-2026: AICPA, *Peer Review Conference* (must-select training on Government Auditing Standards), 2026-08, https://www.aicpa-cima.com/cpe-learning/conference/aicpa-peer-review-conference
  - AICPA-NFPWEBCAST-2026: AICPA & CIMA, *Practical AI Techniques for CPAs Serving Not-for-profits* (webcast), 2026-09-23, https://www.aicpa-cima.com/cpe-learning/webcast/practical-ai-techniques-for-cpas-serving-not-for-profits
  - WK-GOVAI-2026: Wolters Kluwer CPELink, *Using AI in a Government Audit* (self-study), 2026-05, https://www.cchcpelink.com/self-study/using-ai-in-a-government-audit/34745/
  - TR-GAFEATURES-2026: Thomson Reuters, *Guided Assurance features* (vendor; date from page metadata), 2026-05-20, https://tax.thomsonreuters.com/en/products/checkpoint-engage/features
  - TR-SAMBROWN-2026: Thomson Reuters, *Small firm, big leverage: Sam Brown, CPA, Inc.* (vendor; date from page metadata), 2026-05-11, https://tax.thomsonreuters.com/en/insights/case-studies/small-firm-big-leverage-sam-brown-cpa-inc-scales-advisory-and-streamlines-audits-with-ai
  - CASEWARE-PIONEER-2026: Caseware, *Caseware launches Verity Agentic Pioneer Program*, 2026-06-04, https://www.caseware.com/news/trusted-by-the-majority-of-top-30-u-s-accounting-firms-caseware-launches-verity-agentic-pioneer-program
  - CASEWARE-PKF-2026: Caseware, *PKF O'Connor Davies adopts AI-enabled DAS Suite powered by Caseware Verity, and joins the Caseware Agentic Pioneer Program*, 2026-10-08, https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program
  - ATODAY-DAVIS-2026: Accounting Today, *"AI cannot audit itself" - a response* (Scott Davis, Prager Metis), 2026-06-05, https://www.accountingtoday.com/opinion/ai-cannot-audit-itself-a-response
  - OATH-2026: Oath, *Oath | Swear by your numbers* (firm home page; live page, undated), 2026-10, https://www.oathverified.com/
  - APRIO-JOB-2026: Aprio, *Senior Audit Manager, Non-Profit* job posting, 2026-09-18, https://jobs.lever.co/Aprio/705d6e91-0dd0-4097-bae2-768a2c252f1d
