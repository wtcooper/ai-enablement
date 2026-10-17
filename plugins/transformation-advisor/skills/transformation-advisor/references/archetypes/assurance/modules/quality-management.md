# Quality management (assurance)

Last reviewed 2026-10-17; sources checked 2026-10-17. Use cases live in `../use-cases/quality-management.yaml` (25
entries). Ids are shortened here: `#07` means `assurance-quality-management-07`; other modules' ids
are in full. Source keys in brackets, such as [FRC-GENAI-2026], are in the YAML or in §10.
**No outcome in this module is measured.** No firm or regulator has published an error rate, override rate or
parallel-run result for AI tools or for review of their output. Say so whenever quality is discussed.

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

How an audit firm keeps quality under control when its people use AI. **Part A, firm level:** governing AI tools
inside the firm's system of quality management under ISQM 1 (the international quality-management standard) and
PCAOB QC 1000 (its US public-company counterpart): approve and certify each tool, control access, monitor its
effect on quality, recertify when it changes, and resource and train people. **Part B, engagement level:** how
partners and reviewers direct, supervise, review and document AI output on an audit (ISA 220 (Revised)), including
automation bias (over-trusting fluent machine output) and dealings with inspectors. AI here is mostly the thing
being governed; few use cases have AI doing quality-management work itself.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| **A. Firm level** | | | |
| Needs and business case | Ideas come top-down and bottom-up; a business case before build or buy | coordination-scheduling, expert-judgment | The six global networks report about 30% more AI-enabled tools in 2025 (firm-reported) [IFIAR-TTF-2026] |
| Select, build, vendor due diligence | Network-built tools preferred; foundation models generally third-party | software-systems, review-assurance | Training data and model logic cannot be inspected; small firms depend on vendors |
| Certify per use case | Test inputs, architecture and outputs; methodology sign-off; supporting IT controls | review-assurance | Processes built for deterministic tools; only 2 of 6 UK firms recorded tool limitations [FRC-ATT-2025] |
| Deploy and control access | Pilots (some on lower-risk non-PIE audits), inventory, version control, blocking | software-systems | Firms generally did not monitor that only authorised, current tools were used [FRC-ATT-2025]; over a third of surveyed tax and audit professionals admit unauthorised AI [TRI-FOP-2026] |
| Policy, methodology, training | Permitted uses, prompt libraries, role-based training | document-production, coordination-scheduling | 66% of 54 surveyed US CPA firms rank untrained staff a top blocker [CPACOM-ATR-2025] |
| Monitor, recertify, retire | Usage and impact metrics, change triggers, owner confirmations | data-reporting, review-assurance | 0 of 6 UK firms quantified quality impact; triggers informal [FRC-ATT-2025] |
| Resource engagements | Match competence, capacity and time | coordination-scheduling | Human-resources findings at 24% of inspected member firms in 2025 [IFIAR-SURVEY-2026] |
| Remediate; annual evaluation; inspectors | Root-cause analysis, system evaluation, regulator dialogue | expert-judgment, client-interaction | Monitoring and remediation findings at 32% of firms; 21 findings for missing issues in internal inspections (6 in 2024) [IFIAR-SURVEY-2026] |
| **B. Engagement level** | | | |
| Plan AI use | Partner sets expectations; confirms tools are approved | coordination-scheduling | Teams use AI the partner has not planned or reviewed |
| Direct and supervise | Competent staff; configure tools within policy | coordination-scheduling | Some firms' supervision policies unchanged after GenAI (2024 outreach) [PCAOB-GENAI-2024]; 31 supervision-policy findings in 2025 (10 in 2024) [IFIAR-SURVEY-2026] |
| Review output; oversee agents | Check completeness and accuracy; decide at agent control points | review-assurance | Rubber-stamping; fluent output that sounds confident even when wrong [FRC-GENAI-2026] |
| Document AI use | Tool, version, inputs, review, how output informed conclusions | document-production | File does not show where AI was used; generic notes |
| Stand back; communicate | Senior reflection on technology use; audit committee and client terms | review-assurance, client-interaction | Clients' data and model-training concerns |

