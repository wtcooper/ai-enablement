# Security operations (SOC): practice deep dive

Archetype: security. Module: operations. Angle: practice. Compiled 2026-10-17. Working files were kept in a private `mktemp -d` folder. Web search was used 5 times (Google triage agent, independent benchmarks, in-house SOC write-ups, detection-engineering deployments, Arctic Wolf launch). All other sources were opened with `curl`, `pdftotext`, the Greenhouse public job API or the `r.jina.ai` mirror.

## 1. Summary

- **What is real in production.** The best-documented in-house case is Elastic's own SOC ("Customer Zero"). It runs deterministic queries first, then narrow agents, and creates the case before an analyst opens it. It reports AI verdict correctness rising from 60% to 92% by changing the context given to agents, not the model (`ELASTIC-ACCURACY-2026`). Named MSSP and small-team deployments (ECS, Zapier, Mysten Labs) report large cuts in Tier-1 effort, but every figure comes from the AI vendor's own case study (`DROPZONE-ECS-2026`, `DROPZONE-ZAPIER-2026`, `DROPZONE-MYSTEN-2026`).
- **Adoption is wide but shallow.** SANS 2026: 79% of SOCs use AI or ML tools; 36% have integrated them into a defined workflow (`SANS-SOC-2026`).
- **Quality evidence is thin and mixed.** Independent or academic measurement shows the risk: in one benchmark every tool-using triage approach tested missed at least 40.4% of attack-related alerts (`ARXIV-2610.10608`), and a log-borne prompt-injection study shows the SOC's own AI is an attack surface (`ARXIV-2605.24421`). Vendor "bake-off" and parallel-run figures exist, but most customers are unnamed.
- **The supervision model is converging.** Agents prepare the work; people decide. High-confidence benign closure is automated; response actions that touch users, availability or executives stay with people (`CISCO-SPLUNK-CONF26-2026`, `EXPEL-3LEADERS-2026`, `MSFT-PHISHTRIAGE-2026`).
- **Work is being reorganised, not only sped up.** Job postings from Robinhood, Databricks, Cloudflare, Expel and Figma now ask for agentic-workflow and AI-coding experience from detection and response engineers. Robinhood advertises a "Security Operations AI Tech Lead" role (`ROBINHOOD-JOB-SECOPSAI-2026`).
- **MDR is repositioning.** Arctic Wolf, eSentire, Sophos, Expel and CrowdStrike Falcon Complete all describe AI-led, human-accountable services. Gartner's 2026 MDR Market Guide, as quoted by Expel, keeps "human-led" in the definition (`EXPEL-GARTNERMDR-2026`).

Use cases by grade: A = 7, B = 9, C = 4, D = 0 (20 total).

## 2. Use cases

