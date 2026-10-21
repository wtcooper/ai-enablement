# Advisory (archetype)

Last researched 2026-10-21. The index for the advisory archetype: read it once onboarding points here, then load only
the module and archetype files the conversation needs. Source keys in brackets resolve in [sources.md](sources.md).

## What it covers

The advisory and outsourced-services side of accounting and advisory firms, mostly serving private and middle-market
companies: client accounting services (outsourced accounting and close, fractional CFO, payroll), risk and controls
advisory (outsourced internal audit, SOX readiness, governance of clients' AI), transaction advisory, valuation,
forensic and disputes, FP&A and performance work, and private client (family offices, owners). The client buys a
recurring service or an expert answer from named professionals, with no attest opinion attached.

## Who it serves

- **Firms:** top-100 and mid-market CPA firms with CAS and advisory practices, private-equity-backed platforms whose
  advisory arm sits beside a separate licensed attest firm, Big Four deal and risk groups, independent valuation and
  forensic firms, small firms and solo practitioners, and AI-native providers ([state-of-ai.md](state-of-ai.md)).
- **In-house teams that buy or mirror the work:** controllers and finance teams, chief audit executives and SOX leads,
  corporate and PE deal teams, family offices. Their own agent use sets what they will buy.
- **Typical users:** CAS and advisory practice leaders, risk and internal-audit partners, transaction, valuation and
  forensic leaders, family-office directors, managing partners of mid-market firms.

## What it extends

It extends **[professional-services](../professional-services/ARCHETYPE.md)**: firm operations (pursuit, pricing the
firm's own work, staffing, billing, ownership) are there. It sits beside **assurance** (attest) and **tax** (tax
technical work). Advisory changes three things. Independence limits follow the client: a service sold freely to one
client is restricted for a client the firm also audits [SEC-RULE2-01-2026]. No regulator has issued AI guidance written
for most of this work, so existing codes apply; valuation standards and evidence rules are the parts in motion
[JOFA-ETHAI-2026; IVSC-IVSED-2026]. And recurring outsourced work (CAS) is the base many firms grow advisory from [ACCTODAY-CASKEYS-2026].

## Recognition cues

Match on what is delivered, to whom and who regulates it, not on job titles. Cues that point to advisory:
- **CAS:** "CAS" or "CAAS", "outsourced accounting", "we close the books for clients", "fractional CFO", "payroll",
  "bill pay", "clients per accountant", "QuickBooks, Xero, Intacct", "fixed monthly fee", "cleanup and catch-up".
- **Risk and controls:** "outsourced or co-sourced internal audit", "SOX readiness", "RCM", "ITGCs", "control
  testing for clients", "COSO", "AI governance for our clients", "AIUC-1 readiness", "the IIA framework".
- **Deals and events:** "QoE", "FDD", "databook", "proof of cash", "add-backs", "net working capital", "sell-side",
  "lender QoE"; "PPA", "impairment", "fund marks", "IVS", "USPAP"; "fraud investigation", "damages", "expert
  witness", "tracing", "Rule 702 or 707", "ACFE".
- **FP&A and private client:** "budget cycle", "rolling forecast", "board pack", "CPM or ERP implementation",
  "managed FP&A"; "family office", "principals", "capital calls", "consolidated reporting", "succession", "exit readiness".

**Not advisory:** attest opinions, SOC reports and assurance over AI systems are assurance; returns, the provision,
tax advice and estate, gift or 409A valuations are tax; the firm's own pursuit, pricing, staffing, billing and
ownership are professional-services; regulated investment advice is out of scope. **Independence limit:** some advisory
services are restricted for the firm's own audit clients. For SEC issuer audit clients these include bookkeeping,
financial-system design, valuation and fairness opinions, internal-audit outsourcing, management functions,
investment-banking-type services and expert advocacy, plus any contingent fee [SEC-RULE2-01-2026]. Ask which clients
are also audit clients before planning AI on their books ([guardrails.md](guardrails.md) §3).

## Modules

**Evidence** is each module's share of use cases graded A or B (strong: 50% or more; moderate: 30-49%; thin: under
30%), as of the last review. One entry is grade A (CAS `#01`, an independent field study); **no firm publishes an
error, override or parallel-run rate for AI-assisted advisory work**. Use thin modules for probes, not proof points.

