# Synthesis report: assurance / soc-attestation

- **Prepared:** 2026-10-16
- **Inputs:** `landscape-assurance.md`, `assurance-soc-attestation-practice.md` (P, 22 candidates),
  `assurance-soc-attestation-discourse.md` (D, 13), `assurance-soc-attestation-governance.md` (G, 12)
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/soc-attestation.md` (299 lines)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/soc-attestation.yaml` (16 entries)
- **Validator:** `INFO .../use-cases/soc-attestation.yaml: 16 use cases, 9 graded A/B (56%)`. No ERROR lines for either
  file. The remaining warnings are the missing SKILL.md and two sibling modules below target.
- **Not yet verified.** Like the pilot, this output needs the verification pass against the sources themselves.

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 22 | 13 | 12 | 47 |
| Merged into this module's YAML | 12 | 8 | 9 | 29 |
| Placed in existing controls-testing pilot entries (referenced, not duplicated) | 9 | 5 | 3 | 17 |
| Routed to another module | 1 | 0 | 0 | 1 |

- **Out:** 16 use cases. 9 are merges of two to five candidates; 7 come from one candidate.
- **Landscape:** contributed no YAML entries of its own. Used for context (TQA 9561 date, EY poll, KPMG webcast,
  the module-split recommendation).
- **Partial carries:** practice-13 split between pilot CT-14 (auditor API) and `#13` (Vanta network figures, A-LIGN
  quote); discourse-09 split between pilot CT-13 (report review) and `#12` (uniform-language flags).

## 2. Placement decisions against the controls-testing pilot

The caller asked to reference pilot ids instead of duplicating. When a candidate described the same change to the work
as a pilot entry, it was placed there, and the module points to the pilot id (written `CT-nn`).

| Pilot id | Candidates placed there | Why it is the same change | New evidence the pilot could add at its next review |
|---|---|---|---|
| CT-11 SOC testing (KPMG UK) | P01, P02, P03, P04, D11 | KPMG UK's Clara agents, Copilot and DataSnipper in SOC/ISAE engagements: CT-11 already lists walkthrough prep, test plans, collating Description of Service comments and DataSnipper extraction, with the ~18% / ~15% figures. D11 is the generic "auditor uses AI in fieldwork" | PKF-AI-2025 (limits: scope, materiality, sufficiency stay human); SD-TQA "responsibility does not transfer"; CHIARO-WHO-2026 (confidentiality of evidence in AI tools) |
| CT-01 / CT-02 walkthroughs, control-wording scores | P01, P02 (also) | Same KPMG UK tools | none |
| CT-12 SOC-cycle drafting | P10, P11, D01, D05, D06, G11 | Section 3 drafting, management responses to deviations and project tracking, all on the EY poll | EY-SOC-2025 (logical access behind 52% of SOC 1 and 40% of SOC 2 deviations); CHIARO-AINATIVE-2026 ("submitted" versus "accepted" evidence); JOFA-SOCETH-2026 (an auditor or vendor writing management's responses raises objectivity questions) |
| CT-13 reading vendor SOC reports | P17, D09 (report-review part), G10 | User-entity review of received reports | Vanta vendor-risk feature (Duolingo quote, VANTA-AI-2026); Whistic bulk assessment (WHISTIC-DELVE-2026); PCAOB-DATA-2024 baseline (~17% of comment forms; CUECs not tested); KPMG-CHECKBOX-2026 "test of one" warning |
| CT-14 platforms feeding examiners | P13 (auditor-API part), D10, G02 | Examiner pulls evidence and status from the client's compliance platform | VANTA-AUDITORS-2026 (Auditor API; A-LIGN's 50% quote); XRB-3402-2026 para 25 (enquiry plus other procedures); LINFORD-FAQ-2022 (edited CSV exports, stale syncs). With named platforms and practitioner descriptions of normal use, CT-14 may merit grade B |
| CT-23 idea: evidence fabrication screening | P22 | Same idea in a SOC setting | ISACA-EVIDENCE-2026 (fabricated document with synthetic signatures and metadata); LINFORD-ASSURE-2026 ("too clean" evidence) |

