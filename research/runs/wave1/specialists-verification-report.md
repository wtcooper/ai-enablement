# Verification report: assurance / specialists

- **Verified:** 2026-10-17
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/specialists.yaml` (13 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/specialists.md` (272 lines, under the 300 limit)
- **Method:** every cited URL was opened with `curl` (`pdftotext` for PDFs). Pages that blocked curl were read through the
  `r.jina.ai` mirror (BV Resources, Federal Register, Going Concern). DOI landing pages returned 403, so abstracts and
  dates came from the Crossref API. Dates were checked against bylines, `article:published_time`, JSON-LD, the IVSC
  WordPress API and PDF metadata.
- **Validator:** `python3 scripts/validate.py` shows 0 ERRORs for either file. The expected below-target WARN remains
  (13 use cases, 2 A/B = 15%). The only current ERRORs are broken links in `assurance/ARCHETYPE.md`. That file is not
  in scope and was not touched.

## 1. Counts

| | Use cases |
|---|---|
| Kept | 1 (`#12`) |
| Fixed | 12 |
| Rejected | 0 |

Module: about 30 statements fixed (attributions, dates, standards wording). One unverifiable count was removed. Five
standards facts were added from primary sources: PCAOB Release 2018-006, ED-500 para 14, the PIOB approval date, the
UK "periods commencing" wording and AICPA "nonauthoritative".

## 2. Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 0 | |
| B | 2 | `#01` (Big Four valuation advisory), `#13` (KPMG UK tax advisory). Both adjacent, not audit-side |
| C | 3 | `#02`, `#03`, `#12` |
| D (idea) | 8 | `#04`-`#11` |

No grade changed. `#13` keeps B, but now on a different basis: the predictive tool KPMG says it uses. Ask Blue J itself
was only announced (see fix 13).

## 3. Fixes and rejections

