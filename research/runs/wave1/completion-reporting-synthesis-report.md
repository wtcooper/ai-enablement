# Synthesis report: assurance / completion-reporting

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-assurance.md`, `assurance-completion-reporting-practice.md` (P, 17 candidates),
  `assurance-completion-reporting-discourse.md` (D, 12), `assurance-completion-reporting-governance.md` (G, 14)
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/completion-reporting.md` (288 lines)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/completion-reporting.yaml` (18 entries)
- **Validator:** `INFO .../completion-reporting.yaml: 18 use cases, 4 graded A/B (22%)`, plus the matching WARN for
  being below the 50% A/B target. No ERROR lines (0 errors overall). A script check confirmed that every bracketed key
  in the module is in the YAML or the module's Sources list, and that every inline ref in a YAML entry appears in that
  entry's `sources`.
- **Not yet verified.** This output needs the verification pass against the sources themselves.

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 17 | 12 | 14 | 43 |
| Merged into this module's YAML | 16 | 12 | 14 | 42 |
| Placed in an existing entry in another module (referenced, not duplicated) | 1 (P10 → ST-13) | part of D05 (PwC) → ST-13 | 0 | 1+ |

- **Out:** 18 use cases. 12 are merges of two to five candidates; 6 come from one candidate.
- **Landscape:** contributed no YAML entries of its own. It was used for context and cross-checks only. Per the
  governance file, two landscape claims were not carried forward as stated (see §8).

## 2. Duplicates merged

| Output | Merged from | Choices made |
|---|---|---|
| 01 Disclosure checklist first pass (Caseware, TR, Ideagen, DataSnipper) | P01, P02, P03, D01, G01 | Vendor-split entries in P merged because they describe the same change. Grade C (P, D) over B (G), see §5. Maturity piloting (P) over in-production (D, G): no named user |
| 02 Big Four platform engines (KPMG FRA, Deloitte Omnia) | P04, P05 (disclosure part), D07 | Kept apart from 01 because it is the build-not-buy route and announcement-only |
| 03 AI second look at a completed checklist | D02, G02, divergence feature from P02 | Ladder augment (D) over assist (G); pattern reconcile-exceptions (D) over draft-review-loop (G); maturity piloting (G) over in-production (D) |
| 04 "No" and "Not applicable" calls | P06, D03 | Maturity announced (D) over emerging (P) |
| 05 Management-report review (German Big 4 firm) | P07, D04, G03 | Scope step (D, G) over process (P). Grade B (P, D) over C (G), flagged |
| 06 Casting, cross-referencing, tie-out (Validate at HLB and MHA; Suralink) | P08, D05 (Suralink part), G05 (CPA.com part) | PwC tie-out (P10, D05 PwC part) left in ST-13 |
| 07 Field Financials drafting and continuous tie-out | P09, G04, G05 (Fieldguide part) | Scope process (P) over step (G); ladder augment (P, G04) over automate (G05) |
| 08 Engagement-file review assistant, sign-off readiness, pre-EQR | P12, D06, G11 | Augment, step (two of three). G11 was an idea (D); absorbed into a C entry |
| 09 Audit committee communications analysis (PwC) | P13, D08, G12 | Pattern research-brief (P, G); runtime workflow-automation (P, D) |
| 10 Going-concern model or LLM signal | P14, G08 | Grade B: G's A downgraded, P's B kept (see §5) |
| 11 ISA 570 tools (idea) | G09 | |
| 12 KAM/CAM identification (idea) | P15, G10 | |
| 13 Memo and documentation drafting, with verification gate | P11, G14, D10 | D10 (an idea for a control, not an AI use) folded in as a guardrail. Ladder augment (P) over delegate (G) |
| 14 Uniper internal audit reporting | P16 | Capped at B (adjacent process) |
| 15 FS error detection (idea) | P17 (LLM-audit part), G07 | |
| 16 XBRL consistency (idea) | D12, G06, P17 (FinAuditing part) | Ladder assist (G, P) over augment (D) |
| 17 Reviewing agent checks preparing agent (idea) | D09 | |
| 18 Agent completes workpapers (idea) | D11, G13 | |

Every source from every merged candidate was kept, except the volatile Caseware homepage (P01 notes only) and
search-only leads, which stay in notes.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 09, 10, 11, 12, 15, 16 | | | 6 |
| augment | 01, 02, 03, 04, 05, 08, 13, 14 | 07 | | 9 |
| automate | 06 | | | 1 |
| delegate | | 17, 18 | | 2 |
| **Total** | 15 | 3 | 0 | 18 |

- **No model-scope evidence.** No firm sells agent-delivered completion work, and no source describes a completion
  step that has stopped existing. The cell was left empty.
- **Delegate rests only on ideas** (`#17` from guidance and a conference panel, `#18` from a synthetic benchmark).
  No delegate deployment exists in completion.
