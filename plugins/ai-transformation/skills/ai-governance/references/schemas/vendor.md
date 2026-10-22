# Schema: overlay/vendors/<vendor>.md frontmatter (vendor/v1)

One file per vendor product, named by a vendor-product slug. The frontmatter holds the scorecard; the body
(`../templates/vendor.md`) holds the evidence and reasoning. Method: `../vendor-evaluation.md`.

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
evaluation: desk | full | null      # desk = public documentation read; full = contract and vendor answers checked; null = neither yet
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

- **Every rating has a note** saying what the evidence is and where (`sources_checked` locator). A claim with no
  document behind it is `unknown`, not `meets`.
- **`evaluation`** is `desk` only once public documents are read and listed in `sources_checked`; until then it is
  `null`, with `label: draft-to-validate` and ratings `unknown` where only the user's report supports them.
- **`desk` evaluations** keep `label: draft-to-validate`: published terms may differ from the signed contract. For
  `client-confidential` and `regulated` data the decision stays `pending` until someone checks the contract; a narrower
  decision (say, a `pilot` on firm-internal data) may rest on what the user confirms.
- **`pending` in the catalog:** the entry has `status: under-review`, or the narrower status with only its data classes.
- **Decision rules** are in `../vendor-evaluation.md` §5. A `needs-review` screen names its reviewer in the body.
- **No confidential data:** record contract and clause references, not commercial terms or prices. Quote free text.

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
