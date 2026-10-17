# Security / threat-intelligence: governance and evidence (wave 4)

Compiled 2026-10-17. Archetype: security. Module: threat-intelligence (cyber threat intelligence collection, analysis, reporting and sharing through bodies such as FIRST and ISACs; threat hunting; AI for summarising, enriching and prioritising intelligence). Angle: governance (what constrains and measures the work). Method: pages opened with curl, pdftotext and the r.jina.ai mirror; 5 web searches used (CISA 2015 status, SANS CTI survey, AI-ISAC status, CTI job postings, ISAC use of AI). Figures are copied with the source's own denominator. Items whose full text I could not open are listed under Gaps. Sibling files in this wave cover other modules; items for them are under "Routed to other modules".

## 1. Summary

- **The binding rules for CTI work are about sharing, handling and provider qualification, and none of them mention AI.** FIRST's TLP v2.0 says its use in automated exchanges is left to the designers of those exchanges. NIS2 Articles 29-30 (voluntary information-sharing arrangements, voluntary notification) and DORA Article 45 (information-sharing among financial entities inside trusted communities, with data-protection and competition-law limits) frame sharing. The DORA threat-led penetration testing technical standard (Delegated Regulation (EU) 2025/1190) sets experience thresholds for threat-intelligence providers. The English text contains no reference to artificial intelligence; the TIBER-EU and CBEST pages I opened do not mention it either. The nearest AI statement is NIS2 recital 51, which encourages AI for detection and requires compliance with data-protection principles such as accuracy and minimisation. The practical constraint on an AI-assisted CTI team is therefore handling rules (TLP, sharing agreements, personal data), not an AI-specific rule.
- **The clearest governance statement on AI in finished intelligence comes from ENISA.** Its Threat Landscape 2026 (September 2026) says AI was used in a limited capacity to support collection and processing, outputs were validated by subject-matter experts, and no AI-generated content was used. Its updated methodology (18 September 2026, section 2.4.7) says AI-supported tools may help with monitoring, collection and limited editorial work, but trend identification, analytical judgements and assessments stay with analysts, who retain accountability. This is the one worked example I found of a published boundary between AI assistance and analytic judgement.
- **Independent measurement shows AI is useful for extraction and poor at open-ended judgement.** On CTI report text, a 2026 benchmark of seven open-source models reached a best micro-F1 of 0.22 for multi-label ATT&CK classification of complex reports; a multi-institution SoK pilot (first authors at UC Santa Barbara) reached F1 0.71-0.72 for technique mapping on sandbox reports but recovered only 25-31% of labeled indicators; a preregistered audit of extraction from 354 incident campaigns found micro precision of 0.03-0.34. On open-ended threat hunting over raw logs, the best of five frontier models flagged 3.8% of malicious events. Detection-rule generation and structured tagging look better (for example a 0.94 F1 for IOC owner tagging on 100 reports) but come from authors' own evaluations.
- **The most important failure mode for CTI is adversarial input.** Content the AI reads is attacker-influenced. A USENIX Security 2026 paper reports up to 88.2% attack success against LLM log analysis in the unmitigated baseline, with layered defences cutting attacks by 90.4% and leaving 8.4% residual. Google's threat intelligence group reports malware loaders carrying prompts aimed at LLM security scanners. A FIRST 2026 session shows a single poisoned report or email steering an LLM-assisted workflow.
- **Practice is ahead of measurement.** SANS 2026: 45% of organizations use AI in CTI today, mainly for summarisation and report writing, and 55% lack legally reviewed CTI sharing processes. Most teams have fewer than four full-time staff; 57% of programs do not track maturity over time and 49% gather no systematic effectiveness feedback. I found no independent study of time saved, override rates or error rates for AI in a live CTI team, and no inspection findings.
- **US sharing law and institutions are unsettled.** CISA's AIS page says the Cybersecurity Information Sharing Act of 2015 was extended to 2026-09-30; I could not confirm what happened after that date. The AI-ISAC called for in the July 2025 AI Action Plan was still in development with no timeline in February 2026.

Evidence grades across the 19 use cases: A 0, B 3, C 16, D 0. No entry reaches A because no source publishes a measured operational outcome from a named organization's live CTI use of AI. Entries that rest on a benchmark or prototype are graded C (not B or D) and say so in `notes`; D is not used because every idea here has at least a prototype with published measurements. The 16 C-grade entries therefore include several that are independent academic measurements rather than vendor claims.

## 2. Use cases

