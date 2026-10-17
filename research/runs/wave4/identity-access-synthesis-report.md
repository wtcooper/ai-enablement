# Synthesis report: security / identity-access

Prepared 2026-10-17. Outputs:

- Module: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/identity-access.md` (269 lines)
- Use cases: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/identity-access.yaml` (24 entries)
- `python3 scripts/validate.py`: no errors for these files. One warning: 11 of 24 graded A/B (46%), below the 50%
  target. Grades were not raised to meet it. (The validator's remaining errors are in `archetypes/tax/ARCHETYPE.md`,
  outside this task.)

## 1. Counts in and out

| Input | Candidates | Grades in |
|---|---|---|
| Practice angle | 20 | A 3, B 7, C 9, D 1 |
| Discourse angle | 16 | B 2, C 12, D 2 |
| Governance angle | 14 | C 8, D 6 |
| Landscape scan | 0 (leads only) | n/a |
| Items routed to identity-access from other security angle files | 6 pointers (section 6) | n/a |
| **Total in** | **50 candidates** | A 3, B 9, C 29, D 9 |
| **Out** | **24 use cases** | A 1, B 10, C 12, D 1 |

47 of 50 candidates are merged into the 24. Three are not carried as entries: discourse 12 (Silverfort AI
attack-chain simulation; security testing, routed to vulnerability-exposure, figures kept in the module frontier),
governance 11 (LLM triage of identity telemetry for insider cases; idea on synthetic data, routed to
security-operations and human-risk) and governance 12 (learned password-guessing models for strength audits; idea,
attacker-side abstract). 90 distinct source refs are used in the YAML; 16 more appear only in the module's Sources
section.

## 2. Duplicates merged

P = practice, D = discourse, G = governance; numbers are each angle's own ids.

| Out | Merged from | Note |
|---|---|---|
| 01 Conditional Access policy-gap agent | P01, D03 | D03 scoped step and graded C; kept process (scan made continuous) and B |
| 02 Passkey adoption campaigns | P02 | |
| 03 LLM access-request reviewer | P05, D14 | D14 was process; kept automate step (approval step automated, exceptions to people) |
| 04 Zero standing privilege, JIT | P11, D09, G10 | G10 was augment; kept automate |
| 05 Conversational IT and access assistant | P06, D11 | |
| 06 Access review recommendations | P04, D01, G08 | |
| 07 Role mining and right-sizing | D02, G09 | |
| 08 Continuous posture checks and evidence | P10, G14 | G14 (D idea, full-population evidence) folded in |
| 09 Governance queries and lifecycle drafting | P07, D10 | |
| 10 Agentic application onboarding | P12 | |
| 11 Policy as code (idea) | P20, D16 | |
| 12 IAM engineers using AI coding tools | P19 | |
| 13 Risky-user summaries | P03, D04 | D04 was assist; kept augment |
| 14 Risk-scored sign-ins and sessions | P08, G06 | G06 was augment; kept automate |
| 15 Closed-loop ITDR response | D05 | |
| 16 MDR for SaaS identity | P09 | Re-scoped process to model (sourcing change) |
| 17 Agentic hunting for identity attacks | D13 | |
| 18 Enforced help-desk verification | P17, D08, G05 | P17 graded A; downgraded to B (see section 4) |
| 19 ML identity proofing | P16, D07, G01, G02 | |
| 20 Identity graph and 1:N search | P18, G03 | |
| 21 Passive caller authentication | P13 | Only A |
| 22 Call risk scoring | P14 | P14 graded A; downgraded to B |
| 23 Synthetic-voice detection | P15, G04, D15 | D15 (audio language models, idea) folded in |
| 24 Behavioural biometrics, continuous authentication | D06, G07, G13 | |
| not carried | D12, G11, G12 | See section 1 |

