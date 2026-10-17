# Synthesis report: assurance / specialists

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-assurance.md` (wave 1 rerun; module check, specialists research leads, ED-500 and REFGLOBAL
  leads), `assurance-specialists-combined.md` (one combined deep dive, 18 candidates)
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/specialists.md` (261 lines)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/specialists.yaml` (13 entries)
- **Validator:** `INFO .../use-cases/specialists.yaml: 13 use cases, 2 graded A/B (15%)`, plus the matching
  below-target WARN. No ERROR for either file. At the time of the final run the validator reported 0 errors overall
  (an earlier run showed one ERROR on `sustainability-assurance.md`, a sibling file being written by another session,
  not this one).
- **Why the below-target warning is accepted.** The caller set this module as low evidence and waived the 15-25 and
  50% A/B targets. The input itself found 0 A and 2 B, and both B entries are adjacent (advisory practices, not
  specialists on audits). Padding to 15 would have meant keeping entries the brief says to drop (duplicates of
  sibling modules, or a "being developed" claim with no use).
- **Not yet verified.** Needs the verification pass against the sources.

## 1. Counts in and out

| | Combined deep dive | Landscape |
|---|---|---|
| Candidates in | 18 (0 A, 2 B, 5 C, 11 D) | 0 YAML candidates (context only) |
| Kept as their own entry | 11 | |
| Merged with another candidate | 2 (02 + 04) | |
| Folded into another entry's notes | 1 (03 into `#01`) | |
| Not repeated: already in a sibling module | 3 (14, 15, 18) | |
| Routed elsewhere as well as kept | 1 (16 also to substantive-testing) | |

**Out: 13 use cases.** Mapping (combined id to output id): 01→01 (+03 in notes), 02+04→02, 05→03, 06→04, 07→05, 08→06,
09→07, 10→08, 11→09, 12→10, 13→11, 16→12, 17→13.

## 2. Duplicates merged and items not repeated

| Output | From | Choices made |
|---|---|---|
| `#01` valuation data gathering | combined-01, combined-03 | 03 (interactive deliverables, "being developed", same panel, weak audit relevance) kept as a note, not an entry. BVR-ASA2026-2026 added to sources (search-only, cited only for the conference date) |
| `#02` valuation providers add vendor AI analytics | combined-02 (CohnReznick), combined-04 (Valutico) | Same change to the work: a valuation provider adds third-party AI analytics inside its methodology. Pattern `other` (04 had `research-brief`); both grade C, announced. All five sources kept |
| not repeated | combined-14 forensic authentication | Same change as `assurance-substantive-testing-04` (ISACA zero-trust, authentication, a forensic practitioner). The module points there |
| not repeated | combined-15 Commerford | Same experiment already in `assurance-substantive-testing-19`. COMMERFORD-2022 is listed in the module's Sources for the objection that cites it |
| not repeated | combined-18 specialists review firm AI output | Input itself says this is quality-management; covered by `assurance-quality-management-18` (FRC p37 reviewer competence). FRC-GENAI-2026 kept in module Sources |

