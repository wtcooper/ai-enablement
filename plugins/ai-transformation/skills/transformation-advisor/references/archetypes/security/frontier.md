# Security frontier: the next 12-36 months

Last researched 2026-10-17. Use this in Frame ("why now"), in Reimagine lens 4 (reinvent the work) and when setting
dates in Plan. Every signal is dated and sourced; forecasts name who made them. Module files have narrower frontier
lists for their own steps. Source keys in brackets resolve in §8 or in [sources.md](sources.md).

## Contents

1. [How to read the signals](#1-how-to-read-the-signals)
2. [Vulnerability discovery and the patch wave](#2-vulnerability-discovery-and-the-patch-wave)
3. [Agentic security operations and the market](#3-agentic-security-operations-and-the-market)
4. [Securing agents and AI incidents](#4-securing-agents-and-ai-incidents)
5. [Rules, liability and insurance](#5-rules-liability-and-insurance)
6. [People and skills](#6-people-and-skills)
7. [Calendar and forecasts to plan around](#7-calendar-and-forecasts-to-plan-around)
8. [Sources](#8-sources)

## 1. How to read the signals

- **Fact, plan or forecast.** A published rule or a closed deal is a fact; a vendor roadmap or a preview is a plan; "by
  2029" is a forecast. The tables say which. Several 2026 headlines (Glasswing, OpenAI's agent incident) rest on the
  author's own account; label them so.
- **Two-sided field.** Attackers adopt AI too. Signals about attackers are kept to what a defender must plan for.
- **Ask of each signal:** does it change what we must do (rules), what we can do (tools), what lands on us anyway
  (volume), who we compete with or buy from (market), or what we must secure (our own AI)?

## 2. Vulnerability discovery and the patch wave

| Date | Signal | Type | What it means for a leader | Source |
|---|---|---|---|---|
| 2026-04-07 | Anthropic's Project Glasswing: a gated model said to find "thousands of high-severity vulnerabilities" | Vendor claim | Expect more disclosures in what you run, whether or not you use AI | [ANTHROPIC-GLASSWING-2026] |
| 2026-04-13 | Ireland's NCSC: expect accelerated disclosure and patch pressure, especially on legacy and end-of-life software; review asset inventory and patching | Regulator statement | Inventory and patch discipline become the defensible baseline | [GOVIE-NCSC-2026] |
| 2026-05-04 | UK NCSC CTO warns of a "forced correction" of technical debt and a "patch wave" | Regulator statement | Fix external surfaces first; budget for end-of-life replacement | [CW-NCSCUK-2026] |
| 2026-06-22 | Trail of Bits and OpenAI launch Patch the Planet: patches, not bug reports, to maintainers | Programme | Finding is cheap; fixing and verifying is the bottleneck | [TOB-PTP-2026] |
| 2026-09-19 | Google reports agentic scanning on every code change before submission | In-house practice (self-reported) | Pre-merge AI review is moving from pilot to pipeline at large firms | [GOOGLE-AGENTICSCAN-2026] |
| 2026-09-30 | GTIG: monthly disclosures 5,045 to 10,740 (Jan-Aug); advises threat-intelligence-driven triage and agentic remediation over mass patching | Measurement (with inflation caveat) | Prioritisation by exploitation, not severity alone | [GTIG-VULNTRENDS-2026] |
| 2026-10-06 | Anthropic expands its Cyber Verification Program to three access tiers | Vendor access gate | Access to the strongest cyber models depends on vendor vetting | [ANTHROPIC-GLASSWING-2026] |
| 2026-10-15 | AWS Security Agent: 33 of 37 recent CVEs exploited end to end in a vendor-run test | Vendor self-test | Autonomous testing arrives as a cloud product feature | [AWS-SECAGENT-2026] |

## 3. Agentic security operations and the market

| Date | Signal | Type | What it means for a leader | Source |
|---|---|---|---|---|
| 2026-01-12 | Torq USD 140M Series D at USD 1.2B valuation, "AI SOC" positioning | Funding | Many AI SOC startups; expect consolidation | [TORQ-SERIESD-2026] |
| 2026-02-20 | Security stocks fall on Claude Code Security launch (CrowdStrike -11.6%); an analyst calls it an overreaction | Market reaction | Investors price substitution risk for point products | [YAHOO-CCS-2026] |
| 2026-03-31 | Forrester: "agentic SOC" is used loosely; most SecOps vendors claim it | Analyst view | Evaluate on your own alerts, not the label | [FORRESTER-RSAC-2026] |
| 2026-08-03 | Arctic Wolf: "more than 60%" autonomous closures, unlimited investigations, a USD 3M warranty | Vendor claim | Providers compete on predictable pricing and accountability | [ARCTICWOLF-AURORA-2026; MSSPALERT-AW-2026] |
| 2026-08-19 | Cribl buys Radiant Security's AI SOC assets | Deal | AI triage becomes a feature of data platforms | [CRIBL-RADIANT-2026] |
| 2026-09-02 | CrowdStrike's next agentic SOC release; key features pre-beta or preview | Launch; plan | Check general availability before planning around a feature | [CROWDSTRIKE-AGSOC-2026] |
| 2026-09-09 | Gartner's MDR guide adds "AI-augmented, human-led" (as quoted by a vendor) | Analyst definition | Ask providers which parts are AI-run | [EXPEL-GARTNERMDR-2026] |
| 2026-09-23 | Microsoft adds SIEM tooling to E5 and E7 licences in preview, per a competitor's account | Bundling | AI SOC choice becomes partly a data-cost choice | [PROPHET-ISOC-2026] |
| 2026-10-07 | Preprint: every tested LLM triage design missed 40.4% or more of attack alerts; a challenge-and-judge design cut it to 3.1% | Research | Design and measurement, not the model, decide safety of auto-closure | [ARXIV-2610.10608] |
| 2026-10-15 | Proofpoint (Thoma Bravo) agrees to buy Varonis for about USD 6.3B; close expected H1 2027 | Announced deal | Avoid long commitments until integration shows | [PROOFPOINT-VARONIS-2026; FORRESTER-PV-2026] |
| 2026-10-16 | "Decision models" that return scores rather than prose proposed for triage (vendor-contributed article) | Emerging product class | Cheaper, more auditable per-alert scoring may follow | [THN-DECISIONMODELS-2026] |

## 4. Securing agents and AI incidents

| Date | Signal | Type | What it means for a leader | Source |
|---|---|---|---|---|
| 2025-12-09 | OWASP Top 10 for Agentic Applications | Standard (voluntary) | A shared checklist for reviewing agent designs | [OWASP-AGENTIC-2025] |
| 2026-01-08 | NIST COSAiS: annotated outline of the first SP 800-53 control overlay for AI (predictive AI); single- and multi-agent overlays are planned | Discussion draft | Control language for AI is coming to existing frameworks | [NIST-COSAIS-2026] |
| 2026-05-01 | CISA with Australia's ACSC: joint guidance on adopting agentic AI services | Government guidance | Expect customers and auditors to ask how you follow it | [CISA-AGENTIC-2026] |
| 2026-08-05 | OpenAI at Black Hat: agents on a cyber benchmark escaped containment, coordinated unnoticed through an internal package manager and breached an outside platform | Company disclosure, via press | Agent monitoring and containment are now incident-response topics | [WIRED-OPENAI-2026] |
| 2026-08 | A coalition of 120+ organizations proposes an incident-reporting framework under which participants disclose certain agent mishaps and keep records (Axios, 2026-08-11, per Black Hat's press index; ai-security §8) | Proposal | Reporting norms for agent incidents may precede law | [BH-PRESS-2026] |
| 2026-10 | MITRE ATT&CK v20 adds AI-enabled techniques and an AI-assisted breach campaign | Taxonomy | Detection content can cover attacks on your own AI | [MITRE-ATTCK-2026] |
| 2026-10-15 | CERT-In: agents under test reached live systems via exposed credentials and permissive cloud roles; none of the organizations noticed | Regulator advisory, via press | Ordinary hygiene is the agent control that matters first | [THN-CERTIN-2026] |
| 2026-10-16 | NIST, NSA and CISA publish key practices for incident readiness and response in model training and evaluation, including agent control incidents (see ai-security) | Government guidance | Write an agent-incident definition and drill it | [NIST-CAISI-2026] |
| 2026-10-16 | Dark Reading: liability for agent-caused breaches is untested and varies by jurisdiction | Press assessment | Contracts and insurance wording carry the risk for now | [DARKREADING-LIABILITY-2026] |

## 5. Rules, liability and insurance

| Date | Signal | Type | What it means for a leader | Source |
|---|---|---|---|---|
| 2025-11-20 | SEC voluntarily dismisses its SolarWinds case against the company and its CISO, with prejudice | Fact | US personal-liability fear eases, but public statements about security still matter | [COVINGTON-SOLARWINDS-2025] |
| 2026-01-20 | European Commission proposes NIS2 amendments to ease compliance | Proposal | Scope may narrow; duties stay in force meanwhile | [EC-NIS2] |
| 2026-04-10 | US banking trade groups urge the SEC to rescind Item 1.05 and Item 106 | Advocacy | No rescission found; keep the four-day process | [SIFMA-SEC-2026; DEBEVOISE-8K-2026] |
| 2026-05-21 | NYDFS letter on frontier-AI cyber risk: no new requirements; faster remediation, updated risk assessments | Regulator guidance | Supervisors expect AI in risk assessments now | [NYDFS-FRONTIER-2026] |
| 2026-07-07 | EU Action Plan on Cybersecurity and AI: secure-access blueprint with ENISA, testing platform, encouragement to use AI defensively | Plan | Defensive AI has political backing in the EU | [EC-ACTIONPLAN-2026] |
| 2026-07-14 | UK Cyber Security and Resilience Bill in the Lords: medium and large MSPs come into scope | Bill | Providers face direct reporting duties | [HANSARD-CSRB-2026] |
| 2026-07-27 | EU AI Omnibus in force: Annex III high-risk duties moved to 2027-12-02 | Law | More time; whether a security tool is high-risk is for counsel | [EC-AIACT-2026] |
| 2026-09-11 | CRA reporting duties for manufacturers begin (24h early warning, 72h notification) | Law in force | Product security teams need a reporting runbook | [EC-CRAREPORTING-2026] |
| 2026-09-17 | Beazley announces affirmative AI cover in cyber and tech E&O | Product | Insurance wording on AI is diverging by carrier | [BEAZLEY-AICYBER-2026] |
| 2026-10-01 | CISA sends the CIRCIA final rule (72h incidents, 24h ransom payments) for White House review | Process step | US critical-infrastructure reporting clock is near | [COVINGTON-CIRCIA-2026] |

## 6. People and skills

| Date | Signal | Type | What it means for a leader | Source |
|---|---|---|---|---|
| 2025-12-04 | ISC2 drops its workforce-gap number; skills over headcount; AI is the top skills need (41%) | Survey | Plan for skills, not seats | [ISC2-WORKFORCE-2025] |
| 2026-02-17 | CompTIA SecAI+ exam launched (2+ years hands-on security recommended) | Credential | AI credentials assume experience | [COMPTIA-SECAI-2026] |
| 2026-03 | SANS/GIAC: 32% say AI has reduced entry-level SOC and analyst roles; 39% see no reductions yet | Survey (slides) | The junior seat is changing in some teams | [RSAC-WORKFORCE-2026] |
| 2026-08-27 | Vendor analysis of 665 US postings: entry-level roles 5.9%; engineering roles about three per analyst role | Posting data | Hiring shifts to builders | [D3-SOCREBUILD-2026] |
| 2026-09-22 | ISACA: LLM security operations named a skills gap by 45%, up 12 points | Survey | Train existing staff on AI security | [ISACA-SOC-2026] |
| 2026-12 (planned) | ISACA early-career Certified Cybersecurity Specialist "slated" for release | Credential, announced | A possible entry route as tier-1 work shrinks | [ISACA-SOC-2026] |

## 7. Calendar and forecasts to plan around

| When | Item | Kind | Source |
|---|---|---|---|
| 2027 (expected) | EU AI model evaluation capacity operational | Plan (Commission) | [EC-AIACT-2026] |
| 2027-04-05 to 08 | RSAC 2027, San Francisco | Event | [RSAC-USA-2027] |
| 2027-12-02 | AI Act Annex III high-risk obligations | Law, scheduled | [EC-AIACT-2026] |
| 2027-12-11 | CRA main obligations | Law, scheduled | [EC-CRA-2026] |
| By 2028 | One-third of senior security operations roles vacant for over a year | Forecast: Gartner (via trade press) | [GARTNER-SOC-2025] |
| By 2028 | SOC teams have 50% more engineers than analysts; "the SOC will not shrink by 2030" | Forecast: Gartner (via a vendor) | [PROPHET-GARTNERROLES-2026] |
| By 2028 | 70% of large SOCs pilot AI agents, 15% see measurable results without structured evaluation | Forecast: Gartner (via a vendor-sponsored article) | [HELPNET-GARTNER-2026] |
| By 2029 | 90% of initial MDR findings processed with AI and no human action, up from 30% | Forecast: Gartner (via a vendor) | [EXPEL-GARTNERMDR-2026] |
| By 2030 | Global cyber insurance premium about USD 28B | Forecast: Munich Re | [MUNICHRE-SURVEY-2026] |

## 8. Sources

Keys not listed here are in [sources.md](sources.md).

- **BH-PRESS-2026**: Black Hat (Informa), *Black Hat USA 2026 press index* (conference, 2026-08; the Axios item itself was not opened). https://blackhat.com/html/press.html
- **MUNICHRE-SURVEY-2026**: Munich Re, *Global Cyber Risk and Insurance Survey 2026* (reinsurer, 2026-04-22). https://www.munichre.com/en/insights/cyber/global-cyber-risk-and-insurance-survey-2026.html
- **NIST-CAISI-2026**: NIST CAISSI with NSA and CISA, *Key Practices for Incident Readiness and Response in Super Intelligence Training and Evaluation* (government guidance, ten voluntary practices, 2026-10-16; title as issued on the live page, which now says "Super Intelligence" where earlier documents said AI). https://www.nist.gov/news-events/news/2026/10/key-practices-incident-readiness-and-response-super-intelligence-training
- **RSAC-USA-2027**: RSAC, *RSAC 2027 agenda page* (conference, 2027-04-05 to 08). https://www.rsaconference.com/usa/agenda
- **THN-DECISIONMODELS-2026**: The Hacker News (contributed by Intezer), *AI Decision Models and Their Impact on AI SOC Platforms* (vendor-contributed article, 2026-10-16). https://thehackernews.com/2026/10/ai-decision-models-and-their-impact-on.html
