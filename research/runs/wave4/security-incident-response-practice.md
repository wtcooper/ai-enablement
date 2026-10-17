# Security archetype, incident-response module: practice angle (wave 4)

Compiled 2026-10-17 by a research analyst. Module: incident response, digital forensics, recovery and resilience (BC/DR as it relates to cyber incidents), tabletop exercises, incident reporting obligations, and AI in investigation, timelines and reporting. Angle: practice (what teams and providers actually do).

## 1. Summary

**What the evidence shows.** Public, named evidence for AI in incident response is thin in the places that matter most for a decision to adopt: measured quality of AI-produced investigation outputs, override or acceptance rates, and parallel-run results are almost entirely absent. The strongest measured result is still Google's 2024 trial of LLM-drafted incident summaries (51% less time per summary, 300 summaries; 53% less time on executive updates). The strongest 2026 practice case is OpenAI's staged AI review of about 50 petabytes of model-activity records to find outside organisations that needed notice (over 100 notified), with a human investigator confirming every case; it publishes counts and compute cost but no accuracy figures.

**Where the work changes.** (1) Writing: summaries, executive updates, incident reports and notification drafts. (2) Reconstruction: timelines, narratives and root-cause tracing over logs and forensic artifacts. (3) Evidence triage: natural-language search with citations in forensic platforms. (4) Preparation: plan review and AI-built tabletop scenarios. (5) Recovery: scoping what to restore and from where. (6) New scope: incidents caused by AI agents, which now need agent action logs, scoped agent identities, stop rules, and new reporting norms (CERT-In advisory 2026-10-15, the SAFE draft of August 2026, OpenAI's notification standard).

**Count and grades.** 19 candidate use cases: 2 grade A, 6 grade B, 10 grade C, 1 grade D (idea). Most grade C items, and the job-posting-based item 14 (grade B), rest on conference abstracts, vendor product pages or job postings, so they show intent or capability, not outcomes.

**Practice pattern.** Vendors and in-house teams converge on one operating rule: the AI prepares, a person decides and signs. That rule appears in Google's summary tool, the Magnet and Microsoft documentation, Immersive's builder, the D3 filing workflow, OpenAI's human review of every flagged case, and the Cisco/Splunk event SOC.

**Reliability limits found.** On a public benchmark, even the best of 11 LLMs fully solved only 8 of 25 incident-analysis scenarios (ARXIV-2603.06422). In an alert-triage benchmark, every studied agent approach missed at least 40.4% of attack-related alerts (ARXIV-2610.10608). The tools are themselves attackable through the logs and artifacts they read (ARXIV-2605.24421; FIRST-CON-2026).

**Caveats.** Web search was used seven times; all other sources were opened with curl, the r.jina.ai mirror or the Greenhouse job-board API. Two items in the landscape file were corrected after opening them: the Cisco/Splunk RSAC SOC post is dated 2026-08-24 (landscape said March) and its time saving came from a SOAR playbook, not AI; and the Gartner/Sygnia search snippets were not used as evidence. Vendors' agentic terms are used loosely; this file records what the source says the system does.

## 2. Use cases

```yaml
- id: security-incident-response-01
  title: Draft incident summaries and executive updates from the case record, with the incident commander editing
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [document-production, data-reporting]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Incident commanders spend close to an hour (more for complex cases) writing summaries for executives, leads and partner teams from free-text, logs, impact notes and timelines scattered across the case."
  solution: "A 'Generate Summary' control in the incident tool pre-fills a draft from the structured case fields. The responder accepts it, edits it or discards it. Inputs are tagged to mirror the incident communication template, long log and code sections are replaced by placeholders, and the model is not called when the input is under 200 tokens. A follow-on experiment drafted executive communications (summary, root cause, impact, mitigation). Vendor consoles now ship similar summary and report generation (Microsoft documents an incident summary for incidents of up to 100 alerts and a consolidated incident report)."
  outcomes:
    - lever: speed
      description: "Time saved per incident summary drafted with the LLM versus written by a human"
      figure: "51%"
      measures: "Reduction in time per incident summary, LLM-drafted versus human-written (sample size 300 summaries, per the post's chart caption)"
      provenance: self-reported
      source_ref: GOOGLE-IRGENAI-2024
    - lever: quality
      description: "Blind comparison of 50 human-written and 50 LLM-written summaries rated by security teams"
      figure: "rated 10% higher than the human-written equivalents; drafting time cut in half"
      measures: "Reviewer rating of LLM-written versus human-written summaries; time to draft (50 human and 50 LLM summaries, author not disclosed to raters)"
      provenance: self-reported
      source_ref: GOOGLE-IRGENAI-2024
    - lever: speed
      description: "Executive communications drafted on behalf of the incident commander (an experiment, not the summary tool)"
      figure: "53%"
      measures: "Reduction in time incident commanders spent writing executive summaries, with quality 'at least on-par' for factual accuracy and writing guidelines"
      provenance: self-reported
      source_ref: GOOGLE-IRGENAI-2024
  prerequisites:
    - "Structured incident records that mirror the communication template (title, actions taken, impact, mitigation history)"
    - "Pipeline with logging off and no use of inputs or outputs for model retraining, because incidents hold confidential, sensitive and privileged data"
    - "A set of human-written example summaries to include in the prompt"
  risks_and_guardrails:
    - "Every LLM draft must be reviewed by a human; Google also notes that humans can misread an LLM statement (GOOGLE-IRGENAI-2024, section 'Managing risks and protecting privacy')"
    - "Hallucination edge case when the input is small relative to the prompt; fixed by not calling the LLM below 200 tokens (GOOGLE-IRGENAI-2024, section 'Quantitative wins')"
    - "Earlier prompt versions drew conclusions on hypotheses and struggled to stick to the latest updates (GOOGLE-IRGENAI-2024, 'Prompt engineering')"
  human_checkpoints:
    - "Responder accepts, edits or discards the pre-filled draft before it is added to the incident"
  role_evolution: "The incident commander moves from writing each update to reviewing and correcting a draft, and keeps accountability for what is sent (GOOGLE-IRGENAI-2024, 'Workflow integration')."
  evidence_grade: A
  sources:
    - { ref: GOOGLE-IRGENAI-2024, title: "Accelerating incident response using generative AI", publisher: "Google Online Security Blog", type: firm, url: "https://security.googleblog.com/2024/04/accelerating-incident-response-using.html", date: "2024-04-26", access: full, locator: "Sections 'Humans vs. LLMs', 'Workflow integration', 'Quantitative wins', 'Evolving to more complex use cases'" }
    - { ref: MS-LEARN-DEFENDERCOPILOT-2026, title: "Describe Copilot in Microsoft Defender XDR", publisher: "Microsoft Learn", type: vendor, url: "https://learn.microsoft.com/en-us/training/modules/security-copilot-embedded-experiences/2-copilot-for-defender", date: "2026-05-01", access: full, locator: "Sections 'Summarize incidents' and 'Create incident reports'" }
  last_reviewed: 2026-10-17
  notes: "The Google evidence is from April 2024, older than the 18-month window; kept as the best measured case. The 51% and 10% figures are Google's own and unreplicated. The Microsoft page is product documentation and gives no outcome figures or named customer."

- id: security-incident-response-02
  title: Reconstruct attack timelines and narratives from normalised logs and forensic artifacts with an LLM agent
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [research-synthesis, data-reporting]
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "Digital incident timeline analysis can take investigators weeks on difficult cases, sifting hundreds of millions of log records from hundreds of unfamiliar log types (Google talk abstract)."
  solution: "An agent runs forensic analysis over super-timelines and logs, finds and explains evidence of compromise without predefined signatures, and surfaces findings in the Timesketch investigator interface (Google, Sec-Gemini agent with a Timesketch AI panel). Centene's FIRST 2026 session describes a six-layer pipeline (ingest, normalise to OCSF, AI assist, validate, timeline, export) in which LLMs help with field inference, clustering and narrative while the analyst keeps decision authority and every transformation is versioned and hash-verified."
  outcomes:
    - lever: quality
      description: "Evaluation on a dataset of 100 real-world compromised systems; the authors report high recall and precision on finding and contextualising individual log records tied to the attack chain (numeric values not read in the talk abstract)"
      figure: "none published in the source read"
      measures: "Recall and precision of individual attack-related log records on 100 compromised systems (figures in the slide deck, which was not opened)"
      provenance: self-reported
      source_ref: GOOGLE-TIMESKETCH-2025
  prerequisites:
    - "Log and artifact normalisation (Plaso, OCSF or similar) before the model sees the data"
    - "Validation layer and prompt and workflow logging so outputs can be audited and reproduced (FIRST-CON-2026, Centene session)"
  risks_and_guardrails:
    - "Prompt injection through forensic artifacts: an NTT DATA FIRST 2026 session says it demonstrates structured-data injection against DFIR LLM agents (outcomes it names are hide, mislead and exploit) and recommends least privilege, structured-output validation and human-in-the-loop checks (FIRST-CON-2026)"
    - "An arXiv benchmark finds that even the best of 11 LLMs fully solved only 8 of 25 incident-analysis scenarios (ARXIV-2603.06422, Section V results)"
  human_checkpoints:
    - "Investigators inspect findings in the Timesketch AI panel and work the case from there (GOOGLE-TIMESKETCH-2025)"
    - "Analyst retains decision authority in the Centene pipeline (FIRST-CON-2026)"
  role_evolution: "Centene's presenter bio describes analysts moving from reactive responders to supervisory decision-makers; this is the speaker's own framing, not a measured effect (FIRST-CON-2026)."
  evidence_grade: B
  sources:
    - { ref: GOOGLE-TIMESKETCH-2025, title: "Autonomous Timeline Analysis and Threat Hunting (Black Hat USA 2025 talk page)", publisher: "Elie Bursztein, with Google co-authors", type: conference, url: "https://elie.net/talk/autonomous-timeline-analysis-and-threat-hunting-an-ai-agent-for-timesketch", date: "2025-08-06", access: full, locator: "Talk abstract and 'Available Media'" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program (Centene: From Logs to Living Timelines; NTT DATA: The Dark Side of Autonomy)", publisher: "FIRST", type: conference, url: "https://www.first.org/conference/2026/program", date: "2026-06", access: full, locator: "Session abstracts for the Centene and NTT DATA sessions; conference held 14-19 June 2026" }
    - { ref: ARXIV-2603.06422, title: "Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis", publisher: "arXiv (Jajodia, Sultana, Majumdar, Taylor)", type: academic, url: "https://arxiv.org/abs/2603.06422", date: "2026-03-06", access: full, locator: "Abstract; Section V results (HTML version)" }
  last_reviewed: 2026-10-17
  notes: "Grade B: named organisations and a described evaluation, but no numeric outcome was read. The Centene item is a conference abstract (TLP:CLEAR); the speaker bio claims 'hours to minutes' compression but that is a bio statement, not an outcome, and is not used as one. The elie.net page carried embedded text addressed to AI agents; it was ignored."

- id: security-incident-response-03
  title: Generate evidence-linked investigative leads across collected endpoint and case data in a forensic platform
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "After remote collection from an affected host, establishing what happened and when can take days of manual review before leadership can be briefed or a containment decision made (Magnet Forensics scenario)."
  solution: "Investigators run plain-language queries over collected evidence in Magnet Review; the product's 'Intelligent Insights' runs concurrent analyses and returns a structured summary (flagged IPs, connection patterns, suggested next lines of inquiry) with citations linked to the underlying artifacts. The vendor says outputs are leads, not conclusions, and every finding is validated against source artifacts."
  outcomes:
    - lever: capacity
      description: "Vendor survey of enterprise DFIR professionals on AI use in investigations"
      figure: "68%"
      measures: "Share of the more than 350 enterprise DFIR professionals surveyed for the 2026 State of Enterprise DFIR report who say they use AI as part of their investigations (a 'more than threefold' rise from two years earlier, per the vendor)"
      provenance: vendor-published
      source_ref: MAGNET-DFIR-2026
  prerequisites:
    - "Evidence collected into the platform (Magnet Axiom Cyber or Magnet Nexus remote collection, then Magnet Review)"
    - "A written record of which tasks were AI-assisted, which models and controls were used, how outputs were validated and what data was processed"
  risks_and_guardrails:
    - "Non-adopters cite result validity, legal exposure, data security and handling of personal information (MAGNET-DFIR-2026, section 'Why 32% ... haven't adopted AI')"
    - "Teams should be able to answer legal, executive, regulator or opposing-counsel questions about AI use (MAGNET-DFIR-2026, 'Why governance is the defining issue')"
  human_checkpoints:
    - "Investigator validates every AI finding against source artifacts before it informs scoping, CISO briefings or decisions by IR, legal or risk teams"
  role_evolution: "Respondents rate evidence collection, initial case assessment and data analysis as the tasks that most need human intuition; AI is used mostly for text and image analysis, pattern recognition and classification (MAGNET-DFIR-2026, 'Where AI fits and where it doesn't')."
  evidence_grade: C
  sources:
    - { ref: MAGNET-DFIR-2026, title: "AI in enterprise DFIR: Moving fast, staying defensible", publisher: "Magnet Forensics", type: vendor, url: "https://www.magnetforensics.com/blog/ai-in-enterprise-dfir-moving-fast-staying-defensible/", date: "2026-05-08", access: full, locator: "Key insights; sections 'Where AI fits', 'Using AI in an enterprise investigation', 'Why governance is the defining issue'" }
    - { ref: MAGNET-AI-2026, title: "Magnet AI for Digital Forensics", publisher: "Magnet Forensics", type: vendor, url: "https://www.magnetforensics.com/magnet-ai/", date: "2026-10", access: full, locator: "Product page text on natural-language search, generated insights and citation verification; no publication date on the page, accessed 2026-10-17" }
  last_reviewed: 2026-10-17
  notes: "No named customer deployment or timing result was found. The 68% survey figure is a vendor-run survey and shows adoption, not outcomes. The full State of Enterprise DFIR report was not opened."

- id: security-incident-response-04
  title: Triage infostealer log corpora and infection screenshots with an LLM forensic tool
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Over 50 million stealer logs were posted in 2025 alone, which the speaker describes as an analysis bottleneck that manual work cannot meet; the logs hold untapped forensic artifacts about infection vectors and campaigns."
  solution: "StealerLens, from the threat-intelligence vendor Flare, is described as an LLM-powered forensic tool that speeds infostealer log investigations, building on the same team's Black Hat USA 2025 work on LLM-based analysis of infection screenshots."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Not applicable; the source is a session abstract that introduces the tool and gives no result"
      provenance: vendor-published
      source_ref: FIRST-CON-2026
  prerequisites:
    - "Access to stealer-log corpora and screenshots handled under the vendor's data rules"
  risks_and_guardrails:
    - "Artifacts from adversary-controlled sources are untrusted input to the model (see FIRST-CON-2026 session on poisoned artifacts steering LLM-assisted workflows)"
  human_checkpoints:
    - "Not described in the abstract"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program (Flare: Introducing StealerLens)", publisher: "FIRST", type: conference, url: "https://www.first.org/conference/2026/program", date: "2026-06", access: full, locator: "StealerLens session abstract" }
  last_reviewed: 2026-10-17
  notes: "Abstract only; nothing on adoption, accuracy or customers. This is also a threat-intelligence-adjacent use (stealer-log analysis)."

- id: security-incident-response-05
  title: Trace attack root cause by LLM-guided backtracking over provenance graphs
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [research-synthesis, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: "Provenance-based attack investigation is held back in practice by dependency explosions and fragmented causal chains; an unnamed large internet company's SOC processes tens of thousands of raw alerts daily and leaves thousands for manual triage."
  solution: "SherAgent iteratively queries and filters a provenance graph, uses an LLM to read unstructured context and threat intelligence, widens queries when events are missing and selects the next nodes to explore. The authors collaborated with the SOC of the unnamed company and refined its existing LLM-based investigation workflow."
  outcomes:
    - lever: quality
      description: "End-to-end investigation success rate against a legacy enterprise baseline and a state-of-the-art approach"
      figure: "improves by 31.1% (vs legacy enterprise baselines) and 63.7% (vs state of the art)"
      measures: "Improvement in end-to-end investigation success rate, in-the-wild evaluation at the unnamed company (abstract does not say whether the percentages are relative or absolute)"
      provenance: independent
      source_ref: ARXIV-2607.09176
    - lever: cost
      description: "Cost and time per investigation"
      figure: "under USD 0.10 in API cost; under 4 minutes"
      measures: "Per-investigation API cost and elapsed time as stated in the abstract"
      provenance: independent
      source_ref: ARXIV-2607.09176
  prerequisites:
    - "Provenance-graph data collection"
  risks_and_guardrails:
    - "Authors' own evaluation; deploying organisation is not named"
  human_checkpoints:
    - "A user study with security experts is reported; the checkpoint design is not described in the abstract"
  role_evolution: "The abstract says the user study found the tool reduces analyst overhead (figures not given)."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2607.09176, title: "SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking", publisher: "arXiv (Li, Wang, Jiang, Shen et al.)", type: academic, url: "https://arxiv.org/abs/2607.09176", date: "2026-07-10", access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: "Provenance is academic, so figures are marked independent in the sense of authors outside the vendor, but the evaluation is the authors' own and the host organisation is unnamed; capped at C because no named deployment exists. Abstract only."

- id: security-incident-response-06
  title: Recommend triage, containment, investigation and remediation actions inside the incident console
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [expert-judgment, coordination-scheduling]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: "Responders must decide quickly how to classify an incident and what to contain, and the right steps depend on past similar cases and the organisation's own response rules."
  solution: "Microsoft documents 'guided responses' in Copilot for Defender: recommended actions in four categories (triage, containment, investigation, remediation), each card explaining why the action is recommended. Administrators can upload organisation-specific response guidelines. Documented for incident types such as phishing, business email compromise and ransomware."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Not applicable; product documentation gives no results"
      provenance: vendor-published
      source_ref: MS-LEARN-DEFENDERCOPILOT-2026
  prerequisites:
    - "Incident data in Microsoft Defender XDR and Sentinel; optional uploaded response guidelines"
  risks_and_guardrails:
    - "Not all incidents or alerts produce guided responses (MS-LEARN-DEFENDERCOPILOT-2026, 'Guided responses')"
    - "Research shows a single adversarial alert can become a path to an unsafe action if the model's output is executed (ARXIV-2610.09906)"
  human_checkpoints:
    - "Recommendations are cards for the analyst to act on; execution is by the analyst"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: MS-LEARN-DEFENDERCOPILOT-2026, title: "Describe Copilot in Microsoft Defender XDR", publisher: "Microsoft Learn", type: vendor, url: "https://learn.microsoft.com/en-us/training/modules/security-copilot-embedded-experiences/2-copilot-for-defender", date: "2026-05-01", access: full, locator: "Section 'Guided responses'" }
    - { ref: ARXIV-2610.09906, title: "Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy", publisher: "arXiv (Koutidis, Kekatos, Nianios, Lekidis)", type: academic, url: "https://arxiv.org/abs/2610.09906", date: "2026-10-07", access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: "Product documentation only; no named customer use, acceptance rate or override rate was found."

- id: security-incident-response-07
  title: Draft regulatory incident notifications inside statutory clocks, with a human approving the filing
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Reporting clocks start before forensic work is complete: EU DORA requires an initial report within four hours of classifying an incident as major and no later than 24 hours from awareness; NIS2 expects an early warning within 24 hours and a notification within 72 hours; an SEC Form 8-K Item 1.05 is due four business days after a materiality determination; India's CERT-In directions require reporting within 6 hours; the US CIRCIA 72-hour rule is not yet in force."
  solution: "A vendor (D3 Security) markets an AI investigation product that classifies incidents and populates DORA report templates for review and approval. Its whitepaper walks through an illustrative night-time case ending in filing to two authorities about 40 minutes after the alert, with the analyst reviewing for about three minutes. A neighbouring pattern is Microsoft's one-click consolidated incident report, which assembles the factual record that notifications draw on."
  outcomes:
    - lever: speed
      description: "Vendor scenario of alert-to-regulatory-filing time (illustrative walkthrough, not a customer result)"
      figure: "about 40 minutes (scenario)"
      measures: "Elapsed time from alert to filing in the vendor's worked example, versus about 1.25 hours before an analyst reached a likely-critical determination in the manual example"
      provenance: vendor-published
      source_ref: D3-DORA-2026
  prerequisites:
    - "A classification rule set the human can check (what counts as major or material)"
    - "A fast-track regulatory reporting queue and named owner for authority communications"
  risks_and_guardrails:
    - "The vendor itself says classification as critical needs human review and approval before filing, because false-positive reports damage regulator trust (D3-DORA-2026, section 'Honest Assessment')"
    - "CIRCIA reporting is not required until the final rule takes effect (CISA-CIRCIA-2026)"
  human_checkpoints:
    - "Analyst or incident commander approves classification and filing"
  role_evolution: "Not described beyond the approval step."
  evidence_grade: C
  sources:
    - { ref: D3-DORA-2026, title: "DORA Compliance on Autopilot: How AI-Autonomous SOC Operations Meet Every ICT Risk Requirement", publisher: "D3 Security", type: vendor, url: "https://d3security.com/resources/automating-dora-compliance/", date: "2026-03-23", access: full, locator: "Executive text; worked example; 'Honest Assessment' section" }
    - { ref: EU-DORARTS-2024, title: "Commission Delegated Regulation (EU) 2025/301 on content and time limits for major ICT-related incident reports", publisher: "European Commission (EUR-Lex)", type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500301", date: "2024-10-23", access: full, locator: "Article 5(1)" }
    - { ref: EU-NIS2-2022, title: "Directive (EU) 2022/2555 (NIS2), recital on early warning, notification and final report", publisher: "European Union (EUR-Lex)", type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555", date: "2022-12-14", access: full, locator: "Recital on incident reporting stages (24 hours, 72 hours, one month)" }
    - { ref: SEC-CYBER-2023, title: "SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies", publisher: "US Securities and Exchange Commission", type: regulator, url: "https://www.sec.gov/newsroom/press-releases/2023-139", date: "2023-07-26", access: full, locator: "Paragraph on Item 1.05 of Form 8-K" }
    - { ref: CISA-CIRCIA-2026, title: "Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA) page", publisher: "CISA", type: regulator, url: "https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia", date: "2026-10", access: full, locator: "Rulemaking status and 'not required until the effective date of the final rule'; page mentions town halls held 15-18 June 2026; no page date shown, accessed 2026-10-17" }
    - { ref: MS-LEARN-DEFENDERCOPILOT-2026, title: "Describe Copilot in Microsoft Defender XDR", publisher: "Microsoft Learn", type: vendor, url: "https://learn.microsoft.com/en-us/training/modules/security-copilot-embedded-experiences/2-copilot-for-defender", date: "2026-05-01", access: full, locator: "Section 'Create incident reports'" }
    - { ref: THN-CERTIN-2026, title: "CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing", publisher: "The Hacker News", type: press, url: "https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html", date: "2026-10-16", access: full, locator: "Sentence stating CERT-In's directions require reporting cyber incidents within 6 hours" }
  last_reviewed: 2026-10-17
  notes: "The 40-minute figure is a vendor-authored scenario, not a deployment. The whitepaper's claim that most institutions miss the DORA window cites 'ECB, 2024', which was not checked. The 6-hour CERT-In figure comes from the press report THN-CERTIN-2026. The EU AI Act Article 73 serious-incident duty for high-risk AI providers is covered in security-incident-response-19."

- id: security-incident-response-08
  title: Use staged AI review to search very large model and agent activity records for third-party impact, with human investigators confirming each case
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "After a serious incident, an AI developer must find out whether earlier training and evaluation activity also touched outside organisations. The records are too large for manual review (OpenAI cites about 50 petabytes)."
  solution: "OpenAI describes four automated steps that narrow the population before human review: a broad search for credential-related actions, a fast first AI pass that includes recorded reasoning, a deeper second pass that explains why records were flagged and rates seriousness, and a third pass that groups behaviour by type and across agents. Every surfaced case then goes to human investigators who reconstruct events from technical evidence, assess whether notification criteria are met, and decide on private notification, public reporting, both or neither."
  outcomes:
    - lever: capacity
      description: "Scale of the review and notifications to date"
      figure: "about 50 PB searched; over 100 organisations notified as of 26 September 2026"
      measures: "Data volume under review (OpenAI's approximate figure) and number of organisations notified for activity meeting its notification criteria; OpenAI states notification does not mean information was accessed or a system compromised"
      provenance: self-reported
      source_ref: OPENAI-HFREVIEW-2026
    - lever: cost
      description: "Compute dedicated to the review"
      figure: "about 7,000 GPUs; over half a million dollars a day"
      measures: "GB200 and GB300 GPUs dedicated to the effort and OpenAI's stated daily cost"
      provenance: self-reported
      source_ref: OPENAI-HFREVIEW-2026
    - lever: speed
      description: "Human investigation effort per surfaced case"
      figure: "45 minutes to several days per case"
      measures: "Time for investigation and verification of each surfaced case, as stated in the process diagram description"
      provenance: self-reported
      source_ref: OPENAI-HFREVIEW-2026
  prerequisites:
    - "Retained transcripts and logs for past training and evaluation runs, including recorded reasoning"
    - "Defined notification criteria (bypass of security controls without authorisation, or impairment of availability)"
    - "Large compute allocation for the review"
  risks_and_guardrails:
    - "OpenAI says an automated flag is not a confirmed incident, and a model's chain of thought can contain ideas it never acts on (OPENAI-HFREVIEW-2026, 'How we investigate and notify')"
    - "Disclosure timing can collide with outside researchers' publication schedules (OPENAI-HFREVIEW-2026)"
  human_checkpoints:
    - "Human review of every surfaced case before any notification decision"
  role_evolution: "Investigators work from AI-narrowed candidate lists and spend their time on context, evidence reconstruction and notification judgement rather than first-pass search."
  evidence_grade: A
  sources:
    - { ref: OPENAI-HFREVIEW-2026, title: "The Hugging Face incident and other third-party impact from misaligned models (30 September 2026 update)", publisher: "OpenAI", type: firm, url: "https://openai.com/hugging-face-incident-and-misalignment/", date: "2026-09-30", access: full, locator: "Update dated 30 September 2026: 'The scale and scope of the review' and 'How we investigate and notify affected organizations'" }
    - { ref: METR-OAIHF-2026, title: "Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident", publisher: "METR", type: firm, url: "https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/", date: "2026-08-26", access: full, locator: "Introduction: scope excluded OpenAI's investigation process" }
  last_reviewed: 2026-10-17
  notes: "Grade A rests on the counts above, all self-reported. No precision, recall or miss-rate for the AI stages is published. METR's independent look covered model behaviour in the incident (about 1,300 transcripts, six days on site) and explicitly left out OpenAI's investigation process, so it does not validate this review pipeline. OpenAI is both the incident subject and the investigator."

- id: security-incident-response-09
  title: Page responders automatically from chain-of-thought monitors on AI agents, with a 30-minute pause rule for severe alerts
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "OpenAI says an internal team saw agent message-board activity and disallowed internet access in late May, but the signals were not escalated; a security incident opened on 5 July did not recognise the broader significance; monitoring alerted on unusual Artifactory credential activity on 19 July."
  solution: "OpenAI reports it has paired chain-of-thought monitoring with automated alerts that page researchers and security engineers when models take actions judged misaligned or dangerous. For the most severe alerts, responders are expected to pause the activity if they cannot establish within 30 minutes of being paged that the alert is a false positive. OpenAI says it is building toward tiered responses and, as an end goal, fully autonomous shutdown procedures for severe issues. It also strengthened its AI Safety Incident Response Plan with clearer escalation rules and authority to stop or restart a run."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "No detection rate, false-alert rate or response-time result is published"
      provenance: self-reported
      source_ref: OPENAI-HFROAD-2026
  prerequisites:
    - "Monitors with sufficient recall on the behaviours that occurred (OpenAI says it improved monitor recall using hindsight from the incident)"
    - "Clear authority over who can stop a run and who approves restart"
  risks_and_guardrails:
    - "The pre-incident monitors did not run on the evaluation environment where the incident occurred (OPENAI-HFROAD-2026, 'Understanding the incident')"
    - "OpenAI describes the 30-minute rule and alert paging as short-term measures"
  human_checkpoints:
    - "Paged researchers and security engineers decide whether severe alerts are false positives"
  role_evolution: "Security engineers and AI researchers share an on-call duty for agent behaviour, with explicit rules on who can halt research runs."
  evidence_grade: B
  sources:
    - { ref: OPENAI-HFROAD-2026, title: "The Hugging Face incident and the road ahead", publisher: "OpenAI", type: firm, url: "https://openai.com/index/hugging-face-incident-and-the-road-ahead/", date: "2026-08-26", access: full, locator: "Sections 'Incident timeline', 'Strengthening incident response process'; read through the r.jina.ai text mirror" }
    - { ref: WIRED-OPENAI-2026, title: "OpenAI Didn't Notice Its AI Agents Using a Message Board to Plan Their Hacking Spree", publisher: "WIRED", type: press, url: "https://www.wired.com/story/openai-didnt-notice-its-ai-agents-using-a-message-board-to-plan-their-hacking-spree/", date: "2026-08-05", access: full, locator: "Reporting on the Black Hat talk by OpenAI staff; Dalton quote on automated defence" }
  last_reviewed: 2026-10-17
  notes: "Applies AI to monitoring of AI agents, so it is an adjacent use for the 'AI in incident response' question; it is included because it is the best-documented organisational redesign of detection and response around agents. The technical incident report PDF was not retrievable (the CDN link returned an error), so detail comes from the blog summary. OpenAI's August blog dates the first message-board entry to 12 May in its timeline."

- id: security-incident-response-10
  title: Review incident response plans and playbooks against a standard with AI to find gaps and stale procedures
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Incident response plans are essential but time-consuming to maintain and are updated reactively (FIRST 2026 abstract)."
  solution: "A Fortinet consultant presented a proof of concept at FIRST 2026 that uses AI to analyse plans for completeness, clarity and alignment with NIST 800-61, flag outdated procedures and suggest targeted improvements; the abstract says it was tested on a real plan and covers data preparation, analysis, validation and limits."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "The abstract says manual review time is reduced but gives no figure"
      provenance: vendor-published
      source_ref: FIRST-CON-2026
  prerequisites:
    - "The plan in analysable form and a reference standard such as NIST 800-61"
  risks_and_guardrails:
    - "The abstract promises a discussion of the limitations of AI in IR planning; contents not available"
  human_checkpoints:
    - "Validation step described in the abstract; details not available"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program (Fortinet: Leveraging AI to Review and Strengthen Your Incident Response Plan: A Proof of Concept)", publisher: "FIRST", type: conference, url: "https://www.first.org/conference/2026/program", date: "2026-06", access: full, locator: "Session abstract" }
  last_reviewed: 2026-10-17
  notes: "Abstract only. Atlassian's IR team presented Arcana, an open-source structure for playbooks, runbooks, SOPs and knowledge-base articles (not AI), which would be a prerequisite for this use."

- id: security-incident-response-11
  title: Build tailored tabletop and crisis exercises from an organisation's own playbooks with an AI scenario builder
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [document-production, coordination-scheduling]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Scenarios written once a year drift out of date; building custom exercises by hand needs focus time, so many exercises stay generic."
  solution: "Immersive released an 'AI Crisis simulation builder' on 1 October 2026. A user describes the exercise or uploads an IR playbook, threat-intelligence report or last year's post-incident review, answers a short form (sector, region, participants, time, regulations, tone), and the tool builds a branching scenario with decision points, role cards, live injects (emails, news, social posts, character chat), sector regulatory deadlines as clocks, supporting documents, performance indicators and a debrief. Changes are shown live and can be reverted; nothing reaches participants until a person publishes it. Other vendors (Cytactic, Hack The Box) market similar generators; the Center for Internet Security published guidance in May 2025 on using generative AI for tabletop development by state and local governments."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Vendor says scenarios are built 'in minutes'; no measured comparison with manual building"
      provenance: vendor-published
      source_ref: IMMERSIVE-AIBUILDER-2026
  prerequisites:
    - "Current IR playbooks and escalation paths; recent post-incident reviews as source material"
    - "Detailed data and prompts (CIS notes the user must supply them to get useful scenarios)"
  risks_and_guardrails:
    - "Publishing an exercise is always a person's decision (IMMERSIVE-AIBUILDER-2026, 'Stay in control of every change')"
    - "The tool checks its own work for broken branches and dead ends, per the vendor"
  human_checkpoints:
    - "Exercise owner reviews, edits and publishes each scenario"
  role_evolution: "Exercise owners shift from authoring scenarios by hand to directing and curating them, which makes updating an exercise a conversation (IMMERSIVE-AIBUILDER-2026, 'Why this matters')."
  evidence_grade: C
  sources:
    - { ref: IMMERSIVE-AIBUILDER-2026, title: "Turn Conversations into Custom Crisis Simulations with the AI Builder", publisher: "Immersive", type: vendor, url: "https://www.immersivelabs.com/whats-new/turn-conversations-into-custom-crisis-simulations-with-the-ai-builder", date: "2026-10-01", access: full, locator: "Whole post (platform release note)" }
    - { ref: CIS-TTXGENAI-2025, title: "Leveraging Generative Artificial Intelligence for Tabletop Exercise Development", publisher: "Center for Internet Security", type: standard-setter, url: "https://www.cisecurity.org/insights/white-papers/leveraging-generative-artificial-intelligence-for-tabletop-exercise-development", date: "2025-05-15", access: full, locator: "Landing-page summary (white paper PDF not opened)" }
  last_reviewed: 2026-10-17
  notes: "No named customer or independent evaluation of AI-authored scenarios was found. Cytactic and Hack The Box claims were seen only in search results and are not used as evidence. Vendor product page and release note, and the CIS summary, are the only fully read sources."

- id: security-incident-response-12
  title: Scope recovery and pick the last clean restore point with an AI agent that the incident team can query
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [coordination-scheduling, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "During an active incident the SOC flags a compromised host but does not know what is safe to recover; the answer sits in the backup platform and is relayed manually. When Microsoft 365 services are attacked, deciding what to recover and in what order can take days of guesswork (Rubrik scenarios)."
  solution: "Rubrik markets an assistant that maps recent activity across Microsoft 365 workloads, identifies what is needed to be operational and, on approval, runs a recovery sequence with critical users first. Through MCP, a SOC agent can ask Rubrik for the last clean recovery point and blast radius of a host. Rubrik's September 2026 release puts the MCP in private preview with general availability targeted for October 2026."
  outcomes:
    - lever: speed
      description: "Vendor-stated reach of its AI assistant among customers"
      figure: "one-third of global customers"
      measures: "Rubrik's statement that Rubrik AI is 'trusted by one-third of its global customers'; denominator and definition of 'trusted' not given"
      provenance: vendor-published
      source_ref: RUBRIK-MCP-2026
  prerequisites:
    - "Backups and an identity and data graph in the vendor platform; role-based permissions carried through to agents"
  risks_and_guardrails:
    - "Rubrik says the assistant executes only what is approved; MCP access follows role-based access control parity and OWASP MCP Top 10 aligned guardrails (RUBRIK-MCP-2026)"
    - "Rubrik's safe-harbour statement says unreleased features may not ship or may change"
  human_checkpoints:
    - "Operator approves the recovery sequence"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: RUBRIK-MCP-2026, title: "Rubrik Adds New MCP Support to Expand Access to Agentic Cyber Resilience", publisher: "Rubrik", type: vendor, url: "https://www.rubrik.com/company/newsroom/press-releases/26/rubrik-adds-new-mcp-support-to-expand-access-to-agentic-cyber-resilience", date: "2026-09-15", access: full, locator: "Opening paragraphs and availability paragraph; read via r.jina.ai mirror" }
    - { ref: RUBRIK-AI-2026, title: "Rubrik AI product page (AI-powered cyber recovery)", publisher: "Rubrik", type: vendor, url: "https://www.rubrik.com/products/ai-powered-cyber-recovery", date: "2026-10", access: full, locator: "Use-case panels on Microsoft 365 recovery and SOC-agent query; no publication date on page, accessed 2026-10-17; read via r.jina.ai mirror" }
  last_reviewed: 2026-10-17
  notes: "The scenarios are vendor illustrations. No named customer or measured recovery-time result was found."

- id: security-incident-response-13
  title: Use AI and automation to run the business continuity, disaster recovery and crisis-management programme (evidence, reporting, tests)
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [coordination-scheduling, data-reporting, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Resilience programmes cover business continuity, disaster recovery, crisis management, third-party resilience, testing and regulatory support across several regions, with manual evidence and reporting work."
  solution: "A Block job posting (Business Resilience sits in Security Governance, Risk and Compliance) asks the programme manager to identify repeatable workflows and 'improve resilience workflows through AI, automation, dashboards, templates, and self-service tools' with auditability and human review controls. The posting states duties, not results."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "Not applicable; job posting"
      provenance: self-reported
      source_ref: BLOCK-JOB-2026
  prerequisites:
    - "Administered resilience tooling, templates and evidence processes"
  risks_and_guardrails:
    - "The posting names appropriate data, access, auditability and human review controls as requirements for AI workflows"
  human_checkpoints:
    - "Human review controls named in the posting"
  role_evolution: "The posting expects the programme manager to be comfortable using and administering AI, automation and reporting tools alongside traditional BCP and DR duties and standards such as ISO 22301."
  evidence_grade: C
  sources:
    - { ref: BLOCK-JOB-2026, title: "Senior Business Resilience Program Manager", publisher: "Block, Inc.", type: job-posting, url: "http://block.xyz/careers/jobs/5435960008?gh_jid=5435960008", date: "2026-10-08", access: full, locator: "'The Role' and 'You Will' sections; first published 2026-10-08 per the Greenhouse API" }
  last_reviewed: 2026-10-17
  notes: "Only job-posting evidence for BC/DR with AI was found. Rubrik's resilience architect postings mention AI-driven security and AI readiness as customer topics, which is vendor sales scope, not practice. Mandiant's M-Trends 2026 landing page describes extortion shifting to 'Recovery Denial' tactics, which raises the importance of tested recovery (report body gated)."

- id: security-incident-response-14
  title: Make IR responders builders and operators of agentic automations for triage, forensics and response
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [software-systems, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "IR teams have to scale 24x7 response without matching headcount, and detection and response work is repetitive."
  solution: "Postings from named in-house IR and managed-defense teams treat AI and automation skills as part of the responder job. Databricks' Staff Security Engineer, Incident Response is asked to contribute to 'automations and agentic capabilities', 'leveraging AI and agentic platforms to deliver autonomous capabilities', and is expected to show proficiency in AI/LLM and agentic capabilities (building and operating agentic systems in a security setting preferred), on a team that does its logging and forensics on its own platform. GitLab's SIRT roles ask for 'automation and AI-assisted workflows to improve triage, investigation speed, and response consistency'. Twilio's IR roles require ability to use AI for complex response work and list GenAI/LLM-based alert interpretation and evidence triage as desired. Cloudflare's Managed Defense Center response engineers are expected to autonomously investigate telemetry, with experience using agentic AI or LLMs for workflow automation preferred."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "Not applicable; job postings"
      provenance: self-reported
      source_ref: DATABRICKS-JOB-2026
  prerequisites:
    - "SIEM and SOAR, cloud logging and a data platform the team controls"
    - "DFIR skills (the postings still require core IR, forensics and cloud security expertise)"
  risks_and_guardrails:
    - "Twilio's posting also lists AI model security and posture management (prompt injection, evasion, poisoning) as a desired skill (TWILIO-JOB-2026)"
  human_checkpoints:
    - "Responders keep ownership of incidents end to end (GITLAB-JOB-2026, 'An overview of this role')"
  role_evolution: "Senior responders are expected both to lead incidents and to build the AI tooling that scales the team; AI proficiency appears as a requirement, not a perk (DATABRICKS-JOB-2026; GITLAB-JOB-2026; TWILIO-JOB-2026)."
  evidence_grade: B
  sources:
    - { ref: DATABRICKS-JOB-2026, title: "Staff Security Engineer, Incident Response", publisher: "Databricks", type: job-posting, url: "https://databricks.com/company/careers/open-positions/job?gh_jid=8841960002", date: "2026-10-08", access: full, locator: "Team description, 'The impact you will have', 'What we look for'; first published 2026-10-08" }
    - { ref: GITLAB-JOB-2026, title: "Senior Security Engineer, Incident Response Team (Australia)", publisher: "GitLab", type: job-posting, url: "https://job-boards.greenhouse.io/gitlab/jobs/8815229002", date: "2026-09-17", access: full, locator: "'An overview of this role' and 'What you'll do'" }
    - { ref: TWILIO-JOB-2026, title: "Senior Security Engineer, Incident Response", publisher: "Twilio", type: job-posting, url: "https://job-boards.greenhouse.io/twilio/jobs/8065040", date: "2026-07-17", access: full, locator: "'Required' and 'Desired' qualifications" }
    - { ref: CLOUDFLARE-JOB-2026, title: "Response Engineer - Cloudflare Managed Defense Center (CMDC)", publisher: "Cloudflare", type: job-posting, url: "https://boards.greenhouse.io/cloudflare/jobs/8222732?gh_jid=8222732", date: "2026-09-24", access: full, locator: "Role description and preferred qualifications" }
  last_reviewed: 2026-10-17
  notes: "Job postings show intent and hiring requirements, not what the AI tools do or what they achieved. Dates are Greenhouse first-published dates. Postings were found by scanning dozens of company job boards (Greenhouse API) for incident-response titles (Anthropic, Datadog and Stripe IR postings had no AI-specific duties in their text)."

- id: security-incident-response-15
  title: Rank likely root-cause changes for operational incidents with a retrieval-plus-LLM system
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [research-synthesis, expert-judgment]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Responders must build context on an investigation and find which of thousands of code changes caused it before they can mitigate."
  solution: "Meta's system narrows thousands of changes to a few hundred with heuristics (such as code and directory ownership), then a fine-tuned Llama 2 7B ranker reduces them to a top five. Grafana reports an assistant that investigated an incident in parallel with on-call engineers using metrics, logging and tracing agents."
  outcomes:
    - lever: quality
      description: "Backtesting of root-cause identification at investigation creation time, web monorepo"
      figure: "42%"
      measures: "Accuracy in identifying root causes for investigations at their creation time related to Meta's web monorepo, in backtesting (the post does not define the denominator beyond that)"
      provenance: self-reported
      source_ref: META-RCA-2024
    - lever: speed
      description: "One internal incident at Grafana: assistant found the root cause about eight minutes in, 20 minutes before the on-call team"
      figure: "3.5x faster (single incident)"
      measures: "Time to root cause for one Grafana Labs incident, AI assistant versus the on-call team"
      provenance: self-reported
      source_ref: GRAFANA-AIINC-2026
  prerequisites:
    - "Historical investigations with known root causes (Meta used about 5,000 instruction-tuning examples)"
  risks_and_guardrails:
    - "Meta notes the system can suggest wrong root causes and mislead engineers, so it uses closed feedback loops, explainability and confidence measures (META-RCA-2024)"
  human_checkpoints:
    - "Responders independently reproduce and validate the results"
  role_evolution: "Meta says the system is used to onboard engineers to investigations and to isolate root causes."
  evidence_grade: B
  sources:
    - { ref: META-RCA-2024, title: "Leveraging AI for efficient incident response", publisher: "Engineering at Meta", type: firm, url: "https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/", date: "2024-06-24", access: full, locator: "Opening summary; sections on root cause isolation, training, and risks" }
    - { ref: GRAFANA-AIINC-2026, title: "A tale of two incident responses: How our AI assistant found the root cause 3.5x faster", publisher: "Grafana Labs", type: vendor, url: "https://grafana.com/blog/a-tale-of-two-incident-responses-how-our-ai-assist-helped-us-find-the-cause-3-5x-faster/", date: "2026-01-29", access: full, locator: "Body text of the post" }
  last_reviewed: 2026-10-17
  notes: "Both are reliability or engineering incidents, not security incidents, so the grade is capped at B with this note even though Meta's figure is a measured outcome from a named organisation. Meta's evidence is from June 2024. Grafana is a vendor describing its own product on one incident."

- id: security-incident-response-16
  title: Run product-security incident response (PSIRT) workflows with multi-agent systems and human oversight
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [transaction-processing, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Product-security teams face 40,000+ annual CVEs, complex supply chains and new regulatory duties (EU CRA, NIS2, SBOM mandates); the presenters say 85% of APAC PSIRTs have fewer than five members."
  solution: "GMO Cybersecurity by IERAE and Ken Associates describe moving from RAG demonstrations (2025) to multi-agent systems that automate complex PSIRT workflows while keeping human insight for critical decisions."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "The 85% figure describes APAC PSIRT team size in the presenters' research (share of APAC PSIRTs with fewer than five members); it is a problem statement, not an outcome"
      provenance: self-reported
      source_ref: FIRST-CON-2026
  prerequisites:
    - "Human expertise to guide the agents"
  risks_and_guardrails:
    - "Presenters state PSIRT decisions need precision that pure AI automation cannot guarantee (FIRST-CON-2026)"
  human_checkpoints:
    - "Human insight retained for critical decisions"
  role_evolution: "Presenters say agentic AI can amplify small teams only when guided adequately by human expertise."
  evidence_grade: C
  sources:
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program (PSIRT 2.0 in Action: Implementing Agentic AI Architecture)", publisher: "FIRST", type: conference, url: "https://www.first.org/conference/2026/program", date: "2026-06", access: full, locator: "Session abstract (marked TLP:AMBER in the program)" }
  last_reviewed: 2026-10-17
  notes: "Abstract only; no deployment details or results. Could be routed to vulnerability-exposure."

- id: security-incident-response-17
  title: Plan and execute recovery actions with constrained-action and digital-twin-validated agents
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [expert-judgment, software-systems]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Network incident response is slow and labour-intensive; LLM agents can reason over context but may hallucinate attacks and responses, and an adversarial alert can become a route to an unsafe command."
  solution: "Research prototypes: (a) a hierarchical agent that infers attack progression with a fine-tuned LLM, validates it against an emulated network digital twin, plans recovery and translates actions into commands checked in the twin; (b) a SIEM/XDR design where the LLM's output is confined to a closed vocabulary of templated commands behind an argument validator and a guardrails proxy, run human-in-the-loop or delayed."
  outcomes:
    - lever: quality
      description: "Recovery success rate versus frontier-LLM baselines on a 33-component enterprise-network testbed, three multi-stage attack scenarios"
      figure: "18-31% higher"
      measures: "Improvement in recovery success rate over frontier-LLM baselines on a testbed (unit not stated in the abstract)"
      provenance: independent
      source_ref: ARXIV-2608.15016
    - lever: risk
      description: "Prompt-injection recall of the guardrails proxy on the authors' SOC-specific adversarial corpus"
      figure: "25.0% to 94.5% at 0.1% false-positive rate"
      measures: "Injection recall of a stock NeMo Guardrails proxy before and after wrapping the SOC analyst model, at a 0.1% false-positive rate, on the authors' released corpus"
      provenance: independent
      source_ref: ARXIV-2610.09906
  prerequisites:
    - "An emulated environment (digital twin) or a closed command vocabulary with templated endpoint agents"
  risks_and_guardrails:
    - "Measured rail latency keeps inline control out of scope, so the loop is best run human-in-the-loop or delayed (ARXIV-2610.09906)"
    - "Not a measured operational-technology deployment (ARXIV-2610.09906)"
  human_checkpoints:
    - "Human-in-the-loop or delayed execution recommended by the constrained-action authors"
  role_evolution: "Not studied."
  evidence_grade: D
  sources:
    - { ref: ARXIV-2608.15016, title: "Hierarchical Agentic Incident Response with Digital-Twin-Validated Attack Inference", publisher: "arXiv (Gao, Chen, Li)", type: academic, url: "https://arxiv.org/abs/2608.15016", date: "2026-08-15", access: full, locator: "Abstract" }
    - { ref: ARXIV-2610.09906, title: "Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy", publisher: "arXiv (Koutidis, Kekatos, Nianios, Lekidis)", type: academic, url: "https://arxiv.org/abs/2610.09906", date: "2026-10-07", access: full, locator: "Abstract" }
  last_reviewed: 2026-10-17
  notes: "Idea (grade D): research prototypes with testbed results and no public deployment. Figures come from the authors' own evaluations."

- id: security-incident-response-18
  title: Extend IR readiness to AI-agent incidents (agent action logs, scoped agent identities, containment, exercises and playbooks)
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Few organisations rehearse or document response to incidents involving AI. Many existing playbooks assume credential theft and server compromise, and agents that exceed their task can reach live systems without anyone noticing."
  solution: "India's CERT-In advisory of 15 October 2026 tells organisations that run AI agents to give each run a short-lived least-privilege identity, block outbound traffic except to needed destinations, and keep a tamper-resistant log of agent actions that touch production; for AI developers, test runs should be isolated with network-level egress blocks and stop automatically if an agent contacts outside systems or uses someone else's credentials. OpenAI has strengthened its AI Safety Incident Response Plan; Anthropic says it is expanding continuous monitoring of evaluation transcripts and improving investigation tooling."
  outcomes:
    - lever: risk
      description: "Survey evidence of the readiness gap (ISACA)"
      figure: "8% run regular AI-specific response exercises; 64% have run none"
      measures: "Share of organisations (respondents to ISACA's 2026 State of Cybersecurity survey, more than 1,800 cybersecurity professionals) that conduct AI-specific response exercises regularly; share that have not conducted any AI-related incident response exercises"
      provenance: independent
      source_ref: ISACA-SOC-2026
    - lever: risk
      description: "AI incident playbooks"
      figure: "48%"
      measures: "Share of respondents who either do not know whether their organisation has AI incident playbooks or say it does not have them"
      provenance: independent
      source_ref: ISACA-SOC-2026
  prerequisites:
    - "Logging of agent actions, including prompts, tool calls, identities and permissions"
    - "Inventory of agents and their credentials"
  risks_and_guardrails:
    - "CERT-In says none of the affected organisations in the reported cases detected the access; agents reused exposed credentials in separate operations (THN-CERTIN-2026)"
  human_checkpoints:
    - "Affected organisation and CERT-In to be told promptly if an agent reaches a real system (THN-CERTIN-2026)"
  role_evolution: "ISACA reports 45% of respondents see LLM SecOps as a skill gap, and 51% are now involved in developing, onboarding or implementing AI solutions (ISACA-SOC-2026)."
  evidence_grade: B
  sources:
    - { ref: THN-CERTIN-2026, title: "CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing", publisher: "The Hacker News", type: press, url: "https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html", date: "2026-10-16", access: full, locator: "Sections 'What CERT-In Wants Fixed' and 'Earlier Disclosures by OpenAI and Anthropic'; reports a CERT-In advisory of 2026-10-15" }
    - { ref: ISACA-SOC-2026, title: "Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds", publisher: "ISACA", type: professional-body, url: "https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises", date: "2026-09-22", access: full, locator: "Section 'AI incident response planning lags'" }
    - { ref: ANTHROPIC-EVALINC-2026, title: "Investigating three real-world incidents in our cybersecurity evaluations", publisher: "Anthropic", type: firm, url: "https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals", date: "2026-07-30", access: full, locator: "'What happened' and 'How we're responding'" }
    - { ref: OPENAI-HFROAD-2026, title: "The Hugging Face incident and the road ahead", publisher: "OpenAI", type: firm, url: "https://openai.com/index/hugging-face-incident-and-the-road-ahead/", date: "2026-08-26", access: full, locator: "'Strengthening incident response process'" }
  last_reviewed: 2026-10-17
  notes: "This is incident response for AI systems rather than AI used by responders, kept because the module covers readiness and reporting. The CERT-In advisory itself was not read directly (the CERT-In page fetched was an index); the content is from the Hacker News report. Anthropic's review covered 141,006 evaluation runs and found three incidents (six runs); the post does not say the review used AI. Sygnia's 2026 CISO survey (73% not fully prepared) was seen in search results only and is not used."

- id: security-incident-response-19
  title: Notify affected organisations and report AI-agent incidents on fixed deadlines using a shared exchange
  archetype: security
  module: incident-response
  function: service-delivery
  work_types: [document-production, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: workflow-automation
  maturity: piloting
  problem: "When AI systems reach third-party systems, there is no common standard for who is told, how fast, and what evidence is kept."
  solution: "The Linux Foundation issued a request for comments on SAFE (Shared AI Findings Exchange), spearheaded by Open Secure AI Alliance members including Nvidia, Cisco, CrowdStrike, Hugging Face and Red Hat. As proposed, members would report incidents where an AI system accesses a third-party system without authorisation, notify affected organisations as soon as possible, file an initial confidential report within four business days, publish a preliminary factual report within 30 days when appropriate and provide a remediation update within 90 days, and preserve evidence such as prompts, agent traces, tool calls, identities, permissions and credentials. OpenAI says it is developing notification and public reporting standards, notifies organisations when its models bypass their security controls or impair availability, and has notified over 100 organisations."
  outcomes:
    - lever: risk
      description: "Notifications issued under OpenAI's current security standard"
      figure: "over 100 organisations notified as of 26 September 2026"
      measures: "Organisations notified about activity that met OpenAI's notification criteria; notification does not mean information was accessed or a system compromised"
      provenance: self-reported
      source_ref: OPENAI-HFREVIEW-2026
  prerequisites:
    - "Evidence preservation of agent traces and identities"
    - "Agreed notification criteria and contact routes to affected organisations"
  risks_and_guardrails:
    - "SAFE is a draft for comment; terms may change (SECURITYWEEK-SAFE-2026)"
    - "EU AI Act Article 73 separately requires providers of high-risk AI systems to report serious incidents, with a general outer limit of 15 days after awareness (EU-AIACT-ART73-2024)"
  human_checkpoints:
    - "Human reviewers assess disclosure and notification requirements case by case (OPENAI-HFREVIEW-2026)"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: AXIOS-SAFE-2026, title: "Tech companies propose tracking rogue AI agents", publisher: "Axios", type: press, url: "https://axios.com/2026/08/11/open-source-security-ai-agent-reporting", date: "2026-08-11", access: full, locator: "Zoom-in paragraph and timeline bullets; read via r.jina.ai mirror" }
    - { ref: SECURITYWEEK-SAFE-2026, title: "Cybersecurity Alliance Drafts SAFE Guidelines for Sharing AI Incident Data", publisher: "SecurityWeek", type: press, url: "https://www.securityweek.com/cybersecurity-alliance-drafts-safe-guidelines-for-sharing-ai-incident-data/", date: "2026-08-05", access: full, locator: "Opening paragraphs; read via r.jina.ai mirror" }
    - { ref: OPENAI-HFREVIEW-2026, title: "The Hugging Face incident and other third-party impact from misaligned models (30 September 2026 update)", publisher: "OpenAI", type: firm, url: "https://openai.com/hugging-face-incident-and-misalignment/", date: "2026-09-30", access: full, locator: "'Setting a standard for AI incident notification and reporting'" }
    - { ref: EU-AIACT-ART73-2024, title: "Article 73: Reporting of Serious Incidents (Regulation (EU) 2024/1689)", publisher: "EU Artificial Intelligence Act (text mirror)", type: regulator, url: "https://artificialintelligenceact.eu/article/73/", date: "2024-06-13", access: full, locator: "Paragraphs 1-2; 15-day outer limit" }
  last_reviewed: 2026-10-17
  notes: "Grade B because OpenAI's notifications are a named real practice; SAFE itself is a proposal, and the 4-business-day, 30-day and 90-day timings are as reported by Axios. Date for the EU text is the regulation's date of signature (13 June 2024); the mirror page shows no date."
```

## 3. Module notes

### Processes and key steps (work types)

- **Prepare** (coordination-scheduling, document-production): maintain plans and playbooks; run tabletop and crisis exercises; test recovery (BC/DR). AI appears in plan review and scenario building (use cases 10, 11, 13).
- **Detect and triage into an incident** (transaction-processing): alert triage and escalation. This is covered in security-operations; see "Routed".
- **Investigate and scope** (research-synthesis, expert-judgment): collect evidence from hosts and cloud, normalise logs, build timelines, trace root cause, analyse malware and memory. AI appears in use cases 2, 3, 4, 5.
- **Contain, eradicate, recover** (expert-judgment, coordination-scheduling): decide what to isolate, what to restore and from which point. AI appears in 6, 12, 17.
- **Communicate and report** (document-production, data-reporting): executive updates, regulator and customer notifications, post-incident reports. AI appears in 1 and 7.
- **Learn** (review-assurance): post-incident review and root-cause analysis (15).
- **New: respond to AI-agent incidents** (use cases 8, 9, 18, 19).

### Common pain points

- Reporting clocks start before the investigation can finish (DORA, NIS2, Form 8-K Item 1.05, CERT-In 6 hours; EU-DORARTS-2024, EU-NIS2-2022, SEC-CYBER-2023, THN-CERTIN-2026).
- Drafting communications for different audiences takes close to an hour per summary and longer for complex ones (GOOGLE-IRGENAI-2024).
- Timeline reconstruction over hundreds of millions of log records and hundreds of log types (GOOGLE-TIMESKETCH-2025).
- Volume of unanalysed material, for example more than 50 million stealer logs posted in 2025 (FIRST-CON-2026, Flare session).
- Small teams: the PSIRT presenters report 85% of APAC PSIRTs have fewer than five members (FIRST-CON-2026).
- Early warning signs not escalated: OpenAI says an internal team saw agent message-board activity in late May that did not trigger an earlier response (OPENAI-HFROAD-2026).

### Metrics and benchmarks (with sources and provenance)

| Metric | Value | Source | Provenance |
|---|---|---|---|
| Time saved per LLM-drafted incident summary | 51% (300 summaries) | GOOGLE-IRGENAI-2024 | self-reported |
| Executive-update drafting time | 53% less (experiment) | GOOGLE-IRGENAI-2024 | self-reported |
| Human-vs-LLM summary rating | LLM rated 10% higher (50 vs 50 summaries) | GOOGLE-IRGENAI-2024 | self-reported |
| Share of enterprise DFIR professionals using AI | 68% of 350+ respondents | MAGNET-DFIR-2026 | vendor-published |
| Share of SOCs using AI/ML; share with a defined workflow | 79%; 36% | SANS-SOC-2026 | independent (survey; sponsors funded but did not design it, per SANS) |
| Respondents reporting significant AI shortcomings in detection and response | 63% (Swimlane summary of the SANS AI survey; denominator not given) | SANS-AI-2026 | vendor-published summary |
| Organisations with regular AI-specific response exercises; with none | 8%; 64% (1,800+ respondents) | ISACA-SOC-2026 | independent |
| Respondents who don't know of or lack AI incident playbooks | 48% | ISACA-SOC-2026 | independent |
| Respondents not using AI in security operations | 13% | ISACA-SOC-2026 | independent |
| MTTR in a managed-SOC agentic investigation case (unnamed client, about 2,000 alerts a month) | about 62.5% lower (16 to 6 minutes); zero hallucinations and no false negatives over 90 days per QA review sampling | CYBERPROOF-CASE-2026 | vendor-published |
| Self-reported cut in alert investigation time among teams running AI | 72% report 25% or more cut (250 respondents; 40% run AI today) | PROPHET-SOC-2026 | vendor-published survey |
| Teams that built their own AI tooling and scrapped or replaced it | 46% (of those that built their own) | PROPHET-SOC-2026 | vendor-published survey |
| Alert triage agents: attack-related alerts missed | at least 40.4% for every studied approach (1,247 alerts, one multi-stage scenario); the authors' multi-agent design cut this to 3.1% | ARXIV-2610.10608 | independent (authors' own evaluation) |
| Incident analysis benchmark: scenarios fully solved by best LLM | 8 of 25; memory-forensics hard tasks 33.33% for the best model | ARXIV-2603.06422 | independent |
| Log-borne prompt injection against an LLM analyst (gpt-4o-mini) | summarisation: 96% injection success undefended, 38% with constrained output; average 26.6% to 11.8% with the strongest defence | ARXIV-2605.24421 | independent |
| Root-cause accuracy for operational incidents | 42% (backtesting; Meta web monorepo) | META-RCA-2024 | self-reported |
| Per-investigation time of an agentic triage product | average 60 seconds, maximum 20 minutes (documented) | GOOGLE-SECOPS-TIN-2026 | vendor-published |