```yaml
- id: security-threat-intelligence-01
  title: AI-assisted summarisation and drafting of intelligence products, with analysts keeping the judgement
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "CTI teams are small and spend analyst time on summarising sources and writing reports for many audiences. SANS reports that most formal CTI teams have fewer than four full-time employees."
  solution: "Analysts use generative AI to summarise sources, draft trend summaries and first drafts of reports, then edit and own the finished product. ServiceNow's CTI team advertises a reports-officer role that expects use of generative AI to speed intelligence synthesis and automate trend summaries 'without compromising tradecraft integrity'. ENISA's methodology allows AI-supported tools only for limited editorial assistance such as rephrasing, with human review, and states that AI is not used to draw analytical conclusions."
  outcomes:
    - lever: capacity
      description: "SANS reports that 45% of organizations are using AI in their CTI programs today, mainly for data summarization, report writing and workflow automation, with a human-in-the-loop model, and that another 32% plan to adopt it. No time saving or quality figure is published."
      figure: "45% using; 32% planning"
      measures: "Share of surveyed organizations using AI in their CTI programs (and share planning to), from 401 qualified cybersecurity professionals surveyed November 2025 to January 2026. The unit is the respondent's organization. The survey was sponsor-funded; SANS states sponsors had no role in design or analysis."
      provenance: independent
      source_ref: SANS-CTI-2026
    - lever: capacity
      description: "A sponsor's summary of the same survey gives the leading AI use cases as data summarization and report writing (56%), data parsing and normalization (46%) and workflow automation (45%)."
      figure: "56% / 46% / 45%"
      measures: "Share of respondents citing each use case, as summarised by sponsor SOCRadar; the summary does not state the denominator (whether all respondents or only those using AI). Treat as unverified."
      provenance: vendor-published
      source_ref: SOCRADAR-SANSCTI-2026
  prerequisites:
    - "An acceptable-use rule for what intelligence (by TLP label and sensitivity) may be pasted into a hosted model; see use case 19 for local models."
    - "Analytic standards that a human editor checks drafts against (ServiceNow's posting names analytic standards and structured reasoning)."
  risks_and_guardrails:
    - "ENISA states that no AI-generated content was used in its Threat Landscape 2026 report and that AI outputs were reviewed and validated by subject-matter experts (ENISA-ETL-2026, Disclaimer)."
    - "ENISA's methodology says AI-assisted output remains subject to human review and to the same source-validation, information-handling and quality-assurance requirements as other inputs (ENISA-CTL-2026, section 2.4.7)."
    - "LLM failure modes in CTI include spurious correlations from metadata and contradictory knowledge from conflicting sources (ARXIV-2509.23573)."
  human_checkpoints:
    - "Analyst approves the final analytic content and carries accountability (ENISA-CTL-2026, section 2.4.7)."
    - "Reports officer or editor checks accuracy and adherence to analytic standards (JOB-SERVICENOW-2025, responsibilities)."
  role_evolution: "The ServiceNow posting lists LLM-driven drafting, enrichment or summarisation as a required experience for a senior reports role alongside eight or more years of CTI experience, which suggests AI skill is added to, not substituted for, tradecraft (JOB-SERVICENOW-2025, qualifications). SANS write-in comments stress that analyst oversight stays essential for high-stakes calls (SOCRADAR-SANSCTI-2026)."
  evidence_grade: B
  sources:
    - { ref: SANS-CTI-2026, title: "91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (2026 CTI Survey Insights press release) and SANS 2026 CTI Key Findings", publisher: SANS Institute, type: survey, url: "https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report", date: 2026-05-19, access: full, locator: "press release paragraphs 5-8; key findings page FAQ on AI use (full report not read)" }
    - { ref: SOCRADAR-SANSCTI-2026, title: "2026 SANS CTI Survey Report: Key Findings on CTI's Influence Gap", publisher: SOCRadar, type: vendor, url: "https://socradar.io/blog/2026-sans-cti-survey-report-findings/", date: 2026-07-01, access: full, locator: "paragraph on AI use and human-in-the-loop" }
    - { ref: JOB-SERVICENOW-2025, title: "Staff Cyber Threat Intelligence Analyst | Reports Officer", publisher: ServiceNow (via Built In), type: job-posting, url: "https://builtin.com/job/staff-cyber-threat-intelligence-analyst-reports-officer/7520264", date: 2025-10-30, access: full, locator: "Responsibilities (generative AI bullet); Required Qualifications (LLM/AI-driven workflows)" }
    - { ref: ENISA-CTL-2026, title: "ENISA Cybersecurity Threat Landscape Methodology (updated 18 September 2026)", publisher: ENISA, type: regulator, url: "https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20CTL%20Methodology_Updated%2018%20september%202026.pdf", date: 2026-09-18, access: full, locator: "section 2.4.7 Use of AI supported tools" }
    - { ref: ENISA-ETL-2026, title: "ENISA Threat Landscape 2026", publisher: ENISA, type: regulator, url: "https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf", date: 2026-09, access: full, locator: "Disclaimer page" }
    - { ref: ARXIV-2509.23573, title: "Uncovering Vulnerabilities of LLM-Assisted Cyber Threat Intelligence", publisher: arXiv (Meng et al.), type: academic, url: "https://arxiv.org/abs/2509.23573", date: 2025-09-28, access: full, locator: "abstract (v5 revised 2026-05-28)" }
  last_reviewed: 2026-10-17
  notes: "Grade B rests on a named employer expecting the practice (job posting) plus a survey prevalence figure; it is not a measured outcome. ENISA is cited as a governance boundary, not as evidence of AI drafting: its report says no AI-generated content was used."

- id: security-threat-intelligence-02
  title: AI-supported monitoring and collection of open sources for threat-landscape reporting
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Threat-landscape reporting depends on collecting and curating thousands of incident reports from open sources and partners. ENISA notes that open-source reporting has gaps in granularity and timing, and that espionage is typically documented months to years late."
  solution: "ENISA states that AI was used in a limited capacity to support collection and processing of data for its 2026 report, and its methodology allows AI-supported tools for data monitoring and collection. A practitioner session at FIRST 2026 from Apura Cyber Intelligence describes turning large-scale OSINT into structured intelligence with open tooling, retrieval-augmented generation and agentic LLM workflows. A RAID 2026 paper (STINER) extracts strategic entities such as threat actor and sector from posts on X."
  outcomes:
    - lever: capacity
      description: "ENISA published no measure of the effect of AI on its collection work. Its 2026 dataset covers 8,257 incidents from 1 January to 31 December 2025, drawn mainly from open sources plus anonymised information from Member States and the ENISA Cyber Partnership Programme."
      figure: "none published for AI effect"
      measures: "Not applicable. The 8,257 incidents count the dataset size, not an AI outcome."
      provenance: self-reported
      source_ref: ENISA-ETL-2026
    - lever: quality
      description: "A domain-adapted encoder (DarkBERT) reached a strict F1 of 89.33% for extracting eight strategic entity types from social-media alerts, ahead of general-purpose baselines and fine-tuned LLMs, which also had much higher inference latency."
      figure: "89.33% strict F1"
      measures: "Strict entity-level F1 on STINER, an expert-annotated corpus of 2,100 real-world alerts; nine models across 12 configurations were benchmarked. Authors' own corpus, accepted at RAID 2026."
      provenance: self-reported
      source_ref: ARXIV-2608.14418
  prerequisites:
    - "A defined source list and curation rules; ENISA curates the dataset to avoid inflating threats when sector or country reporting is vague."
    - "Primary sources recorded for each assessment (ENISA references primary sources in footnotes)."
  risks_and_guardrails:
    - "ENISA says open sources and voluntarily shared information do not give a complete picture, and that increased reporting can reflect audience interest rather than higher activity (ENISA-ETL-2026, Methodology)."
    - "Source volatility: ENISA warns cited forums and leak sites may disappear (ENISA-ETL-2026, Disclaimer)."
  human_checkpoints:
    - "All AI outputs were reviewed and validated by subject-matter experts (ENISA-ETL-2026, Disclaimer)."
  role_evolution: "ENISA's methodology says it does not use AI to identify trends or formulate assessments, so analysts remain responsible for selecting and validating evidence (ENISA-CTL-2026, section 2.4.7). The methodology also says the process still involves a lot of manual work that could largely be automated, and that ENISA aims to publish more machine-readable output in the mid-term (section 3.1)."
  evidence_grade: B
  sources:
    - { ref: ENISA-ETL-2026, title: "ENISA Threat Landscape 2026", publisher: ENISA, type: regulator, url: "https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf", date: 2026-09, access: full, locator: "Disclaimer; Methodology section" }
    - { ref: ENISA-CTL-2026, title: "ENISA Cybersecurity Threat Landscape Methodology (updated 18 September 2026)", publisher: ENISA, type: regulator, url: "https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20CTL%20Methodology_Updated%2018%20september%202026.pdf", date: 2026-09-18, access: full, locator: "sections 2.4.7 and 3.1" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: Beyond Manual Hunting: OSINT Copilot with LLMs & Evidence-Based Collection, Enrichment, and Investigative Search at Scale", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "session abstract (Apura Cyber Intelligence, Brazil)" }
    - { ref: ARXIV-2608.14418, title: "STINER: Automated Extraction of Strategic Cyber Threat Intelligence from X", publisher: arXiv (Ech-Chammakhy et al.), type: academic, url: "https://arxiv.org/abs/2608.14418", date: 2026-08-14, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Grade B because a named regulator states it used AI in collection and processing; no measurement of effect is published. The Apura session is a conference abstract with no outcome figures."

- id: security-threat-intelligence-03
  title: Mapping intelligence report text to ATT&CK techniques
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Mapping adversary behaviour in reports to ATT&CK techniques is described by MITRE's Center for Threat-Informed Defense as difficult, error-prone and time-consuming. In an 18-person practitioner survey, 10 of 18 named mapping behaviour to standard taxonomies as a recurring challenge."
  solution: "An LLM proposes technique IDs for report text or sandbox output and an analyst reviews them. Newer designs ground each candidate in an evidence span and the official ATT&CK definition before accepting it."
  outcomes:
    - lever: quality
      description: "Seven open-source LLMs (8B to 236B parameters) were tested on complex unstructured reports; the best reached micro-F1 0.22, which the authors say is insufficient for production-grade ATT&CK classification. Prompt strategy and temperature gave no significant gains; parameter size correlated positively with F1."
      figure: "micro-F1 0.22 (best model)"
      measures: "Micro-averaged F1 for multi-label technique classification over 2,076 human-annotated sentences (1,281 technique-positive, 795 negative) from 83 complex CTI reports, 114 unique techniques, inter-annotator agreement kappa 0.68."
      provenance: independent
      source_ref: ARXIV-2606.18166
    - lever: quality
      description: "In a pilot, three LLMs mapped sandbox-report evidence to techniques with F1 0.71-0.72 against 0.16 for Sigma rules, but asserted techniques the evidence did not support and missed others; masquerading (T1036), labeled in 21 reports, was missed by all three."
      figure: "technique F1 0.71-0.72 (LLMs) vs 0.16 (Sigma)"
      measures: "F1 over 254 labeled main techniques across 45 held-out sandbox reports (sub-technique F1 0.66-0.67 over 263 labeled sub-techniques). Models: Claude Opus 4.8, GPT-5.5 and GLM 5.2 as named in the paper."
      provenance: self-reported
      source_ref: ARXIV-2609.01174
    - lever: quality
      description: "The authors of CTI2TTP report 76.48% and 87.39% macro-F1 on two evaluation sets, using evidence-anchored candidate generation then verification, and say this beats chain-of-thought prompting with the same backbone."
      figure: "76.48% / 87.39% macro-F1"
      measures: "Macro-F1 on TRAM-Clean (a cleaned version of the TRAM benchmark) and CTI2TTP-Bench respectively, both defined by the authors. Preprint, not peer-reviewed."
      provenance: self-reported
      source_ref: ARXIV-2605.25836
  prerequisites:
    - "A reference mapping set the team has labeled itself, to test any model before use."
    - "Version control of the ATT&CK release in use (ATT&CK v20 was released in October 2026)."
  risks_and_guardrails:
    - "The F1 figures above are not comparable: they use different data (sentences from complex reports versus technique-level labels on sandbox reports) and different models."
    - "Models both miss techniques that are evidenced and assert ones that are not; ten techniques were both missed where labeled and asserted where absent by every model in the pilot (ARXIV-2609.01174, Experiment 2)."
  human_checkpoints:
    - "Analyst reviews every technique assignment before it enters a tracking system or a shared product."
  role_evolution: "The work shifts from assigning techniques to reviewing and correcting proposed assignments. No source quantifies the review burden."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2606.18166, title: "Evaluating Open-Source LLMs for Multi-Label ATT&CK Technique Classification on CTI Reports", publisher: arXiv (Ryan et al.), type: academic, url: "https://arxiv.org/abs/2606.18166", date: 2026-06-16, access: full, locator: abstract }
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv (Vasan et al.), type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "Table 2b and Experiment 2 text; practitioner survey findings (introduction)" }
    - { ref: ARXIV-2605.25836, title: "CTI2TTP: Evidence-Grounded TTP Extraction from Cyber Threat Intelligence via Diverge-then-Converge Verification", publisher: arXiv (Cheng et al.), type: academic, url: "https://arxiv.org/abs/2605.25836", date: 2026-05-25, access: full, locator: "abstract (v2 revised 2026-10-13)" }
    - { ref: MITRE-CTID-TRAM-2023, title: "Threat Report ATT&CK Mapper (TRAM)", publisher: MITRE Center for Threat-Informed Defense, type: standard-setter, url: "https://ctid.mitre.org/projects/threat-report-attck-mapper-tram/", date: 2023-08-24, access: full, locator: "project description (page metadata date)" }
  last_reviewed: 2026-10-17
  notes: "Grade C: independent and authors' measurements on benchmarks and prototypes; no named deployment found. MITRE's TRAM page describes a fine-tuned-LLM approach and calls the tool measurably effective, but publishes no figure on the page; its page date is 2023, outside the preferred window."

- id: security-threat-intelligence-04
  title: Extracting, tagging and validating indicators of compromise from reports, sandbox output and scripts
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [data-reporting, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Indicators are buried in unstructured reports or noisy attack data. In an 18-person practitioner survey, 13 of 18 named isolating malicious indicators from noisy attack data as a recurring challenge. A wrongly extracted benign value, when shared as a blocklist entry, causes false detections in every recipient."
  solution: "LLMs read reports, sandbox logs or malicious scripts, return candidate indicators with context such as owner and abuse type, and analysts review the output before sharing."
  outcomes:
    - lever: quality
      description: "In a pilot on sandbox execution logs, LLMs reached indicator precision of 0.51-0.78 against 0.09 and 0.41 for two rule baselines, but recovered only 363-461 of 1,472 labeled indicators."
      figure: "precision 0.51-0.78; recall 0.25-0.31"
      measures: "Precision and recall of indicator extraction over 45 held-out sandbox reports with 1,472 labeled indicators; three LLMs (Claude Opus 4.8, GPT-5.5, GLM 5.2 as named in the paper) versus two rule baselines."
      provenance: self-reported
      source_ref: ARXIV-2609.01174
    - lever: quality
      description: "A preregistered audit of two low-cost models and one flagship control found extraction unreliable across tiers, with micro precision 0.03-0.34 and verbalized-confidence calibration error 0.53-0.94. Most false candidates were background mentions (65.6%) or gold-scope gaps (19.9%), with 1.2% unsupported."
      figure: "micro precision 0.03-0.34"
      measures: "Micro precision of entity extraction over 354 incident campaigns (315 unique reports; 630 model-report evaluations); the 65.6%, 19.9% and 1.2% shares are back-projected from a 360-candidate sample."
      provenance: independent
      source_ref: ARXIV-2610.20417
    - lever: quality
      description: "TagZilla, an LLM-based tagger for indicator owner and abuse type, reached F1 0.94 for owner tagging and 0.93 for abuse-type tagging, and was then applied to 765 reports."
      figure: "F1 0.94 / 0.93"
      measures: "F1 on a manually built ground truth of 100 threat reports with 1,534 indicators; authors' own platform."
      provenance: self-reported
      source_ref: ARXIV-2608.28124
    - lever: quality
      description: "On 634 manually verified malicious scripts, the strongest model reached only 65.4 F1 for static indicator recovery; encryption of the indicators degrades recovery sharply."
      figure: "65.4 F1 (best model)"
      measures: "F1 for static recovery of URLs, domains, IP addresses and filesystem artifacts across JavaScript, PowerShell and VBScript samples (SCRIPTIOC-BENCH). A separate 336-program benchmark finds encryption-based concealment severely degrades recovery (ARXIV-2605.06910)."
      provenance: independent
      source_ref: ARXIV-2609.06149
  prerequisites:
    - "A labeled sample of the team's own reports to measure precision and recall before relying on output."
    - "A policy on whether false positives or missed indicators cost more for the intended use (blocklist versus hunting lead)."
  risks_and_guardrails:
    - "The pilot's authors note shared IOCs are consumed as blocklists, so a benign value reported as an indicator raises false detections in every organization that blocks it (ARXIV-2609.01174, Experiment 1)."
    - "A single misattribution sentence flipped high-confidence relation judgements in 95.6-100% of 45 counterfactual targets (ARXIV-2610.20417)."
  human_checkpoints:
    - "Analyst reviews indicators before publication; the pilot's authors conclude each step needs expert supervision (ARXIV-2609.01174, abstract)."
  role_evolution: "No source describes a change in roles; the SoK reports that only 3 of 18 practitioners use LLMs today, and most conversion of attack data into CTI is manual with scripted parsing."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv (Vasan et al.), type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "Table 2a; Experiment 1; introduction (practitioner survey)" }
    - { ref: ARXIV-2610.20417, title: "From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence", publisher: arXiv (Qian), type: academic, url: "https://arxiv.org/abs/2610.20417", date: 2026-10-14, access: full, locator: abstract }
    - { ref: ARXIV-2608.28124, title: "TagZilla: Automated Owner and Abuse Type Tagging for Indicators of Compromise in Threat Reports", publisher: arXiv (Gomez, Caballero), type: academic, url: "https://arxiv.org/abs/2608.28124", date: 2026-08-28, access: full, locator: abstract }
    - { ref: ARXIV-2609.06149, title: "SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs", publisher: arXiv (Kim et al.), type: academic, url: "https://arxiv.org/abs/2609.06149", date: 2026-09-05, access: full, locator: abstract }
    - { ref: ARXIV-2605.06910, title: "Benchmarking Large Language Models for IoC Recovery under Adversarial Code Obfuscation and Encryption", publisher: arXiv (Morales et al.), type: academic, url: "https://arxiv.org/abs/2605.06910", date: 2026-05-07, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Grade C: academic benchmarks and prototypes, no deployment. Results conflict in level (precision 0.51-0.78 in one setting, 0.03-0.34 in another) because tasks, corpora and scoring differ; the 2610.20417 corpus is full-length incident reports and strict entity matching. Both preprints, not peer reviewed. The model names above are as printed in the sources."

- id: security-threat-intelligence-05
  title: Redacting victim-identifying detail from intelligence before it is shared
  archetype: security
  module: threat-intelligence
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Sharing intelligence from an incident requires removing personal and organization-identifying information while keeping the intelligence useful. In an 18-person practitioner survey, 17 of 18 named preventing exposure of sensitive information during sharing as a recurring challenge. SANS reports 55% of organizations lack legally reviewed CTI sharing processes."
  solution: "An LLM proposes values to remove from an incident report, each with a replacement, and an analyst reviews against a sharing policy. The pilot found the model follows whichever goal the prompt states (privacy or utility), so a written redaction policy is needed."
  outcomes:
    - lever: risk
      description: "Under a privacy-preserving prompt, three LLMs redacted nearly all injected identifiers (missing at most 3 of 92) but one removed 50 values that identified no one (35% of everything it removed). Under a utility-preserving prompt, errors reversed and two models missed 8-10 of 92 injected values."
      figure: "F1 0.78-0.99 (privacy prompt); 0.84-0.92 (utility prompt)"
      measures: "F1 for detecting injected PII and OII values (92 values plus 10 descriptive phrases) in 4 held-out incident reports, for three LLMs under two prompts."
      provenance: self-reported
      source_ref: ARXIV-2609.01174
  prerequisites:
    - "A redaction policy stating which details a shared report must keep and which it may lose (for example attacker routes through the victim network)."
    - "Legal review of the sharing process; SANS reports this is missing at 55% of organizations."
    - "A model option that keeps the unredacted report inside the organization, since sending it to a third party for redaction discloses what the organization is trying to protect (ARXIV-2609.01174, discussion)."
  risks_and_guardrails:
    - "FIRST's TLP standard makes the source responsible for ensuring recipients can follow the label, and requires recipients to obtain permission before sharing more widely than the label allows (FIRST-TLP-2022, Usage section)."
    - "NIST SP 800-150 section 3.4 advises organizations to set information sharing rules with input from legal and privacy officials and to describe requirements for redacting or sanitizing information (NIST-SP800150-2016, section 3.4)."
    - "NIS2 Article 29 and DORA Article 45 require sharing arrangements to protect the sensitive nature of what is shared; DORA Article 45 adds personal-data protection under the GDPR and competition-law guidelines."
  human_checkpoints:
    - "Analyst or legal reviewer confirms the redacted version before release to a sharing community."
  role_evolution: "No source describes role change. Practitioners rated this task among the strongest candidates for AI support, while doubting reliability and worrying about privacy (ARXIV-2609.01174, introduction)."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv (Vasan et al.), type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "Table 3 and Experiment 3; introduction" }
    - { ref: SANS-CTI-2026, title: "SANS 2026 CTI Survey Insights (press release and key findings)", publisher: SANS Institute, type: survey, url: "https://www.sans.org/research/cyber-threat-intelligence-report", date: 2026-05-19, access: full, locator: "key findings: 55% lack legally reviewed CTI sharing processes" }
    - { ref: FIRST-TLP-2022, title: "Traffic Light Protocol (TLP) version 2.0", publisher: FIRST, type: standard-setter, url: "https://www.first.org/tlp/", date: 2022-08, access: full, locator: "Usage rules and definitions" }
    - { ref: NIST-SP800150-2016, title: "Guide to Cyber Threat Information Sharing (SP 800-150)", publisher: NIST, type: standard-setter, url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-150.pdf", date: 2016-10, access: full, locator: "section 3.4 and 3.4.1" }
    - { ref: EURLEX-NIS2-2022, title: "Directive (EU) 2022/2555 (NIS 2)", publisher: EUR-Lex, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555", date: 2022-12-14, access: full, locator: "Articles 29 and 30" }
    - { ref: EURLEX-DORA-2022, title: "Regulation (EU) 2022/2554 (DORA)", publisher: EUR-Lex, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554", date: 2022-12-14, access: full, locator: "Article 45" }
  last_reviewed: 2026-10-17
  notes: "Grade C: one academic pilot on 4 reports; small sample. Governance sources are cited for constraints, not as evidence of AI use. The SoK states a reservation that a redaction tool needs a policy and has no baseline."

- id: security-threat-intelligence-06
  title: Packaging findings as STIX objects for sharing platforms
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [data-reporting, document-production]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Indicators often circulate in ad hoc emails and chat threads that bypass STIX/TAXII pipelines, slowing collective defence, according to a CISA session at FIRST 2026. In the practitioner survey, 7 of 18 named translating CTI into the formats sharing platforms require as a recurring challenge."
  solution: "An LLM turns an analyst's findings into STIX 2.x objects and relationships for a TAXII feed or sharing community; a validator and an analyst check the content as well as the format."
  outcomes:
    - lever: quality
      description: "In the pilot, every model produced valid STIX files that preserved the supplied findings and identified software type reliably (19 of 21), but every model asserted relationships the findings did not support; one asserted 73 links where 38 were correct."
      figure: "38 of 73 links correct (GLM 5.2); 67 asserted (GPT-5.5)"
      measures: "Correct links among links asserted in generated STIX files, on the reserved test campaigns; a link counts as correct only if it connects the right objects with the right relationship type."
      provenance: self-reported
      source_ref: ARXIV-2609.01174
    - lever: speed
      description: "CISA described IMX, a newly open-sourced platform that lets analysts publish STIX 2.x packages in minutes through a five-question guided mode (who, what, where, how, why). The abstract makes no AI claim and publishes no usage figures."
      figure: "none published"
      measures: "Not applicable; session abstract only."
      provenance: self-reported
      source_ref: FIRST-CON-2026
  prerequisites:
    - "A STIX/TAXII capability on the receiving side; CISA's AIS service requires a TAXII 2.1 client, a PKI certificate and an interconnection agreement."
    - "Validation that checks claims against the findings, not only schema validity."
  risks_and_guardrails:
    - "A wrong link passes every format check; the pilot's authors recommend requiring each link to name the finding it rests on (ARXIV-2609.01174, Experiment 4)."
    - "CISA 2015's liability and privacy protections for sharing through AIS depend on sharing in accordance with the Act; the page records extension of the Act through 2026-09-30 and I could not confirm its status after that date (CISA-AIS-2026)."
  human_checkpoints:
    - "Analyst verifies the relationships a package asserts before publishing to a feed."
  role_evolution: "CISA's IMX is aimed at experts who lack schema expertise, which lowers the skill needed to publish structured intelligence; no source measures the effect."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv (Vasan et al.), type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "Table 4 and Distribution experiment" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: Indicator Message eXchange (IMX)", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06-15, access: full, locator: "session abstract, Brian DeWyngaert (CISA), 15 June 2026" }
    - { ref: CISA-AIS-2026, title: "Automated Indicator Sharing (AIS)", publisher: CISA, type: regulator, url: "https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/automated-indicator-sharing-ais", date: 2026-10-17, access: full, locator: "participation steps; CISA 2015 sunset paragraph (page undated; date is retrieval date)" }
  last_reviewed: 2026-10-17
  notes: "Grade C. IMX is included as sharing-tool context; its abstract does not say it uses AI. Landing page undated, so the CISA date is the retrieval date."

- id: security-threat-intelligence-07
  title: Turning intelligence reports into detection rules and queries
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [software-systems, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Detection engineers must translate threat reports into precise, testable rules. Open-source and industry rule repositories often fail to keep pace with emerging threats and need customisation."
  solution: "An LLM or agent reads a report, extracts behaviours and commands, and drafts detection rules (Sigma, regular expressions, SIEM queries) that are validated against telemetry or rule repositories before an engineer approves them."
  outcomes:
    - lever: quality
      description: "SIGMERGE, evaluated by its authors against 16 baselines and 13 LLMs on 23 metrics with 10 case studies in real security systems, contributed 4 novel Sigma rules to the official repository, all formally accepted."
      figure: "4 of 4 submitted rules accepted"
      measures: "Rules contributed by the authors to the official Sigma repository that were accepted; the number submitted is not stated beyond 'all'."
      provenance: self-reported
      source_ref: USENIX-SIGMERGE-2026
    - lever: quality
      description: "Sixteen frontier models were scored on interpreting a CTI report and building a detection rule against emulated attacks; the top reward was 0.637, and CTI-specific tools improved performance. A follow-up on 26 models finds an open-weight model can match the strongest closed ones at under a tenth of the cost if given enough turns."
      figure: "best reward 0.637; open-weight at under 1/10 cost"
      measures: "CTI-REALM trajectory-based reward for the top model (Claude Opus 4.6 (High)); the follow-up's cost comparison is for the best open-weight model against leading closed models, with the benchmark's message limit relaxed."
      provenance: independent
      source_ref: ARXIV-2603.13517
    - lever: quality
      description: "IOCRegex-gen, which converts IOCs to regular expressions, reports an average hit rate of 99.1% and a false-positive rate of 0.8%."
      figure: "99.1% hit rate; 0.8% false positives"
      measures: "Hit rate and false-positive rate over more than 3,000 real CTI reports and 2,400 ground-truth strings from the MITRE ATT&CK Evaluations; authors' own system."
      provenance: self-reported
      source_ref: ARXIV-2604.12228
  prerequisites:
    - "Telemetry and a test harness to run candidate rules against; benchmark gains came from CTI-specific tools in the agent environment."
    - "Rule-repository conventions the output must match."
  risks_and_guardrails:
    - "Syntactic validity is a weak proxy for semantic rule quality: several baselines emit well-formed YAML with weak detection logic (ARXIV-2610.09007)."
    - "The CTI-REALM follow-up finds the published message limit is a confound: tasks that exhaust it score zero on every checkpoint, so results partly measure which models finish in time (ARXIV-2610.14180)."
  human_checkpoints:
    - "Detection engineer reviews rule logic and tests it before deployment; the SIGMERGE contribution went through the repository's acceptance process."
  role_evolution: "The authors of CTI-REALM describe the benchmark as showing potential to support labor-intensive parts of detection engineering; no source reports staffing changes."
  evidence_grade: C
  sources:
    - { ref: USENIX-SIGMERGE-2026, title: "From Texts to Rules: Generating Sigma Rules with Large Language Models from Cyber Threat Reports", publisher: USENIX Security Symposium 2026 (Cai et al.), type: academic, url: "https://www.usenix.org/conference/usenixsecurity26/presentation/cai", date: 2026-08, access: full, locator: "abstract on the technical sessions listing" }
    - { ref: ARXIV-2603.13517, title: "CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities", publisher: arXiv (Chakraborty et al.), type: academic, url: "https://arxiv.org/abs/2603.13517", date: 2026-03-13, access: full, locator: abstract }
    - { ref: ARXIV-2610.14180, title: "Unconstrained CTI-REALM with Open-Weights", publisher: arXiv (Garg et al.), type: academic, url: "https://arxiv.org/abs/2610.14180", date: 2026-10-09, access: full, locator: abstract }
    - { ref: ARXIV-2604.12228, title: "From IOCs to Regex: Automating CTI Operationalization for SOC with LLMs", publisher: arXiv (Tseng et al.), type: academic, url: "https://arxiv.org/abs/2604.12228", date: 2026-04-14, access: full, locator: abstract }
    - { ref: ARXIV-2610.09007, title: "Sigma-Hunter: A Domain-Specific Language Model for Threat Hunting and Detection Engineering", publisher: arXiv (Davaslioglu, Kompella), type: academic, url: "https://arxiv.org/abs/2610.09007", date: 2026-10-06, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Grade C: peer-reviewed prototype (USENIX Security 2026) plus preprints and benchmarks; no named operational deployment or measured production outcome. The accepted-rules figure is the only external-acceptance signal. CTI-REALM authors are named in the arXiv record; the landscape file attributes the benchmark to Microsoft, which I did not confirm from the abstract page."

- id: security-threat-intelligence-08
  title: Generating environment-aware hunt leads from intelligence reports
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, expert-judgment]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Threat hunting depends on turning unstructured reports into concise, investigable hypotheses grounded in observable artifacts and techniques. Doing it manually is slow, and automated approaches stop at entities, ignore the defender's own environment, or treat each report in isolation."
  solution: "A retrieval system combines vector search with a knowledge graph seeded with ATT&CK, and constrains each lead to the defender's own assets and controls, emitting structured hunt leads rather than loose indicators."
  outcomes:
    - lever: quality
      description: "AHLERT raised mean F1 from 0.44 to 0.85 over a flat retrieval baseline and reports an effectiveness score of about 86.95% against off-the-shelf models."
      figure: "mean F1 0.44 to 0.85"
      measures: "Mean F1 for lead extraction on public CTI reports for well-known APTs across multiple proprietary and open-weight models, hybrid retrieval with ontology grounding versus single-route flat retrieval; authors' own system, accepted at an IEEE DSC 2026 workshop."
      provenance: self-reported
      source_ref: ARXIV-2609.08790
  prerequisites:
    - "An asset and control inventory expressed in a form the retrieval can ground against."
    - "Telemetry coverage for the techniques a lead refers to."
  risks_and_guardrails:
    - "Leads built from public reports are only as good as the report; see the vendor-bias finding in use case 12."
    - "A related FIRST 2026 session shows a single attacker-crafted report or email can bias retrieval and generation in LLM-assisted workflows (FIRST-CON-2026); see use case 15."
  human_checkpoints:
    - "Hunter decides whether a lead is worth investigating and runs the hunt."
  role_evolution: "Hunters would spend less time reading reports and more time testing generated hypotheses; no source measures this."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2609.08790, title: "Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports", publisher: arXiv (Prakash et al.), type: academic, url: "https://arxiv.org/abs/2609.08790", date: 2026-09-08, access: full, locator: abstract }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: One Poisoned Artifact Can Steer Your AI", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06-18, access: full, locator: "session abstract, 18 June 2026" }
  last_reviewed: 2026-10-17
  notes: "Grade C: single prototype evaluation on public reports; no deployment."

- id: security-threat-intelligence-09
  title: Autonomous hunting for malicious activity in raw telemetry (negative measured evidence)
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Hunting requires finding malicious events in large volumes of raw logs without guided questions. Hunters are scarce, and vendors promise AI-driven hunting."
  solution: "An LLM agent iteratively queries a log database, forms hypotheses and flags malicious events. The measured results show current models fall far short of a bar for unsupervised use."
  outcomes:
    - lever: quality
      description: "The best of five frontier models submitted correct flags for only 3.8% of malicious events on average, no run found all flags, and no model met a 50% recall bar on every ATT&CK tactic; the leader cleared the bar on 5 of 13 tactics."
      figure: "3.8% recall (best model)"
      measures: "Average recall of malicious event timestamps across 26 campaigns covering 105 of 106 procedures wrapped from OTRF Security-Datasets, each presented as 75,000-135,000 log records in a SQLite database; five models evaluated (Claude Opus 4.6, GPT-5, Gemini 3.1 Pro, Kimi K2.5, Gemini 3 Flash)."
      provenance: independent
      source_ref: ARXIV-2604.19533
  prerequisites:
    - "A benchmark or replay environment drawn from the team's own telemetry before any autonomy is granted."
  risks_and_guardrails:
    - "The benchmark's authors define a passing score as at least 50% recall on every tactic as the minimum bar for unsupervised SOC deployment, and conclude no model passes."
    - "A separate benchmark finds that structured, modular workflows help while open-ended reasoning shows clear limits in real threat hunting (ARXIV-2509.23571, ICML 2026)."
    - "A FIRST 2026 session reports early findings from a controlled experiment on whether a general-purpose LLM can do tier-1 triage on synthetic alerts with hidden campaigns and progressively adversarial noise; it publishes no figures in its abstract."
  human_checkpoints:
    - "Hunters remain the decision-makers; the evidence does not support removing them."
  role_evolution: "The measured shortfall implies hunters stay in the loop for open-ended work; AI is better suited to well-specified sub-tasks such as those in use cases 3, 4, 7 and 8."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2604.19533, title: "Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps", publisher: arXiv (Chona et al.), type: academic, url: "https://arxiv.org/abs/2604.19533", date: 2026-04-21, access: full, locator: "abstract (v3 updated leaderboard 2026-04-23)" }
    - { ref: ARXIV-2509.23571, title: "Benchmarking LLM-Assisted Blue Teaming via Standardized Threat Hunting", publisher: arXiv (Meng et al.; ICML 2026), type: academic, url: "https://arxiv.org/abs/2509.23571", date: 2025-09-28, access: full, locator: "abstract (v3 revised 2026-05-28)" }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: Can a General-Purpose LLM Do Tier-1 Triage?", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06, access: full, locator: "session abstract (speaker Romulo Rocha); the landscape file attributes it to TandemTrace, which I did not see in the program text" }
  last_reviewed: 2026-10-17
  notes: "Grade C. This entry records negative independent evidence; the maturity is emerging and the ladder shows the aspiration the benchmark tests, not a state anyone has reached. Benchmark covers Windows event logs only."

- id: security-threat-intelligence-10
  title: Scoring and prioritising intelligence items and indicators
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [data-reporting, expert-judgment]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Teams receive more intelligence than they can assess. Flashpoint's interview study reports alert noise and false positives as the most common operational problem (65% of respondents) and insufficient analyst bandwidth as next (55%)."
  solution: "A model assigns a threat level or priority to feed items or vulnerability evidence, with source-linked reasoning for analyst inspection."
  outcomes:
    - lever: quality
      description: "On threat-level determination from MISP OSINT feeds, zero-shot models performed weakly; after supervised fine-tuning, F1 reached 0.40-0.58 depending on base model, which the authors judge too low for practical deployment."
      figure: "F1 0.40-0.58 (fine-tuned)"
      measures: "F1 on a curated dataset derived from public MISP OSINT feeds, eight LLMs compared zero-shot and fine-tuned."
      provenance: self-reported
      source_ref: ARXIV-2609.07582
    - lever: quality
      description: "POLAR, an evidence-synthesis framework that estimates near-term exploitation likelihood and organises mitigations by urgency, is reported to improve threat ranking and mitigation retrieval over baselines; the abstract gives no figure."
      figure: "none published in abstract"
      measures: "Not stated in the abstract."
      provenance: self-reported
      source_ref: ARXIV-2610.07298
  prerequisites:
    - "Labeled history of the team's own prioritisation decisions to test against."
  risks_and_guardrails:
    - "Raw volume can mislead without threat-intelligence context: Google's group notes automated CVE assignment can inflate counts, for example about 5,000 Linux Kernel CVEs from January to August 2026 with no observed exploited zero-days (GTIG-VULNTRENDS-2026)."
  human_checkpoints:
    - "Analyst confirms priority before an item drives blocking, patching or escalation."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2609.07582, title: "Benchmarking LLMs for Threat Level Determination", publisher: arXiv (Wang et al.), type: academic, url: "https://arxiv.org/abs/2609.07582", date: 2026-09-07, access: full, locator: abstract }
    - { ref: ARXIV-2610.07298, title: "Polar: LLM-Powered Synthesis of Real-World Cyber Evidence for Prioritization and Mitigation", publisher: arXiv (Tang et al.), type: academic, url: "https://arxiv.org/abs/2610.07298", date: 2026-10-05, access: full, locator: abstract }
    - { ref: FLASHPOINT-ETIR-2026, title: "Nearly Half of Enterprise Threat Intelligence Teams Are Using or Piloting Agentic AI as AI Threats Lead 2027 Priorities, Flashpoint Research Finds", publisher: Flashpoint (PRNewswire/PRWeb), type: survey, url: "https://www.prweb.com/releases/nearly-half-of-enterprise-threat-intelligence-teams-are-using-or-piloting-agentic-ai-as-ai-threats-lead-2027-priorities-flashpoint-research-finds-302906892.html", date: 2026-10-13, access: full, locator: "paragraph on pain points" }
    - { ref: GTIG-VULNTRENDS-2026, title: "Vulnerability Discovery and Exploitation Trends in the AI Era", publisher: Google Threat Intelligence Group, type: vendor, url: "https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/", date: 2026-09-30, access: full, locator: "section 'Distinguishing Threat Risk from CVE Inflation'" }
  last_reviewed: 2026-10-17
  notes: "Grade C. The Flashpoint pain-point figures come from a vendor-commissioned study of more than 20 interviewees and are context, not evidence for the scoring approach."

- id: security-threat-intelligence-11
  title: Agentic workflows across collection, enrichment and briefing, with analyst control
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting, document-production]
  pattern: research-brief
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: "CTI teams are small, and intelligence often arrives late or never reaches the front line. Cyware's RSAC 2026 survey reports about 40% of respondents say integration of intelligence into workflows is mostly manual."
  solution: "Agents run multi-step collection, enrichment and triage on a threat-intelligence platform and hand results to analysts. Vendors expose platform data to LLMs through connectors (for example SOCRadar's MCP server). Survey respondents say they want agents that keep analysts in control."
  outcomes:
    - lever: capacity
      description: "Flashpoint reports 25% of the organizations it interviewed use agentic AI in production for threat-intelligence work, 20% are piloting and 35% plan adoption within 12 to 24 months; 75% are still evaluating where it creates value."
      figure: "25% production; 20% piloting; 35% planning"
      measures: "Share of more than 20 threat-intelligence budget owners and influencers at large North American enterprises (financial services and insurance, healthcare and biotech, retail, IT and telecom) interviewed in early fall 2026. A small qualitative sample commissioned by Flashpoint; not an adoption measure."
      provenance: vendor-published
      source_ref: FLASHPOINT-ETIR-2026
    - lever: speed
      description: "Cyware reports effective automation between CTI and SecOps tools doubled from 13% to 26% year on year, and 79.6% of respondents report measurable improvement in intelligence operations from AI."
      figure: "13% to 26%; 79.6%"
      measures: "Shares of respondents in Cyware's survey of security professionals at RSAC 2026; the number of respondents is not stated, and the respondent set is conference attendees. Vendor survey."
      provenance: vendor-published
      source_ref: CYWARE-RSAC-2026
  prerequisites:
    - "Integration between the intelligence platform and the tools that act on intelligence; Cyware reports only 27.5% of respondents have intelligence fully integrated into detection and response."
    - "Evidence of value before wider rollout: 55% of Flashpoint interviewees require demonstrable time savings or extended analyst reach, and 35% want a proof of concept first."
  risks_and_guardrails:
    - "Cyware reports 77% of respondents favour AI that prioritises analyst oversight, and that 56% of organizations are developing AI security guardrails while 32.1% have defined policies."
    - "SANS notes write-in responses consistently stress analyst oversight for high-stakes calls (SOCRADAR-SANSCTI-2026)."
    - "Unpredictable AI cost and lack of demonstrable value are cited barriers to investment (FLASHPOINT-ETIR-2026)."
    - "NIS2 recital 51 asks that any AI used for detection comply with data-protection principles of accuracy, minimisation, fairness, transparency and security (EURLEX-NIS2-2022)."
  human_checkpoints:
    - "Analyst approval for high-stakes calls and for any action that changes a control; respondents want analyst control (CYWARE-RSAC-2026)."
  role_evolution: "Cyware reports 72.4% of respondents are likely to build their own custom security AI agents, which implies analysts and engineers building workflows rather than only consuming them. SANS reports security operations (71%) has overtaken threat hunting as the leading CTI use case, so CTI roles are increasingly tied to daily operations (SANS-CTI-2026)."
  evidence_grade: C
  sources:
    - { ref: FLASHPOINT-ETIR-2026, title: "Nearly Half of Enterprise Threat Intelligence Teams Are Using or Piloting Agentic AI as AI Threats Lead 2027 Priorities, Flashpoint Research Finds", publisher: Flashpoint (PRNewswire/PRWeb), type: survey, url: "https://www.prweb.com/releases/nearly-half-of-enterprise-threat-intelligence-teams-are-using-or-piloting-agentic-ai-as-ai-threats-lead-2027-priorities-flashpoint-research-finds-302906892.html", date: 2026-10-13, access: full, locator: "paragraphs 5-8 and methodology paragraph" }
    - { ref: CYWARE-RSAC-2026, title: "What Security Professionals at RSAC2026 Told Us About AI and Threat Intelligence", publisher: Cyware, type: survey, url: "https://www.cyware.com/blog/what-security-professionals-at-rsac2026-told-us-about-ai-and-threat", date: 2026-04-28, access: full, locator: "summary bullets and body" }
    - { ref: SOCRADAR-SANSCTI-2026, title: "2026 SANS CTI Survey Report: Key Findings on CTI's Influence Gap", publisher: SOCRadar, type: vendor, url: "https://socradar.io/blog/2026-sans-cti-survey-report-findings/", date: 2026-07-01, access: full, locator: "paragraphs on AI use and the SOCRadar MCP server" }
    - { ref: SANS-CTI-2026, title: "SANS 2026 CTI Survey Insights (press release and key findings)", publisher: SANS Institute, type: survey, url: "https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report", date: 2026-05-19, access: full, locator: "paragraph on SecOps as top use case" }
    - { ref: EURLEX-NIS2-2022, title: "Directive (EU) 2022/2555 (NIS 2)", publisher: EUR-Lex, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555", date: 2022-12-14, access: full, locator: "recital 51" }
  last_reviewed: 2026-10-17
  notes: "Grade C: both quantified sources are vendor-authored or vendor-commissioned with small or unstated samples. Maturity is piloting because Flashpoint's 25% in production is a share of about 20 interviewees, not a named deployment. The ladder level is delegate because the sources describe agents owning multi-step work; they do not specify the scope of autonomy."

- id: security-threat-intelligence-12
  title: Measuring coverage, overlap and bias across intelligence sources
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [data-reporting, research-synthesis]
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Annual incident-response and threat-intelligence reports frequently contradict each other on top intrusion vectors and on definitions such as credential misuse. A FIRST 2026 session from Team Cymru argues the contradictions come from structural bias in each vendor's data-collection pipeline."
  solution: "An LLM pipeline structures a large body of reports (actors, victims, vendors, indicators, techniques) so a team can compare vendor coverage and decide how many sources add value. A 2026 study did this for 16,096 reports over two decades."
  outcomes:
    - lever: quality
      description: "The study finds a fragmented ecosystem of silos with geographic and sectoral reporting biases, low overlap between vendors, and diminishing returns from additional sources beyond a few core providers."
      figure: "16,096 reports analysed"
      measures: "Count of open-source CTI reports ingested and structured by the authors' LLM pipeline; no overall accuracy figure is given in the abstract."
      provenance: independent
      source_ref: ARXIV-2602.17458
    - lever: risk
      description: "A measurement using watermarked network indicators found that dissemination of submitted threat intelligence almost always leads to disruption of threats, but selective sharing limits utility and bottleneck vendors delay sharing by hours to days."
      figure: "delays of hours to days"
      measures: "Propagation of watermarked binaries through the threat-intelligence ecosystem across submission, extraction, sharing and disruption stages; not an AI use case, included as measurement of the sharing ecosystem."
      provenance: independent
      source_ref: NDSS-TIECO-2026
  prerequisites:
    - "Access to a corpus of the reports the team subscribes to."
  risks_and_guardrails:
    - "Treat vendor reports as partial lenses rather than authoritative truth (FIRST-CON-2026, Team Cymru session)."
    - "ENISA similarly warns that reported volume can reflect audience interest, not activity (ENISA-ETL-2026)."
  human_checkpoints:
    - "Analyst decides subscription and weighting changes from the comparison."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2602.17458, title: "The CTI Echo Chamber: Fragmentation, Overlap, and Vendor Specificity in Twenty Years of Cyber Threat Reporting", publisher: arXiv (Suarez-Roman et al.), type: academic, url: "https://arxiv.org/abs/2602.17458", date: 2026-02-19, access: full, locator: "abstract (v3 revised 2026-08-19)" }
    - { ref: NDSS-TIECO-2026, title: "Actively Understanding the Dynamics and Risks of the Threat Intelligence Ecosystem", publisher: NDSS Symposium 2026 (Galloway et al.), type: academic, url: "https://www.ndss-symposium.org/ndss-paper/actively-understanding-the-dynamics-and-risks-of-the-threat-intelligence-ecosystem/", date: 2026-02, access: full, locator: abstract }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: Disparate Data, Distorted Decisions: Vendor Data Bias in CTI", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06-15, access: full, locator: "session abstract, 15 June 2026 (Eli Woodward, Team Cymru)" }
  last_reviewed: 2026-10-17
  notes: "Grade C: one academic study; no organization reports using this to manage subscriptions. The NDSS paper is a measurement of the ecosystem and uses no AI; it is cited for the sharing-delay finding only."

- id: security-threat-intelligence-13
  title: Building cross-source knowledge graphs from intelligence reports
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting]
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "The same threat appears under unrelated names in different reports, and reports are unstructured, so teams cannot easily link actors, campaigns, techniques and indicators across sources."
  solution: "LLM pipelines extract entities and relations per report, verify them against evidence and ATT&CK definitions, and merge them into one graph. One design runs a local model to keep sensitive internal incident data from reaching an enterprise API."
  outcomes:
    - lever: quality
      description: "ANCHOR with a local LLM closely matches enterprise-LLM typing performance and outperforms baselines on ontology typing and schema compliance across the UCO, STIX and MALOnt schemas. BEACON and TACTIC-KG report gains over baselines; their abstracts give no single headline figure I could verify."
      figure: "none verified"
      measures: "Not stated as a single figure in the abstracts."
      provenance: self-reported
      source_ref: ARXIV-2606.01208
  prerequisites:
    - "A schema choice (STIX, UCO or other) and a validator."
  risks_and_guardrails:
    - "Both BEACON and CTI2TTP use a propose-then-verify design that grounds candidates in report evidence to suppress misclassification and hallucination."
    - "Confidentiality: ANCHOR's authors motivate a local model by privacy constraints on sending internal incident data to enterprise APIs."
  human_checkpoints:
    - "Analyst validates merged entities before they inform attribution or reporting."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2606.01208, title: "Schema-Agnostic Knowledge Graph Construction via Hybrid Ontology Discovery for Cyber Threat Intelligence", publisher: arXiv (Kim et al.), type: academic, url: "https://arxiv.org/abs/2606.01208", date: 2026-05-31, access: full, locator: abstract }
    - { ref: ARXIV-2608.28394, title: "BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence", publisher: arXiv (Li et al.), type: academic, url: "https://arxiv.org/abs/2608.28394", date: 2026-08-28, access: full, locator: abstract }
    - { ref: ARXIV-2607.05001, title: "TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction", publisher: arXiv (Bouchiha, Blanc), type: academic, url: "https://arxiv.org/abs/2607.05001", date: 2026-07-06, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Grade C: three preprints, none deployed; I did not read the full texts, so no figures are claimed."

- id: security-threat-intelligence-14
  title: Active elicitation of intelligence from underground forums by a multi-agent system
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, client-interaction]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Valuable intelligence in underground forums has moved to private or harder-to-reach spaces, so passive monitoring misses it."
  solution: "A multi-agent LLM system (DarkBot, eleven agents) decides whether to engage, generates questions guided by ATT&CK tactics, adapts its style to the forum, and filters for relevance and safety. This is an active agent interacting with threat actors, so it adds legal and ethical review questions that passive collection does not."
  outcomes:
    - lever: quality
      description: "In a controlled evaluation the system recovered 72.8% of validated ATT&CK techniques present in the original discussions from the first post alone and outperformed a monolithic baseline. In a prospective matched deployment, threads assigned to it accumulated an average of 3.85 more CTI entities than controls over seven days, and across 104 live conversations no account suspensions or accusations of automated participation were observed. The layered safety design contained all injected jailbreak attempts."
      figure: "72.8% of techniques; +3.85 entities per thread"
      measures: "Share of validated MITRE ATT&CK techniques recovered across 100 CrimeBB conversations; mean extra CTI entities per thread over seven days against matched controls; 104 live forum conversations for the no-suspension observation. Authors' own system."
      provenance: self-reported
      source_ref: ARXIV-2608.23185
  prerequisites:
    - "Legal and ethics review of active engagement with threat actors; the abstract does not state what review was done."
  risks_and_guardrails:
    - "The authors report engagement gating and safety filtering, and that all injected jailbreak attempts were contained at the pipeline level."
  human_checkpoints:
    - "Not described in the abstract; I did not read the full paper."
  role_evolution: "Would move forum analysts from reading threads toward supervising agents; no source states this."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2608.23185, title: "Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums", publisher: arXiv (Bossi et al.), type: academic, url: "https://arxiv.org/abs/2608.23185", date: 2026-08-24, access: full, locator: abstract }
  last_reviewed: 2026-10-17
  notes: "Grade C: a preprint prototype. The point about legal and ethical review is an analyst observation prompted by the design (an agent conversing with criminals), not a statement in the source."

- id: security-threat-intelligence-15
  title: Hardening AI-assisted analysis against attacker-influenced content
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "CTI and SOC assistants read content that attackers influence: log fields, phishing emails, incident notes, external reports and malware itself. Google's threat intelligence group observed a financially motivated actor embedding prompts in malware loader scripts, apparently to make LLM security scanners fail or skip analysis."
  solution: "Treat all ingested content as untrusted: input filtering, prompt hardening, output validation, constrained output formats, and evidence-grounded verification. Evaluate these against injection test sets before putting an LLM in the analysis path."
  outcomes:
    - lever: risk
      description: "In LLM log analysis, passive prompt injection reached up to 88.2% attack success (83.4% average) in the baseline. Layered defences (input filtering, prompt hardening, output validation) cut attacks by 90.4%, leaving 8.4% residual vulnerability."
      figure: "88.2% peak; 90.4% reduction; 8.4% residual"
      measures: "Attack success over LogInject-1.0, 12,847 log entries including 2,569 adversarial samples, across three production LLMs and four attack objectives; reduction and residual are for layered defences against the same set."
      provenance: self-reported
      source_ref: USENIX-LOGINJECT-2026
    - lever: risk
      description: "A separate study using gpt-4o-mini as analyst found persona-hijack attacks suppressed 68% of malicious logs under a naive classifier, summarisation was the highest-risk task (96% injection success for context manipulation without defences, 38% with constrained output), and the strongest defence cut average success from 26.6% to 11.8%."
      figure: "26.6% to 11.8% average success"
      measures: "Injection success across 48 strategy-defence-task combinations with one analyst model; the authors also show simulation mispredicts real model behaviour."
      provenance: self-reported
      source_ref: ARXIV-2605.24421
  prerequisites:
    - "Logging of model inputs and outputs so a manipulated narrative can be traced."
    - "An adversarial test set built from the team's own input types."
  risks_and_guardrails:
    - "A FIRST 2026 session by CyCraft shows that one crafted phishing email, chat transcript, incident note or external report can be formatted to bias retrieval and generation and alter the analyst-facing narrative; it offers low-cost defences."
    - "Defences reduce but do not eliminate the attack; both papers report residual risk."
    - "Google describes prompts embedded in malware loader scripts as likely intended to make LLM security scanners fail or skip analysis; the passage I read does not say whether any scanner was bypassed (GTIG-AITRACKER-2026)."
    - "NIST is developing SP 800-53 control overlays for securing AI systems, with a use case for using generative AI assistants and LLMs (NIST-COSAIS-2026)."
  human_checkpoints:
    - "Analyst verification of any AI-produced conclusion that would suppress or escalate an alert; USENIX authors call for defence in depth and continued human oversight for security-critical decisions."
  role_evolution: "CTI and SOC engineers take on adversarial testing of their own AI pipeline; no source measures staffing."
  evidence_grade: C
  sources:
    - { ref: USENIX-LOGINJECT-2026, title: "Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation", publisher: USENIX Security Symposium 2026 (Karanjai et al.), type: academic, url: "https://www.usenix.org/conference/usenixsecurity26/technical-sessions", date: 2026-08, access: full, locator: "abstract on the technical sessions listing" }
    - { ref: ARXIV-2605.24421, title: "Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content", publisher: arXiv (Pandey, Bhujang), type: academic, url: "https://arxiv.org/abs/2605.24421", date: 2026-05-23, access: full, locator: abstract }
    - { ref: FIRST-CON-2026, title: "38th FIRST Conference program: One Poisoned Artifact Can Steer Your AI", publisher: FIRST, type: conference, url: "https://www.first.org/conference/2026/program", date: 2026-06-18, access: full, locator: "session abstract, CyCraft AI Lab, 18 June 2026" }
    - { ref: GTIG-AITRACKER-2026, title: "GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI", publisher: Google Threat Intelligence Group, type: vendor, url: "https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/", date: 2026-09-08, access: full, locator: "section on UNC6780 / DUSTMAKER and Figure 1" }
    - { ref: NIST-COSAIS-2026, title: "Control Overlays for Securing AI Systems (COSAiS)", publisher: NIST, type: standard-setter, url: "https://csrc.nist.gov/projects/cosais", date: 2026-01-08, access: full, locator: "project page: use cases and news items" }
  last_reviewed: 2026-10-17
  notes: "Grade C: the attack rates are authors' measurements on benchmarks; Google's observation shows the technique in the wild but not any defender deployment. Maturity is emerging: GTIG documents attackers already doing this and FIRST sessions describe defences, but I found no named deployment of the hardening itself. Details of attacker payloads are intentionally not reproduced."

- id: security-threat-intelligence-16
  title: Evidence-grounded verification gates before AI-extracted intelligence enters a platform
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [review-assurance, data-reporting]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "LLM extraction is unreliable on full-length reports, and the model's own confidence does not verify truth. An audit of extraction found a single misattribution sentence flipped high-confidence relation judgements in 95.6-100% of cases."
  solution: "Insert deterministic checks and independent verification between extraction and storage: anchor each claim to a source span, check identifiers against authoritative definitions (for example ATT&CK IDs), rank candidates by self-consistency to set review priority, and route low-confidence items to an analyst."
  outcomes:
    - lever: quality
      description: "Self-consistency frequency tiering passed a preregistered top-30% precision-gain bar in all six test-split cells, but the authors conclude confidence may set review priorities, never truth."
      figure: "6 of 6 test-split cells passed the precision-gain bar"
      measures: "Number of the six test-split model-type cells in which top-30% self-consistency tiering met the preregistered precision-gain bar; the abstract does not define the cells further. The study used 630 model-report evaluations."
      provenance: independent
      source_ref: ARXIV-2610.20417
    - lever: quality
      description: "Verifiable-reward training on CTI tasks with task-specific verifiers raised the mean score by 15.8 percentage points over base models and 4.3 points over GRPO."
      figure: "+15.8 points over base"
      measures: "Mean score improvement averaged across four backbones and 12 CTI benchmarks, authors' own training pipeline (Minerva)."
      provenance: self-reported
      source_ref: ARXIV-2602.00513
  prerequisites:
    - "Authoritative identifier sets (ATT&CK, CVE, STIX schema) to verify against."
  risks_and_guardrails:
    - "Even an explicitly unrelated background sentence still bound a fake vulnerability in up to 26.7% of counterfactual cases (ARXIV-2610.20417)."
  human_checkpoints:
    - "Analyst reviews the tiers the system routes to review; confidence sets priority only."
  role_evolution: "No source describes role change."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2610.20417, title: "From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence", publisher: arXiv (Qian), type: academic, url: "https://arxiv.org/abs/2610.20417", date: 2026-10-14, access: full, locator: abstract }
    - { ref: ARXIV-2602.00513, title: "Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs", publisher: arXiv (Alam et al.), type: academic, url: "https://arxiv.org/abs/2602.00513", date: 2026-01-31, access: full, locator: "abstract (v3 revised 2026-05-07)" }
  last_reviewed: 2026-10-17
  notes: "Grade C: preprints. CTIBench (arXiv 2406.07599, 2024-06-11) is the foundation benchmark cited by this line of work: it states concerns about reliability, accuracy and hallucination as the motivation."

- id: security-threat-intelligence-17
  title: Planning adversary-emulation exercises from intelligence reports
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [review-assurance, software-systems]
  pattern: document-to-decision
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Testing defences against the behaviour in a threat report requires translating the report into an emulation plan. Regulated financial entities under DORA and TIBER-EU already require threat-intelligence-led testing based on bespoke intelligence about their own threats."
  solution: "An LLM framework generates an emulation plan (playbook) from a technique-aligned report, runs it in a test platform, and revises steps that fail. This is a defender-side purple-team capability; plan details are not reproduced here."
  outcomes:
    - lever: quality
      description: "Using the best-performing model among four, the framework achieved 84.22% execution success after revision and CTI precision, recall and F1 of 73.95%, 52.48% and 60.50%. The failure-recovery mechanism raised execution success by 14.59 to 17.23 percentage points across models."
      figure: "84.22% execution success; F1 60.50%"
      measures: "Execution success after revision of generated abilities (27.3 per playbook on average) on 11 CTI reports with Claude Sonnet 4.5; precision, recall and F1 of the emulated behaviour against the report's CTI. Authors' own framework, in a test environment."
      provenance: self-reported
      source_ref: ARXIV-2607.14566
  prerequisites:
    - "An isolated test environment and sign-off for any emulation; DORA's technical standard requires risk management for tests in live production, including controlled access and secrecy."
  risks_and_guardrails:
    - "DORA Delegated Regulation 2025/1190 requires the control team to manage risks of the test and sets qualification thresholds for threat-intelligence providers (a manager with at least 5 years of experience in threat intelligence, at least one other member with at least 2 years, and combined participation in at least three previous assignments). The English text I read contains no reference to artificial intelligence (EURLEX-DORATLPT-2025, Articles 5 and 7)."
    - "The DORA recital notes the threat-intelligence gathering process typically lasts about 4 weeks, based on TIBER-EU application (EURLEX-DORATLPT-2025, recital 18)."
  human_checkpoints:
    - "Test authority, control team and testers approve and supervise live tests; AI generation of plans does not change those roles."
  role_evolution: "No source describes role change; the regulation names experience-based qualifications that an AI-assisted provider would still have to meet."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2607.14566, title: "Fully Automated End-to-End Adversary Emulation from MITRE ATT&CK Based Cyber Threat Intelligence Using LLMs", publisher: arXiv (Choi et al.), type: academic, url: "https://arxiv.org/abs/2607.14566", date: 2026-07-16, access: full, locator: abstract }
    - { ref: EURLEX-DORATLPT-2025, title: "Commission Delegated Regulation (EU) 2025/1190 (threat-led penetration testing)", publisher: EUR-Lex, type: regulator, url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R1190", date: 2025-02-13, access: full, locator: "recitals 17-19; Article 7 (selection of TLPT providers)" }
    - { ref: ECB-TIBER-2026, title: "What is TIBER-EU? (undated page; date is retrieval date)", publisher: European Central Bank, type: regulator, url: "https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html", date: 2026-10-17, access: full, locator: "framework description and provider due diligence paragraph" }
  last_reviewed: 2026-10-17
  notes: "Grade C: one preprint prototype evaluated in a test environment. Included because TLPT/TIBER make regulated threat intelligence a distinct process; no source shows AI used by a threat-intelligence provider in a regulated test. The TIBER-EU and CBEST pages I opened do not mention AI."

- id: security-threat-intelligence-18
  title: LLM-assisted analysis of large investigative data volumes by an in-house threat intelligence team
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [research-synthesis, data-reporting]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Investigating a large campaign generates data volumes that exceed what analysts can read in the time available."
  solution: "Anthropic states its Threat Intelligence team used Claude extensively to analyse the enormous amounts of data generated during its investigation of a campaign it reported in November 2025, alongside banning accounts, notifying affected entities and coordinating with authorities."
  outcomes:
    - lever: capacity
      description: "No measurement of time saved, accuracy or error rate is published. Anthropic describes the use qualitatively."
      figure: "none published"
      measures: "Not applicable."
      provenance: vendor-published
      source_ref: ANTHROPIC-GTG1002-2025
  prerequisites:
    - "Not stated."
  risks_and_guardrails:
    - "The same report describes the attackers' use of an agentic model to run intrusion tasks, which is why the vendor advises defenders to experiment with AI in SOC automation, detection, vulnerability assessment and incident response."
  human_checkpoints:
    - "Not described in the post."
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: ANTHROPIC-GTG1002-2025, title: "Disrupting an AI-orchestrated cyber espionage campaign", publisher: Anthropic, type: vendor, url: "https://www.anthropic.com/news/disrupting-AI-espionage", date: 2025-11-13, access: full, locator: "section on why continue to develop and release models" }
  last_reviewed: 2026-10-17
  notes: "Grade B: a named organization's own statement of use without measurement. Conflict note: Anthropic makes the model whose use it describes, and the analyst who compiled this file is itself an Anthropic model, so treat as vendor evidence."

- id: security-threat-intelligence-19
  title: Locally hosted or open-weight models for processing restricted intelligence
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types: [software-systems, research-synthesis]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Intelligence arrives under handling labels such as TLP, and incident reports carry victim detail. In the practitioner survey, 13 of 18 named data privacy as a hurdle to AI and 6 of 18 named cost."
  solution: "Run an open-weight model inside the organization's boundary for extraction, mapping and redaction, so restricted material is not sent to a hosted service. Pilots show open-weight models close to proprietary ones on some tasks."
  outcomes:
    - lever: cost
      description: "At list prices, running the reserved test data for all four experiments cost about USD 84 for GPT-5.5, USD 207 for Claude Opus 4.8 and USD 75 for GLM 5.2, an open-weight model that matched the proprietary models at technique mapping and redaction under both prompts but had the weakest indicator precision (0.51) and asserted the most unsupported relationships."
      figure: "USD 75 vs USD 84 vs USD 207"
      measures: "Approximate list-price cost of running the study's reserved test data through each model; one study, one data set."
      provenance: self-reported
      source_ref: ARXIV-2609.01174
    - lever: cost
      description: "On CTI-REALM, an open-weight model can match the strongest closed models at less than a tenth of their cost, provided it is given enough turns."
      figure: "under 1/10 cost"
      measures: "Cost comparison on 26 models (19 open-weight, 7 closed) under a common harness with the benchmark's message limit relaxed."
      provenance: independent
      source_ref: ARXIV-2610.14180
  prerequisites:
    - "Compute and operations capacity to host and update a model."
    - "A decision on which TLP labels and data classes may leave the boundary. FIRST's standard defines an 'organization' by formal membership and common policies and leaves TLP use in automated exchange to the designers of the exchange, so whether a hosted model counts inside the label's boundary is a question to settle in policy, not a rule I found stated."
  risks_and_guardrails:
    - "The TLP standard requires recipients to obtain explicit permission from the source before sharing more widely than the label indicates (FIRST-TLP-2022)."
    - "ENISA's methodology requires AI-assisted outputs to meet the same information-handling requirements as other inputs (ENISA-CTL-2026, section 2.4.7)."
  human_checkpoints:
    - "Data-owner or legal sign-off on what may be processed."
  role_evolution: "No source describes role change; teams would need engineering support to host and evaluate models."
  evidence_grade: C
  sources:
    - { ref: ARXIV-2609.01174, title: "A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing", publisher: arXiv (Vasan et al.), type: academic, url: "https://arxiv.org/abs/2609.01174", date: 2026-09-01, access: full, locator: "section on open-weight model, cost and confidentiality" }
    - { ref: ARXIV-2610.14180, title: "Unconstrained CTI-REALM with Open-Weights", publisher: arXiv (Garg et al.), type: academic, url: "https://arxiv.org/abs/2610.14180", date: 2026-10-09, access: full, locator: abstract }
    - { ref: ARXIV-2610.09007, title: "Sigma-Hunter: A Domain-Specific Language Model for Threat Hunting and Detection Engineering", publisher: arXiv (Davaslioglu, Kompella), type: academic, url: "https://arxiv.org/abs/2610.09007", date: 2026-10-06, access: full, locator: "abstract: adapted models run locally for disconnected environments" }
    - { ref: FIRST-TLP-2022, title: "Traffic Light Protocol (TLP) version 2.0", publisher: FIRST, type: standard-setter, url: "https://www.first.org/tlp/", date: 2022-08, access: full, locator: "definitions of organization and community; usage rule on sharing beyond the label; automated exchange" }
    - { ref: ENISA-CTL-2026, title: "ENISA Cybersecurity Threat Landscape Methodology (updated 18 September 2026)", publisher: ENISA, type: regulator, url: "https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20CTL%20Methodology_Updated%2018%20september%202026.pdf", date: 2026-09-18, access: full, locator: "section 2.4.7" }
  last_reviewed: 2026-10-17
  notes: "Grade C: academic pilots; costs are list prices from one study. The TLP interpretation is flagged as unresolved, not as a finding."
```

