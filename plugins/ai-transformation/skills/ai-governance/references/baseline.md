# Baseline (step 1)

Read this on entering step 1. It finds out what is really happening before any rule is written: the AI tools in use
(sanctioned and not), the data that goes into them, the professional regimes that bind the firm, the policies that
already exist and who owns what. Source keys in brackets are listed in §9. Tags: **[T]** team, **[U/O]** unit or
organization.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [Expert moves](#4-expert-moves)
5. [Checklists and decision rules](#5-checklists-and-decision-rules)
6. [Common traps](#6-common-traps)
7. [Worked example](#7-worked-example)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** A picture of current practice the user agrees is true, so the policy closes real gaps instead of
describing an ideal. Governance work is mostly known duties applied to a new tool: the AICPA ethics article and ABA
Opinion 512 say existing duties continue and the professional stays responsible for the output, and firms told PCAOB
staff the same [JOFA-2026; ABA-OP512-2024; PCAOB-GENAI-2024].

**Exit when all of these are true:**
- **Scope and sponsor:** firm, practice or team; the sponsoring role; who will approve the policy.
- **Tools in use:** each tool or feature with its tier, whether it is sanctioned, what it is used for, which data
  classes go in, who pays, and where the information came from (survey, logs, report). Counts and tools only.
- **Regimes flagged:** tax-return preparation, attest clients, legal practice, client contract terms, EU use,
  personal data (§5 decision rules).
- **Existing policies and processes** listed: acceptable use, data classification, third-party risk, privacy
  impact assessment, incident handling, records.
- **Owners mapped** by role: who decides whether a tool is allowed today, and how long it takes.
- **Signals recorded:** the last "no" or "wait" and what followed, policy awareness, incidents or near misses,
  embedded AI, agents.
- **A first gap list:** gap, evidence, consequence, owner, fix type.

## 2. How to run it

1. **Remind the user once** not to share client-confidential data or names (core rule 5). You need tools, data
   classes, counts and roles, never who did what (core rule 1).
2. **Ask the discovery question first** (§4, move 1). If the user does not know, suggest how they could find out:
   an anonymous poll, licence and expense records, network or identity logs held by IT.
3. **Ask what happened the last time someone was told "no" or "wait"** (move 2). It shows whether a ban or a slow
   approval is pushing use out of sight.
4. **Flag the regimes** with the decision rules in §5. If the advisor has a plan in this folder, read its profile
   (archetype, constraints) instead of asking again.
5. **List what already exists** and who owns it. Look for an existing process AI questions can join (move 5).
6. **Map the owners**, including informal ones (move 6). In a partnership, practice leaders matter as much as IT.
7. **Ask about embedded AI and agents** (moves 4 and 7) at unit or organization scope.
8. **Play the baseline back**, agree the gap list, write section 1 of `overlay/policy.md`, and name step 2 as next.

## 3. Question bank

Core questions first, one at a time, in this wording.

| # | Question | Scope |
|---|---|---|
| B1 | Which AI tools did people use last month for client work, including personal accounts, free tools and browser add-ons? | [all] |
| B2 | Which professional rules bind this work: audit or attest, tax-return preparation, legal practice, client contracts that mention AI? | [U/O] |
| B3 | Who decides today whether a new tool is allowed, and how long did the last decision take? | [all] |
| B4 | What happened the last time someone was told "no" or "wait" about a tool? | [all] |
| B5 | Do you have an AI policy, and what share of staff could state its rule on client data? | [U/O] |

More, as needed:
- What do your largest client contracts and outside guidelines say about AI, subcontractors and data location? [U/O]
- Which existing owners (privacy, security, risk, ethics, general counsel, quality, independence) already cover part of this? [U/O]
- Where is AI already built into software you license? [U/O]
- Which incidents or near misses with AI have you logged, and who looked at them? [U/O]
- Could you tell if someone set up an agent that acts on firm systems without approval? [U/O]
- What evidence could you show today that review happened on the last five AI-assisted deliverables? [T]

## 4. Expert moves

Format: **move**: when to use it; what it reveals; source.

1. **Ask about last month's actual tools, including personal accounts and free tools, before drafting anything.**
   Opening the step. Reveals the real data flows and the gap between policy and practice. In a 47-country survey of
   48,340 people led by the University of Melbourne with KPMG, most employees who use AI at work used free public
   tools, and 48% said they had uploaded sensitive company information to public AI tools (self-reported)
   [KPMG-MELB-2025, pp.6, 75]. In Microsoft and LinkedIn's survey of 31,000 knowledge workers in 31 markets, 78% of
   AI users said they bring their own AI tools to work (vendor-published) [MSFT-WTI-2024].
2. **Ask what happened after the last "no" or "wait".** Policy diagnosis. Reveals whether restriction drives use out
   of sight. In the same survey, such uploads were reported by 67% of employees whose employer banned generative AI
   and 33% of those with no policy; the authors say this suggests bans may be ineffective (self-reported, correlational)
   [KPMG-MELB-2025, p.75].
3. **Run a one-question awareness poll: "Do we have an AI policy, and what does it say about client data?"** Before
   and after launch. Reveals the awareness gap: only about two in five employees in the survey said their
   organization had a policy or guidance, and almost one in five did not know [KPMG-MELB-2025, p.71].
4. **Build the inventory to include AI inside existing software, with the underlying model.** Unit or organization
   scope. Reveals AI that arrives inside licensed products; NIST suggests the policy define any inventory exemptions
   for embedded generative AI and lists the underlying model and version as an inventory field [NIST-600-1-2024,
   GV-1.6-002, GV-1.6-003].
5. **Add AI questions to the privacy impact process you already run, and let its owner lead.** When a privacy or risk
   function exists. Reveals the cheapest route to an AI assessment: IAPP reports AI questions are commonly added to
   existing privacy documentation where governance grows out of the privacy program, and in its spring-2024 survey of
   more than 670 people in 45 countries, privacy and legal and compliance were each named the primary owner of AI
   governance by 22% of respondents (self-reported) [IAPP-GOV-2025].
6. **Map the informal leaders, not only the org chart.** In a partnership. Reveals who can move peers and who can
   quietly block; Empson's study, as reviewed, describes a "leadership constellation" of the senior pair, practice
   heads, business-services heads and key influencers [JOTWELL-EMPSON-2013].
7. **Ask whether you could detect an unauthorized agent.** Where agents or automations are in use. Reveals a
   visibility gap: 26% of surveyed US senior AI executives whose organizations use agentic AI said they could not
   (self-reported, EY-commissioned) [EY-AIGOV-2026].

## 5. Checklists and decision rules

**Baseline checklist:** regimes · existing owners · existing policies · tools in use (survey or discovery) · embedded
AI · agents and automations · client contract terms · incidents and near misses · policy awareness · current approval
path and time.

**Decision rules**
- The unit prepares tax returns → flag `tax-7216` from the start. It serves attest clients → flag
  `attest-independence`. It practises law → flag `legal-practice` (consent and fees) [ECFR-7216-2008; JOFA-2026;
  ABA-OP512-2024].
- Client contracts or outside guidelines mention AI, subcontracting or data location → flag `client-terms`.
- AI is used in the EU → flag `eu-deployer`; recruitment, decisions on terms of work, task allocation based on
  behaviour or personal traits, and monitoring or evaluating staff are listed in Annex III
  [AIACT-EXPL-2026, Annex III point 4].
- A ban with no approved alternative → a first-priority gap (advisor default, built on [KPMG-MELB-2025, p.75]).
- No record of who reviewed AI-assisted client work → a gap [CPAI-2026].
- The answer to B3 has no owner or no stated time → a gap for step 7.

## 6. Common traps

| Trap | Why it happens | How to avoid |
|---|---|---|
| Quoting another organization's survey figure as this firm's baseline | Survey numbers are vivid | Use the firm's own discovery results; survey figures are context only |
| Asking who used what | Discovery feels like an investigation | Ask about tools, counts and data classes; never record names (core rule 1) |
| Starting from a policy template | It feels faster | Baseline first: a policy that ignores current tools is bypassed |
| Missing embedded features and agents | They arrive inside approved software | Ask B-questions on licensed software and agents [NIST-600-1-2024, GV-1.6-002; EY-AIGOV-2026] |
| Treating IT as the only owner | AI looks like a technology question | Map privacy, risk, quality, independence and practice leaders too [IAPP-GOV-2025] |

## 7. Worked example

Illustrative, not a case study. A mid-sized accounting and advisory firm with audit, tax and advisory practices has a
one-page acceptable-use note. Its managing partner asks for "a proper AI policy".

- **Discovery (B1):** an anonymous poll and the expense records show three free chat tools, a transcription add-on
  and a business-tier assistant that one practice bought on a card. Meeting notes and client emails are going into
  free tools.
- **Last "no" (B4):** a manager asked IT for the business-tier assistant and heard nothing; the team bought it.
- **Regimes (B2):** tax returns (`tax-7216`), attest clients (`attest-independence`), client terms in two large
  contracts (`client-terms`), personal data (`privacy-law`).
- **Owners (B3):** IT security approves software; the risk partner owns engagement acceptance; nobody owns AI
  tools; the last decision took months.
- **Gap list:** no approved tool for client work; no owner for AI decisions; no record of review on AI-assisted
  deliverables; embedded transcription not inventoried.
- **Next:** step 2, starting from the data classes the free tools are receiving.

## 8. Output

Fill the frontmatter fields for step 1 (`title`, `scope`, `archetype`, `regimes`, `owners`) and write section 1 of
`overlay/policy.md` from `references/templates/policy.md`. Set `step_completed: 1`, `next_step: 2`, `updated`. Schema:
`references/schemas/policy.md`. Tools found in use stay in the section 1 table; they enter `overlay/tool-catalog.yaml` only after
step 2 or 6 decides on them.

## 9. Sources

- **ABA-OP512-2024**: American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools* (professional body, 2024-07-29). https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
- **AIACT-EXPL-2026**: Future of Life Institute, *EU AI Act Explorer: Annex III* (annotated regulation, accessed 2026-10-20). https://artificialintelligenceact.eu/annex/3/
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **ECFR-7216-2008**: US Treasury and IRS, *26 CFR 301.7216-1 to -3* (regulation, T.D. 9375 of 2008 as amended). https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?part=301&section=301.7216-3
- **EY-AIGOV-2026**: Ernst & Young LLP, *EY survey finds that autonomous AI implementation outpaces oversight* (consultancy survey press release, 2026-09-15). https://www.ey.com/en_us/newsroom/2026/09/ey-survey-finds-that-autonomous-ai-implementation-outpaces-oversight-yielding-an-ai-governance-gap
- **IAPP-GOV-2025**: IAPP, *AI Governance Profession Report 2025* (professional association research, survey spring 2024, page dated 2025-10-30). https://iapp.org/resources/article/ai-governance-profession-report/
- **JOFA-2026**: Journal of Accountancy, *Accounting ethics in the age of AI* (professional body, 2026-08-05). https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai.html
- **JOTWELL-EMPSON-2013**: John Flood, JOTWELL, *How Are Professional Service Firms Governed?* (review of Empson, 2013-09-24). https://legalpro.jotwell.com/?p=653
- **KPMG-MELB-2025**: University of Melbourne with KPMG, *Trust, attitudes and use of artificial intelligence: A global study 2025* (academic with consultancy, 2025-05). https://kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf
- **MSFT-WTI-2024**: Microsoft and LinkedIn, *AI at Work Is Here. Now Comes the Hard Part* (vendor research; survey fielded by Edelman Data & Intelligence, February-March 2024). https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **PCAOB-GENAI-2024**: PCAOB staff, *Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting* (regulator staff, 2024-07). https://pcaobus.org/documents/generative-ai-spotlight.pdf
