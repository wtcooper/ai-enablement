# Security / operations / discourse: how practitioners talk about AI in the SOC

Archetype: security. Module: operations (SOC: detection engineering, alert triage, investigation, case management, MDR). Angle: discourse. Researched 2026-10-17. Window: roughly 2025-10 to 2026-10.

## 1. Summary

- **The conversation has moved from "copilot" to "who gets to act".** Practitioner write-ups from Figma, Elastic, Slack, Grow Therapy and the DNB Cyber Defense Center describe in-house triage and investigation agents that analysts supervise. Analyst firms (SACR, Forrester) and Gartner (via secondary reports) say triage and investigation are becoming commodity and the open question is trust in response actions. SACR calls this the "action gap".
- **Measured quality evidence is thin and mostly self-reported.** The best numbers are Elastic's AI verdict correctness (60% to 92%, measured against analyst close reasons), Figma's time-to-resolution cut (about 70%) and a CSA/Dropzone randomised study of 148 participants (45-61% faster, 22-29% more accurate). There is no independent, production, multi-organisation measurement of false-negative rates or override rates. Academic and community benchmarks that do exist show weak results for general-purpose models on hard cases (every approach tested in ALERT-BENCH missed at least 40.4% of attack alerts; five of seven frontier models called a real intrusion alert benign in the unsecure.sh scenario).
- **What the successful teams did differently was context, memory and structure, not a better model.** Elastic says it did not change models; it added per-rule investigation guides, HR context and 30 days of closed-case verdicts. Figma separates precedent, policy and procedural memory. Slack and Grow Therapy add a critic or adversarial step because single-pass agents jumped to convenient conclusions.
- **Adoption is wide but shallow.** SANS 2026: 79% of SOCs use AI/ML tools, 36% have built them into a defined workflow. Gartner (via a vendor-sponsored article) puts AI SOC agents at the Peak of Inflated Expectations and forecasts that by 2028, 70% of large SOCs will pilot AI agents for Tier 1 and Tier 2 work but only 15% will see measurable improvement without structured evaluation.
- **The main worries:** (1) the SOC's own AI is an attack surface (log-borne prompt injection; a disclosed weakness in a vendor SOC assistant); (2) junior-pipeline and "five-year problem" effects; (3) vendor sameness and "AI washing"; (4) hosted-model safety filters blocking defenders mid-incident (Hugging Face); (5) autonomy limits: survey data show no respondent grants full unsupervised autonomy.
- **Role effect so far:** on-call and L1 work shifts to reviewing agent output; job postings show roughly three engineering/automation seats for each queue-watching analyst seat (vendor analysis of 665 US postings).

Corrections to the landscape file: the Splunk RSAC SOC post is dated 2026-08-24 (not March); the Forrester RSAC blog is dated 2026-03-31.

## 2. Use cases

