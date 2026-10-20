# Professional services (archetype)

Last researched 2026-10-19. The index for the professional-services archetype: read it once onboarding points here,
then load only the module and archetype files the conversation needs. Source keys in brackets resolve in
[sources.md](sources.md).

## What it covers

How a firm that sells expert work by the engagement or matter wins, accepts, prices, staffs, delivers, quality-checks,
bills and learns from that work, plus its own finance and talent. Clients buy expert judgment as advice, documents or
analysis, with a named professional answerable for it, usually priced by time or by scoped piece of work.

## Who it serves

- **Firms:** law firms, management and technology consultancies, accounting and advisory firms (their firm-operations
  side), engineering and architecture firms, and AI-native entrants. Evidence is densest for law and thinnest for
  engineering and architecture ([state-of-ai.md](state-of-ai.md)).
- **In-house legal and shared-service teams that run like firms:** they take requests, scope, staff, deliver and
  account for work to internal clients, and buy outside firms' work. Public evidence covers in-house legal; finance,
  HR and other shared-service teams are barely documented.
- **Typical users:** managing and practice partners, COOs, CFOs, pricing, innovation, knowledge and talent leads, GCs.

## What it extends

Nothing: this is the base. **Assurance** and **tax** extend it with their field's own work (audit and attestation; tax
compliance and advice), and **security service providers** (MDR, pentest, IR retainers) use it for pursuit, pricing,
staffing, delivery and billing. Three things set this field apart. The professional stays accountable for AI-assisted
work under bar, institute or code rules that apply existing duties to AI [CALBAR-GENAI-2026; ICMCI-AICODE-2026].
Hourly fees turn AI efficiency into a pricing question [STANFORD-DEL-2026]. And junior work is both billable output
and the training ground [VAULT-PYRAMID-2026].

## Recognition cues

Match on what is delivered, to whom and how it is paid for, not on job titles:
- **Law firms:** "matters", "fee earners", "billable hours", "realisation", "write-downs", "conflicts", "OCGs",
  "e-billing rejections", "associates and partners", "Harvey", "Legora", "lateral hires", "the rate round".
- **Consultancies:** "engagements", "SOWs", "utilisation", "bench", "PSA", "time and materials", "fixed fee",
  "outcome-based fees", "pyramid", "proposals and RFPs", "delivery margin", "the pitch".
- **Accounting and advisory firms (firm side):** "WIP", "lockup", "partner track", "graduate intake", "private equity
  investment", "advisory pricing", "client onboarding and KYC", "staff utilisation".
- **Engineering and architecture firms:** "projects", "SF-330s", "utilisation", "project managers", "Deltek", "turnover".
- **In-house legal and shared-service teams:** "legal operations", "intake front door", "outside counsel spend",
  "panel", "invoice review", "insourcing", "internal clients", "CLOC".

**Not professional services alone:** audit opinions, SOC reports and attestation are assurance; tax returns, provisions
and tax advice are tax; security operations (SOC, MDR, pentests) are security. Use both: the field archetype for the
field's own work, this one for winning, pricing, staffing and billing it.

## Modules

**Evidence** is each module's share of use cases graded A or B (strong: 50% or more; moderate: 30-49%; thin: under
30%), as of the last review. Only work-production and talent-learning have grade A; most B entries rest on vendor or
self-reported figures, and **no firm publishes an error, override or parallel-run rate for AI-assisted work**.

| Module | What it covers | Evidence |
|---|---|---|
| [pursuit-proposals](modules/pursuit-proposals.md) | Go/no-go, RFPs, credentials, drafting, the pitch, answering clients' AI questions; widest use, least measured | moderate (9 of 20 A/B) |
| [client-development](modules/client-development.md) | Relationship data, key accounts, outreach, the client AI-value conversation, client AI terms | strong (11 of 22 A/B) |
| [acceptance-risk](modules/acceptance-risk.md) | Conflicts, KYC, engagement risk, engagement letters, OCGs, client AI terms, ethical walls, in-house intake | moderate (6 of 14 A/B) |
| [scoping-pricing](modules/scoping-pricing.md) | Scope, estimates, price model, SOW and fee proposal, who keeps the AI saving, productised services | strong (14 of 23 A/B) |
| [staffing-resourcing](modules/staffing-resourcing.md) | Demand, capacity, skills data, matching, utilisation, supply decisions, agents as capacity | thin (5 of 21 A/B) |
| [delivery-management](modules/delivery-management.md) | Handoff, plans, status, risk, scope change, engagement economics, close-out; PSA agents | moderate (7 of 15 A/B) |
| [work-production](modules/work-production.md) | Research, synthesis, extraction, first drafts, playbook review, release checks; mostly legal | strong (18 of 25 A/B) |
| [quality-review](modules/quality-review.md) | Verification, supervisory sign-off, the firm's AI quality system, disclosure, error response | strong (11 of 18 A/B) |
| [billing-collections](modules/billing-collections.md) | Time capture, narratives, pre-bill, e-billing, collections, in-house invoice review | thin (5 of 17 A/B) |
| [knowledge-management](modules/knowledge-management.md) | Capture, curation, search, reuse, expertise location, governing what AI may see | strong (12 of 23 A/B) |
| [talent-learning](modules/talent-learning.md) | Intake, AI training, the apprenticeship, evaluation, incentives, career paths, the pyramid | strong (15 of 25 A/B) |
| [firm-finance](modules/firm-finance.md) | Fee mix, rates, realisation, AI investment, return and cost, partner economics, outside capital | strong (9 of 17 A/B) |

