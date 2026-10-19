# Verification report: professional-services / delivery-management

Checked 2026-10-19 against the sources themselves. Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/delivery-management.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/delivery-management.md`

I opened all 62 sources cited in the YAML and the 13 sources cited only in the module (75 in total). Most were fetched directly. Four were read through the r.jina.ai mirror: PwC, the AGS PDF, and two PMI pages. Supporting checks used the Greenhouse job API (Thoughtworks posting dates), page JSON-LD and HTTP last-modified headers. No web search was used.

The YAML was rewritten by a structured edit: it was loaded, changed field by field and dumped at width 120. Some unchanged lines therefore wrap differently, but their content is identical. The module is still 300 lines.

## Counts

| Action | Entries |
|---|---|
| Kept | 3 (`-03`, `-14`, `-15`) |
| Fixed | 13 (`-01`, `-02`, `-04` to `-13`, `-16`) |
| Rejected | 0 |

No entry needed rejecting. Every named deployment traces to a source that was read in full. No grade changed: there are no A claims, every B rests on a named organization in a source read in full, and no C entry had evidence for B.

## Final grade mix

| Grade | Count |
|---|---|
| A | 0 |
| B | 7 (`-01`, `-02`, `-03`, `-04`, `-05`, `-12`, `-14`) = 44% |
| C | 6 |
| D | 3 (`-09`, `-10`, `-16`, all labelled "Idea") |

Targets:

- **16 use cases** (target 15–25): met.
- **A or B: 44%** (target at least 50%): **not met**. This was already the case before verification. No C entry could honestly be raised. `validate.py` reports it as a warning.
- **Every source has a URL and an ISO date**: met.
- **Ids are unique** (16 of 16): met.
- **Quotations are all under 25 words.** The only longer quoted strings in the module are the interview probes, which are our own questions, not quotations.
- **Cross-references:** all 17 ids for other modules and archetypes exist and match the topics described.
- `validate.py`: 0 errors. The 44% warning is the only one for these files.

## Fixes and removals

| Entry / section | What was wrong | Fix |
|---|---|---|
| `-01` problem | Unsourced connective claims: "plans rebuilt from a salesperson's recollection" and "architects spend large blocks of time" | Replaced with Certinia's own wording ("chasing notes, assembling SOWs…") and the Spaulding Ridge 80-hour baseline, each with a ref |
| `-01` checkpoint | Embellished: EINF §5.5 does not say the project manager approves the plan before kickoff | Restated as EINF's finding: control stays with the project manager, and only tasks that can be verified go to AI |
| `-02` problem | Wrong attribution: the Rocketlane testimonial was described as "speaker not identified". It is Stacey Milgram Potzka, a VP of Operations and Implementations (company not named), and her comment is prospective ("could"). An unsourced line, "commitments slip", was also present. | Speaker and prospective framing added; the EarthWise pain is now cited |
| `-02` prerequisite; module §6 | Wrong document: California's guidance says nothing about recording consent. Its p.5 is about vendor terms of use. | Recording consent now cites KJZZ-OTTER-2025; vendor terms cite CALBAR p.5 |
| `-02` source date | DELOITTE-AWS-2026 was dated 2026-09-30, which appears nowhere on the listing. The page data gives a creation date of 2025-06-24. | Ref renamed DELOITTE-AWS-2025, dated 2025-06-24 (used only in this file) |
| `-02` source date | ROCKETLANE-EARTHWISE-2026 is undated. 2026-10-14 is a last-modified header, and an image on the page was uploaded in May 2025. | Title and notes now say so |
| `-02`, `-03`, `-05`, `-07` source dates | DELTEK-DELA-2026 and DELTEK-POLARIS-2026 were dated 2026-05-27. That is the dateModified of related articles on the pages, not of the product pages. | Dated 2026-10-19 (read date), and the titles mark them undated. ROCKETLANE-AGENTIC-2026 is marked as dated by its last-modified header, which was confirmed. |
| `-04` problem | Embellished: Harvey says *partners* ask *associates* to rebuild status. It does not mention "PMO leads". | Restated as Harvey's law-firm example |
| `-04` risk | Unsourced inference: the 89% verification time was said to offset the speed claim | Reworded: no source measures the offset |
| `-05` problem; module §2 | Unsourced claims about periodic reviews and RAG ratings, attributed in the module to Certinia, whose page does not say this. The 47% figure is a barrier to *AI-augmented resource management*, not to AI in general. | Replaced with Certinia's "manual status-chasing", and the barrier stated precisely |
| `-05` prerequisite and checkpoint | Embellished: the release does not say the agent "does not create entries" or "does not change records". "Checking flags against outcomes" was presented as California's rule; California asks for periodic reassessment of capabilities and risks. | Reworded to what the sources say |
| `-05` risk | GARTNER-PMO-2026 was search-only, blocked (403), dated only "2026" and inside a B entry | Removed |
| `-05` role_evolution | Unsourced connective claim: "PMO leaders move from periodic reviews to continuous alerts" | Now attributed to Kantata's product page |
| `-06` problem; module §2 | Embellished: "change orders written after the work is done". The guide says the work is already under way by the time the project manager notices. | Reworded |
| `-06` risk | "No false-positive rate is published anywhere" overlooked the guide's own unsupported claims: near-zero false positives by week four, and 15–25% less out-of-scope work | Those claims are now named as unsupported vendor assertions |
| `-07` problem | Teamwork's four leak points were paraphrased incorrectly ("wrong-rate staffing, unlogged time"). BigHand's page was turned into a pain statement ("built by hand… seen late") that it does not make. | Teamwork's four leak points are now used, and BigHand's claim is stated as marketing |
| `-07` prerequisite and role_evolution | Missing ref; unsourced "exception lists instead of reconciling" | Refs added (Rocketlane, Certinia); the change is labelled as unmeasured |
| `-08`, `-10` risks | A statistic reported as something it doesn't measure: the tau-bench figures are GPT-4o on retail customer-service tasks, not delivery agents | The adjacent context is now stated |
| `-09` solution | "Most often wanted" overstated: autonomous agents (6 participants) were mentioned more. The paper calls calendar management the most anticipated *administrative* capability (4 of 12). | Corrected |
| `-10` risk | One interviewee's view (P11) was generalised to all interviewees | Stated as one interviewee, with the six who want humans to keep decision control |
| `-11` risk | The ILTA "fewer than one in five" figure lacked its context | Context added: tracking and compliance tools for work-product governance |
| `-12` role_evolution | Connective inference presented as the session's claim | Restated as what the session presents |
| `-13` problem | Wrong document: "more go-lives with the same team size" is Tandem's claim, not SPI's | Cited to TANDEM-2026 |
| `-13` role_evolution | "The Big Four hiring technologists": the figures are for Accenture, which is not Big Four, and EY | Corrected |
| `-16` checkpoint and role_evolution | TRI-METER does not say pricing leaders decide pass-through, or that KM and innovation managers "take on" cost control | Restated as the question ILTACON left open, and who spoke |
| `-16` risk | AMLAW: "surveyed" is not in the teaser | Restated as the teaser's wording; body not read |
| Module §2 meetings row | "Written after the fact; commitments slip" is not what EarthWise says | Now EarthWise's manual notes and "he said, she said" |
| Module §6 PMI | "Governs AI projects, not AI used to run projects" is an inference | Softened to the release's scope: delivering AI initiatives |
| Module §7 legal | Unsourced connective claim: "pricing and innovation officers speak for firms". "Legal ops runs legal project management" is overstated; the report says its remit *can include* it. | The TRI-LEGALWEEK clause was dropped, and TRI-LDOR reworded |
| Module §8 | ILTACON entry dated only "2026-09", and "per matter" embellished. PMI Summit dates "21–24 Oct" are not on the cited page. | Dated 2026-09-09 and reworded; the Summit is now given as October 2026, Detroit, with the source note corrected |

## Spot-confirmed without change (sample)

- Moonnox release (2026-07-21; Laabs "approximately 80 hours to under 20 hours"; Paoni "without manual rework")
- Certinia Veda agent catalogue, Siemens quote and results panel (~50%, 11–23%, 60%)
- Diabsolut 70% and Nextview's steering packs (Certinia blog; Dreamforce 14–17 Sep confirms 2026)
- SPI benchmark figures: 66.4%, 73.8%, 10.7%, 37.7%, 27.1%, 500+ firms, project-ERP growth and EBITDA
- SPI AI study: 245 firms, 43.6% vs 23.1%, 84.8%
- PwC Intelligent Status Insights: ~40%, 120 hours, USD 7,000–24,000 projected (2026-03-24)
- Wellingtone 72%, 36% and 67% (2026-03-12)
- Automation Consultants session abstract (2026-10-08, sponsored, roughly 25%, tripled, 11 engagements)
- zeb/NTT DATA (published 2026-05-07)
- Harvey Legal Work Orchestration (2026-10-15, 20% in six months)
- Kantata SOPSI (12%, 88% and 89%, 54%, 90%; 200 leaders, Censuswide)
- Kantata RMI (52.7%, 4%, 7.3%, 44 organisations)
- Certinia GSD (78%, 38% and 75%; 24 and 16 points; IDC quote; June 2026, Sapio)
- Deltek Clarity (29%, 26%, 70%, 38%)
- EU AI Act Annex III 4(b) and Annex III dates moved to 2 Dec 2027
- ABA 512 Parts II.B, II.C, II.E and II.F
- California guidance pp.3–9 (PDF created 2026-05-15, consistent with approval on 2026-05-14)
- ICMCI sections 2.2, 3.4, 5.4 and 7.3 (adopted May 2026)
- AGS update 327 (2025-04-04)
- EINF (available online 2026-04-23; Tables 3, 5 and 6; §5.5)
- Thoughtworks postings (first published 2026-07-03 and 2026-08-19, per Greenhouse)
- Basware release (2026-10-13; TSW session on 2026-10-20)
- TRI-METER (Fox, roughly 1%)
- ACC 59%
- KPMG 82% of 468 GCs
- Napta 68% and 16%
- Lawyer Monthly on the SRA guidance (2026-06-12)
- DAC Beachcroft (2026-09-28)
- Legora–Laurel second phase (2026-10-13)
- PMI standard (9 June 2026)

## Sources that could not be reached

- **GARTNER-PMO-2026** (gartner.com): 403 bot check. It was search-only and is now removed.
- **AMLAW-CONSUMPTION-2026**: only the teaser bullets are readable; the body is paywalled. It stays `search-only`, in a D entry.
- **PMI-SUMMIT-2026**: the call-for-speakers page was read via the mirror after a direct 403, but it gives no event dates.
- Read via the mirror after the direct route failed: PWC-STATUS-2026 (403), PMI-AISTD-2026 (403) and AGS-AIMODELCLAUSES-2025 (timeout).
- Unresolved date, for the coordinator to settle: CALBAR-GENAI-2026 is 2026-05-14 here but 2026-05 in some other module files. The PDF metadata shows creation on 2026-05-15, consistent with Board approval on 2026-05-14.

## Error patterns to fix in the briefs

1. **Product-page dates taken from the wrong element.** DELTEK-DELA and DELTEK-POLARIS took the dateModified of related-article JSON-LD blocks. The AWS Marketplace listing got a date that appears nowhere on it. The Rocketlane pages took the HTTP last-modified header as a publication date. Rule: use a date only if it belongs to the cited document itself. Otherwise mark the page undated and use the read date.
2. **Paraphrase drift into pain statements.** Vendor marketing outcomes were turned into "the problem" (BigHand's write-offs), and generic pain was pinned on a vendor page that does not say it (RAG ratings and periodic reviews on Certinia). Each sentence in `problem` needs its own ref, in the source's terms.
3. **Wrong-document attribution in governance text.** California was cited for recording consent, and SPI for Tandem's go-lives claim. When a sentence merges two sources, check each clause against its own ref.
4. **One respondent generalised to "interviewees"**, and a "most" ranking taken from a sub-section (EINF). For qualitative studies, give the count of participants, as the paper does.
5. **Benchmarks cited without their task context** (tau-bench is GPT-4o on retail tasks). State the system and task for any reliability figure from another domain.
6. **"Speaker not identified" when the speaker is named on the page.** Read the full testimonial block, not only the quote text.
7. **Embellished qualifiers** were again the most frequent error: "does not create entries", "does not change records", "runs legal project management", "Big Four", "surveyed", "per matter". Use the source's own verb and scope.