## 3. Module notes

**Processes and key steps (with work types)**
- Direction and requirements: agree intelligence requirements with stakeholders (expert-judgment, coordination-scheduling). SANS finds 91% of CISOs value CTI but 26% say it significantly influences decisions; security executives' top asks are actively exploited vulnerabilities (79%) and adversary TTPs (77%) (SANS-CTI-2026).
- Collection: OSINT, feeds, partner and ISAC sharing, telemetry, dark-web and forum monitoring (research-synthesis). Use cases 2, 14.
- Processing and extraction: indicators, techniques, entities from reports and malware output (data-reporting). Use cases 3, 4, 13.
- Analysis and assessment: attribution, prioritisation, scoring, hunt hypotheses (expert-judgment). Use cases 8, 9, 10.
- Production and dissemination: reports, briefs, structured packages with handling labels (document-production). Use cases 1, 5, 6.
- Operationalisation: detection rules, blocklists, emulation plans (software-systems). Use cases 7, 17.
- Feedback and measurement: SANS reports 57% of programs do not track maturity over time and 49% do not gather systematic feedback (SANS-CTI-2026).

**Common pain points**
- Small teams: most formal CTI teams have fewer than four full-time staff; top barriers are lack of time (44%) and funding (44%) (SANS-CTI-2026).
- Alert noise and bandwidth: 65% and 55% of Flashpoint interviewees (more than 20 enterprises; vendor-commissioned) (FLASHPOINT-ETIR-2026).
- Manual conversion of evidence into shareable intelligence: 5 of 18 practitioners use ML and 3 use LLMs; sensitive-data exposure (17 of 18), noisy indicators (13), taxonomy mapping (10), format translation (7) (ARXIV-2609.01174).
- Source disagreement and bias in vendor reports (FIRST-CON-2026, Team Cymru; ARXIV-2602.17458).
- Legal uncertainty about sharing: 55% lack legally reviewed CTI sharing processes (SANS-CTI-2026).

