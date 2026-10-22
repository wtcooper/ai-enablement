# Schema: overlay/tool-catalog.yaml (tool-catalog/v1)

The approved-tool catalog. Every skill reads it (core rule 6). Version 1 keeps the starter shape (`tools` with
`name`, `runtime_class`, `approved_for`, `owner`, plus `not_approved_note`) and adds optional fields, so an existing
catalog stays valid.

## Contents

1. [Format](#1-format)
2. [Field rules](#2-field-rules)
3. [How other skills read it](#3-how-other-skills-read-it)
4. [Example](#4-example)

## 1. Format

```yaml
schema: tool-catalog/v1
updated: YYYY-MM-DD
owner: role                         # who maintains the catalog
request_path:                       # how to ask for something not listed
  how: string                       # where the request goes
  response_commitment: string       # the stated response time the owner commits to
  fast_lane: string                 # which requests are approved from the catalog's conditions
tools:
  - name: string                    # required: the product as the firm names it
    runtime_class: id               # required: from vocabulary.yaml runtime_classes
    approved_for: string            # required: plain-language summary of what it may be used for
    owner: role                     # required: who owns this entry
    use_for: [ string ]             # jobs staff should use it for, in the words of the tool landscape §2
    id: string                      # stable id, unique in this file, e.g. chat-commercial
    status: id                      # policy.md §3.5; missing means approved (starter catalogs)
    vendor: string
    tool_tier: consumer | commercial | firm-controlled
    contract: string                # the contract or terms this approval rests on
    data_classes: [ id ]            # classes this entry may receive (policy.md §3.2)
    max_risk_tier: tier-1 | tier-2 | tier-3 | tier-4
    user_groups: [ string ]         # roles or groups; "all staff" is allowed
    embedded_in: string | null      # host product, when the AI is a feature inside other software
    underlying_model: string        # model and version where the vendor states it
    processing_regions: [ string ]
    retention: string               # retention setting and who can retrieve history
    conditions: [ string ]          # settings or rules the approval depends on
    flags: { tax_7216: bool, independence: bool, client_consent: bool, eu_high_risk: bool }
    vendor_file: path               # e.g. vendors/<vendor>.md
    reapproval_triggers: [ id ]     # policy.md §3.5
    exit_plan: string
    last_reviewed: YYYY-MM-DD
not_approved_note: string           # required: what to tell people about anything not listed
```

## 2. Field rules

| Step | Fields that must be filled for each entry |
|---|---|
| 2 Acceptable use and data | `name`, `runtime_class`, `approved_for`, `use_for`, `owner`, `tool_tier`, `data_classes` |
| 3 Risk tiers | `max_risk_tier` |
| 6 Vendor and tool evaluation | `id`, `status`, `vendor`, `contract`, `conditions`, `vendor_file`, `reapproval_triggers`, `exit_plan`, `last_reviewed` |
| 7 Secure enablement | top-level `owner` and `request_path` |

- **One entry per tool + tier + contract.** A consumer entry never lists `client-confidential` or `regulated`.
- **Embedded features count:** AI inside licensed software gets its own entry with `embedded_in`, unless the policy
  exempts it.
- **`not-approved` entries stay listed** with the reason and the alternative in `approved_for`.
- **Flags** are `true` when the regime's step applies to the entry; they do not replace the per-workflow decision in
  `policy.md`.
- **Quote free text.** Dates record when something happened (`updated`, `last_reviewed`), never a deadline.

## 3. How other skills read it

- Recommend only entries with `status` `approved` or `approved-with-conditions` (or no `status`), only for their
  `data_classes` and `max_risk_tier`, and mention their `conditions`. `pilot` entries are for their `user_groups` only.
- Treat `under-review`, `not-approved` and `retired` as outside the catalog and flag them. With no fitting entry,
  describe the need by runtime class and point to `request_path`.
- `use_for` answers "which approved tool for this job". `approved_for` says what the tool may be used for and with
  which data. Match a job to `use_for` first, then check `approved_for`, `data_classes` and `max_risk_tier`. The
  jobs and tool types are in `../../../transformation-advisor/references/library/tool-landscape.md` §2.

## 4. Example

```yaml
schema: tool-catalog/v1
updated: 2026-10-20
owner: "IT security lead"
request_path:
  how: "Request form on the intranet AI page; the AI lead triages"
  response_commitment: "Stated in the policy; the owner reports turnaround at each review"
  fast_lane: "Public or firm-internal data, tier-1 or tier-2 use, on an approved entry"
tools:
  - name: "Enterprise chat assistant (business tier)"
    runtime_class: personal-assistant
    approved_for: "Drafting and research; client-confidential data allowed in the firm tenant"
    owner: "IT security lead"
    use_for: ["Draft and edit inside Word, Excel or Docs", "Ask questions of a team's documents", "Analyse a large document set"]
    id: chat-commercial
    status: approved-with-conditions
    vendor: "<vendor>"
    tool_tier: commercial
    contract: "Business terms and data processing addendum on file"
    data_classes: [public, firm-internal, client-confidential]
    max_risk_tier: tier-3
    user_groups: ["all staff after training"]
    embedded_in: null
    underlying_model: "As stated by the vendor; recorded at each review"
    processing_regions: ["US"]
    retention: "Admin-set retention; history retrievable by IT for audit"
    conditions: ["Feedback sharing disabled by the admin", "No tax return information"]
    flags: { tax_7216: false, independence: false, client_consent: false, eu_high_risk: false }
    vendor_file: "vendors/chat-vendor.md"
    reapproval_triggers: [model-change, sub-processor-change, terms-change, new-data-class, new-use, incident]
    exit_plan: "Export workspace history; vendor deletion on termination confirmed in contract"
    last_reviewed: 2026-10-20
  - name: "Enterprise chat assistant (personal accounts)"
    runtime_class: personal-assistant
    approved_for: "Not approved for firm work: consumer terms. Use the business tier"
    owner: "IT security lead"
    id: chat-consumer
    status: not-approved
    tool_tier: consumer
    data_classes: []
not_approved_note: "Anything not listed needs a request through the request path before use with firm or client data."
```

The entries in this example are illustrative.
