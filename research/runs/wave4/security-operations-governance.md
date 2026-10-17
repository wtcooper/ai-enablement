# Security operations: governance and evidence (wave 4 deep dive)

Archetype: security. Module: operations (SOC: detection engineering, alert triage, investigation, case management, MDR). Angle: governance (regulators, standard-setters, academic studies, surveys, benchmarks). Compiled 2026-10-17. Source refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape file's refs where the document is the same.

## 1. Summary

- **Scope of work.** 19 candidate use cases (evidence grades: A 2, B 2, C 10, D 5) and 63 sources (regulator 14; standard-setter 4; professional-body 3; survey 4; academic 26; conference 2; vendor 5; press 5). All were opened and read except `SIFMA-SEC-2026`, which was seen only in search results and is marked `search-only`.
- **What the governance material says.** Where the sources speak to SOC use (mainly the NCSC), the consistent message is: let AI prepare, summarise and recommend, and keep people or deterministic, tested automation in control of actions that can disrupt the business. The NCSC turns this into a scoring scheme for defensive actions (`NCSC-AGENTICDEF-2026`) and an interim control list for agents (`NCSC-AGENTICRISK-2026`); CISA with Australia's ACSC issued joint agentic-AI guidance on 2026-05-01 (`CISA-AGENTIC-2026`); the US federal logging memo sets a measurable data foundation for the SOC (`OMB-M2614-2026`). I found no regulator that sets AI-specific SOC performance thresholds.
- **What the measurement material says.** Independent measurement of AI in the SOC is thin. The one randomised comparison with human analysts is simulated and vendor-involved (`CSA-SOCBENCH-PR-2025`: 148 participants, 45-61% faster, 22-29% more accurate). Peer-reviewed or preprint benchmarks show large misses (every approach tested on ALERT-BENCH missed at least 40.4% of attack-related alerts, `ARXIV-2610.10608`) and show LLM log analysis is open to log-borne injection (up to 88.2% attack success at baseline, `USENIX-LOGINJECT-2026`). The Cisco/Splunk live agentic SOC published activity metrics but no accuracy or override rate (`CISCO-SPLUNK-CONF26-2026`).
- **Adoption versus embedding.** SANS 2026: 79% of SOCs use AI or ML tools, 36% have built them into a defined workflow, and 70% still cite incident count as their top SOC metric (`SANS-SOC-2026`).
- **Corrections to the landscape file** are listed in section 3.9. The main one: the 9+ analyst hours saved at the RSAC 2026 SOC came from a deterministic SOAR playbook, not from AI.

## 2. Use cases

Grades: A = measured outcome from a named organisation; B = named deployment without published measurement; C = vendor/analyst claim or research result without a named deployment; D = idea (labelled), discussed by practitioners, regulators or researchers. Several grade-C entries are academic results; they are independent of a vendor but are not live-SOC measurements.

