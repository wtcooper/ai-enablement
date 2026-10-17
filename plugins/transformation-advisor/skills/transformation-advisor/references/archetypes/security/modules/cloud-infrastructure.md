# Cloud and infrastructure security (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/cloud-infrastructure.yaml` (24 entries). Ids are shortened
here: `#05` means `security-cloud-infrastructure-05`. Source keys in brackets are in the YAML or in §10.
Read this first: almost every outcome figure is **vendor-published** (Wiz, AWS, Tamnoon, CrowdStrike, Check Point) or
**self-reported** by the deploying organisation; no independent measurement of any cloud-security agent exists, and
the independent lab research is more cautious. Only 5 of 24 entries are graded B and none A: ZS's figure (`#02`) is a
customer's spoken account on an undated vendor page with no published method. fwd:cloudsec talk abstracts (talks not
viewed) support grade C at most. Say "vendor claim" whenever you quote a vendor figure.

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

Securing cloud accounts and workloads (posture management, runtime detection and response, Kubernetes), cloud
identities and permissions, infrastructure as code (IaC: cloud resources defined in files such as Terraform), network
and edge policy (firewalls, WAFs, egress) and endpoints, including developer machines that run coding agents. It is
the team that owns the infrastructure layer; the agent incidents CERT-In reported in 2026-10 ran through exposed
credentials and permissive cloud roles, and it asks for per-run agent identities and default-deny egress [CERTIN-CIAD0049-2026].
Boundaries: agent identity, containment and action logging are in ai-security (`security-ai-security-06`, `-10`,
`-12`); the Wiz Red Agent perimeter agent is `security-vulnerability-exposure-21`; autonomous pentest agents such as
AWS Security Agent are `security-vulnerability-exposure-17`; calibrated endpoint-triage classifiers (CrowdStrike) are
`security-operations-06`; pull-request scanning of application code is in application-security.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Inventory and exposure discovery | Find accounts, assets, internet-facing apps and APIs | data-reporting | CERT-In: agents got in through ordinary weaknesses (exposed keys, old test APIs, broad cloud roles) [THN-CERTIN-2026] |
| Posture assessment and prioritisation | Score misconfigurations (CSPM, CNAPP: posture and cloud-native protection platforms); rank by reachability, privilege, data | review-assurance, data-reporting | Teams investigate about 4% of alerts (vendor research) [TAMNOON-REMEDIATION-2026]; over half of high-priority findings fall away with context [WIZ-CLOUDRISK-2026] |
| Ownership and routing | Find who owns the resource and at which layer to fix it | coordination-scheduling | Routing can take longer than the fix [WIZ-PILLAR2-2026]; ownership graph is never complete [WRITER-CEREBRO-2026] |
| Remediation and change | Fix, approve, apply, verify, prevent recurrence | software-systems | Critical misconfigurations open 128 days on average (vendor) [TAMNOON-REMEDIATION-2026]; fear of breaking production |
| Identity and permission hygiene | Right-size roles, keys, service accounts | software-systems, review-assurance | 59% of AWS IAM users have an access key over a year old [DATADOG-SOCS-2025]; console fixes are overwritten by IaC [AWS-LEASTPRIV-2026] |
| Preventive guardrails in IaC | Approved modules, policy as code, pipeline gates | software-systems | AI assistants write most IaC in many organisations (speaker claim) [FWDCLOUDSEC-RENGASAMY-2026]; LLM IaC has 3.21x-3.87x human vulnerability density [ARXIV-2608.28021] |
| Runtime detection and investigation | Cloud and Kubernetes alerts, verdicts, containment | transaction-processing, research-synthesis | About 2% of cloud alerts actionable at WRITER [WRITER-CEREBRO-2026]; runtime noise [AWS-GUARDDUTY-ETD-2026] |
| Network and edge policy | Firewall rules, WAF virtual patches, segmentation | software-systems, review-assurance | Rulebases drift between review cycles [CHECKPOINT-AGENTICNET-2026]; 43-day median patch time cited [FWDCLOUDSEC-ALIM-2026] |
| Endpoint protection | EDR (endpoint detection and response) policy, developer endpoints | software-systems, expert-judgment | Coding agents act on privileged endpoints, approvals often skipped [PERPLEXITY-NUMBAT-2026] |
| Detection engineering and validation | Write, test and retire cloud detection rules; attack simulation | software-systems, review-assurance | 1 in 3 of 2,000+ public cloud rules defective (speaker claim) [FWDCLOUDSEC-GOWTHAM-2026] |
| Compliance and continuous authorisation | Evidence for FedRAMP-style regimes; policy as code | review-assurance, document-production | Point-in-time checks lag dynamic cloud [WIZ-FORGOV-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (the service or operating model changes). In the deployments found,
people keep merges, risky fixes and higher-severity verdicts; WRITER also reserves IAM and network changes for people.

**Posture and prioritisation**
- Improve: `#01` rank findings by reachability, toxic permission combinations and data access; Microsoft's Posture
  Prioritization Agent (read-only preview) explains what to fix first. Wiz says context removes more than half of
  high-priority findings (vendor, grade C).

**Runtime detection and investigation**
- Automate: `#02` an agent investigates cloud detections; ZS ran it in parallel with analysts for three months
  ("around 95.17%" agreement, its own validation), then let it close a defined set of low-severity alerts with an
  end-of-shift human review. Redis: 85.7% accuracy over 431 cases (vendor-published). Grade B: method unpublished.
- Improve (process): `#03` in-house triage agents over posture findings: Cohere via an MCP server (attack-path
  analysis "up to 120 minutes to 20 seconds", vendor headline); WRITER's open-source Cerebro with evidence rules
  (grade B).
- Improve: `#04` GuardDuty folds weak runtime signals and posture context into one attack sequence (AWS: about one in
  four sequences net-new; signal correlation, not an LLM). `#05` a read-only Kubernetes triage agent that still failed
  four times (talk abstract).

**Remediation**
- Improve: `#06` remediation agents find owner, root cause and fix layer and draft the ticket or pull request
  (project44: "10x faster" remediation, metric undefined; Rogo AI quote; grade B).
- Automate: `#07` evidence-gated auto-remediation: safe fixes run, risky ones wait for approval, unsafe ones go to the
  owner (Tamnoon method; PatchWeaver prototype had about half the policy violations in lab tests; grade C).

**Identities and permissions**
- Improve (process): `#08` unused-access findings become least-privilege IaC pull requests (AWS reference pattern,
  research prototypes; grade C).
- Delegate: `#09` a four-agent "team" scored and cut identity risk 42.7% in one AWS account in five days (talk abstract
  by a vendor's Field CTO; grade C).
- Improve: `#10` AI-assisted discovery of new IAM privilege-escalation paths, each validated in a lab (talk abstract).

**Infrastructure as code**
- Improve (process): `#11` guardrails for AI-written and AI-repaired IaC: approved modules served to coding agents,
  multi-scanner gates, plan comparison. Research: 71.4% of plan-compared Terraform repairs were deceptive (grade C).
- Idea: `#12` agents detect drift from IaC and propose reconciling changes.

**Network and edge**
- Improve (process): `#13` AI-assisted WAF virtual patching (Adobe manager's abstract; Palo Alto announcements).
- Improve: `#14` firewall rule hygiene (Cato, Check Point docs); `#15` intent-to-rule authoring with change-impact
  checks (Fortinet, Palo Alto, Check Point, Cisco features; FwChange says few use them daily). All grade C.

**Endpoints**
- Automate (process): `#16` Perplexity's Numbat guards coding agents on thousands of its endpoints and an agent drafts
  detection changes for human review (grade B).
- Idea: `#17` agents tune EDR policy from a bounded action catalogue.

**Detection engineering and validation**
- Improve (assist): `#18` LLM help in writing cloud detections, plus rule-quality tests that catch hallucinated
  fields (job postings; talk abstract).
- Ideas: `#19` agent-run attack simulation to map telemetry to techniques (delegate); `#20` cloud canaries to detect
  and steer AI attackers.

**Compliance**
- Improve (process): `#21` AI-assisted evidence for continuous authorisation inside FedRAMP High (Wiz announcement)
  and LLM-drafted policy as code (research).

**Operating and service model (reinvent)**
- `#22` a shared security AI platform team on which each security function builds governed agents (Databricks
  posting; grade B). `#23` managed cloud security on a multi-tenant AI platform (Wiz MSP programme; announced).
- Idea: `#24` a runtime control layer that decides whether live cloud actions proceed (SACR category).

**Cross-module.** Agent sandboxes and egress: `security-ai-security-10`; agent identity: `-06`; tamper-resistant agent
logs: `-12`; untrusted log content: `-13`; secret sweeps and LLM privilege audit: `-09`. Perimeter agent:
`security-vulnerability-exposure-21`. Constrained response actions: `security-operations-19`.

Coverage: most entries are augment (16). Automate has five (`#02`, `#07`, `#16`, `#17`, `#24`; two are ideas). Assist
has one (`#18`). Delegate has only a talk abstract (`#09`) and an idea (`#19`); the strongest delegate evidence nearby
is autonomous pentesting in vulnerability-exposure. Model scope has two entries (`#22`, `#23`), neither with outcomes.
There are no entries for assist at process or model scope, or for automate or delegate at model scope.

## 4. Interview probes

1. **When a cloud finding is raised, who owns it, and how do you know?** Reveals ownership-data quality, the
   precondition for `#03` and `#06`; WRITER found its graph is never complete.
2. **What share of posture findings does anyone investigate, and what decides which ones?** Reveals whether
   prioritisation uses reachability, privilege and data (`#01`) or severity alone.
3. **If an agent investigated your low-severity cloud detections, how long a parallel run and what agreement rate
   would you need before it closed alerts alone, and who reviews what it closed?** Reveals readiness for `#02`; ZS
   used three months and an end-of-shift review.
4. **Which cloud fixes run today without a human, what evidence says a fix is safe, and when did an automated fix last
   break something?** Reveals the gate design for `#07`.
5. **When AI proposes an IAM or network change, where does the fix live (console or IaC), how many reviews a week can
   owning teams absorb, and what is the break-glass path?** Reveals fit for `#08`; AWS warns against flooding reviewers.
6. **How do you verify an AI-proposed Terraform or Kubernetes change independently of the tool that wrote it?**
   Reveals whether `#11` controls exist; a passing scanner is not proof.
7. **What can each of your agents reach (identity, scopes, secrets, egress, cost ceiling), and could you list every
   agent running in your estate today?** Reveals agent governance; "read-only" alone failed in `#05`.
8. **Where do logs, tickets or telemetry reach an AI tool, and who can write to them?** Reveals exposure to prompt
   injection through logs (`#02`, `#05`; `security-ai-security-13`).
9. **If a critical exploit were public within the hour, how fast could your change board approve a WAF rule or
   network change?** Reveals the "authority gap" ENISA describes and fit for `#13`.
10. **Which developer machines run coding agents, with what permissions, and what telemetry do you get from them?**
    Reveals endpoint readiness for `#16`.
11. **Who builds and tests the sandboxes your organisation's AI agents run in?** Reveals whether this team owns agent
    isolation (`security-ai-security-10`).
12. **If a regulator (DORA, NIS2, FINRA or a FedRAMP assessor) asked how you supervise AI in cloud security, what
    evidence would you hand over?** Reveals audit readiness for `#21`.

## 5. Metrics and benchmarks

| Metric | Figure | Source (provenance) |
|---|---|---|
| Agent verdict agreement, parallel run | "around 95.17%" over three months (ZS) | [WIZ-ZS-2026] (customer quote on vendor page; method unpublished) |
| Agent accuracy vs final dispositions | 85.7%; false negatives below 2%; 431 cases (Redis) | [WIZ-RUNTIME-2026] (vendor) |
| Investigation speed and throughput | 80-90% faster verdicts; 4x throughput (ZS) | [WIZ-ZS-2026] (vendor headline) |
| False-positive investigation time | 20-30 min to 5 min (Owkin) | [WIZ-OWKIN-2026] (vendor headline) |
| Attack-path analysis; triage hours | up to 120 min to 20 s; about 145 h/week (Cohere) | [WIZ-COHERE-2026] (vendor headline) |
| Remediation speed | "10x", metric undefined (project44) | [WIZ-PROJECT44-2026] (vendor) |
| Actionable cloud alerts (baseline) | about 2% | [WRITER-CEREBRO-2026] (self-reported) |
| Alerts investigated / fixed; age | about 4% / under 1%; 128 days (2025), 150 days (2026 report) | [TAMNOON-REMEDIATION-2026], [TAMNOON-CORTEX-2026] (vendor) |
| Findings removed by context | more than half of high-priority findings | [WIZ-CLOUDRISK-2026] (vendor) |
| Net-new runtime attack sequences | about one in four, first week | [AWS-GUARDDUTY-ETD-2026] (vendor) |
| Missed attack alerts, LLM triage agents | at least 40.4% for every approach tested | [ARXIV-2610.10608] (independent) |
| Deceptive Terraform repairs | 71.4% of plan-compared repairs | [ARXIV-2606.26590] (independent) |
| Cloud guardrails vs log injection | Azure Prompt Shield 1 of 32 payloads; GCP Model Armor 0 | [ARXIV-2604.15368] (independent) |
| Change-policy violations, prototype | 4.73% vs 9.95% of steps | [USENIX-PATCHWEAVER-2026] (independent) |
| Long-lived keys; IMDSv2; public buckets | 59% of IAM users; 49% of EC2 enforce IMDSv2; about 1% of S3 | [DATADOG-SOCS-2025] (vendor telemetry) |
| Cloud in incidents; preventable gaps | 20% of incidents; over 90% had gaps that enabled intrusion | [UNIT42-IR-2026] (vendor) |
| Misconfiguration or accidental exposure as vector | 20.7% of unauthorised-access incidents with an identified vector (5.2% had one) | [ENISA-ETL-2026] (independent) |
| Agents exceeding permissions; unknown agents | 53% (n=445); 82% (n=418) | [CSA-AGENTSCOPE-2026], [CSA-UNKNOWNAGENTS-2026] (sponsor-funded) |

What to measure with a client: share of findings with a confirmed owner; share investigated; time from finding to fix
by severity; agent-versus-analyst agreement in a parallel run and a sampled review of what the agent closed; override
rate (WRITER tracks it); AI-proposed changes reverted or causing incidents; review queue per team per week.

## 6. Guardrails

- **Agents that touch infrastructure.** CERT-In (2026-10-15): give each agent run a short-lived least-privilege
  identity, enforce default-deny egress at the network layer and keep tamper-resistant logs of actions on production
  [CERTIN-CIAD0049-2026]; its directions require incident reports within 6 hours, per the press report
  [THN-CERTIN-2026]. Joint CISA, NSA and partner guidance (2026-05-01): human approval for high-impact steps, agents
  may not change their own privileges, separation of duties, sandbox testing, rollback, unified audit logs
  [CISA-AGENTIC-2026]. Detail: `security-ai-security-06`, `-10`, `-12`.
- **NIST IR 8596 (draft Cyber AI Profile, 2025-12-16).** Gate AI-initiated network changes and privilege use with human
  approval or policy checks (PR.IR-01); version and track model configurations, prompts, thresholds and guardrail
  rules (PR.PS-01) [NIST-IR8596-2025].
- **Speed versus approval.** ENISA's "Authority Gap": change boards cannot approve in the minutes available, so critical
  providers may be forced into autonomous patching, at the risk of outages [ENISA-FRONTIER-2026].
- **US federal.** BOD 26-04 (2026-06-10, per a vendor summary): risk-based remediation by exposure, KEV status, exploit
  automatability and impact; three days for the highest risk [CROWDSTRIKE-BOD2604-2026].
- **Financial services and EU.** FINRA: consider how to monitor agent system access, where to place human checks and
  how to track agent actions [FINRA-ROR-2026]. DORA's 19 designated critical ICT providers include AWS, Google Cloud
  and Microsoft entities [EBA-CTPP-2025]. The AI Act's high-risk rules for areas including critical infrastructure
  moved to 2027-12-02 [EC-AIACT-2026]. Sovereign security operations offers cite GDPR, NIS2 and DORA [PANW-DT-2026].
- **Separation of duties for tools.** The tool that writes a firewall rule should not be the only judge of its impact
  (NIST SP 800-53 CM-4, AC-5, argued by an interested vendor) [FWCHANGE-VENDORAI-2026].
- **Shared responsibility.** Who is liable when a SaaS pentest agent leaves scope is unclear [FWDCLOUDSEC-FAN-2026].
- **Practitioner controls.** Evidence before any decision, approval for IAM and network changes, "needs human review"
  when evidence is missing [WRITER-CEREBRO-2026]; dry runs, pull-request limits, manual review for admin roles
  [AWS-LEASTPRIV-2026]; scope enforced in infrastructure, not prompts [FWDCLOUDSEC-RAJI-2026]; re-run the full scanner
  and compare plans [ARXIV-2606.26590]; treat log content as hostile [ARXIV-2605.24421].
- **Human judgment stays on:** IAM and network-boundary changes; higher-severity verdicts; risky fixes; merges of AI
  IaC; firewall change approval; scope and authorisation of agent testing; exceptions and risk acceptance.

## 7. Roles and how they evolve

- **Analysts become exception reviewers.** ZS analysts review what the agent closed at the end of each shift; analysts
  without deep cloud experience can read its verdicts [WIZ-ZS-2026].
- **Small teams cover large estates.** Owkin (three people, more than 50 AWS accounts) credits Wiz's agents; La Centrale
  (three people, more than 2,000 Lambda functions) credits graph context and developer ownership [WIZ-OWKIN-2026, WIZ-LACENTRALE-2026].
- **Engineers fix rather than validate.** project44 ran an engineering-wide enablement session; developers get
  pre-filled tickets or pull requests [WIZ-PROJECT44-2026, WIZ-OPMODEL-2026].
- **Reviewers of agents, not only answers.** Engineers check an agent's reach, identity and cost [FWDCLOUDSEC-RAJI-2026].
- **Builders of agent sandboxes.** Datadog runs a multi-cloud sandbox for untrusted code and agents at tens of millions
  of executions a month and probes it with an offensive agent; a Roblox engineer describes a hardened sandbox for
  coding agents (talk abstracts) [FWDCLOUDSEC-DENARDOU-2026, FWDCLOUDSEC-MITHANI-2026].
- **Platform teams for agents.** Databricks advertises a shared Agentic Security Engineering team serving every security
  function [DATABRICKS-JOB-AGENTICSEC-2026]; Block, Cloudflare, Pinterest and Robinhood postings ask for AI fluency
  [BLOCK-JOB-PLATSEC-2026, CLOUDFLARE-JOB-VM-2026, PINTEREST-JOB-SECOPS-2026, ROBINHOOD-JOB-SECENG-2026].
- **Cloud security folds into infrastructure security.** A Datadog leader argues AI security will be absorbed the same
  way [FWDCLOUDSEC-GONDA-2026]; more CISOs own infrastructure teams [VENTUREINSEC-INFRA-2026].
- **Talent market.** Forrester heard vendors still hire early-career staff, in fewer numbers [FORRESTER-RSAC-2026]. In a
  10-month study, SOC analysts used LLMs for sensemaking, not high-stakes calls [ARXIV-2508.18947]. No source
  measures headcount change in cloud security.

## 8. Frontier

- 2026-03-18 to 03-30: Orca's agentic platform; Wiz Workflows, Green Agent and Blue Agent general availability
  [ORCA-AGENTIC-2026, WIZ-WORKFLOWS-2026, WIZ-GREEN-2026, WIZ-BLUEAGENT-GA-2026].
- 2026-05-01 and 06-11: joint agentic-AI guidance from six agencies; SACR names "Agentic Cloud Security Platforms" [CISA-AGENTIC-2026, SACR-ACSP-2026].
- 2026-07-02: Wiz MCP server generally available, so customers build their own agents on the graph [WIZ-MCP-2026].
- 2026-07-07 and 07-29: ENISA's "Authority Gap"; Perplexity open-sources Numbat for coding agents on endpoints [ENISA-FRONTIER-2026, PERPLEXITY-NUMBAT-2026].
- 2026-08-03 and 08-06: Microsoft's posture agent preview; Orca's agent pods [MSFT-LEARN-PPA-2026, ORCA-AGENTPODS-2026].
- 2026-08-19: Palo Alto's Frontier AI Critical Defense Program with virtual patching [PANW-FRONTIERCDP-2026].
- 2026-08-26: Trail of Bits says a VM will not contain a cyber-capable agent [TOB-VMS-2026]; OpenAI's incident report
  plans narrower egress [OPENAI-HFTECH-2026].
- 2026-09-08: fwd:cloudsec Europe talks on agents in Kubernetes, sandboxes and "infrastructure security"
  [FWDCLOUDSEC-RAJI-2026, FWDCLOUDSEC-GONDA-2026].
- 2026-09-17 and 09-28: Cisco's Policy Change Impact Analyzer, per FwChange; Wiz MSP programme [FWCHANGE-VENDORAI-2026, WIZ-MSP-2026].
- 2026-10-05 and 10-06: CrowdStrike AI remediation plans; Wiz AI SAST ties code findings to what runs in production
  [CROWDSTRIKE-CLOUDREM-2026, WIZ-AISAST-2026].
- 2026-10-12 and 10-14: GuardDuty attack sequences gain posture indicators; Wiz agents run inside FedRAMP High [AWS-GUARDDUTY-ETD-2026, WIZ-FORGOV-2026].
- 2026-10-15: CERT-In advisory treats AI agents as attack vectors exploiting conventional cloud weaknesses
  [CERTIN-CIAD0049-2026]; AWS publishes its own 37-CVE agent benchmark (33 exploited) [AWS-SECAGENT-2026].

## 9. Common objections

- **"Read-only access is safe."** A read-only Kubernetes agent reached secrets through pod specs and logs, left an
  unattributable log line and over-fetched; controls that held were infrastructure, controls that failed were prompts
  [FWDCLOUDSEC-RAJI-2026].
- **"The numbers are marketing."** Mostly true: nearly every figure sits on a vendor page, and independent triage
  research found every tested approach missed at least 40.4% of attack alerts [ARXIV-2610.10608]. Ask for a parallel
  run on your own alerts, as ZS did [WIZ-ZS-2026], and for false-alarm rates [AWS-DECEPTION-2026].
- **"An AI fix will break production."** Agents holding production permissions can: one reported AWS disruption
  followed an AI coding tool erasing its environment, though Amazon called it user error [TOMSHW-AWSKIRO-2026]. Use usage evidence and approval tiers (`#07`),
  dry runs and review limits (`#08`).
- **"The scanner passes, so it is fixed."** Not reliable: for the primary model, 83.3% of repairs removed the targeted
  finding but 10.4% were clean under a full scan [ARXIV-2606.26590].
- **"Attackers can't touch our AI."** Log fields are attacker-controlled; cloud providers' guardrails missed log-embedded
  injections [ARXIV-2604.15368, ARXIV-2605.24421]. Constrain what the model can trigger (`security-operations-19`).
- **"Rule-based scanners already do this."** A founder of an AI DevOps product said he keeps rule-based scanners for
  determinism [HN-DATAFRUIT-2025]; the entries here put AI on context, triage and fix drafting (`#01`, `#06`, `#11`).
- **"Our change board can't move that fast."** ENISA agrees [ENISA-FRONTIER-2026]; vendors let teams set autonomy per
  workflow [WIZ-FORGOV-2026], and research encodes change rules as policy (`#07`).
- **"AI will only grow the backlog."** Tamnoon expects AI scanning to deepen configuration backlogs (vendor view)
  [TAMNOON-CORTEX-2026]; ask where findings wait today before adding discovery.
- **"Containing our own agents is the AI team's job."** CERT-In's cases ran through exposed credentials and permissive
  cloud roles, and it asks organisations to give each agent run a short-lived identity and default-deny egress
  [CERTIN-CIAD0049-2026]: identity and network controls (`security-ai-security-10`).

## 10. Sources

Full details are in the YAML. Keys cited here but not in the YAML:

- [THN-CERTIN-2026] The Hacker News, "CERT-In Warns AI Agents Accessed Sensitive Data at Indian Organizations During Testing", 2026-10-16. https://thehackernews.com/2026/10/cert-in-warns-ai-agents-accessed.html
- [CERTIN-CIAD0049-2026] CERT-In, "CIAD-2026-0049: AI Agents as Attack Vectors", regulator advisory, 2026-10-15. https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02
- [FINRA-ROR-2026] FINRA, "2026 Annual Regulatory Oversight Report: GenAI section", 2025-12-09. https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
- [EBA-CTPP-2025] EBA, EIOPA and ESMA, "ESAs designate critical ICT third-party providers under DORA", 2025-11-18 (the 19 names are in the linked list PDF). https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital
- [EC-AIACT-2026] European Commission, "AI Act regulatory framework" page (undated; retrieved 2026-10-17). https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- [PANW-DT-2026] Palo Alto Networks press release with Deutsche Telekom on sovereign security operations, 2026-06-09. https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-and-deutsche-telekom-bring-ai-driven-security-with-advanced-sovereignty-controls-for-european-regulated-industries
- [UNIT42-IR-2026] Palo Alto Networks Unit 42, "2026 Global Incident Response Report", 2026-02 (month inferred). https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report
- [ENISA-ETL-2026] ENISA, "ENISA Threat Landscape 2026", 2026-09-22. https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf
- [CSA-AGENTSCOPE-2026] Cloud Security Alliance, survey commissioned by Zenity on agent scope violations (n=445), 2026-04-16. https://cloudsecurityalliance.org/press-releases/2026/04/16/more-than-half-of-organizations-experience-ai-agent-scope-violations-cloud-security-alliance-study-finds
- [CSA-UNKNOWNAGENTS-2026] Cloud Security Alliance, survey commissioned by Token Security on unknown agents (n=418), 2026-04-21. https://cloudsecurityalliance.org/press-releases/2026/04/21/new-cloud-security-alliance-survey-reveals-82-of-enterprises-have-unknown-ai-agents-in-their-environments
- [FWDCLOUDSEC-FAN-2026] Richard Fan, "Whose Fault When a Pentest Agent Attacks the Wrong Target?", fwd:cloudsec Europe abstract, 2026-09-07. https://pretalx.com/fwd-cloudsec-europe-2026/talk/VWFXZS/
- [FWDCLOUDSEC-DENARDOU-2026] Denardou and Henkel (Datadog), "What Could Possibly Go Wrong? Running untrusted code in the cloud", abstract, 2026-09-07. https://pretalx.com/fwd-cloudsec-europe-2026/talk/E8CFEJ/
- [FWDCLOUDSEC-MITHANI-2026] Sakina Mithani (Roblox), "Release the Kraken: Putting Tentacles on Your AI 'Paved Road'", abstract, 2026-06-01. https://pretalx.com/fwd-cloudsec-2026/talk/BYFWBG/
- [FWDCLOUDSEC-GONDA-2026] Tim Gonda (Datadog), "Cloud Security Is Dead. Long Live Infrastructure Security.", abstract, 2026-09-08. https://pretalx.com/fwd-cloudsec-europe-2026/talk/M7LSGF/
- [VENTUREINSEC-INFRA-2026] Venture in Security, "Infra + security: why more & more CISOs are starting to own infrastructure", 2026-04-28. https://ventureinsecurity.net/p/infra-security-why-more-and-more
- [FORRESTER-RSAC-2026] Forrester, "RSAC 2026: An AI Coming-Of-Age Story Without The Romance", 2026-03-31. https://www.forrester.com/blogs/rsac-2026-an-ai-coming-of-age-story-without-the-romance
- [ARXIV-2508.18947] "LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres", arXiv preprint (abstract; listed "under review"), 2025-08-26. https://arxiv.org/abs/2508.18947
- [TOB-VMS-2026] Trail of Bits, "VMs won't contain cyber-capable agents", 2026-08-26. https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/
- [OPENAI-HFTECH-2026] OpenAI, "OpenAI - Hugging Face Incident Technical Report", 2026-08-26. https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf
- [WIZ-AISAST-2026] Wiz, "Wiz AI SAST: AI Code Security With Code-to-Cloud Context", 2026-10-06. https://www.wiz.io/blog/introducing-wiz-ai-sast
- [AWS-SECAGENT-2026] AWS Security Blog, "AWS Security Agent (now part of AWS Continuum) exploited 33 of 37 new real-world CVEs", 2026-10-15. https://aws.amazon.com/blogs/security/aws-security-agent-now-part-of-aws-continuum-exploited-33-of-37-new-real-world-cves/
