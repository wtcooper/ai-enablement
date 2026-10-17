# Security / threat-intelligence / discourse: how practitioners talk about AI in cyber threat intelligence and threat hunting

Archetype: security. Module: threat-intelligence (collection, analysis, reporting and sharing; threat hunting; AI for summarising, enriching and prioritising intelligence). Angle: discourse. Researched 2026-10-17. Window: roughly 2025-09 to 2026-10, with two 2025-03/09 papers kept as foundations.

## 1. Summary

- **The field's working consensus is "AI for the grunt work, people for judgment", and the evidence behind it is thin.** SANS's 2026 CTI survey (401 practitioners plus 67 security executives, fielded Nov 2025 to Jan 2026) reports 45% of organizations using AI in CTI, mainly for summarization, report writing and workflow automation, with another 32% planning to adopt (`SANS-CTI-2026`). Flashpoint's vendor-commissioned interviews (more than 20 budget owners and influencers) put agentic AI at 25% in production, 20% piloting and 35% planning within 12 to 24 months, with a tone of "high bar, not hype" (`FLASHPOINT-ENTERPRISE-2026`). Both are aggregate, unnamed-organization numbers.
- **Quality evidence is almost entirely lab benchmarks, and the results are uneven.** In one controlled study, three LLMs recovered 363 to 461 of 1,472 labeled indicators (precision 0.51 to 0.78) but mapped ATT&CK techniques at F1 about 0.7; another study of open models on complex report prose reached only F1 0.22; fine-tuned threat-level scoring reached F1 0.40 to 0.58; the best agent on Microsoft's CTI-REALM detection benchmark scored 0.637 (`ARXIV-2609.01174`, `ARXIV-2606.18166`, `ARXIV-2609.07582`, `ARXIV-2603.13517`). No override rates, parallel-run results, inspection findings or independent production measurements were found. The only measured outcome from a named organization is a self-reported threat-hunting agent at Grow Therapy (`GROWTHERAPY-HUNT-2026`).
- **A dated tension runs through the year.** In January 2026, six of 14 practitioners surveyed by Feedly called AI-threat narratives overhyped and one said there was zero evidence of fully autonomous AI attacks at scale (`FEEDLY-ROUNDUP-2026`); in February Intel 471 wrote that threat actors attaining fully autonomous operations "has yet to occur" and described a paper claiming 80% of ransomware attacks use AI that its authors removed after errors were reported (`INTEL471-AIHUMAN-2026`). By September, Google's threat intelligence group reported adversaries moving from prompting to agentic workflows, including a cloud credential-harvesting campaign planned and run in under six hours (`GTIG-AITRACKER-2026`). The defender-side discourse has not resolved which of these should set collection priorities; Flashpoint's interviewees rank AI-related threats first for expanded coverage (`FLASHPOINT-ENTERPRISE-2026`).
- **Where the field says it is heading:** chained report-to-ticket workflows with analyst approval gates; portable "skills" and MCP connections to TIPs and ticketing; cheaper open-weight models; coverage of AI-enabled adversary behavior (ATT&CK v20 adds AI-focused and AI-enabled techniques); and a hiring profile built around validation and context engineering (`FEEDLY-AUTOMATE-2026`, `DETENGWEEKLY-167-2026`, `ARXIV-2610.14180`, `MITRE-ATTCK-2026`, `FEEDLY-HIRING-2026`).
- **What it worries about:** an agent that is "confidently wrong", analyst de-skilling and a shrinking entry-level pipeline, sycophantic models validating weak hypotheses, attacker-controlled content steering AI-assisted workflows, black-box vendor triage, and the legal side of sharing (55% of organizations lack legally reviewed CTI sharing processes while NIS2 and the Cyber Resilience Act add obligations) (`FLASHPOINT-ENTERPRISE-2026`, `FEEDLY-VALUE-2026`, `INTEL471-HUNTING-2025`, `FIRST-CON-2026`, `FORRESTER-PREDICT-2025`, `SANS-CTIPR-2026`).
- **Count:** 19 candidate use cases: 1 grade A, 3 grade B, 10 grade C, 5 grade D (ideas). 55 distinct sources read; see section 5.

Notes on the landscape file: the CTI leads that were followed are the FIRST OSINT-copilot session (it is Apura Cyber Intelligence), the GTIG AI Threat Tracker and vulnerability trends posts, ATT&CK v20 (released 2026-10-13) and ENISA's threat landscape. Not followed: CISA's advisory on model distillation, Unit 42's espionage report, the CrowdStrike Global Threat Report and MITRE ATLAS. Several 2026 model names that appear in the studies cited (for example Claude Opus 4.6 and 4.8, GPT-5.5, GLM 5.2) are as published by the authors.

## 2. Use cases

Grade scope: a grade reflects evidence for this module's use. Grade A means a measured outcome from a named organization; none of the lab benchmarks below qualify, so they are reported as `independent` outcomes under grade C or D with the limit stated in `notes`. Grade D entries are ideas discussed by researchers or practitioners.

