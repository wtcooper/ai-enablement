# Threat intelligence (security)

Sources checked 2026-10-17. Use cases live in `../use-cases/threat-intelligence.yaml` (24 entries). Ids are shortened here: `#05`
means `security-threat-intelligence-05`; other modules' ids are in full. Source keys in brackets, such as [SANS-CTIPR-2026], are in the YAML or in §10.
**Evidence is thin and mostly vendor-shaped.** 14 of 24 entries are graded A or B, but only two carry a figure a named
organization reports as measured (Grow Therapy's own cost and noise data, `#21`; Microsoft's customer-feedback precision for its
own agent, `#22`). Everything else is a vendor claim, a customer quote in a vendor case study, a survey share or a lab benchmark.
No source publishes analyst override rates, error rates of a deployed CTI assistant, or a parallel run against human output.
Say so when you quote a figure.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Cyber threat intelligence (CTI) is the work of collecting, analysing, reporting and sharing information about attackers: who
they are, how they operate and which indicators of compromise (IOCs: hashes, domains, IP addresses and similar traces) reveal
them. The module covers the intelligence cycle from requirements to dissemination, sharing through bodies such as FIRST and
ISACs (industry information sharing and analysis centers), and threat hunting (proactively searching your own telemetry for
attackers that no alert has caught). It applies to in-house CTI teams, intelligence vendors and managed providers. Alert triage
belongs to security-operations, response to incident-response, patch prioritization to vulnerability-exposure, and the security
of AI systems themselves to ai-security; overlaps are flagged by entry.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Direction and requirements | Agree priority intelligence requirements (PIRs: the standing questions the team must answer) with stakeholders | expert-judgment, coordination-scheduling | 91% of CISOs value CTI but only 26% say it drives their decisions; 57% of programs do not track maturity and 49% gather no systematic feedback [SANS-CTIPR-2026] |
| Collection | Feeds, vendor reports, OSINT (open-source intelligence), dark web and forums, stealer logs, partner and ISAC sharing, telemetry | research-synthesis | Alert noise and false positives top the problem list (65% of Flashpoint interviewees), then analyst bandwidth (55%) [FLASHPOINT-ENTERPRISE-2026]; over 50 million stealer logs posted in 2025 [FIRST-CON-2026] |
| Processing and enrichment | Extract indicators and entities, normalize, tag, map to MITRE ATT&CK (the public catalogue of attacker techniques), translate | data-reporting, transaction-processing | 13 of 18 practitioners struggle to isolate indicators from noisy data; 10 of 18 to map to taxonomies [ARXIV-2609.01174] |
| Analysis | Relevance to the organization, prioritization, malware analysis, attribution, campaign tracking | expert-judgment | Vendor reports contradict each other because of each vendor's collection bias [FIRST-CON-2026; ARXIV-2602.17458] |
| Production and dissemination | Briefings and finished reports for SOC, resilience leads and executives | document-production | Analyzing one incident from an article typically takes several hours (Microsoft-authored paper) [ARXIV-2603.09452] |
| Sharing | Redact, package as STIX/TAXII (the standard exchange formats) or MISP, label under TLP (Traffic Light Protocol sharing labels), publish to ISACs and partners | review-assurance, document-production | 17 of 18 practitioners cite exposure of sensitive data [ARXIV-2609.01174]; 55% of organizations lack legally reviewed sharing processes [SANS-CTIPR-2026] |
| Action | Turn intelligence into detection rules, blocklists, hunts, tickets and SOAR (automated response) playbooks | software-systems, coordination-scheduling | One inbound report can consume a morning from extraction to ticket [FEEDLY-AUTOMATE-2026]; about 40% say integration into workflows is mostly manual (vendor survey) [CYWARE-RSAC-2026] |
| Threat hunting | Trigger, hypothesis, query, analysis, conversion to standing detection | expert-judgment, research-synthesis | Scarce senior hunters [CYBERPROOF-HUNTING-2026]; query-language expertise [MSFT-HUNTASSIST-2026]; short log retention [INTEL471-HUNTING-2025] |
| Feedback and measurement | Track whether intelligence changed decisions | data-reporting | Practitioners reject report and IOC (indicator of compromise) counts in favour of decisions influenced and time from intelligence to action [FEEDLY-ROUNDUP-2026] |

