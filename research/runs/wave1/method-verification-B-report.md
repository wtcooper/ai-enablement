# Method verification B: report

Verifier B. Date: 2026-10-16.
Brief: `research/briefs/templates/verifier-docs.md` (error patterns from `verifier.md`).
Files checked, all in `plugins/transformation-advisor/skills/transformation-advisor/references/method/`:
`reimagine.md`, `prioritize.md`, `business-case.md`, `plan-and-control.md`, `people-and-change.md`, `index.md`.
Traced against `research/runs/wave1/method-*.md` and `method-synthesis-B-report.md`.

## Counts

| File | Claims checked | Kept | Fixed | Removed | Source-entry fixes |
|---|---|---|---|---|---|
| reimagine.md | 38 | 35 | 3 | 0 | 3 |
| prioritize.md | 26 | 22 | 4 | 0 | 2 |
| business-case.md | 32 | 26 | 6 | 0 | 2 |
| plan-and-control.md | 37 | 29 | 8 | 0 | 3 |
| people-and-change.md | 34 | 28 | 6 | 0 | 2 |
| **Total** | **167** | **140** | **27** | **0** | **12** |

- "Claims" means figures, dates, attributed statements, regulatory points and forecasts. The worked-example
  arithmetic counts too: all ten prioritize weighted scores, the 180–1,190 hour range and the 1,500–2,400
  hour baseline. All of it recomputes correctly.
- `index.md`: all eleven method files listed, every link resolves, and the phase mapping is right. Two
  trigger descriptions were reworded to match the target files' own "read this when" lines.
- One build-only reference removed, in `reimagine.md` §3.1 (see the table).
- "Pilot" in these files always means a client's trial of a tool or workflow, not the build pilot, so it was
  kept. No "spec", "spec §" or research-path references remain.
- `python3 scripts/validate.py`: 0 errors in these six files, and the `index.md` link check passes. The one
  remaining ERROR is outside both verifiers' scope:
  `archetypes/assurance/modules/planning-risk-assessment.md` is 307 lines against a limit of 300, from a
  concurrent edit.
- Every source key used is listed, and every listed key is used (checked by script).
- Every source entry now carries a URL and a date. Where the page shows no date, the entry says
  "accessed 2026-10-16".
- All files with more than 100 lines have a table of contents. All are under 300 lines (255–276).

## Fixes