**Metrics and benchmarks (with sources)**
- Prevalence: 45% of organizations use AI in CTI, 32% plan to (SANS-CTI-2026; 401 respondents).
- CTI-REALM: 16 frontier models, best reward 0.637; follow-up with 26 models (ARXIV-2603.13517, ARXIV-2610.14180).
- Cyber Defense Benchmark: best recall 3.8% of malicious events (ARXIV-2604.19533).
- ATT&CK mapping on complex reports: best micro-F1 0.22 (ARXIV-2606.18166).
- IOC extraction: SoK recall 0.25-0.31, precision 0.51-0.78; SCRIPTIOC-BENCH best 65.4 F1 (ARXIV-2609.01174, ARXIV-2609.06149).
- Threat-level scoring: F1 0.40-0.58 after fine-tuning (ARXIV-2609.07582).
- Prompt injection: up to 88.2% attack success; 90.4% reduction with layered defences (USENIX-LOGINJECT-2026).
- Foundation benchmark: CTIBench, arXiv 2406.07599 (June 2024; last revised 2024-11-11).
- Missing: no override-rate, parallel-run, time-saved or inspection data for AI in a live CTI team; no independent test of any vendor's AI CTI product.

**Guardrails and regulatory points**
- FIRST TLP v2.0 (authoritative from August 2022): four labels; sources can add restrictions; recipients need permission to share wider; TLP is not a classification scheme and its use in automated exchange is left to the designers (FIRST-TLP-2022).
- NIST SP 800-150 (October 2016): establish information sharing rules with legal and privacy input, including redaction (NIST-SP800150-2016, section 3.4). NIST CSF 2.0 ties intelligence to outcomes ID.RA-02 (receive CTI from information sharing forums) and DE.AE-07 (integrate CTI into analysis) (NIST-CSF-2024).
- NIS2 Articles 29-30: voluntary information-sharing arrangements within communities of essential and important entities; entities notify authorities of their participation; voluntary notification of threats and near misses; recital 51 on AI and data-protection principles (EURLEX-NIS2-2022).
- DORA Article 45: sharing among financial entities in trusted communities with GDPR and competition-law compliance (EURLEX-DORA-2022). DORA TLPT standard 2025/1190: provider experience thresholds, no AI reference (EURLEX-DORATLPT-2025). TIBER-EU and CBEST pages do not mention AI (ECB-TIBER-2026, BOE-CBEST-2026).
- EU AI Act: the high-risk examples on the Commission page do not name threat-intelligence analysis; I did not find an AI Act obligation specific to CTI (EC-AIACT-2026). The EU Action Plan on Cybersecurity and AI (2026-07-07) encourages organisations to use AI, including open-source models where appropriate, to detect and address vulnerabilities (EC-ACTIONPLAN-2026).
- US: CISA 2015 extended through 2026-09-30 per CISA's AIS page; status after that date not confirmed (CISA-AIS-2026). Joint CISA/ACSC guidance on agentic AI adoption was released 2026-05-01 (CISA-AGENTIC-2026; landing page only). NIST is developing COSAiS overlays including a use case for generative AI assistants (NIST-COSAIS-2026).
- Analytic standards: UK NCSC Assessment uses the PHIA probability yardstick for every judgement (NCSC-UK-AI2027-2025); ENISA uses a words-of-estimative-probability table with percentage bands (ENISA-ETL-2026, Appendix B). Neither addresses AI-generated text; ENISA keeps judgement human.
- ENISA discloses AI use in the report itself, a practice other producers could adopt (ENISA-ETL-2026, Disclaimer). ENISA's earlier Threat Landscape 2025 analysed 4,875 incidents over July 2024 to June 2025; the 2026 edition changed the reporting period to the calendar year and expanded tracked cybercrime, so counts are not comparable across editions (ENISA-ETL-2025, ENISA-ETL-2026 Methodology).
- Standards for exchange: STIX 2.1 and TAXII 2.1 are OASIS standards for automated exchange; a multi-vendor interoperability PlugFest was held 15-17 June 2022 (OASIS-CTI-TC). CISA's AIS service uses TAXII 2.1.
- A document analysis of 25 studies (2022-2025) concludes successful GenAI integration in cybersecurity requires human oversight, data quality and explainability, and finds central banks and financial institutions leading adaptation under regulatory pressure; it is a preprint review, not CTI-specific (ARXIV-2506.12060).

