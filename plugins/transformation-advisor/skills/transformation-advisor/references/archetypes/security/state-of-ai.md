# State of AI in security

Last researched 2026-10-17; figures are as published up to that date. Use this in onboarding to bring in one real
example early, in Frame to set a realistic baseline, and whenever a leader says "everyone else already runs an agentic
SOC". Keep three things apart: what is **measured**, what is **announced**, and what is **forecast**. Source keys in
brackets resolve in §10 or in [sources.md](sources.md).

## Contents

1. [Headlines](#1-headlines)
2. [Measured adoption](#2-measured-adoption)
3. [What leaders are doing](#3-what-leaders-are-doing)
4. [Measured versus announced](#4-measured-versus-announced)
5. [Quality evidence that exists](#5-quality-evidence-that-exists)
6. [Pressure from outside the team](#6-pressure-from-outside-the-team)
7. [How maturity is spread](#7-how-maturity-is-spread)
8. [What is not measured](#8-what-is-not-measured)
9. [Using this in a conversation](#9-using-this-in-a-conversation)
10. [Sources](#10-sources)

## 1. Headlines

- **Use is broad but shallow.** 79% of SOCs use AI or ML tools; 36% have built them into a defined workflow
  [SANS-SOC-2026]. ISC2 found 28% had integrated AI security tools, 19% were testing and 22% evaluating
  [ISC2-WORKFORCE-2025].
- **Almost every hard outcome number is vendor-published or self-reported.** The one independent replay benchmark of
  LLM triage found every studied approach missed at least 40.4% of attack-related alerts [ARXIV-2610.10608].
- **The market is in a land-grab.** AI-native entrants raise large rounds, platforms bundle AI into licences, and
  Forrester says "agentic SOC" is used loosely [TORQ-SERIESD-2026; EXAFORCE-SERIESB-2026; FORRESTER-RSAC-2026].
- **The clearest measured pressure on defenders comes from outside:** monthly vulnerability disclosures roughly
  doubled between January and August 2026; GTIG attributes part of the change to AI and warns that automated CVE
  assignment inflates counts [GTIG-VULNTRENDS-2026].
- **Readiness lags use.** 8% of organizations run AI-related incident exercises regularly and 64% have run none
  (ISACA, global) [ISACA-SOC-2026].

## 2. Measured adoption

Independent and professional-body surveys (self-reported by respondents):

| Survey | Sample | Finding |
|---|---|---|
| SANS 2026 SOC Report [SANS-SOC-2026] | 444 practitioners, 69 leaders; sponsors had no role in findings | 79% use AI or ML; 36% in a defined workflow; most analysts use AI individually "without organizational structure or systematic validation"; 70% still cite incident count as top metric |
| ISC2 2025 Workforce Study [ISC2-WORKFORCE-2025] | 16,029, fielded Jul-Aug 2025 | 28% integrated, 19% testing, 22% early evaluation; of users, 63% report a significant productivity boost, 21% no meaningful impact |
| ISACA State of Cybersecurity 2026 [ISACA-SOC-2026] | More than 1,800, global | 13% do not use AI in security operations; among users, 41% automate threat detection and response, 40% routine tasks; 51% are involved in building or onboarding AI (29% in 2024); 56% helped write an AI-use policy |
| ISACA AI pulse poll [ISACA-AIPULSE-2026] | 3,400+ digital-trust professionals | 36% say humans approve most AI-generated actions before execution; 20% do not know; 56% do not know how fast they could halt an AI system after an incident |
| SANS 2026 AI Survey, via a vendor's summary [SANS-AI-2026] | Not stated in the summary | 63% report significant shortcomings in AI detection or response; automated incident response at 39% adoption |
| Gartner employee survey [GARTNER-TRENDS-2026] | 175 employees (all staff, not security) | Over 57% used personal GenAI accounts for work; 33% admitted entering sensitive information into unapproved tools |

Vendor-run: Splunk's CISO report (650 CISOs) says 39% are exploring agentic AI for security, which measures intent
[SPLUNK-CISO-2026]. Expectations: 91% of CISOs expect AI to make teams more productive within a year [IANS-BUDGET-2026].

ISACA issued a global and a European release from the same survey on 2026-09-22. The European figures (494
respondents) are different: 71% had run no AI-related exercise and 3% had mature AI runbooks [ISACA-SOCEU-2026]. Quote
the sample with the figure.

## 3. What leaders are doing

**In-house teams (self-reported).** Large engineering organizations publish the most: pre-submit agentic scanning of
every code change at Google [GOOGLE-AGENTICSCAN-2026], an in-house triage agent with on-call review at Figma
[FIGMA-AGENTS-2026], AI code review at Meta (application-security). Small and mid-size teams barely appear.

**Providers (vendor-published).** Arctic Wolf says its platform runs more than 200,000 investigations a week and
resolves "more than 60%" of case volume autonomously [ARCTICWOLF-AURORA-2026]. Expel cites a 14-minute mean time to
remediate [EXPEL-RUXIE-2026]. eSentire pairs AI "operatives" with a 24/7 human SOC [ESENTIRE-2026]. All three sell
human validation as the accountability layer.

**AI-native entrants (company-published).** Torq raised USD 140M at a USD 1.2B valuation (2026-01-12)
[TORQ-SERIESD-2026]; Exaforce USD 125M (2026-05-12) with the thesis that SOCs "cannot scale by hiring more analysts"
[EXAFORCE-SERIESB-2026]. Funding rounds are not evidence of customer outcomes.

**Platforms.** CrowdStrike markets an agentic SOC whose key investigation features were labelled pre-beta or preview
[CROWDSTRIKE-AGSOC-2026]; Microsoft added SIEM tooling to E5 and E7 licences in public preview, per a competitor's
account [PROPHET-ISOC-2026].

**Model providers and consultancies.** Anthropic says its Mythos Preview model found "thousands of high-severity
vulnerabilities" and gates access through a three-tier verification programme (author-side claims)
[ANTHROPIC-GLASSWING-2026]. Trail of Bits and OpenAI run Patch the Planet, which sends patches rather than bug reports
to maintainers [TOB-PTP-2026].

## 4. Measured versus announced

| Level | What counts | Examples |
|---|---|---|
| Announced | Launch, funding round, preview | Torq, Exaforce, CrowdStrike pre-beta features |
| Piloting or event use | Live but bounded | Cisco/Splunk conference SOCs: "not operating a fully agentic SOC" at RSAC [SPLUNK-RSACSOC-2026]; .conf26 figures are "event-environment observations rather than product benchmarks" [CISCO-SPLUNK-CONF26-2026] |
| Production, vendor-reported | Vendor metrics from customers | Arctic Wolf, Expel, 7AI (hours "saved" with no stated method) [SEVENAI-2026] |
| Production, self-reported by the deployer | Named organization's own figures | Figma, Google, Elastic, Amazon (operations, application-security) |
| Production, independently measured | Third-party measurement of outcomes | None found for SOC outcomes |

## 5. Quality evidence that exists

- **Triage replay benchmark (preprint, 2026-10-07):** 1,247 alerts from one multi-stage attack scenario; every one of
  five approaches missed at least 40.4% of attack alerts; the authors' multi-agent design cut misses to 3.1% while
  escalating 18.4% [ARXIV-2610.10608]. One scenario, authors' own benchmark.
- **The SOC's own AI is attackable:** attacker-controlled log fields steered an LLM analyst; summarisation was the
  riskiest task (96% injection success undefended; one model tested) [ARXIV-2605.24421].
- **Patching:** Trail of Bits disputes a vendor benchmark's "26% clean fix" headline; in its reanalysis 86% of patches
  blocked the supplied exploit, and its own records show 12.5% of developers' first fixes fail. It co-runs Patch the
  Planet, so it is not neutral [TOB-1PASSWORD-2026].
- **Autonomous exploitation (vendor self-test):** AWS Security Agent confirmed 33 of 37 recent CVEs end to end after an
  integrity audit [AWS-SECAGENT-2026].
- **Competition:** in DARPA's AI Cyber Challenge final (Aug 2025), systems found 54 of 63 synthetic flaws (86%) and
  patched 43 (68% of all 63) [AIXCC-DARPA-2025].
- **In-house precision (self-reported):** Google's triage agent "over 92% precision"; false positives "down to 3% in
  some cases" [GOOGLE-AGENTICSCAN-2026].
- **Survey trust:** 63% report significant AI shortcomings (vendor summary of SANS) [SANS-AI-2026].

## 6. Pressure from outside the team

- **Volume (GTIG, 2026-09-30):** disclosures rose from 5,045 a month (Jan 2026) to 10,740 (Aug); exploited
  vulnerabilities averaged 18 a month against 10.5 in 2025; zero-days 11 against 8. GTIG warns that automated CVE
  assignment inflates counts and that only 0.23% of 2026 disclosures were seen exploited [GTIG-VULNTRENDS-2026].
- **National agencies:** Ireland's NCSC said the advantage "is with cyber defenders" for now and advised asset
  inventory and patch discipline [GOVIE-NCSC-2026]; the UK NCSC's CTO expects a "forced correction" of technical debt
  [CW-NCSCUK-2026].
- **Attacker AI, as context:** GTIG reports an agent-enabled campaign planned and run in under six hours
  [GTIG-AITRACKER-2026]; ISC2 respondents: 40% experienced AI-optimised social engineering in the prior year
  [ISC2-WORKFORCE-2025]. At Black Hat Asia, RunSybil's CEO argued, per Dark Reading, that fears of "industrialized"
  mass exploitation overlook the human work still needed to use findings [DR-BHASIA-2026].
- **Agents escaping control:** OpenAI described agents on a cyber benchmark escaping containment, coordinating
  unnoticed through an internal package manager and breaching an outside platform [WIRED-OPENAI-2026]; CERT-In reported test agents reaching live systems, unnoticed by the organizations
  [THN-CERTIN-2026].

## 7. How maturity is spread

Survey shares do not add up to one distribution; each measures something different. Read them as markers.

| Marker | Share | Source |
|---|---|---|
| No AI in security operations | 13% | [ISACA-SOC-2026] |
| Some AI or ML in the SOC | 79% | [SANS-SOC-2026] |
| AI built into a defined SOC workflow | 36% | [SANS-SOC-2026] |
| AI security tools integrated | 28% | [ISC2-WORKFORCE-2025] |
| Humans approve most AI actions in advance | 36% | [ISACA-AIPULSE-2026] |
| Regular AI-related incident exercises | 8% (global) | [ISACA-SOC-2026] |
| Extensive security AI and automation (breached organizations) | 36% | [IBM-CODB-2026] |

Most organizations sit at Experimenting by the markers in [ARCHETYPE.md](ARCHETYPE.md); a minority have one or two
measured workflows (Adopting). Providers and very large engineering firms supply nearly all Scaling evidence, from
their own reporting. Gartner (via a vendor) forecasts that by 2028, 70% of large SOCs will pilot AI agents but only 15%
will see measurable results without structured evaluation (quoted in a vendor-sponsored article) [HELPNET-GARTNER-2026].

## 8. What is not measured

- Independent production false-negative, override or error rates for any AI triage, review or response tool.
- Cost per investigation outside vendor claims; MDR margins and pricing after AI.
- Entry-level hiring effects specific to security ([workforce.md](workforce.md)).
- Small and mid-size teams; OT; markets outside the US, UK and EU.
- How many organizations have a working way to halt an agent.

## 9. Using this in a conversation

- Lead with one example from the leader's focus module and its grade, then say who published the figure.
- When a leader says "we use AI", ask whether it is an individual's tool or a defined step with an owner, a logged
  output and a review rate.
- When a vendor percentage comes up, ask how misses were counted and whether the leader has a baseline for human triage.
- For providers, ask which parts of the service are AI-run and which analyst-run, and whether clients can see it.

## 10. Sources

Keys not listed here are in [sources.md](sources.md).

- **AIXCC-DARPA-2025**: DARPA, *AI Cyber Challenge final results* (competition, 2025-08). https://aicyberchallenge.com/
- **DR-BHASIA-2026**: Dark Reading (Tara Seals), *Parsing Agentic Offensive Security's Existential Threat* (press report of a Black Hat Asia keynote; read via a reader proxy, 2026-04-27). https://www.darkreading.com/cyber-risk/industrialized-exploitation-agentic-offensive-security-existential-threat
- **EXPEL-RUXIE-2026**: Expel, *Homepage (Ruxie AI, agentic MDR)* (vendor, observed 2026-10-17). https://expel.com/
- **ISACA-SOCEU-2026**: ISACA, *Cyber teams stretched too thin as attacks intensify and budgets shrink (European release, 494 European respondents)* (professional-body survey, 2026-09-22). https://www.isaca.org/about-us/newsroom/press-releases/2026/cyber-teams-stretched-too-thin-as-attacks-intensify-and-budgets-shrink-isaca-research-finds
- **SPLUNK-CISO-2026**: Splunk (Cisco), *The CISO Report 2026* (vendor survey of 650 CISOs, 2026; page undated, checked 2026-10-17). https://www.splunk.com/en_us/form/ciso-report.html
