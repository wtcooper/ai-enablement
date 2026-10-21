# Verification report: assurance / benefit-plans

Checked 2026-10-21 against the sources themselves. Files edited in place:
`plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/benefit-plans.yaml` and
`.../assurance/modules/benefit-plans.md`. `scripts/validate.py`: 0 errors (one existing warning: 47% A/B for this file).

## Counts

| Action | Entries |
|---|---|
| Kept unchanged | 0 |
| Fixed | 15 (01-15) |
| Rejected | 0 |

Every entry needed at least one correction, mostly wording and attribution. No grade changed. No source was
missing. Both blocked sources (dol.gov and psca.org, 403) were read in full through the r.jina.ai mirror.

## Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 0 | none |
| B | 7 | 01, 03, 05, 06, 07, 09, 10 |
| C | 6 | 02, 04, 08, 11, 12, 13 |
| D | 2 | 14, 15 (both labelled "Idea") |

## Fixes (use cases)

| Entry | Fix | Reason (error pattern) |
|---|---|---|
| 01 | The 40% Rea figure and the 80-to-54 Belfint figure are now attributed to the vendor's narration, not to the firms' managers | Both figures sit in Autire's own text, not in the quoted speakers' words (wrong speaker) |
| 01 | "On first use at an existing client, 8,000 flagged records" changed to "the managing director recalls opening a file with 8,000 flags" | The source does not say it was the first run or an existing client (embellished qualifier) |
| 01 | Firm name changed to "Rea" (Rea Business Advisors in the case study, Rea & Associates elsewhere on the vendor site); "pilot in 2022" | Case study uses the new name |
| 01 | "Not model output" changed to the vendor's own contrast with "probabilistic output" | Embellished paraphrase |
| 01 | Added the DOL primary study (EBSA-AUDITQ-2023) with 48 of 307 = 15.6% | Primary source now read; figure was only from a firm blog |
| 02 | The 50-hour tile moved from AUTIRE-TESTING-2026 to AUTIRE-AI-2026 and split into its own outcome. The 30-minute testimonial is now marked as being about compliance testing in general, not the AI feature | Figure cited to the wrong page; testimonial described as something it does not measure |
| 02 | Maturity changed from in-production to announced | In-production needs a named organization; both users are unnamed |
| 02 | Practice-aid sentence now attributed to the AICPA chief auditor's quotation in the news release | Wrong-document attribution |
| 03 | Ledgerline prerequisite: only the payroll provider is connected once; the recordkeeper package is still requested | Overstated |
| 03 | ICPAS checkpoint changed from "audit programs include" to "the author recommends" | A recommendation was stated as a fact |
| 03, 10 | Sikich brochure dated 2026-07 (PDF creation metadata 20 Jul 2026), not "2026" | Missing precise date |
| 04 | Human checkpoint now matches the source: documentation stays with the auditor, and a manager checks whether the numbers make sense | Paraphrase invented a review gate |
| 05 | "Anders says it saved hundreds of hours" changed to "the vendor's case study says"; "regional" removed | Vendor narration given as the firm's words; descriptor not in source |
| 06 | Sensiba's 30-45 minutes is now labelled as general technical research, not plan audits | Evidence from an adjacent process |
| 06 | "Seniors review conclusions" removed; checkpoint now follows Sensiba's wording | Unsourced connective claim |
| 06 | Role evolution attributed to the vendor's case study, plus the auditor's own quote | Attribution |
| 07 | Checkpoint "auditor judges deviations and CUECs (Kimberlin)" replaced: Kimberlin does not describe review; AuditMiner's toolkit footnote leaves reliance decisions to the auditor | Unsourced claim attributed to the wrong document |
| 07 | Anders "(regional firm)" removed; the claim is attributed to the vendor's case study | Descriptor not in source |
| 08 | Checkpoint "the auditor still concludes" replaced with what the release says; the ladder note is marked as analyst judgment | Unsourced connective claim |
| 08 | Locator notes the release dateline (2 Dec 2024) against the page date (10 Dec 2024) | Date discrepancy |
| 09 | "Controlled by New Mountain Capital since April 2022" changed to "took a controlling investment announced April 2022", with a note that the 2024 paper does not cover later ownership | A 2024 source was extended to the present |
| 09, 11, 12 | DOL figures re-sourced to the primary study; 80% changed to "nearly 80% (83 of 105)"; peer review "Pass" for 96 of 105 deficient audits | Precision; primary source |
| 10 | Speed as a selling point and TPA referrals now attributed to the case study's narration | Wrong speaker |
| 12 | "Plan audits are concentrated in specialist firms" replaced with the DOL population figures (133 firms with 100+ audits did 47,982 of 86,863) | "Specialist" was not in the source |
| 13 | Checkpoint about the acceptance process removed | Unsourced connective claim |
| 14 | Checkpoint "auditor concludes on reliance (AICPA-TQA9561-2026)" replaced | TQA 9561 covers the service auditor's SOC examination, not user-auditor reliance (wrong document) |
| 14 | Audenza prerequisite: "system description" removed; the CUEC section is "frequently skipped" | Embellished |
| 14 | Added the PSCA column on recordkeepers' existing AI use | Better source found |
| 15 | PSCA source upgraded from search-only to full (mirror); date corrected from 2026-08 to 2026-08-25; now described as an opinion column by a recordkeeper's general counsel about sponsor-side compliance monitoring; "unverified" removed | Search-only source; imprecise date and description |