**Frontier signals (dated and sourced)**
- 2026-09-18: ENISA updates its methodology to state a boundary between AI assistance and analyst judgement, and aims to publish more machine-readable output in the mid-term (ENISA-CTL-2026).
- 2026-10 (v20): MITRE ATT&CK adds AI-focused and AI-enabled techniques (for example AI Result Poisoning and AI-Enabled Exfiltration) and a campaign on an AI-assisted breach of Mexican government infrastructure, so analysts must tag AI-related behaviour in reports (MITRE-ATTCK-2026).
- 2026-10-13: Flashpoint interviewees rank AI-related threats (deepfake detection, AI-accelerated vulnerability exploitation) as the leading priority for expanded coverage (FLASHPOINT-ETIR-2026).
- 2026-09-08: Google reports adversaries moving to agentic workflows (a mass credential-harvesting campaign planned and run in under six hours) and targeting AI assets and LLM security scanners (GTIG-AITRACKER-2026).
- 2026-09-30: Google says organisations must move from unprioritised mass patching to threat-intelligence-driven triage (GTIG-VULNTRENDS-2026); this makes intelligence prioritisation more central to vulnerability work.
- 2025-07-23: the US AI Action Plan recommends an AI Information Sharing and Analysis Center led by DHS (WH-AIACTIONPLAN-2025). 2026-02-03: it was still in development with no timeline, and a draft implementation memo was in interagency process (NEXTGOV-AIISAC-2026, CYBERSECDIVE-AIISAC-2026). IT-ISAC argued in August 2025 that existing ISACs can share AI threat information (ITISAC-AIISAC-2025).
- 2025-05-07: UK NCSC assesses AI will almost certainly make elements of intrusion operations more effective and expects a digital divide between systems keeping pace and those that do not (NCSC-UK-AI2027-2025).
- 2026-09: ENISA assesses AI will highly likely increasingly support malicious operations, and that it is likely 2026 will see more kill-chain phases directly enabled by AI (ENISA-ETL-2026, executive summary).

