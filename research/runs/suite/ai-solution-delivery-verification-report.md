# Verification report: ai-solution-delivery

Prepared 2026-10-20. Brief: `research/runs/suite/briefs/verify-ai-solution-delivery.md`. Files checked: every file in
`plugins/ai-transformation/skills/ai-solution-delivery/` (SKILL.md, 6 method files, 2 pointer files, 4 templates,
1 schema, 1 brief). No git commands were run. Sources were downloaded to a private `mktemp -d` folder.

## 1. Summary

| | Count |
|---|---|
| Sources opened and checked | 36 of 36 cited (34 read directly; BCG-2024, BCG-ATWORK-2025, BOE-2023 and the RAND and HBS pages read through the r.jina.ai mirror) |
| Attributed claims checked (figures, quotes, regulatory points, dates, named examples) | about 95 |
| Kept as written | about 60 |
| Fixed | 35 claim-level fixes (table in §2), plus 1 format fix and 1 usability fix |
| Removed | 0 |

No claim was unsupported outright. The fixes fall into five patterns: survey figures without their population
(10), embellished qualifiers (6), attribution drift or unsourced connective claims (6), misread statistics (3) and
missing or out-of-date dates (5). The validator reports 0 errors. The other warnings it reports are all about
use-case targets in the archetypes, not these files. Every method file stays under 300 lines (eval-plan.md is
the longest at 294), and SKILL.md has 232 lines.

## 2. Fixes and removals

