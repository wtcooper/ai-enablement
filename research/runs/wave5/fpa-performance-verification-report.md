# Verification report: advisory / fpa-performance

Checked 2026-10-21 against the sources themselves. Files edited in place:

- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/fpa-performance.yaml`
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/fpa-performance.md`

I opened all 53 sources cited in the YAML and the 12 sources that only the module cites (65 in all). Most were fetched directly. Others needed a different route:

- The four Gartner pages came through the r.jina.ai browser engine.
- The Armanino, CFGI, Crowe, ISG/PwC and Rillet job pages came through the r.jina.ai mirror.
- The SSRN abstract came from the Crossref record for its DOI.
- The SEC rule text came from the eCFR API.
- The IESBA 606.3 A1 text came from the pronouncement PDF.

I checked the Rillet posting dates against the Ashby job-board API. No web search was used.

## Counts

| Action | Entries |
|---|---|
| Kept | 2 (`-05`, `-14`) |
| Fixed | 12 (`-01`, `-02`, `-03`, `-04`, `-06`, `-07`, `-08`, `-09`, `-10`, `-11`, `-12`, `-13`) |
| Rejected | 0 |

No grade changed. Both B entries rest on named deployments: Creative Planning and Practice Executive using Jirav JIF, and Cox Enterprises in OneStream's private preview. Both come from vendor-published material, and neither has a measured figure from the organisation itself, so neither qualifies for A under the 2026-10-17 rule.

## Final grade mix

| Grade | Count |
|---|---|
| A | 0 |
| B | 2 (14%) |
| C | 11 |
| D | 1 (`-14`, labelled idea) |

**Targets:**

- Use cases: 14 meets the brief's 12–20 range, but `validate.py` applies 15–25 and warns.
- A or B share: 14%, against a target of at least 50%. Not met.
- Every source has a URL and an ISO date ✔. Ids are unique ✔. Vocabulary values are valid ✔. Quotations are under 25 words ✔.
- Cross-references: all 16 named entries exist (assurance-acceptance-independence-15; advisory-risk-controls-17 and -21; advisory-client-accounting-services-06, -07, -08, -20 and -21; professional-services-scoping-pricing-14, -17 and -19; talent-learning-07, -19 and -20; quality-review-04 and -05) ✔.

`validate.py` reports no errors in these files, only the A/B-share warning. Its one error is in `advisory/modules/valuation.md`, which is outside this module.

## Fixes

| Entry / section | What was wrong | Fix |
|---|---|---|
| `-01` solution | Datarails was listed as a CohnReznick reporting tool. JofA lists it under scenario modeling and Excel add-ins; the reporting tools are Reach, Qvinci and Spotlight. | Reworded to the source |
| `-01` role_evolution; module §7 | Intuit "38% of firms prioritise strategic judgment". The survey counts respondents (725 professionals), and the figure is the expertise they prioritise *most*. | Restated |
| `-02` solution | Embellished: "the firm adds its own market intelligence and client knowledge as further forecasts". The source says "more advanced forecasts built with proprietary firm advisory insights can then be added". | Restated to the source |
| `-02` role_evolution | Claim attributed to the wrong speaker: "Jirav's CEO says…". The scaling-without-headcount line is unattributed release text. | Attributed to the release |
| `-02` notes | Contradicted the field: the notes said "Maturity is piloting" while the field says `in-production` | Note now explains why it is in-production (Creative Planning uses it for over 200 clients) |
| `-02`, `-08` source date | GARTNER-FPALEADER-2026 was dated 2026-05-13, which could not be confirmed. The page shows no date, its server timestamp is 2026-09-30, and the text addresses leaders "heading into 2026". | Date set to `2026`; the locator explains why |
| `-03` role_evolution; module §7 | Unsourced connective claim: the Aprio posting does not say budgets and scenarios are "built with AI-enabled templates". It lists modelling duties and, separately, developing AI-enabled workflows. | Split as in the source. The "by 2030" qualifier was added to Gartner's catalysts claim. |
| `-03` prerequisite | The 11% real-time figure was given as near-real-time, which the webinar does not say; the survey blog does | Attributed to the survey release |
| `-04` title, solution, notes; module §3 | Embellished: "agents collect budget inputs… and consolidate submissions". Abacum says its Workflow Intelligence "automates budget input collection, approval routing, and cross-team collaboration". It names agents only for anomaly flagging and model changes, and says nothing about consolidation. | Retitled "…automated inside the planning platform (vendor claim)"; the solution and notes were corrected |
| `-06` problem | Unsourced: "finance staff already use general-purpose assistants outside governed data" | Restated as Abacum's own claim (users wait in the finance queue; context is missing from the tools teams use) |
| `-06` solution | "Byron Patrick ran an ENGAGE session". The source is a schedule published before the event. | Changed to "was scheduled to run" |
| `-07` risk | Unsourced connective claim: "daily finance work is only as good as the model logic, so a change log and reviewer sign-off matter more than speed". It was attributed to CPAPA, which says none of this. | Replaced with what controls 2 and 3 say; carrying them over to model changes is labelled an inference |
| `-07` SSRN source | Access was marked `full`, but SSRN blocks automated access | Locator now records that the abstract was read through the Crossref DOI record (registered 2026-08-16). Figures confirmed: 63/58/42 of 100. |
| `-09` notes; module §5 | Unsourced figure: Kaufman Rossin's sample "(100 decision-makers, December 2025)" is not in the release | Replaced with "sample size and fieldwork dates not stated in the release" |
| `-10` risk | Misstated the rule: the "unless the results will not be subject to audit procedures" exception was applied to management functions too. In Rule 2-01 it qualifies only financial information systems design and implementation, under (c)(4)(ii). Management functions are listed separately under (c)(4)(vi). | Reworded with paragraph cites |
| `-10` risk; module §5 | The 63% was attributed to "in-house finance teams in a March 2026 survey of 204". The release ties the 204-leader survey to its chart. The 63% is a finding of the report card. | Reworded |
| `-11` problem | Unsourced: "on a quarterly cadence" | Changed to "with each product release (Sage Intacct had three 2026 releases by August)" |
| `-12` risks, notes; module §5 | The notes said "later status of the partnerships was not found", but the Rillet page itself was updated 2026-08-25. It still lists Armanino and Wiss, reports 600+ customers, and its FAQ says implementations take 4–6 weeks *led by Rillet's own CPA team* (against 3–12 months). That undercuts reading the speed claim as evidence of partner delivery. | Added; the module metric row now gives both vendor figures |
| `-13` risk | Claim attributed to the wrong section: "production alongside pilots and demonstrations" is from ISG's Executive Summary, not the FP&A Observations | Locators split |
| Module §8 (2026-07-08) | The 15% / 51% agent figures were dated to the survey release but appear only in the webinar (page dated 2026-07-09) | The survey release and the webinar figures are now cited separately |
| Module §8 (2026-09) | Embellished scope: ISG lists outcome-linked commercial structures, and the expansion of managed FP&A and tax, as leading indicators for FAO overall, not "in managed FP&A" | Reworded |
| Module §8 (DCPA) | "Agenda not retrievable", but the page links an agenda | "Agenda not read" |
| Module §9 | Several statements went further than the sources: Datarails "75% of surveyed CFOs" (the sample is CFOs *and finance leaders*); the Fearless Foundry consultant (clients *already* self-prepare, and the risk is being "caught on their heels"); the fractional CFO ("surprised by the lack of desire", not "how little they have") | Each reworded to its source |
| `-01`…`-14` | — | `last_reviewed` set to 2026-10-21 |