**Workforce and role effects**
- Job posting (2025-10-30) expects LLM-driven drafting and enrichment in a senior reports role (JOB-SERVICENOW-2025).
- ISC2 (2025-12-04): AI is the top skills need (41%); roles such as SOC analyst and incident responder are evolving; the study is general cybersecurity, not CTI-specific (ISC2-WORKFORCE-2025).
- Cyware: 72.4% of respondents likely to build their own agents; 77% want analyst control (CYWARE-RSAC-2026; vendor survey, respondent count not stated).
- No data on junior-analyst pipeline or headcount effects in CTI.

**Objections and concerns practitioners raise**
- Reliability and grounding: models recover a fraction of indicators and cannot ground every claim (ARXIV-2609.01174).
- Privacy: 13 of 18 practitioners name data privacy as a hurdle (ARXIV-2609.01174).
- Unclear value and cost: lack of demonstrable value and unpredictable AI costs are barriers (FLASHPOINT-ETIR-2026).
- Evidence gap: a FIRST 2026 speaker says measured evidence of where AI-driven SOCs succeed or fall short remains scarce (FIRST-CON-2026).
- Legal exposure: sharing without legal review (SANS-CTI-2026).

**Interview probes for an advisor**
1. Which intelligence (by TLP label and source agreement) may an analyst put into an AI tool today, who decided, and where is it written down?
2. Pick one AI-assisted product or extraction step: what was its precision and recall against analyst verdicts on your own reports, and who reviews the misses?
3. What happens when a phishing email, report or log line contains instructions aimed at your model; have you tested it?
4. How do you tell stakeholders which parts of a finished report involved AI, and who signs the analytic judgement?
5. Who reviewed your sharing processes legally (NIS2, DORA, CISA 2015 where relevant), and does the review cover AI-assisted redaction and packaging?