Teams are small: most formal CTI teams have fewer than four full-time staff, and lack of time and of funding (44% each) are the
top barriers [SANS-CTIPR-2026].

## 3. Where AI is changing the work

Lenses: improve (assist or augment one step), automate (no person on the normal path), delegate (an agent owns a multi-step
outcome), reinvent (the service or operating model changes). Improve is crowded and mostly grade B or C. Automate has three
entries and no figures. Delegate has the only two grade A entries, both in hunting. Reinvent has one entry. **No evidence was found
for automate at step level**, or for new CTI service lines, pricing or sourcing models driven by AI.

**Direction, collection and processing**
- Improve: `#02` AI-supported OSINT collection (ENISA uses AI in a limited capacity for collection and processing, with all outputs
  validated by experts; B). `#03` underground, dark-web and stealer-log triage (Flare StealerLens, Mandiant 2023; C). `#06` ATT&CK
  mapping and hunt enrichment (Intel 471's hunters; lab F1 0.71 on sandbox reports but 0.22 on complex prose; B). `#01` idea: agents
  that watch PIR coverage (D). `#07` idea: merging whole report corpora into knowledge graphs and measuring vendor overlap (D).
- Automate: `#05` report-to-indicator pipelines that keep the source report attached and mark which tags are automatic (Cloudflare
  Threat Signals, Adobe; B, no figures; lab precision ranges from 0.03 to 0.78 depending on task).
- Delegate (frontier): `#04` a research prototype that elicits intelligence in forums by conversing with actors (C; legal and
  ethical questions unresolved).

**Analysis and production**
- Improve: `#11` cited Q&A over a vendor's intelligence corpus, including for non-security staff (Cowbell: answers in minutes not
  days, a customer quote; B). `#08` relevance scoring against an organization profile (Google, Microsoft; vendor claims only; C).
  `#09` malware-analysis agent (Google, CISA pre-deployment; C). `#10` research agent that drafts cited reports and verifies
  indicators against VirusTotal (Microsoft-authored; precision gains of a few points at several times the run time; B).
  `#12` scheduled and on-demand briefings for different audiences (Microsoft, Google Flows, Cowbell, CISA, ServiceNow posting; B).

**Sharing**
- Improve: `#13` PII screening before indicator sharing (CISA AIS, NLP not generative AI, analysts confirm every flag; B), plus lab
  pilots of LLM redaction and STIX packaging that over-redact or assert unsupported links.

**Action**
- Improve: `#14` report-to-detection rules (best agent reward 0.637 on a Microsoft benchmark; C). `#15` SOAR enrichment and MCP
  connections (MCP: a standard way to connect agents to tools and data) so agents pull intelligence on demand (Superhuman; B).
- Automate: `#16` Adobe's pipeline matches new indicators against EDR, email, cloud and identity logs; Adobe recommends that teams
  building similar systems also recheck earlier intelligence that produced no matches (B). `#18` agents that package takedown evidence for phishing and brand-abuse sites (vendor descriptions; C).
- Delegate: `#17` chained report-to-ticket workflows with an approval gate before any write (Feedly recipes, Cyware; C).

**Threat hunting**
- Improve: `#19` assistants inside human-led hunts (Intel 471, Microsoft Threat Hunting Assistant, Google's frontline team; B).
  `#23` CISA machine-learning anomaly surfacing on Einstein network data, with a CyberSentry equivalent at an early stage (B).
- Delegate: `#21` Grow Therapy's ~20 daily Claude hunts with an adversarial self-check, about $500 a month (A, self-reported).
  `#22` Microsoft's always-on investigation agent, 80.1% precision on customer feedback over 120 days (A, vendor's own product).
  `#20` CyberProof's managed hunting agents, "10 to 15 times more hunts" for an unnamed client (C).