```yaml
- id: security-operations-01
  title: In-house agentic triage pipeline that investigates every alert and builds the case before an analyst opens it
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, research-synthesis]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Manual investigation of each alert takes about half an hour; hiring more analysts does not scale with alert volume; long AI summaries that were wrong too often were ignored by analysts."
  solution: "A detection rule triggers a workflow. Deterministic ES|QL checks close obvious false positives at no token cost. A narrow Initial Triage agent returns a structured verdict; a high-confidence false positive is closed. Everything else becomes a case, specialised agents (endpoint, cloud, SaaS) investigate, and a Final Review agent writes the verdict to the case. Agents receive the rule's investigation guide, user context and 30 days of past cases with analyst closure reasons."
  outcomes:
    - { lever: quality, description: "AI verdict correctness rose after the team changed the context given to the agents; the team says it did not switch models", figure: "60% to 92%", measures: "AI verdict compared with the analyst's close reason on cases, tracked on a dashboard (denominator and period not stated)", provenance: self-reported, source_ref: ELASTIC-ACCURACY-2026 }
    - { lever: speed, description: "A 30-minute manual investigation now finishes in under 3 minutes", figure: "30 minutes to under 3 minutes", measures: "Elastic's stated manual investigation time vs pipeline time; sample size not stated", provenance: self-reported, source_ref: ELASTIC-AGENTICSOC1-2026 }
    - { lever: cost, description: "Cost to investigate a Windows endpoint alert with specialised workflow agents vs one agent with 14 skills", figure: "USD 0.69 vs USD 3.42 per alert", measures: "inference cost per investigation, from a parallel test across 36,822 Agent Builder conversations", provenance: self-reported, source_ref: ELASTIC-TOKENS-2026 }
  prerequisites:
    - "Detection rules carry investigation guides written by detection engineers, and rules are tagged by triage category"
    - "Case management where analysts must pick a closure reason, so AI verdicts can be scored against human outcomes"
    - "Context lookups: asset inventory, HR/user data, 30 days of past cases per rule"
    - "Inference routed only to providers with zero data retention (Elastic's stated choice)"
  risks_and_guardrails:
    - "Before the context changes, accuracy hovered around 60% and analysts stopped reading the AI summaries (ELASTIC-ACCURACY-2026, introduction)"
    - "Queries replace agents wherever a check is predictable, to avoid hallucination, prompt injection and cost (ELASTIC-AGENTICSOC1-2026, first-step section)"
    - "The Pattern Finder agent has no tools, so injected content cannot make it call out (ELASTIC-ACCURACY-2026, agent section)"
  human_checkpoints:
    - "Only high-confidence false positives are closed without an analyst (ELASTIC-AGENTICSOC1-2026, Initial Triage section)"
    - "Analysts confirm or override in Slack or the case, and must choose a closure reason; an optional 'AI Incorrect?' field feeds the tuning loop (ELASTIC-ACCURACY-2026)"
  role_evolution: "Detection engineers write investigation guides that serve both analysts and agents; analysts review a prepared case and their closure reasons become corrective context for the agents (ELASTIC-ACCURACY-2026)."
  evidence_grade: A
  sources:
    - { ref: ELASTIC-ACCURACY-2026, title: "Agentic SOC alert triage: 60% to 92% AI accuracy", publisher: Elastic Security Labs, type: vendor, url: "https://www.elastic.co/security-labs/alert-triage-agentic-soc-self-correcting-agents", date: 2026-08-25, access: full, locator: "Opening summary; 'Context enrichment sources'; feedback-loop section" }
    - { ref: ELASTIC-AGENTICSOC1-2026, title: "Alert triage in under 3 minutes with Elastic's agentic SOC", publisher: Elastic Security Labs, type: vendor, url: "https://www.elastic.co/security-labs/alert-triage-agentic-soc-elastic-workflows", date: 2026-07-02, access: full, locator: "Summary; Initial Triage agent section; case path" }
    - { ref: ELASTIC-TOKENS-2026, title: "Agentic SOC architecture: specialized agents cut costs 5.7x", publisher: Elastic Security Labs, type: vendor, url: "https://www.elastic.co/security-labs/agentic-soc-token-budget-architecture", date: 2026-07-24, access: full, locator: "Opening summary and cost table" }
  last_reviewed: 2026-10-17
  notes: "Elastic is both the vendor and the deploying SOC, so all figures are self-reported. Verdict correctness measures agreement with analysts, not independent ground truth. The 60% baseline is for the earlier set-up with no past-case context."

- id: security-operations-02
  title: Precedent retrieval that shows analysts how similar alerts were closed before
  archetype: security
  module: operations
  function: service-delivery
  work_types: [transaction-processing, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Many queue alerts look almost identical to cases already investigated and closed, but proving that meant digging through closed tickets, raw logs and several tools."
  solution: "Features of a new alert (name, vendor, severity, message, device or org context, narrative) are embedded and matched by similarity search against previously triaged alerts. The analyst sees a suggested read (benign, malicious, unknown), the nearest historical cases with their dispositions, and counterfactuals. Weak or unverified matches default to escalation."
  outcomes:
    - { lever: risk, description: "Safety gate intended to stop known true-positive patterns being called benign", figure: "under 1% suppressed true-positive rate", measures: "stated as a design property of the safety gate; no measured result published", provenance: self-reported, source_ref: EXPEL-PRECEDENT-2026 }
    - { lever: capacity, description: "Initiative target: overall queue reduction", figure: "10% or greater queue reduction with under 1% change in recall (target, not result)", measures: "Expel's stated target for the initiative; no result published", provenance: self-reported, source_ref: EXPEL-PRECEDENT-2026 }
  prerequisites:
    - "A store of previously triaged alerts with verified dispositions"
    - "Per-vendor calibrated similarity thresholds"
  risks_and_guardrails:
    - "Unverified history and weak matches default to escalation (EXPEL-PRECEDENT-2026, mechanism section)"
    - "Expel says analysts should not fall into 'trusting AI or accepting a historical disposition' (EXPEL-PRECEDENT-2026)"
  human_checkpoints:
    - "The analyst always makes the disposition (EXPEL-PRECEDENT-2026)"
  role_evolution: "Analysts spend less time hunting for past context; output also feeds Expel's rapid alert triage agent (EXPEL-PRECEDENT-2026)."
  evidence_grade: B
  sources:
    - { ref: EXPEL-PRECEDENT-2026, title: "New Ruxie AI power-up: Precedent engine turns repetitive alerts into faster decisions", publisher: Expel, type: vendor, url: "https://expel.com/blog/new-ruxie-ai-power-up-precedent-engine/", date: 2026-09-10, access: full, locator: "Mechanism and 'Higher signal, less noise' sections" }
  last_reviewed: 2026-10-17
  notes: "The post describes planned rollout phases (alert mutation to route repeat noise out of the primary queue), so parts are not yet live. No measured results."

- id: security-operations-03
  title: Agent triages user-reported phishing emails and closes the false alarms
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "User-reported suspicious emails arrive continuously; reviewing each one slows response and risks genuine threats being missed."
  solution: "When a user reports an email and an alert is created, an LLM-based agent assesses it (file and URL detonation, screenshot analysis, threat intelligence, advanced hunting), classifies it as real threat or false positive, and explains the verdict in natural language. False positives are resolved; true positives stay open for an analyst."
  outcomes:
    - { lever: capacity, description: "Valvoline's CISO says analysts reclaimed hours and containment actions became automatic after Torq's platform automated phishing triage; no figure given", figure: "none published", measures: "quote in a funding press release; no numerator or denominator", provenance: vendor-published, source_ref: TORQ-SERIESD-2026 }
  prerequisites:
    - "Security Copilot capacity (Security Compute Units), unified RBAC for Defender for Office 365, user-reported-message settings and the 'reported by user' alert policy turned on (MSFT-PHISHTRIAGE-2026, prerequisites)"
    - "Alert-tuning rules that auto-resolve the same alert must be disabled or the agent never sees it (MSFT-PHISHTRIAGE-2026)"
  risks_and_guardrails:
    - "Analyst feedback can teach the agent, but feedback is accepted once per alert and the lesson should be previewed before saving (MSFT-PHISHTRIAGE-2026, feedback section)"
    - "Microsoft extended the same agent to cloud and identity alerts, with those types in preview (MSFT-DEFENDER-AGENTS-2026)"
  human_checkpoints:
    - "True-positive incidents remain open for an analyst to investigate (MSFT-PHISHTRIAGE-2026)"
    - "Analysts can reject or reclassify the verdict and see the reasoning (MSFT-PHISHTRIAGE-2026)"
  role_evolution: "Analysts shift from reading each reported email to filtering the queue for confirmed threats and teaching the agent through plain-language feedback (MSFT-PHISHTRIAGE-2026)."
  evidence_grade: B
  sources:
    - { ref: MSFT-PHISHTRIAGE-2026, title: "Microsoft Security Copilot Phishing Triage Agent in Microsoft Defender", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent", date: 2026-07-02, access: full, locator: "Overview; prerequisites; feedback sections (page metadata ms.date; updated 2026-08-11)" }
    - { ref: MSFT-DEFENDER-AGENTS-2026, title: "Deploy AI agents in Microsoft Defender", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender", date: 2026-05-12, access: full, locator: "Security Alert Triage Agent section (page metadata ms.date; updated 2026-08-07)" }
    - { ref: TORQ-SERIESD-2026, title: "Torq Secures $140M Series D at $1.2B Valuation to Lead the AI SOC and Agentic AI Era", publisher: Torq, type: vendor, url: "https://torq.io/news/torq-seriesD/", date: 2026-01-12, access: full, locator: "Valvoline CISO quote" }
  last_reviewed: 2026-10-17
  notes: "Microsoft's page says the agent has 'demonstrated measurable improvements' but gives no figures. No customer is named on the Microsoft pages; Valvoline is a Torq customer, not necessarily a user of Microsoft's agent. The two sources describe different products with the same pattern."

- id: security-operations-04
  title: MSSP uses an AI SOC analyst to investigate every Tier-1 alert and auto-close the benign majority
  archetype: security
  module: operations
  function: service-delivery
  work_types: [transaction-processing, research-synthesis]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Alert volume grew faster than analyst headcount; most alerts were benign; human triage varied by shift and experience; SOAR could enrich but could not reason through investigations or safely auto-close."
  solution: "Alerts flow from detection platforms through SOAR into an AI SOC analyst for autonomous investigation; outcomes are written back into ServiceNow for case management and audit."
  outcomes:
    - { lever: capacity, description: "Share of Tier-1 alerts closed automatically", figure: "70%", measures: "'Tier 1 alerts automatically closed' of alerts handled; denominator and period not stated", provenance: vendor-published, source_ref: DROPZONE-ECS-2026 }
    - { lever: capacity, description: "Alert handling scaled past the previous ceiling without adding headcount", figure: "about 30,000 alerts per month", measures: "alerts per month the SOC processed before the tool", provenance: vendor-published, source_ref: DROPZONE-ECS-2026 }
    - { lever: speed, description: "Every alert investigated on creation instead of waiting in a queue", figure: "100% of alerts investigated immediately", measures: "stated in the case study; no timing distribution given", provenance: vendor-published, source_ref: DROPZONE-ECS-2026 }
  prerequisites:
    - "Structured proof of value on real production alerts, benchmarking against existing tools and human triage"
    - "SOAR and ServiceNow integration; an Elastic integration was built during the engagement"
  risks_and_guardrails:
    - "ECS says it did not intend to replace analysts and needed standardised, auditable triage (DROPZONE-ECS-2026, challenge section)"
  human_checkpoints:
    - "Analysts handle what is not auto-closed; outcomes land in the case system for audit (DROPZONE-ECS-2026)"
  role_evolution: "Senior staff move to threat hunting, detection engineering and SOC improvement; the case study also reports less burnout (DROPZONE-ECS-2026)."
  evidence_grade: A
  sources:
    - { ref: DROPZONE-ECS-2026, title: "How ECS Broke the SOC Scalability Ceiling with AI SOC Agents", publisher: Dropzone AI, type: vendor, url: "https://www.dropzone.ai/case-studies/how-ecs-broke-the-soc-scalability-ceiling-with-ai-soc-agents", date: 2026-05-01, access: full, locator: "Challenges, solution and results sections (date is the site's sitemap last-modified; the page shows no publication date)" }
  last_reviewed: 2026-10-17
  notes: "Vendor-authored case study with a named customer; no accuracy or false-negative figure. A second, unnamed 'leading European MSSP' case study by the same vendor reports a proof of concept with investigation accuracy of 'approximately 90 to 95 percent' on Microsoft Defender and Sentinel alerts and says it improved margins by allowing more customers without proportional staffing (DROPZONE-EUMSSP-2026, 2026-05-27); treat as a vendor claim."

- id: security-operations-05
  title: Lean detection and response team offloads alert investigation to an AI SOC analyst
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "A team 'you could count on one hand' faced 50-100+ daily investigations, mostly false positives, and alert triage consumed whole sprints that should have gone to detections and hardening."
  solution: "The AI analyst investigates each alert across Okta, AWS, Google Workspace and Panther, pushes enriched investigations into Panther, can interview users over Slack, and takes environment details through a context memory (for example flagging travelling users)."
  outcomes:
    - { lever: speed, description: "Average time to triage an alert", figure: "10-15 minutes to under 2 minutes (stated as 85% faster)", measures: "average investigation time per alert as stated by Zapier's detection and response team; sample size not stated", provenance: vendor-published, source_ref: DROPZONE-ZAPIER-2026 }
    - { lever: capacity, description: "Daily investigations needing attention", figure: "50-100+ daily investigations reduced to 'only the handful' needing attention", measures: "no count given for the handful", provenance: vendor-published, source_ref: DROPZONE-ZAPIER-2026 }
  prerequisites:
    - "Integrations with identity, cloud, workspace and SIEM; deployment completed in two days per the case study"
    - "Analysts add business context (for example travel) to context memory"
  risks_and_guardrails:
    - "Analysts can see every query and each piece of evidence, which Zapier cites as the basis for trust (DROPZONE-ZAPIER-2026)"
  human_checkpoints:
    - "Analysts act on the handful of alerts that are surfaced; a missing AI comment on an alert is treated as a signal (DROPZONE-ZAPIER-2026)"
  role_evolution: "Engineers spend time on detections, observability and maturity projects; GRC staff self-serve audit evidence through a question feature (DROPZONE-ZAPIER-2026)."
  evidence_grade: A
  sources:
    - { ref: DROPZONE-ZAPIER-2026, title: "How Zapier Cut Manual Alert Investigation by 85% With Dropzone AI", publisher: Dropzone AI, type: vendor, url: "https://www.dropzone.ai/case-studies/how-zapier-cut-manual-alert-investigation-by-85-with-dropzone-ai", date: 2026-01-28, access: full, locator: "Results section (date is the site's sitemap last-modified; the page shows no publication date)" }
  last_reviewed: 2026-10-17
  notes: "Vendor-authored. No false-negative or override rate."

- id: security-operations-06
  title: "A SOCless model: AI investigates all alerts and senior engineers are paged only for serious events"
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, expert-judgment]
  pattern: intake-triage
  ladder: automate
  change_scope: model
  runtime_class: background-agent
  maturity: in-production
  problem: "A small, all-senior engineering team targeted by state-sponsored attackers was swamped by thousands of monthly alerts, mostly false positives, from detections built like observability."
  solution: "All alert types (endpoint, identity, cloud, email, network) go to an AI SOC analyst; results are pushed back into the SIEM and on-call engineers are paged for serious events. There are no dedicated security analysts."
  outcomes:
    - { lever: capacity, description: "Alerts needing human review per month", figure: "thousands reduced to fewer than 20 (stated as 99% reduction)", measures: "monthly alerts needing human review, as stated by the company", provenance: vendor-published, source_ref: DROPZONE-MYSTEN-2026 }
    - { lever: speed, description: "Time engineers spend on one alert", figure: "30-60 minutes to roughly 1 minute", measures: "per-alert engineer time as stated; sample size not stated", provenance: vendor-published, source_ref: DROPZONE-MYSTEN-2026 }
  prerequisites:
    - "Custom strategies that tell the system what is irrelevant and what matters; deployment finished in a day per the case study"
    - "Engineers who know the systems and accept on-call paging"
  risks_and_guardrails:
    - "Very low risk tolerance is the stated reason for tuning strategies and escalating only what humans need to review (DROPZONE-MYSTEN-2026)"
  human_checkpoints:
    - "On-call engineers are paged for serious events (DROPZONE-MYSTEN-2026)"
  role_evolution: "Alerts route to IT and application engineers instead of a SOC tier; the head of security frames operations as site-reliability engineering (DROPZONE-MYSTEN-2026)."
  evidence_grade: A
  sources:
    - { ref: DROPZONE-MYSTEN-2026, title: "How Mysten Labs Eliminated Toil and Scaled Security With Dropzone AI", publisher: Dropzone AI, type: vendor, url: "https://www.dropzone.ai/case-studies/how-mysten-labs-eliminated-toil-and-scaled-security-with-dropzone-ai", date: 2026-01-28, access: full, locator: "Results section (date is the site's sitemap last-modified; the page shows no publication date)" }
  last_reviewed: 2026-10-17
  notes: "Vendor-authored. A very small, all-staff-level team; likely not typical. The page reports no missed-threat check."

- id: security-operations-07
  title: Triage agent embedded in the SIEM investigates alerts as they fire
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Analysts pivot manually across data to decide whether each alert is real."
  solution: "Google's Triage and Investigation agent runs automatically (default: five minutes after the alert, to let events arrive) or on demand. It uses dynamic searches, threat-intelligence enrichment of indicators, command-line analysis and process-tree reconstruction, then gives a true or false positive verdict with a written explanation."
  outcomes:
    - { lever: speed, description: "Google says a typical 30-minute manual analysis falls to about 60 seconds", figure: "30 minutes to about 60 seconds; more than 5 million alerts investigated", measures: "Google's figures as reported by TechInformed from a Google Cloud post of 10 June 2026; no baseline method or false-positive rate given", provenance: vendor-published, source_ref: TECHINFORMED-GOOGLE-2026 }
  prerequisites:
    - "Data in Google SecOps SIEM; single-tenant or MSSP set-up with one SOAR tenant (GOOGLE-TIN-2026)"
  risks_and_guardrails:
    - "Each investigation averages 60 seconds and runs at most 20 minutes; there is no queue, and alerts above the limit are not analysed automatically (GOOGLE-TIN-2026, 'Trigger TIN')"
    - "The trade press notes the post gives no false-positive rates, customer ranges or human-approval criteria for containment (TECHINFORMED-GOOGLE-2026)"
  human_checkpoints:
    - "Analysts decide on closure and remediation; Google says analysts keep control of 'critical, high-impact actions' (TECHINFORMED-GOOGLE-2026)"
  role_evolution: "Not described in the sources read."
  evidence_grade: C
  sources:
    - { ref: GOOGLE-TIN-2026, title: "Triage alerts with the Triage Agent", publisher: Google Cloud documentation, type: vendor, url: "https://docs.cloud.google.com/chronicle/docs/secops/triage-agent", date: 2026-10-13, access: full, locator: "Overview, 'Trigger TIN' and auto-investigation settings (page footer 'Last updated 2026-10-13')" }
    - { ref: TECHINFORMED-GOOGLE-2026, title: "Google's SOC agent cuts alert review from 30 minutes to 60 seconds", publisher: TechInformed, type: press, url: "https://techinformed.com/googles-soc-agent-cuts-alert-review-from-30-minutes-to-60-seconds/", date: 2026-06-16, access: full, locator: "Opening paragraphs and closing 'boundaries' paragraph" }
  last_reviewed: 2026-10-17
  notes: "Search results also mention a BBVA testimonial; that detail was seen only in search results and is not used. The product has had a trial in 2026 per search results (search-only)."

- id: security-operations-08
  title: Live event SOC runs an AI triage agent with analysts validating each recommendation
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "A temporary, noisy conference network has short baselines and unmanaged devices, so activity that is alarming on a corporate network can be normal there."
  solution: "The Splunk Enterprise Security AI Triage Agent investigates findings as they appear in the analyst queue and gives a suggested disposition, rationale and next steps before a human takes ownership. A blended Tier 1, 2, 3 and detection-engineering team validates; a dashboard tracks agent activity, confidence and hand-offs."
  outcomes:
    - { lever: capacity, description: "Triage analysis coverage shown on the operations dashboard over the whole conference including set-up days", figure: "94% triage analysis coverage", measures: "'Triage analysis coverage' on the dashboard snapshot; the post does not define numerator and denominator, and says these are event-environment observations, not product benchmarks", provenance: vendor-published, source_ref: CISCO-SPLUNK-CONF26-2026 }
    - { lever: capacity, description: "Agent activity counts", figure: "1,503 AI events; 7,605 SPL queries; 26,207 pieces of evidence; 11,250 threat-intelligence lookups", measures: "activity counts, not accuracy", provenance: vendor-published, source_ref: CISCO-SPLUNK-CONF26-2026 }
  prerequisites:
    - "A single evidence platform (detections, risk, investigations, searches) so analysts can inspect what the agent used"
    - "Packet capture and identity/endpoint telemetry for validation"
  risks_and_guardrails:
    - "RSAC 2026 SOC authors say they were 'not operating a fully agentic SOC'; AI is decision support, humans keep response decisions (SPLUNK-RSACSOC-2026)"
    - "A cleartext-credential workflow was automated with a SOAR playbook (deterministic), saving more than nine analyst hours (SPLUNK-RSACSOC-2026)"
  human_checkpoints:
    - "Analysts decide whether a finding is closed, escalated, investigated further or acted on (CISCO-SPLUNK-CONF26-2026)"
  role_evolution: "Cisco Live 2026 'built the first Agentic SOC for a major Cisco event'; analysts began from a structured incident narrative instead of assembling context by hand (SPLUNK-CISCOLIVE-2026)."
  evidence_grade: B
  sources:
    - { ref: CISCO-SPLUNK-CONF26-2026, title: "Splunk .conf26: Tracking the Triage Agent in the Agentic SOC", publisher: Cisco Blogs, type: vendor, url: "https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/", date: 2026-10-08, access: full, locator: "'Building the Triage Agent Dashboard' and 'Dashboard Snapshot' table" }
    - { ref: SPLUNK-RSACSOC-2026, title: "From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC", publisher: Splunk, type: vendor, url: "https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html", date: 2026-08-24, access: full, locator: "Opening section and cleartext-credential example" }
    - { ref: SPLUNK-CISCOLIVE-2026, title: "Machine Speed, Human Judgment: Inside the Cisco Live Agentic SOC", publisher: Splunk, type: vendor, url: "https://www.splunk.com/en_us/blog/security/inside-the-cisco-live-agentic-soc.html", date: 2026-08-31, access: full, locator: "Opening paragraphs; analyst-training paragraph" }
  last_reviewed: 2026-10-17
  notes: "The dashboard also shows suggested dispositions (True Positive 44%, Benign Positive 42%, False Positive 6%, No suggestion 7%, Undetermined 1%) and average-confidence bands, but there is no comparison with analyst verdicts, so accuracy is unknown. The landscape file dated the RSAC SOC post to Mar 2026; the page shows 2026-08-24."

- id: security-operations-09
  title: Agent-written investigation narratives help junior analysts work above their experience level
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis, expert-judgment]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "New analysts spend their first hours or months learning where tools live and how to assemble context."
  solution: "Analysts start from an agent-prepared incident narrative, supporting evidence and recommended next steps; at one customer, junior analysts learned from the agent's visible investigation reasoning."
  outcomes:
    - { lever: capacity, description: "Cisco Live reports that more than a dozen new analysts were trained and operated at Tier 2 level with agentic support", figure: "more than a dozen new analysts", measures: "count of newly trained analysts at one event SOC; no performance measure", provenance: vendor-published, source_ref: SPLUNK-CISCOLIVE-2026 }
    - { lever: speed, description: "Cabinetworks says ramp-up for junior analysts fell from months to weeks", figure: "months to weeks (no figures)", measures: "customer's stated ramp-up time; no numbers or sample", provenance: vendor-published, source_ref: PROPHET-CABINET-2026 }
  prerequisites:
    - "Agent reasoning that is visible to the analyst"
  risks_and_guardrails:
    - "Not discussed in either source"
  human_checkpoints:
    - "Analysts validate and decide (SPLUNK-CISCOLIVE-2026)"
  role_evolution: "Ramp-up to Tier-2 work is shortened; Prophet's case study calls the agent's reasoning a 'master class in investigative thinking' (PROPHET-CABINET-2026)."
  evidence_grade: B
  sources:
    - { ref: SPLUNK-CISCOLIVE-2026, title: "Machine Speed, Human Judgment: Inside the Cisco Live Agentic SOC", publisher: Splunk, type: vendor, url: "https://www.splunk.com/en_us/blog/security/inside-the-cisco-live-agentic-soc.html", date: 2026-08-31, access: full, locator: "Paragraph beginning 'The SOC trained more than a dozen new analysts'" }
    - { ref: PROPHET-CABINET-2026, title: "Cabinetworks: Revolutionizing SOC efficiency with Prophet AI", publisher: Prophet Security, type: vendor, url: "https://www.prophetsecurity.ai/case-studies/cabinetworks-revolutionizing-soc-efficiency-with-prophet-ai", date: 2026-04-30, access: full, locator: "Benefits section (date is the site's sitemap last-modified; the page shows no publication date)" }
  last_reviewed: 2026-10-17
  notes: "Qualitative and vendor-authored. The Cabinetworks page also reports alert queue 'from thousands to dozens', over 1,000 investigations resolved in Q1 2025, and SIEM spend down by over 90% because the agent queries native systems; those are vendor-authored and not used as outcomes."

- id: security-operations-10
  title: MDR provider moves to an agent-led, human-accountable service model
  archetype: security
  module: operations
  function: service-delivery
  work_types: [transaction-processing, client-interaction]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Alerts are investigated in tiers one after another, so attackers move while cases wait; providers also cap what they will investigate."
  solution: "MDR providers describe swarms or teams of specialist agents (triage, investigation, response) with oversight or judge agents and a route to human experts when confidence is low. Arctic Wolf calls its model 'AI-led with humans in the loop'; Expel says Ruxie triages and enriches before an analyst touches an alert while analysts make consequential calls; eSentire and Sophos describe agentic AI under human accountability."
  outcomes:
    - { lever: speed, description: "Arctic Wolf says businesses can resolve cases 15x faster while keeping an average of one customer ticket per day", figure: "15x faster", measures: "baseline and sample not stated in the article", provenance: vendor-published, source_ref: CIO-ARCTICWOLF-2026 }
    - { lever: speed, description: "Expel states a 14-minute mean time to remediate on fully automated high and critical incidents", figure: "14 minutes", measures: "Expel's MTTR on 'fully automated high and critical incidents'; period and count not stated", provenance: self-reported, source_ref: EXPEL-GARTNERMDR-2026 }
  prerequisites:
    - "A body of historical cases and analyst validations to build agent context (Arctic Wolf says more than 1,000 analysts validated its data and workflows)"
  risks_and_guardrails:
    - "Arctic Wolf routes low-confidence work to a human and a 'Swarm Judge' validates decisions; it says it deploys an agent only after it beats existing workflows in its own SOC (CIO-ARCTICWOLF-2026)"
    - "Gartner's 2026 MDR guide, as quoted by Expel, says buyers should demand clarity on which services are AI-augmented and which still rely on analysts (EXPEL-GARTNERMDR-2026)"
  human_checkpoints:
    - "Human experts take over work outside an agent's validated experience (CIO-ARCTICWOLF-2026)"
    - "Gartner's quoted definition keeps MDR 'human-led' (EXPEL-GARTNERMDR-2026)"
  role_evolution: "Tiered hand-offs are replaced by parallel agent work; analysts validate and supervise. Expel's guidance, citing Gartner, also expects 90% of initial MDR findings to be handled by AI without human action by 2029 (see frontier signals)."
  evidence_grade: C
  sources:
    - { ref: CIO-ARCTICWOLF-2026, title: "Inside Arctic Wolf's new agentic security platform", publisher: CIO.com, type: press, url: "https://www.cio.com/article/4211089/inside-arctic-wolfs-new-agentic-security-platform.html", date: 2026-08-26, access: full, locator: "Paragraphs on Swarm of Experts, validation framework and '15x faster'" }
    - { ref: EXPEL-GARTNERMDR-2026, title: "AI-augmented, still human-led: What changed in the 2026 Gartner Market Guide for Managed Detection and Response", publisher: Expel, type: vendor, url: "https://expel.com/blog/what-changed-in-the-2026-gartner-market-guide-for-managed-detection-and-response/", date: 2026-09-21, access: full, locator: "Opening paragraphs; footnote naming the Gartner report of 9 September 2026" }
    - { ref: ESENTIRE-2026, title: "Managed Detection and Response Services & Security Operations Platform", publisher: eSentire, type: vendor, url: "https://www.esentire.com/", date: 2026-05-07, access: full, locator: "Home page 'Controlled Autonomy SecOps' paragraph (page modified date)" }
    - { ref: SOPHOS-MDR-2026, title: "Sophos MDR | 24/7 Managed Detection & Response | Agentic SOC", publisher: Sophos, type: vendor, url: "https://www.sophos.com/en-us/products/managed-detection-and-response", date: 2026-10-17, access: full, locator: "Product page text read through the text mirror; no publication date on page, date shown is retrieval date" }
  last_reviewed: 2026-10-17
  notes: "All performance claims come from the providers. The CIO.com article reads like vendor-supplied material (no independent data). Launch date for Arctic Wolf's Aurora Agentic SOC (RSAC, 2026-03-23) was seen only in search results (search-only). Arctic Wolf's home page says 'fewer than 5 percent of security teams have agentic capabilities today' without a source; not used as a figure."

- id: security-operations-11
  title: SOC teams build their own agents in a no-code workspace
  archetype: security
  module: operations
  function: technology-it
  work_types: [software-systems, transaction-processing]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Each SOC has its own playbooks, asset criticality and escalation paths; that institutional knowledge is lost to turnover, and generic automation does not capture it."
  solution: "Analysts encode playbooks and SOPs into agents on CrowdStrike Charlotte AI AgentWorks using plain language, choosing models per task. Named examples: a Detection Analyzer Agent at Pan-American Life Insurance Group that produces structured investigation reports with ATT&CK mapping; a Detection Engineering Agent at Kroll; teams at Pegasystems, American Express Global Business Travel, Americas Styrenics and Infios."
  outcomes:
    - { lever: speed, description: "One analyst reports building the same agent in four minutes in AgentWorks vs six to eight hours in Microsoft Copilot", figure: "6-8 hours vs 4 minutes", measures: "one unnamed analyst's comparison of build time, as quoted by the vendor", provenance: vendor-published, source_ref: CROWDSTRIKE-AGENTWORKS-2026 }
  prerequisites:
    - "Telemetry on the vendor's platform; knowledge bases of playbooks, SOPs and environment context"
  risks_and_guardrails:
    - "Agents are bounded in action scope, versioned, governed by role policies, cost-capped and traceable; teams benchmark agent versions against fixed datasets before promotion (CROWDSTRIKE-AGENTWORKS-2026, governance section)"
    - "CrowdStrike lists three reasons agentic SOC efforts fail: fragmented data, isolated agents giving late or wrong verdicts, and ungoverned automation (CROWDSTRIKE-AGSOC-2026)"
  human_checkpoints:
    - "For each workflow, teams set what is fully automated and what requires approval (CROWDSTRIKE-AGSOC-2026, unified agentic SOAR workspace)"
  role_evolution: "Senior analysts encode their knowledge into agents (Americas Styrenics quote); the Pan-American Life engineer says the hard part is deciding which problem to solve first (CROWDSTRIKE-AGENTWORKS-2026)."
  evidence_grade: B
  sources:
    - { ref: CROWDSTRIKE-AGENTWORKS-2026, title: "How AI-leading Security Teams Are Building the Agentic SOC", publisher: CrowdStrike, type: vendor, url: "https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/", date: 2026-07-06, access: full, locator: "Customer examples list; governance paragraph (date is the page's modified timestamp)" }
    - { ref: CROWDSTRIKE-AGSOC-2026, title: "CrowdStrike Delivers the Next Evolution of the Agentic SOC", publisher: CrowdStrike, type: vendor, url: "https://www.crowdstrike.com/en-us/blog/crowdstrike-delivers-next-evolution-of-agentic-soc/", date: 2026-09-18, access: full, locator: "'Updated September 18, 2026' note; three reasons; unified agentic SOAR workspace (public preview)" }
  last_reviewed: 2026-10-17
  notes: "Customer statements are quoted by the vendor and give no outcome figures. Several features in the 2026-09-18 post are labelled pre-beta or public preview."

- id: security-operations-12
  title: Agent drafts the investigation report and case write-up for analyst sign-off
  archetype: security
  module: operations
  function: technology-it
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Analysts write structured reports for technical and non-technical readers after gathering evidence across tools."
  solution: "At Pan-American Life, a Detection Analyzer Agent produces structured investigation reports with ATT&CK mapping, with technical readouts for SOC and IR analysts and plain-language summaries for others. Elastic's Final Review agent writes the verdict to the case; Expel's Ruxie writes plain-language incident reports that humans review and sign off before they are final."
  outcomes:
    - { lever: speed, description: "Pan-American Life says reporting that once took hours now arrives automatically", figure: "none published", measures: "qualitative statement; no time figures", provenance: vendor-published, source_ref: CROWDSTRIKE-AGENTWORKS-2026 }
  prerequisites:
    - "Evidence already attached to the case; a report template or structure"
  risks_and_guardrails:
    - "Elastic found its earlier long AI summaries inaccurate 40% of the time and analysts ignored them; report quality depends on verdict accuracy (ELASTIC-ACCURACY-2026)"
  human_checkpoints:
    - "Humans review and sign off before incident reports are final (EXPEL-RUXIE-2026)"
  role_evolution: "Analysts review and edit instead of authoring from scratch."
  evidence_grade: B
  sources:
    - { ref: CROWDSTRIKE-AGENTWORKS-2026, title: "How AI-leading Security Teams Are Building the Agentic SOC", publisher: CrowdStrike, type: vendor, url: "https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/", date: 2026-07-06, access: full, locator: "Customer examples list, first bullet" }
    - { ref: EXPEL-RUXIE-2026, title: "Ruxie, Expel's AI for cybersecurity", publisher: Expel, type: vendor, url: "https://expel.com/ai-automation/", date: 2026-10-14, access: full, locator: "Incident report paragraph (page modified date; first published 2025-07-31)" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: CoAnalyst: An AI-Driven Framework for Enhanced SOC Triage (Cisco CSIRT)", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06-16, access: full, locator: "Session abstract, 16 June 2026" }
  last_reviewed: 2026-10-17
  notes: "The Cisco CoAnalyst abstract says the framework combines LLMs with historical incident data and existing tools and promises 'substantial reductions in manual effort', with no figures; it is a conference abstract, so no outcome is recorded."

- id: security-operations-13
  title: Multi-agent detection-rule generation with a separate judge model and human code review
  archetype: security
  module: operations
  function: technology-it
  work_types: [software-systems, expert-judgment]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Turning each new high-severity CVE into a validated detection rule meant an analyst finding proof-of-concept exploit code, writing the rule, tuning against traffic logs and waiting for peer review, so coverage had to be prioritised."
  solution: "RuleForge ingests and scores public exploit code, runs parallel rule-generation agents, uses a separate judge model to score sensitivity and specificity, validates rules on synthetic and real traffic logs, and sends the best candidate to human code review."
  outcomes:
    - { lever: speed, description: "Rules produced and validated faster than manually over the last four months of 2025 after confidence scoring was deployed in August 2025", figure: "336% faster", measures: "Amazon's productivity comparison against manual rule creation over four months; the article does not define the unit", provenance: self-reported, source_ref: AMAZON-RULEFORGE-2026 }
    - { lever: quality, description: "A dedicated judge model reduced false positives while keeping the same number of true positives", figure: "67% fewer false positives", measures: "false positives from candidate rules with judge vs without, as stated by Amazon; test size not stated", provenance: self-reported, source_ref: AMAZON-RULEFORGE-2026 }
  prerequisites:
    - "A corpus of exploit proofs of concept, real traffic logs for validation, and detection rules in a reviewable format"
  risks_and_guardrails:
    - "The generation model rated almost all its own rules as good, so generation was separated from evaluation (AMAZON-RULEFORGE-2026)"
    - "Asking the judge for the probability a rule fails improved calibration over asking if it succeeds (AMAZON-RULEFORGE-2026)"
  human_checkpoints:
    - "A security engineer reviews the best rule; human judgment is the final gate before production (AMAZON-RULEFORGE-2026)"
  role_evolution: "Analyst focus shifts from authoring to review (AMAZON-RULEFORGE-2026)."
  evidence_grade: A
  sources:
    - { ref: AMAZON-RULEFORGE-2026, title: "How Amazon uses agentic AI for vulnerability detection at global scale", publisher: Amazon Science, type: vendor, url: "https://www.amazon.science/blog/how-amazon-uses-agentic-ai-for-vulnerability-detection-at-global-scale", date: 2026-04-08, access: full, locator: "Key points; 'Multistage validation'; results paragraph on the August 2025 deployment" }
  last_reviewed: 2026-10-17
  notes: "Scope is CVE-exploit detection rules written in Amazon's JSON format for its honeypot and detection systems, not general SIEM detection content. Adjacent to vulnerability-exposure; kept here as detection engineering."

- id: security-operations-14
  title: Agent translates detections across SIEMs and finds coverage gaps
  archetype: security
  module: operations
  function: technology-it
  work_types: [software-systems]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Detection libraries must keep pace with threats and be moved between query languages when platforms change."
  solution: "Kroll's Detection Engineering Agent identifies coverage gaps, translates SIEM logic from Splunk, Sentinel and Elastic into CrowdStrike Query Language and validates new detections in real time. Google previews a Detection Engineering agent that turns exploitation patterns into custom detections and validates them with synthetic events."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "no figures in either source", provenance: vendor-published, source_ref: CROWDSTRIKE-AGENTWORKS-2026 }
  prerequisites:
    - "Existing detection library and a target query language; synthetic event testing"
  risks_and_guardrails:
    - "Google's agent validates rules with synthetic events before an exploit reaches the environment (TECHINFORMED-GOOGLE-2026)"
  human_checkpoints:
    - "Not stated for the Kroll agent. Panel members at Expel's webinar keep detection engineering and remediation in the human column (EXPEL-3LEADERS-2026)"
  role_evolution: "Detection engineers move toward reviewing and validating generated content."
  evidence_grade: B
  sources:
    - { ref: CROWDSTRIKE-AGENTWORKS-2026, title: "How AI-leading Security Teams Are Building the Agentic SOC", publisher: CrowdStrike, type: vendor, url: "https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/", date: 2026-07-06, access: full, locator: "Customer examples list, Kroll bullet" }
    - { ref: TECHINFORMED-GOOGLE-2026, title: "Google's SOC agent cuts alert review from 30 minutes to 60 seconds", publisher: TechInformed, type: press, url: "https://techinformed.com/googles-soc-agent-cuts-alert-review-from-30-minutes-to-60-seconds/", date: 2026-06-16, access: full, locator: "Paragraph on the Detection Engineering agent (preview)" }
    - { ref: EXPEL-3LEADERS-2026, title: "Why three security leaders still won't let AI make the call", publisher: Expel, type: vendor, url: "https://expel.com/blog/why-three-security-leaders-still-wont-let-ai-make-the-call/", date: 2026-10-02, access: full, locator: "McIntyre quote on detection engineering and remediation" }
  last_reviewed: 2026-10-17
  notes: "Maturity set to piloting because the named Kroll example is stated without scale and Google's agent is in preview. Expel says Ruxie 'autonomously writes new detection rules' for gaps (EXPEL-RUXIE-2026), a vendor claim not verified."

- id: security-operations-15
  title: Analyst copilot for investigation queries and incident summaries
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Analysts take time to gather and read incident information from many sources before they can resolve an incident."
  solution: "A copilot built into the XDR portal aggregates incident information and presents it in human-readable form; analysts use it for natural-language queries and summaries."
  outcomes:
    - { lever: speed, description: "Adoption of Microsoft Security Copilot was associated with lower mean time to resolution three months after adoption, compared with a control group", figure: "30.13% reduction", measures: "difference-in-differences on incident mean time to resolution (first opened by an analyst to marked resolved), Defender XDR metadata from over 150 organizations across 180 days in 2024; association, not causal", provenance: vendor-published, source_ref: MSFT-BONO-2024 }
  prerequisites:
    - "Copilot licensing and an XDR deployment"
  risks_and_guardrails:
    - "The authors say selection into treatment prevents causal identification (MSFT-BONO-2024, abstract)"
    - "Swimlane's SOC leader says summarisation, log analysis and report writing are the easy wins; harder tasks need context and runbooks (SANS-AI-2026)"
  human_checkpoints:
    - "Analyst remains the decision-maker; the tool serves information"
  role_evolution: "Not described."
  evidence_grade: A
  sources:
    - { ref: MSFT-BONO-2024, title: "Generative AI and Security Operations Center Productivity: Evidence from Live Operations", publisher: arXiv (Microsoft authors), type: academic, url: "https://arxiv.org/abs/2411.03116", date: 2024-11-05, access: full, locator: "Abstract; data and method section" }
    - { ref: SANS-AI-2026, title: "A SOC Leader's Guide to the 2026 SANS AI Survey", publisher: Swimlane, type: vendor, url: "https://swimlane.com/blog/sans-ai-2026-soc-trust/", date: 2026-05-18, access: full, locator: "Paragraph on low-hanging fruit" }
  last_reviewed: 2026-10-17
  notes: "Older than the 12-18 month window (November 2024) and about an assistant, not an agent. Authors are Microsoft employees and the product is Microsoft's, so it is not independent. It is the largest live-operations measurement found for this module."

- id: security-operations-16
  title: Agent prepares the investigation, analyst makes the call (measured in controlled tests)
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis, expert-judgment]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: "Manual investigations are slow, vary by analyst and degrade as analysts tire."
  solution: "Analysts receive an agent's evidence gathering and report and decide on the verdict. Two controlled or comparative studies measured the effect: a Cloud Security Alliance benchmark with an AI investigation platform and a university SOC study of a locally deployed ReAct agent."
  outcomes:
    - { lever: speed, description: "AI-assisted analysts completed investigations faster than manual analysts in two scenarios", figure: "45-61% faster (58 vs 105 minutes; 30 vs 78 minutes)", measures: "investigation time in two simulated scenarios (AWS and Microsoft Entra ID alerts); participants randomly assigned to AI-assisted or manual groups (148 participants in total)", provenance: vendor-published, source_ref: DROPZONE-CSA148-2026 }
    - { lever: quality, description: "Accuracy of investigations in the same two scenarios", figure: "68% to 97% and 63% to 85% (CSA summary: 22-29% higher accuracy)", measures: "accuracy as scored in the study; the CSA summary does not say whether 22-29% are percentage points", provenance: vendor-published, source_ref: CSA-BENCH-2025 }
    - { lever: speed, description: "AI-assisted triage reduced ticket completion time in a university SOC", figure: "about 40%", measures: "average ticket completion time over 8 real tickets, each handled once manually and once with the agent, by the researchers who built it", provenance: independent, source_ref: NDSS-WOSOC-2026 }
  prerequisites:
    - "Integrated access to SIEM, enrichment and OSINT tools; in the university study the agent ran locally so data did not leave the network"
  risks_and_guardrails:
    - "The CSA study was commissioned by the vendor and covers analysts using the tool for the first time in simulated scenarios (DROPZONE-CSA148-2026)"
    - "The university study used only eight tickets, researchers familiar with the system, and notes over-reliance on alert metadata in one failure case (NDSS-WOSOC-2026, evaluation and limitations)"
  human_checkpoints:
    - "Agent output is reviewed by human analysts; analysts can prompt the agent with more context (NDSS-WOSOC-2026)"
  role_evolution: "In the CSA study, 94% of participants said their view of AI in cybersecurity became more positive after hands-on use (CSA-BENCH-2025)."
  evidence_grade: B
  sources:
    - { ref: CSA-BENCH-2025, title: "Beyond the Hype: A Benchmark Study of AI Agents in the SOC", publisher: Cloud Security Alliance, type: professional-body, url: "https://cloudsecurityalliance.org/artifacts/a-benchmark-study-of-ai-agents-in-the-soc", date: 2025, access: full, locator: "Abstract on the publication page (full report not opened; year taken from the vendor's description of it as a 2025 study)" }
    - { ref: DROPZONE-CSA148-2026, title: "AI SOC Agents: What 148 Analysts Think (2026 CSA Study)", publisher: Dropzone AI, type: vendor, url: "https://www.dropzone.ai/blog/soc-analysts-ai-perception-148-study", date: 2026-05-15, access: full, locator: "Study summary and results tables" }
    - { ref: NDSS-WOSOC-2026, title: "Experiences of Using Agentic AI to Fill Tooling Gaps in a Security Operations Center", publisher: NDSS Symposium (WOSOC 2026), type: academic, url: "https://www.ndss-symposium.org/wp-content/uploads/wosoc26-02.pdf", date: 2026-02-23, access: full, locator: "Abstract; Table I; limitations paragraph" }
  last_reviewed: 2026-10-17
  notes: "Maturity is piloting because both studies are tests, not production use. The numbers for time and accuracy are from the vendor blog describing the CSA study; the CSA page gives only the ranges. Grade capped at B because scenarios were simulated or small."

- id: security-operations-17
  title: Guardrailed containment and response actions proposed by agents
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Investigation is faster with agents, but response actions such as blocking, killing a process or isolating a host can cause harm if the agent is wrong or manipulated."
  solution: "Google previews agentic containment that pairs agents (evidence and reasoning) with deterministic playbooks that keep high-impact actions under analyst control. A research design confines the agent to a closed vocabulary of intents with templated commands and an argument validator, behind a guardrails proxy. A Torq customer (Valvoline) says containment actions became automatic."
  outcomes:
    - { lever: risk, description: "In the research design, the stock guardrails proxy raised injection recall at a fixed false-positive rate on a SOC-specific adversarial corpus", figure: "25.0% to 94.5% recall at 0.1% false positives", measures: "prompt-injection recall on the authors' released adversarial corpus; not a production measurement", provenance: independent, source_ref: ARXIV-2610.09906 }
  prerequisites:
    - "Deterministic playbooks for the action itself; closed intent vocabulary and argument validation"
  risks_and_guardrails:
    - "A single adversarial alert can become a path to executing an action through the model's reasoning (ARXIV-2610.09906, abstract)"
    - "Measured rail latency keeps inline control out of scope; the authors suggest human-in-the-loop or delayed operation (ARXIV-2610.09906)"
    - "Expel's panel: leaders treat context, executives and production changes as human-decided, but a routine 3am account lockout with guardrails might be automated (EXPEL-3LEADERS-2026)"
  human_checkpoints:
    - "High-impact actions stay under analyst control (TECHINFORMED-GOOGLE-2026)"
  role_evolution: "Analysts write the authorisation rules for what an agent may do alone; Expel's panel prefers a human 'over the loop' watching the process."
  evidence_grade: C
  sources:
    - { ref: TECHINFORMED-GOOGLE-2026, title: "Google's SOC agent cuts alert review from 30 minutes to 60 seconds", publisher: TechInformed, type: press, url: "https://techinformed.com/googles-soc-agent-cuts-alert-review-from-30-minutes-to-60-seconds/", date: 2026-06-16, access: full, locator: "Paragraph on agentic containment and response (preview)" }
    - { ref: ARXIV-2610.09906, title: "Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2610.09906", date: 2026-10-07, access: full, locator: "Abstract" }
    - { ref: EXPEL-3LEADERS-2026, title: "Why three security leaders still won't let AI make the call", publisher: Expel, type: vendor, url: "https://expel.com/blog/why-three-security-leaders-still-wont-let-ai-make-the-call/", date: 2026-10-02, access: full, locator: "Trust-versus-impact discussion" }
    - { ref: TORQ-SERIESD-2026, title: "Torq Secures $140M Series D at $1.2B Valuation to Lead the AI SOC and Agentic AI Era", publisher: Torq, type: vendor, url: "https://torq.io/news/torq-seriesD/", date: 2026-01-12, access: full, locator: "Valvoline CISO quote" }
  last_reviewed: 2026-10-17
  notes: "Evidence is a preview product, a research design and one customer quote. The ARXIV-2610.09906 authors say the OT fit is architectural, not a measured OT deployment."

- id: security-operations-18
  title: Continuous scoring of AI verdicts against analyst outcomes, and parallel-run bake-offs before delegating
  archetype: security
  module: operations
  function: technology-it
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Vendors give clean accuracy figures; teams need evidence on their own alerts, especially for false negatives."
  solution: "Teams record the AI verdict and the analyst's closure reason on each case and chart agreement on a dashboard (Elastic), run proofs of value on real production alerts against existing tools and human triage (ECS), run side-by-side bake-offs (an unnamed UnderDefense customer), benchmark agent versions on fixed datasets before promotion (CrowdStrike), or replay incidents in benchmarks (AWS SIR-Bench, ALERT-BENCH)."
  outcomes:
    - { lever: quality, description: "AI verdict agreement with analyst close reasons, tracked over time", figure: "60% to 92%", measures: "AI verdict compared with analyst close reason on cases", provenance: self-reported, source_ref: ELASTIC-ACCURACY-2026 }
    - { lever: risk, description: "In an independent benchmark, every tool-using triage approach tested missed attack alerts; a structured multi-agent design cut misses", figure: "at least 40.4% of attack-related alerts missed by every approach; 3.1% false-negative rate for the authors' AIDA design, escalating 18.4% of alerts", measures: "1,247 alerts from one multi-stage attack scenario replayed through a live SIEM; five approaches studied", provenance: independent, source_ref: ARXIV-2610.10608 }
  prerequisites:
    - "Analyst closure reasons captured as structured fields; a replayable set of alerts with ground truth for benchmarks"
  risks_and_guardrails:
    - "In ALERT-BENCH, attack alerts were more likely to be dismissed when searches returned no records, and same-context self-review had negative net correction (ARXIV-2610.10608, abstract)"
    - "UnderDefense reports an unnamed customer bake-off of 12,000 investigations over two weeks with 99.3% agreement with the in-house SOC team; this is the vendor's own operating evidence and the customer is unnamed (UNDERDEFENSE-AISOC-2026)"
    - "Gartner's 2026 Hype Cycle, as summarised by Dropzone, warns of 'AI washing' and 'agent washing' and advises piloting against your own baseline (DROPZONE-GARTNERHC-2026)"
  human_checkpoints:
    - "Analysts' closure reasons are treated as truth in Elastic's prompts"
  role_evolution: "Detection engineers and automation teams own the measurement dashboards and tune prompts or context from override data (ELASTIC-ACCURACY-2026)."
  evidence_grade: A
  sources:
    - { ref: ELASTIC-ACCURACY-2026, title: "Agentic SOC alert triage: 60% to 92% AI accuracy", publisher: Elastic Security Labs, type: vendor, url: "https://www.elastic.co/security-labs/alert-triage-agentic-soc-self-correcting-agents", date: 2026-08-25, access: full, locator: "Data paragraph and 'AI Incorrect?' field explanation" }
    - { ref: ARXIV-2610.10608, title: "From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2610.10608", date: 2026-10-07, access: full, locator: "Abstract" }
    - { ref: UNDERDEFENSE-AISOC-2026, title: "AI SOC in 500 Real Incidents: Where It Still Asks for a Human", publisher: UnderDefense, type: vendor, url: "https://underdefense.com/blog/ai-soc-real-incidents/", date: 2026-07-06, access: full, locator: "Bake-off paragraphs" }
    - { ref: DROPZONE-GARTNERHC-2026, title: "The 2026 Gartner Hype Cycle for Security Operations", publisher: Dropzone AI, type: vendor, url: "https://www.dropzone.ai/blog/gartner-hype-cycle-security-operations-2026", date: 2026-06-16, access: full, locator: "'AI washing' section; footnote naming the Gartner report of 5 June 2026" }
  last_reviewed: 2026-10-17
  notes: "The benchmark result is independent but is a single scenario, not production. The 95% auto-close and 99.3% agreement figures are vendor operating claims. AWS authors also published SIR-Bench (794 test cases from 129 incident patterns; their agent reached 97.1% true-positive detection and 73.4% false-positive rejection), which is vendor-authored (AWS-SIRBENCH-2026)."

- id: security-operations-19
  title: SOC and detection engineers use coding agents and LLMs to build automation, detections and agents
  archetype: security
  module: operations
  function: technology-it
  work_types: [software-systems]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Detection and response work needs custom automation, queries and pipelines; teams are small and the backlog is long."
  solution: "Job postings now ask detection and response engineers to use AI coding tools as a normal part of work, and some ask for experience building agentic SOC workflows. Examples: Expel (Claude Code via MCP as 'a first-class part of how you work'); Databricks incident response (contributing to automation and agentic capabilities; experience with AI coding tools); Robinhood (agentic AI workflows for SecOps; an AI-native detection platform); Cloudflare's managed defense center (experience using agentic AI or LLMs to optimise operations, preferred); Figma (used AI-powered tools to automate SecOps workflows); Anthropic (ML-powered detection and Claude-based security operations)."
  outcomes:
    - { lever: capacity, description: "none published", figure: "none published", measures: "job postings describe requirements, not outcomes", provenance: self-reported, source_ref: EXPEL-JOB-DR-2026 }
  prerequisites:
    - "Engineers with scripting skills and API access to SIEM, SOAR and case systems"
  risks_and_guardrails:
    - "Not stated in the postings. Cloudflare's posting lists agentic AI experience as 'preferred'"
  human_checkpoints:
    - "Not stated"
  role_evolution: "Detection and response roles are becoming engineering roles; Robinhood advertises a Senior Staff role as 'Security Operations AI Tech Lead' to own an AI roadmap and 'build a synthetic workforce' (ROBINHOOD-JOB-SECOPSAI-2026)."
  evidence_grade: B
  sources:
    - { ref: EXPEL-JOB-DR-2026, title: "Senior Detection & Response Engineer", publisher: Expel (Greenhouse job board), type: job-posting, url: "https://expel.com/about/career-listing/8836996002", date: 2026-09-26, access: full, locator: "Requirements list (first published date from the job API)" }
    - { ref: DATABRICKS-JOB-IR-2026, title: "Staff Security Engineer, Incident Response", publisher: Databricks (Greenhouse job board), type: job-posting, url: "https://databricks.com/company/careers/open-positions/job?gh_jid=8841960002", date: 2026-10-08, access: full, locator: "Role description and requirements" }
    - { ref: ROBINHOOD-JOB-DR-2026, title: "Senior Security Engineer, Detection & Response", publisher: Robinhood (Greenhouse job board), type: job-posting, url: "https://boards.greenhouse.io/robinhood/jobs/8202863", date: 2026-09-21, access: full, locator: "Role description; AI Experience section" }
    - { ref: ROBINHOOD-JOB-SECOPSAI-2026, title: "Senior Staff Security Engineer, Security Operations", publisher: Robinhood (Greenhouse job board), type: job-posting, url: "https://boards.greenhouse.io/robinhood/jobs/8259431", date: 2026-10-06, access: full, locator: "Responsibilities (Security Operations AI Tech Lead)" }
    - { ref: CLOUDFLARE-JOB-CMDC-2026, title: "Response Engineer - Cloudflare Managed Defense Center (CMDC)", publisher: Cloudflare (Greenhouse job board), type: job-posting, url: "https://boards.greenhouse.io/cloudflare/jobs/8222732", date: 2026-09-24, access: full, locator: "Preferred qualifications" }
    - { ref: FIGMA-JOB-SECOPS-2026, title: "Manager, Security Operations", publisher: Figma (Greenhouse job board), type: job-posting, url: "https://boards.greenhouse.io/figma/jobs/6015609004", date: 2026-06-05, access: full, locator: "Qualifications" }
    - { ref: ANTHROPIC-JOB-DRPLATFORM-2026, title: "Security Software Engineer, Detection & Response Platform", publisher: Anthropic (Greenhouse job board), type: job-posting, url: "https://job-boards.greenhouse.io/anthropic/jobs/4595463008", date: 2025-03-24, access: full, locator: "Role summary (first published 2025-03-24; updated 2026-08-24)" }
  last_reviewed: 2026-10-17
  notes: "Evidence is hiring intent, so grade B is the ceiling and confidence is moderate. Dates are first-published dates from the Greenhouse API; the postings were open on 2026-10-17 at retrieval. Anthropic develops the model used to write this report; its posting is included as one data point among six. Two Tines postings for a Senior Security Operations Engineer contained text addressed to AI agents telling them not to apply; that text was not acted on and is not evidence."

- id: security-operations-20
  title: Always-on agent finds detection gaps and false negatives by correlating alerts and intelligence
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis, software-systems]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Rules miss activity that no single alert flags, so false negatives go unseen."
  solution: "Microsoft documents a Dynamic Threat Detection Agent in the Defender portal: an always-on backend service that uses AI to correlate alerts, events, anomalies and threat intelligence, and raises a dynamic alert with a natural-language explanation, mapped ATT&CK techniques and remediation steps."
  outcomes:
    - { lever: quality, description: "none published", figure: "none published", measures: "documentation only", provenance: vendor-published, source_ref: MSFT-DEFENDER-AGENTS-2026 }
  prerequisites:
    - "Defender and Microsoft Sentinel environments"
  risks_and_guardrails:
    - "No guardrail or accuracy information in the section read"
  human_checkpoints:
    - "Analysts receive the generated alert; handling is not described in the section read"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: MSFT-DEFENDER-AGENTS-2026, title: "Deploy AI agents in Microsoft Defender", publisher: Microsoft Learn, type: vendor, url: "https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender", date: 2026-05-12, access: full, locator: "Dynamic Threat Detection Agent section (page metadata ms.date; updated 2026-08-07)" }
  last_reviewed: 2026-10-17
  notes: "Maturity set to announced because the documentation does not show use or scale. CrowdStrike also describes detection running inside the data pipeline (pre-beta, 2026-09-18, CROWDSTRIKE-AGSOC-2026)."
```

