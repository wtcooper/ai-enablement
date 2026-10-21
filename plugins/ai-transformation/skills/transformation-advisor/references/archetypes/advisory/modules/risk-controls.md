# Risk and controls advisory (advisory)

Last reviewed 2026-10-21 (source-verified). Use cases live in `../use-cases/risk-controls.yaml` (24 entries). Ids
are shortened: `#05` means `advisory-risk-controls-05`; other archetypes' ids are in full. Source keys in brackets, such
as [KPMG-SOX2030-2026], are listed in §10 and given in full in the YAML. No entry is graded A: every outcome figure is
vendor-published or self-reported, and nobody has published an error rate, override rate or parallel-run result for AI
in internal audit or SOX work. Say so when you quote a figure.

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

Risk and controls work that accounting and advisory firms sell, mostly to private middle-market companies:
outsourced and co-sourced internal audit, SOX readiness and testing (SOX: the US law requiring public companies to
test internal control over financial reporting, ICFR), third-party and enterprise risk, and the new line of advising
clients on governing their own AI. It also covers what clients' in-house audit teams now do with agents, because that
sets what they will buy. Issuing SOC reports and certifying AI systems is attest work in the assurance archetype; the
firm's own pricing, quality control and staffing are in professional-services.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Risk assessment and audit planning | Interviews, external risk scan, planning memo, work program | research-synthesis, expert-judgment | Starts from a blank page; AI use is heaviest here, but Gartner says it is not generally transforming processes |
| SOX scoping, RCM and control design | Build the risk and control matrix (RCM: risks linked to the controls that address them), narratives, attributes | document-production, expert-judgment | A first RCM takes one to two days (RSM); vague attributes and exception rules break agents (Riveron) |
| Test design and evidence requests | Test steps, sample sizes, requests to control owners ("provided by client", PBC), chasing | coordination-scheduling, document-production | About 1 in 5 requests wrong first time (a vendor CEO's unsourced estimate) [CPAPA-5Q-2026]; email and spreadsheet tracking |
| Control testing, including IT general controls (ITGCs: access, change, operations) | Match evidence to samples, test each attribute, write the workpaper | review-assurance, transaction-processing | 16 testing hours per control in FY2024, up from 12 in FY2022; SOX control cost up 45% between KPMG's 2023 and 2025 surveys [KPMG-SOX2030-2026] |
| Review and deficiency evaluation | Workpaper review; is it missing support or a true exception; severity | review-assurance, expert-judgment | Review bottleneck; AI flags false exceptions where practice is undocumented [GT-INFERENCEGAP-2026] |
| Reporting and remediation | Observations (detail, root cause, impact, recommendation), audit committee, follow-up | document-production, coordination-scheduling | Slow, varies by author |
| Third-party and SOC report review | Read vendors' SOC reports, map gaps to contracts and the customer's own controls | review-assurance, research-synthesis | Reports may say little about AI components [CPAPA-AGENTSCLOSE-2026]; IIA Third-Party Topical Requirement in force from 2026-09-15 |
| Enterprise risk management (ERM) | Risk registers, monitoring, board reporting | research-synthesis, data-reporting | Baker Tilly's "signal gap"; no named AI deployment found |
| Advising clients on their own AI | Inventory, ownership, control design, monitoring, certification readiness | expert-judgment, review-assurance | Use outruns control: active AI use in finance 75%, only 29% track where it fails [KPMG-AIFINANCE-2026] |

Capacity context: 52% of internal-audit departments spent over 40% of their hours on SOX in FY2024, and 28% of companies
used outsourced providers for SOX testing [KPMG-SOX2030-2026]. Before any of these steps, ask who the client is: the
same service can be restricted for a firm's own audit client (§6).

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or sourcing model changes). Improve is dense;
delegate rests on vendor-published cases; automate has one firm description (C) and one adjacent academic case (C).

**Planning and risk assessment**
- Improve: `#01` assistive pre-planning research, walkthrough notes and starting risk scores (polls only: 60% use genAI
  for pre-planning). `#02` board-material and risk-register signals turned into audit actions between planning cycles
  (Diligent, announced; continuous ERM sensing is an idea).

**Control design, evidence and testing**
- Improve: `#03` RCMs, narratives, test procedures and request lists drafted for review (RSM in user testing; Grant
  Thornton CompliAI). `#04` request drafting, completeness checks and follow-up in a co-sourced audit (Baker Tilly).