```yaml
- id: security-operations-01
  title: Triage agent prepares a suggested disposition for each queued finding; an analyst decides
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - transaction-processing
  - research-synthesis
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: Analysts spend first-level triage time gathering context for each queued finding before they can decide whether to close, escalate or investigate it.
  solution: 'An agent inside the SIEM investigates findings as they appear in the analyst queue: it gathers context, runs searches and threat-intelligence lookups, and returns a suggested disposition, rationale and recommended next steps. A tiered analyst team reviews the evidence and decides. Cisco describes the same pattern for Tier 1 in its CoAnalyst framework, which combines an LLM with historical incident data and existing security tools.'
  outcomes:
  - lever: capacity
    description: Activity and coverage of the Triage Agent over the whole .conf26 event SOC (event-environment observations, which the post says are not product benchmarks). The post publishes no agreement-with-analyst or miss rate.
    figure: 94% triage analysis coverage; 1,503 AI agentic events; 7,605 SPL queries generated and run; 26,207 pieces of evidence considered; 11,250 threat-intelligence lookups
    measures: '''Triage analysis coverage'' as shown on the displayed operations dashboard for the entire .conf26 conference including setup days; the post does not define the numerator and denominator further'
    provenance: vendor-published
    source_ref: CISCO-SPLUNK-CONF26-2026
  - lever: quality
    description: Distribution of the agent's suggested dispositions and of finding status on the same dashboard snapshot. These describe what the agent suggested, not whether it was right.
    figure: 'Suggested dispositions: True Positive 44%, Benign Positive 42%, No suggestion 7%, False Positive 6%, Undetermined 1%. Finding status: Closed 51%, New 37%, Pending 7%, In Progress 5%'
    measures: 'Share of findings by suggested disposition and by status in the dashboard snapshot (scope: entire conference); no ground-truth comparison is reported'
    provenance: vendor-published
    source_ref: CISCO-SPLUNK-CONF26-2026
  prerequisites:
  - Normalised, correlated and enriched telemetry in one analyst workspace (here Splunk Enterprise Security with Cisco, Endace and convention-centre data)
  - A way to measure the agent from the same data it works on (the post built an operations dashboard in an afternoon)
  - A tiered analyst team plus detection engineers able to validate results and tune content
  risks_and_guardrails:
  - The post frames the principle as agents prepare the work and people inspect the evidence and decide; the Splunk RSAC SOC post says AI is decision support, not an accountability replacement.
  - 'Event SOC with temporary, highly dynamic traffic: activity that would alarm on a corporate network can be normal there, so results do not transfer directly to an enterprise SOC.'
  - No accuracy, false-negative or override rate was published, so the tool's reliability is not evidenced by this source.
  human_checkpoints:
  - Analyst reviews the suggested disposition, rationale and underlying data before closing, escalating, investigating further or acting
  - Detection engineers tune content from what analysts learn
  role_evolution: Tier 1 analysts review agent-prepared findings rather than gather context themselves; Tier 2 and Tier 3 handle complex findings and hunting; detection engineers tune detections from the feedback (Cisco .conf26 post).
  evidence_grade: B
  sources:
  - ref: CISCO-SPLUNK-CONF26-2026
    title: 'Splunk .conf26: Tracking the Triage Agent in the Agentic SOC'
    publisher: Cisco Blogs (Cisco and Splunk)
    type: vendor
    url: https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/
    date: '2026-10-08'
    access: full
    locator: Sections 'A blended analyst team', 'Building the Triage Agent Dashboard in an Afternoon', Dashboard Snapshot table
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program agenda and session abstracts (Denver, 14-19 June 2026)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: 'Session ''CoAnalyst: An AI-Driven Framework for Enhanced SOC Triage'' (Cisco), abstract; no figures in the abstract'
  - ref: SPLUNK-RSACSOC-2026
    title: 'From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC'
    publisher: Splunk
    type: vendor
    url: https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html
    date: '2026-08-24'
    access: full
    locator: 'Closing list of patterns: ''Treat AI as decision support, not an accountability replacement'''
  last_reviewed: '2026-10-17'
  notes: Maturity is 'piloting' because the deployment was a temporary conference SOC, not a standing enterprise SOC. The agent is the Splunk Enterprise Security AI Triage Agent (vendor product). CoAnalyst session content was not available beyond the abstract.
- id: security-operations-02
  title: AI investigation platform assists analysts on escalated alerts (randomised comparison against manual work)
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - research-synthesis
  - document-production
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Analysts investigating escalated alerts must pull evidence from several tools and write up findings, and report quality can decline over repeated investigations.
  solution: An AI SOC analyst platform (Dropzone AI) performs the investigation steps and drafts the conclusions; the analyst reviews and finalises. The CSA study measured analysts with and without the platform on two escalated alert scenarios.
  outcomes:
  - lever: speed
    description: AI-assisted analysts completed the escalated investigations faster than manual analysts in both scenarios.
    figure: 45% faster (scenario 1, AWS S3 bucket alert); 61% faster (scenario 2, Microsoft Entra ID failed login alert)
    measures: Investigation completion time of AI-assisted versus manual participants per scenario; 148 participants randomly assigned (study run July-August 2025)
    provenance: vendor-published
    source_ref: CSA-SOCBENCH-PR-2025
  - lever: quality
    description: AI-assisted analysts scored higher against expert-modelled ideal responses.
    figure: 22% greater accuracy (scenario 1); 29% greater accuracy (scenario 2)
    measures: Accuracy score of AI-assisted versus manual participants per scenario, scored against expert-modelled 'ideal responses'
    provenance: vendor-published
    source_ref: CSA-SOCBENCH-PR-2025
  - lever: quality
    description: Manual analysts' written detail fell over the session while AI-assisted analysts maintained or slightly increased theirs.
    figure: 'Manual analysts: report detail down 27%, conclusion detail down 20%'
    measures: Change in detail scores of manual participants over the study, as stated in the press release
    provenance: vendor-published
    source_ref: CSA-SOCBENCH-PR-2025
  prerequisites:
  - Alert and telemetry access for the platform
  - Expert-modelled ideal responses are needed to score analyst and AI output if you want to repeat this kind of test
  risks_and_guardrails:
  - Simulated scenarios, two escalated alert types only; not live production alerts and not tier-1 volume triage.
  - The platform is the sponsor's product; Dropzone is a CSA corporate member and CSA states Dropzone had no influence on content, but the press release is co-announced by both.
  - Participants used the tool for the first time; long-term effects and false-negative rates in production are not measured.
  - NCSC advises that judge or helper models be independently evaluated and that named individuals own agent activity (see use case 9).
  human_checkpoints:
  - Analyst reviews the platform's investigation and conclusion before it is recorded
  role_evolution: Analysts spend less time collecting evidence and writing it up; the study reports that 94% of participants said their view of AI in cybersecurity became more positive after hands-on use (CSA report page).
  evidence_grade: A
  sources:
  - ref: CSA-SOCBENCH-PR-2025
    title: New Study from Cloud Security Alliance Finds AI Improves Analyst Accuracy, Speed, and Consistency in Security Investigations (press release)
    publisher: Cloud Security Alliance
    type: survey
    url: https://cloudsecurityalliance.org/press-releases/2025/10/07/new-csa-study-finds-ai-improves-analyst-accuracy-speed-and-consistency-in-security-investigations
    date: '2025-10-07'
    access: full
    locator: Paragraphs on study design, key findings (accuracy, speed, completeness) and methodology (148 participants, July-August 2025)
  - ref: CSA-SOCBENCH-2025
    title: 'Beyond the Hype: A Benchmark Study of AI Agents in the SOC (report landing page)'
    publisher: Cloud Security Alliance
    type: survey
    url: https://cloudsecurityalliance.org/artifacts/a-benchmark-study-of-ai-agents-in-the-soc
    date: '2025-10-06'
    access: full
    locator: 'Report summary: 94% of participants said their view of AI became more positive after hands-on use'
  last_reviewed: '2026-10-17'
  notes: Only controlled (randomised) comparison with human analysts found in this scan. The 'in-production' maturity rests on the vendor's own boilerplate (customer count and names), which was not verified. Grade A reflects a measured outcome by a named organisation, with simulation and sponsor caveats above.
- id: security-operations-03
  title: Replay-benchmark acceptance testing of SOC AI before go-live and after each model or prompt change
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: SOCs adopting triage and investigation agents lack agreed ways to measure whether the agent misses attacks; practitioners say measured evidence of where such systems succeed and fall short is scarce.
  solution: 'Replay recorded or synthetic alert and incident sets with expert-validated ground truth through the candidate agent, score triage accuracy, missed attacks and investigation quality, and repeat after changes. Public benchmarks (ALERT-BENCH, SIABench, SIR-Bench, CyberSOCEval) and a FIRST controlled experiment are the available examples. Pattern is ''other'': an evaluation harness.'
  outcomes:
  - lever: risk
    description: On ALERT-BENCH every studied triage approach missed a large share of attack-related alerts in a replayed multi-stage attack, showing why pre-deployment testing matters.
    figure: At least 40.4% of attack-related alerts missed by every approach tested
    measures: Attack-related alerts missed, out of the attack-related alerts among 1,247 alerts from a multi-stage attack scenario replayed through a live SIEM; five approaches compared
    provenance: independent
    source_ref: ARXIV-2610.10608
  - lever: quality
    description: Authors' own incident-response agent on SIR-Bench (794 test cases from 129 anonymised incident patterns).
    figure: 97.1% true-positive detection; 73.4% false-positive rejection; 5.67 novel key findings per case
    measures: True positives detected, false positives rejected, and novel findings per case on SIR-Bench; scored with an adversarial LLM-as-judge; agent built by the benchmark's authors
    provenance: independent
    source_ref: ARXIV-2604.12040
  prerequisites:
  - Labelled alert and incident history, or synthetic scenarios, with expert-validated ground truth
  - Telemetry replay into a real or test SIEM
  - Someone accountable for acceptance thresholds
  risks_and_guardrails:
  - Benchmarks use replayed or synthetic data; the SIR-Bench scores come from the authors' own agent and an LLM judge.
  - SIABench frames the problem as the absence of rigorous benchmarking creating risk when organisations adopt LLMs for incident analysis.
  - A FIRST 2026 talk reports early findings from an ongoing controlled experiment and promises 'an honest view' of limits (abstract only).
  human_checkpoints:
  - Experts validate ground truth and review failure traces
  - Go/no-go decision on autonomy level uses the benchmark results
  role_evolution: 'Detection engineers or SOC engineers add an evaluation role: curating replay sets and owning acceptance thresholds for agents.'
  evidence_grade: C
  sources:
  - ref: ARXIV-2610.10608
    title: 'From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.10608
    date: '2026-10-06'
    access: full
    locator: 'Abstract: ALERT-BENCH, 1,247 alerts, every approach missed at least 40.4% of attack-related alerts'
  - ref: ARXIV-2604.12040
    title: 'SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2604.12040
    date: '2026-04-13'
    access: full
    locator: 'Abstract: 794 test cases, 97.1% TP detection, 73.4% FP rejection'
  - ref: ARXIV-2603.06422
    title: 'Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis (SIABench)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2603.06422
    date: '2026-03-06'
    access: full
    locator: 'Abstract: SIABench, 25 deep-analysis scenarios and 135 alert-triage scenarios, 11 LLMs benchmarked'
  - ref: ARXIV-2509.20166
    title: 'CyberSOCEval: Benchmarking LLMs Capabilities for Malware Analysis and Threat Intelligence Reasoning'
    publisher: arXiv (released within Meta CyberSecEval 4)
    type: academic
    url: https://arxiv.org/abs/2509.20166
    date: '2025-09-24'
    access: full
    locator: 'Abstract: open-source benchmarks for malware analysis and threat-intelligence reasoning; current LLMs far from saturating them'
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program agenda and session abstracts (Denver, 14-19 June 2026)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: Session 'Can a General-Purpose LLM Do Tier-1 Triage?' (TandemTrace), abstract
  last_reviewed: '2026-10-17'
  notes: 'Grade C: academic benchmark results and a conference abstract; no named SOC reports using a benchmark as a formal acceptance gate. Benchmarks are independent of the deploying SOC but are not live-production measurement.'
- id: security-operations-04
  title: Adversarial challenge and judge before an agent may dismiss an alert
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - transaction-processing
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Single-pass triage agents tend to dismiss attack alerts when searches return nothing, and self-review in the same context can make decisions worse.
  solution: Require an explicit proposed decision, then an independent challenge in a separate reasoning context and a judge that weighs both against evidence, with stronger evidence required before dismissal and an append-only investigation ledger. CORTEX proposes a related multi-agent split between behaviour analysis, evidence gathering and a reasoning agent that produces an auditable decision.
  outcomes:
  - lever: risk
    description: AIDA reduced false negatives on the same replayed alerts while escalating a minority of alerts to analysts.
    figure: False-negative rate 40.4% to 3.1%; F1 0.958 versus 0.371-0.744 for the studied approaches; 18.4% of alerts escalated to analysts
    measures: Attack-related alerts missed / attack-related alerts, and F1, on 1,247 alerts from one multi-stage attack scenario in ALERT-BENCH; method and benchmark built by the same authors
    provenance: independent
    source_ref: ARXIV-2610.10608
  - lever: quality
    description: CORTEX claims fewer false positives and better investigation quality than single-agent baselines; the abstract gives no figures.
    figure: none published
    measures: Not stated in the abstract
    provenance: independent
    source_ref: ARXIV-2510.00311
  prerequisites:
  - Benchmark or replay set to show the dismissal bar works
  - Evidence-retrieval tools with logging so a challenger can re-check
  - Analyst capacity to take the escalated share
  risks_and_guardrails:
  - Results come from one replayed attack scenario; the authors designed both method and benchmark.
  - Trace analysis in the paper finds same-context self-review has negative net correction and dismissal receives no consistently stronger investigation than escalation, which is the control gap this design targets.
  - Escalating 18.4% of alerts still needs analyst capacity.
  human_checkpoints:
  - Analysts handle escalated alerts; the judge's reasoning and ledger are reviewable
  role_evolution: Analysts become reviewers of contested decisions; engineers own thresholds for what counts as enough evidence to dismiss.
  evidence_grade: C
  sources:
  - ref: ARXIV-2610.10608
    title: 'From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.10608
    date: '2026-10-06'
    access: full
    locator: 'Abstract: AIDA, F1 0.958, false-negative rate 40.4% to 3.1%, 18.4% escalated'
  - ref: ARXIV-2510.00311
    title: 'CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2510.00311
    date: '2025-09-30'
    access: full
    locator: 'Abstract: multi-agent architecture and released dataset of production SOC investigations'
  last_reviewed: '2026-10-17'
  notes: Research prototype; no named SOC deployment.
- id: security-operations-05
  title: Threshold-gated auto-closure of low-risk alerts, with analyst feedback updating the agent
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - transaction-processing
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Most alerts are benign, and analysts cannot triage the daily volume, so true detections can wait while benign alerts are reviewed by hand.
  solution: 'Let an agent or classifier close only the alerts it judges benign at a stated confidence, keep recall as a hard constraint, and feed analyst dispositions back so the agent keeps up with organisation-specific standards. REFINE encodes analyst expertise as structured skills and treats recall of 1.0 as a constraint during evolution; a reasoning triage classifier adds a trained calibrator so the confidence used for automation is reliable. A vendor panel on the SANS AI survey describes the same sequence: start with false positives and low-severity noise.'
  outcomes:
  - lever: risk
    description: REFINE kept recall at 1.0 on all evolution sets and on future test windows in three of four scenarios.
    figure: Recall 1.0 on all evolution sets; recall 1.0 in 3 of 4 future-window scenarios; degraded case 0.807 versus 0.49-0.58 for self-evolution baselines
    measures: Recall (attack alerts caught / attack alerts) in four real industrial SOC scenarios across four MITRE ATT&CK phases, temporal train/test split; organisations not named
    provenance: independent
    source_ref: ARXIV-2609.32516
  - lever: quality
    description: Trained reasoning classifier on real human-labelled Windows endpoint detections.
    figure: 82.6% test accuracy; at the high-confidence operating point benign recall up 43.0% and malicious recall up 18.3% over a direct-label LLM classifier
    measures: Accuracy on a test set; recall differences at the operating point that governs automated triage; an untrained confidence judge collapsed high-confidence recall to zero
    provenance: independent
    source_ref: ARXIV-2607.28460
  prerequisites:
  - Analyst-labelled history to train and calibrate
  - A confidence calibrator and a recall floor agreed with the SOC lead
  - A path for analysts to override closures and feed corrections back
  risks_and_guardrails:
  - Degraded recall in one REFINE scenario (0.807) shows closures drift on future windows without monitoring.
  - SANS AI survey (as summarised by Swimlane) reports automated incident response at 39% adoption and 63% reporting significant AI shortcomings in detecting or responding to threats.
  - Closing alerts removes them from analyst view, so sampling of closures is the main safeguard (see use case 16).
  human_checkpoints:
  - Sampling review of auto-closed alerts
  - Analyst override and disposition feedback
  - Review of recall on rolling windows
  role_evolution: Tier 1 analysts shift from clearing benign volume to teaching and auditing the agent through dispositions.
  evidence_grade: C
  sources:
  - ref: ARXIV-2609.32516
    title: 'REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2609.32516
    date: '2026-09-26'
    access: full
    locator: 'Abstract: recall=1.0 hard constraint; four real industrial SOC scenarios; 0.807 degraded case'
  - ref: ARXIV-2607.28460
    title: Cybersecurity Detection Classification with Reasoning-enabled Language Models
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.28460
    date: '2026-07-30'
    access: full
    locator: 'Abstract: 82.6% test accuracy; benign recall +43.0%, malicious recall +18.3%; calibrator necessary'
  - ref: SANS-AI-2026
    title: A SOC Leader's Guide to the 2026 SANS AI Survey (vendor blog summarising the SANS AI Survey; the survey itself was not opened)
    publisher: Swimlane
    type: vendor
    url: https://swimlane.com/blog/sans-ai-2026-soc-trust/
    date: '2026-05-18'
    access: full
    locator: Sections 'Where Automation Actually Earns Trust' and 'Trust Requires Context'; 39% automated incident response adoption and 63% shortcomings as reported by the vendor
  - ref: ARXIV-2505.06394
    title: Towards AI-Driven Human-Machine Co-Teaming for Adaptive and Agile Cyber Security Operation Centers
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2505.06394
    date: '2025-05-09'
    access: full
    locator: 'Abstract: vision of LLM agents learning tacit SOC knowledge from analysts; invites SOCs to collaborate; no results reported'
  last_reviewed: '2026-10-17'
  notes: Both papers are academic/industrial research; no named SOC in production. The 63% / 37% reading comes from Swimlane's post, which infers 37% 'trust' from the 63% figure; the SANS survey itself was not opened.
- id: security-operations-06
  title: Automated attack investigation by iterative query-and-filter backtracking over provenance data
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: Provenance-based investigation breaks down in practice through dependency explosions and missing events, leaving thousands of alerts a day for manual triage even with LLM-based workflows in place.
  solution: SherAgent lets an LLM iteratively query, filter and select nodes over a provenance graph, widening the search where events are missing, to find an incident's root cause.
  outcomes:
  - lever: quality
    description: Investigation success compared with the SOC's legacy enterprise baseline and a state-of-the-art approach, in the wild.
    figure: End-to-end investigation success up 31.1% versus legacy enterprise baselines and 63.7% versus state-of-the-art approaches
    measures: Relative improvement in end-to-end investigation success rate in evaluations at the SOC of a major Internet corporation (not named)
    provenance: independent
    source_ref: ARXIV-2607.09176
  - lever: cost
    description: Per-investigation cost and time reported by the authors.
    figure: Under $0.10 in API costs; under 4 minutes per investigation
    measures: Per-investigation API cost and time, as stated in the abstract
    provenance: independent
    source_ref: ARXIV-2607.09176
  prerequisites:
  - Provenance or audit-log data collected in a graph form
  - Access to the SOC's existing LLM investigation workflow for baseline
  risks_and_guardrails:
  - Evaluated with one unnamed SOC; the user study is described only as confirming clear insights.
  - Provenance queries run by an LLM over untrusted data inherit the injection risks in use case 7.
  human_checkpoints:
  - Security experts review the root-cause findings
  role_evolution: Investigators receive a candidate attack chain to verify rather than building it from alerts.
  evidence_grade: C
  sources:
  - ref: ARXIV-2607.09176
    title: 'SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2607.09176
    date: '2026-07-10'
    access: full
    locator: 'Abstract: collaboration with the SOC of a major Internet corporation; +31.1% / +63.7%; <$0.10 and <4 minutes; user study'
  last_reviewed: '2026-10-17'
  notes: Grade C because the organisation is not named.
- id: security-operations-07
  title: 'Treat log and artifact content as adversarial input to SOC copilots: filtering, prompt hardening and output validation'
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - software-systems
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Many log fields (user agents, URLs, DNS queries, usernames) are attacker controlled, so an LLM that summarises or triages them can be told what to say about the intrusion that produced them.
  solution: 'Design SOC copilots on the assumption that raw log content is hostile: filter inputs, harden prompts, constrain and validate outputs, limit what the model can do, and keep a human on security-critical decisions. FIRST 2026 sessions from NTT DATA and CyCraft show the same risk in DFIR agents and retrieval-based triage.'
  outcomes:
  - lever: risk
    description: 'LogInject on three production LLMs: baseline attack success, and effect of layered defences.'
    figure: Up to 88.2% attack success (83.4% average across models) at baseline; layered defences cut attacks by 90.4% with 8.4% residual
    measures: 'Attack success rate over LogInject-1.0 (12,847 log entries including 2,569 adversarial samples) across four objectives: concealment, false-positive generation, exfiltration, output hijacking'
    provenance: independent
    source_ref: USENIX-LOGINJECT-2026
  - lever: risk
    description: 'Poisoning the Watchtower on gpt-4o-mini as analyst: injection success without and with strongest defence; summarisation worst.'
    figure: Average injection success 26.6% (naive prompting) to 11.8% (strongest defence); context manipulation 96% success on summarisation without defences, 38% with constrained output; persona hijack suppressed 68% of malicious logs under a naive classifier
    measures: Injection success across 48 strategy-defence-task combinations; suppression = malicious logs mislabelled benign under a naive classifier
    provenance: independent
    source_ref: ARXIV-2605.24421
  prerequisites:
  - Inventory of untrusted fields that reach the model
  - Red-team test set of log-borne injections
  - Least-privilege tool access for the model
  risks_and_guardrails:
  - Defences reduce but do not eliminate the risk (8.4% residual in LogInject; 11.8% in the other study).
  - The USENIX paper concludes defence in depth and continued human oversight are required for security-critical decisions.
  - Simulation mispredicted real model behaviour in the arXiv study, so tests need live models.
  human_checkpoints:
  - Human verification for security-critical outputs
  - Periodic injection red-teaming of triage and summarisation prompts
  role_evolution: Detection and SOC engineers add adversarial testing of their own AI tooling to the job.
  evidence_grade: C
  sources:
  - ref: USENIX-LOGINJECT-2026
    title: 'Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation (Karanjai et al.)'
    publisher: USENIX Security 2026
    type: academic
    url: https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai
    date: 2026-08
    access: full
    locator: 'Abstract: LogInject, up to 88.2% (83.4% average), 90.4% reduction, 8.4% residual'
  - ref: ARXIV-2605.24421
    title: 'Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2605.24421
    date: '2026-05-23'
    access: full
    locator: 'Abstract: 26.6% to 11.8%; 96% and 38%; 68%'
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program agenda and session abstracts (Denver, 14-19 June 2026)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: 'Sessions ''The Dark Side of Autonomy: Exploiting DFIR Agents Through Adversarial Manipulation'' (NTT DATA) and ''One Poisoned Artifact Can Steer Your AI'' (CyCraft AI Lab), abstracts'
  last_reviewed: '2026-10-17'
  notes: Attack technique is described only at the level defenders need; no payloads are recorded here. Primarily an ai-security topic, kept here because it governs how operations teams may use LLMs on logs.
- id: security-operations-08
  title: 'Constrained-action remediation: closed intent vocabulary, argument validator and guardrail proxy between the SOC AI and endpoints'
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - software-systems
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: If an LLM can issue block, kill or quarantine commands, a single adversarial alert can become a remote code path through the model's reasoning.
  solution: Confine the model's output to a closed set of intents whose templated commands are run by thin endpoint agents behind an argument validator, and wrap the analyst LLM in a guardrail proxy with input and output rails; run the loop human-in-the-loop or delayed.
  outcomes:
  - lever: risk
    description: Stock guardrail proxy on a SOC-specific adversarial corpus released by the authors.
    figure: Injection recall 25.0% to 94.5% at a 0.1% false-positive rate
    measures: Injection recall (adversarial alerts flagged) and false-positive rate for the proxy on the authors' SOC adversarial corpus; a live red-team exercise reported containment of observed failure modes
    provenance: independent
    source_ref: ARXIV-2610.09906
  prerequisites:
  - SIEM/XDR control plane that correlates host events
  - Defined list of permitted remediation intents and argument checks
  - Endpoint agents that execute templates only
  risks_and_guardrails:
  - The authors state the measured rail latency keeps inline control out of scope, so the loop is best run human-in-the-loop or delayed.
  - Fit for operational technology is described as architectural, not a measured OT deployment.
  human_checkpoints:
  - Human approval or delay window before commands execute
  role_evolution: SOC engineers curate the permitted action vocabulary; analysts approve actions.
  evidence_grade: C
  sources:
  - ref: ARXIV-2610.09906
    title: Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.09906
    date: '2026-10-07'
    access: full
    locator: 'Abstract: closed intent vocabulary, argument validator, NeMo Guardrails proxy, 25.0% to 94.5% at 0.1% FPR, human-in-the-loop or delayed'
  last_reviewed: '2026-10-17'
  notes: Research prototype.
- id: security-operations-09
  title: 'Risk-tiered autonomy policy for defensive actions: score each automated action before allowing it to run unattended'
  archetype: security
  module: operations
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Defensive automation is limited by organisational risk (a wrong block can take down the business) more than by technical capability, and teams lack a shared way to decide which actions an agent may take alone.
  solution: Score each candidate automation on potency (advice only to code execution), scope, criticality, rollout confidence and recoverability, start with low-potency advise-a-human actions, and choose human-in-the-loop, on-the-loop or out-of-the-loop per action. The NCSC proposes the scoring dimensions; an academic framework maps five autonomy levels to human roles and trust thresholds across monitoring, detection, triage and response.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No measurement published; the NCSC framework is a proposal and the survey figures below describe attitudes only
    provenance: independent
    source_ref: NCSC-AGENTICDEF-2026
  - lever: risk
    description: Arctic Wolf survey (vendor, MDR provider) on trust in autonomous action, as reported by a news summary.
    figure: 14% say AI is central to their security-operations strategy; 53% trust AI even for narrowly defined actions such as blocking a malicious IP at a firewall
    measures: Share of 1,350 security and IT decision-makers (Sapio Research survey, report released 2026-07-28) giving each answer; not independent measurement
    provenance: vendor-published
    source_ref: LDS-ARCTICWOLF-2026
  prerequisites:
  - Inventory of automated and proposed actions
  - Test and rollback capability (digital twin, audit mode, ring deployment)
  - Named owner for each agent's activity
  risks_and_guardrails:
  - 'NCSC: where unintended activity would be significant, name responsible individuals or groups, keep human oversight and use real-time monitoring; judge agents should themselves be independently evaluated.'
  - 'NCSC notes existing remedial automation such as SOAR is deterministic: each rule is crafted and tested.'
  - Interim NCSC advice; the NCSC says formal guidance is being developed and will supersede its agentic-risk blog.
  human_checkpoints:
  - Approval of each autonomy level by the accountable owner
  - Emergency shutdown ability for agents
  role_evolution: SOC leads become owners of an autonomy register; analysts move between approving, monitoring and handling exceptions.
  evidence_grade: D
  sources:
  - ref: NCSC-AGENTICDEF-2026
    title: One does not simply defend agentically (blog by Dave Chismon)
    publisher: UK National Cyber Security Centre
    type: regulator
    url: https://www.ncsc.gov.uk/blogs/one-does-not-simply-defend-agentically
    date: '2026-09-21'
    access: full
    locator: Risk table with dimensions Potency, Scope, Criticality, Rollout confidence, Recoverability; footnote on SOAR determinism
  - ref: NCSC-AGENTICRISK-2026
    title: Managing the cyber risk of agentic AI (interim blog by Toby W)
    publisher: UK National Cyber Security Centre
    type: regulator
    url: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai
    date: '2026-08-20'
    access: full
    locator: 'Section ''Set the right level of oversight'': human-in-the-loop, on-the-loop, out-of-the-loop; named responsibility; judge agents evaluated independently'
  - ref: ARXIV-2505.23397
    title: A Unified Framework for Human AI Collaboration in Security Operations Centers with Trusted Autonomy
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2505.23397
    date: 2025-05
    access: full
    locator: 'Abstract: five levels of AI autonomy mapped to HITL roles and task-specific trust thresholds; evaluated in a simulated cyber range'
  - ref: CISA-AGENTIC-2026
    title: Careful Adoption of Agentic AI Services (CISA landing page; the guidance itself is hosted by ASD's ACSC)
    publisher: CISA with ASD's ACSC and partners
    type: regulator
    url: https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services
    date: '2026-05-01'
    access: full
    locator: 'Landing page summary: guidance on designing, deploying and operating agentic systems safely; aligns AI risk management with existing frameworks (guidance text not opened)'
  - ref: LDS-ARCTICWOLF-2026
    title: Arctic Wolf Survey Finds AI Trust Gap (news summary of Arctic Wolf's 2026 AI & Cybersecurity Trends Report, released 2026-07-28)
    publisher: Let's Data Science
    type: press
    url: https://letsdatascience.com/news/arctic-wolf-survey-finds-ai-trust-gap-b12457e5
    date: '2026-09-14'
    access: full
    locator: 'Key points: 94% LLM use, 14% central, 53% trust for narrow actions'
  last_reviewed: '2026-10-17'
  notes: 'Idea (grade D): discussed by a regulator and researchers; no organisation reports running this scoring. The CISA/ACSC guidance document itself (hosted at cyber.gov.au) could not be opened, so only the CISA landing summary is used.'
- id: security-operations-10
  title: 'Observability of the SOC''s own agents: activity dashboard, attribution of agent actions and emergency shutdown'
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Once agents act inside security tooling, analysts and auditors need to see what each agent did, with what evidence, and be able to stop it.
  solution: Log agent actions as security telemetry, make each action attributable to an identity and owner, dashboard what the agent considered and suggested so analysts can inspect and tune it, and keep a way to 'pull the plug'. At .conf26 Cisco/Splunk built a Triage Agent operations dashboard in an afternoon; the NCSC lists observability, attribution and emergency shutdown among its agentic-risk considerations, and CISA/NIST/NSA set out incident-readiness practices for agent control incidents.
  outcomes:
  - lever: risk
    description: 'The dashboard made agent activity visible to analysts: events, queries, evidence considered, confidence bands, suggested dispositions and handoff status.'
    figure: '1,503 AI agentic events; confidence bands 20-39: 0%, 40-59: 13%, 60-79: 53%, 80-100: 34%'
    measures: Count of agent events and share of findings by average confidence band, entire .conf26 conference; described as event-environment observations, not benchmarks
    provenance: vendor-published
    source_ref: CISCO-SPLUNK-CONF26-2026
  prerequisites:
  - A SIEM or data platform that holds both the agent's actions and the evidence
  - Agent identities that can be attributed and scoped
  - Defined kill-switch procedure
  risks_and_guardrails:
  - 'NCSC interim advice: log, audit and monitor agentic AI activity as part of security operations; make AI activity easy to attribute; keep emergency shutdown.'
  - CISA/NIST/NSA key practices (2026-10-16) cover limiting agent access, monitoring for unexpected activity, preserving evidence and shutting down undesired behaviour, and reporting incidents and near-misses; they target organisations training and evaluating highly capable agents.
  - Confidence bands are model outputs; the post does not validate them against outcomes.
  human_checkpoints:
  - Analysts inspect the agent's data trail before acting
  - Named group responsible for agent activity
  role_evolution: No source describes a role change for this practice; the NCSC advice implies a named individual or group owns agent activity.
  evidence_grade: B
  sources:
  - ref: CISCO-SPLUNK-CONF26-2026
    title: 'Splunk .conf26: Tracking the Triage Agent in the Agentic SOC'
    publisher: Cisco Blogs (Cisco and Splunk)
    type: vendor
    url: https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/
    date: '2026-10-08'
    access: full
    locator: Section 'Building the Triage Agent Dashboard in an Afternoon' and Dashboard Snapshot table
  - ref: NCSC-AGENTICRISK-2026
    title: Managing the cyber risk of agentic AI (interim blog by Toby W)
    publisher: UK National Cyber Security Centre
    type: regulator
    url: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai
    date: '2026-08-20'
    access: full
    locator: 'Key considerations list: ''Observability: log, audit and monitor agentic AI activity as part of security operations'', ''Make your AI activity easy to attribute'', ''Emergency shutdown'''
  - ref: CISA-KEYPRACTICES-2026
    title: Key Practices for Incident Readiness and Response in Super Intelligence Training and Evaluation (CISA landing page)
    publisher: CISA with NIST and NSA
    type: regulator
    url: https://www.cisa.gov/resources-tools/resources/key-practices-incident-readiness-and-response-super-intelligence-training-and-evaluation
    date: '2026-10-16'
    access: full
    locator: Summary of ten voluntary practices and bullet list of coverage (access limits, monitoring, evidence, rebuild, reporting)
  last_reviewed: '2026-10-17'
  notes: 'Grade B: a named deployment (event SOC) built the dashboard but published no outcome measure for the observability itself.'
- id: security-operations-11
  title: Conference SOC turns a recurring analyst search into a formal detection linked to a SOAR playbook (deterministic automation, not AI)
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Cleartext credentials kept appearing on the RSAC network, and in prior years each finding needed manual work to identify the user, document it, notify them and close the case.
  solution: Searches that had supported dashboards were converted into formal Splunk Enterprise Security detections; automation rules linked them to a Splunk SOAR playbook that extracted the user, sent a standard notification, updated the disposition and closed the case. Included because the source frames it as part of agentic-SOC principles and because NCSC treats SOAR as the established, deterministic form of automated action.
  outcomes:
  - lever: capacity
    description: Analyst time saved by the playbook during the event.
    figure: More than nine hours of analyst time
    measures: Analyst time saved over the RSAC 2026 conference by the cleartext-credential detection and playbook, as stated by the operators
    provenance: self-reported
    source_ref: SPLUNK-RSACSOC-2026
  prerequisites:
  - Normalised telemetry and a SIEM with detections and SOAR integration
  - A repeatable, low-risk finding class
  risks_and_guardrails:
  - Splunk says this was not a fully agentic SOC at RSAC 2026.
  - NCSC notes SOAR automations are crafted, tested and highly deterministic, unlike LLM judgement.
  human_checkpoints:
  - Detections authored and tuned by engineers before automation; humans keep control of response decisions affecting users, availability or trust
  role_evolution: Analysts spend less time on notification-and-close work; detection engineers own the conversion from search to detection to playbook.
  evidence_grade: A
  sources:
  - ref: SPLUNK-RSACSOC-2026
    title: 'From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC'
    publisher: Splunk
    type: vendor
    url: https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html
    date: '2026-08-24'
    access: full
    locator: 'Passage on cleartext credentials: detection, SOAR playbook, ''saved more than nine hours of analyst time''; list of patterns'
  - ref: NCSC-AGENTICDEF-2026
    title: One does not simply defend agentically (blog by Dave Chismon)
    publisher: UK National Cyber Security Centre
    type: regulator
    url: https://www.ncsc.gov.uk/blogs/one-does-not-simply-defend-agentically
    date: '2026-09-21'
    access: full
    locator: 'Footnote 1: remedial action automated through SOAR, each rule crafted, tested and highly deterministic'
  last_reviewed: '2026-10-17'
  notes: Measured outcome, but from deterministic automation. The landscape file summarised this as AI decision support plus automation saving hours; the saving is attributed in the source to the SOAR playbook, not to AI. Self-reported by Cisco/Splunk, who are also the vendors.
- id: security-operations-12
  title: AI-drafted detection rules scored against human-written rules and threat-intelligence reports
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - software-systems
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Detection engineers spend labour-intensive time turning threat reports into queries and rules and tuning them, and crowdsourced rule repositories show uneven quality control.
  solution: 'Agents read threat-intelligence reports, run queries against telemetry and draft detection rules, which humans review; evaluation frameworks score generated rules against held-out human rules. Examples: the CTI-REALM benchmark, Sublime Security''s Automated Detection Engineer evaluation, SIGMERGE and AUTOSIGMA for Sigma rules.'
  outcomes:
  - lever: quality
    description: CTI-REALM best overall reward among 16 frontier models.
    figure: Highest reward 0.637; second 0.624
    measures: Overall reward (final detection results and trajectory-based rewards) on CTI-REALM emulated attacks across Linux, cloud and AKS
    provenance: independent
    source_ref: ARXIV-2603.13517
  - lever: quality
    description: SIGMERGE contributions to the official Sigma repository.
    figure: 4 novel Sigma rules accepted into the official repository
    measures: Count of rules contributed by the SIGMERGE authors and accepted; evaluated on 23 metrics against 16 baselines and 13 LLMs
    provenance: independent
    source_ref: USENIX-SIGMERGE-2026
  prerequisites:
  - Machine-readable threat reports and a test environment with emulated attacks and ground truth
  - Rule repository with review workflow
  risks_and_guardrails:
  - USENIX study of the Sigma repository finds informal rule evaluation, inexperienced contributions in places and divergences when rules migrate across SIEM vendors, so generated rules need the same review.
  human_checkpoints:
  - Detection engineer reviews and tests each rule before release
  role_evolution: Detection engineers review and test machine-drafted rules rather than write each from scratch.
  evidence_grade: C
  sources:
  - ref: ARXIV-2603.13517
    title: 'CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2603.13517
    date: '2026-03-13'
    access: full
    locator: 'Abstract: 16 frontier models, top reward 0.637, CTI-specific tools improve performance'
  - ref: ARXIV-2509.16749
    title: Evaluating LLM Generated Detection Rules in Cybersecurity (Sublime Security)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2509.16749
    date: '2025-09-20'
    access: full
    locator: 'Abstract: open-source framework scoring LLM-generated rules against human corpus using Sublime Security''s rules and ADE'
  - ref: USENIX-SIGMERGE-2026
    title: 'From Texts to Rules: Generating Sigma Rules with Large Language Models from Cyber Threat Reports (Cai et al.)'
    publisher: USENIX Security 2026
    type: academic
    url: https://www.usenix.org/conference/usenixsecurity26/presentation/cai
    date: 2026-08
    access: full
    locator: 'Abstract: 23 metrics, 16 baselines, 13 LLMs; 4 rules accepted'
  - ref: ARXIV-2608.19011
    title: 'From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation (AUTOSIGMA)'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.19011
    date: '2026-08-19'
    access: full
    locator: 'Abstract: AUTOSIGMA outperforms alternatives on rule validity, relevancy and ATT&CK coverage (no figures in abstract)'
  - ref: USENIX-SIGMA-2026
    title: Credible Threat Detection? Measuring Contribution Dynamics and Quality Control in a Crowdsourced Threat Detection Ecosystem (Virkud, Wang, Bates)
    publisher: USENIX Security 2026
    type: academic
    url: https://www.usenix.org/conference/usenixsecurity26/presentation/virkud
    date: 2026-08
    access: full
    locator: 'Abstract: informal rule evaluation, inexperienced contributions, divergences across SIEM vendors'
  last_reviewed: '2026-10-17'
  notes: 'Grade C: research benchmarks plus one product evaluation by its vendor; no operating SOC reports production results. CTI-REALM author affiliation was not verified on the abstract page.'
- id: security-operations-13
  title: LLM-assisted forensic timelines on a common schema with a validation layer before analyst use
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - research-synthesis
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Investigators stitch fragmented logs into a chronological narrative by hand, and AI-generated narratives must stand up to audit, regulation or legal scrutiny.
  solution: 'A six-layer pipeline on the Open Cybersecurity Schema Framework: ingest, normalise, AI assist, validate, timeline, export. LLMs help with field inference, clustering and narrative; every transformation is versioned, hash verified and logged, and decision authority stays with the analyst.'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: No figures in the session abstract
    provenance: self-reported
    source_ref: FIRST-CON-2026
  prerequisites:
  - Logs normalised to OCSF
  - Existing SOC platform such as Splunk, Sentinel or Databricks
  - Confidence scoring, prompt traceability and workflow logging
  risks_and_guardrails:
  - The abstract aligns the approach with evidentiary standards for scientific reliability (names Daubert, Frye and Durant); no external review is reported.
  - Evidence of deployment was not seen beyond the abstract.
  human_checkpoints:
  - Human-in-the-loop controls so decision authority never leaves the analyst
  role_evolution: Analysts verify machine-built timelines against hash-verified source evidence.
  evidence_grade: C
  sources:
  - ref: FIRST-CON-2026
    title: 38th Annual FIRST Conference program agenda and session abstracts (Denver, 14-19 June 2026)
    publisher: FIRST
    type: conference
    url: https://www.first.org/conference/2026/program
    date: 2026-06
    access: full
    locator: 'Session ''From Logs to Living Timelines: AI-Assisted Incident Response in Hybrid Cloud Using OCSF'' (Centene), abstract'
  last_reviewed: '2026-10-17'
  notes: Presented by Centene staff; the abstract describes a designed framework and does not say it is in production, so grade is C and maturity emerging. The session itself was not viewed. Closely adjacent to the incident-response module.
- id: security-operations-14
  title: LLM drafts shift summaries, threat explanations and incident reports for analyst review
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Analysts spend time writing up findings and explaining indicators, and report detail can decline with fatigue.
  solution: Use LLMs for summarisation and report generation, which are the lower-risk, easier-to-verify tasks. In 25 interviews, SOC practitioners valued report automation while rating high-impact tasks such as incident analysis as not yet feasible. A vendor panel on the SANS AI survey names log analysis, explaining threats and report writing as the quick wins.
  outcomes:
  - lever: quality
    description: In the CSA study manual analysts' written detail dropped over the session while AI-assisted analysts maintained it; the study does not isolate report drafting.
    figure: 'Manual analysts: report detail down 27%, conclusion detail down 20%'
    measures: Change in detail scores of manual participants over the study; press release
    provenance: vendor-published
    source_ref: CSA-SOCBENCH-PR-2025
  prerequisites:
  - Approved tool and data-handling policy for what may be pasted or connected
  - Templates and review standards
  risks_and_guardrails:
  - The USENIX LogInject paper finds summarisation is exposed to log-borne injection; Poisoning the Watchtower finds summarisation the highest-risk task, so drafts from logs need the controls in use case 7.
  - Interview participants located limits in SOC readiness and human factors driving over-reliance.
  human_checkpoints:
  - Analyst edits and approves before a report is filed
  role_evolution: Analysts review drafts instead of writing them; interview participants stress keeping a human in the loop.
  evidence_grade: C
  sources:
  - ref: ARXIV-2608.00672
    title: 'From Chasing Ghosts to Missed Attacks: Perspectives and Perceptions of SOC Practitioners on LLM Integration, Risks, and Readiness'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2608.00672
    date: '2026-08-01'
    access: full
    locator: 'Abstract: 25 interviews; 15 use cases in six categories; report automation valued; incident analysis rated not yet feasible'
  - ref: SANS-AI-2026
    title: A SOC Leader's Guide to the 2026 SANS AI Survey (vendor blog summarising the SANS AI Survey; the survey itself was not opened)
    publisher: Swimlane
    type: vendor
    url: https://swimlane.com/blog/sans-ai-2026-soc-trust/
    date: '2026-05-18'
    access: full
    locator: 'Section ''The Gap Between Adoption and Maturity'': log analysis, explaining threats and report writing as easy adoption (vendor view)'
  - ref: CSA-SOCBENCH-PR-2025
    title: New Study from Cloud Security Alliance Finds AI Improves Analyst Accuracy, Speed, and Consistency in Security Investigations (press release)
    publisher: Cloud Security Alliance
    type: survey
    url: https://cloudsecurityalliance.org/press-releases/2025/10/07/new-csa-study-finds-ai-improves-analyst-accuracy-speed-and-consistency-in-security-investigations
    date: '2025-10-07'
    access: full
    locator: 'Completeness bullet: manual analysts'' report detail down 27%, conclusion detail down 20%'
  last_reviewed: '2026-10-17'
  notes: Interview participants are unnamed; no named SOC reports measured time saved on reporting.
- id: security-operations-15
  title: 'Hybrid cloud-edge triage: on-premises specialist models produce structured, auditable decisions under data-residency limits'
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - transaction-processing
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Verbose reasoning ensures accuracy and auditability but costs latency and tokens, while fully cloud-hosted LLMs raise latency, cost and privacy concerns for alert data.
  solution: A cloud model routes alerts to on-premises expert models that emit SOAR-ready JSON with compact, decision-critical reasoning, keeping data in-house.
  outcomes:
  - lever: speed
    description: AIDR versus chain-of-thought prompting.
    figure: 40.6% latency reduction versus chain-of-thought; 68% token reduction in compact datasets
    measures: Latency relative to chain-of-thought on the authors' alert datasets; token reduction from distilling alerts into 3-5 bullets
    provenance: independent
    source_ref: ARXIV-2512.08169
  prerequisites:
  - Training data of labelled alerts
  - On-premises compute for LoRA-tuned experts
  - SOAR to consume structured output
  risks_and_guardrails:
  - Authors' own experiments only; no named SOC.
  human_checkpoints:
  - Structured output reviewable and loggable before SOAR actions
  role_evolution: SOC engineers maintain specialist triage models; analysts see structured, concise rationales.
  evidence_grade: C
  sources:
  - ref: ARXIV-2512.08169
    title: Information-Dense Reasoning for Efficient and Auditable Security Alert Triage (AIDR)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2512.08169
    date: '2025-12-08'
    access: full
    locator: 'Abstract: cloud-edge architecture, 40.6% latency reduction, 68% token reduction, full data residency'
  last_reviewed: '2026-10-17'
  notes: Research prototype.
- id: security-operations-16
  title: Outcome-based SOC measurement and sampled quality assurance of AI dispositions
  archetype: security
  module: operations
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: SOCs report activity (incident counts) rather than whether the right threats were caught early, and AI closures remove alerts from human view without anyone checking the miss rate.
  solution: Replace volume metrics with decision-quality measures (agreement with senior-analyst review of sampled closures, miss rate on seeded or replayed attacks, time to decision, escalation rate, coverage) and sample AI-closed and AI-escalated alerts for review. This is an idea drawn from the gaps the sources describe; no organisation reports running this scheme.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Not published; SANS reports that 70% of respondents cite incident count as top SOC metric
    provenance: independent
    source_ref: SANS-SOC-2026
  prerequisites:
  - Seeded or replayed attack sets
  - Sampling protocol and reviewer capacity
  - Agreement on what a correct disposition is
  risks_and_guardrails:
  - ALERT-BENCH shows dismissals can be weakly investigated, which sampling is meant to catch.
  - NCSC recommends independent evaluation of judge agents.
  human_checkpoints:
  - Senior analysts review the samples and own the miss-rate trend
  role_evolution: Senior analysts or SOC engineers act as quality reviewers.
  evidence_grade: D
  sources:
  - ref: SANS-SOC-2026
    title: 'SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense (landing page with top takeaways, methodology and FAQ)'
    publisher: SANS Institute
    type: survey
    url: https://www.sans.org/research/security-operations-report
    date: '2026'
    access: full
    locator: 'Top takeaways and FAQ: 70% still cite incident count as top SOC metric; it measures volume of activity'
  - ref: ARXIV-2610.10608
    title: 'From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage'
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2610.10608
    date: '2026-10-06'
    access: full
    locator: 'Abstract: dismissal receives no consistently stronger investigation than escalation'
  - ref: NCSC-AGENTICRISK-2026
    title: Managing the cyber risk of agentic AI (interim blog by Toby W)
    publisher: UK National Cyber Security Centre
    type: regulator
    url: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai
    date: '2026-08-20'
    access: full
    locator: 'Section ''Set the right level of oversight'': judge agents should be independently evaluated'
  - ref: OMB-M2614-2026
    title: OMB Memorandum M-26-14, Ensuring Effective and Efficient Agency Logging and Network Visibility to Defend Against Evolving Cyber Threats
    publisher: US Office of Management and Budget
    type: regulator
    url: https://www.whitehouse.gov/wp-content/uploads/2026/05/M-26-14-Ensuring-Effective-and-Efficient-Agency-Logging-and-Network-Visibility-to-Defend-Against-Evolving-Cyber-Threats.pdf
    date: '2026-05-22'
    access: full
    locator: 'Measuring Maturity and Appendix C: progress reported as percentage of systems at each maturity level'
  last_reviewed: '2026-10-17'
  notes: 'Idea (grade D): no published practitioner discussion of this exact scheme was found; the components are individually described by SANS, researchers, the NCSC and OMB. Treat as a hypothesis to test in interviews.'
- id: security-operations-17
  title: Sanctioned, logged analyst AI assistants in place of ad hoc personal use
  archetype: security
  module: operations
  function: technology-it
  work_types:
  - review-assurance
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: SANS reports most analysts use AI individually, without organisational structure or systematic validation.
  solution: Provide approved assistants grounded in the SOC's runbooks and escalation criteria, with logging and a validation routine, and an acceptable-use position on what alert and log data may leave the tenant.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Not published
    provenance: independent
    source_ref: SANS-SOC-2026
  prerequisites:
  - Approved tooling and data-handling policy
  - Runbooks and knowledge base to ground the assistant
  risks_and_guardrails:
  - A law-firm summary of IBM's report says incidents involving shadow AI by employees more than doubled to 43 percent from 20 percent in 2025; the summary does not state the denominator and the finding concerns staff generally, not SOC analysts.
  - Swimlane's post argues trust needs the SOC's own context (runbooks, escalation criteria) fed to the AI.
  human_checkpoints:
  - Validation routine for assistant output
  role_evolution: Analysts use governed tools; SOC leads own acceptable-use and validation.
  evidence_grade: D
  sources:
  - ref: SANS-SOC-2026
    title: 'SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense (landing page with top takeaways, methodology and FAQ)'
    publisher: SANS Institute
    type: survey
    url: https://www.sans.org/research/security-operations-report
    date: '2026'
    access: full
    locator: 'FAQ: ''Most analysts use AI individually, without organizational structure or systematic validation''; 79% use AI or ML tools, 36% in a defined workflow'
  - ref: ELASTIC-SANS-2026
    title: '2026 SANS SOC Survey: A decade of cyber defense insights (sponsor summary page)'
    publisher: Elastic
    type: vendor
    url: https://www.elastic.co/resources/security/report/sans-soc-survey-insights-2026
    date: '2026'
    access: full
    locator: 'Sponsor summary: unchallenged outputs when analysts use AI without governance or validation (sponsor''s phrasing)'
  - ref: BAKERDONELSON-IBM-2026
    title: Ten Takeaways from IBM's 2026 Cost of a Data Breach Report
    publisher: Baker Donelson
    type: press
    url: https://www.bakerdonelson.com/ten-takeaways-from-ibms-2026-cost-of-a-data-breach-report
    date: '2026'
    access: full
    locator: 'Takeaway 6: incidents involving shadow AI 43 percent versus 20 percent in 2025, secondary summary of IBM report'
  - ref: SANS-AI-2026
    title: A SOC Leader's Guide to the 2026 SANS AI Survey (vendor blog summarising the SANS AI Survey; the survey itself was not opened)
    publisher: Swimlane
    type: vendor
    url: https://swimlane.com/blog/sans-ai-2026-soc-trust/
    date: '2026-05-18'
    access: full
    locator: Section 'Trust Requires Context, Not Just Speed'
  last_reviewed: '2026-10-17'
  notes: Idea (grade D). The remedy is inferred from the finding; the SANS landing page and Elastic's sponsor summary report the problem, not the fix.
- id: security-operations-18
  title: Logging-coverage maturity as the gate for AI-assisted detection tuning (federal logging requirements)
  archetype: security
  module: operations
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: OMB says the earlier memo's requirement to retain vast quantities of log data without clear utility proved neither operationally feasible nor cost-effective for most agencies; CISA describes fragmented logging practices as what the new architecture moves agencies away from.
  solution: OMB M-26-14 requires a risk-based, prioritised logging approach focused on continuous event monitoring (typically in the SOC) and threat hunting, investigation, response and forensics, with a maturity model reported as the percentage of systems at each level. The highest maturity level expects detections to be tuned using techniques such as machine learning or AI, and CISA's reference architecture will inform AI integration 'while still maintaining required governance and oversight'.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: No outcome figures; first Agency Logging Plans are due 2026-11-18 per CISA
    provenance: independent
    source_ref: CISA-LOGGING-2026
  prerequisites:
  - Agency Logging Plan submitted to OMB and CISA
  - System inventory visibility and log management planning
  risks_and_guardrails:
  - Required minimum is Advanced (Level 3) within 320 days of the reference architecture's release; ML/AI tuning appears in the top (Level 4) column only, so AI use is not mandated.
  - Logs must not capture or expose data contrary to law; sensitive log data needs protection.
  human_checkpoints:
  - Agency CISO sign-off of logging plan; CISA and FBI access to logs on request after a suspected compromise
  role_evolution: SOC and logging teams report maturity per system; AI-assisted tuning is an upper-tier practice.
  evidence_grade: D
  sources:
  - ref: OMB-M2614-2026
    title: OMB Memorandum M-26-14, Ensuring Effective and Efficient Agency Logging and Network Visibility to Defend Against Evolving Cyber Threats
    publisher: US Office of Management and Budget
    type: regulator
    url: https://www.whitehouse.gov/wp-content/uploads/2026/05/M-26-14-Ensuring-Effective-and-Efficient-Agency-Logging-and-Network-Visibility-to-Defend-Against-Evolving-Cyber-Threats.pdf
    date: '2026-05-22'
    access: full
    locator: 'Pages 2-4: CEM and THIRF objectives, Agency Logging Plan, maturity model, timelines; Appendix A AI row; Appendix C maturity table'
  - ref: CISA-LOGGING-2026
    title: CISA Releases Foundational, Flexible Guidance to Help Federal Agencies Implement Effective Logging, Visibility and Operational Standards (Logging Reference Architecture press release)
    publisher: CISA
    type: regulator
    url: https://www.cisa.gov/news-events/news/cisa-releases-foundational-flexible-guidance-help-federal-agencies-implement-effective-logging
    date: '2026-08-20'
    access: full
    locator: 'Press release: Logging Reference Architecture, plan due 2026-11-18, AI integration statement'
  last_reviewed: '2026-10-17'
  notes: Included as a measurable regulatory benchmark for the SOC's data foundation. It applies to US federal civilian agencies; CISA encourages critical infrastructure and SLTT entities to use it to benchmark. No deployment evidence yet; 'idea' label means no operating example found.
- id: security-operations-19
  title: Assurance of AI-enabled MDR and SOC suppliers against regulator risk lists
  archetype: security
  module: operations
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Outsourced detection and response now includes vendor AI agents that act on customer environments, and regulated customers must show control over ICT third parties.
  solution: 'Use regulator risk lists as a supplier questionnaire for MDR and SOC-as-a-service providers: authorisation and risk management, legality and permissions, sandboxing, secure integration, data protection, supply chain, efficacy and verification, responsible action (NCSC); and, in the EU financial sector, DORA, under which the ESAs say they are engaging critical ICT third-party providers on measures to adapt to frontier-AI cyber risk.'
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Not published
    provenance: independent
    source_ref: NCSC-AIADOPT-2026
  prerequisites:
  - Contract rights to evidence of AI validation, change control and incident reporting
  - Inventory of where supplier agents can act
  risks_and_guardrails:
  - NCSC list is a set of risks to manage, not an audit standard; a commentary expects it may become the audit basis, which is the commentator's prediction.
  - UK joint statement of 2026-05-15 restates existing operational-resilience expectations and adds no new rules (law-firm summary).
  human_checkpoints:
  - Third-party risk sign-off before onboarding or change to an AI-enabled service
  role_evolution: Third-party and security governance teams add AI-specific diligence to MDR renewals.
  evidence_grade: D
  sources:
  - ref: NCSC-AIADOPT-2026
    title: Supporting AI adoption for UK cyber defence (blog by Peter Haigh)
    publisher: UK National Cyber Security Centre
    type: regulator
    url: https://www.ncsc.gov.uk/blogs/supporting-ai-adoption-for-uk-cyber-defence
    date: '2026-04-23'
    access: full
    locator: List of eight risks including 'Customers and supply chain' and 'Efficacy and verification'
  - ref: AOSHEARMAN-ESRB-2026
    title: ESRB issues warning on systemic cyber risks from frontier AI models (law-firm summary of the ESRB warning and ESAs press release of 2026-06-25)
    publisher: A&O Shearman
    type: press
    url: https://finreg.aoshearman.com/esrb-issues-warning-on-systemic-cyber-risks-from-frontier-ai-models
    date: '2026-07-07'
    access: full
    locator: ESAs oversee risks under DORA and engage critical ICT third-party providers
  - ref: COOLEY-UKFIN-2026
    title: 'Busy Week for AI: FCA Reopens AI Input Zone, Regulators Issue Statement on Frontier AI Cyber Risks (law-firm summary of the Bank of England / FCA / HM Treasury joint statement of 2026-05-15)'
    publisher: Cooley LLP
    type: press
    url: https://finsights.cooley.com/busy-week-for-ai-fca-reopens-ai-input-zone-regulators-issue-statement-on-frontier-ai-cyber-risks/
    date: '2026-05-26'
    access: full
    locator: Five domains for action include managing risks from third parties; no new requirements
  - ref: EIOPA-DORA-2025
    title: Digital Operational Resilience Act (DORA) page
    publisher: EIOPA
    type: regulator
    url: https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en
    date: '2026-10-17'
    access: full
    locator: DORA applies since 17 Jan 2025 to financial entities and ICT third-party service providers
  last_reviewed: '2026-10-17'
  notes: 'Idea (grade D): no source reports a customer applying this to an MDR provider. Related vendor claims about ''agentic MDR'' belong to the practice angle.'
```