## 3. Module notes

### Processes and key steps (work types)

- **Detection engineering**: threat or CVE input, rule authoring, testing against logs, peer review, deployment, tuning. Work types: software-systems, expert-judgment. AI role seen: rule generation with a judge model and code review (`AMAZON-RULEFORGE-2026`); rule translation and gap finding (`CROWDSTRIKE-AGENTWORKS-2026`).
- **Alert intake and triage**: alert fires, enrich with user, asset and threat intelligence, decide benign or escalate. Work types: transaction-processing. Largest area of AI deployment (use cases 01-07).
- **Investigation**: pivot across SIEM, EDR, identity and cloud logs; build a timeline and verdict. Work types: research-synthesis, expert-judgment.
- **Case management and documentation**: create the case, attach evidence, write the report, close with a reason. Work types: document-production, coordination-scheduling. AI writes drafts; closure reasons double as training signal (`ELASTIC-ACCURACY-2026`).
- **Response and containment**: block, isolate, reset. Work types: transaction-processing, expert-judgment. Mostly kept under human control (`EXPEL-3LEADERS-2026`).
- **MDR service delivery**: 24/7 monitoring, customer communication, tickets. Work types: client-interaction (`EXPEL-GARTNERMDR-2026`).
- **SOC measurement and engineering**: metrics, dashboards, SOAR and agent configuration. Work types: data-reporting, software-systems.