- Delegate: `#05` in-house teams hand test execution to agents (Reddit: 175 controls in three months, -60% time per
  control, vendor-published). `#06` firms run agentic testing in co-sourced and outsourced engagements (RSM Beacon live;
  Riveron; Protiviti with Fieldguide; PwC's 30-40% claim).
- Automate the flow: `#07` 100% of a control population instead of a sample (Armanino). `#08` year-round testing instead
  of one cycle (Klaviyo). `#09` first-line continuous monitoring with human-approved auto-clear rules (C; self-healing
  controls are an idea).

**Review and reporting**
- Improve: `#10` AI pre-review and challenge of workpapers, scope and draft findings (FJ Management, Baker Tilly).
  `#11` observation drafting (RSM; 60% of polled auditors draft issues with genAI).

**Third parties**
- Improve: `#12` reading vendors' SOC reports and vendor AI risk; agent support announced (KPMG framework, Optro).

**Delivery and sourcing model**
- Reinvent: `#13` one agentic platform for internal-audit, ISO, HITRUST and PCI work (Aprio, Cherry Bekaert, Baker Tilly).
  `#14` Havertys moves outsourced IT SOX testing to agents. `#15` AI-native vendors sell agent-run SOX testing direct
  (Petual, named customer Navan). `#16` SOX teams repositioned as controls advisers (KPMG, practitioner panel).

**Client AI (the growth line)**
- Reinvent: `#17` AI governance, control design and certification-readiness advisory (COSO roadmap, AIUC-1 readiness).
  `#19` internal-audit review of a client's AI governance (Grant Thornton for a global bank, the one named case).
- Improve: `#18` AI inventory, shadow-AI discovery, review of user-built automations. `#20` SOX scoping of AI inside
  business controls. Ideas: `#21` written controls before finance agents go live; `#23` AI-enabled fraud readiness.
- Automate: `#22` confidence-threshold routing, low-confidence items to a person (C; academic data, unnamed bookkeeper).

**The firm's own testing tools**
- Improve (idea): `#24` certify AI testing tools with a parallel run and recertify after vendor changes.

Coverage: the set spans assist to delegate and step, process and model. No evidence was found for automate at model
level, assist at process level or any delegate step. Covered elsewhere, not duplicated: Microsoft's ITGC test agent
(`assurance-controls-testing-06`), citation checks before issue (`professional-services-quality-review-04`), AI-use
records on file (`professional-services-quality-review-03`), AI terms in engagement letters
(`professional-services-scoping-pricing-07`), synthetic-data stress tests (`assurance-controls-testing-25`), AIUC-1 and
ISO/IEC 42001 certification (`assurance-assurance-over-ai-19`, `assurance-assurance-over-ai-15`).

## 4. Interview probes

Ask in the person's setting: provider (outsourced or co-sourced internal audit, SOX), client CAE (chief audit
executive) or SOX lead, or a client buying AI governance help.

1. **"Walk me through one key control from evidence request to sign-off. Where do the hours go?"** Reveals the baseline
   against 16 hours per control and whether the pain is chasing (`#04`), testing (`#05`, `#06`) or review (`#10`).
2. **"Which tests does an agent run first today, and what did you compare it with before trusting it? Do you track
   reviewer overrides or rework?"** Reveals whether any quality evidence exists; no published source has it (`#24`).
3. **"Does every control have written attributes, evidence requirements and exception rules?"** Reveals readiness;
   Riveron says many programs define these less precisely than agents need.
4. **"When an agent reports an exception, how do you tell a missing document from a failed control, and who decides?"**
   Reveals inference-gap risk and whether deficiency evaluation stays human.
5. **"Has the external auditor said what it will rely on when AI prepares or executes tests, and is that written
   down?"** Reveals the biggest open risk; in an informal poll, uncertainty (48%) led [IAC-SOXRELIANCE-2026].
6. **Provider: "What is your agent plan, and do you expect client testing spend to fall, stay flat or move to advisory?"
   Client: "What did you bring in-house first?"** Reveals sourcing pressure (`#14`, `#15`).
7. **"Which of your advisory clients are also audit clients, under which regime, and who signs off a new service?"**
   Reveals independence readiness; listen for a system rather than memory.
8. **"Which of your (or your clients') AI uses can you list today, who owns each, and has the auditor asked?"** Reveals
   inventory and shadow-AI gaps (`#18`, `#20`).
