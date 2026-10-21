# Solution design brief (step 3)

Read this on entering step 3. It turns the sourcing decision into a design brief that a builder or configurer
can work from: architecture by runtime class, data and retrieval, integration with the systems professionals
already use, security and access, and the human checkpoints from the pattern file. You design; the firm's
people build or configure. Keys in brackets are listed in §9. Lines marked *(advisor default)* are working rules,
not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Design elements](#3-design-elements)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: evidence matching in an audit practice](#7-worked-example-evidence-matching-in-an-audit-practice)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** A one-to-two-page design that says what the solution does and does not do, where a person checks it,
what it may touch, and how it fails safely.

**Exit when all of these are true:**

- **Purpose and non-goals** written.
- **Runtime class and rung** confirmed, with a written rule for the evidence that moves it up a rung and the
  event that moves it down.
- **Architecture sketch:** inputs → retrieval → model calls → tools → outputs → human checkpoint → system of record.
- **Data and retrieval:** source of truth, its owner, how it stays current, access model, data class.
- **Integration and permission table:** every system, read or write, approval needed, and the worst thing the
  solution could do with that permission.
- **Security and privacy:** a risk screen, data handling, access control, and the risk tier from the governance
  policy (or a request to **ai-governance** for one).
- **Human checkpoints and escalation triggers** taken from the pattern file and drawn on the flow; anything
  irreversible pauses for a person.
- **Failure behaviour:** what it does when it does not know, and the manual fallback.
- **Logging and retention**, a **cost envelope** as a range, and **role evolution** with the capacity choice
  (rule 2).

## 2. How to run it

1. **Open the pattern file** named in `classification.pattern`:
   `../../../transformation-advisor/references/library/patterns/<pattern>.md`. Use it as the design checklist:
   §3 Up the ladder (rung, runtime class, checkpoint before moving up), §4 How it is built (inputs, the AI's
   role, human checkpoint, thresholds, sampling, logging), §5 Prerequisites, §6 Failure modes and controls, §7
   metrics. Every §6 failure mode becomes a control here and a failure mode in the step 4 evaluation plan.
2. **Write purpose and non-goals** in two or three lines each. Non-goals stop scope creep.
3. **Sketch the flow** by runtime class (§3.1). Ask where the input comes from, where the output lands, and who
   touches it in between.
4. **Settle data and retrieval** (§3.2): the source of truth and its owner come before any retrieval method.
5. **Fill the permission table** with the user (§3.3). Start read-only; require approval for write or delete.
6. **Run the security screen** (§3.4) and read `overlay/policy.md` for data classes and the risk tier. With no
   policy, ask **ai-governance** for a tier and the review it requires.
7. **Draw the checkpoints** (§3.5): copy the pattern's key checkpoint, place each one on the flow, name the
   role, what they check and their time per item.
8. **Decide failure behaviour, logging and cost** (§3.6).
9. **Write role evolution:** tasks moving, new work, capacity redeploy or reduce, using the opportunity's
   `role_evolution` and `../../../transformation-advisor/references/method/people-and-change.md`.
10. **Play back** the brief on one screen; write it; name step 4 as next.

For a delegated or agent design, also apply the controls for automated and delegated steps in
`../../../transformation-advisor/references/method/plan-and-control.md` §3.4 (autonomy tiers, escalation,
rubber-stamp watch, tracing, security) and, at the Adopting stage, the five delegation gates in
`../../../transformation-advisor/references/method/onboarding.md` §5.

## 3. Design elements

### 3.1 Architecture by runtime class

| Runtime class | Sketch | Where the checkpoint usually sits |
|---|---|---|
| `personal-assistant` | Person gives input and context → model → person uses or edits the output | The person reviews every output before use |
| `shared-team-skills` | Shared prompt or skill + approved reference material → model → output in the team's tool | Reviewer sign-off before anything leaves the team; shared evaluation cases |
| `workflow-automation` | Trigger → fixed steps through existing systems, with a model at some steps → output to the system of record | Review queue for low-confidence or high-risk items; sampled checks |
| `background-agent` | Schedule or event → agent works through steps → result held for review | Review at the end, and before anything irreversible |
| `managed-agent-runtime` | Hosted agent with tools, state, permissions and isolation inside business systems | Named checkpoints at key decisions; approval for irreversible actions |

Climb one rung at a time and write down what evidence moves the design up; higher rungs cost more latency,
money and testing effort, and errors compound across steps [ANTHROPIC-2024; OPENAI-2025]. Constrained autonomy
is the norm in production: 68% of surveyed deployed agent systems run at most 10 steps before a person steps in
(UC Berkeley-led academic study, N=60 for that question) [BERKELEY-2026].

### 3.2 Data and retrieval

- **Source of truth and owner first.** Who owns the content the solution reads, and how is it kept current?
  GOV.UK Chat chose retrieval over fine-tuning because its content is edited and published regularly; its first
  retrieval returned whole pages that sometimes exceeded token limits, which led to work on chunking, embedding
  models and re-ranking [UKGDS-2025].
- **Access model.** Who may see which content; the solution should not widen it.
- **Sensitivity.** Name the data classes in scope (from `overlay/policy.md`); remove personal data the model
  does not need, as GOV.UK Chat did for pages the model could read [UKGDS-2025].
- **Retrieval quality is evaluated** in step 4, not assumed.

### 3.3 Integration and permissions

| System | Read or write | Approval needed | Worst thing it could do with this permission |
|---|---|---|---|

Start with read-only tools and require approval for write or delete; in LangChain's survey of over 1,300
professionals, very few let agents read, write and delete freely, and most used read-only permissions or human
approval for writes and deletes (vendor-published, self-reported) [LANGCHAIN-2024]. Queries that insert, update or
delete data should not run without human approval [HUYEN-2024]. Prefer integration into systems professionals already use, so the
output lands where the work is reviewed *(advisor default)*.

### 3.4 Security and privacy screen

- Map guardrails to the OWASP LLM risks that apply to this runtime and permission set, for example prompt
  injection (LLM01), improper output handling (LLM05) and excessive agency (LLM06) [OWASP-2025; OPENAI-2025].
- Layer input and output guardrails [HUYEN-2024].
- Ask what client or personal data is in scope and what the access model is [UKGDS-2025; HUYEN-2024].
- Copy the risk tier from `overlay/policy.md` into the brief's frontmatter; never invent one. While the policy is
  not `approved`, copy its proposed tier and mark it "provisional" (`../schemas/solution.md` §4).

### 3.5 Human checkpoints and escalation

- **From the pattern file:** take its key checkpoint and the rung's "checkpoint before moving up"; add the
  controls from its §6 for each failure mode.
- **Two escalation triggers:** a failure threshold (retries, failed attempts) and a list of high-risk actions
  (sensitive, irreversible or high-stakes) that hand over to a person until the system's reliability is shown
  [OPENAI-2025]. In this skill, irreversible actions (send, file, pay, delete) always pause for a person
  (rule 12).
- **Design the review as editing a suggestion,** and capture the edit as feedback; this gives a feedback loop
  [APPLIEDLLMS-2024, 2.3.2, 3.2.5; YAN-2023] and a clear point of accountability *(advisor default)*.
- **Give the reviewer time.** Name the time budget per item; a checkpoint with no time becomes a stamp
  *(advisor default)*.
- **Professional work:** the professional stays responsible for the output; the ABA says the right amount of
  verification depends on the tool and the task [ABA-2024].

### 3.6 Failure behaviour, logging and cost

- **When it does not know,** it should say so and route to a person. Design that path explicitly and test it:
  models often return output even when they should not, and prompting for "unknown" is not foolproof
  [APPLIEDLLMS-2024, 1.4.7]. Name the manual fallback; it may be the old process [NIST-2024, GV-6.2-006].
- **Logging:** inputs, outputs, model and prompt version, retrieved sources, reviewer and decision, kept under
  the engagement's confidentiality terms [HUYEN-2024; UKGDS-2024].
- **Cost envelope:** a range per task and per month at expected volume, with assumptions.

## 4. Question bank

- What is the simplest rung (rule, single call with retrieval, fixed workflow, agent) that could meet the
  quality bar? [T][U/O]
- Which systems does it read from and write to, with what permissions, and what is the worst thing it could do
  with them? [T][U/O]
- Where does a person review or approve, and what triggers an escalation? [T][U/O]
- What is the source of truth for retrieval, how is it kept current, and who owns it? [U/O]
- What client or personal data is in scope, and what is the access model? [U/O]
- What happens when it does not know? Does it say so? [T]
- Which runtime class fits, and why not the one below it? [U/O]
- Who reviews, what do they check, and how much time do they have per item? [T]

## 5. Expert moves

1. **Climb the autonomy ladder one rung at a time and write down what evidence moves you up** [ANTHROPIC-2024;
   OPENAI-2025]. Reveals whether extra complexity buys measured improvement.
2. **Draw the human checkpoints on the flow**: failure thresholds and high-risk actions. Reveals where a wrong
   output becomes an irreversible action [OPENAI-2025; HUYEN-2024].
3. **Design the review as editing a suggestion, and keep the edit** [APPLIEDLLMS-2024; YAN-2023]. Reveals a
   built-in feedback loop and who is accountable.
4. **Layer guardrails mapped to the OWASP LLM risks** at the security review [OWASP-2025; OPENAI-2025;
   HUYEN-2024]. Reveals which risks are real for this integration.
5. **Start with read-only permissions; require approval for write or delete** [LANGCHAIN-2024]. Reveals the
   blast radius.

## 6. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Too much autonomy too early | Autonomy costs more and errors compound [ANTHROPIC-2024]; constrained autonomy is the production norm [BERKELEY-2026] | Climb the ladder with written promotion rules |
| Checkpoints with no time or skill behind them | Pattern files report rubber-stamp review (for example `document-to-decision` §6 and `draft-review-loop` §2) | Time budget per item; override rate tracked from day one |
| Stale or unowned retrieval content | Content that changes needs an owner in the loop [UKGDS-2025] | Name the content owner and refresh route |
| Silent failures from upstream changes | A stale table caused months of gradual decay at Google [GOOGLE-RULES, Rule 10] | Monitor input coverage and freshness, not only outputs |
| Write access granted for convenience | [HUYEN-2024; OWASP-2025, LLM06] | Read-only first; approval for writes |

## 7. Worked example: evidence matching in an audit practice

Illustrative, continuing step 2 (`configure`, `workflow-automation`, `augment`, pattern `document-to-decision`).

- **Purpose:** propose a match between each selected sample and client-provided evidence, with a link to the
  source text for each test attribute. **Non-goals:** no conclusion on the control; no client communication; no
  sample selection.
- **Flow:** samples and client evidence already in the audit platform → feature extracts attribute values with a
  pointer to the page → proposes match or mismatch per attribute → staff member reviews every match and works
  every mismatch → senior reviews the test.
- **Rung rule:** stays at `augment` until re-performed samples agree within the step 4 threshold across the first
  engagements; then the owner may move clean categories to sampled review (`automate`). Any miss found later moves
  that category back.
- **Data:** client evidence as received; the attribute checklist (owner: methodology team) is the criteria
  source and is versioned.
- **Permissions:** read samples and evidence; write proposed matches to a review field only; never write test
  conclusions.
- **Security:** client documents may contain embedded text instructions; outputs are treated as proposals,
  never executed. The governance policy places attest evidence in `tier-4`.
- **Checkpoints (from `document-to-decision`):** staff confirm or override each item; the senior re-performs a
  sample of accepted matches; time per item is budgeted in the engagement plan.
- **When it does not know:** marks the attribute "no evidence found" with the files searched; staff match by hand.
- **Role evolution:** vouching moves to the tool; staff investigate mismatches and do earlier risk work; juniors
  explain back a sample of matches to keep learning. Capacity: redeploy.

## 8. Output

In `brief.md`, write §3 Solution design from `../templates/brief.md`. In the frontmatter confirm
`classification` (record any change from the advisor option and why in the decisions log), set `risk_tier` if
the policy gives one (provisional while the policy is not `approved`), `step_completed: 3`, `next_step: 4` and
`updated`.

## 9. Sources

- `ABA-2024` — American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools*,
  professional-body opinion, 2024-07-29. https://www.mcle.org/ePrograms/2250081P01/1--aba-formal-opinion-512.pdf
- `ANTHROPIC-2024` — Anthropic, *Building effective agents*, vendor engineering guide, 2024-12-19.
  https://www.anthropic.com/engineering/building-effective-agents
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, practitioner guide,
  2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, academic paper, 2026-06-04.
  https://arxiv.org/pdf/2512.04123
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, practitioner guide, page last updated 2025-08-25.
  https://developers.google.com/machine-learning/guides/rules-of-ml
- `HUYEN-2024` — Chip Huyen, *Building A Generative AI Platform*, practitioner article, 2024-07-25.
  https://huyenchip.com/2024/07/25/genai-platform.html
- `LANGCHAIN-2024` — LangChain, *State of AI Agents* (2024 survey; the page now carries a 2026 date stamp), vendor
  survey. https://www.langchain.com/stateofaiagents
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, vendor guide, 2025-04.
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `OWASP-2025` — OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*, 2025.
  https://genai.owasp.org/llm-top-10/
- `UKGDS-2024` — UK Government Digital Service, *Generative AI Framework for HMG*, 2024-01-18 (withdrawn 2025-02-10).
  https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, 2025-02-10.
  https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
- `YAN-2023` — Eugene Yan, *Patterns for Building LLM-based Systems and Products*, practitioner article, 2023-07.
  https://eugeneyan.com/writing/llm-patterns/