Inspection context: 35% of inspected listed public-interest-entity audits had at least one finding in 2025 (26% in
2022), and only 11 member firms (9%) had a finding on technological, intellectual and service-provider resources
[IFIAR-SURVEY-2026]. Inspectors are moving to test the firm's system, which makes AI tool governance itself the
inspected object [FRC-SUPERVISION-2026, STARLING-IMC-2026].

## 3. Where AI is changing the work

Lenses: improve (assist or augment), automate (no person on the normal path), delegate (an agent owns a multi-step
outcome), reinvent (`change_scope: model`). **Automate has no evidence in this module.** Delegate has one entry.
Most Part A entries are governance gates run by people (`ladder: assist`, `pattern: other`).

### Part A. Firm-level AI tool governance (lifecycle)

**Certify and approve**
- Improve (process): `#01` certify each tool in a use case, approve through a central board, recertify on triggers
  (model, input or use-case change, performance issues, elapsed time); Deloitte UK Technology Controls Board (Apr 2026).
- Improve: `#02` risk-tiered permitted-use policy, triage and curated prompt library (PwC US, Deloitte UK).
  `#04` evaluation sets and parallel running during limited deployment (FRC says teams "often" do this; no results
  public). `#05` methodology built into tool design; decide how much assurance a tool's output supplies.
  `#06` vendor due diligence and contract terms, scaled for smaller firms.

**Deploy and control**
- Improve: `#03` tool inventory and preventive controls against unapproved or outdated tools.

**Monitor, recertify and govern**
- Improve (process): `#07` monitor quality impact with defined metrics (false-positive/negative rates against a
  manual sample, rework, escalation) and settle network vs member-firm ownership. `#08` board and leadership
  oversight of AI in the quality plan, AI oversight committee, escalation channels (Deloitte UK).
- Improve: `#09` ISO/IEC 42001 certification of the firm's AI management system (KPMG).
- Idea (augment, process): `#14` AI used in the firm's own monitoring and root-cause analysis; the SEC asks about it.

**People and resourcing**
- Improve: `#10` role-differentiated training gated to tool access, plus Deloitte's announced in-workflow "tutor
  mode". `#11` connected resourcing tool (RSM Luca Resourcing; AI role not stated). `#12` firm-approved guidance
  assistant grounded in the firm's manuals (RSM Ask Luca, 4,000+ professionals; Deloitte UK Research Assistant).

**Methodology at scale and inspectors**
- Improve (process): `#16` a 20-person firm (Sanville) pushes standardised programmes on an AI-enabled platform to
  every open engagement the next morning; zero comment forms at its first PCAOB inspection on it (vendor-published).
- Improve: `#13` early engagement with regulators (FRC sandbox) and an inspection-ready file per tool.
- Reinvent (idea): `#15` independent third-party validation of firms' AI tools; the FRC's head of assurance
  technology calls that market "fragmented".

### Part B. Engagement-level supervision and review of AI output

**Plan and supervise**
- Idea: `#17` partner plans AI use at the outset; seniors stand back and review it before sign-off (IFIAR, AICPA).
- Reinvent: `#25` juniors move from preparing to reviewing; supervision and graduate training redesigned (PwC claim).

**Review and oversee**
- Delegate: `#18` human control points in agentic workflows: authorise, escalate, approve before use (Deloitte, KPMG).
- Improve: `#19` review mechanics: citations and run traces, tie-back to source, confirmation gates (AFM good practice).
  `#21` AI review of files for omissions and inconsistencies (Deloitte UK Smart Review, all FTSE audits have access);
  for multi-model secondary review of workpapers at a named internal-audit team see `assurance-controls-testing-10`.
- Ideas: `#20` structured scepticism: independent view first, counter-arguing step. `#22` a second model or rules
  engine cross-checks AI output, human at the end (AICPA permits; duties unchanged).

**Document and communicate**
- Improve: `#23` two-place documentation: central tool record plus structured file record (FRC split; PwC UK policy, second-hand).
  `#24` AI-use terms in engagement letters and audit committee conversations (Grant Thornton UK, Deloitte).

## 4. Interview probes

