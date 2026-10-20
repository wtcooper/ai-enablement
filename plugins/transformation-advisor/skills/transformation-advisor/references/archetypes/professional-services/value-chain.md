# Professional-services value chain

Last researched 2026-10-19. Use this in Map to lay out stages, processes and key steps before asking for real volumes
and times, and to pick focus modules. Each step carries work types from the controlled vocabulary. Step detail, pain
points and AI use cases are in the module files' §2 and §3; this file does not repeat them. Source keys in brackets
resolve in §7 or in [sources.md](sources.md).

## Contents

1. [How to use it](#1-how-to-use-it)
2. [Stages at a glance](#2-stages-at-a-glance)
3. [Where the work types cluster](#3-where-the-work-types-cluster)
4. [Stage by stage](#4-stage-by-stage)
5. [Layers that cut across every stage](#5-layers-that-cut-across-every-stage)
6. [Firm-type and in-house variants](#6-firm-type-and-in-house-variants)
7. [Sources](#7-sources)

## 1. How to use it

- The chain is the life of one matter, engagement or project, from first contact to cash, plus the firm-level work
  that learns from it and pays for it. Show the leader the stage table in §2, then ask which stages hurt most.
- For each process the leader cares about, open the linked module's §2 for the step table and typical pains, then ask
  for their own numbers: proposals, new matters, engagements and invoices a year; hours per step by grade; write-downs,
  rejections, rework and review notes.
- Field archetypes plug into stage 3. Audit procedures sit in [assurance](../assurance/ARCHETYPE.md), tax technical
  work in [tax](../tax/ARCHETYPE.md), detection and response in [security](../security/ARCHETYPE.md). Stages 1, 2 and 4
  work the same way for those firms.
- The same stages fit an in-house legal or shared-service team: "win" becomes intake and demand from the business,
  "bill" becomes cost allocation and outside-counsel spend (§6).

## 2. Stages at a glance

| # | Stage | Main processes | Modules | Public AI evidence |
|---|---|---|---|---|
| 1 | Win the work | Pursuit and proposals; client development | [pursuit-proposals](modules/pursuit-proposals.md), [client-development](modules/client-development.md) | Wide use, little measurement; 79% of 1,533 bid teams (all industries) used AI in 2025 [LOOPIO-TRENDS-2026] |
| 2 | Accept and price | Acceptance and risk; scoping and pricing | [acceptance-risk](modules/acceptance-risk.md), [scoping-pricing](modules/scoping-pricing.md) | Acceptance thin and vendor-heavy; pricing-model change well reported, AI pricing tools not |
| 3 | Staff and deliver | Staffing; delivery management; work production; quality review | [staffing-resourcing](modules/staffing-resourcing.md), [delivery-management](modules/delivery-management.md), [work-production](modules/work-production.md), [quality-review](modules/quality-review.md) | Densest in work production (legal); staffing thinnest; no firm publishes review error rates |
| 4 | Bill, collect, learn and run the firm | Billing and collections; knowledge management; talent and learning; firm finance | [billing-collections](modules/billing-collections.md), [knowledge-management](modules/knowledge-management.md), [talent-learning](modules/talent-learning.md), [firm-finance](modules/firm-finance.md) | Time capture has named users; firm return on AI is not measured; one randomised trial on skills [NBER-AUTOR-2026] |

## 3. Where the work types cluster

Use this in Diagnose to judge AI fit by step type. It summarises the module tables; the modules give the evidence.

| Work type | Typical steps | Usual AI pattern | Evidence strength |
|---|---|---|---|
| document-production | Proposals, SOWs, engagement letters, first drafts, status reports, time narratives | Draft from precedent or data; person edits and signs | Broad use; vendor and self-reported figures |
| research-synthesis | Legal or market research, record summaries, content and credential search, pitch research | Retrieve and summarise with citations; person verifies | Tool benchmarks only [VALS-VLAIRFEB-2025; STANFORD-MAGESH-2024] |
| review-assurance | Conflicts hits, playbook review, citation checks, pre-bill review, sign-off | Flag and suggest; person decides | Suggestion-acceptance telemetry from one vendor; no firm error rates |
| expert-judgment | Go/no-go, price model, staffing calls, advice, sign-off, partner pay, rates | AI informs; person owns | Stays human in every source read |
| data-reporting | Utilisation, budgets, WIP, realisation, matter profitability, AI usage | Ask in plain language; alerts; forecasts | Named PSA users; no forecast-error data |
| coordination-scheduling | Staffing bookings, plans, reminders, review routing, onboarding | Agents propose; people approve | Announced agents; no delegated staffing in production |
| client-interaction | Pitches, the AI-value conversation, scope negotiation, intake | Prepare and brief; the conversation stays human | Survey perceptions only |
| transaction-processing | Time entry, intake requests, e-billing submission, collections reminders | Capture and pre-fill; some automation | Time capture best evidenced; automation thin |
| software-systems | Ethical walls for AI, connectors to DMS and PSA, agent permissions | Configure and govern access | Vendor-described |

## 4. Stage by stage

### Stage 1. Win the work

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Qualify and respond to RFPs | Go/no-go; read the solicitation; screen client terms; find credentials; draft and review; submit | expert-judgment, review-assurance, research-synthesis, document-production | [pursuit-proposals](modules/pursuit-proposals.md) |
| Pitch and learn | Pitch research and rehearsal; answer the client's AI questions; win/loss debrief | research-synthesis, client-interaction, data-reporting | [pursuit-proposals](modules/pursuit-proposals.md) |
| Grow existing clients | Capture relationship data; map coverage; plan key accounts; prepare outreach | data-reporting, research-synthesis, expert-judgment | [client-development](modules/client-development.md) |
| Hold the AI-value conversation | Show what AI changed; agree client AI terms; act on feedback and retention risk | client-interaction, expert-judgment | [client-development](modules/client-development.md) |

### Stage 2. Accept and price

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Clear and accept | Intake request; conflicts search and clearance; KYC and AML; engagement risk approval; ethical walls | transaction-processing, review-assurance, expert-judgment | [acceptance-risk](modules/acceptance-risk.md) |
| Agree terms | Engagement letter with AI terms; capture OCGs and client AI restrictions; monitor after acceptance | document-production, review-assurance | [acceptance-risk](modules/acceptance-risk.md) |
| Scope and estimate | Scope capture; effort estimate and budget from past matters | client-interaction, data-reporting | [scoping-pricing](modules/scoping-pricing.md) |
| Price and propose | Choose the price model; draft the fee proposal or SOW; reasonableness and fee-rule check | expert-judgment, document-production, review-assurance | [scoping-pricing](modules/scoping-pricing.md) |

### Stage 3. Staff and deliver

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Staff the work | Turn demand into roles; forecast capacity; match and book; reallocate; supply decisions | coordination-scheduling, data-reporting, expert-judgment | [staffing-resourcing](modules/staffing-resourcing.md) |
| Run the engagement | Handoff; plan; meetings and status; risk and health; scope change; budget and margin; close-out | coordination-scheduling, document-production, data-reporting | [delivery-management](modules/delivery-management.md) |
| Produce the work | Set up the workspace; research; synthesise records; extract; first draft; review against a playbook | research-synthesis, data-reporting, document-production, review-assurance | [work-production](modules/work-production.md) |
| Check and release | Drafter's check; citation check; supervisory sign-off; record of the check; client disclosure; incident response | review-assurance, expert-judgment, client-interaction | [quality-review](modules/quality-review.md) |

Field-specific production replaces "Produce the work" for audit, tax and security; delivery, staffing and quality
review still apply around it.

### Stage 4. Bill, collect, learn and run the firm

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Time to cash | Time capture; narratives and codes; guideline checks; pre-bill review; e-billing; appeals; collections | transaction-processing, review-assurance, coordination-scheduling | [billing-collections](modules/billing-collections.md) |
| Reuse what the firm knows | Capture; curate; organise and secure; find; reuse; govern what AI may see | document-production, review-assurance, research-synthesis, software-systems | [knowledge-management](modules/knowledge-management.md) |
| Build the people | Intake sizing; screening; onboarding and AI training; supervised learning; evaluation; career paths | coordination-scheduling, expert-judgment, review-assurance | [talent-learning](modules/talent-learning.md) |
| Run the firm's economics | Fee mix; rate round; realisation; matter profitability; AI investment and cost; partner economics; capital | expert-judgment, data-reporting | [firm-finance](modules/firm-finance.md) |

## 5. Layers that cut across every stage

- **Data layer: time, matter, documents and relationships.** Most AI steps depend on joined data that firms hold in
  separate systems: practice management or PSA (matters, time, budgets), the DMS (documents), CRM (relationships) and
  HR systems (skills). Thomson Reuters Institute's premortem (fictional scenarios) has agentic pilots failing on
  undocumented exceptions and fragmented storage [TRI-PILOTFAIL-2026]. In one vendor-commissioned resource-management study 47% cite poor or fragmented
  data [KANTATA-RMI-2026]; 78% of 123 law and accounting firm partners in a vendor survey say relationship data is hard
  to act on [INTROHIVE-LAWSITES-2026].
- **Client AI terms.** What each client allows enters at stage 2 and is checked again at production, release and the
  bill (acceptance-risk, quality-review, billing-collections). Some clients demand AI savings and others forbid AI
  without permission [TRI-LEGALWEEK-2026].
- **Governance of the firm's own AI.** Policy, approved tools, training before access and review rules apply at every
  stage ([guardrails.md](guardrails.md); work-production and quality-review hold the steps).
- **AI cost.** Seat licences are moving toward usage-based charges, which turns AI into a per-matter cost
  [TRI-METER-2026; LEGORA-CBP-2026]; see [economics.md](economics.md).

## 6. Firm-type and in-house variants

| Setting | What changes in the chain | Where the evidence is |
|---|---|---|
| Law firms | Conflicts and OCGs are heavy at stage 2; e-billing and client guidelines at stage 4; the hourly fee dominates | Densest public record (bars, courts, ILTA, TRI, Harvey, Legora) |
| Consultancies and implementation firms | SOWs and estimates at stage 2; PSA-run staffing and delivery at stage 3; outcome-linked fees more common | PSA vendors (Certinia, Kantata); press on McKinsey, PwC, Accenture |
| Accounting and advisory firms (firm side) | Acceptance includes independence; production handed to assurance or tax; PE capital at stage 4 | Assurance and tax archetypes; accounting press |
| Engineering and architecture | Proposals (including SF-330s) at stage 1; project delivery and utilisation at stage 3 | One annual benchmark [DELTEK-CLARITY-2026] |
| In-house legal and legal operations | Stage 1 is intake from the business; stage 2 includes sourcing to outside firms; stage 4 is invoice review and spend | CLOC, TRI legal-department data, vendor surveys |
| Other shared-service teams (finance, HR) | Same stages for internal clients | Almost no public evidence; use the library functions |

## 7. Sources

Keys not listed here are in [sources.md](sources.md).

- **TRI-PILOTFAIL-2026**: Thomson Reuters Institute, *Why your agentic AI pilot probably will fail (and what that says about you) (introduces TRI's premortem feature)* (press, 2026-02-20). https://www.thomsonreuters.com/en/institute/articles/feature-agentic-ai-pilot-failure
