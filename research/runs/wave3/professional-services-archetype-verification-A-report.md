# Professional-services archetype verification, part A

Checked 2026-10-19/20. Files: `economics.md`, `state-of-ai.md`, `frontier.md`, `disruption.md` and `workforce.md` in
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/`.

## Counts

| | Count |
|---|---|
| Source keys cited (all resolve to a listed source with URL and date) | 163 (164 before the removal) |
| Citation instances checked | 333 |
| Discrete factual claims checked (figures, dates, attributions, rules, forecasts) | about 400 |
| Kept | about 372 |
| Fixed | 27 edits (about 22 distinct errors, some repeated across files) |
| Removed | 1 |

All 164 cited URLs were downloaded. 19 returned 403/406 directly and were then read through r.jina.ai. One stayed
blocked (see below).

## Fixes and removals

| File | Claim | Action | Reason |
|---|---|---|---|
| economics §4 | HFS: "20% of current engagements are outcome-based" | Fixed | Misread statistic. 20% is the share of 510 enterprise decision makers who name outcome-based (shared-revenue) models as their current model, not a share of engagements |
| economics §4 | HFS: 56% prefer base plus kicker | Fixed | Added the sample: 101 participants, which differs from the 510 for "current model" |
| disruption §3 | HFS: "54% of current engagements are effort-based" | Fixed | Same misread. 54% of 510 decision makers name effort-based pricing as their current model |
| economics §4 | CMS: 54% of UK law firms expect more fixed fees | Fixed | Attribution drift. CMS quotes Clio UK Legal Trends (vendor data). Now labelled "as quoted by CMS" |
| economics §5 | Baker Donelson: "one major model vendor changed rates in ten of the last 13 months" | Fixed | The source says "at least one major vendor" changed rates in 10 of 13 months, not a single vendor |
| economics §5; state-of-ai §1 | TR: "18% of organisations track AI ROI" | Fixed | The unit is respondents: 18% say their organisations collect ROI metrics, and 40% do not know whether they do |
| state-of-ai §2 | ILTA via Legal Geek: 19% had fully rolled out M365 Copilot | Removed | Source blocked (bot wall on direct, jina and Wayback). The figure is not in ILTA's executive summary, and one web search found nothing |
| state-of-ai §5 | ILTA size bands: "11% to 72%", "31% to 83%", "8% to 38%" | Fixed | The range ends come from different size bands (72% is over 700 lawyers; 83% and 38% are 350-699). Each band is now named |
| state-of-ai §4; workforce §6 | NBER trial: "Google, whose model was tested" | Fixed | The source says only that a "custom AI patent drafting assistant" was used, with Google conducting and funding the study. Now reads "conducted and funded by Google (several authors are Google employees)" |
| frontier §2 | *Heppner* dated "13 or 17 Feb; sources differ" | Fixed | The only cited source (Orrick) says 13 Feb 2026. Court (SDNY) added |
| frontier §2 | California guidance dated 14 May 2026 | Fixed | The 14 May date could not be confirmed (PDF created 15 May). Now "May 2026" |
| frontier §2 | BSB row: "UK regulators now address agentic use" | Fixed | Unsourced connective claim. The BSB release does not mention agentic AI. Now says barristers have regulator AI guidance citing *Ayinde* |
| frontier §3 | Certinia "commits to every workflow being executable by an agent or a human" | Fixed | Not in the source. It commits to "100% agentic capability coverage across the services lifecycle by year-end". MCP calls apply to its intelligent actions |
| frontier §3 | Harvey launched Intake on 13 Oct 2026 | Fixed | Harvey's product page is undated and no launch post was found. The 13 Oct date is now given for Legora only |
| frontier §4; workforce §4 | PwC CEO: partners resisting AI "have no place at the firm" | Fixed | Not a direct quote. It is the headline's paraphrase of an FT interview. Quotation marks removed and "as reported" added |
| frontier §6 | Colorado "developer duties for high-risk AI" | Fixed | SB26-189 covers automated decision-making technology used in consequential decisions, so the wording now follows the act |
| frontier §6 | "Thomson Reuters (vendor): AI more likely to accelerate demand" | Fixed | Attribution drift. The statement is CEO Steve Hasker's view in the report foreword |
| workforce §3 | Citi/Hildebrandt: "US associates overall", 86% plan to grow | Fixed | Wrong population. The source covers large law firms in the US, UK, China and India |
| workforce §3 | ICAEW: 68% "expect fewer early-career roles" | Fixed | The source says 68% expect AI to reduce the need for *some* early-career roles |
| workforce §4, §6 | "Trainees warn..." and "some trainees say..." | Fixed | Embellished qualifier. Both views come from one junior accountant quoted by ICAEW |
| workforce §4 | Partners "become coaches of verification" | Fixed | Embellished. The source (one expert's view) says senior lawyers' mentoring and supervision are critical |
| workforce §7 | "No organisation in that study runs agents as assignable resources" | Fixed | Not stated. The report gives 32% not on roadmap, 25.3% exploring and 10.7% piloting |
| workforce §7 | "the only randomised test of algorithmic assignment" | Fixed | Unsourced superlative. Now "a randomised test" |
| workforce §9 | "Legal operations is described as becoming a design function" | Fixed | Attribution drift. This is a single respondent quote in the TR report |

## Kept after checking (selected high-risk items)

- **McKinsey outcome fees.** About a quarter is confirmed by Business Insider (Birshan). Smaje's "20% probably more
  recent" and ResultSense's "a third of work" are both correctly labelled as different measures.
- **NBER trial.** 133 lawyers at 11 firms; 0.34 and 0.38 SD; seniors +0.45 SD; juniors no average gain. Google
  conducted and funded the study, and this is disclosed.
- **Charlotin.** 2,202 decisions, 1,501 US and 76 UK, last updated 19 Oct 2026.
- **Conference and event dates.** The Atlassian Team '26 session was held on 8 Oct 2026, before the research date. TRI
  events, Kantata Converge, CMBDO and ILTACON 2027 dates all match their sources.
- **Vendor and sponsor labels.**
  - Kantata/RMI is commissioned by Kantata.
  - SPI is sponsored by Deltek.
  - ACC/Everlaw is co-published by a vendor.
  - Juro, Axiom, Loopio, Introhive, Clio and BigHand are vendor surveys.
  - The Stanford lab's Accenture gift is disclosed.
- **Loopio 17%.** The "improved win rate" bar was confirmed from the PDF chart positions.

## Sources not reachable

| Key | What happened |
|---|---|
| LEGALIT-LEGALGEEK-2026 | Bot verification on direct, r.jina.ai and Wayback; the claim was removed |
| SRA-WARNING-2026 | sources.md points to the SRA homepage (Cloudflare challenge). The 17 Aug 2026 notice and the 42 reports are confirmed through DWF-SRA-2026, which frontier already labels "secondary". **For the sources.md owner:** the URL should point to the notice itself |
| NBER full-text PDF | Blocked. Only the abstract page was read, so the model identity could not be confirmed |
| Harvey Intake launch post | Not found; see the fix above |

Read only through r.jina.ai: APQC, Clio (×2), CMS, Columbia Blue Sky, Canadian Press/Castanet, Debevoise, EDRM, Fox
Rothschild, Global Legal Post, Goodwin, HBS, Holland & Knight, Law Society, PwC AI Jobs Barometer (×2), Colorado
legislature.

## Structure

- Every key cited in the five files resolves to a listed source with a URL and a date, either in the file's own list or
  in sources.md.
- LEGALIT-LEGALGEEK-2026 is no longer cited in these files, but it is still listed in sources.md. **For the sources.md
  owner:** remove it if no other file cites it.
- All five files are over 100 lines and each starts with a table of contents.
- File lengths are 135-187 lines, within the 300-line limit.
- `python3 scripts/validate.py` reports 0 errors. Its 23 warnings concern use-case YAML targets, not these files.

## Error patterns seen

| Pattern | Instances |
|---|---|
| Misread statistics | HFS chart read as shares of engagements; TR ROI respondent share read as organisations; ILTA band endpoints mixed |
| Attribution drift | CMS quoting Clio; TR CEO's foreword credited to "Thomson Reuters"; a single legal-ops quote presented as a finding; PwC headline paraphrase in quotation marks |
| Survey population misapplied | Citi large firms (multinational) labelled "US associates overall" |
| Embellished qualifiers | "the only" randomised test; "trainees" (one person); "no organisation"; "one vendor" for "at least one vendor"; partners as "coaches" |
| Unsourced connective claims | BSB row "agentic use"; Certinia "agent or a human" |
| Wrong or uncertain dates | Heppner "13 or 17 Feb"; CalBar 14 May; Harvey Intake 13 Oct |
| Funding and design disclosure | NBER "whose model was tested", which goes beyond the source |
| Forecasts presented as facts | None found; forecasts are labelled with who made them |