```yaml
- id: security-operations-01
  title: Precedent retrieval - similar past alerts and analyst dispositions surfaced at triage
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "On-call engineers spent time working out whether an alert resembled something seen last week, whether a PR already addressed it, and what colleagues had concluded in Slack."
  solution: "Figma indexes each alert and the on-call engineer's Slack/Asana comments as 'investigation context', retrieves semantically similar recent alerts when a new one fires, posts a summary in the alert thread, and downgrades severity when similar alerts are judged benign or duplicative with high confidence. Expel describes a similar 'precedent engine' that embeds a new alert, compares it with previously triaged alerts and shows the nearest cases and how they were closed; the analyst still sets the disposition."
  outcomes:
    - lever: cost
      description: "Fewer on-call pages from automatic severity downgrade of alerts matching benign precedent."
      figure: "20% drop in on-call pages"
      measures: "Figma: 'drop in on-call pages from this change alone' (severity downgrade when auto-resolution confidence >= 7); baseline period and denominator not stated"
      provenance: self-reported
      source_ref: FIGMA-AGENTS-2026
    - lever: quality
      description: "Expel states a safety gate keeps known true-positive patterns from being called benign, and sets an initiative target; no measured result published."
      figure: "target: 10% or greater overall queue reduction with less than 1% change in recall; <1% suppressed true-positive rate"
      measures: "Expel: 'initiative target' for queue reduction vs recall change; '<1% suppressed true-positive rate' stated as a property of the safety gate, measurement basis not given"
      provenance: vendor-published
      source_ref: EXPEL-RUXIE-2026
  prerequisites:
    - "Closed alerts that carry analyst reasoning (a closed alert with no comments 'tells you almost nothing', Figma)."
    - "A way to capture analyst notes without changing their workflow (Slack thread comments indexed back to the alert)."
    - "Bias retrieval toward recent cases (Figma found a two-day-old similar alert more useful than a six-month-old duplicate)."
  risks_and_guardrails:
    - "Expel defaults to escalation when the match is weak, absent or from unverified history (EXPEL-RUXIE-2026, section 'How it works')."
    - "Figma separates precedent (retrieved) from policy (steering memory): early on it saved everything as steering memory and that overrode agent behaviour unintentionally (FIGMA-AGENTS-2026, section 'Developing and segmenting agent memory')."
  human_checkpoints:
    - "Analyst makes the disposition in Expel's design (EXPEL-RUXIE-2026)."
    - "On-call engineer reads the generated summary and closes the alert in the thread (FIGMA-AGENTS-2026)."
  role_evolution: "Each useful comment an engineer leaves becomes training signal for future similar alerts; Figma says the existing workflow is the 'training pipeline' (FIGMA-AGENTS-2026)."
  evidence_grade: A
  sources:
    - { ref: FIGMA-AGENTS-2026, title: "How we secure Figma's internal systems with agents", publisher: Figma, type: firm, url: "https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/", date: 2026-07-29, access: full, locator: "sections 'The RAG layer' and 'What retrieval could do, and where it stopped'" }
    - { ref: EXPEL-RUXIE-2026, title: "New Ruxie AI power-up: Precedent engine turns repetitive alerts into faster decisions", publisher: Expel, type: vendor, url: "https://expel.com/blog/new-ruxie-ai-power-up-precedent-engine/", date: 2026-09-10, access: full, locator: "sections 'How it works' and 'How this delivers a better defense for you'" }
  last_reviewed: 2026-10-17
  notes: "Figma's figure is a self-reported single-change effect. Expel's page announces a feature; it publishes targets, not results."

- id: security-operations-02
  title: Context-grounded AI verdict and case summary with one-click analyst close
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, expert-judgment]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Elastic's first AI case summaries were wrong about 40% of the time; analysts stopped reading them because checking a wrong paragraph took longer than triaging manually."
  solution: "Three agents run in a workflow on each alert: a Pattern Finder (no tools; compares the alert with 30 days of closed cases on the same rule, plus Workday risk context), an L1 Investigation agent (follows the detection rule's investigation guide, runs queries) and a Summarizer. The AI verdict and confidence are written to case fields; analysts click 'Close Case: AI Correct' or record that the AI was incorrect, and the mismatch feeds back into the next run."
  outcomes:
    - lever: quality
      description: "AI verdict correctness rose after adding context; the model was not changed."
      figure: "60% to 92%"
      measures: "Elastic: 'AI verdict correctness' based on 'comparing the AI verdict and the analyst close reason'; period and alert volume not stated"
      provenance: self-reported
      source_ref: ELASTIC-TRIAGE-2026
    - lever: speed
      description: "Analysts can double-check the summary and close the case in one step instead of reading a long unreliable summary."
      figure: "none published"
      measures: "no time-saved figure given"
      provenance: self-reported
      source_ref: ELASTIC-TRIAGE-2026
  prerequisites:
    - "Detection engineers write per-rule investigation guides (with separate notes for analysts and AI)."
    - "Analysts must pick a closure reason on every case so the AI verdict can be scored."
    - "Employee context lookups (hire/leave dates, cost centre) from the HR system."
    - "Predictable lookups are built as plain queries, not agents (Elastic: agents only for reading and reasoning)."
  risks_and_guardrails:
    - "Pattern Finder and Summarizer have no tools, which Elastic says prevents injected content from overriding their behaviour (ELASTIC-TRIAGE-2026, section 'Pattern agent')."
    - "A third-party researcher (PromptArmor) reported on 2026-09-28 that a different Elastic product, its AI SOC assistant, could be steered by instructions in an alert into minting API keys, and said the vendor had not engaged after four follow-ups. That report concerns the product assistant, not the internal pipeline described here (PROMPTARMOR-ELASTIC-2026)."
  human_checkpoints:
    - "Analyst selects the closure reason and owns the case; summarizer stops replacing its comment once the case is assigned (ELASTIC-TRIAGE-2026, section 'Summarizer Agent')."
  role_evolution: "Detection engineers now author guides that the AI follows as primary instructions; analysts validate and close (ELASTIC-TRIAGE-2026)."
  evidence_grade: A
  sources:
    - { ref: ELASTIC-TRIAGE-2026, title: "Inside Elastic's agentic SOC: How we took AI alert triage from 60% to 92% accuracy", publisher: Elastic Security Labs, type: vendor, url: "https://www.elastic.co/security-labs/blog/alert-triage-agentic-soc-self-correcting-agents", date: 2026-08-25, access: full, locator: "sections 'When your AI SOC analyst is wrong 40% of the time', 'Leading with the data', 'Summarizer Agent'" }
    - { ref: PROMPTARMOR-ELASTIC-2026, title: "Elastic AI SOC Exfiltrates Credentials", publisher: PromptArmor, type: vendor, url: "https://www.promptarmor.com/resources/elastic-agentic-soc-vulnerable-to-credential-theft", date: 2026-09-28, access: full, locator: "Context; Responsible Disclosure and Timeline" }
  last_reviewed: 2026-10-17
  notes: "Elastic sells the platform it dogfoods ('Customer Zero'). Correctness is agreement with the analyst's close reason, so it inherits any analyst error. Version cited by Elastic: 9.5.1."

- id: security-operations-03
  title: Agentic alert investigation across identity, endpoint, cloud and data-lake sources, with memory and scoped tools
  archetype: security
  module: operations
  function: technology-it
  work_types: [expert-judgment, research-synthesis]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Gathering context was the main burden for on-call engineers; the SIEM raised more checks than a small team could work by hand."
  solution: "Figma's triage agent is tagged into the Slack alert thread, reads the thread, calls scoped tools (Okta, endpoint-control, Wiz, Panther, Slack), delegates data-lake questions to a sub-agent that writes SQL, and keeps three kinds of memory (case, steering, procedural). It can also open draft pull requests for detection or config changes."
  outcomes:
    - lever: speed
      description: "Reduction in time to resolution; the blog gives both a headline and a body figure."
      figure: "71% (summary) / 'around 70% reduction in time-to-resolution on complex alerts' (body)"
      measures: "Figma: 'alert time-to-resolution' (summary) and 'time-to-resolution on complex alerts' (body); baseline and sample not stated"
      provenance: self-reported
      source_ref: FIGMA-AGENTS-2026
    - lever: cost
      description: "Fewer on-call pages through AI-driven severity downgrading."
      figure: "20% reduction"
      measures: "Figma: 'reduction in on-call pages through AI-driven severity downgrading'"
      provenance: self-reported
      source_ref: FIGMA-AGENTS-2026
    - lever: capacity
      description: "Agent redirects users asking about unapproved tools to approved alternatives."
      figure: "25% fewer"
      measures: "Figma: 'fewer endpoint software approval requests'"
      provenance: self-reported
      source_ref: FIGMA-AGENTS-2026
  prerequisites:
    - "Security data lake with audit logs; messy schemas are handled by procedural memory the sub-agent writes itself (first Zoom question took several discovery queries, then one)."
    - "Configuration-as-code for the shared tool set so agents do not fragment into variants."
    - "Alerts already routed to Slack/ticketing with an on-call rotation."
  risks_and_guardrails:
    - "Deterministic safeguards on every tool call: PRs are set to draft by a workflow step, not by a prompt instruction, because the LLM was not reliable at remembering that (FIGMA-AGENTS-2026, section 'Guardrails')."
    - "No ambient access to Slack channels; the agent reads a thread only when re-tagged; channel-aware prompts so sensitive activity data does not surface in large rooms."
    - "Figma says autonomy is more comfortable when the action is bounded, reversible and supported by clear evidence."
  human_checkpoints:
    - "On-call engineer reviews what the agent found, confirms or corrects, and handles cases needing judgment (FIGMA-AGENTS-2026, 'Where we are now')."
    - "PRs stay in draft for human review."
  role_evolution: "The on-call job shifted from 'investigate from scratch' to reviewing and correcting agent output (FIGMA-AGENTS-2026)."
  evidence_grade: A
  sources:
    - { ref: FIGMA-AGENTS-2026, title: "How we secure Figma's internal systems with agents", publisher: Figma, type: firm, url: "https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/", date: 2026-07-29, access: full, locator: "summary paragraph; 'Guardrails'; 'Where we are now and what's next'" }
    - { ref: DETENGWEEKLY-166-2026, title: "DEW #166 - Figma's Agentic SecOps, AI-EDRs and Anthropic Evals Breaking into Companies", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-166-figmas-agentic-secops-ai", date: 2026-08-05, access: full, locator: "Detection Engineering Gem" }
  last_reviewed: 2026-10-17
  notes: "Single team, self-reported, no baseline described. The headline and body figures differ (71% vs 'around 70%' on complex alerts)."

- id: security-operations-04
  title: Multi-persona investigation team (Director, domain Experts, Critic) that on-call staff supervise
  archetype: security
  module: operations
  function: technology-it
  work_types: [expert-judgment, research-synthesis]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "A single 300-word-prompt prototype was highly variable: sometimes insightful, sometimes jumping to a spurious conclusion without questioning its own method; prompts alone could not give fine-grained control."
  solution: "Slack's security engineering team split the investigation into separate model calls with structured outputs: a Director that poses questions and advances phases (discovery, trace, conclude), domain Experts (access, cloud, code, threat) that produce findings, and a Critic that scores finding credibility and assembles the timeline."
  outcomes:
    - lever: quality
      description: "Slack reports 'meaningful benefits' and agent discoveries beyond the triggering alert (for example a credential exposure in an ancestor process), but publishes no rates."
      figure: "none published"
      measures: "no figures given"
      provenance: self-reported
      source_ref: SLACK-AGENTS-2025
  prerequisites:
    - "Data sources exposed to the agents through a controlled tool interface (a stdio MCP server in the prototype)."
    - "A hub/worker service with a dashboard to watch investigations live and inspect each model call."
  risks_and_guardrails:
    - "Structured outputs are 'subject to the usual problems of cheating and hallucination' and can fail if the schema is too complex (SLACK-AGENTS-2025, 'The Solution')."
    - "The Critic is weakly adversarial to the experts to mitigate hallucination and variable interpretation of evidence."
  human_checkpoints:
    - "Staff observe investigations in real time and read the resulting reports; human-in-the-loop details are promised in a later post."
  role_evolution: "Slack says that during on-call shifts it is 'switching to supervising investigation teams' rather than gathering evidence (SLACK-AGENTS-2025, Conclusion)."
  evidence_grade: B
  sources:
    - { ref: SLACK-AGENTS-2025, title: "Streamlining Security Investigations with Agents", publisher: Slack Engineering, type: firm, url: "https://slack.engineering/streamlining-security-investigations-with-agents/", date: 2025-12-01, access: full, locator: "sections 'The Solution', 'Investigation Loop', Conclusion" }
  last_reviewed: 2026-10-17
  notes: "Slack describes itself as 'at an early phase of our journey'."

- id: security-operations-05
  title: Scheduled AI threat hunts over log sources that have no detection rules
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Teams can write deterministic SQL detections for AWS and Okta but not for every SaaS audit log (Grow Therapy cites HubSpot)."
  solution: "A healthcare platform runs daily agent hunts across about 15 log sources. Each hunt is a YAML objective with severity guidelines and known false positives; a five-phase flow (data gathering with a cheaper model, baseline comparison, context enrichment, confidence scoring, adversarial validation) writes findings into the same alerts table as the SQL detections, routed to Slack and Jira."
  outcomes:
    - lever: quality
      description: "Staging the first CloudTrail hunt before it could alert cut its findings per run."
      figure: "from 15+ findings per run to 2-3"
      measures: "Grow Therapy: findings per run of the first CloudTrail hunt, before and after signal-to-noise tuning in staging"
      provenance: self-reported
      source_ref: GROWTHERAPY-HUNT-2026
    - lever: cost
      description: "Running cost of the whole hunting system."
      figure: "$320-510 per month"
      measures: "Grow Therapy cost table total (Claude API, Snowflake compute, Fargate, Lambda/DynamoDB/NAT); Datadog counted as $0 because already paid for"
      provenance: self-reported
      source_ref: GROWTHERAPY-HUNT-2026
  prerequisites:
    - "Logs already centralised in a warehouse and an observability tool."
    - "A feedback loop where analysts mark false positives and the results feed the next hunt, built before deployment."
    - "A staging mode so new hunts write to a staging table until signal-to-noise is acceptable."
  risks_and_guardrails:
    - "The one-shot first version produced vague findings; structuring the work as an analyst would fixed it (GROWTHERAPY-HUNT-2026, 'Extending threat detection with LLMs')."
    - "Start with few tools: a large tool set can bloat context and lower signal-to-noise."
  human_checkpoints:
    - "Analysts click false positive / escalate in Slack; Jira tracks state; the 90-day resolved-alert history feeds known-FP patterns into later hunts."
  role_evolution: "Hunt definitions are drafted by Claude from a one-paragraph description plus an AGENTS.md of conventions, then reviewed by the security team (GROWTHERAPY-HUNT-2026)."
  evidence_grade: A
  sources:
    - { ref: GROWTHERAPY-HUNT-2026, title: "Threat hunt AI: How we built an AI security analyst on AWS for under $500/month", publisher: Grow Therapy engineering, type: firm, url: "https://engineering.growtherapy.com/post/threat-hunt-ai-how-we-built-an-ai-security-analyst-on-aws-for-under-500-month", date: 2026-08, access: full, locator: "cost table; 'Handling noise: False positives & deduplication'; lessons list" }
    - { ref: DETENGWEEKLY-167-2026, title: "DEW #167 - More Security Agentic Breaches, Cheap and Scalable Threat Hunting & Detection Skills", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-167-more-security-agentic-breaches", date: 2026-08-19, access: full, locator: "State of the Art, 'Threat hunt AI'" }
  last_reviewed: 2026-10-17
  notes: "Page has no publication date; DEW #167 (2026-08-19) already featured it, so it is dated 2026-08 or earlier. Newsletter noted the $500 is additive to existing Datadog and Snowflake spend."

- id: security-operations-06
  title: Evidence-gated dismissal - an adversarial or independent challenge before an agent may close an alert
  archetype: security
  module: operations
  function: technology-it
  work_types: [review-assurance, expert-judgment]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Triage agents tend to dismiss attack alerts when searches return nothing, and self-review in the same context does not correct errors."
  solution: "Grow Therapy adds a final phase where the model must argue against each finding and produce counter-evidence (for example an allowlisted service account or a >80% historical false-positive pattern with at least 3 prior occurrences) before it can be dismissed. Slack uses a separate Critic. The ALERT-BENCH study found stronger evidence rules for dismissal worked best in a benchmark."
  outcomes:
    - lever: quality
      description: "Without the adversarial phase, a large share of surfaced findings were noise."
      figure: "about 40% of findings were noise without the phase"
      measures: "Grow Therapy: 'about 40% of findings were noise' without Phase 5; with it 'most of what surfaces is worth looking at' (no figure)"
      provenance: self-reported
      source_ref: GROWTHERAPY-HUNT-2026
    - lever: quality
      description: "In the four-phase first version, findings a human would have dismissed quickly."
      figure: "about a third of confirmed findings"
      measures: "Grow Therapy: 'about a third of confirmed findings were things a human would have dismissed with 30 seconds of context'"
      provenance: self-reported
      source_ref: GROWTHERAPY-HUNT-2026
    - lever: risk
      description: "Benchmark: every studied approach missed attack-related alerts; the authors' multi-agent design with a separate challenger and judge reduced misses."
      figure: "false-negative rate 40.4% to 3.1%; F1 0.958 vs 0.371-0.744; 18.4% of alerts escalated to analysts"
      measures: "ALERT-BENCH: 1,247 alerts from a multi-stage attack scenario replayed through a live SIEM; false-negative rate = attack-related alerts missed; AIDA is the authors' own design, not independently replicated"
      provenance: independent
      source_ref: ARXIV-2610.10608
  prerequisites:
    - "Historical false-positive pattern and actor history tools the challenger can call."
    - "Analyst resolution data stored in a queryable form."
  risks_and_guardrails:
    - "Escalating 18.4% of alerts to analysts is the cost of the lower miss rate in the benchmark (ARXIV-2610.10608)."
    - "Dismissals receive no consistently stronger investigation than escalations in the tested approaches (ARXIV-2610.10608, abstract)."
  human_checkpoints:
    - "Surviving findings go to analysts; the model does not close high-severity items by itself in the described designs."
  role_evolution: "Analysts see fewer, better-qualified findings (GROWTHERAPY-HUNT-2026)."
  evidence_grade: A
  sources:
    - { ref: GROWTHERAPY-HUNT-2026, title: "Threat hunt AI: How we built an AI security analyst on AWS for under $500/month", publisher: Grow Therapy engineering, type: firm, url: "https://engineering.growtherapy.com/post/threat-hunt-ai-how-we-built-an-ai-security-analyst-on-aws-for-under-500-month", date: 2026-08, access: full, locator: "'Phase 5: Adversarial validation'; 'Handling noise'" }
    - { ref: SLACK-AGENTS-2025, title: "Streamlining Security Investigations with Agents", publisher: Slack Engineering, type: firm, url: "https://slack.engineering/streamlining-security-investigations-with-agents/", date: 2025-12-01, access: full, locator: "'Critic Agent'" }
    - { ref: ARXIV-2610.10608, title: "From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage", publisher: arXiv (Tsegai, Kantchelian, Yao, Gao), type: academic, url: "https://arxiv.org/abs/2610.10608", date: 2026-10-07, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Grade A rests on Grow Therapy's self-reported figures. The two Grow figures describe different versions of the system and are not additive. The benchmark result is a research prototype, not a deployment."

- id: security-operations-07
  title: Live event SOC with an AI triage agent and an agent-activity dashboard (Cisco and Splunk)
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, data-reporting]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Event SOCs are noisy, temporary and have little baseline; analysts must move quickly from signal to evidence to decision."
  solution: "At Splunk .conf26 the team ran a live 'agentic SOC': the Splunk ES AI Triage Agent reviewed findings and proposed a disposition, rationale and next steps before a human took ownership; tier 1, 2 and 3 analysts and detection engineers validated and tuned. The team built a dashboard in an afternoon to show agent activity, confidence and analyst handoff. Earlier, at Black Hat USA 2026, an analyst notification bot handed finished agent triage to analysts."
  outcomes:
    - lever: capacity
      description: "Triage agent coverage and activity over the conference; Cisco says these are event observations, not product benchmarks."
      figure: "94% triage analysis coverage; 1,503 AI agentic events; 7,605 SPL queries generated and run"
      measures: "Cisco dashboard snapshot for the entire .conf26 conference including setup days; coverage denominator not defined on the page"
      provenance: vendor-published
      source_ref: CISCO-SPLUNK-CONF26-2026
    - lever: quality
      description: "Suggested dispositions shown on the dashboard; no accuracy against analyst verdicts is reported."
      figure: "True Positive 44%; Benign Positive 42%; No suggestion 7%; False Positive 6%; Undetermined 1%"
      measures: "share of Triage Agent suggested dispositions on the dashboard snapshot (denominator not stated); finding status Closed 51%, New 37%, Pending 7%, In Progress 5%"
      provenance: vendor-published
      source_ref: CISCO-SPLUNK-CONF26-2026
  prerequisites:
    - "Normalised, searchable telemetry and packet evidence: Splunk says the first requirement for an agentic SOC is 'not the agent' but the evidence."
    - "Event-specific context (for example training rooms that generate suspicious-looking activity)."
  risks_and_guardrails:
    - "Cisco states the design principle that agents prepare work and people inspect the evidence and decide (CISCO-SPLUNK-CONF26-2026)."
    - "Splunk says at RSAC 2026 it was 'not operating a fully agentic SOC' (SPLUNK-RSACSOC-2026)."
  human_checkpoints:
    - "Tier 1-3 analysts validate agent output; response decisions affecting users, availability or trust stay human (SPLUNK-RSACSOC-2026)."
  role_evolution: "Blended Cisco, Splunk and Endace team with tiered analysts and detection engineers feeding fixes back into detections (CISCO-SPLUNK-CONF26-2026)."
  evidence_grade: B
  sources:
    - { ref: CISCO-SPLUNK-CONF26-2026, title: "Splunk .conf26: Tracking the Triage Agent in the Agentic SOC", publisher: Cisco Blogs, type: vendor, url: "https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/", date: 2026-10-08, access: full, locator: "sections 'Building the Triage Agent Dashboard in an Afternoon' and 'Dashboard Snapshot'" }
    - { ref: SPLUNK-BHUSA-2026, title: "Black Hat USA 2026: Proving the Splunk ES Foundation for the Agentic SOC", publisher: Splunk, type: vendor, url: "https://www.splunk.com/en_us/blog/security/black-hat-usa-2026-proving-the-splunk-es-foundation-for-the-agentic-soc.html", date: 2026-09-23, access: full, locator: "'From Detections to Findings to Agentic Triage'; 'Making Agentic Triage Operational'" }
    - { ref: SPLUNK-RSACSOC-2026, title: "From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC", publisher: Splunk, type: vendor, url: "https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html", date: 2026-08-24, access: full, locator: "Key takeaways; closing list of patterns" }
  last_reviewed: 2026-10-17
  notes: "Vendor-run showcase environment. The RSAC 2026 'more than nine hours' of analyst time saved came from a SOAR playbook for cleartext-credential notifications, which is not AI, so it is excluded from outcomes."

- id: security-operations-08
  title: Fine-tuned small reasoning model for high-confidence auto-close of detections
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Label-only LLM triage gives a verdict with no rationale and limited recall at the confidence level needed to close alerts safely."
  solution: "CrowdStrike trains a triage classifier to reason step by step before a true/false positive verdict, so benign detections can be auto-closed and real threats prioritised. Currently limited to Windows endpoint detections."
  outcomes:
    - lever: capacity
      description: "Recall at the high-confidence operating point rose with reasoning; 'false positive' recall governs auto-closure."
      figure: "FP recall 21.8% to 64.8%; TP recall 34.7% to 53.0%; overall accuracy 82.6% vs about 55-71% for general-purpose models"
      measures: "CrowdStrike: recall at 98% FP precision / 99% TP precision on a held-out test set of real Windows endpoint detections, reasoning vs direct-label; accuracy as defined by the vendor on the same task"
      provenance: vendor-published
      source_ref: CROWDSTRIKE-REASONING-2026
  prerequisites:
    - "Large labelled history of real detections and analyst verdicts."
  risks_and_guardrails:
    - "Calibration is only as good as the input features: Intezer's contributed piece says a model fed 'malware detected, threat quarantined, low severity' will close alerts where 51% of memory-scanned infected machines had already been reported as mitigated by EDR (THN-DECISIONMODELS-2026)."
  human_checkpoints:
    - "Low-confidence verdicts go to analysts; reasoning trace is readable for review (CROWDSTRIKE-REASONING-2026)."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: CROWDSTRIKE-REASONING-2026, title: "Teaching AI to Reason Through Detection Triage", publisher: CrowdStrike, type: vendor, url: "https://www.crowdstrike.com/en-us/blog/teaching-ai-to-reason-through-detection-triage/", date: 2026-08-17, access: full, locator: "Table 1 and following paragraph" }
    - { ref: THN-DECISIONMODELS-2026, title: "AI Decision Models and Their Impact on AI SOC Platforms", publisher: The Hacker News (contributed by Intezer), type: press, url: "https://thehackernews.com/2026/10/ai-decision-models-and-their-impact-on.html", date: 2026-10-16, access: full, locator: "'But a calibrated guess is still just a guess'" }
  last_reviewed: 2026-10-17
  notes: "Vendor research on its own data; not independently replicated. The reasoning variant is research ('our latest research paper'); the label-only models are described as already running."

- id: security-operations-09
  title: Typed-output 'decision models' scoring every alert against thresholds
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Prose-generating LLM triage is costly per alert, variable and hard to audit, so teams cherry-pick high-severity alerts."
  solution: "Models that return a choice, score or yes/no with a probability (TypeSafe 'Jev', OpenAI Decisions API public beta, Cribl open adapter) could close alerts above a high threshold, escalate below a low one and send the middle band to analysts, logging every verdict as a record."
  outcomes:
    - lever: cost
      description: "Vendor pricing and latency claims for one such model; the article's own estimate of annual model cost for 450,000 alerts."
      figure: "USD 42 per billion input tokens; 70-500 ms; about USD 100 a year for 450,000 alerts"
      measures: "article: TypeSafe Jev price and response time; the annual figure is the author's example calculation, not a measured deployment"
      provenance: vendor-published
      source_ref: THN-DECISIONMODELS-2026
  prerequisites:
    - "Rich per-alert evidence (the article says inputs such as title and severity alone leave the model calibrated about alerts, not hosts)."
  risks_and_guardrails:
    - "'Cannot hallucinate' only means the output matches the schema; a well-formed answer can still be wrong, and Cribl's model card admits overconfidence (THN-DECISIONMODELS-2026)."
    - "Same article: nearly 1% of real incidents in the author's data traced to lowest-severity alerts."
  human_checkpoints:
    - "Mid-confidence band goes to analysts; stricter thresholds suggested for irreversible actions."
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: THN-DECISIONMODELS-2026, title: "AI Decision Models and Their Impact on AI SOC Platforms", publisher: The Hacker News (contributed by Intezer), type: press, url: "https://thehackernews.com/2026/10/ai-decision-models-and-their-impact-on.html", date: 2026-10-16, access: full, locator: "sections 'Why a SOC should be excited' and 'But a calibrated guess...'" }
    - { ref: RISKYBIZ-854-2026, title: "Risky Business #854 -- We're Jevpilled", publisher: Risky Business, type: podcast, url: "https://risky.biz/RB854/", date: 2026-09-23, access: full, locator: "show description (episode audio not heard)" }
  last_reviewed: 2026-10-17
  notes: "The article is vendor-contributed (author is a product marketing manager at Intezer). The podcast page only confirms the topic was discussed. Product category is weeks old at the time of writing."

- id: security-operations-10
  title: Autonomous closure of clearly benign and low-severity alerts, with humans on the exceptions
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Alerts that are obviously noise or misconfiguration consume analyst time; surveyed teams leave many alerts uninvestigated and switch off rules for capacity reasons."
  solution: "Practitioners argue automation should start where the cost of error is lowest: let AI close alerts it is highly confident are benign and keep it away from VIP account actions. Surveyed teams mostly keep review in place."
  outcomes:
    - lever: capacity
      description: "Adoption of automated action is partial."
      figure: "automated incident response 39% adoption"
      measures: "SANS 2026 AI Survey as reported by Swimlane: 'automated incident response sits at 39% adoption'; population not described in the summary"
      provenance: vendor-published
      source_ref: SANS-AI-2026
    - lever: risk
      description: "Autonomy granted to AI, vendor-run survey."
      figure: "57% require a human to review every AI decision before an alert is closed; 30% auto-execute low-risk actions; 13% medium-risk; no respondent full unsupervised autonomy"
      measures: "Prophet Security 'State of AI in Security Operations 2026' as quoted in a sponsored article; respondent base not given in the article"
      provenance: vendor-published
      source_ref: HNS-GARTNER-2026
    - lever: speed
      description: "Gartner forecast, as quoted by Expel, for MDR."
      figure: "90% by 2029, up from 30% today"
      measures: "Gartner Market Guide for MDR (2026-09-09), p.2, as quoted by Expel: initial findings from MDR providers 'processed and addressed with the support of AI models without any human action'"
      provenance: vendor-published
      source_ref: EXPEL-GARTNERMDR-2026
  prerequisites:
    - "Context (runbooks, escalation criteria, knowledge base) fed to the agent; a gift-card keyword means different things at a pharmaceutical firm and a retailer (Swimlane)."
    - "Explainability so a reviewer knows what to verify rather than re-triaging."
  risks_and_guardrails:
    - "Same SANS survey: 63% report significant shortcomings in AI's ability to detect or respond to threats (SANS-AI-2026)."
    - "Prophet survey: 28% of alerts are never investigated; about 60% of respondents said a missed or uninvestigated alert proved material (HNS-GARTNER-2026)."
  human_checkpoints:
    - "Humans review exceptions and anything touching VIP or executive accounts."
  role_evolution: "Analysts spend time on the phishing click that landed or early ransomware signs rather than sifting noise (SANS-AI-2026, Swimlane post)."
  evidence_grade: C
  sources:
    - { ref: SANS-AI-2026, title: "A SOC Leader's Guide to the 2026 SANS AI Survey", publisher: Swimlane, type: vendor, url: "https://swimlane.com/blog/sans-ai-2026-soc-trust/", date: 2026-08-17, access: full, locator: "TL;DR; 'Where Automation Actually Earns Trust'; 'Trust Requires Context'" }
    - { ref: HNS-GARTNER-2026, title: "Gartner: 70% of SOCs will pilot AI agents. Only 15% will see results (sponsored, Prophet Security)", publisher: Help Net Security, type: press, url: "https://www.helpnetsecurity.com/2026/09/09/prophet-security-evaluating-ai-soc-agents/", date: 2026-09-09, access: full, locator: "sections 1 and 5" }
    - { ref: EXPEL-GARTNERMDR-2026, title: "AI-augmented, still human-led: What changed in the 2026 Gartner Market Guide for MDR", publisher: Expel, type: vendor, url: "https://expel.com/blog/what-changed-in-the-2026-gartner-market-guide-for-managed-detection-and-response/", date: 2026-09-21, access: full, locator: "'The 2029 number we think everyone's going to quote'" }
  last_reviewed: 2026-10-17
  notes: "All figures are second-hand through vendors. The SANS AI Survey itself was not opened. The Swimlane page shows a display date of Aug 17, 2026; its metadata carries 2026-05-18."

- id: security-operations-11
  title: Triage-to-detection tuning loop - agent drafts allowlist and rule-change pull requests
  archetype: security
  module: operations
  function: technology-it
  work_types: [software-systems]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Alerts keep firing for known-benign patterns until someone writes the suppression."
  solution: "When an on-call engineer confirms a false positive in the thread, Figma's agent opens a draft PR against the detections repo (allowlist entry or rule tune) and, for infrastructure or IdP config, against the monorepo. It responds to reviewer comments and rebases stale branches. Elastic's Pattern Finder files tuning requests against rules it overclassifies."
  outcomes:
    - lever: speed
      description: "Figma says the step from 'figured out what is going on' to 'a PR that fixes it' saved the most time, but gives no figure."
      figure: "none published"
      measures: "no figure"
      provenance: self-reported
      source_ref: FIGMA-AGENTS-2026
  prerequisites:
    - "Detections and key tool configuration stored as code."
  risks_and_guardrails:
    - "Every PR is set to draft by a deterministic workflow step; agent cannot close or modify PRs it did not author (FIGMA-AGENTS-2026, 'Guardrails')."
    - "Bot-authored PRs hide context in git blame, so Figma now adds the requesting engineer's name and the Slack thread link."
  human_checkpoints:
    - "Human reviewer approves and merges the PR."
  role_evolution: "Detection tuning becomes a review task for engineers (FIGMA-AGENTS-2026)."
  evidence_grade: B
  sources:
    - { ref: FIGMA-AGENTS-2026, title: "How we secure Figma's internal systems with agents", publisher: Figma, type: firm, url: "https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/", date: 2026-07-29, access: full, locator: "'From investigation to code changes'" }
    - { ref: ELASTIC-TRIAGE-2026, title: "Inside Elastic's agentic SOC", publisher: Elastic Security Labs, type: vendor, url: "https://www.elastic.co/security-labs/blog/alert-triage-agentic-soc-self-correcting-agents", date: 2026-08-25, access: full, locator: "'The AI feedback loop' (example of tuning requests already filed against a rule)" }
  last_reviewed: 2026-10-17

- id: security-operations-12
  title: End-to-end detection validation by coding agents (simulate, detonate, query SIEM, retry)
  archetype: security
  module: operations
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Rules pass code review but nobody checks that telemetry arrives and the detection fires; labs and simulations are slow to drive by hand. Detection Engineering Weekly lists four failure modes of rules that 'run but can't see': disconnected, starved, missing fields and ingest-lag blind window."
  solution: "The DNB Cyber Defense Center repurposed coding agents with a plugin that writes TTPForge attack simulations, ships them to a lab host, detonates them, queries Splunk to confirm the detection matched and rewrites on failure. A human reviewed every generated TTP."
  outcomes:
    - lever: quality
      description: "Most generated TTPs were fit for their detection, and the loop surfaced small mechanical issues in the pipeline that had passed code review."
      figure: "none published (numbers redacted)"
      measures: "DNB states 'numbers, volumes, detections, and data sources have been redacted or changed'"
      provenance: self-reported
      source_ref: CAUCHY-DETVAL-2026
  prerequisites:
    - "A reproducible lab with golden images and deployment automation; baseline user activity modelled as well as malicious activity."
    - "Detection-as-code pipeline."
  risks_and_guardrails:
    - "Detonating tooling in production can cause externalities; mirror the environment instead (DETENGWEEKLY-162-2026)."
    - "Synthetic telemetry can be forged: a Windows telemetry researcher showed an EDR accepted fabricated local events, so end-to-end tests matter more than synthetic ingestion tests (DETENGWEEKLY-169-2026)."
  human_checkpoints:
    - "Every TTP reviewed by hand in DNB's run."
  role_evolution: "Detection engineers act more like SREs and software engineers (DETENGWEEKLY-162-2026, commentary)."
  evidence_grade: B
  sources:
    - { ref: CAUCHY-DETVAL-2026, title: "End-to-end detection validation using coding agents", publisher: DNB Cyber Defense Center (Kyrre Wahl Kongsgard), type: firm, url: "https://blog.cauchy.org/blog/detection-validation/", date: 2026-06-16, access: full, locator: "opening summary" }
    - { ref: DETENGWEEKLY-162-2026, title: "DEW #162 - Detonating TTPs with Agents, Writing Rules for Malicious Coding Agents & Skills Threat Models", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-162-detonating-ttps-with-agents", date: 2026-07-08, access: full, locator: "Detection Engineering Gem" }
    - { ref: DETENGWEEKLY-165-2026, title: "DEW #165 - Starved & Neglected Rules, Agentic IR Notebooks and Hacker Summer Camp", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-165-starved-and-neglected-rules", date: 2026-07-29, access: full, locator: "Detection Engineering Gem" }
  last_reviewed: 2026-10-17

- id: security-operations-13
  title: Agent-built case notebooks as the incident workspace (executable, reproducible case file)
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis, document-production]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Incident response means 20+ tabs across SIEM, threat intel and asset tools plus scratch notes; context is lost and chain of evidence is weak."
  solution: "DNB built marimo notebooks with SDKs that run native SPL and KQL, return typed tables joined locally, and let an agent author and run cells in the same live notebook, so the finished notebook is the case file. Domain skills for triage and hunting replace per-alert-type templates."
  outcomes:
    - lever: quality
      description: "Reproducibility and chain-of-evidence benefit stated qualitatively; no figures."
      figure: "none published"
      measures: "no figures"
      provenance: self-reported
      source_ref: CAUCHY-IRNB-2026
  prerequisites:
    - "Query access to SIEM/XDR/warehouse platforms; security data exposed as dataframes."
  risks_and_guardrails:
    - "Real cases are confidential, so the published demo is a simplified scenario (CAUCHY-IRNB-2026, video caption)."
  human_checkpoints:
    - "Analyst works in the same notebook and owns conclusions."
  role_evolution: "Not described beyond analyst and agent sharing one workspace (CAUCHY-IRNB-2026)."
  evidence_grade: B
  sources:
    - { ref: CAUCHY-IRNB-2026, title: "Agentic incident response notebooks", publisher: DNB Cyber Defense Center (Kyrre Wahl Kongsgard), type: firm, url: "https://blog.cauchy.org/blog/incident-response-notebooks/", date: 2026-06-19, access: full, locator: "opening and 'Why marimo fits'" }
    - { ref: DETENGWEEKLY-165-2026, title: "DEW #165", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-165-starved-and-neglected-rules", date: 2026-07-29, access: full, locator: "State of the Art, 'Agentic incident response notebooks'" }
  last_reviewed: 2026-10-17
  notes: "Overlaps the incident-response module; kept here for the investigation and case-management step."

- id: security-operations-14
  title: Self-hosted AI-assisted anomaly triage that surfaced an intrusion (Hugging Face)
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Separating real signals from daily noise in security telemetry."
  solution: "Hugging Face says its anomaly-detection pipeline uses LLM-based triage over security telemetry and that correlation of those signals flagged an intrusion it describes as driven by an autonomous AI agent system. Afterwards it said it improved alerting so a high-severity signal pages a responder in minutes, any day."
  outcomes:
    - lever: risk
      description: "The disclosure credits AI-assisted detection with surfacing the compromise; no detection-rate figure."
      figure: "none published"
      measures: "no figures"
      provenance: self-reported
      source_ref: HUGGINGFACE-INCIDENT-2026
  prerequisites:
    - "Telemetry pipeline feeding the triage model."
  risks_and_guardrails:
    - "After the event Hugging Face added guardrails and stricter admission controls on its clusters."
  human_checkpoints:
    - "Responders handled containment and assessment; 'we are still completing our assessment' at publication."
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: HUGGINGFACE-INCIDENT-2026, title: "Security incident disclosure - July 2026", publisher: Hugging Face, type: firm, url: "https://huggingface.co/blog/security-incident-july-2026", date: 2026-07-16, access: full, locator: "paragraph beginning 'The attack was initially surfaced through AI-assisted detection'" }
  last_reviewed: 2026-10-17
  notes: "One named incident; attribution of the attacking agents to a specific lab is covered in other modules."

- id: security-operations-15
  title: Self-hosted open-weight model for forensic log analysis during an incident
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis, expert-judgment]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Frontier hosted-model safety filters blocked analysis that required submitting real attack commands, exploit payloads and C2 artifacts."
  solution: "Hugging Face ran the forensic analysis on an open-weight model on its own infrastructure, which also kept attacker data and referenced credentials inside its environment. Its lesson: have a capable self-hostable model vetted before an incident."
  outcomes:
    - lever: speed
      description: "Analysis proceeded after hosted-model APIs refused the requests; no timing given."
      figure: "none published"
      measures: "no figures"
      provenance: self-reported
      source_ref: HUGGINGFACE-INCIDENT-2026
  prerequisites:
    - "Compute and a vetted model available before the incident."
  risks_and_guardrails:
    - "Hugging Face notes this is not an argument against safety measures on hosted models (HUGGINGFACE-INCIDENT-2026)."
  human_checkpoints:
    - "Responders interpret results."
  role_evolution: "Detection Engineering Weekly advises defenders to discuss open-weight models for investigation 'all the way up to your CSO' (DETENGWEEKLY-165-2026)."
  evidence_grade: B
  sources:
    - { ref: HUGGINGFACE-INCIDENT-2026, title: "Security incident disclosure - July 2026", publisher: Hugging Face, type: firm, url: "https://huggingface.co/blog/security-incident-july-2026", date: 2026-07-16, access: full, locator: "paragraphs on log analysis and 'The practical lesson for defenders'" }
    - { ref: DETENGWEEKLY-165-2026, title: "DEW #165", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-165-starved-and-neglected-rules", date: 2026-07-29, access: full, locator: "'The Arguments Against Open Source AI are Very Bad'" }
  last_reviewed: 2026-10-17
  notes: "Overlaps incident-response; see Routed section."

- id: security-operations-16
  title: AI-augmented, human-led MDR - provider AI triages and enriches, analysts own the disposition
  archetype: security
  module: operations
  function: service-delivery
  work_types: [transaction-processing, client-interaction]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "MDR buyers face providers that cap what they investigate and a wave of products labelled 'AI MDR'."
  solution: "Expel says its AI SOC manager triages and enriches alerts before an analyst touches them, runs investigative steps and documents outcomes while analysts make consequential calls. Gartner's 2026 MDR Market Guide, per Expel, defines MDR as 'AI-augmented, human-led', requires triage and investigation of all discovered threats regardless of priority, and says buyers should demand clarity on which services are AI-augmented."
  outcomes:
    - lever: speed
      description: "Mean time to remediate on fully automated high and critical incidents."
      figure: "14 minutes"
      measures: "Expel: 'mean time to remediate (MTTR) on fully automated high and critical incidents'; period, volume and definition of 'fully automated' not stated"
      provenance: vendor-published
      source_ref: EXPEL-GARTNERMDR-2026
  prerequisites:
    - "Provider-hosted stack, 24/7 staffing, preapproved remote response (Gartner mandatory features as quoted by Expel)."
  risks_and_guardrails:
    - "Gartner, as quoted: MDR is a human-led service; offerings positioned as AI MDR should be examined (EXPEL-GARTNERMDR-2026)."
  human_checkpoints:
    - "Analysts make the consequential calls; precedent-engine output is decision support, not a disposition (EXPEL-RUXIE-2026)."
  role_evolution: "Provider analysts shift toward reviewing AI-prepared cases; Expel states AI sits 'in the human loop' (EXPEL-GARTNERMDR-2026)."
  evidence_grade: C
  sources:
    - { ref: EXPEL-GARTNERMDR-2026, title: "AI-augmented, still human-led: What changed in the 2026 Gartner Market Guide for MDR", publisher: Expel, type: vendor, url: "https://expel.com/blog/what-changed-in-the-2026-gartner-market-guide-for-managed-detection-and-response/", date: 2026-09-21, access: full, locator: "TL;DR; 'Gartner insights on AI MDR'" }
    - { ref: CLOUDSECPOD-MELLEN-2025, title: "The Truth About AI in the SOC: From Alert Fatigue to Detection Engineering", publisher: Cloud Security Podcast, type: podcast, url: "https://www.cloudsecuritypodcast.tv/videos/the-truth-about-ai-in-the-soc-from-alert-fatigue-to-detection-engineering", date: 2025-10-03, access: full, locator: "episode description (audio not heard)" }
  last_reviewed: 2026-10-17
  notes: "Vendor summary of a paywalled Gartner report; the Gartner document was not opened. Other MDR providers (Arctic Wolf, eSentire) market agentic SOC services but publish no measured outcomes in what was read."

- id: security-operations-17
  title: Evaluation scenarios and scorecards that gate how much authority an AI triage agent gets
  archetype: security
  module: operations
  function: technology-it
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "Vendors show cost and speed; accuracy on ambiguous, multi-plane attacks is rarely shown, and demos use curated alerts."
  solution: "Teams build replayable investigation scenarios with known dispositions and validation gates, scored by a grader model; Gartner (via Prophet) advises asking for benchmarks from similar environments and whether they came from a proof of concept or sustained production. Open benchmarks (SIABench, ALERT-BENCH, SOCBench) are emerging; SACR argues delegation should be decided one action at a time on evidence."
  outcomes:
    - lever: risk
      description: "In one hard scenario, most off-the-shelf frontier models graded the starting alert benign."
      figure: "5 of 7 models gave a false-positive or benign-positive disposition; best weighted score 29%"
      measures: "unsecure.sh: seven models run twice each in Cursor in August 2026 against one scenario with 16 weighted validation gates; hard fail if disposition is not True Positive; scorecard measures recall only"
      provenance: vendor-published
      source_ref: UNSECURE-EVAL-2026
  prerequisites:
    - "Genuine telemetry from played-out intrusions, a grader, and agreed gates."
  risks_and_guardrails:
    - "The scorecard has no penalty for wrong claims; authors note the common failure of implicating the legitimate developer (UNSECURE-EVAL-2026)."
    - "FIRST 2026 talk abstract says vendors promise AI-driven SOCs but 'measured evidence ... remains scarce' (FIRST-CON-2026)."
  human_checkpoints:
    - "Humans decide which actions are delegated and widen scope on evidence (SACR-TRUSTEDSOC-2026)."
  role_evolution: "Detection Engineering Weekly sees evals and harnesses commoditising as teams build their own (DETENGWEEKLY-169-2026)."
  evidence_grade: C
  sources:
    - { ref: UNSECURE-EVAL-2026, title: "A scenario to evaluate your Agentic SOC", publisher: unsecure.sh (John Ao, Michel San), type: vendor, url: "https://unsecure.sh/blog/agentic-soc-scenario/", date: 2026-08-27, access: full, locator: "'Validation gates' and 'How well do off-the-shelf agents perform?'" }
    - { ref: DETENGWEEKLY-169-2026, title: "DEW #169 - Realistic AI SOC evaluation scenarios, tricking EDRs with fake telemetry and Anthropic/OAI cyber eval guardrails", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-169-realistic-ai-soc-evaluation", date: 2026-09-03, access: full, locator: "Detection Engineering Gem" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: 'Can a General-Purpose LLM Do Tier-1 Triage?'", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "session abstract (2026-06-18)" }
    - { ref: SACR-TRUSTEDSOC-2026, title: "AI SOC Technoscope Series: Building the Trusted SOC (Part 1)", publisher: Software Analyst Cyber Research, type: firm, url: "https://softwareanalyst.substack.com/p/ai-soc-technoscope-series-building", date: 2026-07-27, access: full, locator: "'Trusted Security Response Operations'; 'The Practitioner Signal'" }
  last_reviewed: 2026-10-17
  notes: "The authors build a competing harness (Tengu) and the scenario favours it; the eval result is for raw models, not products. The FIRST session reports early findings from an ongoing experiment; results were not in the program text."

- id: security-operations-18
  title: Bounded-authority AI response - grant recommend, prepare, execute and verify one action at a time
  archetype: security
  module: operations
  function: technology-it
  work_types: [transaction-processing, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "AI shortened investigation but not the distance from a validated incident to a safe, verified, state-changing response (SACR's 'action gap')."
  solution: "SACR's Trusted Security Response Operations model grants software authority per action, with explicit evidence, policy, credential, scope and accountability requirements, and keeps fixed logic separate from model reasoning for repeatable containment. A research design confines the LLM to a closed vocabulary of templated actions with an argument validator."
  outcomes:
    - lever: risk
      description: "Guardrail proxy against adversarial alerts in a research test."
      figure: "injection recall 25.0% to 94.5% at 0.1% false-positive rate"
      measures: "arXiv 2610.09906: stock NeMo-Guardrails proxy on a SOC-specific adversarial corpus released by the authors; authors say rail latency keeps inline control out of scope"
      provenance: independent
      source_ref: ARXIV-2610.09906
  prerequisites:
    - "Per-action evidence, approval routing, credential separation, audit records and outcome verification (SACR-TRUSTEDSOC-2026)."
  risks_and_guardrails:
    - "Prophet survey: respondents grant human-approval-by-default with scope widening as track record accrues; none grants full autonomy (HNS-GARTNER-2026)."
    - "Gartner as quoted: distinguish 'human in the loop' from 'human on the loop' (HNS-GARTNER-2026)."
  human_checkpoints:
    - "Approval routing per action; reversibility and proof of execution (SACR-BHUSA-2026, 'AI SOC vendors have a differentiation problem')."
  role_evolution: "Operators decide a portfolio of narrow delegation decisions rather than one trust decision (SACR-TRUSTEDSOC-2026)."
  evidence_grade: C
  sources:
    - { ref: SACR-TRUSTEDSOC-2026, title: "AI SOC Technoscope Series: Building the Trusted SOC (Part 1)", publisher: Software Analyst Cyber Research, type: firm, url: "https://softwareanalyst.substack.com/p/ai-soc-technoscope-series-building", date: 2026-07-27, access: full, locator: "Key Actionable Summary; 'Defining Trusted Security Response Operations'" }
    - { ref: SACR-BHUSA-2026, title: "Black Hat USA 2026: Key Insights We're Observing For H2 2026", publisher: Software Analyst Cyber Research, type: firm, url: "https://softwareanalyst.substack.com/p/black-hat-usa-2026-key-insights-were", date: 2026-08-21, access: full, locator: "'Security Operations Center (The SOC) Trends'" }
    - { ref: ARXIV-2610.09906, title: "Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy", publisher: arXiv (Koutidis, Kekatos, Nianios, Lekidis), type: academic, url: "https://arxiv.org/abs/2610.09906", date: 2026-10-07, access: full, locator: abstract }
    - { ref: HNS-GARTNER-2026, title: "Gartner: 70% of SOCs will pilot AI agents. Only 15% will see results (sponsored, Prophet Security)", publisher: Help Net Security, type: press, url: "https://www.helpnetsecurity.com/2026/09/09/prophet-security-evaluating-ai-soc-agents/", date: 2026-09-09, access: full, locator: "section 5" }
  last_reviewed: 2026-10-17
  notes: "Analyst framework plus a research prototype; the authors of the arXiv paper say it is not a measured operational deployment. SACR is an independent analyst but its report is its own commentary."

- id: security-operations-19
  title: Analyst chat assistants for log analysis, threat explanation and report drafting
  archetype: security
  module: operations
  function: technology-it
  work_types: [research-synthesis, document-production]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Analysts need quick explanations, summaries and queries across many tools."
  solution: "Most SOCs use AI individually. Swimlane's reading of the SANS AI survey is that adoption comes easiest in log analysis, explaining threats and report writing. At a BSides Las Vegas 2026 talk, researchers who captured every AI request from 30 human and AI blue teams in competitions reported that AI triaged broken services from minimal input and filled knowledge gaps, but defenders mostly used it reactively like a search engine."
  outcomes:
    - lever: capacity
      description: "Use is widespread but not embedded."
      figure: "79% of SOCs use AI or ML tools; 36% have built AI tools into a defined SOC workflow"
      measures: "SANS 2026 SOC Survey: 444 practitioners and 69 cyber leaders; first figure counts SOCs using AI/ML tools for security operations, second counts those with AI built into a defined SOC workflow"
      provenance: independent
      source_ref: SANS-SOC-2026
  prerequisites:
    - "Acceptable-use policy and decisions about what data may be pasted into an assistant (not covered in the sources read)."
  risks_and_guardrails:
    - "SANS: most analysts use AI individually, without organisational structure or systematic validation (SANS-SOC-2026, FAQ)."
    - "BSides talk: safety filters blocked legitimate defender prompts hundreds of times while letting malicious ones through (BSIDESLV-2026)."
  human_checkpoints:
    - "Analyst remains the author of the work."
  role_evolution: "Not quantified; see module notes on workforce."
  evidence_grade: C
  sources:
    - { ref: SANS-SOC-2026, title: "SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense", publisher: SANS Institute, type: survey, url: "https://www.sans.org/research/security-operations-report", date: 2026-06, access: full, locator: "Top Takeaways; FAQs" }
    - { ref: SANS-AI-2026, title: "A SOC Leader's Guide to the 2026 SANS AI Survey", publisher: Swimlane, type: vendor, url: "https://swimlane.com/blog/sans-ai-2026-soc-trust/", date: 2026-08-17, access: full, locator: "'The Gap Between Adoption and Maturity'" }
    - { ref: BSIDESLV-2026, title: "BSides Las Vegas 2026: 'Agents Under Fire'", publisher: BSides Las Vegas, type: conference, url: "https://bsideslv.org/talks", date: 2026-08, access: full, locator: "talk abstract (Ground Truth track)" }
  last_reviewed: 2026-10-17
  notes: "SANS report page has no publication date; the survey insights webcast was listed for 2026-06-17 (search result), hence 2026-06. The BSides conclusions are from the abstract, not the talk."

- id: security-operations-20
  title: Staffing the SOC to build and supervise automation rather than watch the queue
  archetype: security
  module: operations
  function: technology-it
  work_types: [coordination-scheduling, software-systems]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Roles organised around manual triage are the smallest, lowest-paid and least automated family in SOC hiring, and entry-level seats are scarce."
  solution: "Job postings coded by D3 Security show teams hiring builders (SecOps, detection and automation engineers) at about three per queue-watching analyst, redefining the analyst tier around validating automated output, and moving entry seats to engineering tracks."
  outcomes:
    - lever: capacity
      description: "Hiring mix in a sample of US SOC postings."
      figure: "247 build-family postings vs 68 SOC analyst postings; entry-level 39 (5.9%); 22.7% with an active AI or automation requirement; 67% with no AI language"
      measures: "D3 Security: 665 in-scope US security operations postings coded from more than 1,000 read in full (collected August 2026); percentages are shares of the 665"
      provenance: vendor-published
      source_ref: D3-SOCHIRING-2026
  prerequisites:
    - "Detections-as-code skills (46% of plain SOC analyst postings mention it per D3)."
  risks_and_guardrails:
    - "D3 warns that teams cutting the junior seat will have no one ready for senior seats in three years (D3-SOCHIRING-2026)."
    - "Forrester heard vendors still hire early-career staff but in fewer numbers and worry about a 'five-year problem' with mid and senior staff adoption (FORRESTER-RSAC-2026)."
  human_checkpoints:
    - "Analyst tier validates AI output; a vendor of autonomous investigation employs tiered human analysts to check it (D3-SOCHIRING-2026)."
  role_evolution: "ISC2 2025: roles such as SOC analyst and incident responder are 'evolving'; the study moves from headcount to skills, with AI the top skills need at 41% (ISC2-WORKFORCE-2025). SANS: 32% of practitioners say management prioritises SOC staffing (SANS-SOC-2026)."
  evidence_grade: C
  sources:
    - { ref: D3-SOCHIRING-2026, title: "SOC Hiring in 2026: Three Builders for Every Analyst", publisher: D3 Security, type: job-posting, url: "https://d3security.com/blog/soc-hiring-2026/", date: 2026-09-11, access: full, locator: "findings 1-5" }
    - { ref: FORRESTER-RSAC-2026, title: "RSAC 2026: An AI Coming-Of-Age Story Without The Romance", publisher: Forrester, type: firm, url: "https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance", date: 2026-03-31, access: full, locator: "'Staffing shortages have been eclipsed by a shortage of open positions'" }
    - { ref: ISC2-WORKFORCE-2025, title: "2025 ISC2 Cybersecurity Workforce Study", publisher: ISC2, type: professional-body, url: "https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study", date: 2025-12-04, access: full, locator: "introduction; skills needs section" }
  last_reviewed: 2026-10-17
  notes: "Postings are a vendor-assembled sample from one month; the vendor sells an AI SOC product (it names its own product in the closing questions). Not representative of all employers."

- id: security-operations-21
  title: Skills and investigation guides attached to each detection so triage agents inherit analyst know-how
  archetype: security
  module: operations
  function: technology-it
  work_types: [document-production, software-systems]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Triage and tuning knowledge disappears when an analyst finishes their shift; every alert type gets its own template."
  solution: "Elastic's detection engineers write per-rule investigation guides that agents follow as primary instructions; Figma stores steering and procedural memory; a vendor (Vega) proposes a portable 'SKILL.md' package of triage, investigation and tuning work shipped with each rule. Detection Engineering Weekly calls this steering-as-code as the next step after detection-as-code."
  outcomes:
    - lever: quality
      description: "Elastic's accuracy gain included the investigation guide as one of several added context sources, not isolated."
      figure: "none isolated"
      measures: "Elastic reports 60% to 92% for all context additions together; the guide's separate effect is not reported"
      provenance: self-reported
      source_ref: ELASTIC-TRIAGE-2026
  prerequisites:
    - "Detection-as-code pipeline; engineers willing to write guides for AI as well as people."
  risks_and_guardrails:
    - "Steering memory can override agent behaviour if misused; keep precedent and policy separate (FIGMA-AGENTS-2026)."
  human_checkpoints:
    - "Engineers author and review guides and skills."
  role_evolution: "Detection engineers become authors of agent instructions (ELASTIC-TRIAGE-2026; DETENGWEEKLY-167-2026)."
  evidence_grade: C
  sources:
    - { ref: ELASTIC-TRIAGE-2026, title: "Inside Elastic's agentic SOC", publisher: Elastic Security Labs, type: vendor, url: "https://www.elastic.co/security-labs/blog/alert-triage-agentic-soc-self-correcting-agents", date: 2026-08-25, access: full, locator: "'Investigation guide lookup: Per-rule triage instructions'" }
    - { ref: DETENGWEEKLY-167-2026, title: "DEW #167", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-167-more-security-agentic-breaches", date: 2026-08-19, access: full, locator: "'Detection Skills by Vega Threat Research'" }
    - { ref: CLOUDSECPOD-RAMP-2026, title: "Why AI Can't Replace Detection Engineers: Build vs. Buy & The Future of SOC", publisher: Cloud Security Podcast, type: podcast, url: "https://www.cloudsecuritypodcast.tv/videos/why-ai-cant-replace-detection-engineers-build-vs-buy-the-future-of-soc", date: 2026-01-21, access: full, locator: "episode description (audio not heard)" }
  last_reviewed: 2026-10-17
  notes: "Grade C because the separate effect of guides is unmeasured and the Vega material is a vendor specification relayed by a newsletter."

- id: security-operations-22
  title: Active agentic defence - defender agents that contain an attack without a human in the loop
  archetype: security
  module: operations
  function: technology-it
  work_types: [expert-judgment]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Practitioners say models that find vulnerabilities outpace detection and patching, and that attackers are bound by no usage policy."
  solution: "Idea discussed publicly: guardrailed agents that stop an active attack without human intervention; a DARPA-derived programme planned to deploy red and blue team agents on digital twins of water systems to learn what blue agents need. No production deployment found in sources read."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "none"
      provenance: self-reported
      source_ref: DETENGWEEKLY-169-2026
  prerequisites:
    - "Trust in agent behaviour, not just capability (DETENGWEEKLY-169-2026)."
  risks_and_guardrails:
    - "Podcast guests said models are better at attacking than defending beyond scanning for vulnerabilities and misconfigurations (REGISTER-BHDC-2026)."
  human_checkpoints:
    - "Not defined; the idea is autonomous."
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: DETENGWEEKLY-169-2026, title: "DEW #169", publisher: Detection Engineering Weekly, type: community, url: "https://www.detectionengineering.net/p/dew-169-realistic-ai-soc-evaluation", date: 2026-09-03, access: full, locator: "section on OpenAI call for collective cyber defence" }
    - { ref: REGISTER-BHDC-2026, title: "Black Hat and DEF CON are AI conferences now, too (Kettle podcast transcript)", publisher: The Register, type: podcast, url: "https://www.theregister.com/security/2026/08/17/black-hat-and-def-con-are-ai-conferences-now-too/5288076", date: 2026-08-17, access: full, locator: "discussion of the water-utility programme and attack versus defence skill" }
  last_reviewed: 2026-10-17
  notes: "Idea, not a deployment. Evidence is practitioner commentary."
- id: security-operations-23
  title: AI investigation platform assisting analysts on escalated alerts (randomised comparison)
  archetype: security
  module: operations
  function: technology-it
  work_types: [expert-judgment, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Vendors claim AI SOC analysts help, but there was little controlled evidence on analyst speed and accuracy."
  solution: "In a CSA study with Dropzone AI, participants of varying SOC and incident-response experience investigated two escalated-alert scenarios (an AWS S3 bucket alert and a Microsoft Entra ID failed-login alert) either with an AI investigation platform or manually."
  outcomes:
    - lever: speed
      description: "AI-assisted investigations were completed faster in both scenarios."
      figure: "45% faster (scenario 1); 61% faster (scenario 2)"
      measures: "CSA: speed of AI-assisted vs manual investigations of escalated alerts, per scenario; 148 participants randomly assigned (July-August 2025); scored against expert-modelled ideal responses"
      provenance: independent
      source_ref: CSA-DROPZONE-2025
    - lever: quality
      description: "AI-assisted analysts scored higher on accuracy; manual analysts' report detail fell over the session."
      figure: "22% greater accuracy (scenario 1); 29% (scenario 2); manual group report detail down 27% and conclusion detail down 20%"
      measures: "CSA: accuracy scores of AI-assisted relative to manual analysts per scenario; detail drop measured for the manual group across the study"
      provenance: independent
      source_ref: CSA-DROPZONE-2025
  prerequisites:
    - "An AI investigation platform integrated with the alert sources."
  risks_and_guardrails:
    - "The study covered escalated investigations that needed analyst involvement, not auto-closed alerts (CSA-DROPZONE-2025)."
    - "Dropzone is a CSA corporate member that supports the project; CSA says it had no influence on content or editorial process, but the vendor promotes the result."
  human_checkpoints:
    - "Analyst remained the investigator and author of the conclusion."
  role_evolution: "CSA's quoted conclusion is that AI can improve human accuracy and speed while sustaining quality across repeated tasks (CSA-DROPZONE-2025)."
  evidence_grade: B
  sources:
    - { ref: CSA-DROPZONE-2025, title: "New Study from Cloud Security Alliance Finds AI Improves Analyst Accuracy, Speed, and Consistency in Security Investigations", publisher: Cloud Security Alliance, type: survey, url: "https://cloudsecurityalliance.org/press-releases/2025/10/07/new-csa-study-finds-ai-improves-analyst-accuracy-speed-and-consistency-in-security-investigations", date: 2025-10-07, access: full, locator: "Key findings list; methodology paragraph" }
    - { ref: CLOUDSECPOD-DROPZONE-2025, title: "AI Agents for SOC: Hype Curve vs. Measurable ROI", publisher: Cloud Security Podcast, type: podcast, url: "https://www.cloudsecuritypodcast.tv/videos/ai-agents-for-soc-hype-curve-vs-measurable-roi", date: 2025-10-28, access: full, locator: "episode description (audio not heard)" }
  last_reviewed: 2026-10-17
  notes: "Controlled experiment in two scenarios, not a production deployment, so it is capped at B even though it is measured. The full report was not opened; figures are from the CSA press release. Vendor-supported."

```

