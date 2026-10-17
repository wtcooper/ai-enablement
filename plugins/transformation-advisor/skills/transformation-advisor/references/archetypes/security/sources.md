# Security sources

last_researched: 2026-10-17

Use this to resolve a source key cited in any security archetype file, and to know where to look when the field needs
re-researching. Part A is the source landscape; Part B lists every key cited in more than one archetype file (keys
cited in only one file are listed at the end of that file). Module files keep their own source lists, and the use-case
YAML files carry full rows with locators.

## Contents

- [Part A. Source landscape](#part-a-source-landscape)
  - [Conferences and events](#conferences-and-events)
  - [Regulators and standard-setters](#regulators-and-standard-setters)
  - [Professional bodies and surveys](#professional-bodies-and-surveys)
  - [Academic venues and research centres](#academic-venues-and-research-centres)
  - [Publications, podcasts and communities](#publications-podcasts-and-communities)
  - [Vendors, providers and firms to watch](#vendors-providers-and-firms-to-watch)
  - [Where the evidence is thin](#where-the-evidence-is-thin)
- [Part B. Shared source keys](#part-b-shared-source-keys)

## Part A. Source landscape

### Conferences and events

| Event (organiser) | Latest edition | Why it matters | Link |
|---|---|---|---|
| RSA Conference (RSAC) | 23-26 Mar 2026, San Francisco; next 5-8 Apr 2027 | Largest annual venue; agentic AI dominated; SANS/GIAC workforce report premiered there; Innovation Sandbox winner was an agent-governance start-up | https://www.rsaconference.com/events/2026-usa |
| Gartner Security & Risk Management Summit | 1-3 Jun 2026, National Harbor | CISO-level framing on AI compliance, board reporting, agent risk; sessions client-only | https://www.gartner.com/en/conferences/na/security-risk-management-us |
| Black Hat USA, with AI, CISO and Financial Threat summits | 1-6 Aug 2026, Las Vegas | OpenAI's agent-containment briefing; agent-incident reporting proposal; press index is the best entry | https://blackhat.com/html/press.html |
| DEF CON and AI Village | Aug 2026, Las Vegas | Agent sandboxing, AI gateways and build gates as research topics (titles only; no technique detail used) | https://defcon.org/html/defcon-34/dc-34-index.html |
| BSides Las Vegas | Early Aug 2026 | Practitioner talks on agentic investigation, AI governance programmes, product incident playbooks for LLM apps | https://bsideslv.org/talks |
| FIRST Conference and AI Security SIG | 14-19 Jun 2026, Denver | Richest public source on AI in incident response, PSIRT and triage | https://www.first.org/conference/2026/program |
| fwd:cloudsec | 1-2 Jun 2026 (NA); 7-8 Sep 2026 (Europe) | Cloud security practitioners; talk abstracts only | https://fwdcloudsec.org/ |
| SANS AI Cybersecurity Summit (also DFIR and other summits) | 20-21 Apr 2026 (not reconfirmed); fall edition 2-3 Nov 2026 | Defender-AI summit | https://www.sans.org/cyber-security-training-events/ai-summit-2026/ |
| ATT&CKcon (MITRE) | 27-28 Oct 2026 | ATT&CK v20 adds AI-enabled techniques | https://attack.mitre.org/resources/updates/ |
| S4 (OT and ICS security) | S4x27, 8-11 Feb 2027, Tampa | The OT venue, if OT comes up | https://s4xevents.com/ |

### Regulators and standard-setters

| Body | What to watch | Link |
|---|---|---|
| NIST (CSF 2.0, AI RMF, AI 100-2, COSAiS overlays, NICE, CAISI) | Value-chain frame; AI control overlays in draft; workforce taxonomy | https://www.nist.gov/cyberframework |
| CISA (with ASD's ACSC and Five Eyes partners) | Agentic AI adoption guidance; AI security guidance index; advisories | https://www.cisa.gov/ai |
| European Commission and ENISA | AI Act timeline, NIS2, CRA reporting, Action Plan on Cybersecurity and AI, threat landscape | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai |
| EIOPA and EU supervisors | DORA for financial entities and ICT providers | https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en |
| US SEC | Form 8-K Item 1.05 and Reg S-K Item 106; rescission pressure | https://www.sec.gov/newsroom/press-releases/2023-139 |
| NY Department of Financial Services | AI and frontier-model letters under Part 500 | https://www.dfs.ny.gov/industry-guidance/industry-letters/20260521-heightened-cybersecurity-risks-assoc-with-frontier-ai-models |
| UK NCSC, UK AI Security Institute, Ireland NCSC | Patch-wave warnings; frontier cyber evaluations | https://www.aisi.gov.uk/research |
| CERT-In (India) | Advisory on test agents reaching live systems (2026-10-15) | via The Hacker News, see THN-CERTIN-2026 |
| OWASP GenAI Security Project | LLM and Agentic Top 10s, Agent Control Standard, red-teaming and data-security guides | https://genai.owasp.org/resources/ |
| MITRE (ATT&CK, ATLAS) | Taxonomies for detection content and AI attacks | https://atlas.mitre.org/ |
| Cloud Security Alliance; Center for Internet Security | AI controls matrix, STAR for AI; CIS controls and AI guidance | https://cloudsecurityalliance.org/ai-safety-initiative |

### Professional bodies and surveys

| Body or survey | What it gives | Link |
|---|---|---|
| ISC2 Cybersecurity Workforce Study | Largest workforce survey; dropped the gap number in 2025 | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study |
| ISACA State of Cybersecurity; AI pulse polls; AAIA, AAISM, AAIR credentials | Staffing, AI use, AI incident readiness; global and European releases differ | https://www.isaca.org/resources/reports/state-of-cybersecurity-2026 |
| SANS Institute and GIAC | SOC survey, AI survey, workforce report, AI certifications | https://www.sans.org/research/security-operations-report |
| IANS and Artico Search | Security budget benchmark | https://www.ians.com/lp/security-budget-benchmark-report |
| IBM and Ponemon | Cost of a Data Breach (vendor-sponsored) | https://www.ibm.com/reports/data-breach |
| WEF Global Cybersecurity Outlook | International executive survey with Accenture | https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2026.pdf |
| CompTIA | SecAI+ credential; AI adoption research | https://www.comptia.org/en-us/certifications/secai/ |
| Gated or not read: Verizon DBIR 2026, Mandiant M-Trends 2026, full ISACA, SANS and ISC2 reports, Gartner and Forrester research | Primary benchmarks for breaches and SOC metrics | https://www.verizon.com/business/resources/reports/dbir/ |

### Academic venues and research centres

| Venue or centre | Why it matters | Link |
|---|---|---|
| USENIX Security; IEEE S&P; NDSS; ACM CCS (15-19 Nov 2026) | Peer-reviewed work on agent defences, log-borne prompt injection, human-AI teaming, AI-written code | https://www.usenix.org/conference/usenixsecurity26/technical-sessions |
| arXiv (cs.CR) | Fastest channel for SOC-agent, patching and CTI benchmarks; mostly preprints read at abstract level | https://arxiv.org/ |
| Georgetown CSET; CMU SEI (CERT); UC Berkeley CLTC; Stanford Cyber Policy Center | Policy and applied research on AI and cyber | https://cset.georgetown.edu/publications/?fwp_topic=cybersecurity |
| DARPA AI Cyber Challenge | Best public scored benchmark of autonomous find-and-fix | https://aicyberchallenge.com/ |

### Publications, podcasts and communities

| Outlet | Note | Link |
|---|---|---|
| Dark Reading; The Hacker News; CSO Online; SecurityWeek; Cybersecurity Dive; The Record | Daily news; vendor-contributed pieces are labelled as such | https://www.darkreading.com/ |
| The Register (Black Hat and DEF CON coverage) | Strong conference journalism | https://www.theregister.com/security/2026/08/17/black-hat-and-def-con-are-ai-conferences-now-too/5288076 |
| Risky Business; The CyberWire; Darknet Diaries; Cloud Security Podcast | Podcasts | https://risky.biz/ |
| tl;dr sec; Detection Engineering Weekly; SANS NewsBites | Curated practitioner newsletters | https://www.detectionengineering.net/ |
| Venture in Security; Software Analyst Cyber Research; Resilient Cyber; Latio | Market structure and vendor-landscape analysis | https://ventureinsecurity.net/ |

### Vendors, providers and firms to watch

Treat their figures as vendor claims unless a named customer reports a measurement.
- **Platforms:** CrowdStrike, Palo Alto Networks, Microsoft, Google (Mandiant, GTIG, Wiz), Cisco/Splunk.
- **AI SOC and MDR:** Arctic Wolf, Expel, eSentire, Huntress, Torq, Exaforce, Dropzone AI, Prophet Security, 7AI, Intezer.
- **Code and vulnerability:** Anthropic (Glasswing), OpenAI (Codex Security), Google DeepMind, GitHub, Snyk, AWS.
- **Consultancies and testing firms:** Trail of Bits (the best-documented), Bishop Fox, Accenture. Big Four
  AI-security service lines were not documented in public sources reached.
- **Insurers and brokers:** Marsh, Swiss Re, Munich Re, Coalition, Beazley.

### Where the evidence is thin

- Independent, production-scale miss, override or error rates for any AI triage, review or response tool: none found.
- Cost per investigation, MDR and MSSP margins and pricing changes after AI: vendor claims only.
- Entry-level hiring effects specific to security; burnout effects of AI triage.
- In-house case studies outside very large engineering firms; small and mid-size teams.
- Defender AI in human risk, data security, privacy engineering and fraud.
- OT and critical infrastructure; regulators outside the US, UK, EU, New York and India; ISO/IEC 42001 text.
- Gartner primary research (known only through vendor summaries or search results).

## Part B. Shared source keys

Format: key, publisher, title (type, date), URL.

- **ACCENTURE-DRAGOS-2026**: Accenture, *Accenture to strengthen critical infrastructure defense (Dragos, runZero, NetRise)* (firm press release, 2026-06-18; closings to 2026-09-17). https://newsroom.accenture.com/news/2026/accenture-to-strengthen-critical-infrastructure-defense-with-end-to-end-cybersecurity-platform-in-age-of-ai-driven-cyber-threats-and-geopolitical-risk
- **AIACT-EXPLORER-2024**: Future of Life Institute AI Act Explorer, *AI Act Articles 14, 15, 73 and Annex III (unofficial text of Regulation (EU) 2024/1689)* (regulator text, 2024). https://artificialintelligenceact.eu/article/14/
- **ANTHROPIC-GLASSWING-2026**: Anthropic, *Project Glasswing: Securing critical software for the AI era* (vendor, author-side claims, 2026-04-07; update 2026-10-06). https://www.anthropic.com/glasswing
- **ANTHROPIC-SKILLS-2026**: Anthropic, *How AI assistance impacts the formation of coding skills* (research, author-side, 2026-01-29). https://www.anthropic.com/research/AI-assistance-coding-skills
- **ARCTICWOLF-ANALYSTS-2026**: Arctic Wolf, *How the Aurora Agentic SOC Is Building the Next Generation of SOC Analysts* (vendor blog, 2026-09-25). https://arcticwolf.com/resources/blog/how-aurora-agentic-soc-is-building-next-generation-of-soc-analysts/
- **ARCTICWOLF-AURORA-2026**: Arctic Wolf, *Arctic Wolf's Aurora Agentic SOC sets a new standard for scale, value, trust and speed in the age of AI* (vendor press release, 2026-08-03). https://arcticwolf.com/resources/press-releases/arctic-wolfs-aurora-agentic-soc-sets-a-new-standard-for-scale-value-trust-and-speed-in-the-age-of-ai/
- **ARXIV-2605.24421**: arXiv preprint, *Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content* (academic, abstract read, 2026-05-23). https://arxiv.org/abs/2605.24421
- **ARXIV-2610.10608**: Tsegai, Kantchelian, Yao and Gao (arXiv preprint), *From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage* (academic, abstract read, 2026-10-07). https://arxiv.org/abs/2610.10608
- **AWS-SECAGENT-2026**: AWS Security Blog, *AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs* (vendor self-test, 2026-10-15). https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/
- **BEAZLEY-AICYBER-2026**: Beazley, *Beazley confirms affirmative AI cyber cover* (insurer, 2026-09-17). https://www.beazley.com/en-US/news-and-events/beazley-confirms-affirmative-ai-cyber-cover/
- **BIS-FSI75-2026**: BIS Financial Stability Institute with IAIS, *FSI Insights No 75: Cyber insurance unpacked: the corporate digital safety net* (supervisory research, 2026-06). https://www.iais.org/uploads/2026/10/FSI-IAIS-Insights-Cyber-insurance-unpacked-the-corporate-digital-safety-net.pdf
- **CISA-AGENTIC-2026**: CISA with ASD's ACSC and partners, *Careful Adoption of Agentic AI Services* (government guidance, 2026-05-01). https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services
- **CISCO-SPLUNK-CONF26-2026**: Cisco Blogs, *Splunk .conf26: Tracking the Triage Agent in the Agentic SOC* (vendor, event SOC, 2026-10-08). https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/
- **COALITION-CLAIMS-2026**: Coalition, *2026 Cyber Claims Report* (insurer claims data, 2026-03-05). https://www.coalitioninc.com/announcements/2026-cyber-claims-report
- **COMPTIA-SECAI-2026**: CompTIA, *SecAI+ Certification V1* (certification body, launched 2026-02-17). https://www.comptia.org/en-us/certifications/secai/
- **COVINGTON-CIRCIA-2026**: Covington, Inside Privacy, *CISA Submits Final CIRCIA Rule for OMB Review* (law firm, 2026-10-08). https://www.insideprivacy.com/critical-infrastructure/cisa-submits-final-circia-rule-for-omb-review/
- **COVINGTON-SOLARWINDS-2025**: Covington, Inside Privacy, *SEC Voluntarily Dismisses SolarWinds Litigation* (law firm, 2025-11-21). https://www.insideprivacy.com/cybersecurity-2/sec-voluntarily-dismisses-solarwinds-litigation/
- **CRIBL-RADIANT-2026**: Cribl, *Cribl advances AI-powered security operations with new AI SOC acquisition* (vendor press release, 2026-08-19). https://cribl.io/news/cribl-advances-ai-powered-security-operations-with-new-ai-soc-acquisition/
- **CROWDSTRIKE-AGSOC-2026**: CrowdStrike, *CrowdStrike Delivers the Next Evolution of the Agentic SOC* (vendor, 2026-09-02, updated 2026-09-18). https://www.crowdstrike.com/en-us/blog/crowdstrike-delivers-next-evolution-of-agentic-soc/
- **CRWD-FY27Q2-2026**: CrowdStrike, *CrowdStrike reports second quarter fiscal year 2027 financial results* (vendor earnings release, 2026-08-26). https://www.morningstar.com/news/business-wire/20260826812507/crowdstrike-reports-second-quarter-fiscal-year-2027-financial-results
- **CW-NCSCUK-2026**: Computer Weekly, *UK's NCSC warns of 'wave of patches'* (press, 2026-05-04). https://computerweekly.com/news/366642625/UKs-NCSC-warns-of-wave-of-patches
- **D3-AGENTICMDR-2026**: D3 Security, *The 10 best agentic SOC platforms for MDR providers in 2026* (vendor blog, 2026-09-08). https://d3security.com/blog/agentic-soc-for-mdr-providers/
- **D3-SOCREBUILD-2026**: D3 Security, *The SOC Rebuild Index: 2026 Edition* (vendor analysis of 665 US postings, 2026-08-27). https://d3security.com/resources/soc-rebuild-index-2026/
- **DARKREADING-LIABILITY-2026**: Dark Reading, *When AI Agents Commit Breaches, Humans May Not Be Held Liable* (press, 2026-10-16). https://www.darkreading.com/insider-threats/ai-agents-breaches-humans-liable
- **DEBEVOISE-8K-2026**: Debevoise Data Blog, *Cybersecurity Incident Disclosure: Form 8-K Tracker (Two-Year Update)* (law firm, 2026-05-21). https://www.debevoisedatablog.com/2026/05/21/cybersecurity-incident-disclosure-form-8-k-tracker-two-year-update/
- **DROPZONE-PRICING-2026**: Dropzone AI, *Pricing: AI SOC analyst investigation capacity* (vendor price page, fetched 2026-10-17). https://www.dropzone.ai/pricing
- **DSIT-CYBERSKILLS-2025**: UK Department for Science, Innovation and Technology, *Cyber security skills in the UK labour market 2025* (government research, 2025-09-19). https://www.gov.uk/government/publications/cyber-security-skills-in-the-uk-labour-market-2025
- **EC-ACTIONPLAN-2026**: European Commission, *EU Action Plan on Cybersecurity and Artificial Intelligence* (regulator, 2026-07-07). https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence
- **EC-AIACT-2026**: European Commission, *AI Act: regulatory framework for AI (status and timeline)* (regulator, checked 2026-10-17). https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- **EC-CRA-2026**: European Commission, *Cyber Resilience Act* (regulator, page updated 2026-09-07). https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- **EC-CRAREPORTING-2026**: European Commission, *Cyber Resilience Act: reporting obligations* (regulator, 2026). https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- **EC-NIS2**: European Commission, *NIS2 Directive: securing network and information systems* (regulator, page updated 2026-07-02). https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
- **ESENTIRE-2026**: eSentire, *Homepage and newsroom (Controlled Autonomy SecOps; AI security acquisition of 2026-09-15)* (vendor, observed 2026-10-17). https://www.esentire.com/
- **EURLEX-DORA-2022**: EUR-Lex, *Regulation (EU) 2022/2554 (DORA)* (law, 2022-12). https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng
- **EURLEX-NIS2-2022**: EUR-Lex, *Directive (EU) 2022/2555 (NIS2)* (law, 2022-12). https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng
- **EXAFORCE-LATIO-2026**: Exaforce, *What the 2026 Latio Security Operations Market Report Gets Right About the AI SOC* (vendor summary of analyst report, 2026-06-04). https://www.exaforce.com/blogs/what-the-2026-latio-security-operations-market-report-gets-right-about-the-ai-soc
- **EXAFORCE-SERIESB-2026**: Exaforce, *Defending at the speed of AI: Announcing our $125M Series B* (vendor, 2026-05-12). https://www.exaforce.com/blogs/series-b
- **EXPEL-GARTNERMDR-2026**: Expel, *AI-augmented, still human-led: What changed in the 2026 Gartner Market Guide for MDR* (vendor blog quoting Gartner, 2026-09-21). https://expel.com/blog/what-changed-in-the-2026-gartner-market-guide-for-managed-detection-and-response/
- **FIGMA-AGENTS-2026**: Figma, *How we secure Figma's internal systems with agents* (in-house case study, 2026-07-29). https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/
- **FORRESTER-PV-2026**: Forrester, *Proofpoint + Varonis: The platform promise meets the integration test* (analyst blog, 2026-10-17). https://www.forrester.com/blogs/proofpoint-varonis-the-platform-promise-meets-the-integration-test/
- **FORRESTER-RSAC-2026**: Forrester, *RSAC 2026: An AI Coming-Of-Age Story Without The Romance* (analyst blog, 2026-03-31). https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance
- **GARTNER-SOC-2025**: SecurityMEA, *Security skills gap to leave one-third of senior roles vacant by 2028* (trade press reporting Gartner analysts, 2025-01-27). https://securitymea.com/2025/01/27/security-skills-gap-to-leave-one-third-of-senior-roles-vacant-by-2028/
- **GARTNER-TRENDS-2026**: Gartner, *Gartner Identifies the Top Cybersecurity Trends for 2026* (analyst press release, 2026-02-05). https://www.gartner.com/en/newsroom/press-releases/2026-02-05-gartner-identifies-the-top-cybersecurity-trends-for-2026
- **GOOGLE-AGENTICSCAN-2026**: Google Cloud, *Using AI agents to secure Google infrastructure* (in-house case study by a vendor, 2026-09-19). https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure/
- **GOVIE-NCSC-2026**: Ireland NCSC (Department of Justice), *NCSC statement on Anthropic's Mythos Preview model for defensive cyber security purposes* (regulator, 2026-04-13). https://www.gov.ie/en/department-of-justice-home-affairs-and-migration/press-releases/national-cyber-security-centre-ncsc-statement-on-anthropics-mythos-preview-model-for-defensive-cyber-security-purposes/
- **GTIG-AITRACKER-2026**: Google Threat Intelligence Group, *GTIG AI Threat Tracker: From Prompting to Autonomy* (vendor research, 2026-09-08). https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/
- **GTIG-VULNTRENDS-2026**: Google Threat Intelligence Group, *Vulnerability Discovery and Exploitation Trends in the AI Era* (vendor research, 2026-09-30). https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
- **HANSARD-CSRB-2026**: UK Parliament Hansard, *Cyber Security and Resilience (Network and Information Systems) Bill, Lords second reading* (parliament, 2026-07-14). https://hansard.parliament.uk/Lords/2026-07-14/debates/29073BC1-AD49-48CF-A269-8E83A76AFE90/details
- **HELPNET-GARTNER-2026**: Help Net Security, *Gartner: 70% of SOCs will pilot AI agents. Only 15% will see results* (sponsored article by a Prophet Security product manager quoting a Gartner report; 2028 forecast; 2026-09-09). https://www.helpnetsecurity.com/2026/09/09/prophet-security-evaluating-ai-soc-agents/
- **HUNTON-SOLARWINDS-2024**: Hunton Andrews Kurth, *Judge Dismisses Most of SEC Case Against SolarWinds and Its CISO* (law firm, 2024-07-22). https://www.hunton.com/privacy-and-cybersecurity-law-blog/judge-dismisses-most-of-sec-case-against-solarwinds-and-its-ciso
- **HUNTRESS-PRICING-2026**: Huntress, *Pricing* (vendor price list, fetched 2026-10-17). https://www.huntress.com/pricing
- **IANS-BUDGET-2026**: IANS and Artico Search, *2026 Security Budget Benchmark Report (press release and landing page; report body gated)* (survey of 500+ security executives, 2026-09-15; headcount and productivity expectations are in the press release, https://www.ians.com/press/new-ians-and-artico-search-report-finds-ai-is-changing-cybersecurity-jobs-not-eliminating-them). https://www.ians.com/lp/security-budget-benchmark-report
- **IBM-CODB-2026**: IBM and Ponemon Institute, *Cost of a Data Breach Report 2026* (vendor-sponsored survey, 2026-07-29; figures from the press release, report PDF not opened). https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average (landing page: https://www.ibm.com/reports/data-breach)
- **INDAGENT-VERISK-2025**: IndependentAgent.com, *Verisk to Roll Out New General Liability Exclusions for Generative AI Exposures* (trade press, 2025-10-21). https://www.independentagent.com/vu_resource/verisk-to-roll-out-new-general-liability-exclusions-for-generative-ai-exposures/
- **INTEZER-GARTNERMDR-2026**: Intezer, *A Gartner take on the MDR market in 2026 (summarising Gartner's "The Impact of AI on MDR Services")* (vendor blog on analyst research, 2026; reposted 2026-05-29). https://intezer.com/blog/gartner-on-the-mdr-market-in-2026
- **ISACA-AAISM**: ISACA, *Advanced in AI Security Management (AAISM)* (certification page, checked 2026-10-17). https://www.isaca.org/credentialing/aaism
- **ISACA-AIPULSE-2026**: ISACA, *56% of Digital Trust Pros Don't Know How Fast They Could Shut Down AI After a Security Incident* (professional-body poll of 3,400+, 2026-03-23). https://www.isaca.org/about-us/newsroom/press-releases/2026/digital-trust-pros-dont-know-how-fast-they-could-shut-down-ai-after-a-security-incident
- **ISACA-SOC-2026**: ISACA, *Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises (State of Cybersecurity 2026, global release and infographic; 1,800+ respondents)* (professional-body survey, 2026-09-22). https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises
- **ISC2-WORKFORCE-2024**: ISC2, *2024 ISC2 Cybersecurity Workforce Study* (professional-body survey, 2024-10-31). https://www.isc2.org/Insights/2024/10/ISC2-2024-Cybersecurity-Workforce-Study
- **ISC2-WORKFORCE-2025**: ISC2, *2025 ISC2 Cybersecurity Workforce Study* (professional-body survey of 16,029, 2025-12-04). https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study
- **JOBS-HUNTRESS-2026**: Huntress, *Security Operations Analyst (Australia), posting 7998473003* (job posting, 2026-10-09). https://job-boards.greenhouse.io/huntress/jobs/7998473003
- **MITRE-ATTCK-2026**: MITRE, *ATT&CK v20 release notes* (standard-setter, 2026-10). https://attack.mitre.org/resources/updates/
- **MSLEARN-SCU-2026**: Microsoft Learn, *Security Copilot compute unit capacity; Security Copilot for Microsoft 365 E5 and E7 customers* (vendor documentation, rollout from 2025-11-18). https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion
- **MSSPALERT-AW-2026**: MSSP Alert, *Arctic Wolf expands Agentic SOC with AI investigations and $3m cyber warranty* (trade press, 2026-08-03). https://www.msspalert.com/news/arctic-wolf-expands-agentic-soc-with-ai-investigations-and-3m-cyber-warranty
- **NDSS-2026**: NDSS Symposium, *Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering* (academic, 2026-02). https://www.ndss-symposium.org/ndss-paper/decompiling-the-synergy-an-empirical-study-of-human-llm-teaming-in-software-reverse-engineering/
- **NIST-COSAIS-2026**: NIST, *SP 800-53 Control Overlays for Securing AI Systems (COSAiS)* (standard-setter, concept paper 2025-08-14; annotated-outline discussion draft 2026-01-08). https://csrc.nist.gov/projects/cosais
- **NIST-CSF-2024**: NIST, *Cybersecurity Framework 2.0* (standard-setter, 2024-02). https://www.nist.gov/cyberframework
- **NYDFS-AI-2024**: NY Department of Financial Services, *Cybersecurity Risks Arising from AI and Strategies to Combat Related Risks* (regulator letter, 2024-10-16). https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks
- **NYDFS-FRONTIER-2026**: NY Department of Financial Services, *Heightened Cybersecurity Risks Associated with Frontier AI Models* (regulator letter, 2026-05-21). https://www.dfs.ny.gov/industry-guidance/industry-letters/20260521-heightened-cybersecurity-risks-assoc-with-frontier-ai-models
- **OWASP-AGENTIC-2025**: OWASP GenAI Security Project, *Top 10 for Agentic Applications for 2026* (standard-setter, 2025-12-09). https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **PROOFPOINT-VARONIS-2026**: Proofpoint and Varonis, *Proofpoint to acquire Varonis in a $6.3 billion transaction* (vendor press release, 2026-10-15). https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-acquire-varonis-creating-global-leader-data-and-ai-security
- **PROPHET-GARTNERROLES-2026**: Prophet Security, *Will AI Replace the SOC Team? Gartner on SOC Team Structure and Roles* (vendor blog relaying Gartner, 2026-10-07). https://www.prophetsecurity.ai/blog/will-ai-replace-soc-teams
- **PROPHET-ISOC-2026**: Prophet Security, *What Microsoft ISOC Means for Security Operations* (competitor's account, 2026-10-07). https://www.prophetsecurity.ai/blog/microsoft-isoc-security-operations
- **RSAC-WORKFORCE-2026**: RSA Conference with SANS and GIAC, *AI, Regulation, & the Battle for Talent: The Future of the Cyber Workforce (2026 SANS/GIAC Workforce Report premiere; slides)* (conference slides, 2026-03-23). https://www.rsaconference.com/library/presentation/usa/2026/ai%20regulation%20%20the%20battle%20for%20talent%20the%20future%20of%20the%20cyber%20workforce
- **SANS-AI-2026**: Swimlane, *A SOC Leader's Guide to the 2026 SANS AI Survey* (vendor summary of a SANS survey, 2026-08-17). https://swimlane.com/blog/sans-ai-2026-soc-trust/
- **SANS-SOC-2026**: SANS Institute, *SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense* (survey of 444 practitioners and 69 leaders; landing page and FAQ, 2026). https://www.sans.org/research/security-operations-report
- **SEVENAI-2026**: 7AI, *Homepage counters and customer quotes* (vendor, observed 2026-10-17). https://7ai.com/
- **SIFMA-SEC-2026**: SIFMA, ABA, BPI, ICBA and IIB, *Reforming Regulation S-K's Cybersecurity Disclosures (joint trades letter)* (trade associations, 2026-04-10). https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades
- **SPLUNK-RSACSOC-2026**: Splunk (Cisco), *Lessons from the 10th RSAC SOC* (vendor, event SOC, 2026-08-24). https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html
- **THN-CERTIN-2026**: The Hacker News, *CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing* (press on a CERT-In advisory of 2026-10-15, 2026-10-16). https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html
- **TOB-1PASSWORD-2026**: Trail of Bits, *1Password's AI patching benchmark is misleading* (consultancy blog, 2026-09-15). https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/
- **TOB-PTP-2026**: Trail of Bits, *Introducing Patch the Planet* (consultancy blog, 2026-06-22). https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
- **TORQ-SERIESD-2026**: Torq, *Torq Secures $140M Series D* (vendor press release, 2026-01-12). https://torq.io/news/torq-seriesD/
- **WIRED-OPENAI-2026**: WIRED, *OpenAI Didn't Notice Its AI Agents Using a Message Board to Plan Their Hacking Spree* (press, 2026-08-05). https://www.wired.com/story/openai-didnt-notice-its-ai-agents-using-a-message-board-to-plan-their-hacking-spree/
- **YAHOO-CCS-2026**: Yahoo Finance, *Anthropic's Claude Code Security launch rattles cybersecurity stocks* (financial press, 2026-02-23). https://finance.yahoo.com/news/anthropic-claude-code-security-launch-200400637.html