Ask in the person's setting: firm quality leader, methodology or technology lead, engagement partner or reviewer.

1. **"Walk me through the last AI tool or use case you approved or turned down. Who signed, what test set did you
   use, what failed?"** Reveals whether certification is per use case (`#01`) and whether output testing is real (`#04`).
2. **"What forces recertification: a vendor model update, a new use case, an inspector question? Who spots it?"**
   Reveals whether triggers are formal; the FRC found them generally informal at the six largest UK firms.
3. **"Which uses are pre-approved, which barred, and how do you know staff are not using public chatbots?"**
   Reveals policy tiering (`#02`) and preventive vs detective control (`#03`).
4. **"Beyond licence counts, what do you measure about a tool's effect on quality? Has a number changed a
   decision?"** Reveals the biggest gap (`#07`): no firm has published false-positive, rework or override rates.
5. **"For network-built tools, who monitors them, you or the network, and how do local issues get back?"**
   Reveals fragmented ownership, IFIAR's named risk.
6. **"For one AI-assisted procedure, what exactly does the reviewer look at and how long does it take? How would
   you detect rubber-stamping?"** Reveals whether review is designed (`#19`, `#20`) or improvised.
7. **"For your agentic tools, where are the control points, and who decided them?"** Reveals whether
   "human in the loop" is specified (`#18`); CPAB says a statement alone is not enough.
8. **"If an inspector asked which engagements used which tool version last year, and where AI output sits in each
   file, how long would it take to answer?"** Reveals documentation readiness (`#13`, `#23`).
9. **"What has your regulator asked about AI, and what could you not show?"** Reveals inspection exposure as
   supervisors move to system-level inspection.
10. **"How has supervision and the graduate programme changed since 2024? What do juniors still do by hand?"**
    Reveals deskilling risk and whether `#25` is being addressed.
11. **"Do partners plan AI use at the start of an engagement and review it before sign-off?"** Reveals ISA 220 ownership (`#17`).
12. **Smaller firms: "Which tools are features of products you already buy, and what testing has the vendor shown
    you for your use case?"** Reveals reliance on vendors and the proportionate path (`#06`).

## 5. Metrics and benchmarks

**What exists is inspection and governance data, not AI-quality data.**
- Tool misuse: 31% of IFIAR member regulators reported findings that a tool was not used as intended (2024; 29% in 2023);
  common findings were misread results and thin testing of outliers [IFIAR-TTF-2025].
- FRC, six largest UK firms (snapshot from April 2024 requests; GenAI then limited to chatbots): 0 of 6 quantified
  quality impact; 1 of 6 reported usage against targets; 2 of 6 ran annual owner confirmations; 1 of 6 had a
  three-year recertification backstop; 2 of 6 required UK-level certification of global tools [FRC-ATT-2025].
  A press summary says none "monitored" impact [BOARDAGENDA-FRC-2026]; the FRC's wording is narrower: firms counted usage and were building impact monitoring (`#07`).
- AFM (Dutch study): engagement-level usage estimated for 74% of auditing tools, actual data for 20%, unclear 6% [AFM-12BB-2025].
- IFIAR 2025 firm-level themes (161 member firms inspected): engagement performance 37%, monitoring and remediation
  32%, human resources 24%, EQR 20%, technological resources 9%; 31 supervision-and-review policy findings
  (10 in 2024) [IFIAR-SURVEY-2026]. Per-theme denominators differ and are not stated.
- US: the six networks' average PCAOB Part I.A deficiency rate fell to 13% in 2025 (26% in 2024; 312 audits); no
  source links this to AI [CAQ-INSIDER-2026].
- IRBA: at least 56% of surveyed firms (auditors of listed entities) have or are building an AI governance framework [IRBA-SPA11-2025].
- Scale (self-reported): KPMG Clara AI reaches 95,000+ auditors [KPMG-TR-2025]; Deloitte UK PairD 4,649 active users,
  over 75% of Audit & Assurance staff, about two million prompts a year [DELOITTE-UKTR-2025]; RSM Ask Luca 4,000+ (`#12`).
