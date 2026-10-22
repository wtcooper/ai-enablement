# Evaluation plan (step 4)

Read this on entering step 4. The evaluation plan is the centre of delivery: it says what "good" means in the
team's own terms, decides whether the solution is fit to launch, and keeps telling the team after launch. You
design the plan; the firm's people run it in their approved systems. Keys in brackets are listed in §7.
*(advisor default)* marks a working rule, not a finding from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Building the plan](#3-building-the-plan)
4. [Thresholds and starting numbers](#4-thresholds-and-starting-numbers)
5. [Worked example: evidence matching in an audit practice](#5-worked-example-evidence-matching-in-an-audit-practice)
6. [Output](#6-output)
7. [Sources](#7-sources)

## 1. Goal and exit criteria

**Goal.** A plan the business owner has agreed, which turns "is it good enough?" into checks anyone can run and a
decision rule for launch.

**Exit when all of these are true:**

- One **quality owner** named by role: the domain expert who decides what "good" means.
- A **case inventory** (§3.1), listed by id, type and source, never content (rule 5), with **gold answers**
  checked by two experts where judgment is involved.
- A **failure taxonomy** with one **binary check** per failure mode and its grader (code, model judge, human);
  **judge calibration** planned for every model-graded check.
- **Consistency** (trials per case, whether every trial must pass) and **thresholds** per failure class,
  including zero-tolerance classes with a mitigating control, agreed by the business owner.
- A **baseline** (the current process on the same cases), **red-teaming** by people outside the build, a
  **regression** policy, **online monitoring** with owners, normal ranges and responses, and **evidence
  retained** for review, inspection or audit.

## 2. How to run it

1. **Name the quality owner:** one accountable domain expert, not a committee.
2. **Collect cases and gold answers** (§3.1). The user holds the cases in the firm's systems. The quality owner
   settles expert disagreements; each one is a requirement to clarify.
3. **Find the failure modes:** before a prototype, from the pattern file's §6 and the step 1 error history; once
   there is one, by error analysis on real traces (§3.2). Choose a check and grader per mode (§3.3).
4. **Set consistency, thresholds and the baseline** (§3.4, §4) with the business owner. A pass rate is a product
   decision about failure tolerance [HUSAIN-2024].
5. **Plan red-teaming, regression and online monitoring** (§3.5, §3.6), using the pattern file's §7 metrics.
6. **Professional work:** set the human verification level by testing on a small, manually reviewed subset
   first; ABA Opinion 512 gives the example of a contract-summary tool tested on a smaller set [ABA-2024]. Record
   the evidence the regulator, client or professional body will expect (§3.7).
7. **Play back** the acceptance sentence; mark the plan `agreed` only when the owner accepts it. Name step 5 as
   next, or loop back to step 3 if the design cannot meet the bar.

## 3. Building the plan

### 3.1 Cases and gold answers

- **Seed from reality:** past failures, reviewer corrections, the step 1 error history. **Balance** with cases
  where the behaviour should not happen, or one-sided tests reward over-triggering [ANTHROPIC-2026, Step 3].
- **Two-expert test:** a good task is one two domain experts would independently pass or fail the same way; have
  someone pass it themselves [ANTHROPIC-2026, Step 2]. Experts may disagree on open-ended outputs, and rater
  disagreement needs reconciling [ANTHROPIC-2026]; in professional services gold answers usually come from a
  senior practitioner *(advisor default)*.

### 3.2 Error analysis

The quality owner reads 20–50 outputs (about 30 minutes), notes the first failure in each, and works up to about
100 diverse traces until new ones stop revealing new failure modes; build the taxonomy from the notes, then the
evaluators [HUSAIN-2026]. Criteria drift is normal: people define "good" after seeing outputs [SHANKAR-2024].

### 3.3 Checks, graders and judge calibration

| Failure is… | Grader | Example |
|---|---|---|
| Objective (format, field present, figure ties to source, cited source exists) | Code check | Every match carries a source link |
| A judgment call (relevance, sufficiency, tone) | Model judge, calibrated; or human | "Evidence supports the attribute" |
| High stakes or new | Human review sample | A manager reviews a set per run |

- Use binary pass/fail per check and report a **pass-all rate** with drill-down, not 1–5 scales
  [HUSAIN-2026; APPLIEDLLMS-2024, 1.4.5]. Read transcripts before believing any score, especially 0% or 100%
  [ANTHROPIC-2026].
- **Check citations, not only conclusions:** a consultancy report for an Australian department contained
  nonexistent references, and a partial refund followed (press report) [GUARDIAN-2025].
- **Calibrate judges** against human labels with precision and recall, not raw agreement; give the judge an
  "unknown" option; judge one dimension at a time; re-check when the model, prompt or case mix changes
  [HUSAIN-2024; ANTHROPIC-2026, Step 5]. Why: the MT-Bench study reported over 80% agreement between a strong
  judge and human preferences but also position, verbosity and self-enhancement biases [LMSYS-2023];
  Thoughtworks moved LLM-as-a-judge to "Assess" in November 2025, citing reliability concerns [THOUGHTWORKS-2025].

### 3.4 Consistency and baseline

- **Consistency:** pass@k asks whether any of k tries works; pass^k whether all k do. A 75% per-trial rate gives
  about 42% over three trials (arithmetic example) [ANTHROPIC-2026; SIERRA-2024]. On a 2024 customer-service
  agent benchmark, the best agent succeeded on under 50% of tasks, and in retail under 25% succeeded on all of
  eight trials (benchmark paper from an agent vendor's research team) [SIERRA-2024]. For client-facing or
  evidence-producing work, report the all-trials rate.
- **Baseline:** run the current process on the same cases; in a UC Berkeley-led survey of practitioners with
  deployed agents, only 39% compared their agent with a non-agentic baseline [BERKELEY-2026].

### 3.5 Red-teaming and regression

- **Red team** any client-facing or tool-using solution before launch, with a scorecard (attack categories,
  attempts, success rate), people not involved in development, and a re-run trigger [NIST-2024, MS-1.3-002,
  MS-1.3-003; MSFT-REDTEAM]. Draw categories from the OWASP risks in the design brief [OWASP-2025].
- **Two suites:** a capability suite that starts low and shows progress, and a regression suite near 100%.
  Graduate reliable cases into regression; retire cases that always pass [ANTHROPIC-2026; HUSAIN-2026]. A 0%
  pass rate usually means a broken task or grader: Anthropic reports a benchmark score moving from 42% to 95%
  after grading and task fixes and a less constrained scaffold (vendor-published) [ANTHROPIC-2026]. Re-run the
  regression suite on every model, prompt, retrieval-index, tool or input-system change.

### 3.6 Online monitoring

| Metric | What it shows | Source |
|---|---|---|
| Override rate and edit size | Where users do not trust or cannot use the output; high or rising overrides, or overrides that beat the system, signal a need to revise | [FRB-2011; NIST-2024, MS-4.2-004] |
| Escalation rate | Load on people; mis-tuned triggers | [OPENAI-2025] |
| Error categories from sampled traces; rework found later | New failure modes; drift; errors that passed review | [HUSAIN-2026]; pattern file §7 |
| Cost per task and usage by group | Cost creep; whether a smaller model passes the same evals | [ANTHROPIC-2026; OPENAI-2025] |
| Input coverage, data freshness, retrieval health | Silent failures that raise no errors | [GOOGLE-RULES, Rule 10] |

Read traces daily while piloting, then 10–20 a week plus 100 or more fresh traces per review cycle (practitioner
guidance) [APPLIEDLLMS-2024, 2.1.2; HUSAIN-2026]. No public source gives measured override or escalation rates
for live knowledge-work systems, so set normal ranges from the team's own pilot.

### 3.7 Evidence for regulated and professional work

Keep the case inventory, gold answers, results by version, judge calibration, red-team scorecard and decisions.
The UK audit regulator's guidance (which adds no new requirements) says firms should document what a tool does,
when it is appropriate, how it was developed and tested, and why the firm is confident it works, with adjusted
expectations for third-party tools [FRC-2025]. Bank model-risk guidance asks for independent validation, a model
inventory and ongoing monitoring, including analysis of overrides [FRB-2011; BOE-2023]. The ABA says the lawyer
stays fully responsible [ABA-2024].

## 4. Thresholds and starting numbers

| Item | Starting value | Basis |
|---|---|---|
| Starter case set | 20–50 tasks | [ANTHROPIC-2026, Step 0] |
| Labelled examples per judged failure mode | roughly 100–200, with enough passes and fails | [HUSAIN-2026] |
| Acceptance pass rate | a product decision by failure tolerance; 100% on everything suggests the evals are too easy | [HUSAIN-2024; HUSAIN-2026] |
| Irreversible or client-facing failure classes | a stated tolerance (including zero) and a mitigating control before launch | *(advisor default)* |
| Launch accuracy bar | no universal number; after an early experiment GDS judged 80% answer accuracy, assessed by content designers, needed improving before deployment, while nearly 70% of testers found responses useful. Set the bar from expert-rated quality, not satisfaction | [UKGDS-2025] |

**Seen in the field.** `professional-services-quality-review-05` (grade B): firms benchmark tools against expert
answers to set review depth by task. `professional-services-quality-review-07` (grade B): standing evaluation
suites, gold answers and change control written into a law firm role (a job description; no results published).
`assurance-quality-management-04` (grade C): evaluation sets and parallel running before limited deployment of
an audit tool (no parallel-run results published). Without an eval system, fixes to one failure can cause
others, as in Rechat's assistant (practitioner case, self-described) [HUSAIN-2024].

## 5. Worked example: evidence matching in an audit practice

Illustrative, continuing step 3. **Cases:** 40 closed-engagement samples: 25 clean, 8 with a known mismatch, 7
with no evidence on file (should not match); two seniors disagree on 6, which clarifies the checklist.
**Checks:** a match without a source link, a missed amount or date mismatch, and a match where no evidence exists
are zero-tolerance code checks; sufficiency is human-reviewed on every pilot case. **Thresholds:** three runs per
case, zero-tolerance checks pass on all three, pass-all at or above the seniors' own rate. **Red team:** staff
from another office try embedded instructions and altered dates.

## 6. Output

Write `eval-plan.md` from `../templates/eval-plan.md` and set its frontmatter (`solution`, `version`, `status`,
`thresholds_agreed_by`). In `brief.md` set `step_completed: 4`, `next_step: 5`, `updated`, and link the plan in
the decisions log. Prototype results go into the plan's §10 results log; they are the evidence the
**ai-portfolio** gate into pilot asks for.

## 7. Sources

- `ABA-2024` — American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools*, 2024-07-29. https://www.mcle.org/ePrograms/2250081P01/1--aba-formal-opinion-512.pdf
- `ANTHROPIC-2026` — Anthropic, *Demystifying evals for AI agents*, vendor engineering guide, 2026-01-09. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, 2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, 2026-06-04. https://arxiv.org/pdf/2512.04123
- `BOE-2023` — Bank of England PRA, *SS1/23 Model risk management principles for banks*, 2023-05-17 (updated version published 2026-04-23, which keeps the model inventory and independent validation principles). https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- `FRB-2011` — Federal Reserve Board and OCC, *SR 11-7: Supervisory Guidance on Model Risk Management*, 2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `FRC-2025` — UK Financial Reporting Council, *AI in audit: illustrative example and documentation guidance*, regulator guidance, 2025-06-26. https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `GUARDIAN-2025` — The Guardian Australia, *Deloitte to pay money back to Albanese government after using AI in $440,000 report*, 2025-10-06. https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report
- `HUSAIN-2024` — Hamel Husain, *Your AI Product Needs Evals*, 2024-03-29. https://hamel.dev/blog/posts/evals/
- `HUSAIN-2026` — Hamel Husain (with Shreya Shankar), *LLM Evals: Everything You Need to Know (FAQ)*, 2026-09-18. https://hamel.dev/blog/posts/evals-faq/
- `LMSYS-2023` — Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, 2023. https://arxiv.org/pdf/2306.05685
- `MSFT-REDTEAM` — Microsoft Learn, *AI Red Teaming Agent*, vendor documentation, undated. https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `OWASP-2025` — OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*, 2025. https://genai.owasp.org/llm-top-10/
- `SHANKAR-2024` — Shankar et al., *Who Validates the Validators?*, 2024-04-18. https://arxiv.org/pdf/2404.12272
- `SIERRA-2024` — Yao et al. (Sierra), *tau-bench*, 2024-06-17. https://arxiv.org/pdf/2406.12045
- `THOUGHTWORKS-2025` — Thoughtworks, *LLM as a judge* (Technology Radar), updated 2025-11-05. https://www.thoughtworks.com/radar/techniques/llm-as-a-judge
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, 2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
