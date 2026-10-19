# Verification report: professional-services / work-production

Checked 2026-10-19 against the sources themselves (r.jina.ai mirror, direct fetch, pdftotext; no web search used).
Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/work-production.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/work-production.md`

All 97 distinct source URLs in the two files were opened. Every figure in an A or B entry was matched to the source
text.

## Counts

| Action | Entries |
|---|---|
| Kept | 3 (`-10`, `-18`, `-20`) |
| Fixed | 22 (all others) |
| Rejected | 0 |

Most fixes are wording, figures, attribution or dates. One grade changed: `-08` went from A to B.

## Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 3 | 2 (`-06`, `-07`) |
| B | 15 | 16 |
| C | 5 | 5 |
| D | 2 | 2 (both labelled "Idea") |

## Fixes and rejections

Ids are shortened: `-08` means `professional-services-work-production-08`.

| Id | Field | Change | Reason |
|---|---|---|---|
| `-01` | outcomes (Schwarcz) | "count of citations to fabricated sources" changed to "number of assignments containing at least one fabricated citation" | Figure 7 of the paper counts assignments with a hallucination, not citations (statistic reported as something it doesn't measure) |
| `-01` | outcomes (Stanford) | "202 queries per the governance deep dive" now cites the paper | The paper's limitations section gives the 202 figure; the claim now rests on the source, not on a deep dive |
| `-01` | prerequisites (ILTA) | "55% to 60% of larger firms" changed to show all bands: 25% / 40-42% / 55-60% | The wording hid the 40-42% mid-size bands |
| `-01` | role_evolution | Cal Bar sentence rewritten; opening claim now cites EWHC-AYINDE-2025 | "Duty to supervise extends to AI output used by subordinates" overstated the guidance. The opening claim had no source |
| `-01`, `-03`, `-05`, `-22`, `-25` | ILTA source date | `2026-06` changed to `2026` | The PDF has no publication date and its metadata shows creation on 2026-08-14. Nothing supports June |
| `-02` | risks, checkpoints | Grant Thornton "checks translations and summaries" changed to "checks translations" | The source describes a quality check of translations only |
| `-02` | role_evolution | "Litigation teams are shifting" changed to "an ILTACON observer said... are beginning to focus" | Embellished, and the observer was not named |
| `-03` | risks | "governing law" changed to "governing rules" | Harvey's wording |
| `-04` | solution, sources | Harvey Horizon Scanning claim now cites HARVEY-HLC-2026 (site navigation) | The claim had no source |
| `-04` | risks | Reference to an internal deep dive removed; recast as "no source tests alert quality" | A connective claim with no source |
| `-05` | solution, locator | Litera: "first drafts from precedent in its Lito agent" changed to "precedent search in Litera Create Content" | Wrong product: the release puts precedent in Create Content, not Lito |
| `-06`, `-10` | NBER date | `2026-09` changed to `2026-09-03` | NBER revision date |
| `-07` | solution | ILTACON sessions "recommended" changed to session abstracts "describe" | The source is a set of session abstracts, not recommendations |
| `-08` | evidence_grade | A changed to B | Microsoft's 70%-kept figure is vendor telemetry about its own product across unnamed users, and it measures acceptance, not quality. The named deployments (Microsoft legal, GE Aerospace) report only one lawyer's estimate (grade inflated) |
| `-08` | outcomes, risks | Ivo benchmark "vendor-commissioned" changed to "vendor-designed (Ivo calls it independent)" | Ivo's CEO says "we designed this benchmark" |
| `-08` | checkpoints, role_evolution | Checkpoint now uses Microsoft's own words. Removed "first-pass reviewer becomes approver and playbook owner" | That sentence had no source |
| `-08` | LegalOn date | `2026-06-03` changed to `2026`, with a note that it was out by 2026-06-22 | The page has no date |
| `-09` | solution | "O'Melveny partners check prior loans" changed to "a real estate partner checks the lender's last 100 loans". The litigator is named by role | One partner, not partners. The source gives the 100-loan detail |
| `-11` | outcomes (Deloitte) | "The department found incorrect footnotes" changed to "a researcher flagged them and Deloitte confirmed" | Wrong actor: Deloitte, not the department, confirmed the errors |
| `-11` | outcomes (Charlotin) | Added a note that the database includes some decisions where AI use was alleged but not confirmed | The database's own scope note says so |
| `-12` | role_evolution | Removed "junior diligence hours are the work most often cited as compressed". Replaced with O'Melveny's sourced lease-abstract statement | A connective claim with no source |
| `-13` | notes | Noted that the `automate` ladder is inferred | Accounting Today does not say whether people review each agent output |
| `-14` | problem, outcomes, notes | "Chat tools read only a fraction" changed to "a standard agent tool loop read under 1%". "Post-training raised the pass rate further" now names the one model. The 1-4% figure is credited to EY | Wrong comparison, an embellished qualifier, and the 1-4% figure came from EY, not Harvey |
| `-15` | locator | The Law Society "glossary definition" locator is now the agentic AI section | The page has no glossary entry |
| `-16` | solution | "Three providers" changed to four, adding Google's Gemini Enterprise for Legal (2026-08-25). The settlement-proposal example is now credited to Peter Lee (Simmons & Simmons) in a Law Society article | The list was incomplete, and the example was credited to the wrong speaker |
| `-16` | notes | Date note updated: the page shows 19 Oct 2026 | The date was confirmed |
| `-17` | risks, role_evolution, sources | Robert Walters posting removed. "Output quality limited by playbook quality" changed to "no source measures this" | The posting could not be reached (403). The connective claim had no source |
| `-19` | outcomes, risks | RSGI now described as a survey of Harvey's own customers | The sample was Harvey customers only, which was not disclosed |
| `-21` | solution, role_evolution, provenance | Kirkland "first tool... fund formation engine" changed to "a private-funds tool with Palantir". The Vault quote is marked as from Axios. Bloomberg provenance changed to independent | Embellishment, credit to the original source, and the vocabulary |
| `-22` | risks | "Free or consumer tools may reuse inputs" changed to Cal Bar's actual point, plus the ABA's self-learning point | Embellished qualifier: Cal Bar does not limit this to free or consumer tools |
| `-23` | outcomes | "One kept a higher false-positive rate" changed to "for issues 5 and 6, round four slightly raised false positives" | The figure was wrong |
| `-23` | risks, solution, role_evolution, notes | Covington "not defensibility-grade validation of recall" now paraphrases the author accurately. Robert Walters posting removed. "Evaluators with a method" framing removed | Mismatch with the author's words, an unreachable source, and a claim with no source |
| `-24` | role_evolution | "Quality, knowledge and innovation teams gain a measurement role" changed to TRI's sourced point plus "no source names which team owns it" | A connective claim with no source |
| `-25` | risks, role_evolution | DLA Piper "same inbox" was the writer's phrase, so it is no longer credited to Blair. The unsourced record-keeping sentence is replaced with ICMCI s.3.6 | Wrong speaker, and a claim with no source |
| Module | header | Grade counts updated to A 2, B 16 | Follows the `-08` downgrade |
| Module | §3, §5, §7, §9 | Six changes, listed after this table | The YAML fixes above and the source checks |
| Module | §5, §9 | Stanford "hallucination" definition corrected. GDPval 47.6% added. SPI's "the leak" restated | SPI's term means time saved but not turned into revenue, not "not resold or repriced" |

The six module changes in §3, §5, §7 and §9:

- The 70%-kept figure is labelled as vendor telemetry.
- Google is added to the `#16` list of providers.
- Kirkland is described as "emphasising exclusivity".
- The RSGI figures are labelled as a survey of Harvey customers.
- The Robert Walters "London firm" posting is removed.
- The "peak legal tech" line is restated. LawSites meant peak energy, not a sign that the hype is fading.