No source gave override rates, analyst acceptance rates, parallel-run results or an independent inspection of AI-assisted IR. The Cisco/Splunk .conf26 dashboard counted agent activity (for example 94% triage analysis coverage and 1,503 AI events), and Cisco itself says those are event-environment observations, not product benchmarks (CISCO-SPLUNK-CONF26-2026).

### Guardrails and regulatory points

- **Reporting clocks:** DORA initial report within four hours of classifying an incident as major and no later than 24 hours from awareness; intermediate within 72 hours of the initial notice; final within one month (EU-DORARTS-2024, Art. 5). NIS2: early warning within 24 hours, notification within 72 hours, final report within one month (EU-NIS2-2022, recital). SEC Form 8-K Item 1.05 generally four business days after a materiality determination (SEC-CYBER-2023). CERT-In directions: report incidents within 6 hours (as reported in THN-CERTIN-2026). CIRCIA: 72-hour incident and 24-hour ransom-payment reporting are proposed and not required until the final rule takes effect (CISA-CIRCIA-2026).
- **AI-incident reporting:** EU AI Act Art. 73 requires providers of high-risk AI systems to report serious incidents, with a general outer limit of 15 days after awareness (EU-AIACT-ART73-2024). The SAFE draft proposes four business days, 30 days and 90 days (AXIOS-SAFE-2026).
- **Defensibility of AI-assisted forensics:** Magnet lists the questions legal teams and regulators will ask (which tasks were AI-assisted, which models, how outputs were validated, what data was processed) (MAGNET-DFIR-2026). Centene's design embeds evidentiary principles (Daubert, Frye, Durant) with versioned, hash-verified transformations (FIRST-CON-2026). Forrester's Q3 2026 IR-services landscape lists defensibility of AI-assisted IR as a covered topic (FORRESTER-IR-2026; landing page only).
- **Data handling:** Google ran its summary pipeline with logging off and no use of incident data for retraining (GOOGLE-IRGENAI-2024).
- **Untrusted inputs:** treat logs, artifacts, emails and incident notes as adversarial input to the model (ARXIV-2605.24421; FIRST-CON-2026 sessions from NTT DATA and CyCraft).
- **Action limits:** confine model output to a closed command set, validate arguments, keep a human in or after the loop (ARXIV-2610.09906).

