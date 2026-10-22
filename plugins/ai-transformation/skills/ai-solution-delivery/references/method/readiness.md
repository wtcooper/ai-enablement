# Production readiness (step 5)

Read this on entering step 5. A solution is ready when someone owns it, can see how it behaves, can change it
safely, can switch it off, and the people using it know what to do when it is wrong. You record the review and
the decision; the firm's owners make and sign the decision. Keys in brackets are listed in §6. Lines marked
*(advisor default)* are working rules, not findings from a source.

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

- Every line of the review (§3) is marked ready, gap or not applicable, with its evidence.
- Evaluation results meet the agreed thresholds in `eval-plan.md`, and red-team results were considered.
- A named owner, a rollback path, logging and a first review point exist.
- An adoption plan exists, agreed with **ai-enablement** or written here in outline.
- The inventory entry and risk tier are confirmed with **ai-governance**; independent validation has happened
  where required.
- The benefit metric, baseline, forecast range and counterfactual are ready for the **ai-portfolio** register.
- A staged launch plan (§4.2) and the decision, with each condition's owner and clearing event, are recorded.

## 2. How to run it

1. **Read the inputs:** `brief.md` (owners, design, checkpoints, cost envelope), `eval-plan.md` (thresholds,
   results, monitoring) and `overlay/policy.md` (risk tier, required review, records of AI use).
2. **Go through the review** (§3) one block at a time. Ask for evidence, not intent: "Show me the runbook", not
   "Is there a runbook?" *(advisor default)*.
3. **Settle the people side** (§3.5); hand the full programme design to **ai-enablement**.
4. **Offer an independent challenge** of the pack before the decision (the `review-solution` brief; SKILL.md,
   Delegation). NIST's profile suggests documenting how structured feedback, including red-teaming, fed the
   go/no-go decision [NIST-2024, MS-4.2-005].
5. **Apply the decision rules** (§4.1), write the staged launch plan (§4.2) and record who decided.
6. **Send the gate evidence** (decision, eval results, benefit inputs) to **ai-portfolio** and name step 6 and the
   event that starts it.

If the portfolio runs a pilot with real users first, use the same review at a lighter depth before the pilot
(owner, logging, rollback, every item reviewed, first group trained) and the full review before production
*(advisor default)*.

## 3. The readiness review

### 3.1 Ownership and support

- Named owner and backup by role; support route; who responds out of hours; a runbook (common failures, how to
  pause, who to call); a review rota that includes reading traces [APPLIEDLLMS-2024, 2.1.2].
- An incident process with ownership, rehearsal and post-incident review [NIST-2024, GV-6.2-003, MG-4.2-002]. UK
  guidance asks for named senior responsible owners [UKGDS-2025].

### 3.2 Change control and rollback

- Any model, prompt, retrieval or tool change re-runs the regression suite before release [UKGDS-2025]; models
  and prompts pinned and versioned [APPLIEDLLMS-2024, 2.2.3].
- A managed release that can be withdrawn, and a tested rollback or pause to the manual process [UKGDS-2025;
  NIST-2024, GV-6.2-006]. Building is cheap relative to maintaining ML systems [GOOGLE-2015].

### 3.3 Monitoring and cost

- The online metrics from `eval-plan.md` are live with alert thresholds and responders [FRB-2011; NIST-2024];
  every input and output logged from the first user, then sampled [HUSAIN-2026].
- Input coverage, data freshness and retrieval health watched, not only outputs [GOOGLE-RULES, Rule 10;
  GOOGLE-2021].
- Cost per task and usage visible to the owner [UKGDS-2024; OPENAI-2025]. For the firm's wider AI spend, see
  `professional-services-firm-finance-11` (grade B; practitioners' own accounts of reading consumption bills).
- Logging, retention and access meet client confidentiality terms [UKGDS-2024; ABA-2024].

### 3.4 Evidence and documentation

- Eval results by version meet thresholds; red-team scorecard reviewed.
- **Independent validation** where required: in regulated settings, independent of development [FRB-2011;
  BOE-2023; NIST-2024, MS-1.3-003].
- **Inventory and risk tier:** recorded in the firm's AI or model inventory with owner and tier [FRB-2011;
  BOE-2023] (with **ai-governance**).
- **Documentation pack** for regulated or professional work: what the tool does, when it is appropriate, how it
  was developed and tested, how the firm knows it works, known limits, review level, change history and owners
  [FRC-2025; FRB-2011]. In law, the lawyer stays fully responsible [ABA-2024].
- Security and privacy sign-off; access-control review [UKGDS-2025; OWASP-2025].

### 3.5 People and adoption

- **Training before access** *(advisor default)*: what it does well, its limits, the review expected, what to do
  when it is wrong. The ABA expects supervising lawyers to make sure staff are trained on capabilities and
  limitations [ABA-2024]. A law firm studied by CIPD made training a condition of use and kept a "verify, verify,
  verify" rule (anonymized practitioner case) [CIPD-2026]. In BCG's survey of more than 10,600 leaders, managers
  and frontline employees in 11 countries and regions, regular use was sharply higher with at least five hours of
  training and access to in-person coaching, and only one-third said they had been properly trained
  (self-reported) [BCG-ATWORK-2025].
- **What changes on the first day**, and who people ask; a **feedback loop** from corrections to the eval set.
- **Visible senior use:** senior people use it and share what worked [CIPD-2026]. Licences alone do not create
  use: Law360 reports firms with unused licences (no figure) [LAW360-2025].
- **Role evolution communicated** in the firm's own terms (rule 2).

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

- **Stages by group**, smallest first; write the evidence needed to widen each time.
- **Human review starts at its fullest** and is reduced only on measured evidence, the logic of testing on a
  small reviewed set first [ABA-2024]; OpenAI advises planning human intervention, especially early in
  deployment [OPENAI-2025].
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
- `GOOGLE-2021` — Google Cloud, *Practitioners guide to MLOps*, white paper, 2021-05. https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HUSAIN-2026` — Hamel Husain, *LLM Evals: Everything You Need to Know (FAQ)*, 2026-09-18. https://hamel.dev/blog/posts/evals-faq/
- `LAW360-2025` — Law360 Pulse, *How Law Firms Turn AI Skeptics Into 'Champions'*, 2025-09-26. https://www.law360.com/pulse/articles/2392818
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `OWASP-2025` — OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*, 2025. https://genai.owasp.org/llm-top-10/
- `UKGDS-2024` — UK Government Digital Service, *Generative AI Framework for HMG*, 2024-01-18 (withdrawn 2025-02-10). https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, 2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
