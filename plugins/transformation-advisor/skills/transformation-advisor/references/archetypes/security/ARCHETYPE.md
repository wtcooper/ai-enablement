# Security (archetype)

Last researched 2026-10-17. The index for the security archetype: read it once onboarding points to security, then
load only the module and archetype files the conversation needs. Source keys in brackets resolve in
[sources.md](sources.md).

## What it covers

Protecting an organization's systems, data, identities and people, and the AI it builds, buys and runs. The value
chain follows the NIST CSF 2.0 functions: Govern, Identify, Protect, Detect, Respond, Recover ([value-chain.md](value-chain.md)).
AI is both a tool in defenders' work and a new thing to secure; attackers' use of AI appears only as context. What is
bought is lower risk at an acceptable cost: detection and response, fewer exploitable flaws, controlled access, evidence.

## Who it serves

- **In-house security functions** (the CISO organization): SOC, AppSec, cloud, IAM, GRC, data protection, awareness,
  AI security. Budgets are flat for many (median growth 0% for a second year; average 5%) [IANS-BUDGET-2026].
- **Security service providers:** MDR and MSSP firms, penetration-testing and red-team firms, incident-response
  retainer firms, security consultancies. Gartner's 2026 MDR guide (as quoted by a vendor) defines MDR as
  "AI-augmented, human-led" [EXPEL-GARTNERMDR-2026].
- **Typical users:** CISOs and deputies, heads of SOC, detection, AppSec, IAM or GRC; provider CEOs and practice leads.

## What it extends