## Journey-stage markers (professional services)

Stage names and gates follow [onboarding.md](../../method/onboarding.md) §5. Place each scope (team, practice, office,
firm or in-house function) by markers you can see or count, not by self-rating.

| Stage | Markers in a firm or in-house team | Ready for the next stage when |
|---|---|---|
| **Curious** | People use public tools outside policy (34% of 1,816 professionals use unsanctioned AI) [TR-FOP-REPORT-2026]; no policy, or a "do not upload client data" memo (formal policy at 57% of law firms under 50 lawyers) [ILTA-TECHSURVEY-2026]; partners do not raise AI with clients [TRI-STANDOUT-2026] | A written rule covers client data, client AI terms and approved tools; named people use AI weekly on real work |
| **Experimenting** | One enterprise or legal AI tool licensed on request; pilots from a team up to 1,300+ lawyers [LEGORA-HLC-2026]; savings anecdotal, "still gathering the data" [TRI-LEGALWEEK-2026]; no baseline of hours, write-downs or review notes | One workflow has an owner, a baseline, a written review step and an approved tool |
| **Adopting** | Training required before access; drafting, review and research used on matters with human sign-off; AI use recorded per matter; client AI questions answered with some data; PSA agents draft estimates or SOWs [CERTINIA-VEDA-2026] | Two or more workflows in production; the second reused the first's data, checklist or controls; value recorded in one place; a named owner |
| **Scaling** | Work redesigned around review gates [HARVEY-ORCH-2026]; AI work flows into time entries and matter economics [LEGORA-LAUREL-2026]; AI cost metered by matter [TRI-METER-2026]; fixed or hybrid fees priced on AI-reduced effort; intake and training redesigned | Value shows in realisation, margin or revenue per head, and leaders ask what to sell and how to price it |
| **AI-native** | Small expert teams directing agents (an AI-native advisory boutique's target of "20 per cent humans, 80 per cent AI agents", as reported from the FT) [RESULTSENSE-2026]; services clients use without a professional in the loop (PwC's stated plan) [CPAPA-PWC-2026]; outcome or hybrid fees the default; agents planned as capacity (none of 44 organisations yet) [KANTATA-RMI-REPORT-2026] | Re-diagnose at each review. No firm has published a measured cost or quality advantage from being AI-native |

**Delegation.** Plan agentic work only at Adopting or later, behind the five gates in onboarding §5. Reference case: an
IT consultancy's 12-agent PMO estate with a human approval gate before anything reaches a client (delivery-management
`#12`; sponsored conference talk, self-reported). California ties required oversight to the system's autonomy [CALBAR-GENAI-2026].

## Files in this archetype

| File | Read when | What it gives you |
|---|---|---|
| [interview-guide.md](interview-guide.md) | Onboarding, and on entering each phase | Wording by firm type, module chooser, boundary probes, phase and in-house questions, vocabulary |
| [value-chain.md](value-chain.md) | Map; choosing focus modules; unit breakdown | Four stages, processes and key steps with work types, linked to modules |
| [economics.md](economics.md) | Frame; Make the case; fees, rates, margins, budgets or ownership | Revenue model, metrics and benchmarks, cost structure, AI cost, pricing pressure |
| [state-of-ai.md](state-of-ai.md) | Onboarding (evidence early); Frame | Surveys by firm type, what leaders are doing, measured versus announced, maturity spread |
| [frontier.md](frontier.md) | Frame (why now); Reimagine lens 4; Plan dates | Dated signals for the next 12-36 months and what each means for a leader |
| [guardrails.md](guardrails.md) | Frame constraints; Reimagine fit checks; Make the case risks | Bar and code duties, courts, billing ethics, confidentiality, client terms, insurance, human judgment |
| [workforce.md](workforce.md) | Role evolution; capacity choice; any fear for roles | Roles, the pyramid, intake data, how roles change, skills, the apprenticeship question |
| [disruption.md](disruption.md) | Unit or firm scope; Frame exposure; lens 4 | Pricing shift, AI-native firms, outside capital, the pyramid, insourcing, labs and platforms |
| [objections.md](objections.md) | When the user pushes back | Cross-cutting objections with evidence-based responses |
| [sources.md](sources.md) | To resolve a source key, or to plan more research | The source landscape and the shared source list |