| File | Location | Was | Now | Reason |
|---|---|---|---|---|
| reimagine | §1 | High performers "were 55% likely to report" redesigned workflows | 55% of AI high performers reported fundamentally redesigned workflows, against 20% of others | Misread statistic: it is a share of respondents (Exhibit 11, n=109 vs 1,644), not a likelihood |
| reimagine | §2 stage table | "broader delegation belongs to Scaling [BCG-GAP-2025]" | Labelled an advisor rule; BCG cited only for agent use concentrated in the most AI-mature firms | Attribution drift: BCG does not state the stage rule |
| reimagine | §3.1 recording rules | "a single merged scale proved ambiguous when reviewers classified the same cases" | The two dimensions are independent questions; one merged scale blurs them | Build-only reference (build-pilot reviewer test) |
| reimagine | §5 move 9 | Netjes heuristics "(remove, merge, parallelize, triage, full population)" | The source's own heuristics: task elimination, composition, parallelism, triage, knock-out ordering | "Full population" is not a Netjes heuristic |
| prioritize | §5 move 6 | "Upend initiatives more than twice as likely…" | Adds the source definition (new value propositions, products or markets) and "functions investing in" | Precision, so the figure isn't misread |
| prioritize | §5 move 11 | "Finance-signed baseline before leaving pilot" | Finance-signed *case* (expected return) before *production*; Dell example: sign-off by the finance partner and the BU head | The source (Roese interview) says an ROI signed off before production, not a baseline |
| prioritize | §6 trap | 45% vs 20% with no base | Adds "survey of 204 finance leaders" | Base added; the release headline frames these as shares of CFOs, the body as shares of investment |
| prioritize | §7 ranges | "PwC calls its year-one savings 'not that drastic yet'" under `ct-07` | PwC's *overall* year-one AI savings in assurance | Attribution drift: the quote is not about evidence matching (archetype module §evidence, YAML #01) |
| business-case | §3.2 | DBT "found no evidence that time savings improved productivity" | "no robust evidence…, though measuring that was not a main aim" | Embellished qualifier: the source says "robust" and states the limitation |
| business-case | §3.2 step 4 | Process cap cited to [NBER-ACEMOGLU-2024; LEI-PEPERKAMP-2026] | Cited to LEI; Acemoglu named as applying the same share-of-tasks logic economy-wide | Attribution drift: Acemoglu is macro (Hulten's theorem), not a process rule |
| business-case | §3.2 | "Only 7% of HR leaders … said their organization gives guidance" | "In a Gartner survey of 114 HR leaders, only 7% of organizations gave employees guidance" | Base added; wording matches the release |
| business-case | §3.6 | "Leaders tracking at least one growth measure…" 35% vs 13% | Companies measuring AI against growth outcomes vs efficiency alone | Matches the Wharton page; the counters (35, 13) were read from the page HTML |
| business-case | §3.7 | [BDEMERSON-2026] cited for "no two units bank the same capacity" | Citation moved to the bridge format; the double-counting check stands as advice | BD Emerson does not discuss double counting |
| business-case | §7 evidence | PwC quote under `#07` evidence | PwC's overall year-one assurance savings | Same attribution drift as prioritize |
| plan-and-control | §3.2 | 100-day plan "mostly drafted during diligence" | "often drafted during diligence" | Embellished: the source says plans are "most likely created" in diligence or after acquiring |
| plan-and-control | §3.4 autonomy tiers | Three tiers (shadow, supervised, monitored) | Shadow, supervised, guided; BCG's fourth tier (full autonomy) only for mature, low-risk work; 90% threshold given as illustrative | The source has four tiers with different names |
| plan-and-control | §3.4 evaluation set | "20–30 real cases (advisor heuristic)" | "Start with 20–50 real cases drawn from real failures", cited [ANTHROPIC-EVALS-2026] | The source gives a sourced figure, so it replaces the heuristic |
| plan-and-control | §3.4 change triggers | Cited [ANTHROPIC-MANAGED-2026] only | Adds [ANTHROPIC-EVALS-2026] (regression evals, new models); managed-agents cited for "assumptions go stale as models change" | The managed-agents post does not say to re-run evals |
| plan-and-control | §3.5 | "licences, pilots and use cases live are activity" | "counts of pilots, tools rolled out or use cases in production" | Wording matches the Gartner CFO release |
| plan-and-control | §5 move 7 | "A 2025 survey attributed 67%…" | "A 2025 survey of private-equity investors…" to controllable causes | Population added |
| plan-and-control | §5 move 10 | "practitioners expect 3–6-month plan reviews to replace annual ones" | The share of PE firms reviewing every 3–6 months is expected to rise from 20% to 39% | Embellished: annual reviews still 42% |
| plan-and-control | §7 90 days | "Adopting markers (one workflow with an owner…)" | Experimenting exit criteria in `onboarding.md` | Cross-file accuracy: that list is the Experimenting exit row |
| people-and-change | §3 | NY Fed 4% layoffs (no period) | "in the past six months" | Period added |
| people-and-change | §3 | "55% of a general-workforce sample … and 69% of professionals mentioned stigma" | Both figures from the general-workforce sample (n=1,000) | Misread population: the 69% is the same sample |
| people-and-change | §5 table | Wharton "leaders tracking a growth measure" | As in business-case | Matches the source |
| people-and-change | §5 checks | "Klarna cut customer-service staff largely through attrition…" | Hiring freeze, shrinkage mostly by attrition (company-wide), CEO's "lower quality", rehiring agents | The attrition figure was company-wide headcount |
| people-and-change | §5 checks | "half of firms citing AI for cuts will rehire for similar work" | Adds "often under new job titles" and "made in a customer-service context" | Headline scope and wording from the iTnews report |
| people-and-change | §6 | Junior-task audit cited to TR Institute | Labelled advisor synthesis; TR cited for junior work serving capacity, risk and training together | Unsourced connective claim: the source has no audit method |
| index | onboarding, interviewing rows | Trigger wording | Aligned with each file's own "read this when" line | Consistency |

Source-entry fixes (12):
- New or updated dates: AZURE-PATTERNS (updated 2026-02-12); IMDA-MGF (updated 2026-06-05); HDR-AIE ×2
  (2013-12-26, updated 2026-01-20); TOCI-5FS (© 2021); FORRESTER-TEI (updated 2024-10-31); LEI-KAIZEN
  (updated 2023-02-02); BRIDGES-ND (updated 2020-03-12).
- Marked "accessed 2026-10-16" because the page shows no date: NIST-CTRL, PROSCI-ADKAR.
- GLOVER-2015: corrected title.
- MCKINSEY-SOAI: provenance note now gives the exhibit number.

## Sources that could not be reached directly

| Source | What happened | How it was verified |
|---|---|---|
| McKinsey, *State of AI 2025* | 403 to curl, r.jina.ai and Wayback | Full third-party copy of the report (rivista.ai PDF), Exhibit 11: 55 vs 20, 2.8× |
| Gartner releases (agentic 40%, HR 7%, CSO, CFO1) | 403 to curl; plain jina returned a tracker stub | r.jina.ai with the browser engine: full text read |
| Gartner CFO2 (2026-07-20) | Blocked on all routes at gartner.com | Same release on Gartner's own `gcom.pdo.aws.gartner.com` host: 45%/20%, n=204, "Upend" more than twice as likely |
| McKinsey *One year of agentic AI*; BCG *agents* | 403 / timeout | r.jina.ai |
| Wharton 2026 report | 403; figures render as animated counters showing "0" | r.jina.ai HTML: `data-counter-value` 35 and 13 |
| Netjes et al. 2007 (vdaalst.com) | 503 | r.jina.ai |
| Wayback Machine | Connection reset for every request | Not used |

Not independently reopened (taken from the inputs or the archetype module):
- the Glover sample (65 events, manufacturing): the abstract was truncated;
- the dates of Deloitte PE (2026-04), Microsoft WTI (2026-05-05) and Wharton (2026-10-13);
- the CFODIVE-PWC quote and IFIAR 31%: cited "via the archetype module", which has its own verifier;
- Kotter's steps: secondary, already flagged;
- HBR Davenport: summary only, already flagged.

## Error patterns seen

- **Misread statistics.** Two cases:
  - McKinsey's share of respondents was written as "55% likely".
  - Anthropic Interviewer: two figures from one sample were attributed to two different populations.
- **Attribution drift** (the most common pattern). Six cases:
  - the PwC "not that drastic yet" quote used as evidence for evidence matching;
  - BD Emerson cited for double counting;
  - Acemoglu cited for a process rule;
  - the managed-agents post cited for eval re-runs;
  - "full population" added to the Netjes heuristics;
  - BCG cited for an advisor stage rule.
- **Embellished qualifiers.** Four cases:
  - Simon-Kucher "replace annual";
  - Grant Thornton "mostly";
  - DBT "no evidence", with "robust" and the limitation dropped;
  - Deloitte's "ROI sign-off before production" turned into "baseline before leaving pilot".
- **Outdated or simplified framework.** BCG's four autonomy tiers were cut to three and renamed. A sourced
  eval-set size (20–50) had been replaced by an unsourced heuristic (20–30).
- **Unsourced connective claims.** Two cases:
  - the junior-task audit method;
  - the Adopting/Scaling delegation split. Both are now labelled advisor synthesis or advisor rule.
- **Wrong or missing dates.** Seven undated source entries; one wrong title. No wrong publication dates
  were found: the 40-odd page dates checked all match.
- **Forecasts presented as facts.** None found. The Gartner 40% and rehire forecasts are already labelled
  as forecasts.

For the briefs: the synthesis prompt should require (a) the respondent base for every percentage and (b) a
check that a quote sits under the use case it describes. Most fixes here were base or population drift, not
wrong numbers.

## Cross-file inconsistencies (for the other verifier or a later pass; not edited)

1. **Capacity framing.**
   - `frame.md` (expert-move table: "State the capacity stance early") lists "absorb through hiring pace"
     as a third stance.
   - `people-and-change.md` §5 classes hiring pace and attrition as `reduce`.
   - `business-case.md` §3.2 uses "absorbed" for leaked time that counts as zero.
   - Suggest `frame.md` say "reduce through hiring pace", or drop "absorb".
2. **Workday figure.** `diagnose.md` says "about 37–40%"; my files use the primary release's "nearly 40%".
   Suggest `diagnose.md` use "nearly 40%".
3. **Wharton wording.** `frame.md` says "35% strongly positive ROI among leaders tracking a growth measure
   against 13% tracking efficiency only". The source says companies measuring against growth outcomes
   versus efficiency alone. This is minor; align if convenient.
4. **Undated-source notes.** `diagnose.md` marks TOCI-5FS "undated; accessed"; `prioritize.md` now gives
   "© 2021 (accessed 2026-10-16)". Both are acceptable.
5. **Cross-references from my files hold:**
   - `onboarding.md`: the five delegation gates, and gates 1 and 2 failing at Experimenting;
   - `onboarding.md`: the Experimenting exit criteria;
   - `frame.md`: weights 0.30 / 0.20 / 0.15 / 0.20 / 0.05 / 0.10 and the levers capacity, quality, risk,
     experience;
   - `diagnose.md`: the shortlist (manager review, evidence requests, attribute testing, walkthrough
     refresh).
   - The source keys (BCG-GAP-2025, MCKINSEY-SOAI-2025) are already harmonized across all eleven files.
6. The earlier "spec §…" references in `frame.md`, `interviewing.md` and `breakdown-and-rollup.md` were gone
   when I last checked.