### Common pain points

- Alert volume and false positives. A Dropzone article citing ACM Computing Surveys gives an average of 2,992 alerts a day, with 63% unaddressed (vendor-cited secondary figure; the survey was not opened) (`DROPZONE-CSA148-2026`).
- Context spread across tools and lost when analysts leave (`DROPZONE-EUMSSP-2026`, `NDSS-WOSOC-2026`).
- Variable triage between analysts and shifts (`DROPZONE-ECS-2026`).
- Staffing: only 32% say management prioritises SOC hiring and retention, though skilled-staff shortage is the top challenge (`SANS-SOC-2026`).
- Measurement: 70% of SOC respondents still cite number of incidents handled as the top metric (`SANS-SOC-2026`).

### Metrics and benchmarks

| Metric | Value | What it measures | Source | Provenance |
|---|---|---|---|---|
| SOCs using AI or ML tools | 79% | share of SOC respondents (survey of 444 practitioners and 69 cyber leaders) | `SANS-SOC-2026` | independent survey, sponsor-funded |
| SOCs with AI in a defined workflow | 36% | share who have integrated AI/ML into a defined workflow | `SANS-SOC-2026` | independent survey |
| Shortcomings in AI detection or response | 63% | respondents reporting significant shortcomings; Swimlane reads the other 37% as trusting AI (inference) | `SANS-AI-2026` | vendor summary of survey |
| Automated incident response adoption | 39% | adoption in 2026 SANS AI survey | `SANS-AI-2026` | vendor summary of survey |
| AI verdict correctness | 60% to 92% | AI verdict vs analyst close reason | `ELASTIC-ACCURACY-2026` | self-reported |
| Per-alert investigation cost | USD 0.69 vs 3.42 | specialised workflow vs single 14-skill agent | `ELASTIC-TOKENS-2026` | self-reported |
| Missed attack alerts | at least 40.4% for all five approaches | 1,247 alerts, one scenario | `ARXIV-2610.10608` | independent (academic) |
| Triage-agent F1 | 0.958 (AIDA design) vs 0.371-0.744 | same benchmark | `ARXIV-2610.10608` | independent (academic) |
| Log-borne injection success | 26.6% average with naive prompting; 11.8% with the strongest defence; 96% for context manipulation in summarisation without defences | one model (gpt-4o-mini) and a 48-combination test | `ARXIV-2605.24421` | independent (academic) |
| Time to resolve (copilot) | 30.13% lower | adoption vs control, observational | `MSFT-BONO-2024` | vendor-authored |
| Controlled investigation speed and accuracy | 45-61% faster; 68% to 97% and 63% to 85% accuracy | 148 participants, simulated scenarios | `DROPZONE-CSA148-2026`, `CSA-BENCH-2025` | vendor-commissioned |
| Amazon rule production | 336% faster | vs manual rule creation | `AMAZON-RULEFORGE-2026` | self-reported |
| Independent production measurement of false negatives or override rates | none found | | | |

