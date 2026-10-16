# Synthesis report: assurance / controls-testing

- **Prepared:** 2026-10-16
- **Inputs:** `landscape-assurance.md` (search snippets only; used as leads, overridden by the deep dives where they
  conflict), `controls-testing-practice.md`, `controls-testing-discourse.md`, `controls-testing-governance.md`
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/controls-testing.md` (281 lines)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/controls-testing.yaml` (25 entries)
- **Validator:** `INFO  .../assurance/use-cases/controls-testing.yaml: 25 use cases, 16 graded A/B (64%)`;
  0 errors (one expected warning: SKILL.md missing).

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidate use cases in | 20 | 20 | 20 | 60 |
| Carried into output | 20 | 20 | 18 | 58 |
| Not carried | 0 | 0 | 2 | 2 |

- **Out:** 25 use cases. 18 are merges of two to five candidates; 7 come from a single candidate.
- **Not carried:** governance-18 (firm-level monitoring of AI tools' quality impact) belongs in the quality-management
  module, and its function value `quality-management` is not in the vocabulary. Governance-20 (SOC-style attestation
  over AI systems) belongs in other assurance; its KPMG UK "SOC 2+" signal is kept in the frontier and in `#15`.
- **Landscape:** contributed no YAML entries of its own. Used for leads only (Workiva testing agents, firm platform
  scale). Where it conflicted with a deep dive, the deep dive won (see §6).

## 2. Duplicates merged

| Output id | Merged from | Notes |
|---|---|---|
| 01 Walkthrough assistants | practice-05, discourse-04, governance-01 | |
| 02 Test-of-design and test plans | practice-06, governance-13 (idea) | FRC aggregation risk kept as a guardrail |
| 03 PBC evidence requests | practice-17, discourse-03, governance-08 | discourse had automate/announced/`other` |
| 04 Risk-scored selection and targeting | practice-18, discourse-08, governance-07, discourse-20 | predictive targeting folded in |
| 05 Agentic attribute testing | practice-01, discourse-01, governance-03, discourse-09 | workpaper-drafting entry folded in |
| 06 Microsoft ITGC change-management agents | practice-02, discourse-02, governance-02 | 850 h/yr confirmed |
| 07 Sample-to-evidence matching | practice-12, discourse-05 | overlaps substantive testing |
| 08 Full-population testing | practice-09, discourse-06, governance-06 | |
| 09 Continuous testing | practice-10, discourse-07, governance-05 | |
| 10 AI secondary review / multi-agent challenge | practice-11, governance-14 (IntelliAudit idea), governance-19 (skepticism idea) | governance-19 kept as a guardrail |
| 12 SOC drafting | practice-08, discourse-11, governance-11 | |
| 13 Third-party SOC report review | practice-16, governance-12 | |
| 15 Testing AI-performed controls | practice-15, discourse-13, governance-09, governance-10, discourse-15 (idea) | ICFR and SOC variants combined |
| 16 Big Four platform agents | practice-13, discourse-19 | |
| 18 Swarm auditing | practice-19, discourse-17 | |
| 20 Agent-delivered co-sourced testing | practice-04, discourse-10, governance-04 | |
| 24 Idea: reliance on AI-enabled management testing | discourse-18, governance-16 | |
| 25 Idea: synthetic stress-testing | discourse-14, governance-17 | |

Single-source entries: 11 (practice-07), 14 (discourse-12), 17 (practice-14), 19 (practice-03), 21 (practice-20),
22 (discourse-16), 23 (governance-15). Every source from every merged candidate was kept. Where the same document
appeared under different refs in different files, it now has one canonical key (§7).

The angles disagreed on lens in 8 of the 18 merged clusters (03, 04, 07, 08, 09, 15, 18, 20) and on ladder in more.
I chose the majority value. On a tie I chose the value the strongest-evidence entry supports. Each choice is noted
in the entry's `notes`.

## 3. Coverage by lens and ladder

| Lens | Count | Ids |
|---|---|---|
| improve | 11 | 01, 02, 03, 04, 10, 11, 12, 13, 21, 22, 23 |
| automate | 3 | 06, 07, 14 |
| delegate | 3 | 05, 16, 18 |
| reinvent | 8 | 08, 09, 15, 17, 19, 20, 24, 25 |

| Ladder | Count | Ids |
|---|---|---|
| assist | 5 | 15, 21, 22, 23, 24 |
| augment | 9 | 01, 02, 03, 04, 10, 11, 12, 13, 25 |
| automate | 5 | 06, 07, 08, 09, 14 |
| delegate | 6 | 05, 16, 17, 18, 19, 20 |
| reinvent | 0 | none |

- **All four lenses have evidence.** Automate and delegate are thin but real: Microsoft, Reddit and Sanville/Oberlander
  are named deployments.
- **No entry sits on the ladder's top "reinvent" rung.** The reinvent-lens entries (service-model or methodology
  change) use agents at automate or delegate level. That follows the deep dives. Nothing was invented to fill the rung.
- **Maturity:** 15 in production, 5 piloting, 5 emerging, 0 announced.

## 4. Grade mix

