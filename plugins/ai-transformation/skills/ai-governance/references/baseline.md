# Baseline (step 1)

Read this on entering step 1. It finds out what is really happening before any rule is written: the AI tools in use
(sanctioned and not), the data going into them, the regimes that bind the firm, the policies that exist and who owns
what. Source keys in brackets are listed in §8. Scope tags: **[T]** team, **[U/O]** unit or organization.

## 1. Goal and exit criteria

**Goal.** A picture of current practice the user agrees is true, so the policy closes real gaps, not ideal ones.

**Exit when all of these are true:**
- **Scope and sponsor:** firm, practice or team; the sponsoring role; who will approve the policy.
- **Tools in use:** each tool or feature with its tier, whether it is sanctioned, its use, the data classes going in,
  who pays, and where the information came from (survey, logs, report). Counts and tools only.
- **Regimes flagged** (§5) and **existing policies** listed: acceptable use, data classification, third-party risk,
  privacy impact assessment, incidents, records.
- **Owners mapped** by role: who decides whether a tool is allowed today, and how long it takes.
- **Signals recorded:** the last "no" or "wait" and what followed, policy awareness, incidents, embedded AI, agents.
- **A first gap list:** gap, evidence, consequence, owner, fix type.

## 2. How to run it

1. **Ask about last month's actual tools first** (B1). If the user does not know, suggest an anonymous poll, licence
   and expense records, or IT's network and identity logs.
2. **Ask what happened after the last "no" or "wait"** (B4): it shows whether a ban or a slow approval pushes use out
   of sight.
3. **Flag the regimes** (§5). If an advisor plan is in this folder, read its profile instead of asking again.
4. **List what exists and who owns it**, including informal leaders; in a partnership, practice leaders matter as much
   as IT. Look for an existing process AI questions can join (move 4).
5. **Ask about embedded AI and agents** at unit or organization scope.
6. **Play the baseline back**, agree the gap list, write section 1 of the policy, and name step 2 as next.

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| B1 | Which AI tools did people use last month for client work, including personal accounts, free tools and browser add-ons? | [all] |
| B2 | Which professional rules bind this work: audit or attest, tax-return preparation, legal practice, client contracts that mention AI? | [U/O] |
| B3 | Who decides today whether a new tool is allowed, and how long did the last decision take? | [all] |
| B4 | What happened the last time someone was told "no" or "wait" about a tool? | [all] |
| B5 | Do you have an AI policy, and what share of staff could state its rule on client data? | [U/O] |

## 4. Expert moves

1. **Ask about real tools, including personal and free ones, before drafting.** In a 47-country survey of 48,340
   people led by the University of Melbourne with KPMG, most employees who use AI at work used free public tools, and
   48% said they had uploaded sensitive company information to public AI tools (self-reported)
   [KPMG-MELB-2025, pp.6, 75].
2. **Ask what followed the last "no".** In the same survey such uploads were reported by 67% of employees whose
   employer banned generative AI and 33% of those with no policy; the authors say bans may be ineffective
   (self-reported, correlational) [KPMG-MELB-2025, p.75].
3. **Poll awareness: "Do we have an AI policy, and what does it say about client data?"** Only about two in five
   employees in that survey said their organization had a policy or guidance [KPMG-MELB-2025, p.71].
4. **Join an existing process.** Where a privacy or risk function exists, add AI questions to its privacy impact
   process and let its owner lead; IAPP reports this is a common route [IAPP-GOV-2025].
5. **Inventory AI inside licensed software, with the underlying model.** NIST suggests the policy define any
   exemptions for embedded generative AI and lists model and version as an inventory field [NIST-600-1-2024,
   GV-1.6-002, GV-1.6-003]. Ask whether an unauthorized agent would be detected: 26% of surveyed US senior AI
   executives whose organizations use agentic AI said they could not (self-reported, EY-commissioned) [EY-AIGOV-2026].

## 5. Decision rules

- Prepares tax returns → flag `tax-7216`. Serves attest clients → `attest-independence`. Practises law →
  `legal-practice` [ECFR-7216-2008; JOFA-2026; ABA-OP512-2024].
- Client contracts or outside guidelines mention AI, subcontracting or data location → `client-terms`.
- AI is used in the EU → `eu-deployer`; recruitment, decisions on terms of work, task allocation on behaviour or
  traits, and monitoring or evaluating staff are listed in Annex III [AIACT-EXPL-2026, Annex III point 4].
- Personal data in scope of data-protection law → `privacy-law`.
- A ban with no approved alternative → a first-priority gap (advisor default, built on [KPMG-MELB-2025, p.75]).
- No record of who reviewed AI-assisted client work → a gap [CPAI-2026]. No owner or stated time for B3 → a gap for
  step 7.
- Use the firm's own discovery results as the baseline; survey figures from other organizations are context only.

## 6. Worked example

Illustrative. A mid-sized accounting and advisory firm has a one-page acceptable-use note. A poll and expense records
show three free chat tools, a transcription add-on and a business-tier assistant one practice bought on a card; the
manager who asked IT for it heard nothing. Regimes: `tax-7216`, `attest-independence`, `client-terms`, `privacy-law`.
Nobody owns AI tools. Gaps: no approved tool for client work, no owner for AI decisions, no record of review, embedded
transcription not inventoried. Next: step 2, starting from the data classes the free tools receive.

## 7. Output

Fill the step 1 frontmatter (`title`, `scope`, `archetype`, `regimes`, `owners`) and write section 1 of
`overlay/policy.md` from `references/templates/policy.md` (schema `references/schemas/policy.md`). Set
`step_completed: 1`, `next_step: 2`, `updated`. Tools found stay in the section 1 table; they enter
`overlay/tool-catalog.yaml` only after step 2 or 6 decides on them.

## 8. Sources

- **ABA-OP512-2024**: American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools* (professional body, 2024-07-29). https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
- **AIACT-EXPL-2026**: Future of Life Institute, *EU AI Act Explorer: Annex III* (annotated regulation, accessed 2026-10-20). https://artificialintelligenceact.eu/annex/3/
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **ECFR-7216-2008**: US Treasury and IRS, *26 CFR 301.7216-1 to -3* (regulation, T.D. 9375 of 2008 as amended). https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?part=301&section=301.7216-3
- **EY-AIGOV-2026**: Ernst & Young LLP, *EY survey finds that autonomous AI implementation outpaces oversight* (consultancy survey press release, 2026-09-15). https://www.ey.com/en_us/newsroom/2026/09/ey-survey-finds-that-autonomous-ai-implementation-outpaces-oversight-yielding-an-ai-governance-gap
- **IAPP-GOV-2025**: IAPP, *AI Governance Profession Report 2025* (professional association research, survey spring 2024, page dated 2025-10-30). https://iapp.org/resources/article/ai-governance-profession-report/
- **JOFA-2026**: Journal of Accountancy, *Accounting ethics in the age of AI* (professional body, 2026-08-05). https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai.html
- **KPMG-MELB-2025**: University of Melbourne with KPMG, *Trust, attitudes and use of artificial intelligence: A global study 2025* (academic with consultancy, 2025-05). https://kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