Light edits (no new facts): term explanations added for ASOP No. 56 and LIME/SHAP; `#10` problem reworded from
"faster than their governance matures" to "while their AI governance is immature" to avoid an implied rate claim; the
FRC p92 code-review precedent added to `#07` notes (from the input's baseline section).

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 06, 09, 10, 12, 13 | | 11 | 6 |
| augment | 01, 02, 03, 04, 07, 08 | | | 6 |
| automate | | | | 0 |
| delegate | 05 | | | 1 |
| **Total** | 12 | 0 | 1 | 13 |

- **No automate entry and no process-scope entry.** Nothing in the inputs shows specialist work running without a
  person on the normal path, or a redesigned specialist flow. Not filled.
- **Delegate:** one idea (`#05`, agent-built models, academic benchmark only).
- **Model scope:** one idea (`#11`, AI and data-science experts as a new kind of auditor's expert).
- **Maturity:** 3 in production (01, 03, 13; all advisory or valuer-side), 1 piloting (12, experiment), 1 announced
  (02), 8 emerging.
- **Ladder caveat:** `#07` is labelled `augment` (as in the input) though it is mainly an audit procedure over a client's
  AI rather than AI doing the auditor's work. A verifier may prefer `assist`.

## 4. Grade mix

| Grade | In (18) | Out (13) |
|---|---|---|
| A | 0 | 0 |
| B | 2 (01, 17) | 2 (`#01`, `#13`), both adjacent: valuation advisory and tax advisory |
| C | 5 (02, 03, 04, 05, 16) | 3 (`#02` merged, `#03`, `#12`) |
| D (idea) | 11 | 8 (`#04`-`#11`) |

The caller's brief summary said "0 A, 2 B, 11 D"; the input also has 5 C entries, all accounted for above. Every D
entry has a regulator, standard-setter, professional-body, practitioner or academic source discussing it, and is
labelled "idea". The only independent measurements (`#05` GAUGE, `#06` INS-ActBench, `#12` field experiment, `#10`
CAQ pulse) come from research or surveys, not deployments.

## 5. Gaps

- **No audit-side deployment evidence** for valuation, actuarial, tax, forensic or environmental specialists. No
  named firm, inspection finding or regulator statement on specialist AI use on audits.
- **No measured outcomes** (error, override, parallel-run, inspection) tied to specialist AI use.
- **Tax provision, environmental and forensic specialists** have no AI use case with a named organization.
- **ISA 500 / management's experts in the IAASB ED.** The combined input says the ED-500 text was behind a login;
  the landscape (and `assurance-planning-risk-assessment` YAML) read it from the IFAC PDF. The module cites the
  landscape's reading (para 68 of the EM: guidance over a technology requirement). What ED-500 proposes for
  management's experts specifically was not read by either input. Resolve in verification.
- **PCAOB primary pages** (AS 1210, AS 1105 App. A, 2018-2019 specialists release) blocked; read through the
  Spotlight only.
- **Abstract-only reads:** SSRN-LLMAQ-2026, ARXIV-GAUGE-2026, ARXIV-INSACTBENCH-2026, COMMERFORD-2022, HIRSCH-2019.
- **Undated or estimated dates:** FORVIS-RESERVING-2025 (year estimated), BVR-BIGFOUR-2025 (from a search
  extract), AAA-GENAI-2024 (month unknown), SSRN-LLMAQ-2026 (posting date unknown).
- **REFGLOBAL-DCF-2026** (LLM DCF valuation: look-ahead leakage) has no URL in the inputs; mentioned only in `#05`
  notes, not cited as a source.

## 6. Ref-key alignment with sibling modules

Same document, same key: the module and YAML use the sibling key where one exists.

| Input key | Key used | Why |
|---|---|---|
| IFIAR-TECH-2026 | IFIAR-TTF-2026 | Same IFIAR 2026 report (2026-04-20) held in substantive-testing; page p5 is from the specialists input's copy and may differ from the fsa.go.jp mirror |
| ISACA-DEEPFAKE-2026 | (not cited) ISACA-EVIDENCE-2026 in substantive-testing | Same URL; entry not repeated |
| WK-AIEVIDENCE-2026 | (not cited) WOLTERSKLUWER-EVIDENCE-2026 in substantive-testing | Same URL |
| COMMERFORD-2022 | COMMERFORD-2022 | Date conflict: input 2021-12 (Crossref first published); substantive-testing 2022-03 (issue). Module gives no date |
| PCAOB-PRIORITIES-2025 | (routed only) | Planning-risk-assessment holds a PCAOB-PRIORITIES-2024 key for a Dec 2024 spotlight; check whether it is the same document |
| AICPA-PA-2026 | AICPA-PA-2026 | Controls-testing and assurance-over-ai use `AICPA-PA` for the same release; the archive has both keys |

## 7. Routed to other modules (from the inputs)

- **controls-testing / assurance-over-ai:** IT-audit specialists and ITGCs over AI components; BDO-ITGC-2026,
  COSO-GENAI-2026 (landscape, not reopened); PCAOB-PRIORITIES-2025 pp6-7 (GenAI may amplify IT risks; ITGC
  procedures to be evaluated).
- **substantive-testing:** evidence authenticity and AI-fabricated third-party documents (AUASB-AI-2025;
  ISACA-DEEPFAKE-2026 = ISACA-EVIDENCE-2026); the LLM inventory-valuation experiment (SSRN-LLMAQ-2026, kept here as
  `#12` too); the FRC contract-review example (FRC-GENAI-2026 example 2), although ISA 620 lists contract
  interpretation as an expert field. Baseline: forensic specialists joined fraud risk assessment on one KPMG audit
  (FRC-ARAQ-2026 p82).
- **quality-management:** firm tool governance and certification (FRC-GENAI-2026; FRC-ARAQ-2026 p27 thematic;
  IFIAR-TTF-2026); specialists as reviewers of AI output (combined-18); PCAOB standard-setting comment letters
  (GOINGCONCERN-PCAOB-2026).
- **planning-risk-assessment:** client AI governance maturity and understanding the entity's AI use
  (BOARDMEMBER-CAQ-2026; AT-AICPAPA-2026).
- **acceptance-independence:** independence of audit-tool and AI vendors; this module covers only expert
  objectivity under ISA 620 para 9.
- **advisory, not audit:** KPMG-Anthropic global alliance (19 May 2026; search-only; KPMG-ANTHROPIC-2026).
- **other-assurance / sustainability / SOC:** IAASB narrow-scope amendments also cover ISAE 3000, ISRE 2400 and
  ISRS 4400 (IAASB-620NEWS-2026).

## 8. Suggested improvements to the briefs

- **Low-evidence variant of the synthesis brief.** State up front when the 15-25 / 50% A/B targets are waived, and
  what the module should optimise for instead (risk map, probes, standards implications). This module needed a
  "Read this first" box and a guardrails subsection on what the standards do *not* say.
- **Sibling-check step.** Ask the synthesiser to grep existing module YAMLs for the same URL before writing, and to
  reference rather than repeat. Three of 18 candidates here were already covered elsewhere.
- **Canonical ref registry.** Same documents carry different keys across modules (AICPA-PA vs AICPA-PA-2026,
  IFIAR-TECH vs IFIAR-TTF, ISACA-DEEPFAKE vs ISACA-EVIDENCE). A shared key list would stop drift.
- **Deep-dive brief: record exact URLs and dates for every lead** (REFGLOBAL-DCF-2026 had neither) and reconcile
  access claims with the landscape (ED-500 "behind a login" versus read in full).
- **Adjacency flag.** Add an optional field (or a fixed notes phrase) for "adjacent evidence: advisory, not audit",
  so grade B entries like `#01` and `#13` are not mistaken for audit-side deployments.
