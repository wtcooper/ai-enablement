# Verification report: ai-portfolio

Date: 2026-10-20. Brief: `briefs/verify-ai-portfolio.md`. Files checked: every file in
`plugins/ai-transformation/skills/ai-portfolio/` (`SKILL.md` and `references/**`, 17 files). Inputs:
`spec/2026-10-20-skill-suite.md`, `topic-portfolio.md`, `ai-portfolio-authoring-report.md`, and the error patterns in
`research/briefs/templates/verifier.md`. Sources were downloaded to a private `mktemp -d` folder. No git run.

## Summary

| | Count |
|---|---|
| Research-backed claims checked (figures, quotes, attributions, named examples, standards and regulatory points, forecasts) | about 120, across 36 sources |
| Archetype grades checked against `evidence_grade` | 3 (all B, as recorded) |
| Worked-example arithmetic checked (weighted score and both indexes) | 4 rows (all correct) |
| Kept as written | about 82 |
| Fixed | 38 |
| Removed | 0 claims. One citation was narrowed: AUSGOV-2013 no longer supports "reusable assets" |
| Source entries checked (exists, URL, date) | 36 of 36. All dates correct. All URLs resolve, directly or through the mirror |

No figure was wrong at its source. The errors fell into the known patterns:

- **Misread statistics (2).** MIT NANDA's ~83% pilot-to-implementation rate was set against a 5% share of all
  organizations. RAND's 84% was given as a share of 65 interviewees when it is a share of 50.
- **Missing survey population or owner (14).**
- **Embellished or drifted attributions (10).** Examples: the Polsinelli chair's account; HBR's "lighter version"
  applied to items, not industries; the Gartner causes; the Microsoft backlog cited to the wrong page; IVI's "action
  list" cited to AUSGOV.
- **Unlabelled skill defaults (3).**
- **One wrong provenance note:** the Accountancy Age figures cite Financial Times analysis.
- **One internal inconsistency:** the live count in the review 3 worked example.

## Fixes

