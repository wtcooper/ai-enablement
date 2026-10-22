# Solution design brief (step 3)

Read this on entering step 3. It turns the sourcing decision into a design brief a builder or configurer can work
from: architecture by runtime class, data and retrieval, permissions, security, and the human checkpoints from
the pattern file. You design; the firm's people build or configure. Keys in brackets are listed in §6. Lines
marked *(advisor default)* are working rules, not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Design elements](#3-design-elements)
4. [Worked example: evidence matching in an audit practice](#4-worked-example-evidence-matching-in-an-audit-practice)
5. [Output](#5-output)
6. [Sources](#6-sources)

## 1. Goal and exit criteria

**Goal.** A one-to-two-page design that says what the solution does and does not do, where a person checks it,
what it may touch, and how it fails safely.

**Exit when all of these are true:**

- **Purpose and non-goals** written.
- **Runtime class and rung** confirmed, with a written rule for the evidence that moves it up a rung and the
  event that moves it down.
- **Architecture sketch:** inputs → retrieval → model calls → tools → outputs → human checkpoint → system of record.
- **Data and retrieval:** source of truth, its owner, how it stays current, access model, data class.
- **Permission table:** every system, read or write, approval needed, and the worst thing it could do.
- **Security and privacy:** a risk screen, data handling, access control, and the risk tier from the governance
  policy (or a request to **ai-governance** for one).
- **Human checkpoints and escalation triggers** from the pattern file, drawn on the flow.
- **Failure behaviour, logging and retention**, a **cost envelope** as a range, and **role evolution** with the
  capacity choice (rule 2).

## 2. How to run it

1. **Open the pattern file** named in `classification.pattern`
   (`../../../transformation-advisor/references/library/patterns/<pattern>.md`) and use it as the checklist: §3 Up
   the ladder, §4 How it is built, §5 Prerequisites, §6 Failure modes and controls, §7 metrics. Every §6 failure
   mode becomes a control here and a failure mode in the step 4 plan.
2. **Write purpose and non-goals** in two or three lines each. Non-goals stop scope creep.
3. **Sketch the flow** by runtime class (§3.1): where the input comes from, where the output lands, who touches it.
4. **Settle data and retrieval** (§3.2), then **fill the permission table** (§3.3) with the user.
5. **Run the security screen** (§3.4) with `overlay/policy.md`. With no policy, ask **ai-governance** for a tier.
6. **Draw the checkpoints** (§3.5): each one on the flow, with the role, what they check and their time per item.
7. **Decide failure behaviour, logging and cost** (§3.6).
8. **Write role evolution:** tasks moving, new work, capacity redeploy or reduce, from the opportunity's
   `role_evolution` and `../../../transformation-advisor/references/method/people-and-change.md`.
9. **Play back** the brief on one screen; write it; name step 4 as next.

For a delegated or agent design, also apply the controls in
`../../../transformation-advisor/references/method/plan-and-control.md` §3.4 and, at the Adopting stage, the five
delegation gates in `../../../transformation-advisor/references/method/onboarding.md` §5.

## 3. Design elements

### 3.1 Architecture by runtime class

| Runtime class | Sketch | Where the checkpoint usually sits |
|---|---|---|
| `personal-assistant` | Person gives input and context → model → person uses or edits the output | The person reviews every output |
| `shared-team-skills` | Shared prompt or skill + approved reference material → model → output in the team's tool | Reviewer sign-off before anything leaves the team |
| `workflow-automation` | Trigger → fixed steps through existing systems, a model at some steps → system of record | Review queue for low-confidence or high-risk items; sampled checks |
| `background-agent` | Schedule or event → agent works through steps → result held for review | At the end, and before anything irreversible |
| `managed-agent-runtime` | Hosted agent with tools, state, permissions and isolation inside business systems | Named checkpoints at key decisions; approval for irreversible actions |

Climb one rung at a time and write down what evidence moves the design up [ANTHROPIC-2024; OPENAI-2025].
Constrained autonomy is the production norm: 68% of surveyed deployed agent systems run at most 10 steps before a
person steps in (UC Berkeley-led academic study, N=60 for that question) [BERKELEY-2026].

### 3.2 Data and retrieval

- **Source of truth and owner first.** GOV.UK Chat chose retrieval over fine-tuning because its content is
  edited regularly; its first retrieval returned whole pages that sometimes exceeded token limits, which led to
  work on chunking, embeddings and re-ranking [UKGDS-2025]. Stale or unowned content needs an owner and a
  refresh route.
- **Access model:** the solution should not widen who sees what. **Sensitivity:** name the data classes from
  `overlay/policy.md`; remove personal data the model does not need, as GOV.UK Chat did [UKGDS-2025].
- **Retrieval quality is evaluated** in step 4, not assumed.

### 3.3 Integration and permissions

| System | Read or write | Approval needed | Worst thing it could do with this permission |
|---|---|---|---|

Start read-only and require approval for write or delete: in LangChain's survey of over 1,300 professionals,
most used read-only permissions or human approval for writes and deletes (vendor-published, self-reported)
[LANGCHAIN-2024]; queries that change data should not run without human approval [HUYEN-2024]. Prefer the
systems professionals already use, so output lands where it is reviewed *(advisor default)*.

### 3.4 Security and privacy screen

- Map layered input and output guardrails to the OWASP LLM risks that apply, for example prompt injection
  (LLM01), improper output handling (LLM05) and excessive agency (LLM06) [OWASP-2025; HUYEN-2024].
- Ask what client or personal data is in scope and what the access model is [UKGDS-2025].
- Copy the risk tier from `overlay/policy.md` into the brief's frontmatter; never invent one. While the policy is
  not `approved`, copy its proposed tier and mark it "provisional" (`../schemas/solution.md` §4).

### 3.5 Human checkpoints and escalation

- **From the pattern file:** its key checkpoint, the rung's "checkpoint before moving up", and its §6 controls.
- **Two escalation triggers:** a failure threshold (retries, failed attempts) and a list of high-risk actions
  that hand over to a person until reliability is shown [OPENAI-2025]. Irreversible actions always pause for a
  person (rule 12).
- **Design the review as editing a suggestion** and keep the edit as feedback [APPLIEDLLMS-2024, 2.3.2;
  YAN-2023].
- **Give the reviewer time.** A checkpoint with no time budget per item becomes a stamp *(advisor default)*; pattern
  files report rubber-stamp review (for example `document-to-decision` §6).
- **Professional work:** the professional stays responsible; the ABA says the right amount of verification
  depends on the tool and the task [ABA-2024].

### 3.6 Failure behaviour, logging and cost

- **When it does not know,** it says so and routes to a person. Design and test that path: models often return
  output when they should not, and prompting for "unknown" is not foolproof [APPLIEDLLMS-2024, 1.4.7]. Name the
  manual fallback; it may be the old process [NIST-2024, GV-6.2-006].
- **Logging:** inputs, outputs, model and prompt version, retrieved sources, reviewer and decision, kept under
  the engagement's confidentiality terms [HUYEN-2024; UKGDS-2024]. Monitor input coverage and freshness too: a
  stale table caused months of gradual decay at Google [GOOGLE-RULES, Rule 10].
- **Cost envelope:** a range per task and per month at expected volume, with assumptions.

## 4. Worked example: evidence matching in an audit practice

Illustrative, continuing step 2 (`configure`, `workflow-automation`, `augment`, `document-to-decision`).

- **Purpose:** propose a match between each sample and client evidence, linking the source text per attribute.
  **Non-goals:** no control conclusion, no client communication, no sample selection.
- **Rung rule:** stays at `augment` until re-performed samples agree within the step 4 threshold; then clean
  categories may move to sampled review. Any later miss moves that category back.
- **Permissions:** read samples and evidence; write proposed matches to a review field only.
- **Checkpoints:** staff confirm or override each item; the senior re-performs a sample; time per item is
  budgeted. **When it does not know:** "no evidence found", with the files searched.
- **Role evolution:** staff move to investigating mismatches and earlier risk work. Capacity: redeploy.

## 5. Output

In `brief.md`, write §3 Solution design from `../templates/brief.md`. In the frontmatter confirm
`classification` (record any change from the advisor option and why in the decisions log), set `risk_tier` if
the policy gives one (provisional while the policy is not `approved`), `step_completed: 3`, `next_step: 4` and
`updated`.

## 6. Sources

- `ABA-2024` — American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools*, professional-body opinion, 2024-07-29. https://www.mcle.org/ePrograms/2250081P01/1--aba-formal-opinion-512.pdf
- `ANTHROPIC-2024` — Anthropic, *Building effective agents*, vendor engineering guide, 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- `APPLIEDLLMS-2024` — Yan et al., *What We've Learned From A Year of Building with LLMs*, practitioner guide, 2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, academic paper, 2026-06-04. https://arxiv.org/pdf/2512.04123
- `GOOGLE-RULES` — Google for Developers, *Rules of Machine Learning*, practitioner guide, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HUYEN-2024` — Chip Huyen, *Building A Generative AI Platform*, practitioner article, 2024-07-25. https://huyenchip.com/2024/07/25/genai-platform.html
- `LANGCHAIN-2024` — LangChain, *State of AI Agents* (2024 survey; the page now carries a 2026 date stamp), vendor survey. https://www.langchain.com/stateofaiagents
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, vendor guide, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `OWASP-2025` — OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*, 2025. https://genai.owasp.org/llm-top-10/
- `UKGDS-2024` — UK Government Digital Service, *Generative AI Framework for HMG*, 2024-01-18 (withdrawn 2025-02-10). https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, 2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
- `YAN-2023` — Eugene Yan, *Patterns for Building LLM-based Systems and Products*, practitioner article, 2023-07. https://eugeneyan.com/writing/llm-patterns/
