# Verification report: assurance / quality-management

- **Verified:** 2026-10-17
- **Files:** `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/quality-management.yaml`
  (25 entries) and `.../assurance/modules/quality-management.md` (299 lines)
- **Method:** every cited URL was fetched with curl (PDFs through pdftotext). The five blocked pages (three PCAOB speeches,
  the preprints.org paper and the Foley & Lardner article, all 403) were read through the r.jina.ai text mirror. Each figure, date, attribution and locator was checked against the text. Grades were re-derived from what
  the source shows, and no grade was raised.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. The one expected warning on this file is
  `25 use cases, 10 graded A/B (40%) — below targets`.

## 1. Counts

| Action | Entries | Ids |
|---|---|---|
| Kept | 8 | 09, 15, 16, 17, 18, 19, 20, 24 (notes cleaned of build references only) |
| Fixed | 17 | 01, 02, 03, 04, 05, 06, 07, 08, 10, 11, 12, 13, 14, 21, 22, 23, 25 |
| Rejected | 0 | none (every entry's core claim is supported by an opened source) |

All 25 entries also received these changes:
- `last_reviewed` was set to 2026-10-17.
- Notes were rewritten without build-only references (merged-from candidate ids, "landscape", "pilot", "R1", "inputs").
- The unverifiable "recorded 7 Nov 2025" was removed from the ICAEW podcast title in 6 entries.
- In 9 entries the NFRA press reports were replaced by the NFRA staff paper itself, which was opened (see §3).

## 2. Final grade mix

| Grade | Before | After | Ids after |
|---|---|---|---|
| A | 0 | 0 | none |
| B | 11 | 10 | 01, 02, 08, 09, 10, 12, 16, 18, 21, 24 |
| C | 9 | 10 | 03, 04, 05, 06, 07, 11, 13, 19, 23, 25 |
| D (idea) | 5 | 5 | 14, 15, 17, 20, 22 |

The A/B share is 40%, below the 50% target. One entry was downgraded (23) and none was raised. The reasons are
unchanged from synthesis: no firm or regulator publishes a measured outcome of AI tool governance or review, and most
evidence is regulator guidance or collective regulator observation.

## 3. Fixes and rejections

### Use cases

| Id | Field | Problem found | Fix |
|---|---|---|---|
| 01 | risks | "AI-specific certification was not observed" is not what the FRC says | Changed to "firms were still planning AI-specific changes to certification" (FRC thematic review, AI section) |
| 02 | problem | Unsourced connective: "so a translation aid and a tool that selects samples would get the same scrutiny" (translation aids are outside the FRC's tool scope; the example is NFRA's) | Removed. Wording now matches the FRC: "same process for every tool in scope for central certification, regardless of assessed risk or impact" |
| 02 | prerequisites | "(FRC-GENAI-2026, p. 36)" was attached to "central owner of a prompt library", which p. 36 does not say | Ref removed |
| 03 | role_evolution | "IT and quality teams jointly enforce tool policy" was attributed to IFIAR p. 6, which does not say it | Replaced with what p. 6 says (deploy only on approved engagements; oversight programmes for non-approved or decommissioned tools) |
| 03, 25 | sources | TRI page marked "undated, 2026-07 per the landscape" | The page's datePublished is 2026-07-21; date and title corrected |
| 04 | solution | The FRC's "often" applies to pilots, but the entry moved it to "lower-risk non-PIE audits" (FRC: "some firms") | Corrected. Also separated IFIAR's benchmarking practice from its thematic-review metrics, which IFIAR lists separately |
| 05 | risks | The persuasiveness claim had no page and was overstated ("need not be as persuasive") | FRC p. 19: outputs "need not exactly match" the persuasiveness of the procedure they replace, provided the methodology does not overstate it. Page added |
| 06 | prerequisites | "(PCAOB-BOTICSF-2026)" was attached to "a named owner, even in a small firm"; Botic does not say this | Ref removed |
| 06 | role_evolution | "In small firms, quality partners take on tool due diligence (ICAEW-POD-2025)" does not appear in the transcript | Replaced with ICAEW's Ian Pay: smaller firms lack specialists and lean on third-party providers (ICAEW-FRCVIEW-2026) |
| 07 | outcome measures | The AFM 74/20/6% split was described as covering "13 firms"; the AFM data also includes a request to six PIE firms, and the chart's population is not stated | Measures text corrected |
| 07 | role_evolution | "Member firms take tool-owner roles" generalised the FRC finding | Corrected to the finding: 2 of 6 firms assign a UK owner to globally deployed tools |
| 08 | risks | Unsourced connective: "a board that sees only usage counts cannot judge quality impact (FRC)" | Replaced with the FRC finding itself |
| 08 | role_evolution | "IFIAR calls on audit quality and ethics leaders" does not appear on IFIAR p. 7 | Changed to IFIAR's suggestion of ethical governance structures such as AI oversight committees |
| 10 | problem | The CPA.com survey was called a benchmark "of small and mid-size firms", with untrained staff the "most-cited" blocker | The report says 54 US CPA firms "of varying sizes", not representative, with this blocker top-ranked at 66%. Corrected |
| 10 | human_checkpoints | "Staff demonstrate competence before reviewing AI output (IFIAR p. 7)" embellished the source | Corrected to IFIAR's text: training mapped to competencies, learning outcomes assessed, records kept |
| 11 | risks | Wrong date, venue and audience: "Botic told firm leaders in January 2026" | JofA (12 Jan 2026) reports remarks made as acting chair at the **December 2025** AICPA conference. Corrected |
| 12 | risks, checkpoints | "RSM presents [firm-approved material] as the quality control" and "auditor checks cited source passages (CAQ-RSM)" both overstated the source | Reworded to what RSM says: grounding in firm-approved guidance and experienced human review "is vital" |
| 13 | problem | Foley & Lardner's own notes were attributed to "a PCAOB board member" | Attributed to Foley's notes of a PCAOB event with board member Botic and a colleague |
| 13 | risks | "PCAOB staff views are not Board policy (DART-SECPCAOB-2025)": DART does not say this | Re-sourced to the staff disclaimers in PCAOB-GENAI-2024 and PCAOB-PRIORITIES-2024. The PRIORITIES locator was corrected from pp. 6-7 to p. 5 |
| 14 | prerequisites, sources | "Root-cause taxonomy (PCAOB-BOTICIOWA-2026)": the speech never mentions root cause | Ref and source removed from this entry |
| 21 | role_evolution | Deloitte UK and the PIA Group interviewee were said to describe reviewers moving from clerical checks to judgemental areas, specifically for Smart Review | Replaced with each source's actual statement (Deloitte UK p. 95; Nyenrode interview) |
| 22 | prerequisites | "Components whose errors are not correlated (ICAEW-POD-2025)" is not in the podcast | Re-sourced to FRC p. 25 ("different capabilities and biases") |
| 22 | role_evolution | "Reviewers handle disagreements rather than every item (ICAEW-POD)" embellished the source | Corrected to McConnon: compare several AI answers, with a human at the end of the process |
| 23 | problem | Foley's notes were attributed to a PCAOB board member | Corrected as for entry 13 |
| 23 | role_evolution | "File records are shorter" is an inference from FRC p. 16 | Changed to the FRC's text: for widely used tools the balance shifts toward the central record |
| 23 | **grade B → C** | B rested only on PwC UK's documentation requirement, known second-hand through the preprint. The PwC UK 2024 report could not be opened (403 direct, empty mirror, archive connection reset) | Downgraded under the blocked-source rule. Note rewritten |
| 25 | problem | PCAOB 2024 outreach: "firms' supervision policies had not changed" | The spotlight says **some** firms. Corrected |
| 25 | risks | Botic's unnamed "recent MIT study" was asserted to be Kosmyna (2025) | Reworded: reports name only "a recent MIT study"; the best-known one is the 54-participant EEG essay study |
| 01, 02, 05, 06, 10, 14, 18, 20, 23 | sources | NFRA was cited through two CAalley press reports ("NFRA document was not opened") | Opened the NFRA paper itself (*Staff Series on Technology in Audit 01*, July 2026) and confirmed every NFRA claim. Replaced the press refs with NFRA-STAFF-2026 plus page locators, changed "as reported" to "NFRA staff", and noted that it is staff material, not Authority policy |

### Module

| Section | Problem found | Fix |
|---|---|---|
| Header | "not yet source-verified" | Now reads "sources verified 2026-10-17" |
| §2 | "Foundation models almost always third-party" overstated the IAASB's "generally" | Changed to "generally" |
| §2 | "Pilots (often lower-risk non-PIE audits)" misplaced the FRC's "often" | Changed to "some on lower-risk non-PIE audits" |
| §2 | "66% of small/mid US firms" misdescribed the survey | Changed to "66% of 54 surveyed US CPA firms" |
| §2 | "Supervision policies unchanged" overgeneralised the PCAOB outreach | Changed to "some firms'" |
| §3 | Entry 23's PwC UK policy is second-hand | Marked "second-hand" |
| §5 | "AFM (13 Dutch firms)" misdescribed the population | Changed to "AFM (Dutch study)" and "engagement-level usage" |
| §5, §9 | "31% of IFIAR members" could be read as firms | Changed to "IFIAR member regulators", with the 2024 date |
| §6 | "No body prohibits AI; none has AI-specific QM requirements" was an unbounded generalisation | Scoped to "these bodies" |
| §6 | "The FRC says the human auditor is always accountable" paraphrased loosely | Changed to the FRC's words: "people (firms and Responsible Individuals) are accountable for audit quality" |
| §6 | The IAASB "no new requirements" claim was sourced only to the minutes | Added IAASB-TQMPLAN-2026 (para 18) |
| §6 | QC 1000 status rested on secondary sources up to 8 Oct | Opened the PCAOB release (9 Sep 2026). It confirms the 15 Dec 2026 effective date and that the amendments take effect then only if the SEC approves. No approval appears on the PCAOB news page as of 17 Oct 2026. Added PCAOB-QCREL-2026 and reworded the EQCF item as a dropped requirement |
| §6 | Botic's lifecycle listed "validation"; the speech says "implementation" | Corrected |
| §6, §8 | NFRA was cited via press | Now cites the NFRA staff paper. The frontier date is 2026-07 (the paper is dated July 2026 and was uploaded on 23 July) |
| §7 | "the inputs show one unnamed example" was build-process wording | Changed to "the only public example is an unnamed firm's board dashboard described by the AFM", with source key |
| §7 | Unsourced connective: "Review, not preparation, becomes the main human task" | Removed. The FRC and Deloitte statements stay |
| §7 | "The study regulators cite is an EEG essay study" | Changed to "Botic cited an unnamed MIT study (the best-known one is …)" |
| §7 | "In small firms a quality partner takes on vendor due diligence" was unsourced | Replaced with the ICAEW statement on reliance on third-party providers |
| §8 | "IAASB approves non-authoritative QM material" (Dec 2025) | The minutes record approval to **develop** the material. Corrected |
| §8 | "PCAOB forms an IMC" | Changed to "launches an Inspections Modernization Council (advisory group)" |
| §9 | "The clearest public failure of review" was an editorial superlative | Changed to "a public review failure". Added that the revised report disclosed GenAI use (AP) |
| §10 | Mentions of the synthesis report, the pilot's keys and "deep dives" | Removed. Also added PCAOB-QCREL-2026 and NFRA-STAFF-2026 to the source lists |

Checked and correct as written: the IFIAR survey figures (35%, 26% in 2022, 161 firms, 37/32/24/20/9%, 31 vs 10
supervision findings, 21 vs 6 internal-inspection findings), the IFIAR 2025 31%/29% figures, all FRC thematic counts
(0, 1, 2, 2, 1 and 2 of 6), Deloitte UK PairD (4,649 users, over 75%, about two million prompts), Smart Review ("all
FTSE audits have access"), the Technology Controls Board (April 2026, p. 48), KPMG 95,000+, RSM 4,000+, CAQ 13% / 26% /
312 audits, the Sanville figures, Fedyk (5.0% / 0.9%, 36 firms), IRBA at least 56%, CPAB 2025 inspection observations,
AFM's precondition ordering, the FRC sandbox terms, the FRC supervision start (April 2026, largest firms), the AICPA
practice aid contents, and Botic's well-below-50% file-review remark.

## 4. Sources

- **Opened: 81 of 81.** That is the 79 sources originally cited (70 in the YAML and 9 cited only in the module) plus
  two primaries added during verification (PCAOB-QCREL-2026 and NFRA-STAFF-2026). Of these, 75 were fetched
  directly. Six were read through the r.jina.ai mirror: PCAOB-BOTICSF-2026, PCAOB-BOTICIOWA-2026, PCAOB-LOGOQC-2026,
  PREPRINT-AIJGDI-2026, FOLEY-PCAOB-2026, and the PCAOB QC release.
- **Unreachable: 1.** The PwC UK 2024 transparency report, the primary source behind the preprint's PwC claims in
  entries 10 and 23. It returned 403 directly, empty text through the mirror, and a connection reset from the Wayback
  Machine. It is not cited directly, but entry 23 was downgraded because of it.
- **Not opened (behind a login, or never cited):** the AICPA practice aid full text (the release and two press reports
  were opened), and the EY UK and KPMG UK 2024 transparency reports (used second-hand via the preprint and flagged in
  notes).
- Two dates rest on page metadata rather than a byline: FIELDGUIDE-SANVILLE-2026 is "2026" (the sitemap shows a
  2026-07-13 update), and the Deloitte UK reports are 2025-09 and 2026-09 (PDF metadata 30 Sep 2025 and 29 Sep 2026).

## 5. Targets

| Target | Status |
|---|---|
| 15–25 use cases | Met (25) |
| ≥50% graded A or B | **Not met (40%)**. Not raised artificially: no measured outcome exists, and #23 had to drop |
| Every source dated (ISO) | Met. The validator passes; the undated TRI page now has 2026-07-21 |
| Ids unique; vocabulary values valid | Met (validator) |
| Quotations under 25 words | Met (the longest source quotes are about 20 words) |
| Module ≤300 lines with table of contents | Met (299) |
| No build-only references | Met. Remaining "pilot" words describe tool pilots; references to other modules' ids are kept |

## 6. Error patterns to fix in the briefs

1. **Speaker and venue drift.** A law firm's own notes were attributed to a PCAOB board member (13, 23). A December
   2025 conference remark was dated to January 2026, when the article reporting it was published (11). Add a rule:
   attribute to the person in the source, and date remarks to when they were made, not when they were reported.
2. **Refs attached to unsupported clauses** in prerequisites and role_evolution (02, 03, 06, 08, 14, 22). The source
   was real but the clause was not in it. The verifier found 8 instances. Add a rule: a parenthetical ref in these
   fields must point to a sentence that states the clause, or be dropped.
3. **Qualifier migration.** "Often", "some" and "most" moved between nouns or were dropped: "pilots are often run on
   non-PIE" (the FRC says some firms), "firms' supervision policies unchanged" (the source says some firms), and
   "almost always third-party" (the source says generally). Ask synthesis to copy quantifiers verbatim.
4. **Population mislabels on statistics**: the AFM chart called "13 firms", IFIAR "members" read as firms, CPA.com
   called "small and mid-size". Make the `measures` field quote the source's population words.
5. **Event inflation in frontier lists.** The IAASB was said to "approve material" when it approved developing it,
   and the PCAOB to "form" a council it had only begun forming. Frontier items should use the source's verb.
6. **Grades resting on a source read second-hand.** Entry 23's B depended on an academic paper's reading of a
   transparency report nobody opened. The vocabulary should state that second-hand evidence of a named practice caps
   at C unless the primary is opened.
7. **Asserted identity of unnamed studies.** "The study regulators cite" was presented as a fact when the regulator
   named no study. Require "unnamed in the source" wording.
8. **Press summaries used when the primary is reachable.** The NFRA paper was on the regulator's site all along. The
   briefs should require one attempt at the primary (site home page through the mirror) before citing press.
9. **Build-only metadata in shipped files.** Notes carried candidate ids ("practice-01"), "landscape", "R1" and
   "pilot". The synthesis brief should say notes are for end readers only.
10. **Search-only figures in A/B entries: none found.** Every source is marked `access: full`.