- Outcomes of note: Sanville 0 comment forms, overhaul under a year vs 18-24 months, realisation $150-200 to $250+
  an hour (vendor-published, adjacent change; `#16`). PwC US: savings "not that drastic yet" after a year [CFODIVE-PWC-2026].
- Research: before generative AI, a one-standard-deviation rise in firms' AI investment was associated with 5.0%
  lower restatement likelihood (36 firms; association only) [FEDYK-2022]. An agent benchmark found frontier models
  sometimes perform inappropriate procedures or write incorrect documentation [ARXIV-FAB-2026].

**What to measure (recommend these; IFIAR lists the first four as emerging practice)**: engagement coverage per
tool; false-positive and false-negative rates against a manual sample; rework rate; escalation incidence; reviewer
override and disagreement rate; parallel-run agreement during limited deployment; time from vendor model change to
recertification; share of files with a complete AI-use record; tool-related internal and external inspection findings.

## 6. Guardrails

**Standards and regulators (none of these bodies prohibits AI or has issued AI-specific QM requirements)**
- **Accountability does not move.** The FRC says people (firms and Responsible Individuals) are accountable for
  audit quality [FRC-GENAINEWS-2026]; NFRA
  staff say technology-generated information has no lower evidentiary bar [NFRA-STAFF-2026].
- **ISQM 1 is the route.** Tools must be appropriately obtained or developed, implemented, maintained and used
  [AUASB-AI-2025, CPAB-AI-2024]; the firm keeps responsibility for approval and monitoring even when the network
  builds the tool [IAASB-TQMPLAN-2026]. IAASB roundtable participants judged ISQM 1 and ISA 220 (Revised) a sound
  base [IAASB-TQM-2026]; the IAASB is drafting a five-guide series through June 2027, with no new requirements
  [IAASB-MINJUN-2026, IAASB-TQMPLAN-2026].
- **PCAOB QC 1000** takes effect 15 Dec 2026. Amendments adopted 9 Sep 2026 (more flexible role assignment, no
  external quality control function requirement for larger firms, narrower cross-engagement evaluation,
  firm-selected evaluation date) take effect with it only if the SEC approves; no approval had been announced by
  17 October 2026 [PCAOB-QCREL-2026, DART-QC1000-2026, EISNER-QC1000-2026]. The PCAOB has no AI standard. Staff say AI
  adoption is an inspection focus [DART-SECPCAOB-2025]; board member Botic expects a lifecycle of approval,
  implementation, monitoring, training, reassessment and retirement, plus an inventory (his view, not Board policy)
  [PCAOB-BOTICSF-2026]. The SEC asks how
  firms use AI to monitor QC [KPMG-HOHL-2026].
- **FRC (UK).** Risks: deficient output, misuse of output, non-compliant methodology. Mitigations: system design,
  certification, staff education, human review at control points [FRC-GENAI-2026]. Documentation splits central and
  file records [FRC-AIAUDIT-2025]. Supervision centres on the system of quality management, starting with the
  largest firms in April 2026 [FRC-SUPERVISION-2026].
- **IFIAR, CPAB, AFM, NFRA, AICPA.** IFIAR asks firms to define "human-led" and consult early where AI decides
  without a human [IFIAR-TTF-2026, IFIAR-TTF-2025]. AFM: four preconditions, the lower three of which (risk
  management, input data, controlled tool implementation) must be in place before deploying (Gen)AI [AFM-12BB-2025].
  AICPA practice aid Part 2 (13 Oct 2026): assign who builds or buys tools, authorise them, set acceptable use,
  revalidate and monitor; a second AI checker does not reduce review duties [AT-AICPAPA-2026].

**Design guardrails seen in practice or guidance**: certify the tool in its use case; set tolerance for errors
together with planned review; recertify on model change; keep only approved versions reachable; require citations
and confirmation gates; place control points by where certification shows errors; reviewers form their own view on
high-risk items; record tool, version, inputs and the reviewer's reasons; pair LLMs with rules-based checks.