| # | Where | Before | Action | Reason |
|---|---|---|---|---|
| 1 | `#01` problem | analysts spend hours "before judgment work begins" | Fix | Embellished. Source: tasks "previously required hours of manual effort" |
| 2 | `#01` BVR-BIGFOUR-2025 | date "from a search extract; page shows no date" | Fix (note) | Date confirmed: 21 May 2025, BVWire issue #272-3 |
| 3 | `#01` BVR-ASA2026-2026 | date 2026-05, search-only, type conference | Fix | Teaser opened: report dated 2026-09-11, type press. It also names "audit scrutiny" as a panel topic |
| 4 | `#02` problem | peer selection is "a manual, judgment-heavy step" [Valutico] | Fix | Not in source. Now: Valutico pitches the release as reducing manual effort |
| 5 | `#02` IVSC locator | "p4 (IVS 104 quotation)" | Fix | Quotation of IVS 104 para 40.01 is on pp10-12 |
| 6 | `#03` problem | narrative sections "take time to write" | Fix | Unsourced. Now uses IVSC p6: report writing is among the straightforward tasks AI can automate |
| 7 | `#04` problem | "quality controls are manual" | Fix | Not in source; removed |
| 8 | `#05` outcome | figure "median score 0.33" attached to the agent finding | Fix | **Statistic reported as something it doesn't measure.** 0.33 is analyst-versus-analyst agreement. Split into two outcomes: the agent result (no score in abstract) and the benchmark-design finding |
| 9 | `#06` AAA-GENAI-2024 | date "2024" | Fix | Page dated 2024-10-30 (Contingencies Nov/Dec 2024 reprint) |
| 10 | `#06` problem, role | "validating models" [SOA]; "must stay qualified without AI" | Fix | Both reworded to the sources' own words ("explain methods, justify assumptions, communicate findings"; "unqualified without AI ... likely not qualified with AI") |
| 11 | `#07`, `#08` FORVIS-RESERVING-2025 | date "2025 (estimate)" | Fix | **Wrong date.** First published on mazars.ie on 22 May 2024 (archived Better Regulation copy). Key renamed FORVIS-RESERVING-2024; BETTERREG-MAZARS-2024 added |
| 12 | `#07` ladder | augment | Fix | The specialist uses XAI and benchmark tools but still does the work, so `assist` |
| 13 | `#13` solution, outcomes, role | Ask Blue J "available in the 3,000-strong function"; it "dramatically reduces time"; frees experts | Fix | **Claim attributed to the wrong subject.** In the release these sentences describe the existing Blue J predictive tool. Ask Blue J "will launch". Provenance changed from vendor-published to self-reported. Title and grade note rewritten |
| 14 | `#09` risk | "PCAOB specialist material read here" | Fix | Process wording. Now names the 2025 Spotlight. Added ED-500 para 14 (management's expert, no AI element) |
| 15 | `#09`, `#04` IVSC-IVSED-2026 | date 2026-01 | Fix | Published 2026-01-30 (IVSC news post; consultation 30 Jan to 30 Apr 2026) |
| 16 | `#10` risk | "practice aid is non-authoritative [AT-AICPAPA-2026]" | Fix | **Wrong document:** Accounting Today does not say it. AICPA's landing page does ("nonauthoritative guidance"); AICPA-GUIDE-2026 added |
| 17 | `#10` AICPA-PA-2026, AUASB-AI-2025 | type standard-setter / regulator | Fix | AICPA practice aid = professional-body; AUASB = standard-setter |
| 18 | `#11` notes, module §6 | "only one of 49 readable comment letters names AI" | Fix | Count could not be re-verified. Replaced with what was verified: ICAN asked; the UK final text (para A1) does not name AI experts |
| 19 | `#11` role | "54 surveyed US firms" | Fix | Report says 54 firms (CPA.com/AICPA survey), not "US". Locator corrected to printed p19 / PDF p20 |
| 20 | `#11`, `#13` risks | none | Fix (added) | PCAOB Release 2018-006: IT and income taxes are specialized areas of accounting and auditing, outside the specialist standards; the Board declined commenters' AI request (pA3-5) |
| 21 | `#09`, `#11`, `#13` FRC-620STD-2026 URL | caalley.com mirror | Fix | Official FRC PDF (frc.org.uk/documents/9933/...). Text checked as identical |
| 22 | `#07`, `#11` sources | FRC-ARAQ-2026 / PCAOB-SPECIALISTS-2025 cited but not listed | Fix | Source entries added |
| 23 | all notes, header | "From combined-NN", research path, "landscape lead A14", "copy saved in the landscape run" | Fix | Build-only references removed |
| 24 | module §1 | no PCAOB dates | Fix | Added: specialist amendments apply to fiscal years ending on or after 15 Dec 2020 [PCAOB-SPECREL-2018, p4] |
| 25 | module §2 | "Required when expertise ... is necessary (para 7)" | Fix | Para 7 requires the auditor to *decide whether* to use an expert. Examples are from para A1 |
| 26 | module §2 | ISA 620 para 11 cited to [PCAOB-SPECIALISTS-2025, p10] | Fix | **Wrong document.** Para 11 is now cited to the FRC standard; the PCAOB understanding is cited separately |
| 27 | module §2 | "(PwC, one impairment)" | Fix | This is PwC's own response section in the FRC report |
| 28 | module §3, §7, §9 | "#13 KPMG UK use Ask Blue J"; "some firms fully automate report writing" | Fix | Same as fix 13. IVSC says report writing "may be" fully automated |
| 29 | module §6 | ISA 620 "effective 15 Dec 2026" only | Fix | Added PIOB approval (Dec 2025) [FRC-620-2026, para 4]. UK wording: periods commencing on or after 15 Dec 2026 |
| 30 | module §6 | TAA amendments "say they do not address AI" | Fix | **Not in source.** Notice says the amendments address only one area of technology use; commenters asked for AI research |
| 31 | module §6 | ED-500 "strains" the input-output model | Fix | Quoted wording: GenAI-enabled tools "challenge elements of the input-output model" (EM paras 67-69). Comments due 15 Dec 2026 |
| 32 | module §5 | "six largest networks" | Fix | IFIAR says GPPC networks |
| 33 | module §7 | "AI and data specialists are a new kind of expert" | Fix | Overstated; this is idea `#11` ("may become") |
| 34 | module §8 | "2026-01 to 04-30"; 2026-09-11 BVR missing; "Revised ISA 620 effective" | Fix | Exact dates; BVR extended report added; "for periods beginning on or after" |
| 35 | module §8 | firms "oppose prescriptive standards now" | Fix | PwC asks for guidance first and possibly standards later. Now: "favour guidance over prescriptive standards for now" |
| 36 | module §6 | "Steps that stay with a person" unsourced | Fix | Sources added (ISA 620 paras 7-13, IVS 105, AUASB) |
| 37 | module §10 | BVR-BIGFOURLIMITS/FVGUIDANCE "search only"; IVSC-DIALOGUE dated by event | Fix | Teasers opened (vol. 32 no. 3, March 2026; no. 7, July 2026). Dialogue page published 2026-03-26 (session 2026-06-25) |

**Checked and confirmed as written:** IAASB issue date 5 Jan 2026 and the four standards affected; FRC final 23 Sep
2026; ISA (UK) 620 paras 6(a), 7, 9, 9A, 9-1 (PIEs), 11, 15-1, A1, A19A; no AI wording in the UK standard. FRC
feedback statement para 10 ("acceptable level" inconsistency). IVSC paper date 23 Jul 2025 and pp4-14 claims. IVS ED:
IVS 107, AI requirements in IVS 101/104/105/106, publication planned 31 Jan 2027, effective 31 Jan 2028. AICPA practice
aid issued 13 Oct 2026, with more sections promised. PCAOB Spotlight (Feb 2025): pp3, 5-7, 10-12 and no AI content.
FRC ARAQ pp14, 26-28, 45, 73, 82, 92, 95. CAQ pulse 6/46/40% and 33/27/27/26%. IFIAR ~30% (p5). Computerworld/FT
7% vs <2%. CohnReznick 26 Mar 2026. Valutico Paraloq 24 Jun 2025. SOA 23 Sep 2026. Both arXiv abstracts (27 Jul
2026). SSRN field experiment abstract. Commerford, Hirsch and Hux abstracts. ICAS 20 Aug 2026. Going Concern 12 Aug
2026. IVSC AGM session on 17 Nov 2026.

## 4. Sources that could not be reached

| Source | Problem | Handling |
|---|---|---|
| Publisher pages for COMMERFORD-2022, HIRSCH-2019, HUX-2022, SSRN-LLMAQ-2026 (doi.org, SSRN, Wiley, AAA) | 403 / bot block | Abstracts and dates from the Crossref API. Entries stay abstract-only |
| AICPA practice aid full text | Member login | Release, landing page and Accounting Today used |
| BV Resources full reports (BVR-BIGFOURLIMITS-2026, BVR-FVGUIDANCE-2026, BVR-ASA2026-2026) | Paywall | Teasers read via mirror. Cited only for titles, dates and topics |
| pcaobus.org AS 1210 standard page | 403 | Release 2018-006 PDF opened from assets.pcaobus.org instead |
| web.archive.org | Proxy connection reset | Better Regulation archived copy used for the Mazars date |
| SOA report PDF | Not downloaded | Landing page only (as before) |

**Totals:** 46 distinct URLs (42 originally cited plus 4 added). 42 were opened and read, directly or through the
mirror. The 4 DOI/SSRN pages were blocked; their abstracts were read through Crossref. Full text was unreachable for
4 documents behind a paywall or login (3 BVR, 1 AICPA aid).

## 5. Targets

| Target | Result |
|---|---|
| 15-25 use cases | **Not met:** 13 |
| At least 50% graded A or B | **Not met:** 15% (2 of 13, both adjacent) |
| Every source dated (ISO) | **Met.** No year-only estimates remain except the AAA-original month, which is noted; Forvis is now 2024-05-22 |

As stated in the module, these targets were waived for this low-evidence module. No audit-side deployment of AI by
specialists was found during verification either.

## 6. Error patterns to fix in the briefs

1. **One source sentence, wrong subject.** Within a single press release, sentences about an existing tool were
   applied to a newly announced product (`#13`). Ask deep-dive writers to quote which product a figure or claim refers
   to.
2. **Figure placed next to the wrong claim.** A benchmark-design statistic (0.33 analyst agreement) sat beside an agent
   capability claim (`#05`). Require `measures` and `description` to describe the same thing.
3. **Attribute to the document that says it.** "Non-authoritative" was cited to a press article that does not say it.
   "Do not address AI" was cited to a notice that does not say it. ISA 620 para 11 was cited to a PCAOB document.
4. **Estimated dates.** "2025 (estimate)" was off by a year. Search for syndicated or archived copies (Better Regulation,
   LinkedIn posts) before estimating. Date by the page's publication date, not the event date.
5. **Unverifiable process counts** ("one of 49 readable letters") should not reach the module. State only what a
   reader can check.
6. **Missed primary sources.** The research said PCAOB pages were blocked, but `assets.pcaobus.org` PDFs open. Release
   2018-006 holds the key AI-relevant statement (IT is outside the specialist definition). Tell researchers to try the
   assets host and the release PDF before giving up.
7. **Mirrors instead of the official URL** (caalley.com for the FRC standard). Require the issuer's URL when one exists.
8. **Embellished problem statements.** Several `problem` fields added causes the source does not give
   ("judgment-heavy", "manual", "before judgment work begins"). Problems need the same sourcing discipline as outcomes.
9. **Build-only notes** ("From combined-NN", research paths) leaked into shipped files. The synthesis brief should forbid
   them.
