# Security objections

Last researched 2026-10-17. Use this when a practitioner pushes back. Each response gives the evidence and its
provenance; concede what is true. Objections about one step (for example "AI will wave real attacks through" in
triage) are in the module files' "Common objections" sections, especially operations §9. Source keys in brackets
resolve in §8 or in [sources.md](sources.md).

## Contents

1. [Quality and trust](#1-quality-and-trust)
2. [Regulation, liability and insurance](#2-regulation-liability-and-insurance)
3. [Economics and providers](#3-economics-and-providers)
4. [People and skills](#4-people-and-skills)
5. [Securing the AI itself](#5-securing-the-ai-itself)
6. [Vulnerability volume and hype](#6-vulnerability-volume-and-hype)
7. [How to respond well](#7-how-to-respond-well)
8. [Sources](#8-sources)

## 1. Quality and trust

| Objection | Response |
|---|---|
| "The agentic SOC is just marketing." | Partly right: Forrester says the term is used loosely, and CrowdStrike labels key features pre-beta or preview [FORRESTER-RSAC-2026; CROWDSTRIKE-AGSOC-2026]. But providers report agents at scale in their own operations (vendor-reported) [ARCTICWOLF-AURORA-2026], and in-house teams publish their own results (operations `#01`, `#09`). Judge by evidence on your own alerts, not the label. |
| "We can't trust AI verdicts." | Reasonable. 63% of SANS respondents report significant shortcomings (via a vendor summary) [SANS-AI-2026], and one replay benchmark found standard designs missed 40.4% or more of attack alerts [ARXIV-2610.10608]. The same benchmark shows design matters: a challenge-and-judge design cut misses to 3.1% while escalating 18.4% of alerts to analysts. Start with high-confidence false positives, sample closures and measure in your environment. |
| "We keep a human in the loop, so we're safe." | Only 36% in ISACA's poll say humans approve most AI actions before execution, and 20% do not know [ISACA-AIPULSE-2026]. A reviewer without evidence, time or sampling rules is not a control ([guardrails.md](guardrails.md) §6). |
| "Vendors' numbers prove it works." | Almost every outcome figure is vendor-published or self-reported; 7AI's "hours saved" has no stated method [SEVENAI-2026]. No independent production miss or override rate was found for any module ([state-of-ai.md](state-of-ai.md) §8). Ask how misses were counted and run a side-by-side test. |

## 2. Regulation, liability and insurance

| Objection | Response |
|---|---|
| "Regulators won't let us use AI for detection and response." | In the texts read, regulators encourage it, with data-protection conditions [EURLEX-NIS2-2022, recital 51; EC-ACTIONPLAN-2026; NYDFS-AI-2024]. No rule found bans AI triage or mandates human approval of SOC actions; what binds is oversight, vendor diligence, data protection and reporting. |
| "If the AI is wrong, the CISO goes to jail." | The SEC's case against SolarWinds and its CISO was dropped; the claims that survived to that point concerned a published security statement, not tool choices [HUNTON-SOLARWINDS-2024; COVINGTON-SOLARWINDS-2025]. NIS2 lets management bodies be held liable, and DORA gives the management body ultimate responsibility for ICT risk [EURLEX-NIS2-2022, Art 20; EURLEX-DORA-2022, Art 5]. But no case has tested agent-caused harm [DARKREADING-LIABILITY-2026]. |
| "The SEC rules are going away." | Not yet: no rescission found, and CRA reporting is live while CIRCIA and UK rules approach [DEBEVOISE-8K-2026; EC-CRAREPORTING-2026; COVINGTON-CIRCIA-2026; HANSARD-CSRB-2026]. |
| "The AI Act doesn't apply to security teams." | Unproven either way. Annex III covers safety components of critical digital infrastructure; whether a given tool qualifies needs legal analysis. High-risk duties start 2027-12-02 [EC-AIACT-2026; AIACT-EXPLORER-2024]. |
| "Our cyber policy covers AI." | Possibly. Most cyber policies do not yet exclude AI, per a BIS/FSI paper; one carrier confirmed affirmative AI wording; general-liability AI exclusions exist [BIS-FSI75-2026; BEAZLEY-AICYBER-2026; INDAGENT-VERISK-2025]. Read your wording. |

## 3. Economics and providers

| Objection | Response |
|---|---|
| "AI will cut our budget and headcount." | 69% of CISOs do not expect AI to reduce existing headcount; software, including AI, is already 35% of budgets (expectations and survey) [IANS-BUDGET-2026]. Budget cuts are already common: 36% of ISC2 respondents' organizations had them in 2025 [ISC2-WORKFORCE-2025]. |
| "We have no budget for this." | 38% of organizations fund AI security outside the security budget; a distinct AI line is associated with more funding growth (correlation) [IANS-BUDGET-2026]. Tie the case to the business's AI programme and to board focus on security, which IANS links to the largest average increases. |
| "Our MDR will pass AI savings on to us." | Gartner expects providers to absorb efficiency gains rather than cut prices (a forecast, per a vendor summary) [INTEZER-GARTNERMDR-2026]. Ask for outcome metrics, closure accuracy and human-validation rates at renewal. |
| "An AI SOC is cheaper than our provider." | Price units exist (up to 4,000 investigations per AI analyst a year, vendor) [DROPZONE-PRICING-2026], but no independent cost-per-investigation figure was found, and someone in house must own the agents ([disruption.md](disruption.md) §3). |
| "Consolidating on one platform will save money." | No source measured savings; Forrester says consolidation does not remove tools, skills or complexity and warns about later pricing [FORRESTER-RSAC-2026; FORRESTER-PV-2026]. |
| "Security AI has no payoff." | Among IBM/Ponemon's breached organizations, extensive security AI and automation coincided with USD 1.93M lower average breach cost than using none; a correlation, not a causal estimate [IBM-CODB-2026]. |
| "A warranty makes the provider accountable." | Arctic Wolf's warranty is up to USD 3M, subject to terms and coverage requirements [MSSPALERT-AW-2026]. Read the terms; no source shows fees that move with outcomes. |
| (Provider) "Clients won't accept AI in our service." | Gartner's MDR definition now says "AI-augmented, human-led" and tells buyers to ask which parts are AI-run [EXPEL-GARTNERMDR-2026]. Clients are being told to expect it; disclosure is the differentiator. |

## 4. People and skills

| Objection | Response |
|---|---|
| "AI will replace our analysts." | No source shows replacement. Gartner (via a vendor) says "The SOC will not shrink by 2030" and shifts to engineering [PROPHET-GARTNERROLES-2026]; in SANS/GIAC's survey 39% report no entry-level reductions yet, while 32% say AI is affecting entry-level SOC analyst roles [RSAC-WORKFORCE-2026]. Neither is measurement. |
| "There's a 4-5 million shortage, so jobs are safe." | ISC2 put the gap at 4.8 million in 2024 but published no gap estimate in 2025, focusing on skills; the UK government's study sizes the UK gap at about 3,800 [ISC2-WORKFORCE-2024; ISC2-WORKFORCE-2025; DSIT-CYBERSKILLS-2025]. A senior shortage can coexist with few entry seats: entry-level roles were 6% of 665 US SOC postings in one vendor's analysis [D3-SOCREBUILD-2026]. |
| "Juniors will adapt; AI is just a tool." | Adjacent evidence cuts both ways: lower mastery with AI in a coding trial, large novice gains in reverse engineering [ANTHROPIC-SKILLS-2026; NDSS-2026]. Design the training ([workforce.md](workforce.md) §6). |
| "Certifications will close the AI skills gap." | New AI credentials assume experience (SecAI+ recommends 2+ years; AAISM needs CISM or CISSP) [COMPTIA-SECAI-2026; ISACA-AAISM]. |
| "Buy MDR and the staffing problem goes away." | Providers hire experienced analysts (one posting asks for 2+ years) and bring humans in when confidence drops or impact rises [JOBS-HUNTRESS-2026; ARCTICWOLF-ANALYSTS-2026]; you still need someone who can judge the provider's AI. |

## 5. Securing the AI itself

| Objection | Response |
|---|---|
| "Attackers can't reach our SOC's AI." | Attacker-controlled log fields steered an LLM analyst in research, with up to 96% injection success on summarisation undefended [ARXIV-2605.24421]. Treat raw logs as hostile input (operations §6). |
| "We'll secure agents once we have more of them." | Organizations in CERT-In's cases did not notice test agents entering through exposed credentials and broad cloud roles [THN-CERTIN-2026]; 56% in ISACA's poll do not know how fast they could halt an AI system [ISACA-AIPULSE-2026]. Inventory, identity and a halt procedure come first (ai-security). |
| "Our data can't leave the tenant." | A real constraint; local and open-weight models have been used during incidents and in a university SOC (operations §9). Decide per workflow and record the reasoning. |

## 6. Vulnerability volume and hype

| Objection | Response |
|---|---|
| "Mythos-class vulnerability finding is hype." | The primary claims are the vendor's [ANTHROPIC-GLASSWING-2026]. But two national agencies told organizations to prepare for faster disclosure, and GTIG measured disclosures roughly doubling; GTIG also cautions that counts are inflated and only 0.23% of 2026 disclosures were seen exploited [GOVIE-NCSC-2026; CW-NCSCUK-2026; GTIG-VULNTRENDS-2026]. Plan for volume without treating every CVE as urgent. |
| "AI patching doesn't work." | A vendor benchmark said 26% clean; Trail of Bits' reanalysis found 86% blocked the supplied exploit in trials where agents could test (not proof of a full repair), and 12.5% of developers' first fixes in its audits failed. Trail of Bits runs its own AI patching programme [TOB-1PASSWORD-2026]. Pilot on your own code with review. |
| "Attackers are already fully automated." | GTIG reports an agent-enabled campaign built and run in under six hours; exploitation rose from 10.5 to 18 vulnerabilities a month, mostly fast n-day weaponization, while zero-days rose only from 8 to 11 a month [GTIG-AITRACKER-2026; GTIG-VULNTRENDS-2026]. Urgency is real; panic is not supported. |

## 7. How to respond well

- Concede the true part first; most objections here contain one.
- Name who measured each figure, and say when nobody independent has.
- Turn the objection into a test: a baseline, a side-by-side run, a sampling rule, a halt drill.
- Do not promise headcount outcomes; use [people-and-change.md](../../method/people-and-change.md).

## 8. Sources

Keys not listed here are in [sources.md](sources.md).
