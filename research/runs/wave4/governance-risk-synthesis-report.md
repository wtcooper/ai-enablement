# Synthesis report: security / governance-risk (wave 4)

Compiled 2026-10-17. Outputs:
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/governance-risk.md`
(275 lines) and `.../security/use-cases/governance-risk.yaml` (21 entries). `scripts/validate.py` reports no errors
for either file (0 errors overall at the time of the run).

## Counts in and out

| Input | Candidates |
|---|---|
| Practice deep dive (P) | 16 (A 3, B 8, C 4, D 1) |
| Discourse deep dive (D) | 18 (A 0, B 1, C 11, D 6) |
| Governance deep dive (G) | 14 (A 3, B 0, C 6, D 5) |
| Routed from other security files | about 25 items; none a full new use case. Used: Trail of Bits AI handbook (into 18), CSA STAR for AI automated AI-CAIQ scoring (16), ISACA AI-policy figures (17, 18), workforce data (20), board and regulation items (10, 14, §6) |
| **Total in** | **48 candidates** |
| **Out** | **21 use cases** |

## Duplicates merged

| Out | Merged from | Note |
|---|---|---|
| 01 Customer questionnaires | P01, G01, D03 (questionnaire remark) | Scope normalised to step |
| 02 Trust centre with AI agent | P02, G01 (Synthesia agent) | |
| 03 Agent-drafted vendor assessments | P03, D03, G09 | P graded A; lowered to B (see grade mix). Ladder normalised to delegate |
| 04 Continuous vendor monitoring incl. embedded AI | P04, D04, P16 | P16 idea folded in as labelled idea |
| 05 Control and evidence mapping | P05, G03 (framework part) | |
| 06 Evidence collection and control monitoring | P06, G02, D01 | G graded A; lowered to B. Ladder normalised to automate |
| 07 Agents test controls and build workpapers | P07 | Ladder automate to delegate per vocabulary example |
| 08 Policy drafting and upkeep | P08 (drafting), D17 | |
| 09 Policy gap analysis | G04, G05, P08 (consistency checks) | |
| 10 Regulatory mapping from shared principles | P12, D11, G03 (Ukrainian RAG proposal) | |
| 11 Risk register triage and drafts | P09 | |
| 12 Risk quantification with AI | P10, D07, G06 | |
| 13 Risk analyses for the firm's own AI | D06, D08, D18, G13 | Four guidance items, one change to the work |
| 14 Board reporting | P11, D12, G07 | |
| 15 Audit responses and audit consolidation | P15, G08 (audit evidence part) | G08 regulator-notification part cross-referenced to incident-response-15 |
| 16 Verifying automated attestations | D02 | |
| 17 Security team as enterprise AI policy author | P14, D05, D16 | |
| 18 Security function's own AI-use policy | G10, G11, D14, D15, routed Trail of Bits handbook | Runtime controls cross-referenced, not duplicated |
| 19 GRC engineering operating model | P13, D10 | |
| 20 Operating model and roles around AI oversight | G12, G14 | |
| 21 Apprenticeship for juniors (idea) | D09 | |

Dropped as separate entries and cross-referenced instead: D13 (AI-assisted micro tabletops; incident-response-02 and
-17 cover it), G11 and D14 as stand-alone runtime-control entries (ai-security-07/08/10/11/12, operations-19/20
cover them; the GRC policy angle went into 18), G08's regulator-notification drafting (incident-response-15).

Canonical keys chosen where angles differed: TECHTARGET-BOARD-2026, TECHTARGET-CISO-2026, TECHTARGET-AIREG-2026
(discourse used TECHTARGET-GARTNER*; the cross-cutting file uses TECHTARGET-GARTNER-REG-2026), RSAC-WORKFORCE-2026
(= SANS-WORKFORCE-RSAC-2026), CSA-MYTHOSREADY-2026 (= CSA-STORM-2026). FAIR-CRMSURVEY-2026 (PDF) and FAIR-SOCRM-2026
(blog summary) are kept as two documents.

## Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 10, 13, 16 | 18 | 17, 21 (D) | 6 |
| augment | 08, 09, 11, 14 | 04, 05, 12, 15 | 19 | 9 |
| automate | 01 | 02, 06 | | 3 |
| delegate | | 03, 07 | 20 | 3 |
| Total | 8 | 9 | 4 | 21 |

Every ladder level and scope has entries. Thin cells: automate has no model-scope entry (no evidence of, for example,
a provider selling AI-answered assurance as a service); delegate rests on one B (03), one announcement (07) and one
survey-based entry (20). No model-scope entry has a measured outcome.

## Grade mix

A 2 (01, 05), B 11 (02, 03, 04, 06, 08, 09, 11, 15, 17, 18, 19), C 7 (07, 10, 12, 13, 14, 16, 20), D 1 (21). A/B
share 62%.

- **Grade A rule applied.** Kept A: 01 (GitHub's 93% against a stated 12-month goal and Carta's header metrics are
  presented as tracked programme metrics, vendor-published; the Carta analyst's 72-of-77 anecdote is noted as a
  recollection) and 05 (Samsara's control and evidence counts). Lowered: 03 from A to B (Samsara's "up to 50%
  faster" has no baseline or method; Hyperproof's customer is anonymous; Calastone's figure is an analyst's
  description); 06 from A (governance angle) to B (figures measure platform automation, AI not isolated). Synthesia's
  "18 months to 3" and "1.5 months" are counterfactual estimates and are labelled so in 05.
- **B entries** rest on named deployments without AI-specific measurement (Synthesia, Calastone, Cengage, Sendbird,
  Trail of Bits) or present-tense job postings (Anthropic, Plaid, OpenAI, Cloudflare, Figma, GitLab, Okta).
- **Provenance.** Every A/B figure is vendor-published. Independent figures are lab studies (ReCon, Scalable Delphi,
  CIS-Controls risk scoring, access-control policy translation) and surveys (ISACA, ISC2, SANS/GIAC, WEF, PwC, FAIR).
- **Borderline to watch.** 01 (A on vendor-published metrics with no definition of "automated" or of accuracy); 18
  (B on one firm's handbook described in its own blog post).

## Gaps

- No override, error or parallel-run data for AI questionnaire answers, vendor assessments, control mapping or
  evidence checks; no auditor-reliance statement; no regulator inspection finding.
- **Data conflict:** the practice and governance angles read ISACA's 2026 release as 56% involved in AI policy and 8%
  running regular AI-specific exercises (64% none); `security-x-guardrails-regulation.md` read 60% and 71% none and
  could not find the 8%. The module flags it; someone should re-open the release and correct whichever reading is wrong.
- Named in-house deployments for AI-drafted board packs, regulator notifications and LLM-built FAIR analyses: none.
- Primary documents not reached: CISA agentic guide body, ISO/IEC 42001, SEC rule text, NYDFS and MAS AI guidance,
  Gartner primary research, full ISACA, SANS, PwC and FAIR reports, the CSA "AI-First Security Organization" draft.
- Small and mid-size teams, sector regulators, cyber insurance and non-US/EU regulators are barely covered.
- Vendor case-study pages are undated; sitemap last-modified months stand in for publication dates.
- application-security.yaml was being renumbered while this file was written, so cross-references to it are by title.

## Routed to other modules (collected from the three inputs)

- **ai-security:** ISO 42001 certification at Samsara and Synthesia and Vanta's ISO 42001 audit lessons; Kovrr AI risk
  quantification and shadow-AI discovery (KOVRR-2026); Optro AI Governance (FairNow) and OneTrust; EU AI Act
  obligations; CISA/partner agentic guidance, NIST COSAiS, CSA AI Controls Matrix, FINRA agent risks, Splunk's 78% with
  dedicated AI-agent teams; AI vendors' disclosure practice (USENIX-PIAO-2026); OpenAI-Hugging Face containment debate
  (RESILIENTCYBER-KORMAN-2026, DARKREADING-ROGUE-2026); FAIR AI attack-surface model.
- **incident-response:** ISACA AI-specific exercises and playbooks (ISACA-SOC-2026); post-incident policy gap proof of
  concept (ARXIV-2601.03287, also used in 09); micro tabletops and notification clocks (RESILIENTCYBER-TABLETOP-2026);
  Centene living-timeline pipeline (FIRST-CON-2026); agent-incident reporting to regulators (DARKREADING-AUSREPORT-2026).
- **vulnerability-exposure:** Gartner's top emerging risk (GARTNER-EMERGING-2026); AI vulnerability storm and VulnOps
  (CSA-MYTHOSREADY-2026); GTIG vulnerability trends; Ireland NCSC statement (GOVIE-NCSC-2026).
- **application-security:** code-quality studies of AI-written code and pipeline gates (FAIR-AGENTICCODING-2026).
- **identity-access:** agent identity and privilege review (FAIR-RISKREPORT-2026, FAIR-ATTACKSURFACE-2026).
- **security-operations:** Vanta/Optro service-account detection and access-review features; guardrail proxy and
  org-scoped agent runtime (ARXIV-2610.09906, ARXIV-2605.30604); breach-cost association with security AI
  (IBM-CODB-2026); live CTF study (USENIX-TANG-2026); BSides/FIRST defenders-using-AI study.
- **human-risk / data-privacy:** Proofpoint's 37% of material data loss from AI misuse or misconfiguration; employee
  GenAI restrictions; PwC data-risk measures (49% data classification, 48% DLP); BSides "The Meeple Problem".
- Not used: Coinbase compliance-agent postings (financial-crime compliance, not security GRC).

Items routed **to** governance-risk from other security files and how they were handled: ai-security governance
(CSA STAR for AI scoring into 16; security team's own AI policy into 17/18; AI insurance and credential market left to
the archetype guardrails and workforce files); application-security (Trail of Bits handbook into 18; CRA, SSDF and
"compliance without per-change review" left to regulation file); incident-response, operations, threat-intelligence,
identity-access, cloud, vulnerability-exposure (SEC, NIS2, DORA, AI Act, BOD 26-04, NCSC, workforce data): covered at
archetype level in `security-x-guardrails-regulation.md` and `security-x-workforce-talent.md`, summarised in module
§6-§7; human-risk (Grant Thornton governance gap, CSD-GT-2026) not used beyond a pointer, as only a fraud figure was
recorded.

## Suggested improvements to the briefs

1. **Give one canonical key registry per archetype before the angles run.** Five documents had two keys each here
   (TechTarget Gartner pieces, SANS/GIAC slides, CSA briefing).
2. **Ask angles to quote survey figures with the exact sentence and to cross-check against the cross-cutting files.**
   The ISACA conflict (8% vs 71% none) survived three research passes.
3. **Say how to grade "up to" figures and counterfactual estimates** ("would have taken 1.5 months") in vendor case
   studies; the A rule covers recollections but not these.
4. **Set ladder and scope examples for GRC work** (questionnaires, vendor assessments, continuous monitoring). The
   three angles labelled the same use cases differently (automate vs augment, step vs process, delegate vs augment).
5. **Tell module researchers where runtime agent controls live** (ai-security, operations) so the governance angle
   records the policy layer only and does not rebuild those entries.
6. **Ask for auditor-side evidence explicitly** (audit firms' statements on AI-prepared evidence, PCAOB/AICPA
   guidance); it is the largest gap and no angle searched for it directly.
