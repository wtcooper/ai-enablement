# Professional-services economics

Last researched 2026-10-19. Use this in Frame (pricing exposure, why now), in Make the case (baselines and the cost
stack) and whenever fees, rates, margins, budgets or ownership come up. Deal-level pricing detail is in
[scoping-pricing](modules/scoping-pricing.md), time-to-cash in [billing-collections](modules/billing-collections.md)
and firm-level finance use cases in [firm-finance](modules/firm-finance.md); this file gives the frame and the numbers
a leader will ask for. Most figures are US law market data from the Thomson Reuters Institute (TRI, part of a group
that sells legal AI), vendor surveys or press-relayed firm statements; labels say so. Samples differ, so do not average
them. Source keys in brackets resolve in §10 or in [sources.md](sources.md).

## Contents

1. [How the business makes money](#1-how-the-business-makes-money)
2. [Scale and growth](#2-scale-and-growth)
3. [Key metrics and benchmarks](#3-key-metrics-and-benchmarks)
4. [Fees and pricing models](#4-fees-and-pricing-models)
5. [Cost structure, including AI cost](#5-cost-structure-including-ai-cost)
6. [Pricing pressure from AI](#6-pricing-pressure-from-ai)
7. [Capital and ownership](#7-capital-and-ownership)
8. [In-house budgets](#8-in-house-budgets)
9. [What to measure in a conversation](#9-what-to-measure-in-a-conversation)
10. [Sources](#10-sources)

## 1. How the business makes money

- **People's time, sold with a margin.** Most firms sell expert hours, directly (hourly fees) or indirectly (fixed fees
  estimated from hours). About 90% of US legal dollars still flow through hourly arrangements [TRI-SOTLM-REPORT-2026].
- **Leverage.** Profit rises when juniors do work that clients pay for at rates above their cost while partners
  originate and supervise. Junior work also trains the next partners, so the pyramid is both a profit engine and a
  pipeline ([workforce.md](workforce.md)).
- **The realisation chain.** Value worked becomes value billed and then cash collected; write-downs and write-offs
  sit between them, decided mostly by partners ([billing-collections](modules/billing-collections.md)).
- **Partnership payout.** The traditional law-firm structure leaves little cash in reserve once partners are paid,
  while AI platforms need substantial upfront investment; that is one reason outside capital is arriving (§7)
  [HK-AMLAW-2026].
- **Where AI hits.** On hourly work, AI efficiency lowers revenue unless the firm sells more work, reprices or changes
  the fee basis; on fixed or value fees it can raise margin ([scoping-pricing](modules/scoping-pricing.md) `#17`).
- **In-house teams** are cost centres: budgets, headcount, technology and outside-counsel spend (§8).

## 2. Scale and growth

Latest reported years; currencies, years and definitions differ, so do not rank the firms.

| Organization (type) | Figure | Source |
|---|---|---|
| PwC network (accounting and advisory) | FY to 30 Jun 2026 revenue $60.2bn, +5.7% in US dollars (+3.5% constant currency); advisory +3.0%, assurance +2.6% | [AT-PWC-2026] |
| Accenture (consulting and technology services) | FY26 revenue $74.18bn (+6% USD); consulting $36.88bn (+5% USD, +3% local); consulting bookings $40.86bn | [ACCENTURE-Q4FY26] |
| Crowe (accounting) | $1.4bn revenue, 539 partners; No. 12 on Accounting Today's Top 100 | [AT-CROWE-KKR-2026] |
| US law market (Am Law 100 and others) | Q1 2026 worked rates up almost 10%, overall demand up 2.7%, Law Firm Financial Index (LFFI) flat at 55; Q2 2026 index up sharply | [TRI-LFFI-Q1-2026; TRI-LFFI-Q2-2026] |
| US Big Law demand (Citi data) | Demand for hours +4.2% in H1 2026 against a normal of about 1.5% | [BLOOMBERG-AICOST-2026] |
| Technology consulting market | Spend forecast to grow 7.5% in 2026 (Source Global Research) | [SOURCE-PRECISION-2026] |
| Architecture and engineering (896 firms) | Revenue forecast +9.5% against staff growth of 1.2% | [DELTEK-CLARITY-2026] |

None of these sources attributes growth or decline to AI. The counter-narrative to "collapse" is that aggregate
revenue is still rising; the pressure shows in pricing, mix and headcount ([disruption.md](disruption.md)).

## 3. Key metrics and benchmarks

| Metric | What it means | Benchmarks (sources differ; not comparable across rows) |
|---|---|---|
| Realisation | Share of worked value collected | Average 88% in Clio's 2025 data (vendor) [CLIO-BILLABLE-2026]; an MSO adviser flags below 85% as an improvement opportunity [WINSTON-PE-2026] |
| Write-downs and write-offs | Value cut before or after the bill | 89% of BigHand respondents report rising write-offs [BIGHAND-FINANCE-2026]; about 300 hours of partners' own write-downs per partner a year [TRI-EFFICIENCY-2025] |
| Worked rates | Rates on hours worked | Am Law 100 almost +10% in Q1 2026; Midsize firms +5.3% [TRI-LFFI-Q1-2026; TRI-LFFI-MIDSIZE-2026]; 96% of BigHand respondents raised rates [BIGHAND-FINANCE-2026] |
| Profit and fees per lawyer | Firm performance | End-2025: profit per lawyer 8.4% and fees worked per lawyer 16.8% above pre-2022 levels, mostly from rate rises [TRI-SOTLM-2026] |
| Leverage | Associate hours relative to partners | Associate demand leverage 1.55 in Q4 2025 (record), 1.47 in Q1 and Q2 2026 [TRI-LFFI-LEVERAGE-2026]; non-equity to equity partner hours highest since late 2018 [TRI-LFFI-Q2-2026] |
| Billable utilisation | Share of available time billed | Services firms 66.4% in 2025, lowest in SPI's history (75% treated as optimal) [DELTEK-SPI-2026]; A&E just under 60% [DELTEK-CLARITY-2026] |
| Project delivery | Overrun and on-time delivery | Overrun 10.7%, on-time 73.8%, project margin 37.7% across 500+ services firms [DELTEK-SPI-2026] |
| Operating profit | Firm margin | A&E operating profit 16.7%, down year on year [DELTEK-CLARITY-2026] |
| Lockup | Time from work to cash | 90% of BigHand respondents report higher lockup [BIGHAND-FINANCE-2026] |
| Overhead | Non-fee-earner cost share | An MSO adviser flags overhead above 55% of revenue [WINSTON-PE-2026] |

SPI's benchmark is published by Deltek, which sponsors it; BigHand and Clio sell to law firms.

## 4. Fees and pricing models

| Model | Where it is common | What the evidence says |
|---|---|---|
| Hourly | Law; much advisory | About 90% of US legal dollars [TRI-SOTLM-REPORT-2026]; 78% of tax firms bill hourly [TRI-CHARGING-2026]; almost two-thirds of 736 law-firm professionals say pricing is unchanged [TRI-FOP-LAW-2026] |
| Fixed, capped and AFAs | Repeatable legal work; consulting phases; compliance | 54% of UK law firms expect more fixed-fee billing in the next 12 months [CMS-TRENDS-2026]; 49% of BigHand respondents see rising AFA demand [BIGHAND-LF-2026] |
| Outcome-linked | Consulting; IT services | McKinsey says about a quarter of global fees are outcome-based (a rounded, self-reported figure; it says the model predates AI) [BI-MCKINSEY-2025]; in HFS buyer data on AI-enabled IT and business services, 20% of current engagements are outcome-based [HFS-SAS-2026] |
| Hybrid (base plus outcome) | Consulting and services buyers' stated preference | 56% of surveyed buyers prefer a base fee plus outcome kicker (adjacent IT and BPO market) [HFS-SAS-2026]; Stanford's framework treats hybrid as the usual resting point [STANFORD-DEL-2026] |
| Subscription and per-document | Productised services; AI-native firms | PwC's US CEO said some services become subscription tools "without a PwC person in the loop" [CPAPA-PWC-2026]; AI-native law firms sell flat bundles or per-document rates ([scoping-pricing](modules/scoping-pricing.md) `#21`) |

**How firms set prices today.** 35% of BigHand's legal-finance respondents default to standard rates and 28% copy a
past matter unchanged [BIGHAND-LF-2026]. Pricing change is gated by measurement: Stanford's rules are to invest in
measurement before outcome pricing and to check whether attribution is the binding constraint [STANFORD-DEL-2026],
and 7.3% of resource managers in one study use outcome data routinely in staffing [KANTATA-RMI-2026]. Billing rules on
AI-assisted work are in [guardrails.md](guardrails.md) §5.

## 5. Cost structure, including AI cost

- **People** are the main cost: salaries, bonuses and partner distributions. A Thomson Reuters estimate puts the cost
  of replacing a professional at $232,000 [TR-FOP-REPORT-2026].
- **Technology and knowledge spend are rising fast in law:** technology +39.3% and KM +37.2% from 2021 to 2025, about
  11% and 10% in 2025 alone [TRI-SOTLM-2026]. Q2 2026 technology plus KM spend +11.6% [TRI-LFFI-COSTS-2026].
- **Large AI commitments:** PwC reports $3bn invested network-wide in AI and other capabilities and 330,000+ people
  trained [AT-PWC-2026]; Kirkland & Ellis's reported $500m AI platform commitment came with no ROI benchmarks
  [BLOOMBERGLAW-KIRKLAND-2026].
- **AI is becoming a variable cost.** Vendors are moving from seats to consumption pricing: Legora prices Agent Pro by
  consumption with matter attribution [LEGORA-CBP-2026]; Harvey token use rose 14x in six months [ARTLAW-HARVEY14X-2026];
  a firm's guide notes one major model vendor changed rates in ten of the last 13 months [BAKERDONELSON-TOKENS-2026].
  Practitioner figures: about 1% of revenue as the level firms are settling on (one officer's statement) and a $2
  PowerPoint [TRI-METER-2026]; $50-$350 per attorney a month, about 30% on top of tool cost (one estimate)
  [BLOOMBERGLAW-TEXAS-2026].
- **Who pays for AI.** General AI subscriptions are overhead; matter-specific costs can reach a client only with
  disclosure, at cost, and no markup without informed written consent (California) [CALBAR-GENAI-2026]. Keypoint Law's
  CEO expects clients to be "annoyed" if firms pass AI costs on [LAWYERSWEEKLY-KEYPOINT-2026].
- **Return is not measured.** 18% of organisations track AI ROI and 40% do not know [TR-AIPS-2026]; 85% of law firms and
  75% of corporate legal respondents collect no AI ROI data or are unsure [TRI-GREATDISCONNECT-2026]. 84.8% of 245
  services firms say AI saves time; the share saying it generates revenue is behind SPI's paywall [SPI-AI-2026].

## 6. Pricing pressure from AI

**From clients**
- 78% of corporate clients call AI-enabled quality gains very important or essential; 6% say most or all providers
  deliver them; 32% have reconsidered, or plan within 12 months to reconsider, providers they see as falling behind
  (vendor survey, client subset size not stated) [TR-FOP-REPORT-2026].
- 59% of 657 in-house respondents see no GenAI savings from law firms yet, and 61% plan to push for change in delivery
  and pricing (vendor co-published) [ACCEVERLAW-2025]. In another vendor survey, 73% of in-house lawyers who knew their
  firms used AI believed the firm keeps all or most of the savings [JURO-INHOUSE-2026].
- Clients at Legalweek asked for matter-level savings and line-item AI transparency; others said they will not pay for
  certain services done by AI [TRI-LEGALWEEK-2026].
- KPMG's audit fee from its auditor reportedly fell about 14% after KPMG argued, among other things, that AI should cut
  the work (secondary report of an FT story) [YAHOO-KPMG-2026]; audit detail is in the assurance archetype.

**From the rules.** Hourly billers may charge only for time actually spent; AI-saved time cannot be billed. That makes
the fee basis, not the tool, the lever ([guardrails.md](guardrails.md) §5).

**Counter-signals.** Rates and demand are strong in law [TRI-LFFI-Q1-2026; BLOOMBERG-AICOST-2026]. TRI warns that firms
using AI mainly to justify higher billing are exposed if an AI investment bubble bursts (a warning, not an observed
event) [TRI-SOTLM-2026]. One GC asks whether partner rates are rising to offset associate hours lost to AI
[TRI-STANDOUT-2026].

**What this means for a leader.** Decide where freed hours go (resell, reprice, give back, invest) before rolling out,
and say it in the engagement terms; scenarios are in [disruption.md](disruption.md) §3.

## 7. Capital and ownership

Detail and scenarios are in [disruption.md](disruption.md) §5 and [firm-finance](modules/firm-finance.md) `#15`-`#17`.

- **Accounting is furthest along.** Crowe closed a KKR investment in August 2026 for talent, technology and innovation,
  separating attest from non-attest services, then launched CroweONE, a shared ownership plan open to all employees
  [AT-CROWE-KKR-2026; AT-CROWE-2026]. Grant Thornton agreed to buy CBIZ for $5bn in cash with New Mountain Capital's
  backing (announced, expected to close in Q4 2026) [BGOV-GTCBIZ-2026]. A law firm's publication says PE holds a stake
  in roughly a third of the 30 largest US accounting firms (not independently verified) [FOXROTHSCHILD-MSO-2026].
- **Law uses workarounds.** Rule 5.4 bars fee-sharing with non-lawyers in most US states; investors use management
  services organisations (MSOs) that fund the back office, including AI [BLOOMBERGLAW-AZ-2026; BESTLAW-WSHB-2026].
- **Investors are re-reading the model.** An Apax co-CEO called hourly-billing bookkeeping-type firms with no regulated
  audit work vulnerable (FT via a Dutch outlet) [VANMORGEN-SUPERRETURN-2026]. Fewer UK mid-tier firms are considering PE
  than in previous years [ICAEW-MIDTIER-2026].

## 8. In-house budgets

- In a vendor survey, 66% of legal departments received budget increases averaging 12%, and 90% still face efficiency
  pressure (sample not stated) [AXIOM-GC-2026].
- 44% of 130+ in-house lawyers were somewhat or very confident they could halve outside-counsel spend and still manage
  risk (vendor survey) [JURO-INHOUSE-2026].
- The share of GCs naming technology a top strategic priority doubled from 2025 to 2026 [TRI-LDOR-2026].
- UBS's legal department checks outside-counsel bills line by line through UnitedLex ([firm-finance](modules/firm-finance.md) `#04`).
- Finance, HR and other shared-service teams that run like firms: no public budget data found.

## 9. What to measure in a conversation

Nobody publishes these for AI yet; recommend them as the leader's baseline before any rollout:
- realisation and write-offs on AI-assisted versus other matters of the same type;
- share of fees by pricing model, and its direction;
- AI cost per matter and as a share of revenue; who absorbs a usage overrun;
- where freed hours went (resold, repriced, given back, training);
- utilisation by band, not just average; revenue per head and margin against AI spend;
- for in-house teams, outside spend moved in house and its quality.

## 10. Sources

Keys not listed here are in [sources.md](sources.md).

- **BAKERDONELSON-TOKENS-2026**: Baker Donelson, *AI Tokenomics Guide: Understanding Token-Based AI Pricing for Legal Technology (Justin Daniels)* (firm, 2026-08-20). https://www.bakerdonelson.com/webfiles/Bios/Token-Pricing-Guide-for-Clients-August-2026.pdf
- **BIGHAND-FINANCE-2026**: BigHand, *2026 Annual Law Firm Finance Report (landing page; 800+ senior finance and legal leaders; vendor)* (survey, 2026-01-21). https://www.bighand.com/en-us/resources/whitepapers/2026-annual-law-firm-finance-report/
- **BLOOMBERGLAW-TEXAS-2026**: Bloomberg Law, *AI, Billing Emerge as Crossroads for Texas Law Firms and Clients* (press, 2026-04-21). https://news.bloomberglaw.com/antitrust/ai-billing-emerge-as-crossroads-for-texas-law-firms-and-clients
- **CLIO-BILLABLE-2026**: Clio, *Will AI mean the death of the billable hour in legal? (cites Clio's 2025 Legal Trends data; vendor)* (vendor, 2026-02-21). https://www.clio.com/blog/death-of-the-billable-hour-legal-ai/
- **CMS-TRENDS-2026**: CMS (law firm), *The Trends Redefining Legal Service Delivery* (firm, 2026-02-12). https://cms.law/en/gbr/publication/the-trends-redefining-legal-service-delivery
- **HK-AMLAW-2026**: Holland & Knight, *Firms Need Capital to Pay for AI Tools. Could PE Investment Be the Solution? (summary of an American Lawyer article)* (firm, 2026-04-20). https://www.hklaw.com/en/news/intheheadlines/2026/04/firms-need-capital-to-pay-for-ai-tools-could-pe-investment
- **TRI-CHARGING-2026**: Thomson Reuters Institute, *If AI can do the work, then what are you actually charging for?* (press, 2026-10-02). https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for
- **TRI-EFFICIENCY-2025**: Thomson Reuters Institute, *The AI-driven future of legal efficiency: How can law firms reclaim millions in lost revenue while enhancing client value?* (press, 2025-04-14). https://www.thomsonreuters.com/en/institute/reports/ai-driven-legal-efficiency-white-paper-2025
- **TRI-FOP-LAW-2026**: Thomson Reuters Institute, *What the '2026 Future of Professionals Report' says law firm leaders should be doing now* (survey, 2026-07-21). https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-law-firms-paper-2026
- **TRI-GREATDISCONNECT-2026**: Thomson Reuters Institute, *The great AI disconnect: Firms and legal departments are not communicating about AI usage* (survey, 2026-03-18). https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect
- **TRI-LFFI-MIDSIZE-2026**: Thomson Reuters Institute, *Q1 2026 LFFI analysis: Midsize law firms* (survey, 2026-05-26). https://www.thomsonreuters.com/en/institute/articles/q1-2026-lffi-analysis-midsize-law-firms
- **YAHOO-KPMG-2026**: Yahoo Finance, *Big Four accounting firm's bold demand is a warning about AI adoption* (press, 2026-02-10). https://finance.yahoo.com/news/big-four-accounting-firms-bold-015348056.html
