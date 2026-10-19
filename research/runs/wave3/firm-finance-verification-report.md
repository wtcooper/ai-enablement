# Verification report: professional-services / firm-finance

Checked 2026-10-19 against the sources themselves. Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/firm-finance.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/firm-finance.md`

I opened all 85 distinct sources cited in the YAML and the 10 sources cited only by the module, either directly or, for Clio and the CTV body, through the r.jina.ai mirror. I also downloaded two further documents to settle claims: the Law Society's full agentic-AI report (PDF) and the CTV article body. I used no web searches.

## Counts

| Action | Entries |
|---|---|
| Kept | 1 (`-15`) |
| Fixed | 16 (`-01` to `-14`, `-16`, `-17`) |
| Rejected | 0 |

No source was missing, and every cited figure was found in its source. No grade changed:

- No entry claims grade A. Tonkon Torp (`-03`) is the closest candidate. Its managing partner refers to the firm's own analysis, but the figures appear in Laurel's text. Under the 2026-10-17 rule the entry stays B, and it now says why.
- Every B entry rests on a named organization in a source read in full.

## Final grade mix

| Grade | Count |
|---|---|
| A | 0 |
| B | 9 (53%) |
| C | 7 |
| D | 1 (`-14`, labelled idea) |

Targets:

- Use cases: 17 (target 15–25). Met.
- Graded A or B: 53% (target at least 50%). Met.
- Every source has a URL and an ISO date. Met. The module's 10 starred sources now carry their URLs too.
- Ids are unique.
- All quotations are under 25 words.
- `validate.py` reports 0 errors. firm-finance is INFO-level only: 17 use cases, 53% A/B. The module is exactly 300 lines.
- All 25 cross-referenced ids exist and match the topics described. These are the scoping-pricing, tax and assurance ids.

## Fixes and rejections

| Entry / section | What was wrong | Fix |
|---|---|---|
| `-01` solution, source title, notes | The Bloomberg Law opinion was described as by "an unnamed general counsel". It is signed by Tim Robb, GC of World Insurance Associates. | Named him |
| `-01` outcome (Clio) | "Survey of over 1,700 respondents" is not on the cited blog page | Removed; sample size marked as not stated |
| `-01` notes | Resultsense says roughly a third of McKinsey's *work* is tied to performance fees. The entry presented it as the fee share. | Reworded and marked as a different measure |
| `-02` problem; module §5 | The 2.7% demand growth is the overall market, but it read as Am Law 100 | Now "overall demand" |
| `-02` solution | Embellished: TRI's forum account does not "describe pricing teams that use AI". One executive said more firms *will need* them. | Reworded to the source |
| `-03` outcome | Said the page does not attribute the figures to a firm analysis, but Tonkon Torp's managing partner cites the firm's own analytical work | Corrected; the B grade is explained |
| `-03` outcome | "508 firms": LawSites says "over 500" | Corrected |
| `-03` dates | The Tonkon Torp and Warren Averett pages were dated `2026-10` as undated, but JSON-LD gives 2026-08-21 | Dated 2026-08-21, with a note that this may be a site republish |
| `-04` role_evolution | Unsourced connective claim: "review flagged exceptions across all lines rather than sampled invoices" | Replaced with the CEO's sourced statement about plain-language queries |
| `-04` outcome | The four bankruptcy cases are listed by the article, not "cited by the CEO" | Corrected |
| `-05` date | Aderant page dated `2026-10` as undated; JSON-LD gives 2026-08-24 | Corrected |
| `-06` date | LEXIS-FORRESTER-2025 was dated `2026-09`. The post was published 2025-05-13; the Forrester study is May 2025. | Corrected |
| `-06` role_evolution | The 2.5-hours finding is Forrester's model, as summarized by LexisNexis, not a LexisNexis statement | Attributed correctly |
| `-07` problem | Few firms formally measuring AI gains is a Blickstein survey finding, not something COOs said | Attributed to the survey |
| `-07` role_evolution | Embellished: "vendors offering to help firms calculate ROI". A panelist urged teams to press vendors on it. | Reworded |
| `-07`, `-13` TR-FOP-2026 date | Dated `2026-09`, but TRI called the report "recent" on 2026-07-21. The page's 2026-10-16 timestamp is a republish. | Set to `2026`, with the reasoning in the locator |
| `-08` role_evolution | Generalized to "enterprise applications and innovation staff own adoption metrics" | Restated as Holland & Hart's practice (early access for respected adopters) |
| `-09` problem and solution | Embellished: "decide before rollout", "a lower price". SPI says to plan how to reprice or resell saved hours, and to tie AI to utilization, margin, revenue per employee and EBITDA. | Reworded to the source |
| `-10` solution and outcome | Attributed to the wrong document: "more than $100 million in year one" and "multi-year" come from the FT via AI Weekly, not Bloomberg Law | Split by source; the FT figure is marked as read only through the summary |
| `-11` risk; module §9 | "You cannot tell a client you ran out of tokens" was shown as a direct quote. TRI paraphrases it. | Paraphrased |
| `-11` risk; module §9 | Artificial Lawyer's argument that lawyers will choose the costlier model was stated as fact | Attributed as Artificial Lawyer's argument |
| `-11` role_evolution | Attributed to the wrong speaker: "restraint is harder than adoption" is TRI's writer, not a speaker | Corrected |
| `-12` risk | Ballard Spahr "a line item you can trace…" was shown as a direct quote; it is TRI's paraphrase | Paraphrased |
| `-12` solution; module §6 | "Illinois State Bar newsletter opinion" reads as a bar ruling. It is Carolyn Elefant's practitioner opinion in an ISBA section newsletter. | Clarified |
| `-12` notes | Said Law360 was read only as a headline | Opening paragraphs now read and confirmed |
| `-13` risk; module §6 | "From 2 December 2027 … is high-risk" misstates the timeline. Employment AI is a high-risk use; obligations apply from that date. | Corrected |
| `-13` role_evolution; module §7 | "IPA expects partner tracks": IPA says the fastest-moving firms *are expanding* them | Corrected |
| `-13` EC-AIACT-2026 date | `2026-07-27` is the AI Omnibus entry-into-force date, not the page date | Set to the read date 2026-10-19, matching the 8 other files that cite it |
| `-14` problem | "DLA Piper's AI head": Barclay Blair is Senior Managing Director of AI Innovation | Corrected |
| `-14` risks | Unsourced connective claims: "leverage rose before any measured AI effect" and "this bears on the supply of future partners" | Replaced with TRI's open question and the NBER authors' own conclusion |
| `-14` locator | The Law Society report was cited at pp. 57 and 59. The text is on p. 53 (synopsis) and p. 58 (firm-type impact). | Corrected after reading the full PDF |
| `-16` problem; module §6 | Embellished: "pay out nearly all profit" and Rule 5.4 as "the main barrier". Sources say little cash is left once partners are paid, and that Rule 5.4 bars fee-sharing and partnerships with non-lawyers. | Reworded |
| `-17` prerequisite and checkpoint | Embellished: "experienced lawyers review and take responsibility for agent work". The episode summary says only that the firm depends on highly experienced lawyers. | Reworded; the checkpoint is labelled as a recommendation |
| Module §3 | "$500 million commitment with Palantir": the commitment is Kirkland's own, and Palantir is one partner | Reworded |
| Module §7 | Unsourced connective claim: "in-house legal ops is the first line for AI pressure". The TRI figure is GCs naming technology "a strategic priority". | Reworded to the source |
| Module §9 | The 32% figure is clients reconsidering providers "falling behind" | Qualifier added |
| Module §10 | The 10 module-only sources had no URLs | URLs added. All 10 were opened and their figures confirmed: BigHand 96/89/90/46%, Deltek 38%, Citi 4.2% against about 1.5%, TRI 85%/75%, LFFI 61/7.1% and 5.3%/9.8%, LDOR doubling, Celeste pricing playbook, and the 21–22 Oct forum. |

**Spot-confirmed without change (sample):**

- McKinsey "about a quarter" and the strategy share under 20%
- Keypoint hybrid pricing
- Stanford Rule 3 and Rule 4
- California p. 8 (PDF dated 2026-05-15)
- Texas Opinion 705
- The full Legal Decoder article
- Laurel Signal and Work Studio statements
- PwC $3 billion and 330,000 trained
- RSM $1 billion; KPMG Copilot tracking
- TR AI in Professional Services 18% and 40%
- Holland & Hart 70% weekly active users and eight weeks
- Kirkland 180+, 50, 250 and 40 openings
- ILTACON meter details: $2 PowerPoint, 1% of revenue, tool counts
- Baker Donelson "ten of the last 13 months"
- Harvey 14x; Legora controls
- Crowe/KKR and CroweONE
- ICAEW 86% of 35
- AICPA comments due 30 April
- WSHB multiples and state rules
- Arizona 114, 51 and 47
- General Legal about 400 clients
- Norm Law, Arceus and Falcon
- Ascend's 30-person AI team

## Sources that could not be reached

- None is fully unreachable.
- **CLIO-SOLO-2026** returned 403 directly; it was read through the mirror.
- **CTV-DELOITTE-2025**: only the page shell loaded directly. The body, including AUD 440,000, was read through the mirror.
- **Partial reads:**
  - The Bloomberg Law pages (Kirkland, Texas, billable opinion, GC x AI) were read in their visible, pre-paywall portion. Every cited claim sits in that portion.
  - SPI's full report is paid; only the landing page was read, as the entry already says.
- **Unresolved date: ILTA-TECHSURVEY-2026.** It is kept at `2026-06` for consistency with 9 other files. As the scoping-pricing report noted, the PDF metadata says 2026-08.
- **Cross-file date conflicts for the coordinator to settle:**
  - TR-FOP-2026 is dated `2026`, `2026-07-21` and `2026-09` across files. I recommend `2026`.
  - EC-AIACT-2026 uses three dates across files.

## Error patterns to fix in the briefs

1. **Paraphrase shown as quotation.** Three times (`-11`, `-12`, module §9), wording that TRI paraphrased was put in quotation marks as a speaker's words. Rule: quote only text inside quotation marks in the source.
2. **Attributed to the wrong document or speaker.** The FT's year-one figure was credited to Bloomberg Law. The author's line about restraint was credited to a speaker. Forrester's model was credited to LexisNexis. Rule: when a figure comes from a secondary summary of another outlet, cite the document that was actually read and name the original.
3. **Embellished qualifiers.** Examples: "main barrier", "nearly all profit", "AI head", "expects", "decide before rollout", "review and take responsibility". Rule: use the source's own verb and title.
4. **Dates taken from retrieval month or a republish timestamp** when a better date existed: JSON-LD on Laurel and Aderant, the Lexis post and the TRI FOP report. Rule: check JSON-LD datePublished and in-page dates first, and treat a "last published" stamp on a living page as a republish.
5. **Unsourced connective claims in `risks_and_guardrails` and `role_evolution`** (`-04`, `-14`, module §7). Each sentence needs its own source or must be labelled an inference.
6. **Regulatory timelines compressed.** "High-risk from 2 December 2027" conflated classification with the date obligations apply. A practitioner's opinion in a bar newsletter read as a bar position. Rule: say who issued a statement and what legal force it has.
7. **Opinion stated as fact.** Artificial Lawyer's argument about model choice was presented as observed behaviour.
