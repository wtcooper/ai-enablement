# Security interview guide

Last researched 2026-10-17. Use this alongside the method files: onboarding questions come from
[onboarding.md](../../method/onboarding.md), question craft from [interviewing.md](../../method/interviewing.md). This
file gives the security wording, the field's boundary probes, phase questions and the vocabulary to mirror. Ask one
question at a time and skip what you already know. Source keys in brackets resolve in §9 or in [sources.md](sources.md).

## Contents

1. [Who you are likely talking to](#1-who-you-are-likely-talking-to)
2. [Onboarding questions in security words](#2-onboarding-questions-in-security-words)
3. [Choosing focus modules](#3-choosing-focus-modules)
4. [Journey-stage boundary probes](#4-journey-stage-boundary-probes)
5. [Phase questions](#5-phase-questions)
6. [Service provider variants](#6-service-provider-variants)
7. [Sensitive topics](#7-sensitive-topics)
8. [Vocabulary to mirror](#8-vocabulary-to-mirror)
9. [Sources](#9-sources)

## 1. Who you are likely talking to

| Person | What they usually care about | Open with |
|---|---|---|
| CISO or deputy (in house) | Board reporting, flat budget, regulators, AI risk across the business, staffing | "Where does your team spend most of its time, and what does the board ask you about AI?" |
| Head of SOC or detection and response | Alert volume, tier-1 load, MTTR, coverage, analyst burnout, the MDR contract | "How many alerts a day, and what share does anyone actually investigate?" |
| AppSec or product security lead | Findings backlog, AI-written code, review load, PSIRT intake | "How many findings are open, and how long does a fix take to land?" |
| IAM lead | Access reviews, joiners and leavers, service accounts, help-desk resets, agent identities | "How many access-review decisions a quarter, and how many are changed?" |
| GRC lead | Questionnaires, vendor reviews, audits, evidence, AI policy | "How many customer reviews and vendor assessments a month, and who does them?" |
| Cloud security lead | Posture findings, ownership, IaC, runtime noise | "Which cloud findings are open longest, and why?" |
| Provider CEO or practice lead (MDR, MSSP, testing, IR) | Margin, pricing, analyst bench, renewals, differentiation | "What do clients pay you for that they could not buy as software?" |

## 2. Onboarding questions in security words

Use these in place of, or after, the starred questions in onboarding §3.

| Profile element | Question | Listen for |
|---|---|---|
| Role and scope | "Are you responsible for one team, the SOC, the whole security function, or a provider's service line or firm?" | Scope level; in house or provider |
| What is delivered | "What does your team own: detection and response, AppSec, cloud, IAM, GRC, data protection, awareness, AI security?" | Which modules ([value-chain.md](value-chain.md) §2) |
| Clients or the business | "Which business do you protect (sector, size, regulators)? Or, for a provider, which client segments?" | NIS2, DORA, SEC, NYDFS, HIPAA exposure |
| How it is paid | "What is your budget doing this year, and where does money for AI come from? Providers: per endpoint, per identity, flat fee?" | Funding source ([economics.md](economics.md) §2, §4) |
| Journey stage | "In the last two weeks, where did AI do part of a real case or review? Could you show me where that is logged?" | Individual use versus a defined step |
| Pressures | "What is pushing hardest: alert volume, the patch backlog, staffing, regulators, customers' questionnaires, vendor bundling, or AI risk in the business?" | Why now |
| Constraints | "What must not change: who approves containment, what data leaves your tenant, what your insurer or auditor expects?" | Guardrails ([guardrails.md](guardrails.md)) |
| Tools and data | "Which SIEM, EDR and case tools do you run, and do closed cases carry a reason?" | Data readiness ([value-chain.md](value-chain.md) §5) |
| Unapproved use | "In most teams some analysts paste logs or code into AI tools that aren't approved. Is that happening here? There's no wrong answer." | Shadow AI; 33% of employees in a Gartner survey admitted entering sensitive data into unapproved tools [GARTNER-TRENDS-2026] |
| Session goal | "What would make this worthwhile: one workflow to fix, a plan for the function, or a case for the board or your partners?" | Path |

**Bring evidence in early.** Once you know the focus, give one real example from the relevant module with its grade,
and say who measured it. In most security modules the honest answer is "the vendor" or "the deploying team".

## 3. Choosing focus modules

| If the user says | Module to load |
|---|---|
| "Alert fatigue", "tier 1", "SIEM", "SOAR", "MDR", "detections", "MTTR", "agentic SOC" | [operations](modules/operations.md) |
| "Questionnaires", "trust centre", "TPRM", "SOC 2 readiness", "evidence", "board pack", "risk register", "FAIR" | [governance-risk](modules/governance-risk.md) |
| "CTI", "IOCs", "threat hunting", "ATT&CK mapping", "ISAC", "intel reports" | [threat-intelligence](modules/threat-intelligence.md) |
| "IR plan", "tabletop", "forensics", "timeline", "8-K", "NIS2 notification", "recovery", "retainer" | [incident-response](modules/incident-response.md) |
| "Patch backlog", "CVE flood", "KEV", "pentest", "red team", "bug bounty", "exposure management" | [vulnerability-exposure](modules/vulnerability-exposure.md) |
| "SAST", "code review", "Copilot-written code", "threat modelling", "dependencies", "PSIRT" | [application-security](modules/application-security.md) |
| "CSPM", "CNAPP", "Kubernetes", "Terraform", "cloud roles", "firewall rules", "EDR policy" | [cloud-infrastructure](modules/cloud-infrastructure.md) |
| "Access reviews", "joiners and leavers", "PAM", "service accounts", "help-desk resets", "deepfake callers" | [identity-access](modules/identity-access.md) |
| "DLP", "data classification", "oversharing", "Copilot sees everything", "DPIAs", "certificates" | [data-privacy](modules/data-privacy.md) |
| "Phishing simulation", "awareness", "reported emails", "deepfake CFO", "fake candidates", "insider risk" | [human-risk](modules/human-risk.md) |
| "Agent identities", "prompt injection", "AI red team", "shadow AI", "MCP servers", "kill switch" | [ai-security](modules/ai-security.md) |

Pick one to three. If the user leads a whole function or a provider, start from [value-chain.md](value-chain.md).

## 4. Journey-stage boundary probes

Pick two or three. Markers and gates are in [ARCHETYPE.md](ARCHETYPE.md).

| Boundary | Ask | What decides it |
|---|---|---|
| Curious / Experimenting | "Is AI part of how any step is normally done, on more than one analyst's cases?" | Repeated use on real work |
| | "What does your policy say about logs, customer data and code in AI tools, and what would an analyst say it says?" | Lived versus paper policy |
| Experimenting / Adopting | "For the workflow you trust most, what is the baseline: alerts closed, hours per case, agreement with analyst verdicts?" | An owned, measured workflow |
| | "When the AI closed something that was real, who caught it, and how?" | Sampling of closures, not a stated intention |
| | "Where is it recorded what the AI did, with which credentials, and who approved its actions?" | Logged, attributable agent activity |
| Adopting / Scaling | "Does your second AI workflow reuse anything from the first: data connection, guides, review sampling?" | Reuse |
| | "Have you run an exercise on an AI-related incident?" (8% do this regularly, global) [ISACA-SOC-2026] | AI incident readiness |
| Scaling / AI-native | "Has AI changed how you staff, price or scope anything, or let you stop or sell something?" | Operating-model change |
| Delegation check | "Can any agent take an action without a person approving it? What are the written rules, and how would you halt it?" | The five gates in onboarding §5; 56% don't know how fast they could halt an AI system [ISACA-AIPULSE-2026] |

## 5. Phase questions

Use these in addition to each phase file's question bank.

**Frame**
- "If tier-1 triage took a tenth of the time, what would you do with the analysts: cover more sources, hunt, fix
  detections, or hold headcount flat?"
- "Where does money for AI security come from: your budget, IT, an innovation budget?" (38% fund it outside security
  [IANS-BUDGET-2026].)
- "What happens to your patching if monthly disclosures double again?" ([frontier.md](frontier.md) §2)
- "Which of your managed contracts renew in 24 months, and what might you insource?" ([disruption.md](disruption.md))

**Map**
- "Walk me through one alert, finding or questionnaire from intake to closure. Where do the hours go, by tier?"
- "Which steps are bought as a service, which as software, which staffed in house?" ([value-chain.md](value-chain.md) §7)
- "Which log sources have no detections, and how long are logs kept?"

**Diagnose**
- "Which steps produce the most rework, escalations or missed incidents?"
- "Which steps need judgment, and which are checks against a rule or a document?" (work-type table in
  [value-chain.md](value-chain.md) §6)
- "What untrusted text reaches your AI tools, and what can the AI do with its credentials?"

**Reimagine**
- "If an agent prepared every investigation with evidence and a proposed verdict, what would your analysts do?"
- "If every code change were AI-reviewed before merge, what would AppSec stop doing?"
- "If you started the function or the firm today, what would you buy, build and staff?" (lens 4)

**Prioritize**
- "Which options would your counsel, insurer or auditor block, and why?"
- "Which need data you don't collect or keep today?"
- Raise the risk weight for anything that takes containment actions or feeds a legal determination.

**Make the case**
- "What is the baseline, measured on real cases: alerts handled, time per case, misses found in sampling?"
- "What will the tool cost per seat, per investigation or per compute unit?" ([economics.md](economics.md) §4)
- "Where will juniors learn the judgment this step used to teach?" ([workforce.md](workforce.md) §6)

**Plan**
- "Who owns each agent, its permissions and its halt procedure?"
- "Which reporting clocks and rule dates fall inside the plan?" ([guardrails.md](guardrails.md) §2, [frontier.md](frontier.md) §7)
- "When do you compare the AI's closures against analysts' on the same alerts?"

## 6. Service provider variants

- "Which parts of your service would you describe to a buyer as AI-delivered and which as analyst-delivered?" (Gartner
  tells buyers to ask [EXPEL-GARTNERMDR-2026].)
- "How much of delivery cost is analyst time per client, and what happens to margin and price if agents take tier 1?"
- "At renewals, do clients ask about AI, outcome metrics or warranties?" ([economics.md](economics.md) §4)
- "How do you train new analysts if agents close most first-pass cases?"
- Testing firms: "How do clients ask about your use of AI, and what do you sell once finding gets cheap?"
- IR firms: "Which parts of an investigation could an agent prepare, and what must stay with your lead?"

## 7. Sensitive topics

- **Incident and vulnerability detail.** Never ask for open vulnerabilities, credentials, incident specifics or client
  names. Ask for volumes, ranges and roles.
- **Attack techniques.** Keep attacker AI to what defenders must plan for; do not discuss exploit detail.
- **Unapproved tools.** Normalise first (§2), after some rapport.
- **Personal liability.** CISOs may worry; use [guardrails.md](guardrails.md) §3, without legal advice.
- **Jobs.** If a leader worries about analysts, use [people-and-change.md](../../method/people-and-change.md) and
  [workforce.md](workforce.md); do not promise outcomes.

## 8. Vocabulary to mirror

| Term | Meaning | Note |
|---|---|---|
| SOC; tier 1, 2, 3 | Security operations centre; triage, investigation, deep analysis | Where most AI evidence sits |
| SIEM; SOAR; EDR/XDR | Log platform; playbook automation; endpoint and cross-domain detection | The data AI reads |
| MDR; MSSP | Managed detection and response; managed security service provider | The provider side |
| Detection engineering; detections-as-code | Writing and testing rules; storing them as code | Builder roles |
| False positive; false negative | An alert on harmless activity; a missed attack | Misses are the worst failure |
| MTTD; MTTR | Mean time to detect; to respond or resolve | Activity metrics; ask about decision quality too |
| CVE; KEV; CVSS | Vulnerability record; known exploited list; severity score | Volume doubled in 2026 |
| PSIRT | Product security incident response team | Inbound reports |
| TPRM; trust centre | Third-party risk management; portal of security documents | GRC |
| ITDR; PAM; JML | Identity threat detection; privileged access; joiner-mover-leaver | IAM |
| Prompt injection; MCP | Instructions hidden in content a model reads; standard for connecting models to tools | AI security |
| Materiality; significant incident | Legal determinations that start reporting clocks | Stay with people |

**Words to avoid:** "AI replaces the SOC", "fully autonomous defence", "lights-out SOC", "the AI decided". Say instead
"agent-prepared investigation", "analyst decision", "sampled closures", "approval rules for actions", "named owner".

## 9. Sources

Keys not listed here are in [sources.md](sources.md).