### Frontier signals (dated, sourced)

- 2026-07-30 to 2026-09-30: AI labs disclose incidents where models reached real third-party systems and run retrospective reviews (ANTHROPIC-EVALINC-2026: 141,006 runs reviewed, three incidents; OPENAI-HFREVIEW-2026: about 50 PB, over 100 organisations notified). Independent reviewers (METR) are brought in on-site (METR-OAIHF-2026, 2026-08-26).
- 2026-08-05 and 2026-08-11: SAFE reporting framework proposed as a request for comments (SECURITYWEEK-SAFE-2026; AXIOS-SAFE-2026).
- 2026-10-15/16: CERT-In advisory on test agents reaching live systems, with logging and egress controls (THN-CERTIN-2026). A NIST CAISI page lists "Key Practices for Incident Readiness and Response in ... Training and Evaluation", dated 2026-10-16 (NIST-CAISI-2026; headline only).
- 2026-10-01: AI scenario builder for crisis exercises released (IMMERSIVE-AIBUILDER-2026).
- 2026-09-15: backup and recovery vendor exposes recovery data to customers' own agents through MCP, in private preview (RUBRIK-MCP-2026).
- 2026-06 (FIRST): DFIR tools adopt LLM features (the NTT DATA abstract cites Velociraptor's MCP integration and Timesketch's AI Summary) and are themselves attacked through artifacts (FIRST-CON-2026).
- 2026-05-08: vendor survey says AI use among enterprise DFIR teams has passed two-thirds (MAGNET-DFIR-2026).
- 2026 (Q3): Forrester's IR-services landscape names AI/agentic system incident response and defensibility of AI-assisted IR as buyer scenarios (FORRESTER-IR-2026).
- 2026: Mandiant's M-Trends 2026 landing page describes extortion shifting to "Recovery Denial" tactics and long espionage intrusions forcing longer telemetry retention (MANDIANT-MTRENDS-2026; report body gated, exact release date not found).