## 3. Module notes

### Processes and key steps (with work types)

- Detection engineering: write, test, tune and retire rules; check rules still see data (`software-systems`, `review-assurance`). Failure modes named by practitioners: disconnected, starved, missing fields, ingest-lag blind window (DETENGWEEKLY-165-2026).
- Alert triage (tier 1): enrich, compare with history, decide benign / escalate (`transaction-processing`).
- Investigation (tier 2/3): query across SIEM, EDR, identity and cloud; build a timeline (`research-synthesis`, `expert-judgment`).
- Case management and closure: document verdict, tune the rule (`document-production`, `data-reporting`).
- Response and containment actions (`expert-judgment`, `transaction-processing`).
- MDR: the same flow delivered as a service, with a client-facing step (`client-interaction`).

### Common pain points

- Alert volume and uninvestigated alerts: in a Prophet Security survey quoted in a sponsored article, 28% of alerts are never investigated and up to 40% of organisations have switched off rules for capacity reasons (HNS-GARTNER-2026).
- Metrics that measure activity: 70% of SANS respondents still name incident count as their top SOC metric (SANS-SOC-2026).
- Context gathering across tools: Figma and Elastic both say context, not model choice, was the limiting factor (FIGMA-AGENTS-2026, ELASTIC-TRIAGE-2026).
- Weak upstream detections cap downstream AI value; SACR reports AI SOC vendors moving left into detection engineering (SACR-TRUSTEDSOC-2026).
- Unrealistic "benign sets" make false-positive rates look better than they are (DETENGWEEKLY-164-2026).

