# Assurance interview guide

Last researched 2026-10-17. Use this alongside the method files: onboarding questions come from
[onboarding.md](../../method/onboarding.md), question craft from [interviewing.md](../../method/interviewing.md). This
file gives the assurance wording, the field's boundary probes, phase questions and the vocabulary to mirror. Ask one
question at a time and skip what you already know. Source keys in brackets resolve in §9 or in [sources.md](sources.md).

## Contents

1. [Who you are likely talking to](#1-who-you-are-likely-talking-to)
2. [Onboarding questions in assurance words](#2-onboarding-questions-in-assurance-words)
3. [Choosing focus modules](#3-choosing-focus-modules)
4. [Journey-stage boundary probes](#4-journey-stage-boundary-probes)
5. [Phase questions](#5-phase-questions)
6. [Internal audit variants](#6-internal-audit-variants)
7. [Sensitive topics](#7-sensitive-topics)
8. [Vocabulary to mirror](#8-vocabulary-to-mirror)
9. [Sources](#9-sources)

## 1. Who you are likely talking to

| Person | What they usually care about | Open with |
|---|---|---|
| Engagement or practice partner | Quality, inspection findings, margins under fee pressure, staffing in busy season | "Which part of the audit eats the most hours or causes the most review notes?" |
| Managing partner or executive | Firm strategy, capital, pricing, talent, competitors | "Why look at AI now, and what would change for the firm in three years?" |
| Innovation or digital audit leader | Tools, adoption, certification, vendor choices | "Which tools are used on most engagements, and which are still trials?" |
| Quality and risk partner | ISQM 1 or QC 1000, inspections, tool governance, independence | "How do you approve and monitor tools today?" |
| SOC practice lead | Volume, platform-driven clients, peer review, AI in client systems | "How many reports a year, and how much of the work is evidence chasing?" |
| Sustainability assurance lead | Regulatory churn, value-chain data, limited assurance | "Which regimes are you assuring under now, and what changed this year?" |
| CAE or SOX lead | Coverage within a flat budget, SOX cost, co-sourcing, the audit committee | "How many controls do you test, and what does a control cost you in hours?" |

## 2. Onboarding questions in assurance words

Use these in place of, or after, the starred questions in onboarding §3.

| Profile element | Question | Listen for |
|---|---|---|
| Role and scope | "Are you responsible for your own engagements, a team, an office or practice, a service line, or the firm?" | Scope level; whether a CAE runs a function or a SOX team only |
| What is delivered | "What do you sign or issue: audit opinions, ICFR opinions, SOC reports, sustainability conclusions, internal audit reports?" | Which service lines and modules |
| Clients | "Who are the clients: listed companies, private companies, public sector, service organisations?" | PCAOB or national inspection, peer review, independence intensity |
| How it is paid | "Is the work priced on budgeted hours, fixed fees, or an internal budget?" | Pricing exposure [CPACOM-ATR-2025] |
| Journey stage | "In the last two weeks, who used AI on a real engagement, and for which step? Could you show me the workpaper?" | Real use versus awareness |
| Pressures | "What is pushing hardest: fees, staffing, inspection findings, client questions about AI, or competitors' announcements?" | Why now |
| Constraints | "What must not change: independence, client confidentiality, your methodology, what the regulator expects on the file?" | Guardrails |
| Tools and data | "Which tools are approved, and how does client data get into your file today: exports, direct extracts, a portal?" | Tool estate; data readiness ([value-chain.md](value-chain.md) §4) |
| Unapproved use | "Some staff in most firms use AI tools that haven't been approved. Is that happening here? There's no wrong answer." | Shadow AI; more than a third of tax and audit professionals admit it (vendor survey) [TRI-FOP-2026] |
| Session goal | "What would make this worthwhile: quick wins for the next busy season, a plan for the practice, or a case for the partners?" | Path |

**Bring evidence in early.** Once you know the focus, give one real example with its grade from the relevant module,
and say who measured it.

## 3. Choosing focus modules

| If the user says | Module to load |
|---|---|
| "Client acceptance", "independence clearance", "rotation", "our new investor", "the AI vendor we partner with" | [acceptance-independence](modules/acceptance-independence.md) |
| "Planning", "risk assessment", "materiality", "the planning memo", "budgets and staffing" | [planning-risk-assessment](modules/planning-risk-assessment.md) |
| "SOX testing", "ITGCs", "walkthroughs", "control deficiencies", "testing hours per control" | [controls-testing](modules/controls-testing.md) |
| "Journal entries", "vouching", "confirmations", "sampling", "estimates", "inventory" | [substantive-testing](modules/substantive-testing.md) |
| "Valuation specialists", "actuaries", "using experts", "the client's AI model drives this number" | [specialists](modules/specialists.md) |
| "Disclosure checklist", "tie-out", "going concern", "EQR", "KAMs or CAMs", "audit committee report" | [completion-reporting](modules/completion-reporting.md) |
| "Tool approval", "certification", "inspection findings", "supervision and review", "ISQM 1", "QC 1000" | [quality-management](modules/quality-management.md) |
| "SOC 2", "Section 3", "Vanta or Drata clients", "bridge letters", "peer review on SOC" | [soc-attestation](modules/soc-attestation.md) |
| "CSRD", "ISSA 5000", "limited assurance", "GHG", "value-chain data" | [sustainability-assurance](modules/sustainability-assurance.md) |
| "Our clients' AI", "AI controls in ICFR", "ISO 42001", "AI certification", "AI governance opinion" | [assurance-over-ai](modules/assurance-over-ai.md) |

Pick one to three. If the user leads a whole practice, start from [value-chain.md](value-chain.md) instead.

## 4. Journey-stage boundary probes

Pick two or three. Markers and gates are in [ARCHETYPE.md](ARCHETYPE.md).

| Boundary | Ask | What decides it |
|---|---|---|
| Curious / Experimenting | "Is there any audit step where AI is part of how the work is normally done on more than one engagement?" | Repeated use on real engagements |
| | "What does your policy say about putting client data into an AI tool, and what would a senior say it says?" | Lived versus paper policy |
| Experimenting / Adopting | "Which tools are certified for which uses, and what happens when the vendor updates the model?" | Certification and recertification [FRC-GENAI-2026] |
| | "On a file that used AI, can I see where the file says which tool, version and inputs, and how the output was used?" | Documentation on the file [FRC-AIAUDIT-2025] |
| | "For the one workflow you trust most, what is the baseline: hours per selection or per control, review notes, rework?" | An owned, measured workflow |
| | "When an AI-assisted workpaper was wrong, who caught it, and how?" | A designed human control point |
| Adopting / Scaling | "Does your second AI workflow reuse anything from the first: the data connection, the review checklist, the certification file?" | Reuse |
| | "Who monitors tool use and its effect on quality across engagements: the network, the firm or each team?" | Monitoring ownership [IFIAR-TTF-2026] |
| Scaling / AI-native | "Has AI changed how you price or scope any engagement, or let you sell something new?" | Commercial change |
| Delegation check | "Is any agent selecting or testing items without a person checking each one? What are the written rules, and what is the override rate?" | The five gates in onboarding §5 |

## 5. Phase questions

Use these in addition to each phase file's question bank.

**Frame**
- "If audits took half the hours, what would happen to your fees, your realization and your staffing?" (87% of small US
  firms track realization; 13% track value billing [CPACOM-ATR-2025].)
- "Has a client or an audit committee asked for a lower fee because of AI? What did you say?" [FERF-2026]
- "What would your quality partner and your regulator accept as proof that an AI-assisted procedure worked?"
- "Which of your service lines would AI threaten, change a lot, or mainly help?" ([disruption.md](disruption.md) §9)
- "How many of your audit clients would lose the ICFR audit requirement under the SEC's filer-status proposal?" (US
  public-company practices) [UNIQUS-FILER-2026]
- "Who funds AI here: partners, debt or an outside investor? On what return?"

**Map**
- "Walk me through one typical engagement from acceptance to sign-off. Where do the hours go by stage and grade?"
- "How does the trial balance and ledger get from the client into your file, and how do you know it is complete?"
- "How many engagements a year, of what types? How many controls, selections or confirmations on a typical one?"
- "Where are the review bottlenecks: manager, partner, EQR?"
- "Which steps are done offshore or by a delivery centre?"

**Diagnose**
- "Which steps produce the most review notes or inspection findings?" (Internal control testing is the largest single
  source of findings at the six largest networks [IFIAR-SURVEY-2026].)
- "Which steps are rolled forward from last year without real change?"
- "Where does work wait on the client?" (Poor client data and no system access are top blockers [CPACOM-ATR-2025].)
- "Which steps need judgement, and which are mechanical checks against evidence?" (Use the work-type table in
  [value-chain.md](value-chain.md) §7.)

**Reimagine**
- "If every population were tested in full, which procedures would you stop, and which exceptions would you staff?"
- "If evidence arrived directly from banks and client systems, which requests would disappear?"
- "What would the file look like if an agent drafted the workpaper and your senior reviewed it against cited evidence?"
- "If you started a firm today with no history, what would you charge for a private-company audit?" (lens 4;
  [disruption.md](disruption.md) §2)

**Prioritize**
- "Which of these options would your quality partner block, and why?"
- "Which need client data you do not get today?"
- "Which depend on a tool you would have to certify first?"
- Raise the risk weight for inspection-exposed work, as the Frame method allows.

**Make the case**
- "What is the baseline, measured on real engagements: hours per selection, hours per control, review notes, rework?"
  (Hours per control was 16 in FY2024 in one company survey [KPMG-SOX-2026].)
- "Where will the hours go: lower budgets, more testing, fewer staff, or more clients?" ([economics.md](economics.md) §4)
- "What does certification, monitoring and parallel running cost in the first year?"
- "Where will juniors learn the judgement this step used to teach?" ([workforce.md](workforce.md) §7)

**Plan**
- "Who owns the tool's certification and monitoring, and who owns the workflow's results?"
- "Which engagements run it first, and when is the parallel run reviewed?"
- "When do you tell the audit committee and the client, and what goes in the engagement letter?"
- "Which regulatory dates fall inside the plan?" ([frontier.md](frontier.md) §6)

## 6. Internal audit variants

- "How did budget and headcount move in the last two years, and who approves the budget?" (19% of functions had budget
  cuts in 2025 [JOFA-IAPULSE-2026].)
- "What share of the plan is co-sourced, and have you reopened co-source terms since providers began announcing AI?"
- "Which controls does an agent test today, what is the re-performance rate, and who signs off?"
- "Has your external auditor agreed to rely on agent-produced workpapers? If not, what would they need?" (No public case
  exists; see [controls-testing](modules/controls-testing.md).)
- "Where does the business use AI, and is it in the audit plan?" ([assurance-over-ai](modules/assurance-over-ai.md))

## 7. Sensitive topics

- **Client data.** Never ask for client names, figures or files. Ask for volumes, ranges and roles.
- **Inspection findings.** Ask about themes, not specific files: "Which areas do inspectors keep raising?"
- **Unapproved tools.** Normalise first (§2), after some rapport.
- **Independence and investors.** Ask whether independence has reviewed a relationship, not for the terms.
- **Jobs.** If a partner or CAE worries about the team, use [people-and-change.md](../../method/people-and-change.md)
  and the evidence in [workforce.md](workforce.md); do not promise outcomes.

## 8. Vocabulary to mirror

| Term | Meaning | Note |
|---|---|---|
| Engagement, the file, workpapers | One audit or assurance job; its documentation | "The file" is what inspectors read |
| PBC (provided by client) | Items the client supplies on request | Where evidence chasing and data quality sit |
| Walkthrough; test of design; operating effectiveness | Tracing a transaction; checking a control is designed and works | Controls testing |
| RCM; ITGCs; IPE | Risk and control matrix; IT general controls; information produced by the entity | Say "ITGCs over AI components" for AI |
| RMM; assertions; significant risk | Risk of material misstatement, by assertion | Planning |
| Materiality, performance materiality | Thresholds for what matters | Judgement owned by the team |
| Journal-entry testing; full-population testing | Testing entries for fraud and error; testing every item | Prefer "whole-population" to "100% assurance" |
| Vouching, tie-out, casting | Matching to evidence; agreeing figures; checking arithmetic | Substantive and completion |
| Confirmations | Evidence obtained directly from third parties | AS 2310 and SAS 150 |
| EQR | Engagement quality review before release | Completion and quality |
| KAMs, CAMs | Key or critical audit matters in the report | Completion |
| ISQM 1, QC 1000 | Quality management standards (international, PCAOB) | Where tool governance lives |
| Inspection findings; peer review | Regulator or peer re-examination results | A sensitive topic |
| ATTs | Automated tools and techniques | The FRC's and IFIAR's term for audit tools |
| Certification, recertification | Approving a tool for a use; re-approving on change | Adopting marker |
| Realization, utilization, leverage | Billed versus standard value; chargeable time; staff per partner | Economics |
| Busy season | Peak period for year-end audits | Timing of any change |
| SOC 1, SOC 2, Type 1 or 2, Section 3, CUECs, bridge letter | SOC report types and parts | SOC module |
| Limited and reasonable assurance; double materiality | Assurance levels; CSRD's two-sided materiality | Sustainability |
| CAE; three lines; co-source; audit universe | Internal audit roles and model | Internal audit |
| Alternative practice structure (APS) | Attest firm kept separate from investor-owned services | Independence |

**Words to avoid:** "automate the audit", "replace auditors", "AI-generated opinion", "100% assurance". Say instead
"tool-assisted procedure", "AI first pass for review", "human control point", "whole-population testing".

## 9. Sources

Keys not listed here are in [sources.md](sources.md).

(All keys cited here are in sources.md.)
