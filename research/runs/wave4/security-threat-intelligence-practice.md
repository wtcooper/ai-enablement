# Security / threat-intelligence / practice: what CTI and hunting teams and their providers actually do with AI

Archetype: security. Module: threat-intelligence (collection, analysis, reporting and sharing of cyber threat intelligence, and threat hunting). Angle: practice. Researched 2026-10-17. Window: mostly 2025-10 to 2026-10, with older foundation sources flagged by date (Mandiant 2023, MITRE 2023, CTIBench 2024).

## 1. Summary

- **Practice clusters in six steps of the CTI cycle**, and most of it is shipped as vendor features rather than built in-house: asking questions of a vendor's intelligence corpus; turning unstructured reports into indicators, ATT&CK techniques and tags; turning reports into hunts or detection rules; drafting briefings; filtering global intelligence against an organization profile; and enriching alerts through SOAR or an MCP server. Named in-house or customer deployments are few: Adobe, Cloudflare, Superhuman, Cowbell, CISA, and the CTI division behind a Microsoft-authored paper (see use cases 01 to 03, 07, 10, 14, 16).
- **Adoption is real but shallow and mostly in summarization.** SANS's 2026 CTI survey press release says 45% of organizations use AI in CTI programs, mainly for summarization and report writing, with a human in the loop (SANS-CTI-2026). A Flashpoint-commissioned interview study of just over 20 enterprise budget owners reports 25% using agentic AI in production, 20% piloting and 35% planning within 12 to 24 months (FLASHPOINT-ENTERPRISETI-2026). An 18-person practitioner survey across five organizations found only 3 using LLMs to turn attack data into shareable CTI (ARXIV-2609.01174).
- **Measured quality evidence exists but is thin, mostly self-reported and mixed.** The strongest production-scale number is Microsoft's Dynamic Threat Detection Agent: 80.1% precision from customer feedback over 120 days (ARXIV-2605.20896, vendor-authored). The best CTI-workflow measurement is the Microsoft-authored Threat Research Agent paper: a few points of precision gained on IoC and TTP extraction at higher run time, and larger gains in expert ratings of drafted narratives; its text and appendix table disagree on the size of the IoC gain (ARXIV-2603.09452). Independent academic tests are far weaker: best open-source F1 of 0.22 on multi-label ATT&CK classification of complex reports (ARXIV-2606.18166), micro precision of 0.03 to 0.34 on entity extraction (ARXIV-2610.20417), and 3.8% of malicious events flagged in open-ended agentic hunting (ARXIV-2604.19533). **No deployer in this sample publishes error rates, analyst override rates or a parallel-run comparison.**
- **The work is becoming engineering-shaped.** Postings for threat-intelligence roles at Anthropic, Cloudflare, Coinbase, GitLab and OpenAI ask for people who build pipelines, MCP servers and agent workflows. Some analyst postings (Recorded Future, Dragos) say nothing about AI.
- **Trust and provenance, not model quality, are what practitioners say gate adoption.** Cloudflare found analysts were far more willing to trust automatic tags when they could see which tags were automatic, and its customers pushed back on AI inventing its own vocabulary. ISAC leaders warn that lower-quality automated output would cost them member trust, and RH-ISAC's security chief also fears damage to chain of custody. A Flashpoint respondent said a confidently wrong agent is worse than a slow one.
- **Not covered here** (routed): adversary use of AI, AI-assisted vulnerability management, SOC alert triage agents and the security of the CTI team's own AI (see section 4).

## 2. Use cases