### Metrics and benchmarks (with sources)

- SANS 2026 SOC Survey: 79% of SOCs use AI/ML tools; 36% built into a defined workflow; 70% cite incident count as top metric; 444 practitioners and 69 leaders (SANS-SOC-2026).
- SANS AI Survey via Swimlane: 63% report significant AI shortcomings in detecting or responding to threats; automated IR at 39% adoption (SANS-AI-2026).
- Prophet Security survey via Help Net Security (sponsored): 40% use AI daily; 56% evaluating or piloting; 72% of AI users cut investigation time by at least 25%; 72% of AI users tried building their own and 46% of builds were abandoned, never reached production or were replaced; 57% require human review of every AI decision before closing (HNS-GARTNER-2026).
- Gartner via same article: by 2028, 70% of large SOCs will pilot AI agents for Tier 1/2 work but only 15% will achieve measurable improvements without structured evaluation (HNS-GARTNER-2026).
- CSA/Dropzone randomised study (148 participants, July-Aug 2025, two escalated-alert scenarios): AI-assisted analysts 45-61% faster, 22-29% more accurate; manual group's report detail fell 27% and conclusion detail 20% (CSA-DROPZONE-2025). Vendor-supported; CSA says Dropzone had no influence on content.
- Elastic: AI verdict correctness 60% to 92% (ELASTIC-TRIAGE-2026). Figma: about 70% shorter time to resolution on complex alerts (FIGMA-AGENTS-2026).
- Independent or academic: ALERT-BENCH (every studied approach missed at least 40.4% of attack-related alerts) (ARXIV-2610.10608); log-substrate prompt injection study (below) (ARXIV-2605.24421); SIABench (11 LLMs, 25 deep-analysis and 135 triage scenarios; abstract gives no scores) (ARXIV-2603.06422); unsecure.sh scenario (UNSECURE-EVAL-2026).
- Named customer examples with no metrics: CrowdStrike's AgentWorks post names Pan-American Life Insurance Group (investigation reports with ATT&CK mapping) and Kroll (detection-engineering agent) (CROWDSTRIKE-AGENTWORKS-2026); Cisco and Splunk ran detection validation across more than 2,100 public detections during Black Hat 2026 (SPLUNK-BHUSA-2026, CISCO-BHUSA-2026).
- Quality evidence absent: no published override rates, no independent parallel-run results from a production SOC, no multi-organisation false-negative measurement. The CSA study and Elastic's correctness metric are the closest. SOCBench (DeepTempo) lists triage and investigation as roadmap items; only detection scores are published; its page is undated.