### Guardrails and regulatory points

- No regulator source was read for this module. Governance is handled in the sibling module brief; the points below are what practice sources show.
- Agent identity and permission scoping: Microsoft lets admins give an agent its own Entra Agent ID or run it with the user's credentials (`MSFT-DEFENDER-AGENTS-2026` and the overview page it links). CrowdStrike lists bounded scope, versioning, role-based policy, cost caps and decision trails (`CROWDSTRIKE-AGENTWORKS-2026`).
- Conservative auto-closure: high-confidence false positives only (`ELASTIC-AGENTICSOC1-2026`); weak matches escalate (`EXPEL-PRECEDENT-2026`); low confidence goes to a human (`CIO-ARCTICWOLF-2026`).
- Treat logs as hostile input: attacker-controlled log fields can carry instructions to the analyst model (`ARXIV-2605.24421`); a FIRST 2026 session demonstrates poisoned artifacts biasing retrieval in SOC LLM workflows (`FIRST-CON-2026`, session "One Poisoned Artifact Can Steer Your AI", abstract only).
- Data handling: Elastic routes inference only to zero-data-retention providers; a university SOC ran its agent locally (`ELASTIC-AGENTICSOC1-2026`, `NDSS-WOSOC-2026`).
- Gartner (as relayed by vendors) warns of AI and agent washing and asks MDR buyers to demand clarity on what is AI-augmented (`DROPZONE-GARTNERHC-2026`, `EXPEL-GARTNERMDR-2026`).