- **Automate has one entry** (`#06`). It is also the only grade-A entry.
- **Process scope** is thin: `#07` (announced) and the two delegate ideas.
- **Maturity:** in-production 3 (05, 06, 14), piloting 4 (01, 03, 10, 13), announced 5 (02, 04, 07, 08, 09),
  emerging 6 (11, 12, 15, 16, 17, 18).

## 4. Open questions (steps with no public AI evidence)

As the caller instructed, these steps have no use cases. The module's §4 gives each one what the research found and an
interview probe:
- subsequent events
- written representations
- summary of uncorrected misstatements
- engagement quality review (AI used by the reviewer)
- KAM/CAM wording
- opinion and report drafting
- going concern in live audits
- drafting of audit committee communications
- the final analytics and completion memo

All three deep dives searched for these and found nothing beyond standards, exam material and adjacent items.

## 5. Grade mix

| Grade | In (43) | Out (18) |
|---|---|---|
| A | 2 (P08, G08) | 1 (`#06`) |
| B | 7 (P07, P10, P14, P16, D04, D05, G01) | 3 (`#05`, `#10`, `#14`) |
| C | 22 | 8 (01, 02, 03, 04, 07, 08, 09, 13) |
| D (idea) | 12 | 6 (11, 12, 15, 16, 17, 18) |

Input grades by angle: practice A1 B4 C10 D2; discourse B2 C6 D4; governance A1 B1 C6 D6. Two ideas were absorbed
into C entries (G11 into `#08`, D10 into `#13`). P10 (B) went to ST-13.

**Why 22% A/B, against a target of at least 50%.** The evidence does not support more, and no grade was inflated to
reach it.
- The disclosure checklist is the busiest step, and every figure there is vendor-published with unnamed customers.
  Practice and discourse graded it C.
- Governance graded the checklist entry B on two grounds, neither of which holds. KPMG's own engine is a firm product
  announcement, graded C under the practice convention. Caseware names its beta partners only for the Verity
  platform, not for the checklist agent.
- Big Four completion items are announcements only.
- Most other steps have no evidence at all (§4).

**Judgement calls for the verifier:**
- `#10` was **downgraded from A (governance) to B.** The BDO Netherlands thesis meets the letter of grade A: a named
  organisation and a measured outcome. But it is a ten-person student experiment on historical cases, it found no
  gain in accuracy or speed, and the governance file itself called the grade "a technicality".
- `#05` was **kept at B** (practice and discourse) over C (governance). The firm is anonymised, so a strict reading of
  "named" gives C. B was kept because a peer-reviewed independent study documents real use. If the verifier applies
  the definition strictly, the entry becomes C and the A/B share falls to 17%.
- `#01` was **kept at C.** A Withum beta partner comments on the checklist agent, but no live-engagement result is
  reported.

## 6. Gaps

- **No quality evidence for any completion tool in live use.** There is no accuracy, miss rate, false-negative rate,
  reviewer override rate or parallel-run result. MHA's "zero false positives" comes from a vendor case study with no
  sample size.
- **No inspection or peer-review finding about AI in completion steps.** IFIAR's tables carry no AI link, and the
  reason for the 2025 rise in audit committee communications findings (from 4% to 11%) was not found.
- **Big Four completion outcomes:** none. The KPMG, Deloitte and EY items are announcements. PwC says savings are
  modest.
