# Synthesis report: security / operations (wave 4)

Compiled 2026-10-17. Outputs:
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/operations.yaml`
(24 use cases) and `.../security/modules/operations.md` (290 lines). `scripts/validate.py` reports no errors or
warnings for either file (the remaining errors are in the tax archetype).

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 20 | 23 | 19 | 62 |
| Grades in (A/B/C/D) | 7/9/4/0 | 5/8/9/1 | 2/2/10/5 | 14/19/23/6 |

Plus items routed to operations by other security files (used: CyberProof managed-SOC case, Hugging Face anomaly
triage, the tl;dr sec note on detections that page no one, SIABench triage accuracy, the SherAgent spot-check).

**Out: 24 use cases** (`security-operations-01` to `-24`); 90 distinct source refs in the YAML plus 18 in the module's
own Sources list.

## 2. Duplicates merged

| Out | Merged from (P = practice, D = discourse, G = governance) |
|---|---|
| 01 Elastic-style context-grounded triage pipeline | P01, D02, D21 |
| 02 Precedent retrieval | P02, D01 |
| 03 SIEM-embedded triage agent proposes a disposition | P07, P08, D07, G01 (P08, D07, G01 are the same Cisco/Splunk event SOC) |
| 04 Phishing-report triage agent | P03 |
| 05 AI SOC analyst closes the benign Tier-1 majority | P04, P05, plus CyberProof (routed from incident-response) |
| 06 Calibrated classifiers and decision models auto-close above a threshold | D08, D09, D10, G05, G15 |
| 07 Evidence-gated dismissal | D06, G04 |
| 08 SOCless model | P06 |
| 09 End-to-end investigation agent, on-call supervises | D03, D04 |
| 10 Controlled studies (CSA 148-person study, university SOC) | P16, D23, G02 |
| 11 Agent narratives help new analysts | P09 |
| 12 Analyst copilot and chat assistants | P15, D19, G17 (idea, folded in as guardrail), D15 (self-hosted model) |
| 13 Report drafting for sign-off | P12, G14 |
| 14 LLM triage of anomaly signals (Hugging Face) | D14, plus tl;dr sec item (routed from application-security) |
| 15 Detection rule drafting, translation and judging | P13, P14, G12 (report-to-rule part left to threat-intelligence-14) |
| 16 Detection validation by coding agents | D12 |
| 17 Triage-to-detection tuning PRs | D11 |
| 18 No-code agent workspace | P11 |
| 19 Constrained-action response | P17, G08 |
| 20 Per-action authority, observability and kill switch | D18, G09, G10 |
| 21 Measuring the SOC's AI | P18, D17, G03, G16, plus CyberProof QA sampling |
| 22 Agent-led, human-accountable MDR; buyer diligence | P10, D16, G19 |
| 23 SOC staffed as builders | P19, D20 |
| 24 Idea: autonomous defender agents | D22 |

**Not kept as operations entries (cross-referenced instead):**
- D05 (Grow Therapy daily hunts) and P20 (Microsoft Dynamic Threat Detection Agent) duplicate
  `security-threat-intelligence-21` and `-22`.
- D13 and G13 (DNB notebooks; Centene OCSF timelines) duplicate `security-incident-response-07` and `-04`.
- G06 (SherAgent) is `security-incident-response-08`, which holds its production audit data.
- G12's report-to-rule benchmarks (CTI-REALM, SIGMERGE, AUTOSIGMA) overlap `security-threat-intelligence-14`.
- G07 (log content as adversarial input) became a guardrail in the module and in entries 01, 13, 19; the use case
  itself overlaps `security-incident-response-11` and ai-security.
- G11 (RSAC SOAR playbook, measured but not AI) is noted in entry 03 and the guardrails.
- G18 (OMB M-26-14 logging maturity) moved to guardrails and metrics; it is a regulatory benchmark, not an AI use case.

Other cross-references added in notes: 12 to incident-response-03; 19 to incident-response-14; 21 to incident-response-11
and -12; 22 to identity-access-16; 23 to incident-response-25 and identity-access-12.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 1 (12) | 1 (21) | 0 | 2 |
| augment | 8 (02, 03, 07, 10, 11, 13, 14, 19) | 2 (15, 17) | 1 (23) | 11 |
| automate | 1 (04) | 4 (01, 05, 06, 20) | 1 (08) | 6 |
| delegate | 0 | 4 (09, 16, 18, 24) | 1 (22) | 5 |

Every ladder level and scope is covered. Thin spots: assist (plain copilot use is common but rarely written up);
model scope (three entries, none above grade B: Mysten Labs vendor case study, MDR provider claims, hiring data);
delegate at model scope rests on MDR vendor claims (grade C).

## 4. Grade mix

Out: **A 6, B 13, C 4, D 1** (19 of 24 A/B, 79%).

- A: 01 (Elastic tracked verdict correctness), 02 (Figma pages), 09 (Figma time to resolution), 12 (Microsoft
  live-operations study), 15 (Amazon RuleForge), 21 (Elastic tracked agreement metric).
- Downgraded under the 2026-10-17 grade A rule: P04 ECS, P05 Zapier, P06 Mysten Labs (customer statements in
  Dropzone-written case studies, no method) from A to B; D06 (Grow Therapy's approximate noise shares and a research
  benchmark) from A to B; G02 CSA study (measured but simulated and vendor-supported; two of three angles capped it at
  B) from A to B.
- Provenance: nearly all outcome figures are self-reported or vendor-published. Independent figures are academic
  benchmarks (ALERT-BENCH, REFINE, AIDR, the guardrail proxy, log-injection studies), the university SOC study and
  the SANS survey.

## 5. Gaps

- No independent, production-scale false-negative rate, override rate or parallel-run result from a named SOC. This
  is the module's central evidence gap; entry 21 tells advisors to have clients measure their own.
- MDR and MSSP economics (pricing, margin, staffing) only as qualitative vendor statements.
- Small and mid-size security teams appear only in vendor case studies.
- No regulator sets AI-specific SOC performance thresholds; no authoritative view on whether SOC AI is high-risk under
  the EU AI Act, or how NIS2 or DORA reporting clocks interact with AI triage. No APAC or Middle East SOC guidance read.
- No hard data on junior-analyst hiring effects beyond one vendor's sample of 665 postings.
- Gated or paywalled: SANS SOC and AI survey bodies, Gartner Hype Cycle and MDR Market Guide, CSA's full report,
  ISACA report (the 8% AI-exercise figure is unverified), IBM report PDF. Most arXiv papers were read at abstract level
  though marked `access: full`.
- Routed items not used: CrowdStrike Charlotte AI triage benchmark (product page, from threat-intelligence practice);
  Cloudflare agentic Managed Defense harness (title only); Push browser-layer detection and Blackpoint identity AI SOC
  agent (identity discourse; the latter search-only); Optro/Vanta service-account detection; CISA "Tale of Two SOCs"
  advisory (no AI content); Vodafone CISO's "human on the loop" remark (DR-RSAC-2026); Daylight Security and Con
  Edison hunting loops (agenda titles only); NDSS KnowHow provenance detection; UNPROMPTED metrics session.

## 6. Routed to other modules (collected from the operations inputs)

- **threat-intelligence:** threat-hunting agents (Microsoft Threat Hunting Assistant, CrowdStrike Agentic Recon,
  Google Threat Hunting agent, Dropzone AI Threat Hunter) and Microsoft's Threat Intelligence Briefing Agent
  [MSFT-DEFENDER-AGENTS-2026, CROWDSTRIKE-AGSOC-2026, TECHINFORMED-GOOGLE-2026]; CoAnalyst and OSINT copilot sessions
  [FIRST-CON-2026]; external internet-intelligence argument [RESILIENTCYBER-FASTER-2026]; CyberSOCEval
  [ARXIV-2509.20166]; ENISA Threat Landscape 2026 [ENISA-ETL-2026].
- **incident-response:** Centene living timelines, Flare StealerLens, DFIR agents, PSIRT 2.0 (85% of APAC PSIRTs have
  fewer than five members) [FIRST-CON-2026]; Hugging Face's self-hosted forensic model [HUGGINGFACE-INCIDENT-2026];
  DNB notebooks [CAUCHY-IRNB-2026]; BSides "After the Jailbreak" playbook [BSIDESLV-2026]; hierarchical agentic IR
  validated in a digital twin, 18-31% better recovery than frontier-LLM baselines [ARXIV-2608.15016]; LLM response
  planning with up to 22% shorter recovery [NDSS-IRPLAN-2026]; CISA/NIST/NSA key practices [CISA-KEYPRACTICES-2026];
  NIST SP 800-61 Rev. 3 [NIST-SP80061R3-2025].
- **vulnerability-exposure / application-security:** vulnerability remediation prioritisation agents at a regional
  health system and a German municipality [CROWDSTRIKE-AGENTWORKS-2026]; GM multi-agent bug-bounty triage
  [BSIDESLV-2026]; PSIRT 2.0 [FIRST-CON-2026].
- **ai-security (threats, agent identity):** log-borne prompt injection, poisoned artifacts, DFIR agent manipulation
  [ARXIV-2605.24421, FIRST-CON-2026]; PromptArmor report on a vendor SOC assistant [PROMPTARMOR-ELASTIC-2026]; agent
  containment incidents [REGISTER-BHDC-2026, DETENGWEEKLY-167-2026]; CEL-rule EDR plugin for coding agents
  [DETENGWEEKLY-166-2026]; agent identities and scoped credentials for SOC agents [MSFT-DEFENDER-AGENTS-2026]; OWASP
  Agentic Top 10, ATT&CK v20 AI techniques, NIST COSAiS, agentic attack-surface SoK; IBM: 92% of organisations with an
  AI-related incident lacked proper AI access controls [BAKERDONELSON-IBM-2026].
- **identity-access:** IBM guidance to scope and attribute agentic identities [IBM-CODB-2026].
- **security-governance-risk:** SEC disclosure rules and rescission push; EU AI Act, NIS2, DORA timelines; UK and EU
  financial-supervisor statements [COOLEY-UKFIN-2026, AOSHEARMAN-ESRB-2026]; workforce data [ISC2-WORKFORCE-2025];
  ISACA AI-exercise finding [ISACA-SOC-2026].
- **cross-cutting (x-economics, x-workforce, x-state-of-ai-disruption):** MSSP margin effects, cost per investigation,
  "AI costs more than people" [DROPZONE-EUMSSP-2026, ELASTIC-TOKENS-2026, EXPEL-3LEADERS-2026]; SOC job descriptions
  [DROPZONE-JD2030-2026]; Gartner's "AI-augmented, human-led" MDR and agent washing [EXPEL-GARTNERMDR-2026,
  DROPZONE-GARTNERHC-2026].

## 7. Reference and date normalisation

- Same document, different refs in the inputs (canonical first): ELASTIC-ACCURACY-2026 = ELASTIC-TRIAGE-2026 =
  ELASTIC-AGENTICSOC-2026; EXPEL-PRECEDENT-2026 (the discourse file used EXPEL-RUXIE-2026 for this post, while practice
  used EXPEL-RUXIE-2026 for Expel's product page: a collision); CSA-SOCBENCH-2025 = CSA-BENCH-2025;
  CSA-SOCBENCH-PR-2025 = CSA-DROPZONE-2025; ARXIV-2604.12040 = AWS-SIRBENCH-2026; GOOGLE-TIN-2026 =
  GOOGLE-SECOPS-TIN-2026.
- Across sibling module YAMLs: HNS-GARTNER-2026 vs HELPNET-GARTNER-2026; HUGGINGFACE-INCIDENT-2026 vs
  HF-DISCLOSURE-2026; DATABRICKS-JOB-IR-2026 vs DATABRICKS-JOB-2026; the module cites the DNB notebook post as
  CAUCHY-IRNOTEBOOKS-2026 to match incident-response. A shared registry would fix these.
- Date conflicts resolved: ARXIV-2610.10608 given as 2026-10 (inputs say 06 or 07); SANS-AI-2026 as 2026-05-18
  (metadata; page displays 2026-08-17); SANS-SOC-2026 as 2026 (page undated; one input inferred 2026-06).

## 8. Suggested improvements to the briefs

1. **Give angle researchers a shared ref registry** (or have them check the landscape and sibling files first). The
   EXPEL-RUXIE-2026 collision and three CSA/Elastic aliases cost verification time.
2. **Put the grade A rule in the angle briefs**, with the case-study example. Five entries were graded A by the angles
   and had to be downgraded here.
3. **Say whether a measured controlled study without a deployment can be A.** The angles split on the CSA study.
4. **Ask governance angles to flag guardrail-only or regulatory items** (log hardening, SOAR baseline, logging
   maturity) instead of numbering them as use cases; they inflate candidate counts.
5. **Record abstract-only reading separately from full reading.** `access: full` currently covers both.
6. **Run module syntheses in an order, or share sibling ids early.** Threat-intelligence and incident-response
   finished during this synthesis and had already absorbed Grow Therapy, DNB notebooks and SherAgent; a routing table
   agreed at angle stage would avoid the late re-cut.
7. **Settle `function` for in-house security teams** (technology-it vs service-delivery); the angles mixed them.
