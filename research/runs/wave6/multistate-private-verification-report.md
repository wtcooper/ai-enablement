# Verification report: tax / multistate-private (wave 6)

Verified 2026-10-21. Files edited in place:
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/tax/use-cases/multistate-private.yaml`
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/tax/modules/multistate-private.md`

All 39 cited sources were reopened, either directly (curl, pdftotext) or through the r.jina.ai mirror. Dates were checked
against `datePublished`, `article:published_time` or the document's own date line. `scripts/validate.py` reports
0 errors. The only warning for this file is the known below-target A/B share.

## Counts

| Action | Entries |
|---|---|
| Kept | 2 (`#06`, `#12`) |
| Fixed | 12 (`#01`–`#05`, `#07`–`#11`, `#13`, `#14`) |
| Rejected | 0 |

No grade changed. Every fix corrects wording, a date, a publisher or a cross-reference. None of the issues found
supported a higher or lower grade.

## Final grade mix

**0 A, 1 B, 9 C, 4 D** (14 entries). That puts 7% at A or B.

## The Vals P-004 question (flagged by synthesis)

I read the live page `https://www.vals.ai/benchmarks/tax_agent_bench` on 2026-10-21 (published 2026-10-20 23:26 GMT).
For the 18 models traced on public question P-004 (New York versus California PTET credit, tax year 2025), one
paragraph states all of the following:
- Grok 4.6 passes all 18 checks.
- Claude Fable 5.1, the overall leader, scores 91%.
- Muse Spark 1.3 scores 79.4%.
- Kimi K3, GPT-5.6 Luna and GPT 5.5 score 76.5% each.
- The remaining twelve score 0. Eleven of them fail the same must-pass check: how New York treats PTET credits from
  more than one electing entity.

**There is no conflict.** `tax-research-advisory-04` ("twelve of eighteen scored 0") and `#07` (91%, 76.5%, one
passing all checks) quote different parts of the same result.

What I changed:
- `#07` now gives the full distribution.
- `#07` now says the per-question scores are illustrative and outside the leaderboard. Failing a must-pass check
  scores 0; otherwise the model gets partial credit, which is consistent with Weighted Pass.
- The headline 49.19% is now described correctly as the share of questions answered fully correctly
  (citation-adjusted), not an "average score".