### Frontier signals (dated, sourced)

- 2026-06-05 (Gartner Hype Cycle for Security Operations, as summarised 2026-06-16): AI SOC agents sit at the Peak of Inflated Expectations, with maturity "Embryonic" and 1-5% market penetration; AI assistants slide toward disillusionment (`DROPZONE-GARTNERHC-2026`).
- 2026-09-09 (Gartner Market Guide for MDR, quoted 2026-09-21): predicts that by 2029 90% of initial MDR findings will be processed and addressed with AI support and no human action, up from 30% today; definition now reads "AI-augmented, human-led" (`EXPEL-GARTNERMDR-2026`).
- 2026-06 (Google): triage agent generally available; Detection Engineering and Threat Hunting agents and agentic containment in preview (`TECHINFORMED-GOOGLE-2026`).
- 2026-09-18 (CrowdStrike): orchestrator and specialist agents with shared context in pre-beta; detection in the data pipeline in pre-beta (`CROWDSTRIKE-AGSOC-2026`).
- 2026 (Microsoft): triage agent extended from phishing to cloud and identity alerts in preview (`MSFT-DEFENDER-AGENTS-2026`).
- 2026-07 to 2026-08 (Elastic): cost-engineered agent design (deterministic first, narrow agents) as an operating discipline (`ELASTIC-TOKENS-2026`).
- 2026-01-12 (Torq): USD 140M Series D for an AI SOC platform, a funding signal (`TORQ-SERIESD-2026`).
- 2026-06 (FIRST): sessions on Tier-1 triage with general-purpose LLMs and controlled experiments with hidden threat campaigns (`FIRST-CON-2026`).