```yaml
- id: security-threat-intelligence-01
  title: Extract indicators and entities from unstructured threat reports into structured records
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Analysts read each vendor or OSINT report and pull out the indicators by hand, then enrich them and tie each one to the malware, technique,
    campaign or actor it appeared with. In a practitioner survey of 18 people at 5 organizations, converting attack data into shareable intelligence
    was described as largely manual, and 13 of 18 named isolating malicious indicators from noisy attack data as a recurring challenge (ARXIV-2609.01174,
    section 3.2).
  solution: An LLM prompt or reusable skill reads the report and returns indicators together with the sentence and source they came from, in STIX
    2.1, for an analyst to review before import into a threat intelligence platform. SANS reports that 45% of surveyed organizations use AI in
    CTI, mainly for summarization, report writing and workflow automation; the pilot organizations in Flashpoint's interviews describe context
    generation and TIP querying (SANS-CTIPR-2026; FLASHPOINT-ENTERPRISE-2026, section 'Agentic AI Adoption Is Underway'). No named organization
    with a production measurement was found for this step.
  outcomes:
  - lever: speed
    description: Feedly estimates time saved per report for its extract-and-enrich workflow (an estimate built from its own manual-step ranges,
      not a measurement).
    figure: 25 to 50 minutes per report (potential)
    measures: 'Feedly: ''Potential time saved'' for Workflow 1, against manual steps of 10-20, 15-30 and 10-20 minutes; no measured baseline or
      sample stated'
    provenance: vendor-published
    source_ref: FEEDLY-AUTOMATE-2026
  - lever: quality
    description: 'Controlled study on held-out sandbox reports: three LLMs returned far fewer false indicators than rule baselines but recovered
      only a minority of the labeled indicators.'
    figure: 363 to 461 of 1,472 labeled indicators recovered; precision 0.51 to 0.78 (rule baselines 0.09 and 0.41)
    measures: true positives out of 1,472 labeled indicators in 45 held-out sandbox reports; precision = true positives out of all values the
      approach reported
    provenance: independent
    source_ref: ARXIV-2609.01174
  - lever: quality
    description: 'Benchmark of static IOC recovery from malicious scripts: the strongest model scored 65.4 F1; the authors state recovery without
      execution remains challenging across model scales.'
    figure: 65.4 F1 (strongest model)
    measures: F1 for URLs, domains, IP addresses and filesystem artifacts recovered without execution from 634 manually verified JavaScript, PowerShell
      and VBScript malware samples
    provenance: independent
    source_ref: ARXIV-2609.06149
  prerequisites:
  - A defined output schema (STIX 2.1 in the Feedly workflow) and a threat intelligence platform to receive it (FEEDLY-AUTOMATE-2026, Workflow
    1).
  - Keep each indicator tied to its source sentence and the related malware, technique, campaign or actor, because an indicator alone ages quickly
    (FEEDLY-AUTOMATE-2026, Workflow 1).
  - 'Evidence-grounded extraction: BEACON''s authors describe a propose-then-verify design that grounds candidates in report evidence to suppress
    misclassification and hallucination (ARXIV-2608.28394, abstract).'
  risks_and_guardrails:
  - Precision matters more than recall for shared indicators because shared IOCs are consumed as blocklists, so one benign value reported as an
    indicator raises false detections in every organization that blocks it (ARXIV-2609.01174, section on Experiments 1 and 2).
  - Encryption-based concealment severely degrades LLM recovery of indicators from obfuscated code, while renaming and Base64 are handled well
    (ARXIV-2605.06910, abstract).
  - A document can be formatted to bias what a RAG-based security workflow retrieves and outputs; the CyCraft session at FIRST demonstrates this
    and offers low-cost defenses (FIRST-CON-2026, 'One Poisoned Artifact Can Steer Your AI', 2026-06-18).
  human_checkpoints:
  - Analyst approval step between any stage that reads and any stage that writes to live tooling (FEEDLY-AUTOMATE-2026, 'Chaining the workflows
    together').
  - Feedly rates this step easy to build and suggests chaining the low-risk read-only stages first (FEEDLY-AUTOMATE-2026, 'Build versus buy').
  role_evolution: Feedly says AI is absorbing much of the routine work of aggregating feeds and enriching indicators and that the premium shifts
    to interpreting what the data means for the organization (FEEDLY-HIRING-2026, sections 'What AI Changes for CTI Teams' and 'Analytical Thinking
    Over Technical Execution').
  evidence_grade: C
  sources:
  - ref: SANS-CTI-2026
    title: SANS 2026 Cyber Threat Intelligence Survey Insights (report landing page with takeaways and FAQ; full report not opened)
    publisher: SANS Institute
    type: survey
    url: https://www.sans.org/research/cyber-threat-intelligence-report
    date: 2026-05
    access: full
    locator: FAQ 'How many organizations are using AI in cyber threat intelligence?'
  - ref: SANS-CTIPR-2026
    title: 91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (press release)
    publisher: SANS Institute
    type: professional-body
    url: https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report
    date: '2026-05-19'
    access: full
    locator: paragraph beginning 'The structural picture'
  - ref: FLASHPOINT-ENTERPRISE-2026
    title: 'The Enterprise Threat Intelligence Report: 2026 (vendor-commissioned qualitative research, more than 20 interviewees)'
    publisher: Flashpoint
    type: survey
    url: https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/
    date: '2026-10-13'
    access: full
    locator: section 'Agentic AI Adoption Is Underway'
  - ref: ARXIV-2609.01174
    title: 'A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.01174
    date: '2026-09-01'
    access: full
    locator: abstract; section 3.2 (practitioner survey); Table 2a
  - ref: ARXIV-2609.06149
    title: 'SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.06149
    date: '2026-09-05'
    access: full
    locator: abstract
  - ref: ARXIV-2605.06910
    title: Benchmarking Large Language Models for IoC Recovery under Adversarial Code Obfuscation and Encryption
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2605.06910
    date: '2026-05-07'
    access: full
    locator: abstract
  - ref: ARXIV-2608.28394
    title: 'BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.28394
    date: '2026-08-28'
    access: full
    locator: abstract
  - ref: FEEDLY-AUTOMATE-2026
    title: How to automate common CTI workflows (J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/how-to-automate-common-cti-workflows
    date: '2026-06-12'
    access: full
    locator: 'Workflow 1: Extracting and enriching the IOCs'
  - ref: FEEDLY-HIRING-2026
    title: 'Hiring for the AI era: A CTI leader''s guide to building tomorrow''s threat intelligence teams (J. Feyerabend)'
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/hiring-for-the-ai-era-a-cti-leader-s-guide-to-building-tomorrow-s-threat-intelligence-teams
    date: '2026-07-16'
    access: full
    locator: section 'What AI Changes for CTI Teams'
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program (session abstracts)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: session abstract, 'One Poisoned Artifact Can Steer Your AI', 2026-06-18 14:20
  last_reviewed: '2026-10-17'
  notes: 'Grade C: the measurements are lab benchmarks from preprints, not production results, and the only adoption figure is an unnamed-organization
    survey share. The SoK uses its own labeled sandbox reports; model names in these 2026 studies are as published by the authors.'
- id: security-threat-intelligence-02
  title: Map reported adversary behavior to ATT&CK techniques and enrich hunts with actor context
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Mapping the behavior in a report to ATT&CK tactics, techniques and sub-techniques, and finding which actors use similar techniques,
    is slow, language-heavy analyst work. In the SoK practitioner survey 10 of 18 participants reported mapping observed behavior to standard
    taxonomies as a recurring challenge (ARXIV-2609.01174, section 3.2).
  solution: 'Intel 471''s threat hunt analysts say they use AI to enrich hunts with CTI context: tagging hunt packages with threat actors seen
    using the same techniques, mapping techniques to MITRE ATT&CK, and adding industry, geography, severity and motivation so teams can prioritize
    hunts (INTEL471-HUNTING-2025, section ''Enrichment''). Feedly publishes a prompt for mapping a report to ATT&CK and visualizing it in Navigator
    (FEEDLY-AUTOMATE-2026, Workflow 2). Flashpoint''s pilot interviewees list ATT&CK mapping among the workflows they are testing (FLASHPOINT-ENTERPRISE-2026,
    section ''Agentic AI Adoption Is Underway'').'
  outcomes:
  - lever: quality
    description: In a controlled study on sandbox reports, three LLMs mapped behavior to techniques far better than a Sigma-rule baseline.
    figure: technique F1 0.71 to 0.72; sub-technique F1 0.66 to 0.67; Sigma-rule baseline technique F1 0.16
    measures: F1 against 254 labeled main techniques and 263 labeled sub-techniques across 45 held-out sandbox reports
    provenance: independent
    source_ref: ARXIV-2609.01174
  - lever: quality
    description: On complex, unstructured CTI reports the best of seven open-source models (8B to 236B parameters) reached a much lower score,
      which the authors call a baseline and conclude is insufficient for proactive defense use.
    figure: micro-averaged F1 0.22 (best model)
    measures: micro F1 for multi-label ATT&CK technique classification on 2,076 human-annotated sentences (1,281 technique-positive) from 83 CTI
      reports, 114 distinct techniques, inter-annotator kappa 0.68
    provenance: independent
    source_ref: ARXIV-2606.18166
  - lever: speed
    description: Feedly estimates time saved per report for mapping and visualizing (an estimate, not a measurement).
    figure: 20 to 45 minutes (potential)
    measures: 'Feedly: ''Potential time saved'' for Workflow 2, against manual steps of 10-20, 20-35 and 10-20 minutes; no sample stated'
    provenance: vendor-published
    source_ref: FEEDLY-AUTOMATE-2026
  prerequisites:
  - Mapping must be checkable against the source text; Feedly advises looking for ATT&CK mappings you can validate against the source if you buy
    (FEEDLY-AUTOMATE-2026, 'Build versus buy').
  - 'Domain-specific scaffolding helps: CTI-REALM found CTI-specific tools significantly improved agent performance (ARXIV-2603.13517, abstract).'
  risks_and_guardrails:
  - 'Score depends heavily on how the task is posed: F1 around 0.7 on sandbox reports versus 0.22 on complex prose in a separate study, so a vendor
    demo on clean input says little about real reports (ARXIV-2609.01174, Table 2b; ARXIV-2606.18166, abstract).'
  - Older studies argue the dominant bottleneck is the threat landscape itself (heterogeneous, volatile, fragmented evidence) rather than generic
    hallucination, and identify spurious correlation from superficial metadata and contradictory sources as failure modes (ARXIV-2509.23573, abstract).
  - Intel 471 warns that models designed to be agreeable can validate a flawed hypothesis, so ask questions constrained by facts (INTEL471-HUNTING-2025,
    section 'Hypothesis Development').
  human_checkpoints:
  - Feedly lists attribution, risk ratings and business-impact statements as outputs a model tends to assert with unwarranted confidence and that
    need analyst review (FEEDLY-AUTOMATE-2026, 'Where the human analyst is still required').
  role_evolution: Intel 471 says it looks for ways AI can streamline enrichment 'to help make human analysts informed decision-makers rather than
    merely performing routine tasks' (INTEL471-HUNTING-2025, section 'Enrichment').
  evidence_grade: B
  sources:
  - ref: INTEL471-HUNTING-2025
    title: How AI can (and can't) help in threat hunting
    publisher: Intel 471
    type: vendor
    url: https://www.intel471.com/blog/how-ai-can-and-cant-help-in-threat-hunting
    date: '2025-09-09'
    access: full
    locator: sections 'Enrichment' and 'Hypothesis Development'
  - ref: FLASHPOINT-ENTERPRISE-2026
    title: 'The Enterprise Threat Intelligence Report: 2026 (vendor-commissioned qualitative research, more than 20 interviewees)'
    publisher: Flashpoint
    type: survey
    url: https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/
    date: '2026-10-13'
    access: full
    locator: section 'Agentic AI Adoption Is Underway'
  - ref: SANS-AGENTICWEB-2026
    title: Agentic CTI Automation For Fun and Profit (webcast by R. Brown and J. Cran; abstract only, webcast not viewed)
    publisher: SANS Institute
    type: conference
    url: https://www.sans.org/webcasts/agentic-cti-automation-for-fun-and-profit
    date: '2026-06-25'
    access: full
    locator: abstract, 'Lessons Learned' list
  - ref: ARXIV-2609.01174
    title: 'A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.01174
    date: '2026-09-01'
    access: full
    locator: section 3.2; Table 2b
  - ref: ARXIV-2606.18166
    title: Evaluating Open-Source LLMs for Multi-Label ATT&CK Technique Classification on CTI Reports
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2606.18166
    date: '2026-06-16'
    access: full
    locator: abstract
  - ref: ARXIV-2509.23573
    title: Uncovering Vulnerabilities of LLM-Assisted Cyber Threat Intelligence
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2509.23573
    date: '2025-09-28'
    access: full
    locator: abstract
  - ref: ARXIV-2503.23175
    title: Large Language Models Are Unreliable for Cyber Threat Intelligence
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2503.23175
    date: '2025-03-29'
    access: full
    locator: abstract
  - ref: ARXIV-2603.13517
    title: 'CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2603.13517
    date: '2026-03-13'
    access: full
    locator: abstract
  - ref: FEEDLY-AUTOMATE-2026
    title: How to automate common CTI workflows (J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/how-to-automate-common-cti-workflows
    date: '2026-06-12'
    access: full
    locator: Workflow 2
  last_reviewed: '2026-10-17'
  notes: 'Grade B rests on Intel 471 describing its own team''s use; no figures are published for that use. The F1 values are lab benchmarks from
    preprints. ARXIV-2509.23573 and ARXIV-2503.23175 (LLMs unreliable for CTI: inconsistent and overconfident on real-size reports, 350 reports)
    are older foundations from 2025.'
- id: security-threat-intelligence-03
  title: Sanitize and codify internal findings into shareable intelligence (redaction and STIX generation)
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Turning an organization's own incident evidence into intelligence that can be shared outside it is slow and risky. In the SoK practitioner
    survey, 17 of 18 participants named preventing the exposure of sensitive information as a recurring difficulty, and 7 of 18 named translating
    CTI into the formats sharing platforms require. SANS reports that 55% of organizations lack legally reviewed CTI sharing processes (ARXIV-2609.01174,
    section 3.2; SANS-CTIPR-2026).
  solution: 'Researchers pilot LLMs for two steps: redacting victim identifiers and personal data from an incident report while keeping useful
    attacker detail, and converting analyst findings into a STIX 2.1 file. This is an idea under study; no organization was found using it in
    production. For contrast, CISA''s IMX platform, described at FIRST, uses a guided five-question interface to help experts publish STIX packages
    without schema expertise, without AI (FIRST-CON-2026, IMX session, 2026-06-15).'
  outcomes:
  - lever: quality
    description: 'Redaction pilot: a privacy-preserving prompt caught nearly every injected identifier but one model also removed many values
      that identify no one; a utility-preserving prompt reversed the errors.'
    figure: 'privacy-preserving prompt: 92 of 92 injected values flagged by Claude Opus 4.8 with 1 false positive; GPT-5.5 91 true positives with
      50 false positives'
    measures: injected personal and organizational identifier values flagged out of 92 injected values (plus 10 descriptive phrases) across 4
      held-out incident reports; false positives are removed values that were never identifiers
    provenance: independent
    source_ref: ARXIV-2609.01174
  - lever: quality
    description: 'STIX generation pilot: models typed software correctly but asserted more relationships than the findings supported.'
    figure: GLM 5.2 asserted 73 links, of which 38 were correct; GPT-5.5 asserted 67
    measures: links (technique-to-software and hash-to-software) asserted in a generated STIX file versus links the findings support
    provenance: independent
    source_ref: ARXIV-2609.01174
  prerequisites:
  - A legal and privacy review process for outward sharing; SANS finds 55% of organizations lack one while NIS2 and the Cyber Resilience Act add
    obligations in 2026 (SANS-CTIPR-2026, paragraph beginning 'The structural picture').
  - 'Labeled ground truth for owner-of-value decisions: the SoK notes a report writes victim and attacker machine names, addresses and accounts
    in the same form, which is why redaction is hard (ARXIV-2609.01174, Experiment 3).'
  risks_and_guardrails:
  - A recipient cannot trust an individual generated link without checking it; the authors suggest requiring every link to name the finding it
    rests on (ARXIV-2609.01174, Experiment 4 discussion).
  - Practitioners doubt AI reliability and worry it may compromise data privacy (ARXIV-2609.01174, introduction summary of the practitioner survey).
  human_checkpoints:
  - The SoK concludes each of the four steps (extraction, normalization and enrichment, codification, distribution) requires expert supervision
    (ARXIV-2609.01174, abstract).
  role_evolution: Not discussed in the sources for this step.
  evidence_grade: D
  sources:
  - ref: ARXIV-2609.01174
    title: 'A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.01174
    date: '2026-09-01'
    access: full
    locator: abstract; section 3.2; Tables 3 and 4
  - ref: SANS-CTIPR-2026
    title: 91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (press release)
    publisher: SANS Institute
    type: professional-body
    url: https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report
    date: '2026-05-19'
    access: full
    locator: paragraph beginning 'The structural picture'
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program (session abstracts)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: session abstract, 'Indicator Message eXchange (IMX)', 2026-06-15 11:00
  last_reviewed: '2026-10-17'
  notes: Idea (grade D). Evidence is a lab pilot with models run on researcher-built evidence; no deployment found. Only 3 of the 18 surveyed
    practitioners used LLMs at all.
- id: security-threat-intelligence-04
  title: Draft and tailor intelligence summaries and briefings for different audiences
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: 'CTI producers write the same finding several times for different readers: indicators for the SOC, operational notes for resilience
    leads, and strategic briefs for executives. SANS finds only 26% of CISOs say CTI significantly influences their decisions even though 91%
    value it, and practitioners in Feedly''s roundup say reports are often written for the analyst rather than the consumer (SANS-CTIPR-2026;
    FEEDLY-ROUNDUP-2026, Q2 Theme 1).'
  solution: Analysts use LLMs to summarize long reports, draft first versions of finished products and re-package the same assessed judgment as
    an executive brief, a technical brief and a risk note. SANS reports 45% of surveyed organizations use AI in CTI, mainly for summarization
    and report writing, with the human-in-the-loop model holding firm (SANS-CTIPR-2026). A practitioner essay (DTN Advisory) says dissemination
    is ripe for transformation because AI can tailor products by audience (DTN-CTI-2026, section on AI in threat intelligence).
  outcomes:
  - lever: capacity
    description: Share of surveyed organizations using AI in CTI programs, mainly for summarization, report writing and workflow automation.
    figure: 45% using; another 32% planning to adopt
    measures: share of surveyed organizations currently using AI in their CTI programs (401 practitioners surveyed Nov 2025 to Jan 2026); the
      32% is the share planning to adopt
    provenance: independent
    source_ref: SANS-CTI-2026
  - lever: quality
    description: No measurement of output quality for this step was found. Feedly's author reports LLM output compared with an analyst's was often
      too verbose, generic and operationally weak and lacked calibrated confidence.
    figure: none published
    measures: qualitative comparison of one request answered by an LLM and by an analyst; not a measured rate
    provenance: vendor-published
    source_ref: FEEDLY-VALUE-2026
  prerequisites:
  - 'Requirements first: DTN Advisory argues that feeding a well-structured priority intelligence requirement gives useful drafts and ''tell me
    about cyber threats'' gives noise at scale (DTN-CTI-2026, section on AI in the intelligence cycle).'
  - A one-page team policy on approved tools, data classification and disclosure of AI use in a report's methodology section (FEEDLY-VALUE-2026,
    section 'AI overreliance and the risk of de-skilling').
  risks_and_guardrails:
  - 'De-skilling: analysts who read AI summaries instead of primary sources may lose pattern recognition and the ability to navigate ambiguity;
    Feedly suggests requiring review of original sources before an assessment is submitted (FEEDLY-VALUE-2026, section ''AI overreliance and the
    risk of de-skilling'').'
  - LLM outputs currently lack calibrated epistemic confidence and compress away the exceptions that often carry the value (FEEDLY-VALUE-2026,
    section 'Model calibration gaps in probabilistic intelligence workflows').
  - Intel 471 says an AI-generated output is only as effective as the analyst validating it, and that intelligence is about trust consciousness
    and source traceability (INTEL471-AIHUMAN-2026, quote from M. DeBolt).
  human_checkpoints:
  - Peer review of analysis and reasoning by people; LLMs limited to surface-level edits (FEEDLY-VALUE-2026, mitigation list).
  role_evolution: Feedly's roundup and value essay both stress stakeholder-centric communication; the value essay warns that efficiency narratives
    could lead to budget cuts, hiring freezes and fewer entry-level roles (FEEDLY-VALUE-2026, section 'Introduction' and 'AI overreliance and
    the risk of de-skilling').
  evidence_grade: C
  sources:
  - ref: SANS-CTI-2026
    title: SANS 2026 Cyber Threat Intelligence Survey Insights (report landing page with takeaways and FAQ; full report not opened)
    publisher: SANS Institute
    type: survey
    url: https://www.sans.org/research/cyber-threat-intelligence-report
    date: 2026-05
    access: full
    locator: FAQ and takeaways
  - ref: SANS-CTIPR-2026
    title: 91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (press release)
    publisher: SANS Institute
    type: professional-body
    url: https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report
    date: '2026-05-19'
    access: full
    locator: paragraphs on CISO influence and AI use
  - ref: DTN-CTI-2026
    title: Your Threat Intelligence Team Is Collecting Data and Calling It Intelligence
    publisher: DTN Advisory (Substack)
    type: community
    url: https://dtnadvisory.substack.com/p/your-threat-intelligence-team-is
    date: '2026-03-31'
    access: full
    locator: section on AI in threat intelligence
  - ref: FEEDLY-VALUE-2026
    title: Quantifying & communicating the value of human-led intelligence in an AI era (A. Streetman)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/quantifying-and-communicating-the-value-of-human-led-intelligence-in-an-ai-era
    date: '2026-03-26'
    access: full
    locator: sections on de-skilling and calibration gaps
  - ref: FEEDLY-ROUNDUP-2026
    title: 2026 CTI Practitioners Roundup (14 practitioners; J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/2026-cti-practitioners-roundup
    date: '2026-01-29'
    access: full
    locator: 'Q2 Theme 1: Build audience identification into intelligence production'
  - ref: INTEL471-AIHUMAN-2026
    title: How AI and the human advantage beat tomorrow's threats
    publisher: Intel 471
    type: vendor
    url: https://www.intel471.com/blog/how-ai-and-the-human-advantage-beat-tomorrows-threats
    date: '2026-02-20'
    access: full
    locator: 'section ''The danger of blind trust: automation bias'''
  last_reviewed: '2026-10-17'
  notes: No named organization with a measured outcome was found. The SANS 45% is the best adoption number; the survey is sponsor-supported (Broadcom,
    ESET, Flare, Intel 471, SOCRadar, ThreatConnect, Wiz per the press release).
- id: security-threat-intelligence-05
  title: Score dark-web and underground events for relevance against an organizational profile
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - transaction-processing
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: External monitoring floods CTI teams with keyword hits. A Google launch post says the problem is a lack of relevance, not a lack of
    data, and that exact-match brand alerts miss a broker who deliberately avoids naming the victim (GOOGLE-DARKWEB-2026). In Flashpoint's interviews,
    alert noise and false positives were the most cited program challenge (65% of respondents), and one healthcare practitioner described alerts
    on seven- or eight-year-old email breaches resurfacing each time the data is resold (FLASHPOINT-ENTERPRISE-2026, section 'Operational Challenges
    Are Putting Pressure on Analyst Capacity').
  solution: Google's Threat Intelligence product uses Gemini to build and keep updating an organizational profile (business operations, mission,
    revenue bracket, geography, portal types) and to cross-reference underground posts against it, so only threats relevant to the business are
    elevated (GOOGLE-DARKWEB-2026). Recorded Future announced an 'Autonomous Threat Operations' layer that de-duplicates, validates, enriches
    and prioritizes feeds against a dynamic threat map and custom risk lists (FORRESTER-PREDICT-2025, section on Autonomous Threat Operations).
  outcomes:
  - lever: quality
    description: Google reports an internal accuracy figure for analyzing external events; the test design is not described.
    figure: 98% accuracy
    measures: 'Google: ''internal tests show Google Threat Intelligence can analyze millions of daily external events - with 98% accuracy''; accuracy
      definition, labels and sample not stated'
    provenance: vendor-published
    source_ref: GOOGLE-DARKWEB-2026
  - lever: quality
    description: A named customer quote in the launch post contrasts earlier tools with the new capability.
    figure: prior dark web tools 'averaged over 90% false positives' (customer's recollection from previous roles)
    measures: 'LastPass director of threat intelligence, quoted in the vendor post: dark web tools he used in previous roles; no measurement basis
      given'
    provenance: vendor-published
    source_ref: GOOGLE-DARKWEB-2026
  prerequisites:
  - A maintained organizational profile; Google says Gemini builds it automatically and adjusts as business operations change (GOOGLE-DARKWEB-2026,
    section 'Use deep business context and AI to move faster than the adversary').
  - 'Clear priority intelligence requirements to collect against: DTN Advisory says AI-driven monitoring needs good requirements and that ''relevant''
    is the key word (DTN-CTI-2026).'
  risks_and_guardrails:
  - Forrester's analyst says the real test of prioritization algorithms is delivering consistently without creating bias and blind spots, and
    that AI-driven triage that becomes a black box risks failing on accuracy and efficiency together (FORRESTER-PREDICT-2025, sections on Autonomous
    Threat Operations and the DRP operations hub).
  - 'Source handling is a gap: Feedly''s roundup quotes a practitioner saying teams talk about dark web monitoring but not real source handling
    (FEEDLY-ROUNDUP-2026, Q3 table).'
  human_checkpoints:
  - Not described for the Google capability; Forrester asks vendors for their testing and validation mechanisms (FORRESTER-PREDICT-2025).
  role_evolution: Defender's Advantage podcast show notes say the dark web rollout is 'fundamentally changing the way defenders track adversaries'
    (GOOGLE-DEFADV-DARKWEB-2026); the notes give no role detail.
  evidence_grade: C
  sources:
  - ref: GOOGLE-DARKWEB-2026
    title: Bringing dark web intelligence into the AI era
    publisher: Google Cloud Blog
    type: vendor
    url: https://cloud.google.com/blog/products/identity-security/bringing-dark-web-intelligence-into-the-ai-era
    date: '2026-03-23'
    access: full
    locator: paragraphs 1-4 and customer quote
  - ref: GOOGLE-DEFADV-DARKWEB-2026
    title: Using GTI to Hunt Adversaries on the Dark Web (The Defender's Advantage podcast; show notes)
    publisher: Google Threat Intelligence Group / Mandiant
    type: podcast
    url: https://feeds.buzzsprout.com/1762840.rss
    date: '2026-03-23'
    access: full
    locator: episode description (show notes only)
  - ref: FORRESTER-PREDICT-2025
    title: 'Recorded Future Predict 2025: Intelligence To Operations ... And Now To Action (J. Shabadu)'
    publisher: Forrester
    type: firm
    url: https://www.forrester.com/blogs/recorded-future-predict-2025-intelligence-to-operations-and-now-to-action/
    date: '2025-10-21'
    access: full
    locator: 'section ''Autonomous Threat Operations: A Supplemental Layer To Tackle Feed Chaos'''
  - ref: FLASHPOINT-ENTERPRISE-2026
    title: 'The Enterprise Threat Intelligence Report: 2026 (vendor-commissioned qualitative research, more than 20 interviewees)'
    publisher: Flashpoint
    type: survey
    url: https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/
    date: '2026-10-13'
    access: full
    locator: section 'Operational Challenges Are Putting Pressure on Analyst Capacity'
  - ref: FEEDLY-ROUNDUP-2026
    title: 2026 CTI Practitioners Roundup (14 practitioners; J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/2026-cti-practitioners-roundup
    date: '2026-01-29'
    access: full
    locator: Q3 table
  - ref: DTN-CTI-2026
    title: Your Threat Intelligence Team Is Collecting Data and Calling It Intelligence
    publisher: DTN Advisory (Substack)
    type: community
    url: https://dtnadvisory.substack.com/p/your-threat-intelligence-team-is
    date: '2026-03-31'
    access: full
    locator: section on AI in threat intelligence (collection paragraph)
  last_reviewed: '2026-10-17'
  notes: Announced capability; the post says the dark web intelligence capability is being introduced and invites RSAC visitors to a demo. The
    98% figure and the LastPass quote are vendor-published; they are reported here as claims, not as measured results.
- id: security-threat-intelligence-06
  title: 'OSINT copilot: LLM-assisted collection, enrichment and investigative search at scale'
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Collecting and enriching open-source and leak data by hand does not scale. Apura's FIRST abstract frames the work as transforming large-scale
    OSINT into structured, actionable intelligence (FIRST-CON-2026, session 2026-06-19 11:50).
  solution: Apura Cyber Intelligence (Brazil) presented a practical approach using open tooling, retrieval-augmented generation and agentic LLM
    workflows covering data extraction, enrichment, indexing and how LLMs support incident response through structured reasoning and reproducible
    analysis (FIRST-CON-2026, same session). SANS's agentic CTI webcast abstract describes automating and scaling OSINT and underground streams
    into usable intelligence (SANS-AGENTICWEB-2026, 'Lessons Learned').
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: The FIRST abstract states no results; slides were not reached.
    provenance: vendor-published
    source_ref: FIRST-CON-2026
  prerequisites:
  - Open tooling and an index over collected data (FIRST-CON-2026, Apura abstract).
  - Requirements to collect against (DTN-CTI-2026).
  risks_and_guardrails:
  - 'Source reliability and legal and ethical boundaries: a practitioner quoted by Feedly says disciplined HUMINT in cybercrime ecosystems means
    evaluating source reliability and spotting manipulation inside clear legal and ethical boundaries (FEEDLY-ROUNDUP-2026, Q3 table).'
  - Reproducibility is an explicit goal of the Apura session ('reproducible analysis') (FIRST-CON-2026, Apura abstract, 2026-06-19 11:50).
  human_checkpoints:
  - Not stated in the abstract.
  role_evolution: Not discussed in the sources.
  evidence_grade: C
  sources:
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program (session abstracts)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: 'session abstract, ''Beyond Manual Hunting: OSINT Copilot with LLMs'', 2026-06-19 11:50'
  - ref: SANS-AGENTICWEB-2026
    title: Agentic CTI Automation For Fun and Profit (webcast by R. Brown and J. Cran; abstract only, webcast not viewed)
    publisher: SANS Institute
    type: conference
    url: https://www.sans.org/webcasts/agentic-cti-automation-for-fun-and-profit
    date: '2026-06-25'
    access: full
    locator: abstract, 'Lessons Learned' list
  - ref: FEEDLY-ROUNDUP-2026
    title: 2026 CTI Practitioners Roundup (14 practitioners; J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/2026-cti-practitioners-roundup
    date: '2026-01-29'
    access: full
    locator: Q3 table, S. O'Connor
  - ref: DTN-CTI-2026
    title: Your Threat Intelligence Team Is Collecting Data and Calling It Intelligence
    publisher: DTN Advisory (Substack)
    type: community
    url: https://dtnadvisory.substack.com/p/your-threat-intelligence-team-is
    date: '2026-03-31'
    access: full
    locator: section on AI in threat intelligence (requirements paragraph)
  last_reviewed: '2026-10-17'
  notes: Vendor-practitioner conference abstract only. Grade C because the presenter is a CTI vendor describing its own approach with no outcome
    or customer.
- id: security-threat-intelligence-07
  title: LLM-assisted triage of infostealer logs and infection screenshots
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - transaction-processing
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Flare's FIRST abstract says over 50 million stealer logs were posted in 2025 alone, creating an analysis bottleneck 'impossible to
    address at scale' by hand, and that the forensic artifacts in those logs (infection vectors, campaign behavior) stay untapped because analysis
    is manual (FIRST-CON-2026, session 2026-06-17 09:40).
  solution: Flare introduced StealerLens at FIRST, an LLM-powered forensic tool to accelerate infostealer log investigations, building on its
    Black Hat USA 2025 work on LLM-based infection screenshot analysis (FIRST-CON-2026, same session).
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: The FIRST abstract states the size of the problem (over 50 million stealer logs posted in 2025) but no result for the tool.
    provenance: vendor-published
    source_ref: FIRST-CON-2026
  prerequisites:
  - Access to stealer-log corpora; not described beyond the abstract.
  risks_and_guardrails:
  - 'Not stated in the abstract. Related: a FIRST session shows crafted artifacts can steer LLM-assisted investigations, so ingestion of attacker-controlled
    data needs hardening (FIRST-CON-2026, CyCraft session 2026-06-18).'
  human_checkpoints:
  - Not stated in the abstract.
  role_evolution: Not discussed in the sources.
  evidence_grade: C
  sources:
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program (session abstracts)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: session abstract, 'Introducing StealerLens', 2026-06-17 09:40
  last_reviewed: '2026-10-17'
  notes: Single conference abstract by the tool's vendor; the Black Hat 2025 talk was not read.
- id: security-threat-intelligence-08
  title: Bounded agents that prepare external-threat evidence and takedown cases (brand abuse and phishing sites)
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - transaction-processing
  - document-production
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Phishing and impersonation sites often live only hours, and Memcyco says manual enrichment and case preparation consume the window
    in which takedown would matter (MEMCYCO-AGENTIC-2026, section on the bottleneck).
  solution: Memcyco's podcast page describes 'agentic threat intelligence' as bounded AI agents that continuously collect, enrich, score and package
    external threat evidence so analysts spend time on judgment and enforcement (MEMCYCO-AGENTIC-2026). Recorded Future announced an AI-driven
    alert triage in a digital risk protection operations hub that filters brand-misuse alerts using customer-provided context, with automatic
    takedowns (FORRESTER-PREDICT-2025, section 'One Platform, Two Promises').
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: Both sources describe intended benefits only; no measurement.
    provenance: vendor-published
    source_ref: MEMCYCO-AGENTIC-2026
  prerequisites:
  - Customer-provided context for relevance filtering (FORRESTER-PREDICT-2025, DRP operations hub paragraph).
  risks_and_guardrails:
  - Forrester says customers should evaluate AI triage on effectiveness and not only efficiency, because a black-box triage can fail on both (FORRESTER-PREDICT-2025,
    DRP operations hub paragraph).
  - Memcyco says analysts stay in control of enforcement decisions (MEMCYCO-AGENTIC-2026, section 'What agentic means in practice').
  human_checkpoints:
  - Analysts keep enforcement decisions (MEMCYCO-AGENTIC-2026).
  role_evolution: Memcyco says analysts move from manual groundwork to judgment and enforcement (MEMCYCO-AGENTIC-2026).
  evidence_grade: C
  sources:
  - ref: MEMCYCO-AGENTIC-2026
    title: 'MemcycoFM Ep 27: What Is Agentic Threat Intelligence? (vendor podcast, written episode page)'
    publisher: Memcyco
    type: podcast
    url: https://webcast.memcyco.com/library/the-memcycofm-show-ep-27/
    date: '2026-07-21'
    access: full
    locator: episode summary and section 'What agentic means in practice'
  - ref: FORRESTER-PREDICT-2025
    title: 'Recorded Future Predict 2025: Intelligence To Operations ... And Now To Action (J. Shabadu)'
    publisher: Forrester
    type: firm
    url: https://www.forrester.com/blogs/recorded-future-predict-2025-intelligence-to-operations-and-now-to-action/
    date: '2025-10-21'
    access: full
    locator: section 'One Platform, Two Promises'
  last_reviewed: '2026-10-17'
  notes: Vendor-authored podcast page and a vendor roadmap as read by an analyst; sits next to brand protection and fraud, which the landscape
    file folds into human-risk. Treated here because takedown evidence preparation is an external-threat intelligence product.
- id: security-threat-intelligence-09
  title: Turn threat reports into tested detection logic and hunt candidates
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - software-systems
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Moving from a threat report to a detection that actually fires requires locating the right telemetry, understanding its schema, writing
    executable logic and checking that it separates attack from normal behavior. Feedly estimates 20 to 40 minutes to convert IOCs into detection
    rules and 20 to 40 minutes to convert TTPs into hunt hypotheses, per report (FEEDLY-AUTOMATE-2026, Workflow 5).
  solution: Agents read a CTI report, query a telemetry store, and draft Sigma or KQL logic. The CTI-REALM benchmark (Microsoft researchers) measures
    this end to end (ARXIV-2603.13517; DETENGWEEKLY-163-2026; PACKT-CTIREALM-2026); Feedly publishes prompts for detection rules and hunt hypotheses
    (FEEDLY-AUTOMATE-2026, Workflow 5); Vega's Detection Skills spec packages triage, investigation and tuning knowledge as portable skill files
    attached to a detection (DETENGWEEKLY-167-2026). Intel 471's hunters are skeptical of out-of-the-box AI detection content (INTEL471-HUNTING-2025,
    section 'Threat Detection').
  outcomes:
  - lever: quality
    description: Sixteen frontier models scored on an executable benchmark; the best normalized reward was well short of 1.
    figure: best reward 0.637 (Claude Opus 4.6, high setting), 0.624 (Claude Opus 4.5)
    measures: normalized reward across five checkpoints (report analysis, ATT&CK mapping, telemetry discovery, query execution, final detection
      quality; final detection carries 65% of the reward) on emulated attacks in Linux, Azure Kubernetes Service and Azure cloud
    provenance: independent
    source_ref: ARXIV-2603.13517
  - lever: cost
    description: On the same benchmark, an open-weight model matched the strongest closed models at under a tenth of their cost when allowed enough
      turns; the benchmark's message limit is a confound.
    figure: less than one tenth of the cost (strongest closed models)
    measures: 26 models (19 open-weight, 7 closed) under a common harness; cost comparison of models with similar rewards; the published agent-message
      limit truncates some models
    provenance: independent
    source_ref: ARXIV-2610.14180
  - lever: quality
    description: An LLM system converting IOCs from CTI reports into regexes reported a high hit rate and low false positives against ground-truth
      strings.
    figure: hit rate 99.1%; false-positive rate 0.8% (authors' system)
    measures: IOCRegex-gen on over 3,000 real CTI reports and 2,400 ground-truth strings from the MITRE ATT&CK Evaluation framework; the authors'
      own experiments
    provenance: independent
    source_ref: ARXIV-2604.12228
  prerequisites:
  - 'Telemetry with a known schema and a place to test: the benchmark runs agents in a containerized environment with a Kusto emulator and recorded
    logs (PACKT-CTIREALM-2026, sections ''How teams can use it today'').'
  - 'Check whether the idea is worth building: a Sigma rule found online is not automatically backlog-worthy; ask whether existing visibility
    and coverage already address it and whether relevant adversaries target a company like yours (DETENGWEEKLY-168-2026, summary of Katz and Deyalsingh).'
  - 'A seeded-context option: memory augmentation closed 33% of the gap between smaller and larger models (ARXIV-2603.13517, abstract).'
  risks_and_guardrails:
  - A fluent explanation of an intrusion can sit alongside a detection that misses it; the newsletter author notes the benchmark does not establish
    adoption in production SOCs (PACKT-CTIREALM-2026, section 'How teams can use it today').
  - Intel 471's hunters cite high false positives and the lack of control as reasons for skepticism about out-of-the-box AI detection content
    (INTEL471-HUNTING-2025, section 'Threat Detection').
  - 'Feedly: a wrong indicator or an unfounded rule at scale generates false positives that erode SOC trust quickly (FEEDLY-AUTOMATE-2026, ''Where
    the human analyst is still required'').'
  human_checkpoints:
  - Output reaching production detection or response tooling needs human review (FEEDLY-AUTOMATE-2026); Microsoft explicitly reinforces human
    review per the newsletter (PACKT-CTIREALM-2026).
  role_evolution: The Detection Engineering Weekly author argues agent skills are the next step after detection-as-code, so analysts encode triage
    and tuning knowledge as well as detection logic (DETENGWEEKLY-167-2026, section on Detection Skills by Vega Threat Research).
  evidence_grade: C
  sources:
  - ref: ARXIV-2603.13517
    title: 'CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2603.13517
    date: '2026-03-13'
    access: full
    locator: abstract
  - ref: ARXIV-2610.14180
    title: Unconstrained CTI-REALM with Open-Weights
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.14180
    date: '2026-10-09'
    access: full
    locator: abstract
  - ref: ARXIV-2604.12228
    title: 'From IOCs to Regex: Automating CTI Operationalization for SOC with LLMs'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2604.12228
    date: '2026-04-14'
    access: full
    locator: abstract
  - ref: PACKT-CTIREALM-2026
    title: '#34: CTI-REALM tests whether AI can turn threat intelligence into detections'
    publisher: Packt Cyber_AI newsletter (Substack)
    type: community
    url: https://packtcyberai.substack.com/p/34-cti-realm-tests-whether-ai-can
    date: '2026-10-07'
    access: full
    locator: sections 'What the score actually measures' and 'How teams can use it today'
  - ref: DETENGWEEKLY-163-2026
    title: 'DEW #163 - Semantic Malware Detections, Microsoft''s CTI REALM evals and Thrunting for Knowledge'
    publisher: Detection Engineering Weekly
    type: community
    url: https://www.detectionengineering.net/p/dew-163-semantic-malware-detections
    date: '2026-07-15'
    access: full
    locator: 'item ''CTI-REALM: A new benchmark'''
  - ref: DETENGWEEKLY-167-2026
    title: 'DEW #167 - More Security Agentic Breaches, Cheap and Scalable Threat Hunting & Detection Skills'
    publisher: Detection Engineering Weekly
    type: community
    url: https://www.detectionengineering.net/p/dew-167-more-security-agentic-breaches
    date: '2026-08-19'
    access: full
    locator: item 'Detection Skills by Vega Threat Research'
  - ref: DETENGWEEKLY-168-2026
    title: 'DEW #168 - The Detection Rule Stork, OpenWeight models vs your SIEM and Sigma vs. YARA'
    publisher: Detection Engineering Weekly
    type: community
    url: https://www.detectionengineering.net/p/dew-168-the-detection-rule-stork
    date: '2026-08-26'
    access: full
    locator: item on where detection ideas originate
  - ref: INTEL471-HUNTING-2025
    title: How AI can (and can't) help in threat hunting
    publisher: Intel 471
    type: vendor
    url: https://www.intel471.com/blog/how-ai-can-and-cant-help-in-threat-hunting
    date: '2025-09-09'
    access: full
    locator: section 'Threat Detection'
  - ref: FEEDLY-AUTOMATE-2026
    title: How to automate common CTI workflows (J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/how-to-automate-common-cti-workflows
    date: '2026-06-12'
    access: full
    locator: Workflow 5
  last_reviewed: '2026-10-17'
  notes: Benchmark evidence only. Overlaps with security-operations (detection engineering); the intelligence-to-rule step is kept here and the
    rule lifecycle is routed. Authors of the open-weight paper evaluate models on a benchmark they did not create; model names are as published.
- id: security-threat-intelligence-10
  title: AI as a sounding board and enrichment layer in human-led, intelligence-driven threat hunts
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: 'Hunters can fixate on one indicator or path, need to understand unfamiliar techniques and query languages, and must document findings
    for several audiences. Intel 471 structures its hunts on the TaHiTI method: initiate (new intelligence, alerts, red-team activity), hunt (hypothesis,
    data sources, queries), finalize (reporting and hand-offs) (INTEL471-HUNTING-2025, section ''How AI can help your threat hunting teams'').'
  solution: Intel 471's threat hunt analysts report using AI to stress-test hypotheses, to suggest related actor groups and ATT&CK techniques
    that expand a hypothesis, to find adjacent hunting paths, to point to query-language documentation, and to draft documentation (INTEL471-HUNTING-2025,
    sections 'Hypothesis Development', 'Enrichment' and 'Reporting and Documentation'). They say AI cannot yet develop a complete hypothesis.
    Researchers separately describe AHLERT, which turns CTI reports into environment-aware hunt leads constrained to the defender's own assets
    and controls (ARXIV-2609.08790, abstract). BSides Las Vegas 2026 lists a hands-on workshop on building agentic AI skill files for network
    security monitoring hunts (BSIDESLV-2026, workshop 'Engineering the Hunt').
  outcomes:
  - lever: quality
    description: Intel 471 publishes no figures for its own use. In a research prototype, retrieval with ontology grounding raised the quality
      of generated hunt leads over a single-route RAG baseline.
    figure: mean F1 0.44 to 0.85 (flat-RAG baseline versus AHLERT's hybrid retrieval with ontology grounding)
    measures: mean F1 of generated hunt leads from public CTI reports for well-known APTs, across proprietary and open-weight models; authors
      report a separate 'effectiveness score' of about 86.95% whose definition is not in the abstract
    provenance: independent
    source_ref: ARXIV-2609.08790
  prerequisites:
  - A structured hunt method with explicit triggers and hypotheses (Intel 471 uses TaHiTI) (INTEL471-HUNTING-2025).
  - 'Adequate log retention and baselines: some EDRs do not retain beyond 30, 60 or 90 days, which can leave too little history to identify anomalies
    confidently (INTEL471-HUNTING-2025, section ''Data Analysis'', quote from L. Archinal).'
  - 'Retrieval over the organization''s own policies, procedures and data: Intel 471''s hunters call RAG a promising way to tailor a pre-trained
    model (INTEL471-HUNTING-2025, section ''Threat Detection'').'
  risks_and_guardrails:
  - 'Sycophancy: models designed to be agreeable can reinforce confirmation bias on a poorly documented technique; Intel 471 recommends fact-finding
    questions before pitching a hypothesis (INTEL471-HUNTING-2025, section ''Hypothesis Development'').'
  - Query design gives mixed results because models lack training on current resources (INTEL471-HUNTING-2025, section 'Data Scoping and Query
    Design').
  - 'Forrester''s analyst framing: use deterministic tools where they suffice and reserve nondeterministic LLM, RAG and agent-style tools for
    where they pay off, and use it to test vendor promises (SANS-LEASTAI-2026, abstract).'
  human_checkpoints:
  - The hunter forms and owns the hypothesis; AI is 'in the loop' of the human's thinking (INTEL471-HUNTING-2025, section 'Hypothesis Development').
  role_evolution: Practitioners quoted by SecurityWeek in January 2026 expect AI to take routine and data-intensive tasks while hunters focus
    on strategic investigations, with several saying full automation is unlikely to replace human hunters (SECURITYWEEK-HUNTING-2026, section
    'The continuing rise of automation'; quotes from Intel 471's A. Jess, Elastic's D. Kerr).
  evidence_grade: B
  sources:
  - ref: INTEL471-HUNTING-2025
    title: How AI can (and can't) help in threat hunting
    publisher: Intel 471
    type: vendor
    url: https://www.intel471.com/blog/how-ai-can-and-cant-help-in-threat-hunting
    date: '2025-09-09'
    access: full
    locator: sections 'Hypothesis Development', 'Data Scoping and Query Design', 'Threat Detection', 'Data Analysis', 'Enrichment', 'Reporting
      and Documentation'
  - ref: ARXIV-2609.08790
    title: Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.08790
    date: '2026-09-08'
    access: full
    locator: abstract
  - ref: BSIDESLV-2026
    title: BSides Las Vegas 2026 talk list (abstracts)
    publisher: BSides Las Vegas
    type: conference
    url: https://bsideslv.org/talks
    date: 2026-08
    access: full
    locator: 'Training Ground workshop ''Engineering the Hunt: Developing AI SKILLs for Network Security Monitoring'', Monday 15:00-19:00'
  - ref: SANS-LEASTAI-2026
    title: 'Principle of Least AI in Threat Intelligence: A Blueprint for Effective GenAI Adoption (J. Shabadu, Forrester; abstract)'
    publisher: SANS Institute
    type: conference
    url: https://www.sans.org/presentations/principle-of-least-ai-in-threat-intelligence-a-blueprint-for-effective-genai-adoption
    date: '2026-01-27'
    access: full
    locator: abstract
  - ref: SECURITYWEEK-HUNTING-2026
    title: 'Cyber Insights 2026: Threat Hunting in an Age of Automation and AI (read through the r.jina.ai text mirror; direct fetch blocked)'
    publisher: SecurityWeek
    type: press
    url: https://www.securityweek.com/cyber-insights-2026-threat-hunting-in-an-age-of-automation-and-ai/
    date: '2026-01-26'
    access: full
    locator: section 'The continuing rise of automation'
  last_reviewed: '2026-10-17'
  notes: 'Grade B: a named company describes how its own hunters use AI; no measurements. The ChatGPT reference model is the one Intel 471''s
    hunters know best, per the post. The AHLERT figure is a lab result from other authors.'
- id: security-threat-intelligence-11
  title: Scheduled AI hunt agents that investigate across log sources, with adversarial validation of findings
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: 'Grow Therapy (a healthcare platform) needed proactive coverage across every system touching sensitive data, but rules cover only patterns
    someone knows how to write: ''everything you can''t write a rule for'' across sources such as AWS, Okta, Google Workspace, GitHub, CrowdStrike,
    Slack and Stripe (GROWTHERAPY-HUNT-2026, section ''Extending threat detection with LLMs'').'
  solution: 'About 20 YAML-defined hunts run daily as containers on AWS ECS Fargate, each a five-phase Claude-based investigation: data gathering
    on a cheaper model, baseline comparison, context enrichment, confidence scoring, and a final phase where the model must argue against its
    own findings and may reject one only with specific counter-evidence. Findings land in the same alert table as SQL detections and flow to Slack
    and Jira (GROWTHERAPY-HUNT-2026, sections ''How it runs on AWS'' and ''Multi-phase analysis''). For contrast, Recorded Future announced an
    ''Autonomous Threat Hunting'' agent that runs tailored hunts and lets users create Sigma rules, which Forrester called a good first step but
    far from true autonomy (FORRESTER-PREDICT-2025, section ''Inching Toward Autonomy'').'
  outcomes:
  - lever: cost
    description: Running about 20 daily AI hunts plus SQL detections costs about $500 per month on existing data infrastructure.
    figure: $320 to $510 per month (about $500)
    measures: 'Grow Therapy''s own monthly cost table: Claude API $250-400, Snowflake compute $60-90, ECS Fargate $10-20, other $5-10; Datadog
      line item $0 because it reuses existing spend. Detection Engineering Weekly notes the figure is additive to baseline Datadog and Snowflake
      spend, which is not disclosed'
    provenance: self-reported
    source_ref: GROWTHERAPY-HUNT-2026
  - lever: cost
    description: Using the cheaper model for the data-gathering phase cut cost.
    figure: about 60% cost reduction
    measures: the post's statement that switching phase 1 to Sonnet alone cut costs by about 60% compared with using the larger model with extended
      thinking for every phase
    provenance: self-reported
    source_ref: GROWTHERAPY-HUNT-2026
  - lever: quality
    description: Adding the adversarial-validation phase reduced noise.
    figure: about 40% of findings were noise without the phase; about one third of confirmed findings in the four-phase version were things a
      human would have dismissed with 30 seconds of context
    measures: Grow Therapy's own estimates of share of findings that were noise or dismissible, before the fifth phase was added; counts and period
      not stated
    provenance: self-reported
    source_ref: GROWTHERAPY-HUNT-2026
  - lever: quality
    description: Tuning a new hunt in a staging table before enabling alerts reduced volume.
    figure: from 15+ findings per run to 2-3 per run (first CloudTrail hunt)
    measures: findings per run for one hunt, before and after signal-to-noise tuning in staging; single-hunt example
    provenance: self-reported
    source_ref: GROWTHERAPY-HUNT-2026
  prerequisites:
  - 'Logs already centralized in a queryable store: the author says the data pipeline matters more than the AI (GROWTHERAPY-HUNT-2026, section
    ''Lessons from building this'').'
  - Build the analyst feedback loop (false-positive clicks flowing back into future hunts) before deploying (same section).
  - 'Start narrow on tools: the first five hunts used two data sources; more tools bloat context and lower signal to noise (same section).'
  - Per-hunt token and cost tracking from day one (same section).
  - 'Risky Business sponsor segments argue the data layer is the lever: a founder says a lot of security is a data problem, and Corelight discusses
    whether a sophisticated model or nicely structured data matters more for automated SOC work (RISKYBIZ-SOAPBOX109-2026; RISKYBIZ-855-2026).'
  risks_and_guardrails:
  - The model can overstate findings and occasionally invent evidence it did not find, so explicit validation is part of the system design (GROWTHERAPY-HUNT-2026,
    section 'Multi-phase analysis').
  - Default is to keep a finding unless the model produces specific counter-evidence; vague counter-evidence does not suppress it (same section).
  - Automated containment is generally limited to high-confidence, contained actions; tiered automation keeps high-risk actions with humans (SECURITYWEEK-HUNTING-2026,
    section 'The continuing rise of automation').
  - Behavioral baselines need 60 to 90 days of data before anomaly detection is reliable, per a vendor quoted by SecurityWeek (SECURITYWEEK-HUNTING-2026).
  human_checkpoints:
  - Analysts mark findings as false positive in Slack, which syncs to Jira and back to the data store; findings with 3 or more occurrences and
    an 80% or higher false-positive rate are injected as known false positives (GROWTHERAPY-HUNT-2026, section 'Handling noise').
  - A weekly report on hunts run, findings, false positives and cost is reviewed to decide which hunts need tuning (GROWTHERAPY-HUNT-2026, section
    'Where it stands today').
  role_evolution: Not discussed in the post beyond the analyst feedback loop (GROWTHERAPY-HUNT-2026).
  evidence_grade: A
  sources:
  - ref: GROWTHERAPY-HUNT-2026
    title: 'Threat hunt AI: How we built an AI security analyst on AWS for under $500/month'
    publisher: Grow Therapy engineering blog
    type: firm
    url: https://engineering.growtherapy.com/post/threat-hunt-ai-how-we-built-an-ai-security-analyst-on-aws-for-under-500-month
    date: 2026-08
    access: full
    locator: sections 'How it runs on AWS', 'Multi-phase analysis', 'Handling noise', 'Lessons from building this', 'Where it stands today'
  - ref: DETENGWEEKLY-167-2026
    title: 'DEW #167 - More Security Agentic Breaches, Cheap and Scalable Threat Hunting & Detection Skills'
    publisher: Detection Engineering Weekly
    type: community
    url: https://www.detectionengineering.net/p/dew-167-more-security-agentic-breaches
    date: '2026-08-19'
    access: full
    locator: 'item ''Threat hunt AI: How we built an AI security analyst on AWS for under $500/month'' (summary and cost caveat)'
  - ref: FORRESTER-PREDICT-2025
    title: 'Recorded Future Predict 2025: Intelligence To Operations ... And Now To Action (J. Shabadu)'
    publisher: Forrester
    type: firm
    url: https://www.forrester.com/blogs/recorded-future-predict-2025-intelligence-to-operations-and-now-to-action/
    date: '2025-10-21'
    access: full
    locator: section 'Inching Toward Autonomy, One Advanced Automation At A Time'
  - ref: SECURITYWEEK-HUNTING-2026
    title: 'Cyber Insights 2026: Threat Hunting in an Age of Automation and AI (read through the r.jina.ai text mirror; direct fetch blocked)'
    publisher: SecurityWeek
    type: press
    url: https://www.securityweek.com/cyber-insights-2026-threat-hunting-in-an-age-of-automation-and-ai/
    date: '2026-01-26'
    access: full
    locator: section 'The continuing rise of automation'
  - ref: RISKYBIZ-SOAPBOX109-2026
    title: 'Soap Box: Using threat hunting to drive detection (sponsored; Nebulock founder; show notes)'
    publisher: Risky Business Media
    type: podcast
    url: https://risky.biz/SOAPBOX109/
    date: '2026-07-08'
    access: full
    locator: show notes
  - ref: RISKYBIZ-855-2026
    title: 'Risky Business #855 -- ShinyHunters done sowing, enters reaping phase (show notes, sponsor interview with Corelight)'
    publisher: Risky Business Media
    type: podcast
    url: https://risky.biz/RB855/
    date: '2026-10-14'
    access: full
    locator: sponsor segment in show notes
  last_reviewed: '2026-10-17'
  notes: The only measured outcome from a named organization found for this module, and it is self-reported by a single company with its own definitions.
    The hunts are log-based and not all are intelligence-driven; included because threat hunting is in the module's scope. The same post is covered
    for SOC operations in the security-operations discourse file. The post is undated; DETENGWEEKLY-167-2026 (2026-08-19) features it, so it is
    dated 2026-08 here.
- id: security-threat-intelligence-12
  title: 'Human-machine teaming for frontline intelligence analysts: assistants, query drafting and judge agents'
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Frontline intelligence work has repetitive steps (decoding scripts, writing hunting queries, labeling metadata) and long ramp-up for
    analysts moving between domains.
  solution: The lead of the AI function for Google Threat Intelligence Group's Frontline Intelligence Operations team describes moving from simple
    prompt engineering to agentic workflows under a 'human-machine teaming' model, with automated script decoding, hunting query creation and
    repetitive metadata labeling; 'judge agents' for quality control; structured analytic techniques; and real-time AI assistants to speed onboarding
    and domain transitions (GOOGLE-DEFADV-HMT-2026, episode description).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Show notes describe use cases and concepts only; no figures. Audio and transcript were not available.
    provenance: vendor-published
    source_ref: GOOGLE-DEFADV-HMT-2026
  prerequisites:
  - Not stated in the show notes.
  risks_and_guardrails:
  - Judge agents are described as a quality-control concept (GOOGLE-DEFADV-HMT-2026). Feedly's author cautions that LLM-as-judge and similar methods
    can reduce obvious errors but do not always remove confident misinterpretation, and that correlated errors are harder to detect than isolated
    ones (FEEDLY-VALUE-2026, section 'The automation tradeoff').
  human_checkpoints:
  - The model is named 'human-machine teaming'; specifics not in the show notes (GOOGLE-DEFADV-HMT-2026).
  role_evolution: The episode links AI assistants to faster onboarding and domain transitions for frontline analysts (GOOGLE-DEFADV-HMT-2026).
    Feedly's hiring guide lists AI literacy as tool proficiency, context engineering and validation (FEEDLY-HIRING-2026, section 'AI Literacy
    as the New Differentiator').
  evidence_grade: B
  sources:
  - ref: GOOGLE-DEFADV-HMT-2026
    title: 'Human-Machine Teaming: Applying AI to Frontline Threat Intelligence Workflows (The Defender''s Advantage podcast; show notes)'
    publisher: Google Threat Intelligence Group / Mandiant
    type: podcast
    url: https://feeds.buzzsprout.com/1762840.rss
    date: '2026-07-13'
    access: full
    locator: episode description, 2026-07-13
  - ref: FEEDLY-VALUE-2026
    title: Quantifying & communicating the value of human-led intelligence in an AI era (A. Streetman)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/quantifying-and-communicating-the-value-of-human-led-intelligence-in-an-ai-era
    date: '2026-03-26'
    access: full
    locator: 'section ''The automation tradeoff: Speed, skill, and systemic risk'''
  - ref: FEEDLY-HIRING-2026
    title: 'Hiring for the AI era: A CTI leader''s guide to building tomorrow''s threat intelligence teams (J. Feyerabend)'
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/hiring-for-the-ai-era-a-cti-leader-s-guide-to-building-tomorrow-s-threat-intelligence-teams
    date: '2026-07-16'
    access: full
    locator: section 'AI Literacy as the New Differentiator'
  last_reviewed: '2026-10-17'
  notes: Grade B on a named team described by its own employer's podcast notes. Whether the work is pilot or production is not stated, so maturity
    is recorded as piloting.
- id: security-threat-intelligence-13
  title: Continuous coverage monitoring against priority intelligence requirements, with standing briefings
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - coordination-scheduling
  - document-production
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: Teams' mandates are growing without matching budgets; in Flashpoint's interviews, alert noise and false positives (65%), analyst bandwidth
    (55%) and integration gaps (half of respondents) were the most-cited barriers, and one healthcare threat intelligence leader said 'we can't
    hire our way out of that problem' (FLASHPOINT-ENTERPRISE-2026, section 'Operational Challenges Are Putting Pressure on Analyst Capacity').
    In the SANS survey most formal CTI teams have fewer than four full-time staff, 57% of programs do not track maturity over time and 49% gather
    no systematic feedback on effectiveness (SANS-CTIPR-2026).
  solution: Flashpoint's report says interviewees see PIR coverage monitoring and intelligence briefings as areas where AI can extend coverage
    and reduce recurring work while keeping analysts involved, and treats tasks with reviewable outputs, reversible actions and clear success
    criteria as the practical starting point (FLASHPOINT-ENTERPRISE-2026, section 'What the Findings Mean for Threat Intelligence Programs').
  outcomes:
  - lever: capacity
    description: Agentic AI adoption among the organizations Flashpoint interviewed.
    figure: 25% in production; 20% piloting; 35% planning adoption within 12 to 24 months
    measures: share of organizations interviewed (more than 20 threat intelligence budget owners and influencers at large North American enterprises
      in financial services and insurance, healthcare and biotech, retail, IT and telecom, early fall 2026); qualitative sample, so shares rest
      on a handful of organizations
    provenance: vendor-published
    source_ref: FLASHPOINT-ENTERPRISE-2026
  - lever: capacity
    description: Budget outlook for threat intelligence among respondents who gave one.
    figure: 50% expect an increase; 35% expect 10% or more; 40% expect flat; none expect a decrease
    measures: share of respondents who provided a budget outlook for the next 12 months
    provenance: vendor-published
    source_ref: FLASHPOINT-ENTERPRISE-2026
  prerequisites:
  - Priority intelligence requirements that connect new coverage areas, such as AI-enabled threats, to business risks (FLASHPOINT-ENTERPRISE-2026,
    section 'AI-Related Threats Are Driving New Coverage Priorities').
  - Clear measures of success before deployment; the report names time savings, accuracy, risk reduction and ROI as what practitioners track (FLASHPOINT-ENTERPRISE-2026,
    introduction).
  risks_and_guardrails:
  - 'One respondent: ''An agent that''s confidently wrong is worse than one that''s slow.'' A retail respondent would consider only read-only
    assistants because of write-permission risk; others raised data leakage, auditability, regulatory requirements and cost (FLASHPOINT-ENTERPRISE-2026,
    section ''Agentic AI Adoption Is Underway'').'
  - 'Feedly''s roundup: practitioners reject activity metrics (report counts, IOC volume) in favor of outcome metrics such as decisions influenced,
    controls implemented and time from intelligence to action (FEEDLY-ROUNDUP-2026, executive summary).'
  human_checkpoints:
  - Analysts stay involved in the intelligence process; agents that move from retrieving to acting need clear controls on access, change, approval
    and audit (FLASHPOINT-ENTERPRISE-2026).
  role_evolution: Recorded Future's customer panelists said junior analysts would not be replaced by AI but their jobs would look very different
    as they use AI to augment their workflows (RF-PRACTITIONER-2025, section 'Looking to the future of threat intelligence').
  evidence_grade: C
  sources:
  - ref: FLASHPOINT-ENTERPRISE-2026
    title: 'The Enterprise Threat Intelligence Report: 2026 (vendor-commissioned qualitative research, more than 20 interviewees)'
    publisher: Flashpoint
    type: survey
    url: https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/
    date: '2026-10-13'
    access: full
    locator: sections 'Executive Summary', 'Agentic AI Adoption Is Underway', 'What the Findings Mean for Threat Intelligence Programs', 'Methodology'
  - ref: SANS-CTIPR-2026
    title: 91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (press release)
    publisher: SANS Institute
    type: professional-body
    url: https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report
    date: '2026-05-19'
    access: full
    locator: paragraph on resourcing
  - ref: FEEDLY-ROUNDUP-2026
    title: 2026 CTI Practitioners Roundup (14 practitioners; J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/2026-cti-practitioners-roundup
    date: '2026-01-29'
    access: full
    locator: executive summary; Q4
  - ref: RF-PRACTITIONER-2025
    title: Practitioners Reveal What Makes Threat Intelligence Programs Mature (webinar recap; page undated, refers to the 2025 State of Threat
      Intelligence Report)
    publisher: Recorded Future
    type: vendor
    url: https://www.recordedfuture.com/blog/practitioner-insights-advancing-threat-intelligence
    date: '2025'
    access: full
    locator: section 'Looking to the future of threat intelligence'
  last_reviewed: '2026-10-17'
  notes: Vendor-commissioned qualitative research with a small sample; the 25/20/35 shares describe a few organizations. The report does not name
    them. RF-PRACTITIONER-2025 is a vendor webinar recap with an undated page.
- id: security-threat-intelligence-14
  title: Consolidate reports about the same threat into one knowledge graph anchored on ATT&CK behavior
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: The same threat is often given unrelated names across vendors, so per-report extraction leaves a fragmented picture; BEACON's authors
    say existing approaches mainly extract partial information within a single report (ARXIV-2608.28394, abstract). A SANS summit talk list includes
    a session on managing the deprecation of threat actor aliases, which points at the naming problem (SANS-CTISUMMIT-2026, Day 2 list; title
    only).
  solution: BEACON is an LLM-driven framework that extracts each report into a graph under a propose-then-verify design, anchors entities on ATT&CK
    behaviors, and merges graphs using signals from character-level similarity through overlapping technique neighborhoods (ARXIV-2608.28394,
    abstract).
  outcomes:
  - lever: quality
    description: BEACON beat all baselines on two human-annotated datasets the authors built.
    figure: at least 23% (extraction) and at least 9% (cross-source consolidation) better than all baselines
    measures: 'authors'' own comparison on their own released datasets from 34 sources: 8,395 elements for report-level extraction and 3,487 for
      cross-source consolidation; the metric behind the percentages is not in the abstract'
    provenance: independent
    source_ref: ARXIV-2608.28394
  prerequisites:
  - Human-annotated ground truth linking entities to technique anchors, which the authors had to build because none existed (ARXIV-2608.28394,
    abstract).
  risks_and_guardrails:
  - Hallucination and misclassification are controlled by grounding candidates in report evidence and official ATT&CK definitions (ARXIV-2608.28394,
    abstract).
  human_checkpoints:
  - Not described.
  role_evolution: Not discussed in the sources.
  evidence_grade: D
  sources:
  - ref: ARXIV-2608.28394
    title: 'BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.28394
    date: '2026-08-28'
    access: full
    locator: abstract
  - ref: SANS-CTISUMMIT-2026
    title: A Visual Summary of SANS CTI Summit 2026 (speaker and talk list)
    publisher: SANS Institute
    type: conference
    url: https://www.sans.org/blog/visual-summary-sans-cti-summit-2026
    date: '2026-01-26'
    access: full
    locator: 'Day 2 talk list: ''Knowing When to Quit: A Framework for Managing the Deprecation of Threat Actor Aliases'''
  last_reviewed: '2026-10-17'
  notes: 'Idea (grade D): a research prototype with authors'' own benchmark; no adoption found.'
- id: security-threat-intelligence-15
  title: Structure the corpus of vendor reports to measure source overlap and bias before buying or trusting a feed
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - data-reporting
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: 'Annual vendor IR and threat reports contradict one another on top intrusion vectors and on definitions of common categories such as
    credential misuse; a Team Cymru FIRST session attributes this to structural bias in each vendor''s data-collection pipeline, not to attacker
    volatility (FIRST-CON-2026, ''Disparate Data, Distorted Decisions: Vendor Data Bias in CTI'', 2026-06-15 11:50).'
  solution: A research team used an LLM-based pipeline to ingest and structure 16,096 open-source CTI reports spanning two decades and extract
    actors, motivations, victims, vendors and indicators, then analyzed the CTI ecosystem itself (ARXIV-2602.17458, abstract). The Team Cymru
    session presents an empirical comparison of major public reports and a framework for reading them as partial lenses (FIRST-CON-2026, same
    session).
  outcomes:
  - lever: quality
    description: The authors report low overlap between vendors and diminishing returns from adding sources.
    figure: none quantified in the abstract
    measures: marginal coverage analysis over 16,096 reports; the abstract states overlap is 'typically low' but gives no number
    provenance: independent
    source_ref: ARXIV-2602.17458
  prerequisites:
  - A structured corpus of reports with extracted entities (ARXIV-2602.17458, abstract).
  risks_and_guardrails:
  - The authors call the LLM pipeline high-precision; precision is theirs to report and was not independently checked here (ARXIV-2602.17458,
    abstract).
  human_checkpoints:
  - Not described.
  role_evolution: Not discussed in the sources.
  evidence_grade: D
  sources:
  - ref: ARXIV-2602.17458
    title: 'The CTI Echo Chamber: Fragmentation, Overlap, and Vendor Specificity in Twenty Years of Cyber Threat Reporting'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2602.17458
    date: '2026-02-19'
    access: full
    locator: abstract
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program (session abstracts)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: 'session ''Disparate Data, Distorted Decisions: Vendor Data Bias in CTI'''
  last_reviewed: '2026-10-17'
  notes: Idea (grade D) in the sense of a research use of LLMs for source evaluation; the Team Cymru human analysis shows the need but is not
    AI.
- id: security-threat-intelligence-16
  title: Extract strategic intelligence (targeted sectors, groups, loss scale) from social media streams
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  - data-reporting
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: STINER's authors say X (formerly Twitter) is often the fastest source of strategic intelligence, with breach announcements appearing
    days before formal vendor reports, but informal language defeats conventional named-entity recognition (ARXIV-2608.14418, abstract).
  solution: A taxonomy of eight entity types and an expert-annotated corpus of 2,100 real-world alerts, used to benchmark nine models in 12 configurations
    (ARXIV-2608.14418, abstract).
  outcomes:
  - lever: quality
    description: A domain-adapted encoder beat general-purpose baselines and fine-tuned LLMs, which also had much higher inference latency.
    figure: strict F1 89.33% (DarkBERT-based)
    measures: strict F1 on the authors' 2,100-alert corpus for extraction of eight strategic entity types, best of nine models in 12 configurations
    provenance: independent
    source_ref: ARXIV-2608.14418
  prerequisites:
  - Annotated social-media data for the target taxonomy (ARXIV-2608.14418, abstract).
  risks_and_guardrails:
  - Smaller adapted models can outperform LLMs on narrow extraction, which fits Forrester's 'Principle of Least AI' argument about matching tool
    type to task (ARXIV-2608.14418, abstract; SANS-LEASTAI-2026, abstract).
  human_checkpoints:
  - Not described.
  role_evolution: Not discussed in the sources.
  evidence_grade: D
  sources:
  - ref: ARXIV-2608.14418
    title: 'STINER: Automated Extraction of Strategic Cyber Threat Intelligence from X'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.14418
    date: '2026-08-14'
    access: full
    locator: abstract
  - ref: SANS-LEASTAI-2026
    title: 'Principle of Least AI in Threat Intelligence: A Blueprint for Effective GenAI Adoption (J. Shabadu, Forrester; abstract)'
    publisher: SANS Institute
    type: conference
    url: https://www.sans.org/presentations/principle-of-least-ai-in-threat-intelligence-a-blueprint-for-effective-genai-adoption
    date: '2026-01-27'
    access: full
    locator: abstract
  last_reviewed: '2026-10-17'
  notes: 'Idea (grade D): research benchmark; no operational use found.'
- id: security-threat-intelligence-17
  title: Multi-agent active elicitation of intelligence in underground forums
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - research-synthesis
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Passive monitoring yields less as forum users grow aware of data collection and valuable intelligence moves to private or harder-to-reach
    spaces (ARXIV-2608.23185, abstract).
  solution: 'DarkBot, described by its authors as the first multi-agent LLM system for active CTI elicitation, uses eleven specialized agents:
    engagement gating for relevance and safety, ATT&CK-driven question generation, and linguistic style adaptation (ARXIV-2608.23185, abstract).
    The pattern is an agent that interacts with outside parties, so it is recorded as ''other''.'
  outcomes:
  - lever: quality
    description: Controlled evaluation on forum conversations.
    figure: 72.8% of validated ATT&CK techniques recovered
    measures: share of validated MITRE ATT&CK techniques present in the original discussions that the system recovered across 100 CrimeBB conversations,
      observing only the initial post
    provenance: independent
    source_ref: ARXIV-2608.23185
  - lever: quality
    description: Prospective matched deployment and live conversations.
    figure: 3.85 more CTI entities per thread than controls over seven days; no account suspensions, moderator interventions or explicit accusations
      of automated participation across 104 live conversations
    measures: average additional CTI entities for threads assigned to the system versus matched controls; observed events across 104 live forum
      conversations
    provenance: independent
    source_ref: ARXIV-2608.23185
  prerequisites:
  - 'Layered safety design: the authors report that all injected jailbreak attempts were contained at the pipeline level (ARXIV-2608.23185, abstract).'
  risks_and_guardrails:
  - Legal and ethical boundaries around engaging cybercrime communities are not addressed in the abstract; a practitioner in Feedly's roundup
    says teams rarely discuss real source handling, evaluating reliability and managing long-term adversarial relationships inside clear legal
    and ethical boundaries (FEEDLY-ROUNDUP-2026, Q3 table).
  human_checkpoints:
  - Engagement gating for relevance and safety is a built-in filter; human oversight is not described (ARXIV-2608.23185, abstract).
  role_evolution: Not discussed in the sources.
  evidence_grade: D
  sources:
  - ref: ARXIV-2608.23185
    title: Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.23185
    date: '2026-08-24'
    access: full
    locator: abstract
  - ref: FEEDLY-ROUNDUP-2026
    title: 2026 CTI Practitioners Roundup (14 practitioners; J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/2026-cti-practitioners-roundup
    date: '2026-01-29'
    access: full
    locator: Q3 table, S. O'Connor
  last_reviewed: '2026-10-17'
  notes: 'Idea (grade D): a research system with live experiments run by the researchers; no CTI team adoption found. Described only at the level
    a defender needs.'
- id: security-threat-intelligence-18
  title: Score and prioritize incoming indicators and threat records
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - transaction-processing
  - data-reporting
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Teams ingest more feeds than they can assess; Flashpoint's interviewees rank alert noise and false positives as the top challenge (65%)
    (FLASHPOINT-ENTERPRISE-2026, section 'Operational Challenges Are Putting Pressure on Analyst Capacity').
  solution: Teams use AI to enrich and score intelligence. A secondary summary of the 2025 SANS survey reports more than one-third of teams already
    used AI to enrich and score intelligence (CSB-CTI-2025, section 'CTI on Paper'). Flashpoint's interviewees describe agents handling alert
    prioritization (FLASHPOINT-ENTERPRISE-2026, section 'Agentic AI Adoption Is Underway').
  outcomes:
  - lever: quality
    description: 'Benchmark of eight LLMs on assigning threat levels to records built from public MISP OSINT feeds: zero-shot results were weak,
      and fine-tuned models reached modest scores that the authors call low for practical deployment.'
    figure: fine-tuned F1 0.40 to 0.58
    measures: F1 for threat level determination on a curated dataset derived from public MISP OSINT feeds, eight LLMs fine-tuned versus zero-shot
    provenance: independent
    source_ref: ARXIV-2609.07582
  prerequisites:
  - Data quality and domain adaptation; the authors point to the need for additional research on data quality, model adaptation and domain-specific
    tuning (ARXIV-2609.07582, abstract).
  risks_and_guardrails:
  - 'Overconfidence and inconsistency: a 2025 study of three LLMs on 350 threat reports found they cannot guarantee sufficient performance on
    real-size reports and are inconsistent and overconfident (ARXIV-2503.23175, abstract).'
  - Forrester's analyst says custom risk lists and re-scored prioritization are incremental tuning at best unless they deliver fewer irrelevant
    alerts, faster triage and better resource allocation (FORRESTER-PREDICT-2025, section 'Autonomous Threat Operations').
  human_checkpoints:
  - Not described in the sources.
  role_evolution: Not discussed in the sources.
  evidence_grade: C
  sources:
  - ref: ARXIV-2609.07582
    title: Benchmarking LLMs for Threat Level Determination
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.07582
    date: '2026-09-07'
    access: full
    locator: abstract
  - ref: ARXIV-2503.23175
    title: Large Language Models Are Unreliable for Cyber Threat Intelligence
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2503.23175
    date: '2025-03-29'
    access: full
    locator: abstract
  - ref: CSB-CTI-2025
    title: 'The Reality of CTI: Voices from the Analysts (10 analyst interviews)'
    publisher: Cybersecurity & Business (Substack)
    type: community
    url: https://cybersecandbiz.substack.com/p/the-reality-of-cti-voices-from-the
    date: '2025-09-30'
    access: full
    locator: 'section ''CTI on Paper: A Maturing Discipline'''
  - ref: FLASHPOINT-ENTERPRISE-2026
    title: 'The Enterprise Threat Intelligence Report: 2026 (vendor-commissioned qualitative research, more than 20 interviewees)'
    publisher: Flashpoint
    type: survey
    url: https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/
    date: '2026-10-13'
    access: full
    locator: sections on challenges and agentic AI
  - ref: FORRESTER-PREDICT-2025
    title: 'Recorded Future Predict 2025: Intelligence To Operations ... And Now To Action (J. Shabadu)'
    publisher: Forrester
    type: firm
    url: https://www.forrester.com/blogs/recorded-future-predict-2025-intelligence-to-operations-and-now-to-action/
    date: '2025-10-21'
    access: full
    locator: section on Autonomous Threat Operations
  last_reviewed: '2026-10-17'
  notes: 'The adoption figure is second-hand: the SANS 2025 survey itself was not opened. Evidence on quality is lab-only and negative.'
- id: security-threat-intelligence-19
  title: Scope intelligence to the organization's assets and controls, then open tickets and update detections
  archetype: security
  module: threat-intelligence
  function: technology-it
  work_types:
  - coordination-scheduling
  - research-synthesis
  - software-systems
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Following one inbound vendor report through extraction, ATT&CK mapping, relevance checking against the asset inventory, ticketing and
    notifying leadership can consume a morning (FEEDLY-AUTOMATE-2026, introduction). Cyware's RSAC segment frames the problem as teams collecting
    large volumes of intelligence but struggling to turn it into coordinated operational response (SCWORLD-CYWARE-2026, segment description).
  solution: 'Feedly''s guide chains five prompts and skills in low-code orchestrators (n8n, Tines): extract IOCs, map to ATT&CK, populate the
    Diamond Model and risk view, scope the threat to the CMDB and controls, then draft detections, hunt hypotheses and tickets, with an analyst
    approval step before any write to live tooling (FEEDLY-AUTOMATE-2026, Workflows 1-5). A SANS webcast abstract describes building agents that
    continuously ingest, reason and act, including automatically opening and enriching tickets tied to real exposure (SANS-AGENTICWEB-2026, abstract).
    Cyware''s sponsored segment describes a portfolio of specialized agents across threat intelligence, detection engineering and response, with
    human oversight (SCWORLD-CYWARE-2026).'
  outcomes:
  - lever: speed
    description: Feedly's estimate for scoping a report's threat to assets and controls.
    figure: 35 to 70 minutes (potential)
    measures: Feedly 'Potential time saved' for Workflow 4, against manual steps of 10-20, 20-40 and 30-60 minutes; estimate, no sample
    provenance: vendor-published
    source_ref: FEEDLY-AUTOMATE-2026
  - lever: speed
    description: Feedly's estimate for turning scoped intelligence into rules, hunts, tickets and a leadership note.
    figure: 40 to 85 minutes (potential)
    measures: Feedly 'Potential time saved' for Workflow 5, against manual steps of 20-40, 20-40 and 35-60 minutes; estimate, no sample
    provenance: vendor-published
    source_ref: FEEDLY-AUTOMATE-2026
  prerequisites:
  - An asset inventory or CMDB, a control matrix and ticketing integrations; Feedly rates the scoping and action workflows 'Hard' to build because
    those systems change and integrations break (FEEDLY-AUTOMATE-2026, 'Build versus buy').
  - Cyware's segment lists asset inventory as an input for better threat detection (SCWORLD-CYWARE-2026, chapter 'Using Asset Inventory for Better
    Threat Detection').
  risks_and_guardrails:
  - Chain the low-risk read-only stages first, prove they run reliably, and only then connect stages that act on the environment (FEEDLY-AUTOMATE-2026,
    'Chaining the workflows together').
  - A retail respondent in Flashpoint's interviews would consider only read-only assistants; interviewees' agent tasks range from retrieval to
    blocking IP addresses and updating blacklists (FLASHPOINT-ENTERPRISE-2026, section 'Agentic AI Adoption Is Underway').
  - Automated containment is generally limited to high-confidence, contained actions, with tiered automation for riskier steps (SECURITYWEEK-HUNTING-2026,
    section 'The continuing rise of automation').
  human_checkpoints:
  - Scoping a threat to the environment depends on organizational context a model does not hold, so Feedly requires analyst review there (FEEDLY-AUTOMATE-2026,
    'Where the human analyst is still required').
  role_evolution: Not discussed beyond analyst approval steps.
  evidence_grade: C
  sources:
  - ref: FEEDLY-AUTOMATE-2026
    title: How to automate common CTI workflows (J. D. MacLellan)
    publisher: Feedly TI Essentials
    type: vendor
    url: https://feedly.com/ti-essentials/posts/how-to-automate-common-cti-workflows
    date: '2026-06-12'
    access: full
    locator: introduction; Workflows 4 and 5; 'Build versus buy'
  - ref: SANS-AGENTICWEB-2026
    title: Agentic CTI Automation For Fun and Profit (webcast by R. Brown and J. Cran; abstract only, webcast not viewed)
    publisher: SANS Institute
    type: conference
    url: https://www.sans.org/webcasts/agentic-cti-automation-for-fun-and-profit
    date: '2026-06-25'
    access: full
    locator: abstract
  - ref: SCWORLD-CYWARE-2026
    title: 'Agentic AI and the Future of Threat Intelligence Operations - Sachin Jade - RSAC26 #2 (sponsored by Cyware; segment description and
      chapter titles)'
    publisher: SC Media
    type: podcast
    url: https://www.scworld.com/podcast-segment/14717-agentic-ai-and-the-future-of-threat-intelligence-operations-sachin-jade-rsac26-2
    date: '2026-03-24'
    access: full
    locator: segment description and chapter titles
  - ref: FLASHPOINT-ENTERPRISE-2026
    title: 'The Enterprise Threat Intelligence Report: 2026 (vendor-commissioned qualitative research, more than 20 interviewees)'
    publisher: Flashpoint
    type: survey
    url: https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/
    date: '2026-10-13'
    access: full
    locator: section 'Agentic AI Adoption Is Underway'
  - ref: SECURITYWEEK-HUNTING-2026
    title: 'Cyber Insights 2026: Threat Hunting in an Age of Automation and AI (read through the r.jina.ai text mirror; direct fetch blocked)'
    publisher: SecurityWeek
    type: press
    url: https://www.securityweek.com/cyber-insights-2026-threat-hunting-in-an-age-of-automation-and-ai/
    date: '2026-01-26'
    access: full
    locator: section 'The continuing rise of automation'
  last_reviewed: '2026-10-17'
  notes: Published recipes, a webcast abstract and a sponsored podcast segment; no deployment with named customer or measurement found. The Cyware
    segment audio was not available.
```