| # | File and place | Was | Now | Reason |
|---|---|---|---|---|
| 1 | frame-problem §2 step 3 | "RAND's practitioner interviews" | "RAND's interviews with 65 experienced data scientists and engineers" | Population missing |
| 2 | frame-problem §3, Task type | "made consultants 19% less likely to be correct" | Adds: preregistered experiment, 758 BCG consultants, GPT-4, 2023 | Population and model year missing (wording matches the HBS page; see §5) |
| 3 | frame-problem §3, Stakes | "Fully automated significant decisions or high-risk outcomes keep a person deciding" | "Be cautious about fully automating significant decisions; high-impact or high-risk outputs need a person validating them" | Embellished: the UK playbook says "be cautious" and asks for human-in-the-loop validation where impact or risk is high |
| 4 | frame-problem §5 move 1 | "price that maximizes profit" | "price that gives the greatest profit margin, not the price that sells the most items" | Wording drift from RAND |
| 5 | frame-problem §5 move 6 | NANDA 90% / 40% with "self-reported interviews and survey" | Adds: 52 organizations interviewed, 153 senior leaders surveyed | Population missing |
| 6 | frame-problem §6, wrong metric | "84% of interviewees cited…" | Adds the population (65 interviewees, 50 from industry) and RAND's own caveat that its mostly non-managerial sample may skew toward leadership causes | Population missing; the source's limitation was left out |
| 7 | frame-problem §6, people and process | "BCG's survey attributes about 70%…" | "BCG's survey of 1,000 CxOs and senior executives in 59 countries…" | Population missing |
| 8 | build-or-buy §3.2, Lock-in | "CIOs told a16z that agent workflows tuned for one model are hard to move" | "a16z reports, from its survey of 100 CIOs and buyer interviews, that guardrails and prompts built for agentic workflows make switching models harder" | Attribution drift: item 10 is a16z's analysis, not a quoted CIO statement |
| 9 | build-or-buy §3.3, background-agent | "66% of surveyed deployed agents tolerate minutes or longer" | "66% of surveyed deployed agent systems allow response times of minutes or longer (UC Berkeley-led academic survey, N=53)" | Population and N missing |
| 10 | build-or-buy §3.4, Regulated work | "a16z reports the shift… has not played out there; assume more in-house control" | The source's scope stated ("regulated or high-risk industries such as healthcare"); the inference is marked *(advisor default)* | Unsourced inference presented as the source's |
| 11 | build-or-buy §3.4, Fine-tuning | "70% of 20 interviewed deployed-agent cases" | "14 of 20 interviewed deployed-agent teams (70%)", UC Berkeley-led | Who ran the study; the raw count |
| 12 | build-or-buy §3.4, Build versus partner | NANDA 67% / 33% | Adds: interview sample of 52 organizations | Population missing |
| 13 | build-or-buy §5 move 3 | The heading said "give suppliers dummy data", but the source sentence omitted it | The playbook's dummy-data and hidden-cost lines are now quoted accurately | The heading claim was not traced to its source sentence |
| 14 | build-or-buy §5 move 5 | "AI tools beat it on four of seven tasks and none beat it on one research task" | "at least one AI tool beat it on four of seven tasks, the lawyers did better on two (including a multi-step research task) and matched the best tool on one" | Misread statistic: Vals reports the lawyers ahead on two tasks (EDGAR research and redlining), not one |
| 15 | build-or-buy §5 move 5; eval-plan §3.5 | "In the Berkeley survey only 39%…" | Adds: UC Berkeley-led survey of practitioners with deployed agents | Population missing |
| 16 | design-brief §3.1 | "academic study, N=60" | "UC Berkeley-led academic study, N=60" | Who ran the study |
| 17 | design-brief §3.3 | "a vendor survey found few respondents…"; "Write queries should not run without human approval" | LangChain's survey of over 1,300 professionals, with the finding as stated; "Queries that insert, update or delete data…" | Population missing; Huyen's point is about SQL insert, update and delete, which "write queries" generalized |
| 18 | design-brief §3.5 | High-risk actions "always pause for a person (cancel, pay, send, file)" [OPENAI-2025] | OpenAI: sensitive, irreversible or high-stakes actions hand over to a person "until confidence in the agent's reliability grows"; "always pause" is attributed to the skill's rule 12 | Embellished qualifier attributed to the source |
| 19 | design-brief §3.5 | Editing a suggestion gives "a clear point of accountability" [APPLIEDLLMS; YAN] | The feedback loop is sourced; accountability is marked *(advisor default)* | Unsourced connective claim |
| 20 | design-brief §3.6 | "When it does not know, it says so and routes to a person" [APPLIEDLLMS 1.4.7] | Design the path explicitly and test it; models often return output when they should not, and prompting for "unknown" is not foolproof | Misread: section 1.4.7 warns that the behaviour is unreliable; it does not say models do this |
| 21 | design-brief §6 | "for example `draft-review-loop` §6" | "`document-to-decision` §6 and `draft-review-loop` §2" | Wrong pointer: draft-review-loop §6 does not mention rubber-stamping |
| 22 | eval-plan §3.1 | "the first discovery is often that seniors disagree [ANTHROPIC-2026]" | Marked *(advisor default)*; Anthropic is cited only for what it says (experts may disagree; rater disagreement needs reconciling) | Attribution drift |
| 23 | eval-plan §3.7 | 42% to 95% "after grading and task fixes" | Adds "and a less constrained scaffold" | Incomplete cause: the source names three fixes |
| 24 | eval-plan §3.9 | "The UK audit regulator expects firms to document…"; override analysis attributed to FRB-2011 and BOE-2023 | Says the guidance adds no new requirements; its documentation topics are now checked against the guidance PDF; override analysis is attributed to FRB-2011 only; the model inventory is added | The source states it introduces no new requirements; override analysis was not confirmed in SS1/23 |
| 25 | eval-plan §4, Launch accuracy bar | "GDS judged 80% expert-rated accuracy insufficient for a public pilot" | "…80% answer accuracy, assessed by content designers, needed improving before deployment to users on GOV.UK" | Source wording ("prior to the product being deployed for users on the site"); who measured |
| 26 | eval-plan §4, note | "nearly 70% of surveyed testers…" | "testers surveyed after use…", "judged not yet enough" | How the figure was measured |
| 27 | eval-plan §6 move 7 | "on a 2024 retail benchmark the best agent passed under 50% of tasks, and under 25% on all of eight trials" | Under 50% is across tau-bench; under 25% pass^8 is in the retail domain; 2024 models; written by an agent vendor's research team | Misread scope; provenance missing |
| 28 | eval-plan §10; readiness §9 (BOE-2023) | Dated 2023-05-17 only | Adds: updated version published 2026-04-23, which keeps the inventory and independent-validation principles | Out-of-date source date |
| 29 | eval-plan §10; readiness §9 (FRC-2025) | News release only | Cites the guidance PDF (*AI in audit*, June 2025), now read | Upgraded source; closes an authoring-report gap |
| 30 | readiness §2 step 6; §4.1 | "NIST asks that go/no-go decisions use red-team and structured-feedback results" | "NIST's profile suggests documenting how structured feedback results, which include red-teaming, fed the go/no-go decision" | Embellished: AI 600-1 is a voluntary profile, and MS-4.2-005 is about documenting structured public feedback (which NIST defines to include red-teaming) |
| 31 | readiness §3.5, Training | "Training before access… [ABA-2024]"; BCG "five or more hours of training… about one-third" | "Before access" marked *(advisor default)*; ABA cited for supervisors ensuring training on capabilities and limits; BCG: survey of more than 10,600 leaders, managers and frontline employees in 11 countries and regions, "at least five hours of training and access to in-person training and coaching", "only one-third" | Attribution drift; population missing; a condition omitted |
| 32 | readiness §3.5, People and process | BCG 70% | Adds: 1,000 CxOs and senior executives | Population missing |
| 33 | launch-review §3.4 | "dependence is stronger evidence for peers than satisfaction (a partner's recollection)" | What the partner recalled is stated as the source's; the "persuades peers" reading is marked *(advisor default)* | Unsourced connective claim |
| 34 | All method files (GOOGLE-RULES) | "undated" | "page last updated 2025-08-25" | Missing date |
| 35 | design-brief, eval-plan (YAN-2023); design-brief (LANGCHAIN-2024) | "2023"; "2024" | "2023-07"; "2024 survey; the page now carries a 2026 date stamp" | Imprecise or ambiguous date |

