# Security economics

Last researched 2026-10-17. Use this in Frame and Make the case, and whenever budgets, pricing, provider margins or
insurance come up. Every figure says who measured it; vendor figures are self-reported. Source keys in brackets resolve
in §10 or in [sources.md](sources.md).

## Contents

1. [Headlines](#1-headlines)
2. [How in-house security is funded](#2-how-in-house-security-is-funded)
3. [Market size, vendors and consolidation](#3-market-size-vendors-and-consolidation)
4. [How security services are sold](#4-how-security-services-are-sold)
5. [Cost structure and the value ceiling](#5-cost-structure-and-the-value-ceiling)
6. [Provider economics and ownership](#6-provider-economics-and-ownership)
7. [Cyber insurance](#7-cyber-insurance)
8. [Pricing pressure from AI](#8-pricing-pressure-from-ai)
9. [Benchmarks to ask for](#9-benchmarks-to-ask-for)
10. [Sources](#10-sources)

## 1. Headlines

- **Budgets are near flat while AI money moves around security, not into it.** Average growth 5% in 2026 (4% in 2025),
  45% flat and 10% cut; at 38% of organizations AI security spending is funded outside the security budget
  [IANS-BUDGET-2026].
- **The market still grows faster than buyers' budgets**, on forecasts and vendor results, both labelled below.
- **Managed security is priced per unit of coverage, and AI adds two new units: investigations and compute**
  [HUNTRESS-PRICING-2026; DROPZONE-PRICING-2026; MSLEARN-SCU-2026].
- **Whether AI lowers prices is open.** Per a vendor's summary of a Gartner note, MDR providers will keep efficiency
  gains rather than cut prices, and buyers may insource [INTEZER-GARTNERMDR-2026].
- **Independent evidence that AI changes cost is thin and cuts both ways**: a breach-cost correlation in IBM's study and
  a replay benchmark with high miss rates (§5, §8).

## 2. How in-house security is funded

IANS and Artico Search, 2026 (more than 500 security executives, seventh year) [IANS-BUDGET-2026]:

| Measure | 2026 figure |
|---|---|
| Average budget growth | 5% (4% in 2025; peak 17% in 2022); median 0% for the second straight year |
| Flat or cut | 45% flat, 10% cut; 64% asked for an increase, 45% got one |
| Security's share of IT spend | 9.9%, the same as 2021, because AI-driven IT budgets grew faster |
| Budget mix | Software (including AI tooling) 35%, two points behind staff and compensation; AI security tooling 3% |
| AI funding | 69% name AI for security the top priority for net-new money; 76% have no distinct AI line; 38% fund AI security outside the security budget |
| AI line and growth | AI funding rose at about 70% of organizations with a separate line, 42% where embedded, 31% where funded by IT, data or innovation budgets (correlation) |
| Drivers of increases | Business or operational risk 48%; board focus gave the largest average increase (23%); regulation 22%; a major industry breach only 3% |
| Cuts | 78% trace to enterprise-wide cost cutting |
| 2027 | 64% expect an increase, 8% a cut |

Other surveys measure differently. PwC (3,887 executives, 72 countries): 78% expect cyber budgets to rise, and AI (36%)
is the top budget priority [PWC-DTI-2026]; this is expected direction, not realized growth. Wiz's vendor-run survey
(300+ leaders) says 85% increased budgets and people are about a quarter of spend [WIZ-CISOBUDGET-2026]. ISC2
respondents reported budget cuts at 36% of organizations in 2025 (37% in 2024), hiring freezes 39% and layoffs 24%
[ISC2-WORKFORCE-2025]. IANS notes that venture-, PE-backed and well-funded public firms kept growing budgets, so the
average hides a split [IANS-BUDGET-2026]. No current, open benchmark of security spend as a share of revenue was found.

## 3. Market size, vendors and consolidation

- **Forecast (Gartner):** worldwide end-user information security spending of USD 244B in 2026 in the 4Q25 forecast
  (seen only in search results) [GARTNER-FORECAST-2026]; the 2Q26 update (revised 2026-07-21), as relayed by an analyst
  blog, puts 2026 at USD 248.2B, up 12.7% in constant currency, and now counts spending on securing AI
  [SSB-GARTNER2Q26-2026].
- **Vendor results (company-published):** Palo Alto next-generation security ARR USD 9.10B, up 63%, with a GAAP net
  loss of USD 282M in Q4 FY26 [PANW-FY26Q4-2026]; CrowdStrike ARR USD 5.84B, up 25%, and 51% of subscription customers
  on six or more modules [CRWD-FY27Q2-2026].
- **Deals:** 219 cybersecurity M&A deals in H1 2026, per an advisory firm summarising Momentum Cyber; Google closed
  Wiz (USD 32B) and Palo Alto CyberArk (USD 25B) [WINDSORDRAKE-MA-2026]. Proofpoint (Thoma Bravo-owned) agreed on
  2026-10-15 to buy Varonis for about USD 6.3B, 8.4x trailing revenue; close expected H1 2027 [PROOFPOINT-VARONIS-2026].
- **Services firms moving into software:** Accenture took a majority stake in Dragos and bought runZero and NetRise
  (combined enterprise value about USD 4.175B); it says its security business had USD 10B revenue in fiscal 2025
  [ACCENTURE-DRAGOS-2026].
- **AI SOC layer:** Cribl bought Radiant Security's AI SOC assets (2026-08-19) [CRIBL-RADIANT-2026]; LevelBlue, which
  calls itself the largest pure-play MSSP, completed its Cybereason purchase (2025-11-25) [LEVELBLUE-CYBEREASON-2025].
- **Analyst caution:** Forrester says consolidation "doesn't eliminate tools, skills, or complexity" and advises
  shorter terms or contractual protection in renewals after a deal [FORRESTER-RSAC-2026; FORRESTER-PV-2026].

Buyer sentiment: 58% of organizations run more than 25 security tools (vendor survey) [WIZ-CISOBUDGET-2026]; 47% of
PwC's executives list tool consolidation as a response to talent shortages [PWC-DTI-2026]. No source measured savings
from consolidation.

## 4. How security services are sold

| Pricing unit | Example (vendor-published, fetched 2026-10-17) | Note |
|---|---|---|
| Per endpoint | Huntress managed EDR with 24/7 SOC USD 8.99 MSRP per endpoint a month [HUNTRESS-PRICING-2026]; CrowdStrike Falcon self-serve USD 7.99-19.99 per device a month, managed tier "Contact sales" [CROWDSTRIKE-PRICING-2026] | Enterprise MDR is mostly quote-only |
| Per identity, data source, learner | Huntress managed ITDR USD 4.80 per identity; managed SIEM USD 4.00 per data source; awareness training USD 2.08 per learner [HUNTRESS-PRICING-2026] | Units of coverage |
| Per investigation capacity | Dropzone: "up to 4,000 full investigations per year per AI analyst", which it equates to a human tier-1 analyst; MSSP tier pools AI analysts across customers [DROPZONE-PRICING-2026] | New unit; quote only |
| Per compute unit | Microsoft Security Copilot billed in compute units; E5 and E7 customers get 400 a month per 1,000 licences, rollout from 2025-11-18 [MSLEARN-SCU-2026] | Bundling pressures standalone tools |
| Flat or unlimited | Arctic Wolf sells "unlimited investigations" at "predictable pricing" and criticises metered AI pricing [ARCTICWOLF-AURORA-2026] | Positioning against compute pricing |
| Warranty | Arctic Wolf: eligibility for up to USD 3M under its warranty, subject to terms [MSSPALERT-AW-2026] | No source shows fees that vary with a measured outcome |

Arctic Wolf also introduced its own metric, "Mean Time to Trusted Action" [MSSPALERT-AW-2026]; Gartner is reported to
advise buyers to move service metrics to outcomes rather than the volume of AI-processed alerts [INTEZER-GARTNERMDR-2026].

## 5. Cost structure and the value ceiling

- **Labour dominates.** Staff and compensation are the largest category in IANS's data (about 37%) [IANS-BUDGET-2026].
- **24x7 coverage multiplies headcount.** Simple arithmetic: 8,760 hours a year over about 2,080 paid hours per
  full-time employee is about 4.2 people per continuously staffed seat, before leave and training. An AI SOC vendor
  estimates 50-60 analysts (about USD 6-7.2M a year) to cover one 2,000-alert-a-day account at one-third staffing
  [D3-AGENTICMDR-2026].
- **Barriers.** SANS names staffing and funding gaps as the biggest barriers, and says most organizations use AI
  without governance, validation or a defined workflow [SANS-SOC-2026].
- **Cost of failure sets the ceiling.** IBM/Ponemon 2026 (602 breached organizations): average breach USD 4.99M, up
  12%; USD 4.00M with extensive security AI and automation against USD 5.93M with none, and 215 against 280 days to
  identify and contain; 36% were in the extensive group [IBM-CODB-2026]. A correlation among breached organizations,
  not a controlled test; Ponemon ran it, IBM sponsored and analysed it. One in four malicious breaches were AI-enabled,
  averaging about USD 6M [IBM-CODB-2026].
- **Token and licence costs** belong in every case; operations §5 and §9 give per-alert cost figures from one deployer.

## 6. Provider economics and ownership

- **Margins (vendor claims):** an AI SOC vendor selling to providers says headcount-bound MDR or MSSP gross margins are
  typically 25-40% and AI-run operation can reach 70-85% at scale, with analyst tenure under 18 months and turnover
  above 30%; no method published [D3-AGENTICMDR-2026].
- **Automation share (self-reported):** Arctic Wolf says agents resolve more than 60% of case volume as high-confidence
  closures and about one-third of complex cases get final human verification [ARCTICWOLF-AURORA-2026].
- **Valuations (M&A intermediary, ranges that "appear"):** MDR and XDR specialists at scale about 12-16x adjusted
  EBITDA or 2-4x recurring revenue, lower-middle-market MSSPs 8-11x; Sophos paid USD 859M for Secureworks, about 2.3-2.6x
  trailing revenue depending on the revenue base [CTACQ-MSSPMULT-2026].
- **Private equity:** Thoma Bravo's Proofpoint is a serial acquirer; Forrester calls its integration record "uneven"
  [FORRESTER-PV-2026]. No census of PE-owned security providers was found.
- **Not found:** audited MSSP or MDR margins, analyst-to-customer ratios, or renewal price changes after AI.

## 7. Cyber insurance

- **Soft market:** cyber rates fell 4% globally in Q2 2026, the twelfth straight quarterly fall; US down 2%
  [MARSH-GIMI-2026]. Swiss Re projects USD 16.4B global premium for 2026 and USD 17.1B for 2027 (forecast)
  [SWISSRE-CYBER-2026]; the NAIC recorded the first-ever fall in US direct written premium (data year 2024) [NAIC-CYBER-2025].
- **Losses (one insurer's book, 2025):** severity down 19% to an average USD 116,000; ransomware the costliest type at
  USD 269,000; business email compromise and funds-transfer fraud 58% of incidents [COALITION-CLAIMS-2026].
- **AI in coverage:** the new AI exclusions reported are three ISO endorsements for general-liability forms and
  Berkley's exclusion for D&O, E&O and fiduciary forms; the article reports none in cyber forms [INSJOURNAL-AIEXCL-2026]. More in [guardrails.md](guardrails.md) §5.
- **Gap:** no readable source ties premium discounts to MDR, EDR or AI use by the insured.

## 8. Pricing pressure from AI

- **Providers keep the gain (Gartner, via a vendor):** cost savings leadership expects from AI in the SOC "will largely
  go unrealized" because providers absorb them; more organizations will consider insourcing MDR; for after-hours
  coverage with no remediation an AI tool may suffice [INTEZER-GARTNERMDR-2026].
- **Hard to compare:** Forrester says most SecOps vendors offer an "agentic SOC" and differences are hard to see at an
  architectural level [FORRESTER-RSAC-2026].
- **Public markets:** after Anthropic launched Claude Code Security (2026-02-20), CrowdStrike fell 11.6% and Zscaler
  11.3% "on the news", per Yahoo Finance (2026-02-23); Wedbush called it an overreaction [YAHOO-CCS-2026]. Months later both platform CEOs
  described AI as raising security's priority for buyers (vendor releases) [CRWD-FY27Q2-2026; PANW-FY26Q4-2026].
- **Bundling:** Microsoft includes Security Copilot capacity in E5 and E7 [MSLEARN-SCU-2026]; Cribl adds an AI SOC to
  its data platform [CRIBL-RADIANT-2026]. Both turn a product into a feature; no source measures the price effect.
- **Quality limits substitution:** in a preprint replay benchmark (1,247 alerts), each of five LLM triage approaches
  missed at least 40.4% of attack-related alerts; the authors' own design cut misses to 3.1% while escalating 18.4%
  [ARXIV-2610.10608].
- **Headcount expectations:** 69% of CISOs do not expect AI to reduce existing headcount, and 91% expect productivity
  gains (expectations) [IANS-BUDGET-2026].

**For providers:** if competitors pass savings through, unit prices fall; if they keep them, buyers push for outcome
metrics and warranties. Decide a position on both before renewal season. See [disruption.md](disruption.md).

## 9. Benchmarks to ask for

| Ask the leader for | Why | External reference |
|---|---|---|
| Budget growth and where AI money sits | Funding is the first constraint | Average 5%, median 0%; 38% fund AI security elsewhere [IANS-BUDGET-2026] |
| Units paid today (endpoints, identities, data sources, investigations, compute) | Which units change if agents do tier 1 | §4 |
| Alerts a day, share investigated, cost per investigation | Cost per outcome, not per endpoint | Vendor claims only; operations §5 |
| Number of security tools and contracts renewing in 24 months | Consolidation leverage and exit risk | 58% run more than 25 tools (vendor survey) [WIZ-CISOBUDGET-2026] |
| Breach cost assumptions in the business case | Value ceiling | USD 4.99M average [IBM-CODB-2026] |
| Insurance premium, retention and AI wording | Underwriting asks about controls | §7 |
| (Providers) delivery cost per client, margin, analyst tenure | Where AI changes cost to serve | Vendor claims only [D3-AGENTICMDR-2026] |

## 10. Sources

Keys not listed here are in [sources.md](sources.md).

- **CROWDSTRIKE-PRICING-2026**: CrowdStrike, *Falcon pricing* (vendor price list, fetched 2026-10-17). https://www.crowdstrike.com/en-us/pricing/
- **CTACQ-MSSPMULT-2026**: CT Acquisitions, *MSSP and Cybersecurity Services M&A Multiples Report 2026* (M&A intermediary, 2026-07-03). https://ctacquisitions.com/guides/mssp-ma-multiples-2026/
- **GARTNER-FORECAST-2026**: Gartner, *Forecast of worldwide end-user spending on information security (4Q25 document 7291530)* (analyst forecast, 4Q25 edition, cited by 2026-03; seen only in search results). https://www.gartner.com/en/documents/7291530
- **INSJOURNAL-AIEXCL-2026**: Insurance Journal, *Insurer interest in AI coverage exclusions growing as risk becomes omnipresent* (trade press, 2026-08-17). https://www.insurancejournal.com/magazines/mag-features/2026/08/17/881424.htm
- **LEVELBLUE-CYBEREASON-2025**: LevelBlue, *LevelBlue completes acquisition of Cybereason* (vendor press release, 2025-11-25). https://www.levelblue.com/newsroom/press-releases/levelblue-completes-acquisition-of-cybereason-expanding-global-leadership-in-managed-detection-and-response-xdr-and-incident-response
- **MARSH-GIMI-2026**: Marsh, *Global Insurance Market Index, Q2 2026* (broker index, 2026-07-23). https://www.marsh.com/en/corp/about/news/global-commercial-insurance-falls-6-percent-q2-2026.html
- **NAIC-CYBER-2025**: NAIC, *Report on the Cybersecurity Insurance Market (data year 2024)* (regulator, 2025-11-10). https://content.naic.org/sites/default/files/inline-files/2025_Cybersecurity_Insurance%20Report.pdf
- **PANW-FY26Q4-2026**: Palo Alto Networks, *Palo Alto Networks reports fiscal fourth quarter and fiscal year 2026 results* (vendor earnings release, 2026-09-01). https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-reports-fiscal-fourth-quarter-and-fiscal-10
- **SSB-GARTNER2Q26-2026**: Software Strategies Blog (Louis Columbus), *Gartner Securing AI Forecast: 2Q26 Spending Hits $248.2B* (analyst blog relaying Gartner forecast G00855892, 2026-07-06; corrected 2026-10-04). https://softwarestrategiesblog.com/2026/07/06/gartner-2q26-information-security-forecast-securing-ai-2030/
- **PWC-DTI-2026**: PwC, *2026 Global Digital Trust Insights (Thailand press release)* (survey of 3,887 executives, 2025-11-14). https://www.pwc.com/th/en/press-room/press-release/2025/press-release-14-11-25-en.html
- **SWISSRE-CYBER-2026**: Swiss Re Institute, *Building a sustainable cyber market in the AI era* (reinsurer research, 2026-08-31). https://www.swissre.com/risk-knowledge/advancing-societal-benefits-digitalisation/building-a-sustainable-cyber-market-in-the-AI-era.html
- **WINDSORDRAKE-MA-2026**: Windsor Drake, *Cybersecurity M&A Report 2026 (citing Momentum Cyber)* (M&A advisory, reviewed 2026-08-05). https://windsordrake.com/cybersecurity-ma-report/
- **WIZ-CISOBUDGET-2026**: Wiz, *2026 CISO Budget Benchmark Report* (vendor survey of 300+, undated, c. late 2025). https://www.wiz.io/reports/ciso-security-budget-benchmark-2026