## 3. Module notes

### Processes and key steps (with work types)

- **Direction and requirements** (priority intelligence requirements, requests for information, audience definition): `expert-judgment`, `coordination-scheduling`. DTN Advisory argues quality of requirements sets quality of intelligence (`DTN-CTI-2026`); Flashpoint recommends tying new AI-related coverage to existing PIRs (`FLASHPOINT-ENTERPRISE-2026`).
- **Collection** (vendor reports, OSINT, dark web and underground sources, stealer logs, feeds, internal telemetry): `research-synthesis`, `transaction-processing`. Use cases 05 to 08, 16, 17.
- **Processing** (extract, deduplicate, normalize, enrich, translate, put into STIX): `data-reporting`. Use cases 01, 02, 18. The SoK splits "generation and sharing" into extraction, normalization and enrichment, codification and distribution (`ARXIV-2609.01174`).
- **Analysis** (ATT&CK mapping, Diamond Model, attribution, confidence statements, structured analytic techniques): `expert-judgment`. Use cases 02, 12, 14, 15.
- **Reporting and dissemination** (tailored products, briefings, sharing through FIRST, ISACs and TLP-marked channels): `document-production`. Use cases 03, 04, 13.
- **Operationalization** (detections, hunts, blocklists, tickets): `software-systems`, `coordination-scheduling`. Use cases 09, 19.
- **Threat hunting** (trigger, hypothesis, data and query, analysis, finalize and hand off; Intel 471 uses the TaHiTI method): `expert-judgment`, `research-synthesis`. Use cases 10, 11 (`INTEL471-HUNTING-2025`).
- **Feedback and measurement:** `data-reporting`. Practitioners favor decisions influenced, controls implemented and time from intelligence to action over report or IOC counts (`FEEDLY-ROUNDUP-2026`).