| # | File and place | Was | Now | Reason |
|---|---|---|---|---|
| 1 | `intake.md` §3.2 | "pilot-to-implementation rate of about 83% for generic chat tools against 5% for task-specific tools" | 83% apparent pilot-to-implementation for generic tools; only 5% of organizations got task-specific tools into production (60% evaluated, 20% piloted); 52 interviews and 153 surveyed leaders | **Misread statistic.** 5% is a share of all organizations, not a pilot-to-implementation rate (that would be about 25%). Population added |
| 2 | `intake.md` §1 | Prioritized backlog with consistent criteria [MSFT-PLAN-2026] | [MSFT-COE-2026], source added to §9 | Attribution drift: the backlog text is on the CoE page |
| 3 | `intake.md` §3.1 | "One sentence … [MSFT-PLAN-2026]" | Microsoft asks for a short statement of activity and result | Embellished: Microsoft says "short statement", not one sentence |
| 4 | `intake.md` §2 | "how often the activity happened last month [MSFT-PLAN-2026]" | "last month" is the skill's prompt; Microsoft asks to confirm the activity happens often enough | Embellished attribution |
| 5 | `intake.md` §5 | MIT NANDA >90% "(small, non-random sample)" | 52 organizations interviewed, 153 senior leaders surveyed; non-random, directional | Population required |
| 6 | `intake.md` §6 | "HBR's whole-portfolio view exists to see [duplicates]" | HBR's approach unifies efforts across departments | Embellished: HBR does not mention duplicates |
| 7 | `screen-and-score.md` §6 | "In RAND's 65 interviews, 84% cited leadership-driven failures" | 84% of RAND's 50 industry interviewees (data scientists and engineers) | **Misread statistic.** RAND interviewed 50 industry practitioners and 15 academics; the 84% is of the industry group |
| 8 | `screen-and-score.md` §3.4 | "Most of Deloitte's EMEA respondents" | Deloitte survey of 1,854 executives in 14 European and Middle East countries (2025) | Population |
| 9 | `screen-and-score.md` §3.4 | "Google Cloud's survey of gen-AI-in-production users" | Survey of 3,466 senior leaders; 74% of those with gen AI in production | Population |
| 10 | `screen-and-score.md` §3.4 | 85% of Deloitte's "ROI Leaders" | Adds "(the top fifth of that survey on its ROI index)" | Definition of the subgroup |
| 11 | `screen-and-score.md` §5 | External partnerships "succeeded about twice as often" | "reached deployment about twice as often" (~67% vs ~33%), self-reported | Wording drift; MIT NANDA flags the figures as self-reported |
| 12 | `screen-and-score.md` §1 | Cooper "pairs any financial model … financial inputs are uncertain or biased" | "pairs a financial model with a scorecard because financial data are often uncertain or biased" | Embellished qualifier ("any") |
| 13 | `screen-and-score.md` §3.2 | BCG "(survey of 1,000 executives)" | BCG survey of 1,000 CxOs and senior executives | Population and owner |
| 14 | `screen-and-score.md` §5, §6 | MIT NANDA budget skew, no population | "MIT NANDA's executive interviews and survey" | Population |
| 15 | `setup.md` §3.1 | BCG "(survey of 1,000 executives)" | BCG survey of 1,000 CxOs and senior executives in 59 countries | Population and owner |
| 16 | `setup.md` §2 step 6 | "a lighter path suits lower regulatory burden, and closely related items … share streamlined approvals [HBR; OMB]" | HBR says a lighter process suits *industries* with lower regulatory burden; OMB asks for streamlined approvals for closely related, similar-risk uses; using this for low-risk items in one firm is labelled the skill's default | Scope drift (industries became items); unlabelled connective claim |
| 17 | `setup.md` §5 | Gartner 30% forecast; S&P 46% "(respondent-reported, secondary)" | Gartner forecast made in 2024 for end-2025; S&P Global Market Intelligence survey of more than 1,000 respondents in North America and Europe, "before production" | Forecast dated; population and owner |
| 18 | `setup.md` §6 | NAO "15 of 32 … (survey of bodies)" | NAO survey of UK government bodies, autumn 2023; "said" use cases were identified | Population, date and wording |
| 19 | `stage-gates.md` §3.2 | "The utility … suggests a lighter version for lower regulatory burden" | The article says a lighter version suits industries with lower regulatory burden; the light path for low-risk items is the skill's default | Attribution (article, not clearly the utility) and scope |
| 20 | `stage-gates.md` §5.1 | "Data not available or not good enough" as Gartner's cause | "Poor data quality" | Gartner's wording; "not available" was added |
| 21 | `stage-gates.md` §5.2 | Lessons and reusable assets [AUSGOV-2013] | Lessons [AUSGOV-2013]; reusable assets uncited | AUSGOV covers lessons learned only |
| 22 | `stage-gates.md` §7 | "about one in five McKinsey respondents" | Respondents to McKinsey's 2026 global survey (1,719 participants); "their organization's AI use" | Population |
| 23 | `portfolio-review.md` §3.3 | Recalibrate "if the forum's decisions keep overriding the scores [HBR-2026]" | HBR for recalibration; the trigger labelled a proposed default | Unsourced connective claim |
| 24 | `portfolio-review.md` §3.3 | McKinsey 28%; Deloitte 95% "more than 10%" | McKinsey 2026 global survey (1,719, 97 countries) and "ICT budget"; Deloitte 2025 survey of 1,854 executives and "technology budget" | Population; Deloitte's base is the technology budget |
| 25 | `portfolio-review.md` §3.4 | "18% of professional-services respondents" | TRI 2026 survey of legal, tax and accounting, corporate and government professionals; "ROI of AI tools" | Population was too narrow; TRI's wording |
| 26 | `portfolio-review.md` §5 | 37% "attribute at least some EBIT impact" | 37% "report that AI contributed positively to EBIT" | Source wording (McKinsey 2026) |
| 27 | `portfolio-review.md` §6 | 80% versus 37%, no population | McKinsey's 2026 global survey (1,719 participants); "their individual productivity" | Population and wording |
| 28 | `portfolio-review.md` §7 | "live four of six"; "Four of five live items" | Live (prototype, pilot, scale) three of six; "All four items past discover" | Internal inconsistency with the live-limit definition in `setup.md` §3.4, the schema and the template |
| 29 | `value-tracking.md` §2 step 7 | Not-achieved benefits stay on the action list [AUSGOV-2013] | "benefits action plan" [IVI-ITCMF-n.d.; AUSGOV-2013] | Attribution: the "expected but not achieved" item is IVI's |
| 30 | `value-tracking.md` §3.2 | McKinsey "14% … against 32% who had expected one" | 14% of respondents from organizations using AI, against 32% who expected reductions **in the previous year's survey** | Two different survey years; population |
| 31 | `value-tracking.md` §3.4 | "the Australian Gate 5 review follows it" | Gate 5 guidance recommends a post-implementation review focused on learnings and broader benefits | Unsupported sequencing claim |
| 32 | `value-tracking.md` §5 | NAO "24 of 32 … named an accountable owner (survey of bodies)" | UK government bodies with deployed AI said their AI use cases had a named accountable owner (NAO survey, autumn 2023) | Wording and population |
| 33 | `value-tracking.md` §6 | TRI 18% "professional-services respondents" | As fix 25 | Population |
| 34 | `value-tracking.md` §6 | "Wharton reports 72% of US enterprise leaders" | Wharton and GBK's 2025 survey of about 800 US enterprise decision makers; "structured, business-linked ROI metrics" | Population and owner |
| 35 | `people-and-change.md` §2 | Chair "gave AI to respected senior people rather than technologists" | Asked some of the firm's most talented business leaders, not technologists, to build the business side alongside the tech team | Embellished. The transcript says the tech team stayed (same finding as the partner-materials verification) |
| 36 | `people-and-change.md` §2 | "17% to 33% hallucination rates in three legal research tools" | Three tools (2024 versions) each hallucinated "between 17% and 33% of the time"; preregistered academic study | Abstract wording; versions dated |
| 37 | `people-and-change.md` §2 | Big Four 179 vs 276 "(trade press; no named data origin)" | UK Big Four; trade press citing Financial Times analysis | Wrong provenance note; scope is UK |
| 38 | `people-and-change.md` §3, `library/index.md` §2 | "Broadcast mandates" trap cited to Empson; `gate_path` "follows practice in regulated settings" | Trap labelled as an inference from Empson's point on formal power; `gate_path` worded as in fix 16 | Unlabelled inference; scope drift |