```yaml
- id: security-threat-intelligence-01
  title: Natural-language questions answered from a curated intelligence corpus, for analysts and for colleagues outside the intelligence team
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Analysts pivot by hand across feeds, portals and query languages, and colleagues outside the security team wait days for answers about the threat landscape."
  solution: "Intelligence platforms put a chat or agent interface on their own corpus. Google Threat Intelligence 'Agentic' retrieves from Google's threat-analysis service, shows its plan, tool calls and cited sources, and offers saved prompt templates and shareable conversation forks (GOOGLE-GTIAGENTIC-2026, sections 1.2, 2.1, 3). Recorded Future AI Sessions answers questions grounded in its Intelligence Graph (RF-AI-2026). Microsoft Security Copilot answers from Microsoft Threat Intelligence content through a plugin (MSFT-MDTICOPILOT-2026). At Cowbell, authorized colleagues outside the intelligence team query the platform directly (RF-COWBELL-2026); at Superhuman, engineers ask Recorded Future AI in natural language (RF-SUPERHUMAN-2026)."
  outcomes:
    - lever: speed
      description: "Cowbell says stakeholder questions about the threat landscape now get an answer in minutes where they used to take two or three days of research by the intelligence team."
      figure: "minutes instead of two to three days"
      measures: "Cowbell customer quote in a vendor-written case study, comparing asking a question of Recorded Future AI Sessions with earlier research by the intelligence team; no sample, baseline period or method given"
      provenance: vendor-published
      source_ref: RF-COWBELL-2026
    - lever: cost
      description: "Cowbell's SVP and GM of Resiliency Services says the company cut threat intelligence costs by over 90% with the Recorded Future platform. The saving is attributed to the platform as a whole, not to the AI features alone."
      figure: "over 90%"
      measures: "Quote from Cowbell's SVP and GM of Resiliency Services ('reduce our threat intelligence costs by over 90%'); cost baseline and scope not stated; platform-wide, not AI-specific"
      provenance: vendor-published
      source_ref: RF-COWBELL-2026
  prerequisites:
    - "A licence tier that includes the AI features: Google Threat Intelligence Agentic needs Enterprise or Enterprise Plus (GOOGLE-GTIAGENTIC-2026, callout 'Special privileges required')."
    - "AI features not switched off for the account or group (GOOGLE-GTIRELEVANCE-2026, note 'AI settings need to be enabled'; GOOGLE-GTIFLOWS-2026, data-privacy callout)."
    - "For Security Copilot, the Microsoft Threat Intelligence plugin turned on (MSFT-MDTICOPILOT-2026, section on turning on the plugin)."
  risks_and_guardrails:
    - "Google's documentation says the generative AI may produce inaccurate information and that responses should be a starting point to double-check (GOOGLE-GTIAGENTIC-2026, callout 'AI is a tool')."
    - "Indicators and files submitted through the web interface are scanned and added to the vendor's shared dataset, so sensitive or personal data should not be submitted (GOOGLE-GTIAGENTIC-2026, opening callouts)."
    - "Recorded Future says outputs are referenced to platform data and the analysis process can be inspected (RF-AI-2026, FAQ answers on 'actionable insights')."
    - "An independent study of LLM failures in CTI attributes them to the threat landscape itself (spurious correlations, contradictory sources, weak generalization to new threats), not only to generic hallucination (ARXIV-2509.23573, abstract)."
  human_checkpoints:
    - "Analyst reads the cited sources and the agent's tool-call trace before relying on an answer (GOOGLE-GTIAGENTIC-2026, section 1.2)."
    - "Superhuman analysts still run in-depth investigations and validate hypotheses themselves (RF-SUPERHUMAN-2026, section on AI-native workflows)."
  role_evolution: "Superhuman says engineers now get threat intelligence directly, which reduces their dependency on the security team (RF-SUPERHUMAN-2026, section on cultural change). Recorded Future's page quotes an anonymous automotive manufacturer saying the AI lets less experienced analysts do more (RF-AI-2026, customer quote); this is marketing copy."
  evidence_grade: A
  sources:
    - { ref: RF-COWBELL-2026, title: "Cowbell Achieves 90% Cost Savings With Recorded Future", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/case-study/cowbell", date: 2026-09-30, access: full, locator: "headline; sections on AI Sessions and on cost and staffing savings" }
    - { ref: RF-SUPERHUMAN-2026, title: "How Superhuman Unlocked a New Era of AI-Driven Threat Intelligence With Recorded Future", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/case-study/superhuman", date: 2026-06-08, access: full, locator: "sections on AI-native workflows and cultural change" }
    - { ref: RF-AI-2026, title: "Streamline Security Workflows with AI", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/platform/ai", date: 2026-10-17, access: full, locator: "feature list; FAQ. Page is undated; date is the day it was read" }
    - { ref: GOOGLE-GTIAGENTIC-2026, title: "Agentic Platform (Google Threat Intelligence documentation)", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/agentic-platform", date: 2026-09-24, access: full, locator: "callouts; sections 1.2, 2.1, 3" }
    - { ref: MSFT-MDTICOPILOT-2026, title: "Use Microsoft Security Copilot for threat intelligence", publisher: Microsoft, type: vendor, url: "https://learn.microsoft.com/en-us/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence", date: 2026-08-02, access: full, locator: "sections on prompts, plugin and promptbooks" }
    - { ref: ARXIV-2509.23573, title: "Uncovering Vulnerabilities of LLM-Assisted Cyber Threat Intelligence", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2509.23573", date: 2025-09-28, access: full, locator: "abstract" }
    - { ref: GOOGLE-GTIFLOWS-2026, title: "Flows (Google Threat Intelligence documentation)", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/flows-guide", date: 2026-07-31, access: full, locator: "callout on AI features being disabled" }
    - { ref: GOOGLE-GTIRELEVANCE-2026, title: "Getting Started with our new Dark Web Intel capabilities, powered by the relevance system", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/dark-web-intel", date: 2026-06-22, access: full, locator: "note 'AI settings need to be enabled'" }
    - { ref: CLOUDFLARE-CLOUDY-2025, title: "Automating threat analysis and response with Cloudy", publisher: Cloudflare, type: vendor, url: "https://blog.cloudflare.com/automating-threat-analysis-and-response-with-cloudy/", date: 2025-08-29, access: full, locator: "sections on the Cloudforce One Threat Events integration" }
    - { ref: CRWD-CHARLOTTE-2026, title: "Charlotte AI: Agentic Analyst for Cybersecurity", publisher: CrowdStrike, type: vendor, url: "https://www.crowdstrike.com/en-us/platform/charlotte-ai/", date: 2026-10-17, access: full, locator: "FAQ: 'Is Charlotte AI a chatbot or an AI agent?'" }
  last_reviewed: 2026-10-17
  notes: "The A grade rests on two quoted figures from one customer in a vendor-written case study; neither has a stated method. Google's blog says an IDC study it commissioned found CTI teams 46% more efficient and customers identifying 139% more threats proactively; the IDC report is gated (landing page read only) and the figures are not specific to AI, so they are not used as outcomes. The same product class appears in Cloudflare's 'Cloudy' assistant for Cloudforce One Threat Events (CLOUDFLARE-CLOUDY-2025, 2025-08-29) and in CrowdStrike's Charlotte AI, which lists threat intelligence analysis among its functions (CRWD-CHARLOTTE-2026)."

- id: security-threat-intelligence-02
  title: Unstructured open-source reports turned into summaries, indicators, techniques and tags, with the source report kept attached
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting]
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Analysts read vendor blogs, advisories and feeds, then retype indicators and context into their tools. Indicators end up separated from the reason they matter, and platforms cannot poll large numbers of feeds."
  solution: "Cloudflare's Threat Signals polls RSS feeds the customer chooses, fetches and cleans each article, and runs an indicator extractor plus summarization, tagging and indicator-contextualization skills. Each indicator is stored as a threat event in the account's private dataset and linked to the report it came from (CLOUDFLARE-THREATSIGNALS-2026, sections on how it works and on lessons). Adobe's CTRI team uses LLMs to extract structured indicators from advisories in many formats and feeds them to automated hunts (ADOBE-CTRI-2026; see use case 03). Anthropic's threat-intelligence engineering posting describes pipelines that ingest RSS, CTI news and partner sharing and use Claude to extract TTPs and generate hunting queries (ANTHROPIC-JOBTIE-2026, responsibilities). OpenCTI offers an Import Document AI connector that turns documents into STIX bundles with a model trained by Filigran, and an on-premises deployment for air-gapped sites (OPENCTI-IMPORTAI-2025)."
  outcomes:
    - lever: quality
      description: "Cloudflare reports that analyst trust depended on three design choices. AI tagging was limited to each account's existing tag catalog. The system recorded whether a tag was automatic or analyst-applied. The link from each event back to its source report was kept."
      figure: "none published"
      measures: "Qualitative statements by Cloudflare's authors from early testing; no counts, error rates or sample"
      provenance: vendor-published
      source_ref: CLOUDFLARE-THREATSIGNALS-2026
    - lever: quality
      description: "Independent test of LLM entity extraction from incident reports: precision stays low across model tiers and the flagship control did not close the gap. Confidence tiering can set review priority but not truth."
      figure: "micro precision 0.03 to 0.34"
      measures: "Micro precision of entity extraction by two low-cost LLMs and one flagship-tier control, scored against gold labels on a public corpus of 354 incident campaigns (315 unique reports, 630 model-report evaluations)"
      provenance: independent
      source_ref: ARXIV-2610.20417
    - lever: quality
      description: "Pilot study of LLM indicator extraction from sandbox reports: precision beat static rules, but the models recovered only a quarter to a third of the labeled indicators."
      figure: "recall 0.25 to 0.31; precision 0.51 to 0.78"
      measures: "Three LLMs recovered 363 to 461 of 1,472 labeled indicators from sandbox reports of 49 malware samples and 5 replayed campaigns; precision and recall as defined by the authors against labels built by two analysts"
      provenance: independent
      source_ref: ARXIV-2609.01174
  prerequisites:
    - "A defined set of trusted source feeds and an existing tag vocabulary (CLOUDFLARE-THREATSIGNALS-2026, 'What we learned')."
    - "A store where indicators keep their provenance, such as Cloudflare's private threat-event dataset or a data-lake schema (CLOUDFLARE-THREATSIGNALS-2026; ADOBE-CTRI-2026, 'Start with a unified data architecture')."
    - "Ingestion connectors per source type, with rate-limit and failure handling (ADOBE-CTRI-2026, 'Build resilient ingestion pipelines')."
  risks_and_guardrails:
    - "Indicators pushed to a blocklist without their context leave people unable to explain later why a domain was blocked (CLOUDFLARE-THREATSIGNALS-2026, introduction)."
    - "Extraction misses most indicators in noisy evidence and can assert techniques the evidence does not support (ARXIV-2609.01174, section 6, Experiments 1 and 2)."
    - "A single misattribution sentence flipped high-confidence judgments in 95.6 to 100% of tested cases (ARXIV-2610.20417, abstract), so confidence scores should not be treated as verification."
    - "Adobe recommends circuit breakers, retries and monitoring dashboards, and running the agentic system alongside existing processes to build trust (ADOBE-CTRI-2026, 'Engineer for production reliability' and closing section)."
  human_checkpoints:
    - "Analysts see which tags were applied automatically and trace each indicator to its report (CLOUDFLARE-THREATSIGNALS-2026, 'What we learned')."
    - "Detections from the Adobe pipeline are compiled into reports for analysts to investigate (ADOBE-CTRI-2026, 'Automated notification')."
  role_evolution: "Anthropic's posting describes a foundational engineering role on a small team that may grow into a multi-person collections function (ANTHROPIC-JOBTIE-2026, 'About the Role'). Cloudflare says Threat Signals began as a one-week internal prototype built by a threat analyst (CLOUDFLARE-THREATSIGNALS-2026, 'What we learned')."
  evidence_grade: B
  sources:
    - { ref: CLOUDFLARE-THREATSIGNALS-2026, title: "Introducing Threat Signals: agentic skills for open-source threat intelligence, free for every Cloudflare account", publisher: Cloudflare, type: vendor, url: "https://blog.cloudflare.com/threat-signals/", date: 2026-09-29, access: full, locator: "how it works; 'What we learned'" }
    - { ref: ADOBE-CTRI-2026, title: "Building an agentic AI-powered threat intelligence platform", publisher: Adobe, type: firm, url: "https://blog.adobe.com/security/building-an-agentic-ai-powered-threat-intelligence-platform", date: 2026-03-19, access: full, locator: "'End-to-end automated workflow' steps 1 and 2; design guidance list" }
    - { ref: ANTHROPIC-JOBTIE-2026, title: "Threat Intelligence Engineer (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5074937008", date: 2026-01-20, access: full, locator: "About the Role; Responsibilities. Posting last updated 2026-08-21" }
    - { ref: OPENCTI-IMPORTAI-2025, title: "On-premise AI extraction (OpenCTI documentation)", publisher: Filigran / OpenCTI, type: vendor, url: "https://docs.opencti.io/latest/deployment/advanced/ai-import-document/", date: 2025-04-11, access: full, locator: "page text on the extraction service and its default hosting" }
    - { ref: ARXIV-2610.20417, title: "From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2610.20417", date: 2026-10-14, access: full, locator: "abstract, findings 1 and 3" }
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "section 6, Experiments 1 and 2, Table 2" }
  last_reviewed: 2026-10-17
  notes: "Grade B: Cloudflare (product, generally available per its post) and Adobe (internal platform) are named deployments with no published outcome figures. The two independent studies measure the technique in lab settings, not either deployment, and show how much is still missed. OpenCTI's page does not publish accuracy."

- id: security-threat-intelligence-03
  title: New indicators matched against enterprise telemetry by an automated hunting pipeline, with prior intelligence rechecked over time
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "When a critical advisory appears, teams spend days reading it, extracting indicators and hunting across several tools to learn whether they are affected, while attackers exploit the gap."
  solution: "Adobe's Cybersecurity Threat Research and Intelligence team built a platform on a lakehouse architecture. It monitors dozens of sources, normalizes them into one schema, uses LLMs to extract structured indicators, enriches them, launches parallel hunting jobs across EDR, email security, cloud and authentication logs, and sends structured reports to analysts. It also revisits earlier intelligence that produced no matches, to catch delayed signals (ADOBE-CTRI-2026, 'End-to-end automated workflow' and 'Implement an automated monitoring and recheck system')."
  outcomes:
    - lever: speed
      description: "Adobe says each hunting job processes thousands of indicators across millions of security events and completes within minutes. No before-and-after comparison is given."
      figure: "scans completed within minutes"
      measures: "Adobe's description of a hunting job ('thousands of IOCs across millions of security events', scans 'within minutes'); no baseline, sample or error rate"
      provenance: self-reported
      source_ref: ADOBE-CTRI-2026
  prerequisites:
    - "A common data schema for indicators, detections, workflows and system state (ADOBE-CTRI-2026, 'Start with a unified data architecture')."
    - "Telemetry from EDR, email security, cloud infrastructure and authentication logs in one queryable store, laid out for fast scans (partition pruning, Z-ordering) (ADOBE-CTRI-2026, 'Design for scale from the start')."
  risks_and_guardrails:
    - "Circuit breakers when external intelligence sources fail, retry strategies, asynchronous job queues and monitoring dashboards for pipeline health (ADOBE-CTRI-2026, 'Engineer for production reliability')."
    - "Run the agentic system beside existing processes so teams can build trust before relying on it (ADOBE-CTRI-2026, closing section)."
    - "Poisoned content in ingested reports is a known attack on LLM-assisted workflows; a FIRST 2026 session showed one crafted artifact steering retrieval and the analyst-facing narrative (FIRST-CON-2026, CyCraft session 'One Poisoned Artifact Can Steer Your AI')."
  human_checkpoints:
    - "Analysts receive compiled detections and investigate (ADOBE-CTRI-2026, 'Automated notification'). The post does not say whether any step needs human approval before a hunt runs."
  role_evolution: "Adobe says the aim is to remove repetitive mechanical work so analysts can focus on investigations and response, not to replace them (ADOBE-CTRI-2026, closing section)."
  evidence_grade: B
  sources:
    - { ref: ADOBE-CTRI-2026, title: "Building an agentic AI-powered threat intelligence platform", publisher: Adobe, type: firm, url: "https://blog.adobe.com/security/building-an-agentic-ai-powered-threat-intelligence-platform", date: 2026-03-19, access: full, locator: "workflow steps 1 to 5; design guidance list; closing section" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program, Denver, 14-19 June 2026", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "CyCraft AI Lab session abstract, 18 June 2026" }
  last_reviewed: 2026-10-17
  notes: "Adobe's blog gives no precision, false-positive or override data and does not say how many hunts ran. Publication date comes from the page's publication-date metadata (03-19-2026)."

- id: security-threat-intelligence-04
  title: Agents turn new campaigns into hunt hypotheses, environment-specific queries and standing detection rules
  archetype: security
  module: threat-intelligence
  function: service-delivery
  work_types: [expert-judgment, research-synthesis, software-systems]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Hypothesis-driven hunting is limited by scarce senior hunters, so teams cannot test for emerging campaigns that have not yet triggered an alert, and leaders wait days for assurance."
  solution: "CyberProof describes four agents run as a managed service for a transport and logistics client: one aggregates and matches campaigns to the client's industry, geography and technology; one turns each relevant campaign into 30 to 40 structured hunting hypotheses; one converts hypotheses into SIEM queries that fit the client's data sources; one turns persistent hunts into standing detection rules (CYBERPROOF-HUNTING-2026, 'Our solution'). Research systems aim at the same step: AHLERT generates environment-aware hunt leads from CTI reports (ARXIV-2609.08790)."
  outcomes:
    - lever: capacity
      description: "CyberProof reports 150 to 200 hunts a month for the client with no matching rise in cost or headcount."
      figure: "10 to 15 times more hunts; 150 to 200 hunts per month"
      measures: "Vendor's description of hunts per month for one unnamed client versus its earlier capacity ('3 to 5 threat hunters were needed'); baseline hunt count not stated"
      provenance: vendor-published
      source_ref: CYBERPROOF-HUNTING-2026
    - lever: risk
      description: "CyberProof says completed hunts converted to detection rules raised active detection coverage."
      figure: "20% increase in active detection coverage"
      measures: "CyberProof's stated increase in the client's continuous-monitoring coverage after relevant hunts became detection rules; denominator and coverage definition not given"
      provenance: vendor-published
      source_ref: CYBERPROOF-HUNTING-2026
    - lever: quality
      description: "Academic test of turning CTI reports into environment-aware hunt leads: grounding in the defender's own assets lifted F1 against a flat retrieval baseline."
      figure: "mean F1 0.44 to 0.85"
      measures: "Mean F1 of hunt-lead extraction on public CTI reports for well-known APTs, hybrid retrieval with ontology grounding versus a single-route flat-RAG baseline, across proprietary and open-weight models (authors at Concordia University and Ericsson Security Research)"
      provenance: independent
      source_ref: ARXIV-2609.08790
  prerequisites:
    - "Open-source and commercial intelligence feeds, plus a description of the client's industry, geography and technology stack (CYBERPROOF-HUNTING-2026, agent 1)."
    - "Access to the client's SIEM data and its naming conventions (CYBERPROOF-HUNTING-2026, agent 3). The client runs a Microsoft security stack."
  risks_and_guardrails:
    - "The client is unnamed and the figures come from the provider's own marketing page; there is no independent check."
    - "An independent benchmark of open-ended agentic hunting on raw logs found five frontier models flagging only 3.8% of malicious events on average (ARXIV-2604.19533, abstract). That task gives the agent no intelligence-derived hypothesis, so it is not a direct test of this design, but it shows that unguided hunting is weak."
    - "Unconstrained LLM agents can invent causal links between log events (ARXIV-2605.29269, abstract)."
  human_checkpoints:
    - "CyberProof says human oversight remains central and senior analysts focus on interpretation and judgment, but the page does not say which steps need approval (CYBERPROOF-HUNTING-2026, 'Our solution')."
  role_evolution: "Query construction, described as a dedicated hunter's job, moves to an agent; senior analysts keep interpretation and judgment (CYBERPROOF-HUNTING-2026, agent 3 and closing paragraph of 'Our solution')."
  evidence_grade: C
  sources:
    - { ref: CYBERPROOF-HUNTING-2026, title: "How agentic AI delivered continuous threat hunting for a transport giant", publisher: CyberProof, type: vendor, url: "https://www.cyberproof.com/case-studies/agentic-ai-transportation/", date: 2026-07, access: full, locator: "Benefits; Our solution; Results. Date is the PDF's creation date (2026-07-16); the web page is undated" }
    - { ref: ARXIV-2609.08790, title: "Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.08790", date: 2026-09-08, access: full, locator: "abstract" }
    - { ref: ARXIV-2604.19533, title: "Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2604.19533", date: 2026-04-21, access: full, locator: "abstract" }
    - { ref: ARXIV-2605.29269, title: "HunterAgent: Neuro-Symbolic Attack Trace Reconstruction under Anti-Forensics", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2605.29269", date: 2026-05-28, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Graded C because the client is not named and every figure is the provider's own. The page describes an early-2026 case in which agents identified MuddyWater-linked campaign signatures on the day and an attempted intrusion was contained at staging; this is the vendor's narrative and is not independently confirmed. Cyber Defense Benchmark: 26 campaigns, 105 of 106 procedures, five frontier models; no model reached 50% recall on every ATT&CK tactic."

- id: security-threat-intelligence-05
  title: Threat reports turned into detection logic (Sigma, YARA, KQL, regex) with validation before deployment
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [software-systems, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Translating a threat report into detection logic is a manual handoff from intelligence analyst to detection engineer that can take days or weeks."
  solution: "Microsoft's Security Copilot ships promptbooks that analyze an external threat article, extract related indicators, summarize it and generate hunting queries to assess impact on the organization (MSFT-MDTICOPILOT-2026, promptbooks list). Anthropic's threat-intelligence engineering posting includes YARA rule infrastructure and using Claude to generate hunting queries from extracted TTPs (ANTHROPIC-JOBTIE-2026, responsibilities). A secondary report says Rapid7's internal security team built an LLM pipeline that extracts behaviors from reports and emits Sigma rules and KQL or SQL queries; Rapid7's own write-up was not found (SECURITYARSENAL-RAPID7-2026). Research tests the step: CTI-REALM, AutoSigma and IOCRegex-gen."
  outcomes:
    - lever: quality
      description: "Microsoft Security AI's benchmark of agents writing detection rules from CTI reports: the top model reached a mean reward of 0.637 among 16 frontier models, and CTI-specific tools improved agent performance."
      figure: "best overall reward 0.637 of 16 models"
      measures: "Overall reward combining final detection results and trajectory-based rewards on emulated attacks across Linux, cloud and Azure Kubernetes Service, 16 frontier models; the abstract does not give the number of tasks"
      provenance: vendor-published
      source_ref: ARXIV-2603.13517
    - lever: quality
      description: "Academic system converting IOCs from CTI reports into regexes reports a high hit rate and low false-positive rate against ground-truth strings."
      figure: "hit rate 99.1%; false-positive rate 0.8%"
      measures: "Average hit rate and false-positive rate on over 3,000 real CTI reports and 2,400 ground-truth strings from the MITRE ATT&CK Evaluations, for the authors' IOCRegex-gen system"
      provenance: independent
      source_ref: ARXIV-2604.12228
  prerequisites:
    - "A detection language the SIEM or EDR accepts, ideally a standard such as Sigma (SECURITYARSENAL-RAPID7-2026, recommendations)."
    - "Non-production data or purple-team scenarios to test generated rules (SECURITYARSENAL-RAPID7-2026, 'Validate AI-Generated Logic')."
  risks_and_guardrails:
    - "Generated rules need peer review and testing before deployment to avoid alert fatigue (SECURITYARSENAL-RAPID7-2026, 'Validate AI-Generated Logic'; secondary source)."
    - "LLMs often cannot reliably verify technical details such as IoCs and TTPs without external ground truth (ARXIV-2603.09452, section 4.4 and section 5.1)."
  human_checkpoints:
    - "Detection engineer or analyst reviews and approves rules before deployment (SECURITYARSENAL-RAPID7-2026, recommendations)."
  role_evolution: "The intelligence-to-detection handoff shifts from rewriting reports as rules to reviewing generated rules (SECURITYARSENAL-RAPID7-2026, 'Translation Layer'; secondary source)."
  evidence_grade: C
  sources:
    - { ref: MSFT-MDTICOPILOT-2026, title: "Use Microsoft Security Copilot for threat intelligence", publisher: Microsoft, type: vendor, url: "https://learn.microsoft.com/en-us/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence", date: 2026-08-02, access: full, locator: "promptbooks: 'Check impact of an external threat article' and 'Threat Intelligence 360 report'" }
    - { ref: ANTHROPIC-JOBTIE-2026, title: "Threat Intelligence Engineer (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5074937008", date: 2026-01-20, access: full, locator: "Responsibilities bullets on YARA infrastructure and on using Claude to extract TTPs" }
    - { ref: SECURITYARSENAL-RAPID7-2026, title: "AI-Driven Detection Engineering: Converting Threat Intel into Executable Hunt Plans", publisher: Security Arsenal, type: press, url: "https://securityarsenal.com/blog/ai-driven-detection-engineering-converting-threat-intel-into-executable-hunt-plans", date: 2026-06-10, access: full, locator: "paragraphs on Rapid7's pipeline and the recommendations list" }
    - { ref: ARXIV-2603.13517, title: "CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2603.13517", date: 2026-03-13, access: full, locator: "abstract; authors listed as Microsoft Security AI" }
    - { ref: ARXIV-2604.12228, title: "From IOCs to Regex: Automating CTI Operationalization for SOC with LLMs", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2604.12228", date: 2026-04-14, access: full, locator: "abstract" }
    - { ref: ARXIV-2603.09452, title: "CyberThreat-Eval: Can Large Language Models Automate Real-World Threat Research?", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2603.09452", date: 2026-03-10, access: full, locator: "section 4.4; section 5.1" }
    - { ref: ARXIV-2608.19011, title: "From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2608.19011", date: 2026-08-19, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Maturity is 'announced' because the product features and the Rapid7 report (a third-party summary; Rapid7's own post not found) are not backed by a customer outcome. Rapid7 is described by the secondary source as led by Senior Threat Hunter Blake McDermott; treat as unverified. AutoSigma (ARXIV-2608.19011, 2026-08-19) also reports better rule validity and ATT&CK coverage than alternatives but gives no figures in its abstract."

- id: security-threat-intelligence-06
  title: Global intelligence filtered and ranked against an organization profile so only relevant alerts and actors surface
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, transaction-processing]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Analysts face a high volume of dark-web, vulnerability and actor alerts; most do not concern their organization, and manual prioritization is described as untenable."
  solution: "Google Threat Intelligence's Relevance System (Beta) builds an organization profile from a name and primary domain, discovering the core business, brands and industry, then scores global intelligence and dark-web findings against that profile and groups findings into alerts under threat scenarios (GOOGLE-GTIORGPROFILE-2026; GOOGLE-GTIRELEVANCE-2026). Its AI-infused Threat Profiles use embeddings and customer feedback to recommend actors, malware and campaigns by industry and region (GOOGLE-GTILANDSCAPE-2026). Microsoft's Threat Intelligence Briefing Agent ranks threats using the customer's own exposure data (MSFT-TIBAGENT-2026). Flashpoint's interview study finds alert noise and false positives the most-cited program problem (FLASHPOINT-ENTERPRISETI-2026)."
  outcomes:
    - lever: quality
      description: "Mandiant (2023) reported that its scoring models cut noise: false positives fell in alert generation and high-confidence filtering shrank the indicator set."
      figure: "96% reduction in false positives during alert generation; 97% IOC reduction when filtering on high-confidence indicators"
      measures: "Mandiant's wording: '96% reduction in false positives during alert generation' and '97% IOC reduction when filtering on high confidence indicators'; baseline, sample and period not given; refers to scoring models for IOCs and Digital Threat Monitoring alerts, published 2023-08-24, outside the 12 to 18 month window"
      provenance: vendor-published
      source_ref: MANDIANT-AIPHASES-2023
    - lever: capacity
      description: "Google's blog says customers report identifying more threats proactively and making CTI teams more efficient, a result it ties partly to AI summarization and context."
      figure: "139% more threats identified proactively; 46% more efficient CTI teams"
      measures: "Google blog sentence 'Our customers report identifying 139% more threats proactively and make their CTI teams 46% more efficient'; the supporting IDC study was commissioned by Google and is gated; the base and method are not given and the figures are not specific to AI"
      provenance: vendor-published
      source_ref: GOOGLE-FORRESTERBLOG-2026
  prerequisites:
    - "An administrator who sets up the organization profile and thresholds; analysts then triage alerts and give feedback (GOOGLE-GTIRELEVANCE-2026, access roles)."
    - "AI settings left enabled for the account (GOOGLE-GTIRELEVANCE-2026, note on AI settings)."
    - "For the Microsoft agent, Defender for Endpoint and Defender External Attack Surface Management signals (MSFT-TIBAGENT-2026, introduction)."
  risks_and_guardrails:
    - "Google says the Relevance System is in Beta and customers should keep Digital Threat Monitoring and Attack Surface Management running in parallel (GOOGLE-GTIRELEVANCE-2026, Beta note)."
    - "The system is tuned to produce few alerts, sometimes zero a day, so a quiet dashboard may hide gaps; Google points users to dark-web search and other tools as a check (GOOGLE-GTIORGPROFILE-2026, note on few alerts)."
    - "Organization-profile edits are cited to the user and versioned, which gives an audit trail (GOOGLE-GTIORGPROFILE-2026, 'Citations and Versioning')."
  human_checkpoints:
    - "Analysts change alert status and give feedback that shapes recommendations (GOOGLE-GTIRELEVANCE-2026, access roles; GOOGLE-GTILANDSCAPE-2026, paragraph on embeddings ('Feedback is incorporated directly'))."
  role_evolution: "Google says threat actors used to be the main entry point and that manual prioritization is not tenable; the profile model recommends actors, malware and campaigns instead, and analysts give feedback that shapes the recommendations (GOOGLE-GTILANDSCAPE-2026, opening and embeddings paragraphs)."
  evidence_grade: C
  sources:
    - { ref: GOOGLE-GTIRELEVANCE-2026, title: "Getting Started with our new Dark Web Intel capabilities, powered by the relevance system", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/dark-web-intel", date: 2026-06-22, access: full, locator: "introduction; Beta and AI-settings notes; access roles" }
    - { ref: GOOGLE-GTIORGPROFILE-2026, title: "Organization Profile (Google Threat Intelligence documentation)", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/my-landscape-organization-profile", date: 2026-06-16, access: full, locator: "Automated Setup; note on alert volume; Citations and Versioning" }
    - { ref: GOOGLE-GTILANDSCAPE-2026, title: "How Your Threat Landscape Uses AI Recommendations", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/threat-landscape-ai-recommendations", date: 2026-02-27, access: full, locator: "whole page" }
    - { ref: MSFT-TIBAGENT-2026, title: "Security Copilot Threat Intelligence Briefing Agent in Microsoft Defender", publisher: Microsoft, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/threat-intel-briefing-agent-defender", date: 2026-07-02, access: full, locator: "introduction" }
    - { ref: FLASHPOINT-ENTERPRISETI-2026, title: "The Enterprise Threat Intelligence Report: 2026", publisher: Flashpoint, type: survey, url: "https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/", date: 2026-10-13, access: full, locator: "key findings; challenges section" }
    - { ref: MANDIANT-AIPHASES-2023, title: "AI and the Five Phases of the Threat Intelligence Lifecycle", publisher: Mandiant (Google Cloud Blog), type: vendor, url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-five-phases-intelligence-lifecycle", date: 2023-08-24, access: full, locator: "section on analysis and prioritization" }
    - { ref: GOOGLE-FORRESTERBLOG-2026, title: "Google named a Leader in the External Threat Intelligence Service Forrester Wave", publisher: Google, type: vendor, url: "https://cloud.google.com/blog/products/identity-security/google-named-a-leader-in-the-external-threat-intelligence-service-forrester-wave", date: 2026-09-18, access: full, locator: "paragraph beginning 'Google Threat Intelligence delivers a measurable impact'" }
  last_reviewed: 2026-10-17
  notes: "Maturity 'piloting' because the Relevance System is labelled Beta; the AI-recommended Threat Profiles feature is documented without a launch date. Vendor claims only; no customer is named and no override rate is published."

- id: security-threat-intelligence-07
  title: Scheduled or on-demand AI drafting of threat briefings, reports and tailored summaries for different audiences
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Building a briefing means pulling data from several feeds, tools and portals, filtering it, mapping it to the organization, and only then writing. Microsoft says this can take hours or days, by which time the threat may have changed."
  solution: "Microsoft's Threat Intelligence Briefing Agent runs on a schedule or on demand, chooses each next step from the result of the previous one, and produces a report combining threat-actor activity with the customer's internal and external vulnerability information (MSFT-TIBAGENT-2026, introduction). Google Threat Intelligence 'Flows' schedule a natural-language prompt, such as a daily executive digest for a sector, and can email the result (GOOGLE-GTIFLOWS-2026; GOOGLE-GTICHANGELOG-2026). Recorded Future AI creates template-based or custom reports referenced to platform data (RF-AI-2026). At Cowbell the platform supplies reports and short summaries for decision-makers (RF-COWBELL-2026). A US public-sector agency uses AI to create weekly reports (RF-PUBSECTOR-2026). CISA is building a RAG-based generative tool to draft summaries of approved products for different publication channels, with staff reviewing and editing drafts (DHS-AIINV-CISA-2026, DHS-2335)."
  outcomes:
    - lever: speed
      description: "Microsoft says the briefing agent produces a customized report in minutes where manual briefing building can take hours or days."
      figure: "minutes versus hours or days"
      measures: "Microsoft documentation statements ('in a matter of minutes'; manual steps 'can take hours or even days'); a design claim in product documentation, not a measurement, and no sample or method given"
      provenance: vendor-published
      source_ref: MSFT-TIBAGENT-2026
    - lever: capacity
      description: "A Recorded Future public-sector customer says using AI to generate weekly reports has saved time on manual compilation."
      figure: "none published"
      measures: "Customer statement ('Having that function where we can utilize AI to create those reports on a weekly basis has been awesome'); no time saved is stated; customer is anonymous"
      provenance: vendor-published
      source_ref: RF-PUBSECTOR-2026
  prerequisites:
    - "For Microsoft's agent: Defender for Endpoint and Defender External Attack Surface Management turned on, the Microsoft Threat Intelligence plugin, and an agent identity or user account with read access to vulnerability and hunting data (MSFT-TIBAGENT-2026, prerequisites and agent-identity sections)."
    - "For Google Flows: an Enterprise or Enterprise Plus licence; the feature is in public preview and unavailable if AI features are disabled (GOOGLE-GTIFLOWS-2026, callouts)."
  risks_and_guardrails:
    - "Microsoft recommends a dedicated agent identity with minimal read permissions, a dedicated service account for separation of duties (MSFT-TIBAGENT-2026, agent identity section)."
    - "Without the right device-group permissions the exposure report can show 'not available' or zero CVEs even when vulnerabilities exist (MSFT-DEFENDERAGENTS-2026, section on configuring Defender for Endpoint permissions)."
    - "CISA staff validate accuracy of drafts under required AI training and use them under applicable law and policy (DHS-AIINV-CISA-2026, DHS-2335 summary)."
  human_checkpoints:
    - "Drafts are reviewed, edited and coordinated by authorized CISA personnel before publication (DHS-AIINV-CISA-2026, DHS-2335 summary)."
    - "Google Flows keeps each run's input and output and links to the full agent session for inspection (GOOGLE-GTIFLOWS-2026, 'Monitoring executions')."
  role_evolution: "Superhuman's security engineers say translating technical intelligence for leadership helps justify investments (RF-SUPERHUMAN-2026, final sections). CISA says contractors currently review pre-production content to build summaries, and that an internal chat tool saves staff time (DHS-AIINV-CISA-2026, DHS-2306 summary)."
  evidence_grade: B
  sources:
    - { ref: MSFT-TIBAGENT-2026, title: "Security Copilot Threat Intelligence Briefing Agent in Microsoft Defender", publisher: Microsoft, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/threat-intel-briefing-agent-defender", date: 2026-07-02, access: full, locator: "introduction; prerequisites; agent identity section" }
    - { ref: MSFT-DEFENDERAGENTS-2026, title: "Deploy AI agents in Microsoft Defender", publisher: Microsoft, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender", date: 2026-08-05, access: full, locator: "section on the Threat Intelligence Briefing Agent" }
    - { ref: GOOGLE-GTIFLOWS-2026, title: "Flows (Google Threat Intelligence documentation)", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/flows-guide", date: 2026-07-31, access: full, locator: "What is a Flow; supported layouts; Monitoring executions" }
    - { ref: GOOGLE-GTICHANGELOG-2026, title: "August 12th, 2026 - Agentic Flows & API, and Threat Actor Naming Updates", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/changelog/august-5th-2026-agentic-flows-api-and-threat-actor-naming-updates", date: 2026-08-12, access: full, locator: "Public Preview: Google TI Flows; example use cases" }
    - { ref: RF-AI-2026, title: "Streamline Security Workflows with AI", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/platform/ai", date: 2026-10-17, access: full, locator: "AI Report Creation paragraph. Page is undated; date is the day it was read" }
    - { ref: RF-COWBELL-2026, title: "Cowbell Achieves 90% Cost Savings With Recorded Future", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/case-study/cowbell", date: 2026-09-30, access: full, locator: "paragraph on reports and short summaries" }
    - { ref: RF-PUBSECTOR-2026, title: "Public Sector Agency Collects Intelligence 95% Faster Using Recorded Future", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/case-study/public-sector-agency", date: 2026-09-29, access: full, locator: "section 'Streamlining Security Workflows With Integrations'" }
    - { ref: RF-SUPERHUMAN-2026, title: "How Superhuman Unlocked a New Era of AI-Driven Threat Intelligence With Recorded Future", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/case-study/superhuman", date: 2026-06-08, access: full, locator: "paragraphs on leadership communication" }
    - { ref: DHS-AIINV-CISA-2026, title: "Cybersecurity and Infrastructure Security Agency - AI Use Cases (DHS AI Use Case Inventory)", publisher: US Department of Homeland Security, type: regulator, url: "https://www.dhs.gov/ai/use-case-inventory/cisa", date: 2026-01-28, access: full, locator: "DHS-2335 (pre-deployment) and DHS-2306 (deployed). The page text renders 'AI' as 'SI' after a 2026-09-29 executive order; date is the annual refresh" }
  last_reviewed: 2026-10-17
  notes: "Grade B: Cowbell, Superhuman and CISA are named, but none publishes a measured time saving. CISA's drafting tool is listed as pre-deployment; CISAChat (internal search and summaries of agency materials) is listed as deployed. The Recorded Future public-sector customer is anonymous."

- id: security-threat-intelligence-08
  title: Malware-analysis agent that triages samples, explains behavior and extracts indicators for analysts
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [expert-judgment, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Malware samples submitted by partners need manual reverse engineering to find indicators of compromise and adversary command-and-control, which slows the production of shareable intelligence."
  solution: "Google Threat Intelligence Agentic includes a Malware Analyst agent that triages files by hash or upload, runs private-scan analysis, reverse engineers binaries and scripts, deobfuscates PowerShell, VBA, HTA and JavaScript, and explains behavior in natural language with reasoning shown (GOOGLE-GTIAGENTIC-2026, section 3.1). A 2026-09-10 release added MSI and MSIX installer parsing (GOOGLE-GTICHANGELOG2-2026). CISA lists a malware reverse-engineering use case in pre-deployment: deep learning that assists analysts with triage and indicator extraction and produces a report that human analysts use, with recommendations shown through reverse-engineering tool plugins (DHS-AIINV-CISA-2026, DHS-107)."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No measurement found for either the Google agent or CISA's pre-deployment tool"
      provenance: vendor-published
      source_ref: GOOGLE-GTIAGENTIC-2026
  prerequisites:
    - "Google Threat Intelligence Enterprise or Enterprise Plus licence; uploading files for analysis uses the customer's Private Scanning quota (GOOGLE-GTIAGENTIC-2026, callouts)."
  risks_and_guardrails:
    - "Files and indicators submitted may be added to Google's shared dataset unless handled as private samples; sensitive or personal data should not be submitted (GOOGLE-GTIAGENTIC-2026, callouts)."
    - "Google says the AI may be inaccurate and shows the agent's reasoning and tool calls so users can spot hallucinations (GOOGLE-GTIAGENTIC-2026, section 1.2)."
  human_checkpoints:
    - "CISA's report is used by human analysts to facilitate triage (DHS-AIINV-CISA-2026, DHS-107 summary)."
  role_evolution: "Not described in the sources beyond analysts consuming the agent's reports."
  evidence_grade: C
  sources:
    - { ref: GOOGLE-GTIAGENTIC-2026, title: "Agentic Platform (Google Threat Intelligence documentation)", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/agentic-platform", date: 2026-09-24, access: full, locator: "section 3.1 Malware Analyst Agent; callouts" }
    - { ref: GOOGLE-GTICHANGELOG2-2026, title: "September 10th, 2026 - Single Target Operations (GA), Google Insights, Agentic Updates, and Detection Highlights", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/changelog/september-10th-2026-single-target-operations-ga-google-insights-agentic-updates-and-detection-highlights", date: 2026-09-10, access: full, locator: "Google TI Agentic Updates" }
    - { ref: DHS-AIINV-CISA-2026, title: "Cybersecurity and Infrastructure Security Agency - AI Use Cases (DHS AI Use Case Inventory)", publisher: US Department of Homeland Security, type: regulator, url: "https://www.dhs.gov/ai/use-case-inventory/cisa", date: 2026-01-28, access: full, locator: "Pre-Deployment: Malware Reverse Engineering (DHS-107), classified as classical or predictive machine learning" }
  last_reviewed: 2026-10-17
  notes: "CISA's tool is classified in the inventory as classical or predictive machine learning, not generative AI. Google's changelog lists new capabilities from May to October 2026 for the Malware Analyst, which shows active development but no customer evidence."

- id: security-threat-intelligence-09
  title: Underground, dark-web and infostealer-log collection triaged by NLP and LLM pipelines
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Forum posts, messaging channels and millions of stealer logs are too many and too varied (languages, formats, screenshots) for analysts to read, so valuable signals go unexamined."
  solution: "Mandiant described dozens of AI models over botnet, forum and messaging data, with an NLP pipeline for entity extraction, topic classification and translation (MANDIANT-AIPHASES-2023, 'Structure and Enrichment'). Google's Relevance System filters dark-web findings against an organization profile (GOOGLE-GTIRELEVANCE-2026). At FIRST 2026, Flare presented StealerLens, an LLM-powered tool for infostealer log investigations, citing more than 50 million stealer logs posted in 2025 (FIRST-CON-2026, 17 June). Apura Cyber Intelligence presented an OSINT copilot using open tooling, RAG and agentic LLM workflows for extraction, enrichment and investigative search (FIRST-CON-2026, 19 June)."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "The FIRST abstracts give no results; Mandiant's 2023 post gives no collection-stage figure"
      provenance: vendor-published
      source_ref: FIRST-CON-2026
  prerequisites:
    - "A collection source with legal access to the underground data, and an indexing store for RAG (FIRST-CON-2026, Apura abstract)."
  risks_and_guardrails:
    - "Google tells customers to keep Digital Threat Monitoring and Attack Surface Management running in parallel while the relevance system is in Beta (GOOGLE-GTIRELEVANCE-2026, Beta note)."
    - "The Apura abstract stresses 'evidence-based' and 'reproducible' analysis, which implies that the source posts stay attached to the output (FIRST-CON-2026, Apura abstract title and text). This is an inference from wording."
  human_checkpoints:
    - "Not stated in the abstracts."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program, Denver, 14-19 June 2026", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "Flare StealerLens abstract (17 June); Apura OSINT Copilot abstract (19 June)" }
    - { ref: MANDIANT-AIPHASES-2023, title: "AI and the Five Phases of the Threat Intelligence Lifecycle", publisher: Mandiant (Google Cloud Blog), type: vendor, url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-five-phases-intelligence-lifecycle", date: 2023-08-24, access: full, locator: "'Structure and Enrichment' section" }
    - { ref: GOOGLE-GTIRELEVANCE-2026, title: "Getting Started with our new Dark Web Intel capabilities, powered by the relevance system", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/docs/dark-web-intel", date: 2026-06-22, access: full, locator: "introduction and Beta note" }
  last_reviewed: 2026-10-17
  notes: "Conference abstracts only; slides and recordings were not read. The Mandiant source is from 2023 and is a foundation source. Flashpoint, Intel 471 and Silobreaker offer related products but no usable documentation of AI use was read."

- id: security-threat-intelligence-10
  title: Indicator sharing with automated PII screening and confidence scoring before analysts approve what is published
  archetype: security
  module: threat-intelligence
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Indicators submitted to a sharing service can include names, addresses or other personal data in free-text notes, and receivers need to know how reliable each indicator is. Practitioners surveyed rank exposure of sensitive information as the main difficulty in sharing CTI."
  solution: "CISA's Automated Indicator Sharing service uses natural-language processing to flag potential PII in submissions; flagged submissions go to CISA analysts, who are guided by the tool to confirm or reject and redact; privacy experts monitor the system, give feedback, and audits run regularly (DHS-AIINV-CISA-2026, DHS-4). A decision-tree confidence score that told partners and analysts how reliable and complete a submission was is listed as retired and consolidated into the PII use case (DHS-AIINV-CISA-2026, DHS-5)."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "The inventory gives no detection rate, false-positive rate or review volume"
      provenance: self-reported
      source_ref: DHS-AIINV-CISA-2026
    - lever: quality
      description: "Research pilot of LLM redaction of incident reports with injected personal identifiers: under a privacy-first prompt the three models missed at most 3 of 92 injected values and two removed all ten descriptive phrases, but one also removed many values that identified no one; a utility-first prompt reversed the errors."
      figure: "at most 3 of 92 injected values missed (privacy-first prompt); GPT-5.5 removed 50 values that were never identifiers, 35% of everything it removed"
      measures: "Injected PII and organization-identifying values missed or over-removed by three LLMs on 4 held-out incident reports (92 injected values and 10 descriptive phrases), per prompt, in the SoK authors' pilot (Table 3 and surrounding text); lab pilot, not a deployment"
      provenance: independent
      source_ref: ARXIV-2609.01174
  prerequisites:
    - "A review queue staffed by trained analysts and a privacy function that monitors the tool and feeds corrections back (DHS-AIINV-CISA-2026, DHS-4)."
  risks_and_guardrails:
    - "Over-redaction can strip the attacker's identifiers along with the victim's, because both appear in the same form; a rule that removes every machine name damages the report (ARXIV-2609.01174, section 6, Experiment 3)."
    - "Practitioners: 12 of 18 worried AI could break privacy or regulatory compliance when sharing, and 13 of 18 named data privacy as a hurdle to using AI (ARXIV-2609.01174, section 3.2)."
    - "SANS reports 55% of organizations lack legally reviewed CTI sharing processes (SANS-CTI-2026)."
  human_checkpoints:
    - "CISA analysts confirm or reject each flagged detection and redact (DHS-AIINV-CISA-2026, DHS-4)."
  role_evolution: "Privacy experts become reviewers of the tool's output and a source of feedback (DHS-AIINV-CISA-2026, DHS-4)."
  evidence_grade: B
  sources:
    - { ref: DHS-AIINV-CISA-2026, title: "Cybersecurity and Infrastructure Security Agency - AI Use Cases (DHS AI Use Case Inventory)", publisher: US Department of Homeland Security, type: regulator, url: "https://www.dhs.gov/ai/use-case-inventory/cisa", date: 2026-01-28, access: full, locator: "Deployment: DHS-4; Inactive: DHS-5" }
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "section 3.2; section 6, Experiment 3 and Table 3 (4 held-out reports)" }
    - { ref: SANS-CTI-2026, title: "91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (2026 SANS CTI Survey press release)", publisher: SANS Institute, type: survey, url: "https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report", date: 2026-05-19, access: full, locator: "paragraph on sharing processes" }
  last_reviewed: 2026-10-17
  notes: "The inventory classifies DHS-4 as natural-language processing, not generative AI, and DHS-5 as a decision-tree process. This is adjacent evidence for AI in sharing; the LLM redaction result is a lab pilot, so the grade is capped at B. The mirror text of the DHS page uses 'SI' in place of 'AI'."

- id: security-threat-intelligence-11
  title: Analyst findings converted into shareable, redacted STIX/TAXII or MISP packages by an assistant
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [document-production, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Indicators often circulate in ad-hoc emails and chat threads, bypassing STIX/TAXII pipelines. Analysts struggle to redact sensitive details, map behavior to techniques, and produce the formats each sharing feed requires."
  solution: "Idea discussed by researchers and practitioners: use LLMs for the four steps of generating shareable CTI (extraction, normalization and enrichment, codification and redaction, distribution). In a pilot, models produced STIX files that preserved supplied findings, but each step still needed expert review (ARXIV-2609.01174, abstract and section 6). CISA described IMX, a guided tool for publishing STIX 2.x packages in minutes without schema expertise; the FIRST abstract does not say IMX uses AI (FIRST-CON-2026, 15 June)."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No deployment found; lab results are in the notes"
      provenance: independent
      source_ref: ARXIV-2609.01174
  prerequisites:
    - "Clear information-exchange policy for what may be shared and redistributed; FIRST's Information Exchange Policy SIG says the lack of such policy is an increasing impediment to timely exchange (FIRST-CON-2026, SIG description, 16 June)."
  risks_and_guardrails:
    - "Practitioners in the survey doubt reliability: 14 of 18 lacked confidence AI would do sharing tasks correctly and 13 of 18 expected it to introduce inaccuracies into shared data (ARXIV-2609.01174, section 3.2)."
    - "Models recover only a fraction of the labeled indicators and struggle to ground claims in the supplied evidence (ARXIV-2609.01174, abstract)."
  human_checkpoints:
    - "Expert review at each of the four steps (ARXIV-2609.01174, abstract)."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "abstract; section 3.2 (11 of 18 saw AI support for format translation); section 6" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program, Denver, 14-19 June 2026", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "IMX abstract (15 June); Information Exchange Policy SIG (16 June)" }
    - { ref: CISAGOV-IMX-2026, title: "cisagov/imx README", publisher: CISA, type: regulator, url: "https://raw.githubusercontent.com/cisagov/imx/develop/README.md", date: 2026-10-17, access: full, locator: "whole file. File is undated; date is the day it was read" }
  last_reviewed: 2026-10-17
  notes: "Idea (grade D). The FIRST abstract calls IMX 'newly open-sourced', but the repository README read on 2026-10-17 says 'Code coming soon'. Pilot detail from the SoK: recall of 0.25 to 0.31 on indicators and mixed redaction results; every model produced STIX files that parse and carry all supplied techniques and indicators, but they asserted more links between objects than the findings support (for example 73 asserted links with 38 correct for one model; Table 4 and text), so a recipient cannot trust an individual link without checking. Only 3 of 18 surveyed practitioners used LLMs to turn attack data into CTI."

- id: security-threat-intelligence-12
  title: Natural-language threat hunting assistants that write queries, interpret results and guide a hunt
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [expert-judgment, research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Hunting depends on query-language expertise (such as KQL) and on remembering context across a long session, which limits who can hunt and how fast."
  solution: "Microsoft's Threat Hunting Assistant in Defender advanced hunting takes natural-language questions, reads table schemas before writing a query, runs it, adjusts if results do not answer the question, adds observations and charts, and suggests follow-ups and actions; it supports reviewing the impact of an attack described in a threat intelligence report (MSFT-HUNTASSIST-2026). Job postings show employers expecting this way of working: Huntress asks hunters to use AI-assisted workflows to prototype queries and scaffold detections while verifying output (HUNTRESS-JOBDETH-2026); Twilio asks for experience building AI agents and using AI for complex hunting (TWILIO-JOBSSETH-2026)."
  outcomes:
    - lever: quality
      description: "Independent benchmark of unaided agentic hunting on raw Windows logs: the best of five frontier models submitted correct flags for a small share of malicious events and none reached the authors' bar for unsupervised use."
      figure: "3.8% of malicious events flagged by the best model"
      measures: "Average share of malicious event timestamps correctly flagged across 26 campaigns covering 105 of 106 attack procedures, five frontier models, no hints; passing bar defined by the authors as at least 50% recall on every ATT&CK tactic. Adjacent evidence: autonomous hunting, not the assistant mode"
      provenance: independent
      source_ref: ARXIV-2604.19533
  prerequisites:
    - "Access to Security Copilot in advanced hunting and the data tables to be queried (MSFT-HUNTASSIST-2026, steps to start)."
  risks_and_guardrails:
    - "Queries are grounded in the tables actually available to the user and the logic behind each query can be inspected (MSFT-HUNTASSIST-2026, 'Schema-aware data discovery' and response components)."
    - "Huntress expects hunters to validate AI output before it reaches production environments (HUNTRESS-JOBDETH-2026, requirements)."
  human_checkpoints:
    - "The hunter reviews generated KQL and results, and a suggested action opens a wizard the user completes before anything is applied (MSFT-HUNTASSIST-2026, response components)."
  role_evolution: "Employers ask hunters to orchestrate reusable AI workflows and verify their output (HUNTRESS-JOBDETH-2026) and to build agentic workflows (TWILIO-JOBSSETH-2026)."
  evidence_grade: C
  sources:
    - { ref: MSFT-HUNTASSIST-2026, title: "Microsoft Security Copilot Threat Hunting Assistant in advanced hunting", publisher: Microsoft, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-threat-hunting-assistant", date: 2026-09-10, access: full, locator: "key capabilities; response components" }
    - { ref: HUNTRESS-JOBDETH-2026, title: "Senior Detection Engineering & Threat Hunting Analyst (job posting)", publisher: Huntress, type: job-posting, url: "https://job-boards.greenhouse.io/huntress/jobs/7998321003", date: 2026-09-23, access: full, locator: "responsibilities and requirements bullets on AI-assisted workflows. Posting last updated 2026-10-09" }
    - { ref: TWILIO-JOBSSETH-2026, title: "Staff Security Engineer, Threat Hunting (job posting)", publisher: Twilio, type: job-posting, url: "https://job-boards.greenhouse.io/twilio/jobs/8157344", date: 2026-09-04, access: full, locator: "requirements bullets on AI agents and AI-assisted hunting. Posting last updated 2026-10-14" }
    - { ref: ARXIV-2604.19533, title: "Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2604.19533", date: 2026-04-21, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Graded C: the evidence is product documentation and employer postings, which describe expected practice and not measured use. No named deployment of the Microsoft assistant with results was found."

- id: security-threat-intelligence-13
  title: Always-on investigation agent that finds missed malicious activity and writes explainable detections using threat intelligence
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [expert-judgment, research-synthesis]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Defenders must keep translating new attacker tradecraft into detection logic, which leaves them reactive; attack stories with gaps go unflagged."
  solution: "Microsoft's Dynamic Threat Detection Agent runs continuously across Defender, builds a unified timeline of alerts, events, behavior analytics and threat intelligence, runs a planner-executor loop that generates attack-specific hypotheses and gathers supporting and refuting evidence, and issues a dynamic alert with a title, severity, MITRE mappings, remediation guidance, implicated entities and a natural-language description (ARXIV-2605.20896, abstract; MSFT-DEFENDERAGENTS-2026, section on the agent)."
  outcomes:
    - lever: quality
      description: "Microsoft's authors report that customers rated the agent's alerts as correct four times in five over a 120-day online evaluation."
      figure: "80.1% precision"
      measures: "Precision from customer feedback on the agent's alerts over a 120-day online evaluation across Defender customers; the number of alerts and feedback rate are not in the abstract"
      provenance: vendor-published
      source_ref: ARXIV-2605.20896
    - lever: growth
      description: "The agent produced novel alerts for a share of investigated incidents."
      figure: "approximately 15% of investigated incidents"
      measures: "Share of investigated incidents for which the agent generated novel alerts, as stated in the abstract; base population not given"
      provenance: vendor-published
      source_ref: ARXIV-2605.20896
    - lever: cost
      description: "Authors report cost and reliability of single-incident investigations."
      figure: "median 28 minutes; median token cost USD 2.04; 0.38% job-level failure rate"
      measures: "Median end-to-end time and median token cost per single-incident investigation, and the share of jobs that failed, as reported in the abstract"
      provenance: vendor-published
      source_ref: ARXIV-2605.20896
    - lever: quality
      description: "Offline evaluation of recovering hidden malicious activity with a newer model versus an older one and a baseline."
      figure: "F1 0.78 with GPT-5.4; +0.12 over GPT-4.1; +0.26 over baseline"
      measures: "F1 for recovering hidden malicious activity in the authors' offline evaluation set; dataset size not in the abstract"
      provenance: vendor-published
      source_ref: ARXIV-2605.20896
  prerequisites:
    - "A unified activity timeline spanning alerts, events, user and entity behavior analytics and threat intelligence (ARXIV-2605.20896, abstract)."
    - "Versioned prompt contracts with schema validation, grounding requirements, bounded retries and fail-closed suppression (ARXIV-2605.20896, abstract)."
  risks_and_guardrails:
    - "Fail-closed suppression and bounded retries limit bad outputs reaching customers (ARXIV-2605.20896, abstract)."
    - "At 80.1% precision about one alert in five was not rated correct (ARXIV-2605.20896, abstract), so triage of the agent's own alerts remains work."
  human_checkpoints:
    - "Customer feedback on each alert is the evaluation signal (ARXIV-2605.20896, abstract). Whether a person reviews before an alert is raised is not stated."
  role_evolution: "Microsoft describes the agent as uncovering false negatives and filling gaps for analysts, not as replacing them (MSFT-DEFENDERAGENTS-2026, agent description)."
  evidence_grade: A
  sources:
    - { ref: ARXIV-2605.20896, title: "GenAI-Driven Threat Detection with Microsoft Security Copilot", publisher: arXiv (Microsoft authors), type: academic, url: "https://arxiv.org/abs/2605.20896", date: 2026-05-20, access: full, locator: "abstract" }
    - { ref: MSFT-DEFENDERAGENTS-2026, title: "Deploy AI agents in Microsoft Defender", publisher: Microsoft, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender", date: 2026-08-05, access: full, locator: "section on the Dynamic Threat Detection Agent" }
  last_reviewed: 2026-10-17
  notes: "Authors are Microsoft staff, so the figures are vendor-published; customers are not named. The paper says the agent is deployed across tens of thousands of Defender customers. The agent works across alerts and telemetry, so it also belongs to security operations (see routing). Only the abstract was read for the figures."

- id: security-threat-intelligence-14
  title: OSINT triage, deep search and report drafting agent with expert feedback and external verification
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Analysts triage articles, gather supporting evidence and write the report. Analysts at the paper's authors' organization said that analyzing one incident described in an article typically takes several hours."
  solution: "Authors from Microsoft Research and Microsoft describe a Threat Research Agent (TRA) integrated into their organization's CTI workflow. An LLM does preliminary research on a seed article, generates queries, retrieves supplementary content from public and proprietary sources, filters and evaluates it, and drafts a cited report for human review. Verifiers cross-check IoCs and TTPs against external sources such as VirusTotal, and expert corrections are fed back into the prompts (ARXIV-2603.09452, sections 1 and 5)."
  outcomes:
    - lever: quality
      description: "IoC extraction precision rose a few points with TRA for every base model, at several times the run time. The paper's text states a much larger gain (26 percentage points); its appendix table does not support that, so the table values are used here."
      figure: "IoC precision +0.02 to +0.05 across four base models (for example 0.8240 to 0.8496 for GPT-4o; 0.8503 to 0.8864 for o3-mini)"
      measures: "Precision of IoC extraction on the CyberThreat-Eval benchmark, built from the authors' daily CTI workflow, vanilla LLM versus the same LLM inside TRA (Table 6, Appendix D); GPT-4o run time rose from about 580 s to about 2,286 s; benchmark size not read; section 5.2 text says 'by 26 percentage points' and does not match Table 6"
      provenance: self-reported
      source_ref: ARXIV-2603.09452
    - lever: quality
      description: "TTP identification precision rose modestly with TRA while recall was flat or lower, so TTP mapping stays the weak point."
      figure: "TTP precision 0.3480 to 0.4190 (o3-mini), 0.2787 to 0.3065 (GPT-4o), 0.2387 to 0.2508 (fine-tuned GPT-4o); recall 0.1759 to 0.1558 for o3-mini"
      measures: "Precision and recall of ATT&CK TTP identification on CyberThreat-Eval, vanilla versus TRA (Table 6); section 5.2 text quotes 0.28 to 0.42 and 0.24 to 0.31, which differ from the table"
      provenance: self-reported
      source_ref: ARXIV-2603.09452
    - lever: quality
      description: "Expert ratings of generated narratives improved most, especially for weaker base models; the paper calls TRA drafts 'publish-ready' (under 25 words quoted)."
      figure: "threat-actor relevance 1.547 to 2.902 (GPT-4o); clarity 4.753 to 4.814 and coherence 4.731 to 4.810 (o3-mini)"
      measures: "Average expert scores on a five-point scale for threat-actor narratives, vanilla versus TRA (Table 6); number of raters and items not read"
      provenance: self-reported
      source_ref: ARXIV-2603.09452
    - lever: quality
      description: "Without TRA, the same models over-accepted articles at triage and gave weak priority scores."
      figure: "triage precision typically below 0.40 with recall often above 0.90; priority-score accuracy 55 to 60%"
      measures: "Article accept/reject precision and recall, and accuracy of priority scores, for the tested LLMs on CyberThreat-Eval triage tasks (section 4, Table 4 discussion)"
      provenance: self-reported
      source_ref: ARXIV-2603.09452
  prerequisites:
    - "A benchmark from the team's own workflow with expert annotations (ARXIV-2603.09452, section 3)."
    - "Access to external ground-truth sources such as VirusTotal for verification (ARXIV-2603.09452, section 5.1)."
  risks_and_guardrails:
    - "LLMs struggled to distinguish correct from incorrect information and to map ATT&CK TTPs; TRA 'cannot yet fully automate' the workflow without human oversight (ARXIV-2603.09452, abstract and section 5.2)."
    - "There is a trade-off between precision, latency and token cost; for IoC extraction TRA raised precision but also run time several-fold (ARXIV-2603.09452, Table 6 and the discussion of trade-offs)."
  human_checkpoints:
    - "TRA outputs are reviewed by a team of experts and their corrections are collected systematically (ARXIV-2603.09452, section 5.2)."
  role_evolution: "Experts review cited drafts instead of building them; their corrections become labeled data. In one case TRA surfaced a hardcoded-password fact that the analyst, who had read several articles, had missed (ARXIV-2603.09452, section 5.2)."
  evidence_grade: A
  sources:
    - { ref: ARXIV-2603.09452, title: "CyberThreat-Eval: Can Large Language Models Automate Real-World Threat Research?", publisher: arXiv (TMLR 11/2025), type: academic, url: "https://arxiv.org/abs/2603.09452", date: 2026-03-10, access: full, locator: "section 1; section 4.4; section 5.1; section 5.2 and Table 6" }
  last_reviewed: 2026-10-17
  notes: "The paper says 'the company' without naming it; the authors are affiliated with Microsoft Research and Microsoft, so the deploying organization is probably Microsoft's CTI division, but that is an inference. Figures are self-reported by the deploying team on its own benchmark. The paper reports TRA as 'successfully integrated into the company's daily CTI workflow' without usage volumes."

- id: security-threat-intelligence-15
  title: Agents that monitor coverage of priority intelligence requirements and flag collection gaps
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [coordination-scheduling, research-synthesis]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Intelligence requirements are expanding (deepfakes, AI-accelerated exploitation, AI-enabled attack vectors) while analyst capacity is flat, so teams struggle to know which requirements are covered by which sources."
  solution: "Idea reported from interviews: Flashpoint's research says practitioners see PIR coverage monitoring and intelligence briefings as workflows where agents can extend coverage and reduce recurring work while keeping analysts involved (FLASHPOINT-ENTERPRISETI-2026, 'What the Findings Mean')."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "No deployment or measurement found; the report offers interview findings only"
      provenance: vendor-published
      source_ref: FLASHPOINT-ENTERPRISETI-2026
  prerequisites:
    - "Written priority intelligence requirements tied to business risks (FLASHPOINT-ENTERPRISETI-2026, section on AI-related threats)."
  risks_and_guardrails:
    - "Interviewees want read-only assistants, reviewable output, reversible actions and clear success criteria before granting agents more autonomy (FLASHPOINT-ENTERPRISETI-2026, agentic AI section)."
  human_checkpoints:
    - "Analysts stay in the intelligence process (FLASHPOINT-ENTERPRISETI-2026, 'What the Findings Mean')."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: FLASHPOINT-ENTERPRISETI-2026, title: "The Enterprise Threat Intelligence Report: 2026", publisher: Flashpoint, type: survey, url: "https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/", date: 2026-10-13, access: full, locator: "'What the Findings Mean for Threat Intelligence Programs'" }
  last_reviewed: 2026-10-17
  notes: "Idea (grade D). The source is a vendor-commissioned qualitative study of just over 20 budget owners and influencers at large North American enterprises, interviewed in early fall 2026. Cloudflare's PIR and RFI features (2024) are not AI features and are not used as evidence."

- id: security-threat-intelligence-16
  title: SOAR enrichment and an internal MCP server that let agents pull threat intelligence on demand
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [software-systems, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Alerts need threat scores, actor profiles and indicator context before anyone can decide, and manual lookups across tools slow triage."
  solution: "Superhuman first wired Recorded Future into its SOAR so alerts are enriched automatically with threat scores, actor profiles and IOC details, then built an internal MCP server on the Recorded Future API so its AI agents can request intelligence, evaluate risks and summarize threats in natural language. The first AI use case was detection and response; it then extended into enrichment, research and engineering support (RF-SUPERHUMAN-2026, sections on automation and AI-native workflows). Google's changelog describes a SOAR playbook calling its Agentic API to triage an unknown file or IP, gather dark-web chatter and draft YARA rules before an analyst starts (GOOGLE-GTICHANGELOG-2026). Anthropic's posting lists integrations to VirusTotal, Censys and Urlscan through MCP servers for multi-source correlation (ANTHROPIC-JOBTIE-2026). Anthropic also publishes a cookbook agent for IOC enrichment that uses simulated tools (ANTHROPIC-COOKBOOK-TI-2026)."
  outcomes:
    - lever: speed
      description: "Superhuman says investigation times and dwell time are lower with a single trusted source, but gives no numbers."
      figure: "none published"
      measures: "Quote from a Superhuman security engineer ('our investigation times are lower'); no baseline or sample"
      provenance: vendor-published
      source_ref: RF-SUPERHUMAN-2026
  prerequisites:
    - "A SOAR platform or agent framework, and API access to an intelligence provider (RF-SUPERHUMAN-2026)."
    - "Scoped identities and tools for the agent; for Google's Agentic API, an Enterprise, Enterprise Plus or Integration Advanced licence (GOOGLE-GTICHANGELOG-2026, 'Public Preview: Agentic API')."
  risks_and_guardrails:
    - "Superhuman advises starting with a specific use case and not 'using AI just to use AI' (RF-SUPERHUMAN-2026, closing section)."
    - "In OpenCTI, tools that change the platform can be gated for approval; an 'always allow' choice also applies to scheduled runs with no one watching, and unattended AI features stop and report that approval was needed (OPENCTI-COPILOT-2026, 'Approving a tool call')."
    - "Anthropic's cookbook states that its example tools are simulated and must be swapped for real APIs (ANTHROPIC-COOKBOOK-TI-2026, introduction)."
  human_checkpoints:
    - "Superhuman analysts keep doing in-depth investigations; the agents summarize and enrich (RF-SUPERHUMAN-2026)."
  role_evolution: "Security engineers at Superhuman build and operate the integrations; engineers elsewhere in the company query intelligence themselves (RF-SUPERHUMAN-2026). Anthropic and Coinbase postings ask intelligence engineers to build MCP and agent integrations and to feed 'agent workflows' downstream (ANTHROPIC-JOBTIE-2026; COINBASE-JOBTIPE-2026)."
  evidence_grade: B
  sources:
    - { ref: RF-SUPERHUMAN-2026, title: "How Superhuman Unlocked a New Era of AI-Driven Threat Intelligence With Recorded Future", publisher: Recorded Future, type: vendor, url: "https://www.recordedfuture.com/case-study/superhuman", date: 2026-06-08, access: full, locator: "sections on SOAR automation, the internal MCP server and closing advice" }
    - { ref: GOOGLE-GTICHANGELOG-2026, title: "August 12th, 2026 - Agentic Flows & API, and Threat Actor Naming Updates", publisher: Google, type: vendor, url: "https://gtidocs.readme.io/changelog/august-5th-2026-agentic-flows-api-and-threat-actor-naming-updates", date: 2026-08-12, access: full, locator: "Public Preview: Agentic API; example use case on SOAR alert enrichment" }
    - { ref: ANTHROPIC-JOBTIE-2026, title: "Threat Intelligence Engineer (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5074937008", date: 2026-01-20, access: full, locator: "Responsibilities bullet on MCP integrations. Posting last updated 2026-08-21" }
    - { ref: COINBASE-JOBTIPE-2026, title: "Threat Intelligence Platform Engineer (job posting)", publisher: Coinbase, type: job-posting, url: "https://www.coinbase.com/careers/positions/8177619", date: 2026-09-03, access: full, locator: "What you'll do bullets. Posting last updated 2026-10-13" }
    - { ref: ANTHROPIC-COOKBOOK-TI-2026, title: "Threat intelligence enrichment agent (Claude Cookbook)", publisher: Anthropic, type: vendor, url: "https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent", date: 2026-04-07, access: full, locator: "introduction; tool definitions" }
    - { ref: OPENCTI-COPILOT-2026, title: "Interactions using AI (chatbot) - CTI Copilot (OpenCTI documentation)", publisher: Filigran / OpenCTI, type: vendor, url: "https://docs.opencti.io/latest/usage/copilot/", date: 2026-08-27, access: full, locator: "'Approving a tool call'. The source page is marked as under construction" }
  last_reviewed: 2026-10-17
  notes: "Grade B: Superhuman is named but publishes no figures. Superhuman's case study is written by Recorded Future. The Anthropic cookbook is a reference design and not evidence of use."

- id: security-threat-intelligence-17
  title: Automatic mapping of CTI report text to ATT&CK techniques
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [data-reporting, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Mapping report sentences to a taxonomy of more than 200 technique classes is slow and error-prone, but the mapping is what lets teams compare actors and drive detection."
  solution: "MITRE's Center for Threat-Informed Defense describes TRAM as an open-source platform that maps CTI reports to ATT&CK (CTID-TRAMREADME-2026), and its project page says the latest work improves training data and fine-tunes LLMs for the mapping (MITRE-TRAM-2023). EclecticIQ's Intelligence Center markets AI-embedded search and, in release 3.9, lets customers connect Azure, Anthropic's Claude, Mistral, OpenAI, Ollama, Amazon Bedrock and other LLM endpoints per capability, including summarization (EIQ-IC39-2026). Research evaluates the task on realistic reports."
  outcomes:
    - lever: quality
      description: "Independent test on complex, unstructured reports: the best of seven open-source LLMs scored low; the authors conclude open-source LLMs are not sufficient for production-grade classification."
      figure: "best micro-averaged F1 0.22"
      measures: "Micro-averaged F1 of multi-label ATT&CK technique classification on 2,076 human-annotated sentences (1,281 technique-positive) from 83 CTI reports, seven open-source LLMs from 8B to 236B parameters; inter-annotator kappa 0.68"
      provenance: independent
      source_ref: ARXIV-2606.18166
    - lever: quality
      description: "Microsoft-authored workflow benchmark: baseline LLMs had low TTP identification precision."
      figure: "TTP precision 0.18 to 0.35 for baseline models"
      measures: "Precision of TTP identification on CyberThreat-Eval for vanilla GPT-4o, o3-mini, fine-tuned GPT-4o and fine-tuned GPT-4o-mini (Table 6)"
      provenance: self-reported
      source_ref: ARXIV-2603.09452
  prerequisites:
    - "A recent ATT&CK version in the platform; EclecticIQ 3.9 added ATT&CK v19.1 support after the Enterprise Defense Evasion tactic was split (EIQ-IC39-2026, ATT&CK section)."
  risks_and_guardrails:
    - "Models both miss techniques whose evidence is plain (masquerading was labeled in 21 reports and missed by all three tested models) and assert techniques the report does not support (ARXIV-2609.01174, section 6, Experiment 2)."
    - "Mappings should be reviewed by analysts; the independent F1 results show current open models are not production-grade on complex reports (ARXIV-2606.18166, abstract)."
  human_checkpoints:
    - "Not described for the products. In the independent evaluation, human-annotated sentences are the reference standard (ARXIV-2606.18166, abstract)."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: MITRE-TRAM-2023, title: "Threat Report ATT&CK Mapper (TRAM)", publisher: MITRE Center for Threat-Informed Defense, type: standard-setter, url: "https://ctid.mitre.org/projects/threat-report-attck-mapper-tram/", date: 2023-08-24, access: full, locator: "project summary. Foundation source, older than the 18-month window" }
    - { ref: CTID-TRAMREADME-2026, title: "TRAM README", publisher: MITRE Center for Threat-Informed Defense, type: standard-setter, url: "https://raw.githubusercontent.com/center-for-threat-informed-defense/tram/main/README.md", date: 2026-10-17, access: full, locator: "opening paragraphs. File is undated and references ATT&CK v13; date is the day it was read" }
    - { ref: EIQ-IC39-2026, title: "Intelligence Center 3.9: More AI provider choice, MITRE ATT&CK v19.1 support, and more", publisher: EclecticIQ, type: vendor, url: "https://blog.eclecticiq.com/intelligence-center-3.9", date: 2026-09-22, access: full, locator: "paragraphs on AI providers and ATT&CK v19.1" }
    - { ref: ARXIV-2606.18166, title: "Evaluating Open-Source LLMs for Multi-Label ATT&CK Technique Classification on CTI Reports", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2606.18166", date: 2026-06-16, access: full, locator: "abstract" }
    - { ref: ARXIV-2603.09452, title: "CyberThreat-Eval: Can Large Language Models Automate Real-World Threat Research?", publisher: arXiv (TMLR 11/2025), type: academic, url: "https://arxiv.org/abs/2603.09452", date: 2026-03-10, access: full, locator: "Table 6, TTP Identification precision (vanilla columns)" }
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "section 6, Experiment 2" }
    - { ref: ARXIV-2608.06778, title: "Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2608.06778", date: 2026-08-07, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Graded C: the named tools (TRAM, EclecticIQ) document capability but publish no deployment outcome; the measurements are independent and show weak performance. The MITRE page is from 2023 and its README describes an earlier supervised model that identifies up to 50 techniques, so it is a foundation source. A related independent paper (ARXIV-2608.06778, TTP-R1) reports a fine-tuned 8B model beating a retrieval-augmented frontier model on sub-technique F1 by 7.4 points (2026-08-07); abstract only."

- id: security-threat-intelligence-18
  title: Cross-vendor report normalization to measure overlap and bias before buying or trusting intelligence sources
  archetype: security
  module: threat-intelligence
  function: strategy-planning
  work_types: [data-reporting, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Annual IR and threat reports contradict one another on top intrusion vectors and on how terms such as credential misuse are defined, which causes mis-prioritization. Each vendor's telemetry footprint shapes what it sees."
  solution: "Research idea: use an LLM pipeline to structure many public CTI reports (actors, victims, vendors, IoCs, TTPs) and quantify how much additional sources add. A study structured 16,096 reports this way and found low overlap between vendors and diminishing returns from added sources (ARXIV-2602.17458). A FIRST 2026 talk by Team Cymru proposes treating vendor reports as partial lenses, normalizing conflicting data and pushing for shared taxonomies (FIRST-CON-2026, 15 June)."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "The research measures the CTI ecosystem, not the effect of a team using the method; no deployment found"
      provenance: independent
      source_ref: ARXIV-2602.17458
  prerequisites:
    - "A corpus of reports from the sources under comparison and an extraction pipeline with high precision (ARXIV-2602.17458, abstract)."
  risks_and_guardrails:
    - "Extraction errors would distort overlap statistics; the authors describe their pipeline as high-precision but the abstract gives no figures (ARXIV-2602.17458, abstract)."
  human_checkpoints:
    - "Not described."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2602.17458, title: "The CTI Echo Chamber: Fragmentation, Overlap, and Vendor Specificity in Twenty Years of Cyber Threat Reporting", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2602.17458", date: 2026-02-19, access: full, locator: "abstract" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program, Denver, 14-19 June 2026", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "'Disparate Data, Distorted Decisions: Vendor Data Bias in CTI' abstract" }
  last_reviewed: 2026-10-17
  notes: "Idea (grade D). The FIRST abstract does not say AI is used in the proposed normalization. Pattern is 'other': evidence-quality assessment of sources."

- id: security-threat-intelligence-19
  title: Multi-agent LLM systems that actively elicit intelligence from underground forum conversations
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, expert-judgment]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Valuable intelligence is migrating from open forums to private or harder-to-reach spaces, so passive monitoring sees less."
  solution: "A university prototype, DarkBot, splits interaction across eleven agents in three blocks (relevance and safety gating, question generation guided by ATT&CK tactics, and style adaptation). It was tested on recorded conversations and then in a prospective matched deployment on live forums (ARXIV-2608.23185). This entry records a research result at the level a defender needs; it is not an operational recommendation, and covert engagement with criminal communities raises legal, ethical and operational-security questions that the abstract does not resolve."
  outcomes:
    - lever: growth
      description: "In a controlled evaluation, the system recovered most validated ATT&CK techniques present in the original discussions from the initial post alone; in a matched live deployment threads assigned to it accumulated more CTI entities than controls."
      figure: "72.8% of validated ATT&CK techniques recovered; 3.85 more CTI entities per thread over seven days"
      measures: "Share of validated MITRE ATT&CK techniques recovered across 100 CrimeBB conversations using only the initial post; mean extra CTI entities in threads assigned to DarkBot versus matched controls over seven days; 104 live conversations observed without account suspensions or accusations of automated participation"
      provenance: independent
      source_ref: ARXIV-2608.23185
  prerequisites:
    - "Access to forum accounts and an ethics and legal review (not described in the abstract)."
  risks_and_guardrails:
    - "A layered safety design contained all injected jailbreak attempts at the pipeline level in the authors' tests (ARXIV-2608.23185, abstract)."
  human_checkpoints:
    - "Not described in the abstract."
  role_evolution: "Not described."
  evidence_grade: A
  sources:
    - { ref: ARXIV-2608.23185, title: "Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums", publisher: arXiv (Politecnico di Milano and BV TECH), type: academic, url: "https://arxiv.org/abs/2608.23185", date: 2026-08-24, access: full, locator: "abstract; author affiliations on page 1" }
  last_reviewed: 2026-10-17
  notes: "Graded A only because a named academic organization published measured outcomes; this is a research prototype and not an operating CTI team's practice, so it should not be read as evidence of field adoption. The abstract was read plus the PDF's first page."

- id: security-threat-intelligence-20
  title: AI-lab threat-intelligence teams using their own models in misuse investigations and situational awareness
  archetype: security
  module: threat-intelligence
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Model providers must detect and disrupt misuse of their own products and track threats to themselves, over very large volumes of conversation and telemetry data."
  solution: "OpenAI's Intelligence and Investigations engineering team builds systems that use OpenAI's models for lead generation, triage, synthesis and analysis over large datasets, working directly with analysts and investigators (OPENAI-JOBII-2025). OpenAI's Threat Intelligence team seeks investigators who build agentic workflows to scale investigative throughput on actors targeting OpenAI or misusing its models (OPENAI-JOBTTI-2026). Anthropic's Threat Intelligence team posts for investigators who detect and disrupt misuse of its models for cyber operations (ANTHROPIC-JOBTCTI-2026), and its September 2026 report says the team identified and disrupted operations in which actors tried to use Claude for malicious activity (ANTHROPIC-TIR-2026)."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "Postings and the report do not say how much the models speed investigations"
      provenance: self-reported
      source_ref: OPENAI-JOBII-2025
  prerequisites:
    - "Internal telemetry from the provider's own platform, plus OSINT and vendor data (OPENAI-JOBTTI-2026, responsibilities)."
  risks_and_guardrails:
    - "Not described in the postings."
  human_checkpoints:
    - "Investigators and analysts remain responsible for assessments; engineers build tools to accelerate them (OPENAI-JOBII-2025, 'About the Role')."
  role_evolution: "OpenAI pairs engineers with analysts and investigators on one team; Anthropic describes a small engineering role that may become a multi-person collections function (OPENAI-JOBII-2025; ANTHROPIC-JOBTIE-2026)."
  evidence_grade: C
  sources:
    - { ref: OPENAI-JOBII-2025, title: "Full-Stack Software Engineer, Intelligence & Investigations (job posting)", publisher: OpenAI, type: job-posting, url: "https://jobs.ashbyhq.com/openai/52c72cb9-7c44-4cba-b440-e05262a38491", date: 2025-11-12, access: full, locator: "About the Team; About the Role; 'In this role, you will'" }
    - { ref: OPENAI-JOBTTI-2026, title: "Technical Threat Investigator, Threat Intel Engineering (job posting)", publisher: OpenAI, type: job-posting, url: "https://jobs.ashbyhq.com/openai/f01b7084-a68d-4e30-ace9-6b5e6d90c517", date: 2026-04-30, access: full, locator: "About the Role; responsibilities" }
    - { ref: ANTHROPIC-JOBTCTI-2026, title: "Technical Cyber Threat Investigator (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5066995008", date: 2026-01-13, access: full, locator: "About the Role. Posting last updated 2026-08-21" }
    - { ref: ANTHROPIC-JOBTIE-2026, title: "Threat Intelligence Engineer (job posting)", publisher: Anthropic, type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/5074937008", date: 2026-01-20, access: full, locator: "About the Role" }
    - { ref: ANTHROPIC-TIR-2026, title: "Countering misuse of AI: September 2026", publisher: Anthropic, type: vendor, url: "https://www.anthropic.com/threat-intelligence-report-september-2026", date: 2026-09-10, access: full, locator: "introduction. Date from Anthropic's page listing; page read via text mirror" }
  last_reviewed: 2026-10-17
  notes: "Graded C: job postings describe duties and not measured use. This is a new CTI function (provider-side misuse intelligence) rather than a faster version of an existing one, hence change_scope 'model'. Anthropic's report describes adversary activity and is routed to ai-security for content. All provider statements here are self-descriptions."

- id: security-threat-intelligence-21
  title: Hunting a threat-actor infiltration funnel (fake job applicants) with behavioral detections, enrichment and AI-driven risk assessment, feeding indicators back
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [expert-judgment, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "North Korean threat actors pose as legitimate developers and security engineers in hiring pipelines, and most organizations have visibility gaps in recruiting systems."
  solution: "Datadog's Detection Engineering and Threat Hunting team describes a detection stack for identifying and blocking fake applicants, using behavioral and IOC-based detections, cross-system enrichment for correlation, and AI-driven risk assessment; the team collects intelligence from synthetic personas and converts it into indicators (FIRST-CON-2026, 17 June, TLP:AMBER session abstract)."
  outcomes:
    - lever: risk
      description: "The talk promises metrics from nine months of detecting and tracking fake applicants; the public abstract gives none."
      figure: "none published"
      measures: "The abstract mentions 'metrics and tangible insights from 9 months' without figures"
      provenance: self-reported
      source_ref: FIRST-CON-2026
  prerequisites:
    - "Logs and signals from recruiting systems correlated with other systems (FIRST-CON-2026, abstract)."
  risks_and_guardrails:
    - "The session is marked TLP:AMBER, so detailed content is restricted; only the abstract is public."
  human_checkpoints:
    - "Not described."
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program, Denver, 14-19 June 2026", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "'DPRK Fake Applicants in Your Recruitment Funnel? How to Catch Them All' abstract, 17 June 2026" }
  last_reviewed: 2026-10-17
  notes: "The role of AI in the stack is a single phrase ('AI-driven risk assessment'). Datadog is named as the deploying organization; slides were not read."

- id: security-threat-intelligence-22
  title: "ISAC operations: AI to speed alert distribution and collate open-source intelligence for member reports"
  archetype: security
  module: threat-intelligence
  function: service-delivery
  work_types: [document-production, coordination-scheduling]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "ISACs must analyze and distribute threat intelligence quickly to members whose money or services are at stake, without adding noise or eroding the trust that makes members share."
  solution: "Health-ISAC is looking into whether AI can speed distribution of threat alerts and collation of open-source intelligence for daily reports, which its CEO says would take the noise out of the work (HISAC-AIISAC-2026; CSD-ISACAI-2026). The National Council of ISACs, which she chairs, is considering a cross-sector AI working group (CSD-ISACAI-2026). A government-led AI-ISAC is in development with no launch date (NEXTGOV-AIISAC-2026)."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Described as under consideration; no deployment or measurement"
      provenance: self-reported
      source_ref: CSD-ISACAI-2026
  prerequisites:
    - "Member trust in the quality of shared information; leaders say people must see the value in what is shared (CSD-ISACAI-2026)."
  risks_and_guardrails:
    - "The RH-ISAC chief security officer warned of collateral damage from AI managing workloads at scale, concern that AI analysis could break chain of custody of threat data, and that she saw nothing on the market people trust (CSD-ISACAI-2026, panel at RSAC 2026-03-23)."
    - "FS-ISAC's CISO said trust matters most when converted into action, and his ISAC focuses on implementable advice (CSD-ISACAI-2026)."
  human_checkpoints:
    - "Not described."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: CSD-ISACAI-2026, title: "ISACs confront AI's promise and peril for threat intelligence-sharing", publisher: Cybersecurity Dive, type: press, url: "https://www.cybersecuritydive.com/news/ai-isacs-threat-intelligence-information-sharing-trust/815499/", date: 2026-03-23, access: full, locator: "paragraphs on Health-ISAC, RH-ISAC and FS-ISAC comments" }
    - { ref: HISAC-AIISAC-2026, title: "ISACs confront AI's promise and peril for threat intelligence-sharing (Health-ISAC media mention)", publisher: Health-ISAC, type: community, url: "https://health-isac.org/isacs-confront-ais-promise-and-peril-for-threat-intelligence-sharing/", date: 2026-03-27, access: full, locator: "summary paragraphs" }
    - { ref: NEXTGOV-AIISAC-2026, title: "AI info-sharing center is in development, CISA official says", publisher: Nextgov/FCW, type: press, url: "https://www.nextgov.com/cybersecurity/2026/02/ai-info-sharing-center-development-cisa-official-says/411167", date: 2026-02-03, access: full, locator: "paragraphs quoting the CISA executive assistant director" }
  last_reviewed: 2026-10-17
  notes: "Idea (grade D) with named organizations: Health-ISAC says it is 'looking into' these uses. No FS-ISAC AI program was found; FS-ISAC's newsroom lists AI guidance documents on risk and governance."

- id: security-threat-intelligence-23
  title: Machine-learning anomaly surfacing to focus government threat hunters on critical-infrastructure and federal network data
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [data-reporting, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Hunt and SOC analysts handle terabytes of daily network log data, so they need a way to narrow the data they review."
  solution: "CISA's CyberSentry program uses unsupervised machine learning with rule-based heuristics to automate data fusion and correlation and highlight anomalies in participating critical-infrastructure network data for analyst review, with a query interface and dashboards (DHS-AIINV-CISA-2026, DHS-106, deployed). A similar federal-network use case (DHS-2403) based on Einstein sensor data is listed as retired."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "The inventory gives no detection or workload figures"
      provenance: self-reported
      source_ref: DHS-AIINV-CISA-2026
  prerequisites:
    - "Partner opt-in to CyberSentry monitoring (DHS-AIINV-CISA-2026, DHS-106)."
  risks_and_guardrails:
    - "The retired status of DHS-2403 and the absence of reasons in the inventory mean lessons are not public (DHS-AIINV-CISA-2026, Inactive section)."
  human_checkpoints:
    - "Anomalies are highlighted for CISA analyst review (DHS-AIINV-CISA-2026, DHS-106)."
  role_evolution: "Analysts narrow the scope of analysis and prioritize data for review (DHS-AIINV-CISA-2026, DHS-2403 summary)."
  evidence_grade: B
  sources:
    - { ref: DHS-AIINV-CISA-2026, title: "Cybersecurity and Infrastructure Security Agency - AI Use Cases (DHS AI Use Case Inventory)", publisher: US Department of Homeland Security, type: regulator, url: "https://www.dhs.gov/ai/use-case-inventory/cisa", date: 2026-01-28, access: full, locator: "Deployment: DHS-106; Inactive: DHS-2403" }
  last_reviewed: 2026-10-17
  notes: "The inventory classifies this as classical or predictive machine learning, not generative AI; it is included because it shows named, deployed AI in government threat hunting. Grade B, no measurements."
```