### Common pain points

- Alert noise and false positives (65% of Flashpoint respondents), analyst bandwidth (55%), integration gaps (half) (`FLASHPOINT-ENTERPRISE-2026`).
- Lack of time and of funding (44% each) are the top barriers to implementing CTI; most formal CTI teams have fewer than four full-time staff (`SANS-CTIPR-2026`).
- Weak feedback and measurement: 57% of programs do not track maturity over time and 49% gather no systematic effectiveness feedback (`SANS-CTIPR-2026`).
- Influence: 91% of CISOs value CTI but only 26% say it significantly influences their decisions (`SANS-CTIPR-2026`).
- Converting evidence into shareable form is largely manual; 17 of 18 surveyed practitioners cite preventing exposure of sensitive information (`ARXIV-2609.01174`).
- Vendor reports contradict each other because of each vendor's collection bias (`FIRST-CON-2026`, Team Cymru session; `ARXIV-2602.17458`).
- Tactical CTI is neglected and recycled public rules are common, per interviews with 10 analysts (`CSB-CTI-2025`).

### Metrics and benchmarks (with provenance)

- AI use in CTI: 45% of organizations using, 32% planning (401 practitioners, Nov 2025 to Jan 2026; sponsor-supported survey) (`SANS-CTI-2026`). A secondary summary of the 2025 SANS survey says more than one-third of teams used AI to enrich and score intelligence (`CSB-CTI-2025`; SANS 2025 itself not opened).
- Agentic AI: 25% production, 20% piloting, 35% planning in 12 to 24 months, among more than 20 interviewees (`FLASHPOINT-ENTERPRISE-2026`, vendor-commissioned).
- Indicator extraction: 363 to 461 of 1,472 labeled indicators recovered, precision 0.51 to 0.78; ATT&CK technique F1 0.71 to 0.72 and sub-technique 0.66 to 0.67 on sandbox reports (`ARXIV-2609.01174`, independent, preprint).
- Complex report prose: best open model micro F1 0.22 over 2,076 annotated sentences from 83 reports (`ARXIV-2606.18166`).
- Script IOC recovery: 65.4 F1, strongest model, 634 samples (`ARXIV-2609.06149`); encryption severely degrades recovery (`ARXIV-2605.06910`).
- CTI to detection: best normalized reward 0.637 across 16 models; an open-weight model can match the strongest closed models at less than one tenth of the cost with enough turns; message limits are a confound (`ARXIV-2603.13517`, `ARXIV-2610.14180`).
- Threat level determination: fine-tuned F1 0.40 to 0.58 (`ARXIV-2609.07582`).
- Hunting agent in production: about $500/month, about 60% cost saving from using a cheaper model for data gathering, noise about 40% before an adversarial validation phase (`GROWTHERAPY-HUNT-2026`, self-reported).
- Vendor claims (not independent): Google's 98% internal accuracy figure for dark web event analysis (`GOOGLE-DARKWEB-2026`); Feedly's per-report time-saved ranges (`FEEDLY-AUTOMATE-2026`).
- Context for requirements, not defender-AI performance: ENISA's Threat Landscape 2025 (published 2025-10-01) reports, citing other sources, that AI-supported phishing was reportedly more than 80% of observed social engineering activity worldwide by early 2025, and calls the emergence of stand-alone malicious AI systems since the start of 2025 'of particular concern' (`ENISA-ETL-2025`, front-matter summary and section 4.5). Separately: GTIG's disclosures doubled from 5,045 (Jan 2026) to 10,740 (Aug 2026), while only 0.23% of 2026 disclosures were observed exploited; GTIG advises threat-intelligence-driven triage over mass patching (`GTIG-VULNTRENDS-2026`).