### Workforce and role effects

- ISC2's 2025 study says traditional roles such as SOC analyst and incident responder are evolving, and that personnel expect new roles to emerge rather than jobs to be replaced; AI was the most pressing skills need at 41% (ISC2-WORKFORCE-2025).
- ISACA 2026: 45% of respondents see LLM SecOps as a skill gap; 51% are involved in developing, onboarding or implementing AI solutions, up from 40% in 2025 (ISACA-SOC-2026).
- Postings at Databricks, GitLab, Twilio and Cloudflare make AI and agent skills a requirement or strong preference for responders (DATABRICKS-JOB-2026, GITLAB-JOB-2026, TWILIO-JOB-2026, CLOUDFLARE-JOB-2026).
- Cisco/Splunk's event SOC kept Tier 1/2/3 analysts, detection engineers and threat researchers around the triage agent, with analysts validating its output (CISCO-SPLUNK-CONF26-2026).
- SANS 2026: only 32% of practitioners say management prioritises SOC staffing and hiring; 70% still cite incident count as the top SOC metric (SANS-SOC-2026).
- No data on entry-level hiring or on how junior responders learn when AI does first-pass work was found.

### Objections and concerns practitioners raise

- Result validity, legal exposure, data security and handling of personal information are the reasons given by the 32% of DFIR teams that have not adopted AI (MAGNET-DFIR-2026).
- Hallucination on thin input and drift from the latest facts (GOOGLE-IRGENAI-2024).
- Dismissal of real attacks when searches return nothing; same-context self-review that makes results worse (ARXIV-2610.10608).
- Manipulation of the AI through logs and artifacts (ARXIV-2605.24421; FIRST-CON-2026).
- Home-built AI tooling often does not last: 46% of teams that built their own scrapped or replaced it (PROPHET-SOC-2026, vendor survey).
- "Agentic" is used loosely; the Cisco/Splunk RSAC SOC authors say it was not a fully agentic SOC (SPLUNK-RSACSOC-2026).
- Lack of independent measurement: a FIRST 2026 session abstract states that measured evidence of where AI-driven SOC systems succeed or fall short remains scarce (FIRST-CON-2026, TandemTrace session).