No rejections: every cited source exists and supports the corrected wording.

## Fixes (module file)

| Section | Fix | Reason |
|---|---|---|
| Read this first | "No regulator... has said anything about AI" changed to "this review found no statement" | Unsourced absolute claim |
| 2, acceptance row | Audit threshold corrected to participants with account balances (after the shift away from counting eligible participants), citing Ledgerline and JofA. The plan-type list is now cited to Sikich | The Metz page states the old "eligible participants" rule, and the list of types was not on the Metz page |
| 2, 5, 6, 9 | DOL figures re-sourced to EBSA-AUDITQ-2023 (now read in full). Deficiency-area denominator stated as 307 sampled audits (it was "not stated"). 80% changed to "nearly 80% (83 of 105)". "307 vs 308" is now attributed to the DOL's own text and table. New row: 91% of deficient audits had a Pass peer review | Primary source; precision |
| 5 | EBSA-AUDITQ-2025 renamed to JRCPA-AUDITQ-2025 (a Jones & Roth summary); "affected" changed to "at risk", which matches the DOL wording | Ref named after the wrong publisher; reworded figure |
| 4, 5, 9 | The 8,000-flag wording now matches the source; the 40%, 80-to-54 and Anders figures are attributed to vendor narration | Same errors as in 01 and 05 |
| 6 | "Steps that stay with a person": each step now carries its own source. The SOC 1 step is re-sourced to AuditMiner. The note now says no source describes the review of a generated risk assessment | Unsourced connective claims |
| 7 | Kimberlin and Anders statements attributed to the vendor case studies; "home-page case card" corrected to the site's menu card | Attribution |
| 8 | "Agenda not public" changed to "agenda page did not load for this review" | Overstated |
| 3 | #05 "regional firm" removed; #02 marked announced | Same as the YAML |

## Sources that could not be reached, or were only partly read

- **dol.gov** (DOL Audit Quality Study PDF) and **psca.org** (PSCA column): 403 directly; both read in full through r.jina.ai.
- **AICPA EBP Conference 2026 agenda page**: built by script, so no content loaded. The home page and the workshops page were read.
- **AICPA TQA 9561 body**: login required; the landing page only (scope and date).
- **AICPA EBPAQC tools PDF**: the landing-page summary was read; the PDF itself was not opened.
- **AuditMiner Anders case study**: no text layer; read as page images.
- Citrin Cooperman's ownership after 2024 was not checked. The entry no longer claims it is current.

## Targets

| Target | Result |
|---|---|
| 12-20 use cases | Met (15) |
| At least 50% A or B | **Not met**: 7 of 15 (47%). No grade was raised to reach the target. The C entries are vendor-only (02, 04, 08, 11, 13) or a one-line firm claim (12). |
| Every source dated | Met. Undated vendor and firm pages carry the copyright or retrieval year ("2026") |
| Ids unique; vocabulary values; quotations under 25 words | Met (validator passes; no long quotations) |
| Cross-references exist | Met. Checked: substantive-testing-25, controls-testing-13, quality-management-06/-12/-16/-17/-23, acceptance-independence-20, planning-risk-assessment-20 |

## Error patterns to fix in the briefs

1. **Vendor narration given as the firm's words.** In vendor case studies the headline figures (Rea 40%, Belfint 80 to 54, Anders "hundreds of hours") are usually in the vendor's own text, not in the practitioner's quotes. Briefs should require writers to say which one they are citing.
2. **Recollections turned into events.** "When you see 8,000" became "on first use at an existing client". Briefs should forbid adding a when, a where or a who that the source does not give.
3. **Testimonial tiles cited to the wrong page.** Vendors spread their tiles across pages. Briefs should require the locator to name the tile and the page it sits on.
4. **Human checkpoints and guardrails filled in by inference.** This happened in 06, 07, 08, 13 and 14. Briefs should say: if the source does not describe the review step, write "Not described".
5. **Maturity "in-production" based on unnamed users.** Briefs should repeat the vocabulary rule that in-production needs a named organization.
6. **Point-in-time facts extended to the present** (PE ownership "since 2022"). Briefs should require the source's date to travel with the claim.
7. **Regulatory thresholds taken from marketing pages.** Metz states an outdated audit-requirement rule. Briefs should require a regulator or professional-body source for legal thresholds.
8. **Blocked primaries left as search-only.** Both 403 sources opened through r.jina.ai. Briefs should name the mirror as the first fallback before settling for search-only.
9. **Ref keys named after the wrong publisher** (EBSA-AUDITQ-2025 for a Jones & Roth page). A ref key's publisher prefix should match the actual publisher.
10. Shared-ref note, not fixed here: BORYSOFF-PE-2024 names "The Accounting Review" as publisher, but the document is a registered-report proposal hosted on a GWU site. The ref is shared with quality-management.yaml, so it should be corrected there and here at the same time.