- Counter-evidence to quote: unguided agentic hunting on raw logs flagged 3.8% of malicious events at best [ARXIV-2604.19533].

**Operating model**
- Reinvent: `#24` model providers' threat intelligence teams using their own models to investigate misuse (Anthropic, OpenAI; B).
  The self-service effect in `#11` (engineers outside security query intelligence directly) is the nearest sign of a change in
  who does the work.

Cross-module: `#21` overlaps `security-operations-07` (evidence-gated dismissal); `#22` is referenced from `security-operations-14`;
`#14` hands off to detection-rule work in `security-operations-15`; `#08` feeds `security-vulnerability-exposure-09` (prioritisation);
prompt-injection hardening is `security-ai-security-13`; `#18` sits next to fraud and brand protection in human-risk; Datadog's hunt for fake job applicants with "AI-driven risk
assessment" [FIRST-CON-2026] is in `security-human-risk-12`.

## 4. Interview probes

Ask in the person's setting (in-house CTI team, intelligence vendor, managed provider or ISAC).

1. **"Walk me through one inbound report: which steps does AI touch, and what review sits between AI output and your TIP, SIEM (the log and detection platform),
   ticketing or a stakeholder?"** Reveals where they sit on the ladder and whether `#05`, `#14` or `#17` apply; Feedly's rule is an
   approval step between any read stage and any write stage [FEEDLY-AUTOMATE-2026].
2. **"For one AI step, what share of output is accepted without edit, and have you measured precision against analyst verdicts on
   your own reports?"** Reveals whether any quality evidence exists; none is public, and lab precision for extraction ranges from
   0.03 to 0.78 depending on the task [ARXIV-2610.20417; ARXIV-2609.01174].
3. **"Can an analyst trace every AI-produced indicator, tag or sentence to its source and see whether a person or a machine applied
   it? Who owns the tag vocabulary?"** Reveals the trust conditions Cloudflare found decisive [CLOUDFLARE-THREATSIGNALS-2026].
4. **"Which intelligence, by TLP label and sharing agreement, may go into a hosted model today, who decided, and where is it
   written?"** Reveals handling risk and whether local models are needed (`#13`) [FIRST-TLP-2022].
5. **"What context does the model get: PIRs, asset inventory, an organization profile?"** Reveals readiness for relevance scoring
   (`#08`) and asset scoping (`#17`); DTN Advisory says vague requirements give noise at scale [DTN-CTI-2026].
6. **"What can an agent do without approval: tag, open tickets, update blocklists, deploy rules?"** Reveals the autonomy boundary;
   interviewees range from read-only assistants to agents that block IP addresses [FLASHPOINT-ENTERPRISE-2026].
7. **"What happens when a phishing email, forum post, stealer log or log line contains instructions aimed at your model? Have you
   tested it?"** Reveals exposure to the main failure mode (see §6) [USENIX-LOGINJECT-2026; FIRST-CON-2026].
8. **"How do you hunt today: who writes hypotheses and queries, how long do you keep logs, and how many hunts a month?"** Reveals the
   baseline for `#19` to `#22` and whether data is centralized; Grow Therapy says the data pipeline matters more than the AI
   [GROWTHERAPY-HUNT-2026].
9. **"Do finished reports disclose AI use, and who signs the analytic judgement?"** Reveals governance maturity; ENISA discloses AI
   use and keeps judgement with analysts [ENISA-ETL-2026; ENISA-CTL-2026].
10. **"Who legally reviewed your sharing processes, and does the review cover AI-assisted redaction and packaging?"** Reveals the 55%
    gap [SANS-CTIPR-2026] and fit for `#13`.
11. **"How do junior analysts build tradecraft if drafting, enrichment and mapping are automated? Do they still read primary
    sources?"** Reveals de-skilling risk Feedly warns about [FEEDLY-VALUE-2026].
12. **"Which intelligence actually changed a decision last quarter, and how would you know if AI made that more likely?"** Reveals
    whether the influence gap (26%) is the real problem; no source links AI to closing it.

## 5. Metrics and benchmarks