### Guardrails and regulatory points

- Treat logs and alerts as adversarial input. A study using one small model as the analyst found persona-hijack text suppressed 68% of malicious logs under a naive classifier, summarisation was the riskiest task (96% injection success without defences, 38% with constrained output), and the strongest defence still left 11.8% average success (ARXIV-2605.24421). FIRST 2026 sessions covered the same attack surface from NTT DATA (structured-data injection into DFIR agents) and CyCraft (a poisoned artifact steering retrieval and narrative) (FIRST-CON-2026).
- Deterministic limits outside the prompt: draft-only PRs, no ambient channel access, closed action vocabularies (FIGMA-AGENTS-2026, ARXIV-2610.09906).
- A third party reported that a vendor's SOC assistant could be steered by an alert into creating API keys (PROMPTARMOR-ELASTIC-2026). The vendor's reply is not in the sources.
- Gartner's evaluation questions (as relayed): reduce workload, meaningful outcomes, vendor viability, analyst elevation, autonomy boundaries, stack fit (HNS-GARTNER-2026). Gartner's MDR guide requires triage of all discovered threats regardless of priority (EXPEL-GARTNERMDR-2026).
- Evidence defensibility: Centene's FIRST 2026 session proposes OCSF-based timelines with hashing, confidence scoring and prompt traceability and refers to evidentiary standards (FIRST-CON-2026; abstract only).
- Regulation (EU AI Act, NIS2, DORA) is covered in the governance modules; no SOC-specific regulator statement was found in the discourse sources.