9. **"When AI is audited, do you test whether it works, or only whether it is governed?"** Reveals the safe-versus-
   effective gap: only 53% of those auditing AI review operational effectiveness (`#19`).
10. **"What happens when the vendor updates the model?"** Reveals recertification, rollback and monitoring (`#24`).
11. **"Where does client data go when your people use AI, and what do engagement letters say?"** Reveals
    confidentiality exposure; 34% of professionals use AI their organisation has not approved [TR-FOPREPORT-2026].
12. **"How do juniors learn the work if AI drafts the RCM, the request list and the first findings?"** Reveals pipeline
    risk; route detail to professional-services.

## 5. Metrics and benchmarks

**Baselines to ask for first**
- Testing hours per control: 16 (FY2024), 12 (FY2022); SOX control cost +45% (2023 to 2025 KPMG surveys); 58% said
  outsourced providers were over 20% of SOX budget, denominator unclear [KPMG-SOX2030-2026].
- IT-related material weaknesses: 31% (2021) to 58% (2025), KPMG study as cited [KPMG-IPO-2026].
- About $2.3M a year: Midship (vendor) calls it SOX audit-services spend; a vendor CEO calls it KPMG's 2025 average SOX
  program cost [CPAPA-5Q-2026]. Do not quote it as audit fees `#15`.

**Named outcomes (vendor-published or self-reported; effort, not quality)**
- Reddit: 175 controls (over 40% of SOX scope) in three months; -60% testing time per control; later over 75% of SOX
  controls on agentic testing `#05`.
- Microsoft finance: 850 hours and $185K a year from a two-agent ITGC change-management tester launched in 1-3
  months; method not stated [MSFT-SOXAGENT-2026].
- Armanino: 100% of vendor bank-detail changes tested instead of 1 in 25; about 25+ hours saved on one reconciliation
  (an estimate) `#07`.