## 3. Module notes

### Processes and key steps (with work types)

- **Direction and requirements** (priority intelligence requirements, requests for information, stakeholder questions): expert-judgment, coordination-scheduling. AI touches it only as an idea so far (use cases 15 and 01).
- **Collection** (feeds, OSINT, dark web, stealer logs, telemetry, sandbox output, partner sharing): research-synthesis, data-reporting. Use cases 02, 09.
- **Processing and enrichment** (extraction of indicators, normalization, tagging, ATT&CK mapping, translation, redaction): data-reporting, transaction-processing. Use cases 02, 10, 11, 17.
- **Analysis** (triage, relevance to the organization, malware analysis, attribution, campaign tracking): expert-judgment. Use cases 06, 08, 14.
- **Production and dissemination** (briefings, finished reports, STIX/TAXII and ISAC sharing under TLP): document-production, review-assurance. Use cases 07, 10, 11, 22.
- **Action** (detections, blocklists, hunts, SOAR playbooks): software-systems. Use cases 03, 04, 05, 16.
- **Threat hunting** (hypothesis, query, investigation, conversion to standing detection): expert-judgment, research-synthesis. Use cases 04, 12, 13, 21, 23.
- A practitioner survey and literature review split "generation and sharing" into four steps: intelligence extraction, normalization and enrichment, codification, and distribution (ARXIV-2609.01174, section 5). Mandiant's older description uses the five-phase cycle (MANDIANT-AIPHASES-2023).