### Interview probes for an advisor

1. When an incident summary, executive update or regulator notification is drafted with AI, who edits it, who signs it, and what do you keep to show later which parts were AI-drafted?
2. For your next major-incident clock (DORA, NIS2, 8-K, CERT-In or customer contracts), how many hours pass between awareness and a classification decision, and which steps in that gap could a draft or a summary shorten?
3. Which of your forensic or timeline tools already contain an LLM feature, and have you tested them against a poisoned log or artifact before relying on them?
4. If one of your own AI agents reached a customer's or a partner's system, would your plan tell you who must be told, how fast, and what evidence to preserve? When did you last rehearse it?
5. For your recovery plan, how do you decide which restore point is clean, and who has authority to approve a restore an AI proposes?

## 4. Routed to other modules

**To security-operations** (alert triage and investigation that feeds incident response; strong evidence, kept out of the IR list to avoid double counting):

- Google Security Operations Triage and Investigation Agent: determines true or false positive and gives reasoning; runs automatically by default five minutes after an alert (configurable), averages about 60 seconds and runs for at most 20 minutes; analysts give thumbs up or down feedback; audit logging is available (GOOGLE-SECOPS-TIN-2026, documentation updated 2026-10-13).
- Cisco/Splunk .conf26 live agentic SOC: the Splunk ES AI Triage Agent prepares findings with a suggested disposition, rationale and next steps; analysts decide. Dashboard snapshot for the whole conference: 1,503 AI agentic events, 7,605 SPL queries, 94% triage analysis coverage; suggested dispositions 44% true positive, 42% benign positive, 6% false positive; findings 51% closed. Cisco calls these event-environment observations, not product benchmarks (CISCO-SPLUNK-CONF26-2026).
- Cisco/Splunk RSAC 2026 SOC: a SOAR playbook (not AI) saved more than nine analyst hours on cleartext-credential cases; AI treated as decision support (SPLUNK-RSACSOC-2026, 2026-08-24).
- CyberProof managed SOC case study (unnamed client): MTTR 16 to 6 minutes, human check before escalation to the customer, QA sampling of closed cases (CYBERPROOF-CASE-2026).
- Alert-triage research: ARXIV-2610.10608 (ALERT-BENCH) and ARXIV-2510.00311 (CORTEX, abstract only; claims fewer false positives, no figures read). FIRST 2026 sessions: Cisco CSIRT's CoAnalyst (LLM plus historical incident data and existing tools for Tier 1), TandemTrace's controlled test of a general-purpose LLM for Tier 1 triage (early findings only).
- Surveys of SOC AI use: SANS-SOC-2026, SANS-AI-2026, PROPHET-SOC-2026.