## 3. Module notes

### 3.1 Processes and key steps (with work types)

- **Detection engineering**: write, test, tune and retire detection content; map coverage to ATT&CK; convert recurring hunts into detections. Work type: software-systems. AI touches rule drafting from threat reports (use case 12). ATT&CK v20 (2026-10-13) lists 703 Enterprise detection strategies and 1,770 analytics (`MITRE-ATTCK-2026`, release summary).
- **Alert intake and tier-1 triage**: classify, enrich, close or escalate. Work type: transaction-processing. AI touches it via triage agents (use cases 1, 4, 5, 15).
- **Investigation**: pull evidence from SIEM, EDR, identity and network tools; build the timeline and root cause. Work type: research-synthesis. Use cases 2, 6, 13.
- **Case management and escalation**: tiers, handoffs, dispositions, feedback to detection. Work type: coordination-scheduling. The Cisco .conf26 SOC ran tier 1, tier 2, tier 3 and detection-engineering roles around the agent (`CISCO-SPLUNK-CONF26-2026`, section 'A blended analyst team').
- **Response action**: contain, block, quarantine, notify. Work types: transaction-processing and expert-judgment. Use cases 8, 9, 11.
- **Reporting and measurement**: shift reports, incident write-ups, SOC metrics. Work types: document-production and data-reporting. Use cases 14, 16.
- **Assurance of the SOC's AI and of MDR suppliers**: acceptance testing, QA, supplier diligence. Work type: review-assurance. Use cases 3, 7, 10, 19.