## 4. Routed to other modules

- **vulnerability-exposure**: GTIG disclosure and exploitation trends (disclosures 5,045 in January 2026 to 10,477 in July and 10,740 in August; exploited vulnerabilities from an average of 10.5 per month in 2025 to 18 per month January-August 2026; 141 distinct vulnerabilities disclosed and exploited in that period versus 127 for all of 2025) and its recommendation to adopt threat-intelligence-driven triage (GTIG-VULNTRENDS-2026). UK NCSC and CyberUK statements on frontier AI exposing weak fundamentals (TECHRADAR-NCSC-2026, 2026-04-22).
- **security-operations**: ALERT-BENCH on LLM alert triage (every approach missed at least 40.4% of attack-related alerts across 1,247 alerts; a multi-agent design reached F1 0.958 with a 3.1% false-negative rate; ARXIV-2610.10608, 2026-10-07). Also the log-injection papers apply equally to SOC copilots.
- **ai-security**: ATT&CK v20 AI techniques; GTIG and ENISA findings on adversaries using and targeting AI; NIST COSAiS overlays; CISA/ACSC agentic AI guidance; the AI-ISAC; KnowHow (NDSS 2026), which applies CTI knowledge to provenance analysis (NDSS-KNOWHOW-2026: detects all 16 APT campaigns in its datasets with up to 90% fewer node-level false positives; the authors' own evaluation). Also the Cyber AI Profile (NIST IR 8596), whose page I could not open.
- **security-governance-risk**: SEC cyber-disclosure rules (not opened; blocked), EU AI Act timeline and AI Omnibus, ISACA and ISC2 workforce data, NIS2 and DORA as general obligations, ISO/IEC 27001/27002 control on threat intelligence (not opened).
- **incident-response**: CISA/NIST incident readiness practices for AI training and evaluation (2026-10-16 per CISA page related-resources list; not read).

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ENISA-ETL-2026 | ENISA Threat Landscape 2026 | ENISA | regulator | https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf | 2026-09 | full |
| ENISA-CTL-2026 | ENISA Cybersecurity Threat Landscape Methodology (updated 18 September 2026) | ENISA | regulator | https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20CTL%20Methodology_Updated%2018%20september%202026.pdf | 2026-09-18 | full |
| ENISA-ETL-2025 | ENISA Threat Landscape 2025 (landing page; 4,875 incidents, Jul 2024-Jun 2025; date per landscape file, page shows a later revision notice) | ENISA | regulator | https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025 | 2025-10-01 | full |
| NCSC-UK-AI2027-2025 | Impact of AI on cyber threat from now to 2027 | UK NCSC | regulator | https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027 | 2025-05-07 | full |
| TECHRADAR-NCSC-2026 | Mythos and friends could be a 'net positive' for UK cyber security defenses (NCSC head at CyberUK) | TechRadar | press | https://www.techradar.com/pro/security/mythos-and-friends-could-be-a-net-positive-for-uk-cyber-security-defenses-but-only-if-theyre-secured-says-top-cyber-official | 2026-04-22 | full |
| EC-ACTIONPLAN-2026 | EU Action Plan on Cybersecurity and Artificial Intelligence | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence | 2026-07-07 | full |
| EC-AIACT-2026 | AI Act (policy page; undated, retrieval date) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-17 | full |
| EURLEX-NIS2-2022 | Directive (EU) 2022/2555 (NIS 2) | EUR-Lex | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555 | 2022-12-14 | full |
| EURLEX-DORA-2022 | Regulation (EU) 2022/2554 (DORA) | EUR-Lex | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554 | 2022-12-14 | full |
| EURLEX-DORATLPT-2025 | Commission Delegated Regulation (EU) 2025/1190 (TLPT) | EUR-Lex | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R1190 | 2025-02-13 | full |
| ECB-TIBER-2026 | What is TIBER-EU? (undated, retrieval date) | European Central Bank | regulator | https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html | 2026-10-17 | full |
| BOE-CBEST-2026 | CBEST Threat Intelligence-Led Assessments (undated, retrieval date) | Bank of England | regulator | https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide | 2026-10-17 | full |
| CISA-AIS-2026 | Automated Indicator Sharing (AIS) (undated, retrieval date; read via text mirror) | CISA | regulator | https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/automated-indicator-sharing-ais | 2026-10-17 | full |
| CISA-AGENTIC-2026 | Careful Adoption of Agentic AI Services (landing page only; guidance text not read) | CISA with ASD's ACSC | regulator | https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services | 2026-05-01 | full (landing page) |
| WH-AIACTIONPLAN-2025 | America's AI Action Plan (AI-ISAC recommendation) | The White House | regulator | https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf | 2025-07-23 | full |
| NEXTGOV-AIISAC-2026 | AI info-sharing center is in development, CISA official says | Nextgov/FCW | press | https://www.nextgov.com/cybersecurity/2026/02/ai-info-sharing-center-development-cisa-official-says/411167 | 2026-02-03 | full |
| CYBERSECDIVE-AIISAC-2026 | AI-ISAC inches forward under Trump administration | Cybersecurity Dive | press | https://www.cybersecuritydive.com/news/ai-isac-us-government-update-cisa/811281/ | 2026-02-03 | full |
| ITISAC-AIISAC-2025 | Leverage Existing ISACs to Share AI Threat Information | IT-ISAC | community | https://www.it-isac.org/post/leverage-existing-isacs-to-share-ai-threat-information | 2025-08-12 | full |
| NIST-CSF-2024 | The NIST Cybersecurity Framework (CSF) 2.0 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | 2024-02-26 | full |
| NIST-SP800150-2016 | Guide to Cyber Threat Information Sharing (SP 800-150) | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-150.pdf | 2016-10 | full |
| NIST-COSAIS-2026 | Control Overlays for Securing AI Systems (COSAiS) | NIST | standard-setter | https://csrc.nist.gov/projects/cosais | 2026-01-08 | full |
| FIRST-TLP-2022 | Traffic Light Protocol (TLP) version 2.0 | FIRST | standard-setter | https://www.first.org/tlp/ | 2022-08 | full |
| MITRE-ATTCK-2026 | ATT&CK v20 release notes (Updates page) | MITRE | standard-setter | https://attack.mitre.org/resources/updates/ | 2026-10 | full |
| MITRE-CTID-TRAM-2023 | Threat Report ATT&CK Mapper (TRAM) | MITRE Center for Threat-Informed Defense | standard-setter | https://ctid.mitre.org/projects/threat-report-attck-mapper-tram/ | 2023-08-24 | full |
| OASIS-CTI-TC | OASIS CTI Technical Committee page (STIX/TAXII 2.1 standards; interoperability PlugFest 15-17 June 2022 item) | OASIS | standard-setter | https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti | 2022-06 | full |
| FIRST-CON-2026 | 38th FIRST Conference program (Denver, 14-19 June 2026) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06 | full |
| USENIX-SIGMERGE-2026 | From Texts to Rules: Generating Sigma Rules with LLMs from Cyber Threat Reports | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/cai | 2026-08 | full |
| USENIX-LOGINJECT-2026 | Context Contamination in LLM Analysis of Network Security Logs | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/technical-sessions | 2026-08 | full |
| NDSS-TIECO-2026 | Actively Understanding the Dynamics and Risks of the Threat Intelligence Ecosystem | NDSS 2026 | academic | https://www.ndss-symposium.org/ndss-paper/actively-understanding-the-dynamics-and-risks-of-the-threat-intelligence-ecosystem/ | 2026-02 | full |
| NDSS-KNOWHOW-2026 | KnowHow: Automatically Applying High-Level CTI Knowledge for Interpretable and Accurate Provenance Analysis | NDSS 2026 | academic | https://www.ndss-symposium.org/ndss-paper/knowhow-automatically-applying-high-level-cti-knowledge-for-interpretable-and-accurate-provenance-analysis/ | 2026-02 | full |
| ARXIV-2609.01174 | A SoK for SoCs: Reading the TI Leaves on AI for CTI Generation and Sharing | arXiv (UC Santa Barbara et al.) | academic | https://arxiv.org/abs/2609.01174 | 2026-09-01 | full (PDF read) |
| ARXIV-2610.20417 | From Unreliable to Usable: Failure Modes and Confidence Signals in LLM Entity Extraction (CTI) | arXiv | academic | https://arxiv.org/abs/2610.20417 | 2026-10-14 | full |
| ARXIV-2603.13517 | CTI-REALM benchmark | arXiv | academic | https://arxiv.org/abs/2603.13517 | 2026-03-13 | full |
| ARXIV-2610.14180 | Unconstrained CTI-REALM with Open-Weights | arXiv | academic | https://arxiv.org/abs/2610.14180 | 2026-10-09 | full |
| ARXIV-2606.18166 | Evaluating Open-Source LLMs for Multi-Label ATT&CK Technique Classification | arXiv | academic | https://arxiv.org/abs/2606.18166 | 2026-06-16 | full |
| ARXIV-2605.25836 | CTI2TTP | arXiv | academic | https://arxiv.org/abs/2605.25836 | 2026-05-25 | full |
| ARXIV-2608.28124 | TagZilla | arXiv | academic | https://arxiv.org/abs/2608.28124 | 2026-08-28 | full |
| ARXIV-2609.06149 | SCRIPTIOC-BENCH | arXiv | academic | https://arxiv.org/abs/2609.06149 | 2026-09-05 | full |
| ARXIV-2605.06910 | Benchmarking LLMs for IoC Recovery under Adversarial Code Obfuscation and Encryption | arXiv | academic | https://arxiv.org/abs/2605.06910 | 2026-05-07 | full |
| ARXIV-2604.12228 | From IOCs to Regex (IOCRegex-gen) | arXiv | academic | https://arxiv.org/abs/2604.12228 | 2026-04-14 | full |
| ARXIV-2610.09007 | Sigma-Hunter | arXiv | academic | https://arxiv.org/abs/2610.09007 | 2026-10-06 | full |
| ARXIV-2609.08790 | Evidence-Grounded Retrieval for Investigation Hunt Lead Generation (AHLERT) | arXiv | academic | https://arxiv.org/abs/2609.08790 | 2026-09-08 | full |
| ARXIV-2604.19533 | Cyber Defense Benchmark: Agentic Threat Hunting Evaluation | arXiv | academic | https://arxiv.org/abs/2604.19533 | 2026-04-21 | full |
| ARXIV-2509.23571 | Benchmarking LLM-Assisted Blue Teaming via Standardized Threat Hunting (ICML 2026) | arXiv | academic | https://arxiv.org/abs/2509.23571 | 2025-09-28 | full |
| ARXIV-2509.23573 | Uncovering Vulnerabilities of LLM-Assisted Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2509.23573 | 2025-09-28 | full |
| ARXIV-2609.07582 | Benchmarking LLMs for Threat Level Determination | arXiv | academic | https://arxiv.org/abs/2609.07582 | 2026-09-07 | full |
| ARXIV-2610.07298 | Polar | arXiv | academic | https://arxiv.org/abs/2610.07298 | 2026-10-05 | full |
| ARXIV-2602.17458 | The CTI Echo Chamber | arXiv | academic | https://arxiv.org/abs/2602.17458 | 2026-02-19 | full |
| ARXIV-2606.01208 | ANCHOR schema-agnostic CTI knowledge graph construction | arXiv | academic | https://arxiv.org/abs/2606.01208 | 2026-05-31 | full |
| ARXIV-2608.28394 | BEACON | arXiv | academic | https://arxiv.org/abs/2608.28394 | 2026-08-28 | full |
| ARXIV-2607.05001 | TACTIC-KG | arXiv | academic | https://arxiv.org/abs/2607.05001 | 2026-07-06 | full |
| ARXIV-2608.23185 | Towards Automated CTI Elicitation in Underground Forums (DarkBot) | arXiv | academic | https://arxiv.org/abs/2608.23185 | 2026-08-24 | full |
| ARXIV-2608.14418 | STINER (RAID 2026) | arXiv | academic | https://arxiv.org/abs/2608.14418 | 2026-08-14 | full |
| ARXIV-2605.24421 | Poisoning the Watchtower | arXiv | academic | https://arxiv.org/abs/2605.24421 | 2026-05-23 | full |
| ARXIV-2602.00513 | Minerva | arXiv | academic | https://arxiv.org/abs/2602.00513 | 2026-01-31 | full |
| ARXIV-2607.14566 | Fully Automated End-to-End Adversary Emulation from ATT&CK-Based CTI Using LLMs | arXiv | academic | https://arxiv.org/abs/2607.14566 | 2026-07-16 | full |
| ARXIV-2610.10608 | From Investigation Failures to Reliable SOC Agents (ALERT-BENCH; routed) | arXiv | academic | https://arxiv.org/abs/2610.10608 | 2026-10-07 | full |
| ARXIV-2506.12060 | Organizational Adaptation to Generative AI in Cybersecurity (document analysis of 25 studies) | arXiv | academic | https://arxiv.org/abs/2506.12060 | 2025-05-31 | full |
| ARXIV-2406.07599 | CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2406.07599 | 2024-06-11 | full |
| SANS-CTI-2026 | 2026 CTI Survey Insights press release and Key Findings page | SANS Institute | survey | https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report ; https://www.sans.org/research/cyber-threat-intelligence-report | 2026-05-19 | full (summary pages; full report not read) |
| CYWARE-RSAC-2026 | What Security Professionals at RSAC2026 Told Us About AI and Threat Intelligence | Cyware | survey | https://www.cyware.com/blog/what-security-professionals-at-rsac2026-told-us-about-ai-and-threat | 2026-04-28 | full |
| FLASHPOINT-ETIR-2026 | Flashpoint Enterprise Threat Intelligence Report: 2026 (press release) | Flashpoint | survey | https://www.prweb.com/releases/nearly-half-of-enterprise-threat-intelligence-teams-are-using-or-piloting-agentic-ai-as-ai-threats-lead-2027-priorities-flashpoint-research-finds-302906892.html | 2026-10-13 | full (press release; report not read) |
| SOCRADAR-SANSCTI-2026 | 2026 SANS CTI Survey Report: Key Findings on CTI's Influence Gap | SOCRadar | vendor | https://socradar.io/blog/2026-sans-cti-survey-report-findings/ | 2026-07-01 | full |
| ISC2-WORKFORCE-2025 | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full |
| GTIG-AITRACKER-2026 | GTIG AI Threat Tracker: From Prompting to Autonomy | Google Threat Intelligence Group | vendor | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/ | 2026-09-08 | full |
| GTIG-VULNTRENDS-2026 | Vulnerability Discovery and Exploitation Trends in the AI Era | Google Threat Intelligence Group | vendor | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | full |
| ANTHROPIC-GTG1002-2025 | Disrupting an AI-orchestrated cyber espionage campaign | Anthropic | vendor | https://www.anthropic.com/news/disrupting-AI-espionage | 2025-11-13 | full |
| JOB-SERVICENOW-2025 | Staff Cyber Threat Intelligence Analyst, Reports Officer | ServiceNow (via Built In) | job-posting | https://builtin.com/job/staff-cyber-threat-intelligence-analyst-reports-officer/7520264 | 2025-10-30 | full |

Counts by type (distinct refs, including routed and module-note items): academic 33, regulator 14, standard-setter 7, vendor 4, press 3, survey 3, community 1, conference 1, professional-body 1, job-posting 1. Total 68 sources; 49 are cited in use-case entries and the rest in module notes or routing. All were opened, in the form noted in the Access column (the CISA agentic guidance as a landing page only; SANS and Flashpoint as summary pages or press release).

## 6. Gaps

- **No independent operational evidence.** I found no override rates, parallel-run results, time-saved measurements, analyst-hour savings or inspection findings for AI in a live CTI team, and no independent test of any commercial AI CTI product. Every figure above is a survey prevalence, a benchmark or an author's own prototype evaluation.
- **Full survey reports not read.** The SANS 2026 CTI report is behind a form; I used SANS's press release, key-findings page and a sponsor summary (the 56%/46%/45% use-case split has no stated denominator). Flashpoint's report body was not read. Cyware does not state its respondent count.
- **CISA 2015 after 2026-09-30.** CISA's AIS page records extension through 2026-09-30; a web search did not show what happened afterwards. Treat as unconfirmed.
- **AI-ISAC.** Latest reporting found is from February 2026; I did not find a launch.
- **ISAC practice.** I found no public evidence of FS-ISAC, Health-ISAC or other ISACs using AI on member submissions, and the one ISAC source (IT-ISAC, August 2025) is an advocacy piece.
- **Blocked or unread.** CISA/ACSC agentic AI guidance text (cyber.gov.au failed); Ireland NCSC statement (403); Computer Weekly NCSC article (403); SEC rules (403); ISO/IEC 27001/27002 and 42001 pages (403); NIST Cyber AI Profile (IR 8596) page (404); Mandiant M-Trends and Verizon DBIR (gated); GitHub (TRAM repository; blocked in this session); Gartner and Forrester CTI research (paywalled).
- **Peer-reviewed share is small.** Of the academic items, only SIGMERGE and LogInject (USENIX Security 2026), the NDSS 2026 papers, CyberTeam (ICML 2026), STINER (RAID 2026, accepted) and AHLERT (IEEE DSC 2026 workshop) are marked as accepted at a venue in the sources I read; the rest are preprints. I did not find CTI-specific AI papers in the IEEE S&P 2026 program or ACM CCS 2026 overview (programs searched by keyword only).
- **Abstract-level reading.** For preprints other than the SoK, I read abstracts, not full text; figures come from abstracts and may omit caveats.
- **Regional and sector regulators.** No APAC, Middle East or banking-supervisor guidance on AI in CTI was reviewed beyond the EU and UK financial testing frameworks; the TIBER-EU, CBEST and DORA texts say nothing on AI.
- **Date caveats.** Several regulator pages (ECB TIBER-EU, Bank of England CBEST, CISA AIS, EC AI Act) are undated; their date field is the retrieval date. ENISA's ETL 2026 gives only "September 2026"; its PDF metadata shows creation on 2026-09-22.
- **Terminology anomaly.** CISA's pages retrieved on 2026-10-17 show "SI" where the URL and related titles say "AI" (for example 'Careful Adoption of Agentic SI Services'). I cite the guidance by its URL title and record the anomaly as observed.
- **Module boundary.** No source I found links AI to the decision-influence gap (91% value vs 26% influence) or to CTI measurement and feedback loops, so those areas have no AI use case.
