# Tax disruption scenarios

Last researched 2026-10-17. Use this at unit or organization scope, in Frame (how exposed is this business) and in
Reimagine lens 4 (reinvent). Each scenario separates what exists, what is forecast and what would have to be true. No
source assigns probabilities; neither does this file. Source keys in brackets resolve in §9 or in
[sources.md](sources.md).

## Contents

1. [The short version](#1-the-short-version)
2. [Scenario 1: agentic preparers](#2-scenario-1-agentic-preparers)
3. [Scenario 2: AI-native entrants and roll-ups](#3-scenario-2-ai-native-entrants-and-roll-ups)
4. [Scenario 3: the fee model shifts](#4-scenario-3-the-fee-model-shifts)
5. [Scenario 4: continuous compliance](#5-scenario-4-continuous-compliance)
6. [Scenario 5: the authority computes more of the return](#6-scenario-5-the-authority-computes-more-of-the-return)
7. [Scenario 6: new services around AI](#7-scenario-6-new-services-around-ai)
8. [Exposure by service line](#8-exposure-by-service-line)
9. [Sources](#9-sources)

## 1. The short version

| Scenario | Evidence status | Who it hits first | Signal to watch |
|---|---|---|---|
| 1. Agentic preparers | Products shipped; quality unmeasured; one adopter found none ready | Small and mid-size firms' 1040 and 1065 work; offshore preparers | Independent error rates; vendors' K-1 coverage |
| 2. AI-native roll-ups | Funded and buying; results company-stated; PE is the larger wave | Owner-managed small firms | Deal volume; buyers' margins |
| 3. Fee model shifts | Statements of intent; regulator friction | Hourly advisory and large-firm compliance | IRS answer to the AICPA; published value-priced contracts |
| 4. Continuous compliance | Vendor framing; authority mandates real | Indirect tax and in-house data teams | E-invoicing mandates; agent-executed filings |
| 5. Authority computes more | Policy and research; no AI-driven return-free system live | Retail and simple-return preparers | Pre-population pilots; authority data timing |
| 6. New services around AI | Platform sales and advice demand announced | Big Four and specialist advisers | Agent-platform revenue; OECD guidance on AI transactions |

**The mismatch scenario matters most in a conversation.** Deloitte's framework crosses a company's AI adoption with its
tax authority's, and calls "company advanced, authority not" more realistic for most multinationals; an authority
ahead of the company means "heightened audit and dispute exposure" [DELOITTE-TTT-2026].

## 2. Scenario 1: agentic preparers

**The picture.** An agent drafts the return from source documents; a professional reviews and signs.

- **Exists.** Thomson Reuters Ready to Review (Nov 2025), Black Ore Tax Autopilot (open from 29 Apr 2026), Basis (an
  agent completed a 1065, Feb 2026), Accrual, and Perplexity's consumer agent (Apr 2026) [TR-COCOUNSEL-2025;
  BLACKORE-2026; BASIS-2026; CPAPA-ACCRUAL-2026; PERPLEXITY-2026]. OpenAI reports a 7,000-return pilot with Crete firms
  (its own publication as co-developer) [OPENAI-CODEX-2026].
- **Readiness evidence is mixed to negative.** WCG tested five vendors and committed to none, citing K-1 gaps, the
  proprietary-platform "reset" risk and the handoff into its tax software [WCG-2026]; unaided models compute fewer than a
  third of simplified returns correctly [COLUMN-TAXCALCBENCH-2025].
- **Forecast.** Industry voices at a vendor's summit predicted autonomous individual preparation by 2027, entities soon
  after [BLACKORE-SUMMIT-2026]. Thomson Reuters offers firms three paths: elevate, scale, reimagine [TR-FOP-2026].
- **What would have to be true.** Exception handling that does not strand work; independent error measurement; review
  that keeps pace with volume; a junior learning path ([workforce.md](workforce.md) §6).
- **Counter-view.** Sala: models "conflate tax preparation with tax practice", and AI cannot carry culpability
  [SALA-TAXNOTES-2026].
- **For the leader.** Run a parallel test on last year's returns; compare against the offshore cost, not only onshore.

## 3. Scenario 2: AI-native entrants and roll-ups

- **Exists.** Multiplier bought a 12-person cross-border boutique and says AI more than doubled its margin
  [MULTIPLIER-2025]. Crete, Thrive-backed, planned over US$500m of acquisitions and reported over US$300m revenue, 20+
  firms and 900 staff at Jun 2025 [CRETE-REUTERS-2025]. Its investor says the model works best on small firms, which are
  "more open to changing their existing processes" [MULTIPLIER-2025].
- **The larger wave is private equity.** 10 of the top 20 US firms are or will soon be PE-owned [CFOBREW-2026]; Grant
  Thornton Advisors agreed to buy CBIZ at US$5.0bn [GT-CBIZ-2026]; PE investors pay more for firms using AI to expand
  capacity [CPATL-PEVAL-2026].
- **Software-first entrants sell to firms instead.** Basis raised US$100m at a US$1.15bn valuation [BASIS-2026]; Accrual
  launched with US$75m [CPAPA-ACCRUAL-2026].
- **What would have to be true.** Bought practices accept new processes; quality holds under signing duties; margins
  survive integration. All results so far are company-stated.
- **For the leader.** Ask what a buyer would see in the practice's EBITDA today, and what the leader would change if a
  roll-up bought the nearest competitor ([economics.md](economics.md) §6).

## 4. Scenario 3: the fee model shifts

- **Pressure exists.** Nearly half of tax and audit professionals feel pressure to generate financial gains from AI; a
  third say their firm has not adapted its commercial model [TR-FOP-2026].
- **Stated intent, not published prices.** PwC's US tax leader says time is "becoming less and less" relevant; RSM asks
  whether halved hours are "margin for me or … price reduction"; RKL pilots value pricing with "several dozen" clients
  [BTAX-PRICING-2026].
- **Regulatory friction.** OPR says billing manual time not spent may breach section 10.27; the AICPA says that appears
  not to allow value pricing and has asked for clarification [IRS-OPR-2026; JOFA-FEES-2026].
- **Small firms are already off the clock.** 3% bill tax preparation hourly in one customer survey [IGNITION-2025].
- **Not found.** Any firm publishing outcome-contingent fees on tax work; Circular 230 bars most contingent fees anyway
  [ECFR-10.27].
- **For the leader.** Treat pricing, engagement letters and AI records as one design decision.

## 5. Scenario 4: continuous compliance

- **Exists as vendor framing.** Avalara's agents are "always on, always ready", filing "upon approval"; Thomson Reuters
  sells "touchless compliance … by default, manual by exception"; Sovos plans issue detection before deadlines
  [AVALARA-AGENTIC-2025; TR-SUTAI-2026; SOVOS-SOVI-2026].
- **Authority drivers are real.** OECD administrations are moving toward real-time information-sharing pilots
  [OECD-FTA-2025]; France's e-invoicing mandate went live in Sep 2026 [SOVOS-FRANCE-GOLIVE-2026]; ViDA brings intra-EU
  digital reporting from 1 Jul 2030 [EC-VIDA-2025].
- **Agentic commerce adds a collection question.** AI systems "can't bear tax obligations", so the company operating
  the agent may have to collect; the US$3-5 trillion by 2030 figure is a McKinsey forecast cited by Bloomberg Tax
  [BTAX-AGENTICCOMMERCE-2026].
- **What would have to be true.** Upstream data quality, clear ownership of AI-driven outcomes and audit trails; Deloitte
  lists these in all four of its scenarios [DELOITTE-TTT-2026].
- **For the leader.** Indirect tax and in-house data teams move first; see [indirect-tax](modules/indirect-tax.md) and
  [data-technology](modules/data-technology.md).

## 6. Scenario 5: the authority computes more of the return

- **Feasibility, pre-AI.** A 2022 NBER simulation estimated 42-48% of US returns could be accurately pre-populated from
  third-party and prior-year data, with accuracy falling as income rises [NBER-PREPOP-2022].
- **The constraint is data, not AI.** A May 2026 Direct File policy report says pre-population depends on faster
  third-party information returns and that "we cannot eradicate tax returns altogether" within the current system
  [ESP-DIRECTFILE-2026].
- **Authorities want it.** The IRS CEO frames AI as lifting compliance to the mid-90s with flat headcount (a forecast)
  [IRS-AIFIRST-2026]; ATO prompts taxpayers during online filing to check unusual entries
  ([controversy](modules/controversy.md)).
- **Not found.** An AI-driven, return-free or authority-computed filing system live anywhere.
- **What would have to be true.** Timely third-party data; authority capacity (GAO found AI skills eroded) [GAO-2026].
- **For the leader.** Simple-return preparers face the most exposure; advisory built on the return the least.

## 7. Scenario 6: new services around AI

- **Selling agents and platforms.** EY's Tax Agent Factory builds agents with clients; KPMG's Digital Gateway lets
  clients use Claude-built tax agents [EY-TAXLABS-2025; KPMG-ANTHROPIC-2026].
- **Managed services.** KPMG says 40% of companies have adopted managed services at scale in tax (its survey); its
  leader says the market is "approaching $1B" (his experience) [KPMG-MS-2026].
- **Advice on AI itself.** Companies asked the OECD how to characterise AI transactions between affiliates
  [OECD-INTRAGROUP-2026]; nexus and value creation by AI were debated at the D.C. Bar tax conference [DCBAR-TAX-2026];
  who collects tax at agent checkout is open [BTAX-AGENTICCOMMERCE-2026].
- **Defence against authority AI.** As authorities automate selection and notices, practitioners need notice workflows
  and documented positions ([controversy](modules/controversy.md)).
- **What would have to be true.** Clients pay for platforms and advice they cannot build; no volumes or fees are
  disclosed for any of these offers.

## 8. Exposure by service line

| Service line | Threat | Change a lot | Mainly help | Why (see module) |
|---|---|---|---|---|
| Individual and small-business returns | High for simple returns | Review, pricing, offshore model | Complex K-1-heavy returns | Agentic preparers and pre-population target it first |
| Corporate compliance | Low | Data, calendar, credits | Review analytics | In-house teams expect flat headcount [KPMG-DE-2026] |
| Provision and Pillar Two | Low | Data pipelines and XML | Disclosures | The hard part is data and filing formats [FGS-GIR-2026] |
| Indirect tax | Medium for outsourced filing | Real-time reporting, agent filing | Classification and certificates | Vendors moving to agent-executed filing |
| Transfer pricing | Medium for documentation volume | Local files and benchmarking | Audit defence | The IRS wants formulas and explained AI use [IRS-LBI-TP-2026] |
| Controversy | Low | Notice handling | Defence against authority analytics | The authority side is scaling AI [GAO-2026] |
| Research and advisory | Medium for routine research | Drafting, pricing | Planning, diligence, advice on AI | Clients arrive with chatbot answers |
| Tax data and technology | Low | Ownership and controls | Everything above | Grows as the other lines automate |

These ratings are the advisor's synthesis of the evidence above, not a source's forecast. Revisit them with the leader's
own revenue mix.

## 9. Sources

Keys not listed here are in [sources.md](sources.md).