### Common pain points

- **Noise and capacity.** In Flashpoint's interview study, 65% of respondents named alert noise and false positives, 55% named analyst bandwidth and half named integration gaps (FLASHPOINT-ENTERPRISETI-2026, key findings; just over 20 interviewees, so percentages are small-number).
- **Small teams and little measurement.** Most formal CTI teams have fewer than four full-time staff; 44% cite lack of time and 44% lack of funding as top barriers; 57% of programs do not track maturity and 49% do not gather systematic feedback (SANS-CTI-2026, paragraph on resourcing; survey of 401 respondents plus 67 CISOs and CSOs).
- **Intelligence that does not reach decisions.** 91% of CISOs value CTI but only 26% say it drives their decisions (SANS-CTI-2026, title and opening).
- **Manual sharing.** In an 18-person survey across five organizations with threat-intelligence teams, 17 cited exposure of sensitive information, 13 noisy attack data, 10 mapping to taxonomies and 7 format translation (ARXIV-2609.01174, section 3.2). Indicators often circulate in emails and chats and bypass STIX/TAXII (FIRST-CON-2026, CISA IMX abstract).
- **Slow production.** Analysts at the authors' organization say analyzing one incident from an article typically takes several hours (ARXIV-2603.09452, section 1).
- **Conflicting vendor reports.** Annual reports contradict each other on top intrusion vectors and category definitions because of each vendor's data pipeline (FIRST-CON-2026, Team Cymru abstract).