### Frontier signals (dated)

- 2026-03-31: Forrester says "agentic SOC" now means mostly "AI agents in general"; recommends weighing utility, trust and cost (FORRESTER-RSAC-2026).
- 2026-06-18/19: FIRST sessions on tier-1 triage with general LLMs, CoAnalyst (Cisco), and attacks on DFIR agents (FIRST-CON-2026).
- 2026-07-27 to 2026-08-21: SACR argues triage and investigation are commodity and the "action gap" and "proof gap" (execute, reverse, audit) are the new frontier (SACR-TRUSTEDSOC-2026, SACR-BHUSA-2026).
- 2026-08-27 to 2026-09-03: scenario evals spread; Detection Engineering Weekly says agent evals and harnesses are no longer a startup moat and teams build their own (UNSECURE-EVAL-2026, DETENGWEEKLY-169-2026).
- 2026-09-09: Gartner (via Prophet and Expel) places AI SOC agents at the Peak of Inflated Expectations and forecasts 90% of initial MDR findings handled by AI without human action by 2029 (HNS-GARTNER-2026, EXPEL-GARTNERMDR-2026).
- 2026-07-16: Hugging Face reports hosted-model guardrails blocked incident forensics and advises a vetted self-hostable model (HUGGINGFACE-INCIDENT-2026).
- 2026-09-15 to 2026-10-16: decision models proposed as cheap per-alert scorers (THN-DECISIONMODELS-2026).
- 2026-09-11: hiring shifts toward build roles (D3-SOCHIRING-2026).
- 2026-09-22: ISACA's State of Cybersecurity 2026 says AI adoption for automating security operations is accelerating while AI governance and incident-response maturity remain underdeveloped (ISACA-SOC-2026, landing page; full report gated).

