# Vendor and tool evaluation (step 6)

Read this on entering step 6, and whenever someone asks "can we use tool X with client data". It evaluates one tool
at a time with a repeatable scorecard, decides, and writes the catalog entry. Sources are in §8; vendor documents are
cited only as evidence of what published terms say. Never recommend a vendor.

## 1. Goal and exit criteria

**Goal.** A decision on one tool + tier + contract for named data classes and a maximum risk tier, with evidence. It
is a data-flow and change-control question first: retention, training, sub-processors and regions, certifications,
and what happens when the vendor changes the model or terms, or you leave [NIST-600-1-2024, GV-6.1-004 to GV-6.1-009].

**Exit when all of these are true:**
- **Scorecard filled:** six dimensions rated `meets`, `partial`, `gap` or `unknown`, each with evidence and a locator.
- **Screens done** (independence, 7216 or tax-data rules, client terms); **own-sample test** planned or done for
  tier-3 and tier-4 uses.
- **Decision** with data classes, maximum tier, conditions, re-approval triggers and exit plan; catalog entry and
  vendor file saved.

## 2. How to run it

1. **Pin down the request:** product, tier, contract, use, data classes, runtime class. Each tier is its own evaluation.
2. **Offer a desk evaluation** from public documents, delegated with `references/briefs/evaluate-tool.md` or done
   yourself; it is a draft to validate (rule 15). Play it back dimension by dimension, starting with V2 to V5, and
   change ratings only on evidence from the signed contract or the vendor's answers.
3. **Run the screens** from policy section 6. For tier-3 and tier-4 uses, design the own-sample test
   (`references/risk-tiers.md` move 3) on non-confidential or approved samples with reference answers; the firm runs it.
4. **Decide** with §5; write conditions as checkable settings. Record a `not-approved` decision with its alternative.

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| V1 | Which product tier, contract and data processing terms apply to us? | [T/O] |
| V2 | Are inputs and outputs used for training by default; what are the opt-in and feedback exceptions; can an admin disable them? | [T/O] |
| V3 | What is retained, for how long, who can retrieve it, and can we set retention? | [T/O] |
| V4 | Where is data stored and processed, and which sub-processors touch it? | [O] |
| V5 | What notice do we get of model, sub-processor and terms changes, and how do we export our data and leave? | [O] |

## 4. Expert moves

1. **Read the exceptions to "we don't train on your data".** One provider says rated feedback conversations can be
   stored up to 5 years and an organization owner can disable the feedback control; another says opted-in shared data
   may be used for training [ANTHROPIC-PRIV-2026; OPENAI-ENT-ND]. Make "feedback disabled" a catalog condition.
2. **Ask where inference and storage happen.** One provider's page says customers outside the EU may have queries
   processed in the US, EU or other regions [MSFT-COPILOT-ND]; under the tax regulations, disclosure outside the US
   needs prior consent [ECFR-7216-2008].
3. **Ask what notice you get of model, sub-processor and terms changes, and write the re-approval trigger.** NIST asks
   for ongoing monitoring of third parties, including detecting unauthorized changes [NIST-600-1-2024, GV-6.1-009].
   No benchmark of negotiated notice terms was found, so the trigger list is an advisor default.

## 5. The scorecard and decision rules

| Dimension (id) | What "meets" needs (advisor default) | Evidence to look for |
|---|---|---|
| Security and privacy (`security_privacy`) | Single sign-on and admin controls; activity logging; stated processing regions; security terms in the contract | Trust or security pages; data processing terms [NIST-600-1-2024, GV-6.1-004] |
| Data retention and training (`retention_training`) | No training on business data by default; feedback exceptions can be disabled; admin-set retention; deletion terms | Business privacy pages, data processing terms [OPENAI-ENT-ND; ANTHROPIC-PRIV-2026] |
| Certifications (`certifications`) | A current report or certificate whose scope names this product, with period and exclusions read | SOC 2 Type 2 report, ISO/IEC 27001 or 42001 certificate and scope statement |
| Contract terms (`contract_terms`) | Ownership and usage rights, quality, security, right to evaluate, incident notice, warranties and liability read | Contract, terms, addenda [NIST-600-1-2024, GV-6.1-004, -006] |
| Sub-processor and model changes (`change_control`) | A published sub-processor list with regions; notice of model, sub-processor and terms changes | Sub-processor page; change-notice clause [NIST-600-1-2024, GV-6.1-005, GV-6.1-009] |
| Exit (`exit`) | Data export; deletion on termination; a contingency if the tool fails or is withdrawn | Terms; admin documentation [NIST-RMF-2023, GOVERN 1.7, 6.2] |

**Decision rules (advisor defaults)**
- A `gap` in `retention_training`, or a consumer tier → never approved for `client-confidential` or `regulated` data.
- Any `unknown` on a dimension that matters for the requested data class → ask the vendor; decision stays `pending`.
- A screen marked `needs-review` → no approval for that use until the reviewer clears it. Any re-approval trigger
  (`references/schemas/policy.md` §3.5) → evaluate again.
- A tier-3 or tier-4 use with `own_sample_test: not-run` → at most `pilot`, for named user groups.
- A certification whose scope does not name the product → `partial`, not `meets`.
- An embedded feature that arrives switched on → off for client-confidential work until it has a catalog entry (NIST
  asks that inventories and procurement cover embedded generative AI [NIST-600-1-2024, GV-1.6-002, GV-6.1-009]).
- Agents and runtimes add least privilege and the actions that pause for a person to the conditions
  (`references/risk-tiers.md` move 4); for a `managed-agent-runtime`, evaluate the platform and each agent separately.

## 6. Worked example

Illustrative; the vendor schema example records it. A document platform switches on AI summaries with region, feedback
and change notice unknown: client-confidential use stays `pending` with the feature off; firm-internal use is a `pilot`.

## 7. Output

Write `overlay/vendors/<vendor-product>.md` from `references/templates/vendor.md` (schema `references/schemas/vendor.md`),
the entry in `overlay/tool-catalog.yaml`, and the evaluation in policy section 7. Set `step_completed: 6`,
`next_step: 7` the first time; later evaluations update the files without changing the step.

- **`evaluation`** is `desk` only once public documents are read and listed in `sources_checked`, `full` once the
  signed contract and vendor answers are checked, else `null`; ratings resting only on the user's report stay `unknown`.
- **Write only the template's sections.** Document requests go in the chat, vendor questions in the scorecard.
- **Evaluated by** is a firm role, or "draft (ai-governance)" or "draft (subagent)" until a role confirms it.
- **Request from a solution brief:** hand the vendor file path, catalog entry id and the use's tier back to
  **ai-solution-delivery**, whatever the decision (`SKILL.md`, Handoffs).

## 8. Sources

- **ANTHROPIC-PRIV-2026**: Anthropic, *Is my data used for model training? (commercial products)* (vendor documentation, 2026-08-18). https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training
- **ECFR-7216-2008**: US Treasury and IRS, *26 CFR 301.7216-1 to -3* (regulation, T.D. 9375 of 2008 as amended). https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?part=301&section=301.7216-3
- **MSFT-COPILOT-ND**: Microsoft, *Microsoft 365 Copilot privacy and data protection* (vendor documentation, undated, read 2026-10-20). https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **NIST-RMF-2023**: NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1* (standard, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **OPENAI-ENT-ND**: OpenAI, *Enterprise privacy* (vendor documentation, undated, read 2026-10-20). https://openai.com/enterprise-privacy/
