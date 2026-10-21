# Verification report: ai-enablement

Prepared 2026-10-20. Scope: every file in `plugins/ai-transformation/skills/ai-enablement/` (`SKILL.md`, seven step
files, three templates, two schemas, one brief, two redirect stubs). Checked against the spec
(`spec/2026-10-20-skill-suite.md`), the authoring report and the cited sources. Validator after the edits:
`0 error(s)`. All 25 warnings are use-case target warnings in the core skill's archetypes; none is in this skill.

## 1. Summary

| | Count |
|---|---|
| Sources cited (unique URLs) | 58 |
| Sources opened and read | 58 (54 direct, 4 through the r.jina.ai mirror) |
| Research-backed claims checked (figures, dates, attributions, named examples, regulatory points) | about 125 |
| Kept as written | about 75 |
| Fixed (wording, figure, population, attribution or label) | 47 |
| Removed (claim not in the source) | 3 |
| Archetype use-case grades checked against `evidence_grade` | 15 ids, all match |

Error patterns found, by frequency: **survey population missing** (16 figures; the brief requires population and survey
owner), **embellished qualifiers or unsourced connective claims** (9), **attribution drift** (6), **misread
statistic** (5), **arithmetic** (2, the same error in two files). No wrong dates. No forecast presented as fact. Vendor
sources were already labelled vendor-published; two labels were corrected (ILTA is a trade association survey, BCG's
training figure is correlational, not "qualitative").

## 2. Fixes and removals