### Guardrails and regulatory points

- No regulator or standard-setter statement specific to AI in CTI work was found. The nearest obligations are sharing-related: SANS says 55% of organizations lack legally reviewed CTI sharing processes while NIS2 and the Cyber Resilience Act add obligations in 2026 (`SANS-CTIPR-2026`).
- Practice guardrails: approved-tool list with data classification, AI-use disclosure in a report's methodology section, review of original sources before an assessment is submitted (`FEEDLY-VALUE-2026`); analyst approval between any read stage and any write stage (`FEEDLY-AUTOMATE-2026`); read-only assistants where write permissions are a worry (`FLASHPOINT-ENTERPRISE-2026`); tiered automation, with containment limited to high-confidence cases (`SECURITYWEEK-HUNTING-2026`).
- Source and sharing discipline: DTN Advisory points to Admiralty-style source grading and three audiences (strategic, operational, tactical) (`DTN-CTI-2026`). FIRST marks each conference session with a Traffic Light Protocol label (for example TLP:AMBER for the DFIR-agent manipulation session) (`FIRST-CON-2026`).
- Secure the AI pipeline itself: crafted phishing emails, chat transcripts, incident notes or external reports can steer retrieval and generation in LLM-assisted workflows, and structured forensic data can carry instructions to DFIR agents (`FIRST-CON-2026`, sessions by CyCraft and NTT DATA, 2026-06-18).