### 3.2 Common pain points

- Alert volume with mostly benign alerts and missed attacks (`ARXIV-2610.10608`, abstract; `ARXIV-2510.00311`, abstract).
- Skills and budget limits: ISC2 respondents with budget cuts 36% and hiring freezes 39%; 33% say they cannot afford to adequately staff and 29% cannot hire the skills they need (`ISC2-WORKFORCE-2025`, 'Economic Factors' section). SANS: only 32% of practitioners say management prioritises SOC staffing (`SANS-SOC-2026`).
- Fragmented data: 24% of cyber leaders name lack of enterprise-wide visibility the top barrier (`SANS-SOC-2026`, FAQ). A vendor makes the same point about fragmented data and isolated agents (`CROWDSTRIKE-AGSOC-2026`, vendor claim).
- Metrics measure activity, not catches: incident count top metric for 10 consecutive years, 70% (`SANS-SOC-2026`, FAQ).
- Defensive stress: the SoK on cybersecurity wellbeing (101 papers reviewed, 57 synthesised) reports stressors intrinsic to defensive work, including sustained vigilance and invisible success metrics (`USENIX-WELLBEING-2026`, abstract).
- Organisational limits on action: the NCSC argues defensive problems are mostly organisational, so automation is held back by business risk rather than technical difficulty (`NCSC-AGENTICDEF-2026`, introduction).