- **Named customers** are missing for Caseware's checklist beta, TR Disclosure Review, Ideagen's AI feature and KPMG's
  engine.
- **What PwC's audit committee communications tool reads**, and who uses its output, is unknown.
- **Primary texts not read:**
  - the AICPA practice aid (behind a login)
  - the full Fabian and Ratzinger-Sakel paper (403)
  - ISA 701, 260, 700, 450 and 580, and AS 2805 and 2810
  - the FRC's Annual Review of Audit Quality 2026 (seen only through secondary summaries)
  - the Accountancy Europe GenAI paper (seen only through a Spanish summary)
- **Community voices are missing.** Reddit returned 403, and no forum or LinkedIn discussion was read.
- **Search budgets were spent** in all three deep dives.

## 7. Routed to other modules (collected from the inputs)

| Target module | Items |
|---|---|
| **substantive-testing** | Fieldguide Audit Testing Agent, "up to 70%" of testing automated (FIELDGUIDE-AGENTS-2025 / FIELDGUIDE-FIELDAGENTS-2025, vendor claim). Johnson Lambert and Provectus tie-out pipeline: 60-80 to 12-16 hours per audit, but the same page also gives 20% and 50%, and the figures disagree (PROVECTUS-JL-2026). PwC Evidence Match (PWC-AT-2025). Caseware Document Intelligence Agent and DataSnipper testing-time claims (FGMK: 30-45 minutes to about five per selection, vendor-reported) (CASEWARE-LAUNCH-2026, DATASNIPPER-CONNECT-2026). Fieldguide Field Orchestrator and its Agent Review Experience (FIELDGUIDE-ORCH-2026). Clark "Material Intelligence" (trade-news summary, not read). **PwC Audit Innovation Hub tie-out: already ST-13**; P10 adds CFODIVE-PWC-2026 (the Oct 2026 article does not mention the Hub) |
| **planning-risk-assessment** | Ally internal audit risk-and-control matrices: more than 60 hours per audit, over 75% rated Good or Great (ALLY-2024, self-reported). PwC walkthrough and Simplified Audit planning tools (PWC-AT-2025). Caseware Risk Suggestion Agent and planning-review demo (CASEWARE-CWX-2026). FRC board-minutes example (FRC-GENAI-2026). ICAEW chatbot test (ICAEW-PIERPOINT-2025). PCAOB 2025 inspection attention to companies with significant AI investment (PCAOB-PRIORITIES-2024, p.7). ISA 570 A13 on risk-assessment tools (IAASB-ISA570-2025). Fieldguide Field Planner (announced) |
| **controls-testing** | Workiva testing and regulatory-reporting agents (CPAPA-WORKIVA-2026). CAQ on "invisible AI" and "shadow AI" in ICFR, and the FEI framework (CAQ-ACI-2026-08). CAQ's six audit committee questions on AI in financial reporting (CAQ-ACI-2026-03) |
| **quality-management** | KPMG audit committee guidance on questions for the auditor (KPMG-ACAGENDA-2025). IFIAR 2025 findings for engagement quality control review (10 of 341) and review and supervision (23 of 420). Deloitte Australia refund (BNN-DELOITTEAU-2025). AICPA "one tool may check another" (AT-AICPAPA-2026). IFIAR 2026 on monitoring and recertification (IFIAR-TTF-2026). ISA 220 A63-A64 (IAASB-ISA220-2020). PCAOB staff on firm research tools (PCAOB-GENAI-2024). Links between AI investment, reissued reports and fees (FSA-DP-2025). Firm-level certification, monitoring and QC 1000, and the FRC mitigations (KN-FRC-2026, FRC-NEWS-2026). Negligence commentary (DACB-2026). Reviewer competence and automation bias (ICAEW-FRCVIEW-2026). KPMG pressing its own auditor for fee cuts, and fee and staffing pressure (RESULTSENSE-2026, secondary) |
| **acceptance-independence** | Entity AI use and acceptance or continuance (AT-AICPAPA-2026). SEC chief accountant on independence (KPMG-HOHL-2026) and the PCAOB independence project (TR-PCAOBAGENDA-2026). Big Four alliances with Anthropic and the independence question raised for EY (BIG4NEWS-2026). Management-responsibility threat from autonomous agents (CCAB-AI-2026). Who owns statements drafted by an audit-platform agent (FIELDGUIDE-FINANCIALS-2026). AU-C 210 and engagement-letter disclosure of AI (AT-AICPAPA-2026) |
| **assurance-over-ai** | Client AI governance maturity (6% advanced), AI-operated controls, AI-related representations from management, and AI oversight disclosures read as other information (BOARDMEMBER-CAQ-2026, AT-AICPAPA-2026, FIELDGUIDE-DISC-2026). Audit committee oversight of management's AI use (CAQ-ACI-2026-03, CPAB-AC-2026, AT-ACPR-2026) |
| **cross-cutting context** | EY Canvas scale figures (EY-CANVAS-2026); no completion-specific content |

