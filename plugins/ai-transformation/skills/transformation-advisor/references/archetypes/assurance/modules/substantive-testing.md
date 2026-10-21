# Substantive testing (assurance)

Last reviewed 2026-10-17. Use cases: `../use-cases/substantive-testing.yaml`
(25 entries). `#10` means `assurance-substantive-testing-10`; other modules' ids are
written in full. Source keys in brackets, such as [IFIAR-TTF-2025], are in the YAML or in §11. Almost every outcome
figure is self-reported or vendor-published; no independent measure of any AI substantive tool's accuracy in a live
audit exists. Say so when you quote one.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Journal-entry and fraud testing](#3-journal-entry-and-fraud-testing)
4. [Where AI is changing the work](#4-where-ai-is-changing-the-work)
5. [Interview probes](#5-interview-probes)
6. [Metrics and benchmarks](#6-metrics-and-benchmarks)
7. [Guardrails](#7-guardrails)
8. [Roles and how they evolve](#8-roles-and-how-they-evolve)
9. [Frontier](#9-frontier)
10. [Common objections](#10-common-objections)
11. [Sources](#11-sources)

## 1. What this module covers

Substantive procedures are the tests that look directly for misstatement in balances, transactions and disclosures,
as opposed to tests of controls. This module covers journal-entry and fraud testing, choosing what to test (a sample,
specific high-risk items or the whole population), vouching (matching recorded items to supporting documents),
third-party confirmations, substantive analytics, contract and revenue testing, inventory observation and challenge
of accounting estimates, plus the agent platforms that now run these tests. Journal-entry testing is the most mature
use; evidence-to-sample matching has the only per-task time figures; firms' own verdict on savings is still modest.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Define and validate the population | Extract the ledger, reconcile to the trial balance, confirm completeness | data-reporting | Poor client data (60%) and no system access (53%) are top blockers; 19% automate data ingestion [CPACOM-ATR-2025] |
| Design procedures | Tailor tests to assessed risks; choose all items, specific items or a sample | expert-judgment | GenAI used mostly for admin and research so far [PCAOB-GENAI-2024] |
| Journal-entry and fraud testing | Score or filter entries, select, investigate, extend fraud work | review-assurance, data-reporting | Rules-based filters miss subtle patterns and flood teams with false positives (§3) |
| Item selection and sample size | Risk-based selection; smaller samples where methodology allows | review-assurance, data-reporting | 46 of 420 inspected listed audits had a sampling finding (11%) in 2025 [IFIAR-SURVEY-2026] |
| Evidence requests and confirmations | Request lists, client uploads; bank, AR/AP and legal confirmations | coordination-scheduling, transaction-processing | Manual chasing; PDFs and screenshots are easy to forge; BDO NL sometimes got 156+ bank files per engagement |
| Vouching, tracing, tie-out | Match each item to invoices, contracts and bank activity; recompute; foot | review-assurance, transaction-processing | About two days per engagement (one practitioner); selections of hundreds of items; review backlog |
| Contract and lease review | Extract terms and risk indicators for revenue and lease testing | research-synthesis, review-assurance | Long contracts; a screening summary mistaken for a full read [FRC-GENAI-2026] |
| Substantive analytics | Build an expectation, compare, investigate differences | data-reporting | Only 11% of US firms surveyed automate it [CPACOM-ATR-2025] |
| Inventory observation | Attend counts, test counts, reconcile to perpetual records | physical-field | Slow and disruptive; 9% of inspected listed audits had an inventory finding |
| Accounting estimates | Evaluate management's method, data and assumptions, often with specialists | expert-judgment | Highest inspection finding rate: 22% (112 of 498) [IFIAR-SURVEY-2026] |
| Exceptions and conclusion | Decide misstatement or explained difference; extend testing | expert-judgment | Whole-population tests surface more items; thin outlier testing is a common finding |
| Documentation and review | Workpapers, review, sign-off, record of tool use | document-production | Reviewer and quality-reviewer bottleneck; the FRC expects tool use and use criteria on file |

Inspection context: 35% of inspected listed public-interest-entity audits had at least one finding in 2025 (26% in
2022); none of IFIAR's finding categories is AI-specific [IFIAR-SURVEY-2026].

## 3. Journal-entry and fraud testing

**Why it is the most mature use.** 88% of responding IFIAR members frequently saw automated tools in journal-entry
testing in 2024 audit files, against 55% for other substantive procedures and 43% for controls testing [IFIAR-TTF-2025]. All six US
network firms report tools that identify and select journal entries [PCAOB-TAA-2024]. These counts cover all tools,
not only AI. Testing journals is a required fraud response under ISA 240 (Revised), paragraphs 47-48, effective for
periods beginning on or after 15 Dec 2026 [IAASB-ED330-2026; IAASB-ISA240-2025].

**What the work looks like now (`#01`).** A tool scores every ledger entry with machine-learning and statistical
models, alongside rules; auditors drill down and investigate entries above a threshold. Named users: Buzzacott, BDO UK
(across its audit practice after a trial, June 2026), KPMG (MindBridge feeding Clara) and EY (Canvas processes more
than 1.4 trillion journal-entry lines a year). The FRC's hypothetical example weights an unsupervised model and
rules-based routines in one tool and shows which features made an item unusual [FRC-AIAUDIT-2025].

**Follow-up is the new bottleneck (`#03`).** Vendors such as MindBridge pitch explainable full-population risk scores
that auditors drill into; no follow-up accuracy figure is published. The FRC warns that a flagged item may be fine
while similar unflagged items are the risky ones, so follow-up must go beyond the flagged list [FRC-AIAUDIT-2025].

**Research frontier (`#02`, idea).** A language model flags entries and explains why (tax-ledger data). On a synthetic ledger, rules
produced 942 false positives on 5,000 posting IDs against 12 for the best model; on the real ledger, removing the
statistical hint raised the model's false positives from 32 to 1,973 [ARXIV-AUDITCOPILOT-2025]. Agents passed 16.86%
of journal-entry risk-testing workpapers, against 94.51% for completeness, in a benchmark [ARXIV-FAB-2026].

**AI-enabled fraud and evidence integrity (`#04`, `#05`).** Generative tools make forged invoices, bank letters and
vendor files cheap; IRBA and IFIAR warn that evidence may be AI-generated [IRBA-AI-2024; IFIAR-TTF-2026]. A vendor and
practitioners advise corroborating documents against bank records, vendor masters and approval logs, and verifying authenticity
and provenance independently (`#04`). Preparedness is low: of 713 anti-fraud professionals, 75% report a rise in
GenAI document fraud and forgery over two years and only 7% say their organisation is more than moderately prepared
[SAS-ACFE-2026]; of 373 internal-audit leaders, 65% name fabricated invoices or documents among top concerns and 62%
say they are unprepared or minimally prepared [IIA-AIFRAUD-2026]. When the client's own AI produces entries or
accruals, the AICPA says auditors may test the outputs substantively and, if that is not enough, should test
controls (`#05`, idea; see `assurance-controls-testing-15`).

**Guardrails specific to this area.** Run rules-based routines alongside any model (an unsupervised model misses
entries that are consistently miscoded); document why use criteria were met; run with and without the tool to check
findings (Buzzacott); pair fraud specialists with data tools [NYENRODE-2026]. 31% of IFIAR members reported
findings that tools were not used as intended, mostly misread results and thin outlier testing [IFIAR-TTF-2025].
**Missing:** no firm has published false-positive rates or how many flagged entries proved to be misstatements.

## 4. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome), reinvent (the service model changes, or a process stops existing). Coverage: assist 5, augment 12,
automate 4, delegate 4; step 18, process 6, model 1. Only one entry changes the service model, and no delegate-level
entry has a measured result.

- **Planning and population.** Improve: `#06` GenAI in KPMG Clara helps design substantive procedures (announced);
  `#07` an Excel agent cleans and reconciles a general ledger to the trial balance (59,157 simulated rows, ~10 minutes).
- **Selecting what to test.** Improve: `#08` technology-assisted selection of all items, specific items or a
  risk-targeted sample (six of six US networks); `#09` Cherry Bekaert cuts sample sizes with risk scoring (66% on an
  illustrative client; process scope).
- **Vouching, matching and tie-out.** Automate: `#10` agents match sampled items to documents and bank activity
  (Oberlander about 16 hours to 5-6 per engagement; Sanville hours to minutes; PwC Evidence Match). This is the
  home of these named (estimated, grade B) figures; `assurance-controls-testing-07` covers the same step in tests of controls. `#13` PwC fund-audit
  tie-out (pilot). Improve: `#11` FGMK's firm-built Excel agents (pilot group: 30-45 minutes to about 5 minutes of
  review per selection, plus reviewer-side agents); `#12` DataSnipper evidence snipping and extraction (assist).
- **Contracts, revenue and judgment-heavier tests.** Improve: `#14` contract and lease review (FRC design for revenue
  sampling; CoCounsel "up to 70% faster", a vendor claim); `#15` PwC attempting agents on pharmaceutical rebate
  revenue, and EY expecting agents to flag memos the data does not support.
- **Substantive analytics.** Improve: `#16` technology-built expectations from detailed or unstructured data (11%
  adoption; ED-520 examples).
- **Confirmations and external data.** Automate: `#17` confirmation platforms and direct bank feeds (Moore Polska,
  Crowe Spain, Beever & Struthers; Rabobank and BDO NL feed aimed at 100% testing). Mostly workflow, not AI.
- **Inventory and estimates.** Improve: `#18` drone counts reconciled to perpetual records (2018 EY proof of concept;
  681 to 19 hours in a livestock study); `#19` idea: AI-generated challenge of management's estimates.
- **Agents and the operating model.** Delegate: `#20` KPMG Clara agents for expense vouching and unrecorded
  liabilities, moving to an orchestration pilot (summer 2026), and Fieldguide's orchestrator running the
  unrecorded-liabilities search end to end; `#21` EY auditor agents exchange evidence requests with client agents
  (pilot); `#22` firm-wide platforms (EY, Deloitte, Grant Thornton) run preliminary procedures; `#24` PwC Australia's
  AI-native pilot tests balances on full populations against third-party data (also reinvent: the sample goes; for
  control populations see `assurance-controls-testing-08`). Improve: `#23` idea: a second AI reviews AI-performed work (deployed analogue
  `assurance-controls-testing-10`). Reinvent: `#25` Ledgerline, a pre-launch benefit-plan audit firm built to test every transaction.

## 5. Interview probes

1. **"Walk me through one area (cash, revenue or payables) from population to sign-off. Where do the hours go?"**
   Reveals whether the pain is data access (`#07`), selection (`#08`), vouching (`#10`) or review, and gives a baseline.
2. **"Which tests now run on 100% of a population, and which on a sample? What changed in how you document
   sufficiency and treat exceptions?"** Reveals whether full-population work is real, and expectation-gap risk (`#24`).
3. **"For journal entries: which tool, which rules alongside it, what threshold, how many flags per engagement, and
   how many proved to be misstatements?"** Reveals whether any detection-quality evidence exists. None is public.
4. **"When an agent's match disagrees with a person, who wins, how often, and where is it recorded? Any parallel-run
   results?"** Reveals quality evidence; IFIAR suggests false positives and negatives against a manual sample.
5. **"How do you evidence completeness and reliability of client data before a tool runs, including external
   information the client gives you electronically?"** Reveals readiness for AS 1105.10A and an AFM finding.
6. **"How do you know a document is authentic before you vouch to it? Which confirmations still arrive as PDFs,
   screenshots or email?"** Reveals exposure to AI-forged evidence (`#04`, `#17`).
7. **"Who decided a tool's output was persuasive enough to reduce or replace a sample, and what does the file
   show?"** Reveals methodology risk (FRC) and whether documentation would survive inspection.
8. **"Where does the time saved go: review, more testing, fewer hours billed? Has a client asked for a lower fee?"**
   Reveals the economics; PwC calls savings modest and fee pressure is reported (§10).
9. **"How do juniors learn what a good test looks like when agents do routine testing? What do reviewers check
   first on agent-produced workpapers?"** Reveals skills-pipeline and automation-bias risk.
10. **"Do you work under a third-party methodology, and what still depends on specialists (estimates, complex
    revenue)?"** Reveals the methodology limit on `#09` and where `#15` and `#19` would apply.

## 6. Metrics and benchmarks

**Adoption and regulator observations (independent)**
- IFIAR members "frequently" seeing automated tools, 2023 / 2024 / 2025 (2025 read from an unlabelled chart):
  journal entries 86% / 88% / about 86%; substantive procedures 51% / 55% / about 63%; controls testing 33% / 43% /
  about 44% [IFIAR-TTF-2025; IFIAR-TTF-2026]. Tools not used as intended: 31% of members (2024).
- US networks averaged about 18 audit tools per firm in 2023 (about 13 in 2018); about 90% were for visualisation,
  summarisation, tabulation or modelling and under 7% used AI, blockchain or RPA [PCAOB-TAA-2024].
- US firms with an automated solution (54 firms): foot and proof 39%, confirmations 39%, trial-balance import 35%,
  data ingestion 19%, substantive analytics 11%, none 22%; blockers: untrained staff 66%, poor client data 60%, no
  system access 53% [CPACOM-ATR-2025].
- 2025 inspection finding rates (listed audits where inspected): estimates 22%, sampling 11%, inventory 9%, revenue
  8%, substantive analytics 5%, fraud procedures 4% [IFIAR-SURVEY-2026].

**Named outcomes (vendor-published or self-reported; effort, not quality)**
- Oberlander (owner's estimate): about 16 hours to 5-6 hours per engagement; Sanville: hours to minutes, realisation
  $150-200 to $250+ an hour, zero PCAOB comment forms after a full methodology overhaul (`#10`). FGMK pilot group:
  30-45 minutes to about 5 minutes of review per selection; CROP: cash testing about 80% faster (`#11`). Circit says
  Moore Polska saved up to 20 hours per audit, including PBC requests (vendor narrative) (`#17`).
- Cherry Bekaert: 66% smaller sample on an illustrative client (`#09`). NAO via DataSnipper: GBP 400,000 saved and
  routine work up to three times faster (second-hand, work not stated) (`#12`).
- PwC, a year in: time savings "not that drastic yet" [CFODIVE-PWC-2026]. Forecast: some Big Four leaders expect
  agents to contribute 20-30% of a typical audit by 2029 [CTRLCOUNCIL-WSJ-2026].

**Vendor claims (grade C; ask for measured cases):** CoCounsel up to 70% faster [TR-AGENTIC-2025]; Fieldguide "up to
70%" of testing [FIELDGUIDE-FIELDAGENTS-2025]; DataSnipper "$1.4B" savings, 600,000+ users [DATASNIPPER-PRODUCTIVITY-2026].

**Benchmarks (synthetic or adjacent data)**
- FinancialAuditBench (90 tasks, 11 models; Modus Audit co-authors): best agent 69.17% strict pass in one attempt,
  44.44% across all eight; by area, receivables 4.17%, revenue 7.58%, cash 56.06%, payables 68.18% [ARXIV-FAB-2026].
- General chat models on 167 document samples: 74-96% correct, 76-100% after prompt tuning [GRACZYK-2025].

**What to measure (recommend these, not hours alone):** IFIAR's list of engagement coverage, false-positive and
false-negative rates against a manual sample, rework and escalation rates, and benchmarking against traditional
methods [IFIAR-TTF-2026]; plus time per selection, flags per engagement and the share confirmed as misstatements,
reviewer override rate, match accuracy (a yes/no metric, per PwC [CFOBREW-PWC-2025]) and inspection findings.

## 7. Guardrails

**Standards and regulators (none prohibits AI; none sets AI-specific requirements for substantive testing)**
- **PCAOB.** Technology-assisted-analysis amendments apply to fiscal years beginning on or after 15 Dec 2025
  [SEC-TAAORDER-2024]: AS 1105.10A (understand the source and handling of external information the company provides
  electronically, and test it or the controls over it) [PCAOB-PS2025-004], AS 2301.48 (what a test of details is) and
  AS 2301.49-.50 (investigate items the criteria identify). The Board says they do not address AI as such
  [PCAOB-TAA-2024]. All five commenters to the SEC said guidance was warranted, and PwC would not support the
  amendments without further amendment or interpretive guidance [SEC-TAAORDER-2024]. The new confirmation standard
  covers paper and electronic methods: confirm third-party cash or access external data directly [PCAOB-CONFIRM-2023].
- **AICPA.** SAS No. 150 (confirmations, published 13 Jul 2026) and SAS No. 151 (fraud, published 19 Aug 2026) take
  effect for periods ending on or after 15 Dec 2028 [JOFA-SAS150-2026; JOFA-SAS151-2026]. The October 2026 practice aid
  lets one AI tool check another without reducing the auditor's review duties [AT-AICPAPA-2026].
- **IAASB.** ISA 330/500/520 exposure drafts (5 Aug 2026; comments due 15 Dec 2026) add no technology requirement:
  the board judged it premature, as generative tools may make inputs impossible to evaluate [IAASB-ED500-2026, EM
  paras 67-69]. Appendix 3 warns of automation bias; testing specific items cannot be projected to the population;
  ED-520 shows technology-built expectations [IAASB-ED520-2026]. A March 2026 project will modernise inventory
  attendance (ISA 501) and confirmations (ISA 505) [IAASB-500SERIES-2026].
- **FRC (UK).** June 2025 journal-testing example [FRC-AIAUDIT-2025]; March 2026 generative and agentic AI guidance
  with a contract-review example: risks are deficient output, misuse of output and non-compliant methodology; outputs
  need not match the persuasiveness of the procedure replaced if the methodology does not overstate them
  [FRC-GENAI-2026]. The six largest UK firms did no formal monitoring to quantify tools' quality impact [FRC-ATT-2025].
- **IFIAR and others.** Keep auditors in control; consult regulators early where AI decides without a human; define
  "human-led" [IFIAR-TTF-2025; IFIAR-TTF-2026]. AFM: auditors do not always verify input-data reliability, especially
  with ineffective IT general controls [AFM-12BB-2025]. IRBA: add procedures to verify authenticity [IRBA-AI-2024].
  CPAB (2025 inspections): tools used as primary evidence with limited input validation; one tool left "low-risk" items untested (`#08`) [CPAB-EVOLVING-2025].

**Design guardrails seen in deployments and guidance**
- Rules-based routines and deterministic code alongside models (FRC; Ledgerline's CEO); certification per use case
  and version control so only the approved version runs (FRC; DataSnipper); client data kept out of model training (FGMK).
- Every result traced to its source; agents stop at major steps for review (DataSnipper, Fieldguide, Caseware).
- Shadow mode before cutover and with-and-without runs (Ledgerline; Buzzacott); on file, that a tool was used, why
  use criteria were met, items selected and follow-up done (FRC); corroborate key documents against bank data.

**Steps that stay with a person:** judging whether tool output is persuasive enough to reduce or replace a sample;
population completeness; investigating flagged items and deciding what is a misstatement; judging document
authenticity; estimates and complex revenue; control of confirmations; sign-off.

## 8. Roles and how they evolve

- **Testers become exception investigators.** RSM Australia and Ledgerline describe time moving from selecting and
  ticking to investigating exceptions [RSM-AUS-2026; LEDGERLINE-CPAPA-2026].
- **Preparer, reviewer and QC agents.** FGMK splits agents by role and controls who builds them (`#11`); central
  methodology teams own certification and calibration in the FRC example.
- **Hiring shifts.** KPMG's audit chief digital officer would not hire a graduate to create workpapers
  [CTRLCOUNCIL-WSJ-2026]; PwC hires engineers and dual-track CPA and data-science recruits [PWC-AT-2025]. AI-skilled
  roles were almost 7% of Big Four postings in 2025 against just under 3% for audit roles [COMPUTERWORLD-FT-2026].
- **Juniors.** Upside: Sanville's first-years now do complex revenue testing. Risk: the PCAOB's acting chair said firms
  and educators may need new paths for juniors to build foundational skills [NYSSCPA-BOTIC-2025]; the Thomson Reuters
  Institute urges structured development as work is automated [TRI-FOP-2026]. Deloitte adds "tutor mode" (`#22`).

## 9. Frontier

- **2025-10-28** PwC expects a tool for every audit step in 2026; PwC Australia pilots an AI-native audit (5 clients,
  all by 2028) [PWC-AT-2025; PWCAU-AT-2025]. **2025-12-15** PCAOB amendments apply (fiscal years beginning on or after).
- **2026-03-16 / 03-30** IAASB approves the inventory and confirmations project; FRC issues agentic AI guidance
  [IAASB-500SERIES-2026; FRC-GENAI-2026].
- **2026-04-07 / 04-10** EY: agents in all phases, end-to-end by 2028; WSJ: KPMG orchestration pilot in summer 2026,
  routine testing with no human team in two to three years, EY agent-to-agent pilots [CPAPA-EY;
  CTRLCOUNCIL-WSJ-2026]. **2026-04-20** IFIAR: firms plan agentic AI orchestrating many audit activities [IFIAR-TTF-2026].
- **2026-05-21 to 06-29** Rabobank and BDO NL direct bank data; Fieldguide orchestrator; Deloitte Omnia agents; BDO UK
  expands MindBridge [CIRCIT-CS-BDONL-2026; FIELDGUIDE-ORCH-2026; DELOITTE-OMNIA-2026; MINDBRIDGE-BDOUK-2026].
- **2026-07-13 / 08-19** SAS No. 150 and No. 151 published. **2026-08-05** IAASB exposure drafts [IAASB-ED500-2026].
- **2026-09-22 / 09-26** DataSnipper Alwin and MindBridge agentic risk assessment; FinancialAuditBench published
  [DATASNIPPER-ALWIN-2026; MINDBRIDGE-ARA-2026; ARXIV-FAB-2026].
- **2026-10-07 / 10-14 / 10-15** PwC: savings "not that drastic yet"; AICPA practice aid reported (more on evidence promised);
  Ledgerline warns against selling "we test everything" [CFODIVE-PWC-2026; AT-AICPAPA-2026; LEDGERLINE-CPAPA-2026].
- **2026-12-15** ISA 240 (Revised) effective; IAASB comment deadline. A Thomson Reuters executive expects adoption to
  hit a "hockey stick curve" at some point [TR-STATE-2026]. **2028-12-15** SAS No. 150 and No. 151 effective.

## 10. Common objections

- **"AI can't find fraud; it is too rare."** Partly fair: pattern tools struggle with rare events, so pair them with
  fraud specialists and rules [NYENRODE-2026; FRC-AIAUDIT-2025]. Ask for flag-to-misstatement rates.
- **"If we test everything, we can promise more."** No. Reasonable assurance still applies, specific-item results
  cannot be projected, and "we test everything" widens the expectation gap (`#24`, `#25`).
- **"The savings figures are hype."** Mostly true: single named cases published by vendors, and PwC calls its own
  savings modest. Run in shadow mode and measure your own time per selection and override rate.
- **"Regulators will penalise us."** None prohibits AI and the PCAOB amendments are in force; the FRC says outputs
  need not match the persuasiveness of the procedure replaced if not overstated. The risk is documentation and data.
- **"LLMs give a different answer each time."** RSM UK's analytics director suggests a rules-based tool alongside AI
  [ICAEW-FRCVIEW-2026]; Ledgerline's CEO advises pairing agents with deterministic code.
- **"Documents can be faked now, so matching is worthless."** Matching still helps but must be corroborated:
  authenticated or direct-access confirmations, bank and vendor data (`#04`, `#17`).
- **"Small firms can't afford this."** A PIA Group leader says the business case "just doesn't hold up" for a firm of
  fifty [NYENRODE-SHIFTS-2026]; yet Sanville (about 20 people) and Oberlander's owner report gains.
- **"Clients will demand lower fees."** A secondary report says KPMG pressed its auditor, Grant Thornton UK, for a fee
  cut because of AI and got about 14% [THEFINANCESTORY-KPMGFEE-2026]; Sanville reports realisation rising instead.

## 11. Sources

Full details (title, publisher, type, URL, date, access, locator) are in the YAML.
- **Regulators and standard-setters:** IFIAR-TTF-2025, IFIAR-TTF-2026, IFIAR-SURVEY-2026, PCAOB-TAA-2024, SEC-TAAORDER-2024,
  PCAOB-PS2025-004, PCAOB-CONFIRM-2023, PCAOB-GENAI-2024, FRC-AIAUDIT-2025, FRC-GENAI-2026, FRC-ATT-2025, IAASB-ED500-2026,
  IAASB-ED520-2026, IAASB-ED330-2026, IAASB-EDOVERALL-2026, IAASB-500SERIES-2026, AFM-12BB-2025, IRBA-AI-2024, CPAB-EVOLVING-2025.
- **Firms and press:** KPMG-CLARA-2025, ACCTODAY-KPMG-2025, PWC-AT-2025, CFOBREW-PWC-2025, CFODIVE-PWC-2026, PWCAU-AT-2025,
  CPAPA-EY, ACCTODAY-EY-2024, DELOITTE-OMNIA-2026, CONS-GT, CTRLCOUNCIL-WSJ-2026, BUZZACOTT-PRIME-2025,
  RSM-AUS-2026, DELOITTE-NL-SAMPLE-2026, KPMG-SOX-2026, LEDGERLINE-CPAPA-2026, LEDGERLINE-SITE-2026, AT-AICPAPA-2026,
  JOFA-SAS150-2026, JOFA-APFRAUD-2026, JOFA-EXCELAGENT-2026.
- **Vendors:** TR-AGENTIC-2025, TR-STATE-2026, TR-BANKCONF-2026, TR-BANKSTATE-2026, DATASNIPPER-CONNECT-2026, DATASNIPPER-FGMKEXCEL-2026, DATASNIPPER-FGMK-2026, DATASNIPPER-ALWIN-2026,
  DATASNIPPER-PRODUCTIVITY-2026, DATASNIPPER-CHILE-2026, DATASNIPPER-ODP-2026, DATASNIPPER-PAYABLES-2026, FIELDGUIDE-SANVILLE-2026, FIELDGUIDE-FIELDAGENTS-2025,
  FIELDGUIDE-ORCH-2026, FIELDGUIDE-CHERRY-2026, MINDBRIDGE-BDOUK-2026, MINDBRIDGE-KPMG-2024, MINDBRIDGE-CHERRY-2022, MINDBRIDGE-ARA-2026, MINDBRIDGE-FAKEINV-2025,
  CIRCIT-MOORE-2026, CIRCIT-BEEVER-2026, CIRCIT-CROWE-2026, CIRCIT-KRESTON-2026, CIRCIT-CS-BDONL-2026, CASEWARE-AIDA-2026.
- **Academic, surveys, professional bodies:** ARXIV-AUDITCOPILOT-2025, ARXIV-FAB-2026, GRACZYK-2025, CHRIST-DRONE-2021,
  EY-DRONE-JOFA-2018, COMMERFORD-2022, ICPAS-PEECHER-2026, NYENRODE-2026, CPACOM-ATR-2025, ISACA-EVIDENCE-2026,
  ICAEW-FRCVIEW-2026, ICAEW-PIERPOINT-2025, CAQ-GENAI-2024.
- **Not in the YAML (cited in this module only):**
  - SAS-ACFE-2026: SAS with ACFE, *2026 Anti-Fraud Technology Benchmarking Report* release, 2026-03-25, https://www.sas.com/en_us/news/press-releases/2026/march/acfe-anti-fraud-technology-study-deepfakes.html
  - IIA-AIFRAUD-2026: Internal Audit Foundation with Optro, *Internal Audit and AI-Enabled Fraud*, 2026-02-17, https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf
  - JOFA-SAS151-2026: Journal of Accountancy, *ASB approves standard on auditors' responsibilities relating to fraud*, 2026-08-20, https://www.journalofaccountancy.com/news/2026/aug/asb-approves-standard-on-auditors-responsibilities-relating-to-fraud/
  - IAASB-ISA240-2025: IAASB, *IAASB Revises Fraud Standard to Enhance Public Trust*, 2025-07-08, https://www.iaasb.org/news-events/2025-07/iaasb-revises-fraud-standard-enhance-public-trust
  - COMPUTERWORLD-FT-2026: Computerworld (reporting an FT analysis of job postings), 2026-05-19, https://www.computerworld.com/article/4173296/the-big-four-accounting-firms-are-now-hiring-more-ai-specialists-than-accountants.html
  - TRI-FOP-2026: Thomson Reuters Institute, *Future of Professionals 2026: tax and audit*, 2026-07-21, https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
  - NYSSCPA-BOTIC-2025: NYSSCPA, *PCAOB's Botic Flags Opportunities and Risks in AI*, 2025-12-10, https://nysscpa.org/news/1051584-pcaobs-botic-flags-opportunities-and-risks-in-ai-2025-12-10
  - NYENRODE-SHIFTS-2026: Nyenrode, *AI isn't just speeding up accounting, it's changing it fundamentally*, 2026-05-19, https://www.nyenrode.nl/en/news/n/ai-accounting-changing-fundamentally
  - THEFINANCESTORY-KPMGFEE-2026: TheFinanceStory (secondary report of FT and Going Concern items), 2026-02-12, https://thefinancestory.com/kpmg-forced-auditor-for-a-14-ai-discount-will-the-billable-hour-die