**Adoption (survey shares, unnamed organizations)**
- 45% of organizations use AI in CTI, mainly summarization and report writing, and 32% plan to (401 respondents, Nov 2025 to Jan
  2026; sponsor-supported) [SANS-CTI-2026]. Security operations (71%) overtook threat hunting as the top CTI use case [SANS-CTIPR-2026].
- Agentic AI: 25% in production, 20% piloting, 35% planning in 12 to 24 months, among just over 20 interviewees (vendor-commissioned)
  [FLASHPOINT-ENTERPRISE-2026]. Only 3 of 18 practitioners in a five-organization survey used LLMs to turn attack data into CTI
  [ARXIV-2609.01174]. Effective CTI-to-SecOps automation 13% to 26% year on year (vendor survey, count not stated) [CYWARE-RSAC-2026].

**Named deployments with figures**
- Microsoft agent: 80.1% precision over 120 days; median 28 minutes and USD 2.04 per investigation; 0.38% job failure (vendor-authored)
  [ARXIV-2605.20896].
- Grow Therapy hunts: $320 to $510 a month; about 60% cheaper with a smaller model for data gathering; 15+ to 2-3 findings per run
  after tuning (self-reported) [GROWTHERAPY-HUNT-2026].
- Vendor-published customer figures: Cowbell "over 90%" lower intelligence costs (platform-wide) and answers in minutes not days
  [RF-COWBELL-2026]; CyberProof 150 to 200 hunts a month and 20% more detection coverage for an unnamed client
  [CYBERPROOF-HUNTING-2026]; Google 98% internal accuracy on external events [GOOGLE-DARKWEB-2026]; Mandiant (2023) 96% fewer false
  positives in alert generation [MANDIANT-AIPHASES-2023]; Feedly's potential time savings of 20 to 85 minutes per workflow per
  report are estimates [FEEDLY-AUTOMATE-2026].

**Lab benchmarks (independent unless noted; preprints mostly)**

| Task | Result | Source |
|---|---|---|
| IOC extraction from sandbox reports | recall 0.25 to 0.31, precision 0.51 to 0.78 | [ARXIV-2609.01174] |
| Entity extraction from full incident reports | micro precision 0.03 to 0.34 | [ARXIV-2610.20417] |
| IOC recovery from malicious scripts | best 65.4 F1 | [ARXIV-2609.06149] |
| ATT&CK mapping, sandbox reports vs complex prose | F1 0.71 to 0.72 vs best 0.22 | [ARXIV-2609.01174; ARXIV-2606.18166] |
| Threat-level scoring of MISP records | fine-tuned F1 0.40 to 0.58 | [ARXIV-2609.07582] |
| Report to detection rule (16 models) | best reward 0.637 (Microsoft authors) | [ARXIV-2603.13517] |
| Open-ended agentic hunting on raw logs | best 3.8% of malicious events flagged | [ARXIV-2604.19533] |
| Hunt leads grounded in own assets | mean F1 0.44 to 0.85 vs flat retrieval | [ARXIV-2609.08790] |
| Prompt injection via log content | up to 88.2% success; layered defences cut 90.4% | [USENIX-LOGINJECT-2026] |

Cost: an open-weight model matched the strongest closed models on the detection benchmark at under a tenth of the cost, given enough
turns [ARXIV-2610.14180]. **Missing everywhere:** override and edit rates, error rates of deployed assistants, parallel runs, and any
independent test of a commercial CTI assistant on live data.

## 6. Guardrails

**Standards and regulation (none mention AI in CTI work)**
- TLP 2.0: recipients need the source's permission to share wider than the label; use in automated exchange is left to the designers,
  so whether a hosted model is inside the label's boundary is a policy decision to make explicitly [FIRST-TLP-2022].
- NIST SP 800-150: set sharing rules with legal and privacy input, including redaction [NIST-SP800150-2016]. NIST CSF 2.0 ties CTI
  to outcomes ID.RA-02 and DE.AE-07 [NIST-CSF-2024].
