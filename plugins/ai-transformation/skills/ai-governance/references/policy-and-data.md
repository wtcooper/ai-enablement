# Acceptable use and data rules (step 2)

Read this on entering step 2. It writes the acceptable-use rules and the data rules: a few data classes, and which
data class may go to which tool tier under which contract. Source keys in brackets are listed in §9. Ids for data
classes and tool tiers are in `references/schemas/policy.md` §3.

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

**Goal.** Rules staff can apply in the moment ("what may I paste where"), because for knowledge work a central exposure
is confidential client information entering a tool; the CPAi guide calls data security "vital" for CPA firms and asks
firms to restrict confidential inputs where a tool is not protected [CPAI-2026]. The acceptable-use policy is the floor, not the
program: it works only with a catalog of tools people can actually get, a request path that answers quickly, and
training [CPAI-2026; KPMG-MELB-2025, p.75].

**Exit when all of these are true:**
- **Definitions and scope:** what "AI tool", "generative AI" and "agent" mean here; which people, runtime classes and
  embedded features are covered.
- **Framework backbone** chosen (or "internal"), with any mapping aid.
- **Three to five data classes,** each with one worked example and one redaction example.
- **A data-class by tool-tier matrix** with the conditions for each allowed cell.
- **The rules:** permitted use, prohibited use, the user's responsibility, client restrictions.
- **Who approves** tools, new uses and exceptions, by role.
- **First catalog entries** for tools the user already relies on, with `tool_tier` and `data_classes`.

## 2. How to run it

1. **Define the terms and tie them to existing duties.** Start the policy with what is governed and why, linking use
   to professional obligations and confidentiality agreements [CPAI-2026].
2. **Choose a backbone.** Frameworks are vocabularies, not rulebooks. NIST AI RMF organizes the work into GOVERN, MAP,
   MEASURE and MANAGE [NIST-RMF-2023]; ISO/IEC 42001 is a certifiable management-system standard whose text is
   paywalled; the CSA AI Controls Matrix maps 243 control objectives in 18 domains to ISO/IEC 42001, ISO/IEC 27001 and
   NIST AI RMF [CSA-AICM-2025]. Pick the one the partners or board will accept and map the others to it.
3. **Set the data classes.** Offer the four defaults (`public`, `firm-internal`, `client-confidential`, `regulated`)
   and let the user rename or split them. Ask for one real-shaped example per class (no real client data) and one
   redaction example (move 1).
4. **Set the tool tiers.** The same vendor publishes different terms for consumer and commercial tiers, and the
   commercial-tier pages say business inputs are not used for training by default, with stated exceptions such as
   opt-in feedback [ANTHROPIC-PRIV-2026; OPENAI-ENT-ND; MSFT-COPILOT-ND]. The unit of approval is therefore tool +
   tier + contract + data class.
5. **Fill the matrix** cell by cell (§5 default). For each allowed cell, write the conditions (settings, region,
   regime step).
6. **Write the rules** in short sentences (§5 rule set). Keep the review standard for step 3 and records for step 4;
   here, say only that the user stays responsible.
7. **Name who approves** tools, new uses and exceptions. Unowned exceptions are the main bypass route (move 4).
8. **Play back, write sections 2 and 3 of the policy, add the first catalog entries, and draft guardrail lines.**

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| P1 | What does "approved" mean here: a tool, a tier, a contract, a data class, a user group? | [U/O] |
| P2 | What kinds of information does your work handle, from public material to the most sensitive client data? | [all] |
| P3 | For each kind, where may it go today, and who decided? | [all] |
| P4 | Which decisions or deliverables must never rely on unreviewed AI output? | [T/U] |
| P5 | Who may approve a tool, and who may grant an exception? | [U/O] |

More, as needed:
- Which standard will the partners or board accept as the backbone: NIST AI RMF, ISO/IEC 42001, or your own? [O]
- Can a lower data class do the same job: a redacted, de-identified or summarized input? [T]
- Which controls can be set in the tool (single sign-on, logging, retention, data-loss prevention) rather than left to memory? [U/O]
- Do any clients forbid AI, require disclosure, or limit where data is processed? [U/O]

## 4. Expert moves

1. **Define each data class with one worked example and a redaction example.** Drafting. Reveals whether staff can
   classify in practice; the CPAi guide recommends training with examples of what cannot be entered, how to redact,
   and alternatives that respect privacy requirements [CPAI-2026].
2. **For each tool ask "which product tier and contract?" and record each as a separate catalog entry.** Drafting
   the matrix. Reveals that one vendor's consumer and commercial tiers carry different data terms; one provider's
   commercial page separates its consumer plans from its commercial products [ANTHROPIC-PRIV-2026; OPENAI-ENT-ND;
   MSFT-COPILOT-ND].
3. **Lower the data class before raising the tool tier.** When a use needs client data. Reveals cheaper routes:
   redact, de-identify or summarize first so a lower tier suffices (advisor default).
4. **Write who approves and who grants exceptions into the policy.** Always. Reveals the bypass route: in an
   EY-commissioned survey of 202 senior AI executives at large US public companies, 98% reported formal AI governance
   policies and 47% said their organization had previously not applied its governance process to urgent deployments
   (self-reported) [EY-AIGOV-2026].
