# Security operations (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/operations.yaml` (24 entries). Ids are shortened here:
`#05` means `security-operations-05`. Source keys in brackets, such as [SANS-SOC-2026], are given in full in the YAML
or listed in §10. Almost every outcome figure is self-reported by the deploying team or published by a vendor about its
own product or customer. No independent, production-scale measure of AI miss rates or override rates exists yet. Say
so when you quote a figure.

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

The security operations centre (SOC): the team, in-house or bought as a service, that writes detections, watches
alerts, investigates them, decides what is real and acts. It runs from detection engineering (writing and testing the
rules that raise alerts) through Tier-1 triage (first look: benign or escalate), Tier-2/3 investigation, case
management and response actions, and includes managed detection and response (MDR) and managed security service
providers (MSSPs). Incident response after a confirmed breach, threat intelligence and the security of AI systems
themselves are separate modules.

Terms used below: SIEM (the log platform where detections run), SOAR (scripted playbook automation), EDR/XDR
(endpoint or cross-domain detection tools), false positive (an alert on harmless activity), false negative (a real
attack the system missed), recall (share of real attacks caught), MTTR (mean time to respond or resolve).

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Detection engineering | Turn threats, CVEs and reports into rules; test against logs; peer review; deploy | software-systems, expert-judgment | Each rule is slow to write and validate, so coverage is rationed [AMAZON-RULEFORGE-2026]; crowdsourced rules show informal quality control [USENIX-SIGMA-2026] |
| Detection validation and tuning | Check rules still see data; suppress known-benign patterns | review-assurance, software-systems | Rules that "run but can't see" (disconnected, starved, missing fields, ingest lag) [DETENGWEEKLY-165-2026]; benign alerts fire until someone writes the suppression |
| Alert intake and Tier-1 triage | Enrich with user, asset and threat context; close or escalate | transaction-processing | 28% of alerts never investigated (vendor survey) [HNS-GARTNER-2026]; triage varies by shift [DROPZONE-ECS-2026] |
| Investigation (Tier 2/3) | Pivot across SIEM, EDR, identity and cloud logs; build timeline and verdict | research-synthesis, expert-judgment | About 30 minutes per alert by hand [ELASTIC-AGENTICSOC1-2026]; context spread over 20+ tabs [CAUCHY-IRNOTEBOOKS-2026] |
| Hunting that feeds the queue | Look for activity no rule flags, in sources with no detections | research-synthesis | No detections for many SaaS audit logs [GROWTHERAPY-HUNT-2026] |
| Case management and reporting | Attach evidence, write the report, close with a reason | document-production, coordination-scheduling | Closed cases without reasoning teach nothing [FIGMA-AGENTS-2026]; report detail falls with fatigue [CSA-SOCBENCH-PR-2025] |
| Response and containment | Block, isolate, disable, notify | transaction-processing, expert-judgment | A wrong automated action can disrupt the business as badly as an attack [NCSC-AGENTICDEF-2026] |
| MDR service delivery | The same flow sold as a 24/7 service, with customer communication | client-interaction, transaction-processing | Providers cap what they investigate; "AI MDR" labels are hard to compare [EXPEL-GARTNERMDR-2026] |
| SOC measurement and assurance of the AI | Metrics, QA of closures, testing agents before go-live | data-reporting, review-assurance | 70% still name incident count as top metric [SANS-SOC-2026]; no one checks what the AI closed |

Context: SANS 2026 found 79% of SOCs use AI or ML tools but only 36% have built them into a defined workflow
[SANS-SOC-2026]. Use is wide and shallow.

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome with checkpoints), reinvent (the service or operating model changes).
Coverage: augment 11, automate 6, delegate 5, assist 2; step 10, process 11, model 3. Assist is thin: the sources rarely
write up plain copilot use, though SANS says most analysts use AI individually [SANS-SOC-2026]. Model-level change
has three entries, all vendor-reported or hiring data.

**Alert triage**
- Improve: `#02` precedent retrieval shows how similar alerts were closed (Figma: 20% fewer on-call pages). `#03`
  SIEM-embedded triage agents propose a disposition and an analyst decides (Google, Cisco/Splunk event SOCs,
  Microsoft). `#07` an independent challenge must find counter-evidence before an agent may dismiss a finding.