**Source-key reconciliation.** Canonical keys: MSFT-CAAGENT-2026 (= MS-CAAGENT-2026), MSFT-RISKYUSER-2026
(= MS-ENTRA-RISKYUSER-2025), MSFT-LIFECYCLE-2026 (= MS-ENTRA-LIFECYCLE-2025), MSFT-ARREC-2026
(= MSFT-ENTRA-ACCESSREV-2026; date 2026-03-12 kept over the retrieval date), MSFT-ENTRAWN-2026
(= MS-ENTRA-WHATSNEW-OCT-2026), OKTA-TI-2026 (= OKTA-TI-INVARIANTS-2026), OKTA-AUTHSURVEY-2026 (= OKTA-YUBICO-2026),
FINCEN-DEEPFAKE-2024 (= FINCEN-ALERT004-2024), NIST-SP80063-4-2025 (= NIST-80063-2025; DOI URL used),
CISA-IR8587-2026 (= CISA-NIST-IR8587-2026), PANW-IDLANDSCAPE-2026 (= PANW-LANDSCAPE-2026, an excerpt page of the
same report), PANW-IDIRA-2026 (landscape's PANW-PRESS-2026 index). **Key collision:** practice used FBI-IC3-2025 for
the FBI public service announcement of 2025-05-15 and governance used it for the 2025 Internet Crime Report; the PSA
is renamed FBI-IC3PSA-2025. The archetype-level merge should confirm. **Date conflict:** the CISA IR 8587 press
release is dated 2026-09, 2026-09-09 and 2026-09-15 by the three angles; the month is used. **Same case, two URLs:**
the Reality Defender bank case study was read at two URLs (REALITYDEFENDER-BANK-2026, REALDEFENDER-BANK-2025) with the
same figures; both refs are kept in entry 23.

## 3. Coverage by ladder and change scope

| Ladder \ scope | step | process | model |
|---|---|---|---|
| assist | 09, 12 | none | none |
| augment | 06, 07, 11, 13, 23, 24 | 01, 05, 10, 22 | 16 |
| automate | 03 | 04, 08, 14, 15, 18, 19, 20, 21 | none |
| delegate | none | 02, 17 | none |

- **Model scope: one announced entry (16).** No evidence of new identity services, pricing or sourcing models built
  on AI beyond CrowdStrike's MDR announcement.
- **Delegate: two entries, neither a customer deployment.** 02 is Microsoft documentation; 17 is a vendor's own
  detection-engineering team (adjacent process).
- **Assist at process or model: none.** Not filled.
- **Automate-process** is the largest cell, but 04, 14 and 15 are largely rule-based controls with an AI label.

## 4. Grade mix

A 1 (4%), B 10 (42%), C 12 (50%), D 1 (4%). A/B share 46%.

- **Grade A rule (2026-10-17) applied.** Practice graded three entries A. Kept: 21 (MSUFCU average authentication
  time over 90 days and HealthEquity IVR match rate are tracked operating metrics, though vendor-published).
  Downgraded to B: 18 (Cisco's "three-to-four-hour" to "five minutes" is a principal engineer's description in a
  Persona story, explicitly not a measured average) and 22 (HealthEquity's "over 90%" is an executive statement with
  an undefined metric; VEC's $500K has no derivation; the 800 flagged calls are activity, not confirmed fraud).
- **B entries** rest on named deployments without measurements (Instacart, Okta, Prosper, Cisco, Push Security) or
  on job postings (Coinbase, Cloudflare). Two B entries (05, 17) are adjacent processes.
- **Provenance:** every A/B figure is vendor-published or self-reported. The independent figures (SANS ITDR survey,
  DHS identity-validation test, USENIX VoiceWukong and passkey studies, arXiv policy-synthesis preprints, FBI IC3)
  measure threats, baselines or detector limits, not outcomes of an AI deployment.

## 5. Gaps

- **No quality evidence for AI in workforce IAM.** No override, false-approval, false-negative or parallel-run data
  for access-review recommendations, Conditional Access agents, risky-user summaries, request reviewers or ITDR
  automation. Microsoft's tooling can query overrides of AI suggestions, but nobody publishes the rate.
- **Customer evidence is thin.** No bank or health-system IGA case with AI and figures; SailPoint customer stories
  mention AI only as being explored. Primary Microsoft data behind the 26 gaps, 73% and 83% figures was not reached.
- **Independent tests not reached:** DHS S&T's 2025 Remote Identity Validation Rally reports (only vendor releases
  read); SANS ITDR report body; Verizon DBIR body; Gartner IGA guide; Entrust identity-fraud report.
- **Fraud ownership.** Identity fraud entries (20-24) sit with fraud teams, often outside the CISO; practitioner
  discourse from banks was not found.
- **No data** on identity-team headcount, IAM practitioners' AI use (no IDPro or IDSA survey), or JML automation
  outcomes with AI.
- **Regulation not examined:** US SEC Regulation S-ID, S-P and Item 1.05 in relation to identity fraud; ETSI TS
  119 461 and CEN/TS 18099 on injection-attack detection (cited by a preprint, not opened).

## 6. Routed items

**Picked up from other security angle files (routed to identity-access):**

- ai-security-agent-identity-containment: general privileged access, CISA and NIST token-theft guidance and
  non-human identity governance beyond agents belong here. Covered by entries 04, 08 and 14 and NIST IR 8587 in the
  module guardrails.
- ai-security-governance-assurance: agents as non-human identities with registries and owners
  (OWASP-STATE-AGENTIC-2026, pp. 55-56). Cited in module section 7.
- operations-governance: IBM guidance to scope and attribute agentic identities (IBM-CODB-2026); IBM-reported share
  securing non-human identities in AI workflows (BAKERDONELSON-IBM-2026, takeaway 10, not used: secondary summary).
  IBM-CODB-2026 cited in module section 7.
- threat-intelligence-discourse: DPRK fake-applicant detection stack with AI risk assessment (FIRST-CON-2026,
  Datadog session 2026-06-17; no metrics in the abstract). Module frontier only; also a human-risk item.
- vulnerability-exposure-practice: Mandiant's scoped machine identities for agents (MANDIANT-AIVM-2026). Agent
  identity, left to ai-security; not cited here.
- governance-risk-practice routed Optro/Vanta service-account detection and access-review automation to
  security-operations; cross-referenced here as provisional `security-governance-risk-07` (entry 06 notes, module).

**Routed from the identity-access angles to other modules (for their synthesis):**

- **ai-security:** CrowdStrike Agentic IdP and Continuous Identity for AI Agents (CROWDSTRIKE-AGENTICIDP-2026); Okta
  for AI Agents, Agent Gateway, kill switch, Blueprint Alliance (OKTA-AGENTS-2026); World Central Kitchen
  (OKTA-WCK-2026); Dex registration in Okta's directory and tool scoping (OKTA-DEX-2026); SailPoint Agentic Fabric and
  Autonomous Agents (SAILPOINT-IDSEC-2026, SAILPOINT-AUTONOMOUS-2026); Saviynt Agent Access Gateway and intent-aware
  runtime authorisation (SAVIYNT-IARA-2026); agentic identity parts of Idira (PANW-IDIRA-2026); Entra Agent ID
  permissions (MSFT-ENTRAAGENTS-2026); SailPoint Horizons agent figures (79% run agents in production, 2% with
  purpose-built tools) (SAILPOINT-HORIZONS-2026); Okta/Yubico agent verification (91% essential, 57% critical)
  (OKTA-AUTHSURVEY-2026); Okta Identity team role (OKTA-JOB-IDENG-2026); Forrester Identiverse and Oktane recaps
  (FORRESTER-IDENTIVERSE-2026, FORRESTER-OKTANE-2026); SANS 73% using agentic automations needing credentials with no
  governance control above 40% (SANS-ITDR-2026); Palo Alto 109:1 ratio and agent findings (PANW-IDLANDSCAPE-2026);
  Opal 2,300% growth in non-human and agent identities, 90% unreviewed (OPAL-PALADIN-2026); Gartner IAM Summit agent
  tracks (GARTNER-IAMSUMMIT-2026); Black Hat agent identity launches (SWI-BLACKHAT-2026); Anthropic and OpenAI identity
  verification and hardware passkeys for model access (FORRESTER-CLAUDEIDV-2026, FORRESTER-OPENAIPASSKEY-2026);
  OpenID Foundation agentic identity whitepaper (OPENID-AGENTID-2025); MCP server authentication study, 40.55% expose
  tools without authentication (ARXIV-2605.22333); FragFuse title (USENIX-SEC-2026-TITLES).
- **human-risk:** FBI AI voice impersonation PSA (FBI-IC3PSA-2025 here); staff cannot reliably spot AI-written messages
  (OKTA-AUTHSURVEY-2026); Pindrop deepfake readiness survey (PINDROP-DRI-2026); Above Security AI-native insider-risk
  investigations (SWI-BLACKHAT-2026); DPRK IT-worker fraud and video verification limits (NAMETAG-IMPERSONATION-2026);
  romance-baiting study, LLM agent 46% vs human 18% compliance (USENIX-ROMANCE-2026); IC3 AI employment scams
  (FBI-IC3-2025); ENISA AI-supported phishing figures (ENISA-ETL-2025); NYDFS deepfake training expectations
  (NYDFS-AIGUIDE-2024); LLM insider-threat triage benchmark (ARXIV-2603.22499; governance 11, not carried).
- **security-operations:** Falcon Complete MDR for SaaS identity (CROWDSTRIKE-AGENTICIDP-2026; also entry 16 here);
  Push browser-layer detection (PUSH-PYRAMID-2026, PUSH-SHINYHUNTERS-2026); Blackpoint identity AI SOC agent
  (MSSP-BLACKPOINT-2026, search-only).
- **vulnerability-exposure:** DBIR 2026 finding that vulnerability exploitation overtook stolen credentials as the
  leading initial access vector, median full-patch time 43 days (HNS-DBIR-2026, VERIZON-DBIR-2026); Silverfort AI
  attack-chain simulation (SILVERFORT-ASSUMPTIONS-2026; discourse 12, not carried).
- **cloud-infrastructure:** Entra Actor-token flaw (DIRKJANM-ACTORTOKENS-2025); LLM policy synthesis for cloud IAM
  (ARXIV-2503.11573, also entry 11); secrets in production web code (ARXIV-2609.23042); IR 8587 architecture guidance
  (CISA-IR8587-2026); Google IAM recommender overlap (entry 07).
- **incident-response:** Scattered Spider help-desk intrusion timeline (VECTRA-SPIDER-2026).
- **security-governance-risk:** NIST SP 800-63-4, FinCEN alert and NIST IR 8587 as deployment constraints; EU AI Act
  dates and AI Omnibus (EC-AIACT-2026); NIST AI RMF reference in SP 800-63-4; non-human credential rotation at 8%
  (SANS-ITDR-2026).
- **Out of scope, no clear home:** Affirm's transaction-fraud engineering where "most PRs are co-authored with AI"
  (AFFIRM-JOB-FRAUD-2026).

## 7. Suggested improvements to the briefs

1. **Say how to grade vendor-reported metrics for a named customer.** The grade A rule distinguishes measured
   figures from recollections but not who reports them. Entry 21's figures are tracked metrics published by the
   vendor, not the customer; a one-line rule ("vendor-published tracked metrics for a named customer can be A if
   labelled") would remove the judgement call.
2. **Ask angles to tag rule-based versus model-based automation.** Several identity "AI" features (JIT, ITDR
   playbooks, risk policies) are rules with an AI label; a field or note convention would make the automate cells
   easier to read.
3. **Give a canonical key list per archetype before the angles run.** Twelve documents had two or three keys across
   the angles, and one key (FBI-IC3-2025) pointed to two documents.
4. **Fix module boundaries up front.** Agent identity was routed in both directions between identity-access and
   ai-security; fraud sits between identity-access and human-risk. A boundary table in the landscape brief would cut
   re-routing.
5. **Ask practice angles for override or acceptance rates explicitly**, including product documentation that shows
   how to compute them (Microsoft's override queries), since that is the missing quality evidence in this module.
6. **Allow a date-conflict field** for sources whose publication date differs across angles or pages.