**Format fix.** The type sketch in `references/schemas/solution.md` §1 did not parse:
`opportunity: { file: path, id: string } | null` is a YAML error. It is rewritten as a nested map with a comment.
All five YAML blocks in the schema and all four template frontmatters now parse with PyYAML.

## 3. Claims kept (verified as written)

- **RAND-2024:** 16 of 50 (technology-driven), 30 of 50 (data quality), the if-then rules example, interviews held August to December 2023.
- **OPENAI-2025:** the three agent-fit signals, the two human-intervention triggers, "especially important early in deployment", and setting a baseline with the most capable model before testing smaller ones.
- **ANTHROPIC-2024:** latency and cost trade-off, compounding errors.
- **ANTHROPIC-2026:** published 2026-01-09; 20–50 tasks (Step 0), start from manual checks (Step 1), the two-expert test (Step 2), balanced sets (Step 3), the "Unknown" option and per-dimension judges, capability versus regression suites (regression "nearly 100%"), graduation of cases, 0% pass@100 meaning a broken task, the 0.75³ ≈ 42% example, read the transcripts.
- **BERKELEY-2026:** arXiv v4 dated 2026-06-04; 68% at most 10 steps (N=60); newer models can break workflows (C10).
- **STANFORD-2024:** 17%–33%, preregistered, "hallucination-free" marketing.
- **MITNANDA-2025:** July 2025; figures described as directional; the confounding caveat.
- **A16Z-2025:** posted 2025-06-10; 100 CIOs across 15 industries; items 6, 11 and 12.
- **UKGDS-2025:** retrieval chosen over fine-tuning because content is updated regularly; whole-page retrieval exceeded token limits, leading to chunking, embeddings and re-ranking; personal data removed; red teaming with cyber security experts; lock-in; problem statement; SRO; quantitative testing in change control; managed release that can be withdrawn.
- **NIST-2024:** GV-6.2-003 (incident ownership, rehearsal), GV-6.2-006 (fallback including manual processing), GV-6.2-007 (secondary data use, incident and change notification, SLAs), MS-1.3-002/003 (red-teaming; feedback by people not involved in development), MS-4.2-004 (overrides), MG-4.2-002 (post-mortems), GOVERN 1.7 (decommissioning).
- **FRB-2011:** override analysis ("rate of overrides is high, or… consistently improves model performance… revision or redevelopment"), independence of validation, inventory.
- **ABA-2024:** verification "will necessarily depend on the GAI tool and the specific task"; the contract-summary subset example; "fully responsible"; dated 2024-07-29.
- **GUARDIAN-2025:** partial refund (final instalment), nonexistent references, the A$440,000 contract, 2025-10-06.
- **HUSAIN-2024:** Rechat plateau; pass rate is a product decision; precision and recall over raw agreement.
- **HUSAIN-2026:** published 2026-09-18; 30 minutes on 20–50 outputs; one domain expert ("benevolent dictator"); at least 30 traces annotated yourself, about 100 diverse traces, first failure; 100–200 labels per judged mode; 100+ fresh traces per cycle, 2–4 week cycles, 10–20 weekly; 100% pass suggests evals are too easy; add confirmed failures; retire evals that always pass.
- **APPLIEDLLMS-2024:** published 2024-06-08; sections 1.4.3, 1.4.5, 2.1.2, 2.2.2, 2.2.3, 2.3.2, 3.1.2 ("driven more by FOMO"), 3.2.1 ("least durable component"), 3.2.4 (text-to-SQL, documentation chatbot, knowledge-base support bot; "for a product company").
- **LMSYS-2023:** over 80% agreement; position, verbosity and self-enhancement biases.
- **SHANKAR-2024:** criteria drift.
- **THOUGHTWORKS-2025:** moved from Trial to Assess, Nov 2025 (last updated 2025-11-05).
- **OWASP-2025:** LLM01, LLM05 and LLM06 names correct.
- **MSFT-REDTEAM:** scorecard and attack success rate.
- **GOOGLE-RULES:** Rules 1, 3 and 10 (stale table, gradual decay).
- **GOOGLE-2015:** "relatively fast and cheap… maintaining them over time is difficult and expensive".
- **GOOGLE-2021:** May 2021; monitoring.
- **UKGDS-2024:** withdrawn 2025-02-10.
- **CIPD-2026:** published 2026-03-25; mandatory training before use, "verify, verify, verify", senior lawyers sharing what worked and what didn't.
- **LAW360-2025:** 2025-09-26; licences go unused (no figure).
- **PAPERJAM-2025:** 2025-06-19; "two to three hours a week" (self-reported); the "take it away" question.
- **Archetype grades** as cited match the recorded `evidence_grade`: assurance-controls-testing-07 B, professional-services-quality-review-05 B and -07 B, assurance-quality-management-04 C, professional-services-firm-finance-11 B.
- **Governance tier:** `tier-4` for attest evidence matches the ai-governance policy schema.