### 3.3 Metrics and benchmarks (with provenance)

| Metric | Value | Measures | Provenance | Ref and locator |
|---|---|---|---|---|
| SOCs using AI/ML tools | 79% | share of SOCs using AI or ML tools, 444 practitioners and 69 cyber leaders surveyed | independent survey, sponsor-funded | `SANS-SOC-2026`, top takeaways |
| SOCs with AI in a defined workflow | 36% | share that have built AI tools into a defined SOC workflow | same | `SANS-SOC-2026` |
| Teams integrating AI security tools | 28% integrated, 19% testing, 22% early evaluation (69% on a path to regular use) | share of 16,029 respondents (survey July-August 2025) | independent survey | `ISC2-WORKFORCE-2025`, 'AI Is Creating Opportunities' section |
| Productivity effect among AI tool users | 63% report a significant productivity boost; 21% of active users say no meaningful impact | respondents currently working with AI security tools | self-reported | same |
| Automated incident response adoption | 39%; 63% report significant AI shortcomings in detection or response | SANS 2026 AI Survey as summarised by a vendor; the 'only 37% trust' inference is the vendor's | vendor-published summary | `SANS-AI-2026` |
| Trust in autonomous action | 14% say AI is central to security-operations strategy; 53% trust AI for narrow actions such as blocking an IP | 1,350 decision-makers, Arctic Wolf survey via news summary | vendor-published | `LDS-ARCTICWOLF-2026` |
| Breach cost and AI/automation | USD 4.99M global average, up 12%; USD 1.93M lower with extensive AI and automation versus none | IBM/Ponemon sample; secondary coverage adds 65 days shorter breach lifecycle and 36% extensive use | vendor-published (IBM-sponsored research with Ponemon Institute) | `IBM-CODB-2026`, key figures; `ESECURITYPLANET-IBM-2026` |
| AI agents in SOCs (IBM) | about half of organisations deployed AI agents within SOCs; 18% for vulnerability management | secondary coverage of IBM report; primary not seen | vendor-published research, secondary coverage | `ESECURITYPLANET-IBM-2026`, discussion of SOC deployment |
| Mean time to identify and contain a breach | 247 days, up 2.5%, first rise in five years | IBM report as summarised by a law firm | vendor-published research, secondary coverage | `BAKERDONELSON-IBM-2026`, takeaway 8 |
| Analyst vs AI-assisted (simulated) | 45-61% faster; 22-29% more accurate | 148 participants, two escalated alert scenarios | vendor-published (CSA with Dropzone AI) | `CSA-SOCBENCH-PR-2025` |
| Triage misses in replay | at least 40.4% of attack-related alerts missed by every approach | 1,247 alerts, one multi-stage scenario | independent academic | `ARXIV-2610.10608` |
| Log-injection success | up to 88.2% baseline; 90.4% reduction with layered defence, 8.4% residual | 12,847 log entries, 3 production LLMs | independent academic | `USENIX-LOGINJECT-2026` |
| Federal logging maturity | Level 3 needs alerts covering at least 70% of baseline logging requirements; Level 4 at least 95% and ML/AI tuning | percentage of systems at each maturity level | regulator requirement | `OMB-M2614-2026`, Appendix C |
| Adversary speed (context) | average breakout time 29 minutes | CrowdStrike 2026 Global Threat Report as cited by CrowdStrike | vendor-published | `CROWDSTRIKE-AGSOC-2026` |