### Metrics and benchmarks (with sources)

- Adoption: 45% of organizations use AI in CTI programs (press release wording; survey of 401 respondents), mainly summarization and report writing (SANS-CTI-2026). Interviewees: 25% agentic AI in production, 20% piloting, 35% planning within 12 to 24 months (FLASHPOINT-ENTERPRISETI-2026). Only 3 of 18 practitioners used LLMs to analyze logs for CTI generation (ARXIV-2609.01174, section 3.2).
- Production-scale agent: 80.1% precision from customer feedback over 120 days; median 28 minutes and USD 2.04 per investigation; 0.38% job failure rate (ARXIV-2605.20896, abstract; vendor-authored).
- CTI-workflow tasks: triage precision typically below 0.40 with recall above 0.90, priority-score accuracy 55 to 60%, TRA gains of a few precision points at higher run time (ARXIV-2603.09452, sections 4 and 5, Table 6; the text of section 5.2 quotes larger gains than the table).
- Independent academic results: best F1 0.22 for ATT&CK classification of complex reports (ARXIV-2606.18166); micro precision 0.03 to 0.34 for entity extraction (ARXIV-2610.20417); threat-level determination F1 0.40 to 0.58 after fine-tuning, with zero-shot models weak (ARXIV-2609.07582, abstract); 3.8% of malicious events flagged in open-ended hunting (ARXIV-2604.19533); hunt-lead F1 0.44 to 0.85 with grounding in the defender's assets (ARXIV-2609.08790). Benchmarks to know: CTIBench (ARXIV-2406.07599, 2024), AthenaBench (ARXIV-2511.01144), CTIConnect (ARXIV-2510.11974), CTI-REALM (ARXIV-2603.13517), CyberThreat-Eval (ARXIV-2603.09452).
- Vendor-published: Mandiant 2023 figures (96% fewer false positives in alert generation; 97% IOC reduction at high confidence) (MANDIANT-AIPHASES-2023); Cowbell's over-90% cost saving and CyberProof's 10 to 15 times more hunts (see use cases 01 and 04).
- **Absent everywhere in this sample:** analyst override or edit rates, error rates of deployed assistants, parallel-run comparisons, and any independent test of a vendor CTI assistant on live customer data.