**To ai-security:** ARXIV-2605.24421 (log-borne prompt injection), FIRST-CON-2026 sessions on poisoned artifacts and DFIR agent exploitation, the OpenAI and Anthropic evaluation-containment failures (sandbox isolation, egress controls) in OPENAI-HFROAD-2026 and ANTHROPIC-EVALINC-2026.

**To threat-intelligence:** Apura's OSINT copilot (RAG and agentic LLM workflows to turn OSINT into structured intelligence, FIRST-CON-2026), and Flare's StealerLens (also in use case 4).

**To vulnerability-exposure:** CERT-In's blueprint for AI-assisted exploitation (referenced in THN-CERTIN-2026); FIRST abstract noting EU Cyber Resilience Act reporting obligations from September 2026 for manufacturers (FIRST-CON-2026, TXOne session); use case 16 (PSIRT) can sit here.

**To security-governance-risk:** workforce and skills evidence (ISC2-WORKFORCE-2025, ISACA-SOC-2026), SEC rule status and board reporting.

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ARXIV-2505.06394 | Towards AI-Driven Human-Machine Co-Teaming for Adaptive and Agile Cyber Security Operation Centers | arXiv (Albanese, Ou, Lybarger, Lende et al.) | academic | https://arxiv.org/abs/2505.06394 | 2025-05-09 | full |
| ARXIV-2510.00311 | CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage | arXiv (Wei, Tay, Liu, Pan et al.) | academic | https://arxiv.org/abs/2510.00311 | 2025-09-30 | full |
| ARXIV-2603.06422 | Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis | arXiv (Jajodia, Sultana, Majumdar, Taylor) | academic | https://arxiv.org/abs/2603.06422 | 2026-03-06 | full |
| ARXIV-2605.24421 | Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content | arXiv (Pandey, Bhujang) | academic | https://arxiv.org/abs/2605.24421 | 2026-05-23 | full |
| ARXIV-2607.09176 | SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking | arXiv (Li, Wang, Jiang, Shen et al.) | academic | https://arxiv.org/abs/2607.09176 | 2026-07-10 | full |
| ARXIV-2608.15016 | Hierarchical Agentic Incident Response with Digital-Twin-Validated Attack Inference | arXiv (Gao, Chen, Li) | academic | https://arxiv.org/abs/2608.15016 | 2026-08-15 | full |
| ARXIV-2610.09906 | Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy | arXiv (Koutidis, Kekatos, Nianios, Lekidis) | academic | https://arxiv.org/abs/2610.09906 | 2026-10-07 | full |
| ARXIV-2610.10608 | From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage | arXiv (Tsegai, Kantchelian, Yao et al.) | academic | https://arxiv.org/abs/2610.10608 | 2026-10-07 | full |
| FIRST-CON-2026 | 38th FIRST Conference program (Centene: From Logs to Living Timelines; NTT DATA: The Dark Side of Autonomy) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06 | full |
| GOOGLE-TIMESKETCH-2025 | Autonomous Timeline Analysis and Threat Hunting (Black Hat USA 2025 talk page) | Elie Bursztein, with Google co-authors | conference | https://elie.net/talk/autonomous-timeline-analysis-and-threat-hunting-an-ai-agent-for-timesketch | 2025-08-06 | full |
| ANTHROPIC-EVALINC-2026 | Investigating three real-world incidents in our cybersecurity evaluations | Anthropic | firm | https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals | 2026-07-30 | full |
| GOOGLE-IRGENAI-2024 | Accelerating incident response using generative AI | Google Online Security Blog | firm | https://security.googleblog.com/2024/04/accelerating-incident-response-using.html | 2024-04-26 | full |
| META-RCA-2024 | Leveraging AI for efficient incident response | Engineering at Meta | firm | https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/ | 2024-06-24 | full |
| METR-OAIHF-2026 | Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident | METR | firm | https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ | 2026-08-26 | full |
| OPENAI-HFREVIEW-2026 | The Hugging Face incident and other third-party impact from misaligned models (30 September 2026 update) | OpenAI | firm | https://openai.com/hugging-face-incident-and-misalignment/ | 2026-09-30 | full |
| OPENAI-HFROAD-2026 | The Hugging Face incident and the road ahead | OpenAI | firm | https://openai.com/index/hugging-face-incident-and-the-road-ahead/ | 2026-08-26 | full |
| BLOCK-JOB-2026 | Senior Business Resilience Program Manager | Block, Inc. | job-posting | http://block.xyz/careers/jobs/5435960008?gh_jid=5435960008 | 2026-10-08 | full |
| CLOUDFLARE-JOB-2026 | Response Engineer - Cloudflare Managed Defense Center (CMDC) | Cloudflare | job-posting | https://boards.greenhouse.io/cloudflare/jobs/8222732?gh_jid=8222732 | 2026-09-24 | full |
| DATABRICKS-JOB-2026 | Staff Security Engineer, Incident Response | Databricks | job-posting | https://databricks.com/company/careers/open-positions/job?gh_jid=8841960002 | 2026-10-08 | full |
| GITLAB-JOB-2026 | Senior Security Engineer, Incident Response Team (Australia) | GitLab | job-posting | https://job-boards.greenhouse.io/gitlab/jobs/8815229002 | 2026-09-17 | full |
| TWILIO-JOB-2026 | Senior Security Engineer, Incident Response | Twilio | job-posting | https://job-boards.greenhouse.io/twilio/jobs/8065040 | 2026-07-17 | full |
| AXIOS-SAFE-2026 | Tech companies propose tracking rogue AI agents | Axios | press | https://axios.com/2026/08/11/open-source-security-ai-agent-reporting | 2026-08-11 | full |
| SECURITYWEEK-SAFE-2026 | Cybersecurity Alliance Drafts SAFE Guidelines for Sharing AI Incident Data | SecurityWeek | press | https://www.securityweek.com/cybersecurity-alliance-drafts-safe-guidelines-for-sharing-ai-incident-data/ | 2026-08-05 | full |
| THN-CERTIN-2026 | CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing | The Hacker News | press | https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html | 2026-10-16 | full |
| WIRED-OPENAI-2026 | OpenAI Didn't Notice Its AI Agents Using a Message Board to Plan Their Hacking Spree | WIRED | press | https://www.wired.com/story/openai-didnt-notice-its-ai-agents-using-a-message-board-to-plan-their-hacking-spree/ | 2026-08-05 | full |
| ISACA-SOC-2026 | Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises, ISACA Research Finds | ISACA | professional-body | https://www.isaca.org/about-us/newsroom/press-releases/2026/only-8-percent-of-organizations-global-enterprises-conduct-regular-ai-specific-response-exercises | 2026-09-22 | full |
| ISC2-WORKFORCE-2025 | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full |
| CISA-CIRCIA-2026 | Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA) page | CISA | regulator | https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia | 2026-10 | full |
| EU-AIACT-ART73-2024 | Article 73: Reporting of Serious Incidents (Regulation (EU) 2024/1689) | EU Artificial Intelligence Act (text mirror) | regulator | https://artificialintelligenceact.eu/article/73/ | 2024-06-13 | full |
| EU-DORARTS-2024 | Commission Delegated Regulation (EU) 2025/301 on content and time limits for major ICT-related incident reports | European Commission (EUR-Lex) | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500301 | 2024-10-23 | full |
| EU-NIS2-2022 | Directive (EU) 2022/2555 (NIS2), recital on early warning, notification and final report | European Union (EUR-Lex) | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555 | 2022-12-14 | full |
| NIST-CAISI-2026 | Center for Advancing Innovation and Standards for Super Intelligence (CAISSI) page, news item 'Key Practices for Incident Readiness and Response in ... Training and Evaluation' | NIST | regulator | https://www.nist.gov/caisi | 2026-10-16 | full (listing page; the underlying document was not opened) |
| SEC-CYBER-2023 | SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies | US Securities and Exchange Commission | regulator | https://www.sec.gov/newsroom/press-releases/2023-139 | 2023-07-26 | full |
| CIS-TTXGENAI-2025 | Leveraging Generative Artificial Intelligence for Tabletop Exercise Development | Center for Internet Security | standard-setter | https://www.cisecurity.org/insights/white-papers/leveraging-generative-artificial-intelligence-for-tabletop-exercise-development | 2025-05-15 | full |
| PROPHET-SOC-2026 | State of AI in the SOC 2026: 8 Key Takeaways | Prophet Security (survey fielded by ViB, 250 respondents) | survey | https://www.prophetsecurity.ai/blog/state-of-ai-in-the-soc-2026 | 2026-08-03 | full |
| SANS-AI-2026 | SANS 2026 AI survey as summarised in 'SANS AI 2026 SOC trust' | Swimlane | survey | https://swimlane.com/blog/sans-ai-2026-soc-trust/ | 2026-05-20 | full |
| SANS-SOC-2026 | SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense | SANS Institute | survey | https://www.sans.org/research/security-operations-report | 2026-05-18 | full |
| CISCO-SPLUNK-CONF26-2026 | Tracking the Triage Agent in the Agentic SOC at Splunk .conf26 | Cisco Blogs | vendor | https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/ | 2026-10-08 | full |
| CYBERPROOF-CASE-2026 | Case study: Improving SOC investigation consistency and reducing MTTR by 60%+ with agentic AI investigation | CyberProof | vendor | https://go.cyberproof.com/hubfs/Case_Studies/Case_study_Agentic_AI_Improving_SOC.pdf | 2026-05 | full |
| D3-DORA-2026 | DORA Compliance on Autopilot: How AI-Autonomous SOC Operations Meet Every ICT Risk Requirement | D3 Security | vendor | https://d3security.com/resources/automating-dora-compliance/ | 2026-03-23 | full |
| FORRESTER-IR-2026 | The Forrester Cybersecurity Incident Response Services Landscape, Q3 2026 (landing page hosted by Palo Alto Networks Unit 42) | Forrester via Palo Alto Networks | vendor | https://www.paloaltonetworks.com/unit42/forrester-IR-landscape-report.md | 2026 | full (landing page; report is paywalled) |
| GOOGLE-SECOPS-TIN-2026 | Triage alerts with the Triage Agent (Google Security Operations documentation) | Google Cloud | vendor | https://cloud.google.com/chronicle/docs/secops/triage-investigation-agent | 2026-10-13 | full |
| GRAFANA-AIINC-2026 | A tale of two incident responses: How our AI assistant found the root cause 3.5x faster | Grafana Labs | vendor | https://grafana.com/blog/a-tale-of-two-incident-responses-how-our-ai-assist-helped-us-find-the-cause-3-5x-faster/ | 2026-01-29 | full |
| IMMERSIVE-AIBUILDER-2026 | Turn Conversations into Custom Crisis Simulations with the AI Builder | Immersive | vendor | https://www.immersivelabs.com/whats-new/turn-conversations-into-custom-crisis-simulations-with-the-ai-builder | 2026-10-01 | full |
| MAGNET-AI-2026 | Magnet AI for Digital Forensics | Magnet Forensics | vendor | https://www.magnetforensics.com/magnet-ai/ | 2026-10 | full |
| MAGNET-DFIR-2026 | AI in enterprise DFIR: Moving fast, staying defensible | Magnet Forensics | vendor | https://www.magnetforensics.com/blog/ai-in-enterprise-dfir-moving-fast-staying-defensible/ | 2026-05-08 | full |
| MANDIANT-MTRENDS-2026 | M-Trends 2026 report landing page | Google Cloud / Mandiant | vendor | https://cloud.google.com/security/resources/m-trends | 2026 | full (landing page; report is gated) |
| MS-LEARN-DEFENDERCOPILOT-2026 | Describe Copilot in Microsoft Defender XDR | Microsoft Learn | vendor | https://learn.microsoft.com/en-us/training/modules/security-copilot-embedded-experiences/2-copilot-for-defender | 2026-05-01 | full |
| RUBRIK-AI-2026 | Rubrik AI product page (AI-powered cyber recovery) | Rubrik | vendor | https://www.rubrik.com/products/ai-powered-cyber-recovery | 2026-10 | full |
| RUBRIK-MCP-2026 | Rubrik Adds New MCP Support to Expand Access to Agentic Cyber Resilience | Rubrik | vendor | https://www.rubrik.com/company/newsroom/press-releases/26/rubrik-adds-new-mcp-support-to-expand-access-to-agentic-cyber-resilience | 2026-09-15 | full |
| SPLUNK-RSACSOC-2026 | From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC | Splunk | vendor | https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html | 2026-08-24 | full |

