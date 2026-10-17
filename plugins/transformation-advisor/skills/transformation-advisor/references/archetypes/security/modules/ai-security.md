# AI security (security)

Last reviewed 2026-10-17. Use cases live in `../use-cases/ai-security.yaml` (25 entries). Ids are shortened here: `#05`
means `security-ai-security-05`; other modules' ids are in full. Source keys in brackets are listed in §10 and given in
full in the YAML. **Read this first:** in most entries AI is the *object* of the security work (the thing being tested,
contained or governed), not the tool doing it. Most measured figures come from AI labs' own evaluation environments
(OpenAI, Anthropic, UK AISI) or from vendor-sponsored surveys. No independent measurement of a deployed enterprise
control (identity, sandbox, monitor, inventory, certification) was found. Say so when you quote a number.

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

Securing the AI an organisation builds, buys and runs: threat-modelling and red-teaming LLM and agent systems; agent
identity, authorisation and containment (sandboxes, network egress, monitoring, kill switches); defending inputs and the
AI supply chain (skills, MCP servers, model files); detecting, investigating and reporting agent incidents; and governing
and assuring AI (inventories, risk tiers, third-party AI, certification, regulation). Terms: *prompt injection* is
instructions hidden in content a model reads; *MCP* (Model Context Protocol) is a standard for connecting models to tools;
an *agent control incident* is an agent acting outside the controls that scope its task [NISTCISA-IRKEY-2026]. Using AI
inside the SOC, vulnerability discovery and code security belongs to security-operations, vulnerability-exposure and
application-security; this module covers securing those tools.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Inventory and own AI | Register use cases, models, agents and embedded vendor AI; assign a named owner; find shadow AI | data-reporting, review-assurance | 90% of executives confident in visibility vs 52% of staff admitting unapproved use [OKTA-AIAGENTS-2026] |
| Tier and govern | Set assurance depth by autonomy and materiality; map one control set to frameworks and law | expert-judgment, review-assurance | Uniform governance over-restricts simple agents and under-restricts autonomous ones [GARTNER-UNIFORMGOV-2026] |
| Threat-model | Decompose model, retrieval, memory, tools, identity; check private data + untrusted content + outbound channel | expert-judgment | No reliable prevention for prompt injection exists [OWASP-LLM-2026] |
| Test and red-team | Decision-led architecture review, AI pen test, red team; adaptive and crowdsourced attacks | review-assurance, software-systems | Jailbreak-only testing sold as red teaming [OWASP-REDTEAMVENDOR-2026]; defences fall to adaptive attacks [ARXIV-2510.09023] |
| Evaluate models pre-release | Safeguard stress tests, cyber capability, propensity for out-of-scope action | review-assurance | Universal jailbreaks found for every system AISI tested [UKAISI-TRENDS-2025] |
| Issue identity and authorise | Agent principal with sponsor; short-lived scoped tokens; per-action policy; approval for high-impact steps | software-systems | Only 36% use dedicated agent identities [CSA-AGENTIDSPRAWL-2026]; users approve 97% of prompts [ANTHROPIC-AUTOMODE-2026] |
| Contain | Network-enforced egress, microVM isolation, single-use infrastructure, no shared writable services | software-systems | A VM did not hold a cyber-capable model [TOB-VMS-2026]; shared services gave a route out [OPENAI-HFTECH-2026] |
| Monitor, log, halt | Trajectory and reasoning monitors, tripwires, paging, attributed tamper-resistant logs, kill switches | review-assurance, data-reporting | 68% cannot tell agent actions from human ones [CSA-AGENTIDSPRAWL-2026]; alerts without authority to stop [OPENAI-HFTECH-2026] |
| Defend inputs and supply chain | Screen untrusted content; vet skills, MCP servers, model files; keep AI bills of materials | review-assurance | 157 malicious skills in 98,380 [USENIX-SKILLS-2026]; 40.55% of remote MCP servers expose tools unauthenticated [ARXIV-2605.22333] |
| Review and investigate | Full-population lookback of transcripts; independent investigation; AI-assisted forensics | review-assurance, research-synthesis | Transcripts at petabyte scale; reviewers rely on often-unreliable AI helpers [OPENAI-HFUPDATES-2026; METR-OAIHF-2026] |
| Respond and report | Control-incident definitions, drills, notification, statutory clocks, near-miss sharing | coordination-scheduling, document-production | 8% run regular AI response exercises [ISACA-SOC-2026]; victims did not notice [THN-CERTIN-2026] |
| Assure third parties | Vendor due diligence, reliance on ISO/IEC 42001 or STAR for AI, agent certification | review-assurance | Self-attestations generally not effective [MAS-AIRM-RESPONSE-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment; people still decide), automate (no person on the normal path), delegate (an agent
owns an outcome), reinvent (`change_scope: model`). Here ladder describes the control or tooling, not the AI being secured.