| Grade | In (60) | Out (25) |
|---|---|---|
| A | 12 | 6 (04, 05, 06, 07, 08, 11) |
| B | 19 | 10 (01, 02, 09, 10, 16, 17, 18, 19, 20, 21) |
| C | 18 | 5 (03, 12, 13, 14, 15) |
| D (idea) | 11 | 4 (22, 23, 24, 25) |

A/B share is 64%. C and D entries were kept only where they add something the others do not:
- the evidence-request and SOC steps
- the contested SOC-platform practice
- AI-performed controls as a new test object
- frontier ideas on deficiency evaluation, adversarial evidence, cross-party reliance and pre-go-live testing

**Caveat:** every grade-A figure is self-reported by the deploying organisation or published by its vendor. Graded A
means "named organisation, measured figure", not "independently verified".

## 5. Gaps

- **No independent quality evidence.** No error rates, false-pass rates, reviewer override rates or parallel-run
  comparisons were found. The only quality-type figures come from a non-peer-reviewed prototype (IntelliAudit) and an
  inspection metric (Sanville) that cannot be attributed to AI.
- **No external-auditor reliance case.** No public case was found of an external auditor relying on management's or
  internal audit's agent-produced workpapers. This is the main open question for CAEs.
- **Big Four controls-testing launches are unconfirmed.** KPMG's promised Clara controls-testing agents and PwC's
  controls-testing automation were both still unconfirmed in October 2026.
- **No named failures.** Failure evidence is survey data (Optro), general automated-tool findings (IFIAR) and warnings.
- **Thin segments:** SOC specialist firms (Schellman, A-LIGN, BARR), small practices, Workiva customer outcomes.
- **Primary texts not read:**
  - PCAOB Release 2026-005
  - the IAASB exposure-draft text
  - AICPA TQA 9561
  - the AICPA practice aid
  - the Gartner *AI Implementation Guide: SOX Testing*
  - the NFRA paper itself

  QC 1000's 15 Dec 2026 date was not re-verified on the primary source.
- **Not searched:** 10-K disclosures of AI-related material weaknesses. An EDGAR hit list of about 1,000 filings is
  unreviewed.
- **Leads not used** (single search-only sightings):
  - Gartner/Xerox SOX case
  - ACRA Audit Practice Guidance No. 1 of 2025
  - Protiviti SOX poll percentages
  - Podcast Addict's "70% of recurring SOX testing" for Reddit
  - WSCPA webcast on supervised AI agents (scheduled 2026-11-07)

## 6. Conflicts resolved and items for the verifier

- **Microsoft change-management agent: 850 hours/year.** The landscape's "50 hours" was a dropped glyph in the PDF
  text layer; all three deep dives read 850 (`#06`).
- **Microsoft Sample Selection Agent "~2K hours/year".** Reported by practice and governance. Discourse found a missing
  digit in the text layer and omitted the figure. Kept with a "verify on rendered page" note (`#04`).
- **PwC Australia "lower-risk" pilot clients.** In the landscape only; the article itself does not say so. Dropped (`#17`).
- **EY "now vs 2028".** Agents are in all phases from April 2026; end-to-end support is targeted for 2028 (`#16`).
- **Date and URL conflicts:**
  - KPMG *Seize the future*: 2025-07-31, 2025-08-06 or 2025-08; recorded as 2025-08.
  - Grant Thornton SOX article: two URL paths (/2025/ and /2026/); used the /2025/ path with date 2026-07-21 (two of
    three inputs).
  - EY SOC highlights: typed `conference` by two inputs and `firm` by one; recorded as `conference`.
  - Microsoft PDFs dated "FY26": recorded as `2026`, because the validator needs ISO dates.
- **"Search only" sources carry the marker in `notes`:**
  - PWC-DCT (`#02`)
  - FG-FRAZIER (`#03`, `#11`)

  Their titles also say "search extract only".

## 7. Canonical source keys mapped to input refs

P = practice, D = discourse, G = governance, L = landscape.

