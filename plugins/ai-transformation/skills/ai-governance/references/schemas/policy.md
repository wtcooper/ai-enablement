# Schema: overlay/policy.md frontmatter (policy/v1)

The governance skill keeps its state in the frontmatter of `overlay/policy.md`, so a session can stop after any
step and resume. The body follows `../templates/policy.md`. This file also defines the controlled values the
governance files share (§3); other skills read them from here.

## Contents

1. [Format](#1-format)
2. [Field rules](#2-field-rules)
3. [Controlled values for governance files](#3-controlled-values-for-governance-files)
4. [Example](#4-example)

## 1. Format

```yaml
schema: policy/v1
title: string                      # "AI policy: <firm, practice or team>"
scope: { level: firm | practice | team, name: string }
archetype: id | null               # from the advisor's archetypes index, e.g. tax, assurance
regimes: [ id ]                    # §3.1
owners:                            # roles, never named people
  policy: role
  tool_catalog: role
  request_path: role
  exceptions: role
  incidents: role
backbone: nist-ai-rmf | iso-42001 | internal | null
data_classes: [ id ]               # §3.2; the classes this policy uses
risk_tiers: [ id ]                 # §3.4; the tiers this policy uses
policy_version: integer            # raise by one each time the approved text changes
status: draft | in-review | approved
step_completed: 0-7                # 0 = nothing saved yet
next_step: 1-7 | null              # null when all seven steps are done
updated: YYYY-MM-DD
parent: path | null                # a practice or team policy names the firm policy it adds to
```

## 2. Field rules

| Step | Fields that must be filled |
|---|---|
| 1 Baseline | `title`, `scope`, `archetype`, `regimes`, `owners` (at least `policy`), `step_completed`, `next_step`, `updated` |
| 2 Acceptable use and data | `backbone`, `data_classes` |
| 3 Risk tiers | `risk_tiers` |
| 7 Secure enablement | every `owners` field; `status` moves to `in-review` when the text goes to the approvers |

- **Roles, not people.** Owners are roles ("Head of risk", "IT security lead"), never names (rule 1).
- **Stricter, never looser.** A policy with a `parent` may add classes, tiers or rules; it may not relax the parent.
- **Status is the firm's, not yours.** Set `approved` only when the user tells you the approvers signed it off.
- **Quote free text** in double quotes; an unquoted colon breaks the file.
- **No calendar deadlines.** Review timing lives in the body as a cadence and triggers, never as a plan date.

## 3. Controlled values for governance files

These ids are used by `policy.md`, `tool-catalog.yaml` and `vendors/<vendor>.md`. They are proposed for the shared
`../../../transformation-advisor/references/schemas/vocabulary.yaml`; until then this section is their source.

### 3.1 Regimes (`regimes`)

| Id | Meaning |
|---|---|
| `tax-7216` | Preparing US tax returns: section 7216 use, disclosure and consent rules apply |
| `attest-independence` | Serving audit or attest clients: independence rules apply to AI services and vendor ties |
| `legal-practice` | Practising law: bar rules on confidentiality, consent, supervision and fees apply |
| `client-terms` | Client contracts or outside guidelines restrict AI use, subcontracting or data location |
| `eu-deployer` | Using AI in the EU: AI Act deployer duties, including literacy and any high-risk uses |
| `privacy-law` | Personal data in scope of data-protection law |

### 3.2 Data classes (`data_classes`)

| Id | Meaning |
|---|---|
| `public` | Published or freely available information |
| `firm-internal` | The firm's own non-public information that names no client |
| `client-confidential` | Any information about or from a client, including engagement and matter data |
| `regulated` | Client information with a specific legal regime on top: tax return information, privileged material, special-category personal data |

A firm may split or rename classes in its policy body; keep these ids in the YAML so other skills can read them.

### 3.3 Tool tiers (`tool_tier`)

| Id | Meaning |
|---|---|
| `consumer` | Personal or free accounts on consumer terms |
| `commercial` | A business product tier under a firm contract, with admin controls and published business-data terms |
| `firm-controlled` | A commercial tier where the firm has also confirmed or negotiated retention, region, logging and change notice |

### 3.4 Risk tiers (`risk_tiers`, `max_risk_tier`)

| Id | Name | Typical uses |
|---|---|---|
| `tier-1` | Internal, low consequence | Admin, internal drafts, brainstorming |
| `tier-2` | Informs professional work | Research and analysis a professional then checks and uses |
| `tier-3` | Client-facing or relied on | Deliverables, advice, anything that leaves the firm |
| `tier-4` | Regulated or high-impact | Attest procedures and evidence, filings, court submissions, decisions about people, agents acting on client data |

The review each tier needs is in `../risk-tiers.md`.

### 3.5 Catalog status, scorecard ratings and screens

- `status` (catalog entry): `approved`, `approved-with-conditions`, `pilot`, `under-review`, `not-approved`, `retired`.
- `rating` (scorecard dimension): `meets`, `partial`, `gap`, `unknown`.
- Scorecard dimensions: `security_privacy`, `retention_training`, `certifications`, `contract_terms`,
  `change_control`, `exit`.
- Screens (`independence`, `tax_7216`, `client_terms`): `clear`, `needs-review`, `not-applicable`, `unknown`.
- `own_sample_test`: `not-run`, `passed`, `failed`, `not-applicable`.
- Re-approval triggers: `model-change`, `sub-processor-change`, `terms-change`, `new-data-class`, `new-use`,
  `incident`.

## 4. Example

```yaml
schema: policy/v1
title: "AI policy: tax and advisory practice"
scope: { level: practice, name: "Tax and advisory" }
archetype: tax
regimes: [tax-7216, client-terms, privacy-law]
owners:
  policy: "Practice risk partner"
  tool_catalog: "IT security lead"
  request_path: "IT security lead"
  exceptions: "Firm general counsel"
  incidents: "Practice risk partner"
backbone: nist-ai-rmf
data_classes: [public, firm-internal, client-confidential, regulated]
risk_tiers: [tier-1, tier-2, tier-3, tier-4]
policy_version: 1
status: draft
step_completed: 3
next_step: 4
updated: 2026-10-20
parent: "../firm-policy/overlay/policy.md"
```

The values in this example are illustrative.
