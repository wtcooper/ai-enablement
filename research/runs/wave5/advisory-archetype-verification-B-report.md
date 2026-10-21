# Advisory archetype verification, part B

Run date 2026-10-21. Files checked: `ARCHETYPE.md`, `interview-guide.md`, `value-chain.md`, `guardrails.md`,
`objections.md` and `sources.md` in `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/`.
I opened all 80 source keys these files cite, plus 14 more that appear only in the Part A tables of `sources.md`. I used
curl, pdftotext, the eCFR renderer API (for 17 CFR 210.2-01 and 16 CFR 314), r.jina.ai for blocked pages, and one web
search to find a URL for the Cuatrecasas note.

## Counts

| | Count |
|---|---|
| Claims checked (figures, dates, attributions, regulatory points, forecasts, use-case cross-references) | ~165 |
| Kept as written | ~125 |
| Fixed | 40 |
| Removed | 0 |
| Part B source rows checked to confirm the key resolves and has a URL and date | 80 |

Structure:
- Every key cited in the five content files resolves in `sources.md` with a URL and a date. The one gap was
  CUATRECASAS-AIOMNIBUS-2026, which had no URL; it is now fixed.
- `ARCHETYPE.md` is still 100 lines, so it needs no table of contents. All the other files are under 300 lines and have
  one.
- `validate.py` reports 0 errors. Its warnings are only the module-level grade-mix targets.
- The ARCHETYPE Evidence column matches the validator's A/B counts for all seven modules: 12/24, 12/23, 5/16, 3/15, 5/15,
  2/14 and 6/17. CAS `#01` is the only grade A entry, as the file says.
- `archetypes/index.md` lists advisory with all seven modules as Available, and the `../professional-services/ARCHETYPE.md`
  link resolves.
- All the module use-case ids cited in value-chain, objections and interview-guide exist and match their topics.

## Fixes