Every other figure checked out against its source. Examples:

- KPMG: 40 to 5 people; $100M; 1,013 respondents; 30% to 75%; 64%; 33% vs 6%; 42% and 29%; 71% vs 44%; 36%.
- OneStream: 47%, 32%, 19%, 44%, 39% to 29%, 21%, 12%, 64% vs 35%, 19% / 59%, 35%. Cox Enterprises: 10 minutes to 1 minute, 8 minutes to 30 seconds, 67–98%, and a six-month process.
- Datarails 26%; Intuit 86%, 30%, 41%, 51% and three in five; RSM 53%, 47%, 40% and 88%; S&P Global 72%; Gartner 84% / 4%, 63% and 66%.
- CohnReznick 50–70%; Panorama "more than a quarter"; Deloitte Australia AU$440,000; ISG's EY profile, "thousands of hours into minutes".
- Regulatory and standard-setting text: Rule 2-01 (c)(4)(ii), (vi) and (c)(5); IESBA 606.3 A1 (hosting data); COSO 2026-02-23 and its 17 principles; AICPA's SOC guidance superseding the CPAPA statement; the AIUC full launch in early 2027.

## Sources that could not be reached directly

- Gartner (4 pages): 403 direct; read via the r.jina.ai browser engine.
- SSRN (Vidal): Cloudflare-blocked by every route; the abstract was read via Crossref.
- Armanino (3 pages), CFGI, Crowe and ISG/PwC PDF: 403 direct; read via the r.jina.ai mirror.
- Wayback Machine: unreachable through the proxy.
- Not opened: the 'EY x Rillet Alliance' page linked from Rillet's footer, and the Kaufman Rossin and FP&A Trends full reports (gated).

## Cross-file note (not edited; outside this module)

The same documents carry different refs in different files:

- JOFA-ETHICSAI-2026 (fpa, private-client, transactions, valuation) and JOFA-ETHAI-2026 (client-accounting-services, assurance) are the same document.
- IESBA-TECH-2023 and IESBA-TECHREV-2023 are the same document.

This module uses the majority advisory spelling. One spelling should be standardised across the repository.

SEC-RULE2-01-2026 is dated 2026-10-01 (the eCFR version date) in every file. The section was last amended on 2021-06-09.

## Patterns of error to fix in the briefs

1. **Unsourced connective claims** in risks and role_evolution (`-07` model-logic sentence, `-03` Aprio "AI-enabled templates", `-06` problem). Briefs should require each clause to quote or closely paraphrase a located sentence.
2. **Embellished scope**: "agents" and "consolidate" added to a vendor's "automates" (`-04`); "in managed FP&A" for an FAO-wide indicator; "quarterly cadence".
3. **Wrong speaker or section**: release text attributed to a CEO (`-02`); an Executive Summary sentence cited as FP&A Observations (`-13`).
4. **Statistics restated as something else**: "% of firms" for respondents, "naming forecasting a top use" for usage share, and Rule 2-01's exception extended to a second paragraph.
5. **Dates and sample details not on the page**: the Gartner agenda date and the Kaufman Rossin sample. Briefs should require the date's source (byline, JSON-LD or header) to be recorded in the locator when it is not visible.
6. **Notes contradicting fields** (`-02` maturity). Run a field-versus-notes consistency pass.
7. **Stale "not found" statements**: re-open a page's "last updated" section before claiming no follow-up exists (Rillet).

The grade mix is the module's structural gap. The public record for this module consists of vendor releases, firm service pages and sponsored surveys. Raising the A/B share needs named firm case studies with client results, not rewording.
