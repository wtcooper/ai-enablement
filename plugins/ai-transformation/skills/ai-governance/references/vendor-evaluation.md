# Vendor and tool evaluation (step 6)

Read this on entering step 6, and whenever someone asks "can we use tool X with client data". It evaluates one tool
at a time with a repeatable scorecard, decides, and writes the approved-tool catalog entry. Source keys in brackets
are listed in §9. Vendor documents are cited only as evidence of what published terms say; never recommend a vendor.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [Expert moves](#4-expert-moves)
5. [The scorecard and decision rules](#5-the-scorecard-and-decision-rules)
6. [Common traps](#6-common-traps)
7. [Worked example](#7-worked-example)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** A decision on one tool + tier + contract for named data classes and a maximum risk tier, with the evidence
behind it. Vendor evaluation is a data-flow and change-control question first: what is retained and for how long,
whether it trains models, who the sub-processors are and where processing happens, which certifications cover this
product, and what happens when the vendor changes the model, a sub-processor or its terms, or when you leave
[NIST-600-1-2024, GV-6.1-004 to GV-6.1-008; OPENAI-ENT-ND; MSFT-COPILOT-ND].

**Exit when all of these are true:**
- **Scorecard filled:** six dimensions rated `meets`, `partial`, `gap` or `unknown`, each with evidence and a locator.
- **Screens done:** independence, section 7216 or tax-data rules, client terms.
- **Own-sample test** planned or done for tier-3 and tier-4 uses.
- **Decision** with data classes, maximum tier, conditions, re-approval triggers and exit plan.
- **Catalog entry** written or updated, and the vendor file saved.

## 2. How to run it

1. **Pin down the request:** which product, which tier, which contract, which use, which data classes, which runtime
   class. Separate tiers are separate evaluations (move 1).
2. **Offer a desk evaluation** from public documentation: delegate it with `references/briefs/evaluate-tool.md`
   (one subagent per tool), or do it yourself. Label it a draft to validate.
3. **Play the draft back** dimension by dimension. Ask the user what the signed contract and the vendor's answers
   add; change ratings only on evidence.
4. **Run the screens** from `policy.md` §6 (`references/professional-duties.md`).
5. **Plan the own-sample test** for tier-3 and tier-4 uses: real-shaped, non-confidential or approved samples with
   reference answers from the best reviewers (move 6). The firm runs it; you design it and record the result.
6. **Decide** with §5 rules; write conditions as settings someone can check.
7. **Write the vendor file and the catalog entry.** A `not-approved` decision is recorded too, with the alternative.

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| V1 | Which product tier, contract and data processing terms apply to us? | [T/O] |
| V2 | Are inputs and outputs used for training by default; what are the opt-in and feedback exceptions; can an admin disable them? | [T/O] |
| V3 | What is retained, for how long, who can retrieve it, and can we set retention? | [T/O] |
| V4 | Where is data stored and processed, and which sub-processors touch it? | [O] |
| V5 | What notice do we get of model, sub-processor and terms changes, and how do we export our data and leave? | [O] |

More, as needed:
- Which certifications cover this product and scope (for example SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 42001), for which period, with which exclusions? [O]
- What are the warranties, liability limits and incident-notification terms? [O]
- What can we test before approval on our own samples, and what are the known limitations? [U]
- If it is an agent or runtime: what permissions does it hold, and what actions pause for a person? [U/O]

## 4. Expert moves

1. **Record each product tier and contract as a separate catalog entry.** Every evaluation. Reveals different data
   terms for consumer and commercial tiers of one vendor [ANTHROPIC-PRIV-2026; OPENAI-ENT-ND; MSFT-COPILOT-ND].
2. **Read the exceptions to "we don't train on your data".** Retention and training. Reveals opt-in feedback paths:
   one provider says rated feedback conversations can be stored up to 5 years and an organization owner can disable
   the feedback control; another says opted-in shared data may be used for training [ANTHROPIC-PRIV-2026;
   OPENAI-ENT-ND]. Make "feedback disabled" a catalog condition where available.
3. **Ask where inference and storage happen.** Tax, EU or residency constraints. One provider's page says customers
   outside the EU may have queries processed in the US, EU or other regions [MSFT-COPILOT-ND]; under the tax
   regulations, disclosure outside the US needs prior consent [ECFR-7216-2008].
4. **Use NIST's third-party actions as the contract checklist.** Contract review. Reveals missing clauses: content
   ownership and usage rights, quality, security and provenance (GV-6.1-004); a right to evaluate third-party
   processes (GV-6.1-006); an inventory of third parties with access to content and an approved-provider list
   (GV-6.1-007); records of third-party changes (GV-6.1-008) [NIST-600-1-2024].
5. **Ask what notice you get of model, sub-processor and terms changes, and write the re-approval trigger.** Change
   control. Reveals silent drift; NIST asks for model versions in the inventory and records of third-party changes
   [NIST-600-1-2024, GV-1.6-003, GV-6.1-008]. No benchmark of negotiated notice terms was found, so the trigger list
   is an advisor default.
6. **Challenge the model on your own samples before approval and after model changes.** Tier-3 and tier-4 uses.
   Model-risk guidance applies validation to vendor models and expects the firm to choose models appropriate to its
   use even when relying on a vendor [FRB-SR117-2011]. The advisor's evaluation-set guidance is in
   `../../transformation-advisor/references/method/plan-and-control.md` §3.4.
7. **Ask for the exit and failure plan before signing.** Contract and approval. NIST GOVERN 1.7 asks for safe
   decommissioning and GOVERN 6.2 for contingency processes for failures in high-risk third-party data or AI systems
   [NIST-RMF-2023].

## 5. The scorecard and decision rules

| Dimension (id) | What "meets" needs (advisor default) | Evidence to look for |
|---|---|---|
| Security and privacy (`security_privacy`) | Single sign-on and admin controls; activity logging; stated processing regions; security requirements in the contract | Trust or security pages; data processing terms [NIST-600-1-2024, GV-6.1-004] |
| Data retention and training (`retention_training`) | No training on business data by default; feedback exceptions can be disabled; admin-set retention; deletion terms | Business privacy pages, data processing terms [OPENAI-ENT-ND; ANTHROPIC-PRIV-2026] |
| Certifications (`certifications`) | A current report or certificate whose scope names this product, with period and exclusions read | SOC 2 Type 2 report, ISO/IEC 27001 or 42001 certificate and scope statement |
| Contract terms (`contract_terms`) | Ownership and usage rights, quality, security, right to evaluate, incident notice, warranties and liability read | Contract, terms, addenda [NIST-600-1-2024, GV-6.1-004, -006; LAWSOC-GENAI-2026] |
| Sub-processor and model changes (`change_control`) | A published sub-processor list with regions; notice of model, sub-processor and terms changes | Sub-processor page; change-notice clause [NIST-600-1-2024, GV-6.1-008] |
| Exit (`exit`) | Data export; deletion on termination; a contingency if the tool fails or is withdrawn | Terms; admin documentation [NIST-RMF-2023, GOVERN 1.7, 6.2] |

**Gates outside the scorecard:** profession screens (step 5) and, for tier-3 and tier-4 uses, the own-sample test.

**Decision rules (advisor default unless sourced)**
- A `gap` in `retention_training` → not approved for `client-confidential` or `regulated` data.
- Any `unknown` on a dimension that matters for the requested data class → ask the vendor; decision stays `pending`.
- A consumer tier → never approved for `client-confidential` or `regulated` data.
- A screen marked `needs-review` → no approval for that use until the reviewer clears it.
- A tier-3 or tier-4 use with `own_sample_test: not-run` → at most `pilot`, for named user groups.
- A certification whose scope does not name the product → `partial`, not `meets`.
- An embedded feature that arrives switched on → off for client-confidential work until it has a catalog entry
  [NIST-600-1-2024, GV-1.6-001, GV-1.6-002].
- Re-approve on any trigger: model change, sub-processor change, terms change, new data class, new use, incident.

**Runtime-class notes.** For a `managed-agent-runtime`, evaluate the platform (tenancy, logging, data location, change
notice) and each agent's permissions separately. For `background-agent` and `workflow-automation`, add least privilege
and the actions that pause for a person to the conditions [OWASP-LLM-2025].

## 6. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Treating certifications as fitness for your use | Certificates show controls exist; a vendor blog notes ISO/IEC 42001 certification does not by itself satisfy EU AI Act obligations (directional) [OPENLAYER-2026] | Read scope, period and exclusions; still test on your data and use |
| Approving the vendor, not the tier | [ANTHROPIC-PRIV-2026] | One entry per tool + tier + contract |
| Published terms taken as the contract | Published terms may differ from negotiated contracts and change over time | Keep desk evaluations labelled; check the signed contract |
| Questionnaire first, data flow last | The five data-flow facts decide most cases [NIST-600-1-2024] | Start with V2 to V5 |
| Vendor liability assumed | Legal AI vendors are reported to place liability on the deploying firm (professional-services guardrails §8) [INSINSIDER-LAWYERS-2026] | Negotiate warranties and indemnities; tell the insurer |

## 7. Worked example

Illustrative, not a case study. An accounting firm's document-management vendor announces an AI summarisation
feature, on by default.

- **Request:** the feature (`embedded_in` the document platform), commercial tier, for firm-internal and
  client-confidential documents.
- **Desk evaluation (brief):** security `partial` (admin switch per workspace; AI processing region not stated);
  retention and training `unknown` (feedback exception not described); certifications `partial` (platform report
  does not name the feature); contract `unknown`; change control `gap` (no notice commitment found); exit `meets`.
- **Screens:** independence not applicable; client terms `needs-review` for two clients that restrict AI.
- **Decision:** `pending`; feature off for client-confidential workspaces; firm-internal use approved as a `pilot`
  for the knowledge team; questions on region, feedback and notice sent to the vendor.
- **Catalog:** entry `docs-ai-summary` with `status: pilot`, `data_classes: [public, firm-internal]`.

## 8. Output

Write `overlay/vendors/<vendor-product>.md` from `references/templates/vendor.md` (schema
`references/schemas/vendor.md`). Add or update the entry in `overlay/tool-catalog.yaml`. List the evaluation in
section 7 of `overlay/policy.md`. Set `step_completed: 6`, `next_step: 7` the first time; later evaluations update
the files without changing the step.

## 9. Sources

- **ANTHROPIC-PRIV-2026**: Anthropic, *Is my data used for model training? (commercial products)* (vendor documentation, 2026-08-18). https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training
- **ECFR-7216-2008**: US Treasury and IRS, *26 CFR 301.7216-1 to -3* (regulation, T.D. 9375 of 2008 as amended). https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?part=301&section=301.7216-3
- **FRB-SR117-2011**: Federal Reserve and OCC, *SR 11-7 Supervisory Guidance on Model Risk Management* (regulator, 2011-04-04). https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- **INSINSIDER-LAWYERS-2026**: Insurance Insider, *Lawyers test case for professional liability AI risks* (press, partly paywalled, 2026-05-13). https://www.insuranceinsider.com/sample-content/lawyers-test-case-for-professional-liability-ai-risks
- **LAWSOC-GENAI-2026**: Law Society of England and Wales, *Generative AI: the essentials* (professional body, 2026). https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
- **MSFT-COPILOT-ND**: Microsoft, *Microsoft 365 Copilot privacy and data protection* (vendor documentation, undated, read 2026-10-20). https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **NIST-RMF-2023**: NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1* (standard, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **OPENAI-ENT-ND**: OpenAI, *Enterprise privacy* (vendor documentation, undated, read 2026-10-20). https://openai.com/enterprise-privacy/
- **OPENLAYER-2026**: Openlayer, *ISO 42001: A Complete Guide to AI Management Systems* (vendor blog, 2026-06-17). https://www.openlayer.com/blog/iso-42001-ai-management-systems-guide.md
- **OWASP-LLM-2025**: OWASP Gen AI Security Project, *OWASP Top 10 for LLM Applications 2025* (practitioner standard, 2025). https://genai.owasp.org/llm-top-10/
