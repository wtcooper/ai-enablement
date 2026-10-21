# Verification report: advisory / forensic-disputes

Checked on 2026-10-21 against the cited sources. These files were edited in place:

- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/forensic-disputes.yaml`
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/forensic-disputes.md`

Every cited source key was opened: the 36 keys in the YAML and the 7 keys cited only in module §10, 43 URLs in all.
Most were read directly with curl. PDFs were read in full with `pdftotext`: the J.S. Held report, the ACFE Report to
the Nations, the evidence-rules agenda book (355 pp.), the Standing Committee report, FinCEN, the IAF report, the
Dean Dorton deck, HaystackID, the Relativity/Redgrave preprint, FinTAF, DOJ ECCP, and both arXiv papers. Three pages
were blocked to curl and read through `r.jina.ai`: J.S. Held's expert article, both BVWire articles, and the SEC
press release. JRFM was blocked by MDPI and by the mirror, so its abstract was read from Crossref metadata. Dates were
checked against `article:published_time`, JSON-LD, PDF metadata and bylines. All three ACFE dates were confirmed:
the RTTN press release is dated 2026-05-12, the SAS release 2026-03-25 and the Canada release 2026-10-01.

Every figure in the YAML outcomes and in module §5 was checked against the source text. `scripts/validate.py`
reports 0 errors. Its only warning for this file is the A/B share (see Targets).

## Counts

| Action | Entries | Ids |
|---|---|---|
| Kept | 4 | 02, 06, 13, 14 |
| Fixed | 11 | 01, 03, 04, 05, 07, 08, 09, 10, 11, 12, 15 |
| Rejected | 0 | none (one source, STEPTOE-FRE707-2026, was removed from #15) |

## Final grade mix

| Grade | Count | Ids |
|---|---|---|
| A | 0 | none |
| B | 5 | 01, 02, 04, 06, 07 |
| C | 5 | 03, 05, 08, 09, 10 |
| D | 5 | 11, 12, 13, 14, 15 (all labelled "Idea") |

**Grade A rule.** No entry qualifies. J.S. Held's numbers (25,000+ checks "in days rather than weeks"; 20,000
transactions matched "in just hours"; >$37M found) are narrative case-study figures with unnamed clients, and the
weeks comparison is the firm's own estimate. Kniepmann's 85% vs 99-100% is a recollection in a vendor white paper.
Both stay in B entries, labelled with their provenance. The Redgrave recall and precision figures are measured, but
they come from a test on a public archive in e-discovery, an adjacent process, so #04 stays B.

## Fixes and rejections

| Id / section | Change | Reason |
|---|---|---|
| #01 | "Forensic principal" changed to "litigation principal" at Anders | Wrong title: the white paper gives "Litigation Principal" |
| #01 | The guardrail "extraction needs to be reproducible" now reads "every transaction is linked back to the original banking evidence" | Embellished: p. 4 says linking makes the report withstand courtroom scrutiny. It says nothing about reproducibility |
| #01 | role_evolution attributed to Matthew Cordell (senior director) | Wrong speaker: it is one practitioner's quotation, not "J.S. Held's practitioners" |
| #01 | The VALID8-WP-2025 date note is extended: no earlier than mid-2024 (cites the June 2024 Chevron ruling); the 2025-02 date stays inferred | Undated page. The sitemap shows only a 2026-03 modification |
| #03 | **Grade B to C.** The locators were corrected: Fig. 13 is on pp. 23-24, median loss on p. 40, duration on p. 41 (the p. 47 reference was removed). The JRFM locator now reads "Abstract (via Crossref)" | Grade inflated by an adjacent process: no named AI deployment. ACFE measures analytics in general at victim organisations, not AI. The AI adoption figure comes from an anonymous survey |
| #04 | The Redgrave recall/precision outcome changed from `independent` to `self-reported` provenance | A statistic reported under a provenance it lacks: the figures originate with the Redgrave case study (Keeling et al.) and are only reproduced by the re-analysis |
| #04 | "Independent academics" changed to "independent researchers (University of Waterloo and Elevate)". A note was added that co-author Pickens co-wrote the earlier Relativity/Redgrave Data preprint | Embellished: one author works at Elevate, a legal-services company |
| #04 | Everlaw: "matched human" changed to "comparable to". The figure now reads 0.82 vs 0.60, a relative gain of 36% (22 points) | Statistic misreadable: the 36% is relative, not percentage points |
| #04 | Added the named user quote (Lowenstein Sandler associate, "hundreds of hours" reduced) as a vendor-published outcome | Better support for the B grade and for in-production maturity |
| #05 | "Unnamed customer quote" changed to "Gina Bieber, Director; organisation not given" | Misdescribed: the testimonial is named |
| #07 | The BVR-AICPAAIGUIDE-2025 type changed from `professional-body` to `press` | Wrong source type: BVWire is a trade publisher |
| #08 | The trained-on-past-fraud point is now attributed to others whom the BRG author cites | Wrong speaker: Dery attributes it to "others" |
| #09 | The problem no longer says reports take "a large part" of staff time; it now cites the deck's question without a figure. Dean Dorton date changed from 2025-09 to 2025-09-05 | Unsourced claim. The exact date comes from the PDF metadata |
| #10 | Guardrail rewritten to what KTS says (keep privileged and protective-order material out of gen-AI tools; FRE 502(d) order in high-stakes matters) | Unsourced connective claim: KTS does not discuss collected employee AI chats |
| #11 | "Terminating sanction" changed to "dismissed, citing AI-generated video". "Most respondents favoured a rule" changed to "55% without a challenge; 5 of 15 with one". The judge checklist is now attributed to the NCSC/Thomson Reuters Institute cheat sheet. FJC locator changed to pp. 225-229 (memo dated 2026-03-25) | Embellished: NBC does not say "terminating sanction". The share was overstated. Wrong document: the checklist is not NBC's own guidance |
| #12 | Added "US" to the AFP 76% | Missing qualifier: the survey covers US organisations |
| #15 | **STEPTOE-FRE707-2026 removed.** role_evolution was replaced with the sourced independent-validation factor (agenda pp. 18-19), and the inference is flagged | Source unreachable (403 direct, 401 mirror) and not in search, so it could not be confirmed |
| #15 | The validation-studies sentence is now attributed to the *revised* draft committee note. Locator corrected: pp. 65-66 are the Jan 2026 Standing Committee draft minutes, not a "Nov 2025 report"; pp. 132-133 hold the revised note | Wrong document: the August 2025 published draft does not contain the sentence |
| All | `last_reviewed` set to 2026-10-21. The header grade count was updated | Format |
| Module header and §3 | "6 of 15 are B" changed to 5. "Independent academics" changed to "independent researchers". The named law-firm user was noted | Follows the YAML changes |
| Module §5 | Redgrave provenance relabelled. Everlaw figure clarified as relative. OSINT row now says "only one system of 74 studies; favourable, non-reproducible" | A statistic reported as something it doesn't measure |
| Module §6 | HSFKRAMER-CJC-2026 (search-only) replaced by the primary CJC page (CJC-AIDOCS-2026, June 2026 update: "proportionate transparency in relation to expert evidence") | Better source found. The CJC page does not itself restate the February proposal that experts explain AI use |
| Module §6 | "The AICPA says" changed to a JofA article by the AICPA Ethics Division's communications manager. "Whether an anomaly is fraud" changed to "is meaningful" | Wrong speaker; embellished |
| Module §7, §9 | "AI labs are recruiting / paying" changed to "an AI training-data startup (AfterQuery)". The J.S. Held "thinking not processing" line is now attributed to a senior director | Wrong speaker: AfterQuery is a YC-backed data vendor, not a lab |
| Module §8 | "Terminating sanction" removed from the Mendones item | Embellished |
| Module §10 | STEPTOE-FRE707-2026 and HSFKRAMER-CJC-2026 removed; CJC-AIDOCS-2026 added | As above |

