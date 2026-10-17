# Incident response (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/incident-response.yaml` (22 entries). Ids are shortened
here: `#05` means `security-incident-response-05`; other modules' ids are in full and not repeated here. Source keys in brackets, such as [GOOGLE-IRGENAI-2024], are in
the YAML or in §10. Almost every outcome figure is self-reported by the deploying organisation, published by a vendor,
or a lab benchmark. No independent production measure of AI in incident response exists yet: no override rates, no
parallel runs, no inspection findings. Say so when you quote a figure.

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

Responding to security incidents once they are declared: preparation (plans, playbooks, tabletop exercises), digital
forensics and investigation (DFIR: collecting evidence, building timelines, finding root cause), containment and
recovery (including backup-based cyber recovery and business continuity), and reporting to regulators, customers and
leadership. Since mid-2026 it also covers incidents caused by AI agents themselves. Alert triage before an incident is
declared sits in security-operations; agent containment controls sit in ai-security.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Plans and playbooks | Write and maintain the IR plan, runbooks and escalation paths | document-production, review-assurance | Updated reactively; 48% don't know if they have AI incident playbooks [ISACA-SOC-2026] |
| Exercises | Tabletops, drills, crisis simulations | coordination-scheduling | Scenarios written once a year go stale; 64% have run no AI-related IR exercise [ISACA-SOC-2026] |
| Readiness | Log retention, model access, clean recovery baselines, retainers | software-systems | Hosted models refused attack payloads mid-incident [HF-DISCLOSURE-2026]; agent prompt context lost to log retention [SANS-DFIRSUMMIT-2026] |
| Declare and escalate | Turn signals into an incident with a severity and an owner (triage itself: security-operations) | review-assurance | Early signs not escalated at OpenAI [OPENAI-HFROAD-2026]; Hugging Face's AI correlation did not raise criticality [HF-TIMELINE-2026] |
| Investigate and scope | Collect, normalise logs, build timelines, trace root cause, memory/disk/malware forensics | research-synthesis, data-reporting, expert-judgment | Hundreds of millions of log records [GOOGLE-TIMESKETCH-2025]; a host triage takes an analyst a day [SANS-FINDEVIL-2026]; 10-20 minutes per high-severity alert [ARXIV-2607.09176] |
| Contain and eradicate | Isolate hosts, revoke credentials, freeze pipelines | transaction-processing, software-systems | Median 22 seconds from initial access to hand-off in 2025 [MANDIANT-MTRENDS-EXEC-2026] |
| Recover | Decide what is clean, restore in order, validate | coordination-scheduling, expert-judgment | Attackers target backups, identity and hypervisors ("recovery denial") [MANDIANT-MTRENDS-2026] |
| Notify and report | Regulator, customer and public notices on statutory clocks | document-production, review-assurance | Clocks of 4, 6, 24 and 72 hours start before forensics ends; "major", "significant", "material" are legal calls |
| Communicate | Executive and stakeholder updates during the incident | document-production | Close to an hour per summary [GOOGLE-IRGENAI-2024] |
| Learn | Post-incident review, close findings, update policy | review-assurance | Few AI cases; Cloudflare's reviewer blocks closure of high-severity incidents until findings are addressed (`#16`) |
| AI-agent incidents (new) | Detect, halt, investigate and report incidents where an agent is the actor | expert-judgment, coordination-scheduling | Affected organisations in CERT-In's cases did not detect agent access [CERTIN-CIAD0049-2026]; 56% don't know how fast they could halt an AI system [ISACA-AIPULSE-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (`change_scope: model`, or a flow that is rebuilt). Evidence is densest
in investigation and in the new AI-agent incident work; recovery and exercises are thin and vendor-led.

**Prepare and exercise**
- Improve: `#01` AI checks the IR plan against NIST SP 800-61 and flags stale steps (Fortinet proof of concept).
  `#02` AI builds tabletop scenarios from your own playbooks (Immersive release, 2026-10-01; CIS guidance).
  `#03` keep a vetted self-hosted model ready, so forensic AI is not blocked by provider guardrails (Hugging Face).
- Before trusting an investigation agent, benchmark it on ground-truth scenarios (`security-operations-22`); 5 of 7
  frontier models hard-failed one published scenario (vendor test) [COTOOL-AGENTICSOC-2026].

**Investigate and scope**
- Improve: `#04` LLM agents rebuild timelines from logs and artifacts, validated before export (Hugging Face "hours
  instead of days", Google Timesketch, Centene). `#06` plain-language questions over forensic evidence with linked
  citations (Magnet). Agent-built case notebooks (DNB) and Centene's OCSF pipeline: `security-operations-12`.
  `#08` rank likely root-cause code changes (Meta 42% backtest accuracy; reliability incidents, not security).
  `#09` verify AI findings (existence checks, judge model) and harden tools against attacker-written logs; the
  dismissal challenge is `security-operations-07`.
- Delegate: `#05` an agent drives forensic tools for host triage and ties findings to artifacts (SANS Protocol SIFT,
  14-minute demo; not validated for court). `#07` provenance-graph root-cause agent with daily sampled audit, above 96%
  verified success versus 64.7% for the legacy tool (unnamed SOC; preprint). Mandiant's source-code harness inside IR
  engagements: `security-vulnerability-exposure-04`.

**Contain and recover**
- Improve: `#10` console recommends triage, containment and remediation actions (Microsoft guided responses).
  `#13` find the last clean restore point, flag bad backups, draft runbooks (Rubrik, N2WS; vendor scenarios).
- Automate: `#11` guardrailed automated containment with pre-authorised human override (Unit 42, NIST, CISA advice).
- Delegate (idea): `#12` LLM plans response and recovery, each action checked in a digital twin first. Closed-command
  containment is `security-operations-20`; autonomous containment, the idea `security-operations-25`.

**Communicate, report and learn**
- Improve: `#14` draft incident summaries and executive updates (Google: 51% less time per summary, 300 summaries;
  the module's only measured A outside AI-agent work). `#15` draft regulator notifications inside parallel clocks
  (vendor-only evidence). `#16` AI reviews post-incident reports against standards before closure (Cloudflare).
  SOC investigation reports drafted for sign-off: `security-operations-14`.

**Incidents caused by AI agents (new scope)**
- Improve: `#17` treat agent control incidents as a new class: scoped identities, stop rules, drills, halt authority
  (NIST/NSA/CISA practices, CERT-In). `#20` staged AI review of about 50 PB of agent records found outside
  organisations to notify; a person confirms every case (OpenAI, over 100 notified).
- Automate: `#18` reconstruct agent actions from tamper-resistant logs (Uber ADR, 200,000+ sessions a day, as
  reported). `#19` monitors page responders; severe alerts pause unless cleared in 30 minutes (OpenAI, Anthropic).
- Reinvent: `#21` cross-organisation reporting of agent incidents and near-misses (SAFE draft; OpenAI notifications).
  `#22` responders become builders of agentic automations (Databricks, GitLab, Twilio, Cloudflare postings).

**Gaps.** No delegate entry has a named deployment with outcomes; no model-scope entry has measured results. No AI use
in business-impact analysis, recovery-time testing or a real exercise was found.

## 4. Interview probes

1. **"Take your last serious incident. Where did the hours go: evidence collection, timeline, root cause, writing
   updates, or regulator notices?"** Reveals the pain point; writing (`#14`, `#15`) is the best-evidenced quick win.
2. **"Which clocks started (DORA, NIS2, SEC, CERT-In, contracts), who decided 'major' or 'material', and how many hours
   passed between awareness and that decision?"** Reveals where a draft could help and which calls must stay human.
3. **"When an AI tool gives you a timeline or root cause, what does a person check before it reaches a report,
   regulator or court? Can you show which statements were machine-made?"** Reveals defensibility (`#04`, `#05`, `#09`).
4. **"Do you measure audited accuracy of AI investigations, or only what the tool reports about itself?"** Reveals
   whether any quality evidence exists; SherAgent's legacy tool overstated its own rate (`#07`).
5. **"Which of your forensic or SOC tools already have an LLM feature? Have you tested them with a poisoned log, email
   or ticket note?"** Reveals exposure to log-borne prompt injection (`#09`).
6. **"If your hosted model refused to analyse attacker payloads mid-incident, what is your fallback and who approved
   it?"** Reveals model-access readiness (`#03`) and data-handling rules for incident data.
7. **"Which response actions may run without approval today, and who can override or revoke them?"** Reveals the
   automation boundary (`#11`); in one sponsored survey 57% review every AI decision before closing an alert.
8. **"How do you decide which restore point is clean, and who approves a restore an AI proposes?"** Reveals recovery
   maturity and recovery-denial exposure (`#13`).
9. **"Have you run an exercise where an AI agent or coding assistant is the actor? Do logs keep tool calls and prompt
   context long enough to investigate?"** Reveals AI-incident readiness (`#17`, `#18`).
10. **"If one of your agents reached a customer's system, who must be told, how fast, and what evidence do you keep?"**
    Reveals notification readiness (`#21`) and AI Act Article 73 exposure if you provide high-risk AI.
11. **"Who in the team builds and maintains your AI tooling, and has any home-built tool been dropped?"** Reveals the
    operating model (`#22`); 46% of self-built tools in one vendor survey did not last.
12. **"When did you last update the IR plan, and against which version of NIST SP 800-61?"** Reveals plan currency
    (`#01`); Rev. 3 (April 2025) replaced Rev. 2.

## 5. Metrics and benchmarks

**Baselines to ask for first**
- Time per incident summary and executive update (Google: close to an hour) [GOOGLE-IRGENAI-2024].
- Hours from awareness to classification, and from classification to each filing (`#15`).
- Time to triage a host or high-severity alert (analyst day per host [SANS-FINDEVIL-2026]; 10-20 minutes per alert
  in a 10-person user study [ARXIV-2607.09176]).
- Dwell time and hand-off speed: global median dwell 14 days in 2025, up from 11; hand-off 22 seconds, down from more
  than 8 hours in 2022; exploits the top initial vector at 32% (Mandiant, 500,000+ investigation hours; report body
  gated) [MANDIANT-MTRENDS-2026].

**Named outcomes (self-reported; mostly effort, not accuracy)**
- Google: 51% less time per summary (300 summaries); LLM summaries rated 10% higher in a 50-vs-50 blind test; 53% less
  time on executive updates (2024) `#14`.
- OpenAI: about 50 PB reviewed, over 100 organisations notified, about 7,000 GPUs, 45 minutes to days per human case `#20`.
- SherAgent (unnamed SOC, preprint): above 96% verified success on 980 sampled cases vs 64.7% audited legacy; under
  USD 0.10 and 4 minutes per investigation `#07`.
- Meta: 42% root-cause accuracy in backtesting (reliability incidents) `#08`. Grafana: 3.5x faster on one incident.
- Hugging Face: about 17,600 attacker actions reconstructed, "hours instead of days", no error rate `#04`.
- SANS: 14-minute host investigation demo; 119 of 143 artifacts in one judge's run `#05`.

**Vendor claims (grade C; ask for a named, measured case)**: D3 alert-to-filing about 40 minutes (scenario) `#15`;
Rubrik AI "trusted by one-third" of customers `#13`; Magnet: 68% of 350+ DFIR professionals use AI `#06`.

**Lab benchmarks (independent; quote as limits, not performance)**
- SIABench: best of 11 LLMs fully solved 8 of 25 incident-analysis scenarios; 33.33% on hard memory forensics [ARXIV-2603.06422].
- ALERT-BENCH: every agent approach missed at least 40.4% of attack alerts; a challenge-step design missed 3.1% [ARXIV-2610.10608].
- Log prompt injection: up to 88.2% attack success; layered defences cut it 90.4%, leaving 8.4% [USENIX-LOGINJECT-2026].
- Cotool scenario: 5 of 7 frontier models hard-failed; best 29% of weighted score (vendor) [COTOOL-AGENTICSOC-2026].

**Adoption and readiness surveys**
- SANS 2026: 79% of SOCs use AI or ML tools, 36% in a defined workflow; 70% still cite incident count as the top
  metric [SANS-SOC-2026]. Automated incident response at 39% adoption (vendor summary) [SANS-AI-2026].
- ISACA 2026 (1,800+): 8% run regular AI-specific response exercises, 64% none; 48% lack or don't know of AI incident
  playbooks; 42% highly confident in detection and response; 58% understaffed [ISACA-SOC-2026].
- ISACA AI Pulse (3,400+): 56% don't know how fast they could halt an AI system [ISACA-AIPULSE-2026]; 35% of European
  organisations can't say if they were hit by an AI-powered attack [ISACA-AIPULSE-EU-2026].
- Sponsored survey: 57% require human review of every AI decision; none grant full autonomy [HELPNET-GARTNER-2026].

**What to measure (recommend these, not hours alone)**: audited accuracy on sampled cases versus the tool's own claims;
missed-attack rate on ground-truth scenarios before go-live; reviewer edits and overrides on AI drafts; time from
awareness to classification and to each filing; share of findings traced to an artifact; injection test results;
halt time for AI systems in drills; restore-point accuracy in recovery tests.

## 6. Guardrails

**Reporting clocks (the rules govern timing, not tools; none of the texts read mentions AI as a responder tool)**
- **DORA** (EU finance): initial report within four hours of classifying an incident as major and no later than 24
  hours from awareness; intermediate within 72 hours; final within one month [EUR-LEX-DORA301-2025].
- **NIS2**: early warning 24 hours, notification 72 hours, final report one month [EUR-LEX-NIS2-2022].
- **Cyber Resilience Act**: manufacturers' 24-hour and 72-hour reports apply from 2026-09-11 [EUR-LEX-CRA-2024].
- **EU AI Act Art. 73**: providers of high-risk AI report serious incidents, outer limit 15 days; Annex III
  obligations moved to 2027-12-02 [FLI-AIACT73-2024; EC-AIACT-2026].
- **US**: SEC Form 8-K Item 1.05 four business days after a materiality determination, under a rescission push with no
  final action found [SEC-CYBER-2023; SIFMA-SEC-2026]; CIRCIA not yet in force [FR-CIRCIA-2026]. **India**: CERT-In 6
  hours [CERTIN-BLUEPRINT-2026]. **UK**: a bill would add 24 and 72-hour reporting [GOVUK-CSRB-2025].

**Standards and guidance**
- NIST SP 800-61 Rev. 3 is the reference lifecycle; it keeps manual selection of containment as an option [NIST-80061R3-2025].
- NIST/NSA/CISA ten key practices for agent control incidents (2026-10-16, voluntary): drills, tamper-resistant logs,
  shutdown, verified containment before restart, notification; AI may assist investigations if humans verify key facts
  and a different model family cross-checks [NIST-KEYPRACTICES-2026].
- CISA/ACSC agentic guidance: tested IR for agent compromise; a validating agent before execution; human review of
  guardrail triggers [CISA-AGENTIC-2026]. CERT-In: per-run least-privilege agent identities, egress blocks, auto-stop for test runs [THN-CERTIN-2026].
- Evidence in court: proposed US Rule 707 on machine-generated evidence went back for revision in June 2026
  [PROSKAUER-FRE707-2026]; SANS says Protocol SIFT is not validated for evidentiary use [SANS-PROTOCOLSIFT-2026].

**Design guardrails seen in deployments**
- The AI drafts; a named person accepts, edits or discards (`#14`, `#15`). Every finding links to a source artifact (`#05`, `#06`).
- Logging off and no retraining on incident data [GOOGLE-IRGENAI-2024]; self-hosted models for attacker data (`#03`).
- Treat logs, emails, tickets and artifacts as hostile input; validate structured output; least privilege (`#09`).
- Audit sampled AI investigations against ground truth, not the tool's self-report (`#07`); test on scenarios first (`security-operations-22`).
- Closed command sets, pre-approved actions and break-glass revocation for anything automated (`#11`, `#12`).

**Steps that stay with a person**: declaring "major", "significant" or "material"; approving every external filing;
choosing containment that affects the business; approving a restore point; deciding whether to notify a third party;
restarting a halted agent; signing anything that may go to court.

## 7. Roles and how they evolve

- **Writers become editors.** Incident commanders review and correct drafts and keep accountability [GOOGLE-IRGENAI-2024].
- **Analysts become supervisors and challengers.** Centene's speakers describe "supervisory decision-makers" (their own
  framing) [FIRST-CON-2026]; a SANS instructor asks where challenge skills come from if AI does junior work [SANS-SIMON-2026].
- **Responders become builders.** Databricks, GitLab, Twilio and Cloudflare postings require or prefer AI and agent
  skills alongside core DFIR (`#22`). ISACA: 45% see LLM SecOps as a skill gap; 51% now help implement AI [ISACA-SOC-2026].
- **New duties for AI-agent incidents**: agent indicators, drills, halt authority, on-call for agent behaviour shared
  by security engineers and AI researchers (`#17`, `#19`).
- **Learning curve.** A third of 40+ SANS students found it harder to state investigative intent than to type
  commands [ROBLEE-SUBSTACK-2026]. ISC2: incident responder is "evolving", not disappearing [ISC2-WORKFORCE-2025].
- **Event SOC model.** Cisco/Splunk kept tier 1-3 analysts and detection engineers around its triage agent, with
  analysts validating output [CISCO-SPLUNK-CONF26-2026]. No data on junior hiring or headcount effects was found.

## 8. Frontier

- **2026-01-16 / 03-09** SANS launches Protocol SIFT, an AI layer over forensic tools [ROBLEE-SUBSTACK-2026; SANS-PROTOCOLSIFT-2026].
- **2026-05-14** NIST workshop on AI incident management [NIST-AIINCIDENTWS-2026].
- **2026-06** FIRST: DFIR tools add LLM features and are attacked through artifacts; Centene's AI timelines [FIRST-CON-2026].
- **2026-07-07** EU Action Plan: an ENISA/JRC testing platform for AI in cybersecurity, including incident response [EC-ACTIONPLAN-2026].
- **2026-07-16 to 09-30** Hugging Face discloses an agent-driven intrusion and AI-assisted forensics; OpenAI overhauls its IR
  and notifies 100+ organisations [HF-DISCLOSURE-2026; OPENAI-HFROAD-2026; OPENAI-HFREVIEW-2026].
- **2026-08-04/05** SAFE draft for sharing agent incidents and near-misses [SILICONANGLE-SAFE-2026].
- **2026-09-15** Rubrik exposes recovery data to customers' agents through MCP (private preview) [RUBRIK-MCP-2026].
- **2026-10-01** AI crisis-simulation builder released [IMMERSIVE-AIBUILDER-2026]. Risky Business reports OpenAI found dozens
  of examples of agents acting in undesirable ways [RISKYBIZ-2026].
- **2026-10-15/16** CERT-In advisory on agents reaching live systems; NIST/NSA/CISA key practices; SANS DFIR Summit on forensics
  when "the AI system was the victim" [CERTIN-CIAD0049-2026; NIST-KEYPRACTICES-2026; SANS-DFIRSUMMIT-2026].
- **2026 Q3** Forrester's IR-services landscape names AI-agent incident response and defensibility of AI-assisted IR as
  buyer scenarios (landing page only) [FORRESTER-IR-2026].

## 9. Common objections

- **"AI makes things up; we can't put that in a report."** Real: SherAgent's legacy tool wrote plausible wrong reports
  (`#07`). Answer: link every claim to an artifact, run existence checks, sample-audit (`#05`, `#09`).
- **"It won't stand up in court."** Open question: Rule 707 is unsettled and SANS disclaims evidentiary use. Magnet frames
  AI output as leads, not conclusions, and says to record which tasks were AI-assisted (`#06`).
- **"The AI can be manipulated by the attacker's own data."** True: up to 88.2% attack success in a lab, 8.4% residual
  with layered defences. Treat inputs as hostile and keep a human on conclusions (`#09`).
- **"Hosted models refuse our work."** It happened to Hugging Face. Pre-approve a self-hosted or trusted-access model (`#03`).
- **"Agentic is hype."** Partly: Cotool says the label covers different systems, some fully deterministic
  [COTOOL-AGENTICSOC-2026]; Splunk's RSAC SOC authors said theirs was not fully agentic [SPLUNK-RSACSOC-2026]. Ask
  what the system does, and test on scenarios (`security-operations-22`).
- **"The savings figures are vendor numbers."** Mostly true. The best measured case is Google's 2024 summary study (`#14`).
- **"We built our own and it didn't last."** Common: 46% of self-built tools failed or were replaced in a sponsored
  survey [HELPNET-GARTNER-2026]. Budget for upkeep (`#22`).
- **"The Hugging Face case is an AI scare story."** One blog calls it a classic isolation failure [UPHACK-HF-2026], and
  a podcast host asked whether firms use such incidents to sell products [REGISTER-BHDC-2026]. Either way, the response
  lessons (logs, halt authority, notification) hold (`#17`-`#19`).
- **"Regulators will object to AI-drafted notices."** No regulator statement on AI-drafted notices was found. Even the
  vendor says classification needs human review before filing; keep classification and sign-off human (`#15`).

## 10. Sources

Full details (title, publisher, type, URL, date, access) are in the YAML for every key used there.
- **Regulators and standard-setters:** NIST-KEYPRACTICES-2026, NIST-80061R3-2025, CISA-AGENTIC-2026, CERTIN-CIAD0049-2026,
  CERTIN-BLUEPRINT-2026, EUR-LEX-DORA301-2025, EUR-LEX-NIS2-2022, EUR-LEX-CRA-2024, FLI-AIACT73-2024, EC-AIACT-2026,
  SEC-CYBER-2023, FR-CIRCIA-2026, CISA-CIRCIA-2026, GOVUK-CSRB-2025, CIS-TTXGENAI-2025.
- **Professional bodies and surveys:** ISACA-SOC-2026, ISACA-AIPULSE-2026, ISC2-WORKFORCE-2025, SANS-SOC-2026,
  SANS-PROTOCOLSIFT-2026, SANS-FINDEVIL-2026, SANS-SIMON-2026, SIFMA-SEC-2026.
- **Firms and in-house teams:** GOOGLE-IRGENAI-2024, OPENAI-HFREVIEW-2026, OPENAI-HFROAD-2026, OPENAI-HFINC-2026,
  ANTHROPIC-ALIGNSEC-2026, ANTHROPIC-EVALINC-2026, HF-DISCLOSURE-2026, HF-TIMELINE-2026, META-RCA-2024,
  CLOUDFLARE-CODEX-2026, METR-OAIHF-2026, PROSKAUER-FRE707-2026, HUNTON-OMNIBUS-2025.
- **Vendors:** MANDIANT-AIRR-2026, MANDIANT-MTRENDS-2026, MANDIANT-MTRENDS-EXEC-2026, MS-LEARN-DEFENDERCOPILOT-2026,
  MAGNET-DFIR-2026, D3-DORA-2026, RUBRIK-MCP-2026, N2WS-AIDR-2026, IMMERSIVE-AIBUILDER-2026,
  CYBERTRIAGE-HALLU-2026, UNIT42-AIATTACK-2026, SANS-AI-2026, GRAFANA-AIINC-2026.
- **Academic:** ARXIV-2603.06422, ARXIV-2607.09176, ARXIV-2610.10608, ARXIV-2605.24421, USENIX-LOGINJECT-2026,
  ARXIV-2608.15016, NDSS-HAMMAR-2026, ARXIV-2610.09906, ARXIV-2507.14201, ARXIV-2601.03287.
- **Conferences, press, community, jobs:** FIRST-CON-2026, SANS-DFIRSUMMIT-2026, BSIDESLV-2026, GOOGLE-TIMESKETCH-2025,
  WIRED-OPENAI-2026, THN-CERTIN-2026, SILICONANGLE-SAFE-2026, AXIOS-SAFE-2026, HELPNET-GARTNER-2026, UPHACK-HF-2026,
  DATABRICKS-JOB-2026, GITLAB-JOB-2026, TWILIO-JOB-2026, CLOUDFLARE-JOB-2026, BLOCK-JOB-2026.
- **Not in the YAML (opened by the research angles):** COTOOL-AGENTICSOC-2026 (Cotool, *A scenario to evaluate your
  Agentic SOC*, 2026-08-27, https://unsecure.sh/blog/agentic-soc-scenario/; vendor test);
  ISACA-AIPULSE-EU-2026 (ISACA, *A Third of European Organisations
  Don't Know if They've Been Hit by an AI-Powered Cyberattack*, 2026-06-17,
  https://www.isaca.org/about-us/newsroom/press-releases/2026/a-third-of-european-organisations-dont-know-if-they-have-been-hit-by-an-ai-powered-cyberattack);
  NIST-AIINCIDENTWS-2026 (NIST, *Workshop on AI Incident Management*, 2026-05-14,
  https://www.nist.gov/news-events/events/2026/05/nist-workshop-ai-incident-management);
  EC-ACTIONPLAN-2026 (European Commission, *EU Action Plan on Cybersecurity and AI*, 2026-07-07,
  https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence);
  CISCO-SPLUNK-CONF26-2026 (Cisco, *Tracking the Triage Agent in the Agentic SOC at Splunk .conf26*, 2026-10-08,
  https://blogs.cisco.com/security/conf26-agentic-soc-triage-agent/);
  SPLUNK-RSACSOC-2026 (Splunk, *Lessons from the 10th RSAC SOC*, 2026-08-24,
  https://www.splunk.com/en_us/blog/security/lessons-from-the-10th-rsac-soc.html);
  FORRESTER-IR-2026 (Forrester via Palo Alto Networks, *Cybersecurity Incident Response Services Landscape, Q3 2026*,
  landing page, 2026, https://www.paloaltonetworks.com/unit42/forrester-IR-landscape-report.md);
  RISKYBIZ-2026 (Risky Business, *Srsly Risky Biz: "Rogue" AI Isn't Going Anywhere*, 2026-10-01,
  https://risky.biz/srsly-risky-biz-rogue-ai-isnt-going-anywhere/);
  REGISTER-BHDC-2026 (The Register, *Black Hat and DEF CON are AI conferences now, too*, podcast transcript, 2026-08-17,
  https://www.theregister.com/security/2026/08/17/black-hat-and-def-con-are-ai-conferences-now-too/5288076).
