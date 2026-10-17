# Synthesis report: security / cloud-infrastructure (wave 4)

Compiled 2026-10-17. Outputs:
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/cloud-infrastructure.md`
(300 lines) and `.../security/use-cases/cloud-infrastructure.yaml` (24 entries). `scripts/validate.py` reports no
errors for either file; it warns that the YAML is below the 50% A/B target (21%). The one remaining error is in
`archetypes/tax/ARCHETYPE.md`, which another agent is writing.

## Counts in and out

| Input | Candidates |
|---|---|
| Practice deep dive (P) | 17 (A 1, B 6, C 9, D 1) |
| Discourse deep dive (D) | 18 (A 2, B 4, C 9, D 3) |
| Governance deep dive (G) | 16 (A 0, B 0, C 1, D 15) |
| Routed to cloud-infrastructure from other security files | 9 items; none a full new use case (see below) |
| **Total in** | **51 candidates** |
| **Out** | **24 use cases** |

## Duplicates merged

| Out | Merged from | Note |
|---|---|---|
| 01 Rank posture findings by context; agent fix-first plans | P12, D01, G03 | G03 idea folded in as research evidence |
| 02 Agent investigates and closes low-severity cloud detections | P02, D03 | SecRespond benchmark from G09 kept as a caution |
| 03 In-house triage agent over posture findings | P05 (WRITER), D02 (Cohere) | Cohere lowered A to B (see grades) |
| 04 GuardDuty attack-sequence correlation | P04 | Lowered B to C |
| 05 Read-only Kubernetes triage agent | P10, D13 | Log-injection evidence from G11 |
| 06 Remediation agent: owner, root cause, ticket or PR | P03, D04, CrowdStrike part of P12 | |
| 07 Evidence-gated automated remediation | D05, G06 | G06 idea (PatchWeaver) folded in |
| 08 Least-privilege changes as IaC pull requests | P06 and D06 (AWS, Smolen parts), G05 | |
| 09 Multi-agent cloud identity "team" | P06 and D06 (Horsman parts) | Split from 08: delegate, not augment |
| 10 AI-assisted IAM privilege-escalation discovery | D07 | Lowered B to C (abstract) |
| 11 Guardrails and verification for AI-written and AI-repaired IaC | P07, D09, G01, G02, G04 | Three ideas and one practitioner idea folded into a C entry |
| 12 Drift detection and IaC reconciliation (idea) | G07 | Only reconcile-exceptions entry |
| 13 WAF virtual patching | P08, D08 | |
| 14 Firewall rule hygiene | P09 | |
| 15 Intent-to-rule authoring with impact checks | D16, G08 | |
| 16 Coding-agent guardrails on developer endpoints | D17 | |
| 17 EDR policy tuning agents (idea) | G10 | |
| 18 LLM-assisted detection engineering and rule QA | P14, D12 | |
| 19 Agent-run attack simulation knowledge layer (idea) | D10 | |
| 20 Cloud canaries for AI attackers (idea) | D11 | |
| 21 Continuous compliance and policy as code | P13, G12 | |
| 22 Shared security AI platform team | P15 | |
| 23 Managed cloud security on a multi-tenant platform | P16 | |
| 24 Runtime control layer (idea) | D18 | |

**Not kept as entries; cross-referenced by full id instead of duplicated:**

- P01, D14 (Wiz Red Agent perimeter agent) → `security-vulnerability-exposure-21`. project44's combined Red and Green
  figure stays in 06.
- G14 (AWS Security Agent 33 of 37 CVEs) → `security-vulnerability-exposure-17`.
- P11 (CrowdStrike reasoning triage classifier) → `security-operations-06`, which already cites ARXIV-2607.28460.
- P17 (verdict-triggered containment, constrained action vocabulary) → `security-operations-19` and
  `security-incident-response-11`; the Blue Agent's verdict-to-playbook step is in 02.
- D15 (egress-controlled sandboxes) and G15 (containment controls) → `security-ai-security-10`, `-06`, `-07`, `-12`,
  as the brief asked. Datadog's and Roblox's sandbox talks appear in the module's roles section (§10 sources).
- G09 (cloud incident investigation benchmarks) → incident-response (`security-incident-response-04`, `-09`).
- G11 (operations agents and telemetry sanitisation) → `security-ai-security-13`; its figures support 05.
- G13 (secret-extraction agent) → `security-ai-security-09`.
- G16 (in-tenant CSPM rule derivation) dropped: single-author architecture paper with no results.

Canonical keys where the inputs differed: DATADOG-SOCS-2025 (governance used DATADOG-CLOUDSEC-2025 for the same
report); WIZ-BLUEAGENT-CASE-2026 (discourse used WIZ-BLUEAGENT-2026 for the same URL).

## Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 18 | | | 1 |
| augment | 01, 04, 05, 06, 10, 12 (D), 14, 15, 20 (D) | 03, 08, 11, 13, 21 | 22, 23 | 16 |
| automate | 17 (D) | 02, 07, 16, 24 (D) | | 5 |
| delegate | | 09, 19 (D) | | 2 |
| Total | 11 | 11 | 2 | 24 |

Thin cells: assist has one entry (job postings and an abstract); delegate has one talk abstract and one idea; model
scope has two entries, neither with outcomes. No evidence was found for assist at process or model scope, or for
automate or delegate at model scope; no entries were invented to fill them. The strongest delegate evidence near this
module is autonomous pentesting (`security-vulnerability-exposure-17`).

## Grade mix

A 1 (02), B 4 (03, 06, 16, 22), C 14 (01, 04, 05, 07, 08, 09, 10, 11, 13, 14, 15, 18, 21, 23), D 5 (12, 17, 19, 20,
24). A/B share 21%, below the 50% target; grades were not raised to reach it.

Applying the 2026-10-17 grade A rule and the instruction that fwd:cloudsec abstracts cannot support A or B:

- **02 kept at A, borderline.** It rests on ZS's own three-month validation with an internal framework ("around
  95.17%"), which the page presents as a tracked figure, not a recollection. Against it: the figure is quoted with
  "around" on an undated vendor page and the method is unpublished. Redis's 85.7% over 431 cases is published by Wiz,
  not Redis. Owkin's "10 out of 10" is a recollection and stays labelled as one. A verifier may reasonably lower 02 to B.
- **Cohere (03) lowered A to B.** Its figures are vendor headline metrics with no stated method, and the 30-minute to
  2-hour baseline reads as an estimate.
- **Seth Art (10) lowered B to C; Datadog sandbox (D15) would have been C.** Both rest on abstracts.
- **GuardDuty (04) lowered B to C.** A vendor's claim about its own service, with no named customer.
- **Databricks (22) kept at B, borderline.** A named organisation describes its own team, but only in a job posting.
- Raji's Kubernetes agent (05) runs in production at an unnamed organisation, so its maturity is set to piloting.

## Routed items picked up (from other security files)

| Item | From | Use |
|---|---|---|
| CERT-In: agents entered through exposed credentials and permissive cloud roles | ai-security governance; vulnerability-exposure | Module §1, §6, §9 (THN-CERTIN-2026, CERTIN-CIAD0049-2026) |
| Kubernetes operator RBAC audit (Unit 42) | ai-security agent identity | Already `security-ai-security-09`; cross-referenced in 08 notes |
| Unit 42 on AWS managed policies for compromised IAM credentials (2026-09-21) | ai-security agent identity | Lead only, not opened by any input; listed as a gap |
| Wiz AI SAST code-to-cloud context (WIZ-AISAST-2026) | application-security | Module §8 frontier |
| Wiz Red Agent exposure example | vulnerability-exposure; application-security | Cross-reference to `security-vulnerability-exposure-21` |
| LLM policy synthesis for cloud IAM (ARXIV-2503.11573) | identity-access | Already `security-identity-access-11`; cross-referenced in 08 |
| Entra Actor-token flaw (DIRKJANM-ACTORTOKENS-2025) | identity-access | Not used: not an AI use; better kept in identity-access |
| Secrets served live by production web code (ARXIV-2609.23042) | identity-access governance | Not used: abstract-level, overlaps `security-ai-security-09` |
| CISA/NIST IR 8587 cloud identity-provider guidance | identity-access governance | Not used: identity, not AI in cloud operations |

## Routed to other modules (collected from the three inputs)

- **vulnerability-exposure:** AWS Security Agent 33 of 37 CVEs and the per-deploy pentest gate (AWS-SECAGENT-2026,
  AWS-CONTINUUM-GATE-2026); Wiz Continuous Vulnerability Assessment (WIZ-CVA-2026); Unit 42 Continuous Frontier AI
  Defense (PANW-UNIT42-CFAD-2026); BOD 26-04; Seth Art's privilege-escalation workflow (also kept here as 10); GTIG
  trends, NCSC patch wave, ENISA vulnerability sections, CSA Frontier Ready material, DBIR; VulnCheck's Glasswing
  reconciliation and Patch the Planet funnel (RESILIENTCYBER-RECEIPTS-2026); exposure-time SLAs
  (RESILIENTCYBER-SHIFTLEFT-2026).
- **application-security:** Google pre-submit agentic scanning (GOOGLE-AGENTICSCAN-2026); Red Agent's GitHub Actions
  finding in a Snowflake repository (WIZ-REDAGENT-SNOWFLAKE-2026); AWS Deception Benchmark; AI-written code studies
  (ARXIV-2608.28021, ARXIV-2602.03648).
- **security-operations:** CrowdStrike AgentWorks customer quotes and three reasons agentic SOCs fail
  (CROWDSTRIKE-AGENTWORKS-2026, CROWDSTRIKE-AGSOC-2026); Prophet, Dropzone, Figma and Elastic triage items; IEEE S&P
  LLMs-in-the-SOC study; USENIX crowdsourced Sigma study; log-analysis injection (ARXIV-2607.14493).
- **incident-response:** Centene's OCSF timeline pipeline (FIRST-CON-2026); Wiz multi-cloud investigation
  (WIZ-BLUEAGENT-CASE-2026); SIR-Bench, SecRespond, Holmes and the cloud forensics framework; cloud IR simulation bias
  talk; OpenAI's response errors.
- **ai-security:** OpenAI-Hugging Face incident, Anthropic evaluation incidents, CERT-In in full; agent-identity and
  confused-deputy talks (FWDCLOUDSEC-MOGULL-2026); CSA agent surveys; NIST COSAiS; CSA AI Controls Matrix; FedRAMP AI
  prioritisation; Brucato's benchmark (also kept here as 20).
- **identity-access:** non-human identity debt (FWDCLOUDSEC-WADDELL-2026); Datadog long-lived credentials; Unit 42 on
  identity in almost 90% of investigations; Prose2Policy.
- **threat-intelligence:** Google's account of AI-assisted attackers and LLMjacking (GOOGLE-CISOPERSP-2026); Sysdig's
  JADEPUFFER account (SYSDIG-RUNTIME-2026).
- **governance-risk:** sovereign security operations (PANW-DT-2026); asking vendors for false-alarm rates; Gartner
  predictions (search-only); EU AI Act timing, NIS2, DORA third-party designations, FINRA, IBM breach cost.
- **data-security-privacy:** Red Agent classification and redaction of exposed data; CSA DLP survey (title only).
- **ot-critical-infrastructure (optional):** Palo Alto Frontier AI Critical Defense Program partners (Siemens, Idaho
  National Laboratory, Mitsubishi Electric, Axis Communications, EPRI).

## Gaps

- No independent measurement of any cloud-security agent: no override, false-negative or parallel-run data from a
  third party, and no regulator inspection finding. All customer figures sit on vendor pages.
- Endpoint protection beyond developer endpoints (classic EDR, XDR) and network security (NGFW, SASE,
  microsegmentation) have no named-customer outcomes; firewall evidence is product documentation.
- Primary vendor material not reached: Google Security Command Center AI features, Microsoft Defender for Cloud agent
  pages, Sysdig and Orca customer outcomes, Unit 42 cloud posts; CISA's own pages were blocked (BOD 26-04 comes from
  a vendor summary).
- All fwd:cloudsec evidence is abstract-level; talk recordings were not viewed, so failures and numbers given only in
  talks are missing. Wiz customer pages are undated.
- Not covered: AI for cloud cost and FinOps; small and mid-size teams; non-US/EU regulators other than CERT-In;
  junior-analyst hiring effects; the effect of AI on headcount.

## Suggested improvements to the briefs

1. **Put the conference-abstract cap in the research briefs.** Practice and discourse graded several abstract-only
   entries B (Seth Art, Datadog sandbox). Stating "abstracts cap at C" up front would save regrading.
2. **Declare module boundaries before research.** Seven candidates duplicated entries already owned by ai-security
   (containment), vulnerability-exposure (Red Agent, AWS Security Agent), operations (endpoint triage, constrained
   actions) or incident-response. A one-line split rule per module pair would stop the duplicate work.
3. **Ask the governance angle to attach research to practice entries, not mint ideas.** 15 of its 16 candidates were D
   ideas built on preprints; most became evidence inside practice entries. A rule such as "propose an idea only when
   no practice entry covers the change" would cut merge effort.
4. **Keep a shared source-key registry per wave.** The inputs used two keys for the Datadog report, the Blue Agent case
   post, the Snowflake post and the AWS Continuum gate post, and different source types for the OpenAI and Anthropic
   incident reports (firm vs vendor).
5. **Clarify the A rule for customer-validated figures on vendor pages.** Say whether a customer's tracked figure
   quoted with "around" on a vendor page (ZS) is A, and whether vendor headline metrics for a named customer (Cohere)
   can ever be A.
6. **Define maturity for production use by an unnamed organisation** (Raji's Kubernetes agent), and whether a job
   posting describing a team counts as a named deployment (Databricks).
7. **Point practice researchers at the thin areas:** classic EDR/XDR and firewall vendors' customer stories, Google
   and Microsoft cloud-posture agent documentation, and talk recordings where abstracts promise failure data.
