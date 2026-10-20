# Schema: overlay/vendors/<vendor>.md frontmatter (vendor/v1)

One file per vendor product evaluated, named by a short vendor-product slug. The frontmatter holds the scorecard so
it can be compared across tools; the body (`../templates/vendor.md`) holds the evidence and reasoning. Method:
`../vendor-evaluation.md`.

## Contents

1. [Format](#1-format)
2. [Field rules](#2-field-rules)
3. [Example](#3-example)

## 1. Format

```yaml
schema: vendor/v1
vendor: string
product: string
tool_tier: consumer | commercial | firm-controlled
runtime_class: id                   # vocabulary.yaml runtime_classes
evaluation: desk | full             # desk = public documentation only; full = contract and vendor answers checked
label: draft-to-validate | null     # set for desk evaluations and subagent drafts until the user confirms
evaluated: YYYY-MM-DD
proposed_use: string                # the use and data classes the request is for
data_classes_requested: [ id ]
scorecard:
  security_privacy:   { rating: meets | partial | gap | unknown, note: string }
  retention_training: { rating: id, note: string }
  certifications:     { rating: id, note: string }
  contract_terms:     { rating: id, note: string }
  change_control:     { rating: id, note: string }
  exit:               { rating: id, note: string }
screens:
  independence: clear | needs-review | not-applicable | unknown
  tax_7216: id
  client_terms: id
own_sample_test: not-run | passed | failed | not-applicable
decision: approved | approved-with-conditions | pilot | not-approved | pending
conditions: [ string ]
catalog_id: string | null           # the tool-catalog.yaml entry this evaluation supports
sources_checked:
  - { title: string, url: string, date: string, locator: string }
```

## 2. Field rules

- **Every rating has a note** that says what the evidence is and where it was found (`sources_checked` locator).
  A claim with no document behind it is `unknown`, not `meets`.
- **`desk` evaluations** keep `label: draft-to-validate`. Published terms may differ from the signed contract and
  change over time; for `client-confidential` and `regulated` data the decision stays `pending` until someone checks
  the contract. A narrower decision (for example a `pilot` on firm-internal data) may rest on what the user confirms.
- **`pending` in the catalog.** With no narrower approval, the matching catalog entry has `status: under-review`;
  with one, the entry carries that narrower status and only its data classes.
- **Decision rules** are in `../vendor-evaluation.md` §5. A `gap` in `retention_training` blocks
  `client-confidential` and `regulated` data.
- **Screens** come from the regimes in `policy.md`. A screen marked `needs-review` names who reviews it in the body.
- **No confidential data.** Record contract references and clause numbers, not commercial terms or prices.
- **Quote free text** in double quotes.

## 3. Example

```yaml
schema: vendor/v1
vendor: "<vendor>"
product: "Document platform AI summaries"
tool_tier: commercial
runtime_class: personal-assistant
evaluation: desk
label: draft-to-validate
evaluated: 2026-10-20
proposed_use: "Summarise firm-internal and client-confidential documents inside the document platform"
data_classes_requested: [firm-internal, client-confidential]
scorecard:
  security_privacy: { rating: partial, note: "Admin can switch the feature off per workspace; region not stated for the AI step" }
  retention_training: { rating: unknown, note: "Business terms say no training by default; feedback exception not described" }
  certifications: { rating: partial, note: "Security report covers the platform; scope does not name the AI feature" }
  contract_terms: { rating: unknown, note: "Usage rights and right to evaluate not found in public terms" }
  change_control: { rating: gap, note: "No public notice commitment for model or sub-processor changes" }
  exit: { rating: meets, note: "Export and deletion on termination described in the platform terms" }
screens: { independence: not-applicable, tax_7216: not-applicable, client_terms: needs-review }
own_sample_test: not-run
decision: pending
conditions: ["Feature off for client-confidential workspaces until the contract check is done"]
catalog_id: null
sources_checked:
  - { title: "Platform AI feature terms", url: "<public URL>", date: "2026-10-20", locator: "Data use section" }
```

The ratings in this example are illustrative.