## Sources that could not be reached

- RW-LEGALENGINEER-2026 (Robert Walters posting). It returned 403 directly and a bot wall through the mirror.
  It is removed from `-17`, `-23` and the module. The PwC Legal posting, which was verified, carries the same claims.
- ABA-OP512-2024 at americanbar.org returned 403. It was verified in full from the LawNext-hosted copy
  (`lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf`).
- The first fetch of LEGALIT-LEGALGEEK-2026 hit a bot wall. A mirror retry with a timeout worked, and the 19% Copilot
  figure and the Dentsu figures were confirmed.
- The mirror blocked arXiv (Stanford, GDPval). Direct PDF fetches worked.
- Dates that could not be confirmed from the page:
  - The PwC Legal posting (2026-09-16).
  - The Legora customer and newsroom pages: Goodwin, MinterEllison, Crowell, Hogan Lovells Cadwalader, Laurel. These
    use the Legora "joined" label or the date of the deep dive's read.
  - The Accounting Today podcast, dated to the year only.
  - The Cal Bar guidance PDF has no date. Its metadata (2026-05-15) is consistent with the 2026-05-14 approval date.

## Module targets

| Target | Result |
|---|---|
| 15-25 use cases | 25: met |
| At least 50% graded A or B | 18 of 25 (72%): met |
| Every source dated | Yes. Some dates are year-only or label-based, as listed above |
| Validator | `scripts/validate.py` reports 0 errors in these files. The one error in the run is in `modules/client-development.md` (313 lines), which is outside this brief |

## Cross-module issues for the coordinator

- **ILTA-TECHSURVEY-2026** is dated `2026-06` in other professional-services files (acceptance-risk,
  client-development, delivery-management, firm-finance and others). The PDF has no date and was created on
  2026-08-14. This module now uses `2026`. Align the date across files.
- **LEGALIT-RSGI-2026** describes a survey of Harvey customers only. Check how other modules describe it.

## Error patterns to fix in the briefs

1. **A statistic reported as something it doesn't measure:**
   - Schwarcz counts assignments, not citations.
   - ILTA's size bands were collapsed into "larger firms".
   - RSGI's sample frame (Harvey customers) was not disclosed.
2. **Embellished qualifiers or details:**
   - "Free or consumer tools".
   - "Partners check prior loans".
   - "Teams are shifting".
   - "Chat tools".
   - "Raised further".
   - Kirkland's "first tool... fund formation engine".
   - The Litera product name.
3. **A claim credited to the wrong speaker or document:**
   - The Law Society article example came from a guest, not the Law Society.
   - A journalist's phrase was credited to a panellist.
   - Vault was quoting Axios.
   - Harvey was citing EY.
   - The Deloitte actor was wrong.
4. **Unsourced connective claims:** in `role_evolution` for `-01`, `-08`, `-12`, `-23`, `-24` and `-25`, and in
   `risks_and_guardrails` for `-04` and `-17`. Ask briefs to require a source ref on every sentence in these fields,
   or to label the sentence "inference".
5. **A grade inflated by vendor telemetry:** a vendor's usage metric about its own product (`-08`) was treated as
   a named organization's measured outcome. Add to the grade rule that vendor-reported product telemetry is grade C
   evidence on its own.
6. **Dates:**
   - Month-level dates were taken from file names (ILTA) or search snippets (LegalOn) rather than the page.
   - Ask for the PDF metadata or the page byline, and use year-only dates when neither is available.
7. **Incomplete lists:** "three providers" left out Google, although the cited LawSites article names four.
8. **Search-only figures in A or B entries:** none found. Every source in this module was read in full.