5. **Treat the policy as a data-handling rule first.** Short policies. Reveals the one rule people must remember:
   what may go into which tool (advisor default, built on the CPAi guide's data-security section [CPAI-2026]).

## 5. Checklists and decision rules

**Policy skeleton (for the whole policy):** purpose and definitions; scope; data classes and tool-tier matrix;
approved-tool catalog and request path; risk tiers and review; records of AI use; client disclosure and consent;
training and acknowledgement; incidents; exceptions; maintenance and review [CPAI-2026; NIST-RMF-2023].

**Default matrix (advisor default; adjust with the user):**

| Data class | consumer | commercial | firm-controlled |
|---|---|---|---|
| `public` | Allowed | Allowed | Allowed |
| `firm-internal` | Not allowed | Allowed on catalog entries | Allowed |
| `client-confidential` | Not allowed | Allowed on entries approved for it, when client terms permit | Allowed on entries approved for it, when client terms permit |
| `regulated` | Not allowed | Not allowed unless the entry is approved for this class | Allowed on entries approved for this class, after the regime step (`references/professional-duties.md`) |

**Default rule set (adjust wording to the firm):**
- Use only catalog entries for firm or client work, within their data classes and risk tiers.
- You remain responsible for anything you use, send or sign, whatever tool helped.
- Follow any client instruction that restricts AI (the professional-services guardrails record this duty for
  lawyers and consultants: `../../transformation-advisor/references/archetypes/professional-services/guardrails.md` §6).
- If the catalog has nothing that fits, use the request path; do not use a personal account.
- Report a suspected data or output incident through the incident route.

**Decision rules**
- A consumer-tier entry never receives `client-confidential` or `regulated` data (advisor default).
- An approval names tool, tier, contract and data classes; anything less is not an approval (advisor default, built on
  the tier differences in [ANTHROPIC-PRIV-2026; OPENAI-ENT-ND]).
- The policy names the role that approves tools and the role that grants exceptions (advisor default, built on
  [CPAI-2026; EY-AIGOV-2026]).
- Every restriction names the approved alternative or the request path (advisor default, built on
  [KPMG-MELB-2025, p.75]).

## 6. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Ban-first policy | In the University of Melbourne and KPMG survey of employees in 47 countries, uploads of company information to public tools were reported by 67% where generative AI was banned versus 33% with no policy (self-reported, correlational) [KPMG-MELB-2025, p.75] | Approve a tool and a request path first; then restrict |
| Approving the vendor, not the tier | Published terms differ by consumer and commercial tier [ANTHROPIC-PRIV-2026] | Catalog entry = tool + tier + contract + data class |
| Policy nobody knows | In the same survey, about two in five employees said a policy or guidance existed; 56% had used AI at work without knowing whether it was allowed (self-reported) [KPMG-MELB-2025, pp.71, 75] | Role-based training with examples and acknowledgement; hand to ai-enablement |
| "No training on your data" taken at face value | Commercial pages state exceptions such as opt-in feedback [ANTHROPIC-PRIV-2026; OPENAI-ENT-ND] | Read the exceptions in step 6; set the admin controls as catalog conditions |
| Classes nobody can apply | Definitions without examples | One worked example and one redaction example per class [CPAI-2026] |

## 7. Worked example

Illustrative, not a case study. A consulting and advisory firm's acceptable-use note says "no client data in AI".
Staff ignore it because every engagement involves client data.

- **Classes (P2):** `public`; `firm-internal` (methods, proposals with client names removed); `client-confidential`
  (interview notes, client financials); `regulated` (personal data from client HR projects).
- **Tiers (P1, P3):** the firm holds a commercial-tier assistant under a business contract; staff also hold personal
  accounts.
- **Matrix:** client-confidential data allowed in the commercial entry with feedback sharing disabled and retention
  set by the admin; personal accounts not approved for any client work; regulated personal data only after a privacy
  review names a firm-controlled entry.
- **Approvals (P5):** the AI lead approves tools; the general counsel grants exceptions, logged centrally.
- **Rule people remember:** "Client data only in the firm's business-tier assistant; never in a personal account."

## 8. Output

Write sections 2 and 3 of `overlay/policy.md`; set `backbone` and `data_classes` in the frontmatter. Add or update
entries in `overlay/tool-catalog.yaml` (`references/templates/tool-catalog.yaml`; schema
`references/schemas/tool-catalog.md`) with `tool_tier` and `data_classes`; keep existing entries. Draft the data
lines of `overlay/guardrails.md` (`references/templates/guardrails.md`). Set `step_completed: 2`, `next_step: 3`.

## 9. Sources

- **ANTHROPIC-PRIV-2026**: Anthropic, *Is my data used for model training? (commercial products)* (vendor documentation, 2026-08-18). https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **CSA-AICM-2025**: Cloud Security Alliance, *AI Controls Matrix (AICM) v1* (industry body, 2025-07-09). https://cloudsecurityalliance.org/artifacts/ai-controls-matrix
- **EY-AIGOV-2026**: Ernst & Young LLP, *EY survey finds that autonomous AI implementation outpaces oversight* (consultancy survey press release, 2026-09-15). https://www.ey.com/en_us/newsroom/2026/09/ey-survey-finds-that-autonomous-ai-implementation-outpaces-oversight-yielding-an-ai-governance-gap
- **KPMG-MELB-2025**: University of Melbourne with KPMG, *Trust, attitudes and use of artificial intelligence: A global study 2025* (academic with consultancy, 2025-05). https://kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf
- **MSFT-COPILOT-ND**: Microsoft, *Microsoft 365 Copilot privacy and data protection* (vendor documentation, undated, read 2026-10-20). https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- **NIST-RMF-2023**: NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1* (standard, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **OPENAI-ENT-ND**: OpenAI, *Enterprise privacy* (vendor documentation, undated, read 2026-10-20). https://openai.com/enterprise-privacy/

Vendor documentation is cited only as evidence of what published terms say; nothing here recommends a vendor.