### Guardrails and regulatory points

- **Provenance and trust.** Vendors stress citations and visible tool traces (GOOGLE-GTIAGENTIC-2026; RF-AI-2026). Cloudflare restricted AI tags to the customer's vocabulary and marked who applied each tag (CLOUDFLARE-THREATSIGNALS-2026).
- **Agent permissions.** Microsoft gives its briefing agent a dedicated Entra agent identity with minimal read rights (MSFT-TIBAGENT-2026; MSFT-AGENTSOVERVIEW-2026). OpenCTI gates tools through a separate platform and warns that an 'always allow' choice also covers unattended scheduled runs (OPENCTI-COPILOT-2026). One retail interviewee would accept only read-only AI assistants (FLASHPOINT-ENTERPRISETI-2026, agentic AI section).
- **Data handling.** Google warns that submissions to its web interface may be added to a shared dataset (GOOGLE-GTIAGENTIC-2026). Practitioners rank data privacy as the main hurdle to AI in sharing (ARXIV-2609.01174, section 3.2).
- **Information exchange rules.** FIRST's Information Exchange Policy SIG says missing policy clarity on permitted use and redistribution impedes timely exchange (FIRST-CON-2026, SIG description). SANS reports 55% of organizations lack legally reviewed CTI sharing processes, citing new NIS2 and Cyber Resilience Act obligations in 2026 (SANS-CTI-2026).
- **Federal AI inventory.** CISA lists its CTI-adjacent AI use cases with status and a high-impact flag, the active entries are marked not high-impact (DHS-AIINV-CISA-2026).
- **Poisoned inputs.** A 2026 FIRST session shows that one crafted report or email can steer retrieval and the analyst-facing narrative of an LLM-assisted workflow (FIRST-CON-2026, CyCraft session, 18 June); another session (NTT DATA) covers manipulating DFIR agents (FIRST-CON-2026, title only, TLP:AMBER).