- EU: NIS2 Articles 29-30 and DORA Article 45 frame voluntary sharing, with GDPR and competition-law limits; NIS2 recital 51
  encourages AI for detection under data-protection principles [EURLEX-NIS2-2022; EURLEX-DORA-2022]. DORA's threat-led testing
  standard sets experience thresholds for intelligence providers and does not mention AI [EUR-DORATLPT-2025]. No AI Act
  obligation specific to CTI was found [EC-AIACT-2026].
- US: AIS liability protections rest on the Cybersecurity Information Sharing Act of 2015, extended to 2026-09-30; status after that
  date was not confirmed [CISA-AIS-2026].
- ENISA's published boundary: AI may help with monitoring, collection and limited editorial work; trends, judgements and
  assessments stay with accountable analysts, and AI use is disclosed in the report [ENISA-CTL-2026; ENISA-ETL-2026].

**Controls that recur in the evidence**
- Keep provenance: every indicator linked to its source, automatic tags marked, vocabulary fixed [CLOUDFLARE-THREATSIGNALS-2026].
- Treat ingested content as hostile: one crafted report or email can steer an LLM-assisted workflow [FIRST-CON-2026]; attackers have
  embedded prompts in malware loaders aimed at LLM security scanners [GTIG-AITRACKER-2026]; defences reduce but do not remove the risk
  [USENIX-LOGINJECT-2026; ARXIV-2605.24421].
- Confidence is not verification: a single misattribution sentence flipped high-confidence judgements in 95.6 to 100% of cases;
  use confidence to set review priority only [ARXIV-2610.20417].
- Least privilege for agents: dedicated agent identity with minimal read rights [MSFT-TIBAGENT-2026]; OpenCTI warns an "always allow"
  approval also covers unattended scheduled runs [OPENCTI-COPILOT-2026]; chain read-only stages first [FEEDLY-AUTOMATE-2026].
- Run in parallel first: Adobe and Google both advise keeping existing processes running while trust builds [ADOBE-CTRI-2026;
  GOOGLE-GTIRELEVANCE-2026].
- Restricted material: a local or open-weight model keeps unredacted reports inside the boundary [ARXIV-2609.01174].

**Steps that need human judgement:** attribution, risk ratings and business-impact statements [FEEDLY-AUTOMATE-2026]; scoping a
threat to your environment; approving any write to live tooling (blocklists, rules, tickets) [FEEDLY-AUTOMATE-2026], with automated
containment kept to high-confidence, low-risk actions and high-risk actions left to people [SECURITYWEEK-HUNTING-2026]; release of
shared intelligence after redaction [CISA-AIUC-2024; GAO-24-106246]; forming and owning hunt hypotheses [INTEL471-HUNTING-2025];
the final analytic judgement [ENISA-CTL-2026]; any active engagement with threat actors (`#04`).

## 7. Roles and how they evolve

- **Work is becoming engineering-shaped.** Anthropic, Cloudflare, Coinbase and GitLab postings ask threat intelligence staff to build
  pipelines, automation, MCP integrations or AI-powered workflows [ANTHROPIC-JOBTIE-2026; CLOUDFLARE-JOBSTIE-2026; COINBASE-JOBTIPE-2026;
  GITLAB-JOBTRE-2026]; OpenAI pairs engineers with investigators [OPENAI-JOBII-2025]. Not every posting changes: Recorded Future and
  Dragos analyst postings read in full do not mention AI [RECORDEDFUTURE-JOBTIRA-2026; DRAGOS-JOBCTI-2026].
- **Analysts become reviewers and validators.** Feedly says AI absorbs feed aggregation, enrichment and first drafts, and the premium
  moves to interpretation, communication and validation; it defines AI literacy as tool building, context engineering and validation
  [FEEDLY-HIRING-2026]. ServiceNow's senior reports role asks for LLM-driven drafting on top of eight-plus years of CTI experience
  [JOB-SERVICENOW-2025]. Hunters are asked to verify AI output before production [HUNTRESS-JOBDETH-2026].