### Workforce and role effects

- ISC2 (2025-12-04): AI is the top skills need (41%) ahead of cloud (36%); roles such as SOC analyst and incident responder are "evolving"; professionals expect new roles to emerge rather than job loss (`ISC2-WORKFORCE-2025`; 41% is the share of respondents citing AI as the most pressing skills need, on the ISC2 page).
- Role shift in postings: detection and response engineers asked to build agents and use AI coding tools (`ROBINHOOD-JOB-DR-2026`, `EXPEL-JOB-DR-2026`, `DATABRICKS-JOB-IR-2026`); a dedicated AI Tech Lead for SecOps (`ROBINHOOD-JOB-SECOPSAI-2026`).
- Vendor-imagined future roles (not evidence of practice): Dropzone describes a "SOC Agent Engineer" and an "AI SOC Operator" owning agent configuration and authorisation policy by 2030 (`DROPZONE-JD2030-2026`).
- Ramp-up and tier shifts: juniors working at Tier-2 level with agent support (`SPLUNK-CISCOLIVE-2026`); engineers on call instead of analysts (`DROPZONE-MYSTEN-2026`).
- Team size: no source reports headcount reduction; ECS, Zapier and the European MSSP describe avoiding hiring, not cutting staff (`DROPZONE-ECS-2026`, `DROPZONE-ZAPIER-2026`).

### Objections and concerns raised by practitioners

- Accountability: "You want a human to be able to own that mistake" (Expel CEO summarising the panel). An AI cannot explain itself to a regulator or defend a decision (`EXPEL-3LEADERS-2026`).
- Vendor opacity: one panelist's security vendor automation deleted cloud accounts and the vendor struggled to explain it (`EXPEL-3LEADERS-2026`).
- Cost: Expel's CEO said many companies find AI "more expensive than the people" once licensing, training and tokens are counted (`EXPEL-3LEADERS-2026`).
- Trust and hallucination: a ZoomInfo leader contrasts decades of not trusting SOC staff with trusting a computer that is "known to hallucinate" (`EXPEL-3LEADERS-2026`).
- Missed attacks: false negatives are the worst case for an AI SOC agent (`DROPZONE-GARTNERHC-2026`); the benchmark above shows high miss rates (`ARXIV-2610.10608`).
- Low-signal summaries: Elastic analysts stopped reading AI summaries that were wrong too often (`ELASTIC-ACCURACY-2026`).
- Agent washing: Gartner's Hype Cycle warns four times about GenAI, AI and agent washing, per Dropzone's summary (`DROPZONE-GARTNERHC-2026`).

### Interview probes for an advisor

1. Which alert types does AI close with no analyst today, and what evidence (agreement with analyst close reasons, parallel run, sampled review) justified that? Who reviews the closed set for misses?
2. Show the last month's analyst overrides of AI verdicts. What did the team change as a result: the model, the context, the rule guide?
3. What can an agent do on its own (lock an account, isolate a host), what needs approval, and who wrote that authorisation policy? Does it differ for executives and production systems?
4. If you buy MDR, which parts of the service are AI-run and which analyst-run, and can you see the actions in the provider's console? How has the contract changed?
5. How has the work of your detection engineers and Tier-1 analysts changed in the last year? Who owns agent configuration, prompts and the measurement dashboard?

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| Threat hunting agents (Microsoft Threat Hunting Assistant; CrowdStrike Agentic Recon; Google Threat Hunting agent in preview; Dropzone AI Threat Hunter) | threat-intelligence | `MSFT-DEFENDER-AGENTS-2026`, `CROWDSTRIKE-AGSOC-2026`, `TECHINFORMED-GOOGLE-2026` |
| Threat Intelligence Briefing Agent (Microsoft) | threat-intelligence | `MSFT-DEFENDER-AGENTS-2026` |
| AI-assisted living timelines in hybrid cloud on OCSF (Centene); StealerLens LLM forensics (Flare); DFIR agents | incident-response | `FIRST-CON-2026` |
| Vulnerability remediation prioritisation agents (regional health system, German municipality) | vulnerability-exposure | `CROWDSTRIKE-AGENTWORKS-2026` |
| Hierarchical agentic incident response research (digital-twin validated) | incident-response | landscape `ARXIV-2608.15016` (title only, not opened) |
| Prompt injection into SOC models via logs; poisoned artifacts; DFIR agent manipulation | ai-security-threats (x-ai-security) | `ARXIV-2605.24421`, `FIRST-CON-2026` |
| Agent identities and scoped credentials for SOC agents | ai-security-agent-identity-containment | `MSFT-DEFENDER-AGENTS-2026` |
| Economics: MSSP margin effects, cost per investigation, AI costing more than people | x-economics-business-model | `DROPZONE-EUMSSP-2026`, `ELASTIC-TOKENS-2026`, `EXPEL-3LEADERS-2026` |
| Workforce and role changes, SOC analyst job descriptions | x-workforce-talent | `ISC2-WORKFORCE-2025`, `DROPZONE-JD2030-2026` |
| Gartner's views on "AI-augmented, human-led" MDR and agent washing | x-state-of-ai-disruption | `EXPEL-GARTNERMDR-2026`, `DROPZONE-GARTNERHC-2026` |

## 5. Sources

