# Synthesis report: security / incident-response

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-security.md`, `security-incident-response-practice.md` (P, 19 candidates),
  `security-incident-response-discourse.md` (D, 17), `security-incident-response-governance.md` (G, 16), plus the
  "Routed to other modules" sections of every other `security-*.md` file in wave 4.
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/incident-response.md` (291 lines)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/incident-response.yaml` (22 entries)
- **Validator:** `INFO .../incident-response.yaml: 22 use cases, 12 graded A/B (55%)`. No ERROR or WARN lines for
  these files. The 8 remaining errors overall are all in `archetypes/tax/ARCHETYPE.md` (another module's work). A script
  check confirmed that every bracketed key in the module is in the YAML or in the module's §10, every inline ref in a
  YAML entry is in that entry's `sources`, and every `outcomes[].source_ref` is in its entry.
- **Not yet verified.** This output needs the verification pass against the sources themselves.

## 1. Counts in and out

| | Practice | Discourse | Governance | Routed in | Total |
|---|---|---|---|---|---|
| Candidates in | 19 | 17 | 16 | 3 used (see below) | 52 + 3 |
| Merged into this module's YAML | 17 | 14 | 15 (G02 in part) | 2 (Cloudflare reviewer, ARXIV-2601.03287) | |
| Left in another module's entry (cross-referenced, not duplicated) | 2 (P04, P16) | 3 (D04, D06, D16) | 1 (G12) + G02's design | 1 (GTIG-AVDH) | 7 |

- **Out:** 22 use cases. 15 are merges of two to four candidates; 7 come from one candidate or from routed items.
- **Landscape:** no entries of its own; used for context, frontier dating and two corrections the angles had already
  made (RSAC SOC post dated 2026-08-24, not March; its 9-hour saving came from a SOAR playbook, not AI).
- **Late change.** The security-operations, vulnerability-exposure, identity-access and threat-intelligence YAML files
  appeared while this synthesis was running. Three drafted entries duplicated entries there and were removed, and the
  list was renumbered from 25 to 22 (see §2).

## 2. Duplicates merged

| Output | Merged from | Choices made |
|---|---|---|
| 01 IR plan review vs NIST 800-61 | P10, D08, G06 | Same Fortinet abstract. Pattern document-to-decision (P, D) |
| 02 AI tabletop builder | P11, D09 | D09 (academic idea, D) absorbed into a C entry. G found no AI scenario generation; P found Immersive's release |
| 03 Model-access readiness | D02 | Also routed by ai-security governance and security-operations discourse |
| 04 Timeline reconstruction | P02, D01, D03, G04 | Hugging Face (D01) and Google Timesketch (P02) give B; Centene kept as a source but its pipeline lives in security-operations-12 |
| 05 Agent drives forensic tools | D05, G03 | Protocol SIFT plus SIABench/ExCyTIn/CyberSOCEval benchmarks; G03's C lifted to B by D05 |
| 06 Magnet evidence leads | P03 | |
| 07 SherAgent provenance agent | P05, D07, G01 | **Grade C (P, D) over B (G)**: deploying SOC unnamed. Ladder delegate/process (G) over augment/step (P, D). Provenance self-reported for the audit figures |
| 08 Root-cause ranking (Meta, Grafana) | P15 | Capped at B: reliability incidents |
| 09 Verify findings and harden tools | D15, G11, G02 (part) | AIDA design and figures left in security-operations-07; baseline miss rate kept as a risk |
| 10 Microsoft guided responses | P06 | |
| 11 Guardrailed automated containment | G16, D17 (playbook part) | Maturity emerging (D) over in-production (G): no named AI-driven case |
| 12 Idea: validated LLM response planning | P17, G05, D17 (research part) | Grade D (P) over C (G, D). Closed-command design left in security-operations-20 |
| 13 Cyber recovery and resilience | P12, D11, P13 | Block job posting folded in for BC/DR |
| 14 Incident summaries (Google) | P01 | Grade A kept under the 2026-10-17 rule (measured comparison, 300 summaries) |
| 15 Regulator notifications | P07, D10, G13 | Step (D, G) over process (P). DORA clock per G's reading of Art. 5(1) |
| 16 Post-incident report review | routed: Cloudflare (app-sec discourse), ARXIV-2601.03287 (governance-risk practice) | New entry; no IR angle opened these sources |
| 17 Prepare for AI-agent incidents | G09, P18, G07, G10 | G07 and G10 (C, survey-only) absorbed into B |
| 18 Agent forensics / ADR | D12, G08 | Ladder automate (G) over assist (D) |
| 19 Monitors page responders | P09, D13 | |
| 20 Staged AI review of agent records (OpenAI) | P08, G14 | G14 (idea, NIST practice 5.5) folded in as guidance. Grade A kept: counts OpenAI reports as data; no accuracy figures |
| 21 SAFE and agent-incident notification | P19, D14, G15 | B (P) over C (D, G) because OpenAI's notifications are a named practice |
| 22 Responders as builders | P14 | |

**Left in other modules (cross-referenced by id):** D04 DNB notebooks → security-operations-12; D16 agent evaluation
scenarios → security-operations-22; G12 / GTIG-AVDH Mandiant harness in IR engagements →
security-vulnerability-exposure-04; P16 PSIRT agents → security-vulnerability-exposure-08; P04/D06 StealerLens →
threat-intelligence (infostealer-log triage is security-threat-intelligence-03); G02's AIDA design →
security-operations-07. Module §3 points to these ids and to security-operations-13, -14, -20 and -25.

**Ref normalisation.** One key per document: OPENAI-HFROAD-2026 (D: OPENAI-ROAD-2026); NIST-KEYPRACTICES-2026 (D:
NIST-CAISI-2026 for the same URL); SANS-AI-2026 (D: SWIMLANE-SANSAI-2026); EUR-LEX-DORA301-2025 and EUR-LEX-NIS2-2022
(P: EU-DORARTS-2024, EU-NIS2-2022); FLI-AIACT73-2024 (P: EU-AIACT-ART73-2024); HF-DISCLOSURE-2026 (ops discourse:
HUGGINGFACE-INCIDENT-2026); NDSS-HAMMAR-2026 (ops governance: NDSS-IRPLAN-2026). The two Mandiant M-Trends documents
are different pages and keep separate keys (MANDIANT-MTRENDS-2026 blog summary; MANDIANT-MTRENDS-EXEC-2026).

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 03, 06, 10 | 17 | 21 | 5 |
| augment | 01, 02, 08, 09, 13, 14, 15, 16 | 04, 20 | 22 | 11 |
| automate | 11 | 18, 19 | | 3 |
| delegate | | 05, 07, 12 | | 3 |
| **Total** | 12 | 8 | 2 | 22 |

- **Delegate** has no named deployment with outcomes: 05 is a SANS research tool, 07 an unnamed SOC (preprint), 12
  an idea. The Mandiant harness (a named delegate-style case) sits in security-vulnerability-exposure-04.
- **Automate** rests on AI-agent monitoring (18, 19, both B) and guidance for containment (11, C).
- **Model scope** is thin: a draft reporting scheme plus OpenAI notifications (21) and job postings (22). No firm was
  found selling agent-delivered IR, and no evidence shows a step that stopped existing. Delegate/model and
  automate/model are empty; nothing was invented to fill them.
- **Maturity:** in-production 10 (03, 04, 08, 14, 16, 17, 18, 19, 20, 22), piloting 5 (01, 05, 07, 09, 21), announced 5
  (02, 06, 10, 13, 15), emerging 2 (11, 12).

## 4. Grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 2 | 14 (Google summaries, 2024), 20 (OpenAI staged review) |
| B | 10 | 03, 04, 05, 08, 16, 17, 18, 19, 21, 22 |
| C | 9 | 01, 02, 06, 07, 09, 10, 11, 13, 15 |
| D | 1 | 12 (labelled "Idea") |

- A/B share 55%. Input grade claims were lowered in three places (G01 B → C; D16 B → left in ops-22, where it is
  measured as a vendor test; G14 D and G10 C absorbed). None were raised on their own evidence; merged B entries took
  the strongest named case.
- Entry 20's A speaks to scale (counts OpenAI reports as data), not accuracy; no precision or recall for the AI stages
  exists. Entry 14's A is from April 2024, outside the 18-month window, and unreplicated.
- Provenance: academic authors measuring their own prototype are marked `independent` with "authors' own evaluation"
  in `measures` (P and D practice); SherAgent's audit figures are marked `self-reported` because they describe the
  deployment's own spot-checks (G's view). G marked AIDA and the digital-twin figure self-reported.

## 5. Gaps

- **Quality evidence.** No override or acceptance rates, parallel runs, error rates for AI-written incident reports, or
  regulator inspection findings on AI in IR. Measured items are Google's 2024 study, OpenAI's counts, SherAgent's
  unnamed-SOC audit and lab benchmarks.
- **Named deployments** in forensics platforms (Magnet, Microsoft, Rubrik) and in IR retainer firms' own investigations:
  none found.
- **Recovery, BC/DR and exercises:** vendor scenarios, one job posting and one product release. No AI in business-impact
  analysis, recovery-time testing or a real exercise.
- **Regulatory reporting:** vendor material only; no regulator statement on AI-drafted notifications. SEC Item 1.05
  rescission status and the EU single reporting point remain unconfirmed.
- **Workforce:** no data on junior hiring or headcount effects in IR teams.
- **Unopened primaries:** OpenAI technical incident report PDF, Linux Foundation SAFE RFC text, M-Trends 2026 full
  report, ISACA and SANS full reports, FIRST slides (abstracts only, some TLP:AMBER), Timesketch slide deck.
- **Routed items not used:** VECTRA-SPIDER-2026 (Scattered Spider help-desk intrusion timeline; attack narrative, no AI
  in the response); CISA BOD 26-04 forensic-triage steps and the CRA reporting page EC-CRAREPORT-2026 (the CRA clock is
  carried through EUR-LEX-CRA-2024); M-Trends mean time to exploit (-7 days) belongs to vulnerability-exposure.
- **To verify:** entry 16's "blocks closure of high-severity incidents" wording comes from the application-security
  discourse file's routing note; no IR angle opened CLOUDFLARE-CODEX-2026.

## 6. Routed to other modules (collected from the three IR inputs)

- **security-operations:** Google SecOps Triage Agent (GOOGLE-SECOPS-TIN-2026; about 60 s average, 20 min maximum);
  Cisco/Splunk .conf26 triage agent dashboard (CISCO-SPLUNK-CONF26-2026; event observations, not benchmarks); RSAC SOC
  SOAR saving (SPLUNK-RSACSOC-2026); CyberProof MTTR 16 to 6 minutes, unnamed client (CYBERPROOF-CASE-2026); ALERT-BENCH
  and CORTEX (ARXIV-2610.10608, ARXIV-2510.00311); FIRST CoAnalyst and TandemTrace sessions; Elastic 60% to 92% verdict
  agreement (ELASTIC-AGENTICSOC-2026); Figma triage memory (DETENGWEEKLY-166-2026); Daylight and Con Edison hunt agents
  (SANS-DFIRSUMMIT-2026); SIABench triage accuracy (GPT-5 98%, Claude-4.5-Sonnet 96%, GPT-4o-mini 75% on 100 alerts);
  KnowHow provenance detection (NDSS-KNOWHOW-2026); surveys SANS-SOC-2026, SANS-AI-2026, PROPHET-SOC-2026.
- **ai-security:** log-borne prompt injection (ARXIV-2605.24421, USENIX-LOGINJECT-2026); FIRST sessions on poisoned
  artifacts and DFIR-agent exploitation; OpenAI and Anthropic evaluation-containment failures (OPENAI-HFROAD-2026,
  ANTHROPIC-EVALINC-2026, ANTHROPIC-ALIGNSEC-2026); MCP and AI-IDE security; coding-assistant permission frameworks
  (BSIDESLV-2026); OWASP and MITRE ATLAS; EU testing platform (EC-ACTIONPLAN-2026); agent-identity controls behind
  entries 17 and 18 (CERTIN-CIAD0049-2026).
- **threat-intelligence:** Apura OSINT copilot and Flare StealerLens (FIRST-CON-2026); Unit 42 AI-assisted attack case
  (UNIT42-AIATTACK-2026); M-Trends 2026 adversary tradecraft (MANDIANT-MTRENDS-2026).
- **vulnerability-exposure:** CERT-In blueprint on AI-assisted exploitation (CERTIN-BLUEPRINT-2026); CRA reporting
  obligations for manufacturers from September 2026 (FIRST TXOne session; EUR-LEX-CRA-2024 Art. 14(2)); PSIRT 2.0
  agentic architecture (FIRST-CON-2026); Mandiant source-code harness (MANDIANT-AIRR-2026, GTIG-AVDH-2026).
- **application-security:** patch-quality debates and AI code-review evidence (G).
- **security-governance-risk:** workforce and skills (ISC2-WORKFORCE-2025, ISACA-SOC-2026); SEC Item 1.05/106 status
  and board reporting (SEC-CYBER-2023, SIFMA-SEC-2026); AI Act and NIS2 programmes; AI incident-response governance and
  accountability (ISACA-AIPULSE-2026, ISACA-AIPULSE-EU-2026); junior-pipeline worry (SANS-SIMON-2026); open-weight
  policy debate (DETENGWEEKLY-165-2026).

## 7. Suggested improvements to the briefs

1. **Freeze or sequence cross-module inputs.** Other modules' YAML appeared mid-run, forcing three late removals and a
   renumber. Either run syntheses in a fixed order or give each a snapshot list of existing ids at start.
2. **Shared ref registry.** At least eight documents carried two keys across wave-4 files (see §2). A registry
   (URL → key) checked by `validate.py` would stop drift.
3. **Provenance for academic self-evaluation.** Angles disagreed on whether authors testing their own prototype are
   `independent` or `self-reported`. Add one rule to the vocabulary.
4. **Unnamed deploying organisation.** SherAgent has measured production data from an unnamed SOC; angles graded it B
   or C. State the grade explicitly in the vocabulary.
5. **"AI in IR" versus "IR for AI".** Half the module's B entries are readiness for incidents caused by AI agents. Say
   in the brief whether these count as use cases and how they relate to ai-security.
6. **Living-page dates.** One vendor page got three dates across files (Swimlane: 2026-05-18, 05-20, 08-17). Ask
   researchers to record the date source (byline, metadata, or access date).
7. **Routed items need a reader.** Items routed in from another module's research (Cloudflare reviewer) were never
   opened by this module's angles; ask the receiving angle, or the synthesis, to open them before use.