- **Hunters stay in charge of hypotheses.** Experts quoted by SecurityWeek expect augmentation, not replacement [SECURITYWEEK-HUNTING-2026].
- **Non-security staff self-serve.** Superhuman's engineers query intelligence directly [RF-SUPERHUMAN-2026].
- **Capacity pressure is a stated driver.** A healthcare leader says "we can't hire our way out" [FLASHPOINT-ENTERPRISE-2026].
  Feedly warns efficiency narratives could bring budget cuts, hiring freezes and fewer entry-level roles [FEEDLY-VALUE-2026].
- **Gap:** no headcount, hiring or junior-pipeline data for CTI teams exists in the sources; AI is the top skills need across
  cybersecurity (41%) [ISC2-WORKFORCE-2025].

## 8. Frontier

- 2026-05-20: Microsoft reports an always-on investigation agent at scale across Defender customers (`#22`) [ARXIV-2605.20896].
- 2026-08-12: Google releases scheduled agentic investigations (Flows) and an Agentic API in public preview; its Agentic MCP server
  guide was last updated 2026-09-16 [GOOGLE-GTICHANGELOG-2026; GOOGLE-GTIMCP-2026]; 2026-09-29: Cloudflare makes Threat Signals free to every account
  [CLOUDFLARE-THREATSIGNALS-2026].