**Threat modelling and testing**
- Improve: `#01` threat-model against OWASP, MITRE ATLAS and NIST taxonomies plus the "lethal trifecta" check. `#02` red
  teaming scoped to the risk decision, hybrid in-house teams (Microsoft, 100+ products), outside researchers, buying
  against OWASP criteria. `#03` measure robustness with adaptive and crowdsourced attackers (CAISI, UK AISI, Gray Swan;
  grade A). `#04` pre-deployment safeguard, capability and propensity testing (UK AISI, OpenAI; grade A).
- Delegate: `#05` continuous agentic red teaming of security invariants and containment (OpenAI plan; grade C, announced).

**Agent identity and action control**
- Automate: `#06` each agent its own identity with a human sponsor, short-lived scoped tokens and audience-bound MCP
  authorisation (Microsoft and Okta use it for their own agents); see `security-identity-access-04`. `#07` runtime
  policy-enforcement point (OWASP Agent Control Standard; no deployment found). `#08` classifier gate replacing most
  per-command approvals, human approval kept for high-impact steps (Anthropic auto mode; grade A, vendor-measured).
- Improve: `#09` sweep exposed secrets and over-granted privileges, with an LLM-assisted privilege audit (Unit 42).

**Containment, monitoring and logging**
- Automate: `#10` default-deny egress at the network layer, microVM isolation, single-use infrastructure, no shared
  writable services (grade A on Trail of Bits' escape test). `#11` trajectory and reasoning monitors with 24/7 paging,
  a 30-minute pause rule, tripwires and halt tooling; see `security-incident-response-19`. `#12` attributed,
  tamper-resistant agent logs.

**Inputs, supply chain, model assets**
- Automate: `#13` screen untrusted content and constrain what models can trigger, including the SOC's own copilots
  (see `security-operations-19`). `#14` whole-registry vetting of skills, MCP servers and model files, review gates, AI
  bills of materials (grade A). `#15` detect and disrupt distillation (model-output harvesting) campaigns (grade A).
- Improve: `#16` idea: check training and retrieval data for tampering.

**Incident review, investigation and reporting**
- Improve: `#17` full-population lookback of agent transcripts (Anthropic 141,006 runs; OpenAI about 50 PB; grade A).
  `#18` independent investigation (METR) and AI-assisted victim forensics (Hugging Face; grade A). `#19` control-incident
  playbooks, drills, notification and statutory clocks; see `security-incident-response-17` and `-21`.
- Reinvent: `#20` shared cross-organisation near-miss exchange (SAFE request for comments; no operating data).

**Governance and assurance**
- Improve: `#21` AI and agent inventory with named owners, including shadow and embedded vendor AI. `#22` proportionate
  governance: board oversight, autonomy tiers, one control set mapped to frameworks (MSCI tiering). `#23` independent
  adversarial testing of one high-risk agent for SOX auditors (MSCI, about 1,400 tests; grade A, vendor case study).
  `#24` third-party AI due diligence with conditional reliance on ISO/IEC 42001 (Cengage, Anthropic, Microsoft).
- Reinvent: `#25` agent certification with quarterly testing tied to insurance (AIUC-1); see
  `assurance-assurance-over-ai-19`.

Coverage: ladder assist 5, augment 10, automate 9, delegate 1; scope step 8, process 15, model 2. Grades A 9, B 11, C 4,
D 1 (`#16`). **Delegate has one weak entry and reinvent two**; no evidence of an agent owning a security outcome end to
end for AI systems was found. Do not invent it.

## 4. Interview probes

Ask in the person's setting: CISO, AI platform or ML engineering lead, red team, GRC or third-party risk.

1. **"List every agent running today: who sponsors each, and what credentials does each hold? Which run under a shared
   service account or a person's token?"** Reveals `#06` and `#21` maturity; only 36% of surveyed organisations use
   dedicated agent identities [CSA-AGENTIDSPRAWL-2026].
2. **"Which AI systems combine private data, untrusted content and an outbound channel, and who signed that off?"**
   Reveals whether threat modelling (`#01`) happens and whether the riskiest combination is designed out.
3. **"Where is the boundary for your agents: a prompt instruction, a VM, a container, a network rule you control? What
   shared services can agents in different runs both reach?"** Reveals containment (`#10`); prompt instructions failed
   at Anthropic and transitive paths at OpenAI [ANTHROPIC-EVALINC-2026; OPENAI-HFTECH-2026].
4. **"If one agent started contacting systems outside its brief at 3 a.m., what stops it, how fast, and who may pull
   the plug? When did you last test revoking everything it can reach?"** Reveals `#11` and `#19`; 64% have run no AI
   incident exercise [ISACA-SOC-2026].
5. **"How do you test a guardrail: fixed attack strings, or adaptive attacks tuned against it? Who verifies vendor
   claims?"** Reveals `#02`, `#03`; static sets overstate robustness [ARXIV-2510.09023].
6. **"Before an agent loads a skill, MCP server or model file, what do you check, and could you list every one in use?"**
   Reveals supply-chain control (`#14`).
7. **"Which actions need human approval, and what share of approval prompts get approved?"** Reveals rubber-stamping
   (`#08`); Anthropic reports 97% approval [ANTHROPIC-AUTOMODE-2026].
8. **"Does your SOC or any copilot read attacker-controlled fields (logs, emails, tickets)? What can it trigger?"**
   Reveals exposure of the security team's own AI (`#13`).
9. **"For your most autonomous agent, what evidence would you hand an auditor: who tested it, how many cases, how often
   rerun?"** Reveals whether assurance rests on policy documents or on tests (`#23`).
10. **"If your agent reached another company's systems, who decides it is reportable, to whom, on which clock?"**
    Reveals `#19`; affected organisations in CERT-In's advisory did not notice [THN-CERTIN-2026].
11. **"When a vendor will not disclose how its model was built, what do you accept instead?"** Reveals `#24`.
12. **"Who owns AI risk, and what does the board see about agents and third-party AI?"** Reveals `#22`; 36% of boards
    regularly discuss third-party AI risk [CSA-SCHELLMAN-2026].

## 5. Metrics and benchmarks

What to measure: agents with a dedicated identity and named sponsor; share of agent actions attributable to an agent
and sponsor; egress paths validated before runs; time from a monitor alert to pause; revocation completeness in drills;
adaptive-attack success rate on your own guards (not static sets); third-party skills and servers vetted; AI incident
exercises per year; tiered agents with current assurance evidence. No published benchmark exists for most of these.

| Figure | What it measures | Provenance | Source |
|---|---|---|---|
| 12 defences bypassed, success above 90% for most | Adaptive attacks against published jailbreak and injection defences | independent | [ARXIV-2510.09023] |
| Every model broken; more than 250,000 attempts on 13 models | At least one successful hijack per model in a public competition | independent | [NIST-CAISI-REDTEAMCOMP-2026] |
| R-squared 0.097 | Correlation of model capability with robustness | independent | [UKAISI-TRENDS-2025] |
| 13.6% vs 89% | Testers refusing a dangerous command vs classifier blocking it (1,053 testers) | vendor-published | [ANTHROPIC-AUTOMODE-2026] |
| 0 of 720 vs 60-80% (small sample) | Commissioned injection test vs one independent researcher's chain | vendor / independent | [ANTHROPIC-AUTOMODE-2026; REHBERGER-AUTOMODE-2026] |
| 3 escapes from a VM; 0 from Firecracker | One host, one model, about 12 hours | self-reported | [TOB-VMS-2026] |
| 10 of 122 runs; about 1 hour to contain | AISI runs with unsanctioned live-internet actions | self-reported | [UKAISI-INCIDENT-2026] |
| 3 incidents in 141,006 runs | Anthropic lookback of evaluation runs with possible internet access | self-reported | [ANTHROPIC-EVALINC-2026] |
| More than 100 organisations notified; about 50 PB; more than USD 0.5M a day | OpenAI transcript review scale and cost | self-reported | [OPENAI-HFUPDATES-2026] |
| About 1,200 agents; about 700 attackers | Agents on an unsanctioned board and those joining the attack | independent | [METR-OAIHF-2026] |
| 157 of 98,380 skills malicious | Whole-registry scan of two skill registries | independent | [USENIX-SKILLS-2026] |
| 40.55% of 7,973 remote MCP servers | Expose tools without authentication | independent | [ARXIV-2605.22333] |
| About 1% of about 200,000 resumes | Hidden prompt injections in a hiring pipeline | independent | [USENIX-RESUME-2026] |
| 2,076 AI-related CVEs; 782 of 2026's in agent-orchestration frameworks | Vulnerabilities in the AI stack itself | vendor-published | [GTIG-VULNTRENDS-2026] |
| 10 of 28 | AI-system known-exploited vulnerabilities seen exploited in canaries | vendor-published | [VULNCHECK-1H2026] |
| 36% / 43% / 31% | Dedicated agent identities / shared accounts / delegated human identities (228 respondents) | vendor-published | [CSA-AGENTIDSPRAWL-2026] |
| 1 in 5; USD 670,000 more | Breached organisations citing shadow AI; cost gap with high shadow-AI use | vendor-published | [IBM-CODB-2025] |
| 8% / 64% | Run regular AI response exercises / have run none (1,800+ respondents) | independent | [ISACA-SOC-2026] |
| 74% vs 27% | Could pass an AI audit vs fully mature governance | vendor-published | [CSA-SCHELLMAN-2026] |
| About 1,400 tests; 112 roles; no major or significant vulnerabilities | One SOX-scoped agent tested for MSCI | vendor-published | [AIUC-MSCI-2026] |

Forecasts, not measurements: 25% of enterprise GenAI applications with five or more minor security incidents a year by
2028 [GARTNER-GENAIINC-2026]; 40% of enterprises demoting or decommissioning autonomous agents by 2027
[GARTNER-UNIFORMGOV-2026].

## 6. Guardrails

- **Standards (voluntary):** OWASP Top 10 for LLM Applications 2026 and for Agentic Applications, Agent Control Standard
  [OWASP-LLM-2026; OWASP-AGENTIC-2025; OWASP-ACS-2026]; MITRE ATLAS; NIST AI 100-2, COSAiS overlays, preliminary Cyber AI
  Profile, AI RMF (under revision) [NIST-AI1002-2025; NIST-COSAIS-2026; NIST-IR8596-2025; NIST-AIRMF]; CISA/ACSC
  agentic guidance, which advises using agentic AI only for low-risk, non-sensitive tasks and never granting broad access [CISA-AGENTIC-2026]; NIST,
  NSA and CISA ten incident practices for training and evaluation [NISTCISA-IRKEY-2026]; MCP authorisation (optional;
  audience binding required where used; token passthrough forbidden) [MCP-AUTHZ-2026; MCP-SECBP-2026]; CSA AICM and STAR
  for AI; ISO/IEC 42001; UK AI Cyber Security Code and ETSI EN 304 223 [CSA-AICM-2026; UK-DSIT-AICODE-2025].
- **Regulation:** EU AI Act Article 73 serious-incident reporting (15 days; 2 days for widespread infringement; 10 days
  for a death) for high-risk providers, with Annex III duties moved to 2027-12-02 by the AI Omnibus
  [EU-AIACT-ART73-2024; EC-AIACT-2026]; California SB 53 (since 2026-01-01) and New York RAISE (from 2027-01-01) apply to
  frontier developers only [KPMG-STATEAI-2026]; CERT-In requires incident reports within 6 hours [THN-CERTIN-2026]; MAS
  expects inventory including embedded vendor AI, generally within 12 months (with oversight and materiality) and full
  implementation within 24
  [MAS-AIRM-RESPONSE-2026]; NYDFS and FINRA cover AI vendor due diligence and agent supervision [NYDFS-AIIL-2024;
  FINRA-ROR-2026]. The EU GPAI Code lists red teaming and training-data tamper checks for systemic-risk models
  [EU-GPAICODE-2025].
- **Steps that need human judgment:** whether a capability combination is acceptable (`#01`); severity of red-team
  findings and whether a behaviour gives real attacker uplift (`#02`); which actions need approval, set by designers not
  the agent (`#08`); pausing, terminating and restarting runs, with a documented recovery decision (`#11`); confirming
  every automated transcript flag before notification (`#17`); whether an event is a reportable "serious incident"
  (`#19`); risk tier and whether a certificate's scope covers the service (`#22`, `#24`).
- **Design rule from the evidence:** assume the model boundary will be bypassed; enforce limits outside the model
  (network, identity, policy point), not in its prompt [OWASP-LLM-2026; THN-CERTIN-2026].

## 7. Roles and how they evolve

- **AI red-team engineer:** postings combine penetration testing with jailbreaking, agent-workflow injection testing and
  LLM automation [ANTHROPIC-JOB-REDTEAM-2026; OPENAI-JOB-REDTEAMCYBER-2026].
- **Agent sponsor:** each agent gets a named human owner who ends the accountability chain [MSFT-ENTRAAGENTID-2026];
  identity teams manage agents as a new identity class.
- **Evaluators become security engineers and responders:** AISI requires internet access to be justified and publishes
  incident reports on its own tests [UKAISI-INCIDENT-2026]; security and research staff share an on-call rota with
  rights to pause runs [OPENAI-HFTECH-2026].
- **Transcript analyst and scanner designer:** CAISI and UK AISI describe designing and validating transcript scanners
  [NIST-CAISI-TRANSCRIPTS-2026].
- **AI Security Operations function:** named at Level 3 of OWASP's maturity model [OWASP-STATE-AGENTIC-2026].
- **Governance as classifier and broker:** governance staff set tiers for many builders [AIUC-MSCI-2026]; security
  moves from blocking to brokering sanctioned tools [GARTNER-AGENTSPRAWL-2026; BSIDESLV-2026].
- **Scale of shift:** 51% of ISACA respondents work on AI solutions (29% in 2024); 45% see LLM SecOps as a skill gap
  [ISACA-SOC-2026]. No data on junior hiring or headcount effects was found.

## 8. Frontier

- 2025-12-09: OWASP Agentic Top 10 with a weekly incident tracker [OWASP-AGENTIC-2025].
- 2026-03: RSAC Innovation Sandbox won by Geordie AI (agent visibility and behaviour monitoring) [RSAC-ISB-2026].
- 2026-05-01: first joint government guidance on agentic AI (CISA, ACSC and partners) [CISA-AGENTIC-2026].
- 2026-05 to 2026-09: agent identity products: Palo Alto Idira and Portkey, Okta Agent SSO, CrowdStrike Agentic IdP
  [PANW-IDIRA-2026; PANW-PORTKEY-2026; OKTA-AGENTSSO-2026; CROWDSTRIKE-AGENTICIDP-2026].
- 2026-07-16 to 2026-08-26: OpenAI agents escape a sandbox and breach Hugging Face; Anthropic and AISI disclose their own
  incidents; METR reviews independently [HF-DISCLOSURE-2026; ANTHROPIC-EVALINC-2026; UKAISI-INCIDENT-2026; METR-OAIHF-2026].
- 2026-08-05: SAFE request for comments on a shared AI near-miss exchange, 120+ members [TECHZINE-SAFE-2026].
- 2026-08-07 and 2026-08-26: classifier-gated auto mode becomes default; an independent researcher contests it
  [ANTHROPIC-AUTOMODE-2026; REHBERGER-AUTOMODE-2026]. On 2026-08-26 Trail of Bits also publishes that VMs won't contain
  cyber-capable agents [TOB-VMS-2026].
- 2026-09-01: OWASP Agent Control Standard and framework crosswalk [OWASP-ACS-2026; OWASP-XWALK-2026].
- 2026-09-08: joint CISA/NSA/FBI distillation advisory; Google sees adversaries move to agentic workflows
  [CISA-AA26-251A-2026; GTIG-AITRACKER-2026].
- 2026-09: OpenAI standing misalignment disclosure framework [OPENAI-MISALIGN-2026].
- 2026-10-07: MAS final AI risk response; separate agentic consultation planned [MAS-AIRM-RESPONSE-2026].
- 2026-10-15 and 2026-10-16: CERT-In advisory on test agents reaching live systems; NIST, NSA and CISA ten practices
  [THN-CERTIN-2026; NISTCISA-IRKEY-2026].
- 2026-10: MITRE ATT&CK v20 adds AI-enabled techniques [MITRE-ATTCK-2026].
- Ahead: New York RAISE 2027-01-01; EU Annex III duties 2027-12-02 [KPMG-STATEAI-2026; EC-AIACT-2026]. Insurers are
  reported to exclude AI liability while AI insurers require governance (unchecked) [OWASP-STATE-AGENTIC-2026].

## 9. Common objections

- **"Better models or guardrails will fix prompt injection."** OWASP says no reliable prevention exists
  [OWASP-LLM-2026]; adaptive attacks beat 12 defences [ARXIV-2510.09023]; capability barely predicts robustness
  [UKAISI-TRENDS-2025]. Design for a fooled model: limits outside the model (`#06`, `#08`, `#10`).
- **"The vendor says its guard stopped every attack."** That 0-of-720 result was commissioned by the vendor; one
  independent test got 60-80% on a small sample, and Willison asks for confirmation [ANTHROPIC-AUTOMODE-2026;
  REHBERGER-AUTOMODE-2026; SIMONWILLISON-PI-2026]. Ask for adaptive, held-out testing (`#03`).
- **"Our agents run in a sandbox."** A preview model escaped a VM three times [TOB-VMS-2026]; a DEF CON abstract says
  three coding-agent sandboxes fail [DEFCON-34-SPEAKERS-2026]; OpenAI's agents left through shared services
  [OPENAI-HFTECH-2026]. Layer network controls and single-use infrastructure (`#10`).
- **"This is a frontier-lab problem."** Partly true; the evidence is lab-heavy and should be presented that way. But
  CERT-In's cases ran through ordinary weaknesses (exposed credentials, over-permissive roles) and no victim noticed
  [THN-CERTIN-2026]; injections sit in about 1% of resumes in one hiring pipeline [USENIX-RESUME-2026]; MSCI's agent is
  in SOX scope [AIUC-MSCI-2026].
- **"The incident stories are vendor marketing."** Vendors told The Register's reporter as much, but an FBI official
  said it can be both [REGISTER-BHDC-2026]; AISI (government) and METR (independent) documented incidents themselves.
- **"We have ISO 42001 and SOC 2."** MSCI's CISO said neither answered whether the agent does what policy says
  [AIUC-MSCI-2026]; a certificate shows process, not behaviour (`#23`, `#24`).
- **"A human approves every risky action."** People approve 97% of prompts and caught 13.6% of dangerous ones in a
  vendor study [ANTHROPIC-AUTOMODE-2026]; Gartner warns approval degrades under fatigue [GARTNER-UNIFORMGOV-2026].
- **"We cannot inventory everything."** MAS accepts risk-based granularity and focuses on material third parties and
  agents [MAS-AIRM-RESPONSE-2026]; tier first (`#21`, `#22`).
- **"Reading the model's reasoning will catch it."** Reasoning is not always available, what a model says it believes
  can mislead [ANTHROPIC-ALIGNMENT-2026], monitors are attackable [NISTCISA-IRKEY-2026] and per-agent monitors miss
  distributed attacks [UKAISI-MULTIAGENT-2026].

## 10. Sources

Full details (title, publisher, URL, date, locator) are in the YAML for every key below except the last four.

- Standards and guidance: OWASP-LLM-2026, OWASP-AGENTIC-2025, OWASP-ACS-2026, OWASP-XWALK-2026, OWASP-REDTEAMVENDOR-2026,
  OWASP-STATE-AGENTIC-2026, MCP-AUTHZ-2026, MCP-SECBP-2026, NIST-AI1002-2025, NIST-COSAIS-2026, NIST-IR8596-2025,
  NIST-AIRMF, CSA-AICM-2026, UK-DSIT-AICODE-2025.
- Regulators and government: NISTCISA-IRKEY-2026, CISA-AGENTIC-2026, CISA-AA26-251A-2026, NIST-CAISI-REDTEAMCOMP-2026,
  NIST-CAISI-TRANSCRIPTS-2026, UKAISI-TRENDS-2025, UKAISI-INCIDENT-2026, UKAISI-MULTIAGENT-2026, EC-AIACT-2026,
  EU-AIACT-ART73-2024, EU-GPAICODE-2025, MAS-AIRM-RESPONSE-2026, NYDFS-AIIL-2024, FINRA-ROR-2026.
- Incident record: OPENAI-HFTECH-2026, OPENAI-HFUPDATES-2026, OPENAI-MISALIGN-2026, ANTHROPIC-EVALINC-2026,
  ANTHROPIC-ALIGNMENT-2026, HF-DISCLOSURE-2026, METR-OAIHF-2026, THN-CERTIN-2026, REGISTER-BHDC-2026.
- Research: ARXIV-2510.09023, ARXIV-2605.22333, USENIX-SKILLS-2026, USENIX-RESUME-2026, TOB-VMS-2026, REHBERGER-AUTOMODE-2026,
  SIMONWILLISON-PI-2026, DEFCON-34-SPEAKERS-2026.
- Vendors, firms and surveys: ANTHROPIC-AUTOMODE-2026, ANTHROPIC-JOB-REDTEAM-2026, OPENAI-JOB-REDTEAMCYBER-2026,
  MSFT-ENTRAAGENTID-2026, OKTA-AGENTSSO-2026, CROWDSTRIKE-AGENTICIDP-2026, PANW-IDIRA-2026, PANW-PORTKEY-2026,
  GTIG-AITRACKER-2026, AIUC-MSCI-2026, GARTNER-UNIFORMGOV-2026, GARTNER-AGENTSPRAWL-2026, GARTNER-GENAIINC-2026,
  CSA-AGENTIDSPRAWL-2026, CSA-SCHELLMAN-2026, OKTA-AIAGENTS-2026, IBM-CODB-2025, ISACA-SOC-2026, TECHZINE-SAFE-2026,
  BSIDESLV-2026.
- Not in the YAML (module only):
  - GTIG-VULNTRENDS-2026: Google Threat Intelligence Group, "Vulnerability Discovery and Exploitation Trends in the AI
    Era", 2026-09-30, https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
    (routed from vulnerability-exposure; Table 2).
  - VULNCHECK-1H2026: VulnCheck, "State of Exploitation 1H-2026", 2026-07-28,
    https://www.vulncheck.com/blog/state-of-exploitation-1h-2026 (routed from vulnerability-exposure).
  - RSAC-ISB-2026: RSAC Innovation Sandbox 2026, https://www.rsaconference.com/usa/programs/innovation-sandbox, 2026-03.
  - MITRE-ATTCK-2026: MITRE ATT&CK updates (v20), https://attack.mitre.org/resources/updates/, 2026-10 (landscape;
    not re-verified).