Cross-references were checked, and all exist: `professional-services-quality-review-02/-03/-06/-13/-16`,
`tax-controversy-08`, `assurance-acceptance-independence-15`, `professional-services-talent-learning-07`.

## Sources that couldn't be reached

- **STEPTOE-FRE707-2026** (Steptoe blog, Rule 707): 403 directly, 401 through r.jina.ai, and Google cache and
  archive.ph were blocked. Removed.
- **HSFKRAMER-CJC-2026**: Cloudflare challenge both directly and through the mirror. Replaced by the primary CJC page.
- **JRFM-FORENSICAI-2026**: the article page was blocked by MDPI and by the mirror. The abstract was read via
  Crossref, which supports every use; the locator was narrowed to the abstract.
- The Weber opinion and the Redgrave paper (Keeling et al.) were not opened; their content rests on KTS/AICPA and on
  the arXiv re-analysis, as the notes already said. The Wayback Machine was rate-limited, so VALID8-WP-2025 stays
  inferred-dated.

## Targets

| Target | Result |
|---|---|
| 12-20 use cases | Met: 15 |
| At least 50% graded A or B | **Not met: 5 of 15 (33%)**, down from 6 after #03 was downgraded. This matches the header finding that no accounting-firm forensic practice publishes measured AI outcomes |
| Every source dated | Met. All dates are ISO. Page-access dates are flagged in the locators for undated pages (Relativity, Valid8 hub, SEC eCFR) |
| Vocabulary values, unique ids, quotes under 25 words | Met (the validator reports 0 errors) |

## Error patterns to fix in the briefs

1. **Wrong speaker or document.** Several slips: practitioner titles (Anders), "AI labs" for a data vendor, "the
   AICPA" for a JofA article, a judges' checklist credited to NBC, and an agenda-book page labelled as the wrong
   meeting. Briefs should require the speaker's exact title and the document section for every attributed sentence.
2. **Provenance of reproduced figures.** A figure reproduced in an independent paper was labelled `independent`.
   Provenance should follow the organisation that produced the measurement.
3. **Embellished legal characterisations.** Examples: "terminating sanction", "most judges favoured a rule",
   "reproducible". Legal outcomes should be stated in the source's words.
4. **Adjacent-process grading.** ACFE analytics data lifted a no-named-deployment entry to B. Briefs should say that
   a survey of anonymous respondents is never a "named deployment".
5. **Relative versus absolute percentages.** Vendor "+36%" claims should state both values.
6. **Search-only and blocked sources in the module.** Try the primary regulator or body page (as with the CJC)
   before falling back to a law-firm summary.