An academic survey of LLMs in SOC workflows (`ARXIV-2509.10858`, abstract) and the USENIX Security 2026 program page (`USENIX-SEC-2026`, listing of SOC-relevant papers: LogInject, Sigma quality control, SIGMERGE, the wellbeing SoK) were used to locate peer-reviewed work. Benchmarks to use for acceptance testing: ALERT-BENCH (`ARXIV-2610.10608`), SIABench (`ARXIV-2603.06422`), SIR-Bench (`ARXIV-2604.12040`), CyberSOCEval (`ARXIV-2509.20166`), CTI-REALM for detection rules (`ARXIV-2603.13517`).

### 3.4 Guardrails and regulatory points

- **US federal logging (OMB M-26-14, 2026-05-22)**: rescinds M-21-31; prioritises continuous event monitoring (typically in the SOC) and threat hunting, investigation, response and forensics; CISA's Logging Reference Architecture (press release 2026-08-20) is due to include a discussion of AI for these capabilities; agencies must submit an Agency Logging Plan, first plans due 2026-11-18 per CISA; maturity targets run 120, 180 and 320 days from the reference architecture's release (`OMB-M2614-2026`, pp. 2-4; `CISA-LOGGING-2026`).
- **CISA with ASD's ACSC, "Careful Adoption of Agentic AI Services" (2026-05-01)**: joint guidance on designing, deploying and operating agentic systems safely and aligning AI risk management with existing frameworks (`CISA-AGENTIC-2026`; landing summary only, guidance not opened). Terminology note: CISA pages retrieved on 2026-10-17 show the word "AI" replaced by "Super Intelligence (SI)" in titles and text (for example "Careful Adoption of Agentic SI Services"), while linked ACSC and URL slugs still say AI.
- **CISA/NIST/NSA key practices (2026-10-16)**: ten voluntary practices for organisations training and evaluating highly capable agents, covering access limits, monitoring for unexpected activity, evidence preservation, shutdown, rebuild from verified baselines and reporting incidents and near-misses (`CISA-KEYPRACTICES-2026`). Most relevant to operations teams as a template for agent control incidents.
- **UK NCSC**: eight risks to manage for AI-enabled cyber defence (2026-04-23, `NCSC-AIADOPT-2026`); a five-dimension scoring scheme for defensive actions (2026-09-21, `NCSC-AGENTICDEF-2026`); interim agentic-AI controls including observability as part of security operations, attribution and emergency shutdown, with formal guidance said to be in development (2026-08-20, `NCSC-AGENTICRISK-2026`).
- **NIST**: COSAiS overlays on SP 800-53 for AI systems, with proposed use cases that include single-agent and multi-agent systems; an annotated outline for predictive AI was released 2026-01-08 with feedback requested by 2026-02-13 (`NIST-COSAIS-2026`). SP 800-61 Rev. 3 (April 2025) is the current incident-response recommendation set, framed as a CSF 2.0 community profile (`NIST-SP80061R3-2025`).
- **EU**: NIS2 covers 18 sectors, requires risk-management measures and notification of significant incidents, and makes top management accountable (`EC-NIS2`). DORA has applied since 2025-01-17 to financial entities and ICT third-party providers (`EIOPA-DORA-2025`). The AI Act's high-risk obligations (including logging, documentation, human oversight, robustness and cybersecurity) apply from 2027-12-02 to the listed high-risk categories; the page's list does not name security-operations tools, and I found no authoritative classification of SOC AI (`EC-AIACT-2026`). The Commission's Action Plan on Cybersecurity and AI encourages organisations to use AI, including open-source models where appropriate, to detect and address vulnerabilities faster and to prevent and respond to attacks (`EC-ACTIONPLAN-2026`, date as in the landscape file; the page is undated).
- **EU financial supervisors**: the ESRB warning of 2026-06-25 on systemic cyber risk from frontier AI, welcomed by the ESAs, who say DORA and the AI Act provide a strong foundation and that they engage critical ICT providers (`AOSHEARMAN-ESRB-2026`, law-firm summary).
- **UK financial regulators**: Bank of England, FCA and HM Treasury joint statement of 2026-05-15 on frontier AI and cyber resilience; no new requirements; five domains including third-party risk and response and recovery (`COOLEY-UKFIN-2026`, law-firm summary).
- **US SEC**: Form 8-K Item 1.05 incident disclosure due four business days after a materiality determination, and Regulation S-K Item 106 risk-management disclosure (`SEC-CYBER-2023`). Trade groups asked on 2026-04-10 that both be rescinded or narrowed (`SIFMA-SEC-2026`, search-only); no SEC proposal or final action found in search.
- **Standards bodies**: OWASP Top 10 for Agentic Applications (2025-12-09, 100+ contributors, `OWASP-AGENTIC-2025`); ATT&CK v20 adds AI-enabled and AI-focused techniques including Direct Prompt Injection, Indirect Prompt Injection, AI Result Poisoning and a technique named Impair Autonomous Defenses, so SOC detection content can cover attacks on the SOC's own AI (`MITRE-ATTCK-2026`, 'New Techniques' list).

### 3.5 Frontier signals (dated)

- 2026-10-16: CISA, NIST and NSA publish incident-readiness practices for agent control incidents (`CISA-KEYPRACTICES-2026`).
- 2026-10-08: Cisco and Splunk run a live agentic SOC and publish agent-activity metrics, framing the operating principle as agents prepare, people decide (`CISCO-SPLUNK-CONF26-2026`).
- 2026-10-06/07: preprints on evidence-gated triage (ALERT-BENCH, AIDA) and constrained-action remediation (`ARXIV-2610.10608`, `ARXIV-2610.09906`).
- 2026-09-21: NCSC says it will publish an 'AI for Cyber Defence' problem book and wants research on proving that 'low risk' automated actions are low risk; it names Cyber Shield, a national-scale agentic cyber defence effort with DCMS (`NCSC-AGENTICDEF-2026`).
- 2026-09-16: CISA cyber decoys guidance, guidance on decoys, a non-AI route that CISA says can generate high-fidelity alerts and reduce mean time to detect (`CISA-DECOYS-2026`).
- 2026-08-20: CISA Logging Reference Architecture; NCSC interim agentic controls (`CISA-LOGGING-2026`, `NCSC-AGENTICRISK-2026`).
- 2026-08-01: interview study with 25 SOC practitioners: incident analysis rated not yet feasible for LLMs, strong willingness to adopt under competitive pressure (`ARXIV-2608.00672`).
- 2026-07-28 (survey release): Arctic Wolf survey shows trust lags adoption (`LDS-ARCTICWOLF-2026`).
- 2026-06 (FIRST): sessions on tier-1 LLM triage experiments, schema-first AI-assisted timelines and attacks on DFIR agents (`FIRST-CON-2026`).
- 2026-05-01: first joint government agentic-AI adoption guidance (`CISA-AGENTIC-2026`).