### Workforce and role effects

- On-call and tier 1 shift from investigating to reviewing agent output (FIGMA-AGENTS-2026, SLACK-AGENTS-2025).
- Detection engineers write investigation guides and skills for agents (ELASTIC-TRIAGE-2026).
- Gartner-relayed survey: 57% expect AI to shift SOC roles without changing headcount over two years; 9% expect headcount to grow (HNS-GARTNER-2026).
- ISC2: AI is the top skills need (41%); respondents expect roles to evolve rather than disappear (ISC2-WORKFORCE-2025).
- Forrester at RSAC: vendors still hire early-career staff but fewer, and worry about mid and senior staff adoption (FORRESTER-RSAC-2026).
- Hiring data: entry-level roles 5.9% of 665 postings; zero-experience triage seats survive mainly at MSSPs, MDR providers, staffing contracts and state government (D3-SOCHIRING-2026).

### Objections and concerns practitioners raise

- "Faster to the wrong answer": AI SOCs depend on the data and context fed to them (RESILIENTCYBER-FASTER-2026; sponsored by Censys).
- Non-determinism: Swimlane argues analysts are non-deterministic too, so pair AI with deterministic guardrails (SANS-AI-2026).
- Sameness and "AI washing" (HNS-GARTNER-2026, SACR-BHUSA-2026); vendor sameness past the demo.
- Proof: headline metrics are not comparable because vendors define investigations, actions and time saved differently (SACR-TRUSTEDSOC-2026).
- Budget: SACR notes some agentic security spending comes from temporary transformation funds (SACR-BHUSA-2026).
- Market sprawl: SACR counts close to 140 vendors touching AI in security operations and treats more than 60 as pure-play AI SOC platforms; it ranked 18 in depth (SACR-TRUSTEDSOC-2026, SACR-AISOCMKT-2026).
- Sponsored podcast format: the Dropzone founder's Risky Business Soap Box asks whether the SOC as we know it will exist; description only, vendor-sponsored (RISKYBIZ-SOAPBOX108-2026).
- Skeptic-turned-adopter voice: a former Mandiant/Red Canary SOC lead describes himself as an AI skeptic who changed his view; episode description only (CLOUDSECPOD-PROPHET-2025).

### Interview probes for an advisor

1. Which alert types does an AI touch today, and how do you know its verdict agrees with your analysts' close reasons? Who scores that, and how often?
2. When your agent is wrong or says "benign", what second check exists, and what does a dismissal require that an escalation does not?
3. Which actions can the agent take without a person, written per action, and who can widen or withdraw that authority?
4. What happens if an attacker controls text in a log, email or alert your agent reads? What can the agent do with its credentials?
5. How has your tier-1 seat and your path to tier-2 changed, and who now writes the guides, runbooks and detections the agent relies on?

## 4. Routed to other modules

- **incident-response:** Hugging Face's use of a self-hostable model for forensics and its lessons on guardrail lockout (HUGGINGFACE-INCIDENT-2026); DNB incident notebooks (CAUCHY-IRNB-2026); FIRST sessions on AI-assisted IR timelines (Centene), PSIRT 2.0 agentic architecture (GMO Cybersecurity by IERAE and Ken Associates; reports 85% of APAC PSIRTs have fewer than five members) (FIRST-CON-2026); BSides "After the Jailbreak" PSIRT playbook (BSIDESLV-2026).
- **ai-security:** attacks on SOC AI (log-substrate prompt injection, DFIR agent manipulation, vendor SOC assistant weakness) (ARXIV-2605.24421, FIRST-CON-2026, PROMPTARMOR-ELASTIC-2026); agent containment incidents discussed at Black Hat and DEF CON (REGISTER-BHDC-2026, DETENGWEEKLY-167-2026); monitoring of coding agents with a CEL-rule EDR plugin (DETENGWEEKLY-166-2026).
- **threat-intelligence:** CoAnalyst and OSINT copilot sessions at FIRST (FIRST-CON-2026); external internet-intelligence argument (RESILIENTCYBER-FASTER-2026).
- **vulnerability-exposure / application-security:** BSides talk on multi-agent auto-triage of bug bounty reports at GM (BSIDESLV-2026).
- **security-governance-risk:** workforce data and the 8% AI-specific exercise finding (ISC2-WORKFORCE-2025, ISACA-SOC-2026).

## 5. Sources