| Module | What it covers | Evidence |
|---|---|---|
| [client-accounting-services](modules/client-accounting-services.md) | Coding, reconciliation, close, packages, AP and payroll, fractional CFO, close agents, AI-native bookkeeping, platform choice | strong (12 of 24 A/B) |
| [risk-controls](modules/risk-controls.md) | Outsourced internal audit, SOX scoping and testing with agents, SOC report review, advising clients on governing their AI | strong (12 of 23 A/B) |
| [transactions](modules/transactions.md) | QoE and FDD: mapping, proof of cash, flux, add-backs, data rooms, databooks, AI-native QoE, lender QoE | moderate (5 of 16 A/B) |
| [valuation](modules/valuation.md) | Comparables, modelling, report drafting and review, fund marks, IVS and USPAP AI duties; rich standards, thin practice | thin (3 of 15 A/B) |
| [forensic-disputes](modules/forensic-disputes.md) | Data preparation, tracing, document review, expert reports, evidence law, deepfake and AI-fraud demand | moderate (5 of 15 A/B) |
| [fpa-performance](modules/fpa-performance.md) | Budgets, forecasts, variance narrative, planning and ERP implementation, managed FP&A; the thinnest evidence | thin (2 of 14 A/B) |
| [private-client](modules/private-client.md) | Family-office accounting, alternatives administration, consolidated reporting, payment controls, succession, AI policy | moderate (6 of 17 A/B) |

## Journey-stage markers (advisory)

Stage names and gates follow [onboarding.md](../../method/onboarding.md) §5. Place each scope (team, practice, firm or
in-house function) by markers you can see or count, not by self-rating.

| Stage | Markers in an advisory practice | Ready for the next stage when |
|---|---|---|
| **Curious** | Individual use of public tools; 21% of firms have an AI policy or strategy [KARBON-SOAI-2026]; nobody can list which advisory clients are also attest clients; no deliverable or fee changed | A written rule covers client data, consent and approved tools; named people use AI weekly on real work |
| **Experimenting** | AI use "situational" (54% of 725 respondents) rather than the default (30%) [INTUIT-ACCTTECH-2026]; one-task pilots (coding, variance commentary, an RCM draft, trial-balance mapping); vendor match rates taken on trust | One workflow has an owner, a baseline (hours per client a month, per control, per databook), a written review step and a tool validated on the firm's own data |
| **Adopting** | AI inside the ledger, testing or diligence platform with review gates (Forvis Mazars Group rolled out Opio after a nine-month pilot, with mandatory human review) [FORVISGROUP-OPIO-2026]; independence checked by client in a system; engagement letters cover AI; a one-page answer when clients ask for proof of data protection | Two or more workflows in production; the second reused the first's data feed, checklist or controls; value recorded in one place; a named owner |
| **Scaling** | Agents across practices on a shared platform (RSM's internal-audit testing agent live) [ACCTODAY-RSMBEACON-2026]; firmwide assistants (RSM nearly 20,000 people) [RSM-IMPACT-2026]; live dashboards replace periodic packages [ACCTODAY-CASKEYS-2026]; an agent inventory with owners and replayable evidence [CPAPA-AGENTSCLOSE-2026] | Value shows in margin, clients per person or new revenue, and leaders ask what to sell and how to price it |
| **AI-native** | Practice built around agents with people on review and judgment; AI-native roll-ups [ACCTODAY-CURRENT-2026]; vendors paid only on automation achieved [DIGITS-OUTCOME-2026]; governance or assurance over clients' agents sold [GT-EAS-2026] | Re-diagnose at each review. No firm has published a measured cost or quality advantage from being AI-native |

**Delegation.** Plan agentic work only at Adopting or later, behind the five gates in onboarding §5. Reference case:
firms running agentic control testing in co-sourced internal audit, with a reviewer on every conclusion and "missing
support" kept apart from a true exception (risk-controls `#06`; figures vendor-published or self-reported).

## Files in this archetype

| File | Read when | What it gives you |
|---|---|---|
| [interview-guide.md](interview-guide.md) | Onboarding, and on entering each phase | Advisory wording, module chooser, first independence probes, phase and in-house questions, vocabulary |
| [value-chain.md](value-chain.md) | Map; choosing focus modules; unit breakdown | Four stages, processes and key steps with work types, linked to modules; the client data layer |
| [economics.md](economics.md) | Frame; Make the case; fees, margins, capital or ownership | Revenue model, fees and pricing, margins, cost structure, PE consolidation, AI pricing pressure |
| [state-of-ai.md](state-of-ai.md) | Onboarding (evidence early); Frame | Surveys (practitioner and client side), what leaders are doing, measured versus announced, maturity spread |
| [frontier.md](frontier.md) | Frame (why now); Reimagine lens 4; Plan dates | Dated signals for the next 12-36 months and what each means for a leader |
| [guardrails.md](guardrails.md) | Frame constraints; Reimagine fit checks; Make the case risks | Independence, contingent fees, client data, codes and standards by module, evidence law, human judgment |
| [workforce.md](workforce.md) | Role evolution; capacity choice; any fear for roles | Roles, leverage, the junior pipeline, offshore review, new roles, the apprenticeship question |
| [disruption.md](disruption.md) | Unit or firm scope; Frame exposure; lens 4 | Business-model scenarios with evidence status and signals to watch |
| [objections.md](objections.md) | When the user pushes back | Cross-cutting objections with evidence-based responses |
| [sources.md](sources.md) | To resolve a source key, or to plan more research | The source landscape and the shared source list |