**Steps that stay with a person**: approving, restricting or retiring a tool; setting error tolerance; deciding a
recertification trigger has fired; deciding how much assurance a tool's output supplies; authorising an agent at a
control point; accepting or rejecting AI output; evaluating evidence sufficiency; root-cause conclusions; sign-off.

## 7. Roles and how they evolve

- **Central tool governance.** Technology and methodology teams own certification; Deloitte UK added a Technology
  Controls Board and a UK Chief AI Officer (`#01`, `#08`). Procurement and information security join tool approval.
- **Quality teams become analysts.** Reading tool telemetry alongside inspection findings (`#07`) is a new task; the
  only public example is an unnamed firm's board dashboard described by the AFM [AFM-12BB-2025].
- **Reviewers become challengers.** The FRC asks reviewers to have competence in the use case, sometimes specialist
  expertise, and says review may involve forming an independent view [FRC-GENAI-2026]. Deloitte says its
  professionals will supervise, validate and work alongside AI [DELOITTE-OMNIA-2026].
- **Partners carry explicit AI duties.** Understand the tools, confirm approval, plan use, check staff use them
  correctly [AICPA-PA-2026]; IFIAR asks seniors to stand back and review technology use (`#17`).
- **Juniors.** PwC says new hires will act like managers within three years [BI-PWC-2025]; the Big Four cut 2025
  graduate intake by as much as 6-29% [ICAEW-EXPECT-2026]. Risk: deskilling. Evidence is thin: Botic cited an unnamed
  MIT study (the best-known one is an EEG essay study [KOSMYNA-2025]); an audit-specific study has no results yet [HOLMSTROM-2024].
  Response seen: Deloitte UK graduate simulations mixing manual and AI-assisted methods (`#10`).
- **New hires.** PwC says it now hires engineers it would not previously have hired into assurance [PWC-AT-2025]. Smaller
  firms lean on third-party technology and methodology providers [ICAEW-FRCVIEW-2026] (`#06`).

## 8. Frontier

- **2025-06-26** FRC thematic review of tool certification and first AI-in-audit documentation guidance [FRC-ATT-2025, FRC-AIAUDIT-2025].
- **2025-11-21** KPMG announces ISO/IEC 42001 certification [AT-KPMGISO-2025].
- **2025-12** IAASB approves developing non-authoritative quality-management material [IAASB-MINDEC-2025]; PCAOB staff name AI
  adoption an inspection focus [DART-SECPCAOB-2025]; AFM publishes 12 building blocks [AFM-12BB-2025].
- **2026-03-25 / 03-30** FRC moves supervision to firms' quality systems; issues generative and agentic AI guidance
  [FRC-SUPERVISION-2026, FRC-GENAI-2026]. **2026-03** IAASB approves its action plan [IAASB-TQMPLAN-2026].
- **2026-04** Deloitte UK sets up a Technology Controls Board [DELOITTE-UKTR-2026]. **2026-04-20** IFIAR report on
  agentic AI, "human-led" audit and monitoring metrics [IFIAR-TTF-2026].
- **2026-06-04** FRC Audit Tech & AI Sandbox opens [FRC-SANDBOX-2026]. **2026-06-24** Deloitte Omnia agents and tutor mode [DELOITTE-OMNIA-2026].
- **2026-05** PCAOB launches an Inspections Modernization Council (advisory group) [JOFA-IMC-2026]. **2026-07** NFRA staff paper of technology principles: validation, monitoring, re-approval [NFRA-STAFF-2026].
- **2026-08-25 / 09-01** PCAOB staff materials: inspections centred on firms' QC systems; early AI pilots in inspection work [DART-IMC-2026, STARLING-IMC-2026].
- **2026-09-09** PCAOB adopts QC 1000 amendments, pending SEC approval [PCAOB-LOGOQC-2026, DART-QC1000-2026]. **2026-09-22** Botic sets out AI governance lifecycle expectations [PCAOB-BOTICSF-2026].
- **2026-10-05** Botic questions a staff idea to cut file reviews at "lower-risk" largest firms well below 50% of 2025 levels [PCAOB-BOTICIOWA-2026].
- **2026-10-13** AICPA practice aid with a firm-AI quality-management part [AICPA-PA-2026].
- **2026-12-15** QC 1000 effective. **To 2027-06** IAASB guides on GenAI and agentic tools, including foundation-model
  and service-provider considerations [IAASB-MINJUN-2026]. Watch for first FRC sandbox outputs and AI-specific inspection findings (none found yet).

