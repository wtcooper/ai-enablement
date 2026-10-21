# Synthesis report: advisory / valuation

Run date 2026-10-21 (wave 5; sources checked 2026-10-20). Outputs:
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/valuation.md` (300 lines, table of contents, 10 sections)
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/valuation.yaml` (14 entries, valid YAML)

`scripts/validate.py` reports 0 errors. It warns that the file is below the validator's targets: 14 entries (target 15-25) and 29% A/B (target 50%). The brief's target of 12-20 is met. A script check confirmed that every source key cited in the module is in the YAML or in the module's §10, and that every key named in a YAML entry is in that entry's sources.

## Counts in and out

| Input | Candidates | Kept as entries |
|---|---|---|
| adv-valuation-combined.md (deep dive) | 16 use cases | 14 after two merges (see below) |
| adv-x-independence-pricing.md | 0 (its table says valuation has no pricing or data-handling entry; only the SEC restriction) | Used in guardrails, probes and YAML risks (SEC-RULE2-01-2026, PWC-SECFAQ-2019, JOFA-ETHICSAI-2026) |
| adv-x-state-of-ai-disruption.md | 0 (tracker narrative: PE platforms buying valuation and forensic niches) | Used in frontier and probes (CPATRENDLINES-TRACKER-2026) |
| landscape-advisory.md | 0 new candidates; leads already covered by the deep dive (IVSC-IVSED-2026, BVR-AICPAAIGUIDE-2025, ACCTODAY-VPF-2026, AICPA-FVS-2026, BVR-NACVA-2026) | Used in guardrails and frontier |
| Routed items from other adv-*.md files | 5 items (below) | 0 new entries; folded into notes, guardrails and frontier |

Total in: 16 candidates plus 5 routed items. Total out: 14 entries.

**Id mapping (old deep-dive id to new id):** 02→01, 01→02, 09→03, 15→04, 16→05, 12→06, 13→07, 08→08, 10→09, 03+04→10, 14→11, 11→12, 05→13, 06+07→14.

## Duplicates merged

- **Old 03 + old 04 → new 10** (AI reviewer agents). Both describe the same change: an agent checks a valuation or report against standards, methodology and review policy before sign-off. One is a practitioner idea from an AICPA FVS podcast (D) and the other is Anthropic's 'Valuation reviewer' template (C). The merged entry is graded C and keeps all six sources.
- **Old 06 + old 07 → new 14** (valuation firms sell recurring valuation as an AI-enabled platform with their own opinions). Stout Drivr covers portfolio companies and Kroll REVS covers real estate. Both are firm announcements making the same model change. Graded C, with all sources kept.
- **Kept apart on purpose:**
  - Old 01 (BVR RADA agent, C) and old 09 (Valutico comparables at Kreston Reeves and Rouse, B). They work differently: one is a generative query agent, the other a data platform whose case studies do not claim generative AI. Merging them would put an "AI" label on case studies that do not make that claim.
  - Old 08 (template report generation) and old 10 (generative drafting). Their risks differ: generative drafting can hallucinate and raises confidentiality questions.
- **Overlaps with other finished modules, cross-referenced by id instead of duplicated:**
  - `assurance-specialists-01`, -02, -04 and -05 overlap new 01, 03, 10 and 12. These cover valuation specialists from the audit side.
  - `advisory-forensic-disputes-06`, -07, -09 and -14 cover disputes, verification, drafting and opposing-report critique.
  - `advisory-transactions-07` covers the SBA lender QoE.
  - Further cross-references: `professional-services-talent-learning-06` and -07, `professional-services-quality-review-02`, `professional-services-client-development-16`, `tax-research-advisory-08`, `assurance-substantive-testing-19` and `assurance-acceptance-independence-15`.

## Normalization and drift fixes

- **Unsourced inferences removed:**
  - Old 03's "Review shifts partly to challenging the agent's findings" is now "No role change is documented".
  - Old 05's "valuation committee review marks (implied...)" is now a statement attributed to 73 Strings, plus a note that Hamilton Lane's reviewers are not described.
  - Old 05's "the vendor says AI is only as good as the data under it" has been dropped. The 73 Strings page it came from could not be identified.
  - Old 15's role line is reattributed to BVR's tip and to the NACVA and ASA sources.