### Frontier signals (dated)

- 2026-01-26/27, SANS CTI Summit: Anthropic's cyber threats policy manager gave a keynote on detection systems for AI-enabled adversaries; a Forrester analyst argued for a "Principle of Least AI" (use deterministic tools where they suffice); a Feedly advisor used structured analytic techniques to forecast the CTI industry's future (`SANS-CTISUMMIT-2026`, `SANS-GURU-2026`, `SANS-LEASTAI-2026`, `SANS-FORECAST-2026`).
- 2026-01-29, Feedly roundup: six of 14 practitioners called AI-threat narratives overhyped; seven pointed to neglected basics such as data engineering, HUMINT tradecraft and supply chain visibility (`FEEDLY-ROUNDUP-2026`).
- 2026-02-20, Intel 471: fully autonomous operations by threat actors "has yet to occur"; hallucination is a barrier; "boring" controls and behavioral detection still apply (`INTEL471-AIHUMAN-2026`).
- 2026-03-23/24, launches and RSAC segments: Google's Gemini-based dark web relevance capability (`GOOGLE-DARKWEB-2026`); Cyware's agent portfolio across threat intelligence, detection engineering and response (`SCWORLD-CYWARE-2026`).
- 2026-05-19, SANS CTI survey: SecOps (71%) overtook threat hunting as the leading CTI use case for the first time since 2022 (`SANS-CTIPR-2026`).
- 2026-06-12 and 2026-06-25: Feedly publishes five chained CTI automation workflows (`FEEDLY-AUTOMATE-2026`); SANS runs an "Agentic CTI Automation" webcast (`SANS-AGENTICWEB-2026`).
- 2026-06 (FIRST): sessions on an LLM OSINT copilot, an LLM infostealer forensics tool, vendor data bias in CTI and AI-driven risk assessment of fake job applicants (`FIRST-CON-2026`).
- 2026-07-13, Google GTIG frontline team: "human-machine teaming", judge agents and AI assistants for onboarding (`GOOGLE-DEFADV-HMT-2026`).
- 2026-08-19, packaging knowledge as portable skills: Vega's Detection Skills spec, featured by Detection Engineering Weekly (`DETENGWEEKLY-167-2026`); BSides workshop on building AI skill files for network hunting (`BSIDESLV-2026`).
- 2026-06-10, Forrester's Top Cybersecurity Threats for 2026 lists near-autonomous attacks by nation-states and concerns over agent threats, and tells defenders to prepare for autonomous attacks and adopt agentic security capabilities anchored in trust, cost and utility (`FORRESTER-TOPTHREATS-2026`).
- 2026-09-08, GTIG: adversaries move from prompting to agentic workflows and target AI assets (`GTIG-AITRACKER-2026`).
- 2026-09-30, GTIG: shift from mass patching to threat-intelligence-driven triage (`GTIG-VULNTRENDS-2026`).
- 2026-10-09 to 2026-10-13: open-weight CTI agents compete on cost (`ARXIV-2610.14180`); ATT&CK v20 adds an AI-assisted breach campaign and AI-focused and AI-enabled techniques (`MITRE-ATTCK-2026`); Flashpoint reports AI-related threats as the leading coverage priority for 2027 (`FLASHPOINT-ENTERPRISE-2026`).
- Upcoming: ATT&CKcon 7.0, 2026-10-27/28 (`MITRE-ATTCK-2026`); SANS CTI Summit 2027, 2027-02-01/02, call for presentations closes 2026-10-26 (`SANS-CTISUMMIT-2027`).

