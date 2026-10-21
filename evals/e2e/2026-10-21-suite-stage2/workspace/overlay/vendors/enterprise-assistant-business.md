---
schema: vendor/v1
vendor: "Not recorded (the firm's enterprise assistant; vendor name to be added by the IT/security lead)"
product: "Firm enterprise assistant, business tier"
tool_tier: commercial
runtime_class: personal-assistant
evaluation: desk
label: draft-to-validate
evaluated: "2026-10-21"
proposed_use: "Drafting, research and templates on public and firm-internal material only. Client data not permitted."
data_classes_requested: [public, firm-internal]
scorecard:
  security_privacy: { rating: unknown, note: "Nothing checked yet. Only the portfolio lead's statement that the tool is approved on enterprise terms with a data processing addendum." }
  retention_training: { rating: unknown, note: "Reported by the portfolio lead: no training on the firm's inputs. Not yet checked against the signed contract, and the feedback and opt-in exceptions have not been read." }
  certifications: { rating: unknown, note: "Not checked." }
  contract_terms: { rating: unknown, note: "Data processing addendum reported to exist. Clause text not yet seen." }
  change_control: { rating: unknown, note: "Notice of model, sub-processor and terms changes not checked." }
  exit: { rating: unknown, note: "Export and deletion on termination not checked." }
screens: { independence: not-applicable, tax_7216: not-applicable, client_terms: not-applicable }
own_sample_test: not-applicable
decision: pending
conditions: []
catalog_id: enterprise-assistant-business
sources_checked: []
---

# Vendor evaluation: firm enterprise assistant · business tier

**Request:** Portfolio lead (head of AI office), for the discovery-stage item `ct-int-nonclient-drafting`: public and firm-internal material only, runtime class `personal-assistant`. Client data is not permitted.
**Evaluation type:** contract check, not started · **Evaluated by:** delivery lead's draft from reported facts only · **Draft to validate:** yes

## Status

No evaluation evidence exists yet. Every rating is `unknown`. The portfolio lead will supply the signed contract's no-training and data-processing terms, with no client details. Ratings change only on that evidence (rule: change ratings only on evidence). Record clause references, not prices or confidential terms.

## Scorecard

| Dimension | Rating | Evidence (document, locator, date) | Open question for the vendor |
|---|---|---|---|
| Security and privacy | unknown | None yet | Single sign-on and admin controls; activity logging; processing regions stated in the contract? |
| Data retention and training | unknown | Reported only: no training on inputs | Does the no-training term cover inputs and outputs? What are the feedback or opt-in exceptions, and can the admin disable them? What is retained, for how long, and who can retrieve it? Can the firm set retention? |
| Certifications (product and scope) | unknown | None yet | Which report or certificate names this product and tier, for which period, with which exclusions? |
| Contract terms | unknown | Addendum reported to exist | Ownership and usage rights; right to evaluate; incident notice; warranties and liability limits; where data is stored and processed; sub-processor list. |
| Sub-processor and model changes | unknown | None yet | What notice does the firm get of model, sub-processor and terms changes? Is the model version stated? |
| Exit | unknown | None yet | Data export; deletion on termination; contingency if the tool fails or is withdrawn. |

## What to bring (no client details)

Short excerpts or clause references, with the contract section number, for:
1. **No-training term:** the sentence covering inputs and outputs, and any exception (feedback, opt-in sharing, human review for abuse monitoring).
2. **Data-processing addendum:** purpose limits, retention and deletion, processing regions, sub-processor list and the notice period for changes, breach-notification duty.
3. **Change notice:** how model and terms changes are communicated.
4. **Exit:** export and deletion on termination.
5. **Admin settings:** whether feedback sharing and retention are set at the firm level, and who holds them.
6. **Certifications:** which report names the product, and its period.

## Screens

| Screen | Result | Reasoning | Who reviews |
|---|---|---|---|
| Independence | not-applicable | The use is internal and shares nothing with an attest client; the tool is not built, hosted or shared with a client | Risk lead to confirm |
| Section 7216 or tax-data rules | not-applicable | No tax return information is permitted in the tool for this use | Risk lead to confirm |
| Client terms | not-applicable | No client data goes in, so client engagement-letter restrictions are not engaged | Risk lead to confirm |

## Test on our own samples

Not applicable to this evaluation: the requested use is at most tier-2, where an own-sample test is not required. The item's own-sample test of output quality is separate and is planned in `solutions/ct-int-nonclient-drafting/brief.md`.

## Decision

**Decision:** pending
**Data classes and maximum tier:** public and firm-internal; `tier-2` (proposed, unconfirmed by the risk lead).
**Conditions:** to be written as checkable settings once the contract is read. Current draft conditions are in the catalog entry.
**Re-approval triggers:** model change, sub-processor change, terms change, new data class, new use, incident.
**Exit plan:** to be written from the exit clause.
**Catalog entry:** `enterprise-assistant-business` (`under-review`).

## Sources checked

| Title | URL | Date | Locator |
|---|---|---|---|
| None yet | | | |