### Frontier signals (dated)

- 2026-08-12: Google adds scheduled agentic investigations (Flows) and an Agentic API in public preview, with SOAR enrichment as an example (GOOGLE-GTICHANGELOG-2026). By 2026-09-16 it documents an Agentic MCP server for assistants and custom agents (GOOGLE-GTIMCP-2026).
- 2026-09-22: EclecticIQ lets customers choose among LLM providers per capability, including Claude, Mistral, Azure, OpenAI, Ollama and Bedrock (EIQ-IC39-2026).
- 2026-09-29: Cloudflare makes Threat Signals available to every account and offers custom agentic skills to enterprise tiers (CLOUDFLARE-THREATSIGNALS-2026).
- 2026-10-13: Flashpoint's interviewees rank AI-related threats as the top area for expanded intelligence coverage and say the strongest agent uses are PIR coverage monitoring and briefings (FLASHPOINT-ENTERPRISETI-2026).
- 2026-05-20: Microsoft reports an always-on investigation agent running at scale (ARXIV-2605.20896).
- 2026-02-03: A government-led AI-ISAC is described as in development, with no timeline (NEXTGOV-AIISAC-2026).
- 2026-06 to 2026-09: Adversaries move to agent-run campaigns; Google's AI Threat Tracker (2026-09-08) reports a credential-harvesting campaign planned and executed in under six hours (GTIG-AITRACKER-2026, executive summary). This raises the speed pressure on CTI, and is routed for its own content.

### Workforce and role effects

- Teams are small (SANS: most formal teams under four full-time staff) and cannot hire their way out: 'Good analysts take time to develop and train' (FLASHPOINT-ENTERPRISETI-2026, challenges section, healthcare leader).
- Postings lean toward engineering. Anthropic wants a threat-intelligence engineer to build collections, YARA tooling and MCP integrations (ANTHROPIC-JOBTIE-2026). Cloudflare's Senior Threat Intelligence Engineer role combines intelligence, machine-learning detections and SOAR automation (CLOUDFLARE-JOBSTIE-2026). Coinbase asks intelligence engineers to build automation and its platform engineer to own Vertex Synapse and ship intelligence into 'agent workflows' (COINBASE-JOBSTIE-2026; COINBASE-JOBTIPE-2026). GitLab's threat research engineer builds AI-powered research and detection workflows and is expected to use AI daily (GITLAB-JOBTRE-2026). OpenAI pairs engineers with investigators (OPENAI-JOBII-2025).
- Hunters are asked to use AI and validate its output (HUNTRESS-JOBDETH-2026; TWILIO-JOBSSETH-2026).
- Not every posting changes: Recorded Future's Threat Intelligence Response Analyst and Dragos's Associate Principal CTI Analyst postings read in full contain no mention of AI (RECORDEDFUTURE-JOBTIRA-2026; DRAGOS-JOBCTI-2026). Two postings is a small sample.
- Non-security staff gain access: Superhuman engineers query intelligence directly (RF-SUPERHUMAN-2026).
- Junior-pipeline effects are not documented in the CTI sources read.

### Objections and concerns practitioners raise

- **Reliability.** Of 18 practitioners, 16 questioned whether AI could reliably filter raw logs, 14 lacked confidence AI would do sharing tasks correctly and 13 expected inaccuracies in shared data (ARXIV-2609.01174, section 3.2). One interviewee: 'An agent that's confidently wrong is worse than one that's slow' (FLASHPOINT-ENTERPRISETI-2026).
- **Privacy and compliance.** 12 of 18 worried AI could break privacy or regulatory compliance when sharing (ARXIV-2609.01174, section 3.2).
- **Trust in shared intelligence.** RH-ISAC's chief security officer fears chain-of-custody damage and sees nothing on the market people trust; Health-ISAC and FS-ISAC leaders stress preserving member trust (CSD-ISACAI-2026).
- **Vendor bias.** Reports are partial lenses and vendors overlap little (FIRST-CON-2026; ARXIV-2602.17458).
- **Attack surface of the AI itself.** Poisoned artifacts and manipulated DFIR agents (FIRST-CON-2026, sessions on 18 June).
- **Vendor-supplied numbers.** All outcome figures for named deployments in this sample come from vendors or the deploying teams.

### Interview probes for an advisor

1. Which CTI steps do analysts still do by hand (collection triage, indicator extraction, tagging, ATT&CK mapping, drafting, hunt-query writing), and for each AI-produced output what share is accepted without edit? What is measured (precision of extracted indicators, edit rates, time per report)?
2. Can an analyst trace every AI-produced indicator, tag or sentence to its source report and see whether a human or a machine applied it? Who owns the tag vocabulary?
3. What context does the model get (priority intelligence requirements, asset inventory, organization profile), and how are TLP-marked or partner-shared material and sensitive data kept out of prompts?
4. Which actions can an agent take without approval (updating blocklists, deploying detection rules, closing alerts), and how do you defend against crafted content in ingested reports?
5. How has the team's shape changed: engineers embedded with analysts, how junior analysts learn tradecraft, and which roles you would no longer hire for?

## 4. Routed to other modules

- **vulnerability-exposure**: Mandiant's blueprint for AI-assisted vulnerability management and its guardrails (MANDIANT-AIVM-2026, 2026-07-16); Google's finding that disclosures and exploitation rose and its advice to move to threat-intelligence-driven triage (GTIG-VULNTRENDS-2026, 2026-09-30); Cowbell's vulnerability playbook alerts (RF-COWBELL-2026).
- **operations** (security operations): Charlotte AI detection triage and its stated benchmark against managed-service decisions (CRWD-CHARLOTTE-2026); Cloudflare's agentic Managed Defense harness (listed in Cloudflare's Cloudforce One blog index, post dated 2026-10-07, post not read) (CLOUDFLARE-BLOGINDEX-2026); Cloudy log and analytics assistants (CLOUDFLARE-CLOUDY-2025); the SOC-side parts of the Dynamic Threat Detection Agent (ARXIV-2605.20896); the FIRST sessions on tier-1 triage and CoAnalyst (FIRST-CON-2026, 18 and 19 June).
- **ai-security** (securing and monitoring AI): adversary use of AI (GTIG-AITRACKER-2026; ANTHROPIC-TIR-2026); Google's CISO perspective on monitoring AI threats and supply-chain contamination (GOOGLE-CISOPERSP-2026, 2026-09-16); CyCraft and NTT DATA sessions on attacking LLM-assisted and DFIR agents (FIRST-CON-2026).
- **incident-response**: FIRST sessions on AI-assisted investigations and PSIRT agents listed in the landscape file; Atlassian's IR documentation framework in the FIRST program (FIRST-CON-2026).
- **governance-risk**: the AI-ISAC policy discussion (NEXTGOV-AIISAC-2026) and information-exchange policy (FIRST-CON-2026, SIG description).


## 5. Sources

All sources were opened and read (access: full); none is search-only. Dates are publication dates from page metadata or bylines. Where a page is undated, the date is the day it was read (2026-10-17) and the locator in the use case says so. Refs follow PUBLISHER-SHORT-YYYY and, for arXiv, ARXIV-id. Job postings are dated by first publication on the employer's job board.