| Key | Input refs | Key | Input refs |
|---|---|---|---|
| OPTRO-LAUNCH | P S03, D S04, G S55, L C15/F18 | K-SOX30 | P S11, D S01, G S49, L F3 |
| REDDIT-POST | P S04 | K-AGENTIC | P S12, D S02, G S50 |
| OPTRO-ACT | P S07, D S06 | K-404A | D S03 |
| OPTRO-FIRST | D S07 | K-UKCA | P S13 |
| OPTRO-MIDSHIP | P S06, D S08 | K-CLARA | P S14, L F2 |
| OPTRO-SURVEY | P S40, D S05 | MSFT-CM | P S09, D S14, G S53, L F17 |
| OPTRO-HAVERTYS | P S05 | MSFT-IA | P S10, D S15, G S54, L F17 |
| OPTRO-FJM | P S38 | CPAPA-RSM | P S01, D S16, G S56, L F11 |
| OPTRO-SNOW | P S39 | RSM-BEACON | P S02 |
| AUDITBOARD-ACC | P S37, L C14 | RIVERON | P S24, D S18, L F13 |
| SRA-16H | D S09 | GT-SOX | P S23, D S19, G S52, L F9 |
| SRA-SWARM | D S10, L D2 | CPAPA-ZANIN | P S47, G S59 |
| IIA-SWARM | P S49 | CPAPA-ADEWOLE | P S46, D S33 |
| AUDITPOD-296 | D S12 | CPAPA-WORKIVA | P S36, D S17, L C16 |
| CPAPA-EY | P S20, D S22, L F1 | DELOITTE-OMNIA | P S21, D S23, L F4 |
| AT-PWC | P S16, D S20, G S57, L F5 | CFODIVE-PWC | P S17, D S21, G S58 |
| CFOBREW-PWC | P S18 | AT-PWCAU | P S19 |
| CONS-GT | P S22, L F8 | PWC-DCT | P S60 (search only) |
| FG-AGENTS | P S32 | FG-SANVILLE | P S34 |
| FG-FRAZIER | P S61 (search only) | FG-PCAOB | D S36 |
| FG-FINAUDIT | P S33 | ANDERA-HOME | P S26 |
| PETUAL-HOME | P S29 | A16Z-PETUAL | P S27, D S56 |
| FTG-PETUAL | P S28, D S57 | TR-AGENTIC | P S45, D S62 |
| DS-ARMANINO | P S42 | DS-RMF | P S44 |
| EY-SOC | P S41, D S24, G S46, L C18 | SD-TQA | D S29, G S48 |
| CSA-SOC2 | D S28, G S47 | JOFA-FAST | D S25 |
| JOFA-PRB | D S26, G S30 | JOFA-PODSOC | D S27 |
| IANS-DELVE | D S30 | CCI-DELVE | D S31 |
| BDO-ITGC | P S48 | COSO-GENAI | G S25, L R26 |
| JOFA-COSO | D S55, G S29 | AICPA-PA | G S27, L R22 |
| JOFA-EVAL | G S31 | FRC-GENAI | G S01 (D S40 is its news release), L R9 |
| FRC-THEMATIC | P S55, G S03, L R8 | IFIAR-2025F | G S09 |
| IFIAR-TTF25 | P S56, G S10, L R16 | IFIAR-TTF26 | G S11 |
| NFRA-CAALLEY | G S17, L R19 | PCAOB-2024-007 | G S06, L R2 |
| IIA-PCAOB | G S32 | MINDBRIDGE-PCAOB | D S34 |
| CALCPA | D S35 | IRBA | G S15, L R21 |
| IIAF-FRAUD | G S36 | AFM-12 | G S14 |
| PETERS | G S63, L A3 | INTELLIAUDIT | G S66 |
| KOKINA | G S65 | UNIQUS | D S51 |
| AT-GARTNER | G S45 (also D S49, P S62) | YC-ARDEN | P S54, D S60 |
| YC-MIDSHIP | D S61 | VERDANTIX | D S63, L F21 |
| FOLEY-BOTIC | D S37 | ICAEW-FRC | D S41, G S38 |
| IAASB-ED | G S21 (with S22, S23), D S53, L R12 | CPACOM-ATR | P S57, G S43, L P6 |
| JOB-FG-SOX / JOB-FG-SWE / JOB-NACE | P S50 / S51 / S52 | JOB-REDDIT | D S64 |

## 8. Suggested improvements to the briefs

1. **One source-key scheme across angles.** Each deep dive restarts at S01, so the same document has up to four refs.
   Have deep dives reuse landscape ids or a shared key list. Merging would then not need a remapping table.
2. **Make the YAML format match the validator.** Inputs used `FY2026`, `undated`, `2026 (FY26)` and empty `outcomes: []`,
   all of which the validator rejects. They also used a function (`quality-management`) that is not in the vocabulary.
   State these rules in `vocabulary.md`: ISO dates only (YYYY allowed), at least one outcome (use "none" for ideas),
   and function ids from the list.
3. **Decision rules for lens versus ladder.** The angles disagreed on lens in 8 of 18 clusters. Give worked examples,
   for example: "full-population testing is reinvent/automate" and "evidence matching with exception review is
   automate". Also say whether the ladder's "reinvent" rung should be used for service-model changes.
4. **A structured access field.** Use something like `access: full | search-only` per source instead of free text in
   titles and notes, so the verifier can filter mechanically.
5. **Ask for quality evidence explicitly.** Add to the practice and governance briefs: "look for error rates,
   override rates, parallel-run results, inspection outcomes". All three dives reported the absence only at the end.
6. **Proposed new patterns.** Four recurring `other` patterns could become patterns: assurance over AI-performed
   controls (`#15`), multi-agent orchestration (`#18`), evaluation harness for agents (`#21`), and cross-party
   reliance on AI-generated evidence (`#24`).
7. **Cross-module routing.** Tell deep dives where to send overlapping items: substantive testing (`#07`), quality
   management (governance-18) and other assurance (governance-20). Then synthesis does not have to drop them silently.
8. **Module sources.** Say whether the module may cite sources that are not in the YAML. Two vendor-claim sources
   (ANDERA-HOME, FG-FINAUDIT) are cited only in the module and are listed there with URLs. With 80+ sources, the
   300-line limit leaves room only for keys.
