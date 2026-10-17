# Verification report: security / governance-risk (wave 4)

- **Verified:** 2026-10-17 (verifier brief `research/runs/wave4/briefs/verify-governance-risk.md`)
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/use-cases/governance-risk.yaml` (21 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/modules/governance-risk.md`
- **Method:** I pulled all 95 distinct URLs cited in the two files and reopened every one with `curl` in a private working
  folder. I used `pdftotext` for the PDFs (FAIR report, two CSA papers, the RSAC slide deck, NIST IR 8596, the ReCon and
  CIS-Controls arXiv papers, and ISACA's global and European infographics). Pages that returned 403 went through the
  `r.jina.ai` text mirror: Drata, Hyperproof, Safe (2 pages), Dark Reading, PwC, RSAC and WEF. So did the JavaScript-only
  Ashby postings (OpenAI and Plaid). BleepingComputer blocked the mirror and the Internet Archive was offline, so I read
  it directly with browser request headers. The FINRA report keeps its text on section sub-pages (`/gen-ai`,
  `/third-party-risk`), so I fetched and read those. Dates were checked against on-page bylines, `datePublished`,
  Greenhouse `published_at`, Ashby `datePosted`, arXiv submission history and Vanta, Conveyor and Whistic sitemaps.
  Every quotation in single quotes was matched by script against the source text.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. For this file it gives `INFO ... 21 use cases, 11 graded
  A/B (52%)`. The 18 warnings belong to other streams' files.

## The ISACA conflict (settled)

The research files and the cross-cutting regulation file were each quoting a different, real ISACA press release
issued on 2026-09-22 from the same survey:

| Document | Sample | Regular AI incident exercises | None run | Included in broader exercises / plan to | Helped write AI-use policy |
|---|---|---|---|---|---|
| Global release, "Only 8 Percent of Organizations Conduct Regular AI-Specific Response Exercises" (`ISACA-SOC-2026`), confirmed by ISACA's global infographic (`ISACA-SOCINFO-2026`) | more than 1,800 global respondents | **8%** | **64%** | 17% / 16% | **56%** (47% in 2025, 35% in 2024) |
| London release, "Cyber teams stretched too thin as attacks intensify and budgets shrink" (`ISACA-SOCEU-2026`), matching ISACA's European-edition infographic | 494 European respondents (of 1,888) | **5%** (infographic) | **71%** | 16% / 17% | **60%** |

The cross-cutting file `security-x-guardrails-regulation.md` read the London release as if it were global. Its 37%
for AI-automated threat detection, 3% with mature AI runbooks and 30% not yet started also come from the London
release. Neither reading was invented. They describe different samples.

**Corrected wording for other security files (global figures):**

> ISACA's State of Cybersecurity 2026 survey (more than 1,800 respondents; press release and global infographic, 2026-09-22): 8% of organisations conduct AI-related incident response exercises regularly, and 64% have not conducted any. Another 17% say AI incident response is included in broader cyber incident response exercises, and 16% plan to run such exercises. 56% of respondents say they or someone on their team helped develop a policy governing AI use (up from 47% in 2025 and 35% in 2024). 51% are involved in developing, onboarding or implementing AI solutions (40% in 2025, 29% in 2024). 48% either don't know whether their organisation has AI incident playbooks or say it has none.

**European figures, if wanted, labelled as such:**

> ISACA's European release (London, 2026-09-22; 494 European respondents): 71% have run no AI-related incident response exercises, 3% have mature formal runbooks for AI incidents, 30% have not begun addressing AI incident response, and 60% helped develop AI-use policies. The European infographic gives 5% running exercises regularly.

Files that still carry the European figures as global ones, or call the 8% unverified:
- `security-x-guardrails-regulation.md`, lines 98 and 238
- `security-x-state-of-ai-disruption.md`, line 319
- `security-operations-governance.md`, line 1302
- `operations-synthesis-report.md`, line 101
- `security-ai-security-threats-redteam.md`, line 2136

The ISACA full report sits behind a lead form and was not read.

## 1. Counts

| | Use cases |
|---|---|
| Kept | 4 (`#07`, `#10`, `#13`, `#21`; `#13` had a locator update only) |
| Fixed | 17 (`#01`-`#06`, `#08`, `#09`, `#11`, `#12`, `#14`-`#20`) |
| Rejected | 0 |

Every cited source exists and was reached. The module received 15 edits.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 2 (01, 05) | 2 (01, 05) |
| B | 11 | 9 (02, 03, 06, 08, 09, 15, 17, 18, 19) |
| C | 7 | 9 (`#04` and `#11` added) |
| D | 1 (21) | 1 |

A/B share is now 52% (11 of 21), down from 62%. No A or B entry uses a search-only source. Every source is `access: full`.

- **Grade A rule.** `#01` keeps A. GitHub's 93% sits in the vendor's ROI list as a programme metric against a stated
  12-month goal, and Carta's 83%, 95% and 40% are header metrics. Carta's 72-of-77 is labelled a recollection. `#05`
  keeps A on Samsara's counts (820 to 260 controls, 1,200 evidence items). The description now says the page credits
  the Compliance Agent with evidence mapping and consolidating requirements, but does not separate the agent's share
  of the reduction.
- **`#04` B to C, maturity in-production to announced.** Anthropic's posting describes trigger-based reassessment as
  analyst work. The AI watching for triggers rests only on Safe and Vanta product pages, with no named customer. This
  is a grade inflated by evidence from an adjacent (non-AI) process.
- **`#11` B to C.** The postings describe tooling to be designed and built ("Design and build AI-native risk tooling";
  "Build AI skills and automations"), not a deployed system. Vanta's Agent for Risk names no customer.

## 3. Fixes and rejections

| # | Field | Problem | Fix | Error pattern |
|---|---|---|---|---|
| 01 | risks | CSA AI-CAIQ said to "standardise what AI-related answers must cover" | CSA describes a question set for self-assessment or vendor evaluation; reworded | embellished qualifier |
| 01 | risks | 'improved accuracy' in quotes is not in the arXiv abstract | Quoted the real text: 'significantly improves response accuracy and operational efficiency' | altered quotation |
| 02 | role_evolution | "Synthesia's two-person security team says..." | It is Vanta's narrative, not the team's statement; reattributed and matched to the page | wrong speaker |
| 03 | risks | Trust gap, discomfort with AI negotiating with vendors and "high-trust industries" attributed to Lovable's CISO | All said by Jasper Mills, Ethira's CEO; reattributed | wrong speaker |
| 03 | risks, role_evolution | 'verify agent-drafted evaluations'; "podcast guests expect..." | Posting says 'verifying'; the contracted-workforce view is Ethira's founder's alone | altered quotation; wrong speaker |
| 04 | solution | "an agent watches for [triggers], reopens the assessment..." cited to Anthropic's posting | Posting has the analyst reopen on triggers. Rewritten: analyst process (Anthropic), agent features (Safe Threat Intel and Contract Analysis agents; Vanta TPRM Agent) | grade inflated by adjacent process |
| 04 | role_evolution | Lovable's CISO "says every employee who wires AI into internal data may become a vendor"; "third-party team governs a wider set of producers" | He asks whether internal AI builders should be treated as 'mini vendors'. Unsourced connective removed | embellishment; unsourced connective |
| 04 | grade, maturity | B and in-production | C and announced (see §2) | grade inflation |
| 05 | outcomes | "consolidating controls ... with the Compliance Agent" | Page credits the agent with evidence mapping and consolidating overlapping requirements, and the platform with the common control framework; caveat added | statistic described as more than it measures |
| 01, 05, 08, 09, 11, 19 | sources | Vanta resource dates taken from sitemap months | On-page dates: Compliance Agent and TPRM Agent 2026-03-19 (were 2026-06), Agent for Risk 2026-06-02, Quality Eval 2026-06-10 (was 2026-07), AI governance gap 2026-07-24 | wrong dates |
| 19 | sources, role_evolution | "Vanta cites an Axipro count" | Guest post by Axipro's CEO on Vanta's blog; reattributed | wrong speaker |
| 06 | role_evolution | Figma listed among postings asking for "agent workflows" | Figma's posting names API automation and machine-readable controls, with no AI; separated | embellishment |
| 06 | human_checkpoints | "External auditors still receive the evidence and issue the certifications" | The page shows audit cycles condensed, not auditors' role; reworded | unsourced connective |
| 06 | problem | "staff spend a large share of their time on it" cited to the Anecdotes article | Added Perforce's 60% as the source | missing source |
| 11 | problem, solution | Intake, register hygiene, first drafts and reports cited to Anthropic's analyst posting | Each claim cited to the posting that says it (Anthropic risk engineering, Plaid, Vanta) | wrong document |
| 11 | role_evolution | 'AI power users' | Posting: 'AI power user who automates the work so it scales' | altered quotation |
| 12 | problem, solution | "results go stale"; "use AI to speed scenario scoping and data gathering" cited to Anthropic's posting | Not in the posting; removed. Solution now uses the posting's real wording | unsourced connective |
| 12 | solution | FAIR respondents "use or test AI to quantify risk automatically, forecast and simulate" | These are the areas respondents name as most valuable (42%, 40%, 40%); reworded | statistic described as something it doesn't measure |
| 14 | solution | AI-drafted board pack stated as practice | Labelled "Idea"; no source describes it in use | unsourced claim |
| 15 | human_checkpoints | "Control owners and auditors review responses" cited to Anthropic | Not in the posting; replaced with what the posting says | unsourced connective |
| 15 | problem, role_evolution | "Analysts assemble evidence packs by hand" cited to NIST; 'generat[es] audit responses' | NIST framing restated; quote now 'generating audit responses' | embellishment; altered quotation |
| 16 | solution | Anecdotes quote merged two sentences with a comma | Matched to the source punctuation | altered quotation |
| 17 | outcomes, notes | ISACA conflict carried as unresolved; quotation of 25 words | Global figures confirmed; European source of the 60% and 71% identified; 2025 and 2024 trend added; `ISACA-SOCINFO-2026` added; quote shortened | data conflict |
| 17 | solution, risks | Sendbird's "CSO"; "blocking everything cannot be won" | Page says CISO. He says security "can never stop everything" | wrong title; embellishment |
| 17 | prerequisites | "a written definition of what counts as an AI incident" | Sendbird's CISO says his team is still working out the definition | embellished qualifier |
| 17 | risks | Gartner warns of "stalled AI adoption" | Candrick says "stalled innovation, dated AI tools" | embellishment |
| 18 | solution, prerequisites | "Agent actions are tiered by consequence, agents get their own identities" cited to CISA and Venables | Neither says this. CISA: no broad or unrestricted access, strong identity management. Venables: deterministic gates that bypass the agent's reasoning | wrong document; unsourced connective |
| 18 | outcomes | WEF 64% "assess the security of AI tools before use" | WEF does not say "before use"; reworded | embellished qualifier |
| 18 | outcomes | ISACA 8% with "64% as read by two angles; 71% per regulation file" | Confirmed 8% and 64% (global), plus 17% and 16%; `ISACA-SOCINFO-2026` added | data conflict |
| 03, 18 | sources | FINRA locators point to the landing page, which holds only the table of contents | Locators name the section sub-pages | locator |
| 19 | outcomes, risks | State of GRC survey called "self-selected", attributed to the author | Author says only that the design could be tighter; recruitment is not described | embellishment |
| 20 | solution | "analysts supervise agents" cited to SANS/GIAC slides | Not on the slides; removed | unsourced connective |
| 20 | role_evolution | ISC2 "more strategic roles (72%)" | ISC2: "more strategic cybersecurity mindsets" | statistic described as something it doesn't measure |

**Module edits:**
- §1 A/B count changed to 11 of 21.
- §3 `#04` and `#11` regraded and reworded.
- §5 ISACA rows corrected and expanded; GRC survey labelled "recruitment not described".
- §6 data-conflict bullet replaced with the settled global and European figures and a new `ISACA-SOCEU-2026` source.
- §7 "AI power user" quote fixed.
- §8 Vanta agent dates corrected (2026-03-19, 2026-06-02).
- §8 GRC-role postings reworded: Figma's names automation only, not agents.
- §8 ISACA figures added to the 2026-09-22 entry.
- §9 Sendbird title and Gartner wording fixed.
- §10 EBA URL had a stray `%5C`, now removed; `ISACA-SOCEU-2026` entry added.

## 4. Sources that couldn't be reached

None in the end. Notes on access:
- **Read via the text mirror:** Drata, Hyperproof, Safe (2 pages), Dark Reading, PwC, RSAC landing page and WEF (all 403
  on direct fetch), plus the Ashby postings (JavaScript-only).
- **BleepingComputer:** read directly with browser headers. The mirror was blocked and the Internet Archive offline.
- **Not read:** the full ISACA report (behind a lead form). The global and European infographics stand in for it.
- **Dated from a sitemap, the release date or the retrieval date:** Vanta and Conveyor customer pages and the Whistic
  case study (sitemap last-modified); Drata, Safe and Optro product pages and CSA hub pages (retrieval date);
  `ISACA-SOCINFO-2026` (report release date).
- **Year only:** the SANS 2026 SOC Report landing page and the FAIR report PDF.

## 5. Targets

| Target | Result |
|---|---|
| 15-25 use cases | 21: met |
| At least 50% graded A or B | 52% (11 of 21): met, narrowly |
| Every source dated | Met. Every source has a date. Some are sitemap months, retrieval dates or a year |
| Vocabulary values, unique ids, quotations under 25 words | Met. Validator reports 0 errors; the one 25-word quotation was shortened |

## 6. Error patterns to fix in the briefs

1. **A survey with regional editions.** ISACA issued a global and a European release on the same day from one survey.
   Ask researchers to record the sample (global or regional, n) next to every survey figure, and to check the
   publisher's infographic.
2. **Wrong speaker in podcast transcripts.** Two guests' remarks were merged under one name (Lovable CISO and Ethira
   CEO). Require the speaker label from the transcript for each attributed remark.
3. **Postings read as deployments.** Phrases like "Design and build" and "Build AI skills" were graded B. An analyst's
   manual process was read as an agent's work (`#04`). Tell researchers that a posting supports B only when it
   describes a tool already in use, and to grade the AI step, not the surrounding process.
4. **Citations stretched to cover connective claims.** A real source was attached to a sentence it does not support
   (`#12`, `#15`, `#18`, `#20`). Ask for one ref per claim, not one ref per sentence.
5. **Small embellishments.** Examples: "before use", "self-selected", "written definition", "strategic roles",
   "every employee becomes a vendor". Ask researchers to copy the qualifier from the source.
6. **Quotes edited inside quote marks.** Paraphrases, plurals, tense changes and merged sentences all appeared
   between quote marks. Quoted text must be verbatim; anything else goes outside the marks.
7. **Sitemap months used when an on-page date exists.** Three Vanta resource pages carry bylined dates that differ by
   up to three months. Check the page byline before the sitemap.
8. **Landing-page URLs for content on sub-pages.** FINRA's report is an example. Ask for the section URL or a locator
   that names it.
