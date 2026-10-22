# Acceptable use and data rules (step 2)

Read this on entering step 2. It writes the acceptable-use rules and the data rules: a few data classes, and which data
class may go to which tool tier under which contract. Source keys in brackets are listed in §8; vendor pages are
cited only for what published terms say. Ids for data classes and tool tiers are in `references/schemas/policy.md` §3.

## 1. Goal and exit criteria

**Goal.** Rules staff can apply in the moment ("what may I paste where"). The policy is the floor, not the program: it
works only with a catalog of tools people can get, a request path that answers quickly, and training [CPAI-2026].

**Exit when all of these are true:**
- **Definitions, scope and backbone:** what "AI tool", "generative AI" and "agent" mean; who and what is covered.
- **Three to five data classes,** each with one worked example and one redaction example.
- **A data-class by tool-tier matrix** with the conditions for each allowed cell.
- **The rules** (permitted, prohibited, the user's responsibility, client restrictions) and **who approves** tools,
  new uses and exceptions, by role.
- **First catalog entries** for tools the user already relies on, with `tool_tier` and `data_classes`.

## 2. How to run it

1. **Define the terms** and tie them to existing duties and confidentiality agreements [CPAI-2026].
2. **Choose a backbone** the partners or board will accept, and map others to it: NIST AI RMF (GOVERN, MAP, MEASURE,
   MANAGE) [NIST-RMF-2023], ISO/IEC 42001 (certifiable, paywalled) or internal.
3. **Set the data classes.** Offer the four defaults (`public`, `firm-internal`, `client-confidential`, `regulated`);
   the user may rename or split them. Ask for one real-shaped and one redaction example per class (move 1).
4. **Set the tool tiers** and record each tier as its own catalog entry (move 2).
5. **Fill the matrix** cell by cell (§5), with conditions for each allowed cell (settings, region, regime step).
   Lower the data class before raising the tool tier: redact, de-identify or summarize first (advisor default).
6. **Write the rules** in short sentences (§5); leave review to step 3 and records to step 4. **Name who approves**
   tools, new uses and exceptions (move 3).
7. **Play back, write sections 2 and 3, add the first catalog entries, and draft the guardrail data lines.**

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| P1 | What does "approved" mean here: a tool, a tier, a contract, a data class, a user group? | [U/O] |
| P2 | What kinds of information does your work handle, from public material to the most sensitive client data? | [all] |
| P3 | For each kind, where may it go today, and who decided? | [all] |
| P5 | Who may approve a tool, and who may grant an exception? | [U/O] |

## 4. Expert moves

1. **One worked and one redaction example per class**, never real client data. The CPAi guide recommends training with
   examples of what cannot be entered, how to redact, and privacy-respecting alternatives [CPAI-2026].
2. **Ask "which product tier and contract?"** One vendor publishes different terms for consumer and commercial tiers,
   and commercial-tier pages say business inputs are not used for training by default, with exceptions such as opt-in
   feedback [ANTHROPIC-PRIV-2026; OPENAI-ENT-ND; MSFT-COPILOT-ND]. So the unit of approval is tool + tier + contract +
   data class.
3. **Name who approves and who grants exceptions.** In an EY-commissioned survey of 202 senior AI
   executives at large US public companies, 98% reported formal AI governance policies and 47% said governance had
   previously not been applied to urgent deployments (self-reported) [EY-AIGOV-2026].

## 5. Default matrix and decision rules

**Default matrix (advisor default; adjust with the user):**

| Data class | consumer | commercial | firm-controlled |
|---|---|---|---|
| `public` | Allowed | Allowed | Allowed |
| `firm-internal` | Not allowed | Allowed on catalog entries | Allowed |
| `client-confidential` | Not allowed | Allowed on entries approved for it, when client terms permit | Allowed on entries approved for it, when client terms permit |
| `regulated` | Not allowed | Not allowed unless the entry is approved for this class | Allowed on entries approved for this class, after the regime step (`references/professional-duties.md`) |

**Default rules (adjust wording):** use only catalog entries for firm or client work, within their data classes and
risk tiers · you remain responsible for anything you use, send or sign · follow any client instruction that restricts
AI (`../../transformation-advisor/references/archetypes/professional-services/guardrails.md` §6) · if nothing in the
catalog fits, use the request path, never a personal account · report a suspected incident through the incident route.

**Decision rules (advisor defaults):**
- A consumer-tier entry never receives `client-confidential` or `regulated` data.
- An approval names tool, tier, contract and data classes; anything less is not an approval.
- Approve a tool and a request path before restricting; every restriction names the alternative (rule 12). Bans push
  use out of sight (`references/baseline.md` move 2).
- "No training on your data" has exceptions: read them in step 6 and set the admin controls as catalog conditions.

## 6. Worked example

Illustrative. A consulting firm's "no client data in AI" note is ignored because every engagement uses client data.
The new matrix allows client-confidential data in the firm's commercial assistant with feedback sharing disabled and
admin-set retention, and approves no personal account for client work. The rule people remember: "Client data only in
the firm's business-tier assistant; never in a personal account."

## 7. Output

Write sections 2 and 3 of `overlay/policy.md`; set `backbone` and `data_classes` in the frontmatter. Add or update
entries in `overlay/tool-catalog.yaml` (`references/templates/tool-catalog.yaml`; schema
`references/schemas/tool-catalog.md`) with `tool_tier` and `data_classes`; keep existing entries. Draft the data lines
of `overlay/guardrails.md` (`references/templates/guardrails.md`). Set `step_completed: 2`, `next_step: 3`.

## 8. Sources

- **ANTHROPIC-PRIV-2026**: Anthropic, *Is my data used for model training? (commercial products)* (vendor documentation, 2026-08-18). https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **EY-AIGOV-2026**: Ernst & Young LLP, *EY survey finds that autonomous AI implementation outpaces oversight* (consultancy survey press release, 2026-09-15). https://www.ey.com/en_us/newsroom/2026/09/ey-survey-finds-that-autonomous-ai-implementation-outpaces-oversight-yielding-an-ai-governance-gap
- **MSFT-COPILOT-ND**: Microsoft, *Microsoft 365 Copilot privacy and data protection* (vendor documentation, undated, read 2026-10-20). https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- **NIST-RMF-2023**: NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1* (standard, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **OPENAI-ENT-ND**: OpenAI, *Enterprise privacy* (vendor documentation, undated, read 2026-10-20). https://openai.com/enterprise-privacy/