- **Sources added:** refs were added to attributed sentences in role_evolution, risks and human checkpoints where the inputs left them unsourced. The source records came from the same inputs: BVR-IVSPODCAST-2026 for new 10, and ARXIV-KIM-2024, taken from the transactions research, for new 06.
- **SEC restriction lines:** dropped from the UK-only entry (new 03), where the SEC rule is not relevant. In new 12 and new 14 the line was rewritten so that it does not imply Stout, Kroll or the vendors are audit firms.
- **Plain-language glosses added:** DLOM, DCF, PPA, Level 3, NAV, volatility and attrition analysis, zero-shot and few-shot prompting, hallucination, Model Context Protocol and Rule 707.
- **Formatting:**
  - All dates are quoted ISO strings.
  - Grade D titles start with "Idea:".
  - Each entry's notes say what kind of organization the example is (Big Four, UK or non-US accounting firm, independent valuation firm, in-house investment manager, vendor or AI-native provider).

## Coverage by ladder and change scope

| | step | process | model | total |
|---|---|---|---|---|
| assist | 04, 07, 11 | | | 3 |
| augment | 01, 02, 03, 05, 06, 08, 09, 10 | 13 | 14 | 10 |
| automate | | | | 0 |
| delegate | | 12 | | 1 |

Gaps:
- **Automate:** no evidence. No valuation step runs with no person on the normal path.
- **Delegate:** one entry (12), resting on vendor marketing claims, one of them from a startup-directory profile.
- **Process:** one in-house deployment (13) and the delegate claim.
- **Model:** one merged entry built on two announcements (14).
- **PPA, impairment and fairness opinions:** no deployment evidence.

None of these gaps was filled with an invented entry.

## Grade mix

A 0, B 4 (01, 03, 08, 13), C 7 (02, 04, 05, 09, 10, 12, 14), D 3 (06, 07, 11). That is 29% A/B.
- None qualifies for A under the 2026-10-17 rule. The firm figures (Rouse's "a third", RXM's "months to days") are recollections in vendor case studies. The 3-5x and 90% figures are vendor boilerplate.
- The B grades rest on named organizations with no measurement:
  - 01: KPMG, reported second-hand from a conference panel.
  - 03 and 08: four non-US accounting firms in vendor case studies.
  - 13: Hamilton Lane, in-house, in a Q&A the vendor hosted.
- The C entries are vendor or firm announcements and one standard-setter observation (09). The D entries are two preprints and one piece of conference advice.
- Sessions that are scheduled or exist only as abstracts (AICPA FVS November 2026, ASAIC26) support no grade.

## Gaps

- **Quality evidence.**
  - No error, override or parallel-run rates, no inspection findings about AI use and no independent tests of AI-assisted valuation were found.
  - The only independent items are indirect: Weber, two preprints (abstracts only) and PCAOB findings that predate AI.
- **Firms.** No US top-100 or mid-market accounting firm, and no Big Four firm other than KPMG (second-hand), described valuation AI use in the inputs. A conflict to resolve: the finished `assurance-specialists-02` entry records a CohnReznick valuation-advisory announcement (COHNREZNICK-VALUATION-2026, 2026-03-26) that this module's research did not find. The module flags this in its opening paragraph. Suggest re-reading that source and adding a valuation entry in the next pass.
- **Independence for private-company attest clients.** The AICPA Code text on valuation services (ET 1.295) was not opened. Only the SEC rule and staff FAQ were confirmed.
- **Paywalled or members-only material.** Paywalled BVR material (polls, Big Four panels, monoculture, training transcripts), the AICPA FVS guidelines, the AO-41 full text, IVSC consultation responses and IVSC Pulse results were not read.
- **Practitioner voices.** No community discussions or job postings were found.
- **Source key conflict.** The same IVSC perspectives paper is IVSC-PERSPECTIVES-2025 in the valuation inputs and IVSC-AI-2025 in `assurance-specialists-*`. This file keeps the input key and notes the alias in the module's §10. AICPA-FVS-2026 and SEC-RULE2-01-2026 carry different URLs in different wave 5 files: the events home page vs the agenda feed, and Cornell LII vs eCFR.