## Kept after checking (selection)

- **HBR-2026** (read through the AAPL reprint): the review decisions list; the early-warning triggers (schedule
  slippage, cost overruns, performance shortfalls); the Buy/Sell/Hold criteria; the stage-gate progression tests;
  the OPEN stage names; strategic fit and technical feasibility at the first gate; red-team scrutiny; the
  "considerable increase in cost and development time"; total cost of ownership; advancement by resource
  availability and fixed criteria; "too many pilots with too little coordinated oversight"; and Lloyds' forum
  (cross-functional, prioritizes, allocates resources, accepts abandoning projects when technology changes).
- **Cooper (Stage-Gate):**
  - Go, Kill, Hold or Recycle.
  - Gatekeepers are the senior managers who own or control the resources.
  - "approval without resources".
  - Gates are forward-looking, and both readiness and value criteria apply.
  - The stage sequence.
- **Microsoft:** the CoE pages on the steering committee, monthly sponsor reviews, the advisory shift and its three
  signals, and the CoE page dated 2026-04-10. The Plan page on problem-first framing and the individual-work versus
  business-automation classes, and the Plan page dated 2026-10-15.
- **UK AI Playbook:**
  - Use cases register.
  - "led by business and user needs".
  - Five-part business case near GBP 10 million.
  - Fallback processes.
  - Decommissioning when unacceptable risks or harms are found.