- 2026-08-19: knowledge packaged as portable "skills" attached to detections (Vega's Detection Skills) [DETENGWEEKLY-167-2026].
- 2026-09-08: Google reports adversaries moving from prompting to agentic workflows, including a credential-harvesting campaign planned
  and run in under six hours [GTIG-AITRACKER-2026]. 2026-10-15: CERT-In reports a campaign using open-source AI-agent offensive
  frameworks that cut time from first access to impact from days to a few hours [THN-CERTIN-2026]. Both raise the speed CTI must match.
- 2026-09-18: ENISA publishes a written boundary between AI assistance and analyst judgement [ENISA-CTL-2026].
- 2026-09-30: Google advises moving from mass patching to threat-intelligence-driven triage; 62% of vulnerabilities exploited
  January to August 2026 were zero-days [GTIG-VULNTRENDS-2026]. Intelligence prioritization becomes central to vulnerability work.
- 2026-10-09: open-weight models compete on cost for CTI agents [ARXIV-2610.14180].
- 2026-10-13: ATT&CK v20 adds AI-focused and AI-enabled techniques and an AI-assisted breach campaign, so analysts must tag AI-related
  behaviour [MITRE-ATTCK-2026]; Flashpoint's interviewees rank AI-related threats first for expanded coverage [FLASHPOINT-ENTERPRISE-2026].
- Contested: in January six of 14 practitioners called AI-threat narratives overhyped [FEEDLY-ROUNDUP-2026]; in February Intel 471
  said fully autonomous threat-actor operations "has yet to occur" [INTEL471-AIHUMAN-2026].
- Open: a government-led AI-ISAC was still in development with no timeline in February 2026 [NEXTGOV-AIISAC-2026]. Research
  generates adversary-emulation plans from CTI reports (84.22% execution success in a test environment), relevant to threat-led
  testing under DORA and TIBER-EU; no provider was found using it [ARXIV-2607.14566; EUR-DORATLPT-2025].

## 9. Common objections

- **"An agent that's confidently wrong is worse than one that's slow"** [FLASHPOINT-ENTERPRISE-2026]. Agree, and design for it: Grow
  Therapy makes the model argue against its own findings and tunes each hunt in staging before alerting (15+ to 2-3 findings per run)
  [GROWTHERAPY-HUNT-2026]; Microsoft uses fail-closed suppression [ARXIV-2605.20896]. Start with reviewable, reversible tasks.
- **"LLMs can't do this reliably."** Partly true. Extraction and mapping work on clean input but degrade on complex prose (ATT&CK F1
  0.71 vs 0.22), and open-ended hunting fails (3.8%) [ARXIV-2609.01174; ARXIV-2606.18166; ARXIV-2604.19533]. Grounding in your own
  assets helps (hunt-lead F1 0.44 to 0.85) [ARXIV-2609.08790]. Use AI for bounded sub-tasks and measure on your own reports.
- **"We can't put partner intelligence into a model."** Valid under TLP and sharing agreements [FIRST-TLP-2022]. Options: decide in
  policy which labels may leave the boundary, or run an open-weight model locally [ARXIV-2609.01174; ARXIV-2610.14180].
- **"It will break trust and chain of custody in sharing"** (RH-ISAC) [CSD-ISACAI-2026]. Keep provenance links and human approval;
  CISA's PII screening routes every flag to an analyst [CISA-AIUC-2024; GAO-24-106246; CLOUDFLARE-THREATSIGNALS-2026].
- **"It's just rebranded enrichment and summarization"** [FEEDLY-ROUNDUP-2026]. Often fair; Forrester argues for the "least AI" that
  does the job [SANS-LEASTAI-2026]. Where the evidence shows more than enrichment, it is continuous, agent-run hunting (`#21`, `#22`).
- **"Our analysts will lose their skills."** A real risk [FEEDLY-VALUE-2026]. Require primary-source review before an assessment is
  submitted and disclose AI use in methodology [FEEDLY-VALUE-2026; ENISA-ETL-2026].
- **"Attackers will poison the inputs."** Correct and demonstrated [FIRST-CON-2026; GTIG-AITRACKER-2026]. Layered defences cut log
  injection by 90.4% but leave residual risk, so keep humans on suppress or escalate decisions [USENIX-LOGINJECT-2026].
- **"Vendor numbers are marketing."** Mostly yes; say so. Ask for override rates and a pilot against your own baseline; Forrester asks
  vendors for testing and validation mechanisms [FORRESTER-PREDICT-2025].

## 10. Sources

Full entries (title, publisher, URL, date, locator) are in the YAML for every key cited there. Keys cited only in this file:

- [GTIG-AITRACKER-2026] Google Threat Intelligence Group, "GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI", 2026-09-08, https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/
- [GTIG-VULNTRENDS-2026] Google Threat Intelligence Group, "Vulnerability Discovery and Exploitation Trends in the AI Era", 2026-09-30, https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
- [THN-CERTIN-2026] The Hacker News, report on the CERT-In advisory of 2026-10-15 on AI agents, 2026-10-16, https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html
- [NIST-CSF-2024] NIST, Cybersecurity Framework 2.0, 2024-02-26, https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
- [EUR-DORATLPT-2025] Commission Delegated Regulation (EU) 2025/1190 (threat-led penetration testing), 2025-02-13, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R1190
- [EC-AIACT-2026] European Commission, AI Act policy page (undated; read 2026-10-17), https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- [ARXIV-2607.14566] "Fully Automated End-to-End Adversary Emulation from MITRE ATT&CK Based CTI Using LLMs", arXiv, 2026-07-16, https://arxiv.org/abs/2607.14566
- [NEXTGOV-AIISAC-2026] Nextgov/FCW, "AI info-sharing center is in development, CISA official says", 2026-02-03, https://www.nextgov.com/cybersecurity/2026/02/ai-info-sharing-center-development-cisa-official-says/411167
- [ISC2-WORKFORCE-2025] ISC2, 2025 Cybersecurity Workforce Study, 2025-12-04, https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study
- [CLOUDFLARE-JOBSTIE-2026] Cloudflare, Senior Threat Intelligence Engineer (posting), 2026-01-22, https://boards.greenhouse.io/cloudflare/jobs/7558153
- [GITLAB-JOBTRE-2026] GitLab, Threat Research Engineer (posting), 2026-10-15, https://job-boards.greenhouse.io/gitlab/jobs/8867649002
- [RECORDEDFUTURE-JOBTIRA-2026] Recorded Future, Threat Intelligence Response Analyst (posting), 2026-10-02, https://job-boards.greenhouse.io/recordedfuture/jobs/8859088002
- [DRAGOS-JOBCTI-2026] Dragos, Associate Principal Cyber Threat Intelligence Analyst (posting), 2026-08-27, https://job-boards.greenhouse.io/dragos/jobs/5389909008