Nothing for in-house teams: the security function is its own value chain. **Security service providers** also use
professional-services (pursuit, scoping and pricing, staffing, delivery, billing), which is not yet written; use the
method and the library for those parts. Security differs from other fields in three ways. The counterparty is an
adversary that adopts AI too. Several legal clocks start from a human determination (materiality, "significant
incident"), and no rule read bans AI in triage or response ([guardrails.md](guardrails.md)). And the defenders' own AI
is part of the attack surface [ARXIV-2605.24421].

## Recognition cues

Match on what is delivered, to whom and who regulates it, not on job titles. Cues that point to security:
- In-house: "the CISO", "our SOC", "alert fatigue", "tier 1", "SIEM", "EDR", "SOAR", "detections", "MTTR".
- "AppSec", "SAST", "PSIRT", "bug bounty", "patch backlog", "KEV"; "IAM", "access reviews", "joiners and leavers", "PAM".
- "GRC", "security questionnaires", "TPRM", "SOC 2 readiness", "board reporting", "NIS2", "DORA", "SEC 8-K".
- Providers: "we run MDR or an MSSP", "per endpoint", "24/7 SOC for clients", "pentest", "red team", "IR retainer",
  "tabletops for clients".
- AI security: "agent identities", "prompt injection", "AI red teaming", "shadow AI", "OWASP LLM Top 10", "MCP servers".

**Not security:** issuing a SOC 2 report, attesting to controls or giving assurance over AI systems (assurance:
soc-attestation and assurance-over-ai). Preparing for those audits and answering customers' questionnaires stays here
(governance-risk). Fraud run by fraud or risk teams outside the CISO: use human-risk and identity-access only for the
parts the security team owns. Privacy law advice with no security work belongs to legal (no archetype yet).

## Modules

**Evidence** is each module's share of use cases graded A or B (strong: 50% or more; moderate: 30-49%; thin: under 30%);
counts are as of the last review. **Most A and B figures are self-reported by the deploying team or published by a
vendor; the independent figures are mostly surveys, benchmarks and lab tests, and no module has an independent
production miss, override or error rate.** Use thin modules for risk awareness and interview probes, not as proof points.

| Module | What it covers | Evidence |
|---|---|---|
| [governance-risk](modules/governance-risk.md) | Customer reviews, vendor risk, control evidence, policy, risk quantification, board reporting, the security team's own AI policy, workforce model. Figures are GRC vendors' customer stories | strong (11 of 21 A/B) |
| [operations](modules/operations.md) | The SOC and MDR: detection engineering, triage, investigation, response actions, measuring the SOC's AI. Six A grades: five on deployers' own figures, one on a Microsoft-authored study | strong (20 of 24 A/B) |
| [threat-intelligence](modules/threat-intelligence.md) | Intelligence cycle, enrichment, reporting, sharing, threat hunting. Two entries carry measured figures | strong (14 of 24 A/B) |
| [incident-response](modules/incident-response.md) | Plans, exercises, forensics, containment, recovery, regulatory notices, and incidents caused by AI agents | strong (12 of 22 A/B) |
| [vulnerability-exposure](modules/vulnerability-exposure.md) | Discovery, validation, prioritisation, remediation, disclosure, pentest and red-team services; the 2026 disclosure surge | strong (16 of 25 A/B) |
| [application-security](modules/application-security.md) | Threat modelling, AI-written code, code review, pipeline scanning, AI fixes, supply-chain intake. A grades come from Cloudflare, Google and one testing firm (Trail of Bits) | strong (15 of 17 A/B) |
| [cloud-infrastructure](modules/cloud-infrastructure.md) | Posture, runtime, Kubernetes, IaC, network and edge, endpoints including machines that run coding agents | thin (5 of 24 A/B) |
| [identity-access](modules/identity-access.md) | Joiner-mover-leaver, requests and reviews, privileged access, authentication, ITDR, proofing, help-desk and caller fraud | moderate (11 of 24 A/B) |
| [data-privacy](modules/data-privacy.md) | Discovery, classification, DLP, access governance, keys, privacy engineering, data exposure through AI tools | moderate (8 of 21 A/B) |
| [human-risk](modules/human-risk.md) | Awareness and simulation, reported email, impersonation and deepfakes, hiring verification, insider risk. Defender figures are on vendor pages | strong (9 of 18 A/B) |
| [ai-security](modules/ai-security.md) | Securing the organization's own AI: red teaming, agent identity and containment, monitoring, AI supply chain, AI incidents, governance. Figures come mostly from AI labs' own test settings | strong (20 of 25 A/B) |

Security architecture is a lens inside governance-risk, cloud and AppSec; OT has no module ([value-chain.md](value-chain.md) §7).

## Journey-stage markers (security)

Stage names and gates follow [onboarding.md](../../method/onboarding.md) §5. Place each scope (team, SOC, function or
provider) by markers you can see or count, not by self-rating.

| Stage | Markers in a security team or provider | Ready for the next stage when |
|---|---|---|
| **Curious** | No rule on pasting alerts, logs or code into public tools; AI appears in the risk register only as an attacker capability; no inventory of AI tools or agents; 13% of ISACA respondents do not use AI in security operations at all [ISACA-SOC-2026] | A written rule covers logs, customer data and code; named analysts use approved AI weekly on real cases |
| **Experimenting** | Analysts use assistants individually for queries, scripts and reports (most SOCs: 79% use AI, 36% in a defined workflow) [SANS-SOC-2026]; a vendor copilot trialled in the SIEM; no accuracy baseline | One workflow (phishing triage, alert enrichment, questionnaires) has an owner, a baseline against analyst verdicts, written approval rules for actions, and logging |
| **Adopting** | AI is a defined, measured step; closures sampled; an inventory of sanctioned and unsanctioned AI and agents; agent actions logged and attributable; OWASP lists used in reviews | Two or more workflows in production; the second reused the first's data, guide or review sampling; one place records value; a named owner for the security team's AI |
| **Scaling** | Agents take most tier-1 volume with sampled review; AI drafts and tests detections; agents get scoped, short-lived identities; AI incident exercises run (8% do this regularly) [ISACA-SOC-2026]; metrics move from incident counts to decision quality | Value shows in cost per case, coverage or margin, and leaders ask what to stop, sell or price differently |
| **AI-native** | Analysts work as reviewers and engineers of agents; continuous automated testing of the estate; priorities driven by threat intelligence rather than severity alone; providers priced on outcomes, not analyst hours | Re-diagnose at each review. No organization has published an independent measure of an AI-native cost or quality advantage |

**Quick check:** 56% in an ISACA poll did not know how fast they could halt an AI system after an incident
[ISACA-AIPULSE-2026]. **Delegation:** plan it only at Adopting or later, behind the five gates in onboarding §5. Reference
case: an agent investigates alerts end to end while on-call engineers correct it (operations `#09`; Figma, self-reported).

## Files in this archetype

| File | Read when | What it gives you |
|---|---|---|
| [interview-guide.md](interview-guide.md) | Onboarding, and on entering each phase | Security wording, module chooser, boundary probes, phase and provider questions, vocabulary |
| [value-chain.md](value-chain.md) | Map; choosing focus modules; unit breakdown | NIST CSF 2.0 functions, processes and key steps with work types, linked to modules |
| [economics.md](economics.md) | Frame; Make the case; budgets, pricing or margins | Budgets, market, provider pricing units, consolidation, insurance, AI pricing pressure |
| [state-of-ai.md](state-of-ai.md) | Onboarding (evidence early); Frame | Surveys, measured versus announced, quality evidence, maturity spread |
| [frontier.md](frontier.md) | Frame (why now); Reimagine lens 4; Plan dates | Dated signals for the next 12-36 months and what each means for a leader |
| [guardrails.md](guardrails.md) | Frame constraints; Reimagine fit checks; Make the case risks | Reporting clocks, accountability, AI rules, insurance, steps that need a person |
| [workforce.md](workforce.md) | Role evolution; capacity choice; any fear for roles | Gap studies, roles, pipeline, skills, provider staffing, the apprenticeship question |
| [disruption.md](disruption.md) | Provider or function scope; Frame exposure; lens 4 | Business-model scenarios with evidence status and signals to watch |
| [objections.md](objections.md) | When the user pushes back | Cross-cutting objections with evidence-based responses |
| [sources.md](sources.md) | To resolve a source key, or to plan more research | The source landscape and the shared source list |