## Routed items picked up (from other modules' research)

| From | Item | Where it went |
|---|---|---|
| forensic-disputes | AICPA FVS 2026 sessions FVC2640 "Valuation in an AI World" and FVC2631 "MythBusters" (items on AI disclosure language in BV reports and on public-company AI disclosure suits); scheduled | Module §8, cited as AICPA-FVS-2026 with the agenda-feed URL in §10 |
| forensic-disputes | IVSC exposure draft, Valuation Performance Framework, BVR report quality-control agents | Already in the deep dive: §6 and entry 10 |
| transactions | SBA valuation independence clause (no valuation prepared for the applicant or seller; no dollar threshold), a vendor reading (QOEAGENT-WHO-2026) | Module §6, cross-reference to advisory-transactions-07 |
| transactions | Withdrawn Kim, Muhn and Nikolaev paper (ARXIV-KIM-2024) | Entry 06 notes, as "do not cite" |
| fpa-performance | The same Kim, Muhn and Nikolaev work (SSRN-KMN-2024, search-only) | Not used. The arXiv version is withdrawn (see above) |
| private-client | Masttro's claimed AI valuation of PE and VC holdings (MASTTRO-JEFFERSON-2026 platform pages, not read in detail) | Entry 13 notes, as a lead only |
| risk-controls | IVSC AI disclosure in valuation reports | Already covered in §6 |

Routed out of valuation by the deep dive, for other modules' synthesis:
- **forensic-disputes:** USCOURTS-EVID-2026 (Rule 707 withdrawn as published, with a modified proposal sent for study), GOLDMAN-WEBER-2024, BVR-DISCOVERY-2026, BVR-HEPPNERCOURT-2026 and BVR-LEDOUX-2026.
- **transactions:** FORVIS-QOE-2026, S73-CALLISTO-2026 (data-room automation) and ANTHROPIC-KPMG-2026 (PE portfolio offerings).
- **professional-services:** BVR-KPMGTREND-2026, BVR-TRAINSTAFF-2025 and BVR-MOVERS-2026 (PE ownership of valuation firms).
- **assurance:** PCAOB-SPECIALIST-2025, BVR-PCAOBINSP-2026 and the AICPA audit practice aid.
- **tax:** estate, gift and 409A valuations, and the IRS responsible-AI guidance.
- **risk-controls:** model-risk governance for valuation models (BVR-IVSCDIALOGUE-2026).
- **Service-demand signal:** valuing generative-AI businesses (BRATTLE-INSOL-2025). This is demand for valuation work, not AI used in it, so it has no entry.

## Suggested improvements to the briefs

1. **Give a shared key list for the wave.** Each module's brief should list the source keys already used in finished files across all archetypes, with their URLs. The IVSC-PERSPECTIVES-2025 / IVSC-AI-2025 split and the URL differences for AICPA-FVS-2026 and SEC-RULE2-01-2026 would then not happen.
2. **Tell module research to read the overlapping finished files in other archetypes first.** Here that is `assurance/specialists`. Its CohnReznick source never reached the valuation deep dive.
3. **Ask the deep dive to grade each entry's AI claim separately from its deployment claim.** Vendor case studies (Valutico) often describe automation under an AI brand. A field such as "AI type stated by the source: generative / ML / rules / not stated" would make this visible without notes.
4. **Bring the validator into line with the brief.** For low-evidence modules, either relax the validator's 15-entry floor (the brief allowed 12-20) or state in the brief that a warning is expected.
5. **Ask the deep dive for primary text of the AICPA Code** on valuation for attest clients (ET 1.295), or a note that it is members-only. The independence-pricing file and this module both stop at the SEC rule.
6. **Have routed items carry exact wording and source records** (title, URL, date, locator). The "MythBusters" item was ambiguous about whether the stated point was the myth or the rebuttal, so the module describes it neutrally.