Kept here despite partial overlap: `#06` A-LIGN (CT-03 covers pre-submission checks in SOX; this is a SOC specialist
firm's own platform), `#09` Linford report review (CT-10 covers workpaper secondary review, not report review), `#05`
service-organisation-side monitoring (CT-14 is the examiner side), `#12` templated-report detection (new to both).

## 3. Duplicates merged

| Output | Merged from | Choices made |
|---|---|---|
| 01 Acceptance, sampling, scheduling (Linford) | P09 | |
| 02 Platform-drafted readiness documents | P16, G03 | Generic Section 3 drafting left in CT-12 |
| 03 AI remediation with expert approval | P15 | |
| 04 Cross-framework mapping and evidence reuse | D02, G12, plus A-LIGN's 15 h figure from P05 | Scope: step (D) over process (G); maturity in-production (G) over announced (D) |
| 05 Continuous monitoring and agent-collected evidence | P12, D03, D04, G01 | Ladder automate (3 of 4); runtime background-agent (2–2 tie) |
| 06 A-LIGN pre-fieldwork evidence screening | P05 | |
| 07 Weaver engagement platform | P07 | |
| 08 Fieldguide agent-executed SOC engagement | P06 | |
| 09 AI review of draft SOC reports | P08 | |
| 10 Security questionnaire answers | P14, D07, G08 | Maturity in-production (2 of 3) |
| 11 Trust centre with AI chatbot | D08, G07 | Automate/step (G) over assist/process (D): the AI element is the chatbot |
| 12 Templated-report detection | G09 (idea, D), D09 (Whistic uniform-language part) | Graded C on the Whistic vendor claim; peer-review AI use stays an idea |
| 13 Platform-curated auditor networks | G06, plus P13 network figures | Change scope normalised step → model: the change is who routes buyers to auditors |
| 14 Bundled SOC-as-a-service (Delve allegations) | P19, D13, G04, G05 | Ladder automate (3 of 4); pattern end-to-end-case-agent (2 of 4); grade B on named vendors openly running the model, not on the allegations |
| 15 Platform plus licensed CPA firm | P20, plus A-LIGN from practice's service-model notes | |
| 16 Chiaro AI-native firm | P21, D12 | Grade B (D) over C (P); ladder delegate (D) over augment (P); maturity in-production (D) over piloting (P). Each choice is noted in the entry |

Every source from every merged candidate was kept unless the candidate went to a pilot entry or was routed out.
**Function rule applied:** entries on the service-organisation or report-user side use `risk-compliance-legal`
(practice's convention). Auditor-side and service-model entries use `service-delivery`. Governance had used
`service-delivery` throughout.

## 4. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 01, 12 | 07 | | 3 |
| augment | 02, 03, 04, 06, 09, 10 | | 15 | 7 |
| automate | 11 | 05 | 13, 14 | 4 |
| delegate | | 08 | 16 | 2 |
| **Total** | 9 | 3 | 4 | 16 |

- **Every ladder level and every scope has at least one entry.** Delegate is thin: `#08` is announced only (vendor
  figures with no named firm), and `#16` is one new firm's self-description. No measured delegate deployment exists.
- **Empty cells were not filled:** delegate/step, automate/process beyond monitoring, assist/model. No evidence.
- **Maturity:** 14 in production, 2 announced (`#08`, `#12`), 0 piloting, 0 emerging.
- **Functions:** 8 service-delivery, 8 risk-compliance-legal. The evidence is platform-heavy.

## 5. Grade mix

| Grade | In (47) | Out (16) |
|---|---|---|
| A | 1 (P04) | 0 |
| B | 20 | 9 (01, 05, 06, 07, 09, 13, 14, 15, 16) |
| C | 24 | 7 (02, 03, 04, 08, 10, 11, 12) |
| D (idea) | 2 (P22, G09) | 0 |

- **The only grade-A candidate (P04: KPMG UK ~18%)** is the same change as pilot CT-11, which already carries it at
  grade A. The module cites it through CT-11 and K-UKCA.
- **Both ideas were absorbed.** P22 went to pilot CT-23. G09 merged into `#12`, which a vendor claim lifts to C.
- **C entries kept:** they cover the readiness and post-issuance steps (policies, remediation, mapping,
  questionnaires, trust centres), the only delegate-rung SOC product (`#08`) and the buyer-side quality signal (`#12`).
- **Downgrade considered and kept:** P18 (Drata agent governance) was graded B by practice, but the input does not name
  the early-access customer. It was routed out (see §7), so no grade was assigned here.
- **Caveat:** grade B here usually means "named organisation says it does this". Several B entries (01, 09, 16) rest on
  the deploying firm's own blog or forum post.

## 6. Gaps

- **No independent quality evidence.** There is no error, override, rework, parallel-run, inspection or peer review
  figure for AI in SOC work. Peer review results for SOC practices are not published nationally, and two state reports
  show zero SOC engagements reviewed.
- **The only firm measurement is KPMG UK (~18%)**, and it comes from a tool bundle.
- **Thin segments:** ISAE 3402 / 3000 outside KPMG UK; bridge letters; SOC 3; SOC for Cybersecurity and Supply
  Chain; Deloitte, PwC and mid-tier SOC practices; SOC specialist firms' own AI use (Schellman and BARR publish none
  that was found).
- **No academic study.** The AAA (2023) says little is known.
- **No audit-firm job postings:** only vendor roles (Fieldguide, Drata).
- **Gated primary texts not read:** TQA 9561, the AICPA software-tools FAQ, Ethics Staff Insights, the Reviewer
  Alert and the TSC. All are known through landing pages and secondary summaries (Schneider Downs, Deloitte DART,
  JofA, Linford).
- **Delve:** the last development found is dated 23 Apr 2026 (customer moves). The AICPA inquiry, any state-board
  action and the federal suits (seen only in a comparison site) have no known outcome. Treat every allegation figure as
  unverified.
- **Pricing:** only a lead-generation directory's asking prices. There is no fee or realization data tied to AI from
  any audit firm, except Weaver's platform-driven realization figure.
- **Search budget:** web search ran out in all three deep dives, and several planned searches were not run.

## 7. Routed to other modules (collected from the inputs)

| Target module | Items |
|---|---|
| **assurance-over-ai** | Drata AI Agent Governance (P18; DRATA-AGENTGOV-2026; limited availability 2026-08-04; not a use case here). KPMG UK "SOC 2+" opinion over AI governance (K-UKCA pp.7-8; that module already holds it). TQA 9561 scoping of service organisations' AI (SD-TQA, AICPA-TQA9561-2026, DART-TQA-2026). CSA note on missing AI criteria and auditor overlays (CSA-SOC2). KPMG webcast on TSC restructuring (KPMG-SOC-2026). EY conference theme of AI assurance through SOC and ISO (EY-SOC pp.2-3). JOFA-EVAL (CPAs as AI system evaluators). CSA STAR for AI and CPA guidance (CSA-STAR-2025, CSA-CPAGUIDE-2026). Baker Tilly on AI controls in SOC 2 (BAKERTILLY-AISOC2-2025). ISO 42001 as a separate certification (SOC2AUD-AICOS-2026). Linford on AI/ML subservice organisations (LINFORD-AIML-2023). Fabasoft ISAE 3402 Type 2 covering an AI product (FABASOFT-ISAE-2026). Directory of ISO 42001 certification bodies (SOC2AUD-FIRMS-2026) |
| **acceptance-independence** | JOFA-SOCETH-2026 in full: cross-referrals, bundled fees, network or alternative-practice-structure tool providers, responsible-party test, possible transfer to firms licensing AI audit tools. AICPA-ESISOC-2026. AICPA notice on vendor allegations (AICPA-SOC-2026). Platform-plus-licensed-firm structures (`#15`, `#16`). Readiness-versus-examination independence under ET 1.295 (CHIARO-BUNDLE-2026, CHIARO-METHOD-2026). Linford's use of AI in client acceptance (`#01`) |
| **quality-management** | Peer Review alert and outreach (JOFA-PRB: a single file review is often insufficient; follow-up can mean revising the system of quality management or an outside review of completed engagements; enhanced oversight). Reviewer Alert status as staff communication (AICPA-REVALERT-2026). AICPA SOC Quality Center idea (JOFA-FAST). State peer review activity reports (OSCPA-PR-2026, LASCPA-PR-2026). Firm-level tool governance for SOC practices |
| **controls-testing** | See §2. Also: EY-SOC-2025 pp.4-5 (access-related deviations, manual user-access reviews, IAM automation); SCRUT-EVIDENCE-2026 six-step evidence chain; Fieldguide's evidence-request and testing agents (P06) |
| **substantive-testing** | Fieldguide Audit Testing Agent for financial audit, "up to 70% of testing" (FIELDGUIDE-FINAUDIT-2025, vendor claim; already in the pilot module as FG-FINAUDIT). Citrin Cooperman partner on agents filling workpapers from ledger data and handling cash confirmations (JOFA-TRANSFORM-2026) |
| **completion-reporting** | EY-SOC-2025 p.10: a cyber incident may lead an auditor to modify an opinion, restrict distribution or withdraw an issued report |
| **sustainability assurance** | ASB exposure drafts adding AT-C 325 and 330 for sustainability information (JOFA-ATTEST-2026, CPAPA-ASB-2026, BRIGHT-ATC-2026) |
| **vendor or third-party-risk (outside this archetype)** | Consumption of SOC reports by vendor-risk teams, questionnaire automation and trust centres (`#10`, `#11`, `#12` sit on that boundary) |

## 8. Conflicts resolved and items for the verifier

- **Delve wording.** Every mention says the claims are allegations, that Delve denies them, and that there is no
  regulator finding. No audit firm named in the allegations is named in the outputs. Allegation figures (493 of 494;
  259 of 259; 575 files) appear only in `#14` notes, labelled anonymous, unverified and disputed. A different count
  (533 reports, 455 companies) is noted. The 70% questionnaire figure (Delve's own defence) and the $6,000–$15,000
  price points (unopened secondary sources) are not used.
- **Trust Services Criteria changes.** KPMG's webcast page (2026-09-22) expects a restructuring with AI considerations.
  CSA (2026-08-30) says there are no AI criteria and no exposure draft. These are reconcilable if the changes are
  unpublished. The module states both, without an effective date.
- **TC-DELVE date:** 2026-03-21 (URL path and original post) over 2026-03-22 (update date, used by P and G).
- **IANS-DELVE URL:** two date-stamped variants exist (/2026/03/30/ and /2026/04/19/). Used the pilot's /03/30/ path
  with byline date 2026-03-24. Type `press` (pilot, P, D) over `vendor` (G).
- **AICPA-SOC-2026 URL:** used /resources/landing/system-and-organization-controls-soc-suite-of-services (D, G) over
  practice's /topic/... path. Type `standard-setter` (P, G) over `professional-body` (D). Date 2026-10 (access month).
- **JOFA-SOCETH-2026 type:** `professional-body` (D, G, and the acceptance-independence YAML) over `standard-setter` (P).
- **EY-SOC:** governance carried it as `search-only` with a local file path for a URL. The other angles opened the PDF,
  so the outputs use `full` and the EY URL. Type `conference` (pilot) differs from assurance-over-ai's `firm`; align
  these at verification.
- **SOC2Auditors.org pages:** typed `vendor` throughout (lead-generation site). Governance had typed two of them `press`.
  Three different pages had colliding input refs and now have distinct keys (see §9).
- **Schneider Downs (SD-TQA):** governance reported a 403 and relied on a comparison site; practice and discourse read
  it. Kept as opened.
- **JofA podcast URL:** the percent-encoded form (P, G) is used instead of the pilot's literal non-standard hyphen.
  It is the same document under the pilot key JOFA-PODSOC.
- **Search-only items not used as evidence:** Fieldguide's 36–50 hours per SOC engagement and 66% drafting cut; Vanta
  Agent for Risk and Agentic Trust Platform Business Wire releases; BARR Audit AI connectors; the PCI SSC AI guidance
  cited by Linford.
- **For the verifier to check first:**
  - `#16` (grade, ladder and maturity choices rest on the firm's own statements)
  - `#13` (scope changed to model)
  - `#05` (IDC figure quoted by Vanta)
  - the KPMG UK benchmark percentages in the module (p.10 of K-UKCA)
  - the EY-SOC-2025 deviation shares

## 9. Canonical source keys mapped to input refs

Documents already in the pilot keep the pilot key. New documents use `PUBLISHER-SHORT-YYYY`.

| Canonical key | Practice ref | Discourse ref | Governance ref |
|---|---|---|---|
| EY-SOC | EY-SOC-2026 | EY-SOC-2026 | EY-SOC-2026 (search-only) |
| JOFA-FAST | JOFA-FAST-2026 | JOFA-FAST-2026 | JOFA-FAST-2026 |
| JOFA-PRB | JOFA-PRB-2026 | JOFA-PEER-2026 | JOFA-PEER-2026 |
| JOFA-PODSOC | JOFA-PODSOC-2026 | JOFA-PODCAST-2026 | JOFA-POD-2026 |
| SD-TQA | SDOWNS-TQA9561-2026 | SCHNEIDER-TQA-2026 | (via SOC2AUDITORS-AI-2026) |
| CSA-SOC2 | CSA-SOC2-2026 | CSA-SOC2-2026 | CSA-SOC2-2026 |
| IANS-DELVE | IANS-DELVE-2026 | IANS-DELVE-2026 | IANS-DELVE-2026 |
| K-UKCA | KPMGUK-CONTROLS-2026 | — | — |
| KPMG-CHECKBOX-2026 | — | KPMG-BEYOND-2026 | KPMG-CHECKBOX-2026 |
| TC-DELVE-2026 | TECHCRUNCH-DELVE-2026 | TC-DELVE-2026 (Yahoo copy) | TC-DELVE-2026 |
| TC-CONTEXT-2026 | TECHCRUNCH-CONTEXT-2026 | TC-DELVE2-2026 | — |
| TC-WHISTLE2-2026 | TECHCRUNCH-DELVE2-2026 | — | — |
| TC-DELVEYC-2026 / TC-LITELLM-2026 / TC-COMPAI-2026 | TECHCRUNCH-DELVEYC-2026 / TECHCRUNCH-LITELLM-2026 / TECHCRUNCH-COMPAI-2026 | — | — |
| AICPA-SOC-2026 | AICPA-SOC-2026 | AICPA-SOC-LANDING-2026 | AICPA-SOC-2026 |
| AICPA-FAQ-2026 | AICPA-SOCFAQ-2026 | AICPA-FAQ-2026 | AICPA-FAQ-2026 |
| SOC2AUD-FIRMS-2026 (/soc-2-auditors-ai/) | SOC2AUDITORS-AI-2026 | SOC2AUD-AI-2026 | — |
| SOC2AUD-AICOS-2026 (/insights/soc-2-for-ai-companies/) | — | — | SOC2AUDITORS-AI-2026 |
| SOC2AUD-COST-2026 / SOC2AUD-DELVE-2026 | SOC2AUDITORS-COST-2026 / — | — | — / SOC2AUDITORS-DELVE-2026 |

All other keys are unchanged from the inputs. They include LINFORD-*, VANTA-*, DRATA-*, FIELDGUIDE-*, CHIARO-*,
DELVE-*, ALIGN-*, WISPR-2026, DEEPDELVER-2026, WHISTIC-DELVE-2026, SCRUT-EVIDENCE-2026, BAKERTILLY-TRUST-2026,
XRB-3402-2026, PCAOB-DATA-2024, OSCPA-PR-2026, LASCPA-PR-2026, AICPA-REVALERT-2026, CYBERSECIFY-2026 and
GT-SOC2-2023.

## 10. Suggested improvements to the briefs

1. **Give deep dives the overlapping pilot ids up front.** 17 of 47 candidates re-proposed changes the pilot already
   held (CT-11 to CT-14). A line in the deep-dive brief, such as "these SOC uses already exist as CT-11 to CT-14; add
   evidence to them rather than new entries", would save effort and produce upgrade notes instead of duplicates.
2. **Let synthesis propose edits to another module's entries.** The best new evidence for CT-13 and CT-14 now sits in
   this report (§2). Either a `related_ids` field in the YAML or a standing "pilot upgrade" section would keep the
   evidence from being lost.
3. **Settle the key scheme across waves.** Pilot keys (EY-SOC, JOFA-PRB) lack the year that the wave 1 format requires.
   Inputs used three to four refs for the same document, and SOC2AUDITORS-AI-2026 named two different pages. Publish
   an archetype-wide key registry that every brief reads and appends to.
4. **A function rule for client-side work in professional-services archetypes.** Practice and governance disagreed on
   `function` for service-organisation-side entries. State: "the client's own team doing the work →
   risk-compliance-legal (or the relevant function); the firm's delivery → service-delivery."
5. **A standard rule for contested cases.** Give a fixed wording ("allegation; the company denies it; no regulator
   finding") and grading guidance: grade the openly operated model, never the allegation. Ask deep dives not to name
   third parties who appear only in allegations.
6. **Forbid local paths as URLs.** Governance cited the landscape file as the URL for EY-SOC. The brief should require
   the original document URL taken from the landscape row.
7. **Keep asking for quality evidence, and name where to look.** Governance found state peer review activity reports
   (a new, independent source type). Add "administering-entity peer review reports" and "inspection spotlights" to
   the governance brief's checklist.
8. **Budget searches per angle.** All three deep dives ran out of web search. Reserve part of the budget for
   gap-filling after the first pass.
