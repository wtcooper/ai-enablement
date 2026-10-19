# Verification report: professional-services / scoping-pricing

Checked 2026-10-19 against the sources themselves. Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/scoping-pricing.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/scoping-pricing.md`

I opened 78 cited sources plus the 4 sources that only the module cites, either directly or through the r.jina.ai mirror. One more document was fetched to settle a claim: the Supreme Court of Virginia order containing the LEO 1901 text. One web search was used, for the PwC One release.

## Counts

| Action | Entries |
|---|---|
| Kept | 8 (`-04`, `-08`, `-09`, `-12`, `-14`, `-19`, `-20`, `-21`) |
| Fixed | 15 (`-01`, `-02`, `-03`, `-05`, `-06`, `-07`, `-10`, `-11`, `-13`, `-15`, `-16`, `-17`, `-18`, `-22`, `-23`) |
| Rejected | 0 |

No source was missing, and no entry relied on a claim that could not be supported. No grade changed: no A entry was claimed, and every B entry rests on a named organization in a source that was read in full.

## Final grade mix

| Grade | Count |
|---|---|
| A | 0 |
| B | 14 (61%) |
| C | 8 |
| D | 1 (`-14`, labelled idea) |

Targets: 23 use cases (target 15–25) ✔. A or B: 61% (target ≥50%) ✔. Every source has a URL and an ISO date ✔. `validate.py` reports no errors or warnings for these files. Its one error is in `acceptance-risk.md`, which belongs to another module.

## Fixes

| Entry / section | What was wrong | Fix |
|---|---|---|
| `-01` problem | Embellished: the source says senior consultants spent hours "writing technical plans and chasing spreadsheets". It says nothing about turning transcripts into scope documents. | Restated as Diabsolut's own account; the scoping-from-transcripts pain is now separate and unattributed |
| `-01`, `-02`, `-05` source date | CERTINIA-CUSTOMERS-2026 was dated only "2026" | Changed to `2026-09`: Certinia's sitemap lastmod is 2026-09-09, and the post calls Dreamforce (14–17 Sep) upcoming |
| `-02` problem | Added an unsourced "and margin lost" | Removed; now quotes "gut instinct" |
| `-03` solution | All three job postings were said to ask for AI forecasting, predictive pricing and cost estimation. Pillsbury only asks for experience with AI tools. | Each request is now attributed to the posting that makes it |
| `-03` risk | "So tools may not reach the lawyer" is an unsourced inference. BigHand's president says pricing *expertise* does not reach the lawyer. | Reworded to the source |
| `-03` checkpoint | "Drafts and sends the client email" was embellished; the demo only equips the lawyer to draft it | Changed to "drafts", and a source ref was added |
| `-03` role_evolution; module §7 | The TRI 2024 article is about pricing legal-technology products, not matters | That context was added |
| `-06` role_evolution | Connective claim "rather than into shorter bills alone" is not in the source; Norton Rose says savings pass to the client | Rewritten to the firm's statement |
| `-06` measures | "Touch tech regularly" was paraphrased as "use the tools", and the email attribution was overstated | Corrected |
| `-07` solution; module §8 | "Hallway topic" at ILTACON; the source describes a discussion among press colleagues | Reworded |
| `-07` risk | "Vendors were reluctant when asked" overstates it. The source says vendors did not raise it unless asked and had little insight. | Reworded |
| `-07`, `-15` risks; module §6 and §9 | ABA 512 was cited "as quoted by a commentator" (TRI-ABA512-2025) when the opinion itself is in the file and was read in full | Now cites ABA-OP512-2024 Part II.F directly; the TRI commentary is kept only for the "buyers' remorse" view |
| `-10` title and solution | The TRI "Interdependent" article does not urge firms to pick key clients, co-design use cases or agree how gains are shared. It sets five questions and suggests raising one at the next client meeting. | Rewritten to the source; the title was softened |
| `-11` solution; module §3, §5, §8 | Cause embellished: the fee cut was presented as purely "because of AI-driven efficiencies". Yahoo Finance reports that KPMG also cited a simple tax position. | Now reads "among other arguments" |
| `-11` risk | "Sources disagree on which KPMG entity" is overstated: Yahoo says "international division"; OnlyCFO just says KPMG | Stated precisely |
| `-11` outcome; module §5 | ACC-Everlaw's 64% measures "expect to rely less on outside counsel". Bloomberg Law glossed it as "bring more work in-house". | The release wording is used; the gloss is noted |
| `-11` problem; ICAEW date | The ICAEW example was a *prospective* client asking to cut junior hours *and fees*. The date was given only as 2026-02. | Corrected; the date is now 2026-02-03 |
| `-13` problem | "Named as the main barrier" was embellished and unattributed | Attributed to the ILTACON 2025 coverage: recruiting and pay "hinge largely on utilization" |
| `-15` risk; module §6 | "Criticises the ABA and North Carolina positions": the adopted LEO 1901 names neither. It rejects "contrary views" from other jurisdictions. | Reworded and checked against the Court order. The locator now points to the order. |
| `-15` role_evolution; module §7 | "Cheapest effective resource": the source says "most efficient resource" | Corrected |
| `-16` solution; module §3 and §8 | "Developing" value and outcome pricing; Bloomberg Tax says firm leaders are "brainstorming" | Reworded |
| `-17` risk; module §9 | "Warns against using AI mainly to justify higher rates" overstates it. TRI warns that firms relying on premium pricing without measurable efficiency gains are most exposed. | Reworded |
| `-18` role_evolution | "Billing and appeals departments exist only to manage hourly billing" is embellished | Restated as departments built to counter insurers' bill audits |
| `-18` checkpoint | Unsourced: the KPI agreement and review process is not described in the source | Restated to what the source says; the gap is noted |
| `-22` source | The PwC One release was blocked (403 direct, mirror and Wayback). Its date and title were seen only in search, yet it was marked `access: full`. | Set to `search-only`. The service list and prerequisite now rest on The New Stack, which was read in full. The grade stays B on full-access secondary sources. |
| `-22` role_evolution | Claim attributed to the wrong document: the "time's becoming less and less of relevance" quote is from Bloomberg Tax; Stanford re-cites it | Now cites BLOOMBERGTAX-PRICING-2026 as the primary source |
| `-23` prerequisite and checkpoint | "Partners agree to contribute" and "lawyers curate and review" are embellished | Restated to Debevoise's wording: curated knowledge built on its lawyers' collective experience, complementing their advice |
| Module §5 | The 78%, 6% and 32% figures are from corporate-client respondents, a subset, and were labelled as all 1,816 professionals | The subset is now stated |
| Module §8 | The APS AI plan was unveiled on 2025-11-12; the article is dated 2025-11-13 | Date corrected |
| Module §10 | The four module-only sources (marked *) had no URLs | URLs added; all four were opened and their figures confirmed |

## Spot-confirmed without change (sample)

- BigHand percentages
- Goodwin and PERSUIT release text
- Neocol's nine-day rollout
- California guidance, p. 8 (dated May 2026 from PDF metadata)
- DC Opinion 388 §E
- Texas Opinion 705
- North Carolina 2024 FEO 1, adopted 2024-11-01
- IRS OPR item 2 (2026-06-24)
- ILTA Q3.18 table
- Legora and Laurel announcement (2026-10-13)
- TRI Legalweek article (2026-03-13)
- TRI Stand-out survey figures (one-third / 60%; 2,527 lawyers; 65 countries)
- Deloitte refund details
- APS clauses
- Kopka KPIs
- McKinsey "about a quarter" and 20%
- Reuters TCS 80%, Cognizant, HCLTech and Tech Mahindra details
- Falcon €1,000 for six contracts
- Crosby site
- ABA Journal (STAAR 2.0, A&O Shearman–Harvey)
- TR Future of Professionals (Elevate 52%, trade-offs)
- SPI 84.8%, 43.6% and 23.1%
- TRI-CHARGING figures
- TRI LFFI Q1 2026 (about 10% rate growth, 2.7% demand, index at 55)
- Deltek (896 A&E firms, 38%)
- Bloomberg on Citi (4.2% demand growth against about 1.5% normal)
- TRI COO & CFO Forum (21–22 Oct 2026)
- All nine assurance and tax cross-reference ids exist and match the topics described

## Sources that could not be reached

- **PWC-ONE-2026** (pwc.com): 403 direct, 401 via the mirror, Wayback reset. Title and date were confirmed by a search result and by three press reports. It is now `search-only`, and no claim rests on it alone.
- Several sources were blocked directly but read through the mirror: ABA-LPMRFP-2026, CMS-TRENDS-2026 and ATL-DEFENSE-2026. Others were blocked on the mirror but read directly: BLOOMBERGTAX-PRICING-2026, CALBAR-GENAI-2026, DCBAR-OP388-2024, TRI-LAWYERDEV-2026, BI-MCKINSEY-2025 and YAHOO-KPMG-2026.
- Unresolved date: ILTA-TECHSURVEY-2026. The document is undated, its file code is "2606" and its PDF metadata says 2026-08-14. I kept `2026-06` to match the four other files that cite it, and recorded the metadata in the locator. The coordinator should settle it across all files.

## Error patterns to fix in the briefs

1. **Embellished qualifiers and causes** were the most common error, found in 9 places. Examples: "cheapest" for "most efficient", "developing" for "brainstorming", "main barrier", "exist only to", "because of AI" when the source gives several reasons, and "hallway topic". Briefs should require the source's own verb and qualifier for any causal or ranking claim.
2. **A claim attributed to the wrong document.** Commentary that quotes a primary source was cited instead of the primary source in the file (ABA 512 via TRI; PwC's tax leader via Stanford). Rule: when the primary document is in the source list and was read, cite it.
3. **Unsourced connective text in `role_evolution`, `human_checkpoints` and `risks_and_guardrails`.** Examples: "rather than shorter bills alone", the KPI review process, "partners agree to contribute". Each sentence needs its own ref, or must be marked as an inference.
4. **Paraphrase drift in survey figures.** The 64% from ACC was reported by its secondary gloss, and a client subset (78% and 6%) was presented as the full sample. Briefs should say: quote what the statistic measures from the publisher, and name the subgroup.
5. **Access inflated.** A page seen only in search was recorded as `access: full` (PwC One). Briefs should require an access value that reflects whether the text was actually retrieved this run.
6. **Imprecise dates when a better date is findable.** Examples: "2026" or "2026-02" when a sitemap or byline gives the month or day. Briefs should tell agents to check sitemap lastmod and the HTML `<time>` element as well as JSON-LD.
7. **Over-specific summaries of other jurisdictions' opinions.** One entry said LEO 1901 names the ABA and North Carolina; the adopted text does not. For regulatory claims, read the adopted text, not the proposal notice.