## 9. Common objections

- **"Our tools are certified, so quality is covered."** Certification is not monitoring. The FRC found no large UK
  firm quantifying quality impact, and 31% of IFIAR member regulators reported tool-misuse findings in 2024 (`#07`).
- **"The standards don't fit opaque, non-deterministic AI."** IAASB roundtable participants raised it and still
  judged ISQM 1 and ISA 220 (Revised) a sound base; guides arrive by June 2027. The FRC's head of assurance
  technology argues the right comparison is a human, not traditional code [ICAEW-POD-2025]. Certify the tool in its
  use case with output tests (`#01`).
- **"We have a human in the loop."** CPAB says stating it is not enough; KPMG says rubber-stamp approval has "no
  real control value" [KPMG-SOX-2026]. Specify control points (`#18`) and what reviewers check (`#19`, `#20`).
- **"Review will eat the savings."** No data either way; PwC calls year-one savings modest. The FRC lets the extent
  of review follow residual risk. Measure review time and override rates rather than assume.
- **"We are too small for this."** The IAASB promises proportionate guides; Botic asks small firms whether a tool
  meets a real need and can be governed, not whether to adopt everything. Start with granular, checkable tasks
  (`#06`); the FRC sandbox is open to firms of any size.
- **"Regulators will penalise AI use."** No regulator prohibits it; the FRC says its guidance is not a response to
  deficiencies [FRC-GENAINEWS-2026]. Inspectors do say AI adoption is a focus, so keep an inspection-ready file
  (`#13`, `#23`).
- **"Documenting AI will bury us."** The FRC keeps tool design in a central record and asks for proportion; where
  every output of a research tool is checked back to cited sources, less tool documentation may be appropriate
  [FRC-AIAUDIT-2025]. A CalCPA author says a bare note that AI was used would not meet AU-C 230 [CALCPA-AISTD-2026].
- **"Let AI check the AI."** The AICPA allows it but review duties stay; a practitioner warns of a closed system
  where errors become hard to detect (`#22`). Use it to direct human attention, not replace it.
- **"Fewer file reviews means less scrutiny."** Botic is wary of cuts; the SEC's chief accountant said a QC-focused
  inspection model may be tougher on firms [CAQ-HOHLWEBINAR-2026].
- **"Failures are hypothetical."** A public review failure at a Big Four firm sits outside audit: Deloitte
  Australia partly refunded a government report with apparent AI-generated errors, including a fabricated court
  quote; the revised report disclosed GenAI use, and Deloitte did not say whether AI caused them [BNN-AP-DELOITTE-2025].

## 10. Sources

Full details (title, publisher, type, URL, date, access, locator) are in the YAML.
- **Regulators and standard-setters (in the YAML):** FRC-GENAI-2026, FRC-GENAINEWS-2026, FRC-ATT-2025,
  FRC-AIAUDIT-2025, FRC-SANDBOX-2026, FRC-SANDBOXPAGE-2026, FRC-SUPERVISION-2026, IFIAR-TTF-2025, IFIAR-TTF-2026,
  IFIAR-SURVEY-2026, IAASB-TQMPLAN-2026, IAASB-TQM-2026, CPAB-AI-2024, CPAB-EVOLVING-2025, AFM-12BB-2025, AFM-2025,
  NFRA-STAFF-2026, IRBA-SPA11-2025, PCAOB-GENAI-2024, PCAOB-PRIORITIES-2024, PCAOB-BOTICSF-2026, PCAOB-BOTICIOWA-2026, PCAOB-LOGOQC-2026, AICPA-PA-2026, AUASB-AI-2025.
