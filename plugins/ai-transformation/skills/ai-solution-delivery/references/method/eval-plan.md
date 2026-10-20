# Evaluation plan (step 4)

Read this on entering step 4. The evaluation plan is the centre of delivery: it says what "good" means in the
team's own terms, decides whether the solution is fit to launch, and keeps telling the team after launch. It
covers the test set, gold answers, pass/fail checks per failure mode, thresholds, judge calibration,
consistency, regression, red-teaming and online monitoring. You design the plan; the firm's people run it in
their approved systems. Keys in brackets are listed in §10. Lines marked *(advisor default)* are working rules,
not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Building the plan](#3-building-the-plan)
4. [Thresholds and starting numbers](#4-thresholds-and-starting-numbers)
5. [Question bank](#5-question-bank)
6. [Expert moves](#6-expert-moves)
7. [Common traps](#7-common-traps)
8. [Worked example: evidence matching in an audit practice](#8-worked-example-evidence-matching-in-an-audit-practice)
9. [Output](#9-output)
10. [Sources](#10-sources)

## 1. Goal and exit criteria

**Goal.** A plan the business owner has agreed, which turns "is it good enough?" into checks anyone can run
and a decision rule for launch.

**Exit when all of these are true:**

- One **quality owner** named by role: the domain expert who decides what "good" means.
- A **case inventory** of 20–50 real or realistic cases to start, drawn from real failures and what the team
  checks by hand, balanced with cases where the behaviour should not trigger. Cases are listed by id, type and
  source, never by content (rule 5).
- **Gold answers** for each case, with two-expert agreement checked where judgment is involved.
- A **failure taxonomy** (from error analysis on traces once a prototype exists, and from the pattern file's §6
  until then) with one **binary check** per failure mode and the grader for each (code, model judge, human).
- **Judge calibration** planned for every model-graded check.
- **Consistency:** trials per case and whether every trial must pass.
- **Thresholds** per failure class, including zero-tolerance classes with a mitigating control, agreed by the
  business owner.
- A **baseline**: the current process on the same cases.
- **Red-teaming** by people outside the build, with a scorecard.
- **Regression suite** policy and the change events that re-run it.
- **Online monitoring** metrics with owners, normal ranges and responses.
- **Evidence retained** for review, inspection or audit.

## 2. How to run it

1. **Name the quality owner.** One accountable domain expert, not a committee [HUSAIN-2026].
2. **Collect cases.** Ask for the real failures of recent months and what reviewers already check by hand;
   20–50 tasks is a good start [ANTHROPIC-2026, Steps 0 and 1]. Add should-not cases (§3.1). The user holds
   the cases in the firm's systems; the plan lists them by id, type and source.
3. **Write gold answers with the two-expert test** (§6, move 2). Expect seniors to disagree; record the
   disagreements and let the quality owner settle them. Each disagreement is a requirement to clarify.
4. **Find the failure modes.** Before a prototype: start from the pattern file's §6 failure modes and the step 1
   error history. Once there is a prototype: error analysis on real traces (§3.2).
5. **Choose a check per failure mode** and its grader (§3.3); plan judge calibration (§3.4).
6. **Set consistency, thresholds and the baseline** (§3.5, §4) with the business owner. A pass rate is a product
   decision about failure tolerance [HUSAIN-2024].
7. **Plan red-teaming** (§3.6) and the **regression suite** (§3.7).
8. **Define online monitoring** (§3.8), using the pattern file's §7 quality metrics.
9. **Professional work:** set the human verification level by testing on a manually reviewed subset first
   (§6, move 8) and record what evidence the regulator, client or professional body will expect (§3.9).
10. **Play back** the acceptance sentence; mark the plan `agreed` only when the owner accepts it. Name step 5 as
    next, or loop back to step 3 if the plan shows the design cannot meet the bar.

## 3. Building the plan

### 3.1 Cases and gold answers

- **Seed from reality:** past failures, reviewer corrections, and the step 1 error history. An eval is a test:
  input, grading logic, pass or fail; writing tasks tests whether requirements are concrete enough to build
  [ANTHROPIC-2026].
- **Balance:** include cases where the behaviour should not happen (no match exists, no escalation needed), or
  one-sided tests reward over-triggering [ANTHROPIC-2026, Step 3].
- **Two-expert test:** a good task is one two domain experts would independently pass or fail the same way;
  have someone pass it themselves [ANTHROPIC-2026, Step 2].
- **Gold answers in professional services** usually come from a senior practitioner, and seniors often disagree
  *(advisor default)*. Anthropic notes that experts may disagree on open-ended outputs and that disagreement between
  human raters needs reconciling [ANTHROPIC-2026].

### 3.2 Error analysis

Have the quality owner read 20–50 outputs (about 30 minutes) and note the first failure in each, then work up to
about 100 diverse traces until new traces stop revealing new failure modes; build the taxonomy from the notes,
then build evaluators [HUSAIN-2026, practitioner guidance]. Criteria drift is normal: people define "good" after
seeing outputs, so the rubric cannot be written entirely up front [SHANKAR-2024].

### 3.3 Checks and graders

| Failure is… | Grader | Example |
|---|---|---|
| Objective (format, a field present, a figure ties to source) | Code check | Every match carries a source link |
| A judgment call (relevance, sufficiency, tone) | Model judge, calibrated; or human | "Evidence supports the attribute" |
| High stakes or new | Human review sample | Partner or manager reviews a set per run |

Use binary pass/fail per check, report a **pass-all rate** with drill-down by check, and avoid 1–5 scales that
invite arguments about a 3 versus a 4 [HUSAIN-2026; APPLIEDLLMS-2024, 1.4.5]. Read transcripts before believing
any score [ANTHROPIC-2026].

### 3.4 Judge calibration

- Label roughly 100–200 examples per judged failure mode with enough passes and fails [HUSAIN-2026].
- Compare the judge with human labels using precision and recall, not raw agreement, when classes are imbalanced;
  give the judge an "unknown" option; judge one dimension at a time [HUSAIN-2024; ANTHROPIC-2026, Step 5].
- Why: the MT-Bench study reported over 80% agreement between a strong judge and human preferences but also
  position, verbosity and self-enhancement biases [LMSYS-2023]; Thoughtworks moved LLM-as-a-judge to "Assess"
  in November 2025, citing reliability concerns [THOUGHTWORKS-2025].
- Re-check the judge when the model, prompt or case mix changes.

### 3.5 Consistency and baseline

- **Consistency:** outputs vary run to run. pass@k asks whether any of k tries works; pass^k asks whether all k
  succeed. A 75% per-trial success rate gives about 42% over three trials (arithmetic example) [ANTHROPIC-2026;
  SIERRA-2024]. For client-facing or evidence-producing work, the all-trials number is the relevant one.
- **Baseline:** run the current manual or legacy process on the same cases. Vals used a lawyer control group
  [VALS-2025]; in a UC Berkeley-led survey of practitioners with deployed agents, only 39% compared their agent
  with a non-agentic baseline [BERKELEY-2026].

### 3.6 Red-teaming

Before launch of any client-facing or tool-using solution, run an adversarial test with a scorecard (attack
categories, attempts, success rate) and re-run it on a set trigger. Use people not directly involved in
development [NIST-2024, MS-1.3-002, MS-1.3-003; MSFT-REDTEAM]. Draw attack categories from the OWASP risks in
the design brief [OWASP-2025]. GOV.UK Chat ran red teaming with cyber security experts [UKGDS-2025].

### 3.7 Capability and regression suites

Keep two suites: a **capability** suite that starts with a low pass rate and shows progress, and a **regression**
suite that should stay near 100%. Graduate capability cases that pass reliably into regression; retire cases
that always pass and add nothing [ANTHROPIC-2026; HUSAIN-2026]. A 0% pass rate across many trials usually means
a broken task or grader: Anthropic reports one of its models' benchmark scores moving from 42% to 95% after
grading and task fixes and a less constrained scaffold (vendor-published) [ANTHROPIC-2026]. Re-run the regression suite on every model, prompt, retrieval-index,
tool or input-system change.

### 3.8 Online monitoring

| Metric | What it shows | Source |
|---|---|---|
| Override rate and edit size | Where users do not trust or cannot use the output; high or rising overrides, or overrides that beat the system, signal a need to revise | [FRB-2011; NIST-2024, MS-4.2-004] |
| Escalation rate | Load on people; mis-tuned triggers | [OPENAI-2025] |
| Error categories from sampled traces | New failure modes; drift | [HUSAIN-2026; APPLIEDLLMS-2024] |
| Rework and defects found later | Errors that passed review | Pattern file §7 |
| Cost per task and usage by group | Cost creep; whether a smaller model passes the same evals | [ANTHROPIC-2026; OPENAI-2025] |
| Input coverage, data freshness, retrieval health | Silent failures that raise no errors | [GOOGLE-RULES, Rule 10] |

Sampling cadence: read traces daily while piloting, then 10–20 a week plus 100 or more fresh traces per review
cycle (practitioner guidance; Husain suggests cycles of two to four weeks) [APPLIEDLLMS-2024, 2.1.2; HUSAIN-2026].
No public source gives independently measured override or escalation rates for live knowledge-work systems, so
set the normal range from the team's own pilot.

### 3.9 Evidence for regulated and professional work

Keep the case inventory, gold answers, results by version, judge calibration, red-team scorecard and decisions.
The UK audit regulator's guidance (which adds no new requirements) sets out what firms should document: what a
tool does, when it is appropriate to use, how it was developed and tested, and why the firm is confident it works
as intended, with adjusted expectations for third-party tools [FRC-2025]. Bank model-risk guidance asks for
independent validation, a model inventory and ongoing monitoring [FRB-2011; BOE-2023], including analysis of
overrides [FRB-2011]. The ABA says the lawyer stays fully responsible [ABA-2024].

## 4. Thresholds and starting numbers

| Item | Starting value | Basis |
|---|---|---|
| Starter case set | 20–50 tasks | [ANTHROPIC-2026, Step 0] |
| Traces for discovery | at least 30 read yourself; about 100 diverse traces | [HUSAIN-2026] |
| Labelled examples per judged failure mode | roughly 100–200 | [HUSAIN-2026] |
| Regression suite pass rate | near 100% | [ANTHROPIC-2026] |
| Capability suite | starts low | [ANTHROPIC-2026] |
| Acceptance pass rate | a product decision by failure tolerance; 100% on everything suggests the evals are too easy | [HUSAIN-2024; HUSAIN-2026] |
| Launch accuracy bar | no universal number; after an early experiment, GDS judged that 80% answer accuracy, assessed by content designers, needed improving before deployment to users on GOV.UK | [UKGDS-2025] |
| Irreversible or client-facing failure classes | a stated tolerance (including zero) and a mitigating control before launch | *(advisor default)* |

Set the launch bar from expert-rated quality, not from user satisfaction: nearly 70% of GOV.UK Chat testers
surveyed after use found responses useful, while expert-rated accuracy was 80% and judged not yet enough
[UKGDS-2025].

**Seen in the field.** `professional-services-quality-review-05` (grade B): firms benchmark tools against expert
answers to set review depth by task. `professional-services-quality-review-07` (grade B): standing evaluation
suites, gold answers and change control written into a law firm role (a job description; no results published).
`assurance-quality-management-04` (grade C): evaluation sets and parallel running before limited deployment of
an audit tool (no parallel-run results published).

## 5. Question bank

- What would two senior practitioners independently agree is a correct output for these cases? Where do they
  disagree? [T]
- Which real failures from recent months should become test cases? [T]
- Who is the single domain expert who decides what "good" means? [T][U/O]
- What failure modes have we seen in the first 30–100 traces? [T]
- What pass rate on which cases would we accept, and which failure types are unacceptable at any rate? [U/O]
- Does it need to work every time, or is one good attempt among several enough? [T][U/O]
- How will we check a model judge against human labels, and how often will we recheck? [T]
- Who outside the build team will test it adversarially before launch? [U/O]
- What does the regulator, client or professional body expect to see as evidence of testing? [U/O]
- How does the current process score on the same cases? [T][U/O]

## 6. Expert moves

1. **Seed the set from real failures and from what the team already checks by hand** [ANTHROPIC-2026].
2. **Two-expert test** on every judgment case; make someone pass it themselves [ANTHROPIC-2026]. In professional
   services this is where partners and managers disagree on "correct".
3. **One accountable expert reads 20–50 outputs, then about 100 traces, noting the first failure in each**
   [HUSAIN-2026]. Reveals the taxonomy that decides which evaluators to build.
4. **Choose the grader per failure mode** and label 100–200 examples per judged mode [HUSAIN-2026].
5. **Validate the judge against human labels** with precision and recall [HUSAIN-2024; ANTHROPIC-2026].
6. **Report pass-all with drill-down** [HUSAIN-2026; APPLIEDLLMS-2024].
7. **Run several trials and report the all-trials rate** where users expect it to work every time; on a 2024
   customer-service agent benchmark the best agent (2024 models) succeeded on under 50% of tasks, and in the
   retail domain under 25% succeeded on all of eight trials [ANTHROPIC-2026; SIERRA-2024].
8. **Test the verification effort itself:** check the tool on a small, manually reviewed subset, then set how
   much of the rest to review; ABA Opinion 512 gives the example of testing a contract-summary tool on a smaller
   set first [ABA-2024].
9. **Red-team with a scorecard, using people who did not build it** [NIST-2024; MSFT-REDTEAM].
10. **Distrust a 0% or 100% score until you have read the transcripts** [ANTHROPIC-2026; HUSAIN-2026].

## 7. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Vibe checks only | Rechat's assistant plateaued, with fixes to one failure causing others, before an eval system was built (practitioner case, self-described) [HUSAIN-2024] | Evals before scale; error analysis on traces |
| Generic metrics and 1–5 scales | [HUSAIN-2026; APPLIEDLLMS-2024; YAN-2023] | Failure taxonomy; binary checks; pass-all |
| Trusting an uncalibrated judge | [LMSYS-2023; SHANKAR-2024; THOUGHTWORKS-2025] | Calibrate against human labels |
| Saturated or broken evals | 42% to 95% after grader fixes [ANTHROPIC-2026] | Read transcripts; separate suites |
| Checking conclusions but not citations | A consultancy report for an Australian department contained nonexistent references; a partial refund followed (press report) [GUARDIAN-2025] | A code check that each cited source exists and says what is claimed; a named reviewer |
| Best-of-k reporting | [SIERRA-2024] | Report the all-trials rate for evidence-producing flows |

## 8. Worked example: evidence matching in an audit practice

Illustrative, continuing step 3.

- **Quality owner:** the practice's methodology senior manager.
- **Cases:** 40 samples from closed engagements, held in the audit platform: 25 clean, 8 with a known mismatch
  (wrong period, amount off, missing approval), 7 with no supporting evidence on file (should not match).
- **Gold answers:** two seniors label each case; they disagree on 6 approval-evidence cases, which leads to a
  clearer line in the attribute checklist.
- **Failure modes and checks:** match without a source link (code check, zero tolerance); amount or date mismatch
  missed (code check against the extracted values, zero tolerance); match proposed where no evidence exists
  (code check on should-not cases, zero tolerance); evidence judged sufficient when it is not (human review of
  every case in the pilot; a model judge is not used yet).
- **Consistency:** three runs per case; zero-tolerance checks must pass on all three.
- **Thresholds:** zero-tolerance checks 100% on all trials; pass-all at or above the rate seniors reached by hand
  on the same cases.
- **Baseline:** last season's review notes on evidence for these engagements, and the seniors' own pass-all.
- **Red team:** two staff from another office try evidence files containing embedded instructions and altered
  dates.
- **Monitoring:** override rate per attribute, re-performed sample disagreement, time to approve (rubber-stamp
  watch), cost per engagement.

## 9. Output

Write `eval-plan.md` from `../templates/eval-plan.md`. Set its frontmatter (`solution`, `version`, `status`,
`thresholds_agreed_by`). In `brief.md` set `step_completed: 4`, `next_step: 5`, `updated`, and link the plan in
the decisions log. Results from the prototype go into the plan's §10 results log; they are the evidence the
**ai-portfolio** gate into pilot asks for.

## 10. Sources

- `ABA-2024` — American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools*,
  2024-07-29. https://www.mcle.org/ePrograms/2250081P01/1--aba-formal-opinion-512.pdf
- `ANTHROPIC-2026` — Anthropic, *Demystifying evals for AI agents*, vendor engineering guide, 2026-01-09.
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, 2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, 2026-06-04. https://arxiv.org/pdf/2512.04123
- `BOE-2023` — Bank of England PRA, *SS1/23 Model risk management principles for banks*, 2023-05-17 (updated
  version published 2026-04-23, which keeps the model inventory and independent validation principles).
  https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- `FRB-2011` — Federal Reserve Board and OCC, *SR 11-7: Supervisory Guidance on Model Risk Management*,
  2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `FRC-2025` — UK Financial Reporting Council, *AI in audit: illustrative example and documentation guidance*,
  regulator guidance, 2025-06-26. https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf (news release:
  https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/)
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `GUARDIAN-2025` — The Guardian Australia, *Deloitte to pay money back to Albanese government after using AI in
  $440,000 report*, 2025-10-06. https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report
- `HUSAIN-2024` — Hamel Husain, *Your AI Product Needs Evals*, 2024-03-29. https://hamel.dev/blog/posts/evals/
- `HUSAIN-2026` — Hamel Husain (with Shreya Shankar), *LLM Evals: Everything You Need to Know (FAQ)*, 2026-09-18.
  https://hamel.dev/blog/posts/evals-faq/
- `LMSYS-2023` — Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, 2023. https://arxiv.org/pdf/2306.05685
- `MSFT-REDTEAM` — Microsoft Learn, *AI Red Teaming Agent*, vendor documentation, undated.
  https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, 2025-04.
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `OWASP-2025` — OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*, 2025. https://genai.owasp.org/llm-top-10/
- `SHANKAR-2024` — Shankar et al., *Who Validates the Validators?*, 2024-04-18. https://arxiv.org/pdf/2404.12272
- `SIERRA-2024` — Yao et al. (Sierra), *tau-bench*, 2024-06-17. https://arxiv.org/pdf/2406.12045
- `THOUGHTWORKS-2025` — Thoughtworks, *LLM as a judge* (Technology Radar), updated 2025-11-05.
  https://www.thoughtworks.com/radar/techniques/llm-as-a-judge
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, 2025-02-10.
  https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
- `VALS-2025` — Vals AI with Legaltech Hub, *Vals Legal AI Report*, updated 2025-02-27. https://www.vals.ai/vlair
- `YAN-2023` — Eugene Yan, *Patterns for Building LLM-based Systems and Products*, 2023-07. https://eugeneyan.com/writing/llm-patterns/