- Automate: `#01` Elastic's pipeline: deterministic checks first, narrow agents, high-confidence false positives
  closed, everything else built into a case (verdict correctness 60% to 92%). `#04` phishing-report triage. `#05` an
  AI SOC analyst investigates every Tier-1 alert and closes the benign majority (ECS 70% auto-closed; vendor case
  study). `#06` calibrated classifiers and "decision models" (models that return a score, not prose) close above a
  threshold (research and vendor claims, grade C).
- Reinvent: `#08` "SOCless": no analysts; AI investigates all alerts and engineers are paged for serious ones (Mysten
  Labs, vendor case study).

**Investigation and case management**
- Improve: `#10` controlled studies: AI-prepared investigations 45-61% faster in a 148-person simulation. `#11`
  agent narratives help new analysts work at Tier 2. `#12` analyst copilots (Microsoft study: 30.13% lower time to
  resolution, observational). `#13` agent drafts the report for sign-off.
- Delegate: `#09` an agent investigates end to end and on-call staff supervise (Figma: about 70% shorter time to
  resolution; Slack's Director/Expert/Critic design).
- Elsewhere: agent-built case notebooks and timelines are security-incident-response-07 and -04; provenance-graph
  root-cause agents are security-incident-response-08.

**Hunting and detection engineering**
- Improve: `#14` LLM triage of anomaly signals surfaced an intrusion no single rule flagged (Hugging Face). `#15` AI
  drafts, translates and scores rules with a separate judge model (Amazon: 336% faster, 67% fewer false positives).
  `#17` the agent drafts the suppression pull request once an analyst confirms a false positive.
- Delegate: `#16` coding agents write, detonate and check attack simulations against the SIEM (DNB). `#18` teams
  build their own agents from playbooks (CrowdStrike customers).
- Elsewhere: scheduled AI hunts over log sources without rules (Grow Therapy, USD 320-510 a month) and Microsoft's
  always-on detection agent are security-threat-intelligence-21 and -22; report-to-rule generation is
  security-threat-intelligence-14.

**Response actions**
- Improve: `#19` agents propose actions that run only through templated, validated commands (Google preview,
  research design). Post-incident containment playbooks: security-incident-response-14.
- Automate: `#20` per-action authority: score each action before it may run unattended; keep agents observable,
  attributable and stoppable (NCSC proposal, grade C).
- Idea: `#24` defender agents that contain an attack with no human in the loop (no deployment found).

**Measurement, service and workforce**
- Improve: `#21` measure the AI: score verdicts against analyst close reasons, sample closures, replay benchmarks
  before widening autonomy.
- Reinvent: `#22` MDR providers move to agent-led, human-accountable services; buyers test what the AI does. `#23`
  SOCs hire about three builders per queue-watching analyst (vendor sample of 665 postings).

Overlaps: incident response holds forensics, notebooks and timelines after a confirmed breach; threat intelligence
holds hunting and report-to-rule work; ai-security holds attacks on the SOC's own AI and agent identity.

## 4. Interview probes

1. **Which alert types does AI close today with no analyst, and what evidence justified that?** Reveals whether
   auto-closure rests on measured agreement, a parallel run, or a vendor demo (`#01`, `#21`).
2. **Who samples what the AI closed, and what miss rate have you measured, on what data?** Reveals whether anyone
   watches false negatives, the worst failure [ARXIV-2610.10608].
3. **Show last month's analyst overrides of AI verdicts. What did you change as a result?** Reveals a working
   feedback loop; Elastic's gain came from context, not a new model (`#01`).
4. **What does a dismissal require that an escalation does not?** Reveals whether the "searches came back empty, so
   benign" trap is controlled (`#07`).
5. **For each action an agent can take (lock an account, isolate a host), who approved it, can it be reversed, and how
   do you stop it?** Reveals the autonomy policy and kill switch (`#19`, `#20`).
6. **What untrusted text (log fields, emails, tickets) reaches your AI tools, and what can the AI do with its
   credentials?** Reveals exposure to log-borne prompt injection (§6).
7. **Do your closed cases carry a reason and notes the AI can learn from?** Reveals readiness for precedent retrieval
   and context grounding (`#02`, `#01`).
8. **Are detections, guides and tool configuration stored as code?** Reveals readiness for draft-PR tuning, rule
   generation and validation loops (`#15`-`#17`).
9. **If you buy MDR, which parts are AI-run and which analyst-run, and can you see the agent's actions?** Reveals
   whether the contract and diligence have caught up (`#22`).
10. **What do you report as SOC metrics today, and did that change after AI?** Reveals activity metrics versus
    decision quality and coverage [SANS-SOC-2026].
11. **How have your Tier-1 seat and the path to Tier 2 changed? Who writes the guides the agents follow?** Reveals
    role redesign and junior-pipeline risk (`#11`, `#23`).
12. **What data may leave your tenant, and do you have a vetted self-hostable model for incidents?** Reveals data
    constraints and the hosted-model refusal risk (`#12`; security-incident-response-03).

## 5. Metrics and benchmarks

| Measure | Typical figure | Source and provenance |
|---|---|---|
| AI use in SOCs | 79% use AI/ML tools; 36% in a defined workflow | [SANS-SOC-2026], survey of 444 practitioners and 69 leaders |
| Top SOC metric | Incident count, 70% (activity, not catches) | [SANS-SOC-2026] |
| AI shortcomings; automated response | 63% report significant shortcomings; automated IR at 39% adoption | [SANS-AI-2026], vendor summary of SANS survey |
| Human review of AI decisions | 57% review every decision before closure; 30% auto-run low-risk actions; none full autonomy | [HNS-GARTNER-2026], vendor survey in sponsored article |
| Home-built AI tooling | 46% of builds abandoned, never in production or replaced | [HNS-GARTNER-2026], vendor survey |
| AI verdict correctness | 60% to 92% vs analyst close reasons | [ELASTIC-ACCURACY-2026], self-reported |
| Cost per investigation | USD 0.69 (specialised agents) vs 3.42 (one 14-skill agent) | [ELASTIC-TOKENS-2026], self-reported |
| Triage time | 30 min to under 3 min (Elastic); 30 min to about 60 s (Google) | [ELASTIC-AGENTICSOC1-2026] self-reported; [TECHINFORMED-GOOGLE-2026] vendor figures |
| Time to resolution | about 70-71% lower (Figma); 30.13% lower with copilot (observational, 150+ orgs, 2024 data) | [FIGMA-AGENTS-2026] self-reported; [MSFT-BONO-2024] vendor-authored study |
| Controlled study | 45-61% faster; 22-29% more accurate (simulated, 148 people) | [CSA-SOCBENCH-PR-2025], vendor-supported |
| Detection rules | 336% faster production; 67% fewer false positives with a judge model | [AMAZON-RULEFORGE-2026], self-reported |
| AI hunting cost | USD 320-510 a month for daily hunts over about 15 sources (security-threat-intelligence-21) | [GROWTHERAPY-HUNT-2026], self-reported |
| Missed attacks in replay | Every approach missed at least 40.4%; challenge-and-judge design 3.1% with 18.4% escalated | [ARXIV-2610.10608], academic, one scenario |
| Triage benchmark | GPT-5 98%, Claude-4.5-Sonnet 96%, GPT-4o-mini 75% on a 100-alert set; best model fully solved 8 of 25 deep-analysis scenarios | [ARXIV-2603.06422], academic (as read by the incident-response governance file) |
| Log-borne prompt injection | Up to 88.2% success at baseline; 8.4% residual after layered defences | [USENIX-LOGINJECT-2026], academic |
| Breach cost | USD 4.99M average, up 12%; USD 1.93M lower with extensive AI and automation | [IBM-CODB-2026], vendor-sponsored research |
| Adversary speed | Average breakout time 29 minutes | [CROWDSTRIKE-AGSOC-2026], vendor |
| US federal logging maturity | Level 3: alerts cover at least 70% of baseline logging; Level 4: at least 95% plus ML/AI tuning | [OMB-M2614-2026], regulator |
| Market stage | AI SOC agents at the Peak of Inflated Expectations, 1-5% penetration (Gartner, as summarised) | [DROPZONE-GARTNERHC-2026], vendor relay |

Not found anywhere: independent production false-negative rates, override rates or parallel-run results from a named
SOC. Advise clients to measure their own (`#21`).

## 6. Guardrails

**Standards and regulators**
- UK NCSC: eight risks for AI-enabled defence, which the governance research proposes as an MDR supplier checklist (an idea) [NCSC-AIADOPT-2026]; a five-part score
  for each defensive action (potency, scope, criticality, rollout confidence, recoverability) [NCSC-AGENTICDEF-2026];
  interim agent controls: log agent activity as security telemetry, make it attributable, keep emergency shutdown,
  name owners, evaluate judge agents independently [NCSC-AGENTICRISK-2026].
- CISA with Australia's ACSC: joint guidance on adopting agentic AI (2026-05-01) [CISA-AGENTIC-2026]. CISA, NIST and
  NSA: ten practices for agent control incidents (2026-10-16) [CISA-KEYPRACTICES-2026]. CISA pages retrieved on
  2026-10-17 show "AI" replaced by "Super Intelligence (SI)"; search for both terms.
- US federal: OMB M-26-14 sets risk-based logging with a maturity model; first agency logging plans due 2026-11-18
  [OMB-M2614-2026, CISA-LOGGING-2026]. AI tuning appears only at the top level, so AI is not mandated.
- NIST: SP 800-53 control overlays for AI systems, including single- and multi-agent use cases [NIST-COSAIS-2026]; SP
  800-61 Rev. 3 for incident response [NIST-SP80061R3-2025].
- EU: NIS2 risk-management and incident duties with management accountability [EC-NIS2]; DORA for financial entities
  and their ICT providers [EIOPA-DORA-2025]; AI Act high-risk obligations from 2027-12-02, with no authoritative
  statement found on whether SOC AI is high-risk [EC-AIACT-2026]. The EU action plan encourages defenders to use AI,
  including open models [EC-ACTIONPLAN-2026].
- US SEC: material incidents disclosed four business days after the materiality determination [SEC-CYBER-2023]; trade
  groups asked for rescission (search-only) [SIFMA-SEC-2026].
- MITRE ATT&CK v20 adds AI techniques, including prompt injection and "Impair Autonomous Defenses", so detection
  content can cover attacks on the SOC's own AI [MITRE-ATTCK-2026]; OWASP's Top 10 for Agentic Applications
  [OWASP-AGENTIC-2025].

**Design guardrails seen in practice**
- Deterministic first: plain queries for predictable checks, agents only for reading and reasoning
  [ELASTIC-AGENTICSOC1-2026]; the NCSC notes SOAR rules are crafted, tested and deterministic [NCSC-AGENTICDEF-2026].
- Conservative closure: only high-confidence false positives; weak matches escalate (`#01`, `#02`, `#07`).
- Treat logs as hostile input: attacker-controlled fields can instruct the analyst model; summarisation is the
  riskiest task [ARXIV-2605.24421, USENIX-LOGINJECT-2026]. Elastic gives its pattern and summary agents no tools [ELASTIC-ACCURACY-2026]. A
  vendor SOC assistant was reported steerable by an alert into minting API keys [PROMPTARMOR-ELASTIC-2026].
- Controls outside the prompt: draft-only pull requests set by a workflow step, no ambient channel access
  [FIGMA-AGENTS-2026]; closed action vocabularies [ARXIV-2610.09906].
- Data handling: zero-retention inference [ELASTIC-AGENTICSOC1-2026]; local models [NDSS-WOSOC-2026,
  HUGGINGFACE-INCIDENT-2026].

**Steps that need human judgment**
- Any action touching users, availability, executives or production [SPLUNK-RSACSOC-2026, EXPEL-3LEADERS-2026].
- Approving each level of agent autonomy, and withdrawing it [NCSC-AGENTICDEF-2026].
- Final review of detection rules before production [AMAZON-RULEFORGE-2026].
- Dispositions on escalated, low-confidence or contested alerts; sampling what the AI closed (`#21`).
- Customer-facing MDR decisions; Gartner's quoted definition keeps MDR "human-led" [EXPEL-GARTNERMDR-2026].

## 7. Roles and how they evolve

- **Tier 1 analysts** move from gathering context to reviewing agent-prepared findings [CISCO-SPLUNK-CONF26-2026];
  on-call engineers at Figma and Slack now supervise investigations [FIGMA-AGENTS-2026, SLACK-AGENTS-2025].
- **Detection engineers** write investigation guides the AI follows as instructions [ELASTIC-ACCURACY-2026], review
  generated rules [AMAZON-RULEFORGE-2026] and act more like site-reliability engineers [DETENGWEEKLY-162-2026].
- **New analysts** reached Tier 2 work with agent support at one event SOC [SPLUNK-CISCOLIVE-2026]. But entry-level
  roles were 5.9% of 665 postings, and D3 warns that cutting junior seats empties the senior bench
  [D3-SOCHIRING-2026]; Forrester heard of a "five-year problem" [FORRESTER-RSAC-2026].
- **Builders**: postings show about three engineering seats per analyst seat [D3-SOCHIRING-2026]; Robinhood
  advertises a "Security Operations AI Tech Lead" [ROBINHOOD-JOB-SECOPSAI-2026].
- **Owners of agents**: NCSC advice implies a named owner for each agent's activity [NCSC-AGENTICRISK-2026]. Vendor
  visions of a "SOC Agent Engineer" by 2030 are not evidence of practice [DROPZONE-JD2030-2026].
- **Headcount**: no source reports cuts; ECS and Zapier describe avoiding hires [DROPZONE-ECS-2026,
  DROPZONE-ZAPIER-2026]. ISC2: AI is the top skills need (41%) and SOC roles are "evolving" [ISC2-WORKFORCE-2025].
  SANS: meaningful work and progression outrank pay for retention [SANS-SOC-2026].

## 8. Frontier

- 2026-03-31: Forrester says "agentic SOC" is used loosely [FORRESTER-RSAC-2026].
- 2026-05-01: first joint government guidance on agentic AI adoption [CISA-AGENTIC-2026].
- 2026-06: Google's triage agent generally available; detection-engineering, hunting and containment agents in
  preview [TECHINFORMED-GOOGLE-2026]. FIRST sessions test Tier-1 triage with general LLMs [FIRST-CON-2026].
- 2026-06-05: Gartner Hype Cycle puts AI SOC agents at the peak [DROPZONE-GARTNERHC-2026].
- 2026-07-27 to 08-21: SACR argues triage is becoming commodity and the "action gap" is the frontier
  [SACR-TRUSTEDSOC-2026, SACR-BHUSA-2026].
- 2026-08-27 to 09-03: scenario evaluations spread; teams build their own harnesses [UNSECURE-EVAL-2026,
  DETENGWEEKLY-169-2026].
- 2026-09-09: Gartner (as quoted) expects 90% of initial MDR findings handled by AI without human action by 2029,
  up from 30% [EXPEL-GARTNERMDR-2026].
- 2026-09-18: CrowdStrike orchestrator agents and detection inside the data pipeline, both pre-beta
  [CROWDSTRIKE-AGSOC-2026].
- 2026-09-21: NCSC plans an "AI for Cyber Defence" problem book and names Cyber Shield, a national agentic defence
  effort [NCSC-AGENTICDEF-2026].
- 2026-10-06/07: evidence-gated triage and constrained-action remediation preprints [ARXIV-2610.10608,
  ARXIV-2610.09906].
- 2026-10-16: decision models proposed as cheap, auditable per-alert scorers [THN-DECISIONMODELS-2026]; CISA, NIST
  and NSA publish agent-incident practices [CISA-KEYPRACTICES-2026].

## 9. Common objections

- **"AI will wave real attacks through."** Fair: every approach in one benchmark missed at least 40.4% of attack
  alerts [ARXIV-2610.10608]. Response: close only high-confidence false positives (`#01`), require counter-evidence
  to dismiss (`#07`), and sample closures for misses (`#21`).
- **"It hallucinates, so analysts won't trust it."** Elastic analysts did ignore summaries that were wrong 40% of the
  time; accuracy rose to 92% by adding context, not changing models [ELASTIC-ACCURACY-2026]. Zapier cites visible
  queries and evidence as the basis for trust [DROPZONE-ZAPIER-2026].
- **"It costs more than people."** Expel's CEO said many firms find this once licences and tokens are counted
  [EXPEL-3LEADERS-2026]. Design matters: specialised agents cost USD 0.69 per alert against 3.42 for one generalist
  agent [ELASTIC-TOKENS-2026]; Grow Therapy's hunts run for USD 320-510 a month [GROWTHERAPY-HUNT-2026].
- **"Attackers will steer our AI through the logs."** True in research [USENIX-LOGINJECT-2026]. Response: no-tool
  summarisers, closed action sets, human approval for actions, injection red-teaming (§6).
- **"Who owns the mistake?"** "You want a human to be able to own that mistake" [EXPEL-3LEADERS-2026]. Response: name
  owners per agent and grant authority per action [NCSC-AGENTICRISK-2026, SACR-TRUSTEDSOC-2026].
- **"Every vendor says agentic."** Gartner warns of agent washing [DROPZONE-GARTNERHC-2026]; SACR counts close to 140
  vendors touching AI in security operations [SACR-AISOCMKT-2026]. Response: proof of value on your own alerts and a
  side-by-side run (`#05`, `#21`).
- **"We tried building it ourselves and it failed."** 46% of home builds were abandoned or replaced (vendor survey)
  [HNS-GARTNER-2026]. Figma, Elastic and Grow Therapy report results from built systems that rely on memory, critics and staged rollout
  (`#01`, `#09`; security-threat-intelligence-21).
- **"Our data can't leave, and hosted models refuse attack content."** Local and open-weight models worked for a
  university SOC and for Hugging Face during an incident [NDSS-WOSOC-2026, HUGGINGFACE-INCIDENT-2026].
- **"Faster to the wrong answer."** AI SOCs depend on the data fed to them [RESILIENTCYBER-FASTER-2026]. US federal
  rules now measure logging coverage per system [OMB-M2614-2026]; ask what the client's coverage is.

## 10. Sources

Keys cited above that are not in the YAML (all others are given in full there):

- CISA-AGENTIC-2026: CISA with ASD's ACSC, "Careful Adoption of Agentic AI Services", 2026-05-01, https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services
- CISA-LOGGING-2026: CISA, Logging Reference Architecture press release, 2026-08-20, https://www.cisa.gov/news-events/news/cisa-releases-foundational-flexible-guidance-help-federal-agencies-implement-effective-logging
- OMB-M2614-2026: US OMB, Memorandum M-26-14 on agency logging, 2026-05-22, https://www.whitehouse.gov/wp-content/uploads/2026/05/M-26-14-Ensuring-Effective-and-Efficient-Agency-Logging-and-Network-Visibility-to-Defend-Against-Evolving-Cyber-Threats.pdf
- NIST-COSAIS-2026: NIST, SP 800-53 Control Overlays for Securing AI Systems, 2026-01-08, https://csrc.nist.gov/projects/cosais
- NIST-SP80061R3-2025: NIST SP 800-61 Rev. 3, 2025-04, https://csrc.nist.gov/pubs/sp/800/61/r3/final
- EC-NIS2: European Commission, NIS2 Directive page, checked 2026-10-17, https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
- EC-AIACT-2026: European Commission, AI Act page, checked 2026-10-17, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EC-ACTIONPLAN-2026: European Commission, EU Action Plan on Cybersecurity and AI, 2026-07-07, https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence
- SEC-CYBER-2023: US SEC, cyber incident disclosure rules, 2023-07-26, https://www.sec.gov/newsroom/press-releases/2023-139
- SIFMA-SEC-2026: SIFMA and trade associations, letter on Regulation S-K cyber disclosures, 2026-04-10 (search-only), https://www.sifma.org/advocacy/letters/reforming-regulation-s-ks-cybersecurity-disclosures-joint-trades
- MITRE-ATTCK-2026: MITRE, ATT&CK v20 release notes, 2026-10-13, https://attack.mitre.org/resources/updates/
- OWASP-AGENTIC-2025: OWASP, Top 10 for Agentic Applications for 2026, 2025-12-09, https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- USENIX-LOGINJECT-2026: Karanjai et al., "Context Contamination in LLM Analysis of Network Security Logs", USENIX Security 2026, 2026-08, https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai
- IBM-CODB-2026: IBM and Ponemon, Cost of a Data Breach Report 2026, 2026-07, https://www.ibm.com/reports/data-breach
- SACR-AISOCMKT-2026: Software Analyst Cyber Research, "The AI SOC Market, 2026", 2026-07-30, https://softwareanalyst.substack.com/p/ai-soc-technoscope-series-the-ai
- CAUCHY-IRNOTEBOOKS-2026: DNB Cyber Defense Center (Kyrre Wahl Kongsgard), "Agentic incident response notebooks", 2026-06-19, https://blog.cauchy.org/blog/incident-response-notebooks/ (CAUCHY-IRNB-2026 in the operations inputs; the use case is security-incident-response-07)
- DROPZONE-JD2030-2026: Dropzone AI, "SOC Analyst Job Description: Rewriting It for 2030", 2026-05-13, https://www.dropzone.ai/blog/soc-analyst-job-description-2030
- RESILIENTCYBER-FASTER-2026: Resilient Cyber, "Faster to the Wrong Answer" (partner content with Censys), 2026-10-14, https://www.resilientcyber.io/p/faster-to-the-wrong-answer
