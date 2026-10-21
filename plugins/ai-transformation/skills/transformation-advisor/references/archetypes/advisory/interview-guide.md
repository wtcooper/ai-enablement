# Advisory interview guide

Last researched 2026-10-21. Use this alongside the method files: onboarding questions come from
[onboarding.md](../../method/onboarding.md), question craft from [interviewing.md](../../method/interviewing.md). This
file gives the advisory wording, the first independence and data probes, phase questions and the vocabulary to mirror.
Ask one question at a time and skip what you already know. Source keys in brackets resolve in [sources.md](sources.md).

## Contents

1. [Who you are likely talking to](#1-who-you-are-likely-talking-to)
2. [Onboarding questions in advisory words](#2-onboarding-questions-in-advisory-words)
3. [Choosing focus modules](#3-choosing-focus-modules)
4. [Three probes to ask early](#4-three-probes-to-ask-early)
5. [Journey-stage boundary probes](#5-journey-stage-boundary-probes)
6. [Phase questions](#6-phase-questions)
7. [In-house variants](#7-in-house-variants)
8. [Sensitive topics](#8-sensitive-topics)
9. [Vocabulary to mirror](#9-vocabulary-to-mirror)

## 1. Who you are likely talking to

| Person | What they usually care about | Open with |
|---|---|---|
| CAS or outsourced accounting leader | Clients per accountant, close days, cleanups, platform choice, fixed fees, hiring | "Walk me through one client's month. Where do the hours go?" |
| Managing partner of a mid-market firm | Growth from CAS into advisory, capital and buyers, which AI platform, independence | "Which practice do you expect AI to change first, and what would you sell differently?" |
| Risk, internal-audit or SOX partner | Hours per control, agent testing, what the external auditor will rely on, AI governance demand | "Which tests would you hand to an agent first, and what would you compare it with?" |
| Transaction advisory (TAS) partner | Days to first databook, thin reports, junior pipeline, cheaper AI-native QoE | "In your last three QoEs, which steps did a tool touch, and what did the reviewer change?" |
| Valuation leader | IVSC disclosure, review quality, comparables, recurring fund marks, auditor challenge | "Which valuation steps use AI today, and what goes in the engagement file?" |
| Forensic or disputes leader | Data preparation hours, reproducibility, disclosure to counsel and courts, deepfake matters | "Could you reproduce an AI-assisted result at a deposition?" |
| FP&A or performance advisory lead | Client data readiness, planning-platform alliances, managed FP&A, forecast accuracy | "Which FP&A deliverables does your team draft with AI now, and how much survives review?" |
| Family-office director or private-client partner | Data sensitivity, alternatives administration, consolidated reporting, payment fraud, principals' trust | "How do capital calls and K-1s reach you, and from how many managers?" |

## 2. Onboarding questions in advisory words

Use these in place of, or after, the starred questions in onboarding §3.

| Profile element | Question | Listen for |
|---|---|---|
| Role and scope | "Are you responsible for your own clients, a team, a service line, an office, the advisory practice, or the firm?" | Scope level; firm or in-house |
| What is delivered | "What do clients get from you: closed books and packages, tested controls, a QoE or databook, a valuation report, an expert report, a forecast, a family view?" | Which modules |
| Clients | "Who are the clients: small businesses, middle-market companies, PE sponsors and their portfolio, lenders, counsel, families?" | Segment; who signs off on the client side |
| Audit overlap | "Which of these clients does your firm or an affiliate also audit, review or attest for?" | Independence exposure (§4) |
| How it is paid | "Fixed monthly fee, subscription, hourly, fixed project fee, or something tied to outcomes?" | Who keeps an AI saving ([economics.md](economics.md) §4) |
| Journey stage | "In the last two weeks, who used AI on real client work, and for which step? Where is that recorded?" | Real use versus awareness |
| Pressures | "What is pushing hardest: staffing, fees, AI-native competitors, clients doing it themselves, PE buyers, or clients asking about AI?" | Why now |
| Constraints | "What must not change: who signs, independence, client consent and confidentiality, what auditors, lenders or courts expect?" | Guardrails ([guardrails.md](guardrails.md)) |
| Tools and data | "Which ledgers, testing, diligence, planning or valuation platforms do you use, and how does client data reach them?" | Tool estate; data readiness ([value-chain.md](value-chain.md) §3) |
| Unapproved use | "In most firms some people use AI tools that haven't been approved. Is that happening here? There's no wrong answer." | Shadow AI: 34% of professionals in one survey [TR-FOPREPORT-2026] |
| Session goal | "What would make this worthwhile: something for next month's close, a plan for the practice, or a case for your partners?" | Path |

**Bring evidence in early.** Once you know the focus, give one real example from the module with its grade and who
measured it. In most advisory modules the honest answer is "the vendor" or "the firm itself".

## 3. Choosing focus modules

| If the user says | Module to load |
|---|---|
| "CAS", "our bookkeepers", "the close for clients", "cleanups", "fractional CFO", "payroll", "bill pay", "Botkeeper", "Digits" | [client-accounting-services](modules/client-accounting-services.md) |
| "Co-sourced internal audit", "SOX testing", "RCM", "ITGCs", "AuditBoard or Optro", "Fieldguide", "AI governance for clients", "COSO" | [risk-controls](modules/risk-controls.md) |
| "QoE", "FDD", "databook", "proof of cash", "add-backs", "data room", "sell-side", "SBA lender QoE" | [transactions](modules/transactions.md) |
| "PPA", "impairment", "fund marks", "comparables", "DLOM", "the IVS draft", "USPAP", "BVR" | [valuation](modules/valuation.md) |
| "Investigations", "tracing", "damages", "expert report", "e-discovery", "Weber", "Rule 707", "deepfakes" | [forensic-disputes](modules/forensic-disputes.md) |
| "Budget cycle", "rolling forecast", "board pack", "Adaptive", "Abacum", "ERP implementation", "managed FP&A" | [fpa-performance](modules/fpa-performance.md) |
| "Family office", "principals", "capital calls", "alternatives", "consolidated view", "succession", "exit readiness" | [private-client](modules/private-client.md) |

Pick one to three. If the user leads a whole advisory practice, start from [value-chain.md](value-chain.md). If the
talk turns to pricing the firm's own work, staffing or ownership, load the matching professional-services module.

## 4. Three probes to ask early

These recur in every module and change what is possible, so ask them in the first conversation.

1. **Who is the client?** "List the advisory and CAS clients that are also attest clients. Which regime applies (SEC,
   AICPA, IESBA), and who signs off when a new service is added?" Listen for a system, not memory. A 2016 account
   describes a firm whose systems would not issue a client number until independence was cleared
   [JOFA-NONATTEST-2016]. Detail: [guardrails.md](guardrails.md) §3.
2. **Where does client data go?** "Which AI tools touch client data, on which plan tier, who approved them, and what do
   engagement letters say about AI?" The AICPA Code means asking whether client consent is needed first
   [JOFA-ETHAI-2026]; three in five accountants say clients ask for proof of AI data protection always or frequently,
   while 33% explain their AI use without being asked [INTUIT-ACCTTECH-2026].
3. **Who keeps the saving?** "When AI cuts the hours behind a recurring deliverable, what happens to the fee, the
   margin and the team's incentive?" A named RSM partner frames halved production time as "all margin for me or all
   price reduction for our client" [BBLAW-PRICING-2026]. Detail: [economics.md](economics.md) §6.

## 5. Journey-stage boundary probes

Pick two or three. Markers and gates are in [ARCHETYPE.md](ARCHETYPE.md).

| Boundary | Ask | What decides it |
|---|---|---|
| Curious / Experimenting | "Is there any step where AI is part of how the work is normally done, on more than one client?" | Repeated use on real work |
| | "What does your policy say about putting client books or data-room files into an AI tool?" | Lived versus paper policy; 21% have one [KARBON-SOAI-2026] |
| Experimenting / Adopting | "For the workflow you trust most, what is the baseline: hours per client a month, per control, per databook?" | An owned, measured workflow |
| | "Did you validate the vendor's match or accuracy rate on your own clients' data, or run a parallel close?" | Quality evidence of your own; no vendor publishes it independently |
| | "When the AI was wrong, who caught it, and do you track override or rework rates?" | A designed review step |
| Adopting / Scaling | "Does the second AI workflow reuse anything from the first: the ledger connection, the review checklist, the vendor review?" | Reuse |
| | "Who owns AI across the advisory practice, and where is value recorded?" | Ownership and portfolio tracking |
| Scaling / AI-native | "Has AI changed how you price, staff or package any service, or let you sell something new, such as AI governance?" | Commercial change |
| Delegation check | "Does any agent post entries, test controls or draft findings without a person checking each item? What are the written rules?" | The five gates in onboarding §5 |

## 6. Phase questions

Use these in addition to each phase file's question bank.

**Frame**
- "If the recurring work took half the hours, what would happen to fees, clients per person and hiring?" (Fixed fee
  66% and hourly 60% still dominate in one survey of 200+ firm leaders [BILL-AIAMBITION-2026].)
- "Which of your services would AI threaten, change a lot, or mainly help?" ([disruption.md](disruption.md) §8)
- "Where are your clients putting their consulting and AI budget?" (Among AI-using middle-market leaders raising AI
  spend, 40% take budget from external consulting [CPAPA-RSMMM-2026].)
- "Has anyone approached you about outside capital, and what would it change in what you can sell to audit clients?"
  ([economics.md](economics.md) §7)

**Map**
- "Walk me through one engagement or one client month from data in to deliverable. Where do the hours go, by grade?"
- "How does client data reach you: ledger connections, exports, data rooms, portals, scanned statements?"
- "How many clients, controls, deals, reports or entities a year? What share is recurring?"
- "Which steps are offshore or outsourced today?" (29% of responding firms offshore, per a 2025 AICPA PCPS and CPA.com survey as
  reported [ACCTODAY-OUTSOURCING-2026].)

**Diagnose**
- "Which steps produce the most review notes, rework or client questions?"
- "Where does work wait on the client's data?" (Manual data cleanup is the top advisory blocker, 30%
  [INTUIT-ACCTTECH-2026].)
- "Which steps are mechanical matching against a document, and which need judgment?" (Work types in
  [value-chain.md](value-chain.md) §4.)

**Reimagine**
- "If every client's books closed continuously, what would your seniors spend the month on?"
- "If an agent drafted every RCM and test workpaper, what would your reviewers need to see?"
- "If buyers ran first-pass diligence themselves, what would they still pay you for?"
- "If you started the practice today, what would you charge, and whom would you hire?" (lens 4; [disruption.md](disruption.md))

**Prioritize**
- "Which options would your independence or risk partner block, and for which clients?"
- "Which need data the client cannot give you yet, or consent you have not collected?"
- Raise the risk weight for anything a lender, court, auditor or audit committee will rely on.

**Make the case**
- "What is the baseline on real work, and what review time will you add?" (A JofA guide suggests a 30-60 day pilot
  measuring time saved, added review time, errors and client feedback [JOFA-CASAI-2026].)
- "Is the comparison onshore cost, offshore cost, or both?"
- "Where will juniors learn the judgment this step used to teach?" ([workforce.md](workforce.md) §6)

**Plan**
- "Who owns the tool, its vendor review and its exit plan if the vendor fails?" (Botkeeper announced its closure in
  February 2026 [CPAPA-XENDOO-2026].)
- "Which clients go first, and when do you compare the parallel run with the manual result?"
- "Which rule dates fall inside the plan?" ([frontier.md](frontier.md) §6)

## 7. In-house variants

- **Controller or CFO buying CAS or FP&A:** "Which close or reporting steps would you rather run on your own agents,
  and which would you keep outsourced?" (BlackLine, FloQast, Microsoft and Workday have shipped, previewed or announced
  close agents [CPAPA-AGENTSCLOSE-2026].)
- **CAE or SOX lead:** "What did you bring in-house first, and what does the external auditor say it will rely on?"
  (In an informal poll, uncertainty was the largest answer, 48% [IAC-SOXRELIANCE-2026].)
- **Corporate or PE deal team:** "Which diligence steps do you now run before advisers arrive?" (31% of PE, VC and LP
  respondents report AI somewhat or fully integrated in diligence [SPGLOBAL-PE-2026].)
- **Family office:** "What do you keep in house and what do you outsource, and who owns any AI?" (private-client `#15`)

## 8. Sensitive topics

- **Client data.** Never ask for client names, figures or files. Ask for volumes, ranges and roles.
- **Audit-client overlap.** Ask how the check works, not which named clients are affected.
- **Unapproved tools.** Normalise first (§2), after some rapport.
- **Ownership and buyers.** Ask whether an approach has been made, not for terms.
- **Jobs.** If a leader worries about the team, use [people-and-change.md](../../method/people-and-change.md) and
  [workforce.md](workforce.md); do not promise outcomes or set headcount targets.

## 9. Vocabulary to mirror

| Term | Meaning | Note |
|---|---|---|
| CAS, CAAS | Client accounting (and advisory) services: outsourced or co-sourced financial operations | The base many firms grow advisory from |
| Fractional CFO; controllership | A part-time finance lead; senior accounting oversight | Management-function limits for audit clients |
| Close; package; flux | Month-end close; the reporting pack; period-on-period movement analysis | Where CAS and FP&A meet |
| RCM; ITGCs; PBC | Risk and control matrix; IT general controls; documents "provided by client" | Risk and controls |
| Co-sourced, outsourced internal audit | The firm staffs part or all of a client's internal audit | Restricted for SEC audit clients |
| QoE; FDD; databook; proof of cash | Quality of earnings; financial due diligence; the analysis workbook; tying ledger to bank | Transactions |
| Add-backs; NWC; debt-like items | Normalizing adjustments; net working capital; items treated as debt in the price | Stay human decisions |
| PPA; Level 3; DLOM | Purchase price allocation; fair value from unobservable inputs; discount for lack of marketability | Valuation |
| IVS; USPAP; AO-41 | International Valuation Standards; US appraisal standards; the 2026 advisory opinion on AI | Valuation duties |
| Rule 702; proposed Rule 707 | Expert reliability rule; proposed rule on machine-generated evidence | Forensic |
| CPM; driver-based model | Planning software; a model tied to operating drivers | FP&A |
| Principals; alternatives administration | The family members an office serves; capital calls, distributions, K-1s | Private client |
| APS | Alternative practice structure: an investor-backed advisory entity beside a licensed CPA firm | Sets what can be sold to attest clients |

**Words to avoid:** "AI does the books", "autonomous audit", "AI valuation", "AI expert", "no review needed". Say
instead "AI first pass for review", "agent-tested with reviewer sign-off", "AI-assisted analysis", "the signing
professional", "exceptions queue".