Type counts (distinct refs, 62 total, including 1 search-only): vendor 29, academic 10, job-posting 7, press 2, professional-body 2, conference 1, survey 1. Access: 61 full, 1 search-only.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| SANS-SOC-2026 | SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense | SANS Institute | survey | https://www.sans.org/research/security-operations-report | 2026 (month not shown on page) | full (landing page; report body not opened) |
| SANS-AI-2026 | A SOC Leader's Guide to the 2026 SANS AI Survey | Swimlane | vendor | https://swimlane.com/blog/sans-ai-2026-soc-trust/ | 2026-05-18 | full (SANS AI survey itself not opened) |
| CISCO-SPLUNK-CONF26-2026 | Splunk .conf26: Tracking the Triage Agent in the Agentic SOC | Cisco Blogs | vendor | https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/ | 2026-10-08 | full |
| SPLUNK-RSACSOC-2026 | From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC | Splunk | vendor | https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html | 2026-08-24 | full |
| SPLUNK-CISCOLIVE-2026 | Machine Speed, Human Judgment: Inside the Cisco Live Agentic SOC | Splunk | vendor | https://www.splunk.com/en_us/blog/security/inside-the-cisco-live-agentic-soc.html | 2026-08-31 | full |
| CROWDSTRIKE-AGSOC-2026 | CrowdStrike Delivers the Next Evolution of the Agentic SOC | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/crowdstrike-delivers-next-evolution-of-agentic-soc/ | 2026-09-18 (updated) | full |
| CROWDSTRIKE-AGENTWORKS-2026 | How AI-leading Security Teams Are Building the Agentic SOC | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/ | 2026-07-06 | full |
| DROPZONE-CSA148-2026 | AI SOC Agents: What 148 Analysts Think (2026 CSA Study) | Dropzone AI | vendor | https://www.dropzone.ai/blog/soc-analysts-ai-perception-148-study | 2026-05-15 | full |
| CSA-BENCH-2025 | Beyond the Hype: A Benchmark Study of AI Agents in the SOC | Cloud Security Alliance | professional-body | https://cloudsecurityalliance.org/artifacts/a-benchmark-study-of-ai-agents-in-the-soc | 2025 | full (summary page) |
| DROPZONE-ECS-2026 | How ECS Broke the SOC Scalability Ceiling with AI SOC Agents | Dropzone AI | vendor | https://www.dropzone.ai/case-studies/how-ecs-broke-the-soc-scalability-ceiling-with-ai-soc-agents | 2026-05-01 (sitemap last-modified) | full |
| DROPZONE-ZAPIER-2026 | How Zapier Cut Manual Alert Investigation by 85% With Dropzone AI | Dropzone AI | vendor | https://www.dropzone.ai/case-studies/how-zapier-cut-manual-alert-investigation-by-85-with-dropzone-ai | 2026-01-28 (sitemap last-modified) | full |
| DROPZONE-MYSTEN-2026 | How Mysten Labs Eliminated Toil and Scaled Security With Dropzone AI | Dropzone AI | vendor | https://www.dropzone.ai/case-studies/how-mysten-labs-eliminated-toil-and-scaled-security-with-dropzone-ai | 2026-01-28 (sitemap last-modified) | full |
| DROPZONE-EUMSSP-2026 | How a Leading European MSSP Scaled Alert Investigations Without Scaling the SOC | Dropzone AI | vendor | https://www.dropzone.ai/case-studies/how-a-leading-european-mssp-scaled-alert-investigations-without-scaling-the-soc | 2026-05-27 (sitemap last-modified) | full |
| DROPZONE-JD2030-2026 | SOC Analyst Job Description: Rewriting It for 2030 | Dropzone AI | vendor | https://www.dropzone.ai/blog/soc-analyst-job-description-2030 | 2026-05-13 | full |
| DROPZONE-GARTNERHC-2026 | The 2026 Gartner Hype Cycle for Security Operations | Dropzone AI | vendor | https://www.dropzone.ai/blog/gartner-hype-cycle-security-operations-2026 | 2026-06-16 | full (Gartner report itself not opened) |
| PROPHET-CABINET-2026 | Cabinetworks: Revolutionizing SOC efficiency with Prophet AI | Prophet Security | vendor | https://www.prophetsecurity.ai/case-studies/cabinetworks-revolutionizing-soc-efficiency-with-prophet-ai | 2026-04-30 (sitemap last-modified) | full |
| PROPHET-JBPCO-2026 | JB Poindexter & Co: Unlocking SOC capacity and speed with Prophet AI | Prophet Security | vendor | https://www.prophetsecurity.ai/case-studies/jb-poindexter-co-unlocking-soc-capacity-and-speed-with-prophet-ai | 2026-05-05 (sitemap last-modified) | full |
| EXPEL-PRECEDENT-2026 | New Ruxie AI power-up: Precedent engine turns repetitive alerts into faster decisions | Expel | vendor | https://expel.com/blog/new-ruxie-ai-power-up-precedent-engine/ | 2026-09-10 | full |
| EXPEL-3LEADERS-2026 | Why three security leaders still won't let AI make the call | Expel | vendor | https://expel.com/blog/why-three-security-leaders-still-wont-let-ai-make-the-call/ | 2026-10-02 | full |
| EXPEL-GARTNERMDR-2026 | AI-augmented, still human-led: What changed in the 2026 Gartner Market Guide for MDR | Expel | vendor | https://expel.com/blog/what-changed-in-the-2026-gartner-market-guide-for-managed-detection-and-response/ | 2026-09-21 | full (Gartner guide itself not opened) |
| EXPEL-RUXIE-2026 | Ruxie, Expel's AI for cybersecurity | Expel | vendor | https://expel.com/ai-automation/ | 2026-10-14 (modified; first published 2025-07-31) | full |
| ELASTIC-AGENTICSOC1-2026 | Alert triage in under 3 minutes with Elastic's agentic SOC | Elastic Security Labs | vendor | https://www.elastic.co/security-labs/alert-triage-agentic-soc-elastic-workflows | 2026-07-02 | full |
| ELASTIC-TOKENS-2026 | Agentic SOC architecture: specialized agents cut costs 5.7x | Elastic Security Labs | vendor | https://www.elastic.co/security-labs/agentic-soc-token-budget-architecture | 2026-07-24 | full |
| ELASTIC-ACCURACY-2026 | Agentic SOC alert triage: 60% to 92% AI accuracy | Elastic Security Labs | vendor | https://www.elastic.co/security-labs/alert-triage-agentic-soc-self-correcting-agents | 2026-08-25 | full |
| GOOGLE-TIN-2026 | Triage alerts with the Triage Agent | Google Cloud documentation | vendor | https://docs.cloud.google.com/chronicle/docs/secops/triage-agent | 2026-10-13 | full |
| TECHINFORMED-GOOGLE-2026 | Google's SOC agent cuts alert review from 30 minutes to 60 seconds | TechInformed | press | https://techinformed.com/googles-soc-agent-cuts-alert-review-from-30-minutes-to-60-seconds/ | 2026-06-16 | full |
| MSFT-DEFENDER-AGENTS-2026 | Deploy AI agents in Microsoft Defender | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender | 2026-05-12 | full |
| MSFT-PHISHTRIAGE-2026 | Microsoft Security Copilot Phishing Triage Agent in Microsoft Defender | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent | 2026-07-02 | full |
| MSFT-BONO-2024 | Generative AI and Security Operations Center Productivity: Evidence from Live Operations | arXiv (Microsoft authors) | academic | https://arxiv.org/abs/2411.03116 | 2024-11-05 | full |
| AMAZON-RULEFORGE-2026 | How Amazon uses agentic AI for vulnerability detection at global scale | Amazon Science | vendor | https://www.amazon.science/blog/how-amazon-uses-agentic-ai-for-vulnerability-detection-at-global-scale | 2026-04-08 | full |
| AWS-SIRBENCH-2026 | SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents | arXiv (AWS authors) | academic | https://arxiv.org/abs/2604.12040 | 2026-04-13 | full |
| CIO-ARCTICWOLF-2026 | Inside Arctic Wolf's new agentic security platform | CIO.com | press | https://www.cio.com/article/4211089/inside-arctic-wolfs-new-agentic-security-platform.html | 2026-08-26 | full |
| ARCTICWOLF-AURORA-2026 | Human Instinct Meets AI Speed (home page) | Arctic Wolf | vendor | https://arcticwolf.com/ | 2026-10-01 (modified) | full |
| SECBOULEVARD-ARCTICWOLF-2026 | Arctic Wolf Launches Aurora Agentic SOC, Claims World's Largest Commercial Agentic SOC | Security Boulevard | press | https://securityboulevard.com/2026/03/arctic-wolf-launches-aurora-agentic-soc-claims-worlds-largest-commercial-agentic-soc/ | 2026-03 (from URL) | search-only |
| ESENTIRE-2026 | Managed Detection and Response Services & Security Operations Platform | eSentire | vendor | https://www.esentire.com/ | 2026-05-07 (modified) | full |
| SOPHOS-MDR-2026 | Sophos MDR \| 24/7 Managed Detection & Response \| Agentic SOC | Sophos | vendor | https://www.sophos.com/en-us/products/managed-detection-and-response | 2026-10-17 (retrieval date; page undated) | full |
| TORQ-SERIESD-2026 | Torq Secures $140M Series D at $1.2B Valuation to Lead the AI SOC and Agentic AI Era | Torq | vendor | https://torq.io/news/torq-seriesD/ | 2026-01-12 | full |
| UNDERDEFENSE-AISOC-2026 | AI SOC in 500 Real Incidents: Where It Still Asks for a Human | UnderDefense | vendor | https://underdefense.com/blog/ai-soc-real-incidents/ | 2026-07-06 | full |
| ISC2-WORKFORCE-2025 | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full |
| FIRST-CON-2026 | 38th FIRST Conference program (CoAnalyst; Can a General-Purpose LLM Do Tier-1 Triage?; Living Timelines; One Poisoned Artifact) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06-16 (sessions 16-19 June) | full (abstracts only; talks not seen) |
| NDSS-WOSOC-2026 | Experiences of Using Agentic AI to Fill Tooling Gaps in a Security Operations Center | NDSS Symposium (WOSOC) | academic | https://www.ndss-symposium.org/wp-content/uploads/wosoc26-02.pdf | 2026-02-23 | full |
| ARXIV-2610.10608 | From Investigation Failures to Reliable SOC Agents | arXiv | academic | https://arxiv.org/abs/2610.10608 | 2026-10-07 | full (abstract) |
| ARXIV-2603.06422 | Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis | arXiv | academic | https://arxiv.org/abs/2603.06422 | 2026-03-06 | full (abstract) |
| ARXIV-2510.00311 | CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage | arXiv | academic | https://arxiv.org/abs/2510.00311 | 2025-09-30 | full (abstract) |
| ARXIV-2605.24421 | Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations | arXiv | academic | https://arxiv.org/abs/2605.24421 | 2026-05-23 | full (abstract) |
| ARXIV-2610.09906 | Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy | arXiv | academic | https://arxiv.org/abs/2610.09906 | 2026-10-07 | full (abstract) |
| ARXIV-2505.06394 | Towards AI-Driven Human-Machine Co-Teaming for Adaptive and Agile Cyber SOCs | arXiv | academic | https://arxiv.org/abs/2505.06394 | 2025-05-09 | full (abstract) |
| EXPEL-JOB-DR-2026 | Senior Detection & Response Engineer | Expel | job-posting | https://expel.com/about/career-listing/8836996002 | 2026-09-26 | full |
| DATABRICKS-JOB-IR-2026 | Staff Security Engineer, Incident Response | Databricks | job-posting | https://databricks.com/company/careers/open-positions/job?gh_jid=8841960002 | 2026-10-08 | full |
| ROBINHOOD-JOB-DR-2026 | Senior Security Engineer, Detection & Response | Robinhood | job-posting | https://boards.greenhouse.io/robinhood/jobs/8202863 | 2026-09-21 | full |
| ROBINHOOD-JOB-SECOPSAI-2026 | Senior Staff Security Engineer, Security Operations | Robinhood | job-posting | https://boards.greenhouse.io/robinhood/jobs/8259431 | 2026-10-06 | full |
| CLOUDFLARE-JOB-CMDC-2026 | Response Engineer - Cloudflare Managed Defense Center | Cloudflare | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8222732 | 2026-09-24 | full |
| FIGMA-JOB-SECOPS-2026 | Manager, Security Operations | Figma | job-posting | https://boards.greenhouse.io/figma/jobs/6015609004 | 2026-06-05 | full |
| ANTHROPIC-JOB-DRPLATFORM-2026 | Security Software Engineer, Detection & Response Platform | Anthropic | job-posting | https://job-boards.greenhouse.io/anthropic/jobs/4595463008 | 2025-03-24 (updated 2026-08-24) | full |

## 6. Gaps

- **No independent production measurement.** I found no independent, production-scale figures for false-negative rate, override rate, MTTR change or cost per investigation. The only independent quantitative evidence is academic benchmarks and one university SOC (8 tickets). The largest live-operations study (Microsoft, 150+ organizations) dates from 2024 data, is observational and is authored by the vendor.
- **Named-customer outcomes are almost all vendor-authored.** ECS, Zapier, Mysten Labs, Cabinetworks, JB Poindexter, Valvoline and the CrowdStrike customers are quoted in the provider's own material; no customer-authored write-up with figures was found beyond Elastic's own SOC. Cabinetworks and JB Poindexter case studies were read; JB Poindexter figures (4,407 alerts in 60 days; about 6.3 analyst-years; MTTI under four minutes) are Prophet-authored and are not used in outcomes, only here.
- **Unnamed or unreachable.** The European MSSP and UnderDefense bake-off customers are unnamed. BBVA's testimonial for Google's agent was seen only in search results. Microsoft's primary announcement pages for 2025-2026 Security Copilot agents were not reached beyond Learn documentation. Arctic Wolf's primary launch release was seen only in search results; the Security Boulevard copy came back as navigation text.
- **Paywalled or gated.** The Gartner Hype Cycle and Market Guide for MDR (quoted via Dropzone and Expel), Prophet's Gartner research on AI SOC staffing, SANS SOC and AI survey bodies, and the CSA benchmark report itself were not opened.
- **Dates.** SANS-SOC-2026 and CSA-BENCH-2025 pages show no publication date (year only). Case studies from Dropzone and Prophet show no date; sitemap last-modified is used. Sophos page is undated; retrieval date shown.
- **Quality of the CSA numbers.** The 45-61% speed and accuracy figures come from the vendor's description of the CSA study. It is unclear whether "22-29% higher accuracy" are relative or percentage-point differences (68 to 97 is 29 points).
- **MDR economics and pricing.** No source gave pricing, margin or staffing effects at MDR providers beyond qualitative statements.
- **Job-posting sample.** Postings come from public Greenhouse boards of about 15 companies checked; this is a convenience sample of tech-forward firms, not the market. Only security-operations-relevant postings with AI content are listed.
- **Not covered here.** Regulator and standard-setter guidance on SOC AI (covered by the governance angle), and practitioner discourse beyond the Expel panel and FIRST abstracts (covered by the discourse angle).