## 8. Conflicts resolved and items for the verifier

- **Landscape "1,200-1,500" figure.** Per the governance file, this describes a fully completed checklist in TR's
  Guided Assurance product, not a limit of Disclosure Review. The outputs say so wherever it appears.
- **Caseware date (landscape FS16, "28 Jul 2026").** Governance found no 28 July date on the pages it opened: the
  launch release is 20 May and the CwX blog is 17 June. Practice, however, opened a different Caseware blog ("From
  AiDA to agentic") dated 2026-07-28, which repeats the 2.7-hour figure. In the outputs:
  - the 2.7-hour figure is dated to CwX (2026-06-17);
  - the launch to 2026-05-20;
  - the AiDA blog keeps its own date.
  The landscape's single ref covered three different pages, and they now have distinct keys (§9).
- **Caseware 2.7 hours: unit.** The CwX blog says "per checklist run" and the launch release says "per workflow".
  Both are noted.
- **DataSnipper ref collision.**
  - Practice's DATASNIPPER-DISCLOSURE-2025 is the "5 hidden risks" page.
  - Governance's DATASNIPPER-DISCLOSURE-2025 is a product page (/campaign/disclosure-agents).
  - Discourse called the risks page DS-RISKS-2026.
  The outputs use DATASNIPPER-RISKS-2025 and DATASNIPPER-AGENTS-2025. The risks page's date is 2025 (earliest archive
  2025-10-12), not discourse's 2026 (inferred from a mention of Connect New York 2026). Verify.
- **FABIAN-2026.** Practice used it for the university release, the other two for the JIS paper. The outputs follow
  governance: FABIAN-2026 is the paper (2026-03-03, abstract) and HAMBURG-FABIAN-2026 is the release (2026-03-20).
- **CASEWARE-CWX-2026 type:** vendor (governance, and the existing planning YAML) over conference (discourse).
- **AICPA-PA-2026 type:** professional-body (governance, and the existing YAMLs) over standard-setter (practice).
- **IFIAR-TTF-2026 URL:** the outputs use governance's opened URL (fsa.go.jp/ifiar/2026TTFReport.pdf). The
  substantive-testing YAML uses a different FSA path for the same report. Align these at verification.
- **Deloitte Omnia URL:** global press-room URL (practice, and the existing YAMLs). Governance read a US copy.
- **Deloitte/CAQ audit committee report date:** 2026-09-22 (press, Accounting Today) is used. The DART item is
  dated 2026-10-08.
- **ICAEW-FRCVIEW-2026 date:** 2026-05-06 (from the existing YAMLs). Discourse gave 2026-05.
- **Ideagen:** practice opened /lp/demos/audit-and-risk/disclose. The other two got 404 on a different URL. Its "9 of
  10 top UK firms" claim describes the Disclose product, not the AI feature, and is not used as an outcome.
- **For the verifier to check first:**
  - `#05` and `#10` grades (§5)
  - `#06`: the MHA baseline (possibly tool against tool)
  - `#01`: the 2.7-hour unit, and the DataSnipper date
  - the IFIAR inspection-theme denominators in module §6
  - module §8 quotations (Logothetis, IFIAR "human-led")