- RSM: first-draft RCM in minutes versus one to two days (a director's statement) `#03`.
- Grant Thornton for a bank: seven governance domains under audit, 100+ production AI use cases validated `#19`.

**Vendor claims (grade C; ask for named, measured cases)**: PwC 30-40% less testing effort `#06`; Diligent about 70%
less audit administration, 120 hours to 35, unnamed adopters, plus one named customer (Crown Castle) recalling "more
than half" less evidence chasing `#04`; Petual says customers "can achieve" 68-80% efficiency `#15`; Andera 70% `#15`.

**Adoption and readiness (self-selected polls and sponsored surveys)**
- Gartner poll of 743 audit professionals: 93% use some AI; 60% use it for pre-planning, 60% for drafting issues or
  reports, 30% for testing, 12% for QA reviews [ACCTIMES-GARTNER-2026]. 38% have an AI strategy (press reports differ
  on the base: 743 polled or 161 CAEs); 54% of 142 CAEs have not started measuring AI value [HELPNET-GARTNERIA-2026].
- KPMG webcast (about 3,900 leaders): 33% use AI mainly for research, planning and scoping; about 28% for large data
  sets; 51% of SOX and internal-audit functions at 'some pilots or just starting' [KPMG-FUTURESOX-2026].
- Sikich (222 US audit leaders): 90% use AI; 77% of plans include AI assessments; 82% use external partners
  [SIKICH-IAPRIORITIES-2026]. Wolters Kluwer poll: 17.7% have a formal AI program or broad adoption [CPAPA-IAPOLL-2026].
- Client side: KPMG (1,013 finance leaders, revenue at least $250M): 42% fully assurance-ready; assurance-ready firms
  report error-reduction improvement 33% versus 6% [KPMG-AIFINANCE-2026]. Grant Thornton (950 leaders): 78% lack strong
  confidence they could pass an AI governance audit in 90 days [GT-AISURVEY-2026]; PE leaders: 9% very confident `#17`.
  RSM (1,030 US and Canadian middle-market senior leaders): 67% apply governance controls before pilot or production;
  40% of those raising AI spend take budget from external consulting [CPAPA-RSMMM-2026].
- Agent risk: 34% acted on an inaccurate agent output; 38% let agents approve or reject transactions; 9% redesigned
  workflows (Optro survey of 417) [OPTRO-AGENTICREPORT-2026]. 63% have no formal AI risk appetite or governance
  framework; 28% are confident auditing AI risks [AUDITBOARD-FOCUS-2025].

**Quality evidence: absent for this module.** The nearest independent measures are adjacent: legal AI research tools
hallucinated 17-33% of the time [STANFORD-LEGALAI-2024]; consultants were 19% less likely to be correct on a task
outside AI's frontier [HBS-JAGGED-2023]; the best model scored 64.37% on Vals AI's Finance Agent benchmark (SEC-filing
research, 2026-06-04) [VALS-FAB-2026]; accountants following divergent AI suggestions on uncertain items risked errors
`#22`.

**What to measure (recommend these, not hours alone)**: hours per control before and after; reviewer override and
rework rates; whether a parallel run catches the same exceptions; false-exception rate; request turnaround and
duplicate requests; cycle time to a final workpaper; time to escalate issues; remediation closed; AI-use inventory
coverage. Baker Tilly warns that speed alone is a poor measure [BAKERTILLY-AIIA-2026].

## 6. Guardrails

**Frameworks and guidance (no body forbids AI; none sets a numeric quality bar)**
- **COSO** (23 Feb 2026): internal control over generative AI on the 2013 framework; eight capability types, a six-step
  roadmap (govern, inventory, assess, design, implement, monitor), starter metrics; guidance, not a rule [COSO-GENAI-2026].
- **IIA**: AI Auditing Framework (2024-09-13); board and audit-committee AI questionnaires (2026-06-16) [IIA-AIFW-2024;
  IIA-IPPF-2026]. Topical Requirements: Cybersecurity from 2026-02-05, Third-Party from 2026-09-15, Organizational
  Behavior from 2026-12-15 [BAKERTILLY-GAM-2026].
- **AICPA**: practice aid on AI for financial-statement auditors (2026-10-13; more guidance to follow)
  [JOFA-AIPA-2026]; TQA 9561 on a service organisation's AI in SOC 1 and SOC 2 (by 2026-09-21) [DART-TQA9561-2026].
  The Code's confidential-client-information rule means asking whether client consent is needed before client data goes
  into an AI tool [JOFA-ETHAI-2026].
- **PCAOB**: no AI-specific standard found; 2024 staff outreach heard that GenAI work gets the same supervision
  [PCAOB-GENAI-2024]. **UK FRC** (2026-03-30): certify a tool per use case, test edge cases, recertify after change; the
  human stays accountable [FRC-GENAINEWS-2026; FRC-GENAI-2026]. A useful model for US advisory, not binding on it.
- **Other**: NIST AI RMF (the bank case aligned to it, `#19`) [NIST-AIRMF-2024]; DOJ asks how a company manages AI risk
  and "what baseline of human decision-making is used to assess AI" [DOJ-ECCP-2024]; the EU AI Omnibus (Regulation (EU)
  2026/1744, OJ 2026-07-24) moves stand-alone high-risk duties to 2027-12-02 [CUATRECASAS-AIOMNIBUS-2026].

**Independence (follows the client, not the service line)**
- SEC Rule 2-01(c)(4) bars, for SEC audit clients, internal-audit outsourcing on accounting controls (v) and
  financial-system design (ii) unless results will not be subject to audit procedures, and management functions
  including ongoing monitoring (vi) with no such exception; contingent fees are barred (c)(5) [SEC-RULE2-01-2026]. SEC
  staff hold a rebuttable presumption that such work will be subject to audit procedures [PWC-SECFAQ-2019].
- Private middle-market clients are often non-SEC, so AICPA rules apply: the client must take management
  responsibility, with a skilled overseer and a written understanding (2016 description) [JOFA-NONATTEST-2016]. The
  AICPA says building or hosting an AI system for an attest client can raise concerns [JOFA-ETHAI-2026]; IESBA treats
  hosting an audit client's data as a management responsibility [IESBA-TECHREV-2023]. No AI-specific ruling exists.
- Firms in alternative practice structures (attest firm plus a separately owned advisory arm: Baker Tilly, Grant
  Thornton [BAKERTILLY-AIIA-2026; GT-CBIZ-2026]) face a rule in flux; the AICPA ethics committee was still discussing a
  second exposure draft in August 2026 [JOFA-PEEC-2026]. Route ownership questions to professional-services.

**Design guardrails seen in deployments**
- Reviewer on every conclusion; ambiguous items routed as open items; reasoning log beside evidence (`#06`).
- "Missing support" and "true exception" as separate outcomes; a controls clean-up before agents (`#06`).
- Retain procedure, source data, AI output, exceptions, review and sign-off (`#04`); client data segregated, not used to
  train vendors' models (RSM Beacon).
- Human-approved auto-clear logic and segregation of duties (`#09`); parallel run and recertification (`#24`).
- First line owns monitoring; internal audit tests the monitoring and never designs then assures the same AI
  governance (`#08`, `#19`). Watch for instructions hidden in evidence aimed at testing agents [KPMG-SOX2030-2026].

**Steps that stay with a person**: scope and risk ratings; deciding evidence is sufficient; missing support versus
failure; deficiency severity; reliance on vendor reports; approving auto-clear rules; fraud conclusions; sign-off.

## 7. Roles and how they evolve

- **Preparer to supervisor.** RSM treats its agent as a digital employee that can make intern-like mistakes; auditors
  queue controls and review completed ones (`#03`, `#06`). Riveron's teams spend more time on review, challenge and
  exception analysis.
- **Tester to controls adviser.** KPMG's SOX leader says "the concept of auditor reliance is going to go away" (`#16`);
  two-thirds of polled SOX leaders were asked to add value in operational and technology audits [IAC-SOXCHANGE-2026].
- **New skills.** KPMG says auditing a language model is not core CPA training [KPMG-SOX2030-2026]; RSM's AI-risk
  posting asks for Python and GenAI skills and AAIA, AAISM or AIGP certifications `#17`. The hardest hire is someone
  who is both auditor and technologist [SIKICH-IAPRIORITIES-2026].
- **Identity.** Jones Lang LaSalle's CAE says auditors who built careers on well-crafted workpapers must accept handing
  that work to technology [IIA-UPSKILL-2026].
- **Staffing signals.** Functions reporting staff cuts rose from 11% (2024) to 18% (2025); 11% to 28% at privately held
  ones (n = 29); the Pulse cites budgets, not AI [IIA-PULSE-2026]. Juniors overseeing AI too early may approve bad output
  [ICAEW-VOICES-2026]; the FRC names erosion of human knowledge as a risk it did not address [FRC-GENAI-2026].
- **Provider spend.** Havertys expects outside spend to move from testing hours to advisory (`#14`).

## 8. Frontier

- 2026-01-27: Midship raises a $4.15M seed for agentic SOX testing `#15`.
- 2026-02-23: COSO publishes its generative-AI control guidance [COSO-GENAI-2026].
- 2026-03-03 and 2026-06-03: Protiviti and Cherry Bekaert commit to Fieldguide's agentic platform (`#06`, `#13`).
- 2026-03-09 to 11: the IIA's GAM conference leads on agentic AI in audit [IIA-GAM-2026].
- 2026-03-30: FRC publishes the first audit-regulator guidance on generative and agentic AI [FRC-GENAINEWS-2026].
- 2026-04-24: Petual raises $20M and names Navan as a customer `#15`.
- 2026-08-28: RSM announces Beacon as live for internal-audit control testing `#06`.
- 2026-09-02: Grant Thornton Advisors' CEO expects AI governance demand to grow; CBIZ deal to close Q4 2026 [GT-CBIZ-2026].
- 2026-09-15: IIA Third-Party Topical Requirement takes effect; by 2026-09-21 AICPA TQA 9561 on AI in SOC (`#12`).
- 2026-09-23 and 2026-10-19: Grant Thornton launches AIUC-1 services; AICPA and AIUC announce a joint SOC 2 plus AIUC-1
  engagement, full launch expected early 2027 (`#17`).
- 2026-09-24: KPMG expects the first wave of AI-related material weaknesses in 2027 [KPMG-SOX2030-2026].
- 2026-10-14: Optro extends agentic testing beyond SOX; shadow-AI discovery previews ahead of 2027 (`#05`, `#18`).
- Scheduled, not yet given: ACFE Fraud Conference Canada (2026-11-15 to 17) with a 2026-11-16 session on AI and data
  analytics for ethics and compliance programs [ACFE-CANADA-2026]; IIA Organizational Behavior requirement, 2026-12-15.

## 9. Common objections

- **"The external auditor won't rely on agent-tested work."** Partly true today: practitioners report auditors will not
  rely on pure AI output [IAC-SOXRELIANCE-2026]. KPMG expects external auditors to test full populations themselves,
  shrinking the value of management sampling [KPMG-SOX2030-2026]. Agree evidence expectations in writing first (`#20`).
- **"The vendor promises 70% savings."** Every such figure is vendor-published; none is a parallel-run result. Treat
  match rates as marketing until your data reproduces them [CPAPA-AGENTSCLOSE-2026]; pilot side by side (`#24`).
- **"AI can't make audit judgments."** No deployment asks it to: Accounting Today reports RSM Beacon's AI "does not make
  judgment calls", and every named case keeps a reviewer (`#06`). The risk is weak review: KPMG says a rubber-stamp
  approval is no real control [KPMG-SOX2030-2026]; 34% report acting on a wrong agent output [OPTRO-AGENTICREPORT-2026].
- **"It will flood us with false exceptions."** It can, where practice is undocumented [GT-INFERENCEGAP-2026]; full
  coverage raises exception volume [CPAPA-FULLPOP-2026]. Separate missing support from failure and plan capacity.
- **"Testing everything means nothing is missed."** No: an audit still gives reasonable, not absolute, assurance; say so
  before selling full-population work [CPAPA-FULLPOP-2026].
- **"Independence stops us selling this anyway."** It stops it for your own audit clients; most advisory clients are
  not. But building or hosting AI for an attest client may itself be a new nonattest service [JOFA-ETHAI-2026].
- **"Our clients' AI is governed; they have policies."** Safe is not effective: only 53% of those auditing AI test
  operational effectiveness (`#19`), and 29% of finance leaders track where AI fails [KPMG-AIFINANCE-2026].
- **"Agents will take our co-sourcing revenue."** Some will: Havertys starts with work it outsourced (`#14`) and vendors
  sell direct (`#15`). Firms are responding by running agents in their own delivery (`#06`) and moving to AI governance
  work, where demand is claimed but unmeasured [GT-CBIZ-2026].

## 10. Sources

Full details (publisher, URL, date, locator) are in the YAML. Keys cited here but not in the YAML are marked *; their
details come from the wave-5 research files (practice, discourse, governance, independence-pricing, disruption).

- Firms: KPMG-SOX2030-2026, KPMG-FUTURESOX-2026, KPMG-IPO-2026, KPMG-AIFINANCE-2026, GT-INFERENCEGAP-2026,
  GT-AISURVEY-2026, GT-CBIZ-2026 (Bloomberg Law), BAKERTILLY-AIIA-2026, BAKERTILLY-GAM-2026, MSFT-SOXAGENT-2026*
  (Microsoft, FY26 innovation story, 2026).
- Surveys and polls: ACCTIMES-GARTNER-2026, HELPNET-GARTNERIA-2026, SIKICH-IAPRIORITIES-2026, CPAPA-IAPOLL-2026,
  CPAPA-RSMMM-2026, OPTRO-AGENTICREPORT-2026, AUDITBOARD-FOCUS-2025* (AuditBoard/Optro, 2025-11-12), IIA-PULSE-2026*
  (Internal Audit Foundation, 2026-02), TR-FOPREPORT-2026* (Thomson Reuters report page, 2026-06-22).
- Community and press: IAC-SOXCHANGE-2026, IAC-SOXRELIANCE-2026, CPAPA-5Q-2026, CPAPA-AGENTSCLOSE-2026,
  CPAPA-FULLPOP-2026, ICAEW-VOICES-2026* (ICAEW, 2026-06-10).
- Standard-setters, regulators, professional bodies: COSO-GENAI-2026, IIA-AIFW-2024, IIA-IPPF-2026, IIA-GAM-2026,
  IIA-UPSKILL-2026, JOFA-AIPA-2026, DART-TQA9561-2026, JOFA-ETHAI-2026, PCAOB-GENAI-2024, FRC-GENAINEWS-2026,
  FRC-GENAI-2026, SEC-RULE2-01-2026, DOJ-ECCP-2024, NIST-AIRMF-2024* (NIST, 2024-07-26), CUATRECASAS-AIOMNIBUS-2026*
  (Cuatrecasas, 2026-07-24), PWC-SECFAQ-2019* (SEC staff FAQ via PwC Viewpoint, 2019-06-27), JOFA-NONATTEST-2016*
  (Journal of Accountancy, 2016-11), IESBA-TECHREV-2023* (IESBA, 2023-04-11), JOFA-PEEC-2026* (Journal of
  Accountancy, 2026-08-10), ACFE-CANADA-2026* (ACFE, scheduled 2026-11-15).
- Academic and benchmarks: STANFORD-LEGALAI-2024* (arXiv, 2024-05-30), HBS-JAGGED-2023* (HBS, 2023-09),
  VALS-FAB-2026* (Vals AI leaderboard, read 2026-10-21; leaderboard dated 2026-06-04).