One discrepancy remains: the ref date is 2026-10-16 in `sources.md` and `research-advisory.yaml`, and 2026-10-20 here
(the live page's date). Research-advisory was not edited. The coordinator should align the ref date when that module's
widening is finished.

## Fixes

| Entry / section | Fix | Reason |
|---|---|---|
| `#01` problem | Ref for "few tools to challenge selection" moved from TAXNOTES-UNWATCHED-2026 to NTT-BIAS-2026 | The TaxProf excerpt does not say this; the podcast transcript does (wrong document) |
| `#01` risk, module §6 | "Experts... warn of opaque algorithms" split by source: Bruckner (one expert) on human oversight and discriminatory outcomes; "opaque algorithms" attributed to Kogod's summary | The Post and Courier quotes one expert and never says "opaque"; plural and qualifier were embellished |
| `#01` notes | The Route Fifty item was relabelled from "search-snippet-only" to opened (ROUTEFIFTY-REV-2026). Added a note that the Post and Courier page has two timestamps | The source was in fact opened (`#12`). Date checked: datePublished 2026-04-12 kept |
| `#02` problem | Removed "payroll" from the data states connect | Neither STI nor The Sales Tax People mentions payroll |
| `#02` risk | Added that the consultancy blog's inline citations link to unrelated gas-price and grocery-tax articles | Its factual claims cannot be traced; this matters because `#02`, `#09` and `#11` lean on it |
| `#02` notes | Named the webinar instructors (FTA COO Ryan Minnick, Diane Yetter) | Context for how much weight the listing carries; grade unchanged (C) |
| `#03` solution, source | Publisher corrected to Business Insider (syndicated on Yahoo), summarising CNBC; recipients worded as the source words them; CNBC 403 noted | Wrong publisher attribution |
| `#03` role_evolution | "Ties higher audit volume to fewer auditors" changed to say the source calls the staffing link unclear | Embellished cause |
| `#04` notes | The Truss listing does state the session date (Thu 17 Sep, 1-2 pm ET) | The note wrongly said the listing has no date |
| `#04` solution | Mercor's topic list split between topics assessed and expertise sought. Added Thomson Reuters' CoCounsel Tax nexus templates (TRFORD-SALT-2026) | Precision; a better firm-side source |
| `#04` role_evolution, module §7 | "AI developers recruit..." reworded as Mercor recruiting for AI labs; module topic list corrected | Nonresident withholding and composite filing are expertise requirements, not grading topics |
| `#05` problem, solution | Added refs to the unsourced "before payroll can run" sentence; Warp's claim now names its AI agents as the source states | An unsourced connective claim |
| `#07` outcomes, notes, locator | Full P-004 distribution; corrected the headline metric definition; recorded the live-page check | See the Vals section above |
| `#08` solution | "AT&T, EY, Reed Smith and others" changed to "AT&T, EY and Reed Smith" | The Part 3 presenters are only these three |
| `#09` solution, prerequisites, risk | Removed "payroll registrations with no matching sales tax account" and payroll from the prerequisites; the disclosure-eligibility risk is now labelled inferred | Not in the source (unsourced connective claim) |
| `#10` risk | 23 Sep 2026 is the session date, not the page's publication date | Wrong date type |
| `#10` notes | "tax-\ncontroversy" (broken across a line) changed to "the controversy module" | The folded YAML rendered as "tax- controversy" |
| `#11` problem, module §2 and §6 | "Usually requires no prior contact; registering first can lose eligibility" replaced with the consultancy's actual claim: the window closes once a state opens an audit, with a two-to-four-year lookback | Overstated beyond the source |
| `#11` solution | Added the missing ref (MTC-NEXUSDIR-2026) | Unsourced sentence |
| `#11` role_evolution | MTC Joint Audit Program staffing is now marked as not linked to AI or to disclosure work | Unsourced connective implication in role_evolution |
| `#13` source, solution, notes | Webinar date corrected from 2025-08 to 2025-08-14; URL updated to the Baker Tilly page the Moss Adams link redirects to; title and topics taken from the page | Wrong date precision, and the URL redirects |
| `#14` problem | "Generic calculators handle W-2 cases only" changed to "Gelt says most online calculators are built for simple W-2 scenarios" | Embellished qualifier ("only") |
| `#14` risk | "State-by-state answers are where models do worst" replaced with the one-question fact | A single benchmark item cannot support a general claim |
| `#14` notes | Provisional cross-reference `tax-research-advisory-new-01` replaced with `tax-research-advisory-26`, which now holds the S-election and PTET calculator entry | The cross-reference named an entry that does not exist |
| Module §5 | Vals rows rewritten | Matches the live page |
| Module §6 | Added that OPR Alert 2026-19 notes general AI laws in California, Colorado, Illinois and Utah (not tax-practice rules) | Completeness of the "no state guidance" statement |
| Module §7, §9, §10 | "An academic" changed to "a Tax Notes State author"; "abstract only" changed to "excerpt" | The TaxProf page gives no affiliation for Michael V. Sala and quotes more than the abstract |
| Module §8 | Akerman row reworded as the session date | Wrong date type |
| Module §10 | FTA podcast URL now points to the episode page (2938194), which confirms 2026-06-23 | The episode date was verified |

The remaining cross-references were checked and exist: `tax-controversy-01`, `-14`, `-15`, `-20`; `tax-indirect-tax-13`;
`tax-compliance-corporate-06`, `-12`, `-13`; `tax-research-advisory-01`, `-04`, `-08`, `-23`, `-26`.

## Sources that could not be reached

- CNBC original (cnbc.com, 2024-04-15): HTTP 403. `#03` relies on the Business Insider summary and stays at C.
- gusto.com press page: 403 on direct fetch. It was read via the mirror, and the date was confirmed by the Fintech
  Global coverage (2026-04-13).
- The r.jina.ai mirror rate-limited some requests. Those pages (Akerman, Eide Bailly, Gelt, TaxProf) were fetched
  directly instead.

No source was unreachable by every route.

## Targets

| Target | Status |
|---|---|
| 12–20 use cases | Met (14) |
| At least 50% graded A or B | **Not met** (1 of 14, 7%). This is structural: no firm, PE platform or in-house team has published a multistate AI deployment |
| Every source dated | Met. All YAML sources and the module §10 keys carry ISO dates. FILED-HOME-2026 uses the access date because the page is undated |

## Error patterns to fix in the briefs

1. **Low-quality secondary pages taken at face value.** The Sales Tax People blog cites gas-price articles for
   enforcement claims. Briefs should ask researchers to click through a page's own citations before relying on it.
2. **Embellished qualifiers and plurals.** Examples: "experts" for one expert, "only" for "most", "usually requires no
   prior contact" for "closes once an audit opens". Briefs should require quoting the source's own qualifier.
3. **Unsourced connective claims** in risks, prerequisites and role_evolution. Examples: the payroll-registration check,
   the MTC staffing line.
4. **Date type confusion.** Event or session dates were recorded as publication dates (Akerman), and a listing's stated
   session date was missed (Truss). Briefs should name which date is being recorded.
5. **Partial quotation of a benchmark.** Two modules quoted different halves of the same Vals paragraph, and synthesis
   read that as a conflict. Briefs should ask for the full distribution and the metric's definition (all-pass versus
   partial credit).
6. **Wrong publisher for syndicated content** (Yahoo for Business Insider) and **stale URLs after a merger** (Moss Adams
   now redirects to Baker Tilly).
7. **Provisional ids left in cross-references** after the receiving module has assigned a final id.