### Workforce and role effects

- Routine work absorbed: Feedly says AI is absorbing feed aggregation, indicator enrichment, pattern matching and first-draft summaries; the premium shifts to interpreting meaning, adversarial empathy, communication and validation (`FEEDLY-HIRING-2026`).
- New competence: Feedly defines AI literacy as tool proficiency (building, not just prompting), context engineering and validation, and cites job postings from a major employer that list AI and automation experience (employer's postings not opened) (`FEEDLY-HIRING-2026`).
- De-skilling and pipeline: Feedly's value essay warns of analyst de-skilling, hiring freezes and fewer entry-level roles; a Cybersecurity & Business interviewee says doubt and validation are being exercised less as GenAI advances (`FEEDLY-VALUE-2026`, `CSB-CTI-2025`). Recorded Future's customer panelists said junior analysts would not be replaced but their jobs would look different (`RF-PRACTITIONER-2025`). A Virus Bulletin 2026 session titled around whether CTI agents are friends or rivals to junior analysts exists but only the title was reached (`VB2026-TIPS`, search-only).
- Hunters: several experts quoted by SecurityWeek in January 2026 say AI will augment rather than replace human hunters (`SECURITYWEEK-HUNTING-2026`).
- Capacity: a healthcare TI leader says "we can't hire our way out" (`FLASHPOINT-ENTERPRISE-2026`); most CTI teams are under four people (`SANS-CTIPR-2026`).

### Objections and concerns practitioners raise

- "An agent that's confidently wrong is worse than one that's slow" (`FLASHPOINT-ENTERPRISE-2026`); LLMs lack calibrated confidence and over-attribute (`FEEDLY-VALUE-2026`; `ARXIV-2503.23175`, 350 reports, inconsistent and overconfident).
- AI is rebranding enrichment and summarization as breakthroughs; AI adoption can harm intelligence quality with excess false positives (practitioners quoted in `FEEDLY-ROUNDUP-2026`, Q3 table).
- Sycophancy and confirmation bias in hypothesis work; hives at out-of-the-box AI detection content (`INTEL471-HUNTING-2025`).
- Automation bias and the "productivity trap"; productive friction as a design principle (`INTEL471-AIHUMAN-2026`).
- Black-box vendor triage and unclear validation of "autonomous" features; vanity ROI metrics (`FORRESTER-PREDICT-2025`).
- Hype distracting from basics: "we don't need the AI revolution; we need people that understand security" (an interviewee in `CSB-CTI-2025`).
- Data leakage, auditability, regulatory requirements, cost and permissions (`FLASHPOINT-ENTERPRISE-2026`).
- Attacker-controlled input to AI pipelines (`FIRST-CON-2026`).
- Model-as-data question: a sponsor interview debates whether a sophisticated model or well-structured data matters more for automated SOC work (`RISKYBIZ-855-2026`, sponsor segment; the white paper was not opened).

### Interview probes for an advisor

1. Walk me through one inbound report today: which steps does AI touch, and what review sits between AI output and anything that reaches your TIP, SIEM, ticketing or a stakeholder?
2. What did you measure before turning AI on, and what do you measure now: time per product, decisions influenced, time from intelligence to action, or false-positive and override rates? Who checks the AI's indicators and mappings against source text?
3. How do junior analysts build tradecraft if first drafts, enrichment and mapping are automated? Do analysts still read primary sources, and do reports disclose AI use in their methodology?
4. What permissions would you give an agent: read-only, reversible actions (tickets, tags), or write actions (blocking, rule deployment)? Where do your requirements and asset inventory live in a form an agent could use?
5. How do you handle attacker-controlled content (phishing emails, forum posts, stealer logs) flowing into AI workflows, and what is your legal and privacy review path before AI-assisted intelligence is shared outside the company?

## 4. Routed to other modules

| Item | Target module | Source | Why it belongs there |
|---|---|---|---|
| Tier-1 triage with general-purpose LLMs, CoAnalyst triage framework, OCSF-based AI-assisted IR timelines | operations / incident-response | `FIRST-CON-2026` (sessions 2026-06-18, 2026-06-19, 2026-06-18) | SOC triage and incident timelines, not intelligence production |
| DFIR agents exploited through adversarial manipulation of forensic artifacts (TLP:AMBER session) | incident-response; ai-security | `FIRST-CON-2026` (2026-06-18) | Attack on AI-assisted forensics; the guardrail is cross-referenced in use cases 01 and 07 |
| Prompt injection into SOC and CTI retrieval pipelines via crafted artifacts | ai-security | `FIRST-CON-2026` (CyCraft session) | Security of the AI system itself |
| Vulnerability disclosure doubling (5,045 to 10,740 per month) and the advice to move from mass patching to threat-intelligence-driven triage with agentic remediation | vulnerability-exposure | `GTIG-VULNTRENDS-2026` | Prioritization of patching; CTI supplies exploitation intelligence |
| Adversaries moving to agentic workflows; AI assets as targets; tricking AI coding assistants and LLM scanners in supply chain compromises | ai-security; application-security | `GTIG-AITRACKER-2026` | Attacker capability at defender level; AI supply chain |
| ATT&CK v20 AI-focused and AI-enabled techniques; AI-assisted breach campaign | ai-security (threat model) with CTI as consumer | `MITRE-ATTCK-2026` | Taxonomy for AI-enabled threats |
| Semantic malware ("promptware") and malicious agent skills (ClawHub) | ai-security | `DETENGWEEKLY-163-2026`; `INTEL471-AIHUMAN-2026` | Threats to agent runtimes and skill supply chains |
| DPRK fake-applicant detection stack with AI-driven risk assessment; OSINT checks on fake personas | human-risk; identity-access | `FIRST-CON-2026` (Datadog session 2026-06-17); `BSIDESLV-2026` | Hiring-pipeline and insider risk; intelligence collection is a by-product. Abstract promises 9 months of metrics but none are in the abstract |
| Legal review of CTI sharing, AI-use disclosure policy, tool approval | governance-risk | `SANS-CTIPR-2026`; `FEEDLY-VALUE-2026` | Policy and compliance |
| Detection validation, rule lifecycle and detection-as-code | operations | `DETENGWEEKLY-163-2026`; `DETENGWEEKLY-168-2026` | The intelligence-to-rule step stays in use case 09; the rule pipeline belongs to operations |
| Brand-abuse and phishing takedown case preparation | human-risk (fraud and impersonation) | `MEMCYCO-AGENTIC-2026`; `FORRESTER-PREDICT-2025` | Adjacent to fraud and brand protection; kept as use case 08 because it is an external-threat intelligence product |

## 5. Sources

`access: full` means the page was opened and read (podcast pages: show notes or episode text only, no audio). `search-only` means seen only in a search result. Dates come from byline, article metadata or the schedule where available.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| FIRST-CON-2026 | 38th Annual FIRST Conference program (session abstracts) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06 | full |
| SANS-CTISUMMIT-2026 | A Visual Summary of SANS CTI Summit 2026 (speaker and talk list) | SANS Institute | conference | https://www.sans.org/blog/visual-summary-sans-cti-summit-2026 | 2026-01-26 | full |
| SANS-LEASTAI-2026 | Principle of Least AI in Threat Intelligence: A Blueprint for Effective GenAI Adoption (J. Shabadu, Forrester; abstract) | SANS Institute | conference | https://www.sans.org/presentations/principle-of-least-ai-in-threat-intelligence-a-blueprint-for-effective-genai-adoption | 2026-01-27 | full |
| SANS-GURU-2026 | Keynote: From Theory to Tradecraft: Building Detection Systems to Track AI-Enabled Adversaries (K. Guru, Anthropic; abstract) | SANS Institute | conference | https://www.sans.org/presentations/keynote-from-theory-to-tradecraft-building-detection-systems-to-track-ai-enabled-adversaries | 2026-01-27 | full |
| SANS-FORECAST-2026 | Can We Forecast Our Own Fate? Mapping the Future of the CTI Industry with SATs (J. D. MacLellan, Feedly; abstract) | SANS Institute | conference | https://www.sans.org/presentations/can-we-forecast-our-own-fate-mapping-the-future-of-the-cti-industry-with-sats | 2026-01-27 | full |
| SANS-AGENTICWEB-2026 | Agentic CTI Automation For Fun and Profit (webcast by R. Brown and J. Cran; abstract only, webcast not viewed) | SANS Institute | conference | https://www.sans.org/webcasts/agentic-cti-automation-for-fun-and-profit | 2026-06-25 | full |
| SANS-CTISUMMIT-2027 | SANS Cyber Threat Intelligence Summit & Training 2027 event page (summit 1-2 Feb 2027; call for presentations closes 2026-10-26; page retrieved 2026-10-17, undated) | SANS Institute | conference | https://www.sans.org/cyber-security-training-events/cyber-threat-intelligence-summit-2026/ | 2026-10 | full |
| BSIDESLV-2026 | BSides Las Vegas 2026 talk list (abstracts) | BSides Las Vegas | conference | https://bsideslv.org/talks | 2026-08 | full |
| VB2026-TIPS | TIPS: Harmonizing AI agents and human analysts in CTI - are CTI agents friends or rivals to junior analysts? (T. Kakumaru) | Virus Bulletin | conference | https://www.virusbulletin.com/conference/vb2026/abstracts/tips-harmonizing-ai-agents-and-human-analysts-cti-are-cti-agents-friends-or-rivals-junior-analysts/ | 2026 | search-only |
| GOOGLE-DEFADV-HMT-2026 | Human-Machine Teaming: Applying AI to Frontline Threat Intelligence Workflows (The Defender's Advantage podcast; show notes) | Google Threat Intelligence Group / Mandiant | podcast | https://feeds.buzzsprout.com/1762840.rss | 2026-07-13 | full |
| GOOGLE-DEFADV-DARKWEB-2026 | Using GTI to Hunt Adversaries on the Dark Web (The Defender's Advantage podcast; show notes) | Google Threat Intelligence Group / Mandiant | podcast | https://feeds.buzzsprout.com/1762840.rss | 2026-03-23 | full |
| SCWORLD-CYWARE-2026 | Agentic AI and the Future of Threat Intelligence Operations - Sachin Jade - RSAC26 #2 (sponsored by Cyware; segment description and chapter titles) | SC Media | podcast | https://www.scworld.com/podcast-segment/14717-agentic-ai-and-the-future-of-threat-intelligence-operations-sachin-jade-rsac26-2 | 2026-03-24 | full |
| MEMCYCO-AGENTIC-2026 | MemcycoFM Ep 27: What Is Agentic Threat Intelligence? (vendor podcast, written episode page) | Memcyco | podcast | https://webcast.memcyco.com/library/the-memcycofm-show-ep-27/ | 2026-07-21 | full |
| RISKYBIZ-SOAPBOX109-2026 | Soap Box: Using threat hunting to drive detection (sponsored; Nebulock founder; show notes) | Risky Business Media | podcast | https://risky.biz/SOAPBOX109/ | 2026-07-08 | full |
| RISKYBIZ-855-2026 | Risky Business #855 -- ShinyHunters done sowing, enters reaping phase (show notes, sponsor interview with Corelight) | Risky Business Media | podcast | https://risky.biz/RB855/ | 2026-10-14 | full |
| DETENGWEEKLY-163-2026 | DEW #163 - Semantic Malware Detections, Microsoft's CTI REALM evals and Thrunting for Knowledge | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-163-semantic-malware-detections | 2026-07-15 | full |
| DETENGWEEKLY-167-2026 | DEW #167 - More Security Agentic Breaches, Cheap and Scalable Threat Hunting & Detection Skills | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-167-more-security-agentic-breaches | 2026-08-19 | full |
| DETENGWEEKLY-168-2026 | DEW #168 - The Detection Rule Stork, OpenWeight models vs your SIEM and Sigma vs. YARA | Detection Engineering Weekly | community | https://www.detectionengineering.net/p/dew-168-the-detection-rule-stork | 2026-08-26 | full |
| PACKT-CTIREALM-2026 | #34: CTI-REALM tests whether AI can turn threat intelligence into detections | Packt Cyber_AI newsletter (Substack) | community | https://packtcyberai.substack.com/p/34-cti-realm-tests-whether-ai-can | 2026-10-07 | full |
| CSB-CTI-2025 | The Reality of CTI: Voices from the Analysts (10 analyst interviews) | Cybersecurity & Business (Substack) | community | https://cybersecandbiz.substack.com/p/the-reality-of-cti-voices-from-the | 2025-09-30 | full |
| DTN-CTI-2026 | Your Threat Intelligence Team Is Collecting Data and Calling It Intelligence | DTN Advisory (Substack) | community | https://dtnadvisory.substack.com/p/your-threat-intelligence-team-is | 2026-03-31 | full |
| SECURITYWEEK-HUNTING-2026 | Cyber Insights 2026: Threat Hunting in an Age of Automation and AI (read through the r.jina.ai text mirror; direct fetch blocked) | SecurityWeek | press | https://www.securityweek.com/cyber-insights-2026-threat-hunting-in-an-age-of-automation-and-ai/ | 2026-01-26 | full |
| GROWTHERAPY-HUNT-2026 | Threat hunt AI: How we built an AI security analyst on AWS for under $500/month | Grow Therapy engineering blog | firm | https://engineering.growtherapy.com/post/threat-hunt-ai-how-we-built-an-ai-security-analyst-on-aws-for-under-500-month | 2026-08 | full |
| FORRESTER-PREDICT-2025 | Recorded Future Predict 2025: Intelligence To Operations ... And Now To Action (J. Shabadu) | Forrester | firm | https://www.forrester.com/blogs/recorded-future-predict-2025-intelligence-to-operations-and-now-to-action/ | 2025-10-21 | full |
| FORRESTER-TOPTHREATS-2026 | Announcing Forrester's Top Cybersecurity Threats For 2026 (J. Shabadu) | Forrester | firm | https://www.forrester.com/blogs/announcing-forresters-top-cybersecurity-threats-for-2026/ | 2026-06-10 | full |
| GOOGLE-DARKWEB-2026 | Bringing dark web intelligence into the AI era | Google Cloud Blog | vendor | https://cloud.google.com/blog/products/identity-security/bringing-dark-web-intelligence-into-the-ai-era | 2026-03-23 | full |
| GTIG-AITRACKER-2026 | GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI | Google Threat Intelligence Group | vendor | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai/ | 2026-09-08 | full |
| GTIG-VULNTRENDS-2026 | Vulnerability Discovery and Exploitation Trends in the AI Era | Google Threat Intelligence Group | vendor | https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/ | 2026-09-30 | full |
| INTEL471-HUNTING-2025 | How AI can (and can't) help in threat hunting | Intel 471 | vendor | https://www.intel471.com/blog/how-ai-can-and-cant-help-in-threat-hunting | 2025-09-09 | full |
| INTEL471-AIHUMAN-2026 | How AI and the human advantage beat tomorrow's threats | Intel 471 | vendor | https://www.intel471.com/blog/how-ai-and-the-human-advantage-beat-tomorrows-threats | 2026-02-20 | full |
| FEEDLY-ROUNDUP-2026 | 2026 CTI Practitioners Roundup (14 practitioners; J. D. MacLellan) | Feedly TI Essentials | vendor | https://feedly.com/ti-essentials/posts/2026-cti-practitioners-roundup | 2026-01-29 | full |
| FEEDLY-VALUE-2026 | Quantifying & communicating the value of human-led intelligence in an AI era (A. Streetman) | Feedly TI Essentials | vendor | https://feedly.com/ti-essentials/posts/quantifying-and-communicating-the-value-of-human-led-intelligence-in-an-ai-era | 2026-03-26 | full |
| FEEDLY-AUTOMATE-2026 | How to automate common CTI workflows (J. D. MacLellan) | Feedly TI Essentials | vendor | https://feedly.com/ti-essentials/posts/how-to-automate-common-cti-workflows | 2026-06-12 | full |
| FEEDLY-HIRING-2026 | Hiring for the AI era: A CTI leader's guide to building tomorrow's threat intelligence teams (J. Feyerabend) | Feedly TI Essentials | vendor | https://feedly.com/ti-essentials/posts/hiring-for-the-ai-era-a-cti-leader-s-guide-to-building-tomorrow-s-threat-intelligence-teams | 2026-07-16 | full |
| RF-PRACTITIONER-2025 | Practitioners Reveal What Makes Threat Intelligence Programs Mature (webinar recap; page undated, refers to the 2025 State of Threat Intelligence Report) | Recorded Future | vendor | https://www.recordedfuture.com/blog/practitioner-insights-advancing-threat-intelligence | 2025 | full |
| SANS-CTI-2026 | SANS 2026 Cyber Threat Intelligence Survey Insights (report landing page with takeaways and FAQ; full report not opened) | SANS Institute | survey | https://www.sans.org/research/cyber-threat-intelligence-report | 2026-05 | full |
| FLASHPOINT-ENTERPRISE-2026 | The Enterprise Threat Intelligence Report: 2026 (vendor-commissioned qualitative research, more than 20 interviewees) | Flashpoint | survey | https://flashpoint.io/blog/enterprise-threat-intelligence-report-2026/ | 2026-10-13 | full |
| SANS-CTIPR-2026 | 91% of CISOs Value Cyber Threat Intelligence. Only 26% Say It Drives Their Decisions (press release) | SANS Institute | professional-body | https://www.sans.org/press/announcements/2026-cyber-threat-intelligence-survey-insights-report | 2026-05-19 | full |
| ENISA-ETL-2025 | ENISA Threat Landscape 2025 (89-page PDF, v1.3; read in part) | ENISA | regulator | https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025 | 2025-10-01 | full |
| MITRE-ATTCK-2026 | ATT&CK v20 release (Updates - October 2026) | MITRE | standard-setter | https://attack.mitre.org/resources/updates/ | 2026-10-13 | full |
| ARXIV-2609.01174 | A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing | arXiv | academic | https://arxiv.org/abs/2609.01174 | 2026-09-01 | full |
| ARXIV-2609.06149 | SCRIPTIOC-BENCH: A Benchmark for Recognizing Actionable Threat Intelligence from Script-Based Malware using LLMs | arXiv | academic | https://arxiv.org/abs/2609.06149 | 2026-09-05 | full |
| ARXIV-2605.06910 | Benchmarking Large Language Models for IoC Recovery under Adversarial Code Obfuscation and Encryption | arXiv | academic | https://arxiv.org/abs/2605.06910 | 2026-05-07 | full |
| ARXIV-2606.18166 | Evaluating Open-Source LLMs for Multi-Label ATT&CK Technique Classification on CTI Reports | arXiv | academic | https://arxiv.org/abs/2606.18166 | 2026-06-16 | full |
| ARXIV-2603.13517 | CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities | arXiv | academic | https://arxiv.org/abs/2603.13517 | 2026-03-13 | full |
| ARXIV-2610.14180 | Unconstrained CTI-REALM with Open-Weights | arXiv | academic | https://arxiv.org/abs/2610.14180 | 2026-10-09 | full |
| ARXIV-2604.12228 | From IOCs to Regex: Automating CTI Operationalization for SOC with LLMs | arXiv | academic | https://arxiv.org/abs/2604.12228 | 2026-04-14 | full |
| ARXIV-2609.08790 | Evidence-Grounded Retrieval for Investigation Hunt Lead Generation from CTI Reports | arXiv | academic | https://arxiv.org/abs/2609.08790 | 2026-09-08 | full |
| ARXIV-2609.07582 | Benchmarking LLMs for Threat Level Determination | arXiv | academic | https://arxiv.org/abs/2609.07582 | 2026-09-07 | full |
| ARXIV-2608.28394 | BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2608.28394 | 2026-08-28 | full |
| ARXIV-2602.17458 | The CTI Echo Chamber: Fragmentation, Overlap, and Vendor Specificity in Twenty Years of Cyber Threat Reporting | arXiv | academic | https://arxiv.org/abs/2602.17458 | 2026-02-19 | full |
| ARXIV-2608.14418 | STINER: Automated Extraction of Strategic Cyber Threat Intelligence from X | arXiv | academic | https://arxiv.org/abs/2608.14418 | 2026-08-14 | full |
| ARXIV-2608.23185 | Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums | arXiv | academic | https://arxiv.org/abs/2608.23185 | 2026-08-24 | full |
| ARXIV-2509.23573 | Uncovering Vulnerabilities of LLM-Assisted Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2509.23573 | 2025-09-28 | full |
| ARXIV-2503.23175 | Large Language Models Are Unreliable for Cyber Threat Intelligence | arXiv | academic | https://arxiv.org/abs/2503.23175 | 2025-03-29 | full |

Distinct sources: 55. By type: conference 9, podcast 6, community 6, press 1, firm 3, vendor 10, survey 2, professional-body 1, regulator 1, standard-setter 1, academic 15. Job-posting 0. Vendor-authored sources (flagged `vendor`, plus vendor podcasts, the vendor-commissioned Flashpoint study and vendor-run SANS sponsor content) report their own performance claims, so those figures are labelled `vendor-published`.

## 6. Gaps

- **Independent quality evidence in production:** none found. No published override rates, false-negative rates, parallel-run results or inspection findings for AI in CTI. The only measured named-organization outcome (Grow Therapy) is self-reported; the other numbers are lab preprints (some by the same authors who built the systems), vendor claims or survey shares from unnamed organizations.
- **Search usage:** 7 web searches were used (SANS CTI Summit 2026; SANS CTI survey; Principle of Least AI; CTI podcasts; LLM reliability for CTI; "will AI replace CTI analysts"; a domain-restricted search of CTI vendor and Substack blogs). All other sources were followed by `curl`, `pdftotext` or the `r.jina.ai` mirror.
- **Blocked or not reached:** Black Hat USA 2025 and 2026 briefing schedules (403; mirror returned an empty template); RSAC and Gartner session lists; Gartner and Forrester paid research (only public blogs read); Virus Bulletin 2026 abstract (Cloudflare; only title and speaker reached, so `VB2026-TIPS` is search-only and the NEC affiliation comes from a search snippet and is unverified); SecurityWeek direct fetch (read through the mirror); CISA's IMX repository (403); Reddit (blocked); Hacker News (searched, only Show HN posts, nothing usable); Medium and BleepingComputer (not attempted or blocked).
- **Not opened or only second-hand:** the full SANS 2026 CTI Survey report and the SANS 2025 CTI survey (figures for 2025 are via `CSB-CTI-2025`); SANS summit slide decks (abstracts only); the Microsoft CTI-REALM primary announcement (arXiv and two secondary summaries used); Mandiant M-Trends 2026, CrowdStrike Global Threat Report and Threat Hunting Report (gated landing pages); the Corelight white paper mentioned in a Risky Business sponsor segment; Feedly's prompt-library pieces beyond the four cited; Unit 42, MITRE ATLAS and CISA advisories listed as landscape leads.
- **Podcasts:** show notes or written episode pages only for Google's Defender's Advantage, Risky Business, Cyware at RSAC and Memcyco. No audio or transcripts, so no claim goes beyond the descriptions. Cyware and Memcyco are vendor-sponsored or vendor-produced.
- **Dates not on the page:** Grow Therapy post (2026-08 inferred because Detection Engineering Weekly featured it on 2026-08-19); Recorded Future practitioner recap (year 2025 inferred from the report it cites); Virus Bulletin 2026 session; SANS CTI survey landing page (dated by its 2026-05-19 press release); FIRST and BSides entries carry month-level dates only.
- **Not found:** job postings that show real AI use in CTI roles (Feedly's claim about a major employer's postings was not verified); ISAC-specific practice on AI-assisted sharing; regulator or standard-setter statements specific to AI in CTI; independent accounts of small and mid-size teams; non-US and non-EU practice; defender-side data on CTI-team staffing changes caused by AI.
- **Vendor-heavy discourse:** many practitioner voices come from vendor blogs and sponsored podcasts (Feedly, Intel 471, Flashpoint, Google, Recorded Future, Cyware, Memcyco). Independent voices are the Forrester analyst, SecurityWeek's expert panel, newsletters, in-house engineering blogs and the academic papers.
- **Terminology anomaly** flagged in the landscape file ("Super Intelligence" replacing "AI" on some CISA and NIST pages) was not encountered in any source read here.
