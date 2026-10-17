# Method verification A: report

Stream M · Wave 1 · Verifier A · 2026-10-16

**Files checked** (in `plugins/transformation-advisor/skills/transformation-advisor/references/method/`):
`onboarding.md`, `frame.md`, `map.md`, `diagnose.md`, `interviewing.md`, `breakdown-and-rollup.md`.
Method: every cited URL was opened with `curl` (`pdftotext` for PDFs), with the `r.jina.ai` mirror for blocked pages.
Full papers were pulled where the cited page was only an abstract (arXiv v3 of WORKBank, METR, Wuttke, LLMREI; NBER PDF
of Brynjolfsson; Empson's accepted manuscript; KPMG SOX PDF). Claims were also traced back to the
`research/runs/wave1/method-*.md` inputs.

## 1. Counts

| | Count |
|---|---|
| Factual claims checked (figures, dates, attributions, regulatory points, forecasts) | 170 |
| Kept as written | 119 |
| Fixed (wording, figure, date, attribution, or a better source) | 48 |
| Removed | 3 |
| Build-only references replaced with self-contained wording | 11 |
| Source entries changed (new entries, dates, titles, URLs) | 22 |

All 81 distinct source keys plus the 3 assurance-module keys now used in these files (K-SOX30, CPAPA-ZANIN,
OPTRO-SURVEY) resolve to a listed entry with a URL and a date. Undated pages now say "undated; accessed 2026-10-16".
All six files are over 100 lines and each starts with a table of contents. All are under the 300-line limit (210–282
lines). `python3 scripts/validate.py` reports 0 errors in these files. The only current ERROR is
`archetypes/assurance/modules/soc-attestation.md` (308 lines), which belongs to another stream and was not touched.

## 2. Fixes and removals

| # | File | Claim (before) | Action | Reason |
|---|---|---|---|---|
| 1 | onboarding | "Self-placement runs high: 7% of leaders against 26% of individual contributors did not know…" | Fix | Misread statistic. Gallup measures awareness of adoption by role, not inflated self-placement. Now: 26% ICs, 16% managers, 7% leaders did not know; one person's view is not the scope's stage |
| 2 | onboarding | "Optimism bias; leaders hear about use second-hand [GALLUP]" | Fix | Attribution drift: Gallup says nothing about optimism or second-hand reports. Now: awareness differs sharply by role |
| 3 | onboarding | Trap "Leaders are further from daily use [GALLUP]" | Fix | Unsourced. Now: one person sees only part of the scope |
| 4 | onboarding | Managers are "the main adoption lever below leadership [GALLUP]" | Fix | Embellished. Gallup says broader adoption is "strongly associated" with manager support |
| 5 | onboarding | "Plan against the weakest dimension… [DELOITTE]" | Fix | Connective claim. Added what Deloitte actually reports: firms feel more prepared on strategy than on infrastructure, data, risk and talent |
| 6 | onboarding | "Every model reviewed puts its sharpest break at…" | Fix | Embellished qualifier. Now "the models used here", plus MIT CISR's evidence (stages 1–2 below industry average, 3–4 above) |
| 7 | onboarding | `#05` "vendor-published, confirmed by the team" | Fix | Provenance: the figures are self-reported by Reddit's CAE and republished by the vendor (use-case YAML notes) |
| 8 | onboarding | BCG "links engaged leadership to its top tier" | Fix | Made specific: nearly all C-level leaders in future-built firms use AI day to day (correlation) |
| 9 | onboarding, interviewing | "69% of interviewees mentioned stigma" | Fix | Scope: 69% of the general-workforce professionals (n=1,000 of 1,250) |
| 10 | onboarding | TR-2026 "undated" | Fix | Dated as the 2026 edition, page undated, accessed 2026-10-16 |
| 11 | onboarding, frame | MCKINSEY-SOAI-2025 "read via third-party copy", landing-page URL (blocked) | Fix | Better source. McKinsey's own PDF opened through the mirror; 88%/39%, 55%/20%, 82%/79% vs 50%, ≤10% agents per function all confirmed |
| 12 | frame | "VALUE-LEVERS" source key (no URL or date; cited the spec and research files) | Remove | Build-only and unresolvable. Replaced with inline wording: the seven levers are the advisor's working set, not a published standard |
| 13 | frame | Sage fixed fee "leaves 5 idle hours" | Fix | Embellished. Sage: the firm "gained five hours of capacity, but only if you have somewhere productive to put them" |
| 14 | frame | Full-potential pass "revenue, operational and technology levers" [BAIN-GPER] | Fix | The press release only says "from full potential diligence to execution on Day 1"; quoted that and added BAIN-DILIGENCE for the levers |
| 15 | frame | BCG "calls exclusive technology ownership a marker of stagnating firms" | Fix | Now quotes the exhibit: "a key indicator of stagnating companies" |
| 16 | frame | "Would finance accept this number?" → "Self-reported time saved versus measured value [WHARTON-2025]" | Fix | Connective claim. Wharton 2025 reports 72% formally measure Gen AI ROI, mostly as productivity gains; now says that |
| 17 | frame | Capacity stance → "how staff will read the project [WHARTON-2026]" | Fix | Connective claim. Added what Wharton says: rebuild how work is managed rather than cut headcount |
| 18 | frame | "KPMG's SOX survey… 16 hours in FY2024 for management SOX programmes [K-SOX30]" (key unlisted) | Fix | Confirmed in the KPMG PDF (12 h FY2022 → 16 h FY2024); wording aligned and a K-SOX30 entry added |
| 19 | frame, breakdown | BDEMERSON-2026 title and date "2026-08-16" | Fix | Page title is *The Value Creation Plan: How PE Firms Turn a Thesis into an Exit*; published 2026-07-06, modified 2026-08-16 |
| 20 | frame, interviewing | OPENAI-ACADEMY-2025 title "Run a use case discovery workshop" | Fix | Page title is *Use Case Discovery Workshop Playbook*; updated 2026-06-12 |
| 21 | map | "In one insurance data-entry study…" | Fix | It is one NN/g practitioner's project anecdote, not a study |
| 22 | map | CPAPA-ZANIN used but listed only through the module | Fix | Full entry added (trade press, author is a SOX-tooling vendor CEO, 2026-08-18) |
| 23 | diagnose | Speed-up ceiling cited to [NBER-ACEMOGLU] as if it were the source | Fix | Attribution. The formula is plain share-times-saving arithmetic; Acemoglu applies the same logic (Hulten) economy-wide. Now worded that way |
| 24 | diagnose | Workday "about 37–40%" of AI time savings went to rework | Fix | The cited release says "nearly 40%"; the 37% trade-coverage figure is not the cited source |
| 25 | diagnose | WORKDAY-2026 entry note "about 37% in trade coverage" | Remove | Uncited secondary figure |
| 26 | diagnose | HBS: "19 points less likely to be correct" | Fix | The cited HBS page says "19% less likely to produce correct solutions"; wording now matches |
| 27 | diagnose | "Review is now where most auditor time goes [CPAPA-ZANIN]" | Fix | Context dropped: a vendor CEO says this about an agent-based setup. Now attributed |
| 28 | diagnose | "46% of one vendor's survey respondents spend more time validating AI output" | Fix | Misread: 46% of respondents *report that employees* spend more time reviewing, validating or correcting AI output |
| 29 | diagnose | Kingman: 12.5% more load at 80% "roughly doubles" waiting (4× → 9×) | Fix | 9/4 = 2.25: "more than doubles" |
| 30 | diagnose | Heatmap had no SOC unit, while `breakdown-and-rollup.md` puts SOC and attestation in wave 1 | Fix | Internal inconsistency; added an illustrative SOC row (wave 1) |
| 31 | diagnose | NBER-BRYNJOLFSSON date "2023" | Fix | Issued 2023-04, revised 2023-11 (14% average, 34% novices confirmed) |
| 32 | diagnose | CPAPA-ZANIN and OPTRO-SURVEY used, listed only through the module | Fix | Full entries added (Optro release 2026-10-08) |
| 33 | interviewing | "Ten to fifteen minutes per topic… [ANTHROPIC-INTERVIEWER]" | Fix | Misread: Anthropic's interviews lasted 10–15 minutes in total. Now: the default is advice; interviews of that length worked in one vendor study |
| 34 | interviewing | Empson: "offer the topic list in advance" | Remove | Not found in the abstract or the accepted manuscript. Preparation, an easy opening and going deeper are supported and kept |
| 35 | interviewing | "Not only volunteers [MIT-NANDA]" | Fix | Attribution: MIT NANDA flags self-selection bias in its own sample (§8.2); now says so |
| 36 | interviewing | Trap "Sampling only the willing… [MIT-NANDA]" | Fix | Same as 35 |
| 37 | interviewing | Trap "simulations only for rehearsal [ATAEI-2024]" | Fix | Attribution drift: Elicitron argues for simulated users. Now: simulated users can surface ideas [ATAEI], but they are not facts about this organization |
| 38 | interviewing | CHOPRA-2026 "version 2026-03-09" | Fix | CESifo released it in 2026-06; the authors' version is dated 2026-03-09. Both shown |
| 39 | breakdown | Shared definitions: "inconsistent definitions are the usual reason roll-up fails" | Fix | Embellished. Simon-Kucher says comparison needs standardized KPIs and consistent reporting |
| 40 | breakdown | FTI: "PE firms that ran AI purely company by company found it hard to reuse" | Fix | FTI's actual claim: an operating model built for one portfolio company may not extend to the others (consultancy view) |
| 41 | breakdown | "Owners publish their best cases first [VISTA]"; "survivor bias [VISTA]" | Fix | Connective claim. Vista's figures cover selected portfolio companies; now says that and asks for the denominator |
| 42 | breakdown | Unit status listed as "complete, desk review, in progress, not started" | Fix | Aligned with the `status` values used in §9: `complete`, `desk-review`, `in-progress`, `not-started` |
| 43 | all | 12 lexicon, toolkit and guide entries marked "undated" | Fix | Added "accessed 2026-10-16" so every entry carries a date |

Rows 1–43 cover 51 actions: 48 fixes and 3 removals (rows 12, 25 and 34). Rows 9, 11, 19 and 20 are each counted once per
file they touch.

**Build-only references replaced (11):** "The spec lists… under Adopting" → "The advisor's stage model lists…";
"Emphasis (spec §3.2, sharpened)" → "Emphasis"; "built from the spec's reference persona" → "a typical audit-partner
profile"; "Field names follow spec §5.3" → "follow the plan schema (`../schemas/`)"; "working heuristics from the
maturity research" → "working heuristics… no study found follows firms through these stages"; frame "§9 rules forbid
targets" → "rule 1 in `SKILL.md`"; interviewing "spec §9 rule 8" (×2) → "rule 8 in `SKILL.md`" / "[rule 8…]";
breakdown "spec §9 rule 4" and "spec §9 rule 2" → "rule 4 / rule 2 in `SKILL.md`"; VALUE-LEVERS key (row 12). This
matches editor B's convention ("rule 3 in `SKILL.md`"). No research-file paths remain. "Pilot" in these files always
means an AI pilot (a domain term), never the build pilot, so it stays.

**Kept after checking (selected):** TR 34% unapproved use; Microsoft 78% BYOAI; Anthropic 65/35 vs 47/49; Gallup
n=23,068 and date; Sadiq (five-level trend, no standard terminology); BCG 5%, n=1,250, 79% unstructured data, >40% vs
19% shared ownership, agents "not the starting point"; MIT CISR 7%; Deloitte one in five, 66%/20%, n=3,235, 2026-01-20;
ILTA "nearly 60%" Copilot piloting; Litify stage 3 "ROI not yet proven"; OpenAI irreversible actions and variance;
BCG Trust Protocol shadow mode and promotion thresholds; IMDA v1.5 (2026-05-20) override-rate monitoring; ICAEW six
governance questions; Sage 8 → 3 hours; Bain diligence (<10% of 300+ in revolution, about half augmentation, similar
knowledge tasks, who benefits); Acharya (UK 1996–2004, draft 2009-01-02); MIT NANDA hypothetical $100 to sales and
marketing, "easier metric attribution"; Wharton 35% vs 13%; Bernard (under half recalled correctly); planning fallacy
33.9 vs 55.5 days; NN/g insurance example; METR 24% / 20% / +19%; Brynjolfsson 14% / 34%; WORKBank 46.1% of 844 tasks,
v3 2026-02-01; KPMG 82% data quality, n=130; Anthropic labor "observed exposure"; Chopra 18,000+ questions, 766
interviews, >95% open/neutral/relevant, probing drives the gain; Wuttke (88% of follow-up violations by the AI, judging
remarks); Geiecke (one question per message hard to follow consistently); LLMREI mistake list; Deloitte PE "reuse
validated use cases, don't scale frontier ones"; Bain midyear (VCP "runs out of steam", concentrate resources);
McKinsey "the best use case is the reuse case"; Canaries and Hosseini on junior roles; all queue-rule and worked-example
arithmetic (11.5 h vs 20 days; 11 h / 160 h ≈ 7%; u/(1−u) = 1, 4, 9, 19).

## 3. Sources that couldn't be reached directly

None had to be removed. Reached by another route:
- **MCKINSEY-SOAI-2025:** landing page blocked; McKinsey's own PDF read through `r.jina.ai` and cross-checked against the third-party copy. URL updated to the PDF.
- **BCG-AGENTS-2025, SADIQ-2021, WHARTON-2026:** HTTP 403; read through `r.jina.ai`. Wharton returns only the landing page, but that page carries the 35% vs 13% figure and the headcount advice.
- **BISPO-2022 (PMC), CHOPRA-2026 (CESifo):** script-gated; read through `r.jina.ai`.

Only partly verified (page reached, specific point not fully confirmed):
- **PMMANIFESTO-2012:** landing page only. The manifesto's "question-driven log extraction" principle is standard, but the PDF was not opened.
- **ALTER-2014, KECHT-2026:** abstract and table of contents only (already labelled "abstract read").
- **KANBANU-LITTLE-2022:** the PDF text layer is garbled; the "Little's Law assumptions: stable system" slide is legible, the flow-efficiency slide only partly.
- **TR-2026:** landing page; the report itself was not read (the 34% figure is on the page).

## 4. Error patterns seen

| Pattern | Seen? | Instances |
|---|---|---|
| Misread statistics | Yes | Gallup awareness read as self-placement (1); Optro 46% (28); 10–15 minutes per topic (33); 69% scope (9) |
| Attribution drift | Yes | Gallup "second-hand" (2); Elicitron cited against its own thesis (37); Acemoglu as the source of Amdahl-style arithmetic (23); Bain GPER levers (14); FTI (40); Zanin context (27) |
| Embellished qualifiers | Yes | "Every model reviewed" (6); "main adoption lever" (4); "usual reason it fails" (39); "study" for an anecdote (21); "idle hours" (13); "roughly doubles" (29) |
| Unsourced connective claims | Yes | Deloitte weakest dimension (5); Wharton links in two expert moves (16, 17); Vista survivor bias (41); Gallup trap (3) |
| Wrong dates | Yes, minor | BD Emerson (19); Chopra (38); OpenAI Academy (20); Brynjolfsson (31); TR undated (10) |
| Forecasts presented as facts | No | No forecasts in these six files. Heuristics are already labelled ("advisor heuristic", "not tested thresholds") |

For the briefs: (a) a figure from the module files should carry its source key into the method file's own source
list; (b) when a source is one person's anecdote or a vendor CEO's opinion, say so in the sentence; (c) check that each
cited source argues *for* the point it supports (Elicitron, Acemoglu).

## 5. Consistency with editor B's files

Checked against `reimagine.md`, `prioritize.md`, `business-case.md`, `plan-and-control.md` and `people-and-change.md`.

**Consistent:**
- Journey-stage names and order (Curious, Experimenting, Adopting, Scaling, AI-native) and lower-case YAML values.
- Lever ids, the six scoring weights and their defaults. Prioritize's worked example uses frame's changed weights (risk 0.20, time to value 0.05).
- `units` fields (`id, name, owner, wave, status`), `rolled_up_from`, `phase_completed` / `next_phase`.
- The number labels (reported, from record, observed).
- "Capacity stance" (provisional, set in Frame) versus "capacity choice" (per opportunity, in Make the case); B refers to "the Frame capacity stance".
- Behavioral rules cited as "rule N in `SKILL.md`".
- Delegation: prioritize's stage gate parks delegate options at Curious and Experimenting, and treats a delegate option at Adopting as a big bet. Reimagine's example and prioritize both point to "the delegation gates in `onboarding.md`". Plan-and-control's "at most one or two bounded delegated workflows, in shadow mode" and its shadow → supervised → monitored tiers match gates 4–5.

**Inconsistencies (not fixed; B's files):**
1. **`reimagine.md` §2, Adopting row.** It says "Delegate only bounded, low-risk outcomes with explicit human checkpoints and a control plan". It neither names nor links the five gates: in production with owner and baseline; written criteria with examples; reversible actions or approval of irreversible ones; shadow-mode start with promotion rules; override tracking. "Low-risk" is an extra criterion not in the gates. Suggest: "…only when the five delegation gates in `onboarding.md` hold".
2. **`MCKINSEY-SOAI-2025` in B's files** still says "read via a third-party copy" and points to the blocked landing page. McKinsey's own PDF is reachable (URL now in `onboarding.md` and `frame.md`).
3. **`BDEMERSON-2026` in B's files:** title "Private equity value creation plan", dated 2026-08-16. The page title is *The Value Creation Plan: How PE Firms Turn a Thesis into an Exit*, published 2026-07-06 and updated 2026-08-16.
4. **Source-list format differs.** B uses backtick key + em dash; A uses bold key + colon. Both are readable, but one style across the method folder would be cleaner.
5. **`#03` (grade C).** `prioritize.md` parks `ct-03` at team scope, while `breakdown-and-rollup.md`'s roll-up example merges `#03` into one parent opportunity. Not a contradiction (roll-up merges; Prioritize still scores and may park it), but the two examples could reference each other.
6. **`WORKDAY-2026`:** B lists n=3,200; my files do not state n. Not checked in B's files.

Note: `reimagine.md` and `prioritize.md` were modified in the working tree by another process during this run; I did not
edit them.