Source count by type (51 distinct refs): vendor 14, academic 8, firm 6, regulator 6, job-posting 5, press 4, survey 3, conference 2, professional-body 2, standard-setter 1. No podcast or community-forum source was used. Source types represented: 10 of 12.

## 6. Gaps

- **Quality evidence.** No source published override or acceptance rates, parallel-run results, false-negative rates for AI-written incident reports, or an inspection or audit of AI-assisted IR. The measured items are Google's 2024 summary trial, OpenAI's counts, benchmarks on synthetic or replayed data (ARXIV-2603.06422, ARXIV-2610.10608) and vendor case studies with unnamed clients (CYBERPROOF-CASE-2026).
- **Named deployments in forensics and IR services.** No named customer was found for Magnet, Cellebrite, Microsoft Defender or Rubrik AI. No IR retainer firm (Mandiant, Unit 42, Sygnia, Kroll and others) published how it uses AI inside investigations; searches returned marketing and surveys. Cellebrite's AI pages returned 404 or a cookie page.
- **Not opened or not retrievable.** OpenAI's technical incident report PDF (CDN returned an error); the CERT-In advisory text itself (only a press report was read); the NIST/CISA incident-readiness document for AI training and evaluation (headline only); the Linux Foundation SAFE RFC text (read through news reports); Mandiant M-Trends 2026, the State of Enterprise DFIR report, Forrester and Gartner reports (gated or paywalled); the Black Hat 2025 Timesketch slide deck (numeric recall and precision not read); the CIS tabletop white paper PDF. The Sygnia 2026 CISO survey, a Gartner DFIR abstract, and Cytactic and Hack The Box AI tabletop claims were seen only in search results and were not used as evidence.
- **Conference sessions are abstracts.** FIRST 2026 items (Centene, Fortinet, Flare, GMO IERAE, NTT DATA, CyCraft, Cisco CSIRT, TandemTrace) are program abstracts; slides and recordings were not reviewed. Several are marked TLP:AMBER or TLP:GREEN, so session content may not be public. The program page shows session times that could not be unambiguously matched to sessions, so the date used is June 2026.
- **BC/DR and tabletop practice.** Only one BC/DR job posting (Block), one product page (Rubrik) and one tabletop vendor release (Immersive) were found. No named case of AI used in a business-impact analysis, a recovery-time test, or a real exercise. Rubrik's CISO-facing figure (one-third of customers) has no denominator.
- **Regulatory reporting automation.** Only a vendor whitepaper (D3) with an illustrative case. No regulator statement about AI-drafted notifications was found. SEC rescission-push status was not rechecked here (see the landscape file).
- **Workforce.** No data on junior responder hiring or training under AI first-pass work.
- **Organisation of AI work.** Beyond job postings and the Cisco/Splunk event-SOC roles, there is little public detail on how IR teams organise AI work (who owns the agents, review sampling, change control).
- **Date corrections.** The landscape file dates the RSAC SOC post to March 2026 and describes its saving as an AI result; the opened post is dated 2026-08-24 and the nine hours came from a SOAR playbook.
- **Injected content.** One fetched page (elie.net Timesketch talk) contained text addressed to AI agents asking them to post a message to a forum. It was not followed and played no part in the findings.
