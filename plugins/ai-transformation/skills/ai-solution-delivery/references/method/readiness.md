# Production readiness (step 5)

Read this on entering step 5. A solution is ready when someone owns it, can see how it behaves, can change it
safely, can switch it off, and its users know what to do when it is wrong. You record; the firm's owners decide.
Keys in brackets are listed in §6; *(advisor default)* marks a working rule, not a finding from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [The readiness review](#3-the-readiness-review)
4. [Decision rules and launch plan](#4-decision-rules-and-launch-plan)
5. [Worked example: evidence matching in an audit practice](#5-worked-example-evidence-matching-in-an-audit-practice)
6. [Output and sources](#6-output-and-sources)

## 1. Goal and exit criteria

**Goal.** A recorded go, go-with-conditions or no-go, resting on evidence the firm could show a client, regulator
or inspector.

**Exit when all of these are true:**

- Every line of the review (§3) is marked ready, gap or not applicable, with its evidence; evaluation results
  meet the agreed thresholds in `eval-plan.md`, and red-team results were considered.
- A named owner, a rollback path, logging and a first review point exist; an adoption plan exists, agreed with
  **ai-enablement** or written here in outline.
- The inventory entry and risk tier are confirmed with **ai-governance**; independent validation has happened
  where required.
- The benefit metric, baseline, forecast range and counterfactual are ready for the **ai-portfolio** register.
- A staged launch plan (§4.2) and the decision, with each condition's owner and clearing event, are recorded.

## 2. How to run it

1. **Read the inputs:** `brief.md`, `eval-plan.md` and `overlay/policy.md` (risk tier, required review, records
   of AI use).
2. **Go through the review** (§3) one block at a time. Ask for evidence, not intent: "Show me the runbook", not
   "Is there a runbook?" *(advisor default)*. Hand the full adoption programme to **ai-enablement**.
3. **Offer an independent challenge** of the pack before the decision (the `review-solution` brief; SKILL.md,
   Delegation). NIST's profile suggests documenting how structured feedback, including red-teaming, fed the
   go/no-go decision [NIST-2024, MS-4.2-005].
4. **Apply the decision rules** (§4.1), write the staged launch plan (§4.2) and record who decided.
5. **Send the gate evidence** (decision, eval results, benefit inputs) to **ai-portfolio** and name step 6 and the
   event that starts it.

If the portfolio runs a pilot with real users first, use the same review at a lighter depth before the pilot
(owner, logging, rollback, every item reviewed, first group trained) and the full review before production
*(advisor default)*.

## 3. The readiness review

The review's lines are in `../templates/readiness.md`. What to look for in each block:

| Block | Look for | Source |
|---|---|---|
| Ownership and support | Named owner and backup by role; who responds out of hours; a runbook; an incident process with rehearsal and post-incident review; a review rota that reads traces; UK guidance asks for named senior responsible owners | [NIST-2024, GV-6.2-003, MG-4.2-002; UKGDS-2025; APPLIEDLLMS-2024, 2.1.2] |
| Change control and rollback | Every model, prompt, retrieval or tool change re-runs the regression suite before release; models and prompts pinned; a managed release that can be withdrawn; a tested pause to the manual process. Building is cheap relative to maintaining ML systems | [UKGDS-2025; NIST-2024, GV-6.2-006; GOOGLE-2015] |
| Monitoring and cost | Online metrics from `eval-plan.md` live with alert thresholds and responders; every input and output logged from the first user, then sampled; input coverage and freshness watched; cost per task visible to the owner; logging meets client confidentiality terms | [FRB-2011; HUSAIN-2026; GOOGLE-RULES, Rule 10] |
| Evidence and documentation | Thresholds met; red-team scorecard reviewed; in regulated settings, validation independent of development; an inventory entry with owner and tier (with **ai-governance**); a documentation pack (what it does, when to use it, how it was built and tested, why the firm trusts it, limits, review level, change history, owners), which the UK audit regulator's guidance sets out without adding requirements, with adjusted expectations for third-party tools; security sign-off. In law, the lawyer stays fully responsible | [FRB-2011; BOE-2023; FRC-2025; ABA-2024] |

For the firm's wider AI spend, see `professional-services-firm-finance-11` (grade B; practitioners' own accounts
of reading consumption bills).

**People and adoption.**

- **Training before access** *(advisor default)*: strengths, limits, the review expected, what to do when it is
  wrong. The ABA expects supervising lawyers to make sure staff are trained on capabilities and
  limitations [ABA-2024]. A law firm studied by CIPD made training a condition of use and kept a "verify, verify,
  verify" rule (anonymized practitioner case) [CIPD-2026]. In BCG's survey of more than 10,600 leaders, managers
  and frontline employees in 11 countries and regions, regular use was sharply higher with at least five hours of
  training and access to in-person coaching, and only one-third said they had been properly trained
  (self-reported) [BCG-ATWORK-2025].
- **First-day changes** and who people ask; a **feedback loop** from corrections to the eval set; **role
  evolution** communicated in the firm's own terms (rule 2).
- **Visible senior use:** senior people use it and share what worked [CIPD-2026]. Licences alone do not create
  use: Law360 reports firms with unused licences (no figure) [LAW360-2025].

## 4. Decision rules and launch plan

### 4.1 Decision rules

- **No go-live without** a named owner, a rollback path, logging and a first review point (rule 13).
- **Go/no-go uses** red-team and structured-feedback results explicitly, and the record says how [NIST-2024,
  MS-4.2-005].
- **Any zero-tolerance failure** in the latest results means no-go until fixed and re-run *(advisor default)*.
- **Go-with-conditions** only when each condition is specific, has an owner and names the event that clears it;
  a condition touching a zero-tolerance class or the rollback path is a no-go instead *(advisor default)*.
- **Regulated settings:** validation independent of development before go [FRB-2011; BOE-2023].
- **Outside the catalog:** no go until **ai-governance** has approved the tool.

### 4.2 Staged launch plan

- **Stages by group**, smallest first, with the evidence needed to widen each time. **Human review starts at its
  fullest** and is reduced only on measured evidence; OpenAI advises planning human intervention, especially
  early in deployment [OPENAI-2025].
- **First review point** is an event, for example "after the first full trace-review cycle on live work" (rule 9).
- **Benefits:** agree the counterfactual (parallel run, staggered start or comparison group) before go-live and
  give the metric, baseline and forecast range to **ai-portfolio** for `portfolio/benefits.yaml`.

## 5. Worked example: evidence matching in an audit practice

Illustrative, after a pilot on five engagements. Every block is ready except change control: vendor model
updates arrive with platform releases, and no rule re-runs the regression cases. The inventory shows `tier-4`,
and the quality partner reviewed the pack independently of the pilot team.

- **Decision:** go-with-conditions, decided by the audit partner and the quality partner. **Condition:** the
  methodology lead writes the re-run rule into the methodology note (clears when it is there).
- **Launch plan:** the next ten engagements, every match reviewed; widen when re-performance disagreement stays
  inside the agreed range. First review point: after those ten engagements.

## 6. Output and sources

**Output.** Write `readiness.md` from `../templates/readiness.md` and set its frontmatter (`decision`,
`decided_by`, `conditions`). In `brief.md` set `owners.support`, `step_completed: 5`, `next_step: 6` and
`updated`; record the decision in the decisions log and the handoffs table.

**Sources**

- `ABA-2024` — American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools*, 2024-07-29. https://www.mcle.org/ePrograms/2250081P01/1--aba-formal-opinion-512.pdf
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, 2024-06-08. https://applied-llms.org/
- `BCG-ATWORK-2025` — Boston Consulting Group, *AI at Work: Momentum Builds, but Gaps Remain*, survey report, 2025-06-26. https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
- `BOE-2023` — Bank of England PRA, *SS1/23 Model risk management principles for banks*, 2023-05-17 (updated version published 2026-04-23, which keeps the model inventory and independent validation principles). https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- `CIPD-2026` — CIPD with the Institute for the Future of Work, *How a law firm introduced an AI legal assistant*, practitioner case study, 2026-03-25. https://www.cipd.org/ae/knowledge/case-studies/ai-legal-assistant/
- `FRB-2011` — Federal Reserve Board and OCC, *SR 11-7: Supervisory Guidance on Model Risk Management*, 2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `FRC-2025` — UK Financial Reporting Council, *AI in audit: illustrative example and documentation guidance*, regulator guidance, 2025-06-26. https://www.frc.org.uk/documents/8384/AI_in_Audit.pdf
- `GOOGLE-2015` — Sculley et al., *Hidden Technical Debt in Machine Learning Systems*, 2015. https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HUSAIN-2026` — Hamel Husain, *LLM Evals: Everything You Need to Know (FAQ)*, 2026-09-18. https://hamel.dev/blog/posts/evals-faq/
- `LAW360-2025` — Law360 Pulse, *How Law Firms Turn AI Skeptics Into 'Champions'*, 2025-09-26. https://www.law360.com/pulse/articles/2392818
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, 2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