- **Standards and regulation.** NIST GOVERN 1.6 and 1.7, and MANAGE 1.1. OMB M-25-21 (2025-04-03): the annual use
  case inventory, minimum risk practices for high-impact AI, the plan to discontinue under-performing high-impact
  AI, the termination of non-compliant use, and streamlined approvals for closely related, similar-risk uses.
- **Surveys:**
  - BCG: 70/20/10.
  - Gartner: the 2024 forecast of 30% by end-2025, and the 2025 forecast of more than 40% by end-2027 (through
    Outlook Business).
  - Deloitte: two to four years, seven to 12 months, 6%, 85% and 95%; real data versus dummy data; and
    entanglement with broader transformation.
  - Google: 74%.
  - Wharton: 72%.
  - McKinsey 2026: 37%, 80%, 28%, one in five, and 14% against 32%.
  - TRI: 18%.
- **Benefits practice.** NBER J-curve: model and historical analysis, revised January 2020. IVI's metrics:
  benefits owner, review after go-live, the six-month review, benefit success rate and benefits-led business cases.
  AUSGOV Gate 5: benefit types, owner per benefit, measurement and timing, and lessons learned.
- **Named examples:**
  - DBS: about SGD 1 billion in 2025, self-reported, with the control-group method described in the Business
    Times.
  - The DBS CEO on value growing harder to isolate.
  - Partners Group and FRP: 120 bps, USD 10 million, a clean policy-level dataset.
  - Bain: 10–12% against about 5%, with its leverage and multiple assumptions.
  - MD Anderson: put on hold in 2017 after costs topped USD 62 million.
  - Umbrex: "status theater".
- **Partner sources:**
  - Empson's leadership constellation, as described.
  - Paperjam: an A&O Shearman partner's recollection after six months.
  - Perlin's four variables.
  - KPMG: AI objectives in reviews from 2026, and monitoring "not intended as a disciplinary measure".
  - LexisNexis: consultants' self-reported savings.
- **Archetype grades:** `tax-compliance-individual-business-02`, `professional-services-pursuit-proposals-01` and
  `professional-services-knowledge-management-01` are all B, as recorded.
- **Worked example (`screen-and-score.md` §7):** all four weighted scores and all eight indexes recompute exactly
  with the default weights.

## Usability fixes (`SKILL.md`)

- **Goal per step.** Each of the six steps now has a one-line `Goal:` under its Read now pointer, as in
  ai-solution-delivery. Every step now has a goal, core questions, exit criteria, an output file and one Read now
  pointer.
- **One Read now per step.** Step 3 also pointed to `prioritize.md` §3. That pointer was removed because
  `screen-and-score.md` §2 step 5 already sends the reader to the anchors at the moment of scoring.
- **Rule 7 (never claim to run).** The description now says "Helps set up and run a firm's AI portfolio". The
  opening now says "You help the person accountable … run it". Both previously said the skill runs the portfolio.
  The description is now 964 characters.
- **Rule 9 (no calendar deadlines).** On resume the skill noted items "with a `next_gate` due", but `next_gate`
  has no date. It now notes items "waiting at their `next_gate`".
- **Step 6 exit.** "every item at or past `g3`" now reads "approaching or past `g3`", which matches the rule that
  rows are created before `g3`.
- **Checked and fine:**
  - The description names the moment and all four siblings.
  - The skill saves state after every step and resumes from `portfolio.yaml`.
  - The handoff table names each skill with the `../<skill>/SKILL.md` fallback, and all four paths resolve.
  - Delegation has a fallback for when subagents are not available.
  - The core rules block matches the shared source.
  - Owners are roles, and no named individuals appear except cited authors and quoted roles.
  - Values are ranges.
  - Grades are as recorded.
  - Cadence is a rhythm, not a deadline.
  - The skill designs and records; it never claims to build.