## 4. Fitness for use

**Checked and sound:**

- **Description:** names the moment ("build or buy X", pilot to take live, evaluation plan, "ready for production", post-launch, resume) and all four sibling skills.
- **Steps:** each step has a goal, core questions, exit criteria, one output file and exactly one "Read now" pointer.
- **State and resume:** state is saved after every step (`step_completed`, `next_step`, `updated`), and resume works from `solutions/*/brief.md`.
- **Handoffs:** handoffs name the skill, with the `../<skill>/SKILL.md` file-read fallback; the delegation wording matches the advisor's.
- **Core rules:** the block matches the source. No named individuals appear in the body, apart from source authors in citations. Values are ranges. Grades are given as recorded. Review points are events, and the Husain cadence is labelled as a cadence, not a deadline. The skill designs and records; the firm builds and runs.
- **Ids:** ids in the schema example and templates are in `vocabulary.yaml` or are listed as new in the authoring report §4 (`doc`, `sourcing`, solution `status`, eval `status`, readiness `decision`, `last_decision`).
- **Cross-references:** templates match the schema. The `eval-plan.md` §8 and §10 references in readiness match the template's numbering.

**Usability fixes made:**

1. SKILL.md, Start or resume: added what to do when a found solution has `status: stopped` or `retired` (say so;
   reopen only on new evidence; log the reason). Before this, resume would offer to "continue at `next_step`" on a
   stopped solution.
2. design-brief §6: corrected the pattern-file pointer for rubber-stamp review, so the assistant opens a section
   that actually covers it.
3. solution.md: the schema sketch now parses (see §2).

## 5. Sources not reached, or only partly reached

- **HBS-2023:** the faculty page was read through the r.jina.ai mirror; the working-paper PDF and SSRN abstract were not reached. The page says "19% less likely". My memory is that the paper's abstract says "19 percentage points"; I could not confirm this. The wording is kept as the cited page has it.
- **BCG-2024, BCG-ATWORK-2025, BOE-2023:** read only through the mirror (direct fetches returned stub pages). The BOE April 2026 PDF was read directly.
- **RAND-2024:** read through the mirror (the direct fetch returned a stub).
- **GARTNER-2025** (in the research file) is not cited in the skill, so it was not checked.

## 6. Open questions for the owner

1. **HBS figure:** should "19% less likely" become "19 percentage points less likely" once someone confirms the paper's wording?
2. **BOE SS1/23:** the April 2026 version supersedes the 2023 text. Re-cite to the 2026 PDF across the suite (the advisor files may cite the 2023 version too)?
3. **Brief template placeholders:** the frontmatter defaults `pattern: other`, `ladder: assist` and `runtime_class: personal-assistant`. They are valid ids, but before step 1 they could be read as decisions. Allow `null` until step 1 in `solution/v1`?
4. **Living sources:** HUSAIN-2026 (modified 2026-09-21) and the Thoughtworks blip (no longer on the current Radar edition) can change or drop out. Re-check them at the next suite verification?
5. **Withdrawn source:** UKGDS-2024 is withdrawn but still cited for logging and cost points. Replace it with UKGDS-2025 wherever the playbook covers the same point?
6. **Still open from the authoring report §5:** shared versus local ids, the validator's core-rules paths (the pointer files were left in place as instructed), running readiness twice, the benefits and workflow ownership split, keeping `review-solution.md`, and unified source keys.

**Links to ai-enablement** (the skill is still being written; I left these unchanged; they resolve today, but the
target content may change):

- `SKILL.md`: handoff table row `../ai-enablement/SKILL.md`, and the generic fallback `../<skill>/SKILL.md`.
- `references/method/people-and-change.md`: `../../../ai-enablement/SKILL.md`.
- The method files and templates hand off to **ai-enablement** by name for the adoption plan, training,
  `enablement/workflows/` and uneven adoption: readiness §1, §2, §3.5 and §8; launch-review §1, §3.4 and §8; the
  readiness and post-launch templates.
