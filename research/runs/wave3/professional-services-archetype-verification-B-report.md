# Professional-services archetype verification (B)

Date: 2026-10-19. Files checked: `ARCHETYPE.md`, `interview-guide.md`, `value-chain.md`, `guardrails.md`,
`objections.md`, `sources.md` in `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/`.
Method: every cited URL in these files and their source lists was fetched (138 URLs; `curl`, `pdftotext`, and
`r.jina.ai` for blocked pages), and each claim was checked against the fetched text.

## Counts

| File | Claims checked | Kept | Fixed | Removed |
|---|---|---|---|---|
| ARCHETYPE.md | 18 | 15 | 3 | 0 |
| interview-guide.md | 13 | 10 | 3 | 0 |
| value-chain.md | 10 | 7 | 3 | 0 |
| guardrails.md | 52 | 45 | 6 | 1 |
| objections.md | 54 | 41 | 12 | 1 |
| sources.md (Part A claims; Part B titles, dates and URLs) | 24 | 20 | 4 | 0 |
| **Total** | **171** | **138** | **31** | **2** |

"Removed" means an unsourced connective phrase was deleted inside an otherwise sourced claim. No whole claim or source
key was removed.

## Fixes and removals

| File | Claim | Action | Reason |
|---|---|---|---|
| ARCHETYPE.md | "a consulting target of 20 per cent humans, 80 per cent AI agents" | Fixed | Example without firm type: the target is from the founder of an AI-native advisory boutique (Queen's Tower), told to the FT and summarised by Resultsense |
| ARCHETYPE.md | Services clients use without a professional in the loop [CPAPA-PWC-2026] | Fixed | Marked as PwC's stated plan, not a measured practice |
| ARCHETYPE.md | delivery-management `#12` reference case | Fixed | Labelled as a sponsored conference talk (Atlassian Team '26 Europe, held 8 Oct 2026) as well as self-reported |
| interview-guide.md | "30% of legal-finance respondents keep the margin" | Fixed | Population drift: BigHand's respondents are law firms (vendor pricing survey) |
| interview-guide.md | "only 7.3% use outcome data in staffing" | Fixed | The source says 7.3% find outcome data "easily accessible and used in staffing"; study commissioned by Kantata |
| interview-guide.md | "Only 38% of 896 A&E firms report measurable benefit" | Fixed | Wording aligned with Deltek ("measurable positive business impact"); marked as vendor survey |
| value-chain.md | "79% of bid teams use AI" | Fixed | Population and date added: 1,533 RFP teams across all industries, AI use in 2025 |
| value-chain.md | "47% cite fragmented data" | Fixed | Source category is "poor data quality or fragmented data"; vendor-commissioned |
| value-chain.md | "78% of 123 partners" | Fixed | Firm type and provenance added: law and accounting firm partners, vendor (Introhive) survey |
| guardrails.md §2 | Accounting bodies: "ethics surveys and planned guidance" | Removed / fixed | "Planned guidance" had no source; replaced with ACCA's sourced finding (61% rank AI their top ethical challenge) |
| guardrails.md §5 | "A summary of ABA 512 says lawyers may not charge for learning tools" | Fixed | The full opinion text (LawNext-hosted copy) says this directly; now cited to ABA-OP512-2024 with the summary as support |
| guardrails.md §5 | "Virginia says reduced time does not mean a proportionally reduced fee" | Fixed | Paraphrase tightened to what VSB states: value-based fees can reflect AI efficiency gains and remain reasonable; approval date added |
| guardrails.md §7 | "part of the growth is lag in finding cases" | Fixed | Unsourced connective; replaced with the compiler's own statement that the database is a work in progress |
| guardrails.md §7 | *Rodney*: "the solicitors and the firm's management were referred" | Fixed | Judgment refers both solicitors and the firm (AML Legal), not "management" |
| guardrails.md §8 | "Most law-firm professional liability policies are reported to be silent on AI" | Fixed | Broker said the vast majority have no express AI exclusion; attribution to one broker added |
| guardrails.md §8 | "broad exclusions on some lawyers' and architects' policies" | Fixed | Source reports sweeping exclusions on lawyers' E&O and says the wording is spreading to architects |
| objections.md §1 | "71% of legal professionals ... have a policy" | Fixed | Population: 850 senior legal leaders (Morae, vendor) |
| objections.md §1 | Insurer: "Most law-firm policies are reported silent" | Fixed | As guardrails §8 |
| objections.md §3 | "32% of corporate clients are reconsidering providers" | Fixed | Source: 32% have reconsidered or plan to within 12 months |
| objections.md §3 | McKinsey "prices about a quarter of fees on outcomes" | Fixed | Dated (late 2025) and attributed to McKinsey's own statement; later press reports differ (about a third) |
| objections.md §3 | Demand +4.2% in H1 | Fixed | Underlying data is Citi's, reported by Bloomberg Law |
| objections.md §3 | "vendors are moving to consumption pricing" | Fixed | Embellished plural: the cited source is one vendor (Legora) |
| objections.md §5 | "Current US law data show leverage rising" [TRI-LFFI-Q2-2026] | Fixed | Misread statistic: the Q2 report's leverage figure is non-equity to equity partner hours. Recited to TRI-LFFI-LEVERAGE-2026: associate demand leverage at a 17-year high (1.55, Q4 2025) |
| objections.md §5 | "PwC UK named the economy" | Fixed | Misread: PwC UK's managing partner cited both a sluggish economy and AI |
| objections.md §5 | PwC US CEO said resisters "have no place at the firm" | Fixed | Attribution drift: that phrase is the headline; Griggs's words were "not going to be here that long" |
| objections.md §6 | "capability is rented from vendors" | Removed / fixed | Unsourced connective; replaced with the sourced Ropes & Gray CIO buy-not-build statement. PwC investment dated FY2026 |
| objections.md §6 | "Colorado and others are pushing back" | Fixed | Made specific and sourced: California, Colorado and Illinois restrict fee sharing with ABS firms [BLOOMBERGLAW-AZ-2026] |
| objections.md §6 | Accenture consulting revenue +5% | Fixed | Period and local-currency figure added (fiscal 2026; +3% local currency) |
| objections.md §7 | "73% of in-house lawyers believe [firms keep the savings]" | Fixed | Population: 73% of those who knew whether their firms used AI |
| sources.md Part A | Conference column "Latest edition" | Fixed | Several listed events (Kantata Converge 17 Nov 2026, TRI forums) have not been held yet; column renamed "Latest or next edition" |
| sources.md Part A | ILTACON "recordings members-only" | Fixed | ILTA: logged-in library, or purchase for non-attendees |
| sources.md Part A | "Primary texts not reached: ABA Formal Opinion 512 (read through summaries)" | Fixed | Contradicted Part B: the full opinion was read via the LawNext-hosted PDF. SRA notice and NBER scope clarified |
| sources.md Part B | SRA-WARNING-2026 (URL is the SRA home page) | Fixed | Primary notice blocked; existence and 17 Aug 2026 date confirmed only through DWF Group (2026-08-21). Entry now says so |

## Structure checks

- Every source key cited in the six files resolves to a listed entry with a URL and date (in `sources.md` or the
  file's own Sources list). Module `#nn` references (acceptance-risk 11/12/14, quality-review 11/14/16, work-production
  23, firm-finance 07/08, scoping-pricing 11, delivery-management 12) match the YAML entries they describe.
- All relative links in the six files resolve. The links to `../professional-services/ARCHETYPE.md` in the assurance,
  tax and security ARCHETYPE.md files resolve.
- `archetypes/index.md` lists professional-services as Available with the 12 correct module ids. No change needed.
- ARCHETYPE.md Evidence column matches the validator's A/B counts for all 12 modules, and the strong/moderate/thin
  labels match the stated thresholds. "Only work-production and talent-learning have grade A" is correct (2 each).
- Table of contents is present in every file over 100 lines (guardrails 206, interview-guide 198, value-chain 128,
  sources 251). ARCHETYPE.md and objections.md stay at 100 lines. All files are under the 300-line limit.
- `python3 scripts/validate.py`: 0 errors. The 23 warnings are module A/B targets in YAML files, not these files.

## Sources that could not be reached

- **SRA** (all pages, Cloudflare challenge, including via r.jina.ai). The warning notice was confirmed only via DWF.
- **Legal IT Insider** (LEGALIT-LEGALGEEK-2026): bot check on both routes; only used as a Part A event example.
- **Bloomberg Law / Bloomberg Government** pages: partly paywalled; the quoted figures (19% undecided, no ROI
  benchmarks, 4.2% demand) were visible in the open text.
- **SPI Research** full report: paywalled; "the leak" is visible on the landing page.
- Blocked directly but read via r.jina.ai: APQC, Colorado General Assembly, Canadian Press/Castanet, Fox Rothschild,
  Global Legal Post, Illinois General Assembly, Karbon, People Matters.

## Error patterns seen

- **Population drift (most common, 7 cases):** survey populations widened or swapped (law firms called "legal-finance
  respondents"; senior legal leaders called "legal professionals"; a conditional subgroup reported as all in-house
  lawyers; all-industry RFP teams; leverage of non-equity partners read as junior leverage).
- **Attribution drift (2):** a headline paraphrase quoted as the CEO's words; an FT-reported boutique target presented
  without its firm type.
- **Unsourced connective claims (3):** "planned guidance", "capability is rented from vendors", "lag in finding cases".
- **Embellished qualifiers (3):** "vendors are moving" (one vendor); policies "silent" (no express exclusion);
  "management" referred (the firm was).
- **Misread statistic (2):** LFFI leverage measure; PwC UK's stated reasons for cutting graduate hiring.
- **Wrong or missing dates/periods (4):** McKinsey fee share undated; Accenture growth without period; upcoming events
  labelled "latest edition"; ABA 512 access described inconsistently across Part A and Part B.
- No forecasts presented as facts were found in these files. The NBER trial is correctly described as Google-run and
  funded, and vendor-commissioned surveys are now labelled where cited.