### 3.6 Workforce and role effects

- ISC2 2025: traditional roles such as SOC analyst and incident responder are described as evolving rather than disappearing; AI is the most pressing skills need (41%); 73% of respondents say AI will create more specialised skills (`ISC2-WORKFORCE-2025`, key findings and AI section).
- SANS 2026: meaningful work and career progression have outranked pay as top retention drivers for three straight years (`SANS-SOC-2026`, key findings).
- Interviews: practitioners value AI for repetitive low-level tasks such as report automation; they locate limits in SOC readiness and human factors driving over-reliance (`ARXIV-2608.00672`, abstract).
- Explainability study (survey of 248 and 24 interviews): analysts accepted AI outputs even at lower predictive accuracy when explanations seemed relevant and evidence-backed, a calibration risk (`ARXIV-2503.02065`, abstract).
- Event SOC model: tier 1 reviews agent-prepared findings; detection engineers tune from analyst feedback (`CISCO-SPLUNK-CONF26-2026`).
- NCSC: where unintended activity matters, name individuals or groups responsible for agent activity (`NCSC-AGENTICRISK-2026`, oversight section).
- No hard data on entry-level analyst hiring effects was found (see Gaps).

### 3.7 Objections and concerns practitioners raise

- Over-reliance and missed attacks are the main worry; practitioners fear the false negative a trusted model waves through (`ARXIV-2608.00672`).
- Log content is attacker-controlled, so the SOC's own copilot can be steered (`USENIX-LOGINJECT-2026`; FIRST sessions from NTT DATA and CyCraft, `FIRST-CON-2026`).
- Governance lags adoption: most analysts use AI individually without defined workflow or validation (`SANS-SOC-2026`, FAQ); only 14% say AI is central to security operations (`LDS-ARCTICWOLF-2026`).
- Vendor evidence is self-reported: the one randomised study is simulated and co-announced with the tool vendor (`CSA-SOCBENCH-PR-2025`); Cisco says its dashboard values are not product benchmarks (`CISCO-SPLUNK-CONF26-2026`).
- Autonomy changes the failure mode: a wrong automated action can disrupt the business as badly as an attack (`NCSC-AGENTICDEF-2026`).
- Latency and cost of guardrails: the guardrail-proxy authors say inline control is out of scope on measured latency (`ARXIV-2610.09906`).

### 3.8 Interview probes for an advisor

1. Which alert classes does an AI touch before an analyst sees them, and who samples what it closes? What miss rate have you measured, and on what data?
2. For each automated action (block, isolate, disable account, notify), what is its potency, scope and recoverability, who owns it, and how do you stop it?
3. What does your SOC report today (incident counts, time to decision, coverage) and did the metrics change after AI? Who reviews them?
4. What untrusted content (log fields, email bodies, tickets, threat reports) reaches your LLM tools, and has anyone tried to inject instructions through it?
5. How would you show a regulator, auditor or customer what your agents did, under whose authority, and how your MDR or SOC supplier validates its own AI?

### 3.9 Corrections and flags on the landscape file

- **RSAC SOC time saving.** The landscape row for `SPLUNK-RSACSOC-2026` lists 'automation saved 9+ analyst hours' beside AI decision support. The source attributes the saving to a SOAR playbook that handled cleartext credential findings, not to AI; it also says the SOC was not fully agentic (`SPLUNK-RSACSOC-2026`). Use case 11 reflects this.
- **SANS AI survey.** The '37% trust' reading is the Swimlane author's inference from the 63% figure; the SANS survey itself was not opened (`SANS-AI-2026`).
- **IBM Cost of a Data Breach 2026.** Reading the page directly gives USD 4.99M, up 12%, and USD 1.93M savings from extensive AI and automation (`IBM-CODB-2026`), matching the landscape's 4.99M. A text-mirror copy of the same URL returned stale figures (4.50M, 1.74M); use the direct fetch. The landscape did not capture the savings figure.
- **ISACA 8%.** The ISACA landing page confirms 'AI governance and incident response maturity remain underdeveloped' but not the 8% AI-specific exercise figure (`ISACA-SOC-2026`); treat the 8% as unverified.
- **ENISA.** A newer ENISA Threat Landscape 2026 was published 2026-09-22; its press release says emerging AI models are expected to be used increasingly to support malicious operations (`ENISA-ETL-2026`).
- **CISA/NIST terminology.** Confirmed as observed by the landscape (section 3.4).

## 4. Routed to other modules