| ref | title | publisher | type | url | date | access |
|---|---|---|---|---|---|---|
| FIRST-CON-2026 | 38th FIRST Conference program, Denver, 14-19 June 2026 | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06 | full |
| CISAGOV-IMX-2026 | cisagov/imx README | CISA | regulator | https://raw.githubusercontent.com/cisagov/imx/develop/README.md | 2026-10-17 | full |
| DHS-AIINV-CISA-2026 | Cybersecurity and Infrastructure Security Agency - AI Use Cases (DHS AI Use Case Inventory) | US Department of Homeland Security | regulator | https://www.dhs.gov/ai/use-case-inventory/cisa | 2026-01-28 | full |
| CTID-TRAMREADME-2026 | TRAM README | MITRE Center for Threat-Informed Defense | standard-setter | https://raw.githubusercontent.com/center-for-threat-informed-defense/tram/main/README.md | 2026-10-17 | full |
| MITRE-TRAM-2023 | Threat Report ATT&CK Mapper (TRAM) | MITRE Center for Threat-Informed Defense | standard-setter | https://ctid.mitre.org/projects/threat-report-attck-mapper-tram/ | 2023-08-24 | full |
| ADOBE-CTRI-2026 | Building an agentic AI-powered threat intelligence platform | Adobe | firm | https://blog.adobe.com/security/building-an-agentic-ai-powered-threat-intelligence-platform | 2026-03-19 | full |
| ANTHROPIC-COOKBOOK-TI-2026 | Threat intelligence enrichment agent (Claude Cookbook) | Anthropic | vendor | https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent | 2026-04-07 | full |
| ANTHROPIC-TIR-2026 | Countering misuse of AI: September 2026 | Anthropic | vendor | https://www.anthropic.com/threat-intelligence-report-september-2026 | 2026-09-10 | full |
| CLOUDFLARE-BLOGINDEX-2026 | Posts tagged 'Cloudforce One' (index page) | Cloudflare | vendor | https://blog.cloudflare.com/tag/cloudforce-one/ | 2026-10-17 | full |
| CLOUDFLARE-CLOUDY-2025 | Automating threat analysis and response with Cloudy | Cloudflare | vendor | https://blog.cloudflare.com/automating-threat-analysis-and-response-with-cloudy/ | 2025-08-29 | full |
| CLOUDFLARE-THREATSIGNALS-2026 | Introducing Threat Signals: agentic skills for open-source threat intelligence, free for every Cloudflare account | Cloudflare | vendor | https://blog.cloudflare.com/threat-signals/ | 2026-09-29 | full |
| CRWD-CHARLOTTE-2026 | Charlotte AI: Agentic Analyst for Cybersecurity | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/platform/charlotte-ai/ | 2026-10-17 | full |
| CYBERPROOF-HUNTING-2026 | How agentic AI delivered continuous threat hunting for a transport giant | CyberProof | vendor | https://www.cyberproof.com/case-studies/agentic-ai-transportation/ | 2026-07 | full |
| EIQ-IC39-2026 | Intelligence Center 3.9: More AI provider choice, MITRE ATT&CK v19.1 support, and more | EclecticIQ | vendor | https://blog.eclecticiq.com/intelligence-center-3.9 | 2026-09-22 | full |
| GOOGLE-CISOPERSP-2026 | Cloud CISO Perspectives: How Google monitors AI threats and advances AI defenses | Google | vendor | https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-how-google-monitors-ai-threats-advances-ai-defenses | 2026-09-16 | full |
| GOOGLE-FORRESTERBLOG-2026 | Google named a Leader in the External Threat Intelligence Service Forrester Wave | Google | vendor | https://cloud.google.com/blog/products/identity-security/google-named-a-leader-in-the-external-threat-intelligence-service-forrester-wave | 2026-09-18 | full |
| GOOGLE-GTIAGENTIC-2026 | Agentic Platform (Google Threat Intelligence documentation) | Google | vendor | https://gtidocs.readme.io/docs/agentic-platform | 2026-09-24 | full |
| GOOGLE-GTICHANGELOG-2026 | August 12th, 2026 - Agentic Flows & API, and Threat Actor Naming Updates | Google | vendor | https://gtidocs.readme.io/changelog/august-5th-2026-agentic-flows-api-and-threat-actor-naming-updates | 2026-08-12 | full |
| GOOGLE-GTICHANGELOG2-2026 | September 10th, 2026 - Single Target Operations (GA), Google Insights, Agentic Updates, and Detection Highlights | Google | vendor | https://gtidocs.readme.io/changelog/september-10th-2026-single-target-operations-ga-google-insights-agentic-updates-and-detection-highlights | 2026-09-10 | full |
| GOOGLE-GTIFLOWS-2026 | Flows (Google Threat Intelligence documentation) | Google | vendor | https://gtidocs.readme.io/docs/flows-guide | 2026-07-31 | full |
| GOOGLE-GTILANDSCAPE-2026 | How Your Threat Landscape Uses AI Recommendations | Google | vendor | https://gtidocs.readme.io/docs/threat-landscape-ai-recommendations | 2026-02-27 | full |
| GOOGLE-GTIMCP-2026 | Agentic MCP Server Configuration (Google Threat Intelligence documentation) | Google | vendor | https://gtidocs.readme.io/docs/agentic-mcp-guide | 2026-09-16 | full |
| GOOGLE-GTIORGPROFILE-2026 | Organization Profile (Google Threat Intelligence documentation) | Google | vendor | https://gtidocs.readme.io/docs/my-landscape-organization-profile | 2026-06-16 | full |
| GOOGLE-GTIRELEVANCE-2026 | Getting Started with our new Dark Web Intel capabilities, powered by the relevance system | Google | vendor | https://gtidocs.readme.io/docs/dark-web-intel | 2026-06-22 | full |
| GTIG-AITRACKER-2026 | GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI | Google | vendor | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/ | 2026-09-08 | full |
| GTIG-VULNTRENDS-2026 | Vulnerability Discovery and Exploitation Trends in the AI Era | Google | vendor | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | full |
| MANDIANT-AIPHASES-2023 | AI and the Five Phases of the Threat Intelligence Lifecycle | Mandiant (Google Cloud Blog) | vendor | https://cloud.google.com/blog/topics/threat-intelligence/ai-five-phases-intelligence-lifecycle | 2023-08-24 | full |
| MANDIANT-AIVM-2026 | Demystifying AI Exploits: A Blueprint for AI-Assisted Vulnerability Management | Mandiant (Google Cloud Blog) | vendor | https://cloud.google.com/blog/topics/threat-intelligence/ai-assisted-vulnerability-management | 2026-07-16 | full |
| MSFT-AGENTSOVERVIEW-2026 | Microsoft Security Copilot agents overview | Microsoft | vendor | https://learn.microsoft.com/en-us/copilot/security/agents-overview | 2026-03-18 | full |
| MSFT-DEFENDERAGENTS-2026 | Deploy AI agents in Microsoft Defender | Microsoft | vendor | https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender | 2026-08-05 | full |
| MSFT-HUNTASSIST-2026 | Microsoft Security Copilot Threat Hunting Assistant in advanced hunting | Microsoft | vendor | https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-threat-hunting-assistant | 2026-09-10 | full |
| MSFT-MDTICOPILOT-2026 | Use Microsoft Security Copilot for threat intelligence | Microsoft | vendor | https://learn.microsoft.com/en-us/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence | 2026-08-02 | full |
| MSFT-TIBAGENT-2026 | Security Copilot Threat Intelligence Briefing Agent in Microsoft Defender | Microsoft | vendor | https://learn.microsoft.com/en-us/defender-xdr/threat-intel-briefing-agent-defender | 2026-07-02 | full |
| OPENCTI-COPILOT-2026 | Interactions using AI (chatbot) - CTI Copilot (OpenCTI documentation) | Filigran / OpenCTI | vendor | https://docs.opencti.io/latest/usage/copilot/ | 2026-08-27 | full |
| OPENCTI-IMPORTAI-2025 | On-premise AI extraction (OpenCTI documentation) | Filigran / OpenCTI | vendor | https://docs.opencti.io/latest/deployment/advanced/ai-import-document/ | 2025-04-11 | full |
| RF-AI-2026 | Streamline Security Workflows with AI | Recorded Future | vendor | https://www.recordedfuture.com/platform/ai | 2026-10-17 | full |
| RF-COWBELL-2026 | Cowbell Achieves 90% Cost Savings With Recorded Future | Recorded Future | vendor | https://www.recordedfuture.com/case-study/cowbell | 2026-09-30 | full |
| RF-PUBSECTOR-2026 | Public Sector Agency Collects Intelligence 95% Faster Using Recorded Future | Recorded Future | vendor | https://www.recordedfuture.com/case-study/public-sector-agency | 2026-09-29 | full |
| RF-SUPERHUMAN-2026 | How Superhuman Unlocked a New Era of AI-Driven Threat Intelligence With Recorded Future | Recorded Future | vendor | https://www.recordedfuture.com/case-study/superhuman | 2026-06-08 | full |
| ARXIV-2406.07599 | CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2406.07599 | 2024-06-11 | full |
| ARXIV-2509.23573 | Uncovering Vulnerabilities of LLM-Assisted Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2509.23573 | 2025-09-28 | full |
| ARXIV-2510.11974 | CTIConnect: A Benchmark for Retrieval-Augmented LLMs over Heterogeneous Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2510.11974 | 2025-10-13 | full |
| ARXIV-2511.01144 | AthenaBench: A Dynamic Benchmark for Evaluating LLMs in Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2511.01144 | 2025-11-03 | full |
| ARXIV-2602.17458 | The CTI Echo Chamber: Fragmentation, Overlap, and Vendor Specificity in Twenty Years of Cyber Threat Reporting | arXiv | academic | https://arxiv.org/abs/2602.17458 | 2026-02-19 | full |
| ARXIV-2603.09452 | CyberThreat-Eval: Can Large Language Models Automate Real-World Threat Research? | arXiv | academic | https://arxiv.org/abs/2603.09452 | 2026-03-10 | full |
| ARXIV-2603.13517 | CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities | arXiv | academic | https://arxiv.org/abs/2603.13517 | 2026-03-13 | full |
| ARXIV-2604.12228 | From IOCs to Regex: Automating CTI Operationalization for SOC with LLMs | arXiv | academic | https://arxiv.org/abs/2604.12228 | 2026-04-14 | full |
| ARXIV-2604.19533 | Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps | arXiv | academic | https://arxiv.org/abs/2604.19533 | 2026-04-21 | full |
| ARXIV-2605.20896 | GenAI-Driven Threat Detection with Microsoft Security Copilot | arXiv (Microsoft authors) | academic | https://arxiv.org/abs/2605.20896 | 2026-05-20 | full |
| ARXIV-2605.29269 | HunterAgent: Neuro-Symbolic Attack Trace Reconstruction under Anti-Forensics | arXiv | academic | https://arxiv.org/abs/2605.29269 | 2026-05-28 | full |
| ARXIV-2606.18166 | Evaluating Open-Source LLMs for Multi-Label ATT&CK Technique Classification on CTI Reports | arXiv | academic | https://arxiv.org/abs/2606.18166 | 2026-06-16 | full |
| ARXIV-2608.06778 | Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2608.06778 | 2026-08-07 | full |
| ARXIV-2608.19011 | From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation | arXiv | academic | https://arxiv.org/abs/2608.19011 | 2026-08-19 | full |
| ARXIV-2608.23185 | Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums | arXiv (Politecnico di Milano and BV TECH) | academic | https://arxiv.org/abs/2608.23185 | 2026-08-24 | full |
| ARXIV-2609.01174 | A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing | arXiv | academic | https://arxiv.org/abs/2609.01174 | 2026-09-01 | full |
| ARXIV-2609.07582 | Benchmarking LLMs for Threat Level Determination | arXiv | academic | https://arxiv.org/abs/2609.07582 | 2026-09-07 | full |
| ARXIV-2609.08790 | Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports | arXiv | academic | https://arxiv.org/abs/2609.08790 | 2026-09-08 | full |
| ARXIV-2610.20417 | From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2610.20417 | 2026-10-14 | full |
| FLASHPOINT-ENTERPRISETI-2026 | The Enterprise Threat Intelligence Report: 2026 | Flashpoint | survey | https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/ | 2026-10-13 | full |
| SANS-CTI-2026 | 91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (2026 SANS CTI Survey press release) | SANS Institute | survey | https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report | 2026-05-19 | full |
| CSD-ISACAI-2026 | ISACs confront AI's promise and peril for threat intelligence-sharing | Cybersecurity Dive | press | https://www.cybersecuritydive.com/news/ai-isacs-threat-intelligence-information-sharing-trust/815499/ | 2026-03-23 | full |
| NEXTGOV-AIISAC-2026 | AI info-sharing center is in development, CISA official says | Nextgov/FCW | press | https://www.nextgov.com/cybersecurity/2026/02/ai-info-sharing-center-development-cisa-official-says/411167 | 2026-02-03 | full |
| SECURITYARSENAL-RAPID7-2026 | AI-Driven Detection Engineering: Converting Threat Intel into Executable Hunt Plans | Security Arsenal | press | https://securityarsenal.com/blog/ai-driven-detection-engineering-converting-threat-intel-into-executable-hunt-plans | 2026-06-10 | full |
| HISAC-AIISAC-2026 | ISACs confront AI's promise and peril for threat intelligence-sharing (Health-ISAC media mention) | Health-ISAC | community | https://health-isac.org/isacs-confront-ais-promise-and-peril-for-threat-intelligence-sharing/ | 2026-03-27 | full |
| ANTHROPIC-JOBTCTI-2026 | Technical Cyber Threat Investigator (job posting) | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5066995008 | 2026-01-13 | full |
| ANTHROPIC-JOBTIE-2026 | Threat Intelligence Engineer (job posting) | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/5074937008 | 2026-01-20 | full |
| CLOUDFLARE-JOBSTIE-2026 | Senior Threat Intelligence Engineer (job posting) | Cloudflare | job-posting | https://boards.greenhouse.io/cloudflare/jobs/7558153 | 2026-01-22 | full |
| COINBASE-JOBSTIE-2026 | Senior Threat Intelligence Engineer (job posting) | Coinbase | job-posting | https://www.coinbase.com/careers/positions/8209803 | 2026-09-16 | full |
| COINBASE-JOBTIPE-2026 | Threat Intelligence Platform Engineer (job posting) | Coinbase | job-posting | https://www.coinbase.com/careers/positions/8177619 | 2026-09-03 | full |
| DRAGOS-JOBCTI-2026 | Associate Principal Cyber Threat Intelligence Analyst (job posting) | Dragos | job-posting | https://job-boards.greenhouse.io/dragos/jobs/5389909008 | 2026-08-27 | full |
| GITLAB-JOBTRE-2026 | Threat Research Engineer (job posting) | GitLab | job-posting | https://job-boards.greenhouse.io/gitlab/jobs/8867649002 | 2026-10-15 | full |
| HUNTRESS-JOBDETH-2026 | Senior Detection Engineering & Threat Hunting Analyst (job posting) | Huntress | job-posting | https://job-boards.greenhouse.io/huntress/jobs/7998321003 | 2026-09-23 | full |
| OPENAI-JOBII-2025 | Full-Stack Software Engineer, Intelligence & Investigations (job posting) | OpenAI | job-posting | https://jobs.ashbyhq.com/openai/52c72cb9-7c44-4cba-b440-e05262a38491 | 2025-11-12 | full |
| OPENAI-JOBTTI-2026 | Technical Threat Investigator, Threat Intel Engineering (job posting) | OpenAI | job-posting | https://jobs.ashbyhq.com/openai/f01b7084-a68d-4e30-ace9-6b5e6d90c517 | 2026-04-30 | full |
| RECORDEDFUTURE-JOBTIRA-2026 | Threat Intelligence Response Analyst (job posting) | Recorded Future | job-posting | https://job-boards.greenhouse.io/recordedfuture/jobs/8859088002 | 2026-10-02 | full |
| TWILIO-JOBSSETH-2026 | Staff Security Engineer, Threat Hunting (job posting) | Twilio | job-posting | https://job-boards.greenhouse.io/twilio/jobs/8157344 | 2026-09-04 | full |

## 6. Gaps

- **No independent evaluation of a deployed vendor CTI assistant or agent.** Every outcome figure for a named deployment comes from the vendor, the customer quoted by the vendor, or the deploying team's own paper. No source published analyst override rates, edit rates, error rates or a parallel run of AI against human output for CTI.
- **Gated or unreachable reports:** Mandiant M-Trends 2026, CrowdStrike Global Threat Report and Threat Hunting Report (page read, no AI-hunting data found), the IDC business-value study and the Forrester Wave report (only Google's landing page and blog were read), and Recorded Future's 2025 State of AI and Automation survey (landing page read; figures not recoverable).
- **Blocked sites:** Microsoft Security blog (403), ThreatConnect, Silobreaker, Dataminr and Cisco Talos (403), Flare's site (403), CISA's own AI pages (403; read through a text mirror, which renders 'AI' as 'SI' on DHS pages). GitHub APIs were not available; raw README files were.
- **Customer case studies are few.** Recorded Future's named case studies (Cowbell, Superhuman) were read; Panasonic (2025-10-28) and the others in its list were not examined for AI content. Several vendor case studies have anonymous customers (CyberProof's client, Recorded Future's public-sector agency).
- **Job postings:** read from public Greenhouse and Ashby boards of about 40 companies. Postings at security vendors on other systems (CrowdStrike, Google, Microsoft, Palo Alto Networks) and at banks and large enterprises with in-house CTI teams were not reached. Only 12 postings were read in full; no counts of AI mentions across postings were made.
- **ISAC and government practice is thin:** one panel report (Health-ISAC, RH-ISAC, FS-ISAC), no FS-ISAC or MS-ISAC AI program found, no AI-ISAC launch date. Only CISA's inventory was read; other agencies and bodies (NCSC, ENISA, Europol) were not covered.
- **Conference content:** FIRST 2026 abstracts only; slides and recordings were not read, and several sessions are TLP:AMBER. Black Hat, RSAC, mWISE and SANS summit sessions could not be extracted. The RH-ISAC 2024 session on LLMs in CTI appeared in search results but could not be opened, so it is not cited.
- **Rapid7's internal LLM hunt-plan pipeline** is known only through a third-party summary; Rapid7's own post was not found.
- **Cloudflare's agentic Managed Defense post (2026-10-07), Anthropic's September 2026 report beyond its introduction, and the landscape file's CTI-extraction benchmarks (SCRIPTIOC-BENCH, BEACON, STINER)** were not read.
- **Workforce data:** no published headcount, hiring or role-change data for CTI teams beyond SANS's team-size finding; no evidence on junior-analyst pipeline effects.
- **Real-world prompt injection against CTI pipelines** appears only as conference demonstrations and academic work, not as reported incidents.
- **Web search was used five times** (named customer case studies, ISAC/AI-ISAC news, in-house LLM pipelines, SANS CTI survey, threat-hunting case studies). Other discovery used vendor documentation indexes, RSS feeds, public job-board APIs and arXiv search.