Type counts are given at the end of this section. "Access: full" means the page was opened and read; podcast pages were read for show notes only (no audio or transcript, except The Register's Kettle transcript).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| SANS-SOC-2026 | SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense | SANS Institute | survey | https://www.sans.org/research/security-operations-report | 2026-06 (page undated; webcast listing 2026-06-17) | full (landing page) |
| SANS-AI-2026 | A SOC Leader's Guide to the 2026 SANS AI Survey | Swimlane | vendor | https://swimlane.com/blog/sans-ai-2026-soc-trust/ | 2026-08-17 | full |
| HNS-GARTNER-2026 | Gartner: 70% of SOCs will pilot AI agents. Only 15% will see results (sponsored by Prophet Security) | Help Net Security | press | https://www.helpnetsecurity.com/2026/09/09/prophet-security-evaluating-ai-soc-agents/ | 2026-09-09 | full |
| CSA-DROPZONE-2025 | New Study from CSA Finds AI Improves Analyst Accuracy, Speed, and Consistency (Beyond the Hype benchmark) | Cloud Security Alliance | survey | https://cloudsecurityalliance.org/press-releases/2025/10/07/new-csa-study-finds-ai-improves-analyst-accuracy-speed-and-consistency-in-security-investigations | 2025-10-07 | full (press release; full report not opened) |
| ISC2-WORKFORCE-2025 | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full |
| ISACA-SOC-2026 | State of Cybersecurity 2026 report (landing page) | ISACA | professional-body | https://www.isaca.org/resources/reports/state-of-cybersecurity-2026 | 2026-09-22 | full (summary only; report gated) |
| FIRST-CON-2026 | 38th Annual FIRST Conference program | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06 | full (abstracts) |
| BSIDESLV-2026 | BSides Las Vegas 2026 talks | BSides Las Vegas | conference | https://bsideslv.org/talks | 2026-08 | full (abstracts) |
| FORRESTER-RSAC-2026 | RSAC 2026: An AI Coming-Of-Age Story Without The Romance | Forrester | firm | https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance | 2026-03-31 | full |
| SPLUNK-RSACSOC-2026 | From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC | Splunk | vendor | https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html | 2026-08-24 | full |
| SPLUNK-BHUSA-2026 | Black Hat USA 2026: Proving the Splunk ES Foundation for the Agentic SOC | Splunk | vendor | https://www.splunk.com/en_us/blog/security/black-hat-usa-2026-proving-the-splunk-es-foundation-for-the-agentic-soc.html | 2026-09-23 | full |
| CISCO-BHUSA-2026 | Black Hat USA 2026: Building the Agentic SOC, One Live Event at a Time | Cisco Blogs | vendor | https://blogs.cisco.com/security/bhusa-2026-soc | 2026-09 | full |
| CISCO-SPLUNK-CONF26-2026 | Splunk .conf26: Tracking the Triage Agent in the Agentic SOC | Cisco Blogs | vendor | https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/ | 2026-10-08 | full |
| FIGMA-AGENTS-2026 | How we secure Figma's internal systems with agents | Figma | firm | https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/ | 2026-07-29 | full |
| ELASTIC-TRIAGE-2026 | Inside Elastic's agentic SOC: How we took AI alert triage from 60% to 92% accuracy | Elastic Security Labs | vendor | https://www.elastic.co/security-labs/blog/alert-triage-agentic-soc-self-correcting-agents | 2026-08-25 | full |
| PROMPTARMOR-ELASTIC-2026 | Elastic AI SOC Exfiltrates Credentials | PromptArmor | vendor | https://www.promptarmor.com/resources/elastic-agentic-soc-vulnerable-to-credential-theft | 2026-09-28 | full |
| SLACK-AGENTS-2025 | Streamlining Security Investigations with Agents | Slack Engineering | firm | https://slack.engineering/streamlining-security-investigations-with-agents/ | 2025-12-01 | full |
| GROWTHERAPY-HUNT-2026 | Threat hunt AI: How we built an AI security analyst on AWS for under $500/month | Grow Therapy engineering | firm | https://engineering.growtherapy.com/post/threat-hunt-ai-how-we-built-an-ai-security-analyst-on-aws-for-under-500-month | 2026-08 (undated; featured 2026-08-19) | full |
| CAUCHY-DETVAL-2026 | End-to-end detection validation using coding agents | DNB Cyber Defense Center (K. W. Kongsgard) | firm | https://blog.cauchy.org/blog/detection-validation/ | 2026-06-16 | full |
| CAUCHY-IRNB-2026 | Agentic incident response notebooks | DNB Cyber Defense Center (K. W. Kongsgard) | firm | https://blog.cauchy.org/blog/incident-response-notebooks/ | 2026-06-19 | full |
| HUGGINGFACE-INCIDENT-2026 | Security incident disclosure - July 2026 | Hugging Face | firm | https://huggingface.co/blog/security-incident-july-2026 | 2026-07-16 | full |
| EXPEL-RUXIE-2026 | New Ruxie AI power-up: Precedent engine | Expel | vendor | https://expel.com/blog/new-ruxie-ai-power-up-precedent-engine/ | 2026-09-10 | full |
| EXPEL-GARTNERMDR-2026 | AI-augmented, still human-led: What changed in the 2026 Gartner Market Guide for MDR | Expel | vendor | https://expel.com/blog/what-changed-in-the-2026-gartner-market-guide-for-managed-detection-and-response/ | 2026-09-21 | full |
| CROWDSTRIKE-REASONING-2026 | Teaching AI to Reason Through Detection Triage | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/teaching-ai-to-reason-through-detection-triage/ | 2026-08-17 | full |
| CROWDSTRIKE-AGENTWORKS-2026 | How AI-Leading Security Teams Are Building the Agentic SOC | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/ | 2026-07-06 (listing date) | full |
| UNSECURE-EVAL-2026 | A scenario to evaluate your Agentic SOC | unsecure.sh (J. Ao, M. San) | vendor | https://unsecure.sh/blog/agentic-soc-scenario/ | 2026-08-27 | full |
| THN-DECISIONMODELS-2026 | AI Decision Models and Their Impact on AI SOC Platforms (contributed by Intezer) | The Hacker News | press | https://thehackernews.com/2026/10/ai-decision-models-and-their-impact-on.html | 2026-10-16 | full |
| REGISTER-BHDC-2026 | Black Hat and DEF CON are AI conferences now, too (Kettle transcript) | The Register | podcast | https://www.theregister.com/security/2026/08/17/black-hat-and-def-con-are-ai-conferences-now-too/5288076 | 2026-08-17 | full |
| RISKYBIZ-854-2026 | Risky Business #854 -- We're Jevpilled | Risky Business | podcast | https://risky.biz/RB854/ | 2026-09-23 | full (show notes only) |
| RISKYBIZ-SOAPBOX108-2026 | Soap Box: Detection and response in the AI age (sponsored; Dropzone founder) | Risky Business | podcast | https://risky.biz/SOAPBOX108/ | 2026-06-05 | full (show notes only) |
| CLOUDSECPOD-MELLEN-2025 | The Truth About AI in the SOC: From Alert Fatigue to Detection Engineering (Forrester's Allie Mellen) | Cloud Security Podcast | podcast | https://www.cloudsecuritypodcast.tv/videos/the-truth-about-ai-in-the-soc-from-alert-fatigue-to-detection-engineering | 2025-10-03 (first date on page) | full (description only) |
| CLOUDSECPOD-PROPHET-2025 | How to Build Trust in an AI SOC for Regulated Environments | Cloud Security Podcast | podcast | https://www.cloudsecuritypodcast.tv/videos/how-to-build-trust-in-an-ai-soc-for-regulated-environments | 2025-11-18 (first date on page) | full (description only) |
| CLOUDSECPOD-RAMP-2026 | Why AI Can't Replace Detection Engineers: Build vs. Buy & The Future of SOC | Cloud Security Podcast | podcast | https://www.cloudsecuritypodcast.tv/videos/why-ai-cant-replace-detection-engineers-build-vs-buy-the-future-of-soc | 2026-01-21 (first date on page) | full (description only) |
| CLOUDSECPOD-DROPZONE-2025 | AI Agents for SOC: Hype Curve vs. Measurable ROI | Cloud Security Podcast | podcast | https://www.cloudsecuritypodcast.tv/videos/ai-agents-for-soc-hype-curve-vs-measurable-roi | 2025-10-28 (first date on page) | full (description only) |
| DETENGWEEKLY-162-2026 | DEW #162 | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-162-detonating-ttps-with-agents | 2026-07-08 | full |
| DETENGWEEKLY-164-2026 | DEW #164 - Your Benign Set Stinks | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-164-your-benign-set-stinks-openai | 2026-07-22 | full |
| DETENGWEEKLY-165-2026 | DEW #165 | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-165-starved-and-neglected-rules | 2026-07-29 | full |
| DETENGWEEKLY-166-2026 | DEW #166 | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-166-figmas-agentic-secops-ai | 2026-08-05 | full |
| DETENGWEEKLY-167-2026 | DEW #167 | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-167-more-security-agentic-breaches | 2026-08-19 | full |
| DETENGWEEKLY-169-2026 | DEW #169 | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-169-realistic-ai-soc-evaluation | 2026-09-03 | full |
| SACR-TRUSTEDSOC-2026 | AI SOC Technoscope Series: Building the Trusted SOC (Part 1) | Software Analyst Cyber Research | firm | https://softwareanalyst.substack.com/p/ai-soc-technoscope-series-building | 2026-07-27 | full |
| SACR-AISOCMKT-2026 | AI SOC Technoscope Series: The AI SOC Market, 2026 (Part 2) | Software Analyst Cyber Research | firm | https://softwareanalyst.substack.com/p/ai-soc-technoscope-series-the-ai | 2026-07-30 | full (introduction read; rankings not used) |
| SACR-BHUSA-2026 | Black Hat USA 2026: Key Insights We're Observing For H2 2026 | Software Analyst Cyber Research | firm | https://softwareanalyst.substack.com/p/black-hat-usa-2026-key-insights-were | 2026-08-21 | full |
| RESILIENTCYBER-FASTER-2026 | Faster to the Wrong Answer (partner content with Censys) | Resilient Cyber | community | https://www.resilientcyber.io/p/faster-to-the-wrong-answer | 2026-10-14 | full |
| D3-SOCHIRING-2026 | SOC Hiring in 2026: Three Builders for Every Analyst | D3 Security | job-posting | https://d3security.com/blog/soc-hiring-2026/ | 2026-09-11 | full |
| ARXIV-2610.10608 | From Investigation Failures to Reliable SOC Agents (ALERT-BENCH, AIDA) | arXiv | academic | https://arxiv.org/abs/2610.10608 | 2026-10-07 | full (abstract) |
| ARXIV-2605.24421 | Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations | arXiv | academic | https://arxiv.org/abs/2605.24421 | 2026-05-23 | full (abstract) |
| ARXIV-2603.06422 | Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis (SIABench) | arXiv | academic | https://arxiv.org/abs/2603.06422 | 2026-03-06 | full (abstract) |
| ARXIV-2510.00311 | CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage | arXiv | academic | https://arxiv.org/abs/2510.00311 | 2025-09-30 | full (abstract) |
| ARXIV-2610.09906 | Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy | arXiv | academic | https://arxiv.org/abs/2610.09906 | 2026-10-07 | full (abstract) |
| SOCBENCH-2026 | SOCBench: AI Cyber Operations Benchmark (DeepTempo) | SOCBench | community | https://socbench.org/ | 2026 (page undated) | full (home page) |

Counts of distinct sources by type (51 listed, 12 vendor-authored refs flagged `vendor`): vendor 12; firm 10 (in-house engineering blogs, Forrester, SACR); community 8 (six newsletter issues, Resilient Cyber, SOCBench); podcast 7; academic 5; survey 2; press 2; professional-body 2; conference 2; job-posting 1; regulator 0; standard-setter 0. Five or more source types are present; there are no regulator or standard-setter sources because this angle is practitioner discourse (governance modules cover them).

## 6. Gaps

- **Independent quality measurement:** no published override rates, false-negative rates or parallel-run results from a named production SOC. The CSA/Dropzone study is vendor-supported and experimental; Elastic and Figma figures are self-reported.
- **Community discussion:** Reddit (login wall, jina mirror blocked), Medium (Cloudflare block; Anton Chuvakin's blog not read) and Hacker News (searched; thin, mostly Show HN posts) gave no usable practitioner threads. Detection Engineering Weekly's own Reddit digest was the only community-thread source and was read second-hand.
- **Podcast depth:** Risky Business and Cloud Security Podcast pages give show notes only; no transcripts or audio were available, so no podcast claim is attributed beyond the description.
- **Paywalled or gated:** Gartner Hype Cycle and MDR Market Guide, Forrester research, the SANS 2026 SOC and AI survey full reports, Prophet's State of AI in Security Operations, CSA's full benchmark report, ISACA State of Cybersecurity full report, Intezer's AI SOC Report 2026, Latio's AI security market report. Figures from these appear only as relayed by vendors or press and are labelled so.
- **Conference sessions:** official Black Hat USA 2026, RSAC 2026 and Gartner SRM session lists and recordings were not reachable. FIRST and BSides abstracts were read, but slides and results were not.
- **Dates not on the page:** SANS 2026 SOC Report (2026-06 inferred from a webcast listing found by search), Grow Therapy post (before 2026-08-19 via the newsletter that featured it), SOCBench (undated), Cloud Security Podcast episodes (first date string on the page), Cisco Black Hat post (metadata shows 2026-09-07 and 2026-09-24).
- **Not found:** MDR provider outcome data beyond Expel's single MTTR claim; cost-per-investigation or token-cost data beyond Grow Therapy and the decision-model article; any regulator statement specific to AI in SOC operations; evidence on small and mid-size security teams; Microsoft and Google primary sources on their own SOC agents.
- **Terminology anomaly from the landscape file** (CISA/NIST pages showing "Super Intelligence") was not encountered in the sources read here, except that the Resilient Cyber newsletter archive uses "SI Force Mandate" in a headline.