## Formats and structure

- Both schema examples (`portfolio/v1`, `benefits/v1`) parse with `yaml.safe_load`, and so do both YAML
  templates.
- Item, decision and benefit keys in the examples and in the benefits template match the schema format blocks
  exactly.
- Shared vocabulary ids in the examples exist in `vocabulary.yaml`: `service-delivery`, `document-to-decision`,
  `augment`, `step`, `workflow-automation`, and the levers `capacity`, `quality` and `growth`.
- Portfolio-only ids are listed as new in the authoring report, with one exception: `state.status`
  (`setting-up | running`) is new and not listed there.
- `risk_tier` uses ai-governance's `tier-1` to `tier-4`, which exist in `ai-governance/references/schemas/policy.md`.
- `python3 scripts/validate.py` reports 0 errors. Its 25 warnings are all archetype grade-mix targets outside
  this skill.
- Line counts: `SKILL.md` has 219 lines. The largest method file, `stage-gates.md`, has 227 lines (the limit is
  300). Contents lists hold.
- Sibling links: `../transformation-advisor/SKILL.md`, `../ai-solution-delivery/SKILL.md`,
  `../ai-enablement/SKILL.md` and `../ai-governance/SKILL.md` all exist and resolve now, so none were left
  unresolved.
- The solution file names this skill reads (`readiness.md`, `post-launch.md`) match ai-solution-delivery's
  outputs, and so does its gate mapping.
- As instructed, `references/library/index.md` and `references/method/people-and-change.md` were left in place.

## Sources not reached directly

- **Read through a news report only (as in the research):** Gartner's 2025 agentic release (Outlook Business) and
  S&P Global Market Intelligence's survey (CIO Dive). Their exact wording and sample details are unverified
  beyond the reports.
- **Read through the r.jina.ai mirror (direct fetch blocked):** Gartner 2024, BCG 2024, Deloitte, McKinsey 2026
  (mckinsey.com.br), RAND, TRI, Paperjam, Polsinelli transcript, LexisNexis, Legal Futures, Accountancy Age, IAB,
  DBS, Business Times (FCC) and AUSGOV Gate 5.
- **Read directly when the mirror returned 403:** the Partners Group release, through the Deutsche Boerse feed.
- **Read through the AAPL reprint:** HBR-2026. The hbr.org original is paywalled.
- **Read in part:** HBR-2018 (the introduction only).
- **Not read:**
  - Empson's 2013 report (only Flood's review was read).
  - Perlin's paper.
  - The full TRI 2026 report.
  - The FT partner-promotion analysis.
  - Gartner's and S&P's original documents.

## Open questions for the owner

1. **Live limit definition.** It counts prototype, pilot and scale but not production (`setup.md` §3.4, schema,
   template). Is excluding production intended? It is consistent everywhere now, but a reader may expect a
   production item to use owner and review capacity.
2. **Gartner 2024 forecast.** The forecast's horizon (end-2025) has passed. Keep it as a dated forecast, or replace
   it with a measured outcome if one is found?
3. **Example snapshots.** The `portfolio.yaml` example (last review 2) and the `benefits.yaml` example (actuals at
   review 4) are both dated 2026-10-20. Both are labelled illustrative. Align them, or leave them as separate
   snapshots?
4. **K-1 risk tier.** The example places K-1 extraction at `tier-2`. ai-governance's `tier-4` covers signed returns
   and filings, and its ladder rule raises the tier per rung. Tier-2 is defensible because a preparer reviews every
   flagged field, but ai-governance should confirm.
5. **Vocabulary.** Add `state.status` (`setting-up`, `running`) to the list of portfolio values proposed for
   `vocabulary.yaml`, with the others in the authoring report.
6. **Still pending from authoring:**
   - The core-rules paths, which the coordinator is changing.
   - The acquired-firm playbook placeholder (`stage-gates.md` §9).
   - Whether the validator should check `portfolio/v1` and `benefits/v1` enums.