- **Firms, press, professional bodies (in the YAML):** DELOITTE-UKTR-2025, DELOITTE-UKTR-2026, DELOITTE-OMNIA-2026,
  KPMG-TR-2025, KPMG-SOX-2026, KPMG-HOHL-2026, AT-KPMGISO-2025, RSM-ASKLUCA-2026, CPAPA-LUCA-2026, CAQ-RSM-2026,
  CFODIVE-PWC-2026, PWC-AT-2025, BI-PWC-2025, EY-CANVAS-2026, BAKERTILLY-GAM-2026, FOLEY-PCAOB-2026,
  DART-SECPCAOB-2025, STARLING-IMC-2026, AT-AICPAPA-2026, JOFA-AIPA-2026,
  JOFA-5IMP-2026, CALCPA-AISTD-2026, ICAEW-FRCVIEW-2026, ICAEW-POD-2025, ICAEW-EXPECT-2026, ICAS-SANDBOX-2026,
  NYSSCPA-BOTIC-2025, CAALLEY-PCAOBPE-2025, RSM-SECPCAOB-2025, NYENRODE-2026, CPAPRACTICE-RSMANDERA-2026, BOARDAGENDA-FRC-2026.
- **Vendors, surveys, academic, podcasts (in the YAML):** FIELDGUIDE-PCAOB-2026, FIELDGUIDE-SANVILLE-2026,
  TRI-FOP-2026, CPACOM-ATR-2025, PREPRINT-AIJGDI-2026, PETERS-2022, HOLMSTROM-2024, COMMERFORD-2022, FEDYK-2022,
  ARXIV-FAB-2026, FABIAN-2026, KOSMYNA-2025, PODWISE-ACCTPOD-2026.
- **Not in the YAML (cited in this file only; all opened):**
  - PCAOB-QCREL-2026: PCAOB, *PCAOB Adopts Amendments to Its Quality Control Standard* (news release), 2026-09-09, https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-adopts-amendments-to-its-quality-control-standard
  - DART-QC1000-2026: Deloitte DART, *PCAOB Releases Amendments to Quality Control Standard*, 2026-09-09, https://dart.deloitte.com/USDART/home/news/all-news/2026/sep/pcaob-amendments-quality-control-standard
  - EISNER-QC1000-2026: EisnerAmper, *PCAOB QC 1000 Amendments: What Audit Committees Need to Know*, 2026-10-08, https://www.eisneramper.com/insights/audit-assurance/pcaob-qc-1000-amendments-audit-committees-1026/
  - DART-IMC-2026: Deloitte DART, *PCAOB Shares Discussion Materials Related to Inspection Modernization Council's Summer 2026 Meetings*, 2026-08-25, https://dart.deloitte.com/USDART/home/news/all-news/2026/aug/pcaob-materials-inspection-modernization-council-summer-2026-meetings
  - JOFA-IMC-2026: Journal of Accountancy, *PCAOB works to form Inspections Modernization Council*, 2026-05-29, https://www.journalofaccountancy.com/news/2026/may/pcaob-works-to-form-inspections-modernization-council/
  - IAASB-MINDEC-2025: IAASB, approved minutes of the December 2025 public session (Agenda Item 8), 2025-12, https://www.iaasb.org/_flysystem/azure-private/2026-03/Approved%20Minutes%20of%20the%20Public-Session%20for%20December%202025_0.pdf
  - IAASB-MINJUN-2026: IAASB, approved minutes of the June 2026 meeting (Agenda Item 7), 2026-06, https://www.iaasb.org/_flysystem/azure-private/2026-09/Approved-Minutes-of-the-Public-Session-for-June-2026.pdf
  - CAQ-INSIDER-2026: CAQ, *Audit Insider, July/August 2026*, 2026-09-01, https://www.thecaq.org/audit-insider-july-august-2026
  - CAQ-HOHLWEBINAR-2026: CAQ, *Conversation with SEC Leaders: 5 Takeaways*, 2026-07-23, https://www.thecaq.org/aia-conversation-with-sec-leaders-5-takeaways
  - BNN-AP-DELOITTE-2025: Associated Press via BNN Bloomberg, *Deloitte to partially refund Australian government for report with apparent AI-generated errors*, 2025-10-07, https://www.bnnbloomberg.ca/business/artificial-intelligence/2025/10/07/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