| # | File, section | Was | Now | Reason |
|---|---|---|---|---|
| 1 | assess-and-segment §4 | "Most professionals sit on rung 2" | "Most knowledge workers..." | Section surveyed US knowledge workers, not professionals |
| 2 | assess-and-segment §5 | Wharton 32% "of respondents"; Section tests with no population | About 800 senior decision-makers at large US companies; US knowledge workers | Population missing |
| 3 | assess-and-segment §6 | MIT NANDA "about 40% of companies had bought ... (anonymized)" | Interviews at 52 organizations and 153 senior leaders surveyed; "40% said they had bought" (preliminary) | Population missing; figure is companies' own statement |
| 4 | assess-and-segment §6 | "65% set no expectations or did not hold people accountable" | "set no expectations or encouraged use without holding people accountable"; Section's survey named | Source wording; population |
| 5 | assess-and-segment §6 | Exec 57% vs 18%; BCG frontline 51% "(survey)" | Section named; BCG survey of 10,600+ employees in 11 countries; "said they used" | Population and survey owner |
| 6 | assess-and-segment §6; measure-adoption §5 | HMRC: 46% of non-users "cited" security concerns | "named ... as the main reason" | Source measures the main reason, not any mention |
| 7 | program-design §2 | "Section found 53.2% of workers" | Section's survey of 5,026 US knowledge workers | Population |
| 8 | program-design §5 | "The manager is the weakest link and the cheapest lever." | "Manager expectations are a recurring gap." | Unsourced connective claim |
| 9 | program-design §5 | Gallup 22% "of employees"; BCG 15% to 55% | Gallup panel of US employees; BCG survey, correlational | Population; correlation stated |
| 10 | program-design §6 | Gallup: 15% "expected AI to eliminate their job" | "said it was very or somewhat likely" | Misread statistic (likelihood, not expectation) |
| 11 | program-design §6 | BCG training "associated with higher use (qualitative statement)" | Regular use sharply higher with at least five hours of training and access to in-person coaching (correlational) | Wrong label |
| 12 | program-design §4 | ILTA "(independent survey)" | ILTA's survey of 508 law firms (trade association survey) | Population; provenance label |
| 13 | program-design §7 | "If no learning time can be protected, expect low take-up [UKGDS]" | Labelled a working rule; UK users said capacity limited participation | Source shows a reported barrier, not a take-up effect |
| 14 | program-design §7; measure-adoption §5 | Humlum: "encouragement and training nearly doubled take-up"; earnings and hours effects "zero" | Employer encouragement nearly doubled take-up for a typical worker; users' time saved about 3% of hours; no measurable effect on earnings or hours (precise zeros); conclusion labelled advisor's reading | Embellished cause (training is a separate finding); "zero" overstates a confidence interval |
| 15 | curriculum §4 | "Gowling WLG teaches breaking complex work into steps" | "Gowling WLG's AI lead urges..." | Source is one leader's advice in an interview |
| 16 | curriculum §4, §5, §6 | Section and Wharton figures with no population (21%, 43%, 15%/17%, -8 and -14 points) | Populations added; "year on year" for the Wharton change | Population |
| 17 | curriculum §6 | "HMRC users and non-users asked for practical, tailored training" | HMRC's evaluation lists the need for practical, tailored training among its challenges | Attribution drift |
| 18 | curriculum §6 | KPMG pulse survey, no population | 130 US C-suite and business leaders | Population |
| 19 | curriculum §6 | "Law firms in a Law360 report used lunch-and-learns, short videos and one-page handouts" | One law firm (Lightfoot Franklin) named them among its most successful formats | Attribution drift: one firm, not several (the authoring report's narrowing was still wrong) |
| 20 | curriculum §6, §7 | "Target low-confidence groups first: where coaching pays [UKGDS]" | "Target early"; the UK trial found a correlation, which does not show coaching causes savings; working rule | Causal reading of a correlation |
| 21 | champions §1 | "adoption depends on perceived value, expectations and seeing respected peers use it [HARVEY]" | Source cited only for "discretionary"; the rest labelled advisor's reading | Embellished: source does not say this |
| 22 | champions §2 | "Choose for workflow credibility and standing [HARVEY]" | Adds LAW360 (Michael Best leaned on trusted staff as influencers) | "Standing" was not in the cited source |
| 23 | champions §5 | Community of practice "needs a shared domain, regular meeting and shared artifacts" | Shared domain, a community that interacts regularly, a shared practice | Closer to Wenger-Trayner's three elements |
| 24 | workflow-library §4 | "BBVA reports over 2,900 custom assistants" | OpenAI's guide reports BBVA staff building them | Attribution: the figure is OpenAI's |
| 25 | workflow-library §5 | Morgan Stanley "advisors grading summaries against expert answers" | Advisors and prompt engineers grading AI summaries for accuracy and coherence | Source wording |
| 26 | workflow-library §5; partners §5 | "Legal research tools hallucinated 17% to 33%" | "Leading legal research tools ... in a preregistered 2024 study" | Date the finding; tools have changed since |
| 27 | partners §2 | "an opinion source makes similar distinctions [MANDS-2026]" | **Removed** (and the source entry) | M&S Consulting article does not segment partners this way |
| 28 | partners §4 | "Big Four partner promotions ... 179 vs 276 (trade press, no named data origin)" | UK Big Four; trade press citing a Financial Times analysis | Figures are UK; the article names the FT as data origin |
| 29 | partners §4 | "Automating junior work is also a succession question, which partners care about." | Labelled advisor's judgment | Unsourced connective claim |
| 30 | partners §4 | Ipsos for CAW, no population | 2,718 chartered accountants in 48 countries, run in 2024 | Population |
| 31 | partners §6 | Thomson Reuters Institute 40% | Adds more than 1,500 professionals in 27 countries | Population |
| 32 | partners §7 | Answer with "which task? we will come back to you" [POLSINELLI] | "we'll get back to you", then find out which task it was | The chair said "we'll get back to you, hang in there"; "which task?" was added |
| 33 | partners §7 | 46.1% of tasks "in a study of 1,500 workers" | Stanford study of 1,500 US workers across 104 occupations; "AI agent automation" | Population; precision |
| 34 | partners §7 | A&O Shearman agents "sold to clients with revenue shared" | **Removed** "with revenue shared"; "sold to clients and other law firms" | Not in the press release |
| 35 | partners §8 | "Use peer demonstration plus a stated expectation; neither alone has support" | **Removed** the evidence claim; now an advisor's working rule, noting no source compares them | Unsourced connective claim |
| 36 | partners §8 | Workslop 40% "in one survey" | 1,150 US desk workers, BetterUp and Stanford survey | Population and survey owner |
| 37 | partners §8 traps | "firms do announce role cuts citing AI [Baker; A&O]" | Baker McKenzie cited AI among its reasons; A&O Shearman cited investment in technology and data | A&O's statement does not cite AI |
| 38 | measure-adoption §4 | Anthropic delegation 27% to 39% "(platform data)" | Claude.ai conversation samples, late 2024 to 2025 | Scope of the data |
| 39 | measure-adoption §4 | TRI 18% | Adds the survey and its size | Population |
| 40 | measure-adoption §5 | HMRC "surveyed 1,364 staff ... cut estimates by about 20% ..., giving 2-3%" | Survey answered by 1,364 of the 3,000 (45%); participants self-reported 2-3%; HMRC reduced estimates by about 20%, with its reasons | The source does not say the 2-3% is the post-reduction figure; respondents were users |
| 41 | measure-adoption §5 | Australia "40% reallocated time" | 40% of participants reported being able to reallocate time to higher-value work | Misread statistic (reported ability, not observed reallocation) |
| 42 | measure-adoption §6 | Workslop "(survey)" | "(BetterUp and Stanford survey)" | Survey owner |
| 43 | measure-adoption §9 | Raw 1-2 hours, 20-50% discount, "0.5 to 1.5 hours" | "0.5 to 1.6 hours" | Arithmetic: 2 x 0.8 = 1.6 |
| 44 | schemas/measures.md §4 | Example reading `high: 1.5` | `high: 1.6` | Same arithmetic |

Rows 2, 5, 9, 16 each cover several figures; the 47 fixes and 3 removals count individual claims.

**Kept after checking (sample):** Section's 5,026 sample, 5.5% / 73.5% / 20.9%, 21% and 3.8%, 53.2% and 42 vs 33, 7% and
1.5x, 57% vs 18%; Zapier's four levels and date; Viva's 28-day window and February 2026 fix; MIT NANDA's 90%; Mollick's
Lab and Crowd claims (hidden use, incentives, prompting "getting less important", own benchmarks); UK GDS 20,000 staff,
midpoint method, 26 minutes, 17%, time use not identified, confidence correlation, capacity barrier; HMRC 3,000
randomized licences and date; Humlum 11.9 to 5 points, 47% to 83%; NBER 34% for novices; HBS 19%; BCG 5% / 60% / 1,250
and the 10-20-70 split; ILTA 11% and 72%; KPMG review and "not for policing"; Accenture weekly logins via the FT; PwC CEO
via the FT; Shoosmiths (grade A as recorded); Ropes & Gray 20% billable credit, monthly first-year showcase, 25 teams and
criteria, over 60 champions and about 2,200 users; WBD 2-3 hours, capstone, 150+; Lewis Silkin monthly and weekly
shares, champions, spotlights, Joint Managing Partners, "drumbeat", "standard way the work gets done"; Gowling depth,
pilot measures, "silly poems and cats", decomposition; Polsinelli no billing credit and business-problem framing; ABA
Formal Opinion 512 points (via LawSites); Empson via JOTWELL; Gawande citing Rogers; Edmondson 1999; ADKAR; Wenger;
Perlin's four variables; ACC and Everlaw "nearly 60%"; Deloitte Australia refund; TRI 40% and 18%; A&O "Absolutely not"
and "two to three hours" (self-reported); Kennedys simulation (not yet run); Magesh 17-33%; CIPD case (training before
use, senior lawyers sharing, fortnightly steering group); Microsoft CoE duties and central-to-advisory move; KPMG
sandbox and agent shadowing; DTA agency-specific training; SRA warning via VinciWorks; Big Four figures (now UK).

## 3. Usability fixes

- **A goal for every step in `SKILL.md`.** Steps had core questions, exit criteria, output and a "Read now" pointer but no
  goal; each now opens with a one-line goal (SKILL.md is 244 lines, inside the 150-250 target).
- **One "Read now" pointer in step 6.** The second pointer (archetype `objections.md`) moved into the step file, which
  already routes to it.
- **Leading-partners method linked.** The core `method/leading-partners.md` now exists (the authoring report's open gap).
  Step 6's file points to it, and the reference map lists it.
- **Measures example made consistent.** Step 2 requires at least one `embedded` measure, and the workflow example linked
  to `embedded-workflows`, which did not exist. Added that measure to the measures/v1 example (parses; ids and
  provenance values checked).
- **Self-reported time saved.** Added a field rule: it may use `layer: outcome`, but is reported apart from measured
  outcomes, matching step 7's exit criteria.

Checked and found sound: the description names the moment and all four siblings (950 characters); resume from
`enablement/program.md` frontmatter; save after every step; handoffs name each skill with the `../<skill>/SKILL.md`
fallback; no named individuals in instructions or examples (names appear only in source titles); value as ranges;
grades cited as recorded (15 ids checked); no calendar deadlines (rhythms are habits, targets carry `after`); the skill
designs and plans and never claims to build or run.

## 4. Formats

- Both schema examples parse with `yaml.safe_load`; the `measures.yaml` template and the frontmatter of
  `templates/workflow.md` and `templates/program.md` parse.
- The workflow template's keys equal the workflow/v1 example's keys; the measures example's keys equal the measures/v1
  format.
- Shared ids used (`work_types`, `patterns`, `ladder`, `runtime_classes`, `provenance`, `value_levers`,
  `journey_stages`) are all in `vocabulary.yaml`. Skill-only ids are the ones listed in the authoring report §4.
- The format blocks in the schemas use `a | b` notation and do not parse as YAML; they are specifications, as in the
  core schemas.

## 5. Sources not reached

None unreached. Reached only through the r.jina.ai mirror (direct fetch returned 403 or failed): OpenAI's Morgan Stanley
case study, BCG *AI at Work 2025*, the Australian DTA executive summary and the Ropes & Gray news page. Bloomberg Law and
Law360 pages returned enough article text to check each claim. The 15 cited archetype use cases were checked for
grade and title only; their content was verified by their own verification runs.

## 6. Open questions for the owner

1. **Reliance on one vendor survey.** Section's report (vendor-published) supplies about a dozen figures across four
   files. They check out, but an independent counterweight for manager behaviour and proficiency would help.
2. **Layer for self-reported time saved.** It now sits under `outcome` with a rule to report it apart. A separate layer
   id (for example `estimate`) would make the separation enforceable; it would need a schema change.
3. **Validator coverage.** It does not parse skill-owned schema examples or check that ids cross-referenced between
   examples (measure ids in workflow links) exist. It would have caught the missing `embedded-workflows` measure fixed in §3.
4. Carried from the authoring report: depth ladder ids in the shared vocabulary; whether ai-solution-delivery writes
   `enablement/workflows/` directly; a shared minimum reporting group size from the overlay.
5. The redirect stubs (`references/library/index.md`, `references/method/people-and-change.md`) were left as they are,
   pending the coordinator's change to the core-rules paths.
