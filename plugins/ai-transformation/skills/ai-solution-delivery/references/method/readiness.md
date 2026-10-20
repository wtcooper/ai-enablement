# Production readiness (step 5)

Read this on entering step 5. Readiness is operational, not only technical: a solution is ready when someone
owns it, can see how it behaves, can change it safely, can switch it off, and the people using it know what to do
when it is wrong. This file gives the readiness review, the decision rules for go or no-go, and the launch plan.
You record the review and the decision; the firm's owners make and sign the decision. Keys in brackets are listed
in §9. Lines marked *(advisor default)* are working rules, not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [The readiness review](#3-the-readiness-review)
4. [Decision rules and launch plan](#4-decision-rules-and-launch-plan)
5. [Question bank](#5-question-bank)
6. [Expert moves](#6-expert-moves)
7. [Common traps](#7-common-traps)
8. [Worked example: evidence matching in an audit practice](#8-worked-example-evidence-matching-in-an-audit-practice)
9. [Output and sources](#9-output-and-sources)

## 1. Goal and exit criteria

**Goal.** A recorded go, go-with-conditions or no-go decision, resting on evidence the firm could show a client,
regulator or inspector.

**Exit when all of these are true:**

- Every line of the readiness review (§3) is marked ready, gap or not applicable, with its evidence.
- The evaluation results meet the agreed thresholds in `eval-plan.md`, and red-team results were considered.
- A named owner, a rollback path, logging and a first review point exist (no go-live without them).
- An adoption plan exists, agreed with the **ai-enablement** skill or written here in outline.
- The inventory entry and risk tier are confirmed with **ai-governance**; where independent validation is
  required, it has happened.
- The benefit metric, baseline, forecast range and counterfactual are ready for the **ai-portfolio** benefits
  register.
- A staged launch plan (§4.2) and the decision, with each condition's owner and clearing event, are recorded.

## 2. How to run it

1. **Name the step.** "Now we check whether this is ready to run as a supported service."
2. **Read the inputs:** `brief.md` (owners, design, checkpoints, cost envelope), `eval-plan.md` (thresholds,
   results log, monitoring), and `overlay/policy.md` (risk tier, required review, records of AI use).
3. **Go through the review** (§3) one block at a time. Ask for evidence, not intent: "Show me the runbook"
   rather than "Is there a runbook?". Mark each line.
4. **Settle the people side** with the adoption block (§3.5). Hand the full programme design to
   **ai-enablement**.
5. **Check the documentation pack** for regulated or professional work (§3.4).
6. **Offer an independent challenge** of the whole pack before the decision (the `review-solution` brief; see
   SKILL.md, Delegation). NIST's profile suggests documenting how the results of structured feedback exercises,
   which include red-teaming, fed the go/no-go decision [NIST-2024, MS-4.2-005].
7. **Apply the decision rules** (§4.1), write the staged launch plan (§4.2) and record who decided.
8. **Send the gate evidence** to **ai-portfolio**: the readiness decision, eval results and benefit inputs.
9. **Name step 6** and the event that starts it.

Pilot first? If the portfolio runs a pilot with real users before production, use the same review at a lighter
depth before the pilot (owner, logging, rollback, every item reviewed, first group trained) and the full review
before production *(advisor default)*.

## 3. The readiness review

### 3.1 Ownership and support

- Named owner and backup, by role; support route and hours; who responds when it fails out of hours.
- A runbook: common failures, how to pause, who to call.
- An incident process with defined ownership, rehearsal and post-incident review [NIST-2024, GV-6.2-003,
  MG-4.2-002]. UK guidance asks for named senior responsible owners [UKGDS-2025].
- A review rota that includes reading traces [APPLIEDLLMS-2024, 2.1.2].

### 3.2 Change control and rollback

- A quantitative testing and validation step in change control: any model, prompt, retrieval or tool change
  re-runs the regression suite before release [UKGDS-2025].
- Models and prompts pinned and versioned [APPLIEDLLMS-2024, 2.2.3].
- A managed release that can be withdrawn, and a tested rollback or pause to the manual process [UKGDS-2025;
  NIST-2024, GV-6.2-006].

### 3.3 Monitoring and cost

- The online metrics from `eval-plan.md` §8 are live with alert thresholds and responders: override,
  escalation, error categories, rework, cost per task, usage by group [FRB-2011; NIST-2024].
- Input coverage, data freshness and retrieval health watched, not only outputs [GOOGLE-RULES, Rule 10;
  GOOGLE-2021].
- Cost per task and usage visible to the owner [UKGDS-2024; OPENAI-2025]. For the firm's wider AI spend, see
  `professional-services-firm-finance-11` (grade B; practitioners' own accounts of reading consumption bills).
- Logging, retention and access meet client confidentiality terms [UKGDS-2024; ABA-2024].

### 3.4 Evidence and documentation

- Eval results by version meet thresholds; red-team scorecard reviewed.
- **Independent validation** where required: in regulated settings validation should be independent of
  development [FRB-2011; BOE-2023; NIST-2024, MS-1.3-003].
- **Inventory and risk tier:** the solution is recorded in the firm's AI or model inventory with owner and risk
  tier [FRB-2011; BOE-2023] (with **ai-governance**).
- **Documentation pack** for regulated or professional work: what the tool does, when it is appropriate, how it
  was developed and tested, how the firm knows it works, known limits, the review level, change history and
  owners [FRC-2025; FRB-2011]. In law, the lawyer stays fully responsible for the output [ABA-2024].
- Security and privacy sign-off; access-control review [UKGDS-2025; OWASP-2025].

### 3.5 People and adoption

- **Training before access** *(advisor default)* on what the tool does well, its limits, the review expected, and
  what to do when it is wrong; the ABA expects supervising lawyers to make sure staff are trained on capabilities
  and limitations [ABA-2024]. A law firm studied by CIPD made training a condition of use and kept a "verify,
  verify, verify" rule (anonymized practitioner case) [CIPD-2026]. In BCG's survey of more than 10,600 leaders,
  managers and frontline employees in 11 countries and regions, regular use was sharply higher among employees
  with at least five hours of training and access to in-person training and coaching, and only one-third said
  they had been properly trained (self-reported) [BCG-ATWORK-2025].
- **What changes on the first day:** the steps people now do differently, and who they ask.
- **Feedback loop:** how corrections and failures reach the eval set.
- **Visible senior use:** have senior people use it and share what worked and what did not [CIPD-2026].
- **Role evolution communicated** in the firm's own terms (rule 2; see
  `../../../transformation-advisor/references/method/people-and-change.md`).
- People and process are most of the work: BCG's survey of 1,000 CxOs and senior executives attributes about 70%
  of AI implementation challenges to people and process (self-reported) [BCG-2024].

## 4. Decision rules and launch plan

### 4.1 Decision rules

- **No go-live without** a named owner, a rollback path, logging and a first review point *(advisor default,
  consistent with UKGDS-2025 and NIST-2024)*.
- **Go/no-go uses** red-team and structured-feedback results explicitly, and the record says how [NIST-2024,
  MS-4.2-005].
- **Any zero-tolerance failure** in the latest results means no-go until fixed and re-run *(advisor default)*.
- **Go-with-conditions** only when each condition is specific, has an owner, and names the event that clears it;
  a condition that touches a zero-tolerance class or the rollback path is a no-go instead *(advisor default)*.
- **Regulated settings:** validation independent of development before go [FRB-2011; BOE-2023].
- **Outside the catalog:** no go until **ai-governance** has approved the tool.

### 4.2 Staged launch plan

- **Stages by group**, smallest first, then widen; write the evidence needed to widen each time.
- **Human review starts at its fullest** and is reduced only with measured evidence; testing on a small,
  manually reviewed set first is the logic the ABA describes [ABA-2024]; OpenAI advises planning human
  intervention, especially early in deployment [OPENAI-2025].
- **First review point** is an event, for example "after the first full trace-review cycle on live work", never a
  calendar date (rule 9).
- **Benefits:** agree the counterfactual (parallel run, staggered start or comparison group) before go-live,
  and give the metric, baseline and forecast range to **ai-portfolio** for `portfolio/benefits.yaml`.

## 5. Question bank

- Who is on the hook when it fails at 6pm on a Friday? Show me the runbook. [T][U/O]
- How do we pause or roll back, and who can? Has anyone tried it? [T][U/O]
- What is logged, for how long, who can read it, and how does that meet client confidentiality? [U/O]
- What are the monitoring metrics and their alert thresholds, and who responds? [T][U/O]
- What is the change rule when the model, prompt, retrieval index or tools change? [U/O]
- What is the adoption plan: who is trained, what do they do differently on the first day, what do they do when
  the tool is wrong? [T][U/O]
- Is the solution in the AI inventory with an owner and risk tier? [U/O]
- Who outside the build team reviewed the evidence? [U/O]
- What would make us pull it back after launch? [T][U/O]

## 6. Expert moves

1. **Log every input and output from the first user, then sample** [APPLIEDLLMS-2024; HUSAIN-2026].
2. **Track overrides, escalations and rework as monitoring metrics**; high override rates, or overrides that
   consistently improve on the output, signal a need to revise [FRB-2011; NIST-2024].
3. **Define the managed release and rollback path before launch** [UKGDS-2025; APPLIEDLLMS-2024].
4. **Watch for silent failures:** coverage, freshness, retrieval health [GOOGLE-RULES; GOOGLE-2021].
5. **Track cost per task from the eval runs onward**; set a baseline with the strongest model, then test smaller
   ones against the same evals [ANTHROPIC-2026; OPENAI-2025].
6. **Ask for evidence, not intent**, line by line *(advisor default)*.

## 7. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| No owner, support or runbook after launch | Mostly guidance, not measurement [NIST-2024; UKGDS-2025] | Named owner, runbook and review rota before go |
| Demo-to-production gap | Building is cheap relative to maintaining ML systems [GOOGLE-2015] | Readiness review with evidence; change control |
| Silent decay | [GOOGLE-RULES, Rule 10] | Input and freshness monitoring |
| Licences without use | Law360 reports firms with licences that go unused (no figure) [LAW360-2025] | Training, a named workflow and a champion with access |
| Validation by the builders only | [FRB-2011; NIST-2024, MS-1.3-003] | Independent reviewer for evidence and red team |

## 8. Worked example: evidence matching in an audit practice

Illustrative, continuing step 4. Readiness before production, after a pilot on five engagements.

| Block | Status | Evidence |
|---|---|---|
| Ownership | Ready | Methodology team owns it; pilot lead as backup; runbook covers unreadable files and pausing |
| Change control | Gap | Vendor model updates arrive with platform releases; regression cases exist but no rule to re-run them |
| Rollback | Ready | Feature can be switched off per engagement; manual matching is the fallback, tried on one engagement |
| Monitoring | Ready | Override rate per attribute and re-performance disagreement reported per engagement |
| Evidence | Ready | Zero-tolerance checks passed on all three runs; red-team found one embedded-instruction case, fixed and re-run |
| Documentation | Ready | Methodology note on use, limits and review level; tool and version recorded in each file |
| Governance | Ready | Inventory entry with risk tier `tier-4`; quality partner reviewed the pack independently of the pilot team |
| Adoption | Ready | Two-hour training before access; first-day changes listed; mismatches route to the senior |

- **Decision:** go-with-conditions, decided by the audit partner and the quality partner. **Condition:** the
  methodology team writes the rule that every platform release re-runs the regression cases before use
  (owner: methodology lead; clears when the rule is in the methodology note).
- **Launch plan:** the next ten engagements, every match reviewed; widen when re-performance disagreement stays
  inside the agreed range across them. First review point: after those ten engagements.
- **Handoffs:** gate evidence and the benefit inputs (net hours per engagement, last season's baseline, the
  forecast range, a staggered start by office) to **ai-portfolio**; the training and first-day guide to
  **ai-enablement**.

## 9. Output and sources

**Output.** Write `readiness.md` from `../templates/readiness.md` and set its frontmatter (`decision`,
`decided_by`, `conditions`). In `brief.md` set `owners.support`, `step_completed: 5`, `next_step: 6` and
`updated`; record the decision in the decisions log and the handoffs table.

**Sources**

- `ABA-2024` — American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools*,
  2024-07-29. https://www.mcle.org/ePrograms/2250081P01/1--aba-formal-opinion-512.pdf
- `ANTHROPIC-2026` — Anthropic, *Demystifying evals for AI agents*, 2026-01-09.
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, 2024-06-08. https://applied-llms.org/
- `BCG-2024` — Boston Consulting Group, *AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale
  Value*, press release, 2024-10-24. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- `BCG-ATWORK-2025` — Boston Consulting Group, *AI at Work: Momentum Builds, but Gaps Remain*, survey report,
  2025-06-26. https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
- `BOE-2023` — Bank of England PRA, *SS1/23 Model risk management principles for banks*, 2023-05-17 (updated
  version published 2026-04-23, which keeps the model inventory and independent validation principles).
  https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- `CIPD-2026` — CIPD with the Institute for the Future of Work, *How a law firm introduced an AI legal
  assistant*, practitioner case study, 2026-03-25. https://www.cipd.org/ae/knowledge/case-studies/ai-legal-assistant/
- `FRB-2011` — Federal Reserve Board and OCC, *SR 11-7: Supervisory Guidance on Model Risk Management*,
  2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `FRC-2025` — UK Financial Reporting Council, *AI in audit: illustrative example and documentation guidance*,
  regulator guidance, 2025-06-26. https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf
- `GOOGLE-2015` — Sculley et al., *Hidden Technical Debt in Machine Learning Systems*, 2015.
  https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- `GOOGLE-2021` — Google Cloud, *Practitioners guide to MLOps*, white paper, 2021-05.
  https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HUSAIN-2026` — Hamel Husain, *LLM Evals: Everything You Need to Know (FAQ)*, 2026-09-18. https://hamel.dev/blog/posts/evals-faq/
- `LAW360-2025` — Law360 Pulse, *How Law Firms Turn AI Skeptics Into 'Champions'*, 2025-09-26. https://www.law360.com/pulse/articles/2392818
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, 2025-04.
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `OWASP-2025` — OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*, 2025. https://genai.owasp.org/llm-top-10/
- `UKGDS-2024` — UK Government Digital Service, *Generative AI Framework for HMG*, 2024-01-18 (withdrawn 2025-02-10).
  https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, 2025-02-10.
  https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