- **incident-response**: LLM incident-response planning with bounded hallucination, up to 22% shorter recovery times than frontier LLMs on logs from reported incidents (`NDSS-IRPLAN-2026`, abstract); hierarchical agentic response validated in a digital twin, recovery success better than frontier-LLM baselines by 18-31% on a 33-component testbed (`ARXIV-2608.15016`, abstract); CISA/NIST/NSA key practices for agent control incidents (`CISA-KEYPRACTICES-2026`); NIST SP 800-61 Rev. 3 (`NIST-SP80061R3-2025`); the CERT-In and OpenAI agent-containment incidents are in the landscape file and were not re-read here.
- **ai-security**: OWASP Top 10 for Agentic Applications (`OWASP-AGENTIC-2025`); ATT&CK v20 AI techniques (`MITRE-ATTCK-2026`); NIST COSAiS overlays (`NIST-COSAIS-2026`); SoK on the attack surface of agentic AI (`ARXIV-2603.22928`); IBM finding that 92% of organisations with an AI-related incident lacked proper AI access controls and 68% lacked AI governance policies (`BAKERDONELSON-IBM-2026`, takeaway 5); the log-injection research is shared with use case 7.
- **security-governance-risk**: SEC disclosure rules and rescission push (`SEC-CYBER-2023`, `SIFMA-SEC-2026`); EU AI Act, NIS2, DORA timelines (`EC-AIACT-2026`, `EC-NIS2`, `EIOPA-DORA-2025`); UK and EU financial-supervisor statements (`COOLEY-UKFIN-2026`, `AOSHEARMAN-ESRB-2026`); workforce statistics (`ISC2-WORKFORCE-2025`).
- **threat-intelligence**: CyberSOCEval malware-analysis and threat-intelligence reasoning benchmark (`ARXIV-2509.20166`); ENISA threat landscape 2026 (`ENISA-ETL-2026`).
- **vulnerability-exposure**: FIRST 'PSIRT 2.0 in Action' reports that 85% of APAC PSIRTs operate with fewer than five members and describes human-guided agentic AI for PSIRT workflows (`FIRST-CON-2026`, session abstract).
- **identity-access**: IBM guidance to scope and attribute agentic identities (`IBM-CODB-2026`, 'Secure and control agentic identities'); IBM-reported share securing non-human identities in AI workflows is in the secondary summary (`BAKERDONELSON-IBM-2026`, takeaway 10).

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| `OMB-M2614-2026` | OMB Memorandum M-26-14, Ensuring Effective and Efficient Agency Logging and Network Visibility to Defend Against Evolving Cyber Threats | US Office of Management and Budget | regulator | https://www.whitehouse.gov/wp-content/uploads/2026/05/M-26-14-Ensuring-Effective-and-Efficient-Agency-Logging-and-Network-Visibility-to-Defend-Against-Evolving-Cyber-Threats.pdf | 2026-05-22 | full |
| `CISA-LOGGING-2026` | CISA Releases Foundational, Flexible Guidance to Help Federal Agencies Implement Effective Logging, Visibility and Operational Standards (Logging Reference Architecture press release) | CISA | regulator | https://www.cisa.gov/news-events/news/cisa-releases-foundational-flexible-guidance-help-federal-agencies-implement-effective-logging | 2026-08-20 | full |
| `CISA-AGENTIC-2026` | Careful Adoption of Agentic AI Services (CISA landing page; the guidance itself is hosted by ASD's ACSC) | CISA with ASD's ACSC and partners | regulator | https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services | 2026-05-01 | full |
| `CISA-KEYPRACTICES-2026` | Key Practices for Incident Readiness and Response in Super Intelligence Training and Evaluation (CISA landing page) | CISA with NIST and NSA | regulator | https://www.cisa.gov/resources-tools/resources/key-practices-incident-readiness-and-response-super-intelligence-training-and-evaluation | 2026-10-16 | full |
| `CISA-DECOYS-2026` | New CISA Guidance Helps Critical Infrastructure Detect, Observe and Impede Malicious Cyber Activity (cyber decoys press release) | CISA | regulator | https://www.cisa.gov/news-events/news/new-cisa-guidance-helps-critical-infrastructure-detect-observe-and-impede-malicious-cyber-activity | 2026-09-16 | full |
| `NCSC-AIADOPT-2026` | Supporting AI adoption for UK cyber defence (blog by Peter Haigh) | UK National Cyber Security Centre | regulator | https://www.ncsc.gov.uk/blogs/supporting-ai-adoption-for-uk-cyber-defence | 2026-04-23 | full |
| `NCSC-AGENTICDEF-2026` | One does not simply defend agentically (blog by Dave Chismon) | UK National Cyber Security Centre | regulator | https://www.ncsc.gov.uk/blogs/one-does-not-simply-defend-agentically | 2026-09-21 | full |
| `NCSC-AGENTICRISK-2026` | Managing the cyber risk of agentic AI (interim blog by Toby W) | UK National Cyber Security Centre | regulator | https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai | 2026-08-20 | full |
| `EC-ACTIONPLAN-2026` | EU Action Plan on Cybersecurity and Artificial Intelligence | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence | 2026-07-07 | full |
| `EC-AIACT-2026` | AI Act (policy page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-17 | full |
| `EC-NIS2` | NIS2 Directive: securing network and information systems (policy page) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/nis2-directive | 2026-10-17 | full |
| `EIOPA-DORA-2025` | Digital Operational Resilience Act (DORA) page | EIOPA | regulator | https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en | 2026-10-17 | full |
| `ENISA-ETL-2026` | ENISA Threat Landscape 2026 (publication page and press release) | ENISA | regulator | https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026 | 2026-09-22 | full |
| `SEC-CYBER-2023` | SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies | US Securities and Exchange Commission | regulator | https://www.sec.gov/newsroom/press-releases/2023-139 | 2023-07-26 | full |
| `NIST-COSAIS-2026` | SP 800-53 Control Overlays for Securing AI Systems (COSAiS) project page | NIST | standard-setter | https://csrc.nist.gov/projects/cosais | 2026-01-08 | full |
| `NIST-SP80061R3-2025` | NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile | NIST | standard-setter | https://csrc.nist.gov/pubs/sp/800/61/r3/final | 2025-04 | full |
| `MITRE-ATTCK-2026` | ATT&CK v20 release notes (October 2026) | MITRE | standard-setter | https://attack.mitre.org/resources/updates/ | 2026-10-13 | full |
| `OWASP-AGENTIC-2025` | OWASP Top 10 for Agentic Applications for 2026 (resource landing page) | OWASP GenAI Security Project | standard-setter | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | 2025-12-09 | full |
| `SIFMA-SEC-2026` | Reforming Regulation S-K's Cybersecurity Disclosures (joint trades letter) | SIFMA and joint trade associations | professional-body | https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades | 2026-04-10 | search-only |
| `ISC2-WORKFORCE-2025` | 2025 ISC2 Cybersecurity Workforce Study | ISC2 | professional-body | https://www.isc2.org/Insights/2025/12/2025-isc2-cybersecurity-workforce-study | 2025-12-04 | full |
| `ISACA-SOC-2026` | State of Cybersecurity 2026 report (landing page) | ISACA | professional-body | https://www.isaca.org/resources/reports/state-of-cybersecurity-2026 | 2026-09-22 | full |
| `CSA-SOCBENCH-2025` | Beyond the Hype: A Benchmark Study of AI Agents in the SOC (report landing page) | Cloud Security Alliance | survey | https://cloudsecurityalliance.org/artifacts/a-benchmark-study-of-ai-agents-in-the-soc | 2025-10-06 | full |
| `CSA-SOCBENCH-PR-2025` | New Study from Cloud Security Alliance Finds AI Improves Analyst Accuracy, Speed, and Consistency in Security Investigations (press release) | Cloud Security Alliance | survey | https://cloudsecurityalliance.org/press-releases/2025/10/07/new-csa-study-finds-ai-improves-analyst-accuracy-speed-and-consistency-in-security-investigations | 2025-10-07 | full |
| `SANS-SOC-2026` | SANS 2026 SOC Report: A Decade of Evolution in Cyber Defense (landing page with top takeaways, methodology and FAQ) | SANS Institute | survey | https://www.sans.org/research/security-operations-report | 2026 | full |
| `IBM-CODB-2026` | Cost of a Data Breach Report 2026 (landing page) | IBM and Ponemon Institute | survey | https://www.ibm.com/reports/data-breach | 2026-07 | full |
| `USENIX-LOGINJECT-2026` | Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation (Karanjai et al.) | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai | 2026-08 | full |
| `USENIX-SIGMA-2026` | Credible Threat Detection? Measuring Contribution Dynamics and Quality Control in a Crowdsourced Threat Detection Ecosystem (Virkud, Wang, Bates) | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/virkud | 2026-08 | full |
| `USENIX-WELLBEING-2026` | SoK: Beyond Burnout -- A Gap Analysis of Psychological Harm in Cybersecurity Work (Phelan, Flechais) | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/phelan | 2026-08 | full |
| `USENIX-SIGMERGE-2026` | From Texts to Rules: Generating Sigma Rules with Large Language Models from Cyber Threat Reports (Cai et al.) | USENIX Security 2026 | academic | https://www.usenix.org/conference/usenixsecurity26/presentation/cai | 2026-08 | full |
| `NDSS-IRPLAN-2026` | Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination (Hammar, Alpcan, Lupu) | NDSS Symposium 2026 | academic | https://www.ndss-symposium.org/ndss-paper/incident-response-planning-using-a-lightweight-large-language-model-with-reduced-hallucination/ | 2026-02 | full |
| `ARXIV-2610.10608` | From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage | arXiv | academic | https://arxiv.org/abs/2610.10608 | 2026-10-06 | full |
| `ARXIV-2610.09906` | Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy | arXiv | academic | https://arxiv.org/abs/2610.09906 | 2026-10-07 | full |
| `ARXIV-2605.24421` | Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content | arXiv | academic | https://arxiv.org/abs/2605.24421 | 2026-05-23 | full |
| `ARXIV-2603.06422` | Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis (SIABench) | arXiv | academic | https://arxiv.org/abs/2603.06422 | 2026-03-06 | full |
| `ARXIV-2604.12040` | SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents | arXiv | academic | https://arxiv.org/abs/2604.12040 | 2026-04-13 | full |
| `ARXIV-2509.20166` | CyberSOCEval: Benchmarking LLMs Capabilities for Malware Analysis and Threat Intelligence Reasoning | arXiv (released within Meta CyberSecEval 4) | academic | https://arxiv.org/abs/2509.20166 | 2025-09-24 | full |
| `ARXIV-2510.00311` | CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage | arXiv | academic | https://arxiv.org/abs/2510.00311 | 2025-09-30 | full |
| `ARXIV-2505.06394` | Towards AI-Driven Human-Machine Co-Teaming for Adaptive and Agile Cyber Security Operation Centers | arXiv | academic | https://arxiv.org/abs/2505.06394 | 2025-05-09 | full |
| `ARXIV-2505.23397` | A Unified Framework for Human AI Collaboration in Security Operations Centers with Trusted Autonomy | arXiv | academic | https://arxiv.org/abs/2505.23397 | 2025-05 | full |
| `ARXIV-2609.32516` | REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers | arXiv | academic | https://arxiv.org/abs/2609.32516 | 2026-09-26 | full |
| `ARXIV-2607.28460` | Cybersecurity Detection Classification with Reasoning-enabled Language Models | arXiv | academic | https://arxiv.org/abs/2607.28460 | 2026-07-30 | full |
| `ARXIV-2607.09176` | SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking | arXiv | academic | https://arxiv.org/abs/2607.09176 | 2026-07-10 | full |
| `ARXIV-2512.08169` | Information-Dense Reasoning for Efficient and Auditable Security Alert Triage (AIDR) | arXiv | academic | https://arxiv.org/abs/2512.08169 | 2025-12-08 | full |
| `ARXIV-2509.10858` | Large Language Models for Security Operations Centers: A Comprehensive Survey | arXiv | academic | https://arxiv.org/abs/2509.10858 | 2025-09 | full |
| `ARXIV-2608.00672` | From Chasing Ghosts to Missed Attacks: Perspectives and Perceptions of SOC Practitioners on LLM Integration, Risks, and Readiness | arXiv | academic | https://arxiv.org/abs/2608.00672 | 2026-08-01 | full |
| `ARXIV-2503.02065` | Too Much to Trust? Measuring the Security and Cognitive Impacts of Explainability in AI-Driven SOCs | arXiv | academic | https://arxiv.org/abs/2503.02065 | 2025-03-03 | full |
| `ARXIV-2603.13517` | CTI-REALM: Benchmark to Evaluate Agent Performance on Security Detection Rule Generation Capabilities | arXiv | academic | https://arxiv.org/abs/2603.13517 | 2026-03-13 | full |
| `ARXIV-2509.16749` | Evaluating LLM Generated Detection Rules in Cybersecurity (Sublime Security) | arXiv | academic | https://arxiv.org/abs/2509.16749 | 2025-09-20 | full |
| `ARXIV-2608.19011` | From Threat Intelligence to Detection: Knowledge-driven Enrichment and Template-based Rule Grounding for Automated Sigma Rule Generation (AUTOSIGMA) | arXiv | academic | https://arxiv.org/abs/2608.19011 | 2026-08-19 | full |
| `ARXIV-2608.15016` | Hierarchical Agentic Incident Response with Digital-Twin-Validated Attack Inference | arXiv | academic | https://arxiv.org/abs/2608.15016 | 2026-08-15 | full |
| `ARXIV-2603.22928` | SoK: The Attack Surface of Agentic AI - Tools and Autonomy | arXiv | academic | https://arxiv.org/abs/2603.22928 | 2026-03-24 | full |
| `FIRST-CON-2026` | 38th Annual FIRST Conference program agenda and session abstracts (Denver, 14-19 June 2026) | FIRST | conference | https://www.first.org/conference/2026/program | 2026-06 | full |
| `USENIX-SEC-2026` | USENIX Security 2026 technical sessions (program page with paper abstracts) | USENIX | conference | https://www.usenix.org/conference/usenixsecurity26/technical-sessions | 2026-08 | full |
| `SANS-AI-2026` | A SOC Leader's Guide to the 2026 SANS AI Survey (vendor blog summarising the SANS AI Survey; the survey itself was not opened) | Swimlane | vendor | https://swimlane.com/blog/sans-ai-2026-soc-trust/ | 2026-05-18 | full |
| `ELASTIC-SANS-2026` | 2026 SANS SOC Survey: A decade of cyber defense insights (sponsor summary page) | Elastic | vendor | https://www.elastic.co/resources/security/report/sans-soc-survey-insights-2026 | 2026 | full |
| `CISCO-SPLUNK-CONF26-2026` | Splunk .conf26: Tracking the Triage Agent in the Agentic SOC | Cisco Blogs (Cisco and Splunk) | vendor | https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/ | 2026-10-08 | full |
| `SPLUNK-RSACSOC-2026` | From Live Event Telemetry to Action: Lessons from the 10th RSAC SOC | Splunk | vendor | https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html | 2026-08-24 | full |
| `CROWDSTRIKE-AGSOC-2026` | CrowdStrike Delivers the Next Evolution of the Agentic SOC (page shows 'Updated September 18, 2026') | CrowdStrike | vendor | https://www.crowdstrike.com/en-us/blog/crowdstrike-delivers-next-evolution-of-agentic-soc/ | 2026-09-18 | full |
| `COOLEY-UKFIN-2026` | Busy Week for AI: FCA Reopens AI Input Zone, Regulators Issue Statement on Frontier AI Cyber Risks (law-firm summary of the Bank of England / FCA / HM Treasury joint statement of 2026-05-15) | Cooley LLP | press | https://finsights.cooley.com/busy-week-for-ai-fca-reopens-ai-input-zone-regulators-issue-statement-on-frontier-ai-cyber-risks/ | 2026-05-26 | full |
| `AOSHEARMAN-ESRB-2026` | ESRB issues warning on systemic cyber risks from frontier AI models (law-firm summary of the ESRB warning and ESAs press release of 2026-06-25) | A&O Shearman | press | https://finreg.aoshearman.com/esrb-issues-warning-on-systemic-cyber-risks-from-frontier-ai-models | 2026-07-07 | full |
| `ESECURITYPLANET-IBM-2026` | IBM 2026 Cost of a Data Breach Report: Key Findings | eSecurity Planet | press | https://www.esecurityplanet.com/cybersecurity/ibm-2026-cost-of-a-data-breach-report-key-findings/ | 2026-07-30 | full |
| `BAKERDONELSON-IBM-2026` | Ten Takeaways from IBM's 2026 Cost of a Data Breach Report | Baker Donelson | press | https://www.bakerdonelson.com/ten-takeaways-from-ibms-2026-cost-of-a-data-breach-report | 2026 | full |
| `LDS-ARCTICWOLF-2026` | Arctic Wolf Survey Finds AI Trust Gap (news summary of Arctic Wolf's 2026 AI & Cybersecurity Trends Report, released 2026-07-28) | Let's Data Science | press | https://letsdatascience.com/news/arctic-wolf-survey-finds-ai-trust-gap-b12457e5 | 2026-09-14 | full |

Notes on sources: dates for undated web pages (`EC-AIACT-2026`, `EC-NIS2`, `EIOPA-DORA-2025`) are the retrieval date, 2026-10-17. `SANS-SOC-2026` has no publication date on its page; secondary coverage dated 2026-07-16 shows it was available by then. `IBM-CODB-2026` is dated 2026-07 from secondary coverage of 2026-07-30; the page's own metadata is stale. `CROWDSTRIKE-AGSOC-2026` carries an update date, not an original date. Law-firm summaries (`COOLEY-UKFIN-2026`, `AOSHEARMAN-ESRB-2026`) are secondary to the regulator statements. Arctic Wolf survey figures are taken from a news summary (`LDS-ARCTICWOLF-2026`), not the report.

## 6. Gaps

- **Independent measurement in live SOCs.** No published false-negative rate, analyst override rate, parallel-run result or MTTR change from a named production SOC was found. The best measurements are one simulated randomised study (`CSA-SOCBENCH-PR-2025`) and replay benchmarks. This absence is itself a finding.
- **Primary documents not reached.** The ACSC/CISA agentic guidance text (cyber.gov.au failed with a protocol error); the SANS 2026 SOC report body and the SANS AI Survey; the NCSC 'Thinking carefully before adopting agentic AI' blog (page returned only a cookie banner); the Bank of England/FCA/HM Treasury joint statement, the ESRB warning and the ESAs press release (only law-firm summaries read); the NIST Cyber AI Profile; the ISACA report body; the IBM report PDF.
- **Regulatory scope.** No authoritative statement was found on whether SOC AI is high-risk under the EU AI Act, nor on how NIS2 or DORA incident-reporting clocks interact with AI-assisted triage. ISO/IEC 42001 was not read. Search results mentioned Hong Kong SFC/HKMA circulars (2026-06-02) and a Danish regulator outlook; these were not opened. No APAC or Middle East SOC-specific guidance was read.
- **SEC status** rests on search results and one trade-body letter that was not opened; check sec.gov and the Federal Register.
- **Academic coverage.** Abstracts only for all papers; IEEE S&P 2026 and ACM CCS 2026 programs were not mined for SOC papers; the arXiv search endpoint returned HTTP 400 partway through, so paper discovery relied on a few listing pages and search suggestions. CTI-REALM, CyberSOCEval author affiliations were not verified on the abstract pages.
- **Vendors.** Product-level accuracy or outcome claims by named MDR and agentic-SOC vendors (Expel, Arctic Wolf, CrowdStrike, Microsoft Security Copilot agents) were not collected; those belong to the practice angle. Gartner and Forrester research is paywalled.
- **Roles.** No hard data on junior-analyst hiring or analyst headcount changes attributable to AI.
- **Event sessions.** Recordings of the FIRST sessions (Cisco CoAnalyst, Centene, TandemTrace) were not viewed, so only abstracts support those entries.
- **Tool notes.** A text-mirror copy of the IBM page was stale (see 3.9); web search was used 11 times for directions not reachable by link-following.