| File | Claim | Fix | Reason |
|---|---|---|---|
| ARCHETYPE | "No regulator has issued AI guidance written for most of this work" | Now "The research found no regulator AI guidance…" | Absence stated as fact (unsourced connective) |
| ARCHETYPE | CAS "is the base many firms grow advisory from" | Now "can seed wider advisory: Withum built its advisory practice out of CAS" | The source describes one firm (Withum's Bourke), not "many firms" |
| ARCHETYPE | "firmwide assistants (RSM nearly 20,000 people)" | Now "Microsoft 365 Copilot for nearly 20,000 professionals" | Says what the source actually reports |
| ARCHETYPE | "live dashboards replace periodic packages" | Now "real-time client dashboards built with AI" | "Replace periodic packages" is not in the source (embellished) |
| ARCHETYPE | "AI-native roll-ups [ACCTODAY-CURRENT-2026]" | Now "AI-led roll-ups (Current, formerly Crete)" | Current is a PE-backed network upgrading firms with AI, not AI-native |
| interview-guide | A firm's systems withheld a client number "until independence was cleared" | Now "until the engagement was entered in the independence-monitoring system" | Misread of the 2016 JofA account |
| interview-guide | "AI-using middle-market leaders… 40% take budget from external consulting" | Now "middle-market companies raising AI spend… 40% report reallocating budget from external consulting" | Wrong survey population |
| interview-guide | CAS "the base many firms grow advisory from" | Now "Withum grew its advisory from CAS" | Same over-generalization as in ARCHETYPE |
| interview-guide | Proposed Rule 707 | Adds "published draft withdrawn May 2026, revised draft under study" | Status was out of date (USCOURTS-EVID-2026, p. 1) |
| value-chain | Targets "struggle to pull data however fast the adviser's tools are" | Now "may still be held up by targets with limited transaction experience" | The source says "may still be bottlenecked" (embellished) |
| guardrails §1 | "The AICPA says…" (twice) | Now "A JofA article by the AICPA Professional Ethics Division…"; "No AI-specific independence ruling exists" changed to "was found" | Attribution drift: the article is staff-written in JofA, not an AICPA pronouncement |
| guardrails §1 | "No standard or regulator has issued AI guidance…" | Now "The research found no…" | Absence stated as fact |
| guardrails §3 | "Five carry an exception…; management functions carry none" | Now "The first five ((i)-(v))…; the other five, including management functions, carry none" | The old wording implied only management functions lack the exception |
| guardrails §3 | "In an APS the attest firm treats the affiliated advisory firm's services as its own" | Now names the 2016 example (Mayer Hoffman McCann with CBIZ) | One firm's account was stated as a general rule |
| guardrails §3 | Billing system and client number; "PE affiliates are the hardest to monitor" | Now "until the engagement was entered"; RSM's independence director called PE affiliates "the most significant challenge" (2016) | Misread, plus attribution |
| guardrails §4 | AICPA contingent-fee scope | Adds preparing an original or amended return or a refund claim | Rule stated too narrowly (NYSSCPA-CONTFEE-2015) |
| guardrails §5 | "some sellers bar uploads or require consent" | Now "parties now negotiate clauses that bar uploads to public AI platforms or require prior written consent" | Matches the KJK wording |
| guardrails §5 | "No federal law or professional standard requires CPAs to disclose AI use" | Now dated "as of April 2025"; adds the California and Utah state laws and the IRS OPR disclosure expectation | Stated too broadly; missing date |
| guardrails §6 | Forensic row: "proposed Rule 707 / proposal" | Now "published draft withdrawn, revised draft under study"; cites USCOURTS-EVID-2026 | Out-of-date regulatory status |
| guardrails §7 | Kohls and Weber failures "not on AI use as such" | Now adds that *Weber* held counsel must disclose AI use and that AI evidence may face a Frye hearing | Overstated: *Weber* did set an AI-specific duty |
| guardrails §7 | Rule 707 "is not law" | Adds that the May 2026 committee withdrew the published draft for further study | Out of date |
| guardrails §2 | Courts row | Adds USCOURTS-EVID-2026 | Current source for the rule's status |
| objections §1 | "most advisory clients are not audit clients [SEC-RULE2-01-2026]" | Now "they apply only where the firm or an affiliate audits or attests for the client" | The SEC rule says nothing about "most clients" (unsourced connective) |
| objections §1 | Courts objection | Notes *Weber*'s disclosure duty and the withdrawal of Rule 707 | Same as guardrails §7 |
| objections §2 | Verification "26% of finance staff's time" | Now "270 CFOs and finance leaders… 26% of work time verifying or correcting AI output" | Adds the population and the measure |
| objections §2 | "Forvis Mazars US says exactly this" | Now quotes "thin and unsupported conclusions" for firms over-relying on automation | Embellished |
| objections §2 | "Deloitte Australia repaid" | Now "agreed to repay" | The source (Oct 2025) reports agreement, not payment |
| objections §2 | "balances drift more than 15% after months unattended" | Now "vendor-run benchmark… diverged by more than 15% after several months" | Provenance missing; "unattended" was added |
| objections §3 | "named partners call margin versus price cut an open question"; AI cost attribution | Now one named RSM partner; KPMG's advisory vice chair named for attribution | Attribution drift |
| objections §3 | "78% of corporate clients rate AI-enabled quality essential" | Now "very important or essential", clients of legal and accounting firms | Misread statistic |
| objections §3 | "Intent is high (69%…)" for value pricing | Now "69% of tax professionals expect to move to value-based, hybrid or fixed-fee billing" | Statistic reported as something it doesn't measure |
| objections §3 | "$1B or more" | Now "multiyear AI investments of $1B or more" | Adds the timeframe (3 to 5 years) |
| objections §4 | "1,052 transactions" | Now gives the definition: PE-linked firm transactions worldwide, 2015-2025 (177 direct, 875 roll-ups) | PE deal count without its definition |
| objections §4 | "advisory slowed at the largest firms in 2025" | Now "in Accounting Today's 2025 Top 100 data growth at the largest firms slowed largely on advisory declines" | Wrong date frame |
| objections §5 | "fewer entry-level hires" | Now "lower early-career employment" | Matches what Canaries measures |
| objections §5 | "ICAEW cites the 2008 experience" | Now "a consultant quoted by ICAEW recalls…" | Attribution drift: the source is Jess Larsen relaying a firm's account |
| objections §5 | "over 57% of dealmakers" | Adds "of 400 dealmakers in a vendor survey" | Provenance |
| sources.md | CUATRECASAS-AIOMNIBUS-2026 had no URL | URL added; the note confirms OJ publication on 2026-07-24 and the 2 Dec 2027 date | Structure |
| sources.md Part A | "Proposed Rule 707" | Now gives the withdrawn-and-revised status | Out of date |

## Sources that couldn't be reached

- **BVR-DISCOVERY-2026, BVR-NACVA-2026, BVR-COGDEBT-2026:** BVWire returned 403, and r.jina.ai later blocked anonymous
  requests. I kept the guardrails §7 line ("prompts and drafts could be discoverable, panellists say"). It matches the
  valuation module notes, but I did not re-confirm it here.
- **EUR-Lex** (WAF challenge): I confirmed the EU Omnibus through the Cuatrecasas page.
- **SBA SOP 50 10 8.1 .docx** (it redirected to the new site): I relied on QoEAgent's quotation of Appendix 15, which the
  file attributes to QoEAgent.
- **Reached only by another route:**
  - eCFR (SEC Rule 2-01, FTC Safeguards) through the renderer API.
  - PCAOB, Crowe, Penrose, the SEC exam priorities and BVR-AICPAAIGUIDE through r.jina.ai.

## Error patterns seen

- **Attribution drift** (the most common): staff articles cited as "the AICPA says"; a consultant's anecdote cited as
  ICAEW's view; one partner cited as "partners"; one firm generalized to "many firms" or to all APS firms.
- **Misread statistics:** the 69% figure (billing-model shift among tax professionals) presented as value-pricing intent;
  "very important or essential" shortened to "essential"; survey populations shifted (AI users versus AI-spend
  increasers).
- **Embellished qualifiers:** "exactly this", "however fast", "unattended", "replace periodic packages", "repaid".
- **Unsourced connective claims:** "most advisory clients are not audit clients"; absences of guidance stated as fact.
- **Stale regulatory status:** Rule 707's published draft was withdrawn in May 2026. The archetype files still called it
  simply "proposed", although the valuation module already had this. Agent A's files (frontier, disruption) may carry the
  same stale wording.
- **Dates:** the Woodard advisory slowdown was placed in the wrong year frame. Part B dates for the cited keys matched the
  publication metadata.
- **Forecasts presented as facts:** none found in these files. The outcome-pricing and IVS dates are framed as direction
  or plans.
