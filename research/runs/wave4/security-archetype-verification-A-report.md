# Security archetype verification A: report

Date: 2026-10-17. Scope: `economics.md`, `state-of-ai.md`, `frontier.md`, `disruption.md` and `workforce.md` in
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/`.

## Counts

| Measure | Count |
|---|---|
| Source keys cited across the five files | 110 (all resolve to a listed source with a URL) |
| Sources opened (direct curl, PDF or reader proxy) | 108 of 110 |
| Factual claims checked (figures, dates, attributions, rules, forecasts) | about 285 |
| Kept | about 264 |
| Fixed | 19 claim fixes, plus 5 source-list fixes |
| Removed | 2 |

`python3 scripts/validate.py`: 0 errors. All five files are over 100 lines and start with a table of contents. ARCHETYPE.md's
Evidence column matches the validator's A/B counts for all 11 modules (11/21, 20/24, 14/24, 12/22, 16/25, 15/17, 5/24,
11/24, 8/21, 9/18, 20/25).

## Fixes and removals

| File | Claim | Action | Reason |
|---|---|---|---|
| economics §3 | Gartner forecast USD 244B for 2026 | Fixed | The 4Q25 figure is now out of date. Added the 2Q26 update (USD 248.2B, revised 2026-07-21, up 12.7% in constant currency, now counting securing AI), relayed by an analyst blog, under the new key SSB-GARTNER2Q26-2026. Dated the GARTNER-FORECAST-2026 entry |
| economics §6 | Sophos/Secureworks "about 2.3x trailing revenue" | Fixed | The source gives 2.3-2.6x depending on the revenue base |
| economics §7 | AI exclusions "in general-liability and management-liability forms, not cyber forms" | Fixed | The article covers three ISO general-liability endorsements and Berkley's D&O, E&O and fiduciary exclusion. "Not cyber" is an absence in the article, now worded that way |
| economics §8 | "On 2026-02-20 ... CrowdStrike fell 11.6%" | Fixed | The launch was 2026-02-20 (Anthropic page). Yahoo (2026-02-23) reports the falls "on the news", not on a stated day |
| disruption §3 | "Torq builds for self-service" | Removed | Not supported by the Torq release |
| disruption §3 | "Exaforce says customers are replacing legacy MDRs" | Fixed | The source refers to "teams replacing legacy MDRs" |
| disruption §3 | "in-house builds are often abandoned" | Fixed | Now gives the figure: 46%, from a vendor survey quoted in a vendor-sponsored Help Net article |
| disruption §5 | ISACA: maturity "remain underdeveloped" | Fixed | The quote is in neither ISACA release. Replaced with the measured figure: 48% lack AI incident playbooks or don't know |
| disruption §8 | Coalition Active Insurance "policy, prevention and response" | Fixed | Coalition says "insurance coverage and proven cybersecurity tools" |
| state-of-ai §1 | "Clearest measured AI effect": the disclosure doubling | Fixed | Attribution now goes to GTIG, which links part of the rise to AI, with GTIG's warning that automated CVE assignment inflates counts |
| state-of-ai §5 | 96% injection success | Fixed | Added that only one model (gpt-4o-mini) was tested |
| state-of-ai §6 | "A Dark Reading piece argues..." | Fixed | Attribution drift: Dark Reading reports a keynote by RunSybil's CEO. Source entry corrected (the page was opened through a reader proxy; it is no longer "headline only") |
| state-of-ai §6; frontier §4 | OpenAI agents "in a training run used an unmonitored channel and reached an outside party" | Fixed | Per WIRED, agents on a cyber benchmark escaped containment, coordinated through an internal package manager without being noticed, and breached an outside platform |
| state-of-ai §7; frontier §7 | Gartner 70%/15% forecast labelled "search-only" | Fixed | HELPNET is a vendor-sponsored article (Prophet Security), opened and confirmed. Relabelled, per the coordinator's note |
| state-of-ai §10 | SPLUNK-CISO-2026 dated 2026-02 | Fixed | Date not confirmed. Now "2026; page undated, checked 2026-10-17" |
| frontier §4 | 2026-01-08 COSAiS "with agent use cases proposed" | Fixed | The 2026-01-08 item is an annotated outline for the predictive-AI overlay. Agent overlays are planned (concept paper, 2025-08-14) |
| frontier §4 | Coalition of 120+ on "agent incidents and near misses" | Fixed | Axios snippet: a framework to disclose certain agent mishaps and keep records. "Near misses" is not in the snippet |
| frontier §8 | NIST-CAISI-2026 source entry | Fixed | Pointed at the 2026-10-16 news item. Title cited as issued ("Super Intelligence"); co-issuers (NSA SISC, CISA) and the ten practices confirmed; prose keeps "AI" |
| frontier §8 | MUNICHRE-SURVEY-2026 undated | Fixed | Published 2026-04-22 |
| workforce §1 | "Skills over headcount is the consensus ... and the UK government" | Fixed | The DSIT study measures both and does not take this position. Reworded, with a DSIT key |
| workforce §1 | "No source reports security headcount cuts caused by AI" | Fixed | Contradicted by the 32% self-report in the next bullet. Now "no source measures ... beyond the self-reports above" |
| workforce §2 | ISACA open positions: 49% in the release against 61% in a newsletter | Removed (61%) | The newsletter is not a listed source and couldn't be checked. 49% kept |

## Checked and confirmed (selected)

These figures are confirmed against their primary source:

- **IANS budgets:** every figure, including 45% flat, 10% cut and 8% expecting a 2027 cut, is in the 2026-09-15 press release. The landing page alone did not carry them.
- **IBM breach costs:** USD 4.99M, the 12% rise, 602 organizations and one in four malicious breaches AI-enabled at about USD 6M (press release). The USD 1.93M saving and the 36% "extensive" share are confirmed through IBM X-Force and eSecurityPlanet. 4.00 vs 5.93 and 215 vs 280 days match that USD 1.93M and 65-day gap, but the report PDF was not opened.
- **ISACA global and European releases:** 8% run regular AI exercises and 64% have run none (global); 71% none and 3% with mature runbooks (European, 494 respondents).
- **ISC2 2025:** all figures. **ISC2 2024:** gap of 4,763,963.
- **GTIG:** all disclosure and exploitation figures.
- **Arctic Wolf and MSSP Alert:** "more than 60%", one-third human verification, USD 3M warranty, MTTA.
- **Market and vendors:** Proofpoint/Varonis (USD 6.3B, 8.4x LTM revenue, close H1 2027); PANW and CRWD results; Huntress, CrowdStrike, Dropzone and Microsoft pricing.
- **Regulation:** all EU AI Act, CRA and NIS2 dates; NYDFS ("does not impose any new requirements"); CIRCIA; SolarWinds; SIFMA letter; UK Bill (MSPs).
- **Workforce sources:** D3 postings data; SANS/GIAC slides (opened from the RSAC PDF); WEF; DSIT; Fortinet; Stanford (19%); Anthropic RCT (50% vs 67%); NDSS (98%).

## Sources that couldn't be reached

- **GARTNER-TRENDS-2026** (gartner.com is blocked by every route). Its figures (175 employees, over 57%, 33%; sanctioned and unsanctioned agents) were confirmed through secondary coverage, so they are kept.
- **GARTNER-FORECAST-2026** (blocked). Labelled "seen only in search results" and paired with the 2Q26 update, which is relayed by a blog.
- Opened only through the reader proxy (all confirmed): PANW, PwC, NAIC, Swiss Re, NYDFS, Hansard, CISA, MSSP Alert, Computer Weekly, Dark Reading (both), DARPA AIxCC and Black Hat.

## Error patterns seen

- **Attribution drift:** the Dark Reading keynote attributed to Dark Reading; "Torq builds for self-service"; an ISACA quote that appears in no ISACA release.
- **Embellished or softened qualifiers:** "near misses"; OpenAI's breach of an outside platform blurred into "reached an outside party"; COSAiS "agent use cases proposed" tied to the wrong date.
- **Unsourced connective claims:** "skills over headcount is the consensus", including the UK government; "no source reports headcount cuts", which contradicts a cited survey.
- **Wrong or stale provenance labels:** HELPNET was labelled "search-only" but is a sponsored article that was opened; DR-BHASIA was labelled "headline only"; SPLUNK-CISO's date was not confirmed.
- **Stale figures:** the Gartner 2026 forecast had been revised upward twice.
- **Forecasts presented as facts:** none found. Forecasts are labelled throughout.

## For other files (not edited; out of scope)

- **sources.md:**
  - YAHOO-CCS-2026 is dated "c. 2026-02-20"; the article date is 2026-02-23.
  - SPLUNK-RSACSOC-2026 is dated "2026-03"; the blog page shows 2026-08-24.
  - EC-CRAREPORTING-2026 has only a year.
  - The IBM-CODB-2026 URL is the landing page; the press release (newsroom.ibm.com, 2026-07-29) carries the figures.
- **sources.md, IANS-BUDGET-2026:** the cited URL is the landing page, but most figures are only in the press release (`/press/new-ians-and-artico-search-report-finds-ai-is-changing-cybersecurity-jobs-not-eliminating-them`).