## 9. Canonical source keys mapped to input refs

| Canonical key | Practice | Discourse | Governance |
|---|---|---|---|
| CASEWARE-AIDA-2026 (AiDA blog, 2026-07-28) | CASEWARE-VERITY-2026 | — | — |
| CASEWARE-LAUNCH-2026 (launch release, 2026-05-20) | — | CASEWARE-VERITY-2026 | CASEWARE-VERITY-2026 |
| CASEWARE-CWX-2026 (CwX blog, 2026-06-17) | — | CASEWARE-CWX-2026 | CASEWARE-CWX-2026 |
| DATASNIPPER-RISKS-2025 | DATASNIPPER-DISCLOSURE-2025 | DS-RISKS-2026 | — |
| DATASNIPPER-AGENTS-2025 | — | — | DATASNIPPER-DISCLOSURE-2025 |
| DATASNIPPER-CONNECT-2026 (existing key) | — | DS-CONNECT-2026 | — |
| DATASNIPPER-AIREPORT-2026 | — | DS-AIREPORT-2026 | — |
| IDEAGEN-DISCLOSE-2026 | IDEAGEN-DISCLOSE | — | — |
| FABIAN-2026 (JIS paper) | — | FABIAN-2026 | FABIAN-2026 |
| HAMBURG-FABIAN-2026 (release) | FABIAN-2026 | (in FABIAN-2026) | HAMBURG-FABIAN-2026 |
| BOARDAGENDA-FRC-2026 (existing key) | BOARDAGENDA-FRC-2026 | BOARDAGENDA-2026 | — |
| DELOITTE-ACPR-2026 (existing key) | DELOITTE-CAQAC-2026 | DELOITTE-CAQ-2026 | — |
| AT-ACPR-2026 (existing key) | AT-ACFOCUS-2026 | AT-ACRISK-2026 | — |
| KPMG-ACAGENDA-2025 (existing key) | KPMG-AC-2026 | — | — |
| AT-AICPAPA-2026 (existing key) | — | AT-AICPAPA-2026 | ATODAY-AICPAPA-2026 |
| AT-PCAOBPE-2025 (existing key) | — | AT-PCAOBAI-2025 | — |
| CAQ-ACI-2026-03 | — | CAQ-ACINSIGHTS-2026 | CAQ-ACI-2026-03 |
| FIELDGUIDE-FIELDAGENTS-2025 (existing key; routed only) | FIELDGUIDE-AGENTS-2025 | — | — |

All other keys are unchanged from the inputs.

## 10. Suggested improvements to the briefs

1. **Publish an archetype-wide key registry and make deep dives read it.** Three Caseware pages shared one ref in
   the landscape and in two deep dives. Two DataSnipper pages shared one key. Five documents had two or three keys
   each. The existing assurance YAMLs already disagree with each other (for example CASEWARE-VERITY-2026 points to
   two different pages in two modules, and IFIAR-TTF-2026 has two URLs).
2. **Tell deep dives which steps already have entries in sibling modules.** PwC's tie-out pilot was re-proposed
   here although it is ST-13.
3. **State how to grade anonymised peer-reviewed field studies and named-firm experiments.** Neither fits the A-D
   definitions cleanly, and the three angles split on both (`#05`, `#10`). Suggested wording: "anonymised firm in a
   peer-reviewed study: B, flagged; experiment on historical cases with a named firm: B, never A."
4. **Let a module set its own A/B target when the landscape rates evidence "Medium".** The landscape had already
   said most completion steps lack public evidence. The 50% target cannot be met without inflation, and the brief
   should say an explicit shortfall is the expected result.
5. **Add an "Open questions" section to the module template.** This module needed one, and so will others. Make it
   a standard optional section with "what was searched / what was found / probe" columns.
6. **Ask governance angles for inspection-theme denominators.** The IFIAR survey gives "of N inspected for this
   theme", but the inputs reported it inconsistently. A fixed table format would help.
7. **Reserve search budget for gap-filling.** All three deep dives ran out before checking named customers for the
   vendor tools. A named customer is what would lift several C entries to B.
